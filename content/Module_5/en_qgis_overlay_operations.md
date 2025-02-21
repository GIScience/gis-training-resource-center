::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

## Overlay Operations (Clip, Dissolve, Buffer)

- Overlay operations allow us to combine the geometries of two layers in different ways (see {numref}`overlay_operations`). 
- The difference to spatial joins is that the __geometries are transformed in the process__, and not primarily the attributes. 

```{figure} /fig/overlay_operations.png
---
name: overlay_operations
width: 500 px
---
Visual representation of different overlay operations. 
```

Overlay operations include __Clipping, Buffering, and Dissolving__. In the next subchapters, we will take a 
look at each of these overlay operations in turn and provide some examples for humanitarian work.

### Clip

- The ![](/fig/mAlgorithmClip.png) `Clip` tool is used to cut a vector layer using the boundaries of another polygon layer. In other words, it extracts a portion of a dataset based on the boundaries of another. 
- It keeps only the parts of the features in the input layer that are inside the polygons of the overlay layer, producing a refined dataset.
- While the core attributes of the features remain the same, some properties, like area or length, may change after the clipping operation. If you've stored these properties as attributes, you might need to update them manually.

:::{card}
__Humanitarian Example:__
^^^
*Flood extent data for Pakistan is available, but the focus is on mapping flood damage in a specific administrative region. In this case, the flood layer can be clipped to the administrative boundaries of the area of interest.*
<!---*We have flood extent data for Pakistan, but we are currently working on a map showing the flood damage in a specific administrative region. In this case, we can take the flood layer and clip it to the administrative boundaries of the area of interest.*-->
:::

<!--CHECK IF THIS EXAMPLE IS NEEDED--->

The tool has two different input options:
* __Input layer__: Layer from which the selection is clipped
* __Overlay layer__: Area of interest to which the input layer will be clipped

```{figure} /fig/en_clip_sudan.PNG
---
width: 550 px
name: en_clip_sudan
---
Screenshot of the Clip tool with the input data.
```

### Exercise: Clipping a roads layer to administrative boundaries

Information on road infrastructure for humanitarian aid operations is of great importance 
and can be easily retrieved from open-source data sources like OpenStreetMap. However, this 
information is often included in extensive datasets that contain a significant amount of 
irrelevant details for specific operations or it covers a lot more area than is necessary 
for the operation. To make working with this data more efficient, it is common practice to 
clip the data to the area of interest. In addition to clipping, data can often be filtered, 
in order to remove data we are not interested in.

1. Load the OSM roads data from the HOT Export tool (part of the Humanitarian OpenStreetMap Team) [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Spatial_geodataprocessing/hotosm_sdn_roads_lines_shp.zip) 
as a new layer: __Road_infrastructure_Sudan.geojson__. 

