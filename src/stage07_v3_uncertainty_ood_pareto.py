from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

BASE = Path('/mnt/data')
V1 = BASE / 'DigitalTwin_V1'
V2 = BASE / 'DigitalTwin_V2_Personalized'
OUT = BASE / 'DigitalTwin_V3_Reconstructed'
OUT.mkdir(parents=True, exist_ok=True)

TARGETS = {
    'TAWSS_vector_Pa': 'log1p',
    'OSI': 'identity',
    'RRT_1_per_Pa': 'log1p',
    'peak_WSS_magnitude_Pa': 'log1p',
    'VM_cycle_max_Pa': 'log',
    'VM_temporal_mean_Pa': 'log',
}
LOCAL = [
    's_norm', 'dist_nearest_end', 'radial_norm',
    'local_radius_over_median', 'local_radius_gradient',
    'curvature_radius', 'curvature_side',
    'tangent_alignment_main_axis'
]
PRIMARY_FRAC = 0.05
OOD_K = 10


def tf(y, kind):
    y = np.asarray(y, float)
    if kind == 'identity':
        return y
    if kind == 'log1p':
        return np.log1p(np.maximum(y, 0))
    return np.log(np.maximum(y, 1e-12))


def inv(z, kind):
    z = np.asarray(z, float)
    if kind == 'identity':
        return z
    if kind == 'log1p':
        return np.expm1(z)
    return np.exp(z)


def empirical_percentile(reference, x):

    r = np.sort(np.asarray(reference, float))
    x = np.asarray(x, float)
    return np.searchsorted(r, x, side='right') / len(r)


def weighted_reference_values(train, col):

    vals = []
    n_min = min((train.patient == p).sum() for p in [1, 2, 3])
    rng = np.random.default_rng(20260821)
    for p in [1, 2, 3]:
        q = train.loc[train.patient == p, col].to_numpy(float)
        if len(q) > n_min:
            q = q[rng.choice(len(q), size=n_min, replace=False)]
        vals.append(q)
    return np.concatenate(vals)


def nondominated_mask(a, b):

    a = np.asarray(a, float)
    b = np.asarray(b, float)
    order = np.argsort(-a)
    front = np.zeros(len(a), dtype=bool)
    best_b = -np.inf
    for i in order:
        if b[i] > best_b:
            front[i] = True
            best_b = b[i]
    return front


def dominance_score(a, b):

    a = np.asarray(a, float)
    b = np.asarray(b, float)
    n = len(a)
    score = np.zeros(n)
    for i in range(n):
        score[i] = np.mean((a <= a[i]) & (b <= b[i]) & ((a < a[i]) | (b < b[i])))
    return score


def top10_overlap(y, p):
    k = max(1, int(round(0.1 * len(y))))
    A = set(np.argpartition(y, -k)[-k:])
    B = set(np.argpartition(p, -k)[-k:])
    return len(A & B) / k


def load_core():
    train = pd.read_csv(V1 / 'P123_Training_Table.csv')
    p4f = pd.read_csv(V1 / 'P4_Locked_Test_Features.csv')
    p4pred = pd.read_csv(V2 / 'P4_Personalized_Predictions.csv')
    dev = pd.read_csv(V2 / 'P123_Personalization_LOPO.csv')
    h4 = pd.read_csv(BASE / 'Patient4_VectorResolved_Hemodynamics.csv')
    s4 = pd.read_csv(BASE / 'Patient4_CycleResolved_SolidMechanics_v2.csv')
    for c in ['TAWSS_vector_Pa','OSI','RRT_1_per_Pa','peak_WSS_magnitude_Pa']:
        p4f[c] = h4[c].to_numpy(float)
    for c in ['VM_cycle_max_Pa','VM_temporal_mean_Pa']:
        p4f[c] = s4[c].to_numpy(float)
    return train, p4f, p4pred, dev


def reconstruct_anchor_mask(n, fraction, seed, X):

    from sklearn.cluster import MiniBatchKMeans
    k = max(12, int(round(n * fraction)))
    sc = StandardScaler().fit(X)
    Z = sc.transform(X)
    km = MiniBatchKMeans(
        n_clusters=k, random_state=seed, n_init=3,
        batch_size=1024, max_iter=100
    ).fit(Z)
    ids = sorted(set(int(np.argmin(((Z-c)**2).sum(1))) for c in km.cluster_centers_))
    mask = np.zeros(n, bool)
    mask[np.asarray(ids, int)] = True
    return mask


