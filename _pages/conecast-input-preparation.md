---
layout: page
title: Conecast Input Preparation
permalink: /projects/conecast/input-preparation/
description: Step-by-step walkthrough of generate_huxt_input.py
nav: false
---

[Back to Conecast project page](/projects/conecast/) | [Conecast guide](/projects/conecast/guide/) | [GitHub repository](https://github.com/georgemilosh/conecast)

## Tutorial: preparing HUXt inputs with `generate_huxt_input.py`

This tutorial explains the input-preparation stage for HUXt in this project. The key command is:

```bash
python scripts/generate_huxt_input.py --event 2017-09-06
```

The script reads CME seed events from `data_dir/events.csv`, prepares a background solar-wind boundary from GONG magnetograms and WSA+, and writes the files that later HUXt or GP workflows need.

> Run from the repository root after `source .venv/bin/activate` (see the [Conecast guide](/projects/conecast/guide/)).

---

## 1. What the script produces

For each selected event, outputs are written under:

```text
data_dir/sw/<event>/
```

The important outputs are:

| File | Purpose |
| --- | --- |
| `v_boundary_<event>.npz` | 360-point, 1-degree HUXt inner-boundary speed profile. The array key is `speed_map`. |
| `wsaplus_speed_map_<event>.npz` | Cached WSA+ longitude-latitude speed map object. |
| `wsaplus_speed_map_<event>.png` | Diagnostic plot of the full WSA+ speed map. |
| `huxt_input_speed_profile_<event>.png` | Diagnostic comparison of interpolated and nearest-neighbour sub-Earth speed profiles. |
| `huxt_input_speed_difference_<event>.png` | Difference between interpolation and nearest-neighbour sampling. |
| `huxt_input_subearth_track_<event>.png` | Sub-Earth track overlaid on the WSA+ map. |
| `event_config.yaml` | YAML file with the seed HUXt parameter vector (`initial_theta`) and Carrington rotation (`cr_num`). |
| `*.fits` | GONG magnetograms reused on later runs. |

The HUXt boundary file is the main product. It is loaded later as:

```python
data = np.load("data_dir/sw/2017-09-06/v_boundary_2017-09-06.npz")
v_boundary = data["speed_map"]
```

---

## 2. Event catalogue

Events are defined in `data_dir/events.csv`:

```csv
event,enabled,cme_onset,cme_0p1_au,longitude,latitude,width,speed,notes
2017-09-06,true,2017-09-06T12:24:00,2017-09-06T14:57:00,23.0,-15.0,88.0,1238.0,Prepared seed event
```

Required columns:

| Column | Meaning |
| --- | --- |
| `event` | Directory name under `data_dir/sw/`. |
| `enabled` | Optional; false-like values skip the row when using `--event all`. |
| `cme_onset` | Time used to select nearby GONG magnetograms. |
| `cme_0p1_au` | Time when the CME is assumed to reach 0.1 au; used to compute `inject_hour`. |
| `longitude`, `latitude`, `width`, `speed` | Seed Cone-CME parameters. |
| `notes` | Human-readable provenance or comments. |

---

## 3. Basic commands

Prepare one event:

```bash
source .venv/bin/activate
python scripts/generate_huxt_input.py --event 2017-09-06
```

Prepare all enabled events:

```bash
python scripts/generate_huxt_input.py --event all
```

Prepare several named events:

```bash
python scripts/generate_huxt_input.py --event 2017-09-06 2015-06-21
```

Reuse existing GONG FITS files without downloading:

```bash
python scripts/generate_huxt_input.py --event 2017-09-06 --no-download
```

Skip the optional seed HUXt sanity run:

```bash
python scripts/generate_huxt_input.py --event 2017-09-06 --skip-sanity-plot
```

Rewrite an existing `event_config.yaml` after changing event seed parameters:

```bash
python scripts/generate_huxt_input.py --event 2017-09-06 --force-config
```

Use a non-default event catalogue, output directory, or WSA+ checkpoint:

```bash
python scripts/generate_huxt_input.py \
  --events-file data_dir/events.csv \
  --output-root data_dir/sw \
  --checkpoint-path data_dir/sw/wsaplus.pt \
  --event 2017-09-06
```

---

## 4. How the script works

The script is organized as a small pipeline:

```text
main()
  ├─ parse_args()
  ├─ load_events()
  └─ process_event()              one call per selected event
       ├─ prepare_background()
       │    ├─ download_gong_mag()     optional, unless --no-download
       │    ├─ find_closest_map()
       │    ├─ run_wsaplus()           skipped when cached WSA+ map exists
       │    └─ map_input_huxt()
       │         ├─ compute_subearth_track()
       │         ├─ sample_interpolated()
       │         └─ sample_nearest()
       ├─ rhf.run_huxt_sim()           optional sanity run
       └─ write_event_config()
```

The functions answer different questions:

| Function | Question it answers | Main output |
| --- | --- | --- |
| `truthy()` | Is an optional CSV value such as `enabled` true-like? | Boolean. |
| `load_events()` | Which CME rows should be processed? | List of event dictionaries. |
| `download_gong_mag()` | Do we have GONG magnetograms near the CME onset? | Event-directory FITS files. |
| `find_closest_map()` | Which GONG map is closest to the CME onset? | SunPy map, observation time, time offset. |
| `run_wsaplus()` | What solar-wind speed map does WSA+ infer from that magnetogram? | Cached WSA+ result and PNG. |
| `compute_subearth_track()` | Where is Earth in Carrington longitude/latitude during this rotation? | `SBElon`, `SBElat`. |
| `sample_interpolated()` | What speed does interpolation give along the Earth track? | Interpolated speed series. |
| `sample_nearest()` | What speed comes from the nearest WSA+ grid cells along the Earth track? | Nearest-grid speed series and grid coordinates. |
| `map_input_huxt()` | How does the 2-D WSA+ map become a 1-D HUXt boundary? | 360-point speed profile plus diagnostics. |
| `prepare_background()` | Can we build the background wind for one event? | `v_boundary_<event>.npz`, WSA+ products, Carrington context. |
| `write_event_config()` | What seed metadata should downstream workflows read? | `event_config.yaml`. |
| `process_event()` | How is one CSV row turned into a prepared event directory? | Full event directory under `data_dir/sw/<event>/`. |

### `load_events()`

Reads the CSV, checks required columns, filters disabled rows, and returns one dictionary per selected event. `--event all` keeps every enabled row. Passing event names keeps only those names.

### `process_event()`

This is the per-event driver. It creates `data_dir/sw/<event>/`, calls the background-preparation code, computes the CME injection delay, optionally runs a one-shot HUXt sanity simulation, and writes the YAML metadata/config file.

The seed parameter vector is:

```python
theta = (inject_hour, longitude, latitude, width, speed)
```

`inject_hour` is computed from:

```python
Time(cme_0p1_au) - Time(closest_mag_time)
```

### `prepare_background()`

This prepares the background solar wind:

1. Parses `cme_onset` as an Astropy `Time`.
2. Defines the GONG search window from `cme_onset - 6 h` to `cme_onset`.
3. Downloads GONG files when download is enabled.
4. Finds the GONG map closest to `cme_onset`.
5. Computes the Carrington rotation number from the selected map.
6. Runs or reuses WSA+.
7. Converts the WSA+ map into a HUXt-ready 360-point speed boundary.
8. Saves `v_boundary_<event>.npz`.

If `wsaplus_speed_map_<event>.npz` already exists, the script reuses it and remakes the HUXt boundary and diagnostic plots.

### `download_gong_mag()`

Uses SunPy `Fido` to search and download GONG synoptic magnetograms into the event directory. Existing `*.fits` files cause the download step to be skipped. Downloaded `*.fits.gz` files are converted to plain `*.fits`.

### `find_closest_map()`

Loads all `*.fits` files in the event directory as SunPy maps, reads their observation times, and chooses the map with the smallest absolute time difference from `cme_onset`.

The selected map controls both the Carrington rotation number used for HUXt and the reference time used to compute `inject_hour`.

### `run_wsaplus()`

Calls:

```python
generate_wsaplus_map(filepath, mag_type="GONG", checkpoint_path=str(checkpoint_path))
```

The checkpoint defaults to:

```text
<output-root>/wsaplus.pt
```

The returned WSA+ object contains the longitude grid, latitude grid, and `speed_kms` map. The script saves this object in `wsaplus_speed_map_<event>.npz` and plots `wsaplus_speed_map_<event>.png`.

### WSA+ intermediate products

WSA+ is the bridge between the observed photospheric magnetic field and the HUXt inner-boundary speed profile.

The input to WSA+ is the selected GONG magnetogram:

```text
data_dir/sw/<event>/*.fits
```

The direct WSA+ output is a two-dimensional solar-wind speed map:

```text
wsaplus_speed_map_<event>.npz
```

Inside that `.npz`, the script stores one pickled WSA+ result object under the key `speed_map`.

| Field | Meaning |
| --- | --- |
| `speed_kms` | 2-D solar-wind speed array in km/s. |
| `phi_grid_deg` | 2-D Carrington longitude grid in degrees. |
| `theta_grid_deg` | 2-D latitude grid in degrees. |

The reduction from WSA+ map to HUXt boundary happens in three conceptual steps:

1. **Map geometry:** `compute_subearth_track(cr_num)` computes Earth longitude and latitude through the Carrington rotation of the selected GONG map.
2. **Map sampling:** `sample_interpolated()` and `sample_nearest()` sample `speed_kms` along that Earth track.
3. **HUXt formatting:** `map_input_huxt()` sorts those samples by longitude and resamples them onto `np.arange(1, 361)`.

### `compute_subearth_track()`

Computes Earth coordinates in the Heliographic Carrington frame across the selected Carrington rotation. The result is an hourly track `SBElon, SBElat`.

### `sample_interpolated()` and `sample_nearest()`

Both functions sample the WSA+ speed map along the sub-Earth track:

- `sample_interpolated()` uses `RegularGridInterpolator`.
- `sample_nearest()` picks the closest WSA+ grid cell at each sub-Earth point.

### `map_input_huxt()`

This function turns the WSA+ map into the HUXt boundary:

1. Extracts WSA+ speed, longitude grid, and latitude grid.
2. Computes the sub-Earth track.
3. Samples speeds along that track.
4. Sorts samples by Carrington longitude.
5. Interpolates the sampled profile onto `lon_grid_360 = np.arange(1, 361)`.
6. Saves diagnostic plots.
7. Returns the 360-point speed profile.

The current return value is the nearest-neighbour profile:

```python
return lon_grid_360, speed_nearest_360
```

That `speed_nearest_360` array has shape `(360,)` and is saved as:

```python
np.savez(outdir / f"v_boundary_{event}.npz", speed_map=speed_nearest_360)
```

### `write_event_config()`

Writes `event_config.yaml`, recording the seed `initial_theta` and the Carrington rotation `cr_num`.

---

## 5. Command-line options

| Option | Default | Meaning |
| --- | --- | --- |
| `--events-file` | `data_dir/events.csv` | CSV catalogue to read. |
| `--output-root` | `data_dir/sw` | Parent directory for per-event output folders. |
| `--checkpoint-path` | `<output-root>/wsaplus.pt` | WSA+ model checkpoint. |
| `--event` | `all` | One event, several event names, or `all`. |
| `--no-download` | off | Reuse existing GONG FITS files only. |
| `--force-config` | off | Rewrite `event_config.yaml` if it already exists. |
| `--skip-sanity-plot` | off | Skip the optional seed HUXt run and its plot. |

---

## 6. Reuse and caching rules

The script has several reuse points:

- Existing GONG `*.fits` files prevent a new download.
- Existing `wsaplus_speed_map_<event>.npz` prevents a new WSA+ run.
- Existing `event_config.yaml` prevents config rewriting unless `--force-config` is used.

The boundary and diagnostic plots are regenerated when `prepare_background()` runs, even when the WSA+ map is cached.

---

## 7. Inspecting a prepared event

Check the directory:

```bash
ls data_dir/sw/2017-09-06
```

Check the boundary array:

```bash
python - <<'PY'
import numpy as np
path = "data_dir/sw/2017-09-06/v_boundary_2017-09-06.npz"
data = np.load(path)
arr = data["speed_map"]
print(arr.shape)
print(arr.min(), arr.max(), arr.mean())
PY
```

Expected shape:

```text
(360,)
```

Inspect these plots before trusting the event input:

- `wsaplus_speed_map_<event>.png`
- `huxt_input_speed_profile_<event>.png`
- `huxt_input_speed_difference_<event>.png`
- `huxt_input_subearth_track_<event>.png`

---

## 8. Common problems

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `Missing events CSV` | Wrong working directory or `--events-file` path. | Run from the repo root or pass the full CSV path. |
| `missing required columns` | The event CSV schema changed. | Add the required columns listed above. |
| `No GONG .fits files found` with `--no-download` | The event directory has no local magnetograms. | Remove `--no-download` or place GONG FITS files in `data_dir/sw/<event>/`. |
| WSA+ checkpoint not found | `wsaplus.pt` is not under the output root. | Pass `--checkpoint-path /path/to/wsaplus.pt`. |
| Event skipped at config stage | `event_config.yaml` already exists. | Use `--force-config` if you intentionally changed seed parameters. |
| Boundary looks wrong | Bad or old GONG files, wrong event time, or stale WSA+ cache. | Inspect plots; delete the event-specific cached WSA+ file if rerunning WSA+ is needed. |

---

## 9. Minimal workflow for a new event

1. Add a row to `data_dir/events.csv`.
2. Confirm `enabled` is `true`.
3. Ensure `wsaplus.pt` exists at `data_dir/sw/wsaplus.pt`, or pass `--checkpoint-path`.
4. Run:

```bash
python scripts/generate_huxt_input.py --event <event>
```

1. Inspect the generated plots.
2. Confirm `v_boundary_<event>.npz` has shape `(360,)`.

At that point the event has a prepared HUXt background boundary and seed CME metadata.
