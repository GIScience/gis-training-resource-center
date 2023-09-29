# Types of Geodata

* Vector data
* Raster data
* Non-spatial data transfomed in geodata

# Vector data

Vector data can have the following data formats:

| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.shp | Shapefile |Old but still widely used geodataformat. Can only contain one dataset. The file has to consist of at least three different files (.shp, .shx, .dbf)|
|.gpkg| GeoPackage  | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and not spatial data like tables)|
|.kml |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)|
| .gpx.| GPS Exchange Format|Geodata format for the exchange of coordinates. For example for waypoints of tracks. |

# Raster data 

Raster data can have the following data formats:
| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeference information. If a .tif file has georeferenc information it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be be a raster file. Can contain multible datasets|
|.asc|Esri ASCII Grid files|Old simple raster file format, always with georeference informations|

## Text data

 Filename extension| Name | Dscription |
| ----- | --- | --- |
|.csv|comma-separated values|Very common data format which separates data with commas or other delimiters.|
|.xls|EXCEL|Data format used for EXCEL. EXCEL is a widely used spreadsheet program.|