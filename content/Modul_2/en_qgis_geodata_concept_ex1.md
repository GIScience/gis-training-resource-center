# Geodata Concept Exercise 1

### Aim of the exercise
The objective of this exercise is to make your first steps in QGIS. Understand the user interface and get to know the layer concept. 

* Display vector data in QGIS and view the attributes of the data
* Reproject the vector data (change the projection of the data)

### Links to Wiki articles
will be done when Wiki is finished
<!-- FIXME: to be updated -->

### Data
Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise2_Geodata_Concept/Modul_2_Exercise2_Geodata_Concept.zip) and save the folder on your computer and unzip the file. The zip folder includes:
<!-- CLARIFY: does it matter where they are downloaded? -->
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra Leone national boders (Lines)
    - Sierra Leone provinces (Lines)
- `sierra_leone_health_HOT.shp` (Points) Shapefile
- `sl-airports.csv` (CSV) -modified <!-- CLARIFY: what does "modified" refer to? -->
<!-- CLARIFY: What data is being loaded here? Give a quick explanation for each 
    file -->

### Tasks
1. Open QGIS and familiarise yourself with the user interface.
<!-- FIXME: this is a poorly defined task step -->

2. Open the files you have downloaded in QGIS. Load the vector layers into the 
   program. To load the CSV file, select `Add delimited text`.
<!-- FIXME: We haven't shown people how to open files yet -->

```{figure} /fig/en_delimited_text_screenshot.PNG
---
width: 80%
name: delimited_text
---
Screenshot of Data Source Manager - Delimited Text to load a CSV file
```

3. Interact with the map and explore the datasets. Use the zoom tool and move 
   the map. Take note of the status bar at the bottom of the screen and observe 
   how it changes.

   <!-- CLARIFY: What changes should people expect to see? -->

4. Familiarise yourself with the layer window (layer list). Show and hide 
   different layers and move layers around in the hierarchy. Give the data layer 
   a meaningful name. 

```{Note}
Renaming the layer does not affect the data source, such as file names or 
storage location.
```

5. Check out the attribute data of the layers by examining the attribute table.

6. Change the projection in the map view to `WGS 84 / Pseudo-Mercator EPSG:3857`. 

```{Note}
This does not change the projection (coordinates) of the files, only the 
projection of the map view. Verify this by looking at the properties of the point 
layer. What projection is shown there?
```

```{Hint}
You can use the search bar on the top left.
```
<!-- CLARIFY: use it for what? -->

7. Now save the health layer in the projection `WGS 84 / Pseudo-Mercator EPSG:3857`. 
   This changes the projection of the file. Verify this by looking at the 
   properties of the newly created layer.

8. Save your project.

9. Optional: You can add the OpenStreetMap base map via the browser window, 
   under `XYZ Tiles`. 

```{Note}
Online basemaps can cause display issues when combined with layers in different 
projections. It is important to remove the base map before saving the project.
```
<!-- CLARIFY: What issues? Is there another workaround? -->

```{figure} /fig/en_result_geodata_concept_exercise.png
---
width: 80%
name: en_result_geodata_concept_exercise
---
This is how your output could look like in the end
```