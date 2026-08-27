import os, json, warnings
import numpy as np, pandas as pd
from scipy.interpolate import RBFInterpolator
from scipy.stats import spearmanr
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import r2_score
warnings.filterwarnings('ignore')
BASE='/mnt/data'; IMPL=f'{BASE}/_impl'; OUT=f'{BASE}/ICBME2026_ReviewerLoop/analysis'; os.makedirs(OUT,exist_ok=True)
freeze=json.load(open(f'{IMPL}/DigitalTwin_V1/FREEZE_MANIFEST_PRE_P4.json')); SEED=int(freeze['seed'])
train=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P123_Training_Table.csv'); p4=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P4_Locked_Test_Features.csv')
h4=pd.read_csv(f'{BASE}/Patient4_VectorResolved_Hemodynamics.csv'); s4=pd.read_csv(f'{BASE}/Patient4_CycleResolved_SolidMechanics_v2.csv')
for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']: p4[c]=h4[c].values
for c in ['VM_cycle_max_Pa','VM_temporal_mean_Pa']: p4[c]=s4[c].values
TARGETS={'TAWSS_vector_Pa':'log1p','OSI':'identity','RRT_1_per_Pa':'log1p','peak_WSS_magnitude_Pa':'log1p','VM_cycle_max_Pa':'log','VM_temporal_mean_Pa':'log'}
LOCAL=['s_norm','dist_nearest_end','radial_norm','local_radius_over_median','local_radius_gradient','curvature_radius','curvature_side','tangent_alignment_main_axis']
FRAC=.05; IDW_K=8; IDW_P=3.; RBF_N=80; RBF_S=1e-3

def tf(y,k):
 y=np.asarray(y,float); return y if k=='identity' else np.log1p(np.maximum(y,0)) if k=='log1p' else np.log(np.maximum(y,1e-12))
def inv(z,k):
 z=np.asarray(z,float); return z if k=='identity' else np.expm1(z) if k=='log1p' else np.exp(z)
def met(y,p):
 kk=max(1,int(round(.1*len(y)))); A=set(np.argpartition(y,-kk)[-kk:]); B=set(np.argpartition(p,-kk)[-kk:]); return r2_score(y,p), spearmanr(y,p).statistic, len(A&B)/kk

def anchors(X,strategy,seed):
 k=max(12,int(round(len(X)*FRAC))); sc=StandardScaler().fit(X); Z=sc.transform(X)
 if strategy=='kmeans':
  km=MiniBatchKMeans(n_clusters=k,random_state=seed,n_init=3,batch_size=1024,max_iter=100).fit(Z)
  ids=np.array(sorted(set(int(np.argmin(((Z-c)**2).sum(1))) for c in km.cluster_centers_)))
 else:
  ids=np.sort(np.random.default_rng(seed).choice(len(X),size=k,replace=False))
 return ids

def idw_all(XYZ,cal,z):
 Q=StandardScaler().fit_transform(XYZ); nn=NearestNeighbors(n_neighbors=min(IDW_K,len(cal))).fit(Q[cal]); d,ix=nn.kneighbors(Q); w=1/np.maximum(d,1e-12)**IDW_P; return (w*z[cal][ix]).sum(1)/w.sum(1)
rows=[]
for scope,frames in [('development',[(i,train[train.patient==i].reset_index(drop=True)) for i in [1,2,3]]),('A4',[(4,p4)])]:
 for strategy in ['kmeans','random']:
  for rep in range(10):
   for aid,d in frames:
    cal=anchors(d[LOCAL].to_numpy(float),strategy,SEED+(10000 if scope=='development' else 20000)+rep*17+aid)
    mask=np.ones(len(d),bool);mask[cal]=False
    for t,k in TARGETS.items():
     pred=inv(idw_all(d[['x_mm','y_mm','z_mm']].to_numpy(float),cal,tf(d[t].values,k)),k)
     r2,rho,top=met(d[t].values[mask],pred[mask]); rows.append({'scope':scope,'anchor_strategy':strategy,'replicate':rep,'anatomy':aid,'target':t,'method':'IDW','R2':r2,'Spearman':rho,'Top10':top,'n_anchor':len(cal)})
df=pd.DataFrame(rows); df.to_csv(f'{OUT}/anchor_selection_IDW_robustness_detail.csv',index=False)
macro=df.groupby(['scope','anchor_strategy','replicate','anatomy'])[['R2','Spearman','Top10']].mean().reset_index(); macro.to_csv(f'{OUT}/anchor_selection_IDW_robustness_macro.csv',index=False)
summ=macro.groupby(['scope','anchor_strategy'])[['R2','Spearman','Top10']].agg(['mean','std','median','min','max']); summ.to_csv(f'{OUT}/anchor_selection_IDW_robustness_summary.csv')

X=p4[LOCAL].to_numpy(float); cal=anchors(X,'kmeans',SEED+404+500); mask=np.ones(len(p4),bool);mask[cal]=False; Q=StandardScaler().fit_transform(p4[['x_mm','y_mm','z_mm']]); y=p4.OSI.values
raw=RBFInterpolator(Q[cal],y[cal],kernel='thin_plate_spline',smoothing=RBF_S,neighbors=min(RBF_N,len(cal)))(Q); clipped=np.clip(raw,0,.5)
rr=[]
for n,p in [('raw',raw),('clipped',clipped)]:
 r2,rho,top=met(y[mask],p[mask]); rr.append({'variant':n,'R2':r2,'Spearman':rho,'Top10':top,'min':p[mask].min(),'max':p[mask].max(),'outside':int(((p[mask]<0)|(p[mask]>.5)).sum()),'n_eval':mask.sum()})
pd.DataFrame(rr).to_csv(f'{OUT}/RBF_OSI_physical_bound_sensitivity_A4_5pct.csv',index=False)
print(summ)
print(pd.DataFrame(rr))
