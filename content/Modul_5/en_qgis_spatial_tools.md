# Spatial Geodataprocessing

#### Introduction:
Spatial Geodataprocessing utilises spatial information to extract new and additional meaning from GIS data. This data processing is particularly important in humanitarian work and the planning of aid operations. For instance, the overlay operation __Clip__ can be employed to extract specific areas of interest from multiple layers, allowing us to focus our attention where it is most needed. Meanwhile, the __Dissolve__ operation allows us to simplify complex datasets, revealing broader trends and patterns that inform our decision-making process. Using __Buffer__, we can create zones around features to help identify vulnerable areas and plan evacuation routes in the event of a flooding event. Additionally, __Spatial Joins__ can enrich datasets by incorporating additional information from related layers. They can be crucial for understanding the context of a crisis and tailoring our response accordingly. Similarly, __Spatial Selections__ enable us to target specific features based on their spatial relationship with other elements, facilitating focused interventions.

In this section, we will explore overlay operations, focusing particularly on the operations of __Clip__, __Dissolve__, and __Buffer__. These operations enable us to combine geometries from two layers in various ways. In addition to these, we will cover __Spatial joins__ and __Spatial selections__ in this section. Spatial joins offer opportunities to enhance the attributes of the input layer by incorporating additional information from the join layer, utilizing their spatial relationship. These relationships can also be used to select features from an input layer based on their location in comparison to another layer. All of these operations make use of the spatial information in the provided input data to either enrich the data or perform various analyses.

## Clip

The ![](/fig/mAlgorithmClip.png) `Clip` tool is used to cut a vector layer with the boundaries of another polygon layer. It keeps only the parts of the features in the input layer that are inside the polygons of the overlay layer, creating a refined dataset. While the core attributes of the features remain the same, some properties, like area or length, may change after the clipping operation. If you've stored these properties as attributes, you might need to update them manually.

The tool has two different input option:
* __Input layer__: Layer from which the selection is clipped
* __Overlay layer__: Area of interest that the input layer will be clipped to.

```{figure} /fig/en_clip_sudan.PNG
---
width: 75%
name: en_clip_sudan
---
Screenshot of the Clip tool with the input data
```
Information on road infrastructure for humanitarian aid operations is of great importance and can be easily retrieved from open-source data sources like OpenStreetMap. However, this information is often included in extensive datasets that contain a significant amount of irrelevant details for specific operations, or it covers a lot more area than is necessary for the operation. To make working with this data more efficient, it is common practice to clip the data to the area of interest. In addition to clipping, data can often be filtered, as described in the first part of Module 5.

>here it is not clear what the first part of module 5 is, maybe add link

### Exercise: Clipping a roads layer to administrative boundaries

