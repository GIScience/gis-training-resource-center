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





### quick osm plugin

### overpass turbo

### Adding basemap


## Geo features and attributes


## Feature selection


## Basemap selection