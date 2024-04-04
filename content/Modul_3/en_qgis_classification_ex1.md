# Geodata Classification Exercise 2: Overview map of the prevalence of food insecurity in Sierra Leone

### Aim of the exercise
This exercise aims to create an overview map of the distribition of food insecurity in Sierra Leone at district level. To do this, we will visualize both the distribution of food insecurity and key infrastructure elements such as hospitals, airports and roads. 

### Relevant Wiki Articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Attribute table](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Geodata Classification- Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)
* [Digitization- Point data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer)



### Data
Download all datasets __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_3/Modul_3_Ex_1_Sierra_Leone/Modul_3_Ex_1_Sierra_Leone.zip)__ and save the folder on your computer. Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. Under "data > input" you find the following files:
- `Sierra_leone_foodinsecurity_2015.shp` (Polygon)
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra_Leone_national_borders (Lines)
    - Sierra_Leone_provinces (Lines)
- `Sierra_leone_infrastructure.gpkg` (MultiLineString/Points) GeoPackage
    - Sierra_Leone_health (Points)
    - Sierra_Leone_airports (Points)
    - Sierra_Leone_roads (Lines)

### Tasks
Our goal is to produce an overview of the 2015 food insecurity situation in Sierra Leone together with the display of main infrastructure elements. To achieve this, we will visualize the classification of total food insecurity together with airports, hospitals and primary roads in a map.

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. Once the project is created save the project in the “project” folder of the “Ex_Sierra_Leone_foodinsecurity”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Sierra_Leone_foodinsecurity”.

3. Import the GeoPackages `Sierra_leone_borders.gpkg` and `Sierra_leone_infrastructure.gpkg` aswell as the shapefile `Sierra_leone_foodinsecurity_2015.shp` into your project via drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). 
Or by clicking `Layer`-> `Add Layer`-> `Add Vector Layer`: Click on the three dots ![](/fig/Three_points.png) and navigate to "Sierra_leone_borders.gpkg" in your file Browser. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).

```{Attention}
GeoPackages can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```

4. First have a look at the airport layer(`Sierra_Leone_airports`). Open the attribute table and sort the data. Delete empty columns. See the Wiki entry on the [Attribute table](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html) for further information.

5. Add a base map to your map view using the Plugin `QuickMapServices` by clicking on the ![](/fig/QMS_search_icon.png) symbol in you projct toolbar. Search for "Bing Maps Satellite Imagery" in the QMS panel and add the base map layer via double click.  For an optimized view [adjust the opacity](https://www.youtube.com/watch?v=WguUkN1YRzY&ab_channel=GISBigfootAnswers) of your layers to optimize the use of the base map. 

6. Using  the attribute table of the airports layer zoom to Tongo Airport by right-clicking on the row in the attribute table and selecting `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)). Check the Basemap. Do you think the airstrip is still operational? The answer is no, according to Wikipedia. Delete Tongo Airport in the [Attribute table](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html). Delete Kabala airport too, since it is also not operational anymore.

7. Now we want to check out the airports of the cities of Bo and Kenema. Are these airstrips in better shape? If yes, add them to the airport layer. To find these cities on your map interface use the QGIS Plugin `OSM Place Search`. 
To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for "OSM Place Search". Once you have found it click on it and select `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html#installation-of-plugins)).
    * In the panel, you can search for places on the OpenStreetMap by typing the name in the search bar. Often it makes sense to add additional information like the name of the country. Try for example “Bo, Sierra Leone”.

```{figure} /fig/mod3_classification_ex_OSMsearch.png
---
width: 400px
name: 
align: center
---
OSM place search.
```

Add the airports of Bo and Kenema as points to the layer `Sierra_Leone_airports`. Find help on the addition of features to a point layer [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.md). 
 

8. *Optional:* In the attribute table, create a new column `Runway_length` and add the length of the runways of Bo and Kenema by measuring them approximately with the measuring tool ![](/fig/measuring_tool_icon.png).

9. Now we want to create a intutive visualization of the differences in food insecurity. To achieve this we use the "[Graduated Classification](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)" visualization option for the layer `Sierra_leone_foodinsecurity_2015` by displaying the polygons according to classes created based on the "Total_FI" column in the attribute table.
    * Right-click on the layer `Sierra_leone_foodinsecurity_2015.shp` in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * In the topmost drobdown menu choose `Graduated`. Under `Value` select “Total_FI”.
    * Further down the window click on `Classify`. You now should see multiple classes based on the value range of the "TotalFI" column represented with different colours.  You can adjust the colours by picking different colour palettes in the drop down menu `Color ramp`. Also, you can modify the value distribution of the classes by selecting different classification modes ([Wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)) in the `Mode` dropdown menu. 
    * Play around with these options to achieve a visualisation that suits the display of the values. Once you are done, click `Apply` and `OK` to close the symbology window.

```{figure} /fig/mod3_classification_ex_Graduatedclassification.png
---
width: 900px
name: basic classification
align: center
---
Sierra Leone food insecurity classification.
```

1.  To give the hospitals and airports a more distinctive visualization, open the `Symbology` tab again for the respective layers and choose "Topology" in the dropdown menu above the bottom panel top panel. Search for the airport/hospital symbol and select it by clicking on it. Again, apply your changes by clicking `Apply` and `OK`.

```{figure} /fig/mod3_classification_ex_Topology.png
---
width: 900px
name: basic classification
align: center
---
Symbol for hospital.
```

11. As a last visualisation step open the `Symbology` tab `Sierra_Leone_roads (Lines)` and like in step 9 open the top dropdown menu. Now instead of `Graduated` choose [Categorized Classification](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html) and select "highway" in the `Value` menu. Click `Classify` to get a classification with individual colours for all unique values of the "highway" column. In the squares next to the classes, deselect all classes except for "primary". You can change the colour of the classes by selecting them via click and adjusting the colour in the drop "Symbol" dropdown menu near the top of the window.

```{figure} /fig/mod3_classification_ex_Categorizedclassification.png
---
width: 900px
name: basic classification
align: center
---
Categorized highways Sierra Leone.
```

12. Turn all the layers you loaded into your project to visible and arrange them in an order that is suitable for a good visualization of the food insecurity as well as the infrastructure elements. Choose a basemap that you think is suitable. Your final result could look like this:

```{figure} /fig/mod3_classification_ex_Result.png
---
width: 900px
name: basic classification
align: center
---
Example for the result of this exercise.
```

The layer order here from top to bottom is:
- `Sierra_Leone_health` 
- `Sierra_Leone_airports`
- `Sierra_Leone_roads` 
- `Sierra_Leone_national_borders` 
- `Sierra_leone_foodinsecurity_2015`
- Basemap: `OpenStreetMap`

```{figure} /fig/mod3_classification_ex_LayerOrder.png
---
width: 600px
name: basic classification
align: center
---
Layer order.
```
