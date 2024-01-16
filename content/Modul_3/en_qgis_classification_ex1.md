# Geodata Classification Exercise 1: Overview map of the prevalence of stunting in Sierra Leone

### Aim of the exercise
This exercise aims to create an overview map of the prevalence of stunting in Sierra Leone at district level. To do this, we will visualise both the prevalence of stunting and key infrastructure such as hospitals, airports and roads. The decision on which data to visualise and how to present it is up to you, the cartographer.

### Links to Wiki articles
will be done when Wiki is finished

### Data
Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `Sierra_leone_prevalence_of_stunting_2014.shp` (data is modified) (Polygon)
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra Leone national boders (Lines)
    - Sierra Leone provinces (Lines)
- `Sierra_leone_infrastructure.gpkg` (MultiLineString/Points) GeoPackage
    - Sierra Leone health (Points)
    - Sierra Leone airports (Points)
    - Optional: Sierra Leone roads (Lines)

### Tasks
1. Open from the geopackages the layers national borders and provinces (`Sierra_leone_borders.gpkg`) and the airports (`Sierra_leone_infrastructure.gpkg`) in QGIS.

2. Have a look at the airport layer. Open the attribute table and sort the data. Delete empty columns. See the Wiki entry on the __Attribute table__ for further information.

3. Add a base map to your map view using the Plugin `QuickMapServices`. Adjust the opacity of your layers to optimise the use of the base map. [Tutorial video on how to do that](https://www.youtube.com/watch?v=WguUkN1YRzY&ab_channel=GISBigfootAnswers)

4. Zoom to Tongo Airport by right-clicking on the row in the attribute table and selecting `Zoom to Feature`. Then, check the Bing satellite imagery using the QuickMapServices tool. Do you think the airstrip is still operational? The answer is no according to wikipedia. Delete Tongo Airport in the attribute table. Also, delete Kabal airport since it is also not operational.

5. Now check out the cities of Bo and Kenema. Are these airstrips in better shape? If yes, add them to the airport layer. See the Wiki entry on __Digitalisation__ for further information.

6. Create a new column `Runway_length` and at the length of the runways of Bo and Kenema.

7. Load the vector layer `Sierra_leone_prevalence_of_stunting_2014.shp` into QGIS.

8. Classify the stunting data and adjust the colouring. See the Wiki entry on __Classification__ for further information.

9. (Optional) Also load the health layer from the `Sierra_leone_infrastructure.gpkg` into QGIS. Classify the health layer to only show hospitals. 

```{figure} /fig/en_Symbols_health_exercise_classification.png
---
width: 30%
name: en_Symbols_health_exercise_classification
---
How to classify the health layer to just display the hospitals
```

10. Choose the symbology and colours for borders, roads, hospitals and airports that you think are suitable. See the Wiki entry on __Styling__ for further information.

11. (Optional) Now add the roads layer from the `Sierra_leone_infrastructure.gpkg` to QGIS. Classify the roads with the column `highway`. Choose which roads and paths you want to visualise and create a suitable symbology.

12. Create a print layout and add important map features like title, sources, scales, legend and North arrow. See the Wiki entry on __Map design__ for further information.

13. Export your map as a PDF file.

```{figure} /fig/en_result_classification_exercise.png
---
width: 100%
name: en_result_classification_exercise
---
This is how your output could look like in the end
```