# Geodata Import in QGIS

## Vector data Import 
Vector data can have the following data formats:

| Name | Filename extension | Dscription |
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

:::{grid-item-card} Open vector data via Layer tab

:::{figure} /fig/qgis_open_vector.mp4
:width: 300px
:::

:::{grid-item-card} Open vector data via drag-and-drop

:::{figure} /fig/qgis_import_vector_d_d.mp4
:width: 300px
:::

:::

::::


*QGGIS Version 3.22.15*

