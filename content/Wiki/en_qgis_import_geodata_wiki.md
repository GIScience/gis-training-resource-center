# Geodata Import in QGIS

## Vector data Import 
Vector data can have the following data formats:

| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.shp | Shapefile |Old but still widely used geodataformat. Can only contain one dataset. The file has to consist of at least three different files (.shp, .shx, .dbf)|
|.gpkg| GeoPackage  | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and not spatial data like tables)|
|.kml |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)|
| .gpx.| GPS Exchange Format|Geodata format for the exchange of coordinates. For example for waypoints of tracks. |


```{Tip}
When importing a shapefile by drag-and-drop you have to use the file with the ending .shp!
```
### Open vector layer

::::{grid}
:gutter: 2

:::{grid-item-card} Open vector data via Layer Tab
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>



:::

:::{grid-item-card} Open vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>


::::

## Raster data Import 
Raster data can have the following data formats:
| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeference information. If a .tif file has georeferenc information it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be be a raster file. Can contain multible datasets|
|.asc|Esri ASCII Grid files|Old simple raster file format, always with georeference informations|

::::{grid}
:gutter: 2

:::{grid-item-card} Open raster data via Layer Tab
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>
:::


:::{grid-item-card} Open raster data via drag-and-drop

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>
:::

::::


:::{grid-item-card} Open NetCDF raster files 
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_NetCDF_raster.mp4"></video>

Import via drag-and-drop
1. Layer -> Add Layer -> Add Raster Layer -> Select your file -> click "add" 
2. A window will open and you have to select the exact dataset you want to use. -> Click "add Layers"
3. Click on the ? in the Layers window. The window "Coordination Reference System Selectir" will open. -> Select the correct reference system.-> Click “OK”
:::

## Text data import

Geodata can cum in common text and table data formats like csv. and EXCEL. To import such data directly into QGIS one has to follow specific steps.

| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.csv|comma-separated values|Very common data format which separates data with commas or other delimiters.|
|.xls|EXCEL|Data format used for EXCEL. EXCEL is a widely used spreadsheet program.|

```{Tip}
To directly load .csv or EXCEL data into QGIS, the datasets need to have columns containing geometry in the form of latitude (Y-field) and longitude (X-field). 
```
::::{grid}
:gutter: 2

:::{grid-item-card} Open csv. data in QGIS
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

:::

:::{grid-item-card} Open .xlsx files in QGIS
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_xlsx.mp4"></video>


1. Drag and drop the .xlsx file in QGIS.
2. If the file contains multible tables, select the table you want to work with. Click "add Layers"
3. click on the "Processing" tab -> Toolbox -> search for the tool "Creat points layer from table"
4. Select you table as "Input Layer"
5. Select the  longitude column for "X field" and the latitude column for "Y field"
6. Click Run

```{Tip}
A other option is always to transform the .xlsx file into a .csv, which is eaysier to open in QGIS.
```
:::

::::

*QGGIS Version 3.22.15*

