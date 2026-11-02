# Summary of mc3.py output: python ana3.py mc3_300.jsonl
import sys, json, collections, numpy as np
by = collections.defaultdict(list)
for r in map(json.loads, open(sys.argv[1])):
    if 'raw' in r['sc'] or 'err' in r or not r.get('m') or not r.get('beta'): continue
    by[r['sc']].append(r)
print('cell | n | P(TOS) | median m/β | median AC→ASI (yr) | median ASI | P(ASI < 2030)')
for sc in sorted(by):
    L = by[sc]; ac = np.array([r['ac'] or np.inf for r in L]); asi = np.array([r['asi'] or np.inf for r in L])
    tk = np.where(np.isfinite(ac), asi - ac, np.inf)
    print(sc, len(L), f"{np.mean([r['m'] > r['beta'] for r in L]):.2f}", f"{np.median([r['m']/r['beta'] for r in L]):.2f}",
          f"{np.median(tk):.2f}", f"{np.median(asi):.1f}", f"{np.mean(asi < 2030):.2f}")
