from pathlib import Path

# We’ll just confirm the files exist first
files = [
    "nonanoic_cosmors.solute.orcacosmo",
    "nonanoic_cosmors.solvent.orcacosmo",
    "water_cosmors.solute.orcacosmo",
    "water_cosmors.solvent.orcacosmo",
]
for f in files:
    p = Path(f)
    print(f"{f}: {'OK' if p.exists() else 'MISSING'} ({p.stat().st_size if p.exists() else 'NA'} bytes)")

print("\nNext: tell me which openCOSMO-RS_py API you’re using (your import line),")
print("because there are a couple variants depending on version.")