def uncertainty_stage(train, p4f, p4pred, dev):

    residual_file = BASE / 'DigitalTwin_V3_Multiphysics' / 'DEV_Personalized_Pointwise_Residuals.csv'
    if not residual_file.exists():
        raise FileNotFoundError('Need archived DEV_Personalized_Pointwise_Residuals.csv for exact V3 uncertainty replay.')
    rr = pd.read_csv(residual_file)
    out = p4f[['x_mm','y_mm','z_mm']].copy()
    rows = []
    for target, kind in TARGETS.items():
        q = rr[(rr.target == target) & (rr.calibration_fraction == PRIMARY_FRAC)].copy()
        per_patient = q.groupby('val_patient')['abs_residual_transformed'].quantile(0.90)
        radius = float(per_patient.max())
        pred = p4pred[f'{target}_personalized_5pct'].to_numpy(float)
        z = tf(pred, kind)
        lo = inv(z - radius, kind)
        hi = inv(z + radius, kind)
        truth = p4f[target].to_numpy(float)
        out[f'{target}_lo_emp90'] = lo
        out[f'{target}_hi_emp90'] = hi
        out[f'{target}_width'] = hi - lo
        coverage = np.mean((truth >= lo) & (truth <= hi))
        train_iqr = np.quantile(train[target], 0.75) - np.quantile(train[target], 0.25)
        width_norm = (hi-lo)/(train_iqr+1e-12)
        rows.append({
            'target': target,
            'radius_transformed': radius,
            'P4_coverage_all_nodes': float(coverage),
            'median_width_over_trainIQR': float(np.median(width_norm)),
            'p95_width_over_trainIQR': float(np.quantile(width_norm,0.95)),
        })
    out.to_csv(OUT/'P4_uncertainty_reconstructed.csv', index=False)
    pd.DataFrame(rows).to_csv(OUT/'P4_uncertainty_summary_reconstructed.csv', index=False)


def ood_stage(train, p4f):

    fold_percentiles = []
    fold_rows = []
    for heldout in [1,2,3]:
        ref = train[train.patient != heldout].reset_index(drop=True)
        val = train[train.patient == heldout].reset_index(drop=True)
        sc = StandardScaler().fit(ref[LOCAL])
        Zref = sc.transform(ref[LOCAL])
        Zval = sc.transform(val[LOCAL])
        Zp4 = sc.transform(p4f[LOCAL])
        nn = NearestNeighbors(n_neighbors=OOD_K).fit(Zref)
        dval = nn.kneighbors(Zval, return_distance=True)[0].mean(1)
        dp4 = nn.kneighbors(Zp4, return_distance=True)[0].mean(1)
        pct = empirical_percentile(dval, dp4)
        fold_percentiles.append(pct)
        fold_rows.append({
            'heldout_development_anatomy': heldout,
            'heldout_distance_median': float(np.median(dval)),
            'heldout_distance_p95': float(np.quantile(dval,0.95)),
            'P4_distance_median': float(np.median(dp4)),
        })
    P = np.vstack(fold_percentiles)
    score = np.median(P, axis=0)
    out = p4f[['x_mm','y_mm','z_mm']].copy()
    for i in range(3):
        out[f'fold{i+1}_ood_percentile'] = P[i]
    out['local_ood_percentile_median_pair'] = score
    out.to_csv(OUT/'P4_Geometry_OOD_Map_reconstructed.csv', index=False)
    pd.DataFrame(fold_rows).to_csv(OUT/'DEV_LOPO_OOD_Distance_Summary_reconstructed.csv', index=False)
    pd.DataFrame([{
        'n_points': len(score),
        'median_local_OOD_percentile': np.median(score),
        'p90_local_OOD_percentile': np.quantile(score,0.90),
        'p95_local_OOD_percentile': np.quantile(score,0.95),
        'fraction_local_OOD95': np.mean(score >= 0.95),
        'fraction_local_OOD99': np.mean(score >= 0.99),
    }]).to_csv(OUT/'P4_OOD_Summary_reconstructed.csv', index=False)
    return score


