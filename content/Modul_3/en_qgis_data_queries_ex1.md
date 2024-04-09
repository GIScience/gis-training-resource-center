# Selection and Queries Exercise 1

__🔙[Back to Homepage](/content/intro.md)__

🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Aim of the exercise


### Links to Wiki articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Non-Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html)
* [Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
* [Geoprocessing - Clip](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#clip) 


## Data
Download all the datasets [here]() and save the folder on your computer and unzip the file. The zip folder includes:
- `som_admbnda_adm2_ocha_20230308.shp`: This file contains information about the Somali administrative level 0-2, state, and operational zone level 1 and 2 boundary as shapefiles. The data can also be found on [HDX](https://data.humdata.org/dataset/cod-ab-som).
- `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`: This shapefile illustrates satellite-detected surface waters in Beledweyne City, Beledweyne District, Hiraan Region, Somalia, on 12th of November 2023 at 07:32 UTC. The data is also available on [HDX](https://data.humdata.org/dataset/water-extent-in-beledweyne-city-beledweyne-district-hiraan-region-somalia-12-november-2023).
- `Buildings_Belete_Weyne.geojson`: This dataset is downloaded using [HOT Export Tool](https://export.hotosm.org/v3/exports/new/describe) and contains information about buildings in the Beledweyne district.

The folder is called **Modul_3_Exercise_1_Queries_Somalia** and contains the entire [standard folder structure](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure) with all data in the input folder.

``` {Note}
The naming of the districts and states is not consistent across the different datasets. You will find different spellings for the district name **Beledweyne** which we will be focusing on. Other spellings might be **Belet Weyne** or **Belete Weyne**. 
```

## Tasks
1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` --> `New`.

2. Once the project is created, [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the **project folder** of the exercise **Modul_3_Exercise_1_Queries_Somalia**. To do that click on `Project` --> `Save as` and navigate to the folder. Name the project **Somalia_flood_affected_Beledweyne_2023**.

3. To load the following files into your project, drag and drop them ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer` --> `Add Layer` --> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to the file. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    - `som_admbnda_adm2_ocha_20230308.shp`
    - `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`
    - `Buildings_Belete_Weyne.geojson`: A pop-up window will appear for this file and you will need to decide which data to import. Select the polygons.

4. First, we want to export the district __Beledweyne__ from the Hiraan region from `som_admbnda_adm2_ocha_20230308.shp` to have it as a stand-alone vector layer. To do that:
    1. Open the attribute table of `som_admbnda_adm2_ocha_20230308.shp` by right clicking on the layer  --> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    2. Find the row of `Belet Weyne` and mark it by clicking on the number on the very left-hand side of the attribute table. The row will be highlighted in blue and the district will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    3. Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save Beledweyne as a GeoPackage, so adjust `Format` accordingly. Click on the three points and navigate to your **temp folder**. Here you can give the layer the name **AOI_Beledweyne** and click `Save`. Now click `OK`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file)). In this exercise, we will not reproject the layers and work with the data in `ESPG:4326 - WGS84`.

5. In the following steps, we want to identify all buildings that are likely to be affected by the recent flooding. To do that we will use the tool `Extract by Location`.
    1. In the `Processing Toolbox` --> Search for `Extract by Location`
    2. `Extract features from`: Buildings_Belete_Weyne.geojson
    3. `Where the features (geometric predicate)`: `are within`
    4. `By comparing to the features from`: GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp
    5. Under `Extracted` click on the three points ![](/fig/Three_points.png) --> `Save to File...` and navigate to your **temp folder** and save the new layer under the name **Beledweyne_buildings_affected** and click `Save`. 
    6. Now click `Run`
    7. Adjust your layers in a way that you only see the flooded areas and your new layer **Beledweyne_buildings_affected**. Remove the `som_admbnda_adm2_ocha_20230308.shp` and `Buildings_Belete_Weyne.geojson` layer.

```{Attention}
The tool [`Select by Location`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#select-by-location) is very similar. This tool functions in the same way, but instead of directly extracting the features, it selects them.
```

```{figure} /fig/Extract_by_location_Belet_Weyne.png
---
width: 400px
name: 
align: center
---
```

6. In the next step we want to identify special buildings within the affected buildings. Open the attribute table and check what kind of buildings can be found in the layer. This information can be found in the column „building“. You can sort the column.
To extract „hospitals“, „schools“ and „mosques“ we can use the tool `Extract by Expression` or `Extract by Attribute`.


::::{grid} 2
:::{card} `Extract by Attribute`
1. Find the tool `Extract by Expression` in the `Toolbox.
2. `Expression`: click on ![](mIconExpression.png). 
3. The window „Expression“ will open. Here we can build a very specific query. In the central panel open `Field and Values`. Here you can see all the columns oft he the layer. Click on `building`.On the right-hand side, you should now see the option `All unique`. Click on it. Here you can see now all unique values in the column „building“.
4. 





```md
"building" =  'hospital'or 
"building"  =  'school' or
"building"  = 'mosque' 
```


en_extract_by_expression_som.png

en_extract_by_expression_som2.png

Belet_Weyne_POI_affected.gpkg

:::

:::{card} `Extract by Expression`
In the learning modules, all relevant concepts and techniques of QGIS are explained, enabling trainees to reinforce their understanding of the training content
:::


::::

6. Find the tool `Extract by Expression` in the `Toolbox.
    1. 
