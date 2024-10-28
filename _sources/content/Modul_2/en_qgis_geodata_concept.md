# Introduction to geodata and layers

__🔙[Back to Homepage](/content/intro.md)__

**Competences:**

In this chapter, you will learn what __geodata__ is, and understand the difference between __vector and raster 
data__. Furthermore, this chapter explains the __layer concept__ of GIS-software, which is fundamental to every map 
you will create. 

## What is geodata?

Geodata, geospatial data, or geographic data is data that has geographical information. This means that the data 
refers to a location, that is defined by coordinates. It is similar to other forms of data that can be represented 
in tables (such as Excel spreadsheets or CSV files) but each item in the data set also holds coordinate information 
(see {numref}`Raster Vector Concept`).
GIS software helps us visualise and manipulate geodata in a 2D (or even 3D) space. 
There are two primary types of geographic data: **vector data and raster data**. Both types represent tangible or 
intangible things in the real world. However, how they store this data is quite different. Because of this, the 
manipulation and representation of these two types differs dramatically. Understanding the difference between these 
two types, and how to work with each type on its own, as well as combining both types, will be one of the main skills you will acquire when learning GIS. 

```{figure} /fig/en_vector_raster.png
---
width: 500px
align: center
name: Raster Vector Concept
---
Raster / vector concept. Source: Adapted from [WikiMedia](https://commons.wikimedia.org/wiki/File:Raster_vector_tikz.png)
```

What type of information can be stored in geodata is almost endless. It can hold information about the physical 
world - such as:

* elevation (height) data
* environmental data (soils, climate, temperature, rainfall, information about 
weather events or natural phenomena, such as flooding extent)
* data about the infrastructure, buildings, transportation, etc. 
* sociocultural or economic data - such as demographic data, administrative boundaries, social events, crime, etc. 

Geodata usually represents data entries as __geometries__ on a 2D canvas. These geometries can be points, lines, polygons, or even pixels and can represent various objects that exist in the physical world - such as 
roads, lakes, trees, etc. - or represent intangible objects - such as administrative boundaries, population 
numbers, health indicators, historical events, etc. 


### Vector data


Vector data are digital features and they can store geographic/spatial information, as well as other data attributes. As such, they are ideal to visualise information on a map. Each feature can be displayed on a maps using one out three geometries: __points, lines, or polygons__. A layer can only contain features with same type of geometry. 


```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 650px
align: center
name: Vector Data overview
---
Vector data overview. Source: HeiGIT
```

- Point data usually only has one set of coordinates per data entry (longitude, latitude and sometimes elevation, usually referred to as x, y, and z).
- Lines are constructed by connecting multiple points which are saved as a single data entry.
- Polygons are also constructed by connecting several points, but they form a closed geometry. Each geometry is then represented by a single data entry.


Each feature stores the location (as address or coordinates) and further attributes, e.g. name, ID, or any other sort of 
information. Which geometry is used depends on the type of data that is represented. For example, a road might be 
represented by a line, a building might be represented by polygon and a tree might be represented by a point.


```{figure} /fig/en_geodata_example_2.png
---
name: geometry geodata example 2
width: 700px
---
Geographic information can be an address and/or GPS coordinates. (Source: BRC)
```

- Features are displayed on maps with a geometric representation, but they are made of information organized in tables (see {numref}`geodata example`). 
- Each row in the table will be one feature on the map, while each column will contain one attribute information (field). 
- Multiple attributes can be associated to each feature. 

```{figure} /fig/Geodata_attribute_table_example.png
---
name: geodata example
width: 750px
---
A data table in Microsoft Excel with geographic information. (Source: BRC)
```

{numref}`example_geometric_vs_attribute_view` shows the same dataset displayed both as its geometric representation and as an attribute table. 

```{figure} /fig/example_geometric_and_attribute_view.png
---
name: example_geometric_vs_attribute_view
width: 700 px
---
Each polygon on the left represents one row (feature) on the right.  (Source: BRC)
```

#### Vector file formats

