# Geodata concept

🚧 This training platform and the entire content is under ⚠️construction⚠️ and 
may not be shared or published! 🚧


__🔙[Back to Homepage](/content/intro.md)__

**Competences:**
* Projections
* Layer concept
* Vector and raster data (basic concepts)
* Vector file formats


## Projections 
### Theory

__The earth is a sphere and cannot be represented on a flat map without being 
distorted.__ To able able to display the earth on a flat map for example as a 
rectangle it needs to be projected. For further explanation, watch this video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kIID5FDi2JQ?si=C0tYz7nteMF_xqvr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


For this translation, from a curved on a flat surface, thousands of different 
methods exist. These are called **coordinate reference systems (CRS)**.


```{figure} /fig/en_examples_projections_IBIS.png
---
width: 800px
align: center
name: Examples for Projections (azimuthal, cylindrical and conic)
---
Examples for Projections. Source:(http://ibis.colostate.edu/webcontent/NR505/2012_Projects/Team6/GISConcepts.html)
```


Every projection comes with a trade-off in shape, direction, distance and area. 
That's why it is important to choose different types of CRS for different use 
cases.

For example, Mercator projections don´t represent the area correctly. Google 
Maps still uses the Mercator to be able to represent streets correctly, since it 
<!-- CHECK: I think Google Maps uses variable CRS now -->
works well on a small scale. On a big scale, the shape of the countries stay the 
same but the area is mispresented. You can check the true size in comparison to 
different placements on the map on this [website](https://www.thetruesize.com). 
A popular example is Greenland in comparison with Africa, which seem on the map 
to be about the same size, but in reality Africa is a lot bigger.


```{figure} /fig/en_greenland_africa.png
---
width: 800px
align: center
name: Comparison Greenland - Africa
---
Comparison Greenland - Africa. Source: [The True Size of](https://www.thetruesize.com/#?borders=1~!MTYwODM1MTk.MzkyNDUyNg*MjY5NjM4Mzg(MTA1MjgyOTE~!CONTIGUOUS_US*MTAwMjQwNzU.MjUwMjM1MTc(MTc1)MQ~!IN*NTI2NDA1MQ.Nzg2MzQyMQ)MA~!CN*OTkyMTY5Nw.NzMxNDcwNQ(MjI1)Mg)
```

:::{dropdown} TheTrueSize.com - compare the effects of different projections

%%html
<iframe src="https://www.thetruesize.com/#?borders=1~!MTUxNjUyNzI.MzM1OTE0MQ*MzI2NDc5MjY(NjgwODA4Mg~!GL*OTQ3NTExNQ.MjkxMDYzMzM)Mw" width="750" height="500"></iframe>
:::

```{Attention}
It's important to work with the right projections, if not we will produce wrong 
results! 
```
<!-- FIXME: this statement could do with some clarification -->

This table shows an overview on which projections to use for which needed 
characteristic:

| Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :--------------------: | :-----------------: | :----------: |
| [x] shape              | [ ] shape           | [x] shape    |
| [x] rotation           | [x] rotation        | [ ] rotation |
| [ ] area               | [x] area            | [x] area     |

For smaller areas local projections should be used, since they give a more 
accurate display at the expense of more distortion at the global level. 



```{figure} /fig/en_local_crs.png
---
width: 800px
name: Local and global coordinate reference systems (CRS)
align: center
---
Local and global coordinate reference systems (CRS). Source: British Red Cross (BRC)
```

### Application

```{Attention}
You can find all the projections and their CRS codes [EPSG.io](http://epsg.io). 
```

It is crucial that you are aware that you data can be in one CRS and your QGIS 
project in an other CRS. The data and the project should always be the same, or 
else you will get wrong results! The project CRS is displayed on the bottom left 
corner, as seen [here](../../fig/en_QGIS_User_Interface.png). 
To change the CRS of you data and project, follow the steps explained below.
The default CRS/EPSG code of every QGIS project is the World Geodetic System 84 
(EPSG: 4326). This CRS is optimized for world maps. So not perfect for most 
applications, because we mostly use maps for small areas. 


### How to check EPSG-Code/CRS of your QGIS project and change it
```{Note}
To check and adjust the CRS/ EPSG code should be the first thing you should do 
when starting a new QGIS project.
```

1. Open a QGIS project
2. In the very down right corner of QGIS you find the butten `EPSG`. The number 
next to it is the EPSG Code currently used in the project. For more information 
click on the button.
![](/fig/EPSG_Code.png)
3. The window `Project Properties` will open. Here you can view all availble 
CRS/EPSG-Code and their properties.
4. To change the CRS/EPSG code, select the one you want to use and click `Apply`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

### Changing the projection of a vector layer

1. `Vector` Tab -> `Data Management Tools` -> `Reproject Layer`
2. Select target CRS/EPSG code.
3. Save the new file by clicking on the three dots next to `Reprojected`, 
   specify the file name and the location where you want to save the file.
5. Click `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>


### Changing the projection of a raster layer

1. `Raster` Tab -> `Projections` -> `Warp (Reproject)`
2. Select target CRS/EPSG-Code
3. Select resampling method
4. Save the new file by clicking on the three dots next to `Reprojected`, specify 
   the file name and the location where you want to save the file.
5. Click `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>


### Common mistakes with Coordinate Reference Systems

The website [__I Hate Coordinate Systems!__](https://ihatecoordinatesystems.com/) 
offers a “a problem-based guide of common CRS issues, root causes, and solutions”. 
Check it out in case you have any issues with CRS.


## Layer concept

Geodata represents a real-world object on a map as a feature. A feature consists 
of two types of information: the location and attributes, e. g. name or ID. Those 
informations are collected in layers. A layer can only consist of geographic 
objects of the same type. [^1]
<!-- FIXME: We have not introduced geographic types yet -->


[^1]: https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers

By adding different layers, you build your map and can combine information from 
different sources. With those you then can perform analyses or adapt the 
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


## Vector and raster data

There are two primary types of geographic data: **vector and raster**.  


```{figure} /fig/en_vector_raster.png
---
width: 800px
name: 
align: center
name: Raster Vector Concept
---
Raster Vector Concept. Source: Adapted from [WikiMedia](https://commons.wikimedia.org/wiki/File:Raster_vector_tikz.png)
```

### Vector
Vector data contains a shape or a geometry. By using geometry objects (points, 
lines and polygons) the real world is represented. Each object stores the location 
(as address or coordinates) and further attributes, e.g. name or ID. Which geometry 
is used, depends on the feature it represents.

<!-- FIXME: this section should explain the different geometry types -->

```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 800px
name: 
align: center
name: Vector Data overview
---
Vector Data overview. Source: HeiGIT
```
  
#### Vector file formats

Vector data can have the following data formats:

| Filename extension| Name | Description |
| ----- | --- | --- |
|.shp | Shapefile |Old but still widely used geodata format. Can only contain one dataset. The file has to consist of at least three different files (.shp, .shx, .dbf)|
|.gpkg| GeoPackage  | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and non-spatial data like tables)|
|.kml |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)|
| .gpx| GPS Exchange Format|Geodata format for the exchange of coordinates. For example for waypoints of tracks. |
| .geojson|GeoJSON|Similar to shapefiles, but stores all information in a single file. 

<!-- FIXME: misleading to say GeoJSON is similar to shp - need a new definition? -->
  

```{figure} /fig/en_data_formats.png
---
width: 800px
name: 
align: center
name: The main geographical data formats
---
The main geographical data formats. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/4_data_geo/4_1_formats)
```


### Raster  
Raster data are images which contain a matrix of pixels ("raster" means "grid" 
in German). Each pixel stores a value, which might refer to elevation, 
temperature, population or land cover type. Since a raster is based on an image, 
the resolution is crucial. It defines the precision of the data and size of the 
pixels. 


```{figure} /fig/en_quality_raster.png
---
width: 800px
align: center
name: The main geographical data formats
---
The main geographical data formats. Source: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_3_vector_raster_data)
```

In this picture you can see the same location, on the left as vector data, 
visualising streets and urban area, and on the right hand as raster data 
(satellite image), showing the land cover.


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

| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeferenced data. If a .tif file is georeferenced it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be be a raster file. Can contain multiple datasets|
|.asc|Esri ASCII Grid files|Old, simple raster file format, always with georeferenced data|



