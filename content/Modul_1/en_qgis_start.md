# Getting started with QGIS

## Intro QGIS concept

### What is QGIS?

QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, making QGIS a free application. 
You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 and is a project of volunteers. And it is __constantly changing__.

### Introducing QGIS

- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 

- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blog and subreddit.

 <tagName>  <tagName>

![QGIS_User_Interface](/fig/en_QGIS_User_Interface.png)
User interface

```{Tip}
Exercise 1: Create a new QGIS project  
```
  - In your “GIS_Training” folder, create a __subfolder__ called __“Projects”__
  - Open __QGIS__
  - Click on __New Empty Project__
  - In the top-left corner, click on __Project__
  - Click on __Save as__, browse to your Projects folder and save the project as “Session1”
  - Open your “Projects” folder and check the __.qgzfile__ that you just created

   <tagName>  <tagName>

![Project template](/fig/en_project_template_BRC.png)
Project template

```{Tip}
Exercise 2: Add a vector file
```

- In the menu, click on __Layer "Add Layer" Add Vector Layer__
- __Browse__ to your Shapefiles folder and select the file you downloaded earlier
- Click on __Add__, select the first 3 layers from the list that will open and click on __Add Layers__
- Close the window and explore the layers in the __layer pane__ (bottom-left)

 <tagName>  <tagName>

![Add a vector file](/fig/en_Add_a_vector_file_a.png)
Add a vector file 

