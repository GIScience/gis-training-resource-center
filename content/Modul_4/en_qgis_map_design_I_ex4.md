# Map design Exercise : Creating a Map of Pakistan

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_modul_3_exercises.html
__Click here to return to the exercise overview page for module 3__ 
:::
::::{grid} 2
:::{grid-item-card}
## Aim of the exercise:
Participants will work with multiple layers and conduct spatial queries. Additionally, they will learn how to create their own geodata.
#### Type of trainings exercise:
- This exercise can be used in online and presence training. 
:::
:::{grid-item-card}
#### These skills are relevant for 

- QGIS Essentials
- Working with multiple layers
- Conduct spatial queries
- Creation of geodata

:::
::::

::::{grid} 2
:::{grid-item-card}
#### Estimated time demand for the exercise.
- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.
:::

:::{grid-item-card}
### Relevant wiki articles

* [Visualisation of Vector Data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_visualisation_wiki.html)
* [Map Making](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_map_making_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Geodata Classification - Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)

:::
::::

::::{grid} 1
:::{grid-item-card}

#### Context
In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. You have already conducted an analysis utilizing actual data from this natural disaster. We now want to visualize our findings on an appealing map that can be printed out or shared with different stakeholders. The map will show specific medical centers and healthcare facilities that where impacted by the flooding. Additionally, we will visualize the viability of road access to the city of Larkana throughout the flood period.
:::
::::


### Available Data

You have created the data for Larkana in [Module 3, Exercise 4](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_module_3_ex2.html). In order to conduct this exercise please create a folder on your computer and copy your entire folder structure of Exercise 4 in there. In case you did not do Module 3 - Exercise 4 you can download the data [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_4/Exercise_2/Modul_4_Exercise_2_Larkana_flood_map.zip). Save the folder on your computer an unzip the file.


| Dataset name| Origonal title|Publisher|Download from| 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_adm2_Sindh.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) |UNO SAT | HDX |



```{hint} Folder structure
Keep your data management clean by creating a folder structure on your computer for your QGIS-projects and geodata. 
The exercise data should be saved in a location where you can easily find them and the corresponding QGIS-project
```



## Tasks

### Preparation of the data

1. Load all necesary the files into a new QGIS-project:
- Healthsites: `Health_Facilities_Flood_2024_AOI.gpkg`
- Roads:`Roads_Larkana.gpkg`
- Blocked Roads Points: `PAK_flood_2024_blocked_road.gpkg`
- Flood Extent 2024 reprojected: `PAK_2024_Minimum_Flood_Extend_reprojected.gpkg`
- Administrative Boundaries Sindh: `PAK_Sindh_adm1.shp`

Save your project and give it a clear name, e.g. "Larkana_flood_response"

2. Look into the attribute table of the different layers and look what information is available and how the attributes are named.

3. We want to make a comprehensible map, think about which data we need and what data we can leave out.
    - For example, the layer `Roads_Larkana` contains too many roads for a map on a national scale. Let's open the attribute table and look at how the roads are classified. The data is using the conventional OpenStreetMap classification: The type of road is described under the attribute `highway`. In our case, it might be useful to only display the primary and secondary roads, so all the features where `highway=primary` OR `highway=secondary`.

### Part 1: Symbolization

Now we have assigned a symbol for each layer at our disposal. Look at the map you created and decide if you want to adjust any symbology to make the map easier to read. Do you need to change some colours? Are the layers ordered in a way that the information is visible? Is the font size appropriate, or does it cover up too much information?
Let's go trhough the layers one by one and visualize them in a meaningful way.

__Healthsites__

Doubleclick on the point next to your healthsites vector layer. The symbology window will open. Let's create our own customized symbol for healthcare facilies.
- Under `Symbol layer type`, select __"SVG Marker"__
- Scroll down to the SVG-Browser. Here you will find all the folder of your installed SVG-libraries.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

- Under `landmark` you will find the crescent moon, click on it.

```{figure} ../../fig/crescent_moon.PNG
---
width: 700px
name: SVG Marker
---
Create customized SVG Marker
```
- you can adjust its color and size and rotate it 180° in order to turn it around.
- on the upper right click on the __+__ in order to add another "Simple Marker". Choose a circle and adjust its color and size in order to fit arounf the crescent moon.

__Roads__

