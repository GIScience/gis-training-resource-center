# Introduction to geodata, layers, and projections

__🔙[Back to Homepage](/content/intro.md)__

**Competences:**

In this chapter, you will learn what __geodata__ is, and understand the difference between __vector and raster 
data__. Furthermore, this chapter explains the __layer concept__ of GIS-software, which is fundamental to every map 
you will create. Finally, we will explain the basics of __projections__, which is the method of how we display the 
spherical shape of our planet onto a 2 dimensional plane. 

## What is geodata?

Geodata, geospatial data, or geographic data is data that has geographical information. This means that the data 
refers to a location, that is defined by coordinates. It is similar to other forms of data that can be represented 
in tables (such as Excel spreadsheets or CSV-files) but each item in the data set also holds coordinate information 
(see figure below).
GIS-software helps us visualise and manipulate geodata in a 2D (or even 3D) space. 
There are two primary types of geographic data: **vector data and raster data**. Both types represent tangible or 
intangible things in the real world. However, how they store this data is quite different. Because of this, the 
manipulation and representation of these two types differs dramatically. Understanding the difference between these 
two types, and how to work with each type on it's own, as well as, combining both types, will be one of the main 
skills you will acquire when learning GIS. 

```{figure} /fig/en_vector_raster.png
---
width: 500px
align: center
name: Raster Vector Concept
---
Raster Vector Concept. Source: Adapted from [WikiMedia](https://commons.wikimedia.org/wiki/File:Raster_vector_tikz.png)
```

What type of information can be stored in geodata is almost endless. It can hold information about the physical 
world - such as elevation data, environmental data (soils, climate, temperature, rainfall, information about 
weather events or natural phenomena, such as flooding extent), data about the infrastructure, buildings, transportation, etc. - or 
sociocultural or economic data - such as demographic data, administrative boundaries, social events, crime, etc. 
Geodata usually represents data entries as __geometries__ on a 2D canvas. These geometries can be points, lines, polygons, or even pixels and can represent various objects that exist in the physical world - such as 
roads, lakes, trees, etc. - or represent intangible objects - such as administrative boundaries, population 
numbers, health indicators, historical events, etc. 


<!--ADD: Insert table with examples of geodata, and how the data is stored in different file formats? See Uni Heidelberg lecture slides for this -->


### Vector data


Vector data are digital features and they can store geographic/spatial information, as well as other data attributes. As such, they are ideal to visualise information on a map. Each feature can be displayed on a maps using one out three geometries: __Points, Lines, or Polygons__. A layer can only contain features with same type of geometries. 


```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 650px
align: center
name: Vector Data overview
---
Vector Data overview. Source: HeiGIT
```

- Point data usually only have one set of coordinates (x, y, and sometimes z) per data entry.
- Lines are constructed by connecting multiple points which are saved as a single data entry.
- Polygons are also constructed by connecting several points, but they form a closed geometry. Each geometry is then represented by a single data entry.


Each feature stores the location (as address or coordinates) and further attributes, e.g. name, ID, or any other sort of 
information. Which geometry is used, depends on the type of data that is represented. For example, a road will be 
represented by a line, a building will be represented by polygon and a tree might be represented by a point.


```{figure} /fig/en_geometry_geodata_example.png
---
name: geometry geodata example
width: 400
---
Geographic information can be an address and/or GPS coordinates
```

- Features are displayed on maps with a geometric representation, but they are made of information organized in tables (see figure below). 
- Each row in the table will be one feature on the map, while each column will contain one attribute information (field). 
- Multiple attributes can be associated to each feature. 

```{figure} /fig/Geodata_attribute_table_example.png
---
name: geodata example
width: 450px
---
A data table in Microsoft Excel with geographic information
```

The figure below shows the same dataset displayed both as its geometric representation and as an attribute table. 

```{figure} /fig/example_geometric_and_attribute_view.png
---
name:example_geometric_vs_attribute_view
width: 650 px
---
Each polygon on the left represents one row (feature) on the right. 
```

#### Vector file formats

There are several file formats for vector data. They each differ in how the geometries and attributes are stored. However, they still all only contain points, lines, or polygons. Some formats have advantages over others, while others are still used out of convention, although they are outdated.
The following table gives a short description of commonly used vector file formats.

| Filename extension| Name | Description |
| ----------- | ---------------------- | --------------------------------------------------------- |
|`.shp`       | Shapefile              | Old but still widely used geodata format. Can only contain one dataset. The file has to consist of at least three different files (.shp, .shx, .dbf)|
|`.gpkg`      | GeoPackage             | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and non-spatial data like tables)|
|`.kml`       |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)|
| `.gpx`      | GPS Exchange Format    |Geodata format for the exchange of coordinates. For example for waypoints of tracks. |
| `.geojson`  | GeoJSON                | Open data format using Javascript Object Notation to store geographic data. Can store multiple type of geometries in one file. | 


