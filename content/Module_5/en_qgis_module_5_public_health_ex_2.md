# Exercise 2: Analysing Measles Case Data and Population Distribution
## Background

% MAKE THEM LOOK FOR THE WORLDPOP DATASET ON DEMOGRAPHY AND MAKE THEM CALCULATE THE UNDER 5 POP RASTER

The Epidemiology Department has shared a line-list of suspected measles cases reported by health districts.
Your task in this exercise is to combine this surveillance data with population estimates from WorldPop to identify districts with high measles incidence rates.
This will help the response coordination team prioritise vaccination deployments and plan logistics for outreach activities.

## Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/modul_5/gis_training_public_health_exercise_2/GIS_Training_Public_Health_exercise_2.zip

__In case you did the exercise [Creating an overview map of the health system and vaccination coverage](/content/Module_3/en_module_3_public_health_ex_1.md), you do not need to download this dataset.
If you do this exercise without doing the previous exercise, download all datasets provided by HeiGIT [here](https://nexus.heigit.org/repository/gis-training-resource-center/modul_5/gis_training_public_health_exercise_2/GIS_Training_Public_Health_exercise_2.zip). and save the folder on your computer and unzip the file.__

:::


:::

| Dataset name                       | Description                                          | Source                                      | Download link / note                               |
| :--------------------------------- | :--------------------------------------------------- | :------------------------------------------ | :------------------------------------------------- |
| `QGIS project from Exercise 1 with .qgz extention`   | QGIS project created in Exercise 1                   | [Previous Exercise](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_module_3_public_health_ex_1.html)        | Local project folder `/project/`                   |
| `tcd_admbnda_adm2_20250212_AB.shp` | Chad administrative boundaries (level 2 – districts) | OCHA                                        | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_pop_2025_CN_100m_R2025A_v1.tif`            | 2025 population estimate per grid-cell               | WorldPop                                    | [WorldPop](https://hub.worldpop.org/geodata/summary?id=72895)              |
| `measles_cases_adm2.csv`           | Reported measles cases by district (line list)       | Ministry of Health (MoH) Epidemiology Dept. | Provided for this exercise by HeiGIT                        |

:::{note}

All data provided by HeiGIT can be downloaded [here](https://nexus.heigit.org/repository/gis-training-resource-center/public_health/GIS_Training_Public_Health.zip)

:::

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

1. Add the WorldPop 2025 raster (`tcd_pop_2025_CN_100m_R2025A_v1.tif`) via drag-and-drop or:
    `Layer → Add Layer → Add Raster Layer….`
    - Take the time to investigate the new layer. Where is the population concentrated? What is the highest or median cell value? How is raster data different to vector data? 
    :::{tip}
    You can use the Identify Tool ![](/fig/qgis_identify_features.png) to click on the raster and see population estimates per pixel.
    :::

2. We will now calculate the total population for each district using the tool "Zonal Statistics"
    - In the __[Processing Toolbox](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html#toolbox-toolbars)__, search for "Zonal Statistics" and open the tool.
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
Apply a graduated classification to visualize the district-level population sum results
:::

### Task 3: Calculate the Population under 5 per District

Measles disproportionately affects young children, especially those under five, who are more likely to develop severe complications and have higher mortality rates. Knowing the under-5 population per district helps estimate how many children are at greatest risk, plan targeted vaccination campaigns, and assess whether health resources are sufficient to protect the most vulnerable age group ([WHO on Measles](https://www.who.int/news-room/fact-sheets/detail/measles)).

:::{admonition} Worldpop data in age and sex structures
:class: tip
WorldPop also provides population estimates by age and sex. This is especially important in our scenario, as we need to know the under-5 population for each district. To find this, go to the Age Structures section and search for Chad.

Can you find and download the WorldPop raster containing the population under 5? For a hint look [here](https://hub.worldpop.org/geodata/listing?id=138). If you scroll down, there is list of the Data Files for the specific age groups.
:::

1. Add the population under 5 rasters (`tcd_t_00_2025_CN_100m_R2025A_v1.tif` and `tcd_t_01_2025_CN_100m_R2025A_v1`) via drag-and-drop or:
    `Layer → Add Layer → Add Raster Layer….`
2. We will now calculate the total population under 5 for each district using the “Zonal Statistics” tool. Repeat the steps from the previous task. Since the under-5 population is split across two input rasters, you will need to run the same procedure twice.
    - Set the parameters as follows:
        - Input layer: `tcd_pop_2025_adm2` (output from the previous task already containing the total population sum per districts)
        - Raster layer: `tcd_t_00_2025_CN_100m_R2025A_v1`
        - Raster band: 1 (there will be only one option available)
        - Ouput column prefix: `population_under_1_`
        - Statistics to calculate: `Sum`
    - Click `Run`.
    - Rename the output in the QGIS Layers panel to `tcd_pop_2025_under_1`
3. Repeat this step with the raster `tcd_t_01_2025_CN_100m_R2025A_v1` as input raster layer and name the output column prefix `population_under_5_`. As Input layer, use the "Zonal Statistics" output from the run for the population under 1 renamed to `tcd_pop_2025_under_1`.
    - Rename the output in the QGIS Layers panel to `tcd_pop_2025_under_5` and remove the `tcd_pop_2025_under_1` layer ![](/fig/qgis_remove_selected_layer.png) as we don't need it anymore.
4. Open the field calculator in the attribute table. 
    - <kbd>Right-click</kbd> on the layer and open the attribute table or click on this symbol ![](/fig/qgis_open_attribute_table.png) 
    - In the tool bar of the attribute table, open the ![](/fig/qgis_3.40_open_field_calc_icon.png). The field calculator let's you enter expression to calculate new columns. 
    - A new window will open. This is the expression builder.
5. In the expression builder, we can build and test expressions. 
    - In the middle section, we can open the "Fields and values" header to show the columns of the dataset. Uncollapse it and <kbd>Double-Click</kbd> on `population_under_1_sum` and `population_under_5_sum`. This will add the column to the expression window on the left.
    - In the expression window
    - Enter the following expression: 
    ```
    population_under_1_sum + population_under_5_sum
    ```
    - Make sure to give a meaningful "Output field name" such as `total_population_under_5`
    - Select the correct "Output field type"

    :::{figure} /fig/en_pub_health_2_pop_under_5.png
    ---
    name: en_pub_health_2_pop_under_5
    width: 650 px
    ---
    :::
6. Now remove the fields containing the `population_under_1_sum` and `population_under_5_sum` information as we don't need them anymore. Click on "Delete fields" ![](/fig/qgis_3.40_delete_column_icon.png) and remove these two columns. Save the layer.
    - Save the enhanced population layer by <kbd>right-clicking</kbd> on it and selecting `Make permament...`. Select "Geopackage" as the output format and save the layer to the `data/interim/`-folder and enter a file name such as `tcd_pop_2025_under_5`. Click `Save`.

### Task 4: Import and Explore the Measles Cases List

% Revise this step.

1. [Import](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-import) the `measles_cases_adm2` dataset as a __delimited text layer__ with no geometry.
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

2. Explore the new data file by opening the attribute table.
    - <kbd>Right-click</kbd> on the `measles_cases_adm2`-layer and open the attribute table.
    - Take a look at the columns and at how the data is being stored. 
    - How could we use this data in our map? 

<!--- 

% THIS STEP IS REMOVED AS I DONT HAVE THE DATA SO THE AGGREGATION PART CAN BE DONE. WE WILL SKIP THIS TASK AND DIRECTLY JUMP INTO THE JOIN
% TO ADD SOME ADDITIONAL VALUE THE CALCULATION OF POPULATION UNDER 5 WAS ADDED

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

-->  

### Task 5: Joining the measles cases with our adm2 layer

1. We can join the measles cases with our adm2-layer including the population data (`tcd_pop_2025_under_5`):
    - In the processing toolbox, open the "Join Attributes by Field value"-tool
    - __Input layer:__ `tcd_pop_2025_under_5`
    - __Table field:__ `ADM2_FR`
    - __Input layer 2:__ `measles_cases_adm2`
    - __Table field 2:__ `adm2_name`
    - Under "Layer 2 fields to copy" select `cases_total`
    - Click `Run`.

> The result will be a new layer called `Joined layer`. Let's open the attribute table and look at the data. 

2. If everything is correct, let's make the layer permanent under `tcd_pop_2025_measles_adm2`


### Task 6: Calculating the incidence rate

Our district layer now includes the total population, the population under 5 and the total number of measles cases per district. With this information, we can calculate the incidence rate.

1. Open the field calculator in the attribute table. 
    - <kbd>Right-click</kbd> on the layer and open the attribute table
    - In the tool bar of the attribute table, open the ![](/fig/qgis_3.40_open_field_calc_icon.png).
    - A new window will open with the expression builder.
    - Make sure to give a meaningful "Output field name" such as `measles_incidence_rate`
2. In the expression builder, we can build and test expressions. 
    - In the middle section, we can open the "Fields and values" header to show the columns of the dataset. Uncollapse it and <kbd>Double-Click</kbd> on "population_sum". This will add the column to the expression window on the left.
    - In the expression window
    - Enter the following expression: 
    ```
    (cases_total / population_sum ) * 10000
    ```
    - Save the layer and the changes.

> Great, we have calculated the incidence rate in our polygon layer. Now, we can create a map displaying the information we gained

### Task 7: Creating map of measles incidence rate 

In this task, we will create a map showing the measles incidence rate by district, helping to visualize where the disease burden is highest. We will also add an overview map displaying the population under five, providing important context for understanding the distribution of vulnerable age groups and interpreting the incidence patterns.

#### Task 7.1: Symbology

1. Symbology measles incidence rate
    - Use the `tcd_pop_2025_measles_adm2` layer with the incidence rate from the previous calculation
    - <kbd>Right-click</kbd> on the layer and open the symbology tab
    - Select `Graduated` and `measles_incidence_rate` as the "Value"
    - Color ramp could be `Reds`
    - Select Mode `Equal Interval` and 5 Classes
2. Symbology population under 5
    - Use the `tcd_pop_2025_under_5` layer with the information of population under 5
    - <kbd>Right-click</kbd> on the layer and open the symbology tab
    - Select `Graduated` and `total_population_under_5` as the "Value"
    - Color ramp could be `Turbo`
    - Select Mode `Equal Count` and 5 Classes

#### Task 7.2: Print Layout

Once you are happy with the symbolization and colors of your data, the next step is to create a print layout. By adding additional information such as a title, data sources, projection, description, etc. you provide your audience with the means to contextualise and evaluate the map and it's content by themselves.

1. Open a new print layout and give it a name (e.g. Measles Incidence Chad). A new window will open with a blank canvas and a different set of tools. This is the print layout designer.
    - On the left, you will find a toolbar with tools to add and move items on the print layout canvas.
    - On the right you will find a list of items you added to the print layout (it is still empty). Beneath this, you will find a tab called __"Item properties"__. This is where you modify the items on your print layout (e.g. enter the text for a text box or change the font).
2. Insert a new map by clicking on ![New Map Icon](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) on the left toolbar, and drawing a rectangle on the print canvas. [Video](/content/Module_4/en_qgis_map_design_2.md#adding-a-new-map)
3. Move and position the map so that the entire country is visible at a reasonable scale. The first map will be used for the measles incidence rate.
4. For our example we want to add another map. In this overview map we will display the population under 5.

:::{admonition} Lock layers and Lock styles for layers
When working with multiple maps in the Print Layout, you need to lock the layers and their styles in the Item Properties under the “Layers” section. This ensures that each map remains unchanged, even if you turn layers on or off in the main QGIS window.
:::

5. Let's add a title:
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Drag a rectangle on the canvas.
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter your map title (e.g. Measles Incidence Rate | Chad).
    - Adjust the font size: Click on the __Font__ dropdown menu and adjust the font size for a title (25p or more). Adjust the text box if necessary.
6. Let's add a legend:
    - Click on  ![Add legend icon](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`). 
    - Navigate to the __Item Properties__ panel on the right. 
    - Scroll down a bit and check turn off `Auto Update` by unchecking the check box. Now you can freely edit every item on the legend
    - Adjust the legend by removing unnecessary layers (which are not seen on the map) and rename the layer in the legend by clicking on ![Edit Icon](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) below the legend entries.
7. Now, let's add a scale bar:
    - Click on ![Add Scale bar icon](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Draw a rectangle on the map and position the scale bar on the edge of the map. You can adjust the scale bar units (meters, kilometers, ...), the fixed segment width (50 km, 75 km, 100 km, ...) and the number of segments (to the right).
8. Let's add a north arrow:
    - Click on ![Add North Arrow Icon](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`). 
    - Drag a rectangle on the print layout. Adjust the size and location of the north arrow. You can also change the icon in the item properties.
9. Add a text box with additional information, sources, the author (you), and date of creation.
10. When you are happy with your print layout. You can export it as a PDF. You can save it in the project folder under "results".
11. Once you have exported the map. Look at the PDF and make sure it looks how you intended. Some things might look different in the PDF. If it does not look correct you may need to make some adjustments in the symbology.

The finished map could look something like this:

:::{figure} ../../fig/pub_health_map_measles_incidence_chad.png
---
name: Main road network and hospitals in Ghana, Africa
width: 600px
---
The main map displays the measles incidence rate, while the secondary map shows the population under five.
:::