There are several file formats for vector data. They each differ in how the geometries and attributes are stored. However, they still all only contain points, lines, or polygons. Some formats have advantages over others, while others are still used out of convention, although they are outdated.
The following table gives a short description of commonly used vector file formats.

| Filename extension| Name | Description |
| ----------- | ---------------------- | --------------------------------------------------------- |
|`.shp`       | Shapefile              | A shapefile is a vector data file format commonly used for geospatial analysis. Shapefiles store the location, geometry, and attribution of point, line, and polygon features. It's a common files format used by most GIS software and online mapping platforms. The format is old but still widely used geodata format. One shapefile can only contain one dataset. A complete shapefile has to consist of at least three different files (.shp, .shx, .dbf)| 
|`.gpkg`      | GeoPackage             | The new standard for geodata. GPKG files are an open, portable SQLite-based format for storing vector and raster geospatial data, compatible with various GIS platforms on desktop, web, and mobile. Can contain multiple datafiles (vector, raster and non-spatial data such as tables) |
|`.kml`/`.kmz.`       |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/). KMZ files are compressed versions of KML (Keyhole Markup Language) files used to store geographic data, such as points, paths, and polygons, along with any associated media like images and icons. Commonly used with Google Earth and other mapping software, KMZ files bundle both spatial data and resources in one compact file, making it easy to share interactive maps and visualizations.|
| `.gpx`      | GPS Exchange Format    | Geodata format for the exchange of coordinates. For example for waypoints of tracks. |
| `.geojson`  | GeoJSON                | Open data format using Javascript Object Notation (JSON) to store geographic data. Can store multiple type of geometries in one file and is widely compatible with web and mobile applications. | 
| `.gdb`      | Geodatabase            | Sesigned for efficient data management, spatial analysis, and complex geospatial workflows. Geodatabase files are a proprietary Esri format for storing and managing large volumes of spatial data, including feature classes, tables, and relationships in a structured database. |


```{note}
The different file formats have different use cases, as well as advantages or shortcomings. 

- For instance, __GeoJSON__ files cannot store projection info and are conventionally limited to the WGS84 ellipsoid. This makes it difficult to use GeoJSON files in projects where you are using region-specific projections or use projections based on different ellipsoids.

- __Geodatabase__ and __Geopackage__ are, unlike the other formats, databases. In GIS, databases store spatial data in structured, scalable systems that support multi-user access, complex queries, and large datasets, making them ideal for enterprise-level analysis and data management. Files, on the other hand, store data in individual, portable formats like Shapefiles, GeoJSON, or GeoPackage, which are easier to share and use offline but lack advanced querying capabilities and scalability.

```

#### Shapefile structure

A shapefile is a collection of separate files which commonly come in a single folder/directory. Some files are mandatory, others are optional. In order to have a functioning shapefile, you need to have all the mandatory files in the same folder. 

```{figure} /fig/en_shapefile_structure.png
---
name: shapefile_folderstructure
width: 400 px
---
__SHP, SHX__ and __DBF__ are the __mandatory__ files that every shapefile must contain to work properly. The SHP is the main file and contains the geometry.  
```


### Raster data

Another type of geospatial data is raster data. Raster data consists of cells that are organized into a grid with 
rows and columns, thus forming a raster. Each cell, or pixel, contains a value which holds information (for 
example, temperature, or population density). Since raster data consists of pixels, aerial photographs or satellite 
imagery can also be used as raster data, if they have geographical coordinates (see [georeferencing](/content/Modul_3/en_qgis_georeferencing.md)).

Typical uses for raster data are: 

* elevation data (often referred to as a digital elevation model or DEM)
* precipitation data
* interpolated temperature data
* population density

The value of each cell is usually visualised by assigning a 
color to a value. For elevation data, for example, a color ramp is usually used. For categorical data, such as 
landuse, color categories (such as green = forest; yellow = agricultural landuse, red = residential). 

<!--- ADD: insert example of raster data -->

