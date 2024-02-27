# Sketch Map Tool Exercise 4 - Basic Visualization of the results in QGIS & uMAP
🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧





## Characteristics of the exercise 
#### Aim of this exercise:
Learn how you can visualize your Sketch Map Tool Outputs in either [QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_installation_wiki.html#qgis-installation) or [uMAP](https://umap.openstreetmap.fr/en/).

#### Phase of participatory /community mapping 
analysing participatory mapping
#### Focus group (GIS-Knowlege Level)

- Exercise builds on prior-knowledge of Sketch Map Tool. Make sure [Execise 1](https://giscience.github.io/gis-training-resource-center/content/Mobile_Data_collection/en_SMT_ex1_.html#sketch-map-tool-exercise-1-workflow-exercise) has been done before or knowlege on the background on Sketch Map Tool is there.

- GIS Beginners-level: no specific knowledge about QGIS /uMAP required

#### Type of trainings exercise:
This exercise can be used in online and presence training and is focused on an hands-on experience with the basic of QGIS or UMAP.
#### Estimated time demand for the exercise.
Exercise A: with absolute beginners 2 hours
Exercise B: 30 min

```{Tip}
Decide together with the responsible working group which GIS system is prefered and decide on one. There is no neccesity to learn/use both ways. Generally QGIS will give you more opportunities for visualization and analysis of the results, but if a simple and quick visualization without installation of software packages is desired, UMAP might be an easy solution.
```

## Instructions for the trainers 

:::{dropdown} Trainers Corner
### Preparation
- Online access and devices (PC)
- QGIS installed on the computer
- Take a look and make yourself familiar on the provided material for the exercise and the Sketch Map Tool in general. 

```{Alternatives}  
- If you like to skip parts of the workflow, make sure you have alternative material (like preprinted, or already marked Sketch maps) prepared.
- If you like to adapt this exercise to your specific use case, create your own case-description. 
```


### Available Material
* Introduction Slides about the Sketch Map Tool LINK
* Just the created map for (pre-printing)
* Pre-marked and photographed map
* Geodata of the results


### During the exercise:  
#### Introduction: 
- Introduce the idea, the aim and the general workflow of the Skech Map Tool beforehand 
- Provide access to the needed material 
- check-in if there are questions or problems.

#### Wrap up: 
- Take some time at the end to wrap up and that several people present their result map
- Discuss Benefits of showing results as a map
- Time to for Open questions.
::::


## Step-by step introduction for participants 

link where you can download this part as a short pdf to hand it to participants

If you expieriences any problems during your use of the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) please take a look at the [Help page](https://sketch-map-tool.heigit.org/help).



## Exercise A: Exploration & basic visualization of Sketch Map Tool outputs in QGIS

:::{dropdown} Exercise A: Exploaration & basic visualization of Sketch Map Tool outputs in QGIS
:open:





#### 1. Scenario and Background

critical infrastrucutre and historical flood extent

#### 1. Data Collection

Please download the prepared maps [here]().
Unzip the .zip folder in order to be able to acess the geotiff output.

Optional: You find the empty map [here](). Feel free to draw some additional flood maps by printing the template out and drawing on it or by using a simple graphics editor.


#### 2. Georeferencing and autoextraction with the Sketch Map tool

Upload the sketch maps back to the tool’s website. Head to [sketch-map-tool.heigit.org](https://sketch-map-tool.heigit.org/) and choose 'Digitize your Sketch maps' on the right. Upload all your sketches in .png or .jpg format. You can mark your sketches and simply drag and drop them into the window.

The sketch maps are now being processed and georeferenced with the annotations extracted and vectorized. Download the vectors. You may use the ones we have prepared [here]().

#### 3. Start your QGIS Project

Open QGIS and navigate to `Project` -> `New` and click on `Save`. Naviagte to where you want to save your project, give it a name and clikc `Save` again. When working in QGIS always remember to save your project every now and then.

Now load your vector file ("Schuld_Ahr-tal_sketch-map_Ex4.geojson") and geotiff file ("Schuld_Ahr-tal_sketch-map_Ex4.geotiff") by dragging and dropping them into the layer panel.


#### 3. Explore the data

1. __Orientate in the User Interface__

    If you are a beginner to QGIS get to know the basics of the QGIS User Interface [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#qgis-interface).

2. __Add a Basemap__

    For a better overview and orientation it is always helpful to add a basemap to your project and put your situation in a spatial context. Find in the `Browser` Panel `XYZ Tiles`, open the dropdown by clicking on it and select OpenStreetMap or another basemap.

    Click [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#standard-qgis-basemaps) for more information on basemaps and how toa dd them to your project.

3. __Understand the Layer Concept__

    By dragging and dropping your data into QGIS the data will be visualized in the map canvas and its description will be visible in the `Layers` Panel. You should now have 3 layers in your panel: your geojason output (vector), your geotiff (Raster) and the opentstreetmap basemap. In order to see all the information you have to bing theminto order. It is important to understand the [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html#layer-concept).


    ```{figure} /fig/en_SMT_ex4_fig1.PNG
    ---
    height: 500px
    name: T
    align: center
    ---
    Interface
    ```

4. __Explore the data__

    __Vector data__

    In order to explore your detected markings, right-click on your vector file and navigate to `Open Attribute Table` and click on it. The table has one entry (row) for each detected marking. In our example 6 markings where detecetd. The column "color" describes the color which has been detected for each marking and the column "name" contains the name of your uploaded Sketch Map. 

    ```{Note}
    When you upload several marked Sketch Maps simultaneously, you will get one vector output containing all the markings of all Sketch Maps. In this case the column "name" helps you to track on which map each marking was detected 
    ```

    ```{figure} /fig/en_SMT_ex4_Attrbute_Table.PNG
    ---
    height: 400px
    name: T
    align: center
    ---
    Attribute Tabek of Vector file output of Sketch Map Tool
    ```

    __GeoTIFF__

    The Raster file as result of the SKetch Map Tool is basically the foto you took of your Sketch Map but georeferenced. You see if the georeferencing is correct when it matches the base map. Furthermore your tif File is helpful to compare and review the marking detection (vector file). In this case your tiff is your "groudn truth" and you can check if the marking detection by the tool is true or if there are pieces missing or wongly detected. 

    Question:
    Do your different output match or do you find any errors?

    -> Yes, you are right. Unfortunatly, one marked polygon did not get detected. This can happen since marking are being detected by machien learning algorithms that can encounter problemas in soem situations. 


### 5. Correct or enhance your data



1. Digitalisation: Add a marking manually

So what can we do if a marking has not been detected? We can add missing markings manually by tracking the drawing on the getif file. This process is also called [digitalisation](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html?highlight=digitize#digitalisation). 

Right-click on your vector file and click on `Toggle Editing`. The `Digitizing Toolbox` in your menu bar on top of your QGIS will be activated:

```{figure} /fig/en_SMT_ex4_dig_toolbox.PNG
---
width: 100px
name: T
align: center
---
Digitzing Toolbox
```
Click on `Add Feature: Capture Polygon`![](/fig/mActionCapturePolygon.png). You will note that your mouse market now changed its symbol into a target. This means you can now start tracing the missing polygon my left-clicking. You finish your polygon by a right-click and you will be asked to enter the descriptions. Enter the information and click ok.

 ```{figure} /fig/en_SMT_ex4_dig_info.PNG
---
height:300px
name: T
align: center
---
Digitizing 
```
In the map canvas you can already see your handdrawn polygon. In order to save it you should now right-click on your vector layer and turn off the Editing mode by clickin on `Toggle Editing` -> `Save`. Check your result by looking at the Attribute Table again: You now have 7 features in your table.



 ```{figure} /fig/en_SMT_ex4_Attrbute_Table_new.PNG
---
height: 300px
name: T
align: center
---
Attribute Table with added polygon 
```

The whole process of Digitalisation is explained in detail [here](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html?highlight=digitize#digitalisation).



2. Add a property/column to the Attribute Table

Normally you know the meaning of the markings in your Sketch Map. We will now learn how to add them to your vector layer. In our example we assume we know that black and blue colors were used to mark past flood extents and red was used to mark critical infrastructures. We want to replicate this.
- Right-click on your vector layer and navigate to `Open Attribute Table` and click on it.
- In the upper left corner click on ![](/fig/mActionToggleEditing.png) to toggle editing mode
- click on ![](/fig/mActionNewAttribute.png) to add a new field to the data source
- As `Name` enter "Description", choose "Text (String)" `Type`, as `Length` enter "20" and click `OK`

```{figure} /fig/en_SMT_ex4_addfield.PNG
---
height: 400px
name: T
align: center
---
Attribute Add field
```

- by clicking on each field you can now enter the respective descriptions to the colors:

```{figure} /fig/en_SMT_ex4_addfield_description.PNG
 ---
height: 90px
name: T
align: center
---
Add field description
```

- Save by clicking on ![](/fig/mActionToggleEditing.png) once more -> `Save`


### 6. Visualize your data

Now we want to visualize our results and generate a printable map so the results can be shown to third parties in a clear and comprehensible manner. We can now delete the geotiff layer by right-click -> `Remove Layer` since we will be working with the vector marking detections.

1. __Customize Symbology__

We can customize the symbology of our vectory layer by right-clicking on it in the `Layers` Panel -> `Properties` -> `Symbology`.

First of all we want to assign different colors for different features:

In the topmost drop-down menu, choose `Categorized`. As Value choose "Description" and then click on the bottom left on `Classify`. We are now able to choose colors depending on the value in the column "Descriptioin". By doble-clicking on the colored box in your window next to your value and Legend descriptions the `Symbol Selector` will open in a new window where you can choose the color of your preference by clicking on the drop-down arrow next to "Color".
Right below you can also ajust the opcaty level of your feature.


```{figure} /fig/en_SMT_ex4_dig_categorize.PNG
---
height: 400px
name: T
align: center
---
Symbology 
```


In the `Symbol Selector`, you can also in the upper window click on `Simple line` and change the `Symbol Layer Type`. In tzis example we would like to symbolize the critical Infrastructure with red outlines, so we choose "Outline: Simple Line". Juts below we can adjust the color, stroke witdh stroke line type, etc. You can find more information about the visualization of vector data [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_visualisation_wiki.html#visualisation-of-vector-data).


 ```{figure} /fig/en_SMT_ex4_dig_Symbology.PNG
 ---
height: 400px
name: T
align: center
---
Symbol Selector 
```


2. __Make a printable Map__

FEHLT NOCH: UNTEN ANPASSEN

1. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "Ahrtal Flooding Sketch Map Tool". A new window will open with a blank canvas and a different set of tools. This is the print layout designer.

- Insert a new map by clicking on the ![New Map Icon](/fig/30.30.2_print_layout_insert_map_icon.png) ("Add Map") on the left toolbar, and drawing a rectangle on the print canvas. [Video](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#adding-a-new-map)
2. Move and position the map so that the entire country is visible at a reasonable scale. 
4. Let's add a title: 
    - Click on the ![Add text icon](/fig/30.30.2_print_layout_add_text.png) ("Add text")
    - Drag a rectangle on the canvas
    - In the items properties window on the right, you will find a text box with the text "Lorem ipsum". Here you can enter your map title (e.g.: Map of Ghana with roads and hospitals).
    - Adjust the font size: Click on the __Font__ dropdown menu and adjust the font size for a title (25p or more). Adjust the text box if necessary.
5. Let's add a legend:
    - Click on the ![Add legend icon](/fig/30.30.2_print_layout_add_legend.png) ("Add legend"). 
    - Navigate to the __Item Properties__ panel on the right. 
    - Scroll down a bit and check turn off `Auto Update` by unchecking the check box. Now you can freely edit every item on the legend
    - Adjust the legend by removing unecessary layers (which are not seen on the map) and rename the layer in the legend by clicking on ![Edit Icon](/fig/30.30.2_print_layout_legend_edit.png) below the legend entries.
6. Now, let's add a scale bar:
    - Click on the ![Add Scale bar icon](/fig/30.30.2_add_scale_bar.png) ("Add Scale bar")
    - Draw a rectangle on the map and position the scale bar on the edge of the map. You can adjust the scale bar units (meters, kilometers, ...), the fixed segment width (50 km, 75 km, 100 km, ...) and the number of segments (to the right).
7. Let's add North arrow:
    - Click on the ![Add North Arrow Icon](/fig/30.30.2_print_layout_add_orientation.png) ("Add North Arrow"). 
    - Drag a rectangle on the print layout. Adjust the size and location of the north arrow. You can also change the icon in the item properties.
8. Add a text box with additional information, sources, the author (you), and date of creation.
9. When you are happy with your print layout. You can export it as a PDF. You can save it in the project folder under "results".
10. Once you have exported the map. Look at the PDF and make sure it looks how you intended. Some things might look different in the PDF. If it does not look correct you may need to make some adjustments in the symbology.

The finished map could look something like this:

```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```




[Print Layout](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

In the [Map Making Wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_map_making_wiki.html#map-making-wiki) you can find all the information about making a printable map.

:::

## Exercise B: Basic visulization of Sketch Map Tool outputs in UMAP

:::{dropdown} Exercise B: Basic visulization of Sketch Map Tool outputs in UMAP
:open:

### 1. Background Information on UMAP

UMAP is an online platform that allows users to create custom maps with OpenStreetMap (OSM) as basemap layer. No installation nor registration is necesar. This enables users to quickly gain an intuitive overview of their data.
Useres can customize the appearance of the map and share it with others. It's particularly useful for collaborative mapping projects, quick visualization of geographic data, and creating custom maps tailored to specific needs.

| Feature| QGIS | UMAP |
| :-------------------- | :----------------- | :---------- |
| Type | Desktop Geographic Information System (GIS) software | Online mapping platform|
| Accessibility| Requires installation on a desktop computer | Accessible online via web browser |
| Purpose |Comprehensive GIS software for spatial data analysis | Interactive mapping tool for creating custom maps |
| Data Import | Supports various data formats (shapefiles, geodatabases, etc.) | Vector data only, user input via map canvas, some geo formats (geojson, .gpx, .kml, .osm) |
| Data Visualization and Analysis|Offers extensive visualization and analysis capabilities, Provides a wide range of geospatial analysis tools  | Focuses on creating interactive maps with custom elements; No analysis tools |
| Output | Printable map with all necesary map elements | URL so share map online |


```{Hint}
The Geojson output of the Sketch Map Tool cannot be opened and inspected with commonly available tools. If you use the Sketch Map Tool and do not have QGIS installed but quickly want to examine your result, UMAP is a simple and quick way to do so. But be aware as it is an online platform, a internet connection is required.
```

#### 2. Data Collection

Please download the prepared maps [here]().
Unzip the .zip folder in order to be able to acess the geotiff output.

Optional: You find the empty map [here](). Feel free to draw some additional flood maps by printing the template out and drawing on it or by using a simple graphics editor.


#### 3. Georeferencing and autoextraction with the Sketch Map tool

Upload the sketch maps back to the tool’s website. Head to [sketch-map-tool.heigit.org](https://sketch-map-tool.heigit.org/) and choose 'Digitize your Sketch maps' on the right. Upload all your sketches in .png or .jpg format. You can mark your sketches and simply drag and drop them into the window.

The sketch maps are now being processed and georeferenced with the annotations extracted and vectorized. Download the vectors. You may use the ones we have prepared [here]().

### 4. Load your data 

1. Open the Browser of your choice and navigate to the [UMAP Website](https://umap.openstreetmap.fr/en/) and click on the large green button `Create a Map`.

2. Right above your map canvas you can click in "Untiteld Map" in order to edit your map properties. Give your Map a title and a short description.

- maybe explain here what else can be done in properties-

    ```{figure} /fig/en_SMT_ex4_UMAP_Properties.PNG
    ---
    height: 400px
    name: T
    align: center
    ---
    Attribute Table with added polygon 
    ```

3. You can load your data into the map frame by clicking on the arrow button. The `Import data` window will open on the right hand side. CLick on `Select file` and navigate to your vector output from teh SKetch Map Tool ("Schuld_Ahr-tal_sketch-map_Ex4.geojson") and click on `Open`. UMAP will automatically detect that your vector is a geojason formnat. CLick on `Import` to load your data to your map canvas.

```{figure} /fig/en_SMT_ex4_UMAP_Data_Loaded.PNG
    ---
    height: 100px
    name: T
    align: center
    ---
    Attribute Table with added polygon 
    ```


4. Click in the upper right corner on `Save`. If you are not logged in you will be provided with an URL where you can access and your map any time lateron. Save it somewhere or send it to your email. 


```{Attention}
Without an account, the maps you create are stored temporarily in your browser's local storage or session storage. This means that if you clear your browser's cache or use a different device or browser, you may lose access to the maps you created.
```

```{Note}
Generally, you can create maps, edit them, and share them with others on uMap without signing up for an account. However, if you decide to use uMAP frequently it might be beneficial to create an account. Signing up ensures persistent access to your created maps alowwing to mnanaga dn edit maps over time. Also, some customization options or advanced features may only be available to registered users
```


### 5. Customize your map

Now that you imported your own data you are ready to customize your own map in ordet to show your results to others in a vivid manner.
In the toolbar on the right hand side you have various options to do so.

1. Change the background

Click on `Change tilelayers`![](/fig/en_SMT_ex4_UMAP_basemap.PNG) to choose another background map.

2. Explore and Manage Data Layers

Click on `Manage Layers`![](/fig/en_SMT_ex4_UMAP_layers.PNG) to open your layers panel. In this windows you will see all the layers in your project (in our case it is just one) and you are able to add additional information layers. The small symbols on the left hand side of you layer give you the option to hide, zoom to or delete your layer.


```{figure} /fig/en_SMT_ex4_UMAP_Managelayers.PNG
---
height: 200px
name: T
align: center
---
Manage Layers 
```

You can click on the table button ![](/fig/en_SMT_ex4_UMAP_Table.PNG) in order to view or edit properties in the attribute table of your layer. The table has one entry (row) for each detected marking. In our example 6 markings where detecetd. The column "color" describes the color which has been detected for each marking and the column "name" contains the name of your uploaded Sketch Map.

```{Note}
Sketch Map Vector Output always have this same attribute table structure.
```

```{figure} /fig/en_SMT_ex4_UMAP_AttributeTable.PNG
---
height: 200px
name: T
align: center
---
Attribute Table 
```

2. Custmize your visualization

Now we want to display the criticial infrastructure in red and the past flood extents in blue. For this we have to firstly create a group for each:

- Click on `Manage Layers`![](/fig/en_SMT_ex4_UMAP_layers.PNG) `Add Layers`
- We name the first new layer "Critical Infrastructure" and choose as `Type of layer` -> `Clustered` 
When you click on  `Close` and then on `Manage Layers`![](/fig/en_SMT_ex4_UMAP_layers.PNG) again, you will see you recently create layer "Critical Infrastructure"


```{figure} /fig/en_SMT_ex4_UMAP_Taddlayer.PNG
---
height: 400px
name: T
align: center
---
Add clustered layer
```

- repeat the process creating a clustered layer for "Past flood extent"

```{figure} /fig/en_SMT_ex4_UMAP_3Layers.PNG
---
height: 300px
name: T
align: center
---
Add clustered layer
```


- In the map canvas, you can now click on one of the polygons and toggle editing modus by clicking on the small pen button that appears.

```{figure} /fig/en_SMT_ex4_UMAP_Toggle_editing.PNG
---
height: 200px
name: T
align: center
---
Add clustered layer
```
- The `Feature properties` window will open on the right hand side. On the very top you can now choose the layer group you want to assign this feature to. ALso choose a meaningful name. For the flood polygons we can simply choose as name "Past flood extent" and for the several critical infrastructure polygons you can either choose "critical infrastructure" or "school"/"water treatment plant" as just an example. Click on `Close`. If you click on a flood extent polygon and toggle editing you assign it to you layer "Past flood extent" and if you click on a critical infrastrucutre polygon and toggle editing you assign it to you layer "Critical Infrastructure". Assign now all 6 polygons to the respective layer.


```{figure} /fig/en_SMT_ex4_UMAP_assign_layer.PNG
---
height: 200px
name: T
align: center
---
Assign features to layers
```

- Now click again on `Manage Layers`![](/fig/en_SMT_ex4_UMAP_layers.PNG) and `Edit`![](/fig/en_SMT_ex4_UMAP_Edit.PNG) one iof your new layers, e.g. "Past flood extent". Click on `Shape Properties` to change the color of the layer. You can explore other option you have for styling your features. You always finish by clicking on `Close` in the upper right corner.
- In `Interaction Options` the behavior of the labeling can be determined. For example you can choose `Popup` as `Popup shape` and set `Display label` either `on hover` in order to display the features descriptions only when you srcroll with the mouse over the respective feature on the map or on `always` in order to always see the respective description.


```{figure} /fig/en_SMT_ex4_UMAP_Shape_Properties.PNG
---
height: 500px
name: T
align: center
---
Shape properties
```

### 6. Save and publish your map

Your map could now look like this:

```{figure} /fig/en_SMT_ex4_UMAP_final.PNG
---
height: 100px
name: T
align: center
---
Shape properties
```

If you have displayed everything you planned and you have zoomed to the map extent of your choice you can click on `Save this center and zoom`![](/fig/en_SMT_ex4_UMAP_save.PNG) in order to save your map section. Then click on `Save`on the upper right.


In order to publish the map you can click on `Share and download`![](/fig/en_SMT_ex4_UMAP_share.PNG) on the menu bar on the left side.

```{figure} /fig/en_SMT_ex4_UMAP_sharelast.PNG
---
height: 100px
name: T
align: center
---
Shape properties
```

On the top under `Link to view the map` you receive a URL that you can share with other people so they can view the map you have created.
You also have the option to donwload your layers data or your full backup or to copy an iframe link in order to embed your elf-made map into wour own website.

```{Hint}
If you want to use your map as a simple figure to show offline, you can simply take a screenshot or use the Snipping Tool.
```

