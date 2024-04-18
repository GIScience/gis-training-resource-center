# Geodata Concept Exercise 1

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
Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise2_Geodata_Concept/Modul_2_Exercise2_Geodata_Concept.zip) and save the folder on your computer and unzip the file. The zip folder includes:
<!-- CLARIFY: does it matter where they are downloaded? -->
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra Leone national borders (Lines)
    - Sierra Leone provinces (Lines)
- `sierra_leone_health_HOT.shp` (Points) Shapefile
- `sl-airports.csv` (CSV)

The borders GeoPackage contains administrative information for Sierra Leone at both national and provincial level. Additionally, the shapefile `sierra_leone_health_HOT.shp` provides information on various health facilities within the country, while the `sl-airports.csv` CSV-file offers information on airports.
<!-- CLARIFY: what does "modified" refer to? -->
<!-- CLARIFY: What data is being loaded here? Give a quick explanation for each 
    file -->

### Tasks
1. Open the files you have downloaded in QGIS. To load the vector layers into QGIS, simply drag and drop the downloaded files onto the map canvas. When loading the health facilities, ensure that you select the .shp file. For the CSV file, select `Delimited Text`.
<!-- FIXME: We haven't shown people how to open files yet -->

```{figure} /fig/en_delimited_text_screenshot.PNG
---
width: 80%
name: delimited_text
---
Screenshot of the Data Source Manager - Delimited Text to load a CSV file
```

2. Interact with the map and explore the datasets. Use the zoom tool and move 
   the map. Take note of the status bar at the bottom of the screen and observe 
   how it changes. Focus on the scale window and observe how it varies as you zoom in and out.

   <!-- CLARIFY: What changes should people expect to see? -->

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
<!-- CLARIFY: use it for what? -->

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
<!-- CLARIFY: What issues? Is there another workaround? -->

```{figure} /fig/en_result_geodata_concept_exercise.png
---
width: 80%
name: en_result_geodata_concept_exercise
---
This is how your output could look like in the end
```