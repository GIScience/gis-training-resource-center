::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercise: OpenStreetMap data export

:::{card}
__Aim of the exercise:__
^^^

This exercise aims to show two ways how to get [OpenStreetMap (OSM)](https://www.openstreetmap.org) as a vector 
file into QGIS. We will use the [HOT Export Tool](https://export.hotosm.org/v3/) to download specific data from Open

:::

::::{grid} 2
:::{grid-item-card}
__Larkana Flood Response Exercise Track__

This exercise is part of the [Larkana Flood Response Exercise Track](https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/en_larkana_flood_response.html)

:::

:::{grid-item-card}
__Competences covered in this exercise__
^^^ 
- Export OSM data using the HOT Export Tool.
- Importing files into a QGIS project.
- Adjusting the symbology of a layer.

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^

- The exercise takes around 45 hours to complete and discuss, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant wiki articles__
^^^

* [QGIS Interface](/content/Wiki/en_qgis_interface_wiki.md)
* [Types of Geodata](/content/Wiki/en_qgis_geodata_types_wiki.md)
* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Layer Concept](/content/Wiki/en_qgis_layer_concept_wiki.md)
* [Geodata Classification - Graduated](/content/Wiki/en_qgis_graduated_wiki.md)

:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip

Since the exercise is about finding data, there won't be any data to download. 
Instead download the __standard folder structure__ [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) and save your data into the `data/input`-folder as you download it.

:::

## Tasks

OpenStreetMap (OSM) is a collaborative, open-source project that creates free, editable maps of the world, built by a global community of mappers. There are multiple different ways how to download or export data from OpenStreetMap (OSM), each with it's own advantage. In this exercise, we will go over the [HOT Export Tool](https://export.hotosm.org/v3/). [At the bottom of this exercise](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_data_sources_ex4.html#alternative-tools), you can find a list of alternative tools.

### Using the HOT Export Tool

The [HOT Export Tool](https://export.hotosm.org/v3/) 
is a tool for accessing OSM data offered by Humanitarian OpenStreetMap Team (HOT).
HOT offers a browser-based tool to download OSM data with good options to specify 
region, time, feature type and data format. 
For our following analysis, we want to export the road network for the Larkana district in Pakistan. 


1. Go to the HOT Export tool. To use the tool you need an OSM account. If you 
   don't have an account yet, you will need to create one. Click on `Log in`. In the new window 
   select the option to create a new account. 
2. If you have an OSM account, you can log in directly into the HOT Export tool by 
   clicking on `Log in`.
3. Now we can start creating an OSM export. To do so, click on `Start Exporting`. You will be directed to the export tool.

:::{figure} /fig/en_m2_ex4_HOT_Export_Tool1.png
---
name: HOT_Export_Tool_1
width: 750 pc
---

:::

In the export tool, you have a map canvas on the right and an input area on the left. On the map canvas, you determine the geographic location of the data you want to export. On the left side you determine the metadata of the export, the file format, and select which data will be downloaded (e.g., buildings, roads, hospitals, settlements, etc.)

4. On the left side, give your Export a name such as `Larkana Roads export 20250314` and add a short description of what you are intending to download. In our case, we want to download the road network for Larkana in Pakistan. You can enter a project if you wish (e.g. GIS Training). 

::::{margin}
:::{tip}
There are two entries for Larkana in OpenStreetMap. One refers to the city, and the other to the district. Our area of interest is the __district__. We can choose the entry that has a larger box. 
Alternatively, once you zoomed into the area, you can draw a box or a polygon to select the area. 
:::
::::

5. On the map canvas, search for Larkana in the search bar and select the district. The map will zoom in to show the district. This will also select the district as our area of interest. You can see this by the blue polygon. Our export will only download data that is located within this area.

:::{figure} /fig/Module_2/en_m2_ex_4_HOT_Export_Tool3.png
---
name: HOT_Export_3
width: 500 px
---


6. Click `Next`.

7. Select the format you want to download. We recommend using GeoPackage `.gpkg` but GeoJSON and Shapefile are also fine. Click `Next`.

8. Under the data tab, we can select the key values we are interested in. We want to download to download the road network so we have to open the dropdown under `Transportation` and check the box for `Roads`

:::{figure} /fig/Module_2/en_m2_ex4_HOT_export_tool4.png
---
name: Hot Export Tool 5
width: 500 px
---
:::

9. We are done adjusting the export. Click `Next`. A summary page will open. Click on `Create Export`. Your new export will begin 

:::{figure} /fig/en_Hot_Export.png
---
width: 800px
align: center
name: Hot Export tool download of Mauritius financial institutions
---
:::

::::{dropdown} Bonus Exercise!

In the next exercise of the Larkana Flood Response Exercise track, we want to identify health facilities located in Larkana. Can you think of a way to export health facilities using the HOT Export Tool?

::::

4. [Import the new file into your QGIS project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html).
5. Arrange the layers on the map so you can see the new layer.
6. (optional) Use the classification function to get a better overview to get a better 
   overview:
    * Right-click on the layer `Larkana_Roads` in the `Layer Panel` 
      -> `Properties`. A new window will open up with a vertical tab section on 
      the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menu. Open it and choose `Categorized`. 
      Under `Value` select "highway".
    * Further down the window click on `Classify`.  Now you should see all unique 
      values or attributes of the selected column.  You can adjust the 
      colours by double-clicking on one row in the central field. Once you are 
      done, click `Apply` and `OK` to close the symbology window.

As you can see, the HOT Export tool offers a good mix of flexibility and quick 
access to OSM data.

| Advantages  |  Disadvantages |
|---|---|
|+ Good options for data selection|- Many steps involved |
|+ Many different data formats available|- Only fixed option for data selection|
|+ Easy to use||
|+ Query can easily be repeated | |


## Alternative Tools

:::::{tip}

The HOT Export Tool is a good way to export tailored OSM data for your personal use. However, in some use cases, you might want to choose a different tool such as Geofabrik, QuickOSM, or even just the humanitarian data exchange website. Below, you can find a short description of the tool and it's advantages. You can find out how to use the different tools step by step on [this wiki page](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_OpenStreetMap_wiki.html).

::::{dropdown} Geofabrik, QuickOSM, HDX

:::{card}
__Geofabrik__
^^^
The [Geofabrik website](https://download.geofabrik.de/) offers downloads for OSM data by regions. You can select a region of interest and download all the OSM data inside of that region. This is the most extensive method. We recommend using this method if you want to explore the OSM data or you need a lot of OSM data. However, if you only need specific data, such as roads, or settlement points, or buildings, it might be better to choose the HOT export tool or QuickOSM. 

| Advantages  |  Disadvantages |
|---|---|
|+ Quick access to complete OSM datasets|- If one is only interested in specific features or regions (other then countries), not optimal|
|+ Very up-to-date OSM exports|- Large file size|
|+ Clear documentation of which OSM features are contained in each shapefile|- Only available as shapefile|

:::


:::{card}
__QuickOSM__
^^^
The QuickOSM plugin allows you to load OSM data from inside your QGIS window. It is a quick and easy method, but requires the deepest knowledge about the OSM data model compared to the other options.  
You will need to formulate a data query to find the data that you are looking for. To tailor your query based on the exact key and value you need there are two great resources: 

1. [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page), and especially the 
   [Map features](https://wiki.openstreetmap.org/wiki/Map_features) article. 
2. [Taginfo](https://taginfo.openstreetmap.org/)

This method has the advantage that you can specifically download the data that you need but you need to know how to formulate queries. To use QuickOSM, you have to [install the QGIS plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html). 

| Advantages  |  Disadvantages |
|---|---|
|+ Query can be tailored for very specific data|- Requires knowledge of OSM data model |
|+ Data loads directly in QGIS|- Building queries can quickly become complex |
|+ Query can easily be repeated | |

:::

:::{card}
__Humanitarian Data Exchange (HOT Exports)__
^^^
A quick and easy way to get specific OSM data, such as the road network, or the locations of health facilities, is to search for the data on the [humanitarian data exchange (HDX)](https://data.humdata.org/).

Here, the Humanitarian OpenStreetMap Team provides OSM exports for countries. The disadvantage of this method is that since the exports are for countries, the datasets are generally quite large and difficult to handle with QGIS. 

:::

::::
:::::
