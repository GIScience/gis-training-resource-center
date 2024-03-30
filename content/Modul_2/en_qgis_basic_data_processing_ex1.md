# Basic Geodata Processing Exercise 1 

### Aim of the exercise
The objective of this exercise is to get a feeling for geodata and start working 
with it. Understand the attribute table, sort it, select manually and export the 
selection.

### Links to Wiki articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Attribute Table in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.md)
* [Projections](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html)
<!-- FIXME: add link -->

### Data
Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise_1_Basic_Geodata_Processing/Modul2_Basic_Geodata_Processing_exercise.zip), save the folder on your computer and unzip the file. The zip folder includes:

- `nigeria_populated_places.shp` (Points) Shapefile
- `nigeria_boundaries.geojson` GeoJSON

The shapefile for populated places contains data on human settlements in Nigeria, including cities, villages and others. The GeoJSON file for the boundaries of Nigeria contains information on the administrative boundaries at levels 2 and 4 with level 2 representing the whole country and level 4 being the states.

<!-- CLARIFY: does it matter where to download? What do these datasets 
	represent? -->

### Tasks

1. Load both files into QGIS.

2. Add the OpenStreetMap basemap via the browser panel --> 
   XYZ Tiles. 

3. To familiarise yourself with the data, open the attribute table. Determine the location of the data and the type of information it contains. Understand the different columns and the data they contain in your attribute table and try to get an overview of which columns will be relevant and important for your analysis.
<!-- CLARIFY: What sorts of things should people familiarise themselves with? -->

4. In the `nigeria_populated_places` layer, open the attribute table, select 
   the feature for **Zuyel**, and zoom to the selected point. 

```{Hint}
The place starts with a *Z* so it might help to sort the `name` column in
descending order.
```

5. Export **Zuyel** as its own GeoPackage. Check the projection and choose an 
   appropriate CRS. Name it `zuyel.gpkg`.
  <!-- CHECK: We have previously recommended people use GPKG. Should we use that here? -->

```{Note}
As no calculations are involved, e.g. area, WGS84 (EPSG:4326) is a good choice.
```

:::{dropdown} How do I know which CRS to choose?
[EPSG.io](http://epsg.io) has a database that you can search to find the appropriate CRS 
to use for a country. More information on [Projections](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html) can be found in the Wiki or in the corresponding section in [Modul 2 on Projections](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept.html#projections).
:::
<!-- CLARIFY: is it important to choose an appropriate CRS or should people use 
	the default? Part of this section can be removed. --> 

6. Repeat the steps for the layer `nigeria_boundaries.geojson` and only export 
the district in which **Zuyel** is located. Name it accordingly. To find the district use the ![](/fig/qgis_identify_features.png) `Identify Features` tool and then manually select the correct district in the attribute table.
<!-- FIXME: Exercises should be used to test what has been shown in a section, 
	rather than introduce new functionality -->

7. Remove all the initial layers and then open the attribute table for each of your new layers and check that each layer 
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