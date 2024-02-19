# Geodata concept

🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧


__🔙[Back to Homepage](/content/intro.md)__

**Competences:**
* Projections
* Layer concept
* Vector and raster data (basic concepts)
* Vector file formats


## Projections 
### Theory

__The earth is a sphere and cannot be represented on a flat map without being distorted.__ To able able to display the earth on a flat map for example as a rectangle it needs to be projected. For further explanation, watch this video.
[![preview video](../../fig/screenshot_video_every_world_map_is_wrong.png)](https://www.youtube.com/watch?v=kIID5FDi2JQ "Why every world map is wrong")

For this translation, from a curved on a flat surface, thousands of different methods exist. These are called **Coordinate Reference Systems (CRS)**.

![Different Coordinate Reference Systems](../../fig/en_examples_projections.png)

Every projection comes with a trade-off in shape, direction, distance and area. That's why it is important to choose different types of CRS for different use cases.

For example, Mercator projections don´t represent the area correctly. Google Maps still uses the Mercator to be able to represent streets correctly, since it works well on a small scale. On a big scale, the shape of the countries stay the same but the area is mispresented. You can check the true size in comparison to different placements on the map on this [website](https://www.thetruesize.com). A popular example is Greenland in comparison with Africa, which seem on the map to be about the same size, but in reality Africa is a lot bigger.

![Comparison Greenland - Africa](../../fig/en_greenland_africa.png)

:::{dropdown} Embedded Website 

%%html
<iframe src="https://www.thetruesize.com/#?borders=1~!MTUxNjUyNzI.MzM1OTE0MQ*MzI2NDc5MjY(NjgwODA4Mg~!GL*OTQ3NTExNQ.MjkxMDYzMzM)Mw" width="750" height="500"></iframe>
:::

```{Attention}
It's important to work with the right projections, if not we will produce wrong results! 
```

This table shows an overview on which projections to use for which needed characteristic:

| Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :--------------------: | :-----------------: | :----------: |
| [x] shape              | [ ] shape           | [x] shape    |
| [x] rotation           | [x] rotation        | [ ] rotation |
| [ ] area               | [x] area            | [x] area     |

For smaller areas local projections should be used, since they give a more accurate display at the expense of more distortion at the global level. 

![Local Coordinate Reference Systems](../../fig/en_local_crs.png)

### Application

```{Attention}
You can find all the projections and their CRS code at this [website](http://epsg.io). 
```

It is crucial that you are aware that you data can be in one CRS and your QGIS project in an other CRS. The data and the project should always be the same, or else you will get wrong results! The project CRS is displayed on the bottom left corner, as seen [here](../../fig/en_QGIS_User_Interface.png). 
To change the CRS of you data and project, follow the steps explained below.
The default CRS/EPSG code of every QGIS project is the World Geodetic System 84 (EPSG: 4326). This CRS is optimized for world maps. So not perfect for most applications, because we mostly use maps for small areas. 


### How to check EPSG-Code/CRS of your QGIS Project and change it
```{Note}
To check and adjust the CRS/ EPSG-Code should be the first thing you should do when starting a new QGIS project.
```

1.  Open a QGIS projeckt
2. In the very down right corner of QGIS you find the butten `EPSG`. The number next to it is the EPSG Code currently used in the project. For more information click on the button.
![](/fig/EPSG_Code.png)
3. The window `Project Properties` will open. Here you can view all availble CRS/EPSG-Code and their properties.
4. To change the CRS/EPSG-code, select the one you want to use and click `Apply`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

### Changing the projection of a vector layer

1. `Vector` Tab -> `Data Management Tools` -> `Reproject Layer`
2. Select target CRS/ EPSG-Code.
3. Save the new file by clicking on the three dots next to `Reprojected`, specify the file name and the location where you want to save the file.
5. Click `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>


### Changing the projection of a raster layer

1. `Raster` Tab -> `Projections` -> `Warp (Reproject)`
2. Select target CRS/EPSG-Code
3. Select resampling method
4. Save the new file by clicking on th three dots nest to `Reprojected`, specify the file name and the location where you want to save the file.
5. Click `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>


### Comen mistakes with Coordinate Reference Systems

The website [__I Hate Coordinate Systems!__](https://ihatecoordinatesystems.com/) offers a “a problem-based guide of common CRS issues, root causes, and solutions”. Check it out in case you have any issues with CRS.


## Layer concept

Geodata represents a real-world object on a map as a feature. A feature consists of two types of information: the location and attributes, e. g. name or ID. Those informations are collected in layers. A layer can only consist of geographic objects of the same type. [^1]


[^1]: https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers

By superpositioning different layers, you build your map and can obtain information of different sources. With those you then can perform analyses or adapt the representation by using symbols and colors.

![Layer concept](../../fig/en_layer.png)


## Vector and raster data

There are two file types of geographic data: **vector and raster**.  

![Vector and raster data](../../fig/en_vector_raster.png)
  

### Vector
Vector data contains a shape or a geometry. By using geometry objects (points, lines and polygons) the real world is represented. Each object stores the location (as adress or coordinates) and further attributes, e.g. name or ID. Which geometry is used, depends on the feature it represents.

```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 800px
name: 
align: center
---
```
  
#### Vector file formats

Vector data can have the following data formats:

| Filename extension| Name | Description |
| ----- | --- | --- |
|.shp | Shapefile |Old but still widely used geodataformat. Can only contain one dataset. The file has to consist of at least three different files (.shp, .shx, .dbf)|
|.gpkg| GeoPackage  | Very versatile geodata format and the new standard for geodata. Can contain multiple datafiles (vector, raster and not spatial data like tables)|
|.kml |Keyhole Markup Language | Geodata format for use with [Google Earth]( https://earth.google.com/web/)|
| .gpx| GPS Exchange Format|Geodata format for the exchange of coordinates. For example for waypoints of tracks. |
| .geojson|GeoJSON|Similar to shapefiles, but stores all information in a single file. 
  

![data formats](../../fig/en_data_formats.png)



### Raster  
Raster data are images which contain a matrix of pixels. Each pixel stores a value e.g. elevation, temperature, population or  land cover typ. 
Since a raster is based on an image, the resolution is crucial. It defines the accuracy of the data and size of the pixels. 
![Raster data quality](../../fig/en_quality_raster.png)

In this picture you can see the same location, on the left as vector data, visualising streets and urban area, and on the right hand as raster data (satellite image), showing the land cover.

vector                     |  raster
:-------------------------:|:-------------------------:
![same location as vector data](../../fig/en_same_location_vector.png)  |  ![same location as raster data](../../fig/en_same_location_raster.png)  

#### Raster data formats

Raster data can have the following data formats:

| Filename extension| Name | Dscription |
| ----- | --- | --- |
|.tif/.tiff/.geotiff|Tag Image File Format|Common raster and image data format. Does not necessarily have georeference information. If a .tif file has georeferenc information it is referred to as GeoTIFF.|
|.nc|netCDF|Standard data format for scientific data like speed or temperature. Can be be a raster file. Can contain multible datasets|
|.asc|Esri ASCII Grid files|Old simple raster file format, always with georeference informations|



