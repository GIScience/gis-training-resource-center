# GAIA Pipeline Documentation

## Overview

The GAIA Pipeline produces a series of thematic files for each country at administrative level 2. Each file captures different aspects of population, infrastructure, and environmental conditions. Below is an overview of the available files:

- [**Access to Services**](#access-to-services) – Population accessibility to key facilities such as education and health centers.  
- [**Facilities**](#facilities) – Availability and distribution of essential service infrastructure.  
- [**Coping Capacity**](#coping-capacity) – Combined indicators derived from Access and Facilities layers to assess local coping capacity.  
- [**Demographics**](#demographics) – Distribution of vulnerable population.  
- [**Rural Population**](#rural-population) – Demographic indicators focused specifically on rural populations.  
- [**Vulnerability**](#vulnerability) – Composite indicators derived from Demographics and Rural Population layers.  
- [**Crop Coverage and Change**](#crop-coverage-and-change) – Extent of agricultural land and observed changes over time.  
- [**Vegetation Index**](#vegetation-index) – NDVI-based assessment of vegetation conditions.  
- [**Flood Exposure**](#flood-exposure) – Exposure of populations and facilities to flood hazards.
---
## Risk Assessment Plugin
The datasets produced by GAIA are fully compatible with the [Risk Assessment QGIS Plugin](https://giscience.github.io/gis-training-resource-center/content/GIS_AA/en_qgis_risk_assessment_plugin.html), enabling seamless integration into spatial risk analyses. They are openly available for multiple countries through [HeiGIT on HDX](https://data.humdata.org/organization/heidelberg-institute-for-geoinformation-technology?sort=metadata_modified+desc), providing ready-to-use geospatial layers for risk assessments.

The **Coping Capacity**, **Vulnerability**, and **Flood Exposure** files can be used directly as input for the Risk Assessment QGIS Plugin when analyzing flood hazards. Only minor adjustments, such as renaming the ID columns, are required for compatibility.

---

## Access to Services
Represents the share of the population with access to key facilities within defined distances or travel times.

### Data Sources
- Accessibility data (isochrones) downloaded from:  
  `https://warm.storage.heigit.org/heigit-hdx-public/access/{country_code}/{country_code}_{category}_access.gpkg`  
  Categories: `education`, `hospitals`, `primary_healthcare`.
- Population data: WorldPop raster data (vulnerable populations) via `Demographics`.

### Processing Steps
1. **Download accessibility isochrones** in GPKG format for each category.
2. **Load administrative boundaries** at admin level 2 from local GeoJSON files.
3. **Fetch WorldPop raster datasets** and sum relevant indicators to produce a vulnerable population raster.
4. For each category and cutoff:
   - Select isochrone polygons for the cutoff value.
   - Intersect polygons with administrative boundaries.
   - Use `rasterstats.zonal_stats` to compute total population within the isochrone area.
5. Save results as a CSV containing population counts per administrative unit.

### Outputs
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

## Facilities
Represents the availability and spatial distribution of essential service infrastructure such as schools, hospitals, and primary healthcare centers.

### Data Sources
- **OpenStreetMap (OSM)** data, accessed through either:
  - **Overpass API**, for direct querying of recent OSM feature data; or  
  - **Ohsome API**, for more stable and filtered access to OSM geometries.
- **Administrative boundaries** (GeoJSON): Used to spatially aggregate features at administrative level 2.

### Processing Steps
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

### Outputs
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

## Coping Capacity
Represents the ability of a population to access essential services and benefit from available infrastructure.  
This layer combines `Access to Services` and `Facilities` indicators to assess local capacity to cope with shocks or disruptions.

### Data Sources
- **Access to Services CSVs:** Derived from population accessibility analysis (see `Access to Services` chapter).  
- **Facilities CSVs:** Derived from OpenStreetMap facility data (see `Facilities` chapter).  
- Both inputs are aggregated at the same administrative level (e.g., ADM2).

### Processing Steps
1. **Input CSVs:**  
   - One `Access to Services` CSV and one `Facilities` CSV are provided per administrative level.
   - Each CSV includes an identifier column such as `ADM0_PCODE`, `ADM1_PCODE`, or `ADM2_PCODE`.
2. **Column Detection:**  
   - The script automatically detects the administrative identifier column by searching for any column ending with `_PCODE`.
3. **Merge Operation:**  
   - The two datasets are merged on the identified `*_PCODE` column using a left join.
   - This ensures all access indicators are retained even if some administrative areas lack facility data.
4. **Output Generation:**  
   - The merged dataset is saved as `{country_code}_{admin_level}_coping.csv` under `Output/`.
   - One output is produced per administrative level present in the input data.

### Outputs
- CSV file: `{country_code}_{admin_level}_coping.csv`
  - Columns:  
    - `{admin_level}_PCODE`
    - All accessibility indicator columns (e.g., `access_pop_education_5km`, `access_pop_hospitals_1h`)
    - All facility count columns (e.g., `education_count`, `hospitals_count`, `primary_healthcare_count`)
  - CRS: WGS84 (`EPSG:4326`)
  - Units: counts and population values aggregated per administrative unit

:::{dropdown} Python Script (Coping Capacity)
```python
import os
import pandas as pd
from pathlib import Path
from typing import List

def coping_asset(context, access_asset: List[str], facilities_asset: List[str]) -> list[str]:
    """
    Combine accessibility and facilities CSVs into a single coping dataset.
    Joins on the ADM*_PCODE column per admin level.
    Produces one coping CSV per admin level in Output/.
    """
    country_code = context.partition_key.upper()
    outputs = []

    for access_csv, facilities_csv in zip(access_asset, facilities_asset):
        if not os.path.exists(access_csv) or not os.path.exists(facilities_csv):
            context.log.warning(
                f"Skipping merge for {country_code}: missing files {access_csv}, {facilities_csv}"
            )
            continue

        try:
            df_access = pd.read_csv(access_csv)
            df_facilities = pd.read_csv(facilities_csv)

            # detect admin code column automatically (ADM0_PCODE, ADM1_PCODE, etc.)
            id_col = [c for c in df_access.columns if c.endswith("_PCODE")]
            if not id_col:
                context.log.warning(f"Skipping {access_csv}: no *_PCODE column found")
                continue
            id_col = id_col[0]

            merged = pd.merge(df_access, df_facilities, on=id_col, how="left")

            admin_level = id_col.split("_")[0]  # e.g., ADM2
            output_dir = Path("data") / country_code / "Output"
            output_dir.mkdir(parents=True, exist_ok=True)

            output_path = output_dir / f"{country_code}_{admin_level}_coping.csv"
            merged.to_csv(output_path, index=False)
            outputs.append(str(output_path))

            context.log.info(f"[{country_code}] Wrote coping CSV: {output_path}")

        except Exception as e:
            context.log.warning(f"Failed to merge {access_csv} and {facilities_csv}: {e}")

    if not outputs:
        context.log.warning(f"No coping outputs created for {country_code}")
    return outputs
```
:::

---
## Demographics
Provides population distribution indicators based on **age** and **sex**.  
This layer is derived from the [**WorldPop**](https://www.worldpop.org/) global population dataset and quantifies vulnerable population groups across administrative boundaries.

### Data Sources
- **WorldPop Age-Sex Population Rasters:**  
  Downloaded from the [WorldPop Global Constrained Population dataset](https://www.worldpop.org/geodata/listing?id=77) (`Global_2000_2020_Constrained`).  
- **Administrative boundaries** (GeoJSON): Used to spatially aggregate features at administrative level 2.


### Indicators
Each demographic indicator represents the **sum of population counts** matching specified age and sex ranges:

| Indicator       | Description                                | Ages (years)       | Sexes |
|-----------------|--------------------------------------------|--------------------|-------|
| `female_pop`    | Total female population                    | 0–80+              | f     |
| `children_u5`   | Total children under 5                     | 0–4                | f, m  |
| `female_u5`     | Female children under 5                    | 0–4                | f     |
| `elderly`       | Population aged 65 and above               | 65+                | f, m  |
| `pop_u15`       | Population under 15                        | 0–14               | f, m  |
| `female_u15`    | Female population under 15                 | 0–14               | f     |

### Processing Steps
1. **Download Required WorldPop Tiles**  
   - For each indicator, the script identifies which age/sex rasters are needed (e.g., `m_0`, `f_1`, etc.).  
   - Tiles are downloaded from `https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020_Constrained/2020/{ISO3}/`.
2. **Merge and Sum Rasters**  
   - The corresponding age/sex tiles are summed into one raster per indicator.  
   - Outputs are saved in `data/{country}/Temporary/`.
3. **Aggregate by Administrative Units**  
   - Using the administrative boundary GeoJSON (e.g., `ADM2`), zonal statistics are computed for each indicator.  
   - Population counts are summed per administrative area.
4. **Output**  
   - A single CSV per country: `{country_code}_{admin_level}_demographics.csv`
   - Saved to `data/{country}/Output/`

### Outputs
- **File:** `{country_code}_{admin_level}_demographics.csv`  
- **Columns:**
  - `{admin_level}_PCODE`
  - `female_pop`
  - `children_u5`
  - `female_u5`
  - `elderly`
  - `pop_u15`
  - `female_u15`
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** Population counts (integer, aggregated per administrative unit)

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

# Define indicators directly
INDICATORS = {
    "female_pop": {"ages": [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80], "sexes": ["f"]},
    "children_u5": {"ages": [0, 1], "sexes": ["f", "m"]},
    "female_u5": {"ages": [0, 1], "sexes": ["f"]},
    "elderly": {"ages": [65, 70, 75, 80], "sexes": ["f", "m"]},
    "pop_u15": {"ages": [0, 1, 5, 10], "sexes": ["f", "m"]},
    "female_u15": {"ages": [0, 1, 5, 10], "sexes": ["f"]},
}

BASE_URL = "https://data.worldpop.org/GIS"
POP_TIMEFRAME = "Global_2000_2020_Constrained"
YEAR = "2020"


def download_url(url, dest_path):
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(dest_path, "wb") as fp:
        for chunk in resp.iter_content(1024 * 1024):
            fp.write(chunk)


def merge_and_sum_rasters(raster_paths: List[str], out_path: str, context_log):
    """
    Open each path in `raster_paths`, read band 1 into memory, sum them,
    and write a single‐band float32 GeoTIFF to `out_path`.
    """
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
    """
    Download WorldPop rasters for a country and aggregate into indicator rasters.
    Produces 6 GeoTIFFs: one per indicator (no total population).
    """
    if context_log is None:
        logging.basicConfig(level=logging.INFO)
        context_log = logging.getLogger("worldpop")

    country = country.upper()

    if not worldpop_code:
        worldpop_code = country
        worldpop_code_low = country.lower()
    else:
        worldpop_code_low = worldpop_code.lower()

    # Force output directory to Temporary
    out_dir = os.path.join("data", country, "Temporary")
    os.makedirs(out_dir, exist_ok=True)

    # Pre-check: if all 6 indicator rasters already exist, skip
    expected_outputs = [
        os.path.join(out_dir, f"{country}_pop_{ind_name}_{YEAR}_constrained.tif")
        for ind_name in INDICATORS.keys()
    ]
    if all(os.path.exists(path) for path in expected_outputs):
        context_log.info(f"[{country}] → all {len(expected_outputs)} WorldPop indicators already exist, skipping download.")
        return expected_outputs
    
    out_dir_raw = os.path.join(out_dir, "worldpop_raw")
    os.makedirs(out_dir_raw, exist_ok=True)

    downloaded = []

    # 1) Download needed age/sex rasters
    needed_bins = set()
    for ind in INDICATORS.values():
        for sex in ind["sexes"]:
            for age in ind["ages"]:
                needed_bins.add((sex, age))

    for sex, age in needed_bins:
        fname = f"{worldpop_code_low}_{sex}_{age}_{YEAR}_constrained.tif"
        url = f"{BASE_URL}/AgeSex_structures/{POP_TIMEFRAME}/{YEAR}/{worldpop_code}/{fname}"
        dest = os.path.join(out_dir_raw, f"{country}_{sex}_{age}_{YEAR}_constrained.tif")
        if not os.path.exists(dest):
            context_log.info(f"[{country}] → downloading {sex}_{age}")
            try:
                download_url(url, dest)
            except Exception as e:
                context_log.info(f"[ERROR] failed to download {url}: {e}")
                sys.exit(1)
        else:
            context_log.info(f"[{country}] → skipping existing {fname}")
        downloaded.append(dest)

    # 2) Aggregate indicators
    processed = []
    for ind_name, ind in INDICATORS.items():
        filtered_paths = [
            os.path.join(out_dir_raw, f"{country}_{sex}_{age}_{YEAR}_constrained.tif")
            for sex in ind["sexes"]
            for age in ind["ages"]
        ]
        merged_out = os.path.join(out_dir, f"{country}_pop_{ind_name}_{YEAR}_constrained.tif")
        if not os.path.exists(merged_out):
            context_log.info(f"[{country}] → processing indicator {ind_name}")
            try:
                merge_and_sum_rasters(filtered_paths, merged_out, context_log)
            except Exception as e:
                context_log.info(f"[ERROR] failed to process {ind_name}: {e}")
                sys.exit(1)
        else:
            context_log.info(f"[{country}] → skipping existing {ind_name}")
        processed.append(merged_out)

    # 3) Delete raw folder
    if os.path.exists(out_dir_raw):
        shutil.rmtree(out_dir_raw)
        context_log.info(f"[{country}] → deleted raw folder: {out_dir_raw}")

    context_log.info(f"\n✔ ∙ {len(processed)} indicators saved under {out_dir}")
    return processed


def aggregate_worldpop_to_csv(country_code: str, admin_level="ADM2", context_log=None) -> str:
    """
    Download WorldPop indicators for a country and save CSV.
    """
    temp_dir = os.path.join("data", country_code, "Temporary")
    os.makedirs(temp_dir, exist_ok=True)

    output_dir = os.path.join("data", country_code, "Output")
    os.makedirs(output_dir, exist_ok=True)
    if context_log is None:
        logging.basicConfig(level=logging.INFO)
        context_log = logging.getLogger("worldpop")

    # 1) Fetch indicators (6 GeoTIFFs) into data/{country}/Temporary
    tifs = fetch_worldpop(country=country_code, context_log=context_log)

    # 2) Load ADM polygons
    adm_path = f"data/{country_code}/{country_code}_{admin_level}.geojson"
    gdf = gpd.read_file(adm_path)

    expected_column = f"{admin_level}_PCODE"
    if expected_column not in gdf.columns:
        raise ValueError(
            f"GeoJSON must contain column '{expected_column}' "
            f"(found: {gdf.columns.tolist()})"
        )

    # 3) Map indicator names to files
    indicators = ["female_pop","children_u5","female_u5","elderly","pop_u15","female_u15"]
    tif_map = dict(zip(indicators, tifs))

    results = pd.DataFrame()
    results[f"{admin_level}_PCODE"] = gdf[f"{admin_level}_PCODE"]

    # 4) Compute zonal sums
    for ind, path in tif_map.items():
        stats = zonal_stats(gdf, path, stats="sum", nodata=0)
        results[ind] = [s["sum"] for s in stats]

    # Round all numeric columns to 0 decimals
    numeric_cols = results.columns.drop(f"{admin_level}_PCODE")
    results[numeric_cols] = results[numeric_cols].round(0).astype(int)

    # 5) Save CSV
    out_dir = os.path.join("data", country_code, "Output")
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, f"{country_code}_{admin_level}_demographics.csv")
    results.to_csv(csv_path, index=False)

    return csv_path
```
:::

---
## Rural Population
Represents the proportion and distribution of people living in **rural areas** within each administrative unit.  
This layer combines **WorldPop population rasters** with **Global Human Settlement Layer (GHS-SMOD)** data to estimate rural populations for each demographic group.

### Data Sources
- **WorldPop Population Rasters:**  
  Derived from the [WorldPop Age-Sex structured datasets](https://www.worldpop.org/geodata/listing?id=77).  
  Used to calculate population counts for various demographic indicators (see the `Demographics` chapter).  
- **GHS-SMOD (Settlement Model) Raster:**  
  Downloaded from the [JRC GHSL repository](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/) for the year 2030 projection.  
  Used to classify grid cells as **urban** or **rural** based on settlement patterns.
- **Administrative Boundaries:**  
  GeoJSON boundary files (e.g., ADM2) define the spatial units used for population aggregation.

### Processing Steps
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

### Outputs
- CSV file: `{country_code}_{admin_level}_rural_population.csv`
  - Columns:
    - `{admin_level}_PCODE`
    - `{indicator}_rural` (e.g., `female_pop_rural`, `children_u5_rural`)
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
from scripts.fetch_worldpop import fetch_worldpop

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
    """Download SMOD ZIP, unzip, return path to TIF."""
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
    """
    Compute rural population counts by admin unit for each indicator.
    Generates smod_reclass.tif if missing. Skips if output CSV already exists.
    Adds percentage columns (_rural_perc) for each indicator.
    """
    country_code = country_code.upper()
    work_dir = Path(f"{work_dir}/Temporary")
    temp_dir = Path(f"{work_dir}/data/{country_code}/Temporary")
    output_dir = Path(output_dir)
    reclass_tif = work_dir / "smod_reclass.tif"
    out_csv = output_dir / f"{country_code}_{admin_level}_rural_population.csv"

    # --- skip if CSV exists ---
    if out_csv.exists():
        context.info(f"CSV already exists, skipping: {out_csv}")
        return str(out_csv)

    zip_path = None
    unzip_dir = None

    try:
        # --- ensure smod_reclass.tif exists ---
        if not reclass_tif.exists():
            context.info("smod_reclass.tif missing — will generate it")
            zip_path, unzip_dir, smod_tif = download_and_unzip_smod(work_dir, context)
            reclassify_raster(smod_tif, reclass_tif, RECLASS_MAP, context)
        else:
            context.info("Using existing smod_reclass.tif")

        # Ensure WorldPop files exist
        context.info(f"Ensuring demographic rasters exist in {temp_dir}...")
        indicator_tifs = fetch_worldpop(country_code)
        indicators = ["female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15"]
        tif_map = dict(zip(indicators, indicator_tifs))

        # --- load SMOD raster ---
        smod = rioxarray.open_rasterio(reclass_tif, masked=True).squeeze()

        rural_df = pd.DataFrame({f"{admin_level}_PCODE": gdf[f"{admin_level}_PCODE"]})

        # Store total population sums
        total_pop_counts = {}

        for label in indicators:
            pop_raster_path = tif_map[label]
            pop_raster = rioxarray.open_rasterio(pop_raster_path, masked=True).squeeze()

            # Align SMOD raster to population raster
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

            # Rural population sums per admin unit
            stats = zonal_stats(gdf, tmp_rural, stats="sum", nodata=0)
            rural_df[f"{label}_rural"] = [s["sum"] if s["sum"] is not None else 0 for s in stats]

            # Total population sums per admin unit
            total_stats = zonal_stats(gdf, pop_raster_path, stats="sum", nodata=0)
            total_pop_counts[label] = [s["sum"] if s["sum"] is not None else 0 for s in total_stats]

            context.info(f"Processed rural population for {label}")

        # --- calculate one overall rural percentage column ---
        # Use total population (e.g. pop_u15 as proxy, or sum of all groups)
        total_pop = pd.Series(total_pop_counts["female_pop"]).replace({0: np.nan})
        rural_df["rural_pop_perc"] = (
            rural_df["female_pop_rural"] / total_pop * 100
        ).fillna(0).round(2)

        # --- finalize ---
        count_cols = [c for c in rural_df.columns if c.endswith("_rural")]
        perc_cols = [c for c in rural_df.columns if c.endswith("_rural_perc")]

        # Counts → integers
        rural_df[count_cols] = rural_df[count_cols].fillna(0).round(0).astype(int)

        # Percentages → keep 2 decimals
        rural_df[perc_cols] = rural_df[perc_cols].fillna(0).round(2)

        output_dir.mkdir(parents=True, exist_ok=True)
        rural_df.to_csv(out_csv, index=False)
        context.info(f"Rural population CSV written to {out_csv}")

    finally:
        # cleanup
        if zip_path and zip_path.exists():
            zip_path.unlink()
            context.info(f"Deleted {zip_path}")
        if unzip_dir and unzip_dir.exists():
            shutil.rmtree(unzip_dir)
            context.info(f"Deleted {unzip_dir}")
        
                # cleanup tmp_rural rasters
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
## Vulnerability
Represents the sensitivity of a population to external shocks based on demographic composition and settlement type.  
This layer combines **Demographics** and **Rural Population** indicators to highlight population groups more likely to experience heightened vulnerability in rural or hard-to-reach regions.

### Data Sources
- **Demographics CSVs:** Derived from [WorldPop](https://www.worldpop.org/) population datasets, disaggregated by age and sex (see `Demographics` chapter).  
- **Rural Population CSVs:** Derived from settlement layer analysis separating rural and urban populations (see `Rural Population` chapter).  
- Both datasets are aggregated to the same administrative level (e.g., ADM2).

### Processing Steps
1. **Input CSVs:**  
   - One `Demographics` CSV and one `Rural Population` CSV are provided per administrative level.  
   - Each file contains an identifier column such as `ADM0_PCODE`, `ADM1_PCODE`, or `ADM2_PCODE`.

2. **Column Detection:**  
   - The script automatically detects the administrative identifier column by finding any column ending with `_PCODE`.

3. **Merge Operation:**  
   - The two datasets are merged on the identified `*_PCODE` column using a **left join**.  
   - This ensures demographic indicators are retained even when some administrative areas lack rural population data.

4. **Output Generation:**  
   - The merged dataset is exported as `{country_code}_{admin_level}_vulnerability.csv` to the `Output/` directory.  
   - One file is created per administrative level present in the input data.

### Outputs
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
## Crop Coverage and Change
Quantifies the extent and temporal change of cropland areas within administrative boundaries.  
This layer assesses both **total cropland coverage** and **change in cropland area** between two years using the **Google Dynamic World (V1)** dataset derived from Sentinel-2 imagery.

### Data Sources
- **Dynamic World V1** (`GOOGLE/DYNAMICWORLD/V1`):  
  Global, near real-time land cover dataset from Google Earth Engine, with 10 m spatial resolution and daily temporal frequency.  
- **Administrative Boundaries** (GeoJSON):  
  Used to aggregate cropland extent within each administrative area (e.g., ADM2).  
- **Configuration File** (`configs/assets_config.yaml`):  
  Defines two reference years under `crops_asset: years: [year1, year2]` for comparison.

### Indicators
| Indicator | Description | Units |
|------------|-------------|--------|
| `crops_{year1}_pct` | Percentage of total area classified as crops in the first year | % |
| `crops_{year2}_pct` | Percentage of total area classified as crops in the second year | % |
| `crops_diff_km2` | Absolute change in cropland area between the two years | km² |
| `crops_diff_pctpts` | Percentage point difference in cropland coverage | % points |
| `crops_change_rel_pct` | Relative percentage change compared to the baseline year | % |

### Processing Steps
1. **Configuration Parsing:**  
   - The script reads `assets_config.yaml` and extracts the two comparison years (e.g., 2018 and 2022).  
   - If the configuration does not define two valid years, an error is raised.

2. **Input Geometry:**  
   - The administrative boundary file `data/{country_code}/{country_code}_{admin_level}.geojson` is loaded using `GeoPandas`.

3. **Earth Engine Setup:**  
   - The script initializes Google Earth Engine (`ee.Initialize(project="aa-automatization")`).  
   - The `GOOGLE/DYNAMICWORLD/V1` collection is used to generate yearly **mode composites** for each year and boundary polygon.

4. **Cropland Extraction:**  
   - Each composite image is classified into Dynamic World labels.  
   - Label `4` corresponds to **cropland**.  
   - For each administrative unit, the mean cropland fraction is computed (as % of total area).

5. **Change Calculation:**  
   - The following statistics are derived per polygon:
     - Percentage of cropland per year (`crops_{year1}_pct`, `crops_{year2}_pct`)
     - Absolute area change in km² (`crops_diff_km2`)
     - Difference in percentage points (`crops_diff_pctpts`)
     - Relative change compared to the first year (`crops_change_rel_pct`)

6. **Chunked Processing:**  
   - To handle large datasets, polygons are processed in chunks (default: 20 features at a time).  
   - Each chunk’s results are written to a temporary CSV, then appended to the final output.

7. **Output Generation:**  
   - The combined dataset is saved as `{country_code}_{admin_level}_crops.csv` under `data/{country_code}/Output/`.

### Outputs
- **File:** `{country_code}_{admin_level}_crops.csv`  
- **Columns:**
  - `{admin_level}_PCODE`
  - `crops_{year1}_pct`
  - `crops_{year2}_pct`
  - `crops_diff_km2`
  - `crops_diff_pctpts`
  - `crops_change_rel_pct`
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** Percentages (%) and area (km²)

:::{dropdown} Python Script (Crop Coverage and Change)
```python
import os
import geopandas as gpd
import pandas as pd
import geemap
import ee
import yaml
import argparse

def load_years_from_config(config_path="configs/assets_config.yaml"):
    """Load years from crops_asset in assets_config.yaml"""
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    years = cfg.get("crops_asset", {}).get("years", [])
    if not years or len(years) != 2:
        raise ValueError("assets_config.yaml must define crops_asset: years: [year1, year2]")
    return years[0], years[1]


def process_crops_for_admin(country_code: str, admin_level: str, config_path="configs/assets_config.yaml") -> str:
    """Run crop coverage calculation for a given country/admin level and return output CSV path."""

    # Initialize Earth Engine
    ee.Initialize(project="aa-automatization")

    year_prev, year_curr = load_years_from_config(config_path)

    gdf = gpd.read_file(f"data/{country_code}/{country_code}_{admin_level}.geojson")

    chunk_size = 20
    start_idx = 0
    
    # Ensure Output folder exists
    os.makedirs(f"data/{country_code}/Output", exist_ok=True)
    output_csv = f"data/{country_code}/Output/{country_code}_{admin_level}_crops.csv"

    if os.path.exists(output_csv):
        os.remove(output_csv)

    col_order = [
        f"{admin_level.upper()}_PCODE",
        f"crops_{year_prev}_pct",
        f"crops_{year_curr}_pct",
        "crops_diff_km2",
        "crops_diff_pctpts",
        "crops_change_rel_pct",
    ]

    dw = ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")

    def yearly_composite(y, geom):
        coll = (
            dw.filterDate(f"{y}-01-01", f"{y}-12-31")
            .filterBounds(geom)
            .select("label")
        )
        return coll.reduce(ee.Reducer.mode())

    while start_idx < len(gdf):
        end_idx = start_idx + chunk_size
        gdf_chunk = gdf.iloc[start_idx:end_idx]

        try:
            fc = geemap.geopandas_to_ee(gdf_chunk)

            def add_crops_stats(feature):
                geom = feature.geometry()
                comp_prev = yearly_composite(year_prev, geom)
                comp_curr = yearly_composite(year_curr, geom)

                polygon_area_km2 = ee.Number(geom.area()).divide(1e6)

                crop_prev_raw = comp_prev.eq(4).rename("crops").reduceRegion(
                    reducer=ee.Reducer.mean(),
                    geometry=geom,
                    scale=10,
                    bestEffort=True,
                ).get("crops")

                crop_curr_raw = comp_curr.eq(4).rename("crops").reduceRegion(
                    reducer=ee.Reducer.mean(),
                    geometry=geom,
                    scale=10,
                    bestEffort=True,
                ).get("crops")

                crop_prev_perc = ee.Number(ee.Algorithms.If(crop_prev_raw, crop_prev_raw, 0)).multiply(100)
                crop_curr_perc = ee.Number(ee.Algorithms.If(crop_curr_raw, crop_curr_raw, 0)).multiply(100)

                crops_perc_point_dif = crop_curr_perc.subtract(crop_prev_perc)
                crops_abs_dif_km2 = crops_perc_point_dif.multiply(polygon_area_km2).divide(100)

                crops_rel_change_perc = ee.Algorithms.If(
                    crop_prev_perc.neq(0),
                    crops_perc_point_dif.divide(crop_prev_perc).multiply(100),
                    None,
                )

                return feature.set({
                    f"crops_{year_prev}_pct": crop_prev_perc,
                    f"crops_{year_curr}_pct": crop_curr_perc,
                    "crops_diff_km2": crops_abs_dif_km2,
                    "crops_diff_pctpts": crops_perc_point_dif,
                    "crops_change_rel_pct": crops_rel_change_perc,
                })

            fc_with_stats = fc.map(add_crops_stats)
            fc_filtered = fc_with_stats.select(
                propertySelectors=col_order, retainGeometry=False
            )

            temp_csv = f"data/{country_code}/{country_code}_crops_{admin_level}_temp_chunk.csv"
            geemap.ee_to_csv(fc_filtered, filename=temp_csv)

            df_chunk = pd.read_csv(temp_csv)
            df_chunk = df_chunk[[c for c in col_order if c in df_chunk.columns]]
            df_chunk[col_order[1:]] = df_chunk[col_order[1:]].round(2)

            if start_idx == 0 and not os.path.exists(output_csv):
                df_chunk.to_csv(output_csv, index=False)
            else:
                df_chunk.to_csv(output_csv, mode="a", header=False, index=False)

            os.remove(temp_csv)
            start_idx = end_idx

        except Exception:
            start_idx = end_idx

    return output_csv
```
:::

---
## Vegetation Index
Evaluates vegetation health and density using the **Normalized Difference Vegetation Index (NDVI)** derived from **Landsat** composites. NDVI values range from -1 to +1, where higher values indicate denser and healthier vegetation, while lower values reflect sparse or stressed vegetation, bare soil, or urban surfaces. 

This layer provides summary statistics (mean, median, quartiles) and surface extent of high, medium, and low NDVI zones per administrative boundary.

### Data Sources
- **Landsat NDVI Composite** (`LANDSAT/COMPOSITES/C02/T1_L2_8DAY_NDVI`):  
  8-day composite product containing NDVI values at 30 m resolution.  
- **Administrative Boundaries** (GeoJSON):  
  Used for spatial aggregation at ADM levels (e.g., ADM2).  
- **Configuration File** (`configs/assets_config.yaml`):  
  Defines the target year under `ndvi_asset: year: [YYYY]`.

### Indicators
| Indicator | Description | Units |
|------------|-------------|--------|
| `NDVI_mean` | Mean NDVI value across the administrative unit | NDVI (unitless) |
| `NDVI_median` | Median NDVI value | NDVI (unitless) |
| `NDVI_p25` | 25th percentile NDVI | NDVI (unitless) |
| `NDVI_p75` | 75th percentile NDVI | NDVI (unitless) |
| `NDVI_high_sqkm` | Area with NDVI ≥ 0.6 | km² |
| `NDVI_medium_sqkm` | Area with 0.1 ≤ NDVI < 0.6 | km² |
| `NDVI_low_sqkm` | Area with NDVI < 0.1 | km² |

### NDVI Thresholds
| Category | NDVI Range | Interpretation |
|-----------|-------------|----------------|
| **High NDVI** | ≥ 0.6 | Dense vegetation (forests, crops, green cover) |
| **Medium NDVI** | 0.1 – 0.6 | Moderate vegetation (grasslands, shrubs, mixed use) |
| **Low NDVI** | < 0.1 | Bare soil, urban areas, or degraded vegetation |

### Processing Steps
1. **Configuration Loading**  
   - Extracts `year` from `assets_config.yaml` (`ndvi_asset: year: [YYYY]`).  
   - The script ensures exactly one valid year is defined.

2. **Input Geometry**  
   - Loads administrative boundaries (`data/{country_code}/{country_code}_{admin_level}.geojson`) using GeoPandas.

3. **Earth Engine Initialization**  
   - Connects to Google Earth Engine under the project `aa-automatization`.

4. **Landsat NDVI Aggregation**  
   - Loads Landsat NDVI composites for the specified year.  
   - Calculates the **median NDVI** across the year to reduce noise from clouds and seasonal variation.

5. **NDVI Classification**  
   - Creates three NDVI masks:  
     - `High`: NDVI ≥ 0.6  
     - `Medium`: 0.1 ≤ NDVI < 0.6  
     - `Low`: NDVI < 0.1  
   - Each mask is used to compute the corresponding surface area in square kilometers.

6. **Statistical Summary per Polygon**  
   - Calculates the following metrics using `ee.Reducer`:  
     - Mean, Median, 25th and 75th Percentile NDVI  
     - Area (km²) for each NDVI category  
   - Areas are calculated from pixel counts (`count × 900 / 1,000,000`).

7. **Chunked Processing**  
   - Polygons are processed in chunks (default: 20).  
   - Reduces API payload errors when handling large datasets.  
   - If payloads exceed limits, chunk size automatically decreases.

8. **Output Generation**  
   - Each chunk’s results are exported to temporary CSVs and appended to  
     `data/{country_code}/Output/{country_code}_{admin_level}_ndvi.csv`.  
   - Final columns are reordered and rounded to 2 decimals for clarity.

### Outputs
- **File:** `{country_code}_{admin_level}_ndvi.csv`  
- **Columns:**
  - `{admin_level}_PCODE`
  - `NDVI_mean`
  - `NDVI_median`
  - `NDVI_p25`
  - `NDVI_p75`
  - `NDVI_high_sqkm`
  - `NDVI_medium_sqkm`
  - `NDVI_low_sqkm`
- **CRS:** WGS84 (`EPSG:4326`)  
- **Units:** NDVI (unitless), Area (km²)

:::{dropdown} Python Script (Vegetation Index)
```python
import geopandas as gpd
import geemap
import ee
import pandas as pd
import os
import yaml
import argparse

def load_year_from_config(config_path="configs/assets_config.yaml"):
    """Load year from ndvi_asset in assets_config.yaml"""
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    year = cfg.get("ndvi_asset", {}).get("year", [])
    if not year or len(year) != 1:
        raise ValueError("assets_config.yaml must define ndvi_asset: year: [year]")
    return year[0]

def process_ndvi_for_admin(country_code: str, admin_level: str, config_path="configs/assets_config.yaml") -> str:
    """Run NDVI calculation for a given country/admin level and return output CSV path."""
    # Initialize Earth Engine
    ee.Initialize(project='aa-automatization')

    gdf = gpd.read_file(f"data/{country_code}/{country_code}_{admin_level}.geojson")
    chunk_size = 20
    start_idx = 0
    year = load_year_from_config(config_path)

    os.makedirs(f"data/{country_code}/Output", exist_ok=True)
    output_csv = f"data/{country_code}/Output/{country_code}_{admin_level}_ndvi.csv"

    if os.path.exists(output_csv):
        os.remove(output_csv)

    col_order = [
        f"{admin_level.upper()}_PCODE",
        "NDVI_mean", "NDVI_median", "NDVI_p25", "NDVI_p75",
        "NDVI_high_sqkm", "NDVI_medium_sqkm", "NDVI_low_sqkm"
    ]

    while start_idx < len(gdf):
        end_idx = start_idx + chunk_size
        gdf_chunk = gdf.iloc[start_idx:end_idx]

        try:
            fc = geemap.geopandas_to_ee(gdf_chunk)

            landsat = (ee.ImageCollection("LANDSAT/COMPOSITES/C02/T1_L2_8DAY_NDVI")
                       .filterDate(f"{year}-01-01", f"{year}-12-31")
                       .filterBounds(fc))

            ndvi_image = landsat.select("NDVI").median()

            high_ndvi_mask = ndvi_image.updateMask(ndvi_image.gte(0.6))
            medium_ndvi_mask = ndvi_image.updateMask(ndvi_image.gte(0.1).And(ndvi_image.lt(0.6)))
            low_ndvi_mask = ndvi_image.updateMask(ndvi_image.lt(0.1))

            def add_stats(feature):
                stats = ndvi_image.reduceRegion(
                    reducer=ee.Reducer.mean()
                            .combine(ee.Reducer.median(), "", True)
                            .combine(ee.Reducer.percentile([25, 75]), "", True),
                    geometry=feature.geometry(),
                    scale=30,
                    bestEffort=True
                )

                high_count = high_ndvi_mask.reduceRegion(
                    reducer=ee.Reducer.count(),
                    geometry=feature.geometry(),
                    scale=30,
                    bestEffort=True
                )
                medium_count = medium_ndvi_mask.reduceRegion(
                    reducer=ee.Reducer.count(),
                    geometry=feature.geometry(),
                    scale=30,
                    bestEffort=True
                )
                low_count = low_ndvi_mask.reduceRegion(
                    reducer=ee.Reducer.count(),
                    geometry=feature.geometry(),
                    scale=30,
                    bestEffort=True
                )

                high_count = ee.Dictionary(high_count).map(lambda k, v: ee.Number(v).multiply(900).divide(1_000_000))
                medium_count = ee.Dictionary(medium_count).map(lambda k, v: ee.Number(v).multiply(900).divide(1_000_000))
                low_count = ee.Dictionary(low_count).map(lambda k, v: ee.Number(v).multiply(900).divide(1_000_000))

                all_stats = stats.combine(high_count).combine(medium_count).combine(low_count)
                return feature.set(all_stats)

            fc_with_stats = fc.map(add_stats)
            fc_filtered = fc_with_stats.select(**{
                'propertySelectors': col_order,
                'retainGeometry': False
            })

            temp_csv = f"data/{country_code}/{country_code}_ndvi_{admin_level}_temp_chunk.csv"
            geemap.ee_to_csv(fc_filtered, filename=temp_csv)

            df_chunk = pd.read_csv(temp_csv)
            df_chunk = df_chunk[[c for c in col_order if c in df_chunk.columns]]

            round_cols = ["NDVI_mean", "NDVI_median", "NDVI_p25", "NDVI_p75"]
            df_chunk[round_cols] = df_chunk[round_cols].round(2)

            if start_idx == 0 and not os.path.exists(output_csv):
                df_chunk.to_csv(output_csv, index=False)
            else:
                df_chunk.to_csv(output_csv, mode='a', header=False, index=False)

            os.remove(temp_csv)
            print(f"Processed chunk {start_idx}-{end_idx} (size {chunk_size})")
            start_idx = end_idx

        except ee.EEException as e:
            msg = str(e)
            if "Request payload size exceeds the limit" in msg:
                if chunk_size > 1:
                    chunk_size = max(1, chunk_size // 2)
                    print(f"Payload too large. Reducing chunk size to {chunk_size} and retrying index {start_idx}...")
                else:
                    print(f"Chunk size 1 still too large. Skipping index {start_idx}.")
                    start_idx += 1
            else:
                print(f"EEException: {e}. Skipping chunk.")
                start_idx = end_idx
        except FileNotFoundError:
            print(f"Temp CSV not found. Retrying index {start_idx} with smaller chunk...")
            if chunk_size > 1:
                chunk_size = max(1, chunk_size // 2)
            else:
                start_idx += 1
        except Exception as e:
            print(f"Unexpected error: {e}. Skipping chunk {start_idx}-{end_idx}.")
            start_idx = end_idx

    return output_csv
```
:::

---
## Flood Exposure
Estimates population and facility exposure to flooding using **GLOFAS flood hazard rasters** and **WorldPop demographic layers**. Flooded areas are identified by a configurable **flood threshold**, and exposure metrics are aggregated per administrative boundary.

This layer provides indicators for the number of people affected per demographic group and the percentage/count of critical facilities (education, hospitals, primary healthcare) impacted by flood events of different return periods (RPs).

### Data Sources
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

### Indicators
| Indicator | Description | Units |
|-----------|-------------|-------|
| `RP{rp}_female_pop_{thresh}` | Number of females affected by flood depth ≥ threshold | people |
| `RP{rp}_children_u5_{thresh}` | Number of children under 5 affected | people |
| `RP{rp}_female_u5_{thresh}` | Number of female children under 5 affected | people |
| `RP{rp}_elderly_{thresh}` | Number of elderly (>65) affected | people |
| `RP{rp}_pop_u15_{thresh}` | Number of population under 15 affected | people |
| `RP{rp}_female_u15_{thresh}` | Number of female population under 15 affected | people |
| `RP{rp}_education_{thresh}_pct` | Percentage of educational facilities flooded | % |
| `RP{rp}_education_{thresh}_count` | Number of educational facilities flooded | count |
| `RP{rp}_hospitals_{thresh}_pct` | Percentage of hospitals flooded | % |
| `RP{rp}_hospitals_{thresh}_count` | Number of hospitals flooded | count |
| `RP{rp}_primary_healthcare_{thresh}_pct` | Percentage of primary healthcare facilities flooded | % |
| `RP{rp}_primary_healthcare_{thresh}_count` | Number of primary healthcare facilities flooded | count |

> `{rp}` is the return period (e.g., 10, 50, 100 years), `{thresh}` is the flood threshold in cm.

### Flood Threshold
| Parameter | Value | Description |
|-----------|-------|-------------|
| `setup.flood_threshold` | e.g., 0.3 m | Minimum flood depth considered for exposure (configurable in `assets_config.yaml`) |

### Processing Steps
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
   - Fetches required demographic rasters (total population, female, children under 5, elderly, etc.).  
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

### Outputs
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
    indicators = ["female_pop", "children_u5", "female_u5", "elderly", "pop_u15", "female_u15"]
    tif_map = dict(zip(indicators, indicator_tifs))

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
            f"RP{rp}_{label}_{suffix}" for label in indicators for suffix in THRESH_SUFFIX
        ] + [
            f"RP{rp}_{cat}_{suffix}_pct" for cat in facility_categories for suffix in THRESH_SUFFIX
        ] + [
            f"RP{rp}_{cat}_{suffix}_count" for cat in facility_categories for suffix in THRESH_SUFFIX
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
