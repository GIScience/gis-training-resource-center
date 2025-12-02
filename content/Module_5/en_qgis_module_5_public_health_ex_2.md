# Exercise 2: Analysing Measles Case Data and Population Distribution
## Background

% MAKE THEM LOOK FOR THE WORLDPOP DATASET ON DEMOGRAPHY AND MAKE THEM CALCULATE THE UNDER 5 POP RASTER

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
| `tcd_pop_2025_CN_100m_R2025A_v1.tif`            | 2025 population estimate per grid-cell               | WorldPop                                    | [WorldPop](https://hub.worldpop.org/geodata/summary?id=72895)              |
| `measles_cases_2025.csv`           | Reported measles cases by district (line list)       | Ministry of Health (MoH) Epidemiology Dept. | Provided for this exercise                         |
| `tcd_dem_2025.tif`                 | Digital Elevation Model (optional)                   | NASA SRTM                                   | Optional (for terrain visualization)               |


## Tasks
### Task 1: Open the Project and Prepare the Workspace

1. Open the QGIS project created in Exercise 1:
    - Project → Open… → chad_health_infrastructure.qgz.

2. Verify that the administrative boundaries and health facility layers load correctly.
    - If any layers show an error, use the “Re-link missing layers” dialog to correct their file paths.


Now, lets configure the "Project Home" in the browser panel.

3. In the browser panel on the left, <kbd>right-click</kbd> on `Project Home` → `Set Project Home...` and set the project home folder to the training folder (with the subfolders `/data`, `/project`, etc.). Now you will be able to access all the datasets for this training through the browser.

:::{tip}
Working with the browser panel allows a much quicker access to the files and keeps the folder view organised when working with shapefiles and multiple layers.
:::



### Task 2: Calculate the Population per District

In order to calculate the incidence rate per district, we first need to know the population in each district. In many humanitarian contexts, there may be no recent or reliable census data available due to conflict, displacement, or limited national statistical capacity. In such cases, we can use WorldPop population estimates to approximate the population per district. WorldPop produces high-resolution gridded population datasets by combining census data, satellite imagery, land cover information, and statistical modelling to predict population distribution. While these estimates are very useful for planning and epidemiological analysis, it is important to remember that they are modelled estimates, not exact counts, and may carry some uncertainty.

3. Add the WorldPop 2025 raster (`tcd_pop_2025_CN_100m_R2025A_v1.tif`) via drag-and-drop or:
    `Layer → Add Layer → Add Raster Layer….`
    - Take the time to investigate the new layer. Where is the population concentrated? What is the highest or median cell value? How is raster data different to vector data? 
    :::{tip}
    You can use the Identify Tool to click on the raster and see population estimates per pixel.
    :::

4. We will now calculate the total population for each district using the tool "Zonal Statistics"
    - In the __[Processing Toolbox](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html#toolbox-toolbars)__, search for "Zonal Statistisc" and open the tool.
    - Set the parameters as follows:
        - Input layer: `tcd_admbnda_adm2_20250212_AB`
        - Raster layer: `tcd_pop_2025_CN_100m_R2025A_v1`
        - Raster band: 1 (there will be only one option available)
        - Ouput column prefix: `population_`
        - Statistics to calculate: `Sum`
    - Click `Run`.
    - The Result will be a new layer called `Zonal Statistics`. This is a temporary layer, indicated by the ![](/fig/qgis_3.40_temp_layer.png) on the right of the layer name. 
    - Make the layer permanent by <kbd>right-clicking</kbd> on it → `Make permanent` and give it a name like `tcd_pop_2025_adm2`.  
    - Take a look at the new layer by opening it's attribute table and looking at the new column.
    ::::{margin}
    :::{tip}
    You can also classify the polygons with the new column using [graduated classification](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)
    :::
    ::::

:::{figure} /fig/en_3.40_m3_ex_8_pub_health_2_add_pop.png
---
name: en_3.40_m3_ex_8_pub_health_2_add_pop
width: 650 px
---
Graduated classification to display results of population sum calculation
:::

:::{admonition} Optional: Downloading additional worldpop data
:class: tip
WorldPop also offers estimations of population in age bracktes. For our scenario, it is useful to know the population under 5 per district. Look for Age structures and search for the country of Chad.

Can you find and download the WorlPop raster containing the population under 5? For a hint look [here](https://hub.worldpop.org/geodata/listing?id=138)

Once you've done so, import it to your QGIS project and calculate the population under 5 per district. 

:::

### Task 3: Import and Explore the Measles Cases List

% Revise this step.

5. [Import](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-import) the `measles_cases_adm2` dataset as a __delimited text layer__ with no geometry.
    - In the top bar, navigate to `Layer` → `Add Layer` → `Add Delimited Text Layer...`. A new window will open.
    - To the right of file name, click on the ![](/fig/Three_points.png) three points and navigate to the file in the `/data/input/`-folder. Click `Open`.
    - In the import window, you will see sample data in the sample data field. Take a look at the columns and data available. What kind of data is present in each column? The measles cases don't have any geometry information.
    - Under `Geometry Definition` select `No geometry (attribute only table)`.
    - Check if the sample data displays correctly. Make sure the data type is correct (e.g., cases as integers, not as string).
    - Click `Add`. 

:::{note}
As with other data formats, you can drag-and-drop csv-files onto your map canvas and it will be loaded into your project. __However__, this will lead to mistakes in the data format for each column as it assumes that every column contains text (string) data. You will be unable to perform mathematical or statistical operations with these columns. 

Make sure to always load csv data via the data source manager and not via the drag-and-drop function.

:::

6. Explore the new data file by opening the attribute table.
    - <kbd>Right-click</kbd> on the `measles_cases_adm2`-layer and open the attribute table.
    - Take a look at the columns and at how the data is being stored. 
    - How could we use this data in our map? 

### Task 4: Aggregate the measles case data with the district boundaries (adm2)

We have received a .csv-file containing measle case report. In order to identify the hotspots, we want to aggregate the number of cases per district (adm2). The data does not include geographic coordinates. However, the dataset includes the names of the settlement where the case has been reported, as well as the district. With this information, we can aggregate the number of cases per district and, in a next step, join them with the adm2-layer. 

% Here you could also add a step to filter the date

9. Because multiple records exist per district and data, we'll aggregate them:
    - In the processing toolbox, search for "Aggregate"
    - As __input layer__, select the measles case data we imported in the previous step.
    - __Group by expression:__ adm2_name
    - In the __Aggregates__ table, remove all the columns (under source expression) except for `adm2_name`, `cases`, `settlement`, and `source`. 
        - To delete a row: select it by clicking on the row number on the left (it will be highlighted blue), and click on ![](/fig/qgis_3.40_delete_column_icon.png).
    - Set the __Aggregate Function__ to `concatenate_unique` for "adm2_name".
    - Set the __Aggregate Function__ to `sum` for "cases".
    - Click `Run`. A new layer will be added to the layers panel on the left.

    ```{figure} /fig/en_qgis_3.40_public_health_aggrg_measle_cases_adm2.png
    ---
    name: en_qgis_3.40_public_health_aggrg_measle_cases_adm2
    width: 600 px
    ---
    Set the parameters for the tool as in the picture. Make sure that the field adm2_name is set to `concatenate_unique` and the cases field to `sum`.

Let's take a look at the resulting data table. The resulting table should look like this:

```{figure} /fig/en_3.40_pub_health_aggregated_measles_data_attr_table.png
---
name: en_3.40_pub_health_aggregated_measles_data_attr_table
width: 600 px
---
The aggregated data table.
```

10. Let's make the new layer permanent by <kbd>right-clicking</kbd> on it → `Make permament`. Name the file "Aggregated_measles_cases_adm2".

> Great, we now have an aggregated list of cases that we can join with the adm2 polygon layer.

### Task 5: Joining the aggregated dataset with our adm2 layer

11. We can join the aggregated table with our adm2-layer including the population data:
    - In the processing toolbox, open the "Join Attributes by Field value"-tool
    - __Input layer:__ `adm2_pop`
    - __Table field:__ `ADM2_FR`
    - __Input layer 2:__ `Aggregated_measles_cases_adm2`
    - __Table field 2:__ `adm2_name`
    - __Fields to copy__ `sum`
    - __Joined field prefix:__ `measles_cases_`
    - Click `Run`.

> The result will be a new layer called `Joined layer`. Let's open the attribute table and look at the data. 

12. If everything is correct, let's make the layer permanent.


### Task 6: Calculating the incidence rate

Our district layer now includes both the population and measle cases. With this information, we can calculate the incidence rate.

13. Open the field calculator in the attribute table. The field calculator let's you enter expression to calculate new columns.
    - <kbd>Right-click</kbd> on the layer and open the attribute table (or select the layer and press F6)
    - In the tool bar of the attribute table, open the ![](/fig/qgis_3.40_open_field_calc_icon.png).
    - A new window will open. This is the expression builder.
14. In the expression builder, we can build and test expressions. 
    - In the middle section, we can open the "Fields and values" header to show the columns of the dataset. Uncollapse it and <kbd>Double-Click</kbd> on "pop_sum". This will add the colun to the expression window on the left.
    - In the expression window
    - Enter the following expression: 
    ```
    (CASES / POP ) * 10000
    ```
% ADJUST CODE TO CORRECT LAYERS
> Great, we have calculated the incidence rate in our polygon layer. Now, we can create a map displaying the information we gained

% SWITCH TO EXERCISE IN MODULE 4


