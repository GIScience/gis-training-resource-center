# QGIS Exercise 1: Understand the user interface and get to know the layer concept
### Aim of the exercise:
To take the first steps.
Display vector data in QGIS and view the attribute data.
Reproject vector data (i.e. change the projection of the data).

### Wiki:

- [Interface](https://github.com/QGIS_Training/gis-training-resource-center/Wiki/en_qgis_interface_wiki.md)

- [Projections](https://github.com/QGIS_Training/gis-training-resource-center/Wiki/en_qgis_projections_wiki.md)

- [Layer concept and data import](https://github.com/QGIS_Training/gis-training-resource-center/Wiki/en_qgis_layer_concept_wiki.md)


### Data:

Download the data (zip-file: 83.23 KB) and save it on your PC. Create a local folder and save the above data there. (.zip folders must be unzipped beforehand.)

- Sierra Leone Border (Polygon/Lines) GeoPacked

  - Sierra Leone national boders (Polygon/lines)

  - Sierra Leone provinces (Lines)

- Sierra Leone health (Points)
- Sierra Leone airports (CSV)

### Tasks:

1. Open QGIS and familiarise yourself with the user interface. 

2. Open the above files in QGIS. Load the vector layers into your program. Load the CSV file via "Add delimited text".

![QGIS_User_Interface](/fig/en_airports_text_layer.png)
Airport Text Layer 

3. Interact with the map and explore the data sets. Use the zoom tool and move the map. Notice the status bar at the bottom of the screen and how it changes.

4. Familiarise yourself with the layer window (Layer List). Alternately show and hide different layers and move the layers in the hierarchy. Rename the data layer in a meaningful way. Note that the latter has no effect on the data sources (file names, storage location).

5. View the attribute data of the layers. For this purpose look at the attribute table.

6. Changes the projection in the map view to WGS 84 / Pseudo-Mercator- EPSG:3857. Note that this does not change the projection (the coordinates) of the files, but only affects the projection of the map view.  Check this in the properties of the point layer. Which projection is indicated there? Hint: You can use the searchbar on the top.

7. Now save the health layer in the projection WGS 84 / Pseudo-Mercator- EPSG:3857. This changes the projection of the file. Check this in the properties of the newly created layer.

8. Save your project.

9. Optional: You can add the OpenStreetMap base map via the browser windos => XYZ Tiles. Note that online base maps can lead to problems with the projection of the different layers. Make sure to remove the base map bevor saving the project.

### Result: 

>This (or similar) is what it looks like in the end:

:::{dropdown} Airport Text Layer

![QGIS_User_Interface](/fig/en_eExercise_1_result.png)
Airport Text Layer 
:::


