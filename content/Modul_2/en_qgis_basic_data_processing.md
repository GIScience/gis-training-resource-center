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


:::

::::

### overpass turbo

### quick osm plugin

By installing the QuickOSM plugin you can run the query directly in QGIS to download data from OpenStreetMap. 
First download the plugin by following the steps: 

```{figure} /fig/en_install_plugin.png
---
height: 500px
name: install_plugin
---
Screenshot of how to install plugins
```


```{figure} /fig/en_search_plugin.png
---
height: 500px
name: search_plugin
---
Screenshot of how to search for plugins
```

You will see a new icon on your toolbar on the top. Now it is possible to search for your key:value in a given location and run the query. If you are unsure which key and value are used, take a look in the [OSM wiki](https://wiki.openstreetmap.org/wiki/Tags). 

```{figure} /fig/en_quickosmplugin.png
---
height: 500px
name: quickosmplugin
---
Screenshot of the QuickOSM plugin
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