# Map design Exercise 1: Creating a Map of Ghana


## Characteristics of the exercise

::::{grid} 2
:::{grid-item-card}

## Aim of the exercise

The aim of this exercise is to create an overview map of Ghana with its subdistricts, main roads, settlements, as well as hospitals. Such information can  be of use in humanitarian work. The first part of the exercise will cover the symbolisation of the data layers. The second part will focus on the design of the print layout.

#### Type of trainings exercise:

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}

#### Focus group (GIS-Knowledge Level)


#### These skills are relevant for 

- visualising geographic data 
- creating maps to communicate information

:::
::::

::::{grid} 2
:::{grid-item-card}

#### Estimated time demand for the exercise.

- The exercise takes around 5 hours to complete, depending on the number of participants and trainers. 

:::

:::{grid-item-card}

## Relevant Wiki Articles

- [Visualisation](/content/Wiki/en_qgis_visualisation_wiki.md)  
- [Module 4: Visualisation of Geodata](/content/Modul_4/en_qgis_map_design_I.md)  
- [Module 4: Map Design: The Print Layout](/content/Modul_4/en_qgis_map_design_2.md)
:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md#how-to-do-trainings) for some general tips on training conduction

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

## Available Data

__Download the data for the exercise [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_4/Modul_4_Exercise_1_creating_a_map_of_ghana/Modul_4_Exercise_1.zip).__  
It is always important to make yourself familiar with the data at your disposal.
For this exercise, we will use the following layers:

- Ghana - Subnational Administrative Boundaries (https://data.humdata.org/dataset/cod-ab-gha)
- Ghana Health Facilities (OSM Export; https://data.humdata.org/dataset/hotosm_gha_health_facilities); This data has been cleaned up to only contain hospitals.
- Ghana roads (OSM Export; https://data.humdata.org/dataset/hotosm_gha_roads)
- Ghana settlements (https://data.humdata.org/dataset/ghana-settlements); This data has already been modified. Only the regional, district and country capitals are available.

All data has been downloaded from the Humanitarian Data Exchange. Download the Data from the Nexus, __unzip the folder__, and load the data into a new QGIS project.




## Tasks

### Preparation of the data

1. Load the `.shp`-files into a new QGIS-project.
2. Look into the attribute table of the different layers and look what information is available and how the attributes are named.
3. We want to make a comprehensible map, think about which data we need and what data we can leave out.
    - For example, the layer `hotosm_gha_roads_lines` contains too many roads for a map on a national scale. Let's open the attribute table and look at how the roads are classified. The data is using the conventional OpenStreetMap classification: The type of road is described under the attribute `highway`. In our case, it might be useful to only display the primary and secondary roads, so all the features where `highway=primary` OR `highway=secondary`.

### Part 1: Symbolization

Now that we are familiar with the data at our disposal, let's choose the symbology for the different layers. Which information should be displayed on the map?

Let's start with the administrative boundaries. We want to show the names and outlines for the `adm_1`-layer, as well as the outlines for the `adm_2`-layer.

1. Put the layers for the administrative boundaries in an ascending order with `adm_0` at the bottom, followed by `adm_1` and `adm_2`
2. Open the __Symbology Tab__ for the `adm_2`-layer. Set the __Fill color__ to transparent and the __Stroke width__ to 0.16 Millimeters and the __Stroke style__ to a dashed line.
3. Open the __Symbology Tab__ for the `adm_1`-layer and set the colour as transparent. Leave the stroke width at 0,26 Millimeters and the stroke style as a solid line.
4.  Open the __Symboloy Tab__ for the `adm_0`-layer and set it to a neutral colour (such as a light gray).
5. We want to display the names of the regions (`adm_1`). Open the __Labels Tab__ for the `adm_1`-layer. Select "Single Labels" and choose the attribute `ADM1_EN` for the values that are to be displayed.

---

Let's move on to the settlements.

The layer for the settlements has been cleaned up and only the towns, regional capitals, district capitals, and country capitals are available.

1. Open the __Symbology Tab__ for the `gha_ppl_1m_NGA`-layer and select a categorized symbology.
2. Under "Value", select `popPlace1`
3. Click on "Classify"
4. A list of all the unique values will appear. Assign each a dark grey point marker.
5. We want to be able to differentiate between country, regional, or district capital. The most important capital is the country capital, followed by regional capitals and finally the district capitals. Give each point marker a different size corresponding to its importance.
6. Let us add a label for the country capital and regional capitals next.
7. Navigate to the "__Label Tab__" and select __"Rule-based Labelling"__
8. Add a new rule and enter the following expression in the Filter: `(  "popPlace1"  =   'Country capital'  ) OR ( "popPlace1" = 'Regional capital' )`
9. Set the "Value" to `Name`.
10. Make the font italic and draw a text buffer in order to differentiate the settlement labels from the labels of the regions.

---

Let's move on to the road network.

1. The layer for the road network should sit on top of the administrative boundaries so the course and connections of roads is always visible.
2. Open the __Symbology Tab__ for `hotosm_gha_roads_lines`. Select "__Rule-based__" and add a new filter by double clicking on `(no filter)`. 
3. Open the expression builder by clicking on the icon to the right of the filter option.
4. First, open a parenthesis by double-clicking on `(`.
5. In the middle tab of the expression builder, expand the __"Fields and Values"__ list. Double click on `highway` to add it to the expression on your left. Next, on the right, click on `All Unique` to list all the possible values of that attribute.  
6. Under the left window, click on the `=`-sign to add it to your expression.
7. In the list with all the unique values. Select `primary` and add it to your expression.
8. Close the parenthesis by clicking on `)` under the expression field on the left.
9. Add the Operator `OR` and repeat the same expression with the parenthesis but select the unique value `secondary`
10. The finished expression should be  `(  "highway"  =  'primary' )  OR  ( "highway"  =  'secondary'  )`
11. Select a colour and thickness for the line so it is distinguishable from the administrative boundaries (e.g. yellow; keep in mind that some colors have conventional associations; blue for water for example).

---

Now, as a final touch, let's select a symbol for the health facilities:

1. Navigate to the `hospital_GHA` layer
2. Open the __Symbology Tab__ and select the `Simple Marker`.
3. Under "Symbol Layer type", select SVG-Symbol.
4. Scroll down until you see the SVG-Symbol browser.
5. In the search bar, enter 'hospital'
6. Select one of the SVG-Symbols at your disposal
7. Adjust the colour to red.
8. Click Apply and Ok.

Now we have assigned a symbol for each layer at our disposal. Look at the map you created and decide if you want to adjust any symbology to make the map easier to read. Do you need to change some colours? Are the layers ordered in a way that the information is visible? Is the font size appropriate, or does it cover up too much information?

__Bonus Step__: [Adding a basemap](/content/Wiki/en_qgis_basemaps_wiki.md) can help potential readers orienting themselves.

Now the Map should be ready for a print layout.

### Part 2: Creating the print layout

Once you are happy with the symbolization and colours of your data, the next step is to create a print layout. By adding additional information such as a title, data sources, projection, description, etc. you provide your audience with the means to contextualise and evaluate the map and it's content by themselves.

1. Open a new print layout and give it a name (e.g. Ghana Map with hospitals). A new window will open with a blank canvas and a different set of tools. This is the print layout designer.
    - On the left, you will find a toolbar with tools to add and move items on the print layout canvas.
    - On the right you will find a list of items you added to the print layout (it is still empty). Beneath this, you will find a tab called __"item properties"__. This is where you modify the items on your print layout (e.g. enter the text for a text box or change the font).
2. Insert a new map by clicking on ![New Map Icon](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) on the left toolbar, and drawing a rectangle on the print canvas. [Video](/content/Modul_4/en_qgis_map_design_2.md#adding-a-new-map)
3. Move and position the map so that the entire country is visible at a reasonable scale.
4. Let's add a title:
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Drag a rectangle on the canvas
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter your map title (e.g. Map of Ghana with roads and hospitals).
    - Adjust the font size: Click on the __Font__ dropdown menu and adjust the font size for a title (25p or more). Adjust the text box if necessary.
5. Let's add a legend:
    - Click on  ![Add legend icon](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`). 
    - Navigate to the __Item Properties__ panel on the right. 
    - Scroll down a bit and check turn off `Auto Update` by unchecking the check box. Now you can freely edit every item on the legend
    - Adjust the legend by removing unnecessary layers (which are not seen on the map) and rename the layer in the legend by clicking on ![Edit Icon](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) below the legend entries.
6. Now, let's add a scale bar:
    - Click on ![Add Scale bar icon](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Draw a rectangle on the map and position the scale bar on the edge of the map. You can adjust the scale bar units (meters, kilometers, ...), the fixed segment width (50 km, 75 km, 100 km, ...) and the number of segments (to the right).
7. Let's add a north arrow:
    - Click on ![Add North Arrow Icon](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`). 
    - Drag a rectangle on the print layout. Adjust the size and location of the north arrow. You can also change the icon in the item properties.
8. Let's add a logo (for example, the IFRC logo or the logo of your national society):
    - Click on ![Add Picture](/fig/30.30.2_print_layout_add_image.png) (`Add picture`)
    - Drag a rectangle in the spot where you want to add the logo
    - Navigate to the `Item properties` panel on the right and switch to `Raster image`. 
    - Click on the three dots `...` and select the file with your logo
    - If necessary, resize or move the picture on the print layout.

```{figure} ../../fig/30.30.2_print_layout_add_picture_options.png
---
name: add picture item properties
width: 600 px
---
The item properties panel for pictures. You need to specify the save location of a picture in order to see it on the print layout.
```

9. Add a text box with additional information, sources, the author (you), and date of creation.
10. When you are happy with your print layout. You can export it as a PDF. You can save it in the project folder under "results".
11. Once you have exported the map. Look at the PDF and make sure it looks how you intended. Some things might look different in the PDF. If it does not look correct you may need to make some adjustments in the symbology.

The finished map could look something like this:

```{figure} ../../fig/en_map_design_exercise_1_results.png
---
name: Main road network and hospitals in Ghana, Africa
width: 600px
---
Some space has been left in the bottom-right corner for an overview map
```

What can we learn from this map? We can clearly identify areas that are harder to reach and where the travel time to a hospital is much longer than in the populated regions in the south of Ghana. 

### Bonus Exercise!

If you are finished with the main map, click on the map and navigate to the item properties. In the layer section, check the box `Lock Layers` and `Lock styles for layers`. This means that if you change the map in the main QGIS-window, the map you have added to the Now you can start working on an overview map. We will be using a shapefile with the countries of Africa.  

1. Return to the main QGIS window and load the layers from the `Bonus Exercise`-folder.
2. In the __Layer__ panel, make the layers for the main map invisible by clicking on the ![Eye Icon](/fig/30.30.2_layer_visibility_icon.png) next to the layer name.
3. Style the countries in an neutral, unobtrusive color. For example, you can use the "__Gray 3 Fill__" from the styling templates.
4. Once you are happy with the styling of your overview map, navigate back to the __Print Layout window__.
5. Add a second map and position it in a corner.
6. In the __Item properties__ panel for the second Map ("__Map 2__"), scroll down and open the `Overview`-options.
7. Click on the `+`-button to add a new overview.
8. In the "__Map Frame__"-option, select "__Map 1__". This will show the frame of the main map on your overview map.

Congratulations! You have finished your first map.
