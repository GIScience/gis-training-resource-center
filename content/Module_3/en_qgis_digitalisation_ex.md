::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercise 1 (Digitisation): Access to financial institutions 

## Characteristics of the exercise

::::{grid} 2
:::{grid-item-card}
__Aim of the exercise:__
^^^

In this exercise, you will learn how to digitise points, lines, and polygons of features in settlements by creating new datasets. 

__Type of trainings exercise:__

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__These skills are relevant for:__
^^^ 

- Data collection and digitisation
- Fixing spatial information

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 2 hour to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant Wiki articles:__
^^^

* [QGIS Interface](/content/Wiki/en_qgis_interface_wiki.md)
* [Types of Geodata](/content/Wiki/en_qgis_geodata_types_wiki.md)
* [Digitization](/content/Wiki/en_qgis_digitalization_wiki.md)
* [Basemaps](/content/Wiki/en_qgis_basemaps_wiki.md)

:::

::::

## Instructions for the trainers

:::{admonition} A note on plugins
class: attention

This exercise makes use of a plugin which is not installed by default: `OSM Place Search`
Make sure you take a little bit of time to explain the role of plugins in QGIS and how to install them in QGIS.
Furthermore, instead of using XYZ-tiles for the basemap, you can decide to use the plugin __"QuickMapServices"__. 

:::

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.mdhow-to-do-trainings) for some general tips on how to conduct a training.

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


```{Attention}
Try to always use the standard folder structure. You can find a template __[here](/content/Wiki/en_qgis_projects_folder_structure_wiki.mf#standard-folder-structure)__.
```

## Background: Cash crunch in Abuja

In 2022 there was a cash shortage in Nigeria. Small businesses heavily rely on cash transactions and cash-based services. This lead to a cash crunch in Abuja, the capital city of Nigeria. [No cash article in Abuja](https://businessday.ng/news/article/business-groan-as-cash-crunch-hits-banks-in-abuja/). 

## Task: Map the banks

Our goal is to create a point layers at the three Banks close to each other in the Central Business District (CBD) of Abuja in Nigeria. This is to let people easily identify the banks in the CBD of Abuja for their transaction purposes. 

To this end, we will visualize the digitization of the First Bank, Bank of Industry Building, and Zenith Bank Abuja. 

### Add a basemap

1.  Add the OSM as a base map. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 
Arrange your layer in the `Layer Panel` so the OSM is at the bottom ([Wiki Video](/content/Wiki/en_qgis_basemaps_wiki.md))

```{Tip}
You cannot interact with a base map!
```

2. To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `OSM Place Search`. Once you have found it, click on it and click `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](/content/Wiki/en_qgis_plugins_wiki.md)).
3. In the `OSM place search` panel, search "Abuja Central Business District" and choose Abuja Municipality Area Council, City. Zoom to the Central Business District. We want to digitise the location of banks in this region. 
For this, we will need to create a new point layer: 
    1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder in your project folder. Give the new dataset the name “Abuja_bank_point”. Click `Save`.
    - Under `Geometry type`: Select `Point` 
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
    - Under `New Field` you can add columns to the new layer. Add the column “Name”.
        * `Name` = “Name”
        * `Type`: Select `Text (string)`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
    * Your new layer will appear in the `Layer Panel`


```{admonition} Adding more information
class: tip

You can digitise even more information by adding more columns. For example, you can add a column for `amenity` to indicate the type of amenity (bank). Try thinking about what kind of data you can add. 

```

```{figure} /fig/new_layer_abuja.png
---
height: 400px
name: New point layer Abuja
align: center
---
Create new point layer.
```

4. Now you can create a point for each of the three banks in the area [wiki](/content/Wiki/en_qgis_digitalization_wiki.md#add-geometries-to-a-layer). Currently the new “Abuja_bank_point” is empty. To add features we can use the `Digitizing Toolbar`. If you cannot see the toolbar `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 
    1. Select the point layer “Abuja_bank_point” in the Layer panel. Navigate to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). Now, the layer is in the editing mode.
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

## Map road blocks

There is some reliable information that there is a roadblock due to construction at the junction of "Independent Avenue" and '"Tafawa Balewa Way". To visualise this on our map we want to create a polygon of this roadblock.  The Polygon should cover the entire junction.

1. To do that we need again a new layer. In this case a polygon layer. The creation is basically the same as for the point.
        1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki](/content/Wiki/en_qgis_digitalization_wiki.md)) 
    1. Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Abuja_roadbloc_polygon”. Click `Save`.
    2. `Geometry type`: Select `Polygon`
    4. Select the coordinate reference system (CRS) "EPSG:4326-WGS 84".
    5. Under `New Field` you can add columns to the new layer. Add the column “Roadblock_type”.
        * `Name` = “Roadblock_type”
        * `Type`: Select `Text (string)`
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.

    6. Your new layer will appear in the `Layer Panel`
2. To digitise this area, click on your new „Abuja_roadbloc_polygon“ layer ([Wiki](/content/Wiki/en_qgis_digitalization_wiki.md)). 
    - Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode` and Add Feature: `Capture Polygone`![](/fig/mActionCapturePolygon.png)|. 
    - Draw geometries and enter `feature attributes`, "Roadblock_type" = "Construction_site".
    - Save edits ![](/fig/mActionSaveEdits.png) , exit `edit mode`. 

    
## Map the connection routes

A business man drove all the way from the North of Herbert Macauley Way in the Central Business District of Abuja to do transaction at the Bank of Industry on Monday morning. Unfortunately, he found that the network server of the bank is down and needed to proceed to the Zenith Bank as the only functioning Bank. He later discovered that there is a road blocked at the junction of independence avenue and Tafawa Balewa way due to road construction. 

Create a road line layer that will allow him to get to Zenith Bank easily.

1. To do that we need again a new layer. In this case a line layer. The creation of that is nearly the same as for the point.
        1. Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki](/content/Wiki/en_qgis_digitalization_wiki.md)) 
    - Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name “Abuja_bank_road_connection_line”. Click `Save`.
    - `Geometry type`: Select `Line`.
    - Select the coordinate reference system (CRS) "EPSG:4326-WGS 84".
    - Under `New Field` you can add columns to the new layer. Add the column “Road_type”.
        * `Name` = “Road_type”
        * Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
        * Click `OK`.
            ```{admonition} Adding more information
            class: tip

            Again, by adding more fields, you can add more information. For example, you can add the type of road (e.g., paved, unpaved, highway, residential) or the speed limit, or the number of lanes. Try thinking about what information you could add, and which `Type` would you use? Keep in mind that you cannot perform calculations with string data.

            ```
    * Your new layer will appear in the `Layer Panel`
2. Select the line layer “Abuja_bank_road_connection_line” to add data to in the Layer panel [Wiki](/content/Wiki/en_qgis_digitalization_wiki.md). 
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


