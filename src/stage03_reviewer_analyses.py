import os, json, warnings, hashlib
from itertools import product
import numpy as np
import pandas as pd
from scipy.interpolate import RBFInterpolator
from scipy.stats import spearmanr
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor, NearestNeighbors
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from lightgbm import LGBMRegressor
warnings.filterwarnings('ignore')
BASE='/mnt/data'
IMPL=f'{BASE}/_impl'
OUT=f'{BASE}/ICBME2026_ReviewerLoop/analysis'
os.makedirs(OUT,exist_ok=True)
freeze=json.load(open(f'{IMPL}/DigitalTwin_V1/FREEZE_MANIFEST_PRE_P4.json'))
train=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P123_Training_Table.csv')
p4=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P4_Locked_Test_Features.csv')
p4base=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P4_DigitalTwin_Predictions.csv')
p4pers=pd.read_csv(f'{BASE}/P4_Personalized_Predictions(1).csv')
h4=pd.read_csv(f'{BASE}/Patient4_VectorResolved_Hemodynamics.csv')
s4=pd.read_csv(f'{BASE}/Patient4_CycleResolved_SolidMechanics_v2.csv')
for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']: p4[c]=h4[c].values
for c in ['VM_cycle_max_Pa','VM_temporal_mean_Pa']: p4[c]=s4[c].values
TARGETS={'TAWSS_vector_Pa':'log1p','OSI':'identity','RRT_1_per_Pa':'log1p','peak_WSS_magnitude_Pa':'log1p','VM_cycle_max_Pa':'log','VM_temporal_mean_Pa':'log'}
LOCAL=['s_norm','dist_nearest_end','radial_norm','local_radius_over_median','local_radius_gradient','curvature_radius','curvature_side','tangent_alignment_main_axis']
FEATURES=freeze['features']; CANDS=freeze['candidates']; SELECTED=freeze['selected_models']; SEED=int(freeze['seed'])
FRACS=[.01,.02,.05,.10]

def tf(y,k):
 y=np.asarray(y,float)
 if k=='identity': return y
 if k=='log1p': return np.log1p(np.maximum(y,0))
 return np.log(np.maximum(y,1e-12))
def inv(z,k):
 if k=='identity': return np.asarray(z,float)
 if k=='log1p': return np.expm1(z)
 return np.exp(z)
def rep_indices(X,frac,seed):
 k=max(12,int(round(len(X)*frac))); sc=StandardScaler().fit(X); Z=sc.transform(X)
 km=MiniBatchKMeans(n_clusters=k,random_state=seed,n_init=3,batch_size=1024,max_iter=100).fit(Z)
 ids=np.array(sorted(set(int(np.argmin(((Z-c)**2).sum(1))) for c in km.cluster_centers_)))
 return ids,sc
def metrics(y,p,kind):
 y=np.asarray(y,float); p=np.asarray(p,float)
 kk=max(1,int(round(.1*len(y)))); A=set(np.argpartition(y,-kk)[-kk:]); B=set(np.argpartition(p,-kk)[-kk:])
 z=tf(y,kind); zp=tf(p,kind); iqr=np.quantile(z,.75)-np.quantile(z,.25)
 return {'R2':float(r2_score(y,p)),'MAE':float(mean_absolute_error(y,p)),'RMSE':float(mean_squared_error(y,p)**.5),'Spearman':float(spearmanr(y,p).statistic),'Top10':float(len(A&B)/kk),'TNMAE':float(np.mean(np.abs(z-zp))/(iqr+1e-12))}
def adapt(X,y,base,kind,frac,seed):
 cal,sc=rep_indices(X,frac,seed); mask=np.ones(len(X),bool); mask[cal]=False
 zb=tf(base,kind); zy=tf(y,kind); aff=Ridge(alpha=1e-3).fit(zb[cal,None],zy[cal]); za=aff.predict(zb[:,None]); Z=sc.transform(X)
 resid=zy[cal]-za[cal]; knn=KNeighborsRegressor(n_neighbors=min(10,len(cal)),weights='distance',p=2).fit(Z[cal],resid)
 return inv(za+knn.predict(Z),kind),cal,mask

def idw_predict(Q,cal,z,k,power,eval_idx=None):
 if eval_idx is None: eval_idx=np.arange(len(Q))
 nn=NearestNeighbors(n_neighbors=min(k,len(cal))).fit(Q[cal]); d,ix=nn.kneighbors(Q[eval_idx]); w=1/np.maximum(d,1e-12)**power
 return (w*z[cal][ix]).sum(1)/w.sum(1)


