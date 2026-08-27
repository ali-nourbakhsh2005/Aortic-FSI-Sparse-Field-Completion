import numpy as np,pandas as pd,os
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import r2_score
from scipy.stats import spearmanr
BASE='/mnt/data'; OUT=f'{BASE}/ICBME2026_ReviewerLoop/analysis';os.makedirs(OUT,exist_ok=True)
h=pd.read_csv(f'{BASE}/Patient4_VectorResolved_Hemodynamics.csv'); s=pd.read_csv(f'{BASE}/Patient4_CycleResolved_SolidMechanics_v2.csv'); p=pd.read_csv(f'{BASE}/P4_Personalized_Predictions(1).csv'); b=pd.read_csv(f'{BASE}/ICBME2026_ReviewerLoop/tuned_baseline_A4_predictions.csv'); f=pd.read_csv(f'{BASE}/_impl/DigitalTwin_V1/P4_Locked_Test_Features.csv')
truth={'TAWSS_vector_Pa':h.TAWSS_vector_Pa.values,'OSI':h.OSI.values,'RRT_1_per_Pa':h.RRT_1_per_Pa.values,'peak_WSS_magnitude_Pa':h.peak_WSS_magnitude_Pa.values,'VM_cycle_max_Pa':s.VM_cycle_max_Pa.values,'VM_temporal_mean_Pa':s.VM_temporal_mean_Pa.values}
mask=~b.anchor.astype(bool).values
xyz=h[['x_mm','y_mm','z_mm']].values
nn=NearestNeighbors(n_neighbors=9).fit(xyz); d,_=nn.kneighbors(xyz); w=np.mean(d[:,1:]**2,axis=1); w=w/np.mean(w[mask])
def wr2(y,p,w):
 y=y.astype(float); p=p.astype(float); ww=w.astype(float); mu=np.sum(ww*y)/np.sum(ww); return 1-np.sum(ww*(y-p)**2)/np.sum(ww*(y-mu)**2)
rows=[]; blocks=[]

sval=f.s_norm.values; cuts=np.quantile(sval[mask],[.2,.4,.6,.8]); bid=np.digitize(sval,cuts,right=True)
for t,y in truth.items():
 preds={'Prior':p[f'{t}_personalized_5pct'].values,'IDW':b[f'{t}_IDW'].values,'RBF':b[f'{t}_RBF'].values,'KNN':b[f'{t}_KNN'].values}
 for m,pred in preds.items():
  rows.append({'target':t,'method':m,'weighted_R2':wr2(y[mask],pred[mask],w[mask]),'weighted_MAE':np.average(np.abs(y[mask]-pred[mask]),weights=w[mask])})
  for q in range(5):
   mm=mask&(bid==q); blocks.append({'target':t,'method':m,'block':q+1,'n':mm.sum(),'R2':r2_score(y[mm],pred[mm]),'Spearman':spearmanr(y[mm],pred[mm]).statistic})
pd.DataFrame(rows).to_csv(f'{OUT}/selected_baseline_density_weighted_A4_5pct.csv',index=False)
pd.DataFrame(blocks).to_csv(f'{OUT}/selected_baseline_spatial_blocks_A4_5pct.csv',index=False)
print(pd.DataFrame(rows).pivot(index='target',columns='method',values='weighted_R2').round(3))
print(pd.DataFrame(blocks).groupby(['target','method'])[['R2','Spearman']].agg(['mean','std','min','max']).round(3))