2. Filter the layer by using the __query builder__ to only show __primary and residential roads__ ("highway" = 'primary' OR "highway" = 'residential')
3. Load the admin1 layer for Sudan which contains the district White Nile, __ne_10m_admin_1_Sudan_White_Nile.geojson__. They are downloaded from [Natural Earth Data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
4. Select the roads layer and open the __Clip__ dialogue from `Vector` > `Geoprocessing Tools`
    - Set roads as the __input layer__ and the district boundaries of White Nile as the __overlay layer__
    - Click __Run__ to generate a temporary layer called Clipped
7. You now have a tidy roads layer which contains the necessary information

````{dropdown} Solution: Clipping a roads layer to administrative boundaries
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_clip_roads.mp4"></video>
````


<!--REMOVED: GDAL Operators as not used frequently enough to need inclusion in this section-->

<!--GDAL Operators are needed?--

In addition to the standard QGIS operation __Clip__, there are two other more advanced tools for performing clipping processes. These tools are GDAL operations, which enable the definition of the clipping extent. This extent can be either a specific area or a mask layer. The second option is quite similar to the standard clipping process provided by QGIS.

```{figure} /fig/en_gdal_clipping_tools.PNG
---
width: 250 px
name: gdal_clipping_tools
---
The GDAL tools Clip vector by extent and Clip vector by mask layer
```

::::{tab-set}

:::{tab-item} Clip vector by extent

This operation clips any vector file to a given extent. This clip extent will be defined by a bounding box that should be used for the vector output file. It also has to be defined in the target CRS coordinates. There are different methods to define the bounding box, which are the great difference between this tool and the standard clipping process:
* Calculate from a layer: this uses the extent of a layer loaded into the current project
* Calculate from layout map: uses the extent of a layout map item in the active project
* Calculate from bookmark: uses the extent of a saved bookmark
* Use map canvas extent
* Draw on canvas: click and drag a rectangle delimiting the area to take into account
* Enter the coordinates as xmin, xmax, ymin, ymax

```{figure} /fig/en_clip_vector_by_extent.PNG
---
width: 450 px
name: en_clip_vector_by_extent
---
Screenshot of the tool Clip vector by extent
```

:::

:::{tab-item} Clip vector by mask layer
This operation uses a mask polygon layer to clip any vector layer. This operation only takes two input:
1. The input layer
2. The mask layer which is used as the clipping extent for the input vector layer

```{figure} /fig/en_clip_vector_by_mask_layer.PNG
---
width: 450 px
name: clip_vector_by_mask_layer
---
Screenshot of the tool Clip vector by mask layer
```

:::

::::

-->

### Dissolve

The ![](/fig/mAlgorithmDissolve.png) `Dissolve`-tool creates a new layer and merges overlapping features from 
one or two vector layers. You can pick one or more attributes to group together features that share the same 
value for those attributes. Alternatively, you can combine all features into one. If you're working with polygons, 
it will remove shared boundaries between them.

If you turn on the "Keep disjoint features separate" option when running the tool, it'll make sure that features or parts 
that don't overlap or touch each other are saved as separate features instead of being part of one big feature. This allows 
you to create several vector layers.

:::{card}
__Humanitarian Example:__
^^^
*Two datasets show the flood extent of two different flood events in the past year. Both layers overlap but show differences. Dissolve can create polygons that show the flooded area in the past year.*
:::

```{figure} /fig/en_buffer_dissolve.png
---
width: 550 px
name: buffer_dissolve
---
Buffer zones with dissolved (left) and with intact boundaries (right) showing overlapping areas <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```

In the next section on __buffers__ we will be using the __dissolve-tool__.

### Buffer

Buffering creates zones of predetermined distances around geometric features as a new polygon layer. These buffers surround the input vector features. This buffer zone is typically uniform and extends outward 
from the original input features, making it useful for various spatial analyses and mapping applications. Buffers can be created around points, lines, and polygons as shown in {numref}`buffering_options`.

Examples for analyses using buffers could be:
- Creating of buffer zones to protect the environment
- Analysing greenbelts around residential area
- Creating risk areas for natural disasters. 

:::{card} 
__Humanitarian Example:__
^^^
To analyze access to clean water sources, a scenario considers how far the population can walk to reach them. A 2 km buffer is created around a dataset of wells to visualize which areas fall within this distance. This method helps assess coverage and identify gaps in access to clean water.

:::

```{figure} /fig/en_buffer_point_line_polygon.png
---
width: 550 px
name: buffering_options
---
Different kinds of buffer zones <br /> (Adapted after [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```

There are several variations in buffering. The __buffer distance__ or __buffer size can vary__ according to the numerical values provided. 
The numerical values have to be defined in map units according to the Coordinate Reference System (CRS) used with the data. 

````{Attention}

```{figure} /fig/en_dist_in_degrees_error_msg.png
---
width: 450 px
name: dist_degree_error_message
---
The error message QGIS displays when performing distance based calculations in a geographic coordinate system
```
If...
- You get a projection warning message 
- Your layer(s) don't show up
- Layers look odd ‒ e.g. squashed
- Error message "using degrees" when using distances (as shown in {numref}`dist_degree_error_message`)
... it might be a [projection](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_projections.html) issue.

To solve it, try...

- Changing the CRS for the layer
- Reprojecting the layer

For example, if you are trying to make a buffer on a layer with a Geographical Coordinate System, QGIS will warn you and suggest to reproject the layer to a __metric Coordinate System__. This is because when you are using a metric coordinate system, the algorithm will use degrees to calculate the distance of the buffer size. However, the distance between degrees are not uniform and depend on the latitude (see {numref}`distance_longitudes`)

```{figure} /fig/en_dist_longitudes.png
---
name: distance_longitudes
width: 450 px
---
This image illustrates this – 10 degrees of longitude at the equator is 1,113km, but 10 degrees of
longitude at 70 degrees latitude is only 381km. (Source: [Ricky Angueria](https://x.com/RickyAngueira/status/1594030866132410368)).
```

This is why you’ll need to convert to a local/projected coordinate system to be able to specify distances in km/miles (e.g. when using the buffer tool).

````

### Exercise: Create 10km buffer around health centres

Another example relevant for humanitarian action can be the creation of a map which provides information 
about the coverage of health sites in the distance of 10 km.
To achieve this, a buffer of 10 km is created around points representing healthsites. In some cases, 
this will create buffer zones which overlap. In order to create a homogenous area, we can dissolve overlapping 
buffer zones. 

1. Download the __Sudan health sites__ data from [HDX](https://data.humdata.org/dataset/sudan-healthsites) as a shapefile
2. Load your new data into QGIS. Also add the district boundaries of Khartoum, __ne_10m_admin_1_Sudan_Khartoum.geojson__. 
They are also downloaded and adapted from [Natural Earth Data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
3. Clip your health sites to the boundaries of Karthoum district
4. __Reproject__ the health sites layer to a local coordinate system to enable setting distances in km
    - Vector menu > Data Management Tools > __Reproject Layer__
    - Select the __health sites__ layer as the input layer
    - Set the target __CRS to WGS 84 / UTM zone 36N__ (click the projections icon to search the full list of options)
    - Click  `Run` to reproject
5. Open the __Buffer__ tool by accessing `Vector` > `Geoprocessing Tools` > `Buffer`
    - Select the __reprojected layer__ as the input layer
    - Set the distance to __10km__
    - Check the option to __dissolve__ result
    - Leave the other options as defaults and click `Run`
6. Now you have a rough overview over the coverage with health sites for the district of Khartoum

````{dropdown} Solution: Create 10km buffer around health centres
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_buffer_health.mp4"></video>

1. 
2. 
3. 

````