Raster values usually have only one value per cell, however, it can also have multiple (color) bands. Satellite 
imagery usually offers several bands to represent data collected from different parts of the light spectrum, which we can use to analyze different phenomena,  
such as the humidity of plants. Multiple bands means that you have more than one value per cell.

The main spatial characteristics are the extent - the area the grid represents in the real world (10km², 100km²) - and the raster resolution - the size of each pixel. In {numref}`The main geographical data formats`, you can see two raster datasets with different resolutions.

```{figure} /fig/en_quality_raster.png
---
width: 800px
align: center
name: The main geographical data formats
---
Two raster datasets with different resolution covering the same region. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_3_vector_raster_data)
```

In {numref}`Vector` and {numref}`Raster` you can see the same location, on the left as vector data, visualising streets and urban area, and 
on the right hand as raster data (satellite image), showing the land cover.


::::{grid} 2
:::{card} Vector
```{figure} /fig/en_same_location_vector.png
---
width: 400px
name: Vector
align: center
---
Features represented with vector data. Source: British Red Cross (BRC)
```
:::

:::{card} Raster
```{figure} /fig/en_same_location_raster.png
---
width: 400px
name: Raster
align: center
---
The same location represented as a raster image. Source: British Red Cross (BRC)
```
:::
::::

#### Raster data formats

Raster data can have the following data formats:

| Filename extension| Name | Description |
| ----- | --- | --- |
|`.tif`/`.tiff`/`.geotiff`|Tag Image File Format|Common raster and image data format. Does not necessarily have georeferenced data. If a `.tif` file is georeferenced it is referred to as GeoTIFF.|
|`.nc`|netCDF|Standard data format for scientific data like speed or temperature. Can be a raster file. Can contain multiple datasets|
|`.asc`|Esri ASCII Grid files|Old, simple raster file format, always with georeferenced data|

```{admonition} The advantage of geodatabases

Databases such as Geodatabase (`.gdb`) or 


```

----

{numref}`The main geographical data formats` summarizes the different data formats for raster and vector data commonly used in GIS.

```{figure} /fig/en_data_formats.png
---
width: 700px
align: center
name: The main geographical data formats
---
The main geographical data formats. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/4_data_geo/4_1_formats)
```

## The layer concept

GIS software helps us visualise geographic data. It does so by displaying the geometries or raster cells on a 2D 
canvas. However, when creating a map, we are using multiple datasets at once. Every type of geographic data, such 
as raster data, polygons, points, or lines, is usually stored inside a __layer__. Each layer consists of geographic 
objects of the same type (line, polygon, raster, ...). GIS software displays these layers on top of each other and 
let's you rearrange the order of these layer, in order to create insightful maps.


By adding different layers, you build your map and can combine information from 
different sources. With those, you can then perform analyses or adapt the 
representation by using symbols and colors. 

```{figure} /fig/en_layer.png
---
width: 800px
name: 
align: center
name: Layers in a GIS
---
Layers in a GIS. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers)
```


::::{admonition} Now it's your turn!
:class: note

Practical experience is key to mastering GIS. Now is a good moment to apply what we've learned in the first exercise of module 2.

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept_ex1.html

__Module 2 Exercise 1: Understanding Geodata__

:::
::::

## Data import

Before you can start creating maps in QGIS, you will need to load your data into QGIS. Depending on which file format you want to import, the process differs slightly.

### Vector data import