1. Load the OSM roads data from the [HOT Export tool](https://export.hotosm.org/v3/exports/918cf68d-dfd7-40f1-ab46-4f0426dfaf68/) (part of the Humanitarian OpenStreetMap Team) as a new layer: __Road_infrastructure_Sudan.geojson__.

```{figure} /fig/en_screenshot_hot_export_tool.PNG
---
width: 75%
name: en_screenshot_hot_export_tool
---
Screenshot of the HOT Export tool to download your OSM data
```

2. Filter the layer by using the __query builder__ to only show __primary and residential roads__ ("highway" = 'primary' OR "highway" = 'residential')
3. Load the admin1 layer for Sudan which contains the district White Nile, __ne_10m_admin_1_Sudan_White_Nile.geojson__. They are downloaded and adapted from [Natural Earth Data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
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
width: 40%  
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
width: 75%
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
width: 75%
name: clip_vector_by_mask_layer
---
Screenshot of the tool Clip vector by mask layer
```

:::

::::

## Buffer
The concept of ![](/fig/mAlgorithmBuffer.png) __buffering__ in QGIS for vector data, refers to the process of creating a new polygon layer with areas that represent a __certain distance__ or __buffer around existing vector features__. This buffer zone is typically uniform and extends outward from the original features, making it useful for various spatial analyses and mapping applications. Examples for such analyses could be the creation of buffer zones to protect the environment, analyse greenbelts around residential areas or create risk areas for natural disasters. Buffer can be created around points, lines and polygons as shown in the figure below.

```{figure} /fig/en_buffer_point_line_polygon.png
---
width: 100%
name: spatial_relations
---
Different kinds of buffer zones <br /> (Adapted after [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```
There are several variations in buffering. The __buffer distance__ or __buffer size can vary__ according to the numerical values provided. The numerical values have to be defined in map units according to the Coordinate Reference System (CRS) used with the data. 

```{Attention}
If you are trying to make a buffer on a layer with a Geographical Coordinate System, processing will warn you and suggest to reproject the layer to a __metric Coordinate System__.
```

In the case of humanitarian action, buffering can be used to create a map which provides information about the coverage of health sites in the distance of 10 km. The health sites are points and can be buffered with 10 km. In a next step, the results can be dissolved if two buffer zones overlap and create a homogoneous area. This examples will be done in the next step.

### Exercise: Create 10km buffer around health centres

1. Download the __Sudan health sites__ data from [HDX](https://data.humdata.org/dataset/sudan-healthsites) as a shapefile
2. Load your new data into QGIS. Also add the district boundaries of Khartoum, __ne_10m_admin_1_Sudan_Khartoum.geojson__. They are also downloaded and adapted from [Natural Earth Data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
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
````

## Dissolve
The ![](/fig/mAlgorithmDissolve.png) `Dissolve` operation was already mentioned in the later part of the previous exercise. The dissolve tool combines features in a vector layer to make new ones. You can pick one or more attributes to group together features that share the same value for those attributes. Alternatively, you can combine all features into one. The tool will convert the shapes into multi-geometries, and if you're working with polygons, it'll remove shared boundaries between them.

If you turn on the "Keep disjoint features separate" option when running the tool, it'll make sure that features or parts that don't overlap or touch each other are saved as separate features instead of being part of one big feature. This allows you to create several vector layers.

```{figure} /fig/en_buffer_dissolve.png
---
width: 100%
name: buffer_dissolve
---
Buffer zones with dissolved (left) and with intact boundaries (right) showing overlapping areas <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
```

## Spatial joins
Spatial joins in QGIS enhance the attributes of the input layer by adding additional information from the join layer, relying on their __spatial relationship__. This process enriches your data by incorporating relevant details from one layer into another based on their geographical associations.

Various types of spatial relations exist between the source feature and the target feature, enabling their potential linkage. The subsequent list outlines these distinct options and provides descriptions, all oriented around the lower figure for clarity.

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

```{figure} /fig/en_select_by_location.png
---
width: 100%
name: spatial_relations
---
Looking for spatial relations between layers <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location), Version 3.28)
```

QGIS provides a range of tools that allow users to delve into spatial relationships and leverage them for enhancing their datasets.

::::{tab-set}

:::{tab-item} Join attributes by location
This tool takes an input vector layer and creates a new vector layer that is an extended version of the input, with additional attributes in its attribute table.

The additional attributes and their values are taken from a __second vector layer__. For this layer a __spatial criteria__ is applied to select the values from it that are added to each feature from the first layer.

```{figure} /fig/en_join_attributes_by_location.PNG
---
width: 75%
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by location
```

:::

:::{tab-item} Join attributes by location (summary)
When performing additional calculations in combination with a spatial join, the QGIS tool  __Join attributes by location (summary)__ is really helpful. This functionality closely resembles the previously outlined workflow; however, the algorithm extends its capabilities by calculating statistical summaries for the values from matching features in the second layer. These summaries encompass a wide range of options, including __minimum__ and __maximum values__, __mean values__, as well as __counts__, __sums__, __standard deviation__, and more.

```{figure} /fig/en_join_attributes_by_location_summary.PNG
---
width: 75%
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by location (summary)
```

:::

:::{tab-item} Join attributes by nearest
It takes an input vector layer and uses this information to create a new vector layer. The new layer incorporates additional fields in its attribute table, and these supplementary attributes are obtained from a second vector layer. The joining of features occurs by __identifying the closest features__ from each of these layers.

By default, this operation connects each feature with its nearest counterpart. However, it also offers the flexibility to join with the k-nearest neighboring features if needed.

Furthermore, if a maximum distance is specified, only the features that are within this designated distance will be considered as suitable matches for the joining process.

```{figure} /fig/en_join_attributes_by_nearest.PNG
---
width: 75%
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by nearest
```

:::

::::

In the aftermath of flooding events, data on the affected population and the extent of flooding is crucial. This information can be refined from a nationwide dataset to provide specific numbers for individual districts or states. This can aid in identifying the areas most heavily impacted, leading to more efficient relief operations. In the upcoming exercise, we will calculate the total flooding extent in square kilometers and the affected population for the state of Unity State, South Sudan. To accomplish this, we will utilize the __Join attributes by location (summary)__ tool.

### Exercise: Calculate sum of affected population and flooded area for the Area of interest

1. Load the necessary data for this exercise into your QGIS. Both datasets were downloaded from HDX:
    - [South Sudan - Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-ssd):<br /> __State_Unity_South_Sudan.geojson__
    - [Satellite detected water extents between 11 and 15 August 2023 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-11-and-15-august-2023-over-south-sudan): __VIIRS_20230811_20230815_MaximumFloodWaterExtent_SouthSudan.geojson__
2. Locate the tool named __Join attribute by location (summary)__
    - Choose __state boundaries__ as the target layer for joining features
    - Set __intersect__ as the spatial relationship
    - Select  __flood extent layer__ as the comparison layer
    - Specify the fields to be summarized as __Area_km2__ and __Pop__
    - Choose __sum__ as the type of summaries to be calculated
    - Click Run to start the process
3. Once completed, you will have access to information on the __total affected population__ and __flooded areas__ for the entire state of Unity.


````{dropdown} Solution: Calculate sum of affected population and flooded area for the Area of interest
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_spatial_join.mp4"></video>
````

You can find further information about spatial joins by referring to the QGIS documentation, specifically in the section [Join attributes by location](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location#join-attributes-by-location).

## Select by location
Next to spatial joins, it is also possible to __create a selection in a vector layer__. The criteria for the feature selection is __based on__ the previously described __spatial relationships__ between each feature and the features in an additional layer. The feature selection may be visible in the map view or can be seen in the attribute table.

For this process, we select an input layer that defines the features, and these features are subsequently compared to those in a second input layer. The figure below illustrates an example where we examine health sites in a particular region of Senegal and compare them to flooded areas within the same region. This analysis allows us to identify the health sites that are most vulnerable to flooding in that particular area.

```{figure} /fig/en_ex2_select_by_location_health.PNG
---
width: 70%
name: select_by_location
---
Screenshot of the Select by location tool
```

## Centroids
This process creates a new point layer, with points representing the centroids of the geometries of the input layer. 

The centroid is a single point that shows the middle of all the parts of a feature. It can be outside the feature or on each part of it. An example would be a point, representing a polygon. 

The attributes of the points in the output layer are the same as for the original features.

Centroids can be used in spatial operations such as __spatial joins__ to represent a polygon as points.

```{figure} /fig/en_centroids_screenshot.png
---
width: 80%
name: en_qgis_centroids
---
The black points represent the centroids of the features of the input layer.
```


