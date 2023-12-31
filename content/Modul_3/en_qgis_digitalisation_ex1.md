# Digitization Exercise 1

## Aim of the exercise:

In this exercise, you will learn how to digitise the positions of settlements by creating new datasets. Furthermore, you will learn how to enrich the simple geodata set with additional information.

## Task
Our goal is to produce an overview of the impact of the 2022 flood in the state of Burco in Nigeria. To this end, we will visualize the state and the affected districts, plus we will digitize communities which are reportedly affected.

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created [save the project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#save project) in the “project” folder of the “Ex_Nigeria_flood”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Nigeria_Borno_flood_2022”.
3. Load the GeoPackage "kontur_boundaries_NG_20230628.gpkg" in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)]). Or click on `Layer`-> `Add Layer`-> `Add Vector Layer`. Click on the three points ![](/fig/Three_points.png) and navigate to "kontur_boundaries_NG_20230628.gpkg". Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
This dataset contains all administrative division areas (admin 0 to 5) with the respective population of the areas. 
``` {Attention}
GeoPackage file can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```
4. First, we want to export Borno state from kontur_boundaries_NG_20230628 to have it as a stand-alone vector layer. To do that, 
    * open the attribute table of "nga_admbnda_adm1_osgof_20190417" by right click on the layer nga_admbnda_adm1_osgof_20190417 -> `Open Attribute Table`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)).
    * Find the row of Borno state and mark it by clicking on the number on the very left-hand side of the attribute table. The row will appear blue and the area of Borno state will turn yellow on the map canvas. You can right-click on the row and click `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
.
    * Now right-click on the layer in the Layer Panel and click on `Export` -> `Save Selected Features as`. We want to save Borno as a GeoPackage, so adjust `Format` accordingly. Click on the three points and navigate to your `temp` folder. Here you can give it the layer the name “AOI_Borno_admin1” and click `Save`. Now you should see the same name in the `Layer name` field. Click `ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))
