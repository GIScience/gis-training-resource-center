::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
:link-type: doc
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Estimating Typhoon Uwan’s Exposure – A Manual Analysis Under Pressure <a id="estimating-typhoon-uwan-exposure"></a>

## Characteristics of the exercise <a id="characteristics-of-the-exercise"></a>

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training.
- It can be done as a follow-along exercise or individually as a self-study.
- It works well as a scenario exercise: participants play the GIS team of a National Society in the first days of a typhoon emergency.

:::

:::{grid-item-card}
__Exercise Track:__

This exercise is part of the [Philippines Typhoon Response Exercise Track](../Exercise_tracks/en_phl_typhoon_uwan.md)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^

- Tasks 1–6 (hazard zones): approx. 60 minutes
- Tasks 7–10 (population, agriculture, health sites): approx. 75 minutes
- Tasks 11–13 (visualisation, prior impact, export): approx. 45 minutes
- Discussion: 20–30 minutes

:::

:::{grid-item-card}
__Relevant Wiki Articles__
^^^

* [Zonal Statistics](../Wiki/en_qgis_raster_basic_wiki.md#zonal-statistics)
* [Basic Raster Operations](../Wiki/en_qgis_raster_basic_wiki.md)
* [Spatial Queries](../Wiki/en_qgis_spatial_queries_wiki.md)
* [Non-Spatial Queries](../Wiki/en_qgis_non_spatial_queries_wiki.md)
* [Manipulating the Attribute Table](../Wiki/en_qgis_table_functions_wiki.md)
* [Spatial Processing](../Wiki/en_qgis_geoprocessing_wiki.md)
* [Projections](../Wiki/en_qgis_projections_wiki.md)
* [Graduated classification](../Wiki/en_qgis_graduated_wiki.md)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Aim of the exercise:__
In this exercise you will estimate, step by step and without a model, how many people, how much cropland and how many health facilities lie within the wind zones of Typhoon Uwan (Fung-wong, November 2025). Instead of one fixed buffer you will use the wind radii reported for the storm to create a gale-force zone and a typhoon-force zone. Finally, you will flag which provinces had already been hit by Typhoon Tino a few days earlier, because these are the places where response capacity is most stretched.
^^^

:::

## Instructions for the trainers <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Trainers Corner__

### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material. Run through all tasks once yourself and note down your results. They will be useful as reference values for participants (see [Results](#results)).
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions.
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Ask participants about their computer specifications beforehand. The population and land cover rasters for the whole Philippines are a few hundred MB. On slow machines, consider providing rasters already cut to Luzon.
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md) for some general tips on facilitating trainings.

### Conduct the training <a id="conduct-the-training"></a>

__Introduction (scenario briefing):__

- Introduce the context (see the Context box below). Make clear that participants are standing at the beginning of the emergency: the earthquake and Typhoon Tino have already happened, and Typhoon Uwan is approaching.
- Before opening QGIS, ask the group:
    - Which operations have you been part of where information management helped you, or where it was missing?
    - What can we do with GIS at this stage of the emergency?
    - What would the different sectors or clusters (shelter, health, food security and livelihoods, logistics) need to know from us?
    - Which data would we need, and where could we find it? Collect the answers on the whiteboard and compare them afterwards with the datasets in the folder.
    - Do we have a 3W (Who does What Where) map? Where would we look for previous situation reports?
- Short comment: if a map is only available as an image or PDF (for example in a situation report), the [Georeferencer](../Module_3/en_qgis_georeferencing.md) can be used to bring it into QGIS.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project.
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.
- Tasks 7 to 10 repeat the same logic for different datasets. Once participants have understood the population steps, faster participants can continue on their own while you support the others.

__Wrap up:__

