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
#### Focus group (GIS-Knowlege Level)
- QGIS Beginners
- The skills tested in this exercise are necessary for all GIS-users.
#### These skills are relevant for 
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
| PPAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
|  VIIRS_20240721_20240803_MaximumFloodExtent_PAK.shp & VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) |UNO SAT | HDX |


```{hint} Folder structure
Keep your data management clean by creating a folder structure on your computer for your QGIS-projects and geodata. 
The exercise data should be saved in a location where you can easily find them and the corresponding QGIS-project
```


## Task 1: Gain an overview of the situation around Larkana

You have been deployed as an information manager to the flood-affected regions of Pakistan. Upon your arrival you received reports from the operations team indicating that the city of [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) and its surrounding areas have been severely affected by the floods. The team needs a general overview of the location of the city.
 
1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the “project” folder of the exercise “Modul3_Exercise_2_Flood_Larkana”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “PAK_Larkana_flood_2024”.
3. First, we want to add the OpenStreetMap as a base map for orientation. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 

```{Tip}
You cannot interact with a base map!
```
4. Next, load the GeoPackage "PAK_adm2_Sindh.gpkg" in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to "PAK_adm2_Sindh.gpkg". Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
This dataset contains all administrative division areas (admin 0 to 5) with the respective population of the areas. 
``` {Attention}
GeoPackage files can contain multiple files and even entire QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```


## Task 2: 

Social media posts have also hinted at a significant impact on the health system in the region. You have been tasked to find out as much as you can about the situation and, if feasible, to estimate the effects on the health system.

