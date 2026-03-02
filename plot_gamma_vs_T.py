import csv
import numpy as np
import matplotlib.pyplot as plt

csv_file = "gamma_nonanoic_in_water_vs_T.csv"

T = []
gamma_non = []
lng_non = []

with open(csv_file, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        T.append(float(row["T_K"]))
        gamma_non.append(float(row["gamma_nonanoic"]))
        lng_non.append(float(row["ln_gamma_nonanoic"]))

T = np.array(T)
gamma_non = np.array(gamma_non)
lng_non = np.array(lng_non)

# Plot gamma
plt.figure()
plt.plot(T, gamma_non, marker="o")
plt.xlabel("Temperature (K)")
plt.ylabel("Activity coefficient, γ∞ (nonanoic in water)")
plt.title("COSMO-RS: γ∞ vs Temperature")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("gamma_nonanoic_in_water_vs_T.png", dpi=300)
plt.show()

# Plot ln(gamma)
plt.figure()
plt.plot(T, lng_non, marker="o")
plt.xlabel("Temperature (K)")
plt.ylabel("ln(γ∞) (nonanoic in water)")
plt.title("COSMO-RS: ln(γ∞) vs Temperature")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("ln_gamma_nonanoic_in_water_vs_T.png", dpi=300)
plt.show()

print("Saved:")
print("  gamma_nonanoic_in_water_vs_T.png")
print("  ln_gamma_nonanoic_in_water_vs_T.png")