For categorized classification of the roads right-click on the layer __Roads_Larkana__ in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
* On the top you find a dropdown menu. Open it and choose `Categorized`. Under `Value` select “higway”.
* Further down the window, click on `Classify`.  Now you should see all unique values or attributes of the selected “Flood_affacted” column.  You can adjust the colours by double-clicking on one row in the central field.
* Remove the tick from all categories except: `motorway`, `primary`, `secondary`, `trunk`

    ```{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Pakistan road classification
    ```
* You have the option to customize the width of the main roads' lines to improve the visualization. Open the Symbology window, then select 'Symbol'. In the new window, you can adjust the width of the lines to your preference.
    

    ```{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Pakistan road classification
    ```
* Once you are done, click `Apply` and `OK` to close the symbology window.


__Blocked Roads Points__

Open the __Symbology Tab__ for the `PAK_flood_2024_blocked_road`-layer and choose a meaningful symbol for flood related blocked roads.


__Airport__

In the [previous exercise](/content/Modul_3/en_qgis_module_3_ex2.md) you found out that the Mohenjodaro Airport in the southwest of Larkana City is still accessibible via the road network. Essential supplies could potentially be transported from the airport into the city without encountering any roadblocks. We want to point out this possibility. Let's mark the airport as a point and visualize it!

To do so we will create an entirely new point dataset representing airports.
* Click on  `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md#create-a-new-layer)) 
* Under `Database` click on ![](/fig/Three_points.png) and navigate to `temp` folder. Give the new dataset the name __“PAK_airports”__. Click `Save`.
* `Geometry type`: Select `Point`
* Under `Additional dimension` you should always make sure that you check `None`. 
* Select the coordinate reference system (CRS) "EPSG:4326-WGS 84". By default, the QGIS selects the project CRS. 
* Under `New Field` you can add columns to the new layer. Add the column __“Airport”__.
* `Type`: Select `Text Data`
* Click on `Add to Fields List` ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
* Click `OK`.
* Your new layer will appear in the `Layer Panel`

 
    ```{figure} /fig/Create_Geopackagelayer_airport.PNG
    ---
    width: 400px
    name: Digitalising airports
    align: center
    ---
    Digitalising airports
    ```

 Now you can create a point for the airport and if you would like additional aitports as well [wiki](/content/Wiki/en_qgis_digitalization_wiki.md#add-geometries-to-a-layer). Currently the new layer __“PAK_airports”__ is empty. To add features we can use the `Digitizing Toolbar`. If you cannot see the toolbar `View` -> `Toolbars` and check `Digitizing Toolbar` ([Wiki Video](/content/Wiki/en_qgis_digitalization_wiki.md#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 
*  Once you have found the airport, click on it![](/fig/mActionCapturePoint.png). Left-click on the feature you want to digitalise.
* Once you click on a place, a window will appear. Indicate that the road is blocked by writing `Yes` in the field `Blocked_road`.

    ```{figure} /fig/Feature_Att_Airport.PNG
    ---
    width: 400px
    name: Digitalising airports
    align: center
    ---
    Digitalising airports
    ```

* Once you are done with digitizing click on ![](/fig/mActionSaveEdits.png) to save your edits.
* Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

Now we can use an icon instead of just a point to display the layer __“PAK_airports”__ to visualise this fact better.

* Right-click on the layer__“PAK_flood_2024_blocked_road”__in the `Layer Panel` -> `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab.
* Keep the single symbol option. Select any symbol from the list that is appropriate for marking blocked roads. 
*  Once you are done, click `Apply` and `OK` to close the symbology window.

    ```{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visulsing blocked roads with icons
    align: center
    ---
    Visulsing blocked roads with icons
    ```   

__Flood Extent__

Open the __Symbology Tab__ for the `PAK_2024_Minimum_Flood_Extend_reprojected`-layer. Choose a light-blue as color and adjust the opacity to about 30%.

__Administrative Boundaries__

Open the __Symbology Tab__ for the `PAK_Sindh_amd1`-layer. Click on `Simple Fill` and adjust the `Symbol layer type` to `Simple Line`. You can furthermore adjust now the outline colour and stroke width.


__Bonus Step__: [Adding a basemap](/content/Wiki/en_qgis_basemaps_wiki.md) can help potential readers orienting themselves.

