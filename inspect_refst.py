import opencosmorspy as oc

e = oc.COSMORS()
print("refmix_idxs:", getattr(e, "refmix_idxs", None))
print("mix_lst:", getattr(e, "mix_lst", None))
print("job_lst:", getattr(e, "job_lst", None))
