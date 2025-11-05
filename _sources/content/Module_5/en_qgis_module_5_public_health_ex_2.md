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




### Task 2: Calculate the Population per District

In order to calculate the incidence rate per district, we first need to know the population in each district. In many humanitarian contexts, there may be no recent or reliable census data available due to conflict, displacement, or limited national statistical capacity. In such cases, we can use WorldPop population estimates to approximate the population per district. WorldPop produces high-resolution gridded population datasets by combining census data, satellite imagery, land cover information, and statistical modelling to predict population distribution. While these estimates are very useful for planning and epidemiological analysis, it is important to remember that they are modelled estimates, not exact counts, and may carry some uncertainty.

3. Add the WorldPop 2025 raster (`tcd_worldpop_2025.tif`) via drag-and-drop or:
    `Layer → Add Layer → Add Raster Layer….`
    - Take the time to investigate the new layer. Where is the population concentrated? What is the highest or median cell value? How is raster data different to vector data? 
    :::{tip}
    You can use the Identify Tool to click on the raster and see population estimates per pixel.
    :::

4. We will now calculate the total population for each district using the tool "Zonal Statistics"
    - In the __[Processing Toolbox](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html#toolbox-toolbars)__, search for "Zonal Statistisc" and open the tool.
    - Set the parameters as follows:
        - Input layer: `tcd_admbnda_adm2_20250212_AB`
        - Raster layer: `tcd_worldpop_2025`
        - Raster band: 1
        - Ouput column prefix: `population_`
        - Statistics to calculate: `Sum`
    - Click `Run`.
    - The Result will be a new layer called `Zonal Statistics`. This is a temporary layer, indicated by the ![](/fig/qgis_3.40_temp_layer.png) on the right of the layer name. 
    - Make the layer permanent by <kbd>right-clicking</kbd> on it → `Make permanent`.  
    - Take a look at the new layer by opening it's attribute table and looking at the new column.
    ::::{margin}
    :::{tip}
    You can also classify the polygons with the new column using [graduated classification](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)
    :::
    ::::

### Task 3: Import and Explore the Measles Cases List

5. [Import](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-import) the measles cases dataset as a __delimited text layer__ with no geometry.
    - In the top bar, navigate to `Layer` → `Add Layer` → `Add Delimited Text Layer...`. A new window will open.
    - To the right of file name, click on the ![](/fig/Three_points.png) three points and navigate to the file in the `/data/input/`-folder. Click `Open`.
    - Under `Geometry Definition` select `No geometry (attribute only table)`.
    - Check if the sample data displays correctly.
    - Click `Add`. 

6. Explore the new data file by opening the attribute table.
    - <kbd>Right-click</kbd> on the `measles_cases_adm2`-layer and open the attribute table.
    - Take a look at the columns and at how the data is being stored. 
    - How could we use this data in our map?

### Task 4: Aggregate the measles case data with the district boundaries (adm2)

7. 

