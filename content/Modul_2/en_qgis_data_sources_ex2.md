# Exercise: OpenStreetMap data export
__🔙[Back to Homepage](/content/intro.md)__

## Aim of the exercise:

This exercise aims to show multiple ways how to get OpenStreetMap(OSM) as a vector file into QGIS.

## Relevant Wiki Articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)


## Data sources
In this exercise, you will download all data druing the exercise.



## Task

There are multiple ways how to get data from OpenStreetMap (OSM). 

### Task: GEOFABRIK

The website GEOFABRIK offers the possibility to download the full OSM dataset for a region.

1.	Go to __https://download.geofabrik.de/__ and navigate to the Mauritius  dataset by clicking on `Africa` -> ` Mauritius`
2.	Under __Commonly Used Formats__ select the option `mauritius-latest-free.shp.zip` and download the file. Place it somewhere on your computer where you can find it again and unzip it.
3.	Check out the content of the folder. There are many different shapefiles, each containing one kind of OSM data. The whole list of layers and what they include can be found [here](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf). As well as a short overview below.

6.	 Open a new QGIS project and save it in the “project” folder of your exercise folder.
7.	Load the file “gis_osm_places_a_free_1.shp” into your QGIS. This polygon layer contains the boundaries of different features reaching from named farm to island. Take some time to explore the data by using the attribute table. 
8. (Optional) You can select all features within the layer with the “fclass” = “island” and export them as a new layer.  This will allow you to start creating a map of the islands of Mauritius.
9. Load the file “gis_osm_buildings_a_free_1.shp” into your QGIS. This polygon layer contains all buildings mapped on the OSM for Mauritius. Take some time to explore the layer. You can add a satellite base map by using the [QuickMapService plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#basemaps-from-quickmapservices-plugin) to check if there are unmapped buildings.
10. Load the dataset “gis_osm_landuse_a_free_1.shp” into QGIS. Check out the dataset and use the classification function to get a better overview.
    * Right-click on the layer “Bgis_osm_landuse_a_free_1” in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menue. Open it and choose `Categorized`. Under `Value` select “fclass”.
    * Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected “fclass” column.  You can adjust the colours by double-clicking on one row in the central field. Once you are done, click `Apply` and `OK` to close the symbology window.

As you can see, GEOFABRIk is great if you want to get complete OSM datasets for whole countries or regions. 

| Advantages  |  Disadvantages |
|---|---|
|+ Quick access to complete OSM datasets|- If one is only interested in specific features or regions, not optimal|
|+ Very up-to-date OSM exports|- Large file size|
|+ Clear documentation of which OSM features are contained in each shapefile|- Online available as shapefile|

### Task: HOT Export Tool

The [umanitarianOpenStreetMapTeam (HOT) Export Tool](https://export.hotosm.org/v3/) is an NGO specialising in utilizing an extending OSM for humanitarian purposes. HOT offers a browser-based tool to download OSM data with good options to specify region, time, feature type and data format.
1.	Go to the HOT Export tool. To use the tool you need a OSM account. If you don’t have one you need to create on. Click on `Log in`. In the new window select the option to create a new account. 
2.	With your OSM account you can log in directly into the HOT Export tool by clicking on `Log in`.
3.	In this example, we want to download all features of the OSM related to banking and finance on the main island of Mauritius. 
    1.	Select area or location: Zoom to Mauritius on the map or use the search bar.  To mark the main island there are three options. You can draw a box, draw a polygon or upload a geoJOSN file with your boundaries. In this case, use one of the first two options to mark Mauritius.
    2.	Description: Add a name like “Mauritius finical institutions” for your export and a short description of your export.
    3. Format: The HOT Export tool offers many data formats in which you can export data. In this case, go with GeoPackage only.
    4. Data: The easiest way to select the data you want to download is the Tag Tree. The YAML option offers far more flexibility although is requires more technical knowledge. 
    Since we want to download the position of financial institutions go to “Financial” and select all options (ATM, Bank, Bureau de Change).
    5. Click on `Create Export`. You will be forwarded to a new page. Here you have to wait until the export from OSM is finished and then you can download the file by clicking on the name of the file next to “geoPackage`.gpkg`”.
```{figure} /fig/en_Hot_Export.png
---
width: 800px
align: center
name: Hot Export tool download of Mauritius financial institutions
---
Hot Export tool download of Mauritius financial institutions. Adapted screenshot from [HOT Export Tool](https://export.hotosm.org/v3/exports/new/describe)
```
4.	Load the new file in your QGIS.
5.	Arrange the layers on the map so you can see the new layer.
6.	Use the  classification function to get a better overview to get a better overview:
    * Right-click on the layer “Mauritius_finical_institution” in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * On the top you find a dropdown menue. Open it and choose `Categorized`. Under `Value` select “amnity”.
    * Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected “fclass” column.  You can adjust the colours by double-clicking on one row in the central field. Once you are done, click `Apply` and `OK` to close the symbology window.

As you can see, the HOT Export tool offers a good mix of flexibility and quick access to OSM data. However, there are quite some steps involved until the data is in QGIS.

| Advantages  |  Disadvantages |
|---|---|
|+ Good options for data selection|- Many steps involved |
|+ Many different data formats available|- Only fixed option for data selection|
|+ Easy to use||
|+ Query can easily be repeated | |

### Task: QuickOSM

The Quick Map service plugin allows you to load OSM data directly into QGIS. However, the plugin requires the deepest knowledge of the OSM data model, compared to the previous two options. To tailor your query based on the exact key + value you need there are two great resources. The first is the [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page) and especially the article [Map features](https://wiki.openstreetmap.org/wiki/Map_features#Commercial). And the second is the website [taginfo](https://taginfo.openstreetmap.org/). Have a look at both.
1.	Install the QuickOSM plugin by clicking on the `Plugin` tab, -> `Manage and Install Plugins…` -> `All` -> Search for the plugin -> `Install Plugin`
2.	Now we want to find all health facilities on the island of Mauritius.
    1. Position the island of Mauritius in a way that the island is completely visible in your map canvas.
    2. Open the QuickOSM Plugin by clicking on the `Vector` tab -> `QuickOSM`-> `QuickOSM`
    3. Click on `Quick query`.
    4. In the table create a key + value pair below. This pair will cover all hospital features within the amenity key. See here.
        - Key 	= amenity
        - Value 	=  hospital
    5. Click on the green plus icon to add another line to the table. In this line select “OR” in the small dropdown menu on the left-hand side of the new line
    6. Create a new key + value pair blow. This pair will cover all hospitals in the Healthcare key. See here.
        - Key 	= healthcare
        - Value	= hospital
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
3.	Check out the new layers in the layer panel. Open the attribute table of the point layer. Check the “healthcare” and “amenity” column. Which data would be missing if you would have used only one of the keys?
4.	Do the same query for La Reunion which is direct to the southwest of Mauritius. Move the island in the middle of your map canvas and click `Run query`. Does the attribute table of this new point layer look different?
5.	What if we only want hospitals with an emergency room? In this case, we would need to build a query using a combination of the operators “OR” and “AND”. Look at the image below.
    ```{figure} /fig/en_quick_OSM_hospital_emgerency_key.png
    ---
    width: 800px
    align: center
    name: QuickOSM hospital with emergency  query
    ---
    QuickOSM hospital with emergency  capacity query
    ```
6.	7.	Now try to create a query that shows all accommodations like hotels on the island. To do that, use this [wiki page](https://wiki.openstreetmap.org/wiki/DE:Key:tourism). The solution can be found in the dropdown menu below.

```{dropdown}  Solution accommodation query

```{figure} /fig/en_quick_OSM_accomedation_key.png
---
width: 800px
align: center
name: QuickOSM accomedation query
---
QuickOSM accomedation query
```

| Advantages  |  Disadvantages |
|---|---|
|+ Query can be tailored for very specific data|- Requires knowledge of OSM data model |
|+ Data directly in QGIS|- Query building can quickly become complex|
|+ Query can easily be repeated||
|+ Query can easily be repeated | |



