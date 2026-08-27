import os, json, math, hashlib, datetime, warnings
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from scipy.stats import spearmanr
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from lightgbm import LGBMRegressor
import joblib

warnings.filterwarnings('ignore')
BASE='/mnt/data'; OUT=os.path.join(BASE,'DigitalTwin_V1'); os.makedirs(OUT,exist_ok=True)
SEED=20260821
TARGETS={
'TAWSS_vector_Pa':'log1p','OSI':'identity','RRT_1_per_Pa':'log1p','peak_WSS_magnitude_Pa':'log1p',
'VM_cycle_max_Pa':'log','VM_stress_amplitude_Pa':'log','VM_temporal_mean_Pa':'log'}
CANDIDATES={
'LGB_smooth':dict(n_estimators=180,learning_rate=0.04,num_leaves=15,min_child_samples=100,subsample=0.9,colsample_bytree=0.9,reg_lambda=1.0,random_state=SEED,n_jobs=-1,verbosity=-1),
'LGB_mid':dict(n_estimators=220,learning_rate=0.04,num_leaves=31,min_child_samples=50,subsample=0.9,colsample_bytree=0.9,reg_lambda=1.0,random_state=SEED,n_jobs=-1,verbosity=-1),
'LGB_local':dict(n_estimators=250,learning_rate=0.035,num_leaves=45,min_child_samples=25,subsample=0.9,colsample_bytree=0.85,reg_lambda=2.0,random_state=SEED,n_jobs=-1,verbosity=-1),
}

