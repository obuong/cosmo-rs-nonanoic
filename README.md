# COSMO-RS Modeling of Nonanoic Acid in Aqueous Systems

## Overview

This repository contains COSMO-RS–based thermodynamic modeling of nonanoic acid in water. The project evaluates temperature-dependent activity coefficients and related thermodynamic behavior using openCOSMO-RS.

This modeling framework supports research on wastewater-derived lipid valorization and oxidative cleavage processes for sustainable nonanoic acid production.

---

## Research Context

Nonanoic acid (pelargonic acid) is a bio-based contact herbicide. Understanding its thermodynamic behavior in aqueous systems is important for:

- Phase equilibrium analysis
- Solubility behavior
- Temperature-dependent activity coefficients
- Process optimization and reactor modeling
- Sustainable process design

This repository provides scripts and inputs necessary to compute and analyze activity coefficients using COSMO-RS.

---

## Repository Structure
cosmo-rs-nonanoic/
│
├── run_cosmors_nonanoic.py
├── probe_cosmors_api.py
├── cosmors_discover_and_run.py
├── inspect_refst.py
│
├── plot_gamma_vs_T.py
├── plot_lng_vs_invT.py
├── sweep_gamma_vs_T.py
│
├── nonanoic_cosmors.inp
├── water_cosmors.inp
│
├── nonanoic_cosmors.json
├── water_cosmors.json
│
└── nonanoic_calibration_final.xlsx

Large ORCA-generated binary files such as `.gbw`, `.cpcm`, `.densities`, `.orcacosmo`, and temporary files are excluded from version control.

---

## Requirements

### Software

- Python 3.9 or newer
- openCOSMO-RS_py
- ORCA (only required if generating new COSMO surface files)

### Python Dependencies

Install required Python packages:

```bash
pip install numpy matplotlib
pip install git+https://github.com/TUHH-TVT/openCOSMO-RS_py


Large ORCA-generated binary files such as `.gbw`, `.cpcm`, `.densities`, `.orcacosmo`, and temporary files are excluded from version control.

---

## Requirements

### Software

- Python 3.9 or newer
- openCOSMO-RS_py
- ORCA (only required if generating new COSMO surface files)

### Python Dependencies

Install required Python packages:

```bash
pip install numpy matplotlib
pip install git+https://github.com/TUHH-TVT/openCOSMO-RS_py

Running the Model
1. Execute COSMO-RS Calculation
python run_cosmors_nonanoic.py
2. Generate Activity Coefficient vs Temperature Plot
python plot_gamma_vs_T.py
3. Generate Van’t Hoff Plot (ln(γ) vs 1/T)
python plot_lng_vs_invT.py
4. Perform Temperature Sweep
python sweep_gamma_vs_T.py
Expected Outputs

Temperature-dependent activity coefficients γ(T)

ln(γ) vs 1/T linear regression plots

Thermodynamic property extraction

JSON output files from COSMO-RS engine

Notes

Ensure COSMO surface files are available before running calculations.

Temperature ranges are defined within the respective Python scripts.

Reference state inspection can be performed using inspect_refst.py.

This repository focuses on thermodynamic modeling and does not include reactor-scale simulation.

Author
Esau Obuong
Chemical Engineering
University of Louisiana at Lafayette

Research Areas:

Wastewater valorization

Oleaginous yeast lipid platforms

Nonanoic acid production

Thermodynamic modeling

Sustainable process engineering

License

This repository is intended for academic and research use.
