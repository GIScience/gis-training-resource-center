# Exercise 1: Geodata Concept

### Aim of the exercise
The objective of this exercise is to make your first steps in QGIS. Understand the user interface and get to know the layer concept. 

* Display vector data in QGIS and view the attributes of the data
* Reproject/Change the projection of the vector data

### Links to Wiki articles
* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Attribute Table in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.md)
* [Projections](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html)
<!-- FIXME: to be updated -->

### Data
Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_1/Module_2_Exercise_1_Geodata_concept.zip) and save the folder on your computer and unzip the file. The zip folder includes:
<!-- CLARIFY: does it matter where they are downloaded? -->
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra Leone national borders (Lines)
    - Sierra Leone provinces (Lines)
- `sierra_leone_health_HOT.shp` (Points) Shapefile
- `sl-airports.csv` (CSV)

```{hint} Folder structure
Keep your data management clean by creating a folder structure on your computer for your QGIS-projects and geodata. 
The exercise data should be saved in a location where you can easily find them and the corresponding QGIS-project
```

The borders GeoPackage contains administrative information for Sierra Leone at both national and provincial level. Additionally, the shapefile `sierra_leone_health_HOT.shp` provides information on various health facilities within the country, while the `sl-airports.csv` CSV-file offers information on airports.


### Tasks
1. Open the files you have downloaded in QGIS. 
   - The geopackage (.gpkg) and shapefile (.shp) can be dragged and dropped onto the map canvas in QGIS. 
   - The .csv file needs to be imported via the layer menu.
      - Navigate to `Layer`> `Add Layer` > `Add delimited text layer`. A new window will open. Here you can select the file you want to import by clicking on `...` to the right of the __File name__  field at the top.
      - Navigate to the folder with the exercise files and select `sl-airports.csv`. 
      - Click open. The CSV-import window will update and show you a preview of the CSV-table. 
      - The table contains geographic information. We will need to specify this under __"Geometry Definition"__. 
         - Click on `Point Coordinates` and select `longitude_deg` as your __"X field"__ and `latitude_deg` as your __"Y field"__.
      - Click add. a new point layer with the airports should appear on your map canvas.

:::{figure} /fig/en_3.36_add_csv.png
---
width: 500 px
name: navigation to add csv layer
---
Opening the CSV-import window
:::

<!-- FIXME: We haven't shown people how to open files yet. EDIT: Move this Exercise after geodata management -->

```{figure} /fig/en_delimited_text_screenshot.PNG
---
width: 80%
name: delimited_text
---
Screenshot of the Data Source Manager - Delimited Text to load a CSV file
```

2. Interact with the map and explore the datasets. Use the zoom tool and move 
   the map. Focus on the scale window and observe how it varies as you zoom in and out. 

3. Familiarise yourself with the layer window (layer list). Show and hide 
   different layers and move layers around in the hierarchy. Give the data layer 
   a meaningful name. 

```{Note}
Renaming the layer does not affect the data source, such as file names or 
storage location.
```

4. Check out the attribute data of the layers by examining the attribute table.

5. Change the projection in the map view to `WGS 84 / Pseudo-Mercator EPSG:3857`. 

```{Note}
This does not change the projection (coordinates) of the files, only the 
projection of the map view. Verify this by looking at the properties of the point 
layer. What projection is shown there?
```

```{Hint}
To obtain information about a layer and its projections, double-click on the layer and look for the `Information` section. This section contains general details such as the file name and file path, as well as information about the Coordinate Reference System (CRS) in the respective section.
```
<!-- CLARIFY: use it for what? EDIT: No longer valid comment?-->

6. Save the health facility layer in the `WGS 84 / Pseudo-Mercator EPSG:3857` projection. This will change the projection of the file. This can be done by right-clicking on the layer --> `Export` --> `Save Features As..`. In the pop-up window, select **GeoPackage as the output file format** and **specify the file location and name** by clicking on the three small points. The file can also be given a layer name, which will be displayed when it is loaded into QGIS. Before running this process, the **projection can be changed** by selecting the desired CRS in the designated section. Verify the changed projection by looking at the properties of the newly created layer.

```{figure} /fig/en_ex1_export_layer.PNG
---
width: 40%
name: export_layer
---
Screenshot of the Export window
```

7. Save your project.

8. Optional: You can add the OpenStreetMap base map via the browser window, 
   under `XYZ Tiles`. 

```{Note}
Combining layers in different projections with online basemaps (typically have their own projections) can lead to display issues due to CRS conflicts. When layers have a distinct CRS, they may not align correctly or appear distorted when overlaid with an online basemap. To mitigate these problems, it's advisable to either reproject the layers to match the CRS of the basemap (which is often not applicable) or temporarily remove the basemap before saving the project. This ensures that the map is displayed accurately and avoids potential visual discrepancies caused by CRS inconsistencies.
```
<!-- CLARIFY: What issues? Is there another workaround? EDIT: -->

```{figure} /fig/en_result_geodata_concept_exercise.png
---
width: 80%
name: en_result_geodata_concept_exercise
---
This is how your output could look like in the end
```