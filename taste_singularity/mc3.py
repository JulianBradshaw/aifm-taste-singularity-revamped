# Monte Carlo over the λ range [0.6, 0.9] and the coding-labor ceiling range
# [10x, 75x] for w in {0.4, 0.6, 0.8}, with β and m held per sample at their
# 15x values (from the c_w0.5_fix15 rows of mc300.jsonl).
#   python mc3.py 300 mc3_300.jsonl [sampled|grid|both]
# "sampled": each sample draws λ ~ U[0.6, 0.9] and the ceiling log-uniform on
# [10, 75]. "grid": the corners λ {0.6, 0.9} x ceiling {10, 75}.
import os, sys, json
import numpy as np
import mc
from multiprocessing import get_context
W = [0.4, 0.6, 0.8]
def k(w): return mc.me(w) / mc.BASE
def job(a):
    i, lab, lam, asym, kk, fixr = a
    os.environ['AIFM_FIX_R'] = repr(fixr)
    mc.SC[lab] = (kk, asym); mc.LAM = lam
    r = mc.job((i, lab)); r['lam'] = lam; return r
def run(jobs, out):
    with get_context('fork').Pool(4, maxtasksperchild=50) as pool, open(out, 'a') as f:
        res = []
        for r in pool.imap_unordered(job, jobs, chunksize=2):
            f.write(json.dumps(r) + '\n'); f.flush(); res.append(r)
    return res
ok = lambda r: 'err' not in r and r.get('m') and r.get('beta')
def held(configs, tag, out):
    # configs: {i: [(lam, asym), ...]}. Pass 1 measures m at w = 0.5 with β pinned;
    # pass 2 rescales the slope so m matches the 15x reference, for each w.
    raw = run([(i, f'{tag}raw', lam, a, k(.5), 1 / ref[i]['beta'])
               for i, cs in configs.items() for lam, a in cs], out)
    ratio = {(r['i'], r['lam'], r['asym']): ref[r['i']]['m'] / r['m'] for r in raw if ok(r)}
    jobs = []
    for i, cs in configs.items():
        for lam, a in cs:
            if (i, lam, a) in ratio:
                for w in W:
                    lab = f'{tag}w{w}' if tag == 'samp_' else f'{tag}{lam}_{int(a)}_w{w}'
                    jobs.append((i, lab, lam, a, k(w) * ratio[(i, lam, a)], 1 / ref[i]['beta']))
    run(jobs, out)
if __name__ == '__main__':
    N = mc.N; OUT = mc.OUT; mode = sys.argv[3] if len(sys.argv) > 3 else 'both'
    src = 'mc300.jsonl' if os.path.exists('mc300.jsonl') else 'results/mc300.jsonl'
    ref = {r['i']: r for r in map(json.loads, open(src)) if r['sc'] == 'c_w0.5_fix15' and ok(r)}
    if mode in ('sampled', 'both'):
        rng = np.random.default_rng(20261102)
        lam = rng.uniform(0.6, 0.9, N); asym = 10 ** rng.uniform(1, np.log10(75), N)
        held({i: [(float(lam[i]), float(asym[i]))] for i in range(N) if i in ref}, 'samp_', OUT)
    if mode in ('grid', 'both'):
        held({i: [(l, a) for l in (0.6, 0.9) for a in (10.0, 75.0)] for i in range(N) if i in ref}, 'grid_', OUT)
    print('done')
