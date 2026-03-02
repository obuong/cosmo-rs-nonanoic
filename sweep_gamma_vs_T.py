from pathlib import Path
import numpy as np
import csv
import opencosmorspy as oc

# --- files ---
solute_file = Path("nonanoic_cosmors.solute.orcacosmo")   # component 0
water_file  = Path("water_cosmors.solvent.orcacosmo")     # component 1

assert solute_file.exists(), f"Missing {solute_file}"
assert water_file.exists(), f"Missing {water_file}"

# --- COSMO-RS setup ---
par = oc.Parameterization("BP_TZVP_C30_1701")

# Use a very dilute solute so this approximates infinite dilution
x_solute = 1e-6
x = np.array([x_solute, 1.0 - x_solute], dtype=float)

# Temperature grid (edit as you like)
T_list = np.arange(273.15, 373.15 + 0.001, 5.0)  # 273.15 to 373.15 K every 5 K

out_csv = Path("gamma_nonanoic_in_water_vs_T.csv")

rows = []
for T in T_list:
    engine = oc.COSMORS()
    engine.par = par
    engine.clear_molecules()
    engine.clear_jobs()

    engine.add_molecule([str(solute_file)])  # 0
    engine.add_molecule([str(water_file)])   # 1

    engine.add_job(x, float(T), refst="cosmo")
    out = engine.calculate()

    lng = out["tot"]["lng"][0]          # [lnγ_nonanoic, lnγ_water]
    gam = np.exp(lng)

    rows.append({
        "T_K": float(T),
        "x_nonanoic": float(x[0]),
        "x_water": float(x[1]),
        "ln_gamma_nonanoic": float(lng[0]),
        "gamma_nonanoic": float(gam[0]),
        "ln_gamma_water": float(lng[1]),
        "gamma_water": float(gam[1]),
    })

# Write CSV
with out_csv.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# Print a small preview
print(f"Wrote: {out_csv.resolve()}")
print("Preview (first 5 rows):")
for r in rows[:5]:
    print(r)
