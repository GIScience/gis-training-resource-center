# GAIA Pipeline Documentation <a id="gaia-pipeline-documentation"></a>

## Overview <a id="overview"></a>

The Global Aggregation of Indicators for Anticipatory Action (GAIA) Pipeline produces a series of thematic files for a collection from several countries at administrative level 2, covering multiple countries where administrative boundaries and place codes (PCODEs) are available on HDX. Each file captures different aspects of population, infrastructure, and environmental conditions. Below is an overview of the available files:

1. [**Access to Services**](#access-to-services) – Population accessibility to key facilities such as education and health centers.  
2. [**Facilities**](#facilities) – Availability and distribution of essential service infrastructure.  
3. [**Coping Capacity**](#coping-capacity) – Combined indicators derived from Access, Facilities, Evacuability, and RAI layers.
4. [**Demographics**](#demographics) – Distribution of vulnerable population.
5. [**Rural Population**](#rural-population) – Demographic indicators focused specifically on rural populations.
6. [**Rural Accessibility Index (RAI)**](#rural-accessibility-index-rai) – Percentage of rural population within 2 km of a paved road.
7. [**Vulnerability**](#vulnerability) – Composite indicators derived from Demographics and Rural Population layers.
8. [**Flood Exposure**](#flood-exposure) – Exposure of populations and facilities to flood hazards.
9. [**Cyclone Exposure**](#cyclone-exposure) – Exposure of populations and facilities to cyclone hazards.
10. [**Evacuability**](#evacuability) – Travel time from at-risk areas to the nearest safe zone.

Further details on GAIA’s methodology are available in the [GAIA repository on GitHub](https://github.com/GIScience/gaia).

---

:::{admonition} Information
:class: tip
The **Coping Capacity**, **Vulnerability**, and **Flood Exposure** files can be used directly as input for the Risk Assessment QGIS Plugin when analyzing flood hazards. Only minor adjustments, such as renaming the ID columns, are required for compatibility.
:::

---

## 1. Access to Services <a id="1-access-to-services"></a>
Represents the share of the population with access to key facilities within defined distances or travel times.

### Data Sources <a id="data-sources"></a>
- Accessibility data (isochrones) downloaded from **MinIO** for the categories: `education`, `hospitals`, `primary_healthcare`.
- Population data: WorldPop raster data (vulnerable populations) via *Demographics*.

### Processing Steps <a id="processing-steps"></a>
1. **Download accessibility isochrones** in GPKG format for each category.
2. **Load administrative boundaries** at admin level 2 from local GeoJSON files.
3. **Fetch WorldPop raster datasets** and sum relevant indicators to produce a vulnerable population raster.
4. For each category and cutoff:
   - Select isochrone polygons for the cutoff value.
   - Intersect polygons with administrative boundaries.
   - Use `rasterstats.zonal_stats` to compute total population within the isochrone area.
5. Save results as a CSV containing population counts per administrative unit.

### Outputs <a id="outputs"></a>
- CSV file: `{country_code}_{admin_level}_access.csv`
  - Columns: `{admin_level}_PCODE`, `access_pop_education_5km`, `access_pop_education_10km`, etc.
  - CRS: WGS84 (`EPSG:4326`)
  - Units: population count

:::{dropdown} Python Script (Access to Services)
       
```python
import os
import requests
from pathlib import Path
import geopandas as gpd
import rioxarray
import rasterio
import pandas as pd
import numpy as np
import argparse
import logging
from rasterstats import zonal_stats

from scripts.fetch_worldpop import fetch_worldpop


CATEGORY_SPECS = {
    "education": {
        "ranges": {5000: "access_pop_education_5km",
                   10000: "access_pop_education_10km",
                   20000: "access_pop_education_20km"},
        "type": "distance",  # meters
    },
    "hospitals": {
        "ranges": {1800: "access_pop_hospitals_30min",
                   3600: "access_pop_hospitals_1h",
                   7200: "access_pop_hospitals_2h"},
        "type": "time",  # seconds
    },
    "primary_healthcare": {
        "ranges": {1800: "access_pop_primary_healthcare_30min",
                   3600: "access_pop_primary_healthcare_1h",
                   7200: "access_pop_primary_healthcare_2h"},
        "type": "time",  # seconds
    }
}


def download_access_gpkg(country_code, category, work_dir, context):
    """Download accessibility gpkg file if missing, return path."""
    url = f"https://warm.storage.heigit.org/heigit-hdx-public/access/{country_code.lower()}/{country_code}_{category}_access.gpkg"
    gpkg_path = Path(work_dir) / f"{country_code}_{category}_access.gpkg"

    if not gpkg_path.exists():
        context.info(f"Downloading {category} access GPKG…")
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
        with open(gpkg_path, "wb") as f:
            for chunk in resp.iter_content(1024 * 1024):
                f.write(chunk)
    else:
        context.info(f"{gpkg_path} already exists, skipping download.")

    return gpkg_path


def find_value_field(df, context):
    """Try to find the field that contains the isochrone cutoff values."""
    for candidate in ["value", "range", "cost", "distance", "time"]:
        if candidate in df.columns:
            return candidate
    # fallback: first numeric column
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            context.info(f"Guessed value field: {col}")
            return col
    raise ValueError("Could not identify value/range column in isochrones")


def compute_access_population(country_code, admin_level, gdf_admin, work_dir, output_dir, context):
    """
    Compute how much vulnerable population lives within accessibility isochrones,
    grouped by chosen administrative level.
    """

    country_code = country_code.upper()
    work_dir = Path(work_dir)
    output_dir = Path(output_dir)
    out_csv = output_dir / f"{country_code}_{admin_level}_access.csv"

    if out_csv.exists():
        context.info(f"CSV already exists, skipping: {out_csv}")
        return str(out_csv)

    # --- ensure vulnerable population raster ---
    context.info("Fetching WorldPop rasters…")
    indicator_tifs = fetch_worldpop(country_code)
    pop_rasters = [rioxarray.open_rasterio(p).squeeze() for p in indicator_tifs]

    vuln_pop = sum(pop_rasters)
    vuln_tmp = work_dir / f"{country_code}_vulnerable_pop.tif"
    vuln_pop.rio.to_raster(vuln_tmp)

    results = pd.DataFrame({f"{admin_level}_PCODE": gdf_admin[f"{admin_level}_PCODE"]})

    for category, spec in CATEGORY_SPECS.items():
        gpkg_path = download_access_gpkg(country_code, category, work_dir, context)

        # Load ADM0 isochrones
        isochrones = gpd.read_file(gpkg_path, layer="ADM0")
        isochrones = isochrones.to_crs("EPSG:4326")

        value_field = find_value_field(isochrones, context)

        for cutoff, colname in spec["ranges"].items():
            context.info(f"{category}: processing {cutoff} ({colname})")

            subset = isochrones[isochrones[value_field] == cutoff]
            if subset.empty:
                # Skip creating this column if no polygons found
                context.info(f"  No polygons found for {cutoff} in {category} — skipping.")
                continue 

            # Intersect chosen admin level with isochrone
            admin_in_range = gpd.overlay(gdf_admin, subset, how="intersection")
            if admin_in_range.empty:
                context.info(f"  No intersections found for {cutoff} in {category} — skipping.")
                continue 

            stats = zonal_stats(admin_in_range, vuln_tmp, stats="sum", nodata=0, geojson_out=True)

            if not stats:
                context.info(f"  No zonal stats computed for {cutoff} in {category} — skipping.")
                continue  

            sums = {}
            for s in stats:
                pcode = s["properties"][f"{admin_level}_PCODE"]
                sums[pcode] = sums.get(pcode, 0) + (s["properties"]["sum"] or 0)

            results[colname] = (
                results[f"{admin_level}_PCODE"]
                .map(sums)
                .fillna(0)
                .round(0)
                .astype(int)
            )

    output_dir.mkdir(parents=True, exist_ok=True)
    results.to_csv(out_csv, index=False)
    context.info(f"Accessibility population CSV written to {out_csv}")

    return str(out_csv)
```
:::

---

## 2. Facilities <a id="2-facilities"></a>
Represents the availability and spatial distribution of essential service infrastructure such as schools, hospitals, and primary healthcare centers.

### Data Sources <a id="data-sources-2"></a>
- **OpenStreetMap (OSM)** data, accessed through either:
  - **Overpass API**, for direct querying of recent OSM feature data; or  
  - **Ohsome API**, for more stable and filtered access to OSM geometries.
- **Administrative boundaries** (GeoJSON): Used to spatially aggregate features at administrative level 2.

### Processing Steps <a id="processing-steps-2"></a>
1. **Load administrative boundaries** (GeoJSON) for the target country at the desired administrative level.  
2. **Define filters** for each facility type:
   - **Education:** `amenity=school`
   - **Hospitals:** `amenity=hospital` or `healthcare=hospital`
   - **Primary healthcare:** Non-hospital facilities providing healthcare services, such as `clinic`, `doctors`, `midwife`, `nurse`, or `center`.
3. **Determine API source:**
   - If Overpass is used, queries are dynamically built and executed using bounding boxes of the country boundary.
   - If Ohsome is used, geometry data is fetched for the same bounding box and time period (if specified).
4. **Download and parse facility points**:
   - For Overpass: CSV results are parsed into GeoDataFrames with `lon`, `lat`, and `osmId` attributes.
   - For Ohsome: JSON features are directly converted into GeoDataFrames.
5. **Assign categories and export raw results**:
   - Each facility type (education, hospitals, primary healthcare) is stored as a separate GeoJSON in a `Temporary` folder.
6. **Aggregate by administrative unit**:
   - Facilities are spatially joined (`sjoin`) with administrative polygons.
   - For each category, counts are grouped by `{admin_level}_PCODE`.
7. **Combine and export results**:
   - Counts for all categories are merged into a single summary table.
   - Output is saved as a CSV file in the `Output` directory.

### Outputs <a id="outputs-2"></a>
- CSV file: `{country_code}_{admin_level}_facilities.csv`
  - Columns:
    - `{admin_level}_PCODE`
    - `education_count`
    - `hospitals_count`
    - `primary_healthcare_count`
  - CRS: WGS84 (`EPSG:4326`)
  - Units: number of facilities per administrative unit
- Intermediate GeoJSON files:
  - Stored in `Temporary/` folder as raw point data for each facility category.

:::{dropdown} Python Script (Facilities)
```python
import argparse
import os
import sys
import requests
import geopandas as gpd
import pandas as pd
import overpass
import warnings
from pathlib import Path

os.environ["OGR_GEOJSON_MAX_OBJ_SIZE"] = "0" # no limits when reading complex geojsons

warnings.simplefilter("ignore", UserWarning)

OVERPASS_FILTERS = {
    "education": ["nwr[amenity=school]"],
    "hospitals": ["nwr[amenity=hospital]","nwr[healthcare=hospital]"],
    
    "primary_healthcare": [
        'nwr["amenity"~"^(doctors|clinic)$"]["amenity"!="hospital"]["healthcare"!="hospital"]',
        'nwr["healthcare"~"^(clinic|doctors|midwife|nurse|center)$"]["amenity" != "hospital"]["healthcare" != "hospital"]'
    ] 
}

OHSOME_ENDPOINT = "https://api.ohsome.org/v1/elements/geometry"

OHSOME_FILTERS = {
    "education": "amenity=school",
    "hospitals": "amenity=hospital or healthcare=hospital",
    "primary_healthcare": (
        "not amenity=hospital and not healthcare=hospital and "
        "(amenity=doctors or amenity=clinic or healthcare=clinic or "
        "healthcare=doctors or healthcare=midwife or healthcare=nurse or healthcare=center)"
    ),
}



def parse_overpass_csv_to_gpd(result):
    headers = result[0]
    rows = result[1:]
    df = pd.DataFrame(rows, columns=headers)

    df['@lon'] = df['@lon'].astype(float)
    df['@lat'] = df['@lat'].astype(float)
    df['@id'] = df['@id'].astype(int)

    df = df.rename(columns={'@lon': 'lon', '@lat': 'lat', '@id': 'osmId'})

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df['lon'], df['lat']),
        crs="EPSG:4326"
    )
    return gdf

def fetch_overpass(context_log, boundary_file, output_dir, country_code, admin_level, time=None):
    context_log.info("Using Overpass API to fetch facilities...")
    id_col = f"{admin_level.upper()}_PCODE"

    # Paths for output files
    temp_dir = output_dir / "Temporary"
    out_dir = output_dir / "Output"
    expected_files = [
        out_dir / f"{country_code}_{admin_level}_facilities.csv"
    ] + [
        temp_dir / f"{country_code}_{category}_raw.geojson"
        for category in OVERPASS_FILTERS.keys()
    ]

    # Check if all expected files exist → skip
    if all(f.exists() for f in expected_files):
        context_log.info("All Overpass output files exist. Skipping fetch_overpass.")
        return expected_files[0]  # Return main summary path

    try:
        boundary = gpd.read_file(boundary_file)
    except Exception as e:
        context_log.info(f"Error reading boundary: {e}")
        sys.exit(1)

    if id_col not in boundary.columns:
        context_log.warning(f"Expected ID column {id_col} not found in {boundary_file}")
        return None

    minx, miny, maxx, maxy = boundary.total_bounds.tolist()
    bbox_str = f"{miny},{minx},{maxy},{maxx}"
    date_clause = f'[date:"{time}"]' if time else ''

    api = overpass.API(timeout=300)
    category_gdfs = {}

    for category, exprs in OVERPASS_FILTERS.items():
        filter_parts = [f"{expr}({bbox_str});" for expr in exprs]
        query = f'[out:csv(::lon,::lat,::id,::type)]{date_clause};({"".join(filter_parts)});out center;'

        try:
            result = api.get(query, build=False)
        except Exception as e:
            context_log.info(f"Overpass query failed for {category}: {e}")
            continue

        if not result or len(result) < 2:
            context_log.info(f"No results for {category}")
            continue

        gdf = parse_overpass_csv_to_gpd(result)

        if gdf.empty:
            context_log.info(f"No features found for {category}")
            continue

        gdf["geometry"] = gdf.geometry.centroid
        gdf["category"] = category

        raw_path = temp_dir / f"{country_code}_{category}_raw.geojson"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        gdf.to_file(raw_path, driver="GeoJSON")
        context_log.info(f"Wrote raw {category} features to {raw_path}")

        category_gdfs[category] = gdf

    if not category_gdfs:
        context_log.info("No Overpass features found at all.")
        return None

    counts = boundary[[id_col]].copy()
    for cat, gdf in category_gdfs.items():
        joined = gpd.sjoin(gdf, boundary, how="inner", predicate="intersects")
        grouped = joined.groupby(id_col).size().rename(f"{cat}_count")
        counts = counts.merge(grouped, on=id_col, how="left")

    counts = counts.fillna(0).astype({col: int for col in counts.columns if col != id_col})

    summary_path = out_dir / f"{country_code}_{admin_level}_facilities.csv"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    counts.to_csv(summary_path, index=False)
    context_log.info(f"Wrote summary to {summary_path}")

    return summary_path


def fetch_ohsome(context_log, boundary_file, output_dir, country_code, admin_level, time=None):
    context_log.info("Using Ohsome API to fetch facilities...")

    id_col = f"{admin_level.upper()}_PCODE"

    temp_dir = output_dir / "Temporary"
    out_dir = output_dir / "Output"
    expected_files = [
        out_dir / f"{country_code}_{admin_level}_facilities.csv"
    ] + [
        temp_dir / f"{country_code}_{category}_raw.geojson"
        for category in OHSOME_FILTERS.keys()
    ]

    if all(f.exists() for f in expected_files):
        context_log.info("All Ohsome output files exist. Skipping fetch_ohsome.")
        return expected_files[0]

    try:
        boundary = gpd.read_file(boundary_file)
    except Exception as e:
        context_log.info(f"Error reading boundary: {e}")
        sys.exit(1)

    if id_col not in boundary.columns:
        context_log.warning(f"Expected ID column {id_col} not found in {boundary_file}")
        return None

    minx, miny, maxx, maxy = boundary.total_bounds.tolist()
    bbox_str = f"{minx},{miny},{maxx},{maxy}"

    category_gdfs = {}

    for category, filter_str in OHSOME_FILTERS.items():
        params = {"bboxes": bbox_str, "filter": filter_str}
        if time:
            params["time"] = time

        try:
            r = requests.post(OHSOME_ENDPOINT, params=params)
            r.raise_for_status()
        except Exception as e:
            context_log.info(f"Ohsome query failed for {category}: {e}")
            continue

        data = r.json()
        gdf = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")

        if gdf.empty:
            context_log.info(f"No features found for {category}")
            continue

        gdf = gdf.copy()
        gdf["geometry"] = gdf.geometry.centroid
        gdf["category"] = category

        raw_path = temp_dir / f"{country_code}_{category}_raw.geojson"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        gdf.to_file(raw_path, driver="GeoJSON")
        context_log.info(f"Wrote raw {category} features to {raw_path}")

        category_gdfs[category] = gdf

    if not category_gdfs:
        context_log.info("No categories found, nothing to aggregate.")
        return None

    counts = boundary[[id_col]].copy()
    for cat, gdf in category_gdfs.items():
        joined = gpd.sjoin(gdf, boundary, how="inner", predicate="intersects")
        grouped = joined.groupby(id_col).size().rename(f"{cat}_count")
        counts = counts.merge(grouped, on=id_col, how="left")

    counts = counts.fillna(0).astype({col: int for col in counts.columns if col != id_col})

    summary_path = out_dir / f"{country_code}_{admin_level}_facilities.csv"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    counts.to_csv(summary_path, index=False)
    context_log.info(f"Wrote summary to {summary_path}")

    return summary_path
```
:::

---

## 3. Coping Capacity <a id="3-coping-capacity"></a>
Represents the ability of a population to access essential services and benefit from available infrastructure.  
This layer combines *Access to Services*, *Facilities*, *Evacuability*, and *Rural Accessibility Index (RAI)* indicators to assess local capacity to cope with shocks or disruptions.

### Data Sources <a id="data-sources-3"></a>
- **Access to Services CSVs:** Derived from population accessibility analysis (see *Access to Services* chapter).  
- **Facilities CSVs:** Derived from OpenStreetMap facility data (see *Facilities* chapter).  
- **Evacuability CSVs:** Travel time from at-risk population areas to nearest safe zones (see *Evacuability* chapter).  
- **RAI CSVs:** Rural Accessibility Index (see *RAI* chapter).  
- All inputs are aggregated at the same administrative level (e.g., ADM2).

### Processing Steps <a id="processing-steps-3"></a>
1. **Input CSVs:**  
   - *Access to Services*, *Facilities*, *Evacuability*, and *RAI* CSVs are provided per administrative level.
   - Each CSV includes an identifier column such as `ADM0_PCODE`, `ADM1_PCODE`, or `ADM2_PCODE`.
2. **Column Detection:**  
   - The script automatically detects the administrative identifier column by searching for any column ending with `_PCODE`.
3. **Merge Operations:**  
   - The access and facilities datasets are merged on the identified `*_PCODE` column using a left join.
   - If available, evacuability columns are merged from the evacuability CSV.
   - If available, RAI columns are merged from the RAI CSV.
4. **Output Generation:**  
   - The merged dataset is saved as `{country_code}_{admin_level}_coping.csv` under `Output/`.
   - One output is produced per administrative level present in the input data.

### Outputs <a id="outputs-3"></a>
- CSV file: `{country_code}_{admin_level}_coping.csv`
  - Columns:  
    - `{admin_level}_PCODE`
    - All accessibility indicator columns (e.g., `access_pop_education_5km`, `access_pop_hospitals_1h`)
    - All facility count columns (e.g., `education_count`, `hospitals_count`, `primary_healthcare_count`)
    - All evacuability columns (e.g., `RP{rp}_evac_time_minutes_mean`, `kt34_evac_time_minutes_mean`)
    - All RAI columns (e.g., `rural_access_total_pop`, `RAI_total_pop`, `rural_access_dependency_ratio`)
  - CRS: WGS84 (`EPSG:4326`)
  - Units: counts and population values aggregated per administrative unit

:::{dropdown} Python Script (Coping Capacity)
```python
import os
import pandas as pd
from pathlib import Path
from typing import List

def coping_asset(context, access_asset: List[str], facilities_asset: List[str],
                  evacuability_asset: List[str], RAI_asset: List[str]) -> list[str]:
    """
    Combine accessibility, facilities, evacuability, and RAI CSVs into a single
    coping dataset. Joins on the ADM*_PCODE column per admin level.
    Produces one coping CSV per admin level in Output/.
    """
    country_code = context.partition_key.upper()
    outputs = []

    for i, access_csv in enumerate(access_asset):
        if i >= len(facilities_asset):
            break
        facilities_csv = facilities_asset[i]
        evac_csv = evacuability_asset[i] if i < len(evacuability_asset) else None
        rai_csv = RAI_asset[i] if i < len(RAI_asset) else None

        if not os.path.exists(access_csv) or not os.path.exists(facilities_csv):
            context.log.warning(
                f"Skipping merge for {country_code}: missing files {access_csv}, {facilities_csv}"
            )
            continue

        try:
            df_access = pd.read_csv(access_csv)
            df_facilities = pd.read_csv(facilities_csv)

            id_col = [c for c in df_access.columns if c.endswith("_PCODE")]
            if not id_col:
                context.log.warning(f"Skipping {access_csv}: no *_PCODE column found")
                continue
            id_col = id_col[0]

            merged = pd.merge(df_access, df_facilities, on=id_col, how="left")

            if evac_csv and os.path.exists(evac_csv):
                df_evac = pd.read_csv(evac_csv)
                if id_col in df_evac.columns:
                    evac_cols = [c for c in df_evac.columns if c != id_col]
                    if evac_cols:
                        merged = pd.merge(merged, df_evac[[id_col] + evac_cols], on=id_col, how="left")

            if rai_csv and os.path.exists(rai_csv):
                df_rai = pd.read_csv(rai_csv)
                if id_col in df_rai.columns:
                    rai_cols = [c for c in df_rai.columns if c != id_col]
                    if rai_cols:
                        merged = pd.merge(merged, df_rai[[id_col] + rai_cols], on=id_col, how="left")

            adm_cols = [c for c in merged.columns if c.startswith("ADM") and c.endswith("_PCODE")]
            if "ADM_PCODE_x" in merged.columns or "ADM_PCODE_y" in merged.columns:
                merged["ADM_PCODE"] = merged["ADM_PCODE_x"].combine_first(merged["ADM_PCODE_y"])
                merged.drop(columns=[c for c in ["ADM_PCODE_x", "ADM_PCODE_y"] if c in merged.columns], inplace=True)
            elif "ADM_PCODE" in merged.columns and adm_cols.count("ADM_PCODE") > 1:
                merged = merged.loc[:, ~merged.columns.duplicated()]

            admin_level = id_col.split("_")[0]
            output_dir = Path("data") / country_code / "Output"
            output_dir.mkdir(parents=True, exist_ok=True)

            output_path = output_dir / f"{country_code}_{admin_level}_coping.csv"
            merged.to_csv(output_path, index=False)
            outputs.append(str(output_path))

            context.log.info(f"[{country_code}] Wrote coping CSV: {output_path} ({len(merged.columns)} cols)")

        except Exception as e:
            context.log.warning(f"Failed to merge for {country_code}: {e}")

    if not outputs:
        context.log.warning(f"No coping outputs created for {country_code}")
    return outputs
```
:::

---
## 4. Demographics <a id="4-demographics"></a>
Provides population distribution indicators based on **age** and **sex**.  
This layer is derived from the [**WorldPop**](https://www.worldpop.org/) global population dataset and quantifies vulnerable population groups across administrative boundaries.

### Data Sources <a id="data-sources-4"></a>
- **WorldPop Age-Sex Population Rasters:**  
  Downloaded from the [WorldPop Global Constrained Population dataset](https://www.worldpop.org/geodata/listing?id=77) (`Global_2015_2030`, Release `R2025A`, Year `2030`).  
- **Administrative boundaries** (GeoJSON): Used to spatially aggregate features at administrative level 2.


### Indicators <a id="indicators"></a>
Each demographic indicator represents the **sum of population counts** matching specified age and sex ranges:

| Indicator            | Description                                | Ages (years)       | Sexes |
|----------------------|--------------------------------------------|--------------------|-------|
| `total_pop`          | Total population                           | 0–80+              | f, m  |
| `female_pop`         | Total female population                    | 0–80+              | f     |
| `children_u5`        | Total children under 5                     | 0–4                | f, m  |
| `female_u5`          | Female children under 5                    | 0–4                | f     |
| `elderly`            | Population aged 65 and above               | 65+                | f, m  |
| `pop_u15`            | Population under 15                        | 0–14               | f, m  |
| `female_u15`         | Female population under 15                 | 0–14               | f     |
| `wra_pop`            | Women of reproductive age (15–49)          | 15–49              | f     |
| `dependency_ratio`   | Dependency ratio = (dependents / working) × 100 | Derived      | —     |

### Processing Steps <a id="processing-steps-4"></a>
1. **Download Required WorldPop Tiles**  
   - For each indicator, the script identifies which age/sex rasters are needed (e.g., `m_00`, `f_01`, etc.).  
   - Tiles are downloaded from **Worldpop** using the `Global_2015_2030` / `R2025A` / `2030` constrained dataset.
2. **Merge and Sum Rasters**  
   - The corresponding age/sex tiles are summed into one raster per indicator.  
   - Outputs are saved in `data/{country}/Temporary/`.
3. **Aggregate by Administrative Units**  
   - Using the administrative boundary GeoJSON (e.g., `ADM2`), zonal statistics are computed for each indicator.  
   - Population counts are summed per administrative area.
4. **Derive Dependency Ratio**  
   - `dependency_ratio = (dep_dependents / dep_working) × 100` is computed per administrative unit.
5. **Output**  
   - A single CSV per country: `{country_code}_{admin_level}_demographics.csv`
   - Saved to `data/{country}/Output/`

### Outputs <a id="outputs-4"></a>
- **File:** `{country_code}_{admin_level}_demographics.csv`  
- **Columns:**
  - `{admin_level}_PCODE`
  - `ADM_PCODE` (alias column for compatibility)
  - `total_pop`
  - `female_pop`
  - `children_u5`
  - `female_u5`
  - `elderly`
  - `pop_u15`
  - `female_u15`
  - `wra_pop`
  - `dependency_ratio`
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** Population counts (integer, aggregated per administrative unit), ratio (%)

:::{dropdown} Python Script (Demographics)
```python
import os
import sys
from typing import List
import requests
import rasterio
import pandas as pd
import geopandas as gpd
import argparse
import logging
import shutil
from rasterstats import zonal_stats

INDICATORS = {
    "total_pop": {"ages": [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80], "sexes": ["f", "m"]},
    "female_pop": {"ages": [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80], "sexes": ["f"]},
    "children_u5": {"ages": [0, 1], "sexes": ["f", "m"]},
    "female_u5": {"ages": [0, 1], "sexes": ["f"]},
    "elderly": {"ages": [65, 70, 75, 80], "sexes": ["f", "m"]},
    "pop_u15": {"ages": [0, 1, 5, 10], "sexes": ["f", "m"]},
    "female_u15": {"ages": [0, 1, 5, 10], "sexes": ["f"]},
    "wra_pop": {"ages": [15, 20, 25, 30, 35, 40, 45], "sexes": ["f"]},
    "dep_dependents": {"ages": [0, 1, 5, 10, 65, 70, 75, 80], "sexes": ["f", "m"]},
    "dep_working": {"ages": [15, 20, 25, 30, 35, 40, 45, 50, 55, 60], "sexes": ["f", "m"]}
}

BASE_URL = "https://data.worldpop.org/GIS"
POP_TIMEFRAME = "Global_2015_2030"
RELEASE = "R2025A"
YEAR = "2030"


def download_url(url, dest_path):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(dest_path, "wb") as fp:
        for chunk in resp.iter_content(1024 * 1024):
            fp.write(chunk)


def merge_and_sum_rasters(raster_paths: List[str], out_path: str, context_log):
    if not raster_paths:
        raise ValueError("No rasters passed for merging!")
    with rasterio.open(raster_paths[0]) as src0:
        meta = src0.meta.copy()
        data_sum = src0.read(1, masked=True).filled(0).astype("float64")
    for p in raster_paths[1:]:
        with rasterio.open(p) as src:
            arr = src.read(1, masked=True).filled(0).astype("float64")
            data_sum += arr
    meta.update(dtype="float32", count=1, compress="lzw", nodata=0)
    with rasterio.open(out_path, "w", **meta) as dst:
        dst.write(data_sum.astype("float32"), 1)
    context_log.info(f"Wrote merged raster to {out_path}")


def fetch_worldpop(country, context_log=None, worldpop_code=None):
    if context_log is None:
        logging.basicConfig(level=logging.INFO)
        context_log = logging.getLogger("worldpop")

    country = country.upper()
    worldpop_code = worldpop_code or country
    worldpop_code_low = worldpop_code.lower()

    out_dir = os.path.join("data", country, "Temporary")
    os.makedirs(out_dir, exist_ok=True)

    expected_outputs = [
        os.path.join(out_dir, f"{country}_pop_{ind_name}_{YEAR}_constrained.tif")
        for ind_name in INDICATORS.keys()
    ]
    if all(os.path.exists(path) for path in expected_outputs):
        context_log.info(f"[{country}] -> indicators exist, skipping.")
        return expected_outputs

    out_dir_raw = os.path.join(out_dir, "worldpop_raw")
    os.makedirs(out_dir_raw, exist_ok=True)

    needed_bins = set()
    for ind in INDICATORS.values():
        for sex in ind["sexes"]:
            for age in ind["ages"]:
                needed_bins.add((sex, age))

    for sex, age in needed_bins:
        age_str = str(age).zfill(2)
        fname = f"{worldpop_code_low}_{sex}_{age_str}_{YEAR}_CN_100m_{RELEASE}_v1.tif"
        url = f"{BASE_URL}/AgeSex_structures/{POP_TIMEFRAME}/{RELEASE}/{YEAR}/{worldpop_code}/v1/100m/constrained/{fname}"
        dest = os.path.join(out_dir_raw, f"{country}_{sex}_{age}_{YEAR}_constrained.tif")
        if not os.path.exists(dest):
            context_log.info(f"[{country}] -> downloading {sex}_{age_str} from {url}")
            try:
                download_url(url, dest)
            except Exception as e:
                context_log.error(f"Failed to download {url}: {e}")
                sys.exit(1)

    processed = []
    for ind_name, ind in INDICATORS.items():
        filtered_paths = [
            os.path.join(out_dir_raw, f"{country}_{sex}_{age}_{YEAR}_constrained.tif")
            for sex in ind["sexes"]
            for age in ind["ages"]
        ]
        merged_out = os.path.join(out_dir, f"{country}_pop_{ind_name}_{YEAR}_constrained.tif")
        if not os.path.exists(merged_out):
            merge_and_sum_rasters(filtered_paths, merged_out, context_log)
        processed.append(merged_out)

    if os.path.exists(out_dir_raw):
        shutil.rmtree(out_dir_raw)
    return processed


def aggregate_worldpop_to_csv(country_code: str, admin_level="ADM2", context_log=None) -> str:
    temp_dir = os.path.join("data", country_code, "Temporary")
    os.makedirs(temp_dir, exist_ok=True)

    output_dir = os.path.join("data", country_code, "Output")
    os.makedirs(output_dir, exist_ok=True)
    if context_log is None:
        logging.basicConfig(level=logging.INFO)
        context_log = logging.getLogger("worldpop")

    tifs = fetch_worldpop(country=country_code, context_log=context_log)

    adm_path = f"data/{country_code}/{country_code}_{admin_level}.geojson"
    gdf = gpd.read_file(adm_path)

    expected_column = f"{admin_level}_PCODE"
    if expected_column not in gdf.columns:
        raise ValueError(
            f"GeoJSON must contain column '{expected_column}' "
            f"(found: {gdf.columns.tolist()})"
        )

    tif_map = dict(zip(INDICATORS.keys(), tifs))

    results = pd.DataFrame()
    results[f"{admin_level}_PCODE"] = gdf[f"{admin_level}_PCODE"]
    results["ADM_PCODE"] = gdf[f"{admin_level}_PCODE"]

    for ind, path in tif_map.items():
        stats = zonal_stats(gdf, path, stats="sum", nodata=0)
        results[ind] = [s["sum"] for s in stats]

    admin_col = f"{admin_level}_PCODE"
    if "ADM_PCODE" not in results.columns and admin_col in results.columns:
        results["ADM_PCODE"] = gdf[admin_col]

    numeric_cols = [c for c in results.columns if c not in [admin_col, "ADM_PCODE"]]
    results[numeric_cols] = results[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    ).fillna(0).replace([float("inf"), float("-inf")], 0)

    results[numeric_cols] = results[numeric_cols].round(0).astype(int)

    results["dependency_ratio"] = (
        (results["dep_dependents"] / results["dep_working"].replace(0, pd.NA)) * 100
    ).fillna(0).round(2)

    results.drop(columns=["dep_dependents", "dep_working"], inplace=True)

    out_dir = os.path.join("data", country_code, "Output")
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, f"{country_code}_{admin_level}_demographics.csv")
    results.to_csv(csv_path, index=False)

    return csv_path
```
:::

---
## 5. Rural Population <a id="5-rural-population"></a>
Represents the proportion and distribution of people living in **rural areas** within each administrative unit. Rural areas are those outside urban extents, typically characterized by lower population density, agricultural or natural land use, and limited infrastructure compared to urban centers.

This layer combines **WorldPop population rasters** with **Global Human Settlement Layer (GHS-SMOD)** data to estimate rural populations for each demographic group.

### Data Sources <a id="data-sources-5"></a>
- **WorldPop Population Rasters:**  
  Derived from the [WorldPop Age-Sex structured datasets](https://www.worldpop.org/geodata/listing?id=77).  
  Used to calculate population counts for various demographic indicators (see the *Demographics* chapter).  
- **GHS-SMOD (Settlement Model) Raster:**  
  Downloaded from the [JRC GHSL repository](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/) for the year 2030 projection.  
  Used to classify grid cells as **urban** or **rural** based on settlement patterns.
- **Administrative Boundaries:**  
  GeoJSON boundary files (e.g., ADM2) define the spatial units used for population aggregation.

### Processing Steps <a id="processing-steps-5"></a>
1. **Download GHS-SMOD Raster**  
   - The script downloads the global SMOD ZIP archive for 2030.  
   - Extracts and selects the `.tif` raster corresponding to global settlement data.  
2. **Reclassify SMOD Raster**  
   - Converts original SMOD categories into two classes:  
     - **Rural = 1** (codes 11–13)  
     - **Urban = 2** (codes 21–30)  
     - **Excluded/Water = 0**  
   - The resulting raster is saved as `smod_reclass.tif`.  
3. **Fetch WorldPop Demographic Indicators**  
   - Ensures that population rasters for indicators such as `female_pop`, `children_u5`, etc., are available.  
   - Reuses outputs from the `Demographics` asset.  
4. **Compute Rural Population**  
   - Reprojects the SMOD raster to match each WorldPop raster.  
   - Multiplies each population raster by the rural mask (`smod == 1`).  
   - Performs zonal statistics per administrative unit (e.g., ADM2).  
5. **Output Generation**  
   - Aggregates results into a CSV file per country and administrative level.  
   - Adds both absolute (`_rural`) and relative (`_rural_perc`) population values.

### Outputs <a id="outputs-5"></a>
- CSV file: `{country_code}_{admin_level}_rural_population.csv`
  - Columns:
    - `{admin_level}_PCODE`
    - `ADM_PCODE` (alias column for compatibility)
    - `total_pop_rural`, `female_pop_rural`, `children_u5_rural`
    - `female_u5_rural`, `elderly_rural`, `pop_u15_rural`, `female_u15_rural`, `wra_pop_rural`
    - `dependency_ratio_rural` (rural dependency ratio = dependents / working × 100)
    - `rural_pop_perc` (percentage of population living in rural areas)
  - CRS: WGS84 (`EPSG:4326`)
  - Units: counts and percentages per administrative unit


:::{dropdown} Python Script (Rural Population)
```python
import os
import shutil
import zipfile
import requests
from pathlib import Path
import rioxarray
import rasterio
import pandas as pd
import numpy as np
import argparse
import logging
import geopandas as gpd

from rasterstats import zonal_stats
from scripts.fetch_worldpop import fetch_worldpop, INDICATORS

RECLASS_MAP = {
    10: None,
    11: 1, 12: 1, 13: 1,   # rural
    21: 2, 22: 2, 23: 2, 30: 2,  # urban
}
SMOD_ZIP_URL = (
    "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/"
    "GHS_SMOD_GLOBE_R2023A/GHS_SMOD_E2030_GLOBE_R2023A_54009_1000/"
    "V2-0/GHS_SMOD_E2030_GLOBE_R2023A_54009_1000_V2_0.zip"
)


def download_and_unzip_smod(work_dir, context):
    zip_path = Path(work_dir) / "smod.zip"
    unzip_dir = Path(work_dir) / "unzipped"
    unzip_dir.mkdir(parents=True, exist_ok=True)

    if not zip_path.exists():
        context.info("Downloading SMOD global raster…")
        resp = requests.get(SMOD_ZIP_URL, stream=True)
        resp.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in resp.iter_content(1024 * 1024):
                f.write(chunk)
    else:
        context.info("SMOD ZIP already exists, skipping download.")

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(unzip_dir)

    for root, _, files in os.walk(unzip_dir):
        for fn in files:
            if fn.lower().endswith(".tif"):
                return zip_path, unzip_dir, Path(root) / fn

    raise FileNotFoundError("No .tif found in SMOD ZIP")


def reclassify_raster(in_tif, out_tif, reclass_map, context):
    with rasterio.open(in_tif) as src:
        meta = src.meta.copy()
        arr = src.read(1)
        nodata_val = 0
        out = np.full(arr.shape, nodata_val, dtype=np.uint8)
        for old, new in reclass_map.items():
            mask_val = (arr == old)
            if new is None:
                out[mask_val] = nodata_val
            else:
                out[mask_val] = new
        meta.update(count=1, dtype="uint8", nodata=nodata_val)
        with rasterio.open(out_tif, "w", **meta) as dst:
            dst.write(out, 1)
    context.info(f"Reclassified raster saved to {out_tif}")


def compute_rural_population(country_code, admin_level, gdf, work_dir, output_dir, context):
    country_code = country_code.upper()
    work_dir = Path(f"{work_dir}/downloads")
    temp_dir = Path(f"{work_dir}/data/{country_code}/Temporary")
    output_dir = Path(output_dir)
    reclass_tif = work_dir / "smod_reclass.tif"
    out_csv = output_dir / f"{country_code}_{admin_level}_rural_population.csv"

    if out_csv.exists():
        context.info(f"CSV already exists, skipping: {out_csv}")
        return str(out_csv)

    zip_path = None
    unzip_dir = None

    try:
        if not reclass_tif.exists():
            context.info("smod_reclass.tif missing — will generate it")
            zip_path, unzip_dir, smod_tif = download_and_unzip_smod(work_dir, context)
            reclassify_raster(smod_tif, reclass_tif, RECLASS_MAP, context)
        else:
            context.info("Using existing smod_reclass.tif")

        context.info(f"Ensuring demographic rasters exist in {temp_dir}...")
        indicator_tifs = fetch_worldpop(country_code)
        indicators = ["total_pop", "female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15", "wra_pop", "dep_dependents", "dep_working"]
        tif_map = dict(zip(INDICATORS.keys(), indicator_tifs))

        smod = rioxarray.open_rasterio(reclass_tif, masked=True).squeeze()

        rural_df = pd.DataFrame({
            f"{admin_level}_PCODE": gdf[f"{admin_level}_PCODE"]
        })
        rural_df["ADM_PCODE"] = gdf[f"{admin_level}_PCODE"]

        total_pop_counts = {}

        for label in indicators:
            pop_raster_path = tif_map[label]
            pop_raster = rioxarray.open_rasterio(pop_raster_path, masked=True).squeeze()

            smod_aligned = smod.rio.reproject_match(pop_raster, resampling=rasterio.enums.Resampling.nearest)
            rural_mask = (smod_aligned == 1).astype("float32")
            rural_pop = pop_raster * rural_mask

            tmp_rural = work_dir / f"tmp_rural_{label}.tif"
            with rasterio.open(pop_raster_path) as src:
                meta = src.meta.copy()
                meta.update(compress="lzw", tiled=True,
                            bigtiff="yes" if src.width * src.height > 2**32 else "no")
            with rasterio.open(tmp_rural, "w", **meta) as dst:
                dst.write(rural_pop.values, 1)

            stats = zonal_stats(gdf, tmp_rural, stats="sum", nodata=0)
            rural_df[f"{label}_rural"] = [s["sum"] if s["sum"] is not None else 0 for s in stats]

            total_stats = zonal_stats(gdf, pop_raster_path, stats="sum", nodata=0)
            total_pop_counts[label] = [s["sum"] if s["sum"] is not None else 0 for s in total_stats]

            context.info(f"Processed rural population for {label}")

        dep_col_num = rural_df["dep_dependents_rural"]
        dep_col_den = rural_df["dep_working_rural"].replace(0, pd.NA)
        rural_df["dependency_ratio_rural"] = ((dep_col_num / dep_col_den) * 100).fillna(0).round(2)
        rural_df.drop(columns=["dep_dependents_rural", "dep_working_rural"], inplace=True)

        total_pop = pd.Series(total_pop_counts["total_pop"]).replace({0: np.nan})
        rural_df["rural_pop_perc"] = (
            rural_df["total_pop_rural"] / total_pop * 100
        ).fillna(0).round(2)

        count_cols = [c for c in rural_df.columns if c.endswith("_rural") and "dependency_ratio" not in c]
        perc_cols = [c for c in rural_df.columns if c.endswith("_rural_perc")]

        rural_df[count_cols] = rural_df[count_cols].fillna(0).round(0).astype(int)
        rural_df[perc_cols] = rural_df[perc_cols].fillna(0).round(2)

        output_dir.mkdir(parents=True, exist_ok=True)
        rural_df.to_csv(out_csv, index=False)
        context.info(f"Rural population CSV written to {out_csv}")

    finally:
        if zip_path and zip_path.exists():
            zip_path.unlink()
            context.info(f"Deleted {zip_path}")
        if unzip_dir and unzip_dir.exists():
            shutil.rmtree(unzip_dir)
            context.info(f"Deleted {unzip_dir}")
        for tmp_file in work_dir.glob("tmp_rural_*.tif"):
            try:
                tmp_file.unlink()
                context.info(f"Deleted {tmp_file}")
            except Exception as e:
                context.info(f"Failed to delete {tmp_file}: {e}")

    return str(out_csv)
```
:::

---
## 6. Rural Accessibility Index (RAI) <a id="6-rural-accessibility-index-rai"></a>
Computes the percentage of rural population with access to a paved road within 2 km. The Rural Accessibility Index measures the proportion of people living in rural areas (GHS-SMOD classes 11–13) who live within 2 km of a paved road surface. Results are provided for multiple demographic groups and as a dependency ratio for the accessible rural population.

### Data Sources <a id="data-sources-6"></a>
- **Road Surface Data:** Mapillary road surface classification (`pred_label == 0` for paved) and Planet road surface classification (`DL_road_class_2024 == "paved"`), downloaded from HEiGIT/HDX storage.
- **GHS-SMOD Raster:** Global Human Settlement Layer settlement model for 2030, used to classify grid cells as rural (classes 11–13).
- **WorldPop Population Rasters:** Used to extract population counts per demographic group within accessible rural areas.
- **Administrative Boundaries** (GeoJSON): Used to disaggregate results per admin unit.

### Indicators <a id="indicators-6"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `rural_access_{group}` | Population in rural areas within 2 km of a paved road | people |
| `RAI_{group}` | Rural Accessibility Index = rural access / rural pop × 100 | % |
| `rural_access_dependency_ratio` | Dependency ratio within accessible rural areas | % |

Demographic groups: `total_pop`, `female_pop`, `children_u5`, `female_u5`, `elderly`, `pop_u15`, `female_u15`, `wra_pop`, `dependents`, `working`.

### Processing Steps <a id="processing-steps-6"></a>
1. **Download road surface data** (Mapillary and Planet) for the country, filter to paved roads only.
2. **Buffer paved roads by 2 km** in a projected CRS (UTM zone estimated from country centroid).
3. **Intersect buffered roads with admin boundaries** to determine per-admin-unit road service areas.
4. **Download and reclassify GHS-SMOD raster** into rural (1) / urban (2) / excluded (0).
5. **Clip SMOD to country boundary** and vectorize rural pixels into polygons.
6. **Intersect rural polygons with buffered roads** to identify accessible rural areas.
7. **Extract WorldPop population counts** for each demographic group within accessible rural areas.
8. **Load rural population totals** from the *Rural Population* CSV to use as denominator.
9. **Compute RAI ratios:** `rural_access_{group} / {group}_rural × 100`.
10. **Compute dependency ratio:** `rural_access_dependents / rural_access_working × 100`.
11. **Write CSV** per admin unit.

### Outputs <a id="outputs-6"></a>
- **File:** `{country_code}_{admin_level}_rai.csv`
- **Columns:**
  - `{admin_level}_PCODE`
  - `rural_access_children_u5`, `rural_access_dependents`, `rural_access_working`
  - `rural_access_elderly`, `rural_access_female_pop`, `rural_access_female_u15`
  - `rural_access_female_u5`, `rural_access_pop_u15`, `rural_access_total_pop`
  - `rural_access_wra_pop`, `rural_access_dependency_ratio`
  - `RAI_total_pop`, `RAI_female_pop`, `RAI_children_u5`, `RAI_female_u5`
  - `RAI_elderly`, `RAI_pop_u15`, `RAI_female_u15`, `RAI_wra_pop`
- **CRS:** WGS84 (`EPSG:4326`)
- **Units:** population counts, percentages (%)

:::{dropdown} Python Script (Rural Accessibility Index)
```python
import os
import shutil
from pathlib import Path
import geopandas as gpd
import pandas as pd
import numpy as np
import rioxarray
import rasterio
import requests
from rasterstats import zonal_stats
from scripts.fetch_ruralness_ghsl import download_and_unzip_smod, reclassify_raster, RECLASS_MAP
from scripts.fetch_worldpop import fetch_worldpop, INDICATORS as WP_INDICATORS

RAI_INDICATORS = [
    "total_pop", "female_pop", "children_u5", "female_u5",
    "elderly", "pop_u15", "female_u15", "wra_pop",
    "dep_dependents", "dep_working",
]

OUTPUT_NAME_MAP = {
    "total_pop": "total_pop", "female_pop": "female_pop",
    "children_u5": "children_u5", "female_u5": "female_u5",
    "elderly": "elderly", "pop_u15": "pop_u15",
    "female_u15": "female_u15", "wra_pop": "wra_pop",
    "dep_dependents": "dependents", "dep_working": "working",
}

ISO3_TO_ISO2 = {
    "AFG": "AF", "AGO": "AO", "ALB": "AL", "ARE": "AE", "ARG": "AR",
    "ARM": "AM", "ATG": "AG", "AZE": "AZ", "BDI": "BI", "BEN": "BJ",
    "BFA": "BF", "BGD": "BD", "BGR": "BG", "BHR": "BH", "BHS": "BS",
    "BLR": "BY", "BLZ": "BZ", "BOL": "BO", "BRA": "BR", "BRB": "BB",
    "BTN": "BT", "BWA": "BW", "CAF": "CF", "CHL": "CL", "CHN": "CN",
    "CIV": "CI", "CMR": "CM", "COD": "CD", "COG": "CG", "COL": "CO",
    "COM": "KM", "CPV": "CV", "CRI": "CR", "CUB": "CU", "DJI": "DJ",
    "DMA": "DM", "DOM": "DO", "DZA": "DZ", "ECU": "EC", "EGY": "EG",
    "ERI": "ER", "ESH": "EH", "ETH": "ET", "FJI": "FJ", "FSM": "FM",
    "GAB": "GA", "GEO": "GE", "GHA": "GH", "GIN": "GN", "GMB": "GM",
    "GNB": "GW", "GNQ": "GQ", "GRC": "GR", "GRD": "GD", "GTM": "GT",
    "GUY": "GY", "HND": "HN", "HTI": "HT", "HUN": "HU", "IDN": "ID",
    "IRN": "IR", "IRQ": "IQ", "JAM": "JM", "KAZ": "KZ", "KEN": "KE",
    "KGZ": "KG", "KHM": "KH", "KIR": "KI", "KNA": "KN", "KWT": "KW",
    "LAO": "LA", "LBN": "LB", "LBR": "LR", "LBY": "LY", "LCA": "LC",
    "LKA": "LK", "LSO": "LS", "MAR": "MA", "MDA": "MD", "MDG": "MG",
    "MDV": "MV", "MEX": "MX", "MHL": "MH", "MKD": "MK", "MLI": "ML",
    "MMR": "MM", "MNG": "MN", "MOZ": "MZ", "MRT": "MR", "MUS": "MU",
    "MWI": "MW", "MYS": "MY", "NAM": "NA", "NER": "NE", "NGA": "NG",
    "NIC": "NI", "NPL": "NP", "OMN": "OM", "PAK": "PK", "PAN": "PA",
    "PER": "PE", "PHL": "PH", "PNG": "PG", "PRK": "KP", "PRY": "PY",
    "QAT": "QA", "ROU": "RO", "RUS": "RU", "RWA": "RW", "SAU": "SA",
    "SDN": "SD", "SEN": "SN", "SLB": "SB", "SLE": "SL", "SLV": "SV",
    "SOM": "SO", "SSD": "SS", "STP": "ST", "SUR": "SR", "SWZ": "SZ",
    "SYC": "SC", "SYR": "SY", "TCD": "TD", "TGO": "TG", "THA": "TH",
    "TJK": "TJ", "TLS": "TL", "TON": "TO", "TTO": "TT", "TUN": "TN",
    "TUR": "TR", "TZA": "TZ", "UGA": "UG", "UKR": "UA", "URY": "UY",
    "UZB": "UZ", "VCT": "VC", "VEN": "VE", "VNM": "VN", "VUT": "VU",
    "YEM": "YE", "ZAF": "ZA", "ZMB": "ZM", "ZWE": "ZW",
}


def country_iso2(country_code):
    return ISO3_TO_ISO2.get(country_code.upper(), country_code[:2])


def download_road_data(country_code, download_dir, context):
    country_code = country_code.upper()
    iso3_lower = country_code.lower()
    iso2 = country_iso2(country_code).lower()
    download_dir = Path(download_dir)
    download_dir.mkdir(parents=True, exist_ok=True)

    mapillary_url = (
        f"https://downloads.ohsome.org/hdx/mapillary_road_surface/"
        f"heigit_{iso3_lower}_roadsurface_lines.gpkg"
    )
    planet_url = (
        f"https://hot.storage.heigit.org/heigit-hdx-public/planet_road_data/"
        f"heigit_{iso2.upper()}_planet_roadsurface_lines.gpkg"
    )

    mapillary_path = download_dir / f"heigit_{iso3_lower}_roadsurface_lines.gpkg"
    planet_path = download_dir / f"heigit_{iso2.upper()}_planet_roadsurface_lines.gpkg"

    paths = {"mapillary": None, "planet": None}

    if mapillary_path.exists():
        paths["mapillary"] = str(mapillary_path)
    else:
        resp = requests.get(mapillary_url, stream=True, timeout=300)
        if resp.status_code == 200:
            with open(mapillary_path, "wb") as f:
                for chunk in resp.iter_content(1024 * 1024):
                    f.write(chunk)
            paths["mapillary"] = str(mapillary_path)

    if planet_path.exists():
        paths["planet"] = str(planet_path)
    else:
        resp = requests.get(planet_url, stream=True, timeout=300)
        if resp.status_code == 200:
            with open(planet_path, "wb") as f:
                for chunk in resp.iter_content(1024 * 1024):
                    f.write(chunk)
            paths["planet"] = str(planet_path)

    return paths


def estimate_utm(gdf):
    centroid = gdf.dissolve().centroid.iloc[0]
    lon, lat = centroid.x, centroid.y
    utm_zone = int((lon + 180) / 6) + 1
    return f"EPSG:{32600 + utm_zone if lat >= 0 else 32700 + utm_zone}"


RAI_OUTPUT_COLUMNS = [
    "rural_access_children_u5", "rural_access_dependents", "rural_access_working",
    "rural_access_elderly", "rural_access_female_pop", "rural_access_female_u15",
    "rural_access_female_u5", "rural_access_pop_u15", "rural_access_total_pop",
    "rural_access_wra_pop", "rural_access_dependency_ratio",
    "RAI_total_pop", "RAI_female_pop", "RAI_children_u5", "RAI_female_u5",
    "RAI_elderly", "RAI_pop_u15", "RAI_female_u15", "RAI_wra_pop",
]


def compute_rai(country_code, admin_level, gdf_admin, output_dir, work_dir,
                mapillary_path, planet_path, demographics_csv, rural_csv, context):
    country_code = country_code.upper()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    work_dir = Path(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    temp_dir = work_dir / "rai_temp"
    temp_dir.mkdir(parents=True, exist_ok=True)

    id_col = f"{admin_level}_PCODE"
    if id_col not in gdf_admin.columns:
        raise ValueError(f"Column {id_col} not found in admin boundaries")

    out_csv = output_dir / f"{country_code}_{admin_level}_rai.csv"
    if out_csv.exists():
        return str(out_csv)

    # 1. Load paved road data
    all_roads = []
    if mapillary_path and os.path.exists(mapillary_path):
        mly = gpd.read_file(mapillary_path)
        if "pred_label" in mly.columns:
            mly = mly[mly["pred_label"] == 0]
        all_roads.append(mly.to_crs(4326))
    if planet_path and os.path.exists(planet_path):
        plt = gpd.read_file(planet_path)
        if "DL_road_class_2024" in plt.columns:
            plt = plt[plt["DL_road_class_2024"] == "paved"]
        all_roads.append(plt.to_crs(4326))
    if not all_roads:
        pd.DataFrame({id_col: gdf_admin[id_col]}).to_csv(out_csv, index=False)
        return str(out_csv)

    merged_roads = pd.concat(all_roads, ignore_index=True)

    # 2. Buffer roads by 2 km
    utm_crs = estimate_utm(gdf_admin)
    buffered = (
        merged_roads[["geometry"]].to_crs(utm_crs).buffer(2000).union_all()
    )
    buffered_gdf = gpd.GeoDataFrame(geometry=[buffered], crs=utm_crs).to_crs(4326)

    roads_by_adm = gpd.overlay(buffered_gdf, gdf_admin[[id_col, "geometry"]], how="intersection")
    if roads_by_adm.empty:
        pd.DataFrame({id_col: gdf_admin[id_col]}).to_csv(out_csv, index=False)
        return str(out_csv)

    # 3. Process GHS-SMOD
    smod_work = Path("downloads")
    smod_work.mkdir(parents=True, exist_ok=True)
    reclass_tif = smod_work / "smod_reclass.tif"
    if not reclass_tif.exists():
        _, _, smod_tif = download_and_unzip_smod(smod_work, context)
        reclassify_raster(smod_tif, reclass_tif, RECLASS_MAP, context)

    # 4. Clip SMOD to country
    adm0_path = Path(output_dir).parent.parent / f"{country_code}_ADM0.geojson"
    if adm0_path.exists():
        gdf_adm0 = gpd.read_file(adm0_path)
    else:
        gdf_adm0 = gdf_admin.dissolve()

    smod = rioxarray.open_rasterio(reclass_tif, masked=True).squeeze()
    gdf_adm0_smod = gdf_adm0.to_crs(smod.rio.crs)
    smod_clipped = smod.rio.clip(gdf_adm0_smod.geometry, drop=True)
    rural_mask = (smod_clipped == 1).astype("float32")

    # 5. Vectorize rural SMOD
    from rasterio.features import shapes as rasterio_shapes
    from shapely.geometry import shape

    rural_values = (smod_clipped.values == 1).astype("uint8")
    transform = smod_clipped.rio.transform()
    poly_gen = rasterio_shapes(rural_values, mask=rural_values == 1, transform=transform)
    rural_geoms = [shape(g) for g, _ in poly_gen if g]
    if not rural_geoms:
        pd.DataFrame({id_col: gdf_admin[id_col]}).to_csv(out_csv, index=False)
        return str(out_csv)

    rural_gdf = gpd.GeoDataFrame(geometry=rural_geoms, crs=smod_clipped.rio.crs)
    rural_gdf["geometry"] = rural_gdf["geometry"].make_valid()
    rural_single = rural_gdf.dissolve().to_crs(4326)

    # 6. Intersect rural with buffered roads
    accessible_rural = gpd.overlay(buffered_gdf, rural_single, how="intersection")
    if accessible_rural.empty:
        pd.DataFrame({id_col: gdf_admin[id_col]}).to_csv(out_csv, index=False)
        return str(out_csv)

    accessible_rural = accessible_rural.dissolve()
    accessible_rural["geometry"] = accessible_rural["geometry"].make_valid()

    # 7. Per admin unit
    admin_accessible = gpd.overlay(
        gdf_admin[[id_col, "geometry"]], accessible_rural, how="intersection",
    )
    if admin_accessible.empty:
        pd.DataFrame({id_col: gdf_admin[id_col]}).to_csv(out_csv, index=False)
        return str(out_csv)

    admin_accessible["geometry"] = admin_accessible["geometry"].make_valid()

    # 8. Extract population counts
    indicator_tifs = fetch_worldpop(country_code)
    tif_map = dict(zip(WP_INDICATORS.keys(), indicator_tifs))

    results = pd.DataFrame({id_col: gdf_admin[id_col]})
    for indicator in RAI_INDICATORS:
        pop_tif = tif_map[indicator]
        stats = zonal_stats(admin_accessible, pop_tif, stats="sum", nodata=0)
        output_name = {
            "total_pop": "total_pop", "female_pop": "female_pop",
            "children_u5": "children_u5", "female_u5": "female_u5",
            "elderly": "elderly", "pop_u15": "pop_u15",
            "female_u15": "female_u15", "wra_pop": "wra_pop",
            "dep_dependents": "dependents", "dep_working": "working",
        }[indicator]
        pcode_to_sum = pd.Series(
            [round(s["sum"], 0) if s["sum"] is not None else 0 for s in stats],
            index=admin_accessible[id_col].values,
        )
        results[f"rural_access_{output_name}"] = (
            results[id_col].map(pcode_to_sum).fillna(0).astype(int)
        )

    # 9. Load rural population CSV for denominators
    df_rural = pd.read_csv(rural_csv)
    rural_denom = {
        ind: f"{ind}_rural"
        for ind in RAI_INDICATORS
        if ind not in ("dep_dependents", "dep_working")
    }
    rural_cols = [id_col] + list(rural_denom.values())
    available_rural_cols = [c for c in rural_cols if c in df_rural.columns]
    if available_rural_cols:
        results = results.merge(df_rural[available_rural_cols], on=id_col, how="left")

    # 10. Compute RAI ratios
    name_to_key = {v: k for k, v in {
        "total_pop": "total_pop", "female_pop": "female_pop",
        "children_u5": "children_u5", "female_u5": "female_u5",
        "elderly": "elderly", "pop_u15": "pop_u15",
        "female_u15": "female_u15", "wra_pop": "wra_pop",
        "dependents": "dep_dependents", "working": "dep_working",
    }.items()}

    for output_name in ["total_pop", "female_pop", "children_u5", "female_u5",
                         "elderly", "pop_u15", "female_u15", "wra_pop"]:
        access_col = f"rural_access_{output_name}"
        rural_col = f"{output_name}_rural"
        ratio_col = f"RAI_{output_name}"
        if rural_col in results.columns:
            results[ratio_col] = np.where(
                results[rural_col].fillna(0) > 0,
                (results[access_col].fillna(0) / results[rural_col].replace(0, np.nan) * 100).round(1),
                0,
            )

    dep_num = results["rural_access_dependents"].fillna(0)
    dep_den = results["rural_access_working"].replace(0, pd.NA)
    results["rural_access_dependency_ratio"] = np.where(
        dep_den.notna() & (dep_den > 0),
        (dep_num / dep_den * 100).round(1),
        pd.NA,
    )

    # 11. Finalize and save
    final_cols = [id_col] + [c for c in RAI_OUTPUT_COLUMNS if c in results.columns]
    results[final_cols].round(1).to_csv(out_csv, index=False)

    shutil.rmtree(temp_dir, ignore_errors=True)
    return str(out_csv)
```
:::


## 7. Vulnerability <a id="7-vulnerability"></a>
Represents the sensitivity of a population to external shocks based on demographic composition and settlement type.  
This layer combines *Demographics* and *Rural Population* indicators to highlight population groups more likely to experience heightened vulnerability in rural or hard-to-reach regions.

### Data Sources <a id="data-sources-7"></a>
- **Demographics CSVs:** Derived from [WorldPop](https://www.worldpop.org/) population datasets, disaggregated by age and sex (see *Demographics* chapter).  
- **Rural Population CSVs:** Derived from settlement layer analysis separating rural and urban populations (see *Rural Population* chapter).  
- Both datasets are aggregated to the same administrative level (e.g., ADM2).

### Processing Steps <a id="processing-steps-7"></a>
1. **Input CSVs:**  
   - One *Demographics* CSV and one *Rural Population* CSV are provided per administrative level.  
   - Each file contains an identifier column such as `ADM0_PCODE`, `ADM1_PCODE`, or `ADM2_PCODE`.

2. **Column Detection:**  
   - The script automatically detects the administrative identifier column by finding any column ending with `_PCODE`.

3. **Merge Operation:**  
   - The two datasets are merged on the identified `*_PCODE` column using a **left join**.  
   - This ensures demographic indicators are retained even when some administrative areas lack rural population data.

4. **Output Generation:**  
   - The merged dataset is exported as `{country_code}_{admin_level}_vulnerability.csv` to the `Output/` directory.  
   - One file is created per administrative level present in the input data.

### Outputs <a id="outputs-7"></a>
- **File:** `{country_code}_{admin_level}_vulnerability.csv`
- **Columns:**
  - `{admin_level}_PCODE`
  - All demographic indicator columns (e.g., `female_pop`, `children_u5`, `elderly`, `pop_u15`)
  - All rural population indicator columns (e.g., `rural_pop`, `urban_pop`, `rural_ratio`)
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** Population counts and ratios aggregated per administrative unit

:::{dropdown} Python SCript (Vulnerability)
```python
import os
import pandas as pd
from pathlib import Path
from typing import List

def vulnerability_asset(context, demographics_asset: List[str], rural_asset: List[str]) -> list[str]:
    """
    Combine demographics and rural population CSVs into a single vulnerability dataset.
    Joins on the ADM*_PCODE column per admin level.
    Produces one vulnerability CSV per admin level in Output/.
    """
    country_code = context.partition_key.upper()
    outputs = []

    for demo_csv, rural_csv in zip(demographics_asset, rural_asset):
        if not os.path.exists(demo_csv) or not os.path.exists(rural_csv):
            context.log.warning(f"Skipping merge for {country_code}: missing files {demo_csv}, {rural_csv}")
            continue

        try:
            df_demo = pd.read_csv(demo_csv)
            df_rural = pd.read_csv(rural_csv)

            # detect admin code column automatically (ADM0_PCODE, ADM1_PCODE, etc.)
            id_col = [c for c in df_demo.columns if c.endswith("_PCODE")]
            if not id_col:
                context.log.warning(f"Skipping {demo_csv}: no *_PCODE column found")
                continue
            id_col = id_col[0]

            merged = pd.merge(df_demo, df_rural, on=id_col, how="left")

            admin_level = id_col.split("_")[0]  # e.g., ADM2
            output_dir = Path("data") / country_code / "Output"
            output_dir.mkdir(parents=True, exist_ok=True)

            output_path = output_dir / f"{country_code}_{admin_level}_vulnerability.csv"
            merged.to_csv(output_path, index=False)
            outputs.append(str(output_path))

            context.log.info(f"[{country_code}] Wrote vulnerability CSV: {output_path}")

        except Exception as e:
            context.log.warning(f"Failed to merge {demo_csv} and {rural_csv}: {e}")

    if not outputs:
        context.log.warning(f"No vulnerability outputs created for {country_code}")
    return outputs
```
:::

---
## 8. Flood Exposure <a id="8-flood-exposure"></a>
Estimates population and facility exposure to flooding using **GLOFAS flood hazard rasters** and **WorldPop demographic layers**. Flooded areas are identified by usign a threshold of 30 cm, and exposure metrics are aggregated per administrative boundary.

This layer provides indicators for the number of people affected per demographic group and the percentage/count of critical facilities (education, hospitals, primary healthcare) impacted by flood events of different return periods (RPs).

### Data Sources <a id="data-sources-8"></a>
- **GLOFAS Flood Hazard Rasters** (`https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/`)  
  Raster tiles containing flood depth values for different return periods (RPs).  
- **WorldPop Population Layers** (`scripts/fetch_worldpop.py`)  
  Demographic rasters for multiple indicators at ~100 m resolution: total population, female, children under 5, elderly, etc.  
- **Facilities Data** (`scripts/fetch_facilities_ohsome_overpass.py`)  
  Point geometries of critical infrastructure from OHSOME or Overpass APIs.  
- **Administrative Boundaries** (GeoJSON)  
  Used to aggregate flood exposure per ADM level (e.g., ADM1).  
- **Configuration File** (`configs/assets_config.yaml`)  
  Specifies:  
  - `setup.flood_threshold` (flood depth in meters)  
  - `setup.rps` (return periods)  
  - `facilities_asset.api` (data source for facilities)

### Indicators <a id="indicators-4"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `RP{rp}_female_pop_{thresh}` | Number of females affected by flood depth ≥ threshold | people |
| `RP{rp}_children_u5_{thresh}` | Number of children under 5 affected | people |
| `RP{rp}_female_u5_{thresh}` | Number of female children under 5 affected | people |
| `RP{rp}_elderly_{thresh}` | Number of elderly (>65) affected | people |
| `RP{rp}_pop_u15_{thresh}` | Number of population under 15 affected | people |
| `RP{rp}_female_u15_{thresh}` | Number of female population under 15 affected | people |
| `RP{rp}_wra_pop_{thresh}` | Number of women of reproductive age (15–49) affected | people |
| `RP{rp}_dependency_ratio_{thresh}` | Dependency ratio of the affected population | % |
| `RP{rp}_education_{thresh}_pct` | Percentage of educational facilities flooded | % |
| `RP{rp}_education_{thresh}_count` | Number of educational facilities flooded | count |
| `RP{rp}_hospitals_{thresh}_pct` | Percentage of hospitals flooded | % |
| `RP{rp}_hospitals_{thresh}_count` | Number of hospitals flooded | count |
| `RP{rp}_primary_healthcare_{thresh}_pct` | Percentage of primary healthcare facilities flooded | % |
| `RP{rp}_primary_healthcare_{thresh}_count` | Number of primary healthcare facilities flooded | count |

> `{rp}` is the return period (e.g., 10, 50, 100 years), `{thresh}` is the flood threshold in cm.

### Flood Threshold <a id="flood-threshold"></a>
| Parameter | Value | Description |
|-----------|-------|-------------|
| `setup.flood_threshold` | e.g., 0.3 m | Minimum flood depth considered for exposure (configurable in `assets_config.yaml`) |

### Processing Steps <a id="processing-steps-8"></a>
1. **Configuration Loading**  
   - Reads `setup.flood_threshold` and `rps` from `assets_config.yaml`.  
   - Computes `THRESH_SUFFIX` (flood depth in cm) for indicator naming.

2. **Input Geometry**  
   - Loads administrative boundaries (`data/{country_code}/{country_code}_{admin_level}.geojson`) using GeoPandas.

3. **Tile Selection and Download**  
   - Queries GLOFAS server for all flood tiles corresponding to each RP.  
   - Selects only tiles intersecting the country boundary.  
   - Downloads missing tiles into `data/{country_code}/Temporary`.

4. **Raster Merging and Clipping**  
   - Merges selected tiles into a single raster per RP.  
   - Clips the merged raster to the country boundary and saves to `Temporary`.

5. **WorldPop Population Preparation**  
   - Fetches required demographic rasters (female, children under 5, female under 5, elderly, under 15, female under 15, women of reproductive age, dependents, working-age population).  
   - Ensures rasters exist locally for alignment with flood data.

6. **Facility Data Preparation**  
   - Downloads or loads facilities geometries from the chosen API (`ohsome-api`, `overpass`).  
   - Converts geometries to points and reprojects to match raster CRS.

7. **Flood Exposure Calculation per RP**  
   - **Flooded population**: Multiplies population raster by flood mask (flood depth ≥ threshold) to compute the number of affected people per ADM polygon.  
   - **Flooded facilities**: Samples flood raster at facility locations to compute flooded count and percentage per ADM polygon.

8. **Aggregation and CSV Output**  
   - Merges RP results across population and facilities into a single CSV.  
   - Fills missing values with 0 and rounds numbers to integers.  
   - Final CSV saved to `data/{country_code}/Output/{country_code}_{admin_level}_flood_exposure.csv`.

### Outputs <a id="outputs-8"></a>
- **File:** `{country_code}_{admin_level}_flood_exposure.csv`  
- **Columns:**
  - `{admin_level}_PCODE`
  - Flooded population indicators per RP
  - Flooded facilities indicators per RP
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** people, %, count  

:::{dropdown} Python Script (Flood Exposure)
```python
import os
import re
import argparse
import requests
import geopandas as gpd
import rasterio
from rasterio.merge import merge
from rasterio.mask import mask
from rasterstats import zonal_stats
from rasterio.enums import Resampling
import pandas as pd
import rioxarray
import yaml
from shapely.geometry import mapping
from pathlib import Path

from scripts.fetch_worldpop import fetch_worldpop
from scripts.fetch_facilities_ohsome_overpass import fetch_overpass, fetch_ohsome

ASSET_CONFIG_YAML_PATH = os.path.join(os.getcwd(), "configs", "assets_config.yaml")
with open(ASSET_CONFIG_YAML_PATH) as _fp:
    _asset_config = yaml.safe_load(_fp)

BASE_URL_TEMPLATE = "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/{rp}/"
ALLOWED_RPS = _asset_config.get("setup", {}).get("rps", [])

try:
    FLOOD_THRESHOLD = float(_asset_config["setup"]["flood_threshold"])
except KeyError:
    raise KeyError("Missing 'setup.flood_threshold' in assets_config.yaml")

THRESH_SUFFIX = f"{int(FLOOD_THRESHOLD*100)}cm"


def parse_listing(rp):
    url = BASE_URL_TEMPLATE.format(rp=f"RP{rp}")
    r = requests.get(url)
    r.raise_for_status()
    return re.findall(r'href="([^"]+_RP{}_depth\.tif)"'.format(rp), r.text)


def tile_bounds_from_filename(fname):
    m = re.search(r'_(N|S)(\d+)_([EW])(\d+)_RP', fname)
    if not m:
        return None
    lat_sign = 1 if m.group(1) == "N" else -1
    lat = int(m.group(2)) * lat_sign
    lon_sign = 1 if m.group(3) == "E" else -1
    lon = int(m.group(4)) * lon_sign
    xmin = lon
    xmax = lon + 10
    ymin = lat - 10
    ymax = lat
    return (xmin, ymin, xmax, ymax)


def bbox_intersects(tile_bbox, geom_bbox):
    txmin, tymin, txmax, tymax = tile_bbox
    gxmin, gymin, gxmax, gymax = geom_bbox
    return not (txmax <= gxmin or txmin >= gxmax or tymax <= gymin or tymin >= gymax)


def download_file(context, fname, temporary_dir, rp):
    url = BASE_URL_TEMPLATE.format(rp=f"RP{rp}") + fname
    outpath = os.path.join(temporary_dir, fname)
    if os.path.exists(outpath):
        context.info(f"Already exists: {fname}")
        return outpath
    context.info(f"Downloading {fname}...")
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(outpath, "wb") as f:
            for chunk in r.iter_content(1024 * 64):
                f.write(chunk)
        return outpath
    else:
        context.warning(f"Failed to download {fname}")
        return None


def process_country_rp(context, country_code, rp, admin_level="ADM0"):
    temporary_dir = f"data/{country_code}/Temporary"
    output_dir = f"data/{country_code}/Output"
    os.makedirs(temporary_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    clipped_path = os.path.join(temporary_dir, f"{country_code}_flooded_RP{rp}.tif")
    if os.path.exists(clipped_path):
        context.info(f"Clipped raster already exists: {clipped_path}, skipping ...")
        return clipped_path

    boundary_file = os.path.join("data", country_code, f"{country_code}_{admin_level}.geojson")
    if not os.path.exists(boundary_file):
        raise FileNotFoundError(f"Boundary file not found: {boundary_file}")

    gdf = gpd.read_file(boundary_file)
    gxmin, gymin, gxmax, gymax = gdf.total_bounds
    geom_bbox = (gxmin, gymin, gxmax, gymax)
    context.info(f"Boundary BBOX for {country_code}: {geom_bbox}")

    files = parse_listing(rp)
    context.info(f"Found {len(files)} tiles on server for RP{rp}.")

    selected = [f for f in files if (tb := tile_bounds_from_filename(f)) and bbox_intersects(tb, geom_bbox)]
    context.info(f"Selected {len(selected)} tiles to download.")

    tile_paths = [download_file(context, f, temporary_dir, rp) for f in selected]
    tile_paths = [p for p in tile_paths if p]

    if not tile_paths:
        context.warning(f"No tiles downloaded for RP{rp}, skipping.")
        return None

    context.info("Merging tiles...")
    srcs = [rasterio.open(p) for p in tile_paths]
    mosaic, out_trans = merge(srcs)

    out_meta = srcs[0].meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": out_trans,
        "compress": "lzw"
    })

    context.info("Clipping merged raster to boundary...")
    if gdf.crs != srcs[0].crs:
        gdf = gdf.to_crs(srcs[0].crs)

    geoms = [mapping(geom) for geom in gdf.geometry]
    with rasterio.io.MemoryFile() as memfile:
        with memfile.open(**out_meta) as dataset:
            dataset.write(mosaic)
            out_image, out_transform = mask(dataset, geoms, crop=True)

    out_meta.update({
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        "transform": out_transform
    })

    with rasterio.open(clipped_path, "w", **out_meta) as dest:
        dest.write(out_image)

    context.info(f"Clipped raster saved to {clipped_path}")

    for src in srcs:
        src.close()

    return clipped_path


def process_flood_impact(context, country_code, rps, gdf, admin_level, output_dir):
    """
    Process flooded population for all RPs of a given country/admin_level.
    Generates a single CSV with columns for each RP, indicator, threshold,
    and percentage of facilities flooded.
    """
    country_code = country_code.upper()
    output_dir = Path(output_dir)
    out_csv = output_dir / f"{country_code}_{admin_level}_flood_exposure.csv"
    temp_dir = Path("data") / country_code / "Temporary"

    # Load existing CSV if present, to append missing RPs
    if out_csv.exists():
        context.info(f"CSV exists: {out_csv}, will append missing RPs")
        final_df = pd.read_csv(out_csv)
    else:
        final_df = pd.DataFrame({f"{admin_level}_PCODE": gdf[f"{admin_level}_PCODE"]})

    # Ensure WorldPop files exist
    context.info(f"Ensuring demographic rasters exist in {temp_dir}...")
    indicator_tifs = fetch_worldpop(country_code)
    indicators = ["female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15", "wra_pop", "dep_dependents", "dep_working"]
    tif_map = dict(zip(indicators, indicator_tifs))

    final_indicators = ["female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15", "wra_pop", "dependency_ratio"]

    # Ensure facilities exist
    context.info(f"Ensuring facility raw geometries exist in {temp_dir}...")
    base_path = Path("data") / country_code
    boundary_path = base_path / f"{country_code}_{admin_level}.geojson"
    api_choice = _asset_config.get("facilities_asset", {}).get("api", "").lower()

    if api_choice == "ohsome-api":
        summary_path = fetch_ohsome(
            context, boundary_path, base_path, country_code, admin_level
        )
    elif api_choice == "overpass":
        summary_path = fetch_overpass(
            context, boundary_path, base_path, country_code, admin_level
        )
    elif api_choice == "ohsome-parquet":
        context.info("Not implemented yet: ohsome-parquet")
        return None
    else:
        context.warning(
            f"No valid API configured for facilities_asset (got '{api_choice}')"
        )
        return None

    geojsons_map = {}
    facility_categories = ["education", "hospitals", "primary_healthcare"]
    for category in facility_categories:
        if category not in geojsons_map:
            geojsons_map[category] = base_path / f"Temporary/{country_code}_{category}_raw.geojson"

    for rp in rps:
        context.info(f"Processing RP{rp}...")

        # Skip RP if all expected columns already exist
        expected_cols = [
            f"RP{rp}_{label}_{suffix}" for label in final_indicators for suffix in [THRESH_SUFFIX]
        ] + [
            f"RP{rp}_{cat}_{suffix}_pct" for cat in facility_categories for suffix in [THRESH_SUFFIX]
        ] + [
            f"RP{rp}_{cat}_{suffix}_count" for cat in facility_categories for suffix in [THRESH_SUFFIX]
        ]
        if all(col in final_df.columns for col in expected_cols):
            context.info(f"RP{rp} already processed, skipping...")
            continue

        # Flood raster clipped to country
        clipped_path = process_country_rp(context, country_code, rp, admin_level)
        if not clipped_path:
            context.warning(f"No flood raster for RP{rp}, skipping...")
            continue
        flood = rioxarray.open_rasterio(clipped_path, masked=True).squeeze()

        rp_df = pd.DataFrame({f"{admin_level}_PCODE": gdf[f"{admin_level}_PCODE"]})

        # ---- Flooded population ----
        for label in indicators:
            pop_raster_path = tif_map[label]
            pop_raster = rioxarray.open_rasterio(pop_raster_path, masked=True).squeeze()

            flood_aligned = flood.rio.reproject_match(pop_raster, resampling=Resampling.bilinear)
            flood_mask = (flood_aligned > FLOOD_THRESHOLD).astype("float32")
            flooded_pop = pop_raster * flood_mask

            tmp_flooded = temp_dir / f"tmp_flooded_{label}_RP{rp}_{THRESH_SUFFIX}.tif"
            with rasterio.open(pop_raster_path) as src:
                meta = src.meta.copy()
                meta.update(compress="lzw", tiled=True,
                            bigtiff="yes" if src.width*src.height > 2**32 else "no")
            with rasterio.open(tmp_flooded, "w", **meta) as dst:
                dst.write(flooded_pop.values, 1)

            stats = zonal_stats(gdf, tmp_flooded, stats="sum", nodata=0)
            rp_df[f"RP{rp}_{label}_{THRESH_SUFFIX}"] = [s["sum"] if s["sum"] is not None else 0 for s in stats]

            context.info(f"Processed flooded population for {label} >{FLOOD_THRESHOLD} m ({THRESH_SUFFIX})")

        # Calculate dependency ratio for the flooded population
        dep_col_num = rp_df[f"RP{rp}_dep_dependents_{THRESH_SUFFIX}"]
        dep_col_den = rp_df[f"RP{rp}_dep_working_{THRESH_SUFFIX}"].replace(0, pd.NA)
        rp_df[f"RP{rp}_dependency_ratio_{THRESH_SUFFIX}"] = ((dep_col_num / dep_col_den) * 100).fillna(0).round(2)

        # Drop the intermediate components
        rp_df.drop(columns=[f"RP{rp}_dep_dependents_{THRESH_SUFFIX}", f"RP{rp}_dep_working_{THRESH_SUFFIX}"], inplace=True)

        # ---- Flooded facilities ----
        for category, filepath in geojsons_map.items():
            if not Path(filepath).exists():
                rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_pct"] = 0
                rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_count"] = 0
                continue

            facilities = gpd.read_file(filepath)
            if facilities.empty:
                rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_pct"] = 0
                rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_count"] = 0
                continue

            if not all(facilities.geometry.type == "Point"):
                if facilities.crs != flood.rio.crs:
                    facilities = facilities.to_crs(flood.rio.crs)
                facilities["geometry"] = facilities.geometry.centroid
            if facilities.crs != flood.rio.crs:
                facilities = facilities.to_crs(flood.rio.crs)

            coords = [(x, y) for x, y in zip(facilities.geometry.x, facilities.geometry.y)]
            with rasterio.open(clipped_path) as src:
                values = [v[0] for v in src.sample(coords)]
            facilities["flooded"] = [1 if v > FLOOD_THRESHOLD else 0 for v in values]

            joined = gpd.sjoin(
                facilities, gdf[[f"{admin_level}_PCODE", "geometry"]],
                how="inner", predicate="within"
            )
            grouped = joined.groupby(f"{admin_level}_PCODE")["flooded"].agg(["mean", "sum"]).reset_index()

            grouped[f"RP{rp}_{category}_{THRESH_SUFFIX}_pct"] = (grouped["mean"] * 100).round(1)
            grouped[f"RP{rp}_{category}_{THRESH_SUFFIX}_count"] = grouped["sum"].astype(int)
            grouped = grouped.drop(columns=["mean", "sum"])

            rp_df = rp_df.merge(grouped, on=f"{admin_level}_PCODE", how="left")
            rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_pct"] = rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_pct"].fillna(0)
            rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_count"] = rp_df[f"RP{rp}_{category}_{THRESH_SUFFIX}_count"].fillna(0).astype(int)

            context.info(f"Processed flooded facilities for {category} >{FLOOD_THRESHOLD} m ({THRESH_SUFFIX})")

        final_df = final_df.merge(rp_df, on=f"{admin_level}_PCODE", how="left")
        context.info(f"Processed RP{rp}")

    numeric_cols = final_df.select_dtypes(include=["float", "int"]).columns
    final_df[numeric_cols] = final_df[numeric_cols].fillna(0).round(0).astype(int)
    output_dir.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(out_csv, index=False)
    context.info(f"Flooded population & facilities CSV written to {out_csv}")

    return str(out_csv)
```
:::

---

## 9. Cyclone Exposure <a id="9-cyclone-exposure"></a>
Estimates the exposure of population and critical facilities to tropical cyclones using **IBTrACS** storm track data. Cyclone categories are based on the Saffir-Simpson scale and grouped into three exposure classes (Cat 1, Cat 2-3, Cat 4-5). For each administrative unit, the affected population per demographic group and the count/percentage of flooded facilities are computed per category.

### Data Sources <a id="data-sources-9"></a>
- **IBTrACS Storm Tracks:** International Best Track Archive for Climate Stewardship (since 1980), downloaded from NOAA NCEI as shapefile lines with Saffir-Simpson wind speed categories.
- **WorldPop Population Rasters:** Demographic rasters for multiple indicators used to compute exposed populations (see *Demographics* chapter).
- **Facilities Data:** OSM-derived facility point geometries (education, hospitals, primary healthcare) from Ohsome or Overpass API (see *Facilities* chapter).
- **Administrative Boundaries** (GeoJSON): Used to aggregate exposure per ADM level.

### Indicators <a id="indicators-5"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `kt34_{indicator}_cat{cls}` | Exposed population for a demographic indicator at cyclone category `{cls}` | people |
| `kt34_dependency_ratio_cat{cls}` | Dependency ratio of the exposed population at category `{cls}` | % |
| `kt34_{facility}_count_cat{cls}` | Number of facilities exposed at category `{cls}` | count |
| `kt34_{facility}_perc_cat{cls}` | Percentage of facilities exposed at category `{cls}` | % |

Where `{cls}` is the cyclone exposure class (1 = Cat 1, 2 = Cat 2-3, 3 = Cat 4-5), `{indicator}` is a demographic group (`total_pop`, `female_pop`, `children_u5`, `female_u5`, `elderly`, `pop_u15`, `female_u15`, `wra_pop`), and `{facility}` is a category (`education`, `hospitals`, `primary_healthcare`).

### Cyclone Categories <a id="cyclone-categories"></a>
| Exposure Class | Saffir-Simpson Category | Wind Speed (km/h) |
|----------------|------------------------|-------------------|
| 1 | Category 1 | 119–153 |
| 2 | Categories 2–3 | 154–208 |
| 3 | Categories 4–5 | ≥ 209 |

### Processing Steps <a id="processing-steps-9"></a>
1. **Download and extract IBTrACS storm track data** from NOAA NCEI.
2. **Filter storms** with Saffir-Simpson intensity ≥ 1 and intersecting the country bounding box.
3. **Buffer storm tracks** using the mean radius of maximum winds (R34) converted to meters.
4. **Clip buffers** to the country administrative boundary.
5. **Rasterize** the buffered tracks into a classified exposure raster (classes 1, 2, 3) aligned to WorldPop resolution.
6. **Compute population exposure:** For each demographic indicator and cyclone class, multiply the population raster by the class mask and sum per admin unit using zonal statistics.
7. **Compute dependency ratio:** `kt34_dependency_ratio = (dependents / working) × 100` per class.
8. **Compute facility exposure:** Sample the cyclone exposure raster at facility point locations, then count and percentage per admin unit per class.
9. **Save CSV** with all exposure columns.

### Outputs <a id="outputs-9"></a>
- **File:** `{country_code}_{admin_level}_cyclone_exposure.csv`
- **Columns:**
  - `{admin_level}_PCODE`
  - `ADM_PCODE` (alias column)
  - Population exposed per demographic group per class: `kt34_total_pop_cat1`, `kt34_female_pop_cat2`, `kt34_children_u5_cat3`, etc.
  - Dependency ratio per class: `kt34_dependency_ratio_cat1`, `kt34_dependency_ratio_cat2`, `kt34_dependency_ratio_cat3`
  - Facility counts and percentages per class: `kt34_education_count_cat1`, `kt34_education_perc_cat1`, etc.
- **CRS:** WGS84 (`EPSG:4326`)
- **Units:** people, count, %

:::{dropdown} Python Script (Cyclone Exposure)
```python
import os
from pathlib import Path
import zipfile
import requests
import geopandas as gpd
import numpy as np
import rasterio
from rasterio.features import rasterize
from rasterstats import zonal_stats
import pandas as pd
import yaml
from scripts.fetch_worldpop import fetch_worldpop, INDICATORS
from scripts.fetch_facilities_ohsome_overpass import fetch_overpass, fetch_ohsome

ASSET_CONFIG_YAML_PATH = os.path.join(os.getcwd(), "configs", "assets_config.yaml")
with open(ASSET_CONFIG_YAML_PATH) as _fp:
    _asset_config = yaml.safe_load(_fp)

IBTRACS_URL = (
    "https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/"
    "v04r01/access/shapefile/IBTrACS.since1980.list.v04r01.lines.zip"
)
DOWNLOAD_DIR = "downloads"
IBTRACS_LOCAL_ZIP = os.path.join(DOWNLOAD_DIR, "IBTrACS.since1980.list.v04r01.lines.zip")

FACILITY_CATEGORIES = ["education", "hospitals", "primary_healthcare"]
POP_INDICATORS = ["total_pop", "female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15", "wra_pop", "dep_dependents", "dep_working"]
EXPOSURE_CLASSES = [1, 2, 3]


def ensure_ibtracs_data(context):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    if not os.path.exists(IBTRACS_LOCAL_ZIP):
        context.info("Downloading IBTrACS dataset...")
        r = requests.get(IBTRACS_URL)
        r.raise_for_status()
        with open(IBTRACS_LOCAL_ZIP, "wb") as f:
            f.write(r.content)
    extract_path = os.path.join(DOWNLOAD_DIR, "IBTrACS")
    if not os.path.exists(extract_path):
        with zipfile.ZipFile(IBTRACS_LOCAL_ZIP, "r") as zip_ref:
            zip_ref.extractall(extract_path)
    return os.path.join(extract_path, "IBTrACS.since1980.list.v04r01.lines.shp")


def build_cyclone_buffers(context, country_code, admin_level):
    shapefile_path = ensure_ibtracs_data(context)
    gdf_ibtracs = gpd.read_file(shapefile_path)
    gdf_ibtracs = gdf_ibtracs[gdf_ibtracs["USA_SSHS"].fillna(0) >= 1]

    boundary_path = f"data/{country_code}/{country_code}_{admin_level}.geojson"
    country_gdf = gpd.read_file(boundary_path)
    bbox = country_gdf.total_bounds
    gdf_ibtracs = gdf_ibtracs.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
    if gdf_ibtracs.empty:
        return None

    gdf_ibtracs = gdf_ibtracs.to_crs(epsg=29738)
    country_gdf = country_gdf.to_crs(epsg=29738)
    gdf_ibtracs["mean_r34"] = gdf_ibtracs[["USA_R34_SE", "USA_R34_NE", "USA_R34_NW", "USA_R34_SW"]].mean(axis=1, skipna=True)
    gdf_ibtracs["mean_r34_m"] = gdf_ibtracs["mean_r34"] * 1852
    gdf_ibtracs["geometry"] = gdf_ibtracs.buffer(gdf_ibtracs["mean_r34_m"].fillna(0))
    gdf_ibtracs = gpd.clip(gdf_ibtracs, country_gdf)

    out_geojson = f"data/{country_code}/Temporary/{country_code}_cyclone_buffers.geojson"
    os.makedirs(os.path.dirname(out_geojson), exist_ok=True)
    gdf_ibtracs.to_file(out_geojson, driver="GeoJSON")
    return out_geojson


def calculate_cyclone_exposure(context, country_code, admin_level="ADM2"):
    country_code = country_code.upper()
    admin_level = admin_level.upper()
    temp_dir = Path(f"data/{country_code}/Temporary")
    base_path = Path(f"data/{country_code}")

    buffer_geojson = build_cyclone_buffers(context, country_code, admin_level)
    if not buffer_geojson:
        return None

    gdf_buffers = gpd.read_file(buffer_geojson)
    indicator_tifs = fetch_worldpop(country_code)
    reference_tif = indicator_tifs[0]

    with rasterio.open(reference_tif) as src_ref:
        meta = src_ref.meta.copy()
        transform = src_ref.transform
        width = src_ref.width
        height = src_ref.height
        crs = src_ref.crs

    gdf_buffers = gdf_buffers.to_crs(crs)
    max_raster = np.zeros((height, width), dtype=np.uint8)
    gdf_sorted = gdf_buffers.sort_values("USA_SSHS")
    for _, row in gdf_sorted.iterrows():
        if row.geometry is None or np.isnan(row["USA_SSHS"]):
            continue
        level = int(row["USA_SSHS"])
        shapes = [(row.geometry, level)]
        mask_arr = rasterize(shapes, out_shape=(height, width), transform=transform, fill=0, dtype=np.uint8)
        max_raster = np.maximum(max_raster, mask_arr)

    classified = np.zeros_like(max_raster, dtype=np.uint8)
    classified[(max_raster >= 1) & (max_raster <= 1)] = 1
    classified[(max_raster >= 2) & (max_raster <= 3)] = 2
    classified[(max_raster >= 4) & (max_raster <= 5)] = 3

    raster_path = temp_dir / f"{country_code}_cyclone_exposure.tif"
    meta.update(dtype=rasterio.uint8, count=1, compress="lzw")
    with rasterio.open(raster_path, "w", **meta) as dst:
        dst.write(classified, 1)

    boundary_file = base_path / f"{country_code}_{admin_level}.geojson"
    gdf_admin = gpd.read_file(boundary_file).to_crs("EPSG:4326")
    full_tif_map = dict(zip(INDICATORS.keys(), indicator_tifs))

    df = pd.DataFrame({f"{admin_level}_PCODE": gdf_admin[f"{admin_level}_PCODE"]})
    df["ADM_PCODE"] = df[f"{admin_level}_PCODE"]

    geojsons_map = {}
    api_choice = _asset_config.get("facilities_asset", {}).get("api", "").lower()
    for cat in FACILITY_CATEGORIES:
        geojsons_map[cat] = base_path / f"Temporary/{country_code}_{cat}_raw.geojson"

    with rasterio.open(raster_path) as src:
        cyclone_raster = src.read(1).astype(np.float32)

    for indicator in POP_INDICATORS:
        pop_raster_path = full_tif_map[indicator]
        with rasterio.open(pop_raster_path) as src_pop:
            pop_raster = src_pop.read(1)
            pop_meta = src_pop.meta.copy()
        for cls in EXPOSURE_CLASSES:
            mask_cls = (cyclone_raster == cls).astype(np.float32)
            exposed_pop = pop_raster * mask_cls
            temp_path = base_path / f"Temporary/tmp_{indicator}_cat{cls}.tif"
            pop_meta.update(dtype=rasterio.float32, count=1)
            with rasterio.open(temp_path, "w", **pop_meta) as dst:
                dst.write(exposed_pop, 1)
            stats = zonal_stats(gdf_admin, temp_path, stats="sum", nodata=0)
            df[f"kt34_{indicator}_cat{cls}"] = [round(s["sum"] or 0, 0) for s in stats]

    for cls in EXPOSURE_CLASSES:
        dep_num = df[f"kt34_dep_dependents_cat{cls}"]
        dep_den = df[f"kt34_dep_working_cat{cls}"].replace(0, pd.NA)
        df[f"kt34_dependency_ratio_cat{cls}"] = ((dep_num / dep_den) * 100).fillna(0).round(2)
        df.drop(columns=[f"kt34_dep_dependents_cat{cls}", f"kt34_dep_working_cat{cls}"], inplace=True)

    for category in FACILITY_CATEGORIES:
        filepath = base_path / f"Temporary/{country_code}_{category}_raw.geojson"
        if not filepath.exists():
            continue
        facilities = gpd.read_file(filepath)
        if facilities.empty:
            continue
        facilities = facilities.to_crs(crs)
        facilities["geometry"] = facilities.geometry.centroid
        coords = [(x, y) for x, y in zip(facilities.geometry.x, facilities.geometry.y)]
        with rasterio.open(raster_path) as src:
            values = [v for v in src.sample(coords)]
        facilities["cyclone_class"] = [v[0] for v in values]
        joined = gpd.sjoin(facilities, gdf_admin[[f"{admin_level}_PCODE", "geometry"]], how="inner", predicate="within")
        total_facilities = joined.groupby(f"{admin_level}_PCODE").size().to_dict()
        for cls in EXPOSURE_CLASSES:
            mask_cls = joined["cyclone_class"] == cls
            grouped = joined[mask_cls].groupby(f"{admin_level}_PCODE").size().reset_index(name=f"kt34_{category}_count_cat{cls}")
            df = df.merge(grouped, on=f"{admin_level}_PCODE", how="left")
            df[f"kt34_{category}_count_cat{cls}"] = df[f"kt34_{category}_count_cat{cls}"].fillna(0).astype(int)
            df[f"kt34_{category}_perc_cat{cls}"] = df.apply(
                lambda x: round((x[f"kt34_{category}_count_cat{cls}"] / total_facilities.get(x[f"{admin_level}_PCODE"], 1)) * 100, 0),
                axis=1,
            )

    numeric_cols = [c for c in df.select_dtypes(include=["float", "int"]).columns if "dependency_ratio" not in c]
    df[numeric_cols] = df[numeric_cols].fillna(0).round(0).astype(int)

    output_dir = base_path / "Output"
    output_dir.mkdir(parents=True, exist_ok=True)
    out_csv = output_dir / f"{country_code}_{admin_level}_cyclone_exposure.csv"
    df.to_csv(out_csv, index=False)
    return str(out_csv)
```
:::

---

## 10. Evacuability <a id="10-evacuability"></a>
Estimates the travel time (in minutes) from at-risk areas (flooded or cyclone-affected population) to the nearest safe zone using least-cost path analysis on a motorized friction surface. This provides a measure of how quickly people in hazard-prone areas can reach areas not affected by the hazard.

### Data Sources <a id="data-sources-10"></a>
- **Flood Hazard Rasters:** GLOFAS flood depth rasters for each return period (RP), produced by the *Flood Exposure* asset.
- **Cyclone Exposure Raster:** IBTrACS cyclone exposure raster (binary: affected / not affected), produced by the *Cyclone Exposure* asset.
- **Friction Surface:** Global motorized friction surface COG (2020) hosted on MinIO (`2020_motorized_friction_surface_cog.tif`), representing travel impedance per pixel.
- **WorldPop Population Rasters:** Used to identify the demographic composition of at-risk areas.
- **Administrative Boundaries** (GeoJSON): Used to aggregate travel time statistics per admin unit.

### Indicators <a id="indicators-7"></a>
| Indicator | Description | Units |
|-----------|-------------|-------|
| `RP{rp}_evac_time_minutes_mean` | Mean travel time from flooded areas to safe zone (for return period `{rp}`) | minutes |
| `RP{rp}_evac_time_minutes_max` | Maximum travel time from flooded areas to safe zone | minutes |
| `RP{rp}_evac_time_minutes_median` | Median travel time from flooded areas to safe zone | minutes |
| `RP{rp}_pixels_at_risk` | Number of flooded pixels with computed travel time | count |
| `kt34_evac_time_minutes_mean` | Mean travel time from cyclone-affected areas to safe zone | minutes |
| `kt34_evac_time_minutes_max` | Maximum travel time from cyclone-affected areas to safe zone | minutes |
| `kt34_evac_time_minutes_median` | Median travel time from cyclone-affected areas to safe zone | minutes |
| `kt34_pixels_at_risk` | Number of cyclone-affected pixels with computed travel time | count |

### Processing Steps <a id="processing-steps-10"></a>
1. **Load hazard raster** (flood depth per RP or cyclone binary raster) for the country.
2. **Fetch friction surface** window covering the same extent and align to the hazard raster CRS/resolution.
3. **Classify pixels** into:
   - **Safe zones:** pixels where hazard ≤ threshold (flood) or hazard = 0 (cyclone).
   - **At-risk zones:** pixels where hazard > threshold.
4. **Downsample** if pixel count exceeds performance limit (10 million pixels).
5. **Compute least-cost distances** using `MCP_Geometric` from scikit-image, treating safe zones as source cells and friction as cost per meter.
6. **Upsample** travel time raster back to original resolution if downsampled.
7. **Summarize per admin unit:** mean, max, median travel time and pixel count for at-risk zones.
8. **Write CSV** with flood evacuability per RP and cyclone evacuability columns.

### Outputs <a id="outputs-10"></a>
- **File:** `{country_code}_{admin_level}_evacuability.csv`
- **Columns:**
  - `{admin_level}_PCODE`
  - Flood evacuability per return period: `RP{rp}_evac_time_minutes_mean`, `RP{rp}_evac_time_minutes_max`, `RP{rp}_evac_time_minutes_median`, `RP{rp}_pixels_at_risk`
  - Cyclone evacuability (if cyclone data exists): `kt34_evac_time_minutes_mean`, `kt34_evac_time_minutes_max`, `kt34_evac_time_minutes_median`, `kt34_pixels_at_risk`
- **CRS:** WGS84 (`EPSG:4326`)
- **Units:** minutes (travel time), pixel count

:::{dropdown} Python Script (Evacuability)
```python
import os
import numpy as np
import geopandas as gpd
import pandas as pd
import rasterio
from rasterio.windows import from_bounds, Window
from rasterio.warp import reproject, Resampling
from rasterstats import zonal_stats
from skimage.graph import MCP_Geometric
from pathlib import Path
import tempfile
import yaml

ASSET_CONFIG_YAML_PATH = os.path.join(os.getcwd(), "configs", "assets_config.yaml")
with open(ASSET_CONFIG_YAML_PATH) as _fp:
    _asset_config = yaml.safe_load(_fp)
FLOOD_THRESHOLD = float(_asset_config["setup"]["flood_threshold"])

FRICTION_COG_URL = "https://hot.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/2020_motorized_friction_surface_cog.tif"

MAX_PIXELS_FOR_MCP = 10_000_000
TARGET_RESOLUTION_M = 500
MAX_MCP_SOURCES = 20000


def fetch_friction_window(bounds, target_crs, target_transform, target_shape):
    with rasterio.open(FRICTION_COG_URL) as src:
        friction_crs = src.crs
        friction_nodata = src.nodata
        if target_crs != friction_crs:
            from rasterio.warp import transform_bounds
            src_bounds = transform_bounds(target_crs, friction_crs, *bounds)
        else:
            src_bounds = bounds
        window = from_bounds(*src_bounds, src.transform)
        col_off = max(0, int(window.col_off) - 5)
        row_off = max(0, int(window.row_off) - 5)
        width = min(src.width - col_off, int(window.width) + 10)
        height = min(src.height - row_off, int(window.height) + 10)
        window = Window(col_off, row_off, width, height)
        friction_raw = src.read(1, window=window).astype(np.float32)
        window_transform = src.window_transform(window)
    friction_aligned = np.zeros(target_shape, dtype=np.float32)
    reproject(
        source=friction_raw, destination=friction_aligned,
        src_transform=window_transform, src_crs=friction_crs,
        src_nodata=friction_nodata,
        dst_transform=target_transform, dst_crs=target_crs,
        dst_nodata=np.nan, resampling=Resampling.bilinear,
    )
    return friction_aligned


def downsample_array(arr, scale_factor, method='mean'):
    from scipy.ndimage import zoom
    if scale_factor <= 1:
        return arr
    scale_factor = int(round(scale_factor))
    if method == 'sum':
        h, w = arr.shape
        new_h = (h // scale_factor) * scale_factor
        new_w = (w // scale_factor) * scale_factor
        trimmed = arr[:new_h, :new_w]
        reshaped = trimmed.reshape(new_h // scale_factor, scale_factor, new_w // scale_factor, scale_factor)
        return np.nansum(reshaped, axis=(1, 3)).astype(arr.dtype)
    elif method == 'mean':
        return zoom(arr, 1/scale_factor, order=1)
    else:
        return zoom(arr, 1/scale_factor, order=0)


def upsample_array(arr, target_shape, method='bilinear'):
    from scipy.ndimage import zoom
    scale_y = target_shape[0] / arr.shape[0]
    scale_x = target_shape[1] / arr.shape[1]
    order = 1 if method == 'bilinear' else 0
    return zoom(arr, (scale_y, scale_x), order=order)


def create_cost_surface(friction_arr, hazard_arr, hazard_threshold=FLOOD_THRESHOLD):
    valid = ~np.isnan(hazard_arr)
    at_risk_mask = valid & (hazard_arr > hazard_threshold)
    safe_mask = valid & (hazard_arr <= hazard_threshold)
    no_data = np.isnan(hazard_arr) | (hazard_arr == 0)
    safe_mask = safe_mask | no_data
    cost_arr = friction_arr.copy()
    cost_arr[np.isnan(cost_arr)] = 1e6
    cost_arr[cost_arr <= 0] = 1e6
    return cost_arr, safe_mask, at_risk_mask


def create_cyclone_cost_surface(friction_arr, cyclone_arr):
    valid = ~np.isnan(cyclone_arr)
    at_risk_mask = valid & (cyclone_arr >= 1)
    safe_mask = valid & (cyclone_arr == 0)
    no_data = np.isnan(cyclone_arr)
    safe_mask = safe_mask | no_data
    cost_arr = friction_arr.copy()
    cost_arr[np.isnan(cost_arr)] = 1e6
    cost_arr[cost_arr <= 0] = 1e6
    return cost_arr, safe_mask, at_risk_mask


def calculate_travel_time_mcp(cost_arr, safe_mask, pixel_size_m):
    safe_indices = np.argwhere(safe_mask)
    if len(safe_indices) == 0:
        return np.full(cost_arr.shape, np.nan)
    cost_scaled = cost_arr * pixel_size_m
    mcp = MCP_Geometric(cost_scaled, fully_connected=True)
    starts = [tuple(idx) for idx in safe_indices]
    if len(starts) > MAX_MCP_SOURCES:
        rng = np.random.default_rng(42)
        indices = rng.choice(len(starts), MAX_MCP_SOURCES, replace=False)
        starts = [starts[i] for i in indices]
    cumulative_cost, _ = mcp.find_costs(starts)
    travel_time = cumulative_cost.astype(np.float32)
    travel_time[travel_time >= 1e9] = np.nan
    return travel_time


def compute_evacuability_csv(context, country_code: str, admin_level: str,
                              rps: list[str] | None = None,
                              flood_threshold: float = None) -> str | None:
    log = context.info if hasattr(context, 'info') else print
    if rps is None:
        rps = []

    country_code = country_code.upper()
    admin_level = admin_level.upper()
    base_path = Path(f"data/{country_code}")
    temp_dir = base_path / "Temporary"
    output_dir = base_path / "Output"
    boundary_path = base_path / f"{country_code}_{admin_level}.geojson"
    id_col = f"{admin_level}_PCODE"
    out_csv = output_dir / f"{country_code}_{admin_level}_evacuability.csv"

    if not boundary_path.exists():
        log(f"[{country_code}] Boundary not found: {boundary_path}")
        return None

    gdf = gpd.read_file(boundary_path)
    df = pd.DataFrame({id_col: gdf[id_col]})
    had_data = False

    # --- Flood evacuability per RP ---
    for rp in rps:
        flood_path = temp_dir / f"{country_code}_flooded_RP{rp}.tif"
        if not flood_path.exists():
            continue

        with rasterio.open(flood_path) as src:
            hazard = src.read(1).astype(np.float32)
            crs = src.crs
            transform = src.transform
            bounds = src.bounds
            shape = hazard.shape
            nodata = src.nodata

        if nodata is not None:
            hazard[hazard == nodata] = np.nan

        friction = fetch_friction_window(
            (bounds.left, bounds.bottom, bounds.right, bounds.top),
            crs, transform, shape,
        )

        pixel_size_m = abs(transform.a) * 111000 if crs.is_geographic else (abs(transform.a) + abs(transform.e)) / 2
        total_pixels = hazard.size
        scale_factor = 1

        if total_pixels > MAX_PIXELS_FOR_MCP:
            scale_by_pixels = np.sqrt(total_pixels / MAX_PIXELS_FOR_MCP)
            scale_by_res = TARGET_RESOLUTION_M / pixel_size_m if pixel_size_m < TARGET_RESOLUTION_M else 1
            scale_factor = max(scale_by_pixels, scale_by_res)
            hazard_ds = downsample_array(hazard, scale_factor, method='mean')
            friction_ds = downsample_array(friction, scale_factor, method='mean')
            pixel_size_ds = pixel_size_m * scale_factor
        else:
            hazard_ds = hazard
            friction_ds = friction
            pixel_size_ds = pixel_size_m

        cost_arr, safe_mask, at_risk_ds = create_cost_surface(friction_ds, hazard_ds, flood_threshold or FLOOD_THRESHOLD)

        if at_risk_ds.sum() == 0:
            df[f"RP{rp}_evac_time_minutes_mean"] = None
            df[f"RP{rp}_evac_time_minutes_max"] = None
            df[f"RP{rp}_evac_time_minutes_median"] = None
            df[f"RP{rp}_pixels_at_risk"] = 0
        else:
            travel_time_ds = calculate_travel_time_mcp(cost_arr, safe_mask, pixel_size_ds)

            if scale_factor > 1:
                travel_time = upsample_array(travel_time_ds, shape)
                _, _, at_risk_mask = create_cost_surface(friction, hazard, flood_threshold or FLOOD_THRESHOLD)
            else:
                travel_time = travel_time_ds
                at_risk_mask = at_risk_ds

            travel_time_at_risk = travel_time.copy()
            travel_time_at_risk[~at_risk_mask] = np.nan
            gdf_tt = gdf.to_crs(crs) if gdf.crs != crs else gdf

            with tempfile.TemporaryDirectory() as tmpdir:
                tt_path = os.path.join(tmpdir, "travel_time.tif")
                with rasterio.open(tt_path, 'w', driver='GTiff',
                    height=travel_time_at_risk.shape[0], width=travel_time_at_risk.shape[1],
                    count=1, dtype=np.float32, crs=crs, transform=transform, nodata=np.nan) as dst:
                    dst.write(travel_time_at_risk, 1)
                tt_stats = zonal_stats(gdf_tt, tt_path, stats=['mean', 'max', 'median', 'count'], nodata=np.nan)

            df[f"RP{rp}_evac_time_minutes_mean"] = [round(s['mean'], 1) if s.get('mean') else None for s in tt_stats]
            df[f"RP{rp}_evac_time_minutes_max"] = [round(s['max'], 1) if s.get('max') else None for s in tt_stats]
            df[f"RP{rp}_evac_time_minutes_median"] = [round(s['median'], 1) if s.get('median') else None for s in tt_stats]
            df[f"RP{rp}_pixels_at_risk"] = [s['count'] if s.get('count') else 0 for s in tt_stats]

        had_data = True

    # --- Cyclone evacuability ---
    cyclone_path = temp_dir / f"{country_code}_cyclone_exposure.tif"
    if cyclone_path.exists():
        with rasterio.open(cyclone_path) as src:
            cyclone = src.read(1).astype(np.float32)
            crs = src.crs
            transform = src.transform
            bounds = src.bounds
            shape = cyclone.shape
            nodata = src.nodata

        if nodata is not None:
            cyclone[cyclone == nodata] = np.nan

        friction = fetch_friction_window(
            (bounds.left, bounds.bottom, bounds.right, bounds.top),
            crs, transform, shape,
        )

        pixel_size_m = abs(transform.a) * 111000 if crs.is_geographic else (abs(transform.a) + abs(transform.e)) / 2
        total_pixels = cyclone.size
        scale_factor = 1

        if total_pixels > MAX_PIXELS_FOR_MCP:
            scale_by_pixels = np.sqrt(total_pixels / MAX_PIXELS_FOR_MCP)
            scale_by_res = TARGET_RESOLUTION_M / pixel_size_m if pixel_size_m < TARGET_RESOLUTION_M else 1
            scale_factor = max(scale_by_pixels, scale_by_res)
            cyclone_ds = downsample_array(cyclone, scale_factor, method='max')
            friction_ds = downsample_array(friction, scale_factor, method='mean')
            pixel_size_ds = pixel_size_m * scale_factor
        else:
            cyclone_ds = cyclone
            friction_ds = friction
            pixel_size_ds = pixel_size_m

        cost_arr, safe_mask, at_risk_ds = create_cyclone_cost_surface(friction_ds, cyclone_ds)

        if at_risk_ds.sum() == 0:
            df["kt34_evac_time_minutes_mean"] = None
            df["kt34_evac_time_minutes_max"] = None
            df["kt34_evac_time_minutes_median"] = None
            df["kt34_pixels_at_risk"] = 0
        else:
            travel_time_ds = calculate_travel_time_mcp(cost_arr, safe_mask, pixel_size_ds)

            if scale_factor > 1:
                travel_time = upsample_array(travel_time_ds, shape)
                _, _, at_risk_mask = create_cyclone_cost_surface(friction, cyclone)
            else:
                travel_time = travel_time_ds
                at_risk_mask = at_risk_ds

            travel_time_at_risk = travel_time.copy()
            travel_time_at_risk[~at_risk_mask] = np.nan
            gdf_tt = gdf.to_crs(crs) if gdf.crs != crs else gdf

            with tempfile.TemporaryDirectory() as tmpdir:
                tt_path = os.path.join(tmpdir, "travel_time.tif")
                with rasterio.open(tt_path, 'w', driver='GTiff',
                    height=travel_time_at_risk.shape[0], width=travel_time_at_risk.shape[1],
                    count=1, dtype=np.float32, crs=crs, transform=transform, nodata=np.nan) as dst:
                    dst.write(travel_time_at_risk, 1)
                tt_stats = zonal_stats(gdf_tt, tt_path, stats=['mean', 'max', 'median', 'count'], nodata=np.nan)

            df["kt34_evac_time_minutes_mean"] = [round(s['mean'], 1) if s.get('mean') else None for s in tt_stats]
            df["kt34_evac_time_minutes_max"] = [round(s['max'], 1) if s.get('max') else None for s in tt_stats]
            df["kt34_evac_time_minutes_median"] = [round(s['median'], 1) if s.get('median') else None for s in tt_stats]
            df["kt34_pixels_at_risk"] = [s['count'] if s.get('count') else 0 for s in tt_stats]

        had_data = True

    if not had_data:
        log(f"[{country_code}] No evacuability data produced")
        return None

    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)
    return str(out_csv)
```
:::

---