- Use the discussion questions in the [Results](#results) section.
- Point out that every step done manually here can later be automated with the Model Designer (see the Madagascar exercise track).
- Leave some time for open questions.

:::

:::{dropdown} __Trainers Corner: Preparing the data folder__

The data folder should follow the [standard folder structure](../Wiki/en_qgis_projects_folder_structure_wiki.md#standard-folder-structure). The following files are expected in `data/input`. The file names below are the names used in the instructions; rename the downloaded files accordingly.

| File name in exercise | How to prepare it |
| --- | --- |
| `IBTrACS_WP_2025_points.gpkg` | Download the Western Pacific (WP) **points** shapefile from the [IBTrACS v04r01 shapefile folder](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/shapefile/). In QGIS, extract all features with `"SEASON" = 2025` and save as GeoPackage (EPSG:4326). This keeps the file small but still requires participants to find the right storm. |
| `phl_adm2_provinces.gpkg` | Download the administrative boundaries from [HDX (COD-AB Philippines)](https://data.humdata.org/dataset/cod-ab-phl). Use admin level 2 (provinces). Check that the fields `ADM2_EN` and `ADM2_PCODE` exist. |
| `phl_pop_2025_100m.tif` | Download the 2025 population count raster at 100 m resolution from [HDX (WorldPop Philippines)](https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-phl). |
| `phl_worldcover_2021_100m.tif` | Download the [ESA WorldCover 2021](https://esa-worldcover.org/) tiles covering the Philippines. The 10 m data is too large for a training, so mosaic the tiles and resample them, e.g. `gdalbuildvrt wc.vrt *.tif` followed by `gdalwarp -t_srs EPSG:32651 -tr 100 100 -r mode -co COMPRESS=DEFLATE wc.vrt phl_worldcover_2021_100m.tif`. The raster must be in **EPSG:32651** with **100 m pixels**, because Task 9 relies on each pixel being exactly 1 hectare. |
| `phl_healthsites_osm.gpkg` | Export health facilities for the Philippines with the [HOT Export Tool](https://export.hotosm.org/) (or download them from [healthsites.io](https://healthsites.io/)). Keep the fields `name`, `amenity` and `healthcare`. Convert polygons to points (centroids) so that all facilities are points. |
| *optional:* `phl_pop_age_sex_2025_*.tif` | For the optional vulnerability extension: [WorldPop age and sex structures](https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-phl). Use the 1 km version to save space. |

Note: 2025 storms are still **provisional** tracks in IBTrACS and are usually replaced by reanalysed best tracks within about two years. If you rebuild the data folder later, check whether the wind radii fields have changed.

:::

## Available Data <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/TODO_PHL_UWAN_DATA.zip

__Download all datasets here, save the folder on your computer and unzip the file.__

:::

The folder contains the whole [standard folder structure](../Wiki/en_qgis_projects_folder_structure_wiki.md#standard-folder-structure) with all data in the input folder and the additional documentation in the documentation folder.

| Dataset | Source | Description |
| ----- | --- | --- |
| Tropical cyclone tracks | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) | All storm positions of the 2025 Western Pacific season as points. Each point contains the position, time, wind speed and the wind radii reported by the different agencies. Tracks from 2025 are provisional. |
| Administrative boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-phl) | Province boundaries (admin level 2) of the Philippines, provided by OCHA. |
| Population | [WorldPop](https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-phl) | Estimated number of people per 100 m grid cell for 2025. This is a modelled dataset, not a census count. |
| Land cover | [ESA WorldCover 2021](https://esa-worldcover.org/) | Land cover classes, resampled to 100 m and reprojected to EPSG:32651. Class `40` is cropland. |
| Health facilities | [HOT Export Tool](https://export.hotosm.org/) | Health facilities from OpenStreetMap. Completeness depends on how well an area has been mapped. |


::::{card}
__Context__
^^^

:::{figure} ../../../fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC-icons-colour_SURGE
---
:::

It is **7 November 2025**. About a month ago, a magnitude 6.9 earthquake struck Cebu. Between 4 and 5 November, **Typhoon Tino (Kalmaegi)** made multiple landfalls across the Visayas and Palawan, causing flooding, landslides and widespread damage. Volunteers, staff and relief stocks are already committed to these two operations.

Now a second storm, **Typhoon Uwan (Fung-wong)**, is intensifying east of the Philippines and heading towards Luzon. The Philippine Red Cross has just activated its Early Action Protocol for typhoons. Interestingly, the protocol was not activated for Tino a week earlier.

**Joy** works in the information management team of the Philippine Red Cross. The operations team asks her one question:

> Where will Uwan hit people, crops and health services the hardest, and which of these places are already struggling after Tino?

There is no time to build an automated model. Joy has to do the analysis by hand, quickly and in a way she can explain to the operations team.

::::

:::{note}
In this exercise we use the observed IBTrACS track of Uwan and treat it as if it were the latest forecast. In a real operation you would work with forecast tracks and wind fields from PAGASA, JTWC or JMA, which change with every update.
:::

% TODO figure: workflow diagram (track points -> wind zones -> clip rasters / select points -> zonal statistics per province -> map and table)

# Tasks: <a id="tasks"></a>

## Part A – Preparing the hazard: from storm points to wind zones

1. **Open QGIS** and [create a new project](../Wiki/en_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` → `New`.

2. **Save the project** in the `project` folder. Click on `Project` → `Save as`, navigate to the folder and name the project `Typhoon_Uwan_Exposure`.

3. **Load the storm points and find Uwan:**
   - Load `IBTrACS_WP_2025_points.gpkg` from `data` → `input` by drag and drop ([Wiki Video](../Wiki/en_qgis_import_geodata_wiki.md#open-vector-data-via-drag-and-drop)).
   - Open the attribute table and look at the fields. Find `NAME`, `ISO_TIME` (time in UTC), `USA_WIND` (maximum wind speed in knots) and the wind radii fields `USA_R34_NE`, `USA_R34_SE`, `USA_R34_SW`, `USA_R34_NW` as well as the matching `USA_R64_…` fields.
   - The layer contains every storm of the 2025 season. To keep only Uwan, open the **Processing Toolbox** and search for `Extract by expression`.
   - Input layer: `IBTrACS_WP_2025_points`
   - Expression: `"NAME" LIKE 'FUNG%'`
   - Save the output in the `temp` folder as **`Uwan_Track_Points`**

:::{tip}
Uwan is the local Philippine name (assigned by PAGASA). IBTrACS uses the international name, **Fung-wong**. Storm names are reused over the years, so when you work with the full IBTrACS archive, always combine the name with the season, e.g. `"SEASON" = 2025 AND "NAME" LIKE 'FUNG%'`. If the expression returns nothing, check the spelling of the name in the attribute table.
:::

% TODO figure: Extract by expression dialog

4. **Create a track line for the map.** The points are useful for the analysis, but a line is easier to read on a map.
   - In the **Processing Toolbox**, search for `Points to path`.
   - Input layer: `Uwan_Track_Points`
   - Order expression: `"ISO_TIME"`
   - Save the output in the `temp` folder as **`Uwan_Track_Line`**

5. **Reproject the storm points** to a CRS that uses metres. We need metres because the buffer distances are in metres.
   - In the **Processing Toolbox**, search for `Reproject Layer`.
   - Input: `Uwan_Track_Points`
   - Target CRS: `EPSG:32651` (WGS 84 / UTM zone 51N, which covers Luzon)
   - Save the result in the `temp` folder as **`Uwan_Points_32651`**

:::{Attention}
Buffer distances must be calculated in metres. The IBTrACS data uses EPSG:4326, which measures in degrees. Always reproject to a projected CRS before buffering.
:::

6. **Calculate the wind radii in metres.** Instead of drawing one fixed circle around the track (like the 200 km buffer in the Madagascar exercise), we use the size of the wind field that was reported for each point. IBTrACS gives the **34-knot radius** (gale-force winds, about 63 km/h) and the **64-knot radius** (typhoon-force winds, about 118 km/h) for four quadrants (NE, SE, SW, NW), in **nautical miles**.
   - Open the **Field Calculator** on the layer `Uwan_Points_32651`.
   - Create a new field: name `r34_m`, type `Decimal number (real)`.
   - Expression:

     ```
     max(
       coalesce("USA_R34_NE", 0),
       coalesce("USA_R34_SE", 0),
       coalesce("USA_R34_SW", 0),
       coalesce("USA_R34_NW", 0)
     ) * 1852
     ```
   - Click `OK`.
   - Repeat the same for a field `r64_m`, replacing `R34` with `R64` in all four field names.
   - Save your edits and switch off editing mode.

:::{dropdown} Why `max`, `coalesce` and `1852`?
- `1852` converts nautical miles to metres (1 nautical mile = 1852 m).
- `max(...)` takes the largest of the four quadrants. This turns the asymmetric wind field into a circle that is as large as the widest quadrant. It is a cautious simplification: on the northern hemisphere the strongest winds are usually on the right side of the track, so the real wind field is not a circle.
- `coalesce(field, 0)` replaces missing values with 0. Early and late points of a storm often have no wind radii, and without `coalesce` the whole result would become empty (`NULL`).
:::

7. **Buffer the points with the wind radii (34-knot zone):**
   - In the **Processing Toolbox**, search for `Buffer`.
   - Input: `Uwan_Points_32651`
   - Distance: click the **Data defined override** button next to the distance field, choose `Field type: int, double` and select `r34_m`.
   - Segments: leave default (5)
   - Dissolve result: `Yes`
   - Save the output in the `temp` folder as **`Uwan_Zone_34kt`**

% TODO figure: Buffer dialog with data-defined override

8. **Repeat the buffer for the 64-knot zone** using the field `r64_m`. Save the output as **`Uwan_Zone_64kt`**.

::::{dropdown} Intermediate Result: Wind zones
% TODO figure: track line with the 34-kt and 64-kt zones over the Philippines
The 34-knot zone is a wide corridor along the track. The 64-knot zone is a much narrower corridor in its centre and only exists where Uwan had typhoon strength. Both zones should each be a single feature.
::::

:::{note}
Look closely at the 64-knot zone. Where the circles are small and the storm moved fast, you may see gaps between them. In reality the strong winds were continuous along the track. For this rapid analysis we accept the gaps, but keep them in mind when interpreting results and mention them to the operations team.
:::

9. *Optional – compare with a fixed buffer.* Buffer `Uwan_Track_Line` (after reprojecting it to EPSG:32651) by `200000` metres, as in the Madagascar exercise. Compare it with your two wind zones. Which provinces are inside the 200 km buffer but outside the 34-knot zone, and the other way round?

## Part B – Who and what is exposed?

In the next tasks we calculate, for every province, how much of each dataset lies inside the wind zones. We add the results one after another to the province layer. Each processing step creates a new layer that contains all previous columns plus the new one, so at the end you have **one layer with all results**.

10. **Load the base data:**
    - `phl_adm2_provinces.gpkg`
    - `phl_pop_2025_100m.tif` (`Layer` → `Add Layer` → `Add Raster Layer`)

11. **Calculate the total population per province.** We need it later to calculate what share of each province’s population is exposed.
    - In the **Processing Toolbox**, search for `Zonal Statistics`.
    - Input layer: `phl_adm2_provinces`
    - Raster layer: `phl_pop_2025_100m`
    - Field prefix: `pop_total_`
    - Statistics to calculate: `Sum` only
    - Save the output in the `temp` folder as **`prov_step1`**

12. **Clip the population raster to the wind zones:**
    - In the **Processing Toolbox**, search for `Clip Raster by Mask Layer`.
    - Input layer: `phl_pop_2025_100m`
    - Mask layer: `Uwan_Zone_34kt`
    - Save the output in the `temp` folder as **`Uwan_Pop_34kt`**
    - Repeat with the mask layer `Uwan_Zone_64kt` and save it as **`Uwan_Pop_64kt`**

:::{tip}
The population raster is in EPSG:4326 and the wind zones are in EPSG:32651. `Clip Raster by Mask Layer` handles the difference automatically. If you run into problems, reproject the zones to EPSG:4326 first, as done in the Madagascar exercise.
:::

::::{dropdown} Intermediate Result: Clipped population
% TODO figure: population raster clipped to the 34-kt zone
Only the population inside the 34-knot corridor should remain visible.
::::

13. **Calculate the exposed population per province:**
    - Run `Zonal Statistics` again.
    - Input layer: `prov_step1`
    - Raster layer: `Uwan_Pop_34kt`
    - Field prefix: `pop34_`
    - Statistics: `Sum`
    - Save as **`prov_step2`**
    - Run it once more with input `prov_step2`, raster `Uwan_Pop_64kt`, prefix `pop64_`, and save as **`prov_step3`**

14. **Calculate the share of exposed people.** Open the **Field Calculator** on `prov_step3` and create a new decimal field `pop34_pct`:

    ```
    round(coalesce("pop34_sum", 0) / "pop_total_sum" * 100, 1)
    ```

    Provinces that are completely outside the zone have no value in `pop34_sum`. `coalesce` turns these into 0 %.

:::{dropdown} Why look at both numbers?
The absolute number (`pop34_sum`) shows where most people are affected, which matters for the size of the response. The percentage (`pop34_pct`) shows which provinces are hit almost completely, which matters because neighbouring areas in the same province cannot easily support them. A large province with many exposed people and a small province where nearly everyone is exposed can both be priorities, for different reasons.
:::

15. **Estimate the exposed cropland.** Many households in northern and central Luzon depend on farming, so damage to crops affects livelihoods long after the storm.
    - Load `phl_worldcover_2021_100m.tif`. This land cover raster uses class `40` for cropland.
    - Open `Raster` → `Raster Calculator` and enter:

      ```
      "phl_worldcover_2021_100m@1" = 40
      ```
    - Save the output in the `temp` folder as **`cropland_binary`**. Every cropland pixel now has the value 1, every other pixel the value 0.
    - Clip `cropland_binary` with `Clip Raster by Mask Layer`, mask `Uwan_Zone_34kt`, and save it as **`Uwan_Cropland_34kt`**.
    - Run `Zonal Statistics` with input `prov_step3`, raster `Uwan_Cropland_34kt`, prefix `crop34_ha_`, statistic `Sum`, and save as **`prov_step4`**.

:::{Attention}
Each pixel of the land cover raster is 100 m × 100 m = 10,000 m² = **1 hectare**. Because cropland pixels have the value 1, the sum of the pixels in a province equals the cropland area in hectares. This only works because the raster is in a metre-based CRS with 100 m pixels.
:::

16. **Count the exposed health facilities.**
    - Load `phl_healthsites_osm.gpkg`.
    - In the **Processing Toolbox**, search for `Extract by location`.
    - Extract features from: `phl_healthsites_osm`
    - Where the features: `intersect`
    - By comparing to the features from: `Uwan_Zone_34kt`
    - Save as **`Uwan_Healthsites_34kt`**
    - Repeat with `Uwan_Zone_64kt` and save as **`Uwan_Healthsites_64kt`**
    - In the **Processing Toolbox**, search for `Count points in polygon`.
    - Polygons: `prov_step4`, Points: `Uwan_Healthsites_34kt`, Count field name: `hs34`. Save as **`prov_step5`**.
    - Run it again with polygons `prov_step5`, points `Uwan_Healthsites_64kt`, count field `hs64`. Save the result in the `result` folder as **`Uwan_Exposure_Provinces`**.

17. **Look at the facilities in the typhoon-force zone.** Open the attribute table of `Uwan_Healthsites_64kt`. Use `Select by expression` with `"amenity" = 'hospital'` to see which hospitals lie within the 64-knot zone. These are the facilities whose functioning is most at risk and which the health team should contact first.

:::{note}
OpenStreetMap coverage in the Philippines is comparatively good because of many past mapping activities, but it is not complete. A province with zero health facilities in the result may simply be poorly mapped. Compare with official facility lists (e.g. from the Department of Health) where possible.
:::

## Part C – Making the results usable

18. **Visualise the exposed population.**
    - Right-click on `Uwan_Exposure_Provinces` → `Properties` → `Symbology`.
    - Change `Single Symbol` to `Graduated`.
    - Value: `pop34_sum`
    - Colour ramp: e.g. `Reds`
    - Mode: e.g. `Natural Breaks (Jenks)` with 5 classes
    - Click `Classify`, then `OK`.
    - Add `Uwan_Track_Line` and `Uwan_Zone_64kt` on top, so the reader can see where the storm passed.

:::{tip}
Duplicate the layer (right-click → `Duplicate Layer`) to make a second map of `crop34_ha_sum` or `pop34_pct` without losing your first style. See [Module 4](../Module_4/en_module_4_overview.md) for more on styling and print layouts.
:::

% TODO figure: graduated map of exposed population with track and 64-kt zone

19. **Flag provinces already hit by Typhoon Tino.** This is the step that brings the stretched capacity into the analysis.
    - Repeat Tasks 3, 5, 6 and 7 for Tino, using the expression `"NAME" LIKE 'KALMAEGI%'` in Task 3. You only need the 34-knot zone. Save it as **`Tino_Zone_34kt`**.
    - Use `Select by Location` to select all features of `Uwan_Exposure_Provinces` that **intersect** `Tino_Zone_34kt`.
    - Open the **Field Calculator** on `Uwan_Exposure_Provinces`, make sure `Only update selected features` is **unchecked**, and create a new integer field `tino_hit`:

      ```
      if(is_selected(), 1, 0)
      ```
    - Save your edits and clear the selection.
    - Symbolise these provinces with a hatched outline on top of your population map.

:::{dropdown} Going further: other information on stretched capacity
Tino is only one part of the picture. If available, you could also add:
- the provinces affected by the Cebu earthquake,
- a 3W map showing where Red Cross and partner teams are currently deployed,
- the locations of warehouses with pre-positioned stock (see Exercise 7 of the Madagascar track for an accessibility analysis).
:::

20. **Export the results for the operations team.**
    - Right-click on `Uwan_Exposure_Provinces` → `Export` → `Save Features As…`
    - Format: `Comma Separated Value [CSV]`
    - Under `Select fields to export`, keep `ADM2_EN`, `ADM2_PCODE`, `pop_total_sum`, `pop34_sum`, `pop64_sum`, `pop34_pct`, `crop34_ha_sum`, `hs34`, `hs64` and `tino_hit`.
    - Save it in the `result` folder as **`Uwan_Exposure_Provinces.csv`**.
    - Open the CSV in a spreadsheet and sort by `pop64_sum`. These are the first provinces you would report.

## Optional extension: Who is most vulnerable?

Repeat Tasks 12 and 13 with the WorldPop age and sex rasters (e.g. children under 5 and people over 65). This helps the shelter and health teams estimate how many people will need extra support during evacuation.

# Results <a id="results"></a>

Your final layer `Uwan_Exposure_Provinces` contains, for every province, the total population, the population in the gale-force and typhoon-force zones, the share of exposed people, the exposed cropland in hectares, the number of exposed health facilities and a flag for previous impact by Tino.

% TODO figure: final map (exposed population, 64-kt zone, track, Tino-affected provinces hatched)

:::{dropdown} Reference values (for trainers)
% TODO: fill in after running the exercise with the final data folder
| Indicator | Value |
| --- | --- |
| Population in 34-kt zone | |
| Population in 64-kt zone | |
| Cropland in 34-kt zone (ha) | |
| Health facilities in 34-kt / 64-kt zone | |
| Provinces in 34-kt zone also hit by Tino | |
:::

## Discussion <a id="discussion"></a>

- How do the results change if you use the fixed 200 km buffer instead of the wind zones? Which approach would you trust more, and why?
- **Exposure is not impact.** What is missing from this analysis to say how badly people will be affected (e.g. housing quality, poverty, previous damage)?
- Our analysis only looks at **wind**. Uwan also brought heavy rain, storm surge, landslides and lahar flows. Which areas might be hit hard even though they are outside the wind zones? Which additional data would you need?
- Which crops are in the fields in November, and what does that mean for the livelihood impact?
- The operations team can only support a few provinces. How would you combine the absolute numbers, the percentages and the `tino_hit` flag to suggest priorities?
- The EAP was activated for Uwan but not for Tino, although both caused severe damage. What does that tell you about triggers and about the limits of forecasts?
- Which steps of this exercise would you automate first if a similar storm came next week?
