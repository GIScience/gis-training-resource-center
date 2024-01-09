# Exercise 2: Part 1: Calculate vulnerability index

### Aim of the exercise
We want to create an overview of different vulnerability indicators. From the Covid-19 risk indicators dataset we take `% permanent wall type`, `% permanent roof type` and `poverty incidence`. From the Uganda population statistics we calculate the `% of under fives` and `% of elderly`. We combine the data and we are now able to visualize the areas in Uganda that are most vulnerable.

### Links to Wiki articles
will be done when Wiki is finished

### Data
Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `uga_admbnda_adm2_ubos_20200824.shp`: [Uganda district boundaries (Admin level 2)](https://data.humdata.org/dataset/cod-ab-uga)
- `COVID19_RISK_INDEX.shp`: [Covid-19 risk indicators](https://data.humdata.org/dataset/covid19_risk_index)
- `uga_admpop_adm2_2020proj_1y.csv`: [Uganda population statistics](https://data.humdata.org/dataset/cod-ps-uga)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

### Task
This first part of the exercise will prepare the data for subsequent non-spatial geodataprocessing, such as working with the attribute table. To calculate the vulnerability index, we will join all the relevant data using spatial geodataprocessing into a single vector layer.

1. Load the Uganda district boundaries (admin level 2) (`uga_admbnda_adm2_ubos_20200824.shp`), as well as population statistics (`uga_admpop_adm2_2020proj_1y.csv`) and the Covid-19 risk indicators (`COVID19_RISK_INDEX.shp`) into QGIS.

2. Make sure to reproject the dataset with the __district boundaries__ and the dataset with the __Covid-19 risk indicators__ into UTM zone 36N. Use the tool `Reproject layer` for this process. See the Wiki entry on __Projections__ for further information.

```{Attention}
Before you start doing any GIS operations, __always explore the data__. Always check if the projections of the different layers are the same.
```

```{Hint}
The projected coordinate system for Uganda is `EPSG:32636 WGS 84 / UTM zone 36N`
```

3. We see that the polygons are different in shape and amount! It is likely that the risk data is using an older version of the admin boundaries. This is an issue we need to resolve in order to work properly with the data.

```{figure} /fig/en_ex3_1_attribute_table_size.png
---
width: 100%
name: attribute_table_size
---
Screenshot of different sizes of the attribute tables
```

4. We will use the following solution for this problem:
    - We can take the closest district centroid (from the dataset with the most to the dataset with the fewest records). This is the solution we will use for this exercise as the difference between the two datasets is not drastically.

5. Calculate the ![](/fig/mAlgorithmCentroids.png) `Centroids` for the dataset containing the most elements, which are the district boundaries. You can find the tool under `Vector` --> `Geometry Tools` --> `Centroids`. See the Wiki entry on __Geoprocessing__ for further information.

6. Edit the points so they are inside the correct polygons. This is necessary because the __centroid of a polygon may fall outside of it__ when it has an __unusual shape__. To move a centroid that is outside its boundaries into the district boundaries, first activate the `Toggle editing mode` button, which can be found by clicking on ![](/fig/mActionToggleEditing.png) while activating the centroid layer. Then, select the ![](/fig/mActionMoveFeaturePoint.png) `Move Feature` tool. Search for the centroid that is outside its boundaries and move it to the appropriate district boundary. Save the changes and end the editing mode.

```{figure} /fig/en_centroids_screenshot_red.png
---
width: 80%
name: en_qgis_centroids
---
The black points represent the centroids of the features of the input layer. The red circle indicates the centroid that requires editing.
```

7. There is an issue that can be found when joining the datasets, but it can be solved by using the `Fix geometries` tool on the Covid-19 risk dataset.

```{figure} /fig/en_ex3_1_fix_geometries.PNG
---
width: 60%
name: fix_geometries
---
Screenshot on how to fix the geometries.
```

8. Use the tool `Join attributes by location` to join the Covid-19 risk polygons onto the centroids. As a spatial relationship select `within` and select the columns `%permrooft`, `%permwallt` and `Povertyinc` as the fields that should be added. See the Wiki entry on __Spatial Joins__ for further information.

```{figure} /fig/en_ex3_1_join_attribute_location_1.PNG
---
width: 60%
name: join_attribute_by_location
---
Screenshot of Join attribute by location operation.
```

9. Again use the tool `Join attributes by location` to join the previously enriched points onto the Uganda district boundaries. Now select as a spatial relationship contain and again select the same three columns for joining.

```{figure} /fig/en_ex3_1_join_attribute_location_2.PNG
---
width: 60%
name: join_attribute_by_location_2
---
Screenshot of the second Join attribute by location operation.
```

The next steps of the vulnerability index calculation will be completed in the second part of this exercise, in the Non-spatial Geodataprocessing section. Please refer to the [provided link](/content/Modul_5/en_qgis_non_spatial_tools_ex2.md) for this exercise.