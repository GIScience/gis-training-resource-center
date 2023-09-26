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

:::{figure} /fig/qgis_open_vector.mp4
:width: 300px
Import via Layer Tab

:::

:::{grid-item-card} Open vector data via drag-and-drop

:::{figure} /fig/qgis_import_vector_d_d.mp4
:width: 300px
Import via drag-and-drop
:::

::::

## Raster data Import 
Raster data can have the 
| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeference information. If a .tif file has georeferenc information it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be be a raster file. Can contain multible datasets|
|.asc|Esri ASCII Grid files|Old simple raster file format, always with georeference informations|

::::{grid}
:gutter: 3

:::{grid-item-card} Open raster data via Layer Tab

:::{figure} /fig/qgis_open_raster.mp4
:width: 300px
Import via Layer Tab

:::

:::{grid-item-card} Open raster data via drag-and-drop


:::{figure} /fig/qgis_import_raster_d_d.mp4
:width: 300px
Import via drag-and-drop
:::

:::{grid-item-card} Open NetCDF raster files 

:::{figure} /fig/qgis_import_NetCDFraster.mp4
:width: 300px
Import via drag-and-drop


1. Layer -> Add Layer -> Add Raster Layer -> Select your file -> click "add" 
2. A window will open and you have to select the exact dataset you want to use. -> Click "add Layers"
3. Click on the ? in the Layers window. The window "Coordination Reference System Selectir" will open. -> Select the correct reference system.-> Click “OK”
:::

::::

*QGGIS Version 3.22.15*