The most common file formats used in GIS applications are:
- __Shapefile__: A shapefile is a vector data file format commonly used for geospatial analysis. Shapefiles store the location, geometry, and attribution of point, line, and polygon features. It's a common files format used by most GIS software and online mapping platforms. 
- __Geodatabase__: Similar to shapefile, it’s ESRI ArcGIS most used file format.
- __GeoJSON__: Similar to shapefile, but based on JSON (JavaScript Object Notation) language. Mostly used in mobile and online applications.
- __Kml/Kmz__: Initially developed to use in Google Earth, kml files are based on the XML standard. They are used in most mobile apps.

#### Shapefile structure

A shapefile is a collection of separate files which commonly come in a single folder/directory. Some files are mandatory, others are optional. In order to have a functioning shapefile, you need to have all the mandatory files in the same folder. 

```{figure} /fig/en_shapefile_structure.png
---
name: shapefile_folderstructure
width: 600 px
---
__SHP, SHX__ and __DBF__ are the __mandatory files that every shapefile must contain to work properly. The SHP is the main file, it contains the geometry of the file. 
```


### Raster data

Another type of geospatial data is raster data. Raster data consists of cells that are organized into a grid with 
rows and columns, thus forming a raster. Each cell, or pixel, contains a value which holds information (for 
example, temperature, or population density). Since raster data consists of pixels, aerial photographs or satellite 
imagery can also be used as raster data, if they have geographical coordinates (see [georeferencing]()).
<!-- FIXME: insert georeferencing link --> 

Typical raster data can be, for example, elevation data (or digital elevation model, DEM), precipitation data, 
interpolated temperature data, or population density. The value of each cell is usually visualised by assigning a 
color to a value. For elevation data, for example, a color ramp is usually used. For categorical data, such as 
landuse, color categories (such as green = forest; yellow = agricultural landuse, red = residential). 

<!--- ADD: insert example of raster data -->

Raster values usually have only 1 value per cell, however, it can also have multiple (color-)bands. Satellite 
imagery usually offers several bands (different light spectrum), which we can use to analyze different phenomena, 
such as the humidity of plants. Multiple bands means that you have more than one value per cell.

The main spatial characteristics are the extent - the area the grid represents in the real world (10km², 100km²) - and the raster resolution - the size of each pixel. In the image below, you can see two raster datasets with different resolutions.

```{figure} /fig/en_quality_raster.png
---
width: 800px
align: center
name: The main geographical data formats
---
Two raster datasets with different resolution covering the same region. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_3_vector_raster_data)
```

In this picture you can see the same location, on the left as vector data, visualising streets and urban area, and 
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
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeferenced data. If a .tif file is georeferenced it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be a raster file. Can contain multiple datasets|
|.asc|Esri ASCII Grid files|Old, simple raster file format, always with georeferenced data|

----

The figure below summarizes the different data formats for raster and vector data commonly used in GIS.

```{figure} /fig/en_data_formats.png
---
width: 700px
align: center
name: The main geographical data formats
---
The main geographical data formats. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/4_data_geo/4_1_formats)
```

## The layer concept

GIS-software helps us visualise geographic data. It does so by displaying the geometries or raster cells on a 2D 
canvas. However, when creating a map, we are using multiple datasets at once. Every type of geographic data, such 
as raster data, polygons, points, or lines, is usually stored inside a __layer__. Each layer consists of geographic 
objects of the same type (line, polygon, raster, ...). GIS-software displays these layers on top of each other and 
lets you rearrange the order of these layer, in order to create insightful maps. [^1]

[^1]: https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers

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


## Projections 
### Introduction

:::{dropdown} Video: Why all world maps are wrong
:open:
<iframe width="560" height="315" src="https://www.youtube.com/embed/kIID5FDi2JQ?si=C0tYz7nteMF_xqvr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
:::

An important issue when creating a map of a region, is that it is impossible to create a representation of a sphere 
on a 2D plane without distorting the map. The transformation of a 3D object onto a flat surface can be done with the help of a __projection__. Over the centuries, cartographers and mathematicians have developed a multitude of different methods to project the earth onto a flat surface. However, it is never possible to correctly represent the world on a flat surface (see the video above). 
Every projection distorts either the length between two points, the angles between two lines (directions), or the size of an area. A projection can only correctly represent one of these three dimensions. This means, that depending on the projection method, your world map will not represent the size, angles, or distances correctly. 

```{figure} /fig/en_examples_projections_IBIS.png
---
width: 700px
align: center
name: Examples for Projections (azimuthal, cylindrical and conic)
---
Examples for Projections. Source:(http://ibis.colostate.edu/webcontent/NR505/2012_Projects/Team6/GISConcepts.html)
```

