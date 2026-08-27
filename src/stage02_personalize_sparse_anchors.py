import os, json, math, warnings, hashlib, datetime
import numpy as np, pandas as pd
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from scipy.stats import spearmanr
from lightgbm import LGBMRegressor
warnings.filterwarnings('ignore')

V1='/mnt/data/DigitalTwin_V1'; OUT='/mnt/data/DigitalTwin_V2_Personalized'; os.makedirs(OUT,exist_ok=True)
freeze=json.load(open(V1+'/FREEZE_MANIFEST_PRE_P4.json'))
TARGETS=freeze['target_transforms']; features=freeze['features']; selected=freeze['selected_models']; candidates=freeze['candidates']; SEED=freeze['seed']
train=pd.read_csv(V1+'/P123_Training_Table.csv')
p4f=pd.read_csv(V1+'/P4_Locked_Test_Features.csv')
p4base=pd.read_csv(V1+'/P4_DigitalTwin_Predictions.csv')
h4=pd.read_csv('/mnt/data/Patient4_VectorResolved_Hemodynamics.csv'); s4=pd.read_csv('/mnt/data/Patient4_CycleResolved_SolidMechanics_v2.csv')
for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']: p4f[c]=h4[c].values
for c in ['VM_cycle_max_Pa','VM_stress_amplitude_Pa','VM_temporal_mean_Pa']: p4f[c]=s4[c].values

LOCAL=['s_norm','dist_nearest_end','radial_norm','local_radius_over_median','local_radius_gradient','curvature_radius','curvature_side','tangent_alignment_main_axis']
FRACS=[0.01,0.02,0.05,0.10]
KNN_K=10

def tf(y,k):
 y=np.asarray(y,float)
 if k=='identity': return y
 if k=='log1p': return np.log1p(np.maximum(y,0))
 return np.log(np.maximum(y,1e-12))
def inv(z,k):
 if k=='identity': return z
 if k=='log1p': return np.expm1(z)
 return np.exp(z)
def metrics(y,p):
 k=max(1,int(round(.1*len(y)))); A=set(np.argpartition(y,-k)[-k:].tolist()); B=set(np.argpartition(p,-k)[-k:].tolist())
 return {'R2':float(r2_score(y,p)),'MAE':float(mean_absolute_error(y,p)),'RMSE':float(mean_squared_error(y,p)**.5),'Spearman':float(spearmanr(y,p).statistic),'Top10_overlap':len(A&B)/k}

def representative_indices(X,frac,seed):
 n=len(X); k=max(12,int(round(n*frac))); scaler=StandardScaler().fit(X); Z=scaler.transform(X)
 km=MiniBatchKMeans(n_clusters=k,random_state=seed,n_init=3,batch_size=1024,max_iter=100).fit(Z)
 ids=[]
 for c in km.cluster_centers_:
  ids.append(int(np.argmin(((Z-c)**2).sum(1))))
 ids=np.array(sorted(set(ids)))
 return ids,scaler

def adapt(X,y,base,kind,frac,seed):
 cal,sc=representative_indices(X,frac,seed); test=np.ones(len(X),bool); test[cal]=False
 zb=tf(base,kind); zy=tf(y,kind)

 aff=Ridge(alpha=1e-3).fit(zb[cal,None],zy[cal]); za=aff.predict(zb[:,None])

 resid=zy[cal]-za[cal]; Z=sc.transform(X)
 knn=KNeighborsRegressor(n_neighbors=min(KNN_K,len(cal)),weights='distance',p=2).fit(Z[cal],resid)
 zpred=za+knn.predict(Z); pred=inv(zpred,kind)
 return pred,cal,test


dev_rows=[]
for vp in [1,2,3]:
 tr=train.patient!=vp; va=train.patient==vp
 Xtr=train.loc[tr,features]; Xv=train.loc[va,features]; Xlocal=train.loc[va,LOCAL].to_numpy(float)
 pats=train.loc[tr,'patient'].to_numpy(); cnt={p:(pats==p).sum() for p in np.unique(pats)}; w=np.array([1/cnt[p] for p in pats]); w*=len(w)/w.sum()
 for target,kind in TARGETS.items():
  par=dict(candidates[selected[target]])
  model=LGBMRegressor(**par); model.fit(Xtr,tf(train.loc[tr,target],kind),sample_weight=w)
  base=inv(model.predict(Xv),kind); y=train.loc[va,target].to_numpy(float)
  for frac in FRACS:
   pred,cal,mask=adapt(Xlocal,y,base,kind,frac,seed=SEED+vp+int(frac*10000))
   mm=metrics(y[mask],pred[mask]); dev_rows.append({'val_patient':vp,'target':target,'calibration_fraction':frac,'n_calibration':len(cal),**mm})
dev=pd.DataFrame(dev_rows); dev.to_csv(OUT+'/P123_Personalization_LOPO.csv',index=False)
devsum=dev.groupby(['target','calibration_fraction']).agg(mean_R2=('R2','mean'),mean_MAE=('MAE','mean'),mean_Spearman=('Spearman','mean'),mean_Top10_overlap=('Top10_overlap','mean')).reset_index(); devsum.to_csv(OUT+'/P123_Personalization_Summary.csv',index=False)


manifest={'base_freeze_hash':open(V1+'/FREEZE_MANIFEST_SHA256.txt').read().split()[0],'protocol':'Sparse representative-anchor personalization: affine correction in transformed target space + KNN residual correction in local geometry feature space','local_features':LOCAL,'calibration_fractions':FRACS,'anchor_selection':'MiniBatchKMeans representatives in standardized local-geometry feature space','knn_neighbors':KNN_K,'development_patients':[1,2,3],'personalization_case':4,'note':'P4 zero-shot test was already frozen/evaluated in V1. V2 is a secondary patient-specific calibration experiment, not an unseen zero-shot test.','frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
mp=OUT+'/PERSONALIZATION_PROTOCOL.json'; json.dump(manifest,open(mp,'w'),indent=2)


p4_rows=[]; p4preds=p4base[['x_mm','y_mm','z_mm']].copy()
for target,kind in TARGETS.items():
 y=p4f[target].to_numpy(float); base=p4base[target+'_pred'].to_numpy(float); X=p4f[LOCAL].to_numpy(float)
 for frac in FRACS:
  pred,cal,mask=adapt(X,y,base,kind,frac,seed=SEED+404+int(frac*10000))
  tag=f'{int(frac*100)}pct' if frac>=.01 else str(frac)
  p4preds[f'{target}_personalized_{tag}']=pred
  mm=metrics(y[mask],pred[mask]); p4_rows.append({'target':target,'calibration_fraction':frac,'n_calibration':len(cal),'n_evaluation':int(mask.sum()),**mm})
p4=pd.DataFrame(p4_rows); p4.to_csv(OUT+'/P4_PERSONALIZED_TEST_METRICS.csv',index=False); p4preds.to_csv(OUT+'/P4_Personalized_Predictions.csv',index=False)

report=['# Digital Twin V2 — Sparse Personalized Calibration','',manifest['note'],'','## P1–P3 development validation',devsum.to_markdown(index=False,floatfmt='.4f'),'','## P4 personalization evaluation (remaining non-anchor points only)',p4.to_markdown(index=False,floatfmt='.4f')]
open(OUT+'/DIGITAL_TWIN_V2_REPORT.md','w').write('\n'.join(report))
print('\nDEV SUMMARY\n',devsum.to_string(index=False))
print('\nP4 PERSONALIZED\n',p4.to_string(index=False))
print('\nDONE',OUT)
