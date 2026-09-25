# Known issues

Status: 24 September 2026, `dev` branch. Found with a full link check of all three books
(`scripts/check_site_links.py`, including `--external`).

**English:** every link, image and anchor on English pages works, except the items listed below
that need content (empty links, missing files).
**Spanish and French:** 106 broken links and images on pages in the table of contents.

Run the check yourself after building the books:

```bash
python scripts/check_site_links.py              # internal links, images, anchors
python scripts/check_site_links.py --external   # also external URLs (slow)
```

---

## 1. Spanish and French pages

These pages come from Crowdin. Most problems are the same ones already fixed in the English
source, so they'll mostly clear up with the next **Crowdin Download and Merge** run. Check
again afterwards.

| Problem | Spanish | French |
|---|---|---|
| "Home" and other card links pointing to `intro.md` / `es_intro.md` / `fr_intro.md` (no `:link-type: doc`) | 40 | 25 |
| Card links without `.html` (only work on GitHub Pages) | – | 8 |
| Links to pages that aren't translated yet (the `.md` is left in the link) | 14 | 3 |
| Images and logos with wrong paths or old file names | 5 | 10 |

The image and logo fixes that still need to reach Spanish and French:

- Module 3 digitisation and georeferencing icons, Module 4 single-labels icon (renamed files)
- `qgis_3.44_run_model.png` in the French cyclone trigger page (now `qgis_3.40_run_model.png`)
- `Wiki/fig/quickosmplugin.png` in the Spanish plugins wiki (now `en_quickosmplugin.png`)
- Partner logos on the French About page: use `../_static/...` (the logos are now copied into
  each book's `_static/` folder)

Also:

- `fr_intro.md` and `es_intro.md`: the "Start teaching" / "Start learning" cards link to `.md`
  files, which don't work as card links.
- `fr_config.yml`: the licence line in the footer is still in Spanish.

## 2. Missing content

- **French Trainers' corner:** `content/fr/Trainers_corner/` is empty. `fr_intro.md` links to the
  English page instead.
- **French contribution plan:** `fr_contribution_plan.md` doesn't exist yet.
- **Colombia MHU exercise track** (`Exercise_tracks/mobile_health_training/`): the overview
  page still has "PLACEHOLDING TEXT" in the Context box, and the Track B card has no link.
- **Cards with an empty `:link:`**, which need a destination:
  - `Exercise_tracks/en_public_health_outbreak_and_preparedness.md`
  - `Exercise_tracks/mobile_health_training/en_ex_track_mobile_health_overview.md` (Track B)
  - `Exercise_tracks/mobile_health_training/en_module_5_mobile_health_ex_1.md`
  - `Exercise_tracks/mobile_health_training/en_module_5_mobile_health_ex_1_3.md`
- **Text links with no target** (`[text]()`), which need a file or page:
  - `GIS_AA/en_south_madagascar_drought_EAP.md`: `MDG_DROUGHT_EAP.qgz`
  - `Mobile_Data_collection/en_SMT_ex3_.md`: "EVCA Sketch Map Tool Slides"
  - `Mobile_Data_collection/en_SMT_ex5_.md`: prepared vectors ("here") and "XX Chapter"

## 3. External links

### Downloads on nexus.heigit.org (need server access)

These return 404:

| File | Used on |
|---|---|
| `Module_7/Exercise_1.zip` | `Module_7/*_qgis_module_7_ex1.md` (en, es) |
| `sketch_map_tool_training/Exercise_2.zip` | `en_SMT_ex2_.md`, `en_SMT_ex2_old.md` |
| `sketch_map_tool_training/Sketch_Map_Tool_Exercise_6.zip` | `en_SMT_ex6_.md` |
| `sketch_map_tool_training/Sketch_Map_Tool_Exercise_2_and_3/Case_1_marked_maps_results.zip` | `en_SMT_ex1_.md` |

### Videos that don't play (24)

The video address inside `src="..."` has a line break before `.mp4`
(for example in `Module_4/en_module_4_operation_maps.md`). The video files are in `fig/`. The fix
is to join the line. This affects Module 4 and 6 pages and the Spanish map-making and
visualisation wiki pages.

Separately, `fig/SRCS_trigger_export_image_pdf.mp4` (drought trigger Somalia) doesn't exist.

### Links to old site addresses (11)

Links to `giscience.github.io/gis-training-resource-center/english/content/...` or
`/content/fr/...` no longer work. Most are on `*_OLD` pages. The ones on live pages:

- `Mobile_Data_collection/en_SMT_ex4_.md` (digitisation page)
- `fr/Module_2/fr_data_sources.md`, `fr/Module_3/fr_qgis_module_3_ex5.md`

These should become relative links to the `.md` file.

### Other GitHub links (Spanish wiki)

`es_qgis_common_errors_and_Issues.md` links to repo paths that no longer exist
(`/content/es/...`, `/spanish/content/...`, `fig/GIS_Project_folder_template.zip`).

### Third-party sites

About 40 external links fail. 24 of them return 403/400, which usually means the site blocks
automated checks. Worth checking by hand:

- `manual.forecast-based-financing.org/.../set-the-trigger/` (drought trigger Somalia)
- Copernicus global land cover page (cyclone trigger Madagascar)
- HeiGIT ohsome quality analyst pages (SMT exercises 1 and 2)
- `cartong.pages.gitlab.cartong.org` learning corner (3 links, host not reachable)
- `scihub.copernicus.eu` (retired), `geonode.wfp.org`, `diva-gis.org` (Spanish)
- `pbs.gov.pk` statistical tables, FAO SWALIM land degradation layer
- `guides.mapaction.org` example image (Module 1 theory)

## 4. Localisation pipeline

- **Translated links are never rewritten.** The link-rewrite step only exists in
  `crowdin-sync-and-merge.yml`, which isn't used, and it looks for
  `rewrite_translated_links.py`, but the file is called `rewrite-translated-links.py`.
  `crowdin-download-merge.yml` has no rewrite step.
- **Sources come from `main` on purpose, for now.** `crowdin-upload-sources.yml` uploads from
  `main`, so translators work on the published English content. `crowdin-download-merge.yml`
  merges on `main` too, but opens its PR against `dev`, so translations appear in the preview
  book and go live with the next release. Once most of the platform is translated, the source
  branch moves to `dev`.
- **`crowdin-sync-and-merge.yml` isn't configured properly.** Use upload-sources and
  download-merge instead.

## 5. Repository

- **`main` isn't protected.** Branch protection (changes only through reviewed pull requests) is
  planned.
- **126 built pages aren't in any table of contents.** Examples: `*_OLD.md`, `intro_new.md`,
  `old_en_qgis_drought_trigger_somalia.md`, and French files in the English folder. They're
  still published and reachable by URL. Consider deleting or moving them.
- **Build warnings that are still shown**, and worth cleaning up over time:
  - duplicate labels and duplicate link targets
  - pages not in any table of contents
  - a missing bibtex file
  - unknown directive options
- **The MIT licence for the workflows** is only stated in the README. There's no licence file in
  `.github/workflows/`.