pats=train.patient.to_numpy(); counts={x:int((pats==x).sum()) for x in np.unique(pats)}; weights=np.array([1/counts[x] for x in pats],float); weights*=len(weights)/weights.sum()
rows=[]
for t,kind in TARGETS.items():
 par=dict(CANDS[SELECTED[t]]); mdl=LGBMRegressor(**par); mdl.fit(train[FEATURES],tf(train[t],kind),sample_weight=weights); alt=inv(mdl.predict(p4[FEATURES]),kind)
 y=p4[t].to_numpy(float); current=p4base[f'{t}_pred'].to_numpy(float)
 altp,cal,mask=adapt(p4[LOCAL].to_numpy(float),y,alt,kind,.05,SEED+404+500)
 curp,_,_=adapt(p4[LOCAL].to_numpy(float),y,current,kind,.05,SEED+404+500)
 ma=metrics(y,alt,kind); mc=metrics(y,current,kind); mpa=metrics(y[mask],altp[mask],kind); mpc=metrics(y[mask],curp[mask],kind)
 rows.append({'target':t,'cv_selected_n_estimators':par['n_estimators'],'actual_final_n_estimators':450,
              **{f'zero_selected_{k}':v for k,v in ma.items()},**{f'zero_450_{k}':v for k,v in mc.items()},
              **{f'adapt_selected_{k}':v for k,v in mpa.items()},**{f'adapt_450_{k}':v for k,v in mpc.items()}})
pd.DataFrame(rows).to_csv(f'{OUT}/freeze_refit_450_sensitivity.csv',index=False)


dev={}
for vp in [1,2,3]:
 d=train[train.patient==vp].reset_index(drop=True); X=d[LOCAL].to_numpy(float); cal,sc=rep_indices(X,.05,SEED+vp+500); mask=np.ones(len(d),bool);mask[cal]=False
 dev[vp]=(d,cal,mask,sc.transform(X),StandardScaler().fit_transform(d[['x_mm','y_mm','z_mm']]))
sweep=[]
def summarize(method,config,vals):
 sweep.append({'method':method,'config':config,'mean_TNMAE':np.mean([v['TNMAE'] for v in vals]),'mean_R2':np.mean([v['R2'] for v in vals]),'mean_Spearman':np.mean([v['Spearman'] for v in vals]),'mean_Top10':np.mean([v['Top10'] for v in vals])})
for k in [5,10,20]:
 vals=[]
 for vp,(d,cal,mask,Z,Q) in dev.items():
  for t,kind in TARGETS.items():
   z=tf(d[t].values,kind); pred=inv(KNeighborsRegressor(n_neighbors=min(k,len(cal)),weights='distance',p=2).fit(Z[cal],z[cal]).predict(Z[mask]),kind); vals.append(metrics(d[t].values[mask],pred,kind))
 summarize('KNN',f'k={k}',vals)
for k,power in product([8,12,20],[1,2,3]):
 vals=[]
 for vp,(d,cal,mask,Z,Q) in dev.items():
  e=np.where(mask)[0]
  for t,kind in TARGETS.items():
   pred=inv(idw_predict(Q,cal,tf(d[t].values,kind),k,power,e),kind); vals.append(metrics(d[t].values[mask],pred,kind))
 summarize('IDW',f'k={k},p={power}',vals)
for n,sm in product([30,50,80],[1e-6,1e-3]):
 vals=[]
 for vp,(d,cal,mask,Z,Q) in dev.items():
  for t,kind in TARGETS.items():
   z=tf(d[t].values,kind); pred=inv(RBFInterpolator(Q[cal],z[cal],kernel='thin_plate_spline',smoothing=sm,neighbors=min(n,len(cal)))(Q[mask]),kind); vals.append(metrics(d[t].values[mask],pred,kind))
 summarize('RBF',f'n={n},s={sm:g}',vals)
sweepdf=pd.DataFrame(sweep); sweepdf.to_csv(f'{OUT}/baseline_hyperparameter_sweep_dev5pct.csv',index=False)

best={}
for method in ['KNN','IDW','RBF']:
 q=sweepdf[sweepdf.method==method].sort_values(['mean_TNMAE','mean_Spearman'],ascending=[True,False]).iloc[0]
 best[method]=q['config']
json.dump(best,open(f'{OUT}/baseline_selected_config.json','w'),indent=2)

KNN_K=int(best['KNN'].split('=')[1]); IDW_K=int(best['IDW'].split(',')[0].split('=')[1]); IDW_P=float(best['IDW'].split('p=')[1]); RBF_N=int(best['RBF'].split(',')[0].split('=')[1]); RBF_S=float(best['RBF'].split('s=')[1])


detail=[]
for vp,(d,cal,mask,Z,Q) in dev.items():
 e=np.where(mask)[0]
 for t,kind in TARGETS.items():
  y=d[t].values; z=tf(y,kind)
  pk=inv(KNeighborsRegressor(n_neighbors=min(KNN_K,len(cal)),weights='distance',p=2).fit(Z[cal],z[cal]).predict(Z[mask]),kind)
  pi=inv(idw_predict(Q,cal,z,IDW_K,IDW_P,e),kind)
  pr=inv(RBFInterpolator(Q[cal],z[cal],kernel='thin_plate_spline',smoothing=RBF_S,neighbors=min(RBF_N,len(cal)))(Q[mask]),kind)
  for name,pred in [('KNN',pk),('IDW',pi),('RBF',pr)]: detail.append({'heldout_anatomy':vp,'target':t,'method':name,'n_anchor':len(cal),'n_eval':int(mask.sum()),**metrics(y[mask],pred,kind)})