.
5. In the next steps, we want to create a vector layer with admin 2 areas or in Nigeria called Local Government Areas (LGA) with the population in our project. 
Since we only want the LGAs we need to export those from the original dataset. 
    * Load the GeoPackage file "kontur_boundaries_NG_20230628.gpkg" in the QGIS project. You can use one of the methods above. 
    ```{Note}
    GeoPackage file can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
    ```
    * Open the attribute table of the layer by by right click on the layer -> `Attribute Table` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)). Check out the attribute table. You see two columns of admin levels “admin levels” and “[osm_admin_levels](https://wiki.openstreetmap.org/wiki/Key:admin_level)”. Both have different values. In the [metadata](https://data.humdata.org/dataset/kontur-boundaries-nigeria) of the dataset on HDX we can find out that the column “osm_admin_levels” refers to the admin levels used in OpenStreetMaps (OSM). There is a [list](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#10_admin_level_values_for_specific_countries) of which official admin levels correspond to which OSM admin levels. The LGAs correspond to osm admin __level 6__. This means we want to export all features with `osm_admin_level` = `6`.
    * To export exactly these features we will use the tool `Extract by attribute`. Open the `Processing Toolbox` ([here is how](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#toolbox-toolbars)) and search for the tool.
    Open the tool and choose as `Input Layer` the “kontur_boundaries_NG_20230628.gpkg“ layer. Under `Selection attribute` choose the column `osm_admin_level`. The `Operator` has to `=` and as `value` we set `6` since the LGAs have the osm_admin_level 6. 
    * Under `Extracted (attribute)` click on the three points-> `Save to GeoPackage` navigate to your `temp` folder, and call the new layer “Nigeria_admin2_pop”. Click `Save`. Give the layer the same name ( “Nigeria_admin2_pop”). Click `OK` and then click `Run`.
6. Now we need to extract all LGAs in Borno. For that, we will use the Tool `Extract by Location` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_queries_wiki.html#select-by-expression))
. Search the tool in the `Processing Toolbox` and open it.
    * As `Input Layer` we will use “Nigeria_admin2_pop”.
    * For `By comparing to the features from` we use the layer “AOI_Borno_admin1”.
    * As `Geometric predicate` we use `are within`. 
    * To save the output click on the three points at `Extract (location)` -> `Save to GeoPackage`and navigate to your `temp` folder. Save the new layer under the name “Borno_admin2_pop”. Give the new layer the same `Layer name` and click `Run`.
    * Open the Attribute table of the new layer. You should have 27 features.
```{figure} /fig/en_qgis_extract_by_location_nigeria_flood.png
---
width: 600px
name: 
align: center
---
```
7. We have our admin areas in place and can now start to enrich these layer with additional data regarding the flood of 2022.
Open the Excel or pdf file “Nigeria_flood_2022_affacted_population” and open the sheet Borno. You find a table with the LGAs and communities which were affected by the flood. Now we want to add some of the information to our “Borno_admin2_pop” layer. For that, there are two ways. One simple but more time-consuming and one more complicated but much faster way. We will show here the easy we but in the dropdown below you find the tutorial for the advanced way as well.
    * Open the attribute table of “Borno_admin2_pop” and activate the editing mode by clicking on ![](/fig/mActionToggleEditing.png) ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#attribute-table-data-editing)). Now you are able to edit the data directly in the table.
    * First, we add a new column with the name “Flood_affacted”. To do so click on ![](/fig/mActionNewAttribute.png). In the `Add field` window you have to add the name and set the `Type` to `Text(string)`. Click `OK` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#add-new-column))
.
    * In the next step check in the Excel/PDF table which LGAs were affected and put “Yes” in the attribute table for those LGAs.
    * When you are down click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#attribute-table-data-editing)). 
8. To visualize the enriched data set, we use the function "Categorized Classification" function. This means that we select a column from the attribute table and use the content as categories to sort and display the data ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)).
    * Right-click on the layer “Borno_admin2_pop” in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menue. Open it and choose `Categorized`. Under `Value` select “Flood_affacted”.
    * Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affacted” column.  You can adjust the colours by double-clicking on one row in the central field. Once you are done, click `Apply` and `OK` to close the symbology window.
```{figure} /fig/en_qgis_categorized_classification_nigeria_flood_exercise.png
---
width: 600px
name: 
align: center
---
```
9. Next, we want to visualize the affected communities which are listed in the Nigeria_flood_2022_affacted_population table. To find these communities in QGIS we need two things. An OpenStreetMap base map and the plugin `OSM Place Search`. 
    * To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 
    Arrange your layer in the `Layer Panel` so the OSM is at the bottom ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html))
. 
    ```{Tip}
    You can not interact with a base map!
    ```
    * To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `OSM Place Search`. Once you have found it click on it and click `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html#installation-of-plugins)).
    * In the panel, you can search for places on the OpenStreetMap by typing the name of the place in the search bar. Often it makes sense to add additional information like the name of the country. Try for example “Laujeri Bulama, Nigeria”.
10. Now we have all our tools in place. In the next step, we create a new point vector layer from scratch to digitize the location of the affected communities. 
    * Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Borno_affected_communities_point”. Click `Save`.
    * `Geometry type`: Select `Point`
    - Under `Additional dimension` you should always make sure that you check `None`. 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column “Name”.
        * `Name` = “Name”
        * `Type`: Select `Text Data`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`
```{figure} /fig/en_qgis_create_point_layer_nigeria_flood_exercise.png
---
width: 600px
name: 
align: center
---
```
11. Currently the new “Borno_affected_communities_point” is empty. To add features we can use the `Digitizing Toolbar`. `. If you can not see the toolbar View` -> `Toolbars` and check Digitizing Toolbar` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 

    * Select the point layer “Borno_affected_communities_point” in the Layer panel. Go to the digitalisation toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode .
    * Search an affected community based on the table “Nigeria_flood_2022_affacted_population”. Once you have found one, click on ![](/fig/mActionCapturePoint.png). Left-click on the feature you want to digitalise.
    * Once you click, a window will appear ` Borno_affected_communities_point Feature Attribute`. Here you can add the name of the location.
    *Repeat the same process for as many communities as you like.
    * Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
    * Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.










    













