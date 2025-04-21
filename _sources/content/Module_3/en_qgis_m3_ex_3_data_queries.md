::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

:::{grid-item-card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_exercises.html

__Click here to return to the exercise overview for module 3.__ 
:::
::::

# Exercise 3: Data Queries

## Characteristics of the exercise

:::{topic}
__Aim of the exercise:__
^^^
The aim of this exercise is to learn how to manipulate secondary data to generate insights. In this exercise, we will determine which buildings have been affected by a flood and apply a filter to determine which buildings are part of the critical infrastructure. 
:::


### Links to Wiki articles

* [QGIS Interface](/content/Wiki/en_qgis_interface_wiki.md)
* [Types of Geodata](/content/Wiki/en_qgis_geodata_types_wiki.md)
* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Layer Concept](/content/Wiki/en_qgis_layer_concept_wiki.md)
* [Non-Spatial Queries](/content/Wiki/en_qgis_non_spatial_queries_wiki.md)
* [Spatial Queries](/content/Wiki/en_qgis_spatial_queries_wiki.md)
* [Table function - Add field](/content/Wiki/en_qgis_table_functions_wiki.md)
* [Geoprocessing - Clip](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#clip) 


## Data

Download all the datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_3/Module_3_Exercise_3_Data_Queries.zip), save the folder on your computer, and unzip the file. The zip folder includes:

- `som_admbnda_adm2_ocha_20230308.shp`: This file contains information about the Somali administrative level 0-2, state, and operational zone level 1 and 2 boundary as shapefiles. The data can also be found on [HDX](https://data.humdata.org/dataset/cod-ab-som).
- `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`: This shapefile illustrates satellite-detected surface waters in Beledweyne City, Beledweyne District, Hiraan Region, Somalia, on 12th of November 2023 at 07:32 UTC. The data is also available on [HDX](https://data.humdata.org/dataset/water-extent-in-beledweyne-city-beledweyne-district-hiraan-region-somalia-12-november-2023).
- `buildings_belet_weyne.geojson`: This dataset is downloaded using [HOT Export Tool](https://export.hotosm.org/v3/exports/new/describe) and contains information about buildings in the Beledweyne district.


<!--EDIT: We could add an optional step for trainees to download the data from the HOT Export Tool themselves (requires HOT Export Tool Exercise from Module 2)-->

The folder is called **Module_3_Exercise_3_Data_Queries** and contains the entire [standard folder structure](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure) with all data in the input folder.

``` {Note}
The naming of the districts and states is not consistent across the different datasets. You will find different spellings for the district name **Beledweyne** which we will be focusing on. Other spellings might be **Belet Weyne** or **Belete Weyne**. In many cases, you will have to edit the values in the datasets to remove different spelling of spelling mistakes. This process is called "data cleaning".
```

## Tasks

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` --> `New`.

2. Once the project is created, [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save-project) in the **project folder** of the exercise **Module_3_Exercise_1_Queries_Somalia**. To do that click on `Project` --> `Save as` and navigate to the folder. Name the project **Somalia_flood_affected_Beledweyne_2023**.

3. To load the following files into your project, drag and drop them ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer` --> `Add Layer` --> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to the file. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    - `som_admbnda_adm2_ocha_20230308.shp`
    - `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`
    - `Buildings_Belete_Weyne.geojson`: A pop-up window will appear for this file and you will need to decide which data to import. Select the polygons.

```{tip}
Make sure you __unzip__ the exercise folder before loading the layers into QGIS. QGIS does not accept compressed files.
```

### Extract the district (adm2) from the administrative boundaries layer

4. First, we want to export the district __Beledweyne__ from the Hiraan region from `som_admbnda_adm2_ocha_20230308.shp` to have it as a stand-alone vector layer. To do that:
    1. Open the attribute table of `som_admbnda_adm2_ocha_20230308.shp` by right clicking on the layer  --> `Open Attribute Table`([Wiki Video](/content/Wiki/en_qgis_attribute_table_wiki.md)).
    2. Find the row of `Belet Weyne` and mark it by clicking on the number on the very left-hand side of the attribute table. The row will be highlighted in blue and the district will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    3. Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save Beledweyne as a GeoPackage, so adjust `Format` accordingly. Click on the three points and navigate to your **temp folder**. Here you can give the layer the name **AOI_Beledweyne** and click `Save`. Now click `OK`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file)). In this exercise, we will not reproject the layers and work with the data in `ESPG:4326 - WGS84`.

### Identify the building that might be affected by the flooding

5. In the following steps, we want to identify all buildings that are likely to be affected by the recent flooding. To do that we will use the tool `Extract by Location`.
    ```{figure} /fig/Extract_by_location_Belet_Weyne.png
    ---
    width: 500 px
    name: extract_by_location
    align: center
    ---
    The extract by extraction window in QGIS 3.36
    ```
    1. In the __"Processing Toolbox"__ --> Search for `Extract by Location`
    2. __"Extract features from"__: `Buildings_Belete_Weyne.geojson`
    3. __"Where the features (geometric predicate)"__: `are within`
    4. __"By comparing to the features from"__: `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`
    5. Under `Extracted` click on the three points ![](/fig/Three_points.png) --> `Save to File...` and navigate to your **temp folder** and save the new layer under the name **Beledweyne_buildings_affected** and click `Save`. 
    6. Now, click `Run`.
    7. Adjust your layers in a way that you only see the flooded areas and your new layer **Beledweyne_buildings_affected**. Remove the `som_admbnda_adm2_ocha_20230308.shp` and `Buildings_Belete_Weyne.geojson` layer.

    ```{Attention}
    The tool [`Select by Location`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#select-by-location) is very similar. This tool functions in the same way, but instead of directly extracting the features, it selects them.
    ```

### Identify critical infrastructure affected by the floods

6. In the next step, we want to identify special buildings among the affected buildings. Open the attribute table and check what kind of buildings can be found in the layer. This information can be found in the column "building". You can sort this column.
To extract "hospitals", "schools", and "mosques", we can use the tool `Extract by Expression`.
    1.  Find the tool `Extract by Expression` in the `Toolbox`.
    2. `Expression`: click on ![](/fig/miconexpression.png). 
    3. The window "Expression" will open. Here we can build a very specific query. In the central panel open `Field and values`. Here you can see all the columns oft he the layer. Click on `building`. On the right-hand side, you should now see the option `All unique`. Click on it. Here you can see now all unique values in the column „building“.
    4. In the `Expression` field, enter the following expression (see the figure below):
        ```
        "building" = 'hospital' or
        "building" = 'school' or
        "building" = 'mosque' 
        ```
    5. Click `Ok`. The window will close and you will see the expression you created in the `Expression`-field in the `Extract by Expression` window (see figure below). 
    6. Click `Run`. A new temporary layer called `Matching Features` will be added to your QGIS-project. Close the `Extract by Expression` window.
   
```{figure} /fig/en_extract_by_expression_som.png
---
name: extract_by_expression1
width: 400 px
---
The expression window in QGIS 3.36 with an expression to extract the polygons with the "buildings" value 'hospital', 'school', and 'mosque'. 
```


```{figure} /fig/en_extract_by_expression_som2.png
---
name: extract_by_expression2
width: 400 px
---
The `Extract by Expression` window in QGIS 3.36
```

:::{attention}
A temporary layer will not be saved to your QGIS-project, even after saving the project. Temporary layers are marked by a ![](/fig/icon_scratch_layer.png). In order to save the layer permanently, <kbd>Right Click</kbd> on the layer you wish to make permanent. Then, select the save location for the new layer. Make sure you to save it in the correct folder (see [standard folder structure](/content/Wiki/en_qgis_projects_folder_structure_wiki.md)). 
:::

 
7. Explore the new layer by opening the attribute table, activating and deactivating the layer in the Layers panel. 
8. <kbd>Right Click</kbd> on the `Matching Features` layer and save it to your project folder under  `/data/output/` with the name `Belet_Weyne_POI_affected.gpkg`. 

Congratulations! The extracted information can now be used to perform further analyses or create comprehensive maps of the affected points of interest. 

<!--ADD picture of this step-->

```{note}
This exercise has an optional part 2 in module 4, covering the visualisation of the processed data. 

You can find the exercise [here].

```
