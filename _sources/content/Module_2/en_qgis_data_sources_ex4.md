# Exercise: OpenStreetMap data export
__🔙[Back to Homepage](/content/intro.md)__

__🔙[Back to Exercise overview](/content/Modul_2/en_qgis_modul_2_exercises.md)__


:::{card}
__Aim of the exercise:__
^^^

This exercise aims to show multiple ways how to get OpenStreetMap(OSM) as a vector 
file into QGIS.

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

Since the exercise is about finding data, there won't be any data to download. 
Instead download the usual folder structure [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) and insert your data as you download it.

## Task

There are multiple ways how to get data from OpenStreetMap (OSM). In this exercise, we will go over a few methods to extract data from OSM. Depending on your use-case, you might only want very specific data from OSM, whereas in others, you might want to download almost all the regional OSM data.
<!-- FIXME: This task needs more information. what is the user trying to achieve 
   and why?
   
   ADD: Maybe a discussion step for each extraction method? in which scenarios would you choose which extraction method? -->

### Task: Geofabrik

The Geofabrik website offers downloads of OSM data by region.

1. Go to __https://download.geofabrik.de/__ and navigate to the Mauritius  
   dataset by clicking on `Africa` -> ` Mauritius`
2. Under __Commonly Used Formats__ select the option `mauritius-latest-free.shp.zip` 
   and download the file. Place it somewhere on your computer where you can find 
   it again and unzip it.
3. Check out the content of the folder. There are many different shapefiles, 
   each containing one kind of OSM data. The whole list of layers and what they 
   include can be found [here](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf). 

4. Open a new QGIS project and save it in the `project` folder of your exercise 
   folder.
5. Load the file `gis_osm_places_a_free_1.shp`. This polygon 
   layer contains the boundaries of different features. Take some time to explore 
   the data by using the attribute table. 
6. (Optional) You can select all features within the layer with the 
   “fclass” = “island” and export them as a new layer.  This will allow you to 
   start creating a map of the islands of Mauritius.
7. Load the file `gis_osm_buildings_a_free_1.shp`. This polygon 
   layer contains all buildings in Mauritius mapped on OSM. Take some time 
   to explore the layer. 
8. Add a satellite base map by using the [QuickMapServices plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#basemaps-from-quickmapservices-plugin) 
   to check if there are unmapped buildings. 
8. Load the file `gis_osm_landuse_a_free_1.shp`. Check out the 
    dataset and use the classification function to get a better overview.
    * Right-click on the layer `gis_osm_landuse_a_free_1` in the `Layer Panel` 
      -> `Properties`. A new window will open up with a vertical tab section on 
      the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menu. Open it and choose `Categorized`. 
      Under `Value` select “fclass” (short for _featureclass_).
    * Further down the window click on `Classify`.  You will see all unique 
      values of the “fclass” column.  You can adjust the 
      colours by double-clicking on one row in the central field. Once you are 
      done, click `Apply` and `OK` to close the symbology window.

As you can see, Geofabrik is great if you want to get complete OSM datasets for 
whole countries or regions. 

| Advantages  |  Disadvantages |
|---|---|
|+ Quick access to complete OSM datasets|- If one is only interested in specific features or regions (other then countries), not optimal|
|+ Very up-to-date OSM exports|- Large file size|
|+ Clear documentation of which OSM features are contained in each shapefile|- Only available as shapefile|


### Task: HOT Export Tool

The [HOT Export Tool](https://export.hotosm.org/v3/) 
is a tool for accessing OSM data offered by Humanitarian OpenStreetMap Team (HOT).
HOT offers a browser-based tool to download OSM data with good options to specify 
region, time, feature type and data format.

1. Go to the HOT Export tool. To use the tool you need an OSM account. If you 
   don't have one you need to create one. Click on `Log in`. In the new window 
   select the option to create a new account. 
2. If you have an OSM account you can log in directly into the HOT Export tool by 
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
      <!-- SUGGESTION: I don't think the symbology instructions need to be repeated 
         if they are already provided above -->

As you can see, the HOT Export tool offers a good mix of flexibility and quick 
access to OSM data. However, there are quite some steps involved until the data 
is in QGIS. 
<!-- note: is it quick or are there lots of steps? doesn't make sense if
   both are true! -->

| Advantages  |  Disadvantages |
|---|---|
|+ Good options for data selection|- Many steps involved |
|+ Many different data formats available|- Only fixed option for data selection|
|+ Easy to use||
|+ Query can easily be repeated | |

### Task: QuickOSM

The QuickOSM plugin allows you to load OSM data directly into QGIS. 
However, the plugin requires the deepest knowledge of the OSM data model, 
compared to the previous two options. To tailor your query based on the exact 
key and value you need there are two great resources: 

1. [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page), and especially the 
   [Map features](https://wiki.openstreetmap.org/wiki/Map_features) article. 
2. [Taginfo](https://taginfo.openstreetmap.org/)

Have a look at both.
<!-- NOTE: this feels like info that is best dealt with outside of an exercise -->

1. Install the QuickOSM plugin by clicking on the `Plugin` tab, -> `Manage and 
   Install Plugins…` -> `All` -> Search for "QuickOSM" -> `Install Plugin`
2. Now we want to find all health facilities on the island of Mauritius.
    1. Position the island of Mauritius in a way that the island is completely 
       visible in your map canvas.
    2. Open the QuickOSM plugin by clicking on the `Vector` menu -> `QuickOSM` -> 
       `QuickOSM`
    3. Click on `Quick query`.
    4. In the table, add "amenity" as the key and "hospital" as the value. This 
       query will return hospital data.
    5. Click on the green plus icon to add another line to the table. In this 
       line select “OR” in the small dropdown menu on the left-hand side of the 
       new line
    6. Add "healthcare" as a new key with "hospital" as the value. 
    7. Below the table set the small dropdown menu to “Canvas Extent”
    8. Click on `Run query`

    ```{figure} /fig/en_quick_OSM_hospital_key.png
    ---
    width: 800px
    align: center
    name: QuickOSM hospital query
    ---
    QuickOSM hospital query
    ```
3. Check out the new layers in the layer panel. Open the attribute table of the 
   point layer. Check the “healthcare” and “amenity” columns. Which data would be 
   missing if you would have used only one of the keys?
4. Do the same query for La Reunion which is to the southwest of Mauritius. 
   Move the island in the middle of your map canvas and click `Run query`. Does 
   the attribute table of this new point layer look different?
5. What if we only want hospitals with an emergency room? In this case, we would 
   need to build a query using a combination of the operators “OR” and “AND”. 
   Look at the image below.

    ```{figure} /fig/en_quick_OSM_hospital_emgerency_key.png
    ---
    width: 800px
    align: center
    name: QuickOSM hospital with emergency  query
    ---
    QuickOSM hospital with emergency  capacity query
    ```
<!-- SUGGESTION: This exercise is already long - suggest leaving out the hotels query -->
6.	Now try to create a query that shows all accommodations like hotels on 
   the island. To do that, use this [wiki page](https://wiki.openstreetmap.org/wiki/DE:Key:tourism). 
   The solution can be found in the dropdown menu below.



```{dropdown}  Solution accommodation query

```{figure} /fig/en_quick_OSM_accomedation_key.png
---
width: 800px
align: center
name: QuickOSM accommodation query
---
QuickOSM accommodation query
```

| Advantages  |  Disadvantages |
|---|---|
|+ Query can be tailored for very specific data|- Requires knowledge of OSM data model |
|+ Data loads directly in QGIS|- Building queries can quickly become complex|
|+ Query can easily be repeated||
