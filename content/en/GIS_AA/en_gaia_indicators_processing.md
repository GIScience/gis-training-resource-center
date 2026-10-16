# GAIA Pipeline Documentation <a id="gaia-pipeline-documentation"></a>

## Overview <a id="overview"></a>

The Global Aggregation of Indicators for Anticipatory Action (GAIA) Pipeline produces a series of thematic files per country, aggregated to administrative units (by default administrative level 2). It currently covers **164 countries**: 140 countries with administrative boundaries and place codes (PCODEs) from OCHA on HDX, and 24 EU countries with Eurostat NUTS regions (see [Administrative Boundaries](#administrative-boundaries)). Each file captures different aspects of population, infrastructure, and environmental conditions. Below is an overview of the available files:

1. [**Access to Services**](#1-access-to-services) – Population accessibility to key facilities such as education and health centers.  
2. [**Facilities**](#2-facilities) – Availability and distribution of essential service infrastructure.  
3. [**Coping Capacity**](#3-coping-capacity) – Combined indicators derived from Access, Facilities, Evacuability, and RAI layers.
4. [**Demographics**](#4-demographics) – Distribution of vulnerable population.
5. [**Rural Population**](#5-rural-population) – Demographic indicators focused specifically on rural populations.
6. [**Rural Accessibility Index (RAI)**](#6-rural-accessibility-index-rai) – Percentage of rural population within 2 km of a paved road.
7. [**Vulnerability**](#7-vulnerability) – Composite indicators derived from Demographics and Rural Population layers.
8. [**Flood Exposure**](#8-flood-exposure) – Exposure of populations, cropland and facilities to flood hazards.
9. [**Cyclone Exposure**](#9-cyclone-exposure) – Exposure of populations, cropland and facilities to cyclone hazards.
10. [**Evacuability**](#10-evacuability) – Travel time from at-risk areas to the nearest safe zone.

Where the files are published (HDX, public storage, interactive dashboard) is described in [Outputs and Publishing](#outputs-and-publishing).

Further details on GAIA's methodology are available in the [GAIA repository on GitHub](https://github.com/GIScience/gaia). Each chapter below links to the source code that produces the respective file.

---

:::{admonition} Information
:class: tip
The **Coping Capacity**, **Vulnerability**, and **Flood Exposure** files can be used directly as input for the Risk Assessment QGIS Plugin when analyzing flood hazards. Only minor adjustments, such as renaming the ID columns, are required for compatibility.
:::

---

## Administrative Boundaries <a id="administrative-boundaries"></a>
All indicators are aggregated to administrative units. The boundaries come from one of two sources, depending on the country.

### OCHA Common Operational Datasets (140 countries) <a id="boundaries-ocha"></a>
- **Source:** OCHA Common Operational Datasets for administrative boundaries (COD-AB), downloaded from the HDX dataset `cod-ab-{iso3}` of each country.
- **Levels:** ADM0 (country), ADM1 and ADM2. Deeper levels are not used.
- **Processing:** the boundary files are converted to GeoJSON in WGS84 (`EPSG:4326`) and lightly simplified (tolerance 0.0001°, about 10 m).
- **Identifier:** the OCHA place code (PCODE) in the column `{admin_level}_PCODE`, e.g. `ADM2_PCODE`.

### Eurostat NUTS regions (24 EU countries) <a id="boundaries-nuts"></a>
OCHA COD-AB datasets are not available for most EU countries, so these countries use the official statistical regions of the EU.

- **Countries:** AUT, BEL, BGR, CZE, DEU, DNK, ESP, EST, FIN, FRA, GRC, HRV, HUN, IRL, ITA, LTU, LVA, NLD, POL, PRT, ROU, SVK, SVN, SWE. Cyprus, Luxembourg and Malta are not included because they consist of only one or two NUTS3 regions.
- **Source:** [Eurostat GISCO NUTS 2024](https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics), scale 1:1 million, WGS84 (`EPSG:4326`).
- **Levels:**
  - **ADM2 = NUTS3** for all countries (e.g. the 400 *Kreise* in Germany, the 96 *départements* in France, the 107 *province* in Italy).
  - **ADM1 = NUTS1** for Belgium, Germany and France (regions, *Länder*, *régions*), **NUTS2** for all other countries.
  - **ADM0** is the country outline, built from the regions.
- **Not included:** the French outermost regions (Guadeloupe, Martinique, French Guiana, Réunion, Mayotte), which have their own country codes in global datasets such as WorldPop. The Canary Islands, the Azores and Madeira are included in Spain and Portugal.
- **Region names** are given in the local language in Latin script (e.g. `Stuttgart, Stadtkreis`).
- **Identifier:** the NUTS code (e.g. `DE111`). NUTS codes are hierarchical: `DE111` lies within `DE11`, which lies within `DE1`, which lies within `DE`. They are **not** OCHA place codes, so in all published files of these countries the ID columns are named after NUTS:

  | Column in OCHA countries | Column in NUTS countries |
  |---|---|
  | `ADM2_PCODE` | `NUTS3_CODE` |
  | `ADM1_PCODE` | `NUTS1_CODE` (BEL, DEU, FRA) or `NUTS2_CODE` |
  | `ADM0_PCODE` | `NUTS0_CODE` |
  | `ADM_PCODE` | `NUTS_CODE` |

  The column descriptions in the following chapters use the OCHA names; for NUTS countries, read them according to this table.
- **License:** © EuroGeographics for the administrative boundaries. This notice must be shown wherever the boundaries are displayed.

### Administrative level <a id="administrative-level"></a>
Indicators are computed for ADM2 by default. If a country has no ADM2 boundary, the next available lower level is used (ADM1, then ADM0). The file names always contain the level that was actually used, e.g. `STP_ADM1_facilities.csv`.

**Source code:** [`fetch_boundaries_hdx.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_boundaries_hdx.py) · [`fetch_boundaries_nuts.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_boundaries_nuts.py) · [`boundaries.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/boundaries.py)

---

## 1. Access to Services <a id="1-access-to-services"></a>

Represents the number of people living within defined travel distances or travel times of key facilities (education, hospitals, primary healthcare), per administrative unit.

### Data Sources <a id="data-sources"></a>

- **Accessibility isochrones** published by HeiGIT, downloaded as GeoPackage files from HeiGIT's public storage (`https://hot.storage.heigit.org/heigit-hdx-public/access/{iso3}/{ISO3}_{category}_access.gpkg`) for the categories `education`, `hospitals` and `primary_healthcare`:
  - Education: distance-based, 5 km, 10 km and 20 km.
  - Hospitals and primary healthcare: travel-time-based, 30 minutes, 1 hour and 2 hours.
- **Population data:** WorldPop age and sex structures (release R2025A, constrained, 100 m, population estimates for the year 2030), the same rasters used in [*Demographics*](#4-demographics). For processing they are aggregated to approximately 1 km resolution by summing pixel values.
- **Administrative boundaries:** see [Administrative Boundaries](#administrative-boundaries).

### Processing Steps <a id="processing-steps"></a>

1. **Load administrative boundaries** for the configured admin level (default: ADM2). If no boundary file exists for that level, the next lower level is used (ADM1, then ADM0).
2. **Download the accessibility isochrones** (GeoPackage, national layer) for each category.
3. **Prepare the population raster** (total population) from the WorldPop data.
4. For each category and cutoff:
   - Select the isochrone polygons for that cutoff.
   - Intersect them with the administrative boundaries.
   - Sum the population raster within each intersection (zonal statistics) and add up the results per administrative unit.
5. **Save the results** as a CSV with one row per administrative unit. Units with no population inside an isochrone get `0`.

### Outputs <a id="outputs"></a>

- CSV file: `{ISO3}_{ADM}_access.csv` (e.g. `AFG_ADM2_access.csv`)
  - Columns:
    - `{ADM}_PCODE` – code of the administrative unit (e.g. `ADM2_PCODE`)
    - `ADM_PCODE` – same value as `{ADM}_PCODE`, provided as a level-independent join key
    - `access_pop_education_5km`, `access_pop_education_10km`, `access_pop_education_20km`
    - `access_pop_hospitals_30min`, `access_pop_hospitals_1h`, `access_pop_hospitals_2h`
    - `access_pop_primary_healthcare_30min`, `access_pop_primary_healthcare_1h`, `access_pop_primary_healthcare_2h`
  - Units: number of people (rounded to whole persons)
  - Note: if the isochrone dataset of a country contains no polygons for a given cutoff, the corresponding column is omitted from that country's file.

**Source code:** [`fetch_access_s3.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_access_s3.py) · [`access.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/access.py)

---

## 2. Facilities <a id="2-facilities"></a>

Represents the availability and spatial distribution of essential service infrastructure (schools, hospitals and primary healthcare facilities), as the number of facilities mapped in OpenStreetMap per administrative unit.

### Data Sources <a id="data-sources-2"></a>

- **OpenStreetMap (OSM)** data, accessed through either:
  - the **ohsome API** by HeiGIT (`https://api.heigit.org/ohsome-api/v2-rc`) – default; or
  - the **Overpass API** – alternative, selectable via the pipeline configuration.
- **Administrative boundaries:** see [Administrative Boundaries](#administrative-boundaries).

### Processing Steps <a id="processing-steps-2"></a>

1. **Load administrative boundaries** for the configured admin level (default: ADM2). If no boundary file exists for that level, the next lower level is used (ADM1, then ADM0).
2. **Define OSM tag filters** for each facility type:
   - **Education:** `amenity=school`
   - **Hospitals:** `amenity=hospital` or `healthcare=hospital`
   - **Primary healthcare:** `amenity=doctors|clinic` or `healthcare=clinic|doctors|midwife|nurse|center`, excluding any feature tagged as a hospital (`amenity=hospital` or `healthcare=hospital`).
3. **Count facilities per administrative unit:**
   - **ohsome API (default):** for each administrative unit and facility type, the number of matching OSM features inside the unit's boundary polygon is requested from the ohsome statistics endpoint, using the most recent OSM data available at processing time.
   - **Overpass API:** matching OSM features are downloaded for the country's bounding box, reduced to point locations (centroids for areas), and assigned to administrative units with a spatial join.
4. **Store facility locations:** the matching OSM features for each facility type are additionally downloaded for the whole country and stored as intermediate files. They are used internally by the hazard exposure steps (e.g. [Flood Exposure](#8-flood-exposure)).
5. **Combine and export results:** the counts for all facility types are merged into one table (units with no facilities get `0`) and saved as a CSV.

### Outputs <a id="outputs-2"></a>

- CSV file: `{ISO3}_{ADM}_facilities.csv` (e.g. `AFG_ADM2_facilities.csv`)
  - Columns:
    - `{ADM}_PCODE` – code of the administrative unit (e.g. `ADM2_PCODE`)
    - `ADM_PCODE` – same value as `{ADM}_PCODE`, provided as a level-independent join key
    - `education_count`
    - `hospitals_count`
    - `primary_healthcare_count`
  - Units: number of OSM facilities per administrative unit
  - Note: counts reflect what is mapped in OpenStreetMap and depend on local mapping completeness.

**Source code:** [`fetch_facilities_ohsome_overpass.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_facilities_ohsome_overpass.py) · [`facilities.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/facilities.py)

---

## 3. Coping Capacity <a id="3-coping-capacity"></a>
Represents the ability of a population to access essential services and to move to safety when a hazard strikes.  
This layer does not compute new indicators. It combines, per administrative unit, the outputs of the *Access to Services*, *Facilities*, *Evacuability* and *Rural Accessibility Index (RAI)* layers into one table.

### Data Sources <a id="data-sources-3"></a>
- **Access to Services CSV** (`{country_code}_{admin_level}_access.csv`): population within distance/travel-time thresholds of education, hospital and primary-healthcare facilities (see [Access to Services](#1-access-to-services)).  
- **Facilities CSV** (`{country_code}_{admin_level}_facilities.csv`): number of OpenStreetMap facilities per administrative unit (see [Facilities](#2-facilities)).  
- **Evacuability CSV** (`{country_code}_{admin_level}_evacuability.csv`): travel time from flood- or cyclone-affected areas to the nearest safe area (see [Evacuability](#10-evacuability)).  
- **RAI CSV** (`{country_code}_{admin_level}_rai.csv`): rural population within 2 km of a paved road (see [Rural Accessibility Index (RAI)](#6-rural-accessibility-index-rai)).  
- All inputs refer to the same administrative level (by default ADM2).

### Processing Steps <a id="processing-steps-3"></a>
1. **Input CSVs:**  
   - The four input CSVs are read for each administrative level (default: ADM2).
   - The administrative identifier column (`ADM0_PCODE`, `ADM1_PCODE` or `ADM2_PCODE`) is taken from the Access CSV.
2. **Merge Operations:**  
   - The Access table is the base table; every administrative unit in it appears in the output.
   - Facilities columns are joined to it with a left join on the `*_PCODE` column. The Access and Facilities CSVs are both required; without them no coping file is produced.
   - Evacuability columns are joined if an Evacuability CSV exists for the country. Countries with no flood or cyclone exposure therefore have no evacuation-time columns.
   - RAI columns are joined if an RAI CSV exists.
   - Duplicate identifier columns created by the joins are merged into a single `ADM_PCODE` column.
3. **Output Generation:**  
   - The merged table is saved as `{country_code}_{admin_level}_coping.csv`.
   - One file is produced per administrative level.

### Outputs <a id="outputs-3"></a>
- **File:** `{country_code}_{admin_level}_coping.csv`
- **Columns** (in this order; a group is missing if its source layer was not available):
  - `{admin_level}_PCODE` – administrative unit code
  - **Access to services** (number of people; a column is omitted if no isochrone exists for that threshold):
    - `access_pop_education_5km`, `access_pop_education_10km`, `access_pop_education_20km`
    - `access_pop_hospitals_30min`, `access_pop_hospitals_1h`, `access_pop_hospitals_2h`
    - `access_pop_primary_healthcare_30min`, `access_pop_primary_healthcare_1h`, `access_pop_primary_healthcare_2h`
  - **Facilities** (number of facilities):
    - `education_count`, `hospitals_count`, `primary_healthcare_count`
  - **Flood evacuability** (minutes; one set per flood return period, by default RP 10, 50, 100 and 500):
    - `RP{rp}_evac_time_minutes_mean`, `RP{rp}_evac_time_minutes_max`, `RP{rp}_evac_time_minutes_median`
  - **Cyclone evacuability** (minutes; only for countries with cyclone exposure):
    - `kt34_evac_time_minutes_mean`, `kt34_evac_time_minutes_max`, `kt34_evac_time_minutes_median`
  - **Rural access** (rural population within 2 km of a paved road, persons):
    - `rural_access_children_u5`, `rural_access_dependents`, `rural_access_working`, `rural_access_elderly`, `rural_access_female_pop`, `rural_access_female_u15`, `rural_access_female_u5`, `rural_access_pop_u15`, `rural_access_total_pop`, `rural_access_wra_pop`
    - `rural_access_dependency_ratio` (dependents per 100 working-age people among the rural population with road access)
  - **Rural Accessibility Index** (% of the respective rural population group within 2 km of a paved road):
    - `RAI_total_pop`, `RAI_female_pop`, `RAI_children_u5`, `RAI_female_u5`, `RAI_elderly`, `RAI_pop_u15`, `RAI_female_u15`, `RAI_wra_pop`
  - `ADM_PCODE` – administrative unit code (same as `{admin_level}_PCODE`, kept for compatibility)
- **Format:** tabular CSV without geometry; join it to the boundary layer via `{admin_level}_PCODE`.
- **Units:** population counts, facility counts, minutes (1 decimal) and percentages (1 decimal). Evacuation times are empty for units with no affected area.

**Source code:** [`coping.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/coping.py)

---

## 4. Demographics <a id="4-demographics"></a>
Provides population counts by **age** and **sex** for each administrative unit.  
This layer is derived from the [**WorldPop**](https://www.worldpop.org/) age/sex-structured population estimates and quantifies population groups that are often more vulnerable to hazards (children, elderly people, women of reproductive age).

### Data Sources <a id="data-sources-4"></a>
- **WorldPop Age-Sex Population Rasters:**  
  [WorldPop global age/sex structures](https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/), series `Global_2015_2030`, release `R2025A`, constrained version (population only allocated to built-up areas), 100 m resolution, year **2030** (projected estimates).  
  One raster per sex (`f`, `m`) and age group: `0` (under 1), `1` (1–4), then 5-year groups `5`–`75`, and `80` (80 and older).
- **Administrative boundaries:** used to aggregate the rasters per administrative unit, at the configured administrative level (default: ADM2; see [Administrative Boundaries](#administrative-boundaries)).

### Indicators <a id="indicators"></a>
Each population indicator is the **sum of WorldPop population counts** over the listed age groups and sexes:

| Indicator          | Description                                      | Ages (years)      | Sexes |
|--------------------|--------------------------------------------------|-------------------|-------|
| `total_pop`        | Total population                                 | all (0 – 80+)     | f, m  |
| `female_pop`       | Total female population                          | all (0 – 80+)     | f     |
| `children_u5`      | Children under 5                                 | 0–4               | f, m  |
| `female_u5`        | Female children under 5                          | 0–4               | f     |
| `elderly`          | Population aged 65 and above                     | 65+               | f, m  |
| `pop_u15`          | Population under 15                              | 0–14              | f, m  |
| `female_u15`       | Female population under 15                       | 0–14              | f     |
| `wra_pop`          | Women of reproductive age                        | 15–49             | f     |
| `dependency_ratio` | Dependents (ages 0–14 and 65+) per 100 people of working age (15–64) | derived | f, m |

### Processing Steps <a id="processing-steps-4"></a>
1. **Download WorldPop Rasters**  
   - All age/sex rasters needed for the indicators are downloaded for the country (`Global_2015_2030` / `R2025A` / `2030`, constrained, 100 m).
2. **Sum Rasters per Indicator**  
   - For each indicator, the matching age/sex rasters are added together into one raster.  
   - During this step the 100 m grid is aggregated to approximately 1 km by summing blocks of cells, so population totals are preserved.
3. **Aggregate by Administrative Units**  
   - For each administrative unit, the population of all ~1 km grid cells whose centre lies inside the unit is summed (zonal sum).  
   - If the boundary for the requested level is not available, the next coarser level (ADM1, then ADM0) is used.  
   - Results are rounded to whole persons; missing values are set to 0.
4. **Derive Dependency Ratio**  
   - `dependency_ratio = (population aged 0–14 and 65+) / (population aged 15–64) × 100`, rounded to 2 decimals. Units with no working-age population get 0.
5. **Output**  
   - One CSV per country and administrative level: `{country_code}_{admin_level}_demographics.csv`.

### Outputs <a id="outputs-4"></a>
- **File:** `{country_code}_{admin_level}_demographics.csv`  
- **Columns:**
  - `{admin_level}_PCODE` – administrative unit code
  - `ADM_PCODE` – same code, kept for compatibility
  - `total_pop`
  - `female_pop`
  - `children_u5`
  - `female_u5`
  - `elderly`
  - `pop_u15`
  - `female_u15`
  - `wra_pop`
  - `dependency_ratio`
- **Format:** tabular CSV without geometry; join it to the boundary layer via `{admin_level}_PCODE`.  
- **Units:** population counts (whole persons, 2030 estimates); `dependency_ratio` in dependents per 100 working-age persons (2 decimals).

**Source code:** [`fetch_worldpop.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_worldpop.py) · [`demographics.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/demographics.py)

---

## 5. Rural Population <a id="5-rural-population"></a>

Estimates how many people live in **rural areas** within each administrative unit, broken down by demographic group, together with the overall share of the population that is rural and the dependency ratio of the rural population. Rural areas are defined using the **Global Human Settlement Layer Settlement Model (GHS-SMOD)**: grid cells classified as very low density rural, low density rural or rural cluster.

This layer combines **WorldPop population rasters** with the **GHS-SMOD** settlement classification to estimate rural populations for each demographic group.

### Data Sources <a id="data-sources-5"></a>

- **WorldPop Population Rasters:**  
  [WorldPop Age-Sex structures](https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/), release R2025A, constrained, projection year **2030**, 100 m resolution, aggregated to roughly 1 km for processing.  
  The same demographic rasters are used as in the *Demographics* chapter.  
- **GHS-SMOD (Settlement Model) Raster:**  
  [GHS-SMOD R2023A, epoch 2030, 1 km, Mollweide](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_SMOD_GLOBE_R2023A/GHS_SMOD_E2030_GLOBE_R2023A_54009_1000/V2-0/), from the JRC Global Human Settlement Layer.  
  Used to classify grid cells as **rural** or **urban**.
- **Administrative Boundaries:**  
  Boundary files for the configured administrative level (default: ADM2) define the spatial units used for aggregation (see [Administrative Boundaries](#administrative-boundaries)).

### Processing Steps <a id="processing-steps-5"></a>

1. **Download GHS-SMOD Raster**  
   - The global GHS-SMOD 2030 raster (R2023A, 1 km) is downloaded from the JRC GHSL repository.  
2. **Reclassify SMOD Raster**  
   - Converts the original SMOD classes into two classes:  
     - **Rural = 1** (classes 11–13: very low density rural, low density rural, rural cluster)  
     - **Urban = 2** (classes 21–23 and 30: suburban/peri-urban, semi-dense and dense urban cluster, urban centre)  
     - **Water (class 10) and no data** are excluded.  
3. **Fetch WorldPop Demographic Indicators**  
   - Uses the WorldPop rasters for total population, female population, children under 5, female children under 5, elderly (65+), population under 15, females under 15, women of reproductive age (15–49), dependents (ages 0–14 and 65+) and working-age population (15–64), shared with the *Demographics* layer.  
4. **Compute Rural Population**  
   - Aligns the reclassified SMOD raster to the WorldPop grid.  
   - Keeps only population in rural cells (SMOD class 1).  
   - Sums rural population per administrative unit for each demographic group.  
5. **Derive Ratios**  
   - **Rural dependency ratio** = rural dependents / rural working-age population × 100 (0 if there is no working-age population).  
   - **Rural population share** = rural total population / total population of the unit × 100.  
6. **Output Generation**  
   - Writes one CSV per country and administrative level. Population counts are rounded to whole people; ratio and percentage are rounded to two decimals.

### Outputs <a id="outputs-5"></a>

- CSV file: `{country_code}_{admin_level}_rural_population.csv` (e.g. `AFG_ADM2_rural_population.csv`)
  - Columns:
    - `{admin_level}_PCODE` – administrative unit code
    - `ADM_PCODE` – copy of the administrative unit code (level-independent join key)
    - `total_pop_rural`, `female_pop_rural`, `children_u5_rural`, `female_u5_rural`
    - `elderly_rural`, `pop_u15_rural`, `female_u15_rural`, `wra_pop_rural` – rural population counts per demographic group
    - `dependency_ratio_rural` – rural dependency ratio (dependents aged 0–14 and 65+ per 100 people aged 15–64)
    - `rural_pop_perc` – percentage of the unit's total population living in rural areas
  - Units: number of people (integers); ratio and percentage per administrative unit (two decimals)

**Source code:** [`fetch_ruralness_ghsl.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_ruralness_ghsl.py) · [`rural.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/rural.py)

---

## 6. Rural Accessibility Index (RAI) <a id="6-rural-accessibility-index-rai"></a>

Computes the percentage of rural population living within 2 km of a paved road. The Rural Accessibility Index measures the proportion of people living in rural areas (GHS-SMOD classes 11–13) whose location lies within a 2 km straight-line buffer around a paved road. Results are provided for multiple demographic groups, together with the dependency ratio of the accessible rural population.

### Data Sources <a id="data-sources-6"></a>

- **Road Surface Data:** HeiGIT road surface datasets (published on HDX), combined where both are available:  
  - Mapillary-based road surface classification ([downloads.ohsome.org/hdx/mapillary_road_surface](https://downloads.ohsome.org/hdx/mapillary_road_surface/)); roads predicted as paved (`pred_label == 0`) are used.  
  - Planet imagery-based road surface classification ([hot.storage.heigit.org/heigit-hdx-public/planet_road_data](https://hot.storage.heigit.org/heigit-hdx-public/planet_road_data/)); roads classified as paved (`DL_road_class_2024 == "paved"`) are used.  
- **GHS-SMOD Raster:** Global Human Settlement Layer Settlement Model, R2023A, epoch 2030, 1 km (same file as in *Rural Population*), used to identify rural cells (classes 11–13).
- **WorldPop Population Rasters:** WorldPop Age-Sex structures R2025A, constrained, 2030 (same data as in *Demographics*), used to count population per demographic group within accessible rural areas.
- **Rural Population** output (see *Rural Population*): provides the rural population per group used as denominator.
- **Administrative Boundaries** (default level ADM2, see [Administrative Boundaries](#administrative-boundaries)): used to report results per administrative unit.

### Indicators <a id="indicators-6"></a>

| Indicator | Description | Units |
|-----------|-------------|-------|
| `rural_access_{group}` | Rural population living within 2 km of a paved road | people |
| `RAI_{group}` | Rural Accessibility Index = `rural_access_{group}` / `{group}_rural` × 100 | % |
| `rural_access_dependency_ratio` | Dependency ratio of the accessible rural population (dependents aged 0–14 and 65+ per 100 people aged 15–64) | % |

Groups with both `rural_access_` and `RAI_` values: `total_pop`, `female_pop`, `children_u5`, `female_u5`, `elderly`, `pop_u15`, `female_u15`, `wra_pop`. For `dependents` and `working` only the `rural_access_` counts are provided; they are used for the dependency ratio.

### Processing Steps <a id="processing-steps-6"></a>

1. **Download road surface data** (Mapillary- and Planet-based) for the country and keep paved roads only. If only one source is available, it is used alone.
2. **Buffer paved roads by 2 km** in a projected coordinate system (UTM zone estimated from the country centroid) and merge the buffers into one road service area.
3. **Prepare GHS-SMOD**: reclassify into rural / urban / excluded (as in *Rural Population*) and clip to the country boundary.
4. **Vectorize rural cells** (SMOD classes 11–13) into rural area polygons.
5. **Intersect rural areas with the road service area** to obtain accessible rural areas.
6. **Intersect accessible rural areas with the administrative units.**
7. **Sum WorldPop population** for each demographic group within the accessible rural area of each unit.
8. **Load rural population totals** from the *Rural Population* output as denominator.
9. **Compute RAI:** `rural_access_{group} / {group}_rural × 100`, rounded to one decimal; set to 0 where a unit has no rural population.
10. **Compute dependency ratio:** `rural_access_dependents / rural_access_working × 100`, rounded to one decimal; left empty where there is no accessible working-age population.
11. **Write CSV** with one row per administrative unit. If no paved road data is available for a country, or no accessible rural area is found, the file contains only the administrative unit codes.

### Outputs <a id="outputs-6"></a>

- **File:** `{country_code}_{admin_level}_rai.csv` (e.g. `AFG_ADM2_rai.csv`)
- **Columns:**
  - `{admin_level}_PCODE`
  - `rural_access_children_u5`, `rural_access_dependents`, `rural_access_working`
  - `rural_access_elderly`, `rural_access_female_pop`, `rural_access_female_u15`
  - `rural_access_female_u5`, `rural_access_pop_u15`, `rural_access_total_pop`
  - `rural_access_wra_pop`, `rural_access_dependency_ratio`
  - `RAI_total_pop`, `RAI_female_pop`, `RAI_children_u5`, `RAI_female_u5`
  - `RAI_elderly`, `RAI_pop_u15`, `RAI_female_u15`, `RAI_wra_pop`
- **Units:** population counts (whole people); RAI and dependency ratio in % (one decimal)

**Source code:** [`compute_rai.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/compute_rai.py) · [`rai.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/rai.py)

---

## 7. Vulnerability <a id="7-vulnerability"></a>
Represents the sensitivity of a population to external shocks based on its demographic composition and on how much of it lives in rural areas.  
This layer does not compute new indicators. It combines, per administrative unit, the outputs of the *Demographics* and *Rural Population* layers into one table.

### Data Sources <a id="data-sources-7"></a>
- **Demographics CSV** (`{country_code}_{admin_level}_demographics.csv`): population by age and sex from [WorldPop](https://www.worldpop.org/) (see [Demographics](#4-demographics)).  
- **Rural Population CSV** (`{country_code}_{admin_level}_rural_population.csv`): the same population groups counted only in rural areas, based on the GHSL Settlement Model (SMOD) (see [Rural Population](#5-rural-population)).  
- Both datasets refer to the same administrative level (by default ADM2).

### Processing Steps <a id="processing-steps-7"></a>
1. **Input CSVs:**  
   - One Demographics CSV and one Rural Population CSV are read for each administrative level.  
   - The administrative identifier column (`ADM0_PCODE`, `ADM1_PCODE` or `ADM2_PCODE`) is taken from the Demographics CSV.

2. **Merge Operation:**  
   - The two tables are joined on the `*_PCODE` column using a **left join** on the Demographics table, so every administrative unit with demographic data is kept, even if rural population values are missing.  
   - Duplicate identifier columns created by the join are merged into a single `ADM_PCODE` column.

3. **Output Generation:**  
   - The merged table is saved as `{country_code}_{admin_level}_vulnerability.csv`.  
   - One file is produced per administrative level.

### Outputs <a id="outputs-7"></a>
- **File:** `{country_code}_{admin_level}_vulnerability.csv`
- **Columns:**
  - `{admin_level}_PCODE` – administrative unit code
  - **Demographics** (see [Demographics](#4-demographics)):
    - `total_pop`, `female_pop`, `children_u5`, `female_u5`, `elderly`, `pop_u15`, `female_u15`, `wra_pop` – population counts
    - `dependency_ratio` – dependents (0–14 and 65+) per 100 working-age persons (15–64)
  - **Rural population** (see [Rural Population](#5-rural-population)):
    - `total_pop_rural`, `female_pop_rural`, `children_u5_rural`, `female_u5_rural`, `elderly_rural`, `pop_u15_rural`, `female_u15_rural`, `wra_pop_rural` – population counts in rural areas
    - `dependency_ratio_rural` – dependency ratio of the rural population
    - `rural_pop_perc` – share of the total population living in rural areas (%)
  - `ADM_PCODE` – administrative unit code (same as `{admin_level}_PCODE`, kept for compatibility)
- **Format:** tabular CSV without geometry; join it to the boundary layer via `{admin_level}_PCODE`.  
- **Units:** population counts (whole persons); ratios per 100 working-age persons and percentages (2 decimals).

**Source code:** [`vulnerability.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/vulnerability.py)

---

## 8. Flood Exposure <a id="8-flood-exposure"></a>
Estimates the exposure of population, cropland and critical facilities to riverine flooding using the **JRC GloFAS flood hazard maps** (flood depth for several return periods), **WorldPop demographic layers** and **ESA WorldCover cropland**. A location counts as flooded when the modelled flood depth exceeds a threshold (default 30 cm). Exposure metrics are aggregated per administrative unit.

This layer provides indicators for the number of people affected per demographic group, the flooded cropland area, and the number and percentage of critical facilities (education, hospitals, primary healthcare) affected by flood events of different return periods (RPs).

### Data Sources <a id="data-sources-8"></a>
- **GloFAS Flood Hazard Maps** (`https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/`)  
  Flood depth rasters (in metres, ~100 m resolution) from the JRC Copernicus Emergency Management Service, one set per return period. The pipeline supports return periods of 10, 50, 100 and 500 years.  
- **WorldPop Population Layers** (see [Demographics](#4-demographics))  
  Age- and sex-disaggregated population rasters, aggregated to a 1 km grid: female population, children under 5, female children under 5, elderly, population under 15, female population under 15, women of reproductive age, plus the dependent and working-age components of the dependency ratio.  
- **ESA WorldCover** (`https://esa-worldcover.org`)  
  10 m land cover map; the *Cropland* class is used to derive the share of cropland in each 1 km grid cell. Default release: 2021 (2020 is also available).  
- **Facilities Data** (see [Facilities](#2-facilities))  
  OSM-derived locations of education, hospital and primary healthcare facilities from the ohsome API (default) or the Overpass API.  
- **Administrative Boundaries** (see [Administrative Boundaries](#administrative-boundaries))  
  Used to aggregate flood exposure per admin level (default ADM2; if no boundary exists for the requested level, the next lower level is used).

### Indicators <a id="indicators-4"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `RP{rp}_crops_{thresh}_km2` | Cropland area flooded with depth > threshold | km² |
| `RP{rp}_female_pop_{thresh}` | Number of females affected by flood depth > threshold | people |
| `RP{rp}_children_u5_{thresh}` | Number of children under 5 affected | people |
| `RP{rp}_female_u5_{thresh}` | Number of female children under 5 affected | people |
| `RP{rp}_elderly_{thresh}` | Number of elderly (65+) affected | people |
| `RP{rp}_pop_u15_{thresh}` | Number of people under 15 affected | people |
| `RP{rp}_female_u15_{thresh}` | Number of females under 15 affected | people |
| `RP{rp}_wra_pop_{thresh}` | Number of women of reproductive age (15–49) affected | people |
| `RP{rp}_dependency_ratio_{thresh}` | Dependency ratio of the affected population: people aged 0–14 and 65+ per 100 people aged 15–64 | ratio × 100 |
| `RP{rp}_education_{thresh}_pct` | Percentage of educational facilities flooded | % |
| `RP{rp}_education_{thresh}_count` | Number of educational facilities flooded | count |
| `RP{rp}_hospitals_{thresh}_pct` | Percentage of hospitals flooded | % |
| `RP{rp}_hospitals_{thresh}_count` | Number of hospitals flooded | count |
| `RP{rp}_primary_healthcare_{thresh}_pct` | Percentage of primary healthcare facilities flooded | % |
| `RP{rp}_primary_healthcare_{thresh}_count` | Number of primary healthcare facilities flooded | count |

> `{rp}` is the return period in years (10, 50, 100, 500) and `{thresh}` is the flood depth threshold in cm (default `30cm`). Total population is not reported for floods.

### Flood Threshold <a id="flood-threshold"></a>
| Parameter | Default | Description |
|-----------|---------|-------------|
| `flood_threshold` | 0.3 m | A location counts as flooded when the flood depth is greater than this value. Its value in cm appears in the column names (e.g. `30cm`). |
| `rps` | 10, 50, 100, 500 | Return periods processed |
| `years` | 2021 | ESA WorldCover release used for cropland (2020 or 2021) |
| `api` | `ohsome-api` | Source of facility data (`ohsome-api` or `overpass`) |
| `admin_levels` | ADM2 | Administrative level(s) to aggregate to |

These defaults are part of the pipeline's run configuration and can be changed for a run in the Dagster UI.

### Processing Steps <a id="processing-steps-8"></a>
1. **Input Geometry**  
   - Loads the administrative boundaries of the country at the requested admin level (falling back to a lower level if needed).

2. **Flood Hazard Download and Clipping (per RP)**  
   - Lists the GloFAS flood depth tiles available for the return period and downloads those intersecting the country's bounding box.  
   - Clips the tiles to the country boundary and merges them into a single flood depth raster per RP.

3. **Population and Cropland Preparation**  
   - Ensures the WorldPop demographic rasters (1 km grid) exist for the country.  
   - Builds a cropland-fraction raster on the same 1 km grid from ESA WorldCover (share of each cell classified as cropland).

4. **Facility Data Preparation**  
   - Downloads or loads facility geometries from the configured API (`ohsome-api` or `overpass`); non-point geometries are reduced to their centroids.

5. **Flood Exposure Calculation per RP**  
   - **Flood mask**: The flood depth raster is resampled (bilinear) onto the 1 km population grid; cells with a resampled depth greater than the threshold form the flood mask.  
   - **Flooded population**: Each demographic raster is multiplied by the flood mask and summed per admin unit (zonal statistics). The dependency ratio is computed from the flooded dependent (0–14, 65+) and working-age (15–64) populations; it is 0 where no working-age population is flooded.  
   - **Flooded cropland**: The cropland fraction is multiplied by the flood mask and the approximate cell area, and summed per admin unit (km²).  
   - **Flooded facilities**: The flood depth is sampled at each facility location on the original-resolution flood raster; a facility counts as flooded if the depth exceeds the threshold. Count and percentage of flooded facilities are computed per admin unit and category.

6. **Aggregation and CSV Output**  
   - Merges the results for all RPs into a single table with one row per admin unit.  
   - Fills missing values with 0. Population counts, facility counts, percentages and the dependency ratio are rounded to whole numbers; cropland area keeps two decimals.  
   - Saves the CSV as `{country_code}_{admin_level}_flood_exposure.csv`.

### Outputs <a id="outputs-8"></a>
- **File:** `{country_code}_{admin_level}_flood_exposure.csv` (e.g. `AUT_ADM2_flood_exposure.csv`)  
- **Rows:** one per administrative unit  
- **Columns:**
  - `{admin_level}_PCODE` (e.g. `ADM2_PCODE`)
  - For each return period (`RP10`, `RP50`, `RP100`, `RP500`), in this order: `RP{rp}_crops_{thresh}_km2`; the seven flooded population indicators; `RP{rp}_dependency_ratio_{thresh}`; and `_pct` / `_count` for `education`, `hospitals` and `primary_healthcare`
  - With default settings: 1 + 4 × 15 = 61 columns
- **Units:** people, km², %, count

**Source code:** [`fetch_floods_jrc.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_floods_jrc.py) · [`fetch_worldcover.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_worldcover.py) · [`exposure.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/exposure.py)

---

## 9. Cyclone Exposure <a id="9-cyclone-exposure"></a>
Estimates the historical exposure of population, cropland and critical facilities to tropical cyclones using **IBTrACS** storm track data (since 1980). For every track segment where a storm had hurricane/typhoon strength (Saffir-Simpson category 1–5), the area reached by at least tropical-storm-force winds (34 knots, ≈63 km/h) is mapped and labelled with the storm's category at that time. The categories are grouped into three exposure classes (Cat 1, Cat 2–3, Cat 4–5). For each administrative unit, the exposed population per demographic group, the exposed cropland area, and the count and percentage of exposed facilities are computed per class.

### Data Sources <a id="data-sources-9"></a>
- **IBTrACS Storm Tracks** (`https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/`): International Best Track Archive for Climate Stewardship, version v04r01, all storms since 1980, downloaded from NOAA NCEI as track line segments. Used attributes: Saffir-Simpson category (`USA_SSHS`) and the radius of 34-knot winds in four quadrants (`USA_R34_NE`, `USA_R34_SE`, `USA_R34_SW`, `USA_R34_NW`).
- **WorldPop Population Rasters:** Demographic rasters on a 1 km grid used to compute exposed populations (see [Demographics](#4-demographics)).
- **ESA WorldCover** (`https://esa-worldcover.org`): 10 m land cover; the *Cropland* class is used to derive the cropland share per 1 km grid cell. Default release: 2021 (2020 is also available).
- **Facilities Data:** OSM-derived facility locations (education, hospitals, primary healthcare) from the ohsome API (default) or the Overpass API (see [Facilities](#2-facilities)).
- **Administrative Boundaries:** Used to aggregate exposure per admin level (default ADM2; if no boundary exists for the requested level, the next lower level is used; see [Administrative Boundaries](#administrative-boundaries)).

### Indicators <a id="indicators-5"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `kt34_{indicator}_cat{cls}` | Exposed population for a demographic group in exposure class `{cls}` | people |
| `kt34_dependency_ratio_cat{cls}` | Dependency ratio of the exposed population in class `{cls}`: people aged 0–14 and 65+ per 100 people aged 15–64 | ratio × 100 |
| `kt34_{facility}_count_cat{cls}` | Number of facilities in exposure class `{cls}` | count |
| `kt34_{facility}_perc_cat{cls}` | Percentage of the unit's facilities of that category in exposure class `{cls}` | % |
| `kt34_crops_km2_cat{cls}` | Cropland area in exposure class `{cls}` | km² |

Where `{cls}` is the cyclone exposure class (1 = Cat 1, 2 = Cat 2–3, 3 = Cat 4–5), `{indicator}` is a demographic group (`total_pop`, `female_pop`, `children_u5`, `female_u5`, `elderly`, `pop_u15`, `female_u15`, `wra_pop`), and `{facility}` is a category (`education`, `hospitals`, `primary_healthcare`). `kt34` refers to the 34-knot wind radius used to define the exposed area.

### Cyclone Categories <a id="cyclone-categories"></a>
| Exposure Class | Saffir-Simpson Category | Storm Maximum Sustained Wind (km/h) |
|----------------|------------------------|-------------------|
| 1 | Category 1 | 119–153 |
| 2 | Categories 2–3 | 154–208 |
| 3 | Categories 4–5 | ≥ 209 |

The wind speeds describe the storm's intensity on that track segment, not the wind speed at every location in the exposed area. The exposed area itself is the zone with winds of at least 34 knots. Where footprints of several storms overlap, the highest class is kept, so each location (and each person or facility) is counted in exactly one class: the strongest storm recorded there since 1980.

### Processing Steps <a id="processing-steps-9"></a>
1. **Download and extract IBTrACS storm track data** (v04r01, since 1980) from NOAA NCEI.
2. **Filter track segments** with a Saffir-Simpson category of 1 or higher that intersect the country's bounding box. Storms passing outside this bounding box are not included, even if their wind field reaches the country.
3. **Buffer track segments** by the 34-knot wind radius: the mean of the four quadrant radii, converted from nautical miles to metres. Segments without 34-knot radius data are dropped.
4. **Clip buffers** to the country boundary.
5. **Rasterize** the buffers onto the 1 km WorldPop grid, keeping the highest category per cell, and classify the cells into the three exposure classes (1, 2, 3).
6. **Compute population exposure:** For each demographic group and class, multiply the population raster by the class mask and sum per admin unit (zonal statistics).
7. **Compute dependency ratio:** `kt34_dependency_ratio_cat{cls} = dependents (0–14, 65+) / working-age (15–64) × 100` per class; 0 where no working-age population is exposed.
8. **Compute facility exposure:** Sample the exposure class raster at each facility location (centroid), then count the exposed facilities per admin unit and class and compute their share of all facilities of that category in the unit.
9. **Compute cropland exposure:** Multiply the cropland fraction by each class mask and the approximate cell area, and sum per admin unit (km²).
10. **Save CSV** with all exposure columns. Missing values are filled with 0. All values except the dependency ratio (2 decimals) are rounded to whole numbers.

If no qualifying cyclone track reaches the country, no cyclone exposure file is produced.

### Outputs <a id="outputs-9"></a>
- **File:** `{country_code}_{admin_level}_cyclone_exposure.csv` (e.g. `MMR_ADM2_cyclone_exposure.csv`)
- **Rows:** one per administrative unit
- **Columns:**
  - `{admin_level}_PCODE` (e.g. `ADM2_PCODE`)
  - `ADM_PCODE` (same values; level-independent alias)
  - Population exposed per demographic group and class: `kt34_total_pop_cat1`, `kt34_total_pop_cat2`, `kt34_total_pop_cat3`, `kt34_female_pop_cat1`, … `kt34_wra_pop_cat3` (8 groups × 3 classes)
  - Dependency ratio per class: `kt34_dependency_ratio_cat1`, `kt34_dependency_ratio_cat2`, `kt34_dependency_ratio_cat3`
  - Facility counts and percentages per category and class: `kt34_education_count_cat1`, `kt34_education_perc_cat1`, … `kt34_primary_healthcare_perc_cat3`
  - Cropland exposed per class: `kt34_crops_km2_cat1`, `kt34_crops_km2_cat2`, `kt34_crops_km2_cat3`
  - With complete inputs: 50 columns. Facility or cropland columns are omitted if the corresponding input data is unavailable for a country.
- **Units:** people, count, %, km²

**Source code:** [`fetch_cyclones_ncei.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_cyclones_ncei.py) · [`fetch_worldcover.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/fetch_worldcover.py) · [`exposure.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/exposure.py)

---

## 10. Evacuability <a id="10-evacuability"></a>
Estimates the travel time (in minutes) from areas at risk from floods or tropical cyclones to the nearest area that is not affected by the hazard ("safe zone"). It uses least-cost path analysis on a motorized friction surface. The result shows how quickly people in hazard-prone areas could reach unaffected ground by motorized transport, summarised per administrative unit.

### Data Sources <a id="data-sources-10"></a>
- **Flood Hazard Rasters:** JRC CEMS-GloFAS flood hazard depth maps (metres, ~3 arc-second resolution) for each return period (RP), clipped to the country. These are the same rasters used in [Flood Exposure](#8-flood-exposure).
- **Cyclone Exposure Raster:** The raster produced by the [Cyclone Exposure](#9-cyclone-exposure) step from IBTrACS tracks. It marks areas within the 34-knot wind radius of Category 1–5 storm points (classes 1 = Cat 1, 2 = Cat 2–3, 3 = Cat 4–5; 0 = not affected). It only exists for countries with relevant cyclone tracks.
- **Friction Surface:** The global 2020 motorized friction surface (Cloud-Optimized GeoTIFF, ~1 km resolution), read from HeiGIT's public storage (`2020_motorized_friction_surface_cog.tif`). It gives the travel time needed to cross each pixel.
- **Administrative Boundaries:** used to summarise travel times per admin unit (see [Administrative Boundaries](#administrative-boundaries)).

### Indicators <a id="indicators-7"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `RP{rp}_evac_time_minutes_mean` | Mean travel time from flooded pixels (return period `{rp}`) to the nearest safe zone | minutes |
| `RP{rp}_evac_time_minutes_max` | Maximum travel time from flooded pixels to the nearest safe zone | minutes |
| `RP{rp}_evac_time_minutes_median` | Median travel time from flooded pixels to the nearest safe zone | minutes |
| `kt34_evac_time_minutes_mean` | Mean travel time from cyclone-affected pixels to the nearest safe zone | minutes |
| `kt34_evac_time_minutes_max` | Maximum travel time from cyclone-affected pixels to the nearest safe zone | minutes |
| `kt34_evac_time_minutes_median` | Median travel time from cyclone-affected pixels to the nearest safe zone | minutes |

### Processing Steps <a id="processing-steps-10"></a>
1. **Load the hazard raster** for each configured return period (default: 10, 50, 100, 500 years) and, if available, the cyclone exposure raster. Return periods without a flood raster are skipped.
2. **Reduce resolution for large countries:** if a hazard raster has more than 10 million pixels, the analysis runs on a coarser grid. The cell size is chosen so the grid stays within that limit, and is at least 500 m.
3. **Fetch the friction surface** for the raster's extent and resample it onto the analysis grid.
4. **Classify pixels:**
   - **Flood:** *at risk* if flood depth is greater than the flood threshold (default **0.3 m**). *Safe* if depth is at or below the threshold, or if there is no flood data (including areas outside the country boundary).
   - **Cyclone:** *at risk* if the pixel lies within any 34-knot wind buffer (class ≥ 1). *Safe* otherwise.
5. **Compute travel time** from every pixel to the nearest safe zone, using a least-cost (minimum cumulative cost) algorithm over the friction surface with 8-neighbour movement. Safe-zone pixels are the starting points. For performance, at most 20,000 safe pixels are randomly sampled as starting points, so travel times can be slightly overestimated where safe areas are large.
6. **Cyclone only:** if the raster was reduced in resolution, the travel-time grid is resampled back to the original resolution before summarising.
7. **Summarise per admin unit:** the mean, maximum and median travel time over the at-risk pixels in each unit, rounded to one decimal place.
8. **Write one CSV** per admin level containing the flood columns for each return period and, where cyclone data exists, the cyclone columns.

### Outputs <a id="outputs-10"></a>
- **File:** `{country_code}_{admin_level}_evacuability.csv` (default admin level: `ADM2`; if no boundary exists for the requested level, the next lower available level is used)
- **Columns:**
  - `{admin_level}_PCODE`
  - Flood evacuability per return period: `RP{rp}_evac_time_minutes_mean`, `RP{rp}_evac_time_minutes_max`, `RP{rp}_evac_time_minutes_median`
  - Cyclone evacuability (only if a cyclone exposure raster exists for the country): `kt34_evac_time_minutes_mean`, `kt34_evac_time_minutes_max`, `kt34_evac_time_minutes_median`
- **Units:** minutes (travel time)
- **Empty values:** admin units with no at-risk pixels for a hazard or return period have empty cells in the corresponding columns.

**Source code:** [`calculate_evacuatability.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/calculate_evacuatability.py) · [`evacuability.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/evacuability.py)

---

## Outputs and Publishing <a id="outputs-and-publishing"></a>
All files are published for each country in three places.

### Public storage <a id="publishing-storage"></a>
All indicator CSVs are uploaded to HeiGIT's public storage:

`https://hot.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/{iso3}/{ISO3}_{ADM}_{indicator}.csv`

For example: `.../risk_assessment_inputs/afg/AFG_ADM2_coping.csv`. Before upload, the region codes of every file are checked against the current boundaries of the country; files that were computed on an older boundary version are not published.

### HDX datasets <a id="publishing-hdx"></a>
For each country, the indicator files are listed on HDX as the dataset **"{Country} - Risk Assessment Indicators"** of the [Heidelberg Institute for Geoinformation Technology](https://data.humdata.org/organization/heidelberg-institute-for-geoinformation-technology), part of the data series *Heidelberg Institute for Geoinformation Technology - Risk Assessment Indicators*.

- **Files:** Access, Facilities, Coping Capacity, Demographics, Rural Population, RAI, Vulnerability, Flood Exposure and Evacuability (required), and Cyclone Exposure (only for countries exposed to cyclones). The files link to the public storage described above.
- **Completeness:** a page is only published once all required files of the country are available. If a required file becomes unavailable, the page is removed.
- **License:** Creative Commons Attribution-ShareAlike (CC BY-SA).

### Interactive dashboard <a id="publishing-dashboard"></a>
The [**Disaster Risk Composer**](https://disaster-risk-composer.heigit.org) visualises the indicators and the resulting risk scores per administrative unit. It is embedded on each HDX page (`https://disaster-risk-composer.heigit.org/#/?country={ISO3}&disaster=risk_flood`).

It uses two additional files per country, stored next to the CSVs:

- **`{ISO3}_ADM2_risk.parquet`** – all exposure, vulnerability and coping indicators of the country in one table, with the prefixes `exp_flo_` (flood exposure), `exp_cyc_` (cyclone exposure), `vul_` (vulnerability) and `cop_` (coping capacity), plus the composite risk scores per hazard. The calculation of the risk scores is described in the [GAIA repository](https://github.com/GIScience/gaia#risk-scores).
- **`{ISO3}_ADM2.pmtiles`** – the administrative boundaries as vector tiles (layer `boundary`), with the region code and name. For NUTS countries the file metadata contains the required license notice in the field `attribution`.

**Source code:** [`uploads.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/uploads.py) · [`upload_to_hdx.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/scripts/upload_to_hdx.py) · [`visualization.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/assets/visualization.py) · [`risk.py`](https://github.com/GIScience/gaia/blob/main/src/gaia/defs/risk.py)