Typical [vector data formats](/content/Modul_2/en_qgis_geodata_concept.md#vector-file-formats) are Shapefile (`.shp`) and GeoPackage (`.gpkg`). 
The process of importing vector data in either of the two formats is the same. 

QGIS offers a few ways to load vector data. The most immediate is via drag-and-drop, where you simply 
drag the data files you want to add from your file browser into the QGIS window. Another 
method is via the "__Data Source Manager__" (`Layer` > `Data Source Manager`). You can also open the Data Source 
Manager with the keyboard-shortcut <kbd>CTRL + L</kbd>. 

```{Note}
GeoPackage files can contain multiple datasets and even whole QGIS projects. 
When you load a GeoPackage in QGIS, a window will appear where you can select 
the datasets you want to load.
```

#### Open vector data via the Data Source Manager

1. Click on `Layer`-> `Add Layer`-> `Add Vector Layer...`. This will open the Data Source Manager. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your 
   vector file
3. Select the file and click `Open`. More options will appear. In most cases, you can leave these options as they are.
4. Back in QGIS click `Add`

```{Attention}
QGIS only lets you import __unzipped__ shapefiles. Make sure to unzip your data files before importing them into QGIS.
```

:::{dropdown} Video: Importing vector data via the Data Source Manager
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>
:::

#### Open vector data via drag-and-drop

QGIS lets you open data in your QGIS project by simply dragging the files from your file browser onto your QGIS window. Shapefiles contain only one layer per shapefile, which will be added automatically into you layer panel. Geopackage files (`.gpkg`) can contain multiple layers in a single file. If you add a geopackage file, a new window will open where you will be prompted to select the layers you want to add to your project. 

:::{dropdown} Video: Importing vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

### Delimited text import (.csv, .txt)


In your GIS-career, you will come across geodata in the  format of delimited text files, such as `.csv` files (Comma Separated Values). These files contain tabular data, which can be opened by programs such as Microsoft Excel. They contain geographical or positional information as point coordinates in separated columns (for example, latitude and longitude, or x- and y-coordinates), or as "Well Known Text" (WKT), which represents complex geometries, such as polygons or lines. 


#### Open Delimited Text Layer 

```{Tip}
To load data from spreadsheets such as Comma Separated Value (`.csv`) or 
Excel (`.xlsx`), the datasets need to have columns containing geometry - this is 
most often in the form of latitude (Y field) and longitude (X field), but might 
also be in other formats, such as WKT. In this case, you can also have complex 
geometries in your delimited text file.  
```

```{figure} /fig/en_import_delimeted_text.png
---
width: 600px
name: 
align: center
name: Import delimited text
---
Import delimited text in QGIS 3.36.
```

1. `Layer` -> `Add Layer` -> `Open Delimited Text Layer`.
2. Click on `File name` click on the three points ![](/fig/Three_points.png) and 
   navigate to your CSV file and click `Open`.
3. `File Format`: Here you can specify which delimiter is used in the file you 
   want to import. In a standard CSV file, commas `,` are used. If this is not the 
   case, select `Custom delimiters`. Here you can choose the exact delimiter 
   used in your file. 

```{Tip}
To find out which delimiter is used you can open your .csv file in Notepad or 
Excel. There you can check which delimiter is used to separate the information.
```

```{figure} /fig/en_delimited_text_fileformat.png
---
width: 600px
name: 
align: center
name: Import delimited text - file format
---
Import delimited text in QGIS 3.36 - file format.
```

4. `Geometry definition`: In this section, you specify which columns of the file 
   contain the spatial information to georeference the data on the map. If the 
   file has a column containing __latitude__ and another with __longitude__ data, 
   you can use them to georeferenced the data. Check `Point Coordinates` if the `.csv`-file contains point data. 
   Select for `X field` “LONGITUDE” and for `Y field` “LATITUDE”.
5. Under `Geometry CRS` select the coordinate reference system (CRS). By default, 
   QGIS will select the CRS of the project. 

   If the file does not have spatial information choose the option `No geometry 
   (attribute only table)`.
6. Click `Add`

:::{dropdown} Video: Opening delimited text files in QGIS
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>
:::

### Raster data import

The import of raster data works in the same way as for vector data. You can either drag-and-drop the raster files 
onto your QGIS window, or open then through the "Data Source Manager".


:::{dropdown} Video: Open raster data via the Data Source Manager

1. Click on `Layer`-> `Add Layer`-> `Add Raster Layer`
2. Click on the three points ![](/fig/Three_points.png) and navigate to your 
   raster file
3. Select the file and click `Open`
4. Back in QGIS click `Add` 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>

:::

:::{dropdown} Video: Open raster data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>
:::