```{Tip}
Exercise 3: Add basemaps
```
- In the browser pane scroll to __XYZ Tiles__
- Click on __OpenStreetMap__ and drag it to the layers pane
- Now in the browser pane right-click on XYZ Tiles and select __“New Connection”__
- In __Name__ type “Google Satellite”
- In __url__ copy and paste the following: [https://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}](https://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}) (original link is broken)
- Click __Ok__ then drag the newly created layer from XYZ Tiles to the layers pane
- Repeat for __Google Terrain__, you will find the url at [this link](https://socalgis.org/2019/11/06/add-google-maps-to-qgis-3/)

 <tagName>  <tagName>

![Add_basemaps](/fig/en_Add_basemaps.png) 

Add basemaps


## Installation QGIS

QGIS is open source and therefore freely available to everyone at no cost. You can install QGIS for Windows, Mac and Linux computers. __The actual Long Term Release is QGIS 3.28.11 Firenze__. Generally we recommend to use the __latest Long Term Release__, because it is the most stable and contains the fewest bugs. You can __download__ the latest version here: [https://www.qgis.org/en/site/forusers/download.html](https://www.qgis.org/en/site/forusers/download.html)

For our introduction, the standalone installers from OSGeo4W packages are sufficient for Windows.

### 32 Bit or 64 Bit?

For Windows operating systems, there is always a 32-bit version and a 64-bit version of each QGIS version available for download. __Which version to install depends on your computer and operating system__. If it is not clear how many bits your operating system has, you can easily find out: Left-click on the Windows icon at the bottom left of the screen (alternatively, open the Windows search function). Type "System" on the keyboard, click on the entry "System" in the search results. Under the item "System type" you can read the bit number.

```{Tip}
Exercise: Get to know QGIS and familiarize yourself with geodata
```

 [https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_0](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_0)
 
Data:

-  __Download the data__: [https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/blob/main/Exercise_0/Ex0_data.zip](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/blob/main/Exercise_0/Ex0_data.zip)
 - __Save__ it on your PC. Create a __local folder__ and __save the above data there__ (.zip folders must be unzipped beforehand).

 - [https://hub.arcgis.com/datasets/2b93b06dc0dc4e809d3c8db5cb96ba69_0/explore](World Countries -Generalized) Polygon/Shapefile
 - [https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ngdc.mgg.hazards:G012153](Significant Earthquake Database) CSV
 - [https://datasets.wri.org/dataset/globalpowerplantdatabase](Global Power Plant Database) Points/GeoPackage

Steps: 

- Open QGIS and create a __new project__
- Open the __above files__ in QGIS 
- Load the vector layers via __Layer -> Data Source Manager -> Vector__ into your programme 
-  Load the __test layer file__ (Significant earthquake Data) via  __Layer -> Data Source Manager -> Add Delimited text Layer__ in your programme. While loading the text layer, make sure to open the drop-down menu __“File Format”__ and check the box __“costume delimiter”__ and __“Tab”__ Furthermore, select the coordinate reference system __(CRS) "EPSG:4326-WGS 84"__
- __Arrange the three layers__ in a practical order
- __Interact with the map and explore the data sets__. Use the zoom tool and move the map
- __Save__ your project

This (or similar) is what it looks like in the end:

 <tagName>  <tagName>

![Excercise0_a](/fig/en_Excercise_0_a.png)

![Excercise0_b](/fig/en_Excercise_0_b.png)

See also:

Share link:

[PDF documentation](/QGIS-Training/QGIS-Dokumente/2022_Tutoriel_QGIS_CartONG_EN_p06.pdf) Presentation of the interface,cartONG QGIS-Tutorial, p. 6


<a href=/QGIS-Training/QGIS-Dokumente/2022_Tutoriel_QGIS_CartONG_EN_p06.pdf>
Presentation of the interface, cartONG QGIS-Tutorial, p. 6</a>
 

## QGIS interface description

```{Tip}
Exercise: Take the first steps
```
 [https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_1](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_1)

-  Understand the __user interface__ and get to know the __layer concept__

-  __Display vector data__ in QGIS and __view the attribute data__

- __Reproject vector data__ (i.e. change the projection of the data)

Data:

- __Download the data__ and __save it on your PC__. 

- __Create a local folder__ and save the above data there (.zip folders must be unzipped beforehand)

 - Sierra Leone Border (Polygon/Lines) GeoPacked
    - Sierra Leone national boders (Polygon/lines)
    - Sierra Leone provinces (Lines)
  - Sierra Leone health (Points)
  - Sierra Leone airports (CSV)

Steps:

- __Open QGIS__ and familiarize yourself with the user interface
- __Open the above files__ in QGIS. Load the __vector layers__ into your programme Load the __CSV file__ via __"Add delimited text"__
- __Interact with the map and explore the data sets__. Use the zoom tool and move the map. Notice the status bar at the bottom of the screen and how it changes.
- Familiarize yourself with the __layer window (Layer List)__. Alternately show and hide different layers and move the layers in the hierarchy. __Rename the data layer__ in a meaningful way. Note that the latter has no effect on the data sources (file names, storage location).
- View the __attribute data__ of the layers. For this purpose look at the attribute table
- Changes the projection in the map view to __WGS 84 / Pseudo-Mercator - EPSG:3857__. Note that this does not change the projection (the coordinates) of the files, but only affects the projection of the map view.  Check this in the properties of the point layer. __Which projection is indicated there?__

 ``` {Tip}
 You can use the search bar on the top
 ```
- Now __save the health layer__ in the projection __WGS 84 / Pseudo-Mercator - EPSG:3857__. This changes the projection of the file. Check this in the properties of the newly created layer.
- __Save your project__
- __Optional:__ You can add the __OpenStreetMap base map__ via the browser windos -> XYZ Tiles. Note that online base maps can lead to problems with the projection of the different layers. Make sure to remove the base map bevor saving the project.

This (or similar) is what it looks like in the end:

 <tagName>  <tagName>

![Excercise1_a](/fig/en_Excercise_1_a.png)

![Excercise1_b](/fig/en_Excercise_1_b.png)

### Interface:

#### Overview of QGIS Interface

![Alt text](/fig/en_Interface_01.png)

1. __Layers List / Browser Panel:__ The __layers list__ shows __all layers/files__ that are __loaded in the project__. You can show/hide layers and set other properties.

2. __Toolsbars: __ __Toolbars__ are shortcuts__ to execute frequently used commands. For example, there are special toolbars for __vector and raster files__, but also general ones for saving your project, etc. The toolbar contains, among other things, a list of all the commands you can use. The toolbar also contains the __toolbox__, which is used later in many of the wiki videos.

 <tagName>  <tagName>

![Alt text](/fig/en_Interface_02.png)

3. __Map View:__ The __map view__ is the __central component__ of every GIS programme. This is where the __geodata__ are displayed. The map view has a projection which does not always have to correspond to the projection of the layers.

4.  __Status bar:__ In the __status bar__ you will find __central information about the current map view__. Here you can set the __projection of the map view and the scale__. You can read the coordinates of the mouse pointer and thus quickly find out the coordinates of points on the map. You can rotate your map view, e.g. if you want to create a map facing south.

5. __Side Toolbar__. You may see a __side toolbar__. This is another way to easily open vector and raster files in QGIS.

6. __Locator bar__. Here you can __search for tools and layers__. If you don't know where to find a tool, you can try here.

--------------------
### Move and Zoom

::::{grid}
:gutter:2

:::{grid-item-card} Move the map view

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

![](/fig/qgis_move_symbol.png)
* You can also move with the arrow keys

::: :::{grid-item-card} Zooming in the map view

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>

![](/fig/qgis_zoom_symbol.png)
* You can also zoom by scrolling
* Or with Ctrl+ or Ctrl-

:::

::::

### Properties and Toolbars

::::{grid}
:gutter:2

:::{grid-item-card} Show properties of objects

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_identify.mp4"></video>

* Make sure to select the layer you want identify features in 

::: :::{grid-item-card} Open Toolbar

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

![](/fig/Geschlossene_Toolbox_01.png)
* You can also zoom by scrolling
* Or with Ctrl+ or Ctrl- 

:::

::::

### Save and Open Project

::::{grid}
:gutter:2

:::{grid-item-card} Save project

<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/8e2bb629d9c3189f8f635a4cf1381d2c/qgis_save_project.mp4"></video>

* The layer data used in the project is not saved in the project file

::: :::{grid-item-card} Open project

<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/1655b97b741749bfa46c6c08ee3d0be6/qgis_open_project.mp4"></video>

:::

::::


 ### Configuration

::::{grid}
:gutter:2

:::{grid-item-card} Show and hide displays

<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/b9ccebc4bd584fdbc5092b4804d8a742/Anzeigen_einblenden_ausblenden.mp4"></video>

::: :::{grid-item-card} Move and arrange toolbars

 <video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/07bbf031499eb8da30daaa3bebd24769/qgis_arrange_toolbars.mp4"></video> 

:::

::::

  
### Projection of map view (project CRS)

::::{grid}
:gutter:2

:::{grid-item-card} Projection of map view (project CRS)

<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/325cb2d70b0154c1bd5f38a899cd2b40/qgis_map_projection.mp4"></video> 

:::

::::


See also: 

Share link:

[PDF documentation](/QGIS-Training/QGIS-Dokumente/2022_Tutoriel_QGIS_CartONG_EN_p07-09.pdf) Structuring a QGIS Project, cartONG QGIS-Tutorial, p. 7 - 9 

<a href=/QGIS-Training/QGIS-Dokumente/2022_Tutoriel_QGIS_CartONG_EN_p07-09.pdf>
Structuring a QGIS Project, cartONG QGIS-Tutorial, p. 7 - 9 </a>