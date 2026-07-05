---
layout: page
title: Conecast
description: CME arrival modeling with HUXt and Gaussian-process surrogates
img: assets/img/heliosphere_snapshot.png
permalink: /projects/conecast/
importance: 3
category: work
github: https://github.com/georgemilosh/conecast
---

Conecast is a local, self-contained workflow for emulating coronal mass ejection (CME) arrival at Earth with HUXt and Gaussian-process surrogates.

[Project guide](/projects/conecast/guide/) | [Input-preparation tutorial](/projects/conecast/input-preparation/) | [GitHub repository](https://github.com/georgemilosh/conecast) | [Notebook guide](https://github.com/georgemilosh/conecast/blob/main/notebooks/README.md)

## What it does

- prepares solar-wind boundary conditions from GONG magnetograms via WSA+
- runs HUXt-based CME simulations for curated events
- trains per-event GP surrogate models for hit or miss classification and arrival-time regression
- provides tutorial notebooks and Colab entry points

<!-- markdownlint-disable MD033 -->
<table style="width: 100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align: center;">Hit probability</th>
      <th style="text-align: center;">Arrival time</th>
      <th style="text-align: center;">HUXt heliosphere</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: top;">
        <img src="https://raw.githubusercontent.com/georgemilosh/conecast/main/docs/images/hit_probability_longitude_latitude.png" alt="Hit probability" style="display: block; width: 100%; max-width: 100%; height: auto; border-radius: 0.35rem;">
      </td>
      <td style="text-align: center; vertical-align: top;">
        <img src="https://raw.githubusercontent.com/georgemilosh/conecast/main/docs/images/arrival_mean_longitude_width.png" alt="Arrival time" style="display: block; width: 100%; max-width: 100%; height: auto; border-radius: 0.35rem;">
      </td>
      <td style="text-align: center; vertical-align: top;">
        <img src="https://raw.githubusercontent.com/georgemilosh/conecast/main/docs/images/heliosphere_snapshot.png" alt="HUXt heliosphere" style="display: block; width: 100%; max-width: 100%; height: auto; border-radius: 0.35rem;">
      </td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-enable MD033 -->

Conecast combines WSA+, HUXt, and Gaussian-process surrogates to turn curated CME events into reproducible forecasting experiments.

## Quick start

```bash
python scripts/fetch_wsaplus_checkpoint.py
python scripts/generate_huxt_input.py --event 2017-09-06
python scripts/gp_huxt_surrogate.py --event 2017-09-06 design --n 300
python scripts/gp_huxt_surrogate.py --event 2017-09-06 run --limit 20
python scripts/gp_huxt_surrogate.py --event 2017-09-06 fit
python scripts/gp_huxt_surrogate.py --event 2017-09-06 analyze
```

The repository does not ship large runtime data. WSA+ checkpoints, magnetograms, boundary files, and run outputs are downloaded or generated on demand.

## Tutorial notebooks

- [01 - GP tutorial](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/notebooks/01_gp_tutorial.ipynb)
- [02 - HUXt inputs](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/notebooks/02_huxt_runs.ipynb)
- [03 - Arrival detector examples](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/notebooks/03_arrival_detector_examples.ipynb)
- [04 - GP surrogate application](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/notebooks/04_gp_huxt_application.ipynb)

## Hands-on exercises

Exercise set (built for the [ASAP summer school](https://asap-space.eu/asap-summer-school)). You provision a new CME event and launch a HUXt batch, then - while it runs in the background - study how surrogate skill scales with the number of runs, how the definition of a "hit" reshapes the model, and which launch parameter drives arrival time. 

See the [exercises guide](https://github.com/georgemilosh/conecast/blob/main/exercises/README.md) for the run sheet and Colab notes (the free Colab tier has no terminal, so the batch is launched as a background process).

- [Exercise 1 - Pick a new event and launch a batch](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/exercises/01_exercise_new_event.ipynb)
- [Exercise 2 - How many HUXt runs does the surrogate need?](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/exercises/02_exercise_how_many_runs.ipynb)
- [Exercise 3 - What counts as a "hit"? (compound thresholds)](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/exercises/03_exercise_what_is_a_hit.ipynb)
- [Exercise 4 - Your event: fit, importance, and contrast](https://colab.research.google.com/github/georgemilosh/conecast/blob/main/exercises/04_exercise_your_event_analysis.ipynb)

## Additional links

- [Conecast guide](/projects/conecast/guide/)
- [Conecast input-preparation tutorial](/projects/conecast/input-preparation/)
- [Conecast source repository](https://github.com/georgemilosh/conecast)
- [Conecast project page](https://georgemilosh.github.io/conecast/)
