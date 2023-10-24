# Spatial Geodataprocessing
**Competences:**

## Buffer
The concept of __buffering__ in QGIS for vector data, refers to the process of creating a new polygon layer with areas that represent a __certain distance__ or __buffer around existing vector features__. This buffer zone is typically uniform and extends outward from the original features, making it useful for various spatial analyses and mapping applications. Examples for such analyses could be the creation of buffer zones to protect the environment, analyse greenbelts around residential areas or create risk areas for natural disasters. Buffer can be created around points, lines and polygons as shown in the figure below.

```{figure} /fig/en_buffer_point_line_polygon.png
---
height: 300px
name: spatial_relations
---
Different kinds of buffer zones
```
There are several variations in buffering. The __buffer distance__ or __buffer size can vary__ according to the numerical values provided. The numerical values have to be defined in map units according to the Coordinate Reference System (CRS) used with the data. 

```{Attention}
If you are trying to make a buffer on a layer with a Geographical Coordinate System, processing will warn you and suggest to reproject the layer to a __metric Coordinate System__.
```

For instance, when creating a buffer zone along a riverbank, the buffer's width may vary, contingent upon the nature of the surrounding land use. In cases of intense cultivation, the buffer distance might be more extensive compared to areas dedicated to organic farming.

## Dissolve
The dissolve tool combines features in a vector layer to make new ones. You can pick one or more attributes to group together features that share the same value for those attributes. Alternatively, you can combine all features into one. The tool will convert the shapes into multi-geometries, and if you're working with polygons, it'll remove shared boundaries between them.

If you turn on the "Keep disjoint features separate" option when running the tool, it'll make sure that features or parts that don't overlap or touch each other are saved as separate features instead of being part of one big feature. This allows you to create several vector layers.

## Clip

This tool is used to cut a vector layer with the boundaries of another polygon layer. It keeps only the parts of the features in the input layer that are inside the polygons of the overlay layer, creating a refined dataset. While the core attributes of the features remain the same, some properties like area or length may change after the clipping operation. If you've stored these properties as attributes, you might need to update them manually.

## Clip vector by extent

This operation clips any vector file to a given extent. This clip extent will be defined by a bounding box that should be used for the vector output file. It also has to be defined in the target CRS coordinates. There are different methods to define the bounding box of which the following is the most prominent:
* Calculate from a layer: this uses the extent of a layer loaded into the current project

# DROPDOWN HERE OR TABS
Other option are:
* Calculate from layout map: uses the extent of a layout map item in the active project
* Calculate from bookmark: uses the extent of a saved bookmark
* Use map canvas extent
* Draw on canvas: click and drag a rectangle delimiting the area to take into account
* Enter the coordinates as xmin, xmax, ymin, ymax

## Clip vector by mask layer

This operation uses a mask polygon layer to clip any vector layer.


## Spatial joins
Spatial joins in QGIS enhance the attributes of the input layer by adding additional information from the join layer, relying on their __spatial relationship__. This process enriches your data by incorporating relevant details from one layer into another based on their geographical associations.

```{figure} /fig/en_select_by_location.png
---
height: 500px
name: spatial_relations
---
Looking for spatial relations between layers (source: QGIS Documentation)
```
Various types of spatial relations exist between the source feature and the target feature, enabling their potential linkage. The subsequent list outlines these distinct options and provides descriptions, all oriented around the upper figure for clarity.

| spatial relation | description
|------------------|---------------------------------
| __Intersect__    | Tests whether the geometry of the two layers intersects with one another. Returns 1 (true) if the geometries spatially intersect (share any portion of space, could be overlap or touch) and 0 if they don’t. In the picture above, this will return circles 1, 2 and 3.
| __Contain__      | Returns 1 (true) if and only if no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a. In the picture, no circle is returned, but the rectangle would be if you would look for it the other way around, as it contains circle 1 completely. This is the opposite of are within.
| __Disjoint__     | Returns 1 (true) if the geometries do not share any portion of space (no overlap, not touching). Only circle 4 is returned.
| __Equal__        | Returns 1 (true) if the geometries are exactly the same. No circles will be returned.
| __Touch__        | Tests whether a geometry touches another. Returns 1 (true) if the geometries have at least one point in common, but their interiors do not intersect. Only circle 3 is returned.
| __Overlap__      |Tests whether geometries overlap. Returns 1 (true) if the geometries share space, are of the same dimension, but are not completely contained by each other. Only circle 2 is returned.
| __Are within__   | Tests whether one geometry is within another. Returns 1 (true) if geometry a is completely inside geometry b. Only circle 1 is returned.
| __Cross__        | Returns 1 (true) if the supplied geometries have some, but not all, interior points in common and the actual crossing is of a lower dimension than the highest supplied geometry. For example, a line crossing a polygon will cross as a line (true). Two lines crossing will cross as a point (true). Two polygons cross as a polygon (false). In the picture, no circles will be returned.

QGIS provides a range of tools that allow users to delve into spatial relationships and leverage them for enhancing their datasets.

::::{tab-set}

:::{tab-item} Join attributes by location
This tool takes an input vector layer and creates a new vector layer that is an extended version of the input, with additional attributes in its attribute table.

The additional attributes and their values are taken from a second vector layer. For this layer a spatial criteria is applied to select the values from it that are added to each feature from the first layer.

```{figure} /fig/en_join_attributes_by_location.png
---
height: 500px
name: join_attribute_by_location
---
Screenshot of the tool Join attributes by location
```

:::

:::{tab-item} Join attributes by location (summary)
Content 2
:::

:::{tab-item} Join attributes by nearest
Content 2
:::

::::

Further helpful information on this process can be found on the QGIS documentation under [Join attributes by location](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location#join-attributes-by-location).

For performing additional calculations in combination with a spatial join, the QGIS tool  __Join attributes by location (summary)__ is really helpful. This functionality closely resembles the previously outlined workflow; however, the algorithm extends its capabilities by calculating statistical summaries for the values from matching features in the second layer. These summaries encompass a wide range of options, including __minimum__ and __maximum values__, __mean values__, as well as __counts__, __sums__, __standard deviation__, and more.