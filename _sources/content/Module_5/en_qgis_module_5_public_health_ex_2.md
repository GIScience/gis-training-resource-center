# Exercise 2: Analysing Measles Case Data and Population Distribution
## Background

The Epidemiology Department has shared a line-list of suspected measles cases reported by health districts.
Your task in this exercise is to combine this surveillance data with population estimates from WorldPop to identify districts with high measles incidence rates.
This will help the response coordination team prioritise vaccination deployments and plan logistics for outreach activities.

## Available Data

:::{note}


:::

| Dataset name                       | Description                                          | Source                                      | Download link / note                               |
| :--------------------------------- | :--------------------------------------------------- | :------------------------------------------ | :------------------------------------------------- |
| `chad_health_infrastructure.qgz`   | QGIS project created in Exercise 1                   | [Previous Exercise](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_module_3_public_health_ex_1.html)        | Local project folder `/project/`                   |
| `tcd_admbnda_adm2_20250212_AB.shp` | Chad administrative boundaries (level 2 – districts) | OCHA                                        | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_worldpop_2025.tif`            | 2025 population estimate raster                      | WorldPop                                    | [WorldPop](https://www.worldpop.org/)              |
| `measles_cases_2025.csv`           | Reported measles cases by district (line list)       | Ministry of Health (MoH) Epidemiology Dept. | Provided for this exercise                         |
| `tcd_dem_2025.tif`                 | Digital Elevation Model (optional)                   | NASA SRTM                                   | Optional (for terrain visualization)               |


## Tasks
### Task 1: Open the Project and Prepare the Workspace

1. Open the QGIS project created in Exercise 1:
    - Project → Open… → chad_health_infrastructure.qgz.

2. Verify that the administrative boundaries and health facility layers load correctly.
    - If any layers show an error, use the “Re-link missing layers” dialog to correct their file paths.

### Task 2: Add and Clip the Population raster

3. Add the WorldPop 2025 raster (`tcd_worldpop_2025.tif`) via drag-and-drop or:
    `Layer → Add Layer → Add Raster Layer….`
4. 