::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_exercises.html 
{octicon}`undo;1.5em;sd-text-danger`
:::
::::


# Exercise 2 (Geodata Classification): Map of food insecurity in Sierra Leone

## Characteristics of the exercise

:::{card}
__Aim of the exercise:__
^^^

This exercise aims to create an overview map of the distribution of food insecurity in Sierra Leone at district level. To do this, we will visualise both the distribution of food insecurity and key infrastructure elements such as hospitals, airports and roads. 

:::

::::{grid} 2
:::{grid-item-card}
__Type of exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__These skills are relevant for__ 
^^^

- QGIS Essentials
- The skills tested in this exercise are necessary for all GIS-users.
- Classifying geographic data

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 1 hour to complete, depending on the number of participants and trainers. 

:::

:::{grid-item-card}

### Relevant Wiki Articles

* [QGIS Interface](/content/Wiki/en_qgis_interface_wiki.md)
* [Types of Geodata](/content/Wiki/en_qgis_geodata_types_wiki.md)
* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Layer Concept](/content/Wiki/en_qgis_layer_concept_wiki.md)
* [Attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)
* [Table function - Add field](/content/Wiki/en_qgis_table_functions_wiki.md)
* [Geodata Classification- Categorized](/content/Wiki/en_qgis_categorized_wiki.md)
* [Geodata Classification- Graduated](/content/Wiki/en_qgis_graduated_wiki.md)
* [Digitization- Point data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer)

:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

### Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::


### Available Data

Download all datasets __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_2/Module_3_Exercise_2_Sierra_Leone.zip)__ and save the folder on your computer. Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. Under "data > input" you will find the following files:

- `Sierra_leone_foodinsecurity_2015.shp` (Polygon) Shapefile
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra_Leone_national_borders (Lines)
    - Sierra_Leone_provinces (Lines)
- `Sierra_leone_roads.gpd` (Lines) GeoPackage
- `Sierra_leone_healthsites.gpkg` (Points) Geopackage
- `sl_airports.gpkg` (Points) GeoPackage

### Tasks

Our goal is to produce an overview of the 2015 food insecurity situation in Sierra Leone together with the display of main infrastructure elements. To achieve this, we will visualise total food insecurity classifications alongside airports, hospitals, and primary roads in a map.

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. Once the project is created save the project in the “project” folder of the “Ex_Sierra_Leone_foodinsecurity”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Sierra_Leone_foodinsecurity”.

3. Import the GeoPackages `Sierra_leone_borders.gpkg`, `Sierra_leone_airports`, `Sierra_leone_healthsites` and `Sierra_leone_roads.gpkg` as well as the shapefile `Sierra_leone_foodinsecurity_2015.shp` into your project via drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-raster-data-via-drag-and-drop)). 
Or by clicking `Layer`-> `Add Layer`-> `Add Vector Layer`: Click on the three dots ![](/fig/Three_points.png) and navigate to "Sierra_leone_borders.gpkg" in your file Browser. Select the file and click `Open`. Back in QGIS click `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-raster-data-via-layer-tab)).

```{Attention}
GeoPackages can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```

4. First, let's add a basemap to your map canvas using the plugin `QuickMapServices` by clicking on the ![](/fig/QMS_search_icon.png) symbol in you project toolbar. Search for "Bing Maps Satellite Imagery" in the QMS panel and add the base map layer via double click.  For an optimised view [adjust the opacity](https://www.youtube.com/watch?v=WguUkN1YRzY&ab_channel=GISBigfootAnswers) of your layers to optimise the use of the base map. 

5. Using  the attribute table of the airports layer zoom to Tongo Airport by right-clicking on the row in the attribute table and selecting `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)). Check the Basemap. Do you think the airstrip is still operational? The answer is no, according to Wikipedia. Delete Tongo Airport in the [Attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md). Delete Kabala airport too, since it is also not operational anymore.

6. Now we want to check out the airports of the cities of Bo and Kenema. Are these airstrips in better shape? If yes, add them to the airport layer. To find these cities on your map interface use the QGIS Plugin `OSM Place Search`. 
To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for "OSM Place Search". Once you have found it click on it and select `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html)).
    * In the panel, you can search for places on the OpenStreetMap by typing the name in the search bar. Often it makes sense to add additional information like the name of the country. Try for example “Bo, Sierra Leone”.

```{figure} /fig/mod3_classification_ex_OSMsearch.png
---
width: 400px
align: center
---
OSM place search.
```

Add the airports of Bo and Kenema as points to the layer `Sierra_Leone_airports`. Find help on the addition of features to a point layer [here](/content/Wiki/en_qgis_digitalization_wiki.md). 
 

8. *Optional:* In the attribute table, create a new column `Runway_length` and add the length of the runways of Bo and Kenema by measuring them approximately with the measuring tool ![](/fig/measuring_tool_icon.png).

9. Now we want to create a intuitive visualisation of the differences in food insecurity. To achieve this we use the "[Graduated Classification](/content/Wiki/en_qgis_graduated_wiki.md)" visualization option for the layer `Sierra_leone_foodinsecurity_2015` by displaying the polygons according to classes created based on the "Total_FI" column in the attribute table.
    * Right-click on the layer `Sierra_leone_foodinsecurity_2015.shp` in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
    * In the topmost dropdown menu choose `Graduated`. Under `Value` select “Total_FI”.
    * Further down the window click on `Classify`. You now should see multiple classes based on the value range of the "TotalFI" column represented with different colours.  You can adjust the colours by picking different colour palettes in the drop down menu `Color ramp`. Also, you can modify the value distribution of the classes by selecting different classification modes ([Wiki](/content/Wiki/en_qgis_graduated_wiki.md)) in the `Mode` dropdown menu. 
    * Play around with these options to achieve a colour scheme that suits the data. Once you are done, click `Apply` and `OK` to close the symbology window.

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

11. As a last visualisation step open the `Symbology` tab `Sierra_Leone_roads (Lines)` and like in step 9 open the top dropdown menu. Now instead of `Graduated` choose [Categorized Classification](/content/Wiki/en_qgis_categorized_wiki.md) and select "highway" in the `Value` menu. Click `Classify` to get a classification with individual colours for all unique values of the "highway" column. In the squares next to the classes, deselect all classes except for "primary". You can change the colour of the classes by manually clicking and adjusting the colour in the drop "Symbol" dropdown menu near the top of the window.

```{figure} /fig/mod3_classification_ex_Categorizedclassification.png
---
width: 900px
name: basic classification
align: center
---
Categorized highways Sierra Leone.
```

12. Set all the layers you loaded into your project to visible and arrange them in an order that is suitable for a good visualization of the food insecurity as well as the infrastructure elements. Choose a basemap that you think is suitable. Your final result could look like this:

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
