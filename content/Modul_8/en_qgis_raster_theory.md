# Remote Sensing and Raster data theorie 🛰️

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## What is Raster Data

Raster data is next to vector data a fundamental component of GIS and represents spatial information as a rectangular grid of cells or pixels that are each associated with a specific geographical information. Each cell contains a value representing a certain attribute, such as elevation, temperature or land cover within a specific area. Regarding their structure, geospatial rasters are very similar the representation of optical information in a digital picture, the different beeing that a geospatial raster is accompanied by spatial information that connects the data to a particular location. 

The data format raster data is particularly useful for capturing continuous phenomena across a geographical area such as temperature or elevation that do not suit the visualization with vector geometries due to their continuous nature without clear boundaries.

In each raster cell information is stored with a value that can be interpreted in the context of the attribute/phenomenon the raster expresses, for example elevation in meters or colour intensity in case of an image. 

```{figure} /fig/mod8_rasterdata_rasterbasics.png
---
name: Basic concept of a spatial raster
width: 500px
---

```

## Types of Raster Data
Raster data can be distinguished intwo two common types according to the type of information that is displayed: Continous and catigoral raster data.

Continuous raster data refers to datasets where the values assigned to each pixel represent continuous phenomena that vary smoothly across the area covered by the raster. Some examples of continuous rasters include:
1.	**Precipitation Maps** displaying variable precipitation sums
2.	**Digital Elevation Models** containing altidute values
3.	**Spatially variable Indices** such as the Normalized Difference vegetation Index (NDVI)

```{figure} /fig/mod8_rasterdata_DEM.png
---
name: 
width: 500px
---
Exemplary Digital Elevation Model of an area in the indian Himalayas
```

**Discontinous** rasters contain catigorical data, where each pixel represents a discrete classvalue rather than a value on a continuous scale. The information in these types of raster is sometimes also suitable for the storage with vector data. Some examples of classified maps include:
1.	**Landcover/Land Use Maps** with discrete classes
2.	**Tree height maps classified** as short, medium, and tall trees
3.	**Risk maps** with multiple distinct risk classes

```{figure} /fig/mod8_rasterdata_lulcexample.png
---
name: Basic concept of a spatial raster
width: 500px
---

```

## Properties of Raster data

### Spatial Extent
The spatial extent of a raster refers to the geographical area covered by the grid of cells in the raster dataset. It defines the boundaries of the raster dataset in terms of its geographical coordi-nates. The spatial extent is typically described by the minimum and maximum values of the spatial coordinates in every geographical direction (e.g. minimum and maximum latitude and longitude) that encompass all pixels of the raster.


**BEISPIEL ABBILDUNG**

### Spatial Resolution
The spatial resolution of a raster refers to the area represented by each individual pixel on the ground in the real world. It quantifies the level of detail of the spatial representation within the dataset. For example, a spatial resolution of 30 metres per pixel means that each pixel represents an area of 30x30 metres on the ground. High spatial resolution means smaller pixel sizes, resulting in finer detail and more accurate representation of spatial features within the dataset.

```{figure} /fig/mod8_rasterdata_spatialresolution.png
---
name: Different spatial resolutions of the same raster
width: 900px
---

```

### Coordinate Refernce Sytem (CRS)
As with vector data, the Coordinate Reference System (CRS) of a raster dataset refers to the spa-tial reference framework used to define the geographic location and orientation of the raster on the Earth's surface (CRS WIKI link). It provides a standardised way of representing spatial coor-dinates and ensures that raster data can be accurately geolocated and integrated with other geo-spatial datasets.<br><br>
The CRS includes a number of different parameters:<br>
1. **Coordinate system**: This defines how spatial coordinates are represented. Common coordinate systems include geographic (latitude and longitude) and projected (e.g. Universal Transverse Mercator - UTM).
2. **Datum**: The datum specifies the reference ellipsoid and geodetic parameters used to model the shape of the Earth. It ensures consistency of spatial measurements across different datasets (e.g. the WGS 84 ellipsoid).
3. **Unit**: The unit of measurement for spatial coordinates, such as metres (e.g. in UTM) or degrees in the case of geographical coordinates.
4. **Origin**: The origin or reference point of the coordinate system, which may vary depending on the projection method used.

### Metadata
Metadata for raster data consists of descriptive information that provides context and details about the raster dataset. It includes information such as the dataset source, creation date, spatial extent, spatial resolution, coordinate reference system (CRS), data type, units, compression tech-niques, processing steps, accuracy ratings, and copyright/licensing information.<br><br>
This metadata helps users to understand the content, origin, quality and appropriate use of raster data. It facilitates data discovery, evaluation and integration into geospatial workflows, ensuring that users can effectively interpret and use the data for their specific applications.

## File Format
There are multiple different file formats for storing an working with raster data. Following a short overview over the most common formats that you will likely come by as you work with spaptial rasters:
1.	**GeoTIFF (.tif/.tiff)**: Widely used file format, supports georeferencing and metadata.
2.	**GeoPackage (.gpkg)**: Open format for storing geospatial data, supports raster and vec-tor.
3.	**JPEG (.jpg/.jpeg) & PNG (.png)**: Common formats for images, lacks georeferencing.
4.	**Esri Grid (.adf)**: Esri's raster format, used in ArcGIS, supports georeferncing amd metadata
5.	**GeoPackage (.gpkg)**: Open format for storing geospatial data, supports raster and vec-tor.
