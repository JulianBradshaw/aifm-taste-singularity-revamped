# Taste-only singularity runs

Scripts for asking how often the model gives a taste-only software singularity
(TOS), and how fast takeoff is, when AI research taste improves faster than the
model's default. A sample has a TOS when m > β, where

- m = `slope_times_log_f`, the OOMs of research-taste multiplier gained per OOM
  of effective compute, and
- β = `beta_software` = 1 / r_software after calibration.

All runs use the Eli 08-16-26 preset (or the Eli Q2 sampling config for the
Monte Carlo) with the parallelization penalty λ set to 0.65. In this copy λ is
the forward λ: history and calibration stay at λ 0.5 (see the repository
README), so λ 0.65 changes only how future coding labor scales.

## The two switches

**β-hold.** By default the model refits r_software (and so β) to the 2024
software-efficiency rate on every run, so raising the coding-labor ceiling
(`inf_labor_asymptote`) also changes β. Setting the environment variable
`AIFM_FIX_R` to a number pins r_software to that value right after calibration
(`progress_model/_impl.py`). Unset, the model is unchanged. The runs pin it to
the value calibrated with the 15x ceiling (Eli preset: 3.1377, so β = 0.319),
so that a higher ceiling acts only as a takeoff effect. With two λs, r_software
and m no longer depend on λ, so this value is the same at λ 0.5, 0.65 and 0.9.

**Taste-slope scaling.** `ai_research_taste_slope` is entered in SDs per
progress-year (Eli: 2.1) and the model converts it to m (Eli: 0.245). m is
proportional to the slope, so to reach a target m the scripts multiply the slope
by m_target / 0.245 (in the Monte Carlo, each sample's own draw is multiplied,
which keeps the spread). The deterministic runs then iterate until the reported
m hits the target. Because the slope is per progress-year, a different ceiling
or λ changes the conversion, so the held-m cells rescale the slope again until m
matches the 15x reference sample.

Targets: TasteVal-like m_search = 0.615, direction taste m_dir = 0.24, and the
blend m_eff = w·m_dir + (1 − w)·m_search for w ∈ {0.3, 0.5, 0.7}.

## Results

The 300-sample Monte Carlo results for this copy, with the raw rows, are in
[results/RESULTS.md](results/RESULTS.md).
[REPRODUCING.md](REPRODUCING.md) walks through regenerating them and
deriving each headline number (`derive.py`).

## Scripts

Run from this folder with `AIFM_ROOT=..` (the repository root) after
`pip install -r ../requirements.txt`.

- `base_run.py`, `tos.py`: load a preset from `constants/parameters.ts` and run it
  through `/api/compute`. `python tos.py` runs Eli at λ 0.65.
- `det.py`: deterministic runs a–e (default; TasteVal; w = 0.3/0.5/0.7; w = 0.5
  at 50x and unbounded ceilings).
- `detfix.py`: the same with β held.
- `mc.py N OUT [scenarios]`: Monte Carlo over the Eli Q2 sampling config (seed
  20260810, the same draws in every scenario). Writes one JSON line per
  sample. Run it first as `python mc.py 300 mc300.jsonl`; the scripts below read
  `mc300.jsonl`.
- `mcfix.py`, `mcfix2.py`: the 50x and unbounded cells with β held per sample
  at its 15x value, then with m held too.
- `mc2.py N OUT`: the grid λ ∈ {0.65, 0.9} × ceiling ∈ {15x, 50x} ×
  w ∈ {0.3, 0.5, 0.7}, with β and m held per sample at their λ 0.65, 15x values.
- `mc3.py N OUT [sampled|grid|both]`: λ drawn uniformly from [0.6, 0.9] and the
  ceiling log-uniformly from [10x, 75x] per sample, and the corners of that box,
  for w ∈ {0.4, 0.6, 0.8}, with β and m held per sample at their 15x values.
  Reads `mc300.jsonl` (here or in `results/`). `ana3.py` summarises it.
- `ana.py`, `ana2.py`: summaries (P(TOS), median AC→ASI, median ASI,
  P(ASI < 2030)).

## Caveats

- 300 samples gives roughly ±3 points of sampling error on P(TOS). About 3% of
  samples fail and are dropped.
- With the TasteVal scaling, about a quarter of slope draws exceed the slope's
  input bound of 10; they are not clipped.
- Holding β with a higher ceiling means "the ceiling is high from today with β
  held", not a ceiling that rises after AC.
