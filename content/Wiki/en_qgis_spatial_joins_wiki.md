# Spatial Joins


__🔙[Back to Homepage](/content/intro.md)__


## Join Attributes by location

- Adds additional attributes of the join layer to the input layer based on the __spatial relationship__.
- `Input Layer`: dataset you want to enrich
- `Join layer`: dataset with additional information/attributes
- You can specify which fields of the join layer should be added

:::{dropdown} Example: Add the time zone (join layer) to the cities (input layer)
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_spatial_join_wiki.mp4"></video>
:::

## Join Attributes by location (summary)
- Adds additional attributes of the join layer to the input layer based on the __spatial relationship__.
- `Input Layer`: dataset you want to enrich
- `Join layer`: dataset with additional information/attributes
- Additionally calculates statistical summaries for the values from matching features in the second layer
    - Options: min, max, mean, count, sum

:::{dropdown} Solution: Calculate sum of affected population and flooded area for the Area of interest
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_spatial_join.mp4"></video>
:::

## Spatial joins relationships

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