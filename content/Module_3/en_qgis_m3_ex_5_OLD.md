::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
:::{grid-item-card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_exercises.html
__Click here to return to the exercise overview page for module 3__ 
:::
::::

# Exercise 5: Larkana Flood response

:::{topic} Aim of the exercise

In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. The following analysis will utilize actual data from this natural disaster. The objective is to pinpoint the specific medical centers and healthcare facilities that were impacted by the flooding. Additionally, we will assess the viability of road access to the city of Larkana throughout the flood period.

Participants will work with multiple layers and conduct spatial queries. Additionally, they will learn how to create their own geodata. The exercise is divided into three tasks. In the first part, we will export the administrative boundaries in our area of interest (AOI). In the second task, the health facilities located in our AOI will be extracted and we will identify which health facilities are located inside the flood extent layer. In the third task, the road access will be determined by identifying which roads are potentially flooded. 
:::

::::{grid} 1

:::{grid-item-card}
__Competences covered in this exercise__
^^^ 

- Select features and export to new file
- Extract by Location
- Reproject Layer
- Editing the Attribute Table
- Classification
- Digitising a point Layer

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^

- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant wiki articles and module chapters__
^^^

* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Geodata Classification - Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)
* [Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
* [Digitisation- Point data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer)
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

## Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Modul_3_Exercise_4_Larkana_flood.zip

__Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Modul_3_Exercise_4_Larkana_flood.zip) and save the folder on your computer and unzip the file.__

:::


| Dataset | Original title | Publisher | Downloaded from | 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_Sindh_adm1.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sindh_adm2.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) |UNO SAT | HDX |
| Roads_Larkana.gpkg | [Roads Larkana](https://export.hotosm.org/v3/exports/7f1e78c7-f671-41e3-9ec3-6fc6ac31c929) |Humanitarian OpenStreetMap Team | HOT Export Tool (Export created in September 2024) |

<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint}

Reprojected and fixed Flood extend layer can be downloaded __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Module_3_Exercise_4_Larkana_flood_Day2.zip)__

:::

```{hint} Folder structure
To keep your data organized and easily accessible, it's important to establish a clear folder structure on your computer for your QGIS projects and geodata. Ensure that your exercise data are saved in a location that allows for easy retrieval and association with the corresponding QGIS project.
```

:::{figure} /fig/M3_Ex5_workflow_chart.drawio.png
---
name: M5_Ex5_Workflow_chart
width: 450 px
---
:::

## Task 1: Gain an overview of the situation around Larkana 