def sha256(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for c in iter(lambda:f.read(1<<20),b''): h.update(c)
 return h.hexdigest()

def load_patient(p):
 hf=f'{BASE}/Patient{p}_VectorResolved_Hemodynamics.csv'
 sf=f'{BASE}/Patient{p}_CycleResolved_SolidMechanics.csv' if p<4 else f'{BASE}/Patient4_CycleResolved_SolidMechanics_v2.csv'
 h=pd.read_csv(hf); s=pd.read_csv(sf)
 def xyz(df):
  a=df.iloc[:,:3].to_numpy(float)
  if df.columns[0].endswith('_m') and not df.columns[0].endswith('_mm'): a*=1000.0
  return a
 x=xyz(h); xs=xyz(s)
 if x.shape!=xs.shape or not np.allclose(x,xs,rtol=0,atol=1e-10): raise RuntimeError(f'P{p} coordinate mismatch')
 d=pd.DataFrame(x,columns=['x_mm','y_mm','z_mm'])
 for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']: d[c]=h[c].to_numpy(float)
 for c in ['VM_cycle_max_Pa','VM_stress_amplitude_Pa','VM_temporal_mean_Pa']: d[c]=s[c].to_numpy(float)
 d['patient']=p
 return d,hf,sf

def geom_features(X,n_bins=24):
 X=np.asarray(X,float); cen=X.mean(0); Xc=X-cen
 _,_,Vt=np.linalg.svd(Xc,full_matrices=False); main=Vt[0]; s0=Xc@main
 edges=np.quantile(s0,np.linspace(0,1,n_bins+1)); bi=np.searchsorted(edges[1:-1],s0,side='right')
 C=[]; spos=[]
 for b in range(n_bins):
  m=bi==b
  if m.sum()<5: m=(s0>=edges[b])&(s0<=edges[b+1])
  C.append(X[m].mean(0)); spos.append(np.median(s0[m]))
 C=np.array(C)[np.argsort(spos)]
 Cs=np.column_stack([savgol_filter(C[:,k],7,2,mode='interp') for k in range(3)])
 def derive(CS):
  d=np.gradient(CS,axis=0); T=d/np.linalg.norm(d,axis=1,keepdims=True)
  arc=np.r_[0,np.cumsum(np.linalg.norm(np.diff(CS,axis=0),axis=1))]; L=arc[-1]; sn=arc/L
  idx=np.argmin(((X[:,None,:]-CS[None,:,:])**2).sum(2),1)
  v=X-CS[idx]; rv=v-(v*T[idx]).sum(1)[:,None]*T[idx]; rr=np.linalg.norm(rv,axis=1)
  R=np.zeros(n_bins)
  for b in range(n_bins):
   vals=rr[idx==b]
   if len(vals)<8: vals=rr[np.abs(idx-b)<=1]
   R[b]=np.percentile(vals,90)
  return T,arc,L,sn,idx,rv,rr,R
 T,arc,L,sn,idx,rv,rr,R=derive(Cs)
 if np.median(R[-3:])>np.median(R[:3]): Cs=Cs[::-1].copy(); T,arc,L,sn,idx,rv,rr,R=derive(Cs)
 kv=np.column_stack([np.gradient(T[:,k],arc,edge_order=1) for k in range(3)]); km=np.linalg.norm(kv,axis=1); ku=kv/np.where(km[:,None]>1e-12,km[:,None],1)
 dR=np.gradient(R,arc,edge_order=1); rp=R[idx]; ss=sn[idx]; ru=rv/np.where(rr[:,None]>1e-12,rr[:,None],1)
 side=(ru*ku[idx]).sum(1); align=np.abs((T[idx]*main).sum(1)); Rend=np.median(R[:3]); Rend2=np.median(R[-3:]); Rmed=np.median(R); Rmax=R.max(); Rmean=R.mean()
 tort=L/max(np.linalg.norm(Cs[-1]-Cs[0]),1e-9); bbox=np.sort(np.ptp(X,axis=0))[::-1]
 f=pd.DataFrame({
 's_norm':ss,'dist_nearest_end':np.minimum(ss,1-ss),'radial_norm':rr/np.maximum(rp,1e-9),
 'local_radius_over_length':rp/L,'local_radius_over_median':rp/Rmed,'local_radius_over_large_end':rp/Rend,
 'local_radius_gradient':dR[idx],'curvature_1_per_mm':km[idx],'curvature_radius':km[idx]*rp,'curvature_side':side,
 'tangent_alignment_main_axis':align,'centerline_length_mm':L,'mean_radius_over_length':Rmean/L,'max_radius_over_length':Rmax/L,
 'global_expansion_ratio':Rmax/Rend,'end_radius_ratio':Rend2/Rend,'tortuosity':tort,
 'mean_curvature_times_length':km.mean()*L,'max_curvature_times_length':km.max()*L,'bbox_ratio_2_1':bbox[1]/bbox[0],'bbox_ratio_3_1':bbox[2]/bbox[0]})
 meta={'centerline_length_mm':float(L),'large_end_radius_proxy_mm':float(Rend),'small_end_radius_proxy_mm':float(Rend2),'max_radius_proxy_mm':float(Rmax),'tortuosity':float(tort)}
 return f,meta

def tf(y,k):
 y=np.asarray(y,float)
 if k=='identity': return y
 if k=='log1p': return np.log1p(np.maximum(y,0))
 return np.log(np.maximum(y,1e-12))
def inv(z,k):
 if k=='identity': return z
 if k=='log1p': return np.expm1(z)
 return np.exp(z)
def met(y,p):
 mae=mean_absolute_error(y,p); rmse=mean_squared_error(y,p)**0.5; rho=float(spearmanr(y,p).statistic)
 k=max(1,int(round(.1*len(y)))); A=set(np.argpartition(y,-k)[-k:].tolist()); B=set(np.argpartition(p,-k)[-k:].tolist())
 return {'R2':float(r2_score(y,p)),'MAE':float(mae),'RMSE':float(rmse),'Spearman':rho,'Top10_overlap':len(A&B)/k}

frames={}; meta={}; hashes={}
for p in [1,2,3,4]:
 d,hf,sf=load_patient(p); g,m=geom_features(d[['x_mm','y_mm','z_mm']].values)
 g.insert(0,'z_mm',d.z_mm); g.insert(0,'y_mm',d.y_mm); g.insert(0,'x_mm',d.x_mm); g['patient']=p
 for t in TARGETS: g[t]=d[t].values
 frames[p]=g; meta[p]=m; hashes[f'P{p}_hemo']=sha256(hf); hashes[f'P{p}_solid']=sha256(sf)
train=pd.concat([frames[p] for p in [1,2,3]],ignore_index=True)
features=[c for c in frames[1].columns if c not in ['x_mm','y_mm','z_mm','patient',*TARGETS.keys()]]

cv=[]; best={}; best_oof={}; q90={}
for target,trans in TARGETS.items():
 candidate_summary=[]; cand_oof={}
 for name,par in CANDIDATES.items():
  folds=[]; preds=[]
  for vp in [1,2,3]:
   tr=train.patient!=vp; va=~tr; pats=train.loc[tr,'patient'].to_numpy(); cnt={p:(pats==p).sum() for p in np.unique(pats)}; w=np.array([1/cnt[p] for p in pats]); w*=len(w)/w.sum()
   mdl=LGBMRegressor(**par); mdl.fit(train.loc[tr,features],tf(train.loc[tr,target],trans),sample_weight=w)
   pr=inv(mdl.predict(train.loc[va,features]),trans); y=train.loc[va,target].to_numpy(float); mm=met(y,pr); mm['NMAE']=mm['MAE']/(np.quantile(y,.75)-np.quantile(y,.25)+1e-12)
   row={'target':target,'candidate':name,'val_patient':vp,**mm}; cv.append(row); folds.append(row)
   z=train.loc[va,['patient','x_mm','y_mm','z_mm']].copy(); z['truth']=y; z['prediction']=pr; preds.append(z)
  candidate_summary.append((np.mean([x['NMAE'] for x in folds]),-np.mean([x['Spearman'] for x in folds]),name)); cand_oof[name]=pd.concat(preds,ignore_index=True)
 candidate_summary.sort(); name=candidate_summary[0][2]; best[target]=name; best_oof[target]=cand_oof[name]
 rr=np.abs(tf(best_oof[target].truth.to_numpy(),trans)-tf(best_oof[target].prediction.to_numpy(),trans)); pp=best_oof[target].patient.to_numpy(); q90[target]=max(float(np.quantile(rr[pp==p],.90)) for p in [1,2,3])
cvdf=pd.DataFrame(cv); cvdf.to_csv(f'{OUT}/LOPO_CV_AllCandidates.csv',index=False)
sel=[]
for t,name in best.items():
 q=cvdf[(cvdf.target==t)&(cvdf.candidate==name)]; sel.append({'target':t,'selected_model':name,'mean_R2':q.R2.mean(),'mean_MAE':q.MAE.mean(),'mean_Spearman':q.Spearman.mean(),'mean_Top10_overlap':q.Top10_overlap.mean(),'mean_NMAE':q.NMAE.mean()})
seldf=pd.DataFrame(sel); seldf.to_csv(f'{OUT}/LOPO_SelectedModels.csv',index=False)


master=None
for t,z in best_oof.items():
 z=z.rename(columns={'truth':f'{t}_truth','prediction':f'{t}_pred'}); key=['patient','x_mm','y_mm','z_mm']; master=z if master is None else master.merge(z,on=key)
master.to_csv(f'{OUT}/LOPO_OOF_Predictions.csv',index=False)


freeze={'project':'Aortic FSI Surrogate Digital Twin V1','training_patients':[1,2,3],'locked_test_patient':4,'freeze_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'feature_policy':'geometry-only, patient-normalized PCA/centerline/radius/curvature features; P4 targets excluded from model selection','features':features,'target_transforms':TARGETS,'candidates':CANDIDATES,'selected_models':best,'q90_development_residual_transformed':q90,'source_sha256':hashes,'geometry_metadata':{str(k):v for k,v in meta.items()},'seed':SEED}
fp=f'{OUT}/FREEZE_MANIFEST_PRE_P4.json'; json.dump(freeze,open(fp,'w'),indent=2); fh=sha256(fp); open(f'{OUT}/FREEZE_MANIFEST_SHA256.txt','w').write(fh+'  FREEZE_MANIFEST_PRE_P4.json\n')


p4=frames[4]; predout=p4[['x_mm','y_mm','z_mm']].copy(); models={}
for t,trans in TARGETS.items():
 par=dict(CANDIDATES[best[t]]); par['n_estimators']=450
 pats=train.patient.to_numpy(); cnt={p:(pats==p).sum() for p in np.unique(pats)}; w=np.array([1/cnt[p] for p in pats]); w*=len(w)/w.sum()
 mdl=LGBMRegressor(**par); mdl.fit(train[features],tf(train[t],trans),sample_weight=w); models[t]=mdl
 z=mdl.predict(p4[features]); predout[f'{t}_pred']=inv(z,trans); predout[f'{t}_lo90']=inv(z-q90[t],trans); predout[f'{t}_hi90']=inv(z+q90[t],trans)
joblib.dump({'models':models,'features':features,'targets':TARGETS,'selected':best,'freeze_hash':fh},f'{OUT}/DigitalTwin_V1_Models.joblib',compress=3)


test=[]
for t in TARGETS:
 y=p4[t].to_numpy(float); pr=predout[f'{t}_pred'].to_numpy(float); mm=met(y,pr); lo=predout[f'{t}_lo90']; hi=predout[f'{t}_hi90']; mm['Interval90_coverage']=float(np.mean((y>=lo)&(y<=hi))); mm['target']=t; test.append(mm)
testdf=pd.DataFrame(test); testdf.to_csv(f'{OUT}/P4_LOCKED_TEST_METRICS.csv',index=False); predout.to_csv(f'{OUT}/P4_DigitalTwin_Predictions.csv',index=False)


train.to_csv(f'{OUT}/P123_Training_Table.csv',index=False); p4[['x_mm','y_mm','z_mm','patient',*features]].to_csv(f'{OUT}/P4_Locked_Test_Features.csv',index=False)

report=['# Digital Twin V1 — Frozen Cross-Patient Surrogate','',f'- Freeze SHA256: `{fh}`','- Development: P1 + P2 + P3 only.','- Locked one-shot test: P4.','- Geometry-only inputs; no CFD/FSI targets are model inputs.','- Target-specific LightGBM model selected by leave-one-patient-out validation.','','## Development LOPO',seldf.to_markdown(index=False,floatfmt='.4f'),'','## Locked P4 test',testdf.to_markdown(index=False,floatfmt='.4f'),'','## Guardrail','This is a proof-of-concept computational surrogate, not a clinically validated digital twin. With only three training anatomies, cross-patient R² is expected to be the limiting metric. Negative R² is retained and reported rather than hidden. Spearman correlation and top-10% hotspot overlap are reported to separate spatial localization from absolute calibration.']
open(f'{OUT}/DIGITAL_TWIN_V1_REPORT.md','w').write('\n'.join(report))
print('FREEZE',fh)
print('\nLOPO\n',seldf.to_string(index=False))
print('\nP4 TEST\n',testdf.to_string(index=False))
print('\nDONE',OUT)
