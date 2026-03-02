import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

csv_file = "gamma_nonanoic_in_water_vs_T.csv"

T = []
lng = []

with open(csv_file, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        T.append(float(row["T_K"]))
        lng.append(float(row["ln_gamma_nonanoic"]))

T = np.array(T)
lng = np.array(lng)

invT = 1.0 / T

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(invT, lng)

print("Linear fit: ln(gamma) = A*(1/T) + B")
print(f"A (slope)     = {slope:.6f}")
print(f"B (intercept) = {intercept:.6f}")
print(f"R^2           = {r_value**2:.6f}")

# Estimate apparent excess enthalpy
R = 8.314  # J/mol-K
deltaH = -R * slope
print(f"Apparent ΔH_excess ≈ {deltaH/1000:.3f} kJ/mol")

# Plot
plt.figure()
plt.scatter(invT, lng)
plt.plot(invT, slope*invT + intercept)
plt.xlabel("1/T (1/K)")
plt.ylabel("ln(γ∞)")
plt.title("Van’t Hoff Plot: ln(γ∞) vs 1/T")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("vant_hoff_nonanoic.png", dpi=300)
plt.show()