Every projection has its use case. For example, the Mercator projection displays the angles between to points 
correctly. This was used extensively during the seafaring age without satellites, as ships could navigate to a 
destination by following a straight line on a map. For example, the Mercator projection displays road intersections 
correctly: a road that crosses another road at a right angle, will be displayed as such on a mercator projection. 
This is especially useful when navigating. The shape of an area remains correct, since the angles between each line 
stay true. However, if you increase the scale of the map, the size and distances get distorted dramatically (see 
figure below). Furthermore, the further away from the equator you get, the more distortion you get.

:::[note] The True Size of
The mercator projection is famous for distorting the size of different countries. You can check 
the true size in comparison to different placements on the map on [TheTrueSize.com website](https://www.thetruesize.com).
A popular example is Greenland in comparison with Africa, which seem on the map to be about the same size, but in reality Africa is a lot bigger.

```{figure} /fig/en_greenland_africa.png
---
width: 600px
align: center
name: Comparison Greenland - Africa
---
Comparison Greenland - Africa. Source: [The True Size of](https://www.thetruesize.com/#?borders=1~!MTYwODM1MTk.MzkyNDUyNg*MjY5NjM4Mzg(MTA1MjgyOTE~!CONTIGUOUS_US*MTAwMjQwNzU.MjUwMjM1MTc(MTc1)MQ~!IN*NTI2NDA1MQ.Nzg2MzQyMQ)MA~!CN*OTkyMTY5Nw.NzMxNDcwNQ(MjI1)Mg)
```

:::

In the dropdown below, you can look at the size distortion of mercator yourself.

:::{dropdown} TheTrueSize.com - compare the effects of different projections

%%html
<iframe src="https://www.thetruesize.com/#?borders=1~!MTUxNjUyNzI.MzM1OTE0MQ*MzI2NDc5MjY(NjgwODA4Mg~!GL*OTQ3NTExNQ.MjkxMDYzMzM)Mw" width="750" height="500"></iframe>

:::



### How to choose an appropriate projected coordinate system

In GIS, we project the earth onto a flat coordinate system (hence the name coordinate reference system or CRS). 
It is crucial that you are aware that your data can be in one CRS and your QGIS 
project in another CRS. The data and the project should always be the same, or 
else you will get wrong results! The project CRS is displayed on the bottom right
corner of the [QGIS interface](/content/Modul_1/en_qgis_start.md#overview-of-qgis-interface).  
To change the CRS of your data and project, follow the steps explained below.
The default CRS/EPSG code of every QGIS project is the World Geodetic System 84 
(EPSG: 4326). This CRS is optimized for world maps. So not perfect for most 
applications, because we mostly use maps for small areas. 

```{Tip}
Choose the projection according to your area of interest. There are special CRS, that have been created to reduce 
the distortion and inaccuracy of projections for different regions on earth. You can find all the projections and 
their CRS codes on [EPSG.io](http://epsg.io). 
```

These images show how different CRS distort earth in different ways. 

```{figure} /fit/world_mercator_tissots.png
---
width: 500 px
name: world_mercator_tissots
align: center
---
The Mercator Projection (EPSG:54004)
```

Notice how the shape of the circle stays the same. Out of this, we can conclude that the angles stay the same. However, the circles get bigger the further away they are from the equator, and the distance between these circles change the further they they get from the equator. Therefore, we can conclude that the distances and sizes are being distorted with the mercator projection. The strength of the Mercator projection is that it conserves the angles between to lines. We can see this because the circles stay perfectly circular the further they are from the equator.


```{figure} /fig/WGS_84_tissots.png
---
name: WGS_84_tissots
width: 500 px
---
The World Geodetic System 1984 (EPSG:4326)
```

The WGS 84 is a CRS which consists of an ellipsoid, that resembles the shape of the earth closely. Instead of metrical units of measurements, it uses angular degrees (latitude and longitude). The shape of the Tissot circles is undistorted near the equator, but becomes elongated on the East-West axis the further it gets away from the equator. Unlike the Mercator projection, there is no distortion on the in the North-South direction. As the circles become distorted, we can deduce that the this CRS distorts the angles.


```{figure} /fig/World_equidistant_cylindrical_tissots.png
---
name: World_equidistant_cylindrical_tissots
width: 500 px
---
The World Equidistant Cylindrical Projection (EPSG:54002)
```

The World Equidistant cylindrical CRS is equidistant (not distorting the length) along any meridian (cricles of longitude; North to South), and along the two standard parallels. The shape, scale and area distort the further they are away from the standard parallels. 

This table shows an overview on which projections to use for which needed 
characteristic:

| Characteristic  | Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :----------- |:--------------------: | :-----------------: | :----------: |
| Shape | [x]             |  [ ]          |  [x]    |
| Rotation | [x]           |  [x]      |  [ ]  |
| Area | [ ]              |  [x]            |  [x]    |

 I don't fully understand this?

#### Metric and Geographic Coordinate Reference Systems

There are two different types of Coordinate Reference System: __Geographic__ or __Metric__ CRS. 

- A Geographic CRS is based on a three-dimensional, ellipsoidal model of the Earth. It uses angular measurements (__latitude and longitude__) to define locations on the Earth's surface. The coordinates are usually expressed in degrees (e.g., 45°N, 120°W). 
   - __Advantages__: Since it is based on the Earth's curvature, it can be used to represent locationa anywhere on the earth. Most global datasets, GPS, and mapping systems use Geographic CRS making it highly compatible with various data sources. Locations can be specified accurately with angular measurements.
   - __Disadvantage__: Because it uses angular measurements, distances, areas, and shapes can be highly __distorted__. Since the distance between the circles of latitute and longitude change, the conversion of angles to meters is not constant 
- A metric CRS is a 2D representation of the earths surface. Although it is difficult to represent large areas of the globe on a 2D surface without surface, it is possible to create a 2D projection of a limited region with minimal distortion. The map units are typically metres or feet. It is created by projecting the earth onto a flat plane. 
   - __Advantages__: Since it uses a flat plane, you can calculate distances, areas, and angles accurately.
   - __Disadvantages__: A given projected CRS is usually optimized for a particular region. Using it outside its intended area can lead to significant distortions in distance, area, and shape.

```{figure} /fig/Problem_distance_geographic_coords.png
---
name: problem_distance_geographic_coords
width: 600 px
---

```

#### Local and Global CRS


```{figure} /fig/en_local_crs.png
---
width: 800px
name: Local and global coordinate reference systems (CRS)
align: center
---
Local and global coordinate reference systems (CRS). Source: British Red Cross (BRC)
```

As you can see, smaller regions look skewed and distorted in a global CRS
For smaller areas local projections should be used, since they give a more 
accurate display. However, local projections heavily distort the map on a global level. 

### How to check and change the project coordinate reference system

```{Note}
One of the first things you do when starting a new QGIS project should be to check and adjust the CRS/EPSG code to 
the region or area you are working on. If you are working on a map showing the entire globe, global projection such 
as the mercator projection should be used. If you are working on a smaller region, such as a continent, a country, 
or even smaller regions, __you should always use a local CRS, to avoid inaccuracies__. 
```

1. Open a QGIS project
2. In the very down right corner of QGIS you find the button `EPSG`. The number 
next to it is the EPSG Code currently used in the project. To see more information, or to change the CRS, click on the `Current CRS`-button ![](/fig/EPSG_Code.png). 
3. The window `Project Properties` will open. Here you can view all available 
CRS/EPSG-Code and their properties.
4. To change the CRS/EPSG code, select the one you want to use and click `Apply`.

:::{dropdown} Video: How to check and change the CRS in your QGIS project
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>
:::


### Project CRS and Layer CRS

The coordinate reference system of your QGIS project determines how QGIS displays the information. However, layers 
and datasets have their own CRS. This can be seen in the metadata, or layer properties of the dataset. The layer 
CRS refers to the coordinate system of the features or items in the dataset. The same coordinates in two different 
coordinate reference systems do not refer to the same location on earth. This is because of the distortion of 
distance and area.

```{note}
The first thing you should do when loading a new layer or dataset into your QGIS project, should be to check the 
coordinate reference system of the dataset, and reproject it to the project CRS if necessary. This way, you ensure 
consistency in your project and that the geoobjects in your layer are at the right locations. Otherwise, you will 
create false results.
```


<!--- ADD: insert example of layers that are in a CRS with an inaccuracy of a few meters to show the importance of 
getting the CRS right
ADD: Note that QGIS always uses the units of the layer (asks for degrees when creating a buffer with a geographic CRS) --->



#### Changing the projection of a vector layer

1. `Vector` Tab -> `Data Management Tools` -> `Reproject Layer`
2. Select target CRS/EPSG code.
3. Save the new file by clicking on the three dots next to `Reprojected`, 
   specify the file name and the location where you want to save the file.
5. Click `Run`

:::{dropdown} Video: How to change the CRS of a vector a layer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>
:::

#### Changing the projection of a raster layer

1. `Raster` Tab -> `Projections` -> `Warp (Reproject)`
2. Select target CRS/EPSG-Code
3. Select resampling method
4. Save the new file by clicking on the three dots next to `Reprojected`, specify 
   the file name and the location where you want to save the file.
5. Click `Run`

:::{dropdown} Video: How to change the CRS of a raster layer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>
:::

### Further resources

The website [__I Hate Coordinate Systems!__](https://ihatecoordinatesystems.com/) 
offers a “a problem-based guide of common CRS issues, root causes, and solutions”. 
Check it out in case you have any issues with CRS.
