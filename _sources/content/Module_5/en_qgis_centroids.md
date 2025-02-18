::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# 5.3. Centroids

This process creates a new point layer, with points representing the centroids of the geometries of the input layer. 

The centroid is a single point that shows the middle of all the parts of a feature. It can be outside the feature or on each 
part of it.

The attributes of the points in the output layer are the same as for the original features.

Centroids are especially useful when creating [graduated symbols maps](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#creating-a-graduated-symbols-map), as the size of the point symbols can be graded using the graduated classification method.

```{figure} /fig/en_centroids_screenshot.png
---
width: 650 px
name: en_qgis_centroids
---
The black points represent the centroids of the features from the input layer.
```


