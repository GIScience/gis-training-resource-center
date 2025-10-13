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

:::{dropdown} Python Code
       
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

:::{dropdown} Python Code
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
This layer combines [**Access to Services**](#access-to-services) and [**Facilities**](#facilities) indicators to assess local capacity to cope with shocks or disruptions.

### Data Sources
- **Access to Services CSVs:** Derived from population accessibility analysis (see [*Access to Services*](#access-to-services) chapter).  
- **Facilities CSVs:** Derived from OpenStreetMap facility data (see [*Facilities*](#facilities) chapter).  
- Both inputs are aggregated at the same administrative level (e.g., ADM2).

### Processing Steps
1. **Input CSVs:**  
   - One *Access to Services* CSV and one *Facilities* CSV are provided per administrative level.
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

:::{dropdown} Python Code
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

:::{dropdown} Python Code
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
