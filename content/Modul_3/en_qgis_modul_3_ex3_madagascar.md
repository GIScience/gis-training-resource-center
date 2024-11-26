# Exercise:  Sava Flood response
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
"The Government declared a national emergency situation, on 3 April, following the passage of the Tropical Cyclone (TS) Gamane, that hit the north and northeast of Madagascar on 27 March" [Madagascar: Tropical Cyclone Gamane Flash Update No. 2, 4 April 2024 (reliefweb)](https://reliefweb.int/report/madagascar/madagascar-tropical-cyclone-gamane-flash-update-no-2-4-april-2024). The following analysis will utilize actual data from this natural disaster. The objective is to pinpoint the specific medical centers and healthcare facilities that were impacted by the flooding. Additionally, we will assess the viability of road access to the populated places.
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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip
__Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip) and save the folder on your computer and unzip the file.__
:::

<!--:::{hint}
Reprojected and fixed Flood extend layer can be downloaded __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/______________.zip)__
:::-->

| Dataset name| Original title|Publisher|Download from| 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| mdg_admin1.shp | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-mdg) |UN OCHA| HDX |
| mdg_admin2.shp | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-mdg) |UN OCHA| HDX |
| hotosm_mdg_health_facilities.gpkg |  [Madagascar Health Facilities (OpenStreetMap Export)]([https://data.humdata.org/dataset/hotosm_pak_health_facilities](https://data.humdata.org/dataset/madagascar-healthsites)) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp | [Satellite detected water extent over Sambava and Vohemar Districts, Sava Region, Madagascar as of 01 April 2024]([[https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024))) |UNOSAT | HDX |
|roads_sava.gpkg | Roads Sava |Humanitarian OpenStreetMap Team | HOT Export Tool |


<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

```{hint} Folder structure

To keep your data organized and easily accessible, it's important to establish a clear folder structure on your computer for your QGIS projects and geodata. Ensure that your exercise data are saved in a location that allows for easy retrieval and association with the corresponding QGIS project.
```


## Task 1: Gain an overview of the situation around Sambava and Vehomar 

:::{card}
```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
name: 
align: right
name: IFRC Surge Icon
---
```
Context: 

You have been deployed as an information manager to the flood-affected regions of Madagascar. Upon your arrival you received reports from the operations team indicating that the distrcits [Sambava and Vohemar](https://www.openstreetmap.org/search?query=Sava%2C%20Madagascar#map=8/-14.374/49.795) of the region Sava are affected by the floods. The team needs a general overview of the affected locations.
:::
 
1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the “project” folder of the exercise “Modul3_Exercise_2_Flood_Larkana”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “MDG_Sava_flood_2024”.
3. First, we want to add the OpenStreetMap as a base map for orientation. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 

```{Tip}
You cannot interact with a base map!
```

4. Next, load the GeoPackage __"mdg_admin2.gpkg"__ in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to __"mdg_admin2.gpkg"__. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


``` {Attention}
GeoPackage files can contain multiple files and even entire QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```
5. First, we want to export the district __Sambava__ and the neighbouring district __Vohemar__ from __mdg_admin2__ to have it as a stand-alone vector layer. To do that: 
    * Open the attribute table of __mdg_admin2__ by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    * Find the row of Sambava in the column __ADM2_EN__ and mark it by clicking on the number on the very left-hand side of the attribute table. The row will appear blue and the area of Sambava will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    To select the Vohemar district, click on the `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) icon in the QGIS Toolbar, hold the `Shift` button on your keyboard, and click on the districts either on the map or the attribute table ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#manual-selection)).
    * After you are done selecting districts, click on the icon ![](/fig/qgis_move_symbol.png) to end the feature selection mode.
    * Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save the selected districts as a GeoPackage, so choose the `Format` option accordingly. Click on the three points and navigate to your `temp` folder. Here you can give it the layer the name __“Flood_2024_AOI”__ and click `Save`. Now you should see the same name in the `Layer name` field. Click `ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))
    * Click on the icon ![](/fig/selection_toolbar_feature_deselection.png) in the toolbar to end the feature selection.

:::{card}
Achievement:

Now you have an overview of where the districts Sambava and Vohemar in Sava are located. The operations team can use this information. 
:::

```{Tip}
Do not forget to save your project from time to time!
```

## Task 2: Estimation of Flood Impact on the Health Sector in Sambava and Vohemar

:::{card}
```{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
name: 
align: right

name: IFRC HEalth Icon
---
```
Context: 

Posts on social media have indicated a significant impact on the healthcare system in Madgascar. You have been tasked to find out as much as you can about the situation in Sava and, if feasible, to estimate the impact on the health system.
:::

1. The first thing to do is to find out where the health facilities are located in the area. To do that, you do a quick search on HDX. You find the dataset Madagascar Health Facilities (OpenStreetMap Export). This will do for now.

    * Load the GeoPackage __"hotosm_mdg_health_facilities.gpkg"__ in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to __"mdg_admin2.gpkg"__. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    * First, we must extract the health facilities in our area of interest. We will use the tool __"Extract by Location"__ to do that.
    * Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool.
        * As `Input Layer` we will use “hotosm_mdg_health_facilities”.
        * For `By comparing to the features from` we use the layer “Flood_2024_AOI”.
        * As `Geometric predicate` we use `intersect`. 
        * To save the output click on the three points at `Extract (location)` -> `Save to GeoPackage` and navigate to your `temp` folder. Save the new layer under the name __“Health_Facilities_Flood_2024_AOI”__. Give the new layer the same `Layer name` and click `Run`.
    * Open the Attribute table of the new layer and have a look.
```{figure} /fig/m3_ex6_qgis_task2_1.png
---
width: 400px
name: m3_ex6_qgis_task2_1
align: center
---
Extract by location 
```
Ok, now we have a good overview of the location of health facilities. We need much better information about the flooded area to identify the health facilities impacted by the flood. Fortunately, the UN has just shared a dataset about the extent of floods. Satellite detected water extent over Sambava and Vohemar Districts, Sava Region, Madagascar as of 01 April 2024 .

2. Load the dataset __"TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp"__ into your QGIS.
   * Adjust the opacity of the flood layer by right-clicking on layer __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab. Adjusted the opacity to around 60 % by moving the slider.
<!--3. Once you have loaded the layers in QGIS, you can see that they are correctly displayed. However, upon checking the layer information, you can see that the new layers have a different Coordinate Reference System (CRS). They have the EPSG Code 9707 whereas our project has 4326 ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * Right click on the data layer, click on  “Properties”.
    * The “Layer Properties” Window of the data layer will open. Click on “Information”.
    * Under the headline “Coordinate Reference System (CRS)” you find all information about the CRS. The most important are:
    - __Name:__     Here you find the EPSG Code.
    - __Unites:__    Here you can find whether it is possible to use meters with this data layer, degrees or latitude and longitude. 
4. This will be a problem as soon as we do something different then just displaying the layers. Since we want to manipulate the layers in the next step we need to reproject them first ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)). 
    * Click on the `Vector` tab -> `Data Management Tools` -> `Reproject Layer` or search for the tool in the `Processing Toolbox`.
    * As `Input layer` select __"TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp"__
    * Select as target CRS/ EPSG-Code __4326__.
    * Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png) next to `Reprojected`, specify the file name as __"2024_MinFloodExtend_reprojected"__.
    * Click `Run`
    * Delete the old layer from the layer panel by right click on the layer -> `Remove layer`.
    * Adjust the opacity of the flood layer by right-clicking on layer __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab. Adjusted the opacity to around 60 % by moving the   slider.-->

