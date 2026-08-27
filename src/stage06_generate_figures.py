import os, json
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scipy.signal import savgol_filter
from pathlib import Path

BASE='/mnt/data'
OUT=Path('/mnt/data/ICBME2026_ReviewerLoop/V9_digital_twin_roadmap/figs')
OUT.mkdir(parents=True,exist_ok=True)
IMPL=f'{BASE}/_impl'
train=pd.read_csv(f'{IMPL}/DigitalTwin_V1/P123_Training_Table.csv')
dev=pd.read_csv(f'{IMPL}/DigitalTwin_V2_Personalized/P123_Personalization_LOPO.csv')
p4met=pd.read_csv(f'{BASE}/P4_PERSONALIZED_TEST_METRICS(2).csv')
base=pd.read_csv(f'{BASE}/ICBME2026_ReviewerLoop/analysis/baseline_selected_A4_fractionwise.csv')
bpred=pd.read_csv(f'{BASE}/ICBME2026_ReviewerLoop/tuned_baseline_A4_predictions.csv')
pers=pd.read_csv(f'{BASE}/P4_Personalized_Predictions(1).csv')
h4=pd.read_csv(f'{BASE}/Patient4_VectorResolved_Hemodynamics.csv')
s4=pd.read_csv(f'{BASE}/Patient4_CycleResolved_SolidMechanics_v2.csv')
unc=pd.read_csv(f'{BASE}/DigitalTwin_V3_Multiphysics/P4_Personalized_Uncertainty_5pct.csv')
ood=pd.read_csv(f'{BASE}/DigitalTwin_V3_Multiphysics/P4_Geometry_OOD_Map.csv')
SIX=['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa','VM_cycle_max_Pa','VM_temporal_mean_Pa']
NAME={'TAWSS_vector_Pa':'TAWSS','OSI':'OSI','RRT_1_per_Pa':'RRT','peak_WSS_magnitude_Pa':'Peak WSS','VM_cycle_max_Pa':'Cycle-max VM','VM_temporal_mean_Pa':'Temporal-mean VM'}