pd.DataFrame(detail).to_csv(f'{OUT}/baseline_selected_dev_LOAO_5pct_detail.csv',index=False)


a4rows=[]; bound=[]
for frac in FRACS:
 X=p4[LOCAL].to_numpy(float); cal,sc=rep_indices(X,frac,SEED+404+int(frac*10000)); mask=np.ones(len(p4),bool);mask[cal]=False; Z=sc.transform(X); Q=StandardScaler().fit_transform(p4[['x_mm','y_mm','z_mm']]); e=np.where(mask)[0]
 for t,kind in TARGETS.items():
  y=p4[t].values; z=tf(y,kind)
  pk=inv(KNeighborsRegressor(n_neighbors=min(KNN_K,len(cal)),weights='distance',p=2).fit(Z[cal],z[cal]).predict(Z[mask]),kind)
  pi=inv(idw_predict(Q,cal,z,IDW_K,IDW_P,e),kind)
  pr=inv(RBFInterpolator(Q[cal],z[cal],kernel='thin_plate_spline',smoothing=RBF_S,neighbors=min(RBF_N,len(cal)))(Q[mask]),kind)
  for name,pred in [('KNN',pk),('IDW',pi),('RBF',pr)]:
   a4rows.append({'fraction':frac,'target':t,'method':name,'n_anchor':len(cal),'n_eval':int(mask.sum()),**metrics(y[mask],pred,kind)})
   if t=='OSI': bound.append({'fraction':frac,'method':name,'n_eval':int(mask.sum()),'min_prediction':float(pred.min()),'max_prediction':float(pred.max()),'outside_0_0p5':int(np.sum((pred<0)|(pred>.5)))})
pd.DataFrame(a4rows).to_csv(f'{OUT}/baseline_selected_A4_fractionwise.csv',index=False); pd.DataFrame(bound).to_csv(f'{OUT}/baseline_OSI_bounds_A4.csv',index=False)


frac=.05; X=p4[LOCAL].to_numpy(float); cal,sc=rep_indices(X,frac,SEED+404+500); mask=np.ones(len(p4),bool);mask[cal]=False; Q=StandardScaler().fit_transform(p4[['x_mm','y_mm','z_mm']]); e=np.where(mask)[0]
nn1=NearestNeighbors(n_neighbors=1).fit(Q[cal]); dist=nn1.kneighbors(Q)[0][:,0]; cuts=np.quantile(dist[mask],[.25,.5,.75]); quart=np.digitize(dist,cuts,right=True)

idw_nn=NearestNeighbors(n_neighbors=min(IDW_K,len(cal))).fit(Q[cal]); dd,ix=idw_nn.kneighbors(Q); ww=1/np.maximum(dd,1e-12)**IDW_P
rows=[]
for t,kind in TARGETS.items():
 y=p4[t].values; z=tf(y,kind); idw=inv((ww*z[cal][ix]).sum(1)/ww.sum(1),kind); rbf=inv(RBFInterpolator(Q[cal],z[cal],kernel='thin_plate_spline',smoothing=RBF_S,neighbors=min(RBF_N,len(cal)))(Q),kind); prior=p4pers[f'{t}_personalized_5pct'].values
 iqr=np.quantile(y[mask],.75)-np.quantile(y[mask],.25)
 for name,pred in [('Prior+adapt',prior),('IDW',idw),('RBF',rbf)]:
  err=np.abs(y-pred)/(iqr+1e-12); rho=float(spearmanr(dist[mask],err[mask]).statistic)
  for q in range(4):
   m=mask&(quart==q); rows.append({'target':t,'method':name,'distance_quartile':q+1,'n':int(m.sum()),'median_stdxyz_nearest_anchor_distance':float(np.median(dist[m])),'median_abs_error_over_IQR':float(np.median(err[m])),'mean_abs_error_over_IQR':float(np.mean(err[m])),'Spearman_distance_vs_error':rho})
pd.DataFrame(rows).to_csv(f'{OUT}/A4_nearest_anchor_distance_sensitivity.csv',index=False)


def sha(path):
 h=hashlib.sha256();
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()
files=[f'{IMPL}/digital_twin_v1.py',f'{IMPL}/digital_twin_v2_personalized.py',f'{IMPL}/DigitalTwin_V1/FREEZE_MANIFEST_PRE_P4.json',f'{IMPL}/DigitalTwin_V1/DigitalTwin_V1_Models.joblib']
pd.DataFrame([{'file':os.path.basename(x),'sha256':sha(x)} for x in files]).to_csv(f'{OUT}/core_pipeline_hashes.csv',index=False)
print('Selected baselines:',best)
print(pd.DataFrame(a4rows).query('fraction==0.05').groupby('method')[['R2','Spearman','Top10']].mean())
