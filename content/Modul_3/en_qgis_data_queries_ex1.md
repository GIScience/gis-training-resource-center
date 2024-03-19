# Selection and Queries Exercise 1

__🔙[Back to Homepage](/content/intro.md)__

## Aim of the exercise:


## Relevant Wiki Articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Non-Spatial Querie](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html)
* [Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
html#add-geometries-to-a-layer)
* [Geoprocessing - Clip](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#clip) 


## Data sources
Download the data folder [here]() and save it on your PC. Unzip the .zip file!
The folder is called “Modul_3_Exercise_1_Flood_Nigeria" and contains the whole [standard folder structure](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure) with all data in the input folder and the additional documentation in the documentation folder.

*



1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New` N
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the “project” folder of the exercise “Modul3_Exercise_1_Flood_Nigeria”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Somalia_flood_affected_Blete_Weyne_2023.
3. Load the following files in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to the file. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    - "som_admbnda_adm2_ocha_20230308.shp"
    - "FL20231105SOM — GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.gpkg"
    - "SOM_Blete_Weyne_buildings.gpkg"
This dataset contains all administrative division areas (admin 0 to 5) with the respective population of the areas. 
``` {Attention}
GeoPackage file can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```
4. First, we want to export the district __Belete Weyne__ state from "som_admbnda_adm2_ocha_20230308" to have it as a stand-alone vector layer. To do that, 
    1. Open the attribute table of "som_admbnda_adm2_ocha_20230308" by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    2. Find the row of "Belete Weyne" and mark it by clicking on the number on the very left-hand side of the attribute table. The row will appear blue and the area of Borno state will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    3. Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save Belete Weyne as a GeoPackage, so adjust `Format` accordingly. Click on the three points and navigate to your `temp` folder. Here you can give it the layer the name “AOI_Belete_Weyne” and click `Save`. Now you should see the same name in the `Layer name` field. Click `ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))

5. In the next steps we want to identfy all buildings that are susbected to be affected by the recent flood. To do that we will use the tool `Extract by Location`.
    1. In the `Toolbox` -> Search for `Extract by Location`
    2. `Extract featurs from`: "SOM_Blete_Weyne_buildings.gpkg"
    3. `Where the features (geomeric predicate)`: `are within`
    4. `By comparing to the features from`: "FL20231105SOM — GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.gpkg"
    5. Under `Extraction` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you temp folder and save the new layer under the name "Belet_Weyne_buildings_affected" and click `Save`. 
    6. Click `Run`
    7. Adjust you layer in a way that you only see the flooded areas and your new layer  "Belet_Weyne_buildings_affected".

```{Attention}
The tool [`Select by location`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#select-by-location) is very similar. This tool function in the same way only that it select the features insted of diretly extracting the features.
```

```{figure} /fig/Extract_by_location_Belet_Weyne.png
---
width: 400px
name: 
align: center
---
```

6. In the next step we want to identfy special buildings with in the affeted buildings. Open the attribute table and check what kind of buildings can be found in the layer. This information can be found in the coloumn „building“. You can sort the column.
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