We have observed that certain health facilities are located within the flooded area. In order to visualise this information on the map, we plan to include a new attribute called __"affected"__ in the attribute table of __"Health_Facilities_Flood_2024_AOI"__.
To accomplish this, our first step will involve selecting all the affected health facilities. A new column containing this information is then appended to the __"Health_Facilities_Flood_2024_AOI"__ attribute table.

5. Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool __"Select by Location"__.
    * `Select features from` = __"Health_Facilities_Flood_2024_AOI"__.
    * As `Geometric predicate` we use `intersect`.
    * For `By comparing to the features from` we use the layer __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__.
    * `Modify current selection by` = `creating new selection`.
    *  Click `Run`.

:::{card}
Please note: Based on the original data, no actual health facilities were affected by the flood, but for the purposes of learning QGIS, we have placed three dummy health facilities within the flooded areas.
:::


```{figure} /fig/m3_ex6_qgis_task2_5.png
---
width: 400px
name: m3_ex6_qgis_task2_5
align: center
---
Select flood affected health facilities
```

```{warning}
In case you encounter the error:

> Feature (1) from “TDX_20240401_FloodExtent_SambavaDistrict_MDG” has invalid geometry. Please fix the geometry or change the Processing setting to the “Ignore invalid input features” option.
Execution failed after 0.07 seconds

You need to first use the tool __"Fix Geometry"__ before repeating the previously failed step 5 of using the tool __"Select by Location"__.

* To do so open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool __"Fix Geometries"__.
* `Input layer` = `TDX_20240401_FloodExtent_SambavaDistrict_MDG`
* Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png), specify the file name as __"TDX_20240401_FloodExtent_SambavaDistrict_MDG_fix"__.
*  Click `Run`.

```{figure} /fig/ m3_ex6_qgis_fix.png
---
width: 400px
name: m3_ex6_qgis_fix
align: center
---
Fix Geometry
```
6.  Open the attribute table of __"Health_Facilities_Flood_2024_AOI"__ by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)) and activate the editing mode by clicking on ![](/fig/mActionToggleEditing.png) ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Now you are able to edit the data directly in the table.
7. First, we add a new column with the name __“Flood_affected”__. To do so, click on ![](/fig/mActionNewAttribute.png). In the `Add field` window, you have to add the name and set the `Type` to `Text(string)`. Click `OK` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#add-new-column))


```{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column
align: center
---
Add new column
```
8. Now look for the `Show all Features` option in the lower left corner and click on it. Then, select the option `Show selected features` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). This will filter the table to display only the rows that represent the health facilities directly impacted by the flood.
Fortunately, no health facilities are directly affected by the flood.
9. If any were affected: Write `Yes` in the __"Flood_affected"__ column.
 * When you are done, click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
 * Click on the icon ![](/fig/selection_toolbar_feature_deselection.png) in the toolbar to end the feature selection.

* To visualise the enriched data set, we use the function "Categorized Classification" function. This means that we select a column from the attribute table and use the content as categories to sort and display the data ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)).
    * Right-click on the layer __"Health_Facilities_Flood_2024_AOI"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menu. Open it and choose `Categorized`. Under `Value` select “Flood_affected”.
    * Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affected” column.  You can adjust the colours by double-clicking on each colour in the central field. Once you are done, click `Apply` and `OK` to close the symbology window.

```{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Flood affected health facilities classification
```

:::{card} 
Achievement:
We've pinpointed that 3 health facilities have been inundated by the floods. 
:::

## Task 3: Logistical access

:::{card}

```{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
name: 
align: right

name: IFRC Logistics Icon
---
```
Context: 

The operations team is making plans to deliver much-needed supplies to the affected regions in Sambava and Vohemar.  Currently, there is uncertainty about how the supplies can be transported there. The operations team has asked for more information on this topic.
They need answers to the following three questions:

* Which roads leading into the affected regions are blocked, and at what specific locations are they blocked?
<!--* Are there any bridges that can be crossed from the eastern side of the Indus to the western side, and where are these bridges located?-->
* If transporting supplies by road into the region is not feasible, what alternative method could be used to deliver the supplies?


In order to get a clearer picture, we need to import the road network data for the region into QGIS. Look for the file in the input folder. The road network is initially displayed without showing any road types or other relevant details. We should apply a categorized classification technique only to display the specific roads that we are interested in.
:::

1. Load the dataset __"roads_sava.gpkg"__ from your input folder into your QGIS.
2. For categorized classification right-click on the layer __"roads_sava"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)).
    * On the top you find a dropdown menu. Open it and choose `Categorized`. Under `Value` select “highway”.
    * Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affacted” column.  You can adjust the colours by double-clicking on the coluors in each row in the central field.
    * Remove the tick from all categories except: `motorway`, `primary`, `secondary`, `trunk`
    ```{figure} /fig/m3_ex6_qgis_task3_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2
    align: center
    ---
    Road classification
    ```
    * You have the option to customize the width of the main roads' lines to improve the visualization. Open the Symbology window, then select `Symbol`. In the new window, you can adjust the width of the lines to your preference.
    

    ```{figure} /fig/m3_ex6_qgis_task3_2_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2_2
    align: center
    ---
    Road classification
    ```
    * Once you are done, click `Apply` and `OK` to close the symbology window.
3. To simplify the process, we will visually search for blocked roads and mark them with points. For this purpose, we will create an entirely new point dataset representing blocked roads.
    * Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name __“MDG_flood_2024_blocked_road”__. Click `Save`.
    - `Geometry type`: Select `Point`
    - Under `Additional dimension` you should always make sure that you check none of them.. 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: Select `Text (string)`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Create another field with the `name` __"Blocked_bridge"__ and the `Type`: Select `Text (string)`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`
    ```{figure} /fig/m3_ex6_qgis_Task3_3.png
    ---
    width: 400px
    name: m3_ex6_qgis_Task3_3
    align: center
    ---
    New layer blocked roads
    ```
4. Now you can create a point for each place where the flood layer covers the main roads leading through AOI [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-point-data). Currently the new layer __“MDG_flood_2024_blocked_road”__ is empty. To add features we can use the `Digitizing Toolbar`. If you cannot see the toolbar, click on the tab `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 
    * Activate the editing mode by clicking on ![](/fig/mActionToggleEditing.png). Activate then the option to add new points by clicking on ![](/fig/mActionCapturePoint.png).
    * Look out for places where the flood layer covers the main roads or bridges. Once you have found one, left-click on the location you want to digitise.
    * Once you click on a place, a window will appear. Indicate that the road is blocked by writing `Yes` in the field `Blocked_road`.
    * Repeat this step with all the locations your can find. 
   ```{figure} /fig/m3_ex6_qgis_task3_4.png
    ---
    width: 200px
    name: m3_ex6_qgis_task3_4
    align: center
    ---
    Digitalising blocked roads
    ```
    * Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
    * Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.
5. Now, we have mapped all roads in our AOI that are blocked by the flood. We can use icons instead of just points to display the layer __“MDG_flood_2024_blocked_road”__ to visualise this fact better [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_single_symbol_wiki.html).

    * Right-click on the layer __“MDG_flood_2024_blocked_road”__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * Keep the `Single Symbol` option. Select any symbol from the list that is appropriate for marking blocked roads (make sure the filter is set to `Favourites` or `All Symbols`.
    * Once you are done, click `Apply` and `OK` to close the symbology window.
    * After you are done, click on the icon ![](/fig/qgis_move_symbol.png) to end the feature selection mode.
    ```{figure} /fig/m3_ex6_qgis_task3_5.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_5
    align: center
    ---
    Visualising blocked roads with icons
    ```

:::{card}

The operations team has now all the information they need to plan their logistics. Good Job!
:::
