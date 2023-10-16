# Getting started with QGIS

## Intro QGIS concept

### What is QGIS?

QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, making QGIS a free application. 
You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 and is a project of volunteers. And it is __constantly changing__.

### 32 Bit or 64 Bit?

For Windows operating systems, there is always a 32-bit version and a 64-bit version of each QGIS version available for download. __Which version to install depends on your computer and operating system__. If it is not clear how many bits your operating system has, you can easily find out: Left-click on the Windows icon at the bottom left of the screen (alternatively, open the Windows search function). Type "System" on the keyboard, click on the entry "System" in the search results. Under the item "System type" you can read the bit number.

## Introducing QGIS

- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 

- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blog and subreddit.

### Overview of QGIS Interface

![QGIS_User_Interface](/fig/en_QGIS_GUI.png)
User interface 

1. __Layers List / Browser Panel:__ The __layers list__ shows __all layers/files__ that are __loaded in the project__. You can show/hide layers and set other properties.

2. __Toolsbars: __ __Toolbars__ are shortcuts__ to execute frequently used commands. For example, there are special toolbars for __vector and raster files__, but also general ones for saving your project, etc. The toolbar contains, among other things, a list of all the commands you can use. The toolbar also contains the __toolbox__, which is used later in many of the wiki videos.

 <tagName>  <tagName>

![Alt text](/fig/en_Interface_02.png)
 <br>
<tagName>  <tagName>
Toolbox

3. __Map View:__ The __map view__ is the __central component__ of every GIS programme. This is where the __geodata__ are displayed. The map view has a projection which does not always have to correspond to the projection of the layers.

4.  __Status bar:__ In the __status bar__ you will find __central information about the current map view__. Here you can set the __projection of the map view and the scale__. You can read the coordinates of the mouse pointer and thus quickly find out the coordinates of points on the map. You can rotate your map view, e.g. if you want to create a map facing south.

5. __Side Toolbar__. You may see a __side toolbar__. This is another way to easily open vector and raster files in QGIS.

6. __Locator bar__. Here you can __search for tools and layers__. If you don't know where to find a tool, you can try here.

```{Tip}
Exercise: Create a new QGIS project  
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


### Try out Further Functionalities of QGIS 

Have a look at the tabbed video examples below:

````{tab-set}
```{tab-item} Move and Zoom
Move and Zoom

::::{grid}
:gutter: 2

:::{grid-item-card} Move the map view
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

![](/fig/qgis_move_symbol.png)
* You can also move with the arrow keys

:::
:::{grid-item-card} Zooming in the map view
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>

![](/fig/qgis_zoom_symbol.png)
* You can also zoom by scrolling
* Or with Ctrl+ or Ctrl-

:::

::::

```

```{tab-item} Properties and Toolbars
Properties and Toolbars

::::{grid}
:gutter: 2

:::{grid-item-card} Show properties of objects
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_identify.mp4"></video>

* Make sure to select the layer you want identify features in 

:::
:::{grid-item-card} Open Toolbar
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

![](/fig/Geschlossene_Toolbox_01.png)
* You can also zoom by scrolling
* Or with Ctrl+ or Ctrl- 

:::

::::

```

```{tab-item} Save and Open Project
Save and Open Project

::::{grid}
:gutter: 2

:::{grid-item-card} Save project
<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/8e2bb629d9c3189f8f635a4cf1381d2c/qgis_save_project.mp4"></video>

* The layer data used in the project are not saved in the project file

:::
:::{grid-item-card} Open project
<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/1655b97b741749bfa46c6c08ee3d0be6/qgis_open_project.mp4"></video>

:::

::::

```

```{tab-item} Configuration
Configuration

::::{grid}
:gutter: 2

:::{grid-item-card} Save project
<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/8e2bb629d9c3189f8f635a4cf1381d2c/qgis_save_project.mp4"></video>

* The layer data used in the project are not saved in the project file

:::
:::{grid-item-card} Open project
<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/1655b97b741749bfa46c6c08ee3d0be6/qgis_open_project.mp4"></video>

:::

::::

```

```{tab-item} Projection of Map View
Projection of Map View

::::{grid}
:gutter: 2

:::{grid-item-card} Projection of map view (project CRS)
<video width="100%" controls src="https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/325cb2d70b0154c1bd5f38a899cd2b40/qgis_map_projection.mp4"></video> 

:::

::::

```
````

