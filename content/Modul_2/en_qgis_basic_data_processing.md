# Geodata and Geodata processing
**Competences:**
* Data Import
* Geo features and attributes
* Feature selection
* Basemap selection


## Data import

Before you can start visualizing and analysing in QGIS, you need to import your data. [Here](../../content/Modul_2/en_data_sources.md) you can look up, where to find different data sources.
Depending on which file format you want to import, the process differs slightly.

::::{tab-set}

:::{tab-item} Vector data import
The possible data formats are listed [here](../../content/Modul_2/en_qgis_geodata_concept.md). 
Go to the data source manager and choose vector on the right. By clicking on the three dots you can browse your files and choose the ones you want to import.

![datasource manager](../../fig/en_datasourcemanager_qgis.png)  

![import vector data](../../fig/en_import_vector.png)
:::

:::{tab-item} Raster data import
Go to the data source manager and choose vector on the right. By clicking on the three dots you can browse your files and choose the ones you want to import.  

![datasource manager](../../fig/en_datasourcemanager_qgis.png)  

![import raster data](../../fig/en_import_raster.png)
:::

:::{tab-item} Delimited text import
Go to the data source manager and choose vector on the right. By clicking on the three dots you can browse your files and choose the ones you want to import. Next, choose your file format and expand the geometry definition section to select **latitude (Y field)** and **longitude (X field)**. Usually there is one column each that contains the geometry ot coordinates.  
 Click on Geometry CRS (5) and select the Project CRS.
![import text data](../../fig/en_import_delimeted_text.png)
 When you choose custom delimiters in the file format (3 & 3.1), you can change the delimiters.
![file format](../../fig/en_delimited_text_fileformat.png)
:::

:::{tab-item} GeoPackage import
Go to the data source manager and choose GeoPackage on the right. Click on New to add a connection. Browse through your data to the Geopackage and add. By clicking on Connect and Add you can add the data to your project.


![datasource manager](../../fig/en_datasourcemanager_qgis.png)
![import gpkg](../../fig/en_import_gpkg.png)
:::

::::

### overpass turbo

Overpass turbo is a web based data mining tool for OSM. By running a query, you can download the data and import it into your project. You can either run it by writing your query on the left or by using the wizard which will assist you in writing your queries. One can export the results in various ways.

::::{tab-set}

:::{tab-item} Data
By exporting the data as f.e. GeoJSON you can later on import them in your QGIS project.
```{figure} /fig/en_overpass_turbo_data.png
---
height: 250px
name: overpass_turbo_data
---
Screenshot of how to export data in overpassturbo
```

:::

:::{tab-item} Map
By exporting the query as map, you can share your current view as link or image.

```{figure} /fig/en_overpass_turbo_map.png
---
height: 150px
name: overpass_turbo_map
---
Screenshot of how to export map in overpassturbo
```
:::

:::{tab-item} Query
By exporting your query you can get the text or convert it to an OverpassXML or OverpassQL formated query.

```{figure} /fig/en_overpass_turbo_query.png
---
height: 250px
name: overpass_turbo_query
---
Screenshot of how to export query in overpassturbo
```
:::

::::

For more information, check out the [wiki](https://wiki.openstreetmap.org/wiki/Overpass_turbo).



### Quick OSM plugin

By installing the QuickOSM plugin you can run the query directly in QGIS to download data from OpenStreetMap. 
First download the plugin by following the steps: 

![install plugin](../../fig/en_install_plugin.png)


```{figure} /fig/en_search_plugin.png
---
height: 500px
name: search_plugin
---
Screenshot of how to search for plugins
```

You will see a new icon on your toolbar on the top. Now it is possible to search for your key:value in a given location and run the query. When the download is complete, you will get a notification. The result will be loaded in three temporary layers, one for nodes, ways and relations.


```{figure} /fig/en_quickosmplugin.png
---
height: 500px
name: quickosmplugin
---
Screenshot of the QuickOSM plugin
```
```{note} 
If you are unsure which key and value are used, take a look in the [OSM wiki](https://wiki.openstreetmap.org/wiki/Tags). 
```

<details>
<summary>What do i do if there is no new icon?</summary>
<br>
If you can't find your new icon for the plugin, select view - toolbars and check that the QuickOSM plugin has a tick to be shown.

```{figure} /fig/en_no_new_icon.png
---
height: 500px
name: no_new_icon
---
Screenshot of how to add a new icon
```

</details>



## Geo features and attributes

Each layer consists of geometric elements (points, lines or polygons) and an attribute table. The attribute table contains information on each element of the layer, which is stored in a table as rows and columns. Each row corresponds to an element and each column to an attribute. Atrributes can be for example: ID, name, postal code, street name, ...

What can you do with that

öffnen (2 ways)
sort
manually select / unselect
filter
zoom to selected
edit change data 


```{note} 
If you have multiple layers, only the attribute table of the layer selected in the layer panel on the left will open. 
``````

## Feature selection


## Basemap selection

### OpenStreetMap

If you are using version 3.4 or higher in QGIS, it is by default possible to add the OSM base map to your project. Unfold the XYZ tiles, right-click on OpenStreetMap and select add layer to project.

```{figure} /fig/en_add_osm_basemap.png
---
height: 500px
name: add_osm_basemap
---
Screenshot of how to add OSM basemap
```

### QuickMapServices
BRC exc 1.3

## Data organization