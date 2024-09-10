# Exercise: Larkana Flood response
__🔙[Back to Homepage](/content/intro.md)__

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_modul_3_exercises.html
__Click here to return to the exercise overview page for module 3__ 
:::
::::{grid} 2
:::{grid-item-card}
## Aim of the exercise:
Participants will work with multiple layers and conduct spatial queries. Additionally, they will learn how to create their own geodata.
#### Type of trainings exercise:
- This exercise can be used in online and presence training. 
:::
:::{grid-item-card}
#### These skills are relevant for 

- QGIS Essentials
- Working with multiple layers
- Conduct spatial queries
- Creation of geodata

:::
::::

::::{grid} 2
:::{grid-item-card}
#### Estimated time demand for the exercise.
- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.
:::

:::{grid-item-card}
### Relevant wiki articles

* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Geodata Classification - Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)
* [Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
* [Digitisation- Point data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer)
:::
::::

::::{grid} 1
:::{grid-item-card}
#### Context
In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. The following analysis will utilize actual data from this natural disaster. The objective is to pinpoint the specific medical centers and healthcare facilities that were impacted by the flooding. Additionally, we will assess the viability of road access to the city of Larkana throughout the flood period.
:::
::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) for some general tips on training conduction

### Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::
### Available Data

:::{card}
:link: https://data.humdata.org/dataset/hotosm_pak_health_facilities
__Download all datasets [here]() and save the folder on your computer and unzip the file.__
:::


| Dataset name| Origonal title|Publisher|Download from| 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_adm2_Sindh.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
|  VIIRS_20240721_20240803_MaximumFloodExtent_PAK.shp & VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) |UNO SAT | HDX |

<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

```{hint} Folder structure
Keep your data management clean by creating a folder structure on your computer for your QGIS-projects and geodata. 
The exercise data should be saved in a location where you can easily find them and the corresponding QGIS-project
```


## Task 1: Gain an overview of the situation around Larkana 
```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
name: 
align: right
name: IFRC Surge Icon
---
```

You have been deployed as an information manager to the flood-affected regions of Pakistan. Upon your arrival you received reports from the operations team indicating that the city of [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) and its surrounding areas have been severely affected by the floods. The team needs a general overview of the location of the city.
 
1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the “project” folder of the exercise “Modul3_Exercise_2_Flood_Larkana”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “PAK_Larkana_flood_2024”.
3. First, we want to add the OpenStreetMap as a base map for orientation. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 

```{Tip}
You cannot interact with a base map!
```

4. Next, load the GeoPackage "PAK_adm2_Sindh.gpkg"in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to "PAK_adm2_Sindh.gpkg". Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


``` {Attention}
GeoPackage files can contain multiple files and even entire QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```
5. First, we want to export __Larkana District__ from __PAK_adm2_Sindh__ to have it as a stand-alone vector layer. To do that, 
    * Open the attribute table of __PAK_adm2_Sindh__ by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    * Find the row of Larkana and mark it by clicking on the number on the very left-hand side of the attribute table. The row will appear blue and the area of Larkana will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    To select the surrounding districts, click on the `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) icon in the QGIS Toolbar, hold the `Shift` button on your keyboard, and click on the districts either on the map or the attribute table ([Wiki Video](/content/Wiki/en_qgis_spatial_queries_wiki)).
    * After you are done selecting districts, click on the icon ![](/fig/selection_toolbar_feature_deselection.png) in thetoolbar to end the feature selection mode.
    * Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save Larkana as a GeoPackage, so adjust `Format` accordingly. Click on the three points and navigate to your `temp` folder. Here you can give it the layer the name __“Flood_2024_AOI”__ and click `Save`. Now you should see the same name in the `Layer name` field. Click `ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))

Now you have an overview of where the district of Larkana is located in Sindh. The operations team can use this information. 

## Task 2: Estimation of Flood Impact on the Health Sector in Larkana
```{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
name: 
align: right

name: IFRC HEalth Icon
---
```

Social media posts have hinted at a significant impact on the health system in the region. You have been tasked to find out as much as you can about the situation and, if feasible, to estimate the effects on the health system.

1. The first thing to do is to find out where the health facilities are located in the area. To that end, you do a quick search on HDX. You find the dataset [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities). This will do for now. 

    * Download the dataset directly from HDX and save it in your "input" folder or use the "PAK_Sind_Health_Facilities.gpkg" from the exercise data.
    *  Drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) the dataset into QGIS and save the project.
    * First, we must extract the health facilities in our area of interest. We will use the tool __"Extract by Location"__ to do that.
    * Open the `Processing Toolbox` ([here is how](/content/Wiki/en_qgis_interface_wiki.md#toolbox-toolbars)) and search for the tool.
        * As `Input Layer` we will use “PAK_Sind_Health_Facilities”.
        * For `By comparing to the features from` we use the layer “Flood_2024_AOI”.
        * As `Geometric predicate` we use `intersect`. 
        * To save the output click on the three points at `Extract (location)` -> `Save to GeoPackage` and navigate to your `temp` folder. Save the new layer under the name __“Flood_2024_AOI”__. Give the new layer the same `Layer name` and click `Run`.
    * Open the Attribute table of the new layer and have a look.
```{figure} /fig/PAK_extract_locatio_HS.png
---
width: 400px
name: Extract by location Pakistan
align: center
---
Extract by location Pakistan
```
Ok, now we have a good overview of the location of health facilities. We need much better information about the flooded area to identify the health facilities impacted by the flood. Fortunately, the UN has just shared a dataset about the extent of floods Satellite detected water extents from 08 to 12 August 2024 over Pakistan.

2. Load the dataset __"VIIRS_20240721_20240803_MaximumFloodExtent_PAK.shp"__ and __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ into your QGIS.
3. Once you have loaded the layers in QGIS, you can see that they are correctly displayed. However, upon checking the layer information, you can see that the new layers have a different Coordinate Reference System (CRS). They have the EPSG Code 9707 whereas our project has 4326 ([Wiki Video](/content/Wiki/en_qgis_projections_wiki.md#how-to-check-epsg-code-crs-of-layer-data)).
    * Right click on the data layer, click on  “Properties”.
    * The “Layer Properties” Window of the data layer will open. Click on “Information”.
    * Under the headline “Coordinate Reference System (CRS)” you find all information about the CRS. The most important are:
    - __Name:__     Here you find the EPSG Code
    - __Unites:__    Here you can find whether it is possible to use meters with this data layer or latitude and longitude. 
4. This will be a problem as soon as we do something different then just displaying the layers. Since we want to manipulate the layers in the next step we need to reproject them first ([Wiki Video](/content/Wiki/en_qgis_projections_wiki.md#changing-the-projection-of-a-vector-layer)). 
    * Click on the `Vector` Tab -> `Data Management Tools` -> `Reproject Layer` or search for the tool in the `Processing Toolbox `.
    * As `Input layer` select __"VIIRS_20240721_20240803_MaximumFloodExtent_PAK.shp"__
    * Select as target CRS/ EPSG-Code __4326__.
    * Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png) next to `Reprojected`, specify the file name as "Flood_extand_PAK_2024_Maximum_Flood_Extend_reprojected".
    * Click `Run`
    * Delete the old layer from the layer panel by right click on the layer -> `Remove layer`.
5. Repeat the process with __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ and name the result "Flood_extand_PAK_2024_Minimum_Flood_Extend_reprojected"

	 