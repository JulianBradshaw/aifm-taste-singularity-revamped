# Monte Carlo results (300 samples)

Produced by the scripts in this folder at commit 9821619 (two λs + β-hold). Eli Q2 08-16-26 sampling config, λ (forward) 0.65, 300 samples, seed 20260810, same draws in every scenario. 12 of 300 samples fail (ValueError) in every scenario and are dropped (old repo: 9). History and calibration run at λ 0.5, so β and m no longer depend on λ. The raw rows, one JSON line per sample and scenario, are in this folder:

- `mc300.jsonl`: `mc.py 300 mc300.jsonl` (the nine base scenarios)
- `mcfix.jsonl`, `mcfix2.jsonl`: `mcfix.py`, `mcfix2.py` (50x and unbounded with β held, then β and m held)
- `mc2_300.jsonl`: `mc2.py 300 mc2_300.jsonl` (the λ × ceiling × w grid)

The scripts read these from the working directory, so to re-summarise run `ana.py` / `ana2.py` from here, or copy the files up a level.

Numbers in brackets are the same runs on the earlier single-λ copy ([aifm-taste-singularity](https://github.com/JulianBradshaw/aifm-taste-singularity)), where λ 0.65 also applied to history and calibration.

## Scenarios (old repo in brackets)

| Run | P(TOS) | median m/β | median AC→ASI (yr) | median ASI | P(ASI < 2030) |
|---|---|---|---|---|---|
| a default (sampled ceiling) | 0.41 [0.37] | 0.84 [0.80] | 4.2 [5.1] | 2035.9 [2037.7] | 0.27 [0.24] |
| a default, 15x fixed | 0.40 [0.37] | 0.79 [0.76] | 3.8 [4.6] | 2035.8 [2037.5] | 0.27 [0.24] |
| b TasteVal (m = 0.615) | 0.80 [0.79] | 2.11 [2.03] | 0.91 [0.96] | 2030.6 [2031.2] | 0.44 [0.41] |
| c w = 0.3 | 0.75 [0.74] | 1.73 [1.66] | 1.16 [1.3] | 2031.5 [2032.2] | 0.40 [0.37] |
| c w = 0.5 | 0.67 [0.65] | 1.47 [1.41] | 1.44 [1.6] | 2032.0 [2033.0] | 0.39 [0.34] |
| c w = 0.7 | 0.57 [0.55] | 1.21 [1.16] | 1.99 [2.5] | 2033.0 [2034.1] | 0.35 [0.31] |
| c w = 0.5, 15x fixed | 0.67 [0.65] | 1.38 [1.34] | 1.39 [1.6] | 2032.0 [2032.8] | 0.39 [0.35] |
| d w = 0.5, 50x, β and m held | 0.67 [0.65] | 1.38 [1.34] | 0.99 [1.1] | 2031.2 [2032.0] | 0.42 [0.39] |
| e w = 0.5, unbounded, β and m held | 0.67 [0.65] | 1.38 [1.34] | 0.36 [0.45] | 2029.7 [2030.0] | 0.54 [0.50] |
| d w = 0.5, 50x, β refit | 0.64 [0.63] | 1.32 [1.27] | 1.10 [1.25] | 2031.4 [2032.1] | 0.41 [0.37] |
| e w = 0.5, unbounded, β refit | 0.56 [0.54] | 1.14 [1.09] | 0.58 [0.66] | 2030.0 [2030.6] | 0.50 [0.44] |

## Grid: λ × ceiling × w (β and m held per sample at their 15x values)

| λ | ceiling | P(TOS) w = 0.3 / 0.5 / 0.7 | median AC→ASI (yr) | median ASI | P(ASI < 2030) |
|---|---|---|---|---|---|
| 0.65 | 15x | 73 / 67 / 57% [71 / 65 / 55] | 1.07 / 1.39 / 1.89 [1.21 / 1.58 / 2.13] | 2031.4 / 2032.0 / 2032.8 | 41 / 39 / 34% |
| 0.65 | 50x | 73 / 67 / 57% | 0.81 / 0.99 / 1.36 [0.87 / 1.14 / 1.59] | 2030.6 / 2031.2 / 2031.8 | 44 / 42 / 39% |
| 0.9 | 15x | 73 / 68 / 57% | 1.09 / 1.38 / 1.88 [1.34 / 1.74 / 2.47] | 2031.1 / 2031.7 / 2032.5 | 43 / 41 / 36% |
| 0.9 | 50x | 73 / 68 / 57% | 0.80 / 1.03 / 1.35 [1.03 / 1.37 / 1.86] | 2030.4 / 2031.0 / 2031.5 | 46 / 44 / 41% |

λ 0.9 now changes only future swarms, so it no longer delays AC or slows takeoff (old repo: about 5 months later AC and slower takeoff). It moves ASI 2 to 4 months earlier, and takeoff changes by under 0.05 yr. 16 samples fail in the λ 0.9 cells. Sampling error on P(TOS) is about ±3 points.
