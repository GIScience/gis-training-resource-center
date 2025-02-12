# 5.1. Spatial data processing

## Introduction

Spatial processing uses spatial information to extract new meaning from GIS data. It does so by using the __spatial relationship__ of different layers or features. Spatial relationships describe how things are located in relation to one another. In humanitarian work, this helps answer critical questions like “Which communities are near a water source?” or “Which areas are isolated from health services?”. Or, we might want to identify the best locations for distributing aid, assess flood risk areas, or plan evacuation routes.

We have already encountered spatial relationships in module 3 in the subchapter on __[geometrical operators](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_data_queries.html#geometric-operators)__— also called geometrical predicates in QGIS. 
The table below describes spatial relationships and gives examples when these spatial relationships are relevant in humanitarian aid. 

## Spatial Relationships

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
width: 750 px
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
__non-spatial joins__ and __spatial joins__. 

- Non-spatial joins rely on specific attribute values, which are used as ID-fields, to combine two layers. These are covered in the chapter "[Non-spatial processing tools](/content/Module_5/en_qgis_non_spatial_tools.md)" in this module. 
- Sometimes we want to combine information from different layers that don't share a common value. In these cases, we can use spatial joins, which let us join data based on location rules. 
- Spatial joins in QGIS enhance the attributes of the input layer by adding additional information from the join layer, relying on their __spatial relationship__. This process enriches your data by incorporating relevant details from one layer into another based on their geographical associations. 
- In QGIS, a spatial join creates a new layer by comparing the features of one layer to another, depending on 
their spatial relationship. 
- The restulting joined layer __receives attributes__ from both layers based on the chosen parameters.

For example:

- Any point __within__ a polygon should inherit attributes of the polygon.

::::{card}
__Humanitarian Example:__
^^^
*A flood depth model is available, and the goal is to determine which buildings are flooded under this scenario. This can be achieved by performing a spatial join to add the flood depth to the polygon layer containing the houses.*
<!--
*We have a flood depth model and we want to find out which buildings are flooded under this scenario. We can find this out by performing a spatial join to add the flood depth to the polygon layer with the houses.*
-->
*The resulting map could look something like this:* 

```{figure} /fig/en_flood_damage_assessement_libya.png
---
name: flood damage assessement
width: 450 px
---
A building footprint layer combined with a flood extent layer. By joining them, we can assess which houses are at risk to be damaged by flooding (Source: IFRC).
```


::::

## Geometrical operators

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

### Exercise: Performing a spatial join


```{admonition} Now it's your turn!
:class: tip

Practical exercise is crucial to understand how GIS, and QGIS, works. You can follow along by downloading the necessary data.

```

In the example above ({numref}`spatial_join_example_healthsites`), we have a dataset containing the healthsites by healthsite.io
and a dataset with the administrative boundaries (adm2) of Nigeria. We want to know in which state each healthsite is located. 
To do this, we need to use the tool "Join Attributes by Location".

```{figure} /fig/en_spatial_join_example.png
---
name: spatial_join_example_healthsites
width: 400 px
---
An example of a situation where you will use a spatial join (Source: BRC)
```

::::{margin}

```{tip}
You can find and activate the processing toolbox panel by navigating to `View` > `Panels` > `Processing Toolbox`. It should appear on 
the right side of your screen.
```

::::

:::{dropdown} __Tool:__ Join attributes by location

This tool takes two input layers and creates a new vector layer which has the attributes of both layers in its attribute table.
- The first input layer (see "Join to features in" in {numref}`join_attributes_by_location`) dictates which geometric features will be copied to the new layer.
- The second input layer (see "By comparing to" in {numref}`join_attributes_by_location`) dictates the attributes that will be added to the new layer on top of the attributes of the first input layer. You can select which of these attributes should be transferred to the new layer. 


```{figure} /fig/en_spatial_join_1.PNG
---
width: 450 px
name: join_attributes_by_location
---
The "Join Attributes by Location"-tool in QGIS 3.36.
```

:::

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

``````{list-table}
:header-rows: 1
:widths: 20 25

* - Instruction
  - Join Attributes by Location
* - 1.  Download the necessary datasets [here]()
    2. Unzip the files, create a new QGIS-project, and load the files into the QGIS-project. 
    3. Search for the tool __"Join Attributes by Location"__ in the processing toolbox and <kbd>Double-Click</kbd> on it. A new window will open (see {numref}`join_by_location_ex1`).
    4. Use the health facilities layer as the target ("Join to feature in") and the adm2 layer as the comparison layer ("By comparing to"). 
    5. Use the `are within` geometrical predicate. 
    6. Select the fields to add: `ADM2_EN`, `ADM2_PCODE`
    7. Select `Discard records that could not be joined`
    8. Click `Run` to proceed; the log should confirm success.
    9. A new (temporary) layer called "Joined features" will appear in your layers-panel
    10. <kbd>Right-click</kbd> on the layer and select "Export" or "Make Permanent" to save the new layer.
  -
    ```{figure} /fig/en_3.36_join_by_location_ex1.png
    ---
    name: join_by_location_ex1
    width: 500 px
    ---
    Setting the parameters to perform the spatial join in QGIS 3.36
    ```
``````


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

By default, QGIS provides three different tools to perform spatial joins. 

- The first, and the most common one, is the tool __"Join attributes by location"__ which we used in the previous exercise. 
- There are also the tools __"Join attributes by location (summary)"__ and __"Join attributes by nearest"__.

:::::{tab-set}

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
width: 450 px
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





