# Print the derived numbers behind the λ 0.6–0.9 / 10x–75x results from the
# saved Monte Carlo rows. Run from this folder: python derive.py
import json, math, collections
import numpy as np

D = 'results/'
MD, MS, M0, S0 = 0.24, 0.615, 0.2450743507356192, 2.1   # m_dir, m_exp, Eli's m, Eli's slope
me = lambda w: w * MD + (1 - w) * MS
ok = lambda r: 'err' not in r and r.get('m') and r.get('beta')
rows = lambda f: [r for r in map(json.loads, open(D + f)) if ok(r)]

base = [r for r in rows('mc300.jsonl') if r['sc'] == 'a_fix15']
beta = 1 / 3.1377461411776673   # Eli preset at 15x, as printed by `python tos.py`
print(f"β (Eli preset, 15x): {beta:.3f}   (r_software 3.1377; same at every λ)")
print(f"P(TOS), default taste, 15x: {np.mean([r['m'] > r['beta'] for r in base]):.0%}")
for w in (0.4, 0.6, 0.8):
    print(f"w {w}: m = {w}·{MD} + {1-w:.1f}·{MS} = {me(w):.3f}   m/β = {me(w)/beta:.2f}   "
          f"slope = {S0}·m/{M0:.3f} = {S0*me(w)/M0:.2f}")

by = collections.defaultdict(list)
for r in rows('mc3_300.jsonl'):
    if 'raw' not in r['sc']: by[r['sc']].append(r)
tk = lambda L: float(np.median([(r['asi'] - r['ac']) if r['ac'] and r['asi'] else np.inf for r in L]))
print("\nSampled λ ~ U[0.6, 0.9], ceiling ~ log-U[10x, 75x]:")
for w in (0.4, 0.6, 0.8):
    L = by[f'samp_w{w}']
    print(f"  w {w}: P(TOS) {np.mean([r['m'] > r['beta'] for r in L]):.0%}, median AC→ASI {tk(L):.2f} yr (n={len(L)})")

print("\nCorner grid, change in median AC→ASI:")
for w in (0.4, 0.6, 0.8):
    c = {(l, a): tk(by[f'grid_{l}_{a}_w{w}']) for l in (0.6, 0.9) for a in (10, 75)}
    lam = [1 - c[(0.9, a)] / c[(0.6, a)] for a in (10, 75)]
    asy = [1 - c[(l, 75)] / c[(l, 10)] for l in (0.6, 0.9)]
    print(f"  w {w}: λ 0.6→0.9 shortens it {min(lam):.1%}–{max(lam):.1%}; ceiling 10x→75x {min(asy):.0%}–{max(asy):.0%}")

g = collections.defaultdict(list)
for r in rows('mc2_300.jsonl'):
    if r['sc'].startswith('cell_') or r['sc'].startswith('ref_'): g[r['sc']].append(r)
ref = {0.3: g['ref_w0.3'], 0.5: [r for r in rows('mc300.jsonl') if r['sc'] == 'c_w0.5_fix15'], 0.7: g['ref_w0.7']}
print("\nCeiling 15x→50x at λ 0.65 (w 0.3 / 0.5 / 0.7 grid):")
for w in (0.3, 0.5, 0.7):
    a, b = tk(ref[w]), tk(g[f'cell_0.65_50_w{w}'])
    print(f"  w {w}: {a:.2f} → {b:.2f} yr, {1 - b/a:.0%} shorter")
