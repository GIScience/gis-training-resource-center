# Known issues

Status: 29 October 2026, `main` branch. Items were checked against the Markdown sources of all
three books. External links are from the full check on 24 September 2026
(`scripts/check_site_links.py --external`) and haven't been rechecked since.

**English:** every internal link, image and anchor on English pages works, except the items
listed below that need content (empty links, missing files).
**Spanish and French:** all links were rewritten with `rewrite-translated-links.py` and the
broken image paths fixed. What's left is listed in section 1.

Run the check yourself after building the books:

```bash
python scripts/check_site_links.py              # internal links, images, anchors
python scripts/check_site_links.py --external   # also external URLs (slow)
```

### Fixed since 16 October 2026

- The site moved to gis-training.heigit.org. The old GitHub Pages site redirects there
  (`deploy-pages-redirects.yml`), and the language buttons no longer link to the old site.
- `README.md` describes the new deployment (Docker + Jenkins, release tags go live), the local
  preview (Docker or uv) and the branching: contributors fork the repository (or create a branch)
  and open pull requests into `main`; releases are tags on `main`. `dev` is no longer used.
- The licence line in the `fr_config.yml` footer is in French.
- The French Trainers' corner and the French contribution plan exist as placeholder pages, so the
  links from `fr_intro.md` work.
- A "What's new" page for readers was added (`content/en/whats_new.md`, in the About section).

---

## 1. Spanish and French pages

These pages come from Crowdin. On 16 October 2026 the links in the repo were rewritten with
`scripts/localisation/rewrite-translated-links.py` (Download and Merge runs the same script), and
the broken image and logo paths were fixed by hand. What's left:

- **Pages that aren't translated yet** have a placeholder page (103 French, 43 Spanish, created
  by `scripts/localisation/create-placeholder-pages.py`). It says the page isn't translated yet
  and links to the English page. Placeholders aren't in the French or Spanish menu. Links to a
  section of a placeholder open the top of the page until it's translated. To find them, search
  for `translation_placeholder: true`.
- **Spanish links with English section anchors** (35 on pages in the table of contents, mostly
  in `es_qgis_common_errors_and_Issues.md`): the Spanish pages don't define the English anchor
  IDs, so these links open the top of the page. See section 4.

## 2. Missing content

- **Colombia MHU exercise track** (`Exercise_tracks/mobile_health_training/`): the overview
  page still has "PLACEHOLDING TEXT" in the Context box, and the Track B card has no link.
- **Philippines Typhoon Uwan exercise** (`Module_5/en_qgis_module_5_phl_uwan_ex_1.md`, new):
  links to `Exercise_tracks/en_phl_typhoon_uwan.md`, which doesn't exist yet.
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

These returned 404 on 24 September 2026:

| File                                                                                       | Used on                                                                                                 |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `Module_7/Exercise_1.zip`                                                                  | `Module_7/fr_qgis_module_7_ex1.md`, `es_qgis_module_7_ex1.md` (the English page was retired, see above) |
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
`/content/...` no longer work, and the redirect site doesn't cover them.

- **On a live page:** `Trainers_corner/en_how_to_training.md` (lines 103 and 153, links to
  Module 2 exercise 1 and Module 5 non-spatial tools exercise 1). Replace them with relative links.
- The rest are on pages that aren't in any table of contents (`*_OLD.md`,
  `old_en_qgis_drought_trigger_somalia.md`, `md_building_blocks.md`, and
  `fr/Module_3/fr_qgis_module_3_ex5.md`, whose "next exercise" `fr_qgis_map_design_I_ex4` doesn't
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

- **Translated pages lack the English section anchors.** Download and Merge rewrites links in
  translated pages (`scripts/localisation/rewrite-translated-links.py`). Links to a translated
  page keep their `#anchor`, but most Spanish and French pages (for example the Spanish Wiki)
  don't define the English anchor IDs, so those links open the top of the page. After the rewrite
  in the repo on 16 October 2026: 108 Spanish and 5 French. The script lists them in the run summary.
- **Everything runs on `main`.** `crowdin-upload-sources.yml` uploads from `main`, and
  `crowdin-download-merge.yml` merges on `main` and opens its PR against `main`, like every other
  contribution. Translations go live with the next release.
- **Translated menus (not committed yet):** `scripts/localisation/update-translated-toc.py` and a
  new Download and Merge step that rebuilds `fr_toc.yml` / `es_toc.yml` from the English menu,
  with only translated pages, are in the working tree but not on `main` yet.
- **`crowdin-sync-and-merge.yml` isn't configured properly.** Use upload-sources and
  download-merge instead.

## 5. Repository

- **`main` isn't protected.** Branch protection (changes only through reviewed pull requests) is
  planned. This matters more now that all contributions go straight into `main` through pull
  requests.
- **`dev` and other old branches can be deleted.** `dev` is no longer used and is about 50 commits
  behind `main`. Its only own commit is the deletion of `deploy-book.yml`, which is also gone from
  `main`. Other old local branches: `dev-exercise-track`, `multilang`, `refactor`.
- **126 built pages aren't in any table of contents.** Examples: `*_OLD.md`, `intro_new.md`,
  `en_SMT_ex2_old.md`, `old_en_qgis_drought_trigger_somalia.md`. They're still published and
  reachable by URL. Consider deleting or moving them. Not every one is outdated: many exercise
  pages are only linked from their module's exercise overview.
- **Build warnings that are still shown**, and worth cleaning up over time:
  - duplicate labels and duplicate link targets
  - pages not in any table of contents
  - a missing bibtex file
  - unknown directive options
- **The MIT licence for the workflows** is only stated in the README. There's no licence file in
  `.github/workflows/`.

## 6. Move from GitHub Pages to gis-training.heigit.org

Done: Jenkins builds release tags (`0.1.0`, `0.2.0`) for the live site (and `main` for internal testing),
the old GitHub Pages site is replaced by redirects, and the README and language buttons point to
the new site. Left to do:

- **Rerun the redirect workflow** (`deploy-pages-redirects.yml`, manual) whenever pages are added
  that old links might point to.
- **Update the repository homepage URL** on GitHub (repository settings) to
  `https://gis-training.heigit.org/en/intro.html`.
