::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercise 2: Creating a Flood Situation Map of Larkana, Pakistan

::::{grid} 2
:::{grid-item-card}
__Larkana flood response exercise track:__
^^^

This exercise is the fourth part of the [Larkana flood response exercise track](https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/en_larkana_flood_response.html). 

The previous exercise can be found [here](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_ex5.html)

:::
:::{grid-item-card}
__Competences covered in this exercise:__
^^^ 

- Working with multiple layers
- Importing SVG libraries
- Using SVG markers
- Classifying Geodata
- Creating a print layout
- setting up overview maps

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant wiki articles:__
^^^

* [Visualisation of Vector Data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_visualisation_wiki.html)
* [Map Making](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_map_making_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Geodata Classification - Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)

:::
::::

::::{topic} Context

In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. As a result, critical infrastructure, such as health facilities, were impacted and road access to the city of Larkana was severly limited. You have already conducted an analysis utilizing actual data from this natural disaster in the [previous exercise](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_ex5.html). We now want to visualize our findings on an appealing map that can be printed out or shared with different stakeholders. The map will show specific medical centers and healthcare facilities that where impacted by the flooding. Additionally, we will visualize the road access to the city of Larkana on August 12 2024. This information is crucial to assess the logistical access to the city. 
 
The exercise is split into two parts. In the first part, you will adjust the symbolisation of the layers for the final map. In the second part, you will use the print layout composer to create a finished map that can be printed and distributed. 

::::

```{figure} ../../fig/Larkana_Map_Overview.png
---
width: 700px
name: Map Larkama
---
The map we will be making in this exercise (Source: HeiGIT).
```
### Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/Exercise_2/Module_4_Exercise_2_Larkana_flood_map.zip

You have created the data for Larkana in [Module 3 Exercise 5](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_ex2.html). In order to conduct this exercise please create a folder on your computer and copy your entire folder structure of Exercise 4 in there. __In case you did not do Module 3 - Exercise 4 you can download the data [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/Exercise_2/Module_4_Exercise_2_Larkana_flood_map.zip)__. Save the folder on your computer an unzip the file.
:::


| Dataset name | Original title | Publisher | Downloaded from | 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| Health_Facilities_Flood_2024_AOI.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| PAK_2024_Minimum_Flood_Extend_reprojected.gpkg | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) | UNO SAT | HDX |
| PAK_flood_2024_blocked_road.gpkg | PAK_flood_2024_blocked_road | Yourself | This dataset was created in the [previous exercise](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_module_3_ex2.html) | 


<!--FIX: add all datasets used in this exercise to the table-->


```{hint} Folder structure
Keep your data management clean by creating a standard folder structure on your computer for your QGIS-projects and geodata. 
```

## Task 1: Preparing the Data


1. Create a new QGIS-project and save it to your exercise folder. Give it a clear name, e.g. "Larkana_flood_response_map".

2. In the __Browser panel__, Open the `Project Home`-folder and navigate to the data subfolder. 
3. Import the layers in the folder and import the layers to your QGIS-project:
    - Healthsites: `Health_Facilities_Flood_2024_AOI.gpkg`
    - Roads: `Roads_Larkana.gpkg`
    - Blocked Roads Points: `PAK_flood_2024_blocked_road.gpkg`
    - Flood Extent 2024 reprojected: `PAK_2024_Minimum_Flood_Extend_reprojected.gpkg`

4. Take a moment to familiarise yourself with the available data. Look into the attribute table of the different layers and look what information is available and how the attributes are named.