fig,ax=plt.subplots(figsize=(14.2,7.6)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
def box(x,y,w,h,title,body,ls='-',lw=1.1):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.5',linewidth=lw,linestyle=ls,facecolor='white')
    ax.add_patch(p); ax.text(x+w/2,y+h-3,title,ha='center',va='top',fontsize=9.6,fontweight='bold'); ax.text(x+w/2,y+h/2-2,body,ha='center',va='center',fontsize=8.2,linespacing=1.12); return (x,y,w,h)
def ar(a,b,style='->',ls='-'):
    x,y,w,h=a; x2,y2,w2,h2=b; ax.add_patch(FancyArrowPatch((x+w,y+h/2),(x2,y2+h2/2),arrowstyle=style,mutation_scale=12,linewidth=1.0,linestyle=ls))
ax.text(50,96,'Current computational benchmark and roadmap toward an advanced cardiovascular digital twin',ha='center',va='center',fontsize=13.5,fontweight='bold')
a=box(2,70,16,19,'A1-A3 development','Standardized first-cycle FSI\n6 nonredundant fields\nGeometry point clouds')
b=box(22,70,17,19,'Geometry representation','21 pseudo-centerline descriptors\nAnatomy-balanced LOAO')
c=box(43,70,17,19,'Cross-anatomy prior','Target-specific LightGBM\nZero-shot transfer stress test')
d=box(64,70,14,19,'A4 zero-shot','Target-excluded scoring\nNegative result retained')
for x,y in [(a,b),(b,c),(c,d)]: ar(x,y)
e=box(8,38,19,20,'FSI-derived sparse anchors','1%, 2%, 5%, 10% nodes\nOracle field-completion experiment\nNot clinical measurements')
f=box(33,38,19,20,'Prior + adaptation','Affine correction\n+ local geometry KNN residual')
g=box(58,38,19,20,'Same-anchor controls','KNN / IDW / RBF\nNo A1-A3 target fields')
h=box(82,38,15,20,'Diagnostics','Empirical residual bands\nGeometry OOD\nSpatial failure analysis')
for x,y in [(e,f),(f,g),(g,h)]: ar(x,y)
ax.add_patch(FancyArrowPatch((71,70),(18,58),arrowstyle='->',mutation_scale=12,connectionstyle='arc3,rad=-.08'))

r1=box(8,6,20,20,'Future Phase II','Larger independent anatomy cohort\nPeriodically converged / pressure-loaded FSI\nMeasurement-linked sparse inputs',ls='--')
r2=box(34,6,20,20,'Physics-informed learning','PINNs / physics-informed neural operators\nNavier-Stokes + wall-mechanics constraints\nMulti-fidelity training',ls='--')
r3=box(60,6,18,20,'Online data assimilation','4D-flow / pressure / flow observables\nBayesian or ensemble uncertainty\nActive sensing and OOD-aware updating',ls='--')
r4=box(83,6,15,20,'Advanced digital twin','Longitudinal synchronization\nBidirectional physical-digital update\nProspective external validation',ls='--')
for x,y in [(r1,r2),(r2,r3),(r3,r4)]: ar(x,y,ls='--')
ax.add_patch(FancyArrowPatch((89.5,38),(18,26),arrowstyle='->',mutation_scale=12,linestyle='--',connectionstyle='arc3,rad=.12'))
ax.text(50,31,'Dashed boxes denote planned research directions, not capabilities demonstrated in the present study.',ha='center',fontsize=8.8,fontstyle='italic')
fig.tight_layout(); fig.savefig(OUT/'architecture_roadmap.pdf',bbox_inches='tight'); fig.savefig(OUT/'architecture_roadmap.png',dpi=260,bbox_inches='tight'); plt.close(fig)


fig,axes=plt.subplots(3,1,figsize=(8.7,8.2),sharex=True)
metric_specs=[('R2','$R^2$'),('Spearman','Spearman $\\rho$'),('Top10_overlap','Top-decile overlap')]
for ax,(m,lab) in zip(axes,metric_specs):
    for t in SIX:
        q=dev[dev.target==t].groupby('calibration_fraction')[m].mean().reset_index(); x=q.calibration_fraction*100
        ax.plot(x,q[m],marker='o',linewidth=1.2,label=NAME[t])
    ax.axvline(5,linestyle='--',linewidth=.9); ax.set_ylabel(lab); ax.grid(alpha=.2)
axes[-1].set_xlabel('Calibration nodes (%)'); axes[-1].set_xticks([1,2,5,10])
axes[0].legend(ncol=3,fontsize=7.8,frameon=False,loc='lower right')
fig.suptitle('Development-only LOAO calibration behavior by metric',fontsize=12)
fig.tight_layout(rect=[0,0,1,.97]); fig.savefig(OUT/'calibration_metrics_separated.pdf',bbox_inches='tight'); plt.close(fig)


truth={'OSI':h4.OSI.values,'peak_WSS_magnitude_Pa':h4.peak_WSS_magnitude_Pa.values,'VM_cycle_max_Pa':s4.VM_cycle_max_Pa.values}
xyz=h4[['x_mm','y_mm','z_mm']].to_numpy(float); anchor=bpred.anchor.to_numpy(bool); mask=~anchor
fig=plt.figure(figsize=(13.2,8.7)); targets=[('OSI','OSI'),('peak_WSS_magnitude_Pa','Peak WSS (Pa)'),('VM_cycle_max_Pa','Cycle-max VM (kPa)')]
for r,(t,label) in enumerate(targets):
    ref=truth[t].copy(); prior=pers[f'{t}_personalized_5pct'].values.copy(); idw=bpred[f'{t}_IDW'].values.copy(); rbf=bpred[f'{t}_RBF'].values.copy(); scale=1/1000 if t=='VM_cycle_max_Pa' else 1.
    vals=[ref*scale,prior*scale,idw*scale,rbf*scale]; comb=np.concatenate([v[mask] for v in vals]); lo,hi=np.quantile(comb,[.01,.99])
    for c,(v,ttl) in enumerate(zip(vals,['Reference + anchors','Prior+adapt','IDW','RBF'])):
        ax=fig.add_subplot(3,4,r*4+c+1,projection='3d'); sc=ax.scatter(xyz[mask,0],xyz[mask,1],xyz[mask,2],c=v[mask],s=2.0,vmin=lo,vmax=hi,rasterized=True)
        if c==0: ax.scatter(xyz[anchor,0],xyz[anchor,1],xyz[anchor,2],s=8,marker='x',linewidths=.65)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([]); ax.view_init(18,-58); ax.set_title(ttl if r==0 else '',fontsize=8.8)
        if c==0: ax.text2D(-.16,.5,label,transform=ax.transAxes,rotation=90,va='center',fontsize=8.8,fontweight='bold')
        if c==3: fig.colorbar(sc,ax=ax,shrink=.57,pad=.02)
fig.suptitle('A4 spatial fields at 5% FSI-derived anchors; x marks show calibration nodes',fontsize=11.5)
fig.tight_layout(rect=[0,0,1,.96]); fig.savefig(OUT/'spatial_method_comparison_with_anchors.png',dpi=260,bbox_inches='tight'); plt.close(fig)


fig=plt.figure(figsize=(10.2,8.5))
for r,(t,label) in enumerate(targets):
    ref=truth[t].copy(); scale=1/1000 if t=='VM_cycle_max_Pa' else 1.
    preds=[pers[f'{t}_personalized_5pct'].values,bpred[f'{t}_IDW'].values,bpred[f'{t}_RBF'].values]
    errs=[np.abs(ref-p)*scale for p in preds]; hi=np.quantile(np.concatenate([e[mask] for e in errs]),.99)
    for c,(e,ttl) in enumerate(zip(errs,['Prior+adapt |error|','IDW |error|','RBF |error|'])):
        ax=fig.add_subplot(3,3,r*3+c+1,projection='3d'); sc=ax.scatter(xyz[mask,0],xyz[mask,1],xyz[mask,2],c=e[mask],s=2.0,vmin=0,vmax=hi,rasterized=True)
        ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([]);ax.view_init(18,-58);ax.set_title(ttl if r==0 else '',fontsize=8.8)
        if c==0: ax.text2D(-.18,.5,label,transform=ax.transAxes,rotation=90,va='center',fontsize=8.8,fontweight='bold')
        if c==2: fig.colorbar(sc,ax=ax,shrink=.57,pad=.02)
fig.suptitle('Absolute non-anchor reconstruction error at 5% anchors (matched row-wise error scales)',fontsize=11.5)
fig.tight_layout(rect=[0,0,1,.96]); fig.savefig(OUT/'spatial_error_maps.pdf',bbox_inches='tight'); plt.close(fig)


train_osi_iqr=np.quantile(train.OSI,.75)-np.quantile(train.OSI,.25)
osi_err=np.abs(h4.OSI.values-pers['OSI_personalized_5pct'].values)/(train_osi_iqr+1e-12)
oodv=ood['local_ood_percentile_median_pair'].values
fig=plt.figure(figsize=(11.3,4.2))
ax=fig.add_subplot(1,3,1,projection='3d'); sc=ax.scatter(xyz[mask,0],xyz[mask,1],xyz[mask,2],c=unc['OSI_width_over_trainIQR'].values[mask],s=3,rasterized=True); ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([]);ax.view_init(18,-58);ax.set_title('OSI empirical-band width / IQR',fontsize=9);fig.colorbar(sc,ax=ax,shrink=.63,pad=.03)
ax=fig.add_subplot(1,3,2,projection='3d'); sc=ax.scatter(xyz[mask,0],xyz[mask,1],xyz[mask,2],c=oodv[mask],s=3,rasterized=True); ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([]);ax.view_init(18,-58);ax.set_title('Local geometry-shift percentile',fontsize=9);fig.colorbar(sc,ax=ax,shrink=.63,pad=.03)
ax=fig.add_subplot(1,3,3); ax.scatter(oodv[mask],osi_err[mask],s=4,alpha=.16,rasterized=True)
bins=np.linspace(0,1,11); centers=(bins[:-1]+bins[1:])/2; meds=[]
for lo,hi in zip(bins[:-1],bins[1:]):
    q=mask&(oodv>=lo)&(oodv<(hi if hi<1 else hi+1e-9)); meds.append(np.median(osi_err[q]) if q.any() else np.nan)
ax.plot(centers,meds,marker='o',linewidth=1.4); ax.set_xlabel('Local geometry-shift percentile'); ax.set_ylabel('Normalized |OSI error|'); ax.set_title('Shift-error relation',fontsize=9); ax.grid(alpha=.2)
fig.tight_layout(); fig.savefig(OUT/'uncertainty_ood_with_error_relation.pdf',bbox_inches='tight'); plt.close(fig)


def pseudo_centerline(X,n_bins=24):
    X=np.asarray(X,float); cen=X.mean(0); Xc=X-cen; _,_,Vt=np.linalg.svd(Xc,full_matrices=False); main=Vt[0]; s0=Xc@main
    edges=np.quantile(s0,np.linspace(0,1,n_bins+1)); bi=np.searchsorted(edges[1:-1],s0,side='right'); C=[]; spos=[]
    for b in range(n_bins):
        m=bi==b
        if m.sum()<5: m=(s0>=edges[b])&(s0<=edges[b+1])
        C.append(X[m].mean(0)); spos.append(np.median(s0[m]))
    C=np.array(C)[np.argsort(spos)]; window=7
    Cs=np.column_stack([savgol_filter(C[:,k],window,2,mode='interp') for k in range(3)])
    return Cs
fig=plt.figure(figsize=(10.7,3.8))
for i,p in enumerate([1,2,3],1):
    d=train[train.patient==p]; X=d[['x_mm','y_mm','z_mm']].to_numpy(float); C=pseudo_centerline(X)
    ax=fig.add_subplot(1,3,i,projection='3d'); ids=np.linspace(0,len(X)-1,min(1800,len(X))).astype(int); ax.scatter(X[ids,0],X[ids,1],X[ids,2],s=1.2,alpha=.18,rasterized=True); ax.plot(C[:,0],C[:,1],C[:,2],linewidth=2.0); ax.set_title(f'A{i}'); ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([]);ax.view_init(18,-58)
fig.suptitle('Point-cloud pseudo-centerline used for geometry descriptors',fontsize=11.5); fig.tight_layout(rect=[0,0,1,.94]); fig.savefig(OUT/'pseudo_centerline_A1_A3.pdf',bbox_inches='tight'); plt.close(fig)
print('V9 figures generated')
