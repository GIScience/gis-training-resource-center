# Digitization Exercise 1: Access to financial institutions 

## Aim of the exercise:

In this exercise, you will learn how to digitise points, lines, and polygons of features in settlements by creating new datasets. 

```{Attention}
Try to always use the standard folder structure. You can find a template [__here__](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure).
```

### Relevant Wiki Articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Digitization](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html)
* [Basemaps](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html)


## Background: Cash crunch in Abuja
In 2022 there was a cash shortage in Nigeria. Small businesses heavily rely on cash transactions and cash-based services. This lead to a cash crunch in Abuja, the capital city of Nigeria. [No cash article in Abuja](https://businessday.ng/news/article/business-groan-as-cash-crunch-hits-banks-in-abuja/). 

## Task: Map the banks

Our goal is to create a point layers at the three Banks close to each other in the Central Business District (CBD) of Abuja in Nigeria. This is to let people easily identify the banks in the CBD of Abuja for their transaction purposes. 

To this end, we will visualize the digitization of the First Bank, Bank of Industrie Building, and Zenith Bank Abuja. 

1.  Add the OSM as a base map. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 
Arrange your layer in the `Layer Panel` so the OSM is at the bottom ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html))

```{Tip}
You cannot interact with a base map!
```
2. To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `OSM Place Search`. Once you have found it, click on it and click `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html#installation-of-plugins)).
3. In the panel, search "Abuja Central Business Distric" via the OSM Place Search in QGIS and choose Abuja Municipality Area Council, City. Zoom to the Central Business District. Here we want to digitise the location of banks. But first we need to create a new point layer.  
To do that:
    1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Abuja_bank_point”. Click `Save`.
    - `Geometry type`: Select `Point`
    - Under `Additional dimension` you should always make sure that you check `None`. 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column “Name”.
        * `Name` = “Name”
        * `Type`: Select `Text Data`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`
```{figure} /fig/new_layer_abuja.png

---
height: 400px
name: New point layer Abuja
align: center
---
Create new point layer.
```

4. Now you can create a point for each of the three banks in the area [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer). Currently the new “Abuja_bank_point” is empty. To add features we can use the `Digitizing Toolbar`. If you cannot see the toolbar `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 
    1. Select the point layer “Abuja_bank_point” in the Layer panel. Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). Now the layer is in the editing mode .
    2. Search for banks on the map or use the OSMPlace search panel. Once you have found one, click on ![](/fig/mActionCapturePoint.png). Left-click on the feature you want to digitalize.
    3. Once you click, a window will appear "Abuja_bank_point". Here you can add the name of the bank.
    4. Repeat the same process for as many banks as you can find.
    5. Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
    6. Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

This is what your result should look like. ![](/fig/Abuja_Banks_Point_Layers.png)

```{figure} /fig/Abuja_Banks_Point_Layers.png

---
height: 200px
name: Result Digitalization exercise
align: center
---
Result Digitalization exercise.
```

## Map road blocs

There is some reliable information that there is a roadblock due to construction at the junction of "Independent Avenue" and '"Tafawa Balewa Way". To visualise this on our map we want to create a polygon of this roadblock.  The Polygon should cover the entire junction.

1. To do that we need again a new layer. In this case a polygon layer. The creation is basically the same as for the point.
        1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    1. Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Abuja_roadbloc_polygon”. Click `Save`.
    2. `Geometry type`: Select `Polygon`
    3. Under `Additional dimension` you should always make sure that you check `None`. 
    4. Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
    5. Under `New Field` you can add columns to the new layer. Add the column “Roadblock_type”.
        * `Name` = “Roadblock_type”
        * `Type`: Select `Text Data`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
    6. Your new layer will appear in the `Layer Panel`
2. To digitise this area, click on your new „Abuja_roadbloc_polygon“ layer ([Wiki Video](file:///C:/HeiGIT/RCRC_GIS_Training/gis-training-resource-center/_build/html/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-polygon-data)). 
    - Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode` and Add Feature: `Capture Polygone`![](/fig/mActionCapturePolygon.png)|. 
    - Draw geometries and enter `feature attributes`, "Roadblock_type" = "Construction_site".
    - Save edits ![](/fig/mActionSaveEdits.png) , exit `edit mode`. 

## Map the connection routes
A business man drove all the way from the North of Herbert Macauley Way in the Central Business Distric of Abuja to do transaction at the Bank of Indusrie on Monday morning. Unfortunately, he found that the network server of the bank is down and needed to proceed to the Zenith Bank as the only functioning Bank. He later discovered that there is a road blocked at the junction of Indepence avenue and Tafawa Balewa way due to road construction. 

Create a road line layer that will allow him to get to Zenith Bank easily.

1. To do that we need again a new layer. In this case a line layer. The creation of that is nearly the same as for the point.
        1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#create-a-new-layer)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Abuja_bank_road_connection_line”. Click `Save`.
    - `Geometry type`: Select `Line`
    - Under `Additional dimension` you should always make sure that you check `None`. 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column “Road_typ”.
        * `Name` = “Road_typ”
        * `Type`: Select `Text Data`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`
2. Select the line layer “Abuja_bank_road_connection_line” to add data to in the Layer panel [Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-line-data). 
    1. Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). Now the layer is in the editing mode.
    2.	Click on ![](/fig/mActionCaptureLine.png). 
    3.	To digitalise line features, click along the line. When you are done, right-click on the last point of the line to finish the feature.
    4.	Once you click, a window will appear "Abuja_bank_road_connection_line- Feature Attribute". Add the road typ which is "Secondary_road" 
    5.	Once you are done with digitalization, click on ![](/fig/mActionSaveEdits.png) to save your edits.
    6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

```{figure} /fig/Abuja_Banks_final.png
---
height: 400px
name: Abuja final
align: center
---
Exercise result example.
```