5. [Add a basemap](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#standard-qgis-basemaps):
    - Navigating to the menu bar -> `Layer` -> `Add Layer` -> `Add XYZ-Layer...` and add a OpenStreetMap basemap. 


## Task 2: Symbolization

Creating a good map involves selecting appropriate icons and colours to transmit the information in your data. 
The first step into creating a comprehensible map is to order the layers logically so you can see the information:

In the layers panel: 
- Put the administrative boundaries layer at the bottom,
- put the roads and flood extent layers in the middle,
- and put the point layers (healthsites and blocked roads) to the top.

Each layer has it's own [symbology panel](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#styling-panel) where you can adjust the symbology, colours and labels for the features in that layer. Do you need to change some colours? Are the layers ordered in a way that the information is visible? Think about which data we need and what data we can leave out. 
For example, the layer `Roads_Larkana` contains too many roads for a map on a national scale. Let's open the attribute table and look at how the roads are classified. The data is using the conventional OpenStreetMap classification: The type of road is described under the attribute `highway`. In our case, it might be useful to only display the primary and secondary roads, so all the features where `highway=primary` OR `highway=secondary`.

Let's go through the layers one by one and visualize them in a meaningful way.

### __Healthsites:__

In the __layers panel__, right click on the layer `Health_Facilities_Flood_2024_AOI` > `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
Let's create our own customized symbol for healthcare facilities:
1. Under `Symbol layer type`, select __"SVG Marker"__.
2. Scroll down to the SVG-Browser. Here you will find all the folders of your installed SVG-libraries.

:::{dropwodn} Video: Using SVG symbols 
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>
:::

- Scroll through the folder until you find a suitable symbol (e.g. ![](/fig/en_m4_ex_2_cross_symbol.png)).

```{figure} ../../fig/crescent_moon.PNG
---
width: 450px
name: SVG Marker
---
Create customized SVG Marker.
```

We can customise the icon further:

- On the upper right corner of the symbology tab, click on the `+` to add another "Simple Marker".
- By default, it will be a circle. Make sure the circle is below the ![](/fig/en_m4_ex_2_cross_symbol.png)-symbol by clicking on the ![](/fig/m4_ex2_down_symbol.png).
- Change the colour of the circle to white.
- Click `Apply`, then `OK`.

```{figure} /fig/en_3.36_m4_ex2_complex_symbol.png
---
name: m4ex2_complex_symbol
width: 450 px
---
You can use several symbol layers to create a complex symbol in QGIS 3.36.
```

### __Roads:__

The roads dataset contains a lot of information that we do not necessarily want to display on our final map. We can categorise the data and hide the unwanted information. We already identified the important roads in the previous exercise: The roads where __"highway"__ equals `motorway`, `primary`, `secondary`, `trunk`. These roads are the __major roads__. 



We can categorise the roads and then select the relevant roads to be displayed. To categorize the roads, double-click on the layer `Roads_Larkana`. The properties window will open with a vertical tab bar on the left. Navigate to the __Symbology tab__.
- On the top you find a dropdown menu. Open it and choose `Categorized`. 
- Under `Value` select “highway”.
- Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affected” column.  You can adjust the colours by double-clicking on one row in the central field.
- Remove the tick from all categories except: `motorway`, `primary`, `secondary`, `trunk`

    ```{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Classifying the roads: By unchecking the boxes you can hide the unnecessary information.
    ```

* You have the option to customize the width of the main roads' lines to improve the visualization. Open the Symbology window, then select 'Symbol'. In the new window, you can adjust the width of the lines to your preference.
    
    ```{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Classifying the roads: You can adjust the width of a single category.
    ```

* Once you are done, click `Apply` and `OK` to close the symbology window.

### __Blocked Roads Points:__

* Right-click on the layer __“PAK_flood_2024_blocked_road”__ in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
* Keep the single symbol option. Select any symbol from the list that is appropriate for marking blocked roads. 
* Once you are done, click `Apply` and `OK` to close the symbology window.

    ```{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visulsing blocked roads with icons
    align: center
    ---
    Visualising blocked roads with icons
    ```   


### __Airports:__

In the [previous exercise](/content/Module_3/en_qgis_module_3_ex2.md) you found out that the Mohenjodaro Airport in the southwest of Larkana City is still accessible via the road network. Essential supplies could potentially be transported from the airport into the city without encountering any roadblocks. We want to point out this possibility. Let's mark the airport as a point and visualize it!

To do so we will create an entirely new point dataset representing airports.
* Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](/content/Wiki/en_qgis_digitisation_wiki.md#create-a-new-layer)) 
* Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name __“PAK_airports”__. Click `Save`.
* `Geometry type`: Select `Point`
* Under `Additional dimension` you should always make sure that you check `None`. 
* Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
* Under `New Field` you can add columns to the new layer. Add the column __“Airport”__.
* `Type`: Select `Text(string)`
* Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
* Click `OK`.
* Your new layer will appear in the `Layer Panel`.

    ```{figure} /fig/Create_Geopackagelayer_airport.PNG
    ---
    width: 400px
    name: Digitising airports
    align: center
    ---
    Creating a new point layer for the airports.
    ```

::::{margin}
:::{tip}
If you cannot see the toolbar `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](/content/Wiki/en_qgis_digitisation_wiki.md#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png)
:::
::::

* Now you can create a point for the airport and if you would like additional airports as well ([wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitisation_wiki.html#add-geometries-to-a-layer)). Currently the new layer __“PAK_airports”__ is empty. To add features we can use the `Digitising Toolbar`. 

*  Look for the Mohenjodaro Airport in Google. Once you have found the airport, click on ![](/fig/mActionCapturePoint.png). Left-click on the feature you want to digitise.

    ```{figure} /fig/Feature_Att_Airport.PNG
    ---
    width: 400px
    name: Digitising airports
    align: center
    ---
    Digitising new point features.
    ```

* Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
* Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

Let's symbolise the airport with a plane icon, so we can identify it quickly.  

* Right-click on the layer __"PAK_airports"__ in the `Layer Panel` -> `Properties`. A new window ill open up with a vertical tab section on the left. Navigate to the [`Symbology`-tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#styling-panel).
* Click on `Simple Marker`.
* Under `Symbol layer type`, select __SVG-Marker__.
* Scroll down a bit and you will find a box with all the SVG-symbols available.
* In the search bar under the box, search for "Plane". 
* Select a plane symbol.
* Click `Apply`, then `Ok`.


### __Flood Extent:__

Open the __Symbology Tab__ for the `PAK_2024_Minimum_Flood_Extend_reprojected`-layer. Choose a light-blue as color and adjust the opacity to about 30%.

```{figure} /fig/Module_4/m4_ex2_symbology_flood.png
---
name: m4_ex2_symbology_flood.png
width: 550 px
---
Adjusting the symbology to indicate the flooded area. 
```

## Task 3: Creating the print layout

Once you are happy with the symbolization and colours of your data, the next step is to create a __print layout__. The print layout is where you put all the elements from you map together with additional information to create a comprehensive map. By adding additional information such as a title, data sources, projection, description, etc. you provide your audience with the means to contextualise and evaluate the map and it's content by themselves.

1. Open a new print layout and give it a name (e.g. Larkana_floods).
    - Go to `Project` > `New Print Layout` > enter a name for the new print layout > click `OK`.

```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Creating a new print layout.
```

- A new window with a blank print layout will appear. This is the print layout composer.
    - On the left, you will find a toolbar with tools to add and move items on the print layout canvas.
    - On the right you will find a list of items you added to the print layout (it is still empty). Beneath this, you will find a tab called __"item properties"__. This is where you modify the items on your print layout (e.g. enter the text for a text box or change the font).

2. Insert a new map by clicking on ![New Map Icon](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) on the left toolbar, and drawing a rectangle on the print canvas. [Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.md#adding-a-new-map)

3. Move and position the map so that the area of interest is visible at a reasonable scale. To move the map content, use the tool ![](30.30.2_print_layout_move_content_icon) `Move item content`. 


```{figure} /fig/Module_4/m4_ex2_print_layout_add_map.png
---
name: m4_ex2_print_layout_add_map
width: 650 px
---
Adding the map to the print layout.
```

4. Let's add a label for the city of Larkana. This will help your audience that might be unfamiliar with the region orientate themselves. 
    - Click on the ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`).
    - Draw a small rectangle next to the city of Larkana.
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Enter "Larkana" instead. 
    - Click on the __Font__ dropdown menu and adjust the font size so it can be read easily.
    
```{figure} /fig/Module_4/m4_ex2_print_layout_label_city
---
name: m4_ex2_print_layout_label_city
width: 600 px
---
Adding a label for the city of Larkana.
```

4. Let's add a title:
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`).
    - Drag a rectangle on the canvas.
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter your map title (e.g. "Larkana, Flood-affected Healthsites and Roads").
    - Adjust the font size: Click on the __Font__ dropdown menu and adjust the font size for a title (25p or more). Adjust the text box if necessary.
    - Below the font dropdown menu, add a little bit of horizontal and vertical margin. 

```{figure} /fig/Module_4/m4_ex2_print_layout_add_title.png
---
name: m4_ex2_print_layout_add_title
width: 600 px
---
Adding a title to the print layout.
```


5. Let's add a legend:
    - Click on  ![Add legend icon](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`). 
    - Drag a rectangle on the canvas.
    - Navigate to the __Item Properties__ panel on the right. 
    - Scroll down a bit and check turn off `Auto Update` by unchecking the check box. Now you can freely edit every item on the legend
    - Adjust the legend by removing unnecessary layers (which are not seen on the map) and rename the layer in the legend by clicking on ![Edit Icon](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) below the legend entries. Use the ![](/fig/Module_4/m4_ex2_print_layout_add_to_legend.png)-icon to add or remove layers from the legend.
    - Under the upper `Main Properties`, insert "Legend" as title. 

```{figure} ../../fig/Larkana_Legend.PNG
---
width: 700px
name: Create Print Layout
---
Adjusting the legend.
```

6. Now, let's add a scale bar:
    - Click on ![Add Scale bar icon](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Draw a rectangle on the map and position the scale bar on the edge of the map. You can adjust the scale bar units (meters, kilometers, ...), the fixed segment width (e.g. 10 km, 20 km, 50 km, ...) and the number of segments (to the right). 

7. Let's add a north arrow:
    - Click on ![Add North Arrow Icon](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`). 
    - Drag a rectangle on the print layout. Adjust the size and location of the north arrow. You can also change the icon in the item properties.

8. Let's add a logo (for example, your national society):
    - Click on ![Add Picture](/fig/30.30.2_print_layout_add_image.png) (`Add picture`)
    - Drag a rectangle in the spot where you want to add the logo.
    - Navigate to the `Item properties` panel on the right and switch to `Raster image`. 
    - Click on the three dots `...` and select the file with your logo (for this exercise the logo for the Pakistani Red Crescent Society is saved here: `/Module_4_Exercise_2_Larkana_flood_map/img/`).
    - If necessary, resize or move the picture on the print layout.

9. Add some additional information in a text box. 
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Drag a rectangle on the canvas
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter some additional information of the map, e.g. the coordinate system, basemap information or date. 

When you are finished with your map design you can export your printable map as image or pdf under `Layout`--> `Export as Image` or `Export as PDF`.

You could now have as a result a map similar to this one. Here, some space has been left in order to implement an overview map. If you are still have time go for the bonus exercise and add an overview map!

```{figure} ../../fig/Larkana_Map_withoutOverview.png
---
width: 700px
name: Map Larkama
---
Your final map could look something like this.
```

### Bonus Exercise

If you are finished with the main map, click on the map and navigate to the item properties. In the layer section, check the box `Lock Layers` and `Lock styles for layers`. This means that if you change the map in the main QGIS-window, the first map you have added to the print layout will not be affected by these changes. Now you can start working on an overview map. We will be using a shapefile with the administrative boundaries of Pakistan.  

1. Return to the main QGIS window. Navigate to the folder `Module_4_Exerise_2_Larkana_flood_map/data/Bonus_exercise/` and load the layer `PAK_admbnda_adm0_wfp_20220909` into your QGIS-project.
2. In the __Layer__ panel, make the layers for the main map invisible by clicking on the ![Eye Icon](/fig/30.30.2_layer_visibility_icon.png) next to the layer name.
3. Style the country boundary (ADM0) in a neutral, unobtrusive color. For example, you can use the "__Gray 3 Fill__" from the styling templates.
4. Once you are happy with the styling of your overview map, navigate back to the __Print Layout window__.
5. Add a second map and position it in a corner.
6. In the __Item properties__ panel for the second Map ("__Map 2__"), scroll down and open the `Overview`-options.
7. Click on the `+`-button to add a new overview.
8. In the "__Map Frame__"-option, select "__Map 1__". This will show the frame of the main map on your overview map.
9. You can add a scale bar and a northj arrow to your overview map as well.

```{figure} ../../fig/Larkana_Map_Overview.png
---
width: 700px
name: Map Larkama
---
The finished map could look something like this (Source: HeiGIT).
```

> Congratulations! You have created a finished map that is ready to be printed and distributed. 