If you are happy with the symobolization of your layers, the map should be ready for a print layout.

``` {Attention}
Remember the layer concept and place all layers in a logic order. The flood extents should lay under the roads and the several point layer above the roads.
```



### Part 2: Creating the print layout

Once you are happy with the symbolization and colours of your data, the next step is to create a print layout. By adding additional information such as a title, data sources, projection, description, etc. you provide your audience with the means to contextualise and evaluate the map and it's content by themselves.

1. Open a new print layout and give it a name (e.g. Larkana_floods).
    - Go to __Project > New Print Layout > enter a name for the new print layout > click OK__


```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

- A new window with a blank print layout will appear. This is the print layout designer.
    - On the left, you will find a toolbar with tools to add and move items on the print layout canvas.
    - On the right you will find a list of items you added to the print layout (it is still empty). Beneath this, you will find a tab called __"item properties"__. This is where you modify the items on your print layout (e.g. enter the text for a text box or change the font).

2. Insert a new map by clicking on ![New Map Icon](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) on the left toolbar, and drawing a rectangle on the print canvas. [Video](/content/Modul_4/en_qgis_map_design_2.md#adding-a-new-map)

3. Move and position the map so that the area of interest is visible at a reasonable scale.

4. Let's add a title:
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Drag a rectangle on the canvas
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter your map title (e.g. Larkama Flood Response 2024).
    - Adjust the font size: Click on the __Font__ dropdown menu and adjust the font size for a title (25p or more). Adjust the text box if necessary.

5. Let's add a legend:
    - Click on  ![Add legend icon](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`). 
    - Navigate to the __Item Properties__ panel on the right. 
    - Scroll down a bit and check turn off `Auto Update` by unchecking the check box. Now you can freely edit every item on the legend
    - Adjust the legend by removing unnecessary layers (which are not seen on the map) and rename the layer in the legend by clicking on ![Edit Icon](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) below the legend entries.
    - Under the upper `Main Properties`, insert "Legend" as title

```{figure} ../../fig/Larkana_Legend.PNG
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

6. Now, let's add a scale bar:
    - Click on ![Add Scale bar icon](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Draw a rectangle on the map and position the scale bar on the edge of the map. You can adjust the scale bar units (meters, kilometers, ...), the fixed segment width (50 km, 75 km, 100 km, ...) and the number of segments (to the right).

7. Let's add a north arrow:
    - Click on ![Add North Arrow Icon](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`). 
    - Drag a rectangle on the print layout. Adjust the size and location of the north arrow. You can also change the icon in the item properties.

8. Let's add a logo (for example, your national society):
    - Click on ![Add Picture](/fig/30.30.2_print_layout_add_image.png) (`Add picture`)
    - Drag a rectangle in the spot where you want to add the logo
    - Navigate to the `Item properties` panel on the right and switch to `Raster image`. 
    - Click on the three dots `...` and select the file with your logo
    - If necessary, resize or move the picture on the print layout.

9. Add some additional information as text.
    - Click on ![Add text icon](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Drag a rectangle on the canvas
    - In the item properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter some additional information of the map, e.g. the coordinate system, basemap information or date.

When you are finished with your map design you can export your printable map as image or pdf under `Layout`--> `Export as Image` or `Export as PDF`

You could now have as a result a map similar to this one. Here, some space has been left in order to implement an overview map. If you are still have time go for the bonus exercise and add an overview map!

```{figure} ../../fig/Larkama_Map_withoutOverview.PNG
---
width: 700px
name: Map Larkama
---
Map Larkama
```

### Bonus Exercise!

If you are finished with the main map, click on the map and navigate to the item properties. In the layer section, check the box `Lock Layers` and `Lock styles for layers`. This means that if you change the map in the main QGIS-window, the map you have added to the Now you can start working on an overview map. We will be using a shapefile with the administrative bounadries of Pakistan.  

1. Return to the main QGIS window and load the layers from the `Bonus Exercise`-folder.
2. In the __Layer__ panel, make the layers for the main map invisible by clicking on the ![Eye Icon](/fig/30.30.2_layer_visibility_icon.png) next to the layer name.
3. Style the countries in an neutral, unobtrusive color. For example, you can use the "__Gray 3 Fill__" from the styling templates.
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
Map Larkama
```


Congratulations! You have finished your first map.