:::::{card} 
__Context__
^^^
```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

You have been deployed as an information manager to the flood-affected regions of Pakistan. Upon your arrival you received reports from the operations team indicating that the city of [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) and its surrounding areas have been severely affected by the floods. The team needs a general overview of the location of the city.

:::::


::::{margin}
```{admonition} Tip
:class: note
You cannot interact with a base map!
```
::::

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save) in the “project” folder of the exercise “Modul3_Exercise_2_Flood_Larkana”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “PAK_Larkana_flood_2024”.
3. First, we want to add the OpenStreetMap as a base map for orientation. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 
4. Next, load the GeoPackage __"PAK_Sindh_adm2.gpkg"__ in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to __"PAK_Sindh_adm2.gpkg"__. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


```{Attention}
GeoPackage files can contain multiple files and even entire QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```

5. First, we want to export __Larkana District__ and the neighbouring districts __Kambar Shahdad Kot__, __Shikarpur__  and __Sukkur__ from __PAK_adm2_Sindh__ to have it as a stand-alone vector layer. To do that: 
    * Open the attribute table of __PAK_adm2_Sindh__ by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    * Find the row of Larkana and mark it by clicking on the number on the very left-hand side of the attribute table. The row will appear blue and the area of Larkana will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    To select the surrounding districts, click on the `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) icon in the QGIS Toolbar, hold the `Shift` button on your keyboard, and click on the districts either on the map or the attribute table ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#manual-selection)).
    * After you are done selecting districts, click on the icon ![](/fig/qgis_move_symbol.png) to end the feature selection mode.
    * Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save the selected districts as a GeoPackage, so choose the `Format` option accordingly. Click on the three points and navigate to your `temp` folder. Here you can give it the layer the name __“Flood_2024_AOI”__ and click `Save`. Now you should see the same name in the `Layer name` field. Click `ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))
    * Click on the icon ![](/fig/selection_toolbar_feature_deselection.png) in the toolbar to end the feature selection.

:::{topic} Achievement

Now you have an overview of where the district of Larkana is located in Sindh. The operations team can use this information. 

:::

::::{margin}
```{Tip}
Do not forget to save your project from time to time!
```
::::

## Task 2: Estimation of Flood Impact on the Health Sector in Larkana

::::{topic} Context

```{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
```

Posts on social media have indicated a significant impact on the healthcare system in the region. You have been tasked to find out as much as you can about the situation and, if feasible, to estimate the impact on the health system.

::::

1. The first thing to do is to find out where the health facilities are located in the area. To do that, you do a quick search on HDX. You find the dataset Pakistan Health Facilities (OpenStreetMap Export). This will do for now.

    * Load the GeoPackage __"PAK_Health_Facilities_complete.gpkg"__ in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to __"PAK_Sindh_adm2.gpkg"__. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    * First, we must extract the health facilities in our area of interest. We will use the tool __"Extract by Location"__ to do that.
    * Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool.
        * As `Input Layer` we will use “PAK_Health_Facilities_complete”.
        * For `By comparing to the features from` we use the layer “Flood_2024_AOI”.
        * As `Geometric predicate` we use `intersect`. 
        * To save the output click on the three points at `Extract (location)` -> `Save to GeoPackage` and navigate to your `temp` folder. Save the new layer under the name __“Health_Facilities_Flood_2024_AOI”__. Give the new layer the same `Layer name` and click `Run`.
    * Open the Attribute table of the new layer and have a look.

    * First, we must extract the health facilities in our area of interest. We will use the tool __"Extract by Location"__ to do that.
    * Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool.
        * As `Input Layer` we will use “PAK_Health_Facilities_complete”.
        * For `By comparing to the features from` we use the layer “Flood_2024_AOI”.
        * As `Geometric predicate` we use `intersect`. 
        * To save the output click on the three points at `Extract (location)` -> `Save to GeoPackage` and navigate to your `temp` folder. Save the new layer under the name __“Health_Facilities_Flood_2024_AOI”__. Give the new layer the same `Layer name` and click `Run`.
    * Open the Attribute table of the new layer and have a look.

```{figure} /fig/PAK_extract_locatio_HS.png
---
width: 400px
name: Extract by location Pakistan
align: center
---
Extract by location Pakistan
```

Ok, now we have a good overview of the location of health facilities. We need much better information about the flooded area to identify the health facilities impacted by the flood. Fortunately, the UN has just shared a dataset about the extent of floods. Satellite detected water extents from 08 to 12 August 2024 over Pakistan.

2. Load the dataset __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ into your QGIS.
3. Once you have loaded the layers in QGIS, you can see that they are correctly displayed. However, upon checking the layer information, you can see that the new layers have a different Coordinate Reference System (CRS). They have the EPSG Code 9707 whereas our project has 4326 ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * Right click on the data layer, click on  “Properties”.
    * The “Layer Properties” Window of the data layer will open. Click on “Information”.
    * Under the headline “Coordinate Reference System (CRS)” you find all information about the CRS. The most important are:
    - __Name:__     Here you find the EPSG Code.
    - __Unites:__    Here you can find whether it is possible to use meters with this data layer, degrees or latitude and longitude. <!--ADD: Why is it a problem? Add explanation-->
4. This will be a problem as soon as we do something different then just displaying the layers. Since we want to manipulate the layers in the next step we need to reproject them first ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)). 
    * Click on the `Vector` tab -> `Data Management Tools` -> `Reproject Layer` or search for the tool in the `Processing Toolbox`.
    * As `Input layer` select __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__
    * Select as target CRS/ EPSG-Code __4326__.
    * Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png) next to `Reprojected`, specify the file name as __"2024_MinFloodExtend_reprojected"__.
    * Click `Run`
    * Delete the old layer from the layer panel by right click on the layer -> `Remove layer`.
    * Adjust the opacity of the flood layer by right-clicking on layer __"2024_MinFloodExtend_reprojected"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab. Adjusted the opacity to around 60 % by moving the slider.

We have observed that certain health facilities have been impacted by the flood. In order to visualise this information on the map, we plan to include a new attribute called __"affected"__ in the attribute table of __"Health_Facilities_Flood_2024_AOI"__.
To accomplish this, our first step will involve selecting all the affected health facilities. A new column containing this information is then appended to the __"Health_Facilities_Flood_2024_AOI"__ attribute table.

5. Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox)) and search for the tool __"Select by Location"__.
    * `Select features from` = __"Health_Facilities_Flood_2024_AOI"__.
    * As `Geometric predicate` we use `intersect`.
    * For `By comparing to the features from` we use the layer __"2024_MinFloodExtent_reprojected"__.
    * `Modify current selection by` = `creating new selection`.
    *  Click `Run`.

```{figure} /fig/PAK_flood_select_by_location.PNG
---
width: 400px
name: Select flood affected health facilities
align: center
---
Select flood affected health facilities
```

::::{admonition} Possible Error Message
:class: warning, dropdown
In case you encounter the error:

> Feature (1) from “2024_MinFloodExtend_reprojected” has invalid geometry. Please fix the geometry or change the Processing setting to the “Ignore invalid input features” option.
Execution failed after 0.07 seconds

You need to first use the tool __"Fix Geometry"__ before repeating the previously failed step 5 of using the tool __"Select by Location"__.

* To do so open the [`Processing Toolbox`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#open-toolbox) and search for the tool __"Fix Geometries"__.
* `Input layer` = `2024_MinFloodExtend_reprojected`
* Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png), specify the file name as __"2024_MinFloodExtend_reprojected_fix"__.
*  Click `Run`.

```{figure} /fig/ PAK_flood_ngeomertrie_error.PNG
---
width: 400px
name: Fix Geometry
align: center
---
The error message indicating invalid geometries
```

::::

6.  Open the attribute table of __"Health_Facilities_Flood_2024_AOI"__ by right click on the layer  -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)) and activate the editing mode by clicking on ![](/fig/mActionToggleEditing.png) ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Now you are able to edit the data directly in the table.

7. First, we add a new column with the name __“Flood_affected”__. To do so, click on ![](/fig/mActionNewAttribute.png). In the `Add field` window, you have to add the name and set the `Type` to `Text(string)`. Click `OK` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#add-new-column))

```{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column Pakistan
align: center
---
Add new column
```

8. Now look for the `Show all Features` option in the lower left corner and click on it. Then, select the option `Show selected features` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). This will filter the table to display only the rows that represent the health facilities directly impacted by the flood.
Now, you can write `Yes` in the __"Flood_affected"__ column.
 * When you are done, click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
 * Click on the icon ![](/fig/selection_toolbar_feature_deselection.png) in the toolbar to end the feature selection.

9. To visualise the enriched data set, we use the function "Categorized Classification" function. This means that we select a column from the attribute table and use the content as categories to sort and display the data ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)).
    * Right-click on the layer __"Health_Facilities_Flood_2024_AOI"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menu. Open it and choose `Categorized`. Under `Value` select “Flood_affacted”.
    * Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affacted” column.  You can adjust the colours by double-clicking on each colour in the central field. Once you are done, click `Apply` and `OK` to close the symbology window.

```{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Flood affected health facilities classification
```

:::{card} 
__Achievement:__
^^^

We've pinpointed the specific health facilities that have been inundated by the floods. Our findings indicate that a total of four facilities have been completely flooded and are currently non-operational. Considering we assessed the minimum flood impact, it's highly probable that more health facilities will also be impacted. This data is crucial for our operational team as it will enable them to strategize and execute an effective response.

:::

## Task 3: Logistical access to Larkana City

::::{topic} Context

```{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
name: 
align: right

name: IFRC Logistics Icon
---
```

The operations team is making plans to deliver much-needed supplies to the affected region around Larkana. Currently, there is uncertainty about how the supplies can be transported there. The operations team has asked for more information on this topic.

They need answers to the following three questions:
* Which roads leading into Larkana are blocked, and at what specific locations are they blocked?
* Are there any bridges that can be crossed from the eastern side of the Indus to the western side, and where are these bridges located?
* If transporting supplies by road into the region is not feasible, what alternative method could be used to deliver the supplies?

In order to get a clearer picture, we need to import the road network data for the region into QGIS. Look for the file in the input folder. The road network is initially displayed without showing any road types or other relevant details. We should apply a categorized classification technique only to display the specific roads that we are interested in.
::::

1. Load the dataset __"Roads_Larkana.gpkg"__ from your input folder into your QGIS.
2. For categorized classification right-click on the layer __"Roads_Larkana"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)).
    * On the top you find a dropdown menu. Open it and choose `Categorized`. Under `Value` select "highway".
    * Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected "highway" column.  You can adjust the colours by double-clicking on the colours in each row in the central field.
    * Remove the tick from all categories except: `motorway`, `primary`, `secondary`, `trunk`
    ```{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    The symbolisation window for the Roads_Larkana.gpkg layer.
    ```
    * You have the option to customize the width of the main roads' lines to improve the visualization. Open the Symbology window, then select `Symbol`. In the new window, you can adjust the width of the lines to your preference.
    
    ```{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Adjusting the symbolisation of the different road types
    ```

    * Once you are done, click `Apply` and `OK` to close the symbology window.

::::{margin}
:::{tip}

There are methods to automate the digitisation process which will be covered in [module 5: Intermediate GIS Operations](https://giscience.github.io/gis-training-resource-center/content/Module_5/en_module_5_overview.html)
:::
::::

3. To simplify the process, we will visually search for blocked roads and mark them with points. For this purpose, we will create an entirely new point dataset representing blocked roads.
    * Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name __“PAK_flood_2024_blocked_road”__. Click `Save`.
    - `Geometry type`: Select `Point`
    - Under `Additional dimension` you should always make sure that you check `None`. 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: Select `Text Data`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Create another field with the `name` __"Blocked_bridge"__ and the `Type`: Select `Text Data`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`

    ```{figure} /fig/PAK_blocked_road_new_layer.png
    ---
    width: 400px
    name: Pakistan road classification
    align: center
    ---
    Creating a new point layer. Make sure to specify a location using the three points at the top.
    ```

::::{margin}
:::{tip}
If you cannot see the toolbar, click on the tab `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md#creation-of-point-data))
:::
::::

4. Now you can create a point for each place where the flood layer covers the main roads leading out of Larkana [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-point-data). 
    * Currently the new layer __“PAK_flood_2024_blocked_road”__ is empty. To add features we can use the `Digitizing Toolbar`.  ![](/fig/Digitizing_Toolbar.png) 
    * Activate the editing mode by clicking on ![](/fig/mActionToggleEditing.png). Next, activate the option to add new points by clicking on ![](/fig/mActionCapturePoint.png) `Add Point Feature` .
    * Look out for places where the flood layer covers the main roads or bridges leading out of Larkana. Once you have found one, left-click on the location you want to digitise.
    * Once you click on a place, a window will appear. Indicate that the road is blocked by writing `Yes` in the field `Blocked_road`.
    * Repeat this step with all the locations your can find. 

    ```{figure} /fig/PAK_blocked_road_digitalise.png
    ---
    width: 400px
    name: Digitalising blocked roads
    align: center
    ---
    This pop-up will open once you have selected a location to add a point. Make sure to enter the relevant information in the columns. 
    ```

    * Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
    * Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

5. Now, we have mapped all blocked main access roads into Larkana. We can use icons instead of just points to display the layer __“PAK_flood_2024_blocked_road”__ to visualise this fact better [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_single_symbol_wiki.html).

    * Right-click on the layer __“PAK_flood_2024_blocked_road”__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * Keep the `Single Symbol` option. Select any symbol from the list that is appropriate for marking blocked roads. 
    * Once you are done, click `Apply` and `OK` to close the symbology window.
    * After you are done, click on the icon ![](/fig/qgis_move_symbol.png) to end the feature selection mode.

    ```{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visulsing blocked roads with icons
    align: center
    ---
    Adjusting the symbolisation for the new point layer. Make sure to choose a marker that can be easily identified. 
    ```

Part of your assignment was to point out possible alternatives to road transport. Can you identify any?

:::{dropdown} __Answer__

In the south-west of Larkan City, you can find the [Mohenjodaro Airport](https://www.google.com/search?q=Larkana&rlz=1C1GCEA_enDE1048DE1048&oq=Larkana&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORjjAhiABDIHCAEQLhiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIGCAYQRRg9MgYIBxBFGD2oAgiwAgE&sourceid=chrome&ie=UTF-8#vhid=0x0:0xf59fc8243b2b9d0e&vssid=lclsmap&eim=CAEQDhoRMjcuMzI4NDM3NTc5NDIyNjIiETY4LjE0MjA5NTk3MDUzNTQ4KhQxNzY5OTA4NTExODUyNjQzMDQ3OA). Currently, the road from Larkana City to the airport appears to be open and accessible. This means that essential supplies could potentially be transported from the airport into the city without encountering any roadblocks. 

```{figure} /fig/PAK_road_access_airport.png
---
width: 600px
name: Road access to Mohenjodaro Airport
align: center
---
Road access to Mohenjodaro Airport
```
:::

:::{card} 

The operations team has now all the information they need to plan their logistics. Good Job!

:::


:::{admonition} Continue along this exercise track
:class: note

```{figure} /fig/IFRC-icons-colour_Map.png
---
width: 100px
align: right
name: IFRC map icon
---
```

This exercise is part of the __Larkana Flood Response Exercise track__ and continues with an exercise in module 4.

Click [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I_ex4.html) if you want to continue to the next exercise of this exercise track.

:::
