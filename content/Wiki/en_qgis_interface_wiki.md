# QGIS Interface

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧
## Overview of QGIS Interface

![](/fig/en_QGIS_GUI.png)   

1. __Layers List / Browser Panel:__ The __layers list__ shows __all layers/files__ that are __loaded in the project__. You can show/hide layers and set other properties.

2. __Toolsbars:  __Toolbars__ are shortcuts__ to execute frequently used commands. For example, there are special toolbars for __vector and raster files__, but also general ones for saving your project, etc. The toolbar contains, among other things, a list of all the commands you can use. The toolbar also contains the __toolbox__, which is used later in many of the wiki videos.

![](/fig/Geschlossene_Toolbox_01.png)

3. __Map View:__ The __map view__ is the __central component__ of every GIS programme. This is where the __geodata__ are displayed. The map view has a projection which does not always have to correspond to the projection of the layers.

4.  __Status bar:__ In the __status bar__ you will find __central information about the current map view__. Here you can set the __projection of the map view and the scale__. You can read the coordinates of the mouse pointer and thus quickly find out the coordinates of points on the map. You can rotate your map view, e.g. if you want to create a map facing south.

5. __Side Toolbar__. You may see a __side toolbar__. This is another way to easily open vector and raster files in QGIS.

6. __Locator bar__. Here you can __search for tools and layers__. If you don't know where to find a tool, you can try here.

__Offical QGIS Documentation: [An Overview of the Interface](https://docs.qgis.org/3.4/de/docs/training_manual/introduction/overview.html)__

___

## Moving an orientation on the Map Canvas

### Moving the map view

To move on the map canvas with your mouse cursor you need to toggle the hand button. 

![](/fig/qgis_move_symbol.png)

You can also move on the map canvas with arrow keys on your keyboard.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

### Zooming in the map view

The easiest way to zoom on Map Canvas is by __scrolling__.

Or with the hotkeys `Ctrl`+`+` and `Ctrl`+`-`

![](/fig/qgis_zoom_symbol.png)

Another way is to use the zoom buttons in the toolbox panel.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

## Toolbox & Toolbars

Basically, all the functionality, tools and applications of QGIS are organised in the Toolbox. Some Tools have their own toolbars which you can add to your QGIS interface.

### Open Toolbox

To open the Toolbox in QGIS click on the gearwheel button. Or click on `Processing` -> `Toolbox`

![](/fig/Geschlossene_Toolbox_01.png)

You can use the search bar to find specific tools.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

### Show and hide displays and toolbars

There are toolbars and panels for many different tasks. To avoid an overcrowded interface it is smart to only activate specific toolbars or panels only when you really need them.

To add or remove toolbars from your interface click on `View` -> `Toolbars` -> Check or uncheck the toolboxes you want to add or remove

To add or remove  panels from your interface click on `View` -> `TPanels` -> Check or uncheck the panels you want to add or remove

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video> 

### Move and arrange toolbars

At each toolbar there is a field of two dotted lines. If you move the mouse pointer over it until an arrow cross appears and then hold down the left mouse button, you can move the toolbar. This allows an individualised arrangement of your own tools. By compressing all toolbars into a few lines, the map view window can also be enlarged.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

## Save & Open QGIS Projects

To save progress or to open an existing project in QGIS is very similar to programs like MS Word. However, there is one __BIG__ difference. 
In QGIS the geodata you work with is __not__ saved in your QGIS projectfile. Instead, the project file only contains the file paths where the geodata were located at the time the project was last saved on the PC. If the location of this geodata is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.

### Open Projects

To open an existing QGIS project click on `Project` -> `Open…` -> Navigate to your project and open it.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

### Save Projects

* __When you save the first time__: To save the QGIS project you are working on click on `Project` -> `Save as…`-> Navigate to the folder where you want to save the project -> Give the project a name -> `Save`
* __When you save progress__: To save progress in a project that was already saved somewhere on your computer there are two good options:
    * Use the hotkey `Ctrl`+ `s` on your keyboard. 
    * Click on `Project` -> `Save`. 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>