from pathlib import Path
import json
import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from scipy.stats import spearmanr

BASE=Path('/mnt/data')
V1=BASE/'DigitalTwin_V1'
OUT=BASE/'DigitalTwin_Component_Ablation_Reconstructed'
OUT.mkdir(parents=True,exist_ok=True)
freeze=json.load(open(V1/'FREEZE_MANIFEST_PRE_P4.json'))
TARGETS={k:v for k,v in freeze['target_transforms'].items() if k!='VM_stress_amplitude_Pa'}
FEATURES=freeze['features']; CANDS=freeze['candidates']; SELECTED=freeze['selected_models']; SEED=int(freeze['seed'])
LOCAL=['s_norm','dist_nearest_end','radial_norm','local_radius_over_median','local_radius_gradient','curvature_radius','curvature_side','tangent_alignment_main_axis']


def tf(y,k):
    y=np.asarray(y,float)
    if k=='identity': return y
    if k=='log1p': return np.log1p(np.maximum(y,0))
    return np.log(np.maximum(y,1e-12))

def inv(z,k):
    if k=='identity': return np.asarray(z,float)
    if k=='log1p': return np.expm1(z)
    return np.exp(z)

def representative_indices(X,frac,seed):
    k=max(12,int(round(len(X)*frac)))
    sc=StandardScaler().fit(X); Z=sc.transform(X)
    km=MiniBatchKMeans(n_clusters=k,random_state=seed,n_init=3,batch_size=1024,max_iter=100).fit(Z)
    ids=np.array(sorted(set(int(np.argmin(((Z-c)**2).sum(1))) for c in km.cluster_centers_)))
    return ids,sc

def met(y,p):
    k=max(1,int(round(.1*len(y))))
    A=set(np.argpartition(y,-k)[-k:]); B=set(np.argpartition(p,-k)[-k:])
    return dict(R2=r2_score(y,p),MAE=mean_absolute_error(y,p),RMSE=mean_squared_error(y,p)**.5,
                Spearman=spearmanr(y,p).statistic,Top10=len(A&B)/k)

def variants(Xlocal,y,base,kind,frac,seed):
    cal,sc=representative_indices(Xlocal,frac,seed)
    mask=np.ones(len(y),bool); mask[cal]=False
    Z=sc.transform(Xlocal); zy=tf(y,kind); zb=tf(base,kind)

    aff=Ridge(alpha=1e-3).fit(zb[cal,None],zy[cal])
    za=aff.predict(zb[:,None])
    affine=inv(za,kind)

    res0=zy[cal]-zb[cal]
    k0=KNeighborsRegressor(n_neighbors=min(10,len(cal)),weights='distance',p=2).fit(Z[cal],res0)
    local=inv(zb+k0.predict(Z),kind)

    res1=zy[cal]-za[cal]
    k1=KNeighborsRegressor(n_neighbors=min(10,len(cal)),weights='distance',p=2).fit(Z[cal],res1)
    full=inv(za+k1.predict(Z),kind)
    return {'zero_shot':base,'affine_only':affine,'local_only':local,'full':full},cal,mask


def main():
    train=pd.read_csv(V1/'P123_Training_Table.csv')
    p4f=pd.read_csv(V1/'P4_Locked_Test_Features.csv')
    p4base=pd.read_csv(V1/'P4_DigitalTwin_Predictions.csv')
    h4=pd.read_csv(BASE/'Patient4_VectorResolved_Hemodynamics.csv')
    s4=pd.read_csv(BASE/'Patient4_CycleResolved_SolidMechanics_v2.csv')
    for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']: p4f[c]=h4[c].values
    for c in ['VM_cycle_max_Pa','VM_temporal_mean_Pa']: p4f[c]=s4[c].values

    rows=[]

    for vp in [1,2,3]:
        tr=train.patient!=vp; va=train.patient==vp
        pats=train.loc[tr,'patient'].to_numpy(); cnt={p:(pats==p).sum() for p in np.unique(pats)}
        w=np.array([1/cnt[p] for p in pats]); w*=len(w)/w.sum()
        for target,kind in TARGETS.items():
            model=LGBMRegressor(**dict(CANDS[SELECTED[target]]))
            model.fit(train.loc[tr,FEATURES],tf(train.loc[tr,target],kind),sample_weight=w)
            base=inv(model.predict(train.loc[va,FEATURES]),kind)
            y=train.loc[va,target].to_numpy(float)
            for frac in [0.05,0.10]:
                vv,cal,mask=variants(train.loc[va,LOCAL].to_numpy(float),y,base,kind,frac,SEED+vp+int(frac*10000))
                for name,pred in vv.items():
                    if name!='full' and frac==0.10: continue
                    rows.append({'scope':'development','anatomy':vp,'target':target,'fraction':frac,'variant':name,'n_anchor':len(cal),'n_eval':mask.sum(),**met(y[mask],pred[mask])})


    for target,kind in TARGETS.items():
        y=p4f[target].to_numpy(float); base=p4base[f'{target}_pred'].to_numpy(float)
        for frac in [0.05,0.10]:
            vv,cal,mask=variants(p4f[LOCAL].to_numpy(float),y,base,kind,frac,SEED+404+int(frac*10000))
            for name,pred in vv.items():
                if name!='full' and frac==0.10: continue
                rows.append({'scope':'A4','anatomy':4,'target':target,'fraction':frac,'variant':name,'n_anchor':len(cal),'n_eval':mask.sum(),**met(y[mask],pred[mask])})

    d=pd.DataFrame(rows)
    d.to_csv(OUT/'component_ablation_detail.csv',index=False)
    agg=d.groupby(['scope','variant','fraction'])[['R2','MAE','RMSE','Spearman','Top10']].mean().reset_index()
    agg.to_csv(OUT/'component_ablation_aggregate.csv',index=False)
    print(agg)

if __name__=='__main__':
    main()
