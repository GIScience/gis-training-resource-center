# Basic Geodata processing Exercise 1 

### Aim of the exercise
The objective of this exercise is to get a feeling for Geodata and start working with it. Understand the attribute table, sort it, select manually and export the selection.

### Links to Wiki articles
will be done when Wiki is finished

### Data
Download all datasets [here](linktobeadded.zip) and save the folder on your computer and unzip the file. The zip folder includes:
- `nigeria_populated_places.shp` (Points) Shapefile
- `nigeria_boundaries.geojson` GeoJSON

### Tasks

1. Load both files into your QGIS.

2. Optional: You can add the OpenStreetMap base map via the browser window --> XYZ Tiles. 

3. Familiarise yourself with the data by opening the attribute table.

4. In the `nigeria_populated_places.shp`, select manually **Zuyel** and zoom onto the selected point. 

```{Hint}
The place starts with a *Z* so it might be easiest to sort the column `name` descending.
```

5. Export **Zuyel** as its own Shapefile. Check the projection and choose an appropriate crs. Name it `zuyel.shp`.

:::{dropdown} How do I know which crs to choose?
You can find all projections and their CRS code at this [website](http://epsg.io) and search for the country. 
:::

```{Note}
Since we don't want to calculate anything, f. e. area, WGS84 (EPSG:4326) would be fine to use.
```

6. Repeat the steps for the layer `nigeria_boundaries.geojson` and only export the district in which **Zuyel** is in. Name it accordingly.

:::{dropdown} How do I know in which district Zuyel is in?
You can check by using the `identify features` option.
![Check district by clicking](fig/modul2_ex_nigeria_district.png)
Afterwards you can again select manually by sorting the attribute table.
:::

7. Open the attribute table and check that you only have one feature each.

8. Save your project.

### Result

```{figure} /fig/en_result_geodata_processing_exercise.png
---
width: 80%
name: en_result_geodata_processing_exercise
---
This is how your output could look like in the end
```