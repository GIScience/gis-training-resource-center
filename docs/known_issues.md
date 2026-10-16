# Known issues

Status: 16 October 2026, `main` branch. Internal links were checked in the Markdown sources of
all three books; external links are from the full check on 24 September 2026
(`scripts/check_site_links.py --external`).

**English:** every internal link, image and anchor on English pages works, except the items
listed below that need content (empty links, missing files).
**Spanish and French:** all links were rewritten with `rewrite-translated-links.py` and the
broken image paths fixed. What's left is listed in section 1.

Run the check yourself after building the books:

```bash
python scripts/check_site_links.py              # internal links, images, anchors
python scripts/check_site_links.py --external   # also external URLs (slow)
```

---

## 1. Spanish and French pages

These pages come from Crowdin. On 16 October 2026 the links in the repo were rewritten with
`scripts/localisation/rewrite-translated-links.py` (Download and Merge runs the same script), and
the broken image and logo paths were fixed by hand. What's left:

- **Links to pages that aren't translated yet** point at the page they will become, for example
  `fr_qgis_map_design_I.md`. Until that page exists, the link shows as plain text and the build
  logs a warning. On pages in the table of contents: 35 French, 4 Spanish. The rewrite script
  lists the missing pages in its run summary.
- **Spanish links with English section anchors** (35 on pages in the table of contents, mostly
  in `es_qgis_common_errors_and_Issues.md`): the Spanish pages don't define the English anchor
  IDs, so these links open the top of the page. See section 4.
- `fr_config.yml`: the licence line in the footer is still in Spanish.

## 2. Missing content

- **French Trainers' corner:** `content/fr/Trainers_corner/` is empty. The "Start teaching" card
  in `fr_intro.md` links to `Trainers_corner/fr_TOT_intro`, which works once it's translated.
- **French contribution plan:** `fr_contribution_plan.md` doesn't exist yet (`fr_intro.md` already
  links to it).
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
- **Retired Module 7 exercise 1:** the English page was removed, because its seven tasks are now
  the Madagascar cyclones exercise track. The Module 7 pages link to the track instead. The old
  address (`/en/Module_7/en_qgis_module_7_ex1.html`) now returns 404. The French and Spanish copies
  (`fr_qgis_module_7_ex1.md`, `es_qgis_module_7_ex1.md`) and the link in `es_module_7_overview.md`
  are still there and need removing or repointing.

## 3. External links

### Downloads on nexus.heigit.org (need server access)

These return 404:

| File                                                                                       | Used on                                                                                                 |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `Module_7/Exercise_1.zip`                                                                  | `Module_7/fr_qgis_module_7_ex1.md`, `es_qgis_module_7_ex1.md` (the English page was retired, see below) |
| `sketch_map_tool_training/Exercise_2.zip`                                                  | `en_SMT_ex2_.md`, `en_SMT_ex2_old.md`                                                                   |
| `sketch_map_tool_training/Sketch_Map_Tool_Exercise_6.zip`                                  | `en_SMT_ex6_.md`                                                                                        |
| `sketch_map_tool_training/Sketch_Map_Tool_Exercise_2_and_3/Case_1_marked_maps_results.zip` | `en_SMT_ex1_.md`                                                                                        |

### Missing video

`fig/SRCS_trigger_export_image_pdf.mp4` doesn't exist. It's used in the drought trigger Somalia
page and in the English and French cyclone trigger Madagascar pages.

Some video addresses have a line break before `.mp4` (16 in English, 32 in Spanish, for example
in `Module_4/en_module_4_operation_maps.md`). These videos still play, because browsers remove
line breaks from URLs. This was checked on the live site on 25 September 2026.

### Links to old site addresses

Links to `giscience.github.io/gis-training-resource-center/english/content/...` or
`/content/...` no longer work. The ones on live pages were fixed on 16 October 2026. The rest are
on pages that aren't in any table of contents (`*_OLD.md`, `old_en_qgis_drought_trigger_somalia.md`,
and `fr/Module_3/fr_qgis_module_3_ex5.md`, whose "next exercise" `fr_qgis_map_design_I_ex4` doesn't
exist in any language).

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

- **Translated pages lack the English section anchors.** Download and Merge now rewrites links
  in translated pages (`scripts/localisation/rewrite-translated-links.py`). Links to a translated
  page keep their `#anchor`, but most Spanish and French pages (for example the Spanish Wiki)
  don't define the English anchor IDs, so those links open the top of the page. In the September
  2026 test run: 108 Spanish and 15 French links; after the rewrite in the repo on 16 October 2026: 108 Spanish and 5 French. The script lists them in the run summary.
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

## 6. Move from GitHub Pages to gis-training.heigit.org

The `add-deployment` branch replaces the GitHub Pages workflows with a Dockerfile and a Jenkins
pipeline. Every merge into `main` is deployed to a staging domain, and only releases (git tags)
go live on [gis-training.heigit.org](https://gis-training.heigit.org). These places still point
to the old GitHub Pages site:

- **`README.md`:**
  - The intro says a GitHub Action publishes the site to GitHub Pages whenever changes are
    merged into `main`. It should describe the Jenkins build: `main` goes to staging, and
    releases go live.
  - The "Live site" link and the French and Spanish links (lines 5–6) and the Contribution Plan
    link point to `giscience.github.io/gis-training-resource-center/...`.
  - The branching workflow table says every merge into `main` redeploys the live site.
- **`_launch_buttons.yml`:** the en/es/fr language buttons link to
  `giscience.github.io/gis-training-resource-center/.../intro.html`. Once the new site is live,
  these buttons would send readers back to the old site.
- **Old GitHub Pages site:** once the workflows are removed, it stops updating but stays online.
  Add a redirect to gis-training.heigit.org, or take it down, so old links and search results
  don't lead to an outdated version.
