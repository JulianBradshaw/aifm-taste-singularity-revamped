# Reproducing the λ 0.6–0.9, 10x–75x results

Step by step, from a fresh clone to every number in the
new-ranges section at the end of [results/RESULTS.md](results/RESULTS.md).
The commands are for macOS/Linux; on Windows use `.venv\Scripts\python.exe` and `set AIFM_ROOT=..`.

## 1. Setup

```sh
git clone https://github.com/JulianBradshaw/aifm-taste-singularity-revamped
cd aifm-taste-singularity-revamped
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cd taste_singularity
export AIFM_ROOT=..
PY=../.venv/bin/python
```

## 2. Deterministic Eli run (β and default m)

```sh
$PY tos.py
```

This prints Eli 08-16-26 at λ 0.65 and the 15x ceiling: `beta` 0.319 (`r` 3.1377) and `m` 0.245. Because of the two-λ change, both are the same at any λ.

## 3. Monte Carlo

The new-range run needs the 15x reference samples from `mc.py`. Each step takes about 20 minutes on 4 cores.

```sh
$PY mc.py 300 mc300.jsonl                 # base scenarios, including the 15x reference (c_w0.5_fix15)
$PY mc3.py 300 mc3_300.jsonl both         # sampled ranges, then the corner grid
$PY ana3.py mc3_300.jsonl                 # summary table per cell
```

For the 15x → 50x comparison, also run `$PY mc2.py 300 mc2_300.jsonl`, which takes about 30 minutes. It covers λ {0.65, 0.9} × ceiling {15x, 50x} × w {0.3, 0.5, 0.7}.

Every run uses the Eli Q2 sampling config with seed 20260810, so all scenarios see the same draws. β and m are held per sample at their 15x values. mc3.py draws λ uniformly from [0.6, 0.9] and the ceiling log-uniformly from [10x, 75x], using seed 20261102.

The output from these runs is already in `results/`. To skip them, run the next step on those files directly.

## 4. Derived numbers

```sh
$PY derive.py        # reads results/*.jsonl; copy your own outputs there to use them instead
```

| Number | Value | How it is computed |
|---|---|---|
| β | 0.319 | 1 / r_software, with r_software refit to the 2024 software-efficiency rate at the 15x ceiling (step 2) |
| Default P(TOS) | 40% | share of `a_fix15` samples with m > β (Eli's own taste draws, 15x) |
| Combined m at w 0.4 / 0.6 / 0.8 | 0.465 / 0.390 / 0.315 | m = w·m_dir + (1 − w)·m_exp, with m_dir 0.24 and m_exp 0.615 |
| m/β | 1.46 / 1.22 / 0.99 | combined m ÷ 0.319 |
| Taste slope | 3.98 / 3.34 / 2.70 | 2.1 × m / 0.245; the slope scales m linearly at a fixed ceiling |
| P(TOS) at w 0.4 / 0.6 / 0.8 | 71 / 62 / 52% | share of `samp_w*` samples with m > β |
| Median AC→ASI, sampled ranges | 1.10 / 1.42 / 1.90 yr | median of ASI − AC over `samp_w*` |
| λ 0.6 → 0.9 | 1–3% shorter takeoff (0.7–3.2%) | 1 − tk(λ 0.9) / tk(λ 0.6), at 10x and at 75x, from the `grid_*` cells; tk is median AC→ASI |
| Ceiling 10x → 75x | about 40% shorter (38–43%) | 1 − tk(75x) / tk(10x), at λ 0.6 and at λ 0.9 |
| Ceiling 15x → 50x | 24–28% shorter | 1 − tk(50x) / tk(15x) at λ 0.65 from `mc2_300.jsonl` (w 0.3 / 0.5 / 0.7) |

With β and m held, P(TOS) depends on w only. λ and the ceiling change takeoff speed, but not whether a sample has a TOS. In each sample, m is proportional to its taste-slope multiplier, and β does not depend on the slope. 12 to 16 of the 300 samples fail in each cell and are dropped, which leaves about ±3 points of sampling error on P(TOS).
