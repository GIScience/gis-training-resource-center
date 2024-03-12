# Basic Geodata processing Exercise 1 

### Aim of the exercise
The objective of this exercise is to get a feeling for geodata and start working 
with it. Understand the attribute table, sort it, select manually and export the 
selection.

### Links to Wiki articles
will be done when Wiki is finished
<!-- FIXME: add link -->

### Data
Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise_1_Basic_Geodata_Processing/Modul2_Basic_Geodata_Processing_exercise.zip) 
and save the folder on your computer and unzip the file. The zip folder includes:

- `nigeria_populated_places.shp` (Points) Shapefile
- `nigeria_boundaries.geojson` GeoJSON

<!-- CLARIFY: does it matter where to download? What do these datasets 
	represent? -->

### Tasks

1. Load both files into QGIS.

2. Add the OpenStreetMap basemap via the browser window --> 
   XYZ Tiles. 

3. Familiarise yourself with the data by opening the attribute table.
<!-- CLARIFY: What sorts of things should people familiarise themselves with? -->

4. In the `nigeria_populated_places` layer, open the attribute table, select 
   the feature for **Zuyel**, and zoom to the selected point. 

```{Hint}
The place starts with a *Z* so it might help to sort the `name` column in
descending order.
```

5. Export **Zuyel** as its own Shapefile. Check the projection and choose an 
   appropriate CRS. Name it `zuyel.shp`.
  <!-- CHECK: We have previously recommended people use GPKG. Should we use that here? -->

:::{dropdown} How do I know which CRS to choose?
[EPSG.io](http://epsg.io) has a database you can search to find appropriate CRS 
to use for a country. 
:::

```{Note}
Since we don't want to calculate anything, f. e. area, WGS84 (EPSG:4326) would 
be fine to use.
```
<!-- CLARIFY: is it important to choose an appropriate CRS or should people use 
	the default? Part of this section can be removed. --> 

6. Repeat the steps for the layer `nigeria_boundaries.geojson` and only export 
the district in which **Zuyel** is in. Name it accordingly.

:::{dropdown} How do I know in which district Zuyel is in?
You can check by using the `identify features` option.
![Check district by clicking](fig/modul2_ex_nigeria_district.png)
Afterwards you can again select manually by sorting the attribute table.
:::
<!-- FIXME: Exercises should be used to test what has been shown in a section, 
	rather than introduce new functionality -->

7. Open the attribute table for each of your new layers and check that each layer 
   only contains one feature.

8. Save your project.

### Result

```{figure} /fig/en_result_geodata_processing_exercise.png
---
width: 80%
name: en_result_geodata_processing_exercise
---
This is how your output could look like in the end
```
<!-- FIXME: We have not asked people to remove the initial layers so they would 
	also show in the layers list --> 