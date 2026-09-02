# Aortic-FSI-Sparse-Field-Completion

Geometry-only surrogate and sparse-anchor personalization pipeline for aortic FSI field completion. Repository packages manuscript source code into clean, stage-based layout for reproducible execution and GitHub release.

## Highlights

- Four-patient study design with Patients 1-3 for development and Patient 4 as locked test anatomy.
- Zero-shot surrogate training, sparse personalization, reviewer analyses, robustness checks, figure generation, reconstructed V3 analysis, and component ablation.
- Minimal repo structure with script names matched to analysis stages.
- Frozen configuration artifacts retained under `config/`.

## Repository Layout

```text
Aortic-FSI-Sparse-Field-Completion/
├── README.md
├── requirements.txt
├── config/
│   ├── baseline_selected_config.json
│   ├── freeze_manifest_pre_p4.json
│   ├── personalization_protocol.json
│   └── v3_manifest.json
├── data/
│   └── DigitalTwin_4Patient_Spreadsheet_Package/
├── docs/
│   └── model_files.md
└── src/
    ├── stage01_train_zero_shot.py
    ├── stage02_personalize_sparse_anchors.py
    ├── stage03_reviewer_analyses.py
    ├── stage04_anchor_robustness.py
    ├── stage05_recompute_selected_baselines.py
    ├── stage06_generate_figures.py
    ├── stage07_v3_uncertainty_ood_pareto.py
    └── stage08_component_ablation.py
```

## Stage Guide

1. `stage01_train_zero_shot.py`
   Builds geometry descriptors, trains frozen zero-shot surrogate models, and exports V1 artifacts.
2. `stage02_personalize_sparse_anchors.py`
   Applies sparse representative-anchor personalization and exports Patient 4 adapted predictions.
3. `stage03_reviewer_analyses.py`
   Runs post-freeze reviewer analyses, baseline sweeps, sensitivity studies, and reproducibility hashes.
4. `stage04_anchor_robustness.py`
   Tests anchor-selection robustness and RBF physical-bound sensitivity.
5. `stage05_recompute_selected_baselines.py`
   Recomputes density-weighted and spatial-block baseline comparisons.
6. `stage06_generate_figures.py`
   Generates manuscript and roadmap figures from archived result tables.
7. `stage07_v3_uncertainty_ood_pareto.py`
   Reconstructs V3 uncertainty, local OOD, and multiphysics Pareto analyses.
8. `stage08_component_ablation.py`
   Reconstructs sparse-personalization component ablation experiments.

## Data Expectations

Scripts assume mounted data under `/mnt/data` and use archived file names directly. Required raw inputs include:

- `Patient1_VectorResolved_Hemodynamics.csv`
- `Patient2_VectorResolved_Hemodynamics.csv`
- `Patient3_VectorResolved_Hemodynamics.csv`
- `Patient4_VectorResolved_Hemodynamics.csv`
- `Patient1_CycleResolved_SolidMechanics.csv`
- `Patient2_CycleResolved_SolidMechanics.csv`
- `Patient3_CycleResolved_SolidMechanics.csv`
- `Patient4_CycleResolved_SolidMechanics_v2.csv`

Several later stages also expect generated V1, V2, reviewer-loop, and archived derivative files already present under `/mnt/data`.

## COMSOL Model Files

Large COMSOL `.mph` model files are archived on Zenodo instead of committed to GitHub.

- Zenodo draft record: <https://zenodo.org/deposit/22260376>
- Public record URL after publication: <https://zenodo.org/records/22260376>
- File manifest and checksums: [docs/model_files.md](docs/model_files.md)

Download the model files from Zenodo and place them under local path `models/4Patient Models/` when needed. The `models/` directory is ignored by Git.

## Environment

- Python `3.13.5`
- NumPy `2.3.5`
- pandas `2.2.3`
- SciPy `1.17.0`
- scikit-learn `1.8.0`
- LightGBM `4.6.0`
- Primary random seed `20260821`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Recommended Run Order

```bash
python src/stage01_train_zero_shot.py
python src/stage02_personalize_sparse_anchors.py
python src/stage03_reviewer_analyses.py
python src/stage04_anchor_robustness.py
python src/stage05_recompute_selected_baselines.py
python src/stage06_generate_figures.py
python src/stage07_v3_uncertainty_ood_pareto.py
python src/stage08_component_ablation.py
```