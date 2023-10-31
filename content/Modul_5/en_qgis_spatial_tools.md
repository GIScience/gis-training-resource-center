# Spatial Geodataprocessing

#### Introduction:
The first part of this module explores overlay operations, focusing specifically on the operations of __Clip__, __Dissolve__, and __Buffer__. These operations enable us to combine geometries from two layers in various ways. In addition to these, we will cover __Spatial joins__ in this section. Spatial joins offer opportunities to enhance the attributes of the input layer by incorporating additional information from the join layer, utilizing their spatial relationship. All of these operations make use of the spatial information in the provided input data to either enrich the data or perform various analyses.

## Clip

This tool is used to cut a vector layer with the boundaries of another polygon layer. It keeps only the parts of the features in the input layer that are inside the polygons of the overlay layer, creating a refined dataset. While the core attributes of the features remain the same, some properties like area or length may change after the clipping operation. If you've stored these properties as attributes, you might need to update them manually.

The tool has two different input option:
* Input layer: Layer from which the selection is clipped
* Overlay layer: Area of interest that the input layer will be clipped to.

```{figure} /fig/en_clip_sudan.PNG
---
height: 300px
name: en_clip_sudan
---
Screenshot of the Clip tool with the input data
```
Information on road infrastructure for humanitarian aid operations is of great importance and can be easily retrieved from open-source data sources like OpenStreetMap. However, this information is often included in extensive datasets that contain a significant amount of irrelevant details for specific operations. To make working with this data more efficient, it is common practice to clip the data to the area of interest. In addition to clipping, data can often be filtered, as described in the first part of Module 5

### Exercise: Clipping a roads layer to administrative boundaries

