# File-by-File Spreadsheet Guide

This document describes every included project spreadsheet in English. The numeric CSV files themselves are preserved unchanged; this guide explains how each table fits into the computational workflow.

## 01_Core_FSI_Processed

### 1. `Patient1_VectorResolved_Hemodynamics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A1
- **Dimensions:** 8191 rows × 12 columns
- **Size:** 1.7114 MB
- **Produced by:** COMSOL export + Python WSS post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_m, y_m, z_m, TAWSS_vector_Pa, OSI, RRT_1_per_Pa, mean_WSSx_Pa, mean_WSSy_Pa, mean_WSSz_Pa, mean_WSS_vector_magnitude_Pa, peak_WSS_magnitude_Pa, t_peak_WSS_s
- **Description:** Processed vector-resolved hemodynamic output for anatomy A1, containing inner-wall coordinates and the canonical TAWSS, OSI, RRT, mean WSS-vector, peak WSS, and peak-time fields used downstream.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient1_VectorResolved_Hemodynamics.csv`
- **Original path:** `/mnt/data/Patient1_VectorResolved_Hemodynamics.csv`
- **SHA-256:** `de96441ab19ac1a8a0c8530f940dd6b47033bc9fbe6072077d8e9de2f23cd23f`

### 2. `Patient1_CycleResolved_SolidMechanics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A1
- **Dimensions:** 8191 rows × 10 columns
- **Size:** 1.3871 MB
- **Produced by:** COMSOL export + Python mechanics post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_m, y_m, z_m, VM_cycle_max_Pa, VM_cycle_min_Pa, VM_stress_range_Pa, VM_stress_amplitude_Pa, VM_midrange_stress_Pa, VM_temporal_mean_Pa, t_VM_max_s
- **Description:** Processed solid-mechanics output for anatomy A1, containing saved-state/cycle-resolved von Mises stress maximum, minimum, range, amplitude, midrange, temporal mean, and time of maximum.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient1_CycleResolved_SolidMechanics.csv`
- **Original path:** `/mnt/data/Patient1_CycleResolved_SolidMechanics.csv`
- **SHA-256:** `a5bc7f5f4564492688635701d4fda0057bbf321804c059613a936b1c7148cdbd`

### 3. `Patient2_VectorResolved_Hemodynamics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A2
- **Dimensions:** 6800 rows × 12 columns
- **Size:** 1.4279 MB
- **Produced by:** COMSOL export + Python WSS post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_m, y_m, z_m, TAWSS_vector_Pa, OSI, RRT_1_per_Pa, mean_WSSx_Pa, mean_WSSy_Pa, mean_WSSz_Pa, mean_WSS_vector_magnitude_Pa, peak_WSS_magnitude_Pa, t_peak_WSS_s
- **Description:** Processed vector-resolved hemodynamic output for anatomy A2, containing inner-wall coordinates and the canonical TAWSS, OSI, RRT, mean WSS-vector, peak WSS, and peak-time fields used downstream.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient2_VectorResolved_Hemodynamics.csv`
- **Original path:** `/mnt/data/Patient2_VectorResolved_Hemodynamics.csv`
- **SHA-256:** `ef32c176cc569d5fd3e2ecb4a1b1e8cf417e695d7ee5fb84d7d2a165f897aa15`

### 4. `Patient2_CycleResolved_SolidMechanics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A2
- **Dimensions:** 6800 rows × 10 columns
- **Size:** 1.1589 MB
- **Produced by:** COMSOL export + Python mechanics post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_m, y_m, z_m, VM_cycle_max_Pa, VM_cycle_min_Pa, VM_stress_range_Pa, VM_stress_amplitude_Pa, VM_midrange_stress_Pa, VM_temporal_mean_Pa, t_VM_max_s
- **Description:** Processed solid-mechanics output for anatomy A2, containing saved-state/cycle-resolved von Mises stress maximum, minimum, range, amplitude, midrange, temporal mean, and time of maximum.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient2_CycleResolved_SolidMechanics.csv`
- **Original path:** `/mnt/data/Patient2_CycleResolved_SolidMechanics.csv`
- **SHA-256:** `f74ea371ca8a24e15e1f94c63213a0020f4212b2d139177badf9494ea00b7c4e`

### 5. `Patient3_VectorResolved_Hemodynamics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A3
- **Dimensions:** 3203 rows × 12 columns
- **Size:** 0.6457 MB
- **Produced by:** COMSOL export + Python WSS post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa, OSI, RRT_1_per_Pa, mean_WSSx_Pa, mean_WSSy_Pa, mean_WSSz_Pa, mean_WSS_vector_magnitude_Pa, peak_WSS_magnitude_Pa, t_peak_WSS_s
- **Description:** Processed vector-resolved hemodynamic output for anatomy A3, containing inner-wall coordinates and the canonical TAWSS, OSI, RRT, mean WSS-vector, peak WSS, and peak-time fields used downstream.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient3_VectorResolved_Hemodynamics.csv`
- **Original path:** `/mnt/data/Patient3_VectorResolved_Hemodynamics.csv`
- **SHA-256:** `f149306b97eae7ebbc373df3c6e15d6e0fb4b3ddc4101e9347892e626b37aece`

### 6. `Patient3_CycleResolved_SolidMechanics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A3
- **Dimensions:** 3203 rows × 10 columns
- **Size:** 0.534 MB
- **Produced by:** COMSOL export + Python mechanics post-processing
- **Used by:** V1 feature/target table, V2/V3 analyses
- **Key columns:** x_mm, y_mm, z_mm, VM_cycle_max_Pa, VM_cycle_min_Pa, VM_stress_range_Pa, VM_stress_amplitude_Pa, VM_midrange_stress_Pa, VM_temporal_mean_Pa, t_VM_max_s
- **Description:** Processed solid-mechanics output for anatomy A3, containing saved-state/cycle-resolved von Mises stress maximum, minimum, range, amplitude, midrange, temporal mean, and time of maximum.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient3_CycleResolved_SolidMechanics.csv`
- **Original path:** `/mnt/data/Patient3_CycleResolved_SolidMechanics.csv`
- **SHA-256:** `7d5e2b60cf7385679503d94921a14bb700b30f07ece7dc297173a1388a44fcea`

### 7. `Patient4_VectorResolved_Hemodynamics.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A4
- **Dimensions:** 4055 rows × 12 columns
- **Size:** 0.832 MB
- **Produced by:** COMSOL export + Python WSS post-processing
- **Used by:** V1/V2/V3, reviewer analyses
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa, OSI, RRT_1_per_Pa, mean_WSSx_Pa, mean_WSSy_Pa, mean_WSSz_Pa, mean_WSS_vector_magnitude_Pa, peak_WSS_magnitude_Pa, t_peak_WSS_s
- **Description:** Processed vector-resolved hemodynamic output for anatomy A4. This is the canonical FSI target source for A4 zero-shot evaluation, sparse personalization, baseline interpolation, and diagnostic analyses.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient4_VectorResolved_Hemodynamics.csv`
- **Original path:** `/mnt/data/Patient4_VectorResolved_Hemodynamics.csv`
- **SHA-256:** `7d0ccd9a155961960870a06561a6e911106c414388fa14216c75a12f1a9ec7fd`

### 8. `Patient4_CycleResolved_SolidMechanics_v2.csv`
- **Stage:** FSI post-processing
- **Status:** Current/Canonical
- **Criticality:** Core input
- **Scope:** A4
- **Dimensions:** 4055 rows × 10 columns
- **Size:** 0.6797 MB
- **Produced by:** Corrected COMSOL/CSV export + Python mechanics post-processing
- **Used by:** V1/V2/V3, reviewer analyses
- **Key columns:** x_mm, y_mm, z_mm, VM_cycle_max_Pa, VM_cycle_min_Pa, VM_stress_range_Pa, VM_stress_amplitude_Pa, VM_midrange_stress_Pa, VM_temporal_mean_Pa, t_VM_max_s
- **Description:** Corrected and canonical solid-mechanics output for anatomy A4, with exact 4,055-node correspondence to the A4 hemodynamic table. This is the valid mechanics source used by the final modeling pipeline.
- **Package path:** `spreadsheets_original_csv/01_Core_FSI_Processed/Patient4_CycleResolved_SolidMechanics_v2.csv`
- **Original path:** `/mnt/data/Patient4_CycleResolved_SolidMechanics_v2.csv`
- **SHA-256:** `896544d3f15738c77f9230d704ba0f0dcc6a62e6be270984a60f526056d7d3da`
- **Notes:** The v2 file is the valid canonical A4 mechanics table. The older Patient4_CycleResolved_SolidMechanics.csv was intentionally excluded because it was superseded/invalid.

## 02_FSI_Raw_and_Audits

### 9. `Patient1_VM_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A1
- **Dimensions:** 8199 rows × 2 columns
- **Size:** 3.5268 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_1_Carreau_MR_Final(3.mph
- **Description:** A1 raw VM time series used to derive cycle-resolved mechanics.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient1_VM_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient1_VM_Raw_TimeSeries.csv`
- **SHA-256:** `ef2c2c711fd08fe5879370e15aad0d64e7a71f81487aa81ed7cbc6dad9999d7e`

### 10. `Patient1_VM_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A1
- **Dimensions:** 21 rows × 5 columns
- **Size:** 0.0017 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_VM_Pa, spatial_median_VM_Pa, spatial_p95_VM_Pa, spatial_max_VM_Pa
- **Description:** A1 timewise audit of VM-derived quantities.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient1_VM_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient1_VM_Timewise_Audit.csv`
- **SHA-256:** `00a39aef59a90ac3232b739e47be8f39a792de07578bee3e1748bdf186cb84ce`

### 11. `Patient1_WSS_Native_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A1
- **Dimensions:** 8199 rows × 2 columns
- **Size:** 10.5526 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_1_Carreau_MR_Final(3.mph
- **Description:** A1 native COMSOL WSS time series used as the trusted hemodynamic source/validation reference.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient1_WSS_Native_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient1_WSS_Native_TimeSeries.csv`
- **SHA-256:** `0c02314c102d2af5913f6841998b91caebfa9cf41489dd6fd57f23cd7d31d40d`

### 12. `Patient1_WSS_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A1
- **Dimensions:** 21 rows × 5 columns
- **Size:** 0.0017 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_WSS_Pa, spatial_median_WSS_Pa, spatial_p95_WSS_Pa, spatial_max_WSS_Pa
- **Description:** A1 timewise WSS audit.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient1_WSS_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient1_WSS_Timewise_Audit.csv`
- **SHA-256:** `bd0a8c2bbf7c315df6746c10e7a734339b34d38f7e433d47f950026c9f0a2cf4`

### 13. `Patient2_VM_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A2
- **Dimensions:** 6808 rows × 2 columns
- **Size:** 2.9407 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_2_Saccular(4).mph
- **Description:** A2 raw VM time series used for mechanics post-processing.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient2_VM_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient2_VM_Raw_TimeSeries.csv`
- **SHA-256:** `c0bdca8297bdd280aa7461f8d8f298e2605a0ab9d80ffe7116cbefafb93efd43`

### 14. `Patient2_VM_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A2
- **Dimensions:** 21 rows × 5 columns
- **Size:** 0.0017 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_VM_Pa, spatial_median_VM_Pa, spatial_p95_VM_Pa, spatial_max_VM_Pa
- **Description:** A2 timewise VM audit.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient2_VM_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient2_VM_Timewise_Audit.csv`
- **SHA-256:** `f43e2edd0c5c67041d245cd4124a54de033fcc531829e366f289564238143fb5`

### 15. `Patient2_WSS_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A2
- **Dimensions:** 6808 rows × 2 columns
- **Size:** 34.8757 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_2_Saccular(4).mph
- **Description:** A2 raw gradient-based WSS reconstruction time series.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient2_WSS_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient2_WSS_Raw_TimeSeries.csv`
- **SHA-256:** `9f118bc7a2304a1fe826be02375d2dde7e1c754eeeb011fd5400470a394434a2`

### 16. `Patient2_TAWSS_Carreau.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A2
- **Dimensions:** 6808 rows × 2 columns
- **Size:** 0.8096 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_2_Saccular(4).mph
- **Description:** A2 Carreau-model TAWSS intermediate/verification table.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient2_TAWSS_Carreau.csv`
- **Original path:** `/mnt/data/Patient2_TAWSS_Carreau.csv`
- **SHA-256:** `7a26e9f81b71054be1bf2e67b52ed1881cbfea4b8ebecc9ac5803a2ffd4d92ac`

### 17. `Patient3_VM_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 3211 rows × 2 columns
- **Size:** 1.3649 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_3_Carreau_Final.mph
- **Description:** A3 raw VM time series.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_VM_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient3_VM_Raw_TimeSeries.csv`
- **SHA-256:** `8fba819f7ff6a4e9f245ae425331f7b8930ad9435121f0c96cb72a497fb24fd7`

### 18. `Patient3_VM_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 21 rows × 6 columns
- **Size:** 0.002 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_VM_Pa, spatial_median_VM_Pa, spatial_p95_VM_Pa, spatial_p99_VM_Pa, spatial_max_VM_Pa
- **Description:** A3 timewise VM audit.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_VM_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient3_VM_Timewise_Audit.csv`
- **SHA-256:** `d4305b647698ab52cd00e4c4106a8af57a8316d5aec012001ebc15552d4c1600`

### 19. `Patient3_WSS_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 3211 rows × 2 columns
- **Size:** 16.4564 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_3_Carreau_Final.mph
- **Description:** A3 raw gradient-based WSS time series.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_WSS_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient3_WSS_Raw_TimeSeries.csv`
- **SHA-256:** `ad47d651f962510517765f4a68ed26f290d92fa5b799b6f71d9bdc74b7b30f24`

### 20. `Patient3_WSS_Native_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 3211 rows × 2 columns
- **Size:** 4.1014 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_3_Carreau_Final.mph
- **Description:** A3 native COMSOL WSS time series for reconstruction agreement validation.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_WSS_Native_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient3_WSS_Native_TimeSeries.csv`
- **SHA-256:** `7cec6b0320a32b97252f13e47d83825418d64598fef9a46a1bf6c91c7bef4991`

### 21. `Patient3_WSS_MethodValidation.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 3203 rows × 12 columns
- **Size:** 0.7209 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_native_Pa, TAWSS_gradient_Pa, TAWSS_abs_diff_Pa, OSI_native, OSI_gradient, OSI_abs_diff, RRT_native_1_per_Pa, RRT_gradient_1_per_Pa, RRT_abs_diff_1_per_Pa
- **Description:** A3 pointwise native-vs-reconstructed WSS validation.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_WSS_MethodValidation.csv`
- **Original path:** `/mnt/data/Patient3_WSS_MethodValidation.csv`
- **SHA-256:** `13a623d2f9290964b30f88a04354d41a0d0a7d546b1bd747ccaf05d5d2b1df28`

### 22. `Patient3_WSS_MethodValidation_Timewise.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 21 rows × 7 columns
- **Size:** 0.0025 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, native_mean_WSS_Pa, gradient_mean_WSS_Pa, native_p95_WSS_Pa, gradient_p95_WSS_Pa, native_max_WSS_Pa, gradient_max_WSS_Pa
- **Description:** A3 timewise summary of native-vs-reconstructed WSS agreement.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_WSS_MethodValidation_Timewise.csv`
- **Original path:** `/mnt/data/Patient3_WSS_MethodValidation_Timewise.csv`
- **SHA-256:** `dc81bab671821c3770fb65cd8e1c09697c77e6e099e8ce7b597e1bbc777f0e45`

### 23. `Patient3_WSS_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A3
- **Dimensions:** 21 rows × 7 columns
- **Size:** 0.0026 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_WSS_Pa, spatial_median_WSS_Pa, spatial_p95_WSS_Pa, spatial_max_WSS_Pa, spatial_mean_mu_app_Pa_s, spatial_median_mu_app_Pa_s
- **Description:** A3 temporal WSS audit.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient3_WSS_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient3_WSS_Timewise_Audit.csv`
- **SHA-256:** `7581c9c690f35108f142e1a919b9f473d4910e58f3fd1a95625daa2bc1b5c404`

### 24. `Patient4_VM_Raw_TimeSeries(1).csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 4063 rows × 2 columns
- **Size:** 1.7321 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_4_Carreau_Main_Final.mph
- **Description:** Corrected A4 raw VM time series corresponding to 4055 inner-wall nodes.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_VM_Raw_TimeSeries(1).csv`
- **Original path:** `/mnt/data/Patient4_VM_Raw_TimeSeries(1).csv`
- **SHA-256:** `5e184d3f01fc101a2906ff99e0ed5bcf01d1fe19be77fe1efa9aacb9ce5dc483`

### 25. `Patient4_VM_Timewise_Audit_v2.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 21 rows × 6 columns
- **Size:** 0.002 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_VM_Pa, spatial_median_VM_Pa, spatial_p95_VM_Pa, spatial_p99_VM_Pa, spatial_max_VM_Pa
- **Description:** A4 VM timewise audit based on corrected export.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_VM_Timewise_Audit_v2.csv`
- **Original path:** `/mnt/data/Patient4_VM_Timewise_Audit_v2.csv`
- **SHA-256:** `0e560f10750654ddd0beec68e3546dc9397bf7193809a41ffcbbb763f48b3fc9`

### 26. `Patient4_WSS_Raw_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 4063 rows × 2 columns
- **Size:** 20.7035 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_4_Carreau_Main_Final.mph
- **Description:** A4 raw gradient-based WSS time series.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_WSS_Raw_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient4_WSS_Raw_TimeSeries.csv`
- **SHA-256:** `472b5b0915e5c82ef3529256291de517d031cfbb46d21c9bc8ec726f26d06192`

### 27. `Patient4_WSS_Native_TimeSeries.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 4063 rows × 2 columns
- **Size:** 5.1738 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** % Model, Patient_4_Carreau_Main_Final.mph
- **Description:** A4 native COMSOL WSS time series for method validation.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_WSS_Native_TimeSeries.csv`
- **Original path:** `/mnt/data/Patient4_WSS_Native_TimeSeries.csv`
- **SHA-256:** `ea82297bba8ce7f047f4a0e4fb41f89ebd0d549230b3c153d55e1d5a87a6d45e`

### 28. `Patient4_WSS_MethodValidation.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 4055 rows × 12 columns
- **Size:** 0.9196 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_native_Pa, TAWSS_gradient_Pa, TAWSS_abs_diff_Pa, OSI_native, OSI_gradient, OSI_abs_diff, RRT_native_1_per_Pa, RRT_gradient_1_per_Pa, RRT_abs_diff_1_per_Pa
- **Description:** A4 pointwise native-vs-reconstructed WSS validation.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_WSS_MethodValidation.csv`
- **Original path:** `/mnt/data/Patient4_WSS_MethodValidation.csv`
- **SHA-256:** `7a46fa11fbdd26848f4546d8c85d83bc6f533895c4c7aceadab82010bd352b6e`

### 29. `Patient4_WSS_MethodValidation_Timewise.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 21 rows × 7 columns
- **Size:** 0.0025 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, native_mean_WSS_Pa, gradient_mean_WSS_Pa, native_p95_WSS_Pa, gradient_p95_WSS_Pa, native_max_WSS_Pa, gradient_max_WSS_Pa
- **Description:** A4 timewise native-vs-reconstructed WSS agreement summary.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_WSS_MethodValidation_Timewise.csv`
- **Original path:** `/mnt/data/Patient4_WSS_MethodValidation_Timewise.csv`
- **SHA-256:** `99f2942a173c8a0cad26bf239aed16ae186313f9197096a1d69bd5c91978a177`

### 30. `Patient4_WSS_Timewise_Audit.csv`
- **Stage:** FSI verification/post-processing audit
- **Status:** Validation/Audit
- **Criticality:** Validation/audit
- **Scope:** A4
- **Dimensions:** 21 rows × 7 columns
- **Size:** 0.0025 MB
- **Produced by:** COMSOL exports and validation scripts
- **Used by:** FSI target construction / method validation / manuscript numerical audit
- **Key columns:** t_s, spatial_mean_WSS_Pa, spatial_median_WSS_Pa, spatial_p95_WSS_Pa, spatial_max_WSS_Pa, spatial_mean_mu_app_Pa_s, spatial_median_mu_app_Pa_s
- **Description:** A4 temporal WSS audit.
- **Package path:** `spreadsheets_original_csv/02_FSI_Raw_and_Audits/Patient4_WSS_Timewise_Audit.csv`
- **Original path:** `/mnt/data/Patient4_WSS_Timewise_Audit.csv`
- **SHA-256:** `bc691da72a2bb1009fd8c3c43d0bf1518e33f98283200f667183c72d4ce90464`

## 03_DigitalTwin_V1

### 31. `P123_Training_Table.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A1–A3 development
- **Dimensions:** 18194 rows × 32 columns
- **Size:** 10.1401 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** x_mm, y_mm, z_mm, s_norm, dist_nearest_end, radial_norm, local_radius_over_length, local_radius_over_median, local_radius_over_large_end, local_radius_gradient, curvature_1_per_mm, curvature_radius, curvature_side, tangent_alignment_main_axis, centerline_length_mm, mean_radius_over_length, max_radius_over_length, global_expansion_ratio ...
- **Description:** Primary development table containing 18,194 A1–A3 inner-wall nodes, coordinates, 21 geometry-derived features, anatomy identifiers, and FSI targets. It is the main input for LightGBM development and anatomy-level LOAO analysis.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/P123_Training_Table.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/P123_Training_Table.csv`
- **SHA-256:** `cc91017f0c78af23fecaf54d020926d43df13f95bec421a8bdcdb44a2972a070`

### 32. `P4_Locked_Test_Features.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A4
- **Dimensions:** 4055 rows × 25 columns
- **Size:** 1.7607 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** x_mm, y_mm, z_mm, patient, s_norm, dist_nearest_end, radial_norm, local_radius_over_length, local_radius_over_median, local_radius_over_large_end, local_radius_gradient, curvature_1_per_mm, curvature_radius, curvature_side, tangent_alignment_main_axis, centerline_length_mm, mean_radius_over_length, max_radius_over_length ...
- **Description:** A4 geometry-only feature table with target columns excluded from model input. It is the geometry input used for target-excluded zero-shot inference on the separate anatomy.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/P4_Locked_Test_Features.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/P4_Locked_Test_Features.csv`
- **SHA-256:** `3bb2e58149ff30ae3dda3f8a0d665f5b8bd276e675a2f4a2e6fb2e14656532c6`
- **Notes:** In manuscript V10, the corrected selected-tree-count analysis is primary; historical 450-tree outputs are retained only as a sensitivity/reproducibility audit.
- **Duplicate IDs:** 72

### 33. `LOPO_CV_AllCandidates.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** Project-wide
- **Dimensions:** 63 rows × 9 columns
- **Size:** 0.0084 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** target, candidate, val_patient, R2, MAE, RMSE, Spearman, Top10_overlap, NMAE
- **Description:** Complete development-only LightGBM candidate-evaluation results for every target and leave-one-anatomy-out fold.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/LOPO_CV_AllCandidates.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/LOPO_CV_AllCandidates.csv`
- **SHA-256:** `a8a8acdbee2f5fd171c817c876e23f232f8493b86be21648249831b463b88a05`

### 34. `LOPO_SelectedModels.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 7 columns
- **Size:** 0.0009 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** target, selected_model, mean_R2, mean_MAE, mean_Spearman, mean_Top10_overlap, mean_NMAE
- **Description:** Summary of the target-specific LightGBM candidate selected from development-only LOAO metrics.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/LOPO_SelectedModels.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/LOPO_SelectedModels.csv`
- **SHA-256:** `f3d85c1cd4914f298fca98938485461b769a6c00115838bf7bccfba54a6bae53`

### 35. `LOPO_OOF_Predictions.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** Project-wide
- **Dimensions:** 29786 rows × 18 columns
- **Size:** 8.9444 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** patient, x_mm, y_mm, z_mm, TAWSS_vector_Pa_truth, TAWSS_vector_Pa_pred, OSI_truth, OSI_pred, RRT_1_per_Pa_truth, RRT_1_per_Pa_pred, peak_WSS_magnitude_Pa_truth, peak_WSS_magnitude_Pa_pred, VM_cycle_max_Pa_truth, VM_cycle_max_Pa_pred, VM_stress_amplitude_Pa_truth, VM_stress_amplitude_Pa_pred, VM_temporal_mean_Pa_truth, VM_temporal_mean_Pa_pred
- **Description:** Selected out-of-fold predictions for A1–A3, used for development diagnostics, residual analysis, and later calibration-related audits.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/LOPO_OOF_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/LOPO_OOF_Predictions.csv`
- **SHA-256:** `9ba814ce3391fd24e7788842f4efeeac52edd76055ea1e5cf35611e8d771c1e2`

### 36. `P4_DigitalTwin_Predictions.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A4
- **Dimensions:** 4055 rows × 24 columns
- **Size:** 1.757 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_pred, TAWSS_vector_Pa_lo90, TAWSS_vector_Pa_hi90, OSI_pred, OSI_lo90, OSI_hi90, RRT_1_per_Pa_pred, RRT_1_per_Pa_lo90, RRT_1_per_Pa_hi90, peak_WSS_magnitude_Pa_pred, peak_WSS_magnitude_Pa_lo90, peak_WSS_magnitude_Pa_hi90, VM_cycle_max_Pa_pred, VM_cycle_max_Pa_lo90, VM_cycle_max_Pa_hi90 ...
- **Description:** Historical V1 zero-shot A4 predictions, including the V1 prediction fields and historical residual-band bounds. Retained for reproducibility and sensitivity auditing.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/P4_DigitalTwin_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/P4_DigitalTwin_Predictions.csv`
- **SHA-256:** `fb754e498d04148ae313959d7660e945e00e77caeab24d4e10c10f757df280c4`
- **Notes:** In manuscript V10, the corrected selected-tree-count analysis is primary; historical 450-tree outputs are retained only as a sensitivity/reproducibility audit.

### 37. `P4_LOCKED_TEST_METRICS.csv`
- **Stage:** V1 cross-anatomy prior
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A4
- **Dimensions:** 7 rows × 7 columns
- **Size:** 0.001 MB
- **Produced by:** 01_digital_twin_v1_original.py
- **Used by:** V1 reporting; V2 personalization; V3/reviewer analyses
- **Key columns:** R2, MAE, RMSE, Spearman, Top10_overlap, Interval90_coverage, target
- **Description:** Historical V1 A4 zero-shot performance metrics. Retained to document the original locked-test run and compare it with the corrected final-refit analysis.
- **Package path:** `spreadsheets_original_csv/03_DigitalTwin_V1/P4_LOCKED_TEST_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_V1/P4_LOCKED_TEST_METRICS.csv`
- **SHA-256:** `29a3b94bfb874490dc3db1bd9a302c7240eb596e5a3c94183c02ab20d54c7e73`
- **Notes:** In manuscript V10, the corrected selected-tree-count analysis is primary; historical 450-tree outputs are retained only as a sensitivity/reproducibility audit.

## 04_DigitalTwin_V2

### 38. `P123_Personalization_LOPO.csv`
- **Stage:** V2 sparse personalization
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A1–A3 development
- **Dimensions:** 84 rows × 9 columns
- **Size:** 0.0098 MB
- **Produced by:** 02_digital_twin_v2_personalized_original.py
- **Used by:** V2 report; V3; reviewer baselines; figures
- **Key columns:** val_patient, target, calibration_fraction, n_calibration, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** Detailed A1–A3 LOAO sparse-personalization results for every target and calibration fraction (1%, 2%, 5%, and 10%), evaluated on non-anchor nodes.
- **Package path:** `spreadsheets_original_csv/04_DigitalTwin_V2/P123_Personalization_LOPO.csv`
- **Original path:** `/mnt/data/DigitalTwin_V2_Personalized/P123_Personalization_LOPO.csv`
- **SHA-256:** `62c878f83f0d0ac7b343c0bf85253a38af0eb2424a8338097eedf8ce75c9901d`

### 39. `P123_Personalization_Summary.csv`
- **Stage:** V2 sparse personalization
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A1–A3 development
- **Dimensions:** 28 rows × 6 columns
- **Size:** 0.0027 MB
- **Produced by:** 02_digital_twin_v2_personalized_original.py
- **Used by:** V2 report; V3; reviewer baselines; figures
- **Key columns:** target, calibration_fraction, mean_R2, mean_MAE, mean_Spearman, mean_Top10_overlap
- **Description:** Development-level average personalization metrics summarized by target and calibration fraction.
- **Package path:** `spreadsheets_original_csv/04_DigitalTwin_V2/P123_Personalization_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_V2_Personalized/P123_Personalization_Summary.csv`
- **SHA-256:** `5b4fd4830b959fb796571e40572ff65974070be7673d28da36628c688f66bd65`

### 40. `P4_PERSONALIZED_TEST_METRICS.csv`
- **Stage:** V2 sparse personalization
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A4
- **Dimensions:** 28 rows × 9 columns
- **Size:** 0.0034 MB
- **Produced by:** 02_digital_twin_v2_personalized_original.py
- **Used by:** V2 report; V3; reviewer baselines; figures
- **Key columns:** target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** A4 sparse-personalization performance metrics on non-anchor nodes for each target and each calibration fraction.
- **Package path:** `spreadsheets_original_csv/04_DigitalTwin_V2/P4_PERSONALIZED_TEST_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_V2_Personalized/P4_PERSONALIZED_TEST_METRICS.csv`
- **SHA-256:** `f7939cc5ada54563709032e20e61362bee81557c0886792500087abfbe36ddc2`

### 41. `P4_Personalized_Predictions.csv`
- **Stage:** V2 sparse personalization
- **Status:** Current/Canonical
- **Criticality:** Core model output
- **Scope:** A4
- **Dimensions:** 4055 rows × 31 columns
- **Size:** 2.2417 MB
- **Produced by:** 02_digital_twin_v2_personalized_original.py
- **Used by:** V2 report; V3; reviewer baselines; figures
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_personalized_1pct, TAWSS_vector_Pa_personalized_2pct, TAWSS_vector_Pa_personalized_5pct, TAWSS_vector_Pa_personalized_10pct, OSI_personalized_1pct, OSI_personalized_2pct, OSI_personalized_5pct, OSI_personalized_10pct, RRT_1_per_Pa_personalized_1pct, RRT_1_per_Pa_personalized_2pct, RRT_1_per_Pa_personalized_5pct, RRT_1_per_Pa_personalized_10pct, peak_WSS_magnitude_Pa_personalized_1pct, peak_WSS_magnitude_Pa_personalized_2pct, peak_WSS_magnitude_Pa_personalized_5pct ...
- **Description:** Pointwise A4 personalized predictions for 1%, 2%, 5%, and 10% sparse calibration fractions.
- **Package path:** `spreadsheets_original_csv/04_DigitalTwin_V2/P4_Personalized_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_V2_Personalized/P4_Personalized_Predictions.csv`
- **SHA-256:** `fec43639423d88420d7047ae6236a21bf3821a4732d0ad5376e1798c0de4fbbc`

## 05_DigitalTwin_V3

### 42. `DEV_Calibration_Curve_Aggregate.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A1–A3 development
- **Dimensions:** 4 rows × 4 columns
- **Size:** 0.0003 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** calibration_fraction, mean_R2, mean_Spearman, mean_Top10_overlap
- **Description:** Aggregated development calibration curves used to summarize how reconstruction quality changes as the sparse-label fraction increases.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/DEV_Calibration_Curve_Aggregate.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/DEV_Calibration_Curve_Aggregate.csv`
- **SHA-256:** `06f037be913f74c6ef0705d1ea38dabc00b9c1c3dc1d1a1d6514865e67f0fbb3`

### 43. `DEV_LOPO_OOD_Distance_Summary.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A1–A3 development
- **Dimensions:** 3 rows × 4 columns
- **Size:** 0.0002 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** heldout_patient, median_knn_distance, p95_knn_distance, p99_knn_distance
- **Description:** Development-fold summary of nearest-neighbor geometry distances used to calibrate local geometry-support/OOD diagnostics.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/DEV_LOPO_OOD_Distance_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/DEV_LOPO_OOD_Distance_Summary.csv`
- **SHA-256:** `d0528659f9dd6500fb47a59c75a1256fe51ff1da4a31e61b90bc38881b9fc45c`

### 44. `DEV_Personalized_Pointwise_Residuals.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A1–A3 development
- **Dimensions:** 235613 rows × 4 columns
- **Size:** 9.6075 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** val_patient, target, calibration_fraction, abs_transformed_residual
- **Description:** Pointwise residuals from LOAO sparse personalization on development anatomies; these residuals form the empirical basis for development-calibrated residual bands.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/DEV_Personalized_Pointwise_Residuals.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/DEV_Personalized_Pointwise_Residuals.csv`
- **SHA-256:** `83c5e2d1db04f66ad2f1d950c809ab48ffed330b32af67860873cb341e612f12`

### 45. `FIGURE_INDEX.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** Project-wide
- **Dimensions:** 41 rows × 2 columns
- **Size:** 0.0024 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** category, file
- **Description:** Index of generated analysis figures and the data files used to construct them.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/FIGURE_INDEX.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/FIGURE_INDEX.csv`
- **SHA-256:** `0b37e08d4f8b80d2208f886f6dee2416a26bae9ef90b2a32cd42a7091472e195`

### 46. `P4_Anchor_Masks.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 5 columns
- **Size:** 0.2345 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, anchor_5pct, anchor_10pct
- **Description:** Exact pointwise anchor/non-anchor masks for the tested A4 calibration fractions, allowing reproducible identification of calibration and evaluation nodes.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Anchor_Masks.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Anchor_Masks.csv`
- **SHA-256:** `fec0453ecaa6d874b83d0f577cd1efb7fecb1189fd8bb1b781ab9f730e901740`

### 47. `P4_Geometry_OOD_Map.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 11 columns
- **Size:** 0.6032 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, local_ood_pct_vs_holdout_P1, local_ood_pct_vs_holdout_P2, local_ood_pct_vs_holdout_P3, local_ood_percentile_median_pair, local_ood_percentile_mean_pair, local_ood_percentile_max_pair, local_robust_OOD95, local_robust_OOD99
- **Description:** Pointwise A4 geometry-support/OOD scores derived from nearest-neighbor distances in the geometry-feature representation.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Geometry_OOD_Map.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Geometry_OOD_Map.csv`
- **SHA-256:** `9000d05789763e6d2e719a950fc6e46b5b379036e02d96eeee2ca25648dc9fdb`

### 48. `P4_Global_Anatomy_Envelope.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 10 rows × 9 columns
- **Size:** 0.0015 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** feature, P1, P2, P3, P4, development_min, development_max, P4_outside_development_range, outside_distance_in_dev_range_units
- **Description:** Comparison of A4 global geometry descriptors with the range/envelope observed across development anatomies A1–A3.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Global_Anatomy_Envelope.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Global_Anatomy_Envelope.csv`
- **SHA-256:** `faee01b8551c8813d9f01557f631e9626e72bde3987b93a3ba83f9255d4bf3de`

### 49. `P4_OOD_Error_Association.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 14 rows × 5 columns
- **Size:** 0.0009 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** target, calibration_fraction, Spearman_OOD_vs_normalized_abs_error, mean_error_OOD95, mean_error_in_domain
- **Description:** Target-wise association table relating local geometry OOD/support scores to normalized reconstruction errors on A4.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_OOD_Error_Association.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_OOD_Error_Association.csv`
- **SHA-256:** `09a02c9f8d8a907c5726b16c30def2c753169dc1650621be3a2038c64bbd0cfc`

### 50. `P4_OOD_Summary.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 1 rows × 7 columns
- **Size:** 0.0002 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** n_points, median_OOD_percentile, p90_OOD_percentile, fraction_OOD95, fraction_OOD99, development_calibration_p95_distance, development_calibration_p99_distance
- **Description:** Summary of A4 OOD-score distribution statistics and the fraction of nodes exceeding defined geometry-shift thresholds.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_OOD_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_OOD_Summary.csv`
- **SHA-256:** `26a15a7f0e8b74407ec37e7de650d6425ed18326c84a8af8db8308b13a427a2c`

### 51. `P4_Pareto_Agreement_Summary.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4 rows × 20 columns
- **Size:** 0.0012 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** calibration_fraction, channel, co_burden_Spearman, co_burden_MAE_percentile, co_burden_top10_overlap, joint_topdecile_precision, joint_topdecile_recall, joint_topdecile_F1, joint_topdecile_Jaccard, joint_topdecile_reference_n, joint_topdecile_prediction_n, pareto_front_precision, pareto_front_recall, pareto_front_F1, pareto_front_Jaccard, pareto_front_reference_n, pareto_front_prediction_n, dominance_score_Spearman ...
- **Description:** Summary of predicted-versus-reference agreement for multiphysics co-burden and Pareto/dominance diagnostic channels.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Pareto_Agreement_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Pareto_Agreement_Summary.csv`
- **SHA-256:** `9401a562a9708be1110a598067f11ad39ed3f3353b220761ce862e75d5238c1d`

### 52. `P4_Pareto_CoBurden_10pct.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 24 columns
- **Size:** 1.1812 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, is_calibration_anchor, mechanical_pct_ref, mechanical_pct_pred, peakWSS_pct_ref, peakWSS_pct_pred, RRT_pct_ref, RRT_pct_pred, high_shear_co_burden_ref, high_shear_co_burden_pred, high_shear_co_burden_abs_error, high_shear_joint_topdecile_ref, high_shear_joint_topdecile_pred, high_shear_pareto_front_ref, high_shear_pareto_front_pred, residence_oscillation_co_burden_ref ...
- **Description:** Pointwise A4 co-burden, percentile, dominance, and Pareto diagnostics at the 10% sparse-calibration setting.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Pareto_CoBurden_10pct.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Pareto_CoBurden_10pct.csv`
- **SHA-256:** `ccdbdb3c795de051d229ce7334bf6e7aa17ec00b2ecc6bf2384fa58afd3026b0`

### 53. `P4_Pareto_CoBurden_5pct.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 30 columns
- **Size:** 1.598 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, is_calibration_anchor, mechanical_pct_ref, mechanical_pct_pred, peakWSS_pct_ref, peakWSS_pct_pred, RRT_pct_ref, RRT_pct_pred, high_shear_co_burden_ref, high_shear_co_burden_pred, high_shear_co_burden_abs_error, high_shear_joint_topdecile_ref, high_shear_joint_topdecile_pred, high_shear_pareto_front_ref, high_shear_pareto_front_pred, residence_oscillation_co_burden_ref ...
- **Description:** Pointwise A4 co-burden, percentile, dominance, and Pareto diagnostics at the 5% primary secondary-analysis setting.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Pareto_CoBurden_5pct.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Pareto_CoBurden_5pct.csv`
- **SHA-256:** `d7e3df299a44a1c73e5929c83f9a6d7b13b08ddec92d245bf90ee294214f714c`

### 54. `P4_Personalized_Uncertainty_10pct.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 39 columns
- **Size:** 2.7332 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, is_calibration_anchor, TAWSS_vector_Pa_pred, TAWSS_vector_Pa_lo90, TAWSS_vector_Pa_hi90, TAWSS_vector_Pa_interval_width, TAWSS_vector_Pa_width_over_trainIQR, OSI_pred, OSI_lo90, OSI_hi90, OSI_interval_width, OSI_width_over_trainIQR, RRT_1_per_Pa_pred, RRT_1_per_Pa_lo90, RRT_1_per_Pa_hi90, RRT_1_per_Pa_interval_width ...
- **Description:** A4 10% sparse-calibration predictions with empirical residual-band lower/upper bounds and interval-width diagnostics.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Personalized_Uncertainty_10pct.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Personalized_Uncertainty_10pct.csv`
- **SHA-256:** `f8c7d9424c29fa3aaef5f626113ca3c1bc2f660743c4e33d51ca11d73091502f`

### 55. `P4_Personalized_Uncertainty_5pct.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 39 columns
- **Size:** 2.7269 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, is_calibration_anchor, TAWSS_vector_Pa_pred, TAWSS_vector_Pa_lo90, TAWSS_vector_Pa_hi90, TAWSS_vector_Pa_interval_width, TAWSS_vector_Pa_width_over_trainIQR, OSI_pred, OSI_lo90, OSI_hi90, OSI_interval_width, OSI_width_over_trainIQR, RRT_1_per_Pa_pred, RRT_1_per_Pa_lo90, RRT_1_per_Pa_hi90, RRT_1_per_Pa_interval_width ...
- **Description:** A4 5% sparse-calibration predictions with empirical residual-band lower/upper bounds and interval-width diagnostics.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Personalized_Uncertainty_5pct.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Personalized_Uncertainty_5pct.csv`
- **SHA-256:** `81b370be51b586d69743ce9cafbfaa8caa388d9a049eeb51bb844f9a14d7da47`

### 56. `P4_Uncertainty_Coverage_Summary.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 14 rows × 6 columns
- **Size:** 0.0014 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** target, calibration_fraction, q90_transformed_residual, P4_nonanchor_coverage, median_width_over_trainIQR, p95_width_over_trainIQR
- **Description:** Target-level summary of empirical residual-band coverage and interval widths normalized by the development target IQR.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_Uncertainty_Coverage_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_Uncertainty_Coverage_Summary.csv`
- **SHA-256:** `a28ffa652a51b82da2269ed7f14549c0bee896f70034090bdcd6defbc5f179a8`

### 57. `P4_V3_Master_Pointwise_Table.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** A4
- **Dimensions:** 4055 rows × 81 columns
- **Size:** 4.9688 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa, OSI, RRT_1_per_Pa, peak_WSS_magnitude_Pa, VM_cycle_max_Pa, VM_stress_amplitude_Pa, VM_temporal_mean_Pa, anchor_5pct, anchor_10pct, TAWSS_vector_Pa_zero_shot_pred, TAWSS_vector_Pa_personalized_5pct, TAWSS_vector_Pa_personalized_10pct, TAWSS_vector_Pa_abs_error_5pct, TAWSS_vector_Pa_uncertainty_width_norm_5pct, OSI_zero_shot_pred ...
- **Description:** V3 master pointwise table combining geometry, reference fields, predictions, anchor masks, OOD/support scores, uncertainty diagnostics, and multiphysics diagnostic variables for A4.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/P4_V3_Master_Pointwise_Table.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/P4_V3_Master_Pointwise_Table.csv`
- **SHA-256:** `c2fa5a2c5cb9da87097bb57a5d94d6b97975fa5df2b923b69de5c7f4790c9352`

### 58. `V3_PRIMARY_5PCT_TARGET_SUMMARY.csv`
- **Stage:** V3 uncertainty/OOD/Pareto
- **Status:** Current/Canonical
- **Criticality:** Core diagnostic output
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 13 columns
- **Size:** 0.0015 MB
- **Produced by:** V3 analysis pipeline (archived outputs; codebook reconstructed reference implementation)
- **Used by:** V3 report, V9/V10 figures and discussion
- **Key columns:** target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, Spearman, Top10_overlap, q90_transformed_residual, P4_nonanchor_coverage, median_width_over_trainIQR, p95_width_over_trainIQR
- **Description:** Target-level V3 summary for the primary 5% sparse-calibration secondary-analysis setting.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/V3_PRIMARY_5PCT_TARGET_SUMMARY.csv`
- **Original path:** `/mnt/data/DigitalTwin_V3_Multiphysics/V3_PRIMARY_5PCT_TARGET_SUMMARY.csv`
- **SHA-256:** `21aa62f2e2fc6ec57b2620685080931f896f8e26bcb42c396045cded2bf763df`

### 59. `FIGURE_DISPLAY_BOUNDS.csv`
- **Stage:** V3 figure support
- **Status:** Figure support
- **Criticality:** Core diagnostic output
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 4 columns
- **Size:** 0.0005 MB
- **Produced by:** V3 figure preparation
- **Used by:** V3 spatial figures
- **Key columns:** target, display_lower_1pct_combined, display_upper_99pct_combined, reference_prediction_same_scale
- **Description:** Fixed/shared display bounds for spatial figure color scales, used to keep reference-versus-prediction visual comparisons consistent and fair.
- **Package path:** `spreadsheets_original_csv/05_DigitalTwin_V3/FIGURE_DISPLAY_BOUNDS.csv`
- **Original path:** `/mnt/data/_v3pkg/FIGURE_DISPLAY_BOUNDS.csv`
- **SHA-256:** `afc9be8a515fd58ef690136f9865b0eccb92b95d0836137535820bcfbc8e7b01`

## 06_Final_4Anatomy_Consolidated

### 60. `DEV_LOPO_AllCandidates.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A3 development
- **Dimensions:** 63 rows × 10 columns
- **Size:** 0.0097 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** target, candidate, val_patient, R2, MAE, RMSE, NMAE_IQR, Spearman, Top10_overlap, R2_log1p
- **Description:** Consolidated development candidate-evaluation results included in the final four-anatomy analysis package.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/DEV_LOPO_AllCandidates.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/DEV_LOPO_AllCandidates.csv`
- **SHA-256:** `59e11ad5650756d8005b80be9c9e3bab3390715834c98bfa051e0830711f51bc`

### 61. `DEV_LOPO_OOF_Predictions.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A3 development
- **Dimensions:** 29786 rows × 18 columns
- **Size:** 8.9452 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** patient, x_mm, y_mm, z_mm, TAWSS_vector_Pa_truth, TAWSS_vector_Pa_pred, OSI_truth, OSI_pred, RRT_1_per_Pa_truth, RRT_1_per_Pa_pred, peak_WSS_magnitude_Pa_truth, peak_WSS_magnitude_Pa_pred, VM_cycle_max_Pa_truth, VM_cycle_max_Pa_pred, VM_stress_amplitude_Pa_truth, VM_stress_amplitude_Pa_pred, VM_temporal_mean_Pa_truth, VM_temporal_mean_Pa_pred
- **Description:** Consolidated development out-of-fold predictions included in the final analysis package.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/DEV_LOPO_OOF_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/DEV_LOPO_OOF_Predictions.csv`
- **SHA-256:** `692fc5d479473b847c1a5bf6fbd49fef91239624049e5506bebf0275f504eb4c`

### 62. `DEV_PERSONALIZATION_LOPO.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A3 development
- **Dimensions:** 84 rows × 12 columns
- **Size:** 0.0133 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** val_patient, target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, NMAE_IQR, Spearman, Top10_overlap, R2_log1p
- **Description:** Detailed LOAO sparse-personalization results included in the final consolidated analysis package.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/DEV_PERSONALIZATION_LOPO.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/DEV_PERSONALIZATION_LOPO.csv`
- **SHA-256:** `bafa2dab0849f8992dbe29bbafc8368eb0b788f40953f6be7f56d83f84ebbd5e`

### 63. `DEV_PERSONALIZATION_SUMMARY.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A3 development
- **Dimensions:** 28 rows × 7 columns
- **Size:** 0.0032 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** target, calibration_fraction, mean_R2, min_R2, mean_Spearman, mean_Top10_overlap, mean_NMAE_IQR
- **Description:** Consolidated development personalization summary included in the final analysis package.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/DEV_PERSONALIZATION_SUMMARY.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/DEV_PERSONALIZATION_SUMMARY.csv`
- **SHA-256:** `b4d166026c6419bb94cb271b7122edf4ea56de8408977ac696cb1474f81dad52`

### 64. `DEV_SelectedModels.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A3 development
- **Dimensions:** 7 rows × 22 columns
- **Size:** 0.003 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** target, selected_model, mean_R2, min_R2, mean_MAE, min_MAE, mean_RMSE, min_RMSE, mean_NMAE_IQR, min_NMAE_IQR, mean_Spearman, min_Spearman, mean_Top10_overlap, min_Top10_overlap, mean_R2_log1p, min_R2_log1p, R2_holdout_P1, Spearman_holdout_P1 ...
- **Description:** Target-specific development-selected models included in the final consolidated analysis package.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/DEV_SelectedModels.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/DEV_SelectedModels.csv`
- **SHA-256:** `f39ca169dc142419a6fc6cad7b4c1560c553d9b3a9bfba1e1e678b01ce6723f2`

### 65. `P4_PERSONALIZED_METRICS.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 28 rows × 11 columns
- **Size:** 0.0045 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, NMAE_IQR, Spearman, Top10_overlap, R2_log1p
- **Description:** Final consolidated A4 sparse-personalization metrics for the evaluated calibration fractions.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P4_PERSONALIZED_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P4_PERSONALIZED_METRICS.csv`
- **SHA-256:** `a8d33c173c454d77c63cc2cec24683e0c05d2d77dd78ceadf3f6cc294d71c200`

### 66. `P4_PERSONALIZED_PREDICTIONS.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 4055 rows × 31 columns
- **Size:** 2.2418 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_personalized_1pct, TAWSS_vector_Pa_personalized_2pct, TAWSS_vector_Pa_personalized_5pct, TAWSS_vector_Pa_personalized_10pct, OSI_personalized_1pct, OSI_personalized_2pct, OSI_personalized_5pct, OSI_personalized_10pct, RRT_1_per_Pa_personalized_1pct, RRT_1_per_Pa_personalized_2pct, RRT_1_per_Pa_personalized_5pct, RRT_1_per_Pa_personalized_10pct, peak_WSS_magnitude_Pa_personalized_1pct, peak_WSS_magnitude_Pa_personalized_2pct, peak_WSS_magnitude_Pa_personalized_5pct ...
- **Description:** Final consolidated pointwise A4 sparse-personalization predictions.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P4_PERSONALIZED_PREDICTIONS.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P4_PERSONALIZED_PREDICTIONS.csv`
- **SHA-256:** `8e75f281ef7fc4be5e4fd8f85163b98adf5b3956aee7b8ae9f6ade96c7706695`

### 67. `P4_ZERO_SHOT_METRICS.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 7 rows × 9 columns
- **Size:** 0.0012 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** R2, MAE, RMSE, NMAE_IQR, Spearman, Top10_overlap, R2_log1p, Interval90_coverage, target
- **Description:** Final consolidated A4 zero-shot performance metrics.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P4_ZERO_SHOT_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P4_ZERO_SHOT_METRICS.csv`
- **SHA-256:** `02f186bd77c39922257148281318a930087456f1e6fddec04aece5399102a1ad`

### 68. `P4_ZERO_SHOT_PREDICTIONS.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 4055 rows × 24 columns
- **Size:** 1.7571 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_pred, TAWSS_vector_Pa_lo90, TAWSS_vector_Pa_hi90, OSI_pred, OSI_lo90, OSI_hi90, RRT_1_per_Pa_pred, RRT_1_per_Pa_lo90, RRT_1_per_Pa_hi90, peak_WSS_magnitude_Pa_pred, peak_WSS_magnitude_Pa_lo90, peak_WSS_magnitude_Pa_hi90, VM_cycle_max_Pa_pred, VM_cycle_max_Pa_lo90, VM_cycle_max_Pa_hi90 ...
- **Description:** Final consolidated pointwise A4 zero-shot predictions.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P4_ZERO_SHOT_PREDICTIONS.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P4_ZERO_SHOT_PREDICTIONS.csv`
- **SHA-256:** `bddd86f20fac954dd8190d89ea7fa518c1d918db9bb70893abe1e812384c2fda`

### 69. `P2_ABLATION_PERSONALIZED.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A2 ablation
- **Dimensions:** 28 rows × 23 columns
- **Size:** 0.0102 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** target, calibration_fraction, n_calibration_P123, n_evaluation_P123, R2_P123, MAE_P123, RMSE_P123, NMAE_IQR, Spearman_P123, Top10_overlap_P123, R2_log1p, n_calibration_P13, n_evaluation_P13, R2_P13, MAE_P13, RMSE_P13, Spearman_P13, Top10_overlap_P13 ...
- **Description:** Sensitivity results comparing sparse-personalization behavior with versus without anatomy A2 in the development prior.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P2_ABLATION_PERSONALIZED.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P2_ABLATION_PERSONALIZED.csv`
- **SHA-256:** `ef788d94707e932dcf14c868bb252ba8f8459ee76afdc3f9e18ceeaa3c371c32`

### 70. `P2_ABLATION_ZERO_SHOT.csv`
- **Stage:** Final consolidated pipeline
- **Status:** Current/Canonical
- **Criticality:** Sensitivity/archive
- **Scope:** A2 ablation
- **Dimensions:** 7 rows × 20 columns
- **Size:** 0.0029 MB
- **Produced by:** Final 4-anatomy consolidation scripts
- **Used by:** Manuscript sensitivity and archive
- **Key columns:** R2_P123, MAE_P123, RMSE_P123, NMAE_IQR, Spearman_P123, Top10_overlap_P123, R2_log1p, Interval90_coverage_P123, target, R2_P13, MAE_P13, RMSE_P13, Spearman_P13, Top10_overlap_P13, Interval90_coverage_P13, delta_R2_P123_minus_P13, delta_Spearman_P123_minus_P13, delta_Top10_overlap_P123_minus_P13 ...
- **Description:** Sensitivity results comparing A4 zero-shot behavior with versus without anatomy A2 in the development prior.
- **Package path:** `spreadsheets_original_csv/06_Final_4Anatomy_Consolidated/P2_ABLATION_ZERO_SHOT.csv`
- **Original path:** `/mnt/data/DigitalTwin_Final_4Patient/P2_ABLATION_ZERO_SHOT.csv`
- **SHA-256:** `424f1759e01a856256c1b27287271f4b6f16ebd681724214c8fb813737c7582e`

## 07_Sensitivity_Ablations

### 71. `P13_Training_Table.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 11394 rows × 32 columns
- **Size:** 6.3535 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** x_mm, y_mm, z_mm, s_norm, dist_nearest_end, radial_norm, local_radius_over_length, local_radius_over_median, local_radius_over_large_end, local_radius_gradient, curvature_1_per_mm, curvature_radius, curvature_side, tangent_alignment_main_axis, centerline_length_mm, mean_radius_over_length, max_radius_over_length, global_expansion_ratio ...
- **Description:** Development table using A1+A3 only for P2-ablation sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_Training_Table.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P13_Training_Table.csv`
- **SHA-256:** `e9e05101bc614149a501b614dd17d3e14035c474cf95062d5dc38590636e44a3`

### 72. `P4_P13_Test_Features.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 4055 rows × 25 columns
- **Size:** 1.7607 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** x_mm, y_mm, z_mm, patient, s_norm, dist_nearest_end, radial_norm, local_radius_over_length, local_radius_over_median, local_radius_over_large_end, local_radius_gradient, curvature_1_per_mm, curvature_radius, curvature_side, tangent_alignment_main_axis, centerline_length_mm, mean_radius_over_length, max_radius_over_length ...
- **Description:** A4 geometry features paired with A1+A3-only sensitivity pipeline.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P4_P13_Test_Features.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P4_P13_Test_Features.csv`
- **SHA-256:** `3bb2e58149ff30ae3dda3f8a0d665f5b8bd276e675a2f4a2e6fb2e14656532c6`
- **Duplicate IDs:** 32

### 73. `P13_LOPO_CV_AllCandidates.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 42 rows × 10 columns
- **Size:** 0.0057 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, candidate, train_patient, val_patient, R2, MAE, RMSE, Spearman, Top10_overlap, NMAE
- **Description:** Candidate evaluation in A1+A3-only sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_LOPO_CV_AllCandidates.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P13_LOPO_CV_AllCandidates.csv`
- **SHA-256:** `41c898ef8b5a5a78d798411468907dcba696e37842b1321c7bfb76226eade78c`

### 74. `P13_SelectedModels.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 7 rows × 9 columns
- **Size:** 0.0012 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, selected_model, mean_R2, mean_MAE, mean_Spearman, mean_Top10_overlap, mean_NMAE, R2_P1_holdout, R2_P3_holdout
- **Description:** Selected models in A1+A3-only sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_SelectedModels.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P13_SelectedModels.csv`
- **SHA-256:** `4a2722adc9f773923008cfb44b4711f0535df9f70498a59b810777de204c7372`

### 75. `P13_LOPO_OOF_Predictions.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 18828 rows × 18 columns
- **Size:** 5.6443 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** patient, x_mm, y_mm, z_mm, TAWSS_vector_Pa_truth, TAWSS_vector_Pa_pred, OSI_truth, OSI_pred, RRT_1_per_Pa_truth, RRT_1_per_Pa_pred, peak_WSS_magnitude_Pa_truth, peak_WSS_magnitude_Pa_pred, VM_cycle_max_Pa_truth, VM_cycle_max_Pa_pred, VM_stress_amplitude_Pa_truth, VM_stress_amplitude_Pa_pred, VM_temporal_mean_Pa_truth, VM_temporal_mean_Pa_pred
- **Description:** OOF predictions for A1+A3-only sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_LOPO_OOF_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P13_LOPO_OOF_Predictions.csv`
- **SHA-256:** `c927c4ed1310255fa856d305c81a435166200329e3e9e263f5c1c610d925890a`

### 76. `P4_P13_DigitalTwin_Predictions.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 4055 rows × 24 columns
- **Size:** 1.7568 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_pred, TAWSS_vector_Pa_lo90, TAWSS_vector_Pa_hi90, OSI_pred, OSI_lo90, OSI_hi90, RRT_1_per_Pa_pred, RRT_1_per_Pa_lo90, RRT_1_per_Pa_hi90, peak_WSS_magnitude_Pa_pred, peak_WSS_magnitude_Pa_lo90, peak_WSS_magnitude_Pa_hi90, VM_cycle_max_Pa_pred, VM_cycle_max_Pa_lo90, VM_cycle_max_Pa_hi90 ...
- **Description:** A4 zero-shot predictions from A1+A3-only prior.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P4_P13_DigitalTwin_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P4_P13_DigitalTwin_Predictions.csv`
- **SHA-256:** `4364cbb00e221428f781223eeaff663e4873a1cd8b6c54fcd6b4ad1dfab8f464`

### 77. `P4_HELDOUT_SENSITIVITY_METRICS.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 7 rows × 7 columns
- **Size:** 0.0009 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** R2, MAE, RMSE, Spearman, Top10_overlap, Interval90_coverage, target
- **Description:** Metrics of A4 zero-shot under A1+A3-only sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P4_HELDOUT_SENSITIVITY_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P4_HELDOUT_SENSITIVITY_METRICS.csv`
- **SHA-256:** `e3c018485f16af11a7abdaad4ceb2fe82ce3e7f679e5d328d09f4c89e20e4e38`

### 78. `P13_vs_P123_P4_Comparison.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 7 rows × 14 columns
- **Size:** 0.002 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, P123_R2, P123_MAE, P123_RMSE, P123_Spearman, P123_Top10_overlap, P13_R2, P13_MAE, P13_RMSE, P13_Spearman, P13_Top10_overlap, Delta_R2_P13_minus_P123, Delta_Spearman, Delta_Top10_overlap
- **Description:** Direct comparison of A1+A3 vs A1+A2+A3 zero-shot performance on A4.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_vs_P123_P4_Comparison.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_ZeroShot/P13_vs_P123_P4_Comparison.csv`
- **SHA-256:** `4e04a52945523c4c5f343fa3e13931fcc26b10e059e5ff786410153262889b4a`

### 79. `P13_Personalization_LOPO.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 56 rows × 11 columns
- **Size:** 0.007 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** train_patient, val_patient, target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** Sparse personalization LOAO under A1+A3-only sensitivity.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_Personalization_LOPO.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_Personalized/P13_Personalization_LOPO.csv`
- **SHA-256:** `f0798be301750aecaa8723f9bed1dacb80e9dd4b213e8b911f6c530662c7489d`

### 80. `P13_Personalization_Summary.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 28 rows × 7 columns
- **Size:** 0.0032 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, calibration_fraction, mean_R2, min_R2, mean_MAE, mean_Spearman, mean_Top10_overlap
- **Description:** Aggregate A1+A3-only personalization results.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_Personalization_Summary.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_Personalized/P13_Personalization_Summary.csv`
- **SHA-256:** `5ab4cb6422c0a57632f2abb7683a7b461ae7d0f32f5875f530a9a7d1d3e642e9`

### 81. `P4_P13_PERSONALIZED_METRICS.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 28 rows × 9 columns
- **Size:** 0.0034 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** A4 personalized metrics from A1+A3 prior.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P4_P13_PERSONALIZED_METRICS.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_Personalized/P4_P13_PERSONALIZED_METRICS.csv`
- **SHA-256:** `38cd4857696e0d1661ec9fc7136652160beb6f8ba081e9d5971c1224595b203b`

### 82. `P4_P13_Personalized_Predictions.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A4
- **Dimensions:** 4055 rows × 31 columns
- **Size:** 2.2411 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** x_mm, y_mm, z_mm, TAWSS_vector_Pa_personalized_1pct, TAWSS_vector_Pa_personalized_2pct, TAWSS_vector_Pa_personalized_5pct, TAWSS_vector_Pa_personalized_10pct, OSI_personalized_1pct, OSI_personalized_2pct, OSI_personalized_5pct, OSI_personalized_10pct, RRT_1_per_Pa_personalized_1pct, RRT_1_per_Pa_personalized_2pct, RRT_1_per_Pa_personalized_5pct, RRT_1_per_Pa_personalized_10pct, peak_WSS_magnitude_Pa_personalized_1pct, peak_WSS_magnitude_Pa_personalized_2pct, peak_WSS_magnitude_Pa_personalized_5pct ...
- **Description:** A4 personalized predictions from A1+A3 prior.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P4_P13_Personalized_Predictions.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_Personalized/P4_P13_Personalized_Predictions.csv`
- **SHA-256:** `2492211bc5af00a0ad6c9de9c7a96d3267c7df9bf146d61ce94eb97a5ccf6c1f`

### 83. `P13_vs_P123_Personalized_Comparison.csv`
- **Stage:** P2 cohort ablation
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1+A3 sensitivity
- **Dimensions:** 28 rows × 13 columns
- **Size:** 0.0064 MB
- **Produced by:** P13 sensitivity scripts
- **Used by:** Cohort-sensitivity audit
- **Key columns:** target, calibration_fraction, P123_R2, P13_R2, P123_Spearman, P13_Spearman, P123_Top10_overlap, P13_Top10_overlap, P123_MAE, P13_MAE, Delta_R2_P13_minus_P123, Delta_Spearman, Delta_Top10_overlap
- **Description:** Comparison A1+A3 vs A1+A2+A3 after sparse personalization.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P13_vs_P123_Personalized_Comparison.csv`
- **Original path:** `/mnt/data/DigitalTwin_P13_Personalized/P13_vs_P123_Personalized_Comparison.csv`
- **SHA-256:** `c844783861405f7b1e4ccd33b723d880a7e38477e378873204768bc76a204663`

### 84. `P2_vs_P4_PostHoc_Descriptive_Comparison.csv`
- **Stage:** Cross-anatomy descriptive audit
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A2 ablation
- **Dimensions:** 7 rows × 4 columns
- **Size:** 0.0005 MB
- **Produced by:** Post-hoc audit scripts
- **Used by:** Cohort interpretation
- **Key columns:** metric, P2, P4, relative_abs_difference_P2_vs_P4
- **Description:** Post-hoc descriptive comparison of A2 and A4 field statistics, used to examine whether their FSI field distributions are unusually similar or different.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P2_vs_P4_PostHoc_Descriptive_Comparison.csv`
- **Original path:** `/mnt/data/P2_vs_P4_PostHoc_Descriptive_Comparison.csv`
- **SHA-256:** `01790e889137bd568c0af2fe65e25594b26cbcc7b6ad7d4bd199c482d84b3103`

### 85. `P1_P2_P3_P4_Field_Summary_PostHoc.csv`
- **Stage:** Cross-anatomy descriptive audit
- **Status:** Post-hoc sensitivity
- **Criticality:** Sensitivity/archive
- **Scope:** A1–A4
- **Dimensions:** 4 rows × 8 columns
- **Size:** 0.0006 MB
- **Produced by:** Post-hoc audit scripts
- **Used by:** Cohort interpretation
- **Key columns:** patient, TAWSS_mean_Pa, OSI_mean, RRT_median_1_per_Pa, PeakWSS_mean_Pa, VM_cycle_max_mean_Pa, VM_amp_mean_Pa, VM_temporal_mean_mean_Pa
- **Description:** Post-hoc comparative summary of key FSI field statistics across all four anatomies.
- **Package path:** `spreadsheets_original_csv/07_Sensitivity_Ablations/P1_P2_P3_P4_Field_Summary_PostHoc.csv`
- **Original path:** `/mnt/data/P1_P2_P3_P4_Field_Summary_PostHoc.csv`
- **SHA-256:** `920c43b87dbf6135eb4b6ecf0df51fc49e15204b93bdff83d8e9660faafc69df`

## 08_Reviewer_Controls

### 86. `baseline_hyperparam_sweep.csv`
- **Stage:** Baseline/robustness analysis
- **Status:** Reviewer-motivated control
- **Criticality:** Reviewer-critical control
- **Scope:** Project-wide
- **Dimensions:** 18 rows × 6 columns
- **Size:** 0.0016 MB
- **Produced by:** 03_reviewer_revision_analysis.py
- **Used by:** V9/V10 manuscript and figures
- **Key columns:** method, config, mean_TNMAE, mean_R2, mean_Spearman, mean_Top10
- **Description:** Development-only hyperparameter sweep used to select the same-anchor KNN, IDW, and RBF interpolation controls without using A4 target fields.
- **Package path:** `spreadsheets_original_csv/08_Reviewer_Controls/baseline_hyperparam_sweep.csv`
- **Original path:** `/mnt/data/ICBME2026_ReviewerLoop/baseline_hyperparam_sweep.csv`
- **SHA-256:** `6772390779049838a3f5c860ec4f307a0715edd53f004065dee27a84bb63eac2`

### 87. `tuned_baseline_A4_5pct.csv`
- **Stage:** Baseline/robustness analysis
- **Status:** Reviewer-motivated control
- **Criticality:** Reviewer-critical control
- **Scope:** A4
- **Dimensions:** 18 rows × 7 columns
- **Size:** 0.002 MB
- **Produced by:** 03_reviewer_revision_analysis.py
- **Used by:** V9/V10 manuscript and figures
- **Key columns:** target, method, R2, MAE, RMSE, Spearman, Top10
- **Description:** Target-level summary of development-selected same-anchor baseline performance on A4 at 5% anchors.
- **Package path:** `spreadsheets_original_csv/08_Reviewer_Controls/tuned_baseline_A4_5pct.csv`
- **Original path:** `/mnt/data/ICBME2026_ReviewerLoop/tuned_baseline_A4_5pct.csv`
- **SHA-256:** `907e5e884494d781e56d8bf6bbff539b926ca6a3ea7e047dc176ed9fee3c2179`

### 88. `tuned_baseline_A4_predictions.csv`
- **Stage:** Baseline/robustness analysis
- **Status:** Reviewer-motivated control
- **Criticality:** Reviewer-critical control
- **Scope:** A4
- **Dimensions:** 4055 rows × 22 columns
- **Size:** 1.5309 MB
- **Produced by:** 03_reviewer_revision_analysis.py
- **Used by:** V9/V10 manuscript and figures
- **Key columns:** x_mm, y_mm, z_mm, anchor, TAWSS_vector_Pa_KNN, TAWSS_vector_Pa_IDW, TAWSS_vector_Pa_RBF, OSI_KNN, OSI_IDW, OSI_RBF, RRT_1_per_Pa_KNN, RRT_1_per_Pa_IDW, RRT_1_per_Pa_RBF, peak_WSS_magnitude_Pa_KNN, peak_WSS_magnitude_Pa_IDW, peak_WSS_magnitude_Pa_RBF, VM_cycle_max_Pa_KNN, VM_cycle_max_Pa_IDW ...
- **Description:** Pointwise A4 predictions from the tuned same-anchor KNN/IDW/RBF baselines together with the anchor mask; used for spatial figures, error maps, and physical-bound audits.
- **Package path:** `spreadsheets_original_csv/08_Reviewer_Controls/tuned_baseline_A4_predictions.csv`
- **Original path:** `/mnt/data/ICBME2026_ReviewerLoop/tuned_baseline_A4_predictions.csv`
- **SHA-256:** `764fcba316eda9ff95d58778b83b453127e95d21bded7a07c34208a5f9d9302f`

### 89. `nearest_anchor_distance_sensitivity.csv`
- **Stage:** Baseline/robustness analysis
- **Status:** Reviewer-motivated control
- **Criticality:** Reviewer-critical control
- **Scope:** Project-wide
- **Dimensions:** 72 rows × 8 columns
- **Size:** 0.0075 MB
- **Produced by:** 03_reviewer_revision_analysis.py
- **Used by:** V9/V10 manuscript and figures
- **Key columns:** target, method, distance_quartile, n, median_nearest_anchor_distance_stdxyz, mean_abs_error_over_IQR, median_abs_error_over_IQR, Spearman_distance_vs_abs_error_all_nonanchor
- **Description:** Error-versus-nearest-anchor-distance analysis used to characterize the local field-completion behavior of sparse reconstruction methods.
- **Package path:** `spreadsheets_original_csv/08_Reviewer_Controls/nearest_anchor_distance_sensitivity.csv`
- **Original path:** `/mnt/data/ICBME2026_ReviewerLoop/nearest_anchor_distance_sensitivity.csv`
- **SHA-256:** `ffa6844e81a688b1377853c1279f2936d3148ee7e7feb09e1cb4dcad2cfda1fb`

### 90. `computational_timing_summary.csv`
- **Stage:** Runtime context
- **Status:** Reviewer-motivated control
- **Criticality:** Reviewer-critical control
- **Scope:** Project-wide
- **Dimensions:** 9 rows × 7 columns
- **Size:** 0.0012 MB
- **Produced by:** Timing audit
- **Used by:** V9/V10 Computational Cost section
- **Key columns:** stage, anatomy_or_scope, median_seconds, p10_seconds, p90_seconds, provenance, notes
- **Description:** Summary of archived COMSOL runtimes and post-hoc Python algorithm timings. These values provide computational context and are not interpreted as end-to-end clinical speedup.
- **Package path:** `spreadsheets_original_csv/08_Reviewer_Controls/computational_timing_summary.csv`
- **Original path:** `/mnt/data/ICBME2026_ReviewerLoop/V9_digital_twin_roadmap/analysis/computational_timing_summary.csv`
- **SHA-256:** `871da1f572f96a2a5e63cd263af9774a21fe963396b4a4aa7e18c1d53911c1a8`

## 09_Paper_Tables

### 91. `Table1_P4_Primary_5pct_Performance.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 8 columns
- **Size:** 0.0008 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** Target, R2, MAE, RMSE, Spearman_rho, Top10_hotspot_overlap, Calibration_nodes, Evaluation_nodes
- **Description:** Paper-ready table containing the principal A4 5% sparse-calibration performance results.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Table1_P4_Primary_5pct_Performance.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Table1_P4_Primary_5pct_Performance.csv`
- **SHA-256:** `b9245c9cf94a80c606796bb48bb24cace19f4fe8b30f97d2118dc7b4185e6e0d`

### 92. `Table2_Personalization_Ablation_Aggregate.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 5 rows × 4 columns
- **Size:** 0.0005 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** Variant, Mean_R2, Mean_Spearman_rho, Mean_Top10_overlap
- **Description:** Paper-ready aggregate table for the personalization component-ablation analysis.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Table2_Personalization_Ablation_Aggregate.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Table2_Personalization_Ablation_Aggregate.csv`
- **SHA-256:** `d4b881f4e1353ab5092d7d1087330b2107abb863d546c65ad4daf33ccc9b5255`

### 93. `TableS1_Development_Component_Ablation.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 4 rows × 4 columns
- **Size:** 0.0004 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** Variant, Development_mean_R2, Development_mean_Spearman_rho, Development_mean_Top10_overlap
- **Description:** Supplementary table development component ablation.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/TableS1_Development_Component_Ablation.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/TableS1_Development_Component_Ablation.csv`
- **SHA-256:** `8a2cf7ed9394fd8eb07785ce0e058e515ebec5e850c5e1f15dccceabbd053789`

### 94. `TableS2_P4_PerTarget_Ablation.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 16 columns
- **Size:** 0.0022 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** target, zero_R2, zero_Spearman, zero_Top10, affine5_R2, affine5_Spearman, affine5_Top10, local5_R2, local5_Spearman, local5_Top10, full5_R2, full5_Spearman, full5_Top10, full10_R2, full10_Spearman, full10_Top10
- **Description:** Supplementary per-target A4 ablation.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/TableS2_P4_PerTarget_Ablation.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/TableS2_P4_PerTarget_Ablation.csv`
- **SHA-256:** `19f5eff38b1a278312bc376675269d68de39e1db1e15c5047934263cb660dd19`

### 95. `Ablation_Development_Aggregate.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 4 rows × 6 columns
- **Size:** 0.0004 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** variant, calibration_fraction, mean_R2, mean_Spearman, mean_Top10_overlap, mean_MAE
- **Description:** Aggregate development ablation across targets.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Ablation_Development_Aggregate.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Ablation_Development_Aggregate.csv`
- **SHA-256:** `1db0ad4932fe4303b90ec509f2e4a6132a50a54270b9315737ca790da2188a41`

### 96. `Ablation_Development_LOPO_Detail.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 84 rows × 9 columns
- **Size:** 0.0103 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** val_patient, target, variant, calibration_fraction, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** Detailed development ablation results by LOAO fold, target, and personalization variant.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Ablation_Development_LOPO_Detail.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Ablation_Development_LOPO_Detail.csv`
- **SHA-256:** `e6f1129a7a03b0ee5299b4cf432eab5f7a27bbd09c640e27ec8d0cdebb00d2ac`

### 97. `Ablation_P4_Aggregate.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 5 rows × 5 columns
- **Size:** 0.0004 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** variant, calibration_fraction, mean_R2, mean_Spearman, mean_Top10_overlap
- **Description:** Aggregate A4 ablation.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Ablation_P4_Aggregate.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Ablation_P4_Aggregate.csv`
- **SHA-256:** `41b340b06911b90e9bea659726eb5bdefbb8322d5c624afda6447a4d561243a7`

### 98. `Ablation_P4_Detail.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 35 rows × 10 columns
- **Size:** 0.0046 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** target, variant, calibration_fraction, n_calibration, n_evaluation, R2, MAE, RMSE, Spearman, Top10_overlap
- **Description:** Detailed A4 ablation results by target and personalization variant.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/Ablation_P4_Detail.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/Ablation_P4_Detail.csv`
- **SHA-256:** `bd32eb6ae3d0d3d908d0104dc5b2a2d3f89a690b02167e4e44e04f413e78b947`

### 99. `TABLE_Ablation_P4.csv`
- **Stage:** Manuscript tables
- **Status:** Paper-ready summary
- **Criticality:** Publication summary
- **Scope:** Project-wide
- **Dimensions:** 7 rows × 16 columns
- **Size:** 0.0022 MB
- **Produced by:** Paper analysis/export scripts
- **Used by:** Main/Supplementary manuscript
- **Key columns:** target, zero_R2, zero_Spearman, zero_Top10, affine5_R2, affine5_Spearman, affine5_Top10, local5_R2, local5_Spearman, local5_Top10, full5_R2, full5_Spearman, full5_Top10, full10_R2, full10_Spearman, full10_Top10
- **Description:** Table-ready presentation of the A4 personalization component-ablation results.
- **Package path:** `spreadsheets_original_csv/09_Paper_Tables/TABLE_Ablation_P4.csv`
- **Original path:** `/mnt/data/DigitalTwin_Paper_Final/TABLE_Ablation_P4.csv`
- **SHA-256:** `e5425e328143cebc7a21811e528fc553bcf32ea7afe2bab0fe242d8f5a52064d`
