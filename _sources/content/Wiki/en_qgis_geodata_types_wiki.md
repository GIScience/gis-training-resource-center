# Types of Geodata


__🔙[Back to Homepage](/content/intro.md)__

* Vector data
* Raster data
* Non-spatial data transformed in geodata

# Vector data

Vector data can have the following data formats:

| Filename extension | Name                    | Description                                                                                                                                         |
|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `.shp`               | Shapefile               | Outdated but still widely used geodataformat. Can only contain one dataset. A shapefile **must include** these files: `.shp`, `.shx`, and `.dbf`. It can also contain more files such as:  `.prj` , `.sbn`, `.sbx`, `.cpg`, `.qix` |
| `.gpkg`              | GeoPackage              | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and not spatial data like tables)    |
| `.kml`               | Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)                                                                          |
| `.gpx`               | GPS Exchange Format     | Geodata format for the exchange of coordinates. For example for waypoints of tracks.                                                                |
| `.geojson`           | GeoJSON                 | Similar to shapefiles, but stores all information in a single file.                                                                                 |

# Raster data 

Raster data can have the following data formats:
| Filename extension  | Name                  | Description                                                                                                                                                          |
|---------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `.tif`/`.tiff`/`.geotiff` | Tag Image File Format | Common raster and image data format. Does not necessarily have georeferenced information. If a .tif file has georeferenced information it is referred to as GeoTIFF. |
| `.nc`                 | netCDF                | Standard data format for scientific data like speed or temperature. Can be a raster file. Can contain multiple datasets                                           |
| `.asc`                | Esri ASCII Grid files | Old simple raster file format, always with georeferenced information                                                                                                |

## Text data

 | Filename extension | Name                   | Description                                                                   |
 |--------------------|------------------------|-------------------------------------------------------------------------------|
 | `.xls`               | EXCEL                  | Data format used for EXCEL. EXCEL is a widely used spreadsheet program.       |
 | `.csv`               | comma-separated values | Very common data format which separates data with commas or other delimiters. |

## Good practices

The video below gives a good overview of geodata formats and gives tips on file naming and other good practices.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kggwFZHXCl4?si=i2lLEo0u0wGdB759" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>