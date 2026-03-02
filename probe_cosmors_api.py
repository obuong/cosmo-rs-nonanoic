import importlib

candidates = ["opencosmorspy", "opencosmors", "openCOSMO_RS_py", "openCOSMO_RS"]
for name in candidates:
    try:
        m = importlib.import_module(name)
        print(f"\n=== IMPORT OK: {name} ===")
        print("module file:", getattr(m, "__file__", None))
        print("version:", getattr(m, "__version__", "(no __version__)"))
        keys = [k for k in dir(m) if not k.startswith("_")]
        print("top-level symbols (first 60):")
        print(keys[:60])
        break
    except Exception as e:
        print(f"IMPORT FAIL: {name} -> {type(e).__name__}: {e}")
