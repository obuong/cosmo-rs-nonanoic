from pathlib import Path
import inspect
import opencosmorspy as oc

ORCA_FILES = {
    "nonanoic_solute": "nonanoic_cosmors.solute.orcacosmo",
    "nonanoic_solvent": "nonanoic_cosmors.solvent.orcacosmo",
    "water_solute": "water_cosmors.solute.orcacosmo",
    "water_solvent": "water_cosmors.solvent.orcacosmo",
}

print("opencosmorspy loaded from:", oc.__file__)
print("\nChecking files:")
for k, f in ORCA_FILES.items():
    p = Path(f)
    print(f"  {k:16s} -> {f}  | exists={p.exists()}  size={p.stat().st_size if p.exists() else 'NA'}")

# ---------- helpers to discover loaders ----------
def find_orcacosmo_loaders(module, max_hits=30):
    hits = []
    for name, obj in inspect.getmembers(module):
        try:
            s = (name + " " + getattr(obj, "__doc__", "")).lower()
        except Exception:
            s = name.lower()
        if "orcacosmo" in s and (inspect.isfunction(obj) or inspect.isclass(obj)):
            hits.append((name, obj))
        if len(hits) >= max_hits:
            break
    return hits

print("\nDiscovering possible ORCACOSMO loaders...")
loader_hits = []
for subname in ["input_parsers", "molecules", "helper_functions", "cosmors"]:
    if hasattr(oc, subname):
        sub = getattr(oc, subname)
        hits = find_orcacosmo_loaders(sub)
        if hits:
            loader_hits.append((subname, hits))

if not loader_hits:
    print("  (No obvious loaders found by name scan.)")
else:
    for subname, hits in loader_hits:
        print(f"\n  In oc.{subname}:")
        for n, obj in hits[:15]:
            kind = "class" if inspect.isclass(obj) else "func"
            print(f"    - {n} ({kind})")

# ---------- parameterization discovery ----------
print("\nDiscovering parameterizations...")
param_candidates = []
# common patterns: Parameterization.list(), Parameterization.available(), oc.parameterization.<something>
try:
    Param = oc.Parameterization
    for attr in ["available", "list", "get_available", "available_parameterizations"]:
        if hasattr(Param, attr):
            param_candidates.append(("Parameterization."+attr, getattr(Param, attr)))
except Exception as e:
    print("  Could not access oc.Parameterization:", e)

for tag, fn in param_candidates:
    try:
        val = fn() if callable(fn) else fn
        print(f"  {tag} -> {val}")
    except Exception as e:
        print(f"  {tag} failed -> {type(e).__name__}: {e}")

print("\nTrying to build a Parameterization object (default)...")
param = None
try:
    param = oc.Parameterization()
    print("  Parameterization() OK:", param)
except Exception as e:
    print("  Parameterization() failed:", type(e).__name__, e)

print("\nTrying to initialize COSMORS...")
engine = None
try:
    # some APIs accept param in constructor, some don't
    engine = oc.COSMORS(param) if param is not None else oc.COSMORS()
    print("  COSMORS init OK:", engine)
except TypeError:
    engine = oc.COSMORS()
    print("  COSMORS() init OK (no param arg):", engine)
except Exception as e:
    print("  COSMORS init failed:", type(e).__name__, e)

if engine is not None:
    methods = [m for m in dir(engine) if not m.startswith("_")]
    print("\nCOSMORS methods (first 80):")
    print(methods[:80])

print("\n--- NEXT STEP ---")
print("If you paste the 'possible ORCACOSMO loaders' section + COSMORS methods list,")
print("I’ll map it to the exact few lines needed to load nonanoic + water and compute gamma/solvation.")