1. Load the OSM roads data from the [HOT Export tool](https://export.hotosm.org/v3/exports/918cf68d-dfd7-40f1-ab46-4f0426dfaf68/) (part of the Humanitarian OpenStreetMap Team) as a new layer __Road_infrastructure_Sudan.geojson__.
```{figure} /fig/en_screenshot_hot_export_tool.PNG
---
height: 280px
name: en_screenshot_hot_export_tool
---
Screenshot of the HOT Export tool to download your OSM data
```
2. Filter the layer by using the __query builder__ to only show __primary and residential roads__ ("highway" = 'primary' OR "highway" = 'residential')
3. Load the admin1 layer for Sudan which contains the district White Nile, __ne_10m_admin_1_Sudan_White_Nile.geojson__
4. Select the roads layer and open the __Clip__ dialogue from Vector > Geoprocessing Tools
    - Set roads as the __input layer__ and the district boundaries of White Nile as the __overlay layer__
    - Click __Run__ to generate a temporary layer called Clipped
7. You now have a tidy roads layer which contains the necessary information

````{dropdown} Solution: Clipping a roads layer to administrative boundaries
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_clip_roads.mp4"></video>
````

In addition to the standard QGIS operation __Clip__, there are two other, more advanced tools for performing clipping processes. These tools are GDAL operations, which enable the definition of the clipping extent. This extent can be either a specific area or a mask layer. The second option is quite similar to the standard clipping process provided by QGIS.

```{figure} /fig/en_gdal_clipping_tools.PNG
---
height: 60px
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
height: 350px
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
height: 350px
name: clip_vector_by_mask_layer
---
Screenshot of the tool Clip vector by mask layer
```

:::

::::

## Buffer
The concept of __buffering__ in QGIS for vector data, refers to the process of creating a new polygon layer with areas that represent a __certain distance__ or __buffer around existing vector features__. This buffer zone is typically uniform and extends outward from the original features, making it useful for various spatial analyses and mapping applications. Examples for such analyses could be the creation of buffer zones to protect the environment, analyse greenbelts around residential areas or create risk areas for natural disasters. Buffer can be created around points, lines and polygons as shown in the figure below.

```{figure} /fig/en_buffer_point_line_polygon.png
---
height: 350px
name: spatial_relations
---
Different kinds of buffer zones <br /> (Adapted after [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```
There are several variations in buffering. The __buffer distance__ or __buffer size can vary__ according to the numerical values provided. The numerical values have to be defined in map units according to the Coordinate Reference System (CRS) used with the data. 

```{Attention}
If you are trying to make a buffer on a layer with a Geographical Coordinate System, processing will warn you and suggest to reproject the layer to a __metric Coordinate System__.
```

In the case of humanitarian action buffering can be used to create a map which provides information about the coverage of health sites in the distance of 10 km. The health sites are points and can be buffered with 10 km. In a next step, the results can be dissolved if two buffer zones overlap and create a homogoneous area. This examples will be done in the next step.

### Exercise: Create 10km buffer around health centres

1. Download the Sudan health sites data from [HDX](https://data.humdata.org/dataset/sudan-healthsites) as a shapefile
2. Load your new data into QGIS. Also add the district boundaries of Khartoum, __ne_10m_admin_1_Sudan_Khartoum.geojson__
3. Clip your health sites to the boundaries of Karthoum district
4. __Reproject__ the health sites layer to a local coordinate system to enable setting distances in km
    - Vector menu > Data Management Tools > __Reproject Layer__
    - Select the __health sites__ layer as the input layer
    - Set the target __CRS to WGS 84 / UTM zone 36N__ (click the projections icon to search the full list of options)
    - Click Run to reproject
5. Open the __Buffer__ tool by accessing Vector > Geoprocessing Tools > Buffer
    - Select the __reprojected layer__ as the input layer
    - Set the distance to __10km__
    - Check the option to __dissolve__ result
    - Leave the other options as defaults and click Run

````{dropdown} Solution: Create 10km buffer around health centres
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_buffer_health.mp4"></video>
````

## Dissolve
The dissolve operation was already mentioned in the later part of the previous exercise. The dissolve tool combines features in a vector layer to make new ones. You can pick one or more attributes to group together features that share the same value for those attributes. Alternatively, you can combine all features into one. The tool will convert the shapes into multi-geometries, and if you're working with polygons, it'll remove shared boundaries between them.

If you turn on the "Keep disjoint features separate" option when running the tool, it'll make sure that features or parts that don't overlap or touch each other are saved as separate features instead of being part of one big feature. This allows you to create several vector layers.

```{figure} /fig/en_buffer_dissolve.png
---
height: 175px
name: buffer_dissolve
---
Buffer zones with dissolved (left) and with intact boundaries (right) showing overlapping areas <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```

## Spatial joins
Spatial joins in QGIS enhance the attributes of the input layer by adding additional information from the join layer, relying on their __spatial relationship__. This process enriches your data by incorporating relevant details from one layer into another based on their geographical associations.

```{figure} /fig/en_select_by_location.png
---
height: 300px
name: spatial_relations
---
Looking for spatial relations between layers <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location), Version 3.28)
```
Various types of spatial relations exist between the source feature and the target feature, enabling their potential linkage. The subsequent list outlines these distinct options and provides descriptions, all oriented around the upper figure for clarity.

::::{tab-set}

:::{tab-item} Intersect
Tests whether the geometry of the two layers intersects with one another. Returns 1 (true) if the geometries spatially intersect (share any portion of space, could be overlap or touch) and 0 if they don’t. In the picture above, this will return circles 1, 2 and 3.
:::

:::{tab-item} Contain
Returns 1 (true) if and only if no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a. In the picture, no circle is returned, but the rectangle would be if you would look for it the other way around, as it contains circle 1 completely. This is the opposite of are within.
:::

:::{tab-item} Disjoint
Returns 1 (true) if the geometries do not share any portion of space (no overlap, not touching). Only circle 4 is returned.
:::

:::{tab-item} Equal
Returns 1 (true) if the geometries are exactly the same. No circles will be returned.
:::

:::{tab-item} Touch
Tests whether a geometry touches another. Returns 1 (true) if the geometries have at least one point in common, but their interiors do not intersect. Only circle 3 is returned.
:::

:::{tab-item} Overlap
Tests whether geometries overlap. Returns 1 (true) if the geometries share space, are of the same dimension, but are not completely contained by each other. Only circle 2 is returned.
:::

:::{tab-item} Are within
Tests whether one geometry is within another. Returns 1 (true) if geometry a is completely inside geometry b. Only circle 1 is returned.
:::

:::{tab-item} Cross
Returns 1 (true) if the supplied geometries have some, but not all, interior points in common and the actual crossing is of a lower dimension than the highest supplied geometry. For example, a line crossing a polygon will cross as a line (true). Two lines crossing will cross as a point (true). Two polygons cross as a polygon (false). In the picture, no circles will be returned.
:::

::::

QGIS provides a range of tools that allow users to delve into spatial relationships and leverage them for enhancing their datasets.

::::{tab-set}

:::{tab-item} Join attributes by location
This tool takes an input vector layer and creates a new vector layer that is an extended version of the input, with additional attributes in its attribute table.

The additional attributes and their values are taken from a second vector layer. For this layer a spatial criteria is applied to select the values from it that are added to each feature from the first layer.

```{figure} /fig/en_join_attributes_by_location.PNG
---
height: 500px
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by location
```

:::

:::{tab-item} Join attributes by location (summary)
For performing additional calculations in combination with a spatial join, the QGIS tool  __Join attributes by location (summary)__ is really helpful. This functionality closely resembles the previously outlined workflow; however, the algorithm extends its capabilities by calculating statistical summaries for the values from matching features in the second layer. These summaries encompass a wide range of options, including __minimum__ and __maximum values__, __mean values__, as well as __counts__, __sums__, __standard deviation__, and more.

```{figure} /fig/en_join_attributes_by_location_summary.PNG
---
height: 500px
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by location (summary)
```

:::

:::{tab-item} Join attributes by nearest
It takes an input vector layer and uses this information to create a new vector layer. The new layer incorporates additional fields in its attribute table, and these supplementary attributes are obtained from a second vector layer. The joining of features occurs by identifying the closest features from each of these layers.

By default, this operation connects each feature with its nearest counterpart. However, it also offers the flexibility to join with the k-nearest neighboring features if needed.

Furthermore, if a maximum distance is specified, only the features that are within this designated distance will be considered as suitable matches for the joining process.

```{figure} /fig/en_join_attributes_by_nearest.PNG
---
height: 500px
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by nearest
```

:::

::::

Further helpful information on the processes of spatial joins can be found on the QGIS documentation under [Join attributes by location](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location#join-attributes-by-location).

## Data sources

HOT Export tool for road infrastructure
Natural Earth Data for country and district boundaries (Admin 1 - States, Provinces) and then Download states and provinces
HDX for health sites