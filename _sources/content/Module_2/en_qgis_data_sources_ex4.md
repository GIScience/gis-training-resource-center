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

This exercise aims to show two ways how to get OpenStreetMap(OSM) as a vector 
file into QGIS. We will go through the workflow using Geofabrik, the HOT (Humanitarian OpenStreetMap Team) export tool and the QuickOSM QGIS-plugin.

:::

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 

:::

:::{grid-item-card}
__These skills are relevant for__
^^^ 

- QGIS Essentials
- Finding and downloading relevant datasets and preparing them for further analysis

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^

- The exercise takes around 2 hours to complete, depending on the number of participants and their familiarity with computer systems.

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

OpenStreetMap (OSM) is a collaborative, open-source project that creates free, editable maps of the world, built by a global community of mappers. There are multiple different ways how to download or export data from OpenStreetMap (OSM), each with it's own advantage. In this exercise, we will go over the [HOT Export Tool](https://export.hotosm.org/v3/).

### Task: Using the HOT Export Tool

The [HOT Export Tool](https://export.hotosm.org/v3/) 
is a tool for accessing OSM data offered by Humanitarian OpenStreetMap Team (HOT).
HOT offers a browser-based tool to download OSM data with good options to specify 
region, time, feature type and data format.

1. Go to the HOT Export tool. To use the tool you need an OSM account. If you 
   don't have an account yet, you will need to create one. Click on `Log in`. In the new window 
   select the option to create a new account. 
2. If you have an OSM account, you can log in directly into the HOT Export tool by 
   clicking on `Log in`.
3. In this example, we want to download all banking and finance features from OSM 
   in Mauritius. 
    1. Select area or location: Zoom to Mauritius on the map or use the search 
       bar. To mark the main island there are three options. You can draw a box, 
       draw a polygon or upload a GeoJSON file with your boundaries. In this case, 
       use one of the first two options to mark Mauritius.
    2. Name and description: give your export the name “Mauritius financial 
       institutions” and add a short description of your export.
    3. Format tab: The HOT Export tool offers many data formats in which you can 
       export data. Select GeoPackage (`.gpkg`) and leave the other 
       options unchecked.
    4. Data tab: The easiest way to select the data you want to download is the Tag 
       Tree. Since we want to download financial institutions, find the “Financial” 
       category and select all options (ATM, Bank, Bureau de Change).
    5. Summary tab: Click on `Create Export`. You will be forwarded to a page to 
       wait until the export is finished. When the processing is finished, the 
       page will show a download link for your file. 

```{figure} /fig/en_Hot_Export.png
---
width: 800px
align: center
name: Hot Export tool download of Mauritius financial institutions
---
Hot Export tool download of Mauritius financial institutions. Adapted screenshot from [HOT Export Tool](https://export.hotosm.org/v3/exports/new/describe)
```

4. Load the new file in QGIS.
5. Arrange the layers on the map so you can see the new layer.
6. (optional) Use the classification function to get a better overview to get a better 
   overview:
    * Right-click on the layer `Mauritius_finical_institution` in the `Layer Panel` 
      -> `Properties`. A new window will open up with a vertical tab section on 
      the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menu. Open it and choose `Categorized`. 
      Under `Value` select “amenity”.
    * Further down the window click on `Classify`.  Now you should see all unique 
      values or attributes of the selected “fclass” column.  You can adjust the 
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


`````{tip}

The HOT Export Tool is a simple tool to use, but in some use cases, you might want to choose a different 

::::{dropdown} Other methods

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

Here, the Humanitarian OpenStreetMap Team provides OSM exports for countries.

:::

::::
`````