def global_envelope(train, p4f):
    global_cols = [
        'centerline_length_mm','mean_radius_over_length','max_radius_over_length',
        'global_expansion_ratio','end_radius_ratio','tortuosity',
        'mean_curvature_times_length','max_curvature_times_length',
        'bbox_ratio_2_1','bbox_ratio_3_1'
    ]
    rows=[]
    for c in global_cols:
        dev_vals = train.groupby('patient')[c].first().to_numpy(float)
        p4v = float(p4f[c].iloc[0])
        rows.append({
            'feature': c,
            'dev_min': dev_vals.min(), 'dev_max': dev_vals.max(),
            'P4': p4v,
            'outside_dev_minmax': bool((p4v < dev_vals.min()) or (p4v > dev_vals.max()))
        })
    pd.DataFrame(rows).to_csv(OUT/'P4_Global_Anatomy_Envelope_reconstructed.csv', index=False)


def pareto_stage(train, p4f, p4pred):

    channels = {
        'high_shear': ('peak_WSS_magnitude_Pa', 'VM_cycle_max_Pa'),
        'residence_oscillation': ('RRT_1_per_Pa', 'VM_cycle_max_Pa')
    }
    rows=[]
    for frac_tag in ['5pct','10pct']:
        for cname,(hemo,mech) in channels.items():
            ref_h = weighted_reference_values(train, hemo)
            ref_m = weighted_reference_values(train, mech)
            h_true = p4f[hemo].to_numpy(float)
            m_true = p4f[mech].to_numpy(float)
            h_pred = p4pred[f'{hemo}_personalized_{frac_tag}'].to_numpy(float)
            m_pred = p4pred[f'{mech}_personalized_{frac_tag}'].to_numpy(float)

            hp_t = empirical_percentile(ref_h, h_true)
            mp_t = empirical_percentile(ref_m, m_true)
            hp_p = empirical_percentile(ref_h, h_pred)
            mp_p = empirical_percentile(ref_m, m_pred)
            cob_t = np.minimum(hp_t, mp_t)
            cob_p = np.minimum(hp_p, mp_p)
            front_t = nondominated_mask(hp_t, mp_t)
            front_p = nondominated_mask(hp_p, mp_p)
            dom_t = dominance_score(hp_t, mp_t)
            dom_p = dominance_score(hp_p, mp_p)

            table = p4f[['x_mm','y_mm','z_mm']].copy()
            table['hemo_percentile_ref'] = hp_t
            table['mech_percentile_ref'] = mp_t
            table['hemo_percentile_pred'] = hp_p
            table['mech_percentile_pred'] = mp_p
            table['co_burden_ref'] = cob_t
            table['co_burden_pred'] = cob_p
            table['pareto_front_ref'] = front_t
            table['pareto_front_pred'] = front_p
            table['dominance_ref'] = dom_t
            table['dominance_pred'] = dom_p
            table.to_csv(OUT/f'P4_Pareto_{cname}_{frac_tag}_reconstructed.csv', index=False)

            union = np.sum(front_t | front_p)
            jaccard = np.sum(front_t & front_p)/union if union else np.nan
            rows.append({
                'fraction': frac_tag,
                'channel': cname,
                'co_burden_Spearman': spearmanr(cob_t,cob_p).statistic,
                'co_burden_top10_overlap': top10_overlap(cob_t,cob_p),
                'dominance_score_Spearman': spearmanr(dom_t,dom_p).statistic,
                'dominance_score_MAE': np.mean(np.abs(dom_t-dom_p)),
                'dominance_score_top10_overlap': top10_overlap(dom_t,dom_p),
                'pareto_front_Jaccard': jaccard,
            })
    pd.DataFrame(rows).to_csv(OUT/'P4_Pareto_Agreement_Summary_reconstructed.csv', index=False)


def main():
    train,p4f,p4pred,dev = load_core()
    uncertainty_stage(train,p4f,p4pred,dev)
    ood_stage(train,p4f)
    global_envelope(train,p4f)
    pareto_stage(train,p4f,p4pred)
    print('Reconstructed V3 outputs written to', OUT)


if __name__ == '__main__':
    main()
