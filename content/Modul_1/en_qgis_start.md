# Getting started with QGIS

## Intro QGIS concept

### What is QGIS?

QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, making QGIS a free application. 
You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 and is a project of volunteers. And it is __constantly changing__.

## Introducing QGIS

- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 

- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blog and subreddit.

### QGIS Interface

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

### Further Functionalities

#### Moving the map view

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

![](/fig/qgis_move_symbol.png)
* You can also move with the _arrow keys_

#### Zooming in the map view

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>

![](/fig/qgis_zoom_symbol.png)
* You can also zoom by scrolling
* Or with Ctrl+ or Ctrl-

#### Show properties of objects

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_identify.mp4"></video>

* Make sure to select the layer you want identify features in 

#### Set the projection of the map view (project CRS)

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_map_projection.mp4"></video>

* Geodata concepts are explained in detail in [module 2](../Modul_2/en_qgis_geodata_concept.md)

#### Open Project

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

#### Save Project

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>

*  The layer data used in the project are not saved in the project file. Instead, the project file only contains the file paths where the layer data were located at the time the project was last saved on the PC. If the location of this layer data is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.
Good data organisation with a fixed and well thought-out folder structure prevents such problems.

#### Show and hide displays

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video> 

#### Move and arrange toolbars

*   At each toolbar there is a field of two dotted lines. If you move the mouse pointer over it until an arrow cross appears and then hold down the left mouse button, you can move the toolbar. This allows an individualised arrangement of your own tools. By compressing all toolbars into a few lines, the map view window can also be enlarged.

<tagName>  <tagName>

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

See also:
 [corresponding page in the Wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)

