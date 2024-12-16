# Spatial data processing

## Introduction:

Spatial processing uses spatial information to extract new meaning from GIS data. It does so by using the __spatial relationship__ of different layers or features. Spatial relationships describe how things are located in relation to one another. In humanitarian work, this helps answer critical questions like “Which communities are near a water source?” or “Which areas are isolated from health services?”. Or, we might want to identify the best locations for distributing aid, assess flood risk areas, or plan evacuation routes.

We have already encountered spatial relationships in module 3 in the subchapter on __[geometrical operators](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_data_queries.html#geometric-operators)__— also called geometrical predicates in QGIS. 
The table below describes spatial relationships and gives examples when these spatial relationships are relevant in humanitarian aid. 

| __Spatial Relationship__ | __Description__ | __*Humanitarian Example*__ |
| ------------------------ | --------------- | -------------------------- |
| __Proximity__            | How close one thing is to another | *Find the nearest shelters to a displaced community* | 
| __Containment__          |  Whether something is inside another area/polygon | *Identify which schools are within a specific conflict-affected zone* | 
| __Intersection__         |  Identify geometric features that overlap | *Look for areas where damaged infrastructure overlaps with vulnerable populations* | 
| __Adjacency__            | Geometric features that share a point or a boundary | *Identify regions bordering a conflict zone that may be at risk of displacement* |
| __Connectivity__         | How things are connected through networks such as roads, rivers, or even trade routes | *Map the shortest path between villages and hospitals to plan emergency evacuations* |
| __Direction__            | Relative position, like north, south, east, west, or relative position to the flow of a river, for example | *Locate villages north of a river that are cut off due to flooding and inaccessibility of connecting bridges* | 

QGIS offers a variety of spatial processing tools that we can use to analyse and create new insights using these spatial relationships. For instance:
- __Spatial Joins__ let us join attribute values from one layer to another based on their spatial relationship. This enables us to enrich datasets and 
incorporate additional information from  layers, which can help us understand a situation.
- The overlay operation __Clip__ can be employed to extract specific areas of interest from multiple layers, allowing us to focus our attention where it is most needed.
- The __Dissolve__ operation allows us to simplify geometries by joining geometries from two distinct layer. 
- Using __Buffer__, we can create zones around features to help identify vulnerable areas and plan evacuation routes in the event of a flooding event. 
- __Centroids__ creates point in the geometric centre of the geometries of a layer. This is especially useful when creating graduated symbol maps


```{figure} /fig/en_module5_spatial_geodataprocessing.PNG
---
width: 550 px
name: module5_spatial_geodataprocessing
---
Different spatial geoprocessing tools. Source: Adapted from [Saylor Academy](https://saylordotorg.github.io/text_essentials-of-geographic-information-systems/s11-geospatial-analysis-i-vector-o.html)
```

In this chapter, we will first explore __spatial joins__. Spatial joins, 
for example, allow us to import attributes from one layer to another on the basis of their location 
in relation to geofeatures in another layer. These Spatial relationships can also be used to select 
features of a layer. Furthermore, we will go over the spatial processing tools __buffer__, __clip__, 
and __dissolve__. These operations allow us to combine geometries from two layers in various ways (see 
{numref}`module5_spatial_geodataprocessing`).

<!--

2. Spatial joins
3. Buffer
4. Clip
5. Dissolve

THEN: humanitarian examples.

-->


<!---All of these operations make use of the spatial information in the provided input data to either enrich the data or perform various analyses.-->



<!---## Select by location

Next to spatial joins, it is also possible to __create a selection in a vector layer__. The criteria for the feature selection is __based on__ the previously described __spatial relationships__ between each feature and the features in an additional layer. The feature selection may be visible in the map view or can be seen in the attribute table.

For this process, we select an input layer that defines the features, and these features are subsequently compared to those in a second input layer. The figure below illustrates an example where we examine health sites in a particular region of Senegal and compare them to flooded areas within the same region. This analysis allows us to identify the health sites that are most vulnerable to flooding in that particular area.

```{figure} /fig/en_ex2_select_by_location_health.PNG
---
width: 550 px
name: select_by_location
---
Screenshot of the Select by location tool
```

-->



## Spatial joins

Joins are ways to combine two different data layers. In general, there are two types of joins: 
__non-spatial joins__ and __spatial joins__. Non-spatial joins rely on specific attribute values, 
which are used as ID-fields, to combine two layers. These are covered in the chapter 
"[Non-spatial processing tools](/content/Modul_5/en_qgis_non_spatial_tools.md)" in this module. 
Sometimes we want to combine information from different layers that don't share a common value. 
In these cases, we can use spatial joins, which let us join data based on location rules. 
Spatial joins in QGIS enhance the attributes of the input layer by adding additional information from the join layer, relying on their
__spatial relationship__. This process enriches your data by incorporating relevant details from one layer into another based on their 
geographical associations. In QGIS, a spatial join creates a new layer by comparing the features of one layer to another, depending on 
their spatial relationship. 


For example:

- Any point __within__ a polygon should inherit attributes of the polygon
- Only keep regions which __contain__ an airport.


::::{card}
__Humanitarian Example:__
^^^
*We have a flood depth model and we want to find out which buildings are flooded under this scenario. We can find this out by performing a spatial join to add the flood depth to the polygon layer with the houses*

*The resulting map could look something like this* 

```{figure} /fig/en_flood_damage_assessement_libya.png
---
name: flood damage assessement
width: 450 px
---
A building footprint layer combined with a flood extent layer. By joining them, we can assess which houses are at risk to be damaged by flooding (Source: REACH).
```


::::

Spatial joins rely on the geometrical operators. In the tabs below, you can find the different geometrical operators available in QGIS and how they affect the data processing. 


::::{tab-set}

:::{tab-item} Intersect
Tests whether the geometry of the two layers intersects with one another. The algorithm returns the value "True" (1), 
if the geometries intersect spatially. This means that they share any portion of space, overlap, or touch. If they don't 
overlap, the algorithms returns the value "False" (0). In the picture below, the algorithm will return the circles __1, 2, and 3__.
:::


:::{tab-item} Disjoint
Disjoint features do not share any portion of space. This means that they don't touch or overlap. 
In the picture below, the algorithm would output a layer with only the circle 4. 
:::

:::{tab-item} Equal
The algorithms returns a layer with geometries that are exactly the same (all the points and lines are equal). In the 
picture below, no circles are returned (added to the output layer).  
:::

:::{tab-item} Touch
Tests whether a geometry touches another. The algorithm outputs a new layer with the geometries that have at least one 
point in common, but their interiors do not intersect. In the image below, only circle 3 is returned. 
:::

:::{tab-item} Overlap
Tests whether geometries overlap. Returns geometries if they share space, are of the same dimension, but are not completely 
contained by each other. In the image below, only circle 2 is returned. 
:::

:::{tab-item} Are within
Tests whether one geometry is within another. Returns geometries a if they are completely inside of geometry b. Only circle 
1 is returned.
:::

:::{tab-item} Contain
Returns geometries if and only if no points of b lie in the exterior of a, and at least one point of the interior of b lies 
in the interior of a. In the picture, no circle is returned, but the rectangle would be if you would look for it the other 
way around, as it contains circle 1 completely. This is the opposite of "are within".
:::

:::{tab-item} Cross
Returns geometries that have some, but not all, interior points in common and the actual crossing is of a lower dimension 
than the highest supplied geometry. For example, a line crossing a polygon will cross as aline (true). Two lines crossing 
will cross as a point (true). Two polygons cross as a polygon (false). In the picture below, no circles will be returned. 
:::

::::

```{figure} /fig/en_select_by_location.png
---
width: 600 px
name: spatial_relations
---
Looking for spatial relations between layers <br /> (Source: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location), Version 3.28)
```

### Performing a spatial join


```{admonition} Now it's your turn!
:class: tip

Practical exercise is crucial to understand how GIS, and QGIS, works. You can follow along by download the necessary data.

```

```{figure} /fig/en_spatial_join_example.png
---
name: spatial_join_example_healthsites
width: 400 px
---
An example of a situation where you will use a spatial join (Source: BRC)
```

In the example above ({numref}`spatial_join_example_healthsites`), we have a dataset containing the healthsites by healthsite.io
and a dataset with the administrative boundaries (adm2) of Nigeria. We want to know in which state each healthsite is located. 
To do this, we need to use the tool "Join Attributes by Location":

::::{margin}

```{tip}
You can find activate the processing toolbox panel by navigating to `View` > `Panels` > `Processing Toolbox`. It should appear on 
the right side of your screen
```

::::

1. Download the necessary datasets from HDX 
    - [nigeria-healthsites-shp](https://data.humdata.org/dataset/nigeria-healthsites)
    - [nga_adm_osgof_20190417.zip](https://giscience.github.io/gis-training-resource-center/content/Modul_5/en_qgis_spatial_tools.html)
2. Unzip the files, create a new QGIS-project, and load the files into the QGIS-project.
3. Search for the tool __"Join Attributes by Location"__ in the processing toolbox and <kbd>Double-Click</kbd> on it. A new window will open 
(see {numref}`join_by_location_ex1`). 
4. Use the health facilities layer as the target ("Join to feature in") and the adm2 layer as the comparison layer ("By comparing to"). 
5. Use the `are within` geometrical predicate.
6. Select the fields to add: `ADM2_EN`, `ADM2_PCODE`
7. Select `Discard records that could not be joined`
8. Click `Run` to proceed; the log should confirm success.
9. A new (temporary) layer called "Joined features" will appear in your layers-panel
10. <kbd>Right-click</kbd> on the layer and select "Export" or "Make Permanent" to save the new layer.

```{figure} /fig/en_3.36_join_by_location_ex1.png
---
name: join_by_location_ex1
width: 500 px
---
Setting the parameters to perform the spatial join in QGIS 3.36
```

Congratulations, we now have added the information about the administrative region to the health facilities layer!
We can symbolise the joined layer with the categorised symbology to verify if it worked (see {numref}`spatial_join_ex1_results_categorised`). Note that 
the points in the original dataset which were outside of Nigeria's border have been discarded as they could not be joined.

```{figure} /fig/spatial_join_ex1_results_categorised.png
---
name: spatial_join_ex1_results_categorised
width: 500 px
---
The different colours for the points indicate that they are located in a different state (adm2).
```

### More spatial join-tools in QGIS

By default, QGIS provides three different tools to perform spatial joins. The first, and the most common one, is the tool 
__"Join attributes by location"__. Furthermore, there are also the tools __"Join attributes by location (summary)"__ and 
__"Join attributes by nearest"__.

:::::{tab-set}

::::{tab-item} Join attributes by location

This tool takes two input layers and creates a new vector layer which has the attributes of both layers in its attribute table.
The first input layer (see "Join to features in" in {numref}`join_attributes_by_location`) dictates which geometric features will be copied to the new 
layer. The second input layer (see "By comparing to" in {numref}`join_attributes_by_location`) dictates the attributes that will be added to the new 
layer on top of the attributes of the first input layer. You can select which of these attributes should be transferred to the new layer. 


```{figure} /fig/en_spatial_join_1.PNG
---
width: 450 px
name: join_attributes_by_location
---
The "Join Attributes by Location"-tool in QGIS 3.36.
```

::::

::::{tab-item} Join attributes by location (summary)

This tool is similar to the "Join Attributes by Location"-tool. However, on top of adding the attributes from one layer to another, this algorithms also 
calculates statistical summaries for the values from matching features in the second layer. These summaries include a wide range of options, such as 
__minimum and maximum values__, __mean values__, as well as __counts__, __sums__, __standard deviation__, and more. 

```{figure} /fig/en_spatial_join_3.PNG
---
width: 450 px
name: join_attribute_by_location_summary
---
Screenshot of the tool Join attributes by location (summary) in QGIS 3.36
```

::::

::::{tab-item} Join attributes by nearest

This type of spatial join is similar to the other two joins but the joining of features occurs by 
__identifying the closest features__ from each of these layers. Furthermore, if a maximum distance 
is specified, only the features that are within this designated distance will be considered as 
suitable matches for the joining process.


```{figure} /fig/en_spatial_join_2.PNG
---
width: 400 px
name: join_attribute_by_location_nearest
---
Screenshot of the tool Join attributes by nearest in QGIS 3.36
```

::::

:::::

:::{note}
A detailed description of the functions and settings of these tools can be found in the [QGIS documentation](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location)

:::

### Exercise: Calculate sum of affected population and flooded area for the Area of interest


In the aftermath of flooding events, data on the affected population and the extent of flooding is crucial. 
This information can be refined from a nationwide dataset to provide specific numbers for individual districts 
or states. This can aid in identifying the areas most heavily impacted, leading to more efficient relief 
operations. In the upcoming exercise, we will calculate the total flooding extent in square kilometers and 
the affected population for Unity State, South Sudan. To accomplish this, we will utilize the 
__Join attributes by location (summary)__ tool.

1. Load the necessary data for this exercise into your QGIS. Both datasets were downloaded from HDX:
    - [South Sudan - Subnational Administrative Boundaries](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Spatial_Join/State_Unity_South_Sudan.zip):<br /> __State_Unity_South_Sudan.shp__
    - [Satellite detected water extents between 11 and 15 August 2023 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-11-and-15-august-2023-over-south-sudan): Download the folder __FL20220424SSD_SHP.zip__, unzip it, and search for the file __VIIRS_20230811_20230815_MaximumFloodWaterExtent_SouthSudan.shp__
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



## Overlay Operations (Clip, Dissolve, Buffer)

Overlay operations allow us to combine geometries of two layers in different ways (see {numref}`overlay_operations`). The difference to spatial 
joins is that the geometries are transformed in the process. 

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

The ![](/fig/mAlgorithmClip.png) `Clip` tool is used to cut a vector layer using the boundaries of another polygon layer. 
In other words, it extracts a portion of a dataset based on the boundaries of another. It keeps only the 
parts of the features in the input layer that are inside the polygons of the overlay layer, producing a refined dataset. While the core 
attributes of the features remain the same, some properties, like area or length, may change after the clipping operation. If you've 
stored these properties as attributes, you might need to update them manually.

:::{card}
__Humanitarian Example:__
^^^

*We have flood extent data for Pakistan, but we are currently working on a map showing the flood damage in a specific administrative region. In this case,
we can take the flood layer and clip it to the administrative boundaries of the area of interest.*
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

<!--GDAL Operators are needed?--->

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

*Our data shows roads in segments by type. We dissolve the segments to 
create a single road layer, categorized by road type.*

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
*We need to assess which areas live close enough to clean water sources so the population can easily reach them by walking. 
In this case, we can create buffer zones of 2 km around a dataset with wells to see which areas are covered*

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
... it might be a [projection](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_projections.html) issue.

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
````

<!---MENTION ISOCHRONES AND LINK TO OPENROUTESERVICE? -->


## Centroids


This process creates a new point layer, with points representing the centroids of the geometries of the input layer. 

The centroid is a single point that shows the middle of all the parts of a feature. It can be outside the feature or on each 
part of it.

The attributes of the points in the output layer are the same as for the original features.

Centroids are especially useful when creating [graduated symbols maps](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_styling_vector_data.html#creating-a-graduated-symbols-map), as the size of the point symbols can be graded using the graduated classification method.

```{figure} /fig/en_centroids_screenshot.png
---
width: 650 px
name: en_qgis_centroids
---
The black points represent the centroids of the features from the input layer.
```


