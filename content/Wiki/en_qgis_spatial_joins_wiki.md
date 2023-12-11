# Spatial Joins

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