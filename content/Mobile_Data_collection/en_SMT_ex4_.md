# Sketch Map Tool Exercise 4 - Basic Visualization of the results
🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧





## Characteristics of the exercise 
#### Aim of this exercise:
Learn how you can visualize your Sketch Map Tool Outputs in eather [QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_installation_wiki.html#qgis-installation) or [UMAP](https://umap.openstreetmap.fr/en/).

#### Phase of participatory /community mapping 
analysing participatory mapping
#### Focus group (GIS-Knowlege Level)

- Exercise builds on prior-knowledge of Sketch Map Tool. Make sure [Execise 1](https://giscience.github.io/gis-training-resource-center/content/Mobile_Data_collection/en_SMT_ex1_.html#sketch-map-tool-exercise-1-workflow-exercise) has been done before or knowlege on the background on Sketch Map Tool is there.
- GIS Beginners-level: no specific knowledge about QGIS /Umap required

#### Type of trainings exercise:
This exercise can be used in online and presence training and is focused on an hands-on experience with the basic of QGIS or UMAP.
#### Estimated time demand for the exercise.
Exercise A: with absolute beginners 2 hours
Exewrcise B: 30 min

```{Tip}
Decide together with the responsible working group which GIS system is prefered and decide on one. There is no neccesity to learn/use both ways. Generally QGIS will give you more opportunities for visualization and analysis of the results, but if a simple and quick visualization without installation of software packages is desired, UMAP might be an easy solution.
```

## Instructions for the trainers 

:::{dropdown} Trainers Corner
### Preparation and material 
- Online access and devices (PC)
- QGIS installed on the computer
- Take a look and make yourself familiar on the provided material for the exercise and the Sketch Map Tool in general. 

```
Alternatives  
- If you like to skip parts of the workflow, make sure you have alternative material (like preprinted, or already marked Sketch maps) prepared.
- If you like to adapt this exercise to your specific use case, create your own case-description. 
```



### Available Material: needs to be linked directly 
•	Introduction Slides about the Sketch Map Tool available
•	X EVCA-case studies as examples available 
•	Alternative files based on OSM- and satellite-based Sketch Maps from 5 regions.
o	Just the created maps for (pre-printing)
o	Pre-marked and photographed maps 
o	Geodata of the results and some pictures 


### During the exercise:  
#### Introduction: 
- Introduce the idea, the aim and the general workflow of the Skecht Map Tool beforehand 
- Provide access to the needed material 
- check-in if there are questions or problems.

#### Wrap up: 
- Take some time at the end to wrap up and that several people present their result map
- Discuss Benefits of showing results as a map
- Time to for Open questions.

## Step-by step introduction for participants 

link where you can download this part as a short pdf to hand it to participants

If you expieriences any problems during your use of the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) please take a look at the [Help page](https://sketch-map-tool.heigit.org/help).
::::





## Exercise A: Basic visulaization of Sketch Map Tool outputs in QGIS


critical infrastrucutre and historical flood extent





Exercise Input: jpeg um noch kurz den Prozess im SMT zu wiederholen oder direkt geojson zur Verfügung stellen?

To do: Kontext und Gebiet  auswählen

Schritte:

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

1. Orientate in the User Interface

If you are a beginner to QGIS get to know the basics of the QGIS User Interface [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#qgis-interface).

2. Add a Basemap

For a better overview and orientation it is always helpful to add a basemap to your project and put your situation in a spatial context. Find in the `Browser` Panel `XYZ Tiles`, open the dropdown by clicking on it and select OpenStreetMap or another basemap.

Click [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#standard-qgis-basemaps) for more information on basemaps and how toa dd them to your project.

3. Understand the Layer Concept

By dragging and dropping your data into QGIS the data will be visualized in the map canvas and its description will be visible in the `Layers` Panel. You should now have 3 layers in your panel: your geojason output (vector), your geotiff (Raster) and the opentstreetmap basemap. In order to see all the information you have to bing theminto order. It is important to understand the [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html#layer-concept).


```{figure} /fig/en_SMT_ex4_fig1.PNG
---
height: 50px
name: T
align: center
---
Interface
```

4. Explore the data


Vector data

In order to explore your detected markings, right-click on your vector file and navigate to `Open Attribute Table` and click on it. The table has one entry (row) for each detected marking. In our example 6 markings where detecetd. The column "color" describes the color which has been detected for each marking and the column "name" contains the name of your uploaded Sketch Map. 

```{Note}
When you upload several marked Sketch Maps simultaneously, you will get one vector output containing all the markings of all Sketch Maps. In this case the column "name" helps you to track on which map each marking was detected 
```

```{figure} /fig/en_SMT_ex4_Attrbute_Table.PNG
---
height: 50px
name: T
align: center
---
Attribute Tabek of Vector file output of Sketch Map Tool
```


GeoTIFF

The Raster file as result of the SKetch Map Tool is basically the foto you took of your Sketch Map but georeferenced. You see if the georeferencing is correct when it matches the base map. Furthermore your tif File is helpful to compare and review the marking detection (vector file). In this case your tiff is your "groudn truth" and you can check if the marking detection by the tool is true or if there are pieces missing or wongly detected. 

Question:
Do your different output match or do you find any errors?

-> Yes, you are right. Unfortunatly, one marked polygon did not get detected. This can happen since marking are being detected by machien learning algorithms that can encounter problemas in soem situations. 


### 5. Correct or enhance your data

So what can we do if a marking has not been detected? We can add missing markings manually by tracking the drawing on the getif file. This process is also called [digitalisation](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html?highlight=digitize#digitalisation). 

1. Right-click on your vector file and click on `Toggle Editing`. The `Digitizing Toolbox` in your menu bar on top of your QGIS will be activated:

```{figure} /fig/en_SMT_ex4_dig_toolbox.PNG
---
height: 50px
name: T
align: center
---
Digitzing Toolbox
```
Click on `Add Feature: Capture Polygon`![](/fig/mActionCapturePolygon.png). You will note that your mouse market now changed its symbol into a target. This means you can now start tracing the missing polygon my left-clicking. You finish your polygon by a right-click and you will be asked to enter the descriptions. Enter the information and click ok.

```{figure} /fig/en_SMT_ex4_dig_info.PNG
---
height: 50px
name: T
align: center
---
Digitzing 
```
In the map canvas you can already see your handdrawn polygon. In order to save it you should now right-click on your vector layer and turn off the Editing mode by clickin on `Toggle Editing` -> `Save`. Check your result by looking at the Attribute Table again: You now have 7 features in your table.



```{figure} /fig/en_SMT_ex4_Attrbute_Table_new.PNG
---
height: 50px
name: T
align: center
---
Attribute Table with added polygon 
```


The whole process of Digitalisation is explained in detail [here](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html?highlight=digitize#digitalisation).


### 6. Visualize your data

- Customize colors (Categorize!), opacity, ...
- Lean how to makew a printable map, map layout, legend, north arrow, etc.



## Exercise B: Basic visulaization of Sketch MNap Tool outputs in UMAP

#### Background Information on UMAP

UMAP (Unified Map Platform) is an online platform that allows users to create custom maps using OpenStreetMap (OSM) data. No installation or registration is necesary which enables users to quickly gain an intuitive overview of their data.
Useres can customize the appearance of the map and share it with others. It's particularly useful for collaborative mapping projects, visualizing geographic data, and creating custom maps tailored to specific needs

| Feature| QGIS | UMAP |
| :-------------------- | :----------------- | :---------- |
| Type | Desktop Geographic Information System (GIS) software | Online mapping platform|
| Accessibility| Requires installation on a desktop computer | Accessible online via web browser |
| Purpose |Comprehensive GIS software for spatial data analysis | Interactive mapping tool for creating custom maps |
| Data Import | Supports various data formats (shapefiles, geodatabases, etc.) | Primarily utilizes OpenStreetMap (OSM) data |
| Data Visualization and Analysis|Offers extensive visualization and analysis capabilities, Provides a wide range of geospatial analysis tools  | Focuses on creating interactive maps with custom elements, Limited analysis tools |
| Output | Printable map with all necesary map elements | URL so share map online |




```{Hint}
The Geojson output of the Sketch Map Tool cannot be opened and inspected with commonly available tools. If you use the Sketch Map Tool and do not have QGIS installed and quickly want to examine your result, UMAP is a simple and quick way to do so.
```



Hintergrundkarte kann ausgewählt werden

Karte einen Namen geben

Digitalization:

you can draw polygon, give it name and description