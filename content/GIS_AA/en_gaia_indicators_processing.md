# GAIA Pipeline Documentation

## Overview

The GAIA Pipeline produces a series of thematic files for each country at administrative level 2. Each file captures different aspects of population, infrastructure, and environmental conditions. Below is an overview of the available files:

- **Access to Services** – Population accessibility to key facilities such as education and health centers.  
- **Facilities** – Availability and distribution of essential service infrastructure.  
- **Coping Capacity** – Combined indicators derived from Access and Facilities layers to assess local coping capacity.  
- **Demographics** – Distribution of vulnerable population.  
- **Rural Population** – Demographic indicators focused specifically on rural populations.  
- **Vulnerability** – Composite indicators derived from Demographics and Rural Population layers.  
- **Crop Coverage and Change** – Extent of agricultural land and observed changes over time.  
- **Vegetation Index** – NDVI-based assessment of vegetation conditions.  
- **Flood Exposure** – Exposure of populations and facilities to flood hazards.
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
    from pathlib import Path
    import geopandas as gpd
    import pandas as pd
    import rioxarray
    from rasterstats import zonal_stats

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
*(Details extracted from `facilities.py`)*

...

---

## Coping Capacity
*(Details extracted from `coping_capacity.py`)*

...
