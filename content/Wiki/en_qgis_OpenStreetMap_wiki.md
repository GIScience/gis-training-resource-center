# OpenStreetMap (OSM) Data

## Geofabrik

The [Geofabrik website](https://download.geofabrik.de/) offers downloads for OSM data by regions. You can select a region of interest and download all the OSM data inside of that region. This is the most extensive method. We recommend using this method if you want to explore the OSM data or you need a lot of OSM data. However, if you only need specific data, such as roads, or settlement points, or buildings, it might be better to choose the HOT export tool or QuickOSM. 

***Example***

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

## QuickOSM

The QuickOSM plugin allows you to load OSM data from inside your QGIS window. It is a quick and easy method, but requires the deepest knowledge about the OSM data model compared to the other options.  
You will need to formulate a data query to find the data that you are looking for. To tailor your query based on the exact key and value you need there are two great resources: 

1. [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page), and especially the 
   [Map features](https://wiki.openstreetmap.org/wiki/Map_features) article. 
2. [Taginfo](https://taginfo.openstreetmap.org/)

This method has the advantage that you can specifically download the data that you need but you need to know how to formulate queries. To use QuickOSM, you have to [install the QGIS plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html). 

## Overpass Turbo

[Overpass Turbo](https://overpass-turbo.eu) is a web-based data export tool for 
OSM. By running a query, you can download the data and import it into your project. 
You can either run it by writing your query on the left or by using the wizard 
which will assist you in writing your queries. 
***Example***  
To search for schools in your bounding box or search area you can either write 
the query yourself or get it built by the wizard.  
**1. Check Tagging Guidelines**  
Search for it in the [OSM wiki](https://wiki.openstreetmap.org/wiki/Tags) and/or 
[taginfo](https://taginfo.openstreetmap.org). In our example it is: *amenity=school*  
**2.  Write or build the query**  
Either use the wizard by typing in *amenity=school in Heidelberg* or write your 
own query (f. e. for your bounding box):  
**Wizard:**
:::{figure} /fig/en_wizard_overpassturbo.png
---
height: 250px
align: center
name: en_wizard_overpassturbo_wiki
---
Screenshot of the Wizard in overpass turbo
:::

:::{figure} /fig/en_wizard_result.png
---
height: 250px
align: center
name: en_wizard_result_wiki
---
Screenshot of the result
:::  
**Query:**
```sql
[out:json];  
(  
  node ["amenity"="school"](49.35,8.553,49.481,8.756);
  way ["amenity"="school"](49.35,8.553,49.481,8.756);
  relation ["amenity"="school"](49.35,8.553,49.481,8.756);
);
out; 
```
**Bounding Box**  
To query with a bounding box you need a special format. Specify it like so:
 + s (southern limit in decimal degrees, lowest latitude)
 + w (western limit in decimal degrees, lowest longitude)
 + n (northern limit in decimal degrees, highest latitude)
 + e (eastern limit in decimal degrees, highest longitude)
     + for example:  
```sql
node ["key"="value"] (s, w, n, e);
         out;
```

:::{tip} 
For more information on the query language check out the [Language Guide](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide).
:::
**3. Download the data**  
One can export the results in various ways.

:::::{tab-set}

::::{tab-item} Data
By exporting the data as f.e. GeoJSON you can later on import them in your QGIS 
project.

:::{figure} /fig/en_overpass_turbo_data.png
---
height: 250px
align: center
name: en_overpass_turbo_data_wiki
---
Screenshot of how to export data in overpassturbo
:::

::::

::::{tab-item} Map
By exporting the query as map, you can share your current view as link or image.

:::{figure} /fig/en_overpass_turbo_map.png
---
height: 150px
name: en_overpass_turbo_map_wiki
align: center
---
Screenshot of how to export map in overpassturbo
:::
::::

::::{tab-item} Query
By exporting your query you can get the text or convert it to an OverpassXML or 
OverpassQL formatted query.

:::{figure} /fig/en_overpass_turbo_query.png
---
height: 250px
align: center
name: en_overpass_turbo_query_wiki
---
Screenshot of how to export query in overpassturbo
:::
::::

:::::

:::{tip} 
For more information, check out the [wiki](https://wiki.openstreetmap.org/wiki/Overpass_turbo).
:::
<!---
### Ohsome tools
-->