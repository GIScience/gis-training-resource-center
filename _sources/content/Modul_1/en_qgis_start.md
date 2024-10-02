# Getting started with QGIS

__🔙[Back to Homepage](/content/intro.md)__

<!---**Competences:**

- What is QGIS?
- QGIS and basic functionality
-->

## Introducing QGIS

- QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, 
making QGIS a free application. The entire source code can be viewed and downloaded on https://github.com/qgis/QGIS.
- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons 
you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 
- You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 
and is a project of volunteers. And it is __constantly changing__.
- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blogs, or sub-reddits. The official QGIS community can be found [here](https://qgis.org/en/site/forusers/support.html#support). Additionally, a list of helpful websites can be found on the [wiki here](content/Wiki/en_qgis_common_errors_and_Issues.md).


```{note}
QGIS is constantly changing, with new features being added. Because of this, the newer versions can have changes or even bugs (such as crashes). However, there is always a stable version available, which is supported for longer.
```

```{note}
Keep in mind that as QGIS gets developed further, the interface and functions of QGIS are subject to changes. The material written for this platform is referring to QGIS Version 3.36. If the training material is no longer up to date, take a look at the [QGIS Documentation](https://docs.qgis.org/3.34/en/docs/index.html).

```


## Working with QGIS


In QGIS, you create projects where you visualise and manipulate geodata. There are three main workflows you will use: __Data collection and creation, data processing, and data visualisation__. Geodata is loaded into QGIS projects which will represented as layers on a map canvas.

```{hint} 
There is a lot of complex math involved in the GIS, but QGIS takes care of it on it's own and you don't need to have a deep understanding of maths and algorithms to use QGIS. __As long as you can use Excel and Powerpoint, you shouldn't have trouble learning how to use QGIS__. 
```

::::{tab-set}

:::{tab-item} Data Collection and Creation

QGIS offer tools to create your own geodata. For example, with the digitizing tools, you can create points, polygons, and lines with information which can represent spatial information. Furthermore, georeferencing let's you add geographic information to various types of data, such as satellite imagery or hand-drawn maps. You will learn how to create geodata and how to georeference data in __[module 2](/content/Modul_2/en_module_2_overview.md)__. 

Sometimes working with GIS requires you to go and collect the data in the field. In this case, you can use [web and mobile apps](content\Wiki\en_web_and_mobile_apps_wiki.md). 



:::

:::{tab-item} Data Processing

QGIS offers a wide range of algorithms to process geodata. In the following modules, you will get to know a number of 
algorithms that are especially useful for GIS in humanitarian work. 
You will learn more about data processing and manipulation in [module 2](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_module_2_overview.html) onwards. 

<!--ADD: more examples-->
<!--ADD: add link to basic data processing and visualisation chapters-->


:::

:::{tab-item} Visualisation

QGIS let's you visualise geodata and create maps to communicate information. It does so by assigning symbols and colours 
to different elements in your geodata. Assigning a symbology to the geodata is one of the main skills you will develop 
as a GIS-user and a good visualisation of data is immensely useful when communicating insights. You will learn how to 
assign symbols in [Module 4: Visualisation of Geodata and Map Making](/content/Modul_4/en_qgis_map_design_I.md)

<!--ADD: Insert example for visualisation-->
<!--FIXME: Insert link to overview page on module 3-->


:::
::::




:::{dropdown} A note on plugins


In addition to the algorithms included in the standard installation, QGIS offers plugins which add additional 
functionality to the QGIS application. These plugins are developed by independent organizations or the QGIS-community. 
For example, plugins let you connect to online services such as OpenStreetMap, or add more algorithms to process your 
data. These can be very useful for certain use cases. There are also plugins specifically designed for humanitarian 
work. You will learn more about plugins in the following modules. If you want to know how to install them, look into the [wiki](/content/Wiki/en_qgis_plugins_wiki.md). 


:::

## Opening a new project in QGIS

Open QGIS like any other program on your computer. 
The start screen of QGIS usually shows you the projects you worked on recently and the option to create a new project.

There are __two__ options to create a new project:

1. On the start screen click on `Project Template`


```{figure} /fig/en_project_template_BRC.png
---
height: 400
name: Project Template
align: center
---
```

2. In the upper left corner click on `Project` -> ` New Project `

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>

```{tip} 
A QGIS project file has the format ending `.qgz`
```


## Overview of QGIS Interface

The interface of QGIS is at first glance quite complex. However, once you know all the components you will be able to orientate yourself quickly. Here you can find a description of all components of the interface.

```{tip} When you hover with your mouse cursor over icons, text will appear which explains the function of the button.
```

```{figure} /fig/en_QGIS_GUI.png
---
width: 800px
name: 
align: center
name: QGIS User Interface
---
QGIS User Interface. Source: CartONG
```

1. __Layers List / Browser Panel:__ The __layers list__ shows __all layers/files__ that are __loaded in the project__. You can show/hide layers and set other properties.

2. __Toolsbars:  __Toolbars__ are shortcuts__ to execute frequently used commands. For example, there are special toolbars for __vector and raster files__, but also general ones for saving your project, etc. The toolbar contains, among other things, a list of all the commands you can use. The toolbar also contains the __toolbox__, which is used later in many of the wiki videos.

```{figure} /fig/en_Interface_02.png
---
height: 50px
name: Toolbox button
align: center
---
```
3. __Map View:__ The __map view__ is the __central component__ of every GIS programme. This is where the __geodata__ are displayed. The map view has a projection which does not always have to correspond to the projection of the layers.

4.  __Status bar:__ In the __status bar__ you will find __central information about the current map view__. Here you can set the __projection of the map view and the scale__. You can read the coordinates of the mouse pointer and thus quickly find out the coordinates of points on the map. You can rotate your map view, e.g. if you want to create a map facing south.

5. __Side Toolbar__. You may see a __side toolbar__. This is another way to easily open vector and raster files in QGIS.

6. __Locator bar__. Here you can __search for tools and layers__. If you don't know where to find a tool, you can try here.

 :::{dropdown} Exercise: Create a new QGIS project
 1. In your “GIS_Training” folder, create a __subfolder__ called "Projects"
 2.  Open __QGIS__
 3. Click on `Project` -> ` New Project `
 4. In the top-left corner, click on `Project` -> `Save as`, browse to your Projects folder and save the project as "Session1”
 5. Click on __Save as__, browse to your Projects folder and save the project as “Session1”
 6. Open your “Projects” folder and check the __.qgz file__ that you just created
:::

```{attention}
If you see a `*` in the title bar, to the left of the name of your project, this means that the project has changes which are __unsaved__. Since QGIS can crash from time to time, make sure to save your project periodically to avoid losing progress.
```

## Buttons and Shortcuts

In QGIS, __mouse control__ allows users to interact with the map canvas, enabling functions such as panning, zooming, and selecting features.

__Hotkeys__ in the QGIS interface provide convenient shortcuts for various commands, enhancing efficiency and speeding up workflow. You can find all hotkeys below.

```{dropdown} Navigation in the map view

| Name                      | Menu option                    | Shortcut                        | Description                                 |
|---------------------------|--------------------------------|---------------------------------|---------------------------------------------|
| Map pan                   | ![](/fig/qgis_pan_map.png)     | `Space`, `Page Up`, `Page Down` or the `Arrow Keys` | Move the map                                 |
| Pan map to selection      | ![](/fig/qgis_pan_map_selection.png) |                                  | Pans the map to the selected element        |
| Zoom in                   | ![](/fig/qgis_zoom_in.png)     | `Ctrl` + `Alt` + `+` or mouse wheel   | Zoom into the map                            |
| Zoom out                  | ![](/fig/qgis_zoom_out.png)    | `Ctrl` + `Alt`+ `-` or mouse wheel   | Zoom out of the map                          |
| Zoom full                 | ![](/fig/qgis_zoom_full.png)   | `Ctrl` + `Shift` + `F`                  | Zoom to the selected element                |
| Zoom to selection         | ![](/fig/qgis_zoom_to_selection.png) | `Ctrl` + `J`                       | Zoom to the selected element                |
| Zoom to layer             | ![](/fig/qgis_zoom_to_layer.png) |                                  | Zoom to the selected layer                   |
| Zoom to native resolution | ![](/fig/qgis_zoom_native_resolution.png) |                             | Zoom to the native resolution (100%)         |
| Zoom last                 | ![](/fig/qgis_zoom_last.png)   |                                 | Zoom to the last zoom                        |
| Zoom next                 | ![](/fig/qgis_zoom_next.png)   |                                 | Zoom to the next zoom                        |

```

```{dropdown} Project managment
| Name            | Menu option                        | Shortcut         | Description                             |
|-----------------|------------------------------------|------------------|-----------------------------------------|
| New Project     | ![](/fig/qgis_new.png)             | `Ctrl` + `N`    | Create a new project                    |
| Open Project    | ![](/fig/qgis_open_project.png)   | `Ctrl` + `O`     | Open an existing project                |
| Save            | ![](/fig/qgis_save_project.png)   | `Ctrl` + `S`     | Save the project                        |
| Save as…        | ![](/fig/qgis_save_project_as.png) | `Ctrl` + `Shift` + `S`  | Save the project as…           |
| Properties      |                                    | `Ctrl` + `Shift` + `P`   | Open the project properties      |
| New print layout| ![](/fig/qgis_new_print_layerout.png) | `Ctrl` + `P`  | Opens the Dialog to create a new print layout |
| Search          |                                    | `Ctrl` + `K`          | Opens the search bar                    |

```

```{dropdown} Layer management
| Name                        | Menu option                                  | Shortcut            | Description                       |
|-----------------------------|----------------------------------------------|----------------------|-----------------------------------|
| Data source manager         | ![](/fig/qgis_data_source_manager.png)       | `Ctrl` + `L`        | Add a new layer                   |
| New GeoPackage layer        | ![](/fig/qgis_new_geopackage_layer.png)     | `Ctrl` + `Shift` + `N` | Add a new GeoPackage Layer       |
| Add vector layer            | ![](/fig/qgis_add_vector_layer.png)         | `Ctrl` + `Shift` + `V` | Add a new vector layer           |
| Add raster layer            | ![](/fig/qgis_add_raster_layer.png)         | `Ctrl` + `Shift` + `R` | Add a new raster layer           |
| Remove selected layer       | ![](/fig/qgis_remove_selected_layer.png)    | `Ctrl` + `D`        | Remove the selected layer        |
| Toggle layers view          |                                              | `Ctrl` + `1`        | Toggle the layers view           |
| Toggle browser view         |                                              | `Ctrl` + `2`        | Toggle the browser view          |


```

```{dropdown} Analysis Tools
| Name                                     | Menu option                                 | Shortcut                   | Description                                            |
|------------------------------------------|---------------------------------------------|-----------------------------|--------------------------------------------------------|
| Identify Features | ![](/fig/qgis_identify_features.png) | `Ctrl` + `Shift` + `I`  | Identify features on the map view by clicking on them |
| Select feature   | ![](/fig/qgis_select_features.png) |  | Select a feature by area or single click  |
| Select feature by value | ![](/fig/qgis_select_features_by_value.png) | `F3` | Select features by value  |
| Open Attribute table    | ![](/fig/qgis_open_attribute_table.png)     | `F6`  | Open the Attribute table                              |
| Open Attribute table with selected features only | ![](/fig/qgis_open_attribute_table.png) | `Shift` + `F6`             | Open the Attribute table with selected features only  |
| Open Attribute table with visible features only | ![](/fig/qgis_open_attribute_table.png)  | `Ctrl` + `F6`               | Open the Attribute table with visible features only   |

```

```{dropdown} Advanced Tools
| Name                    | Menu option                            | Shortcut          | Description                  |
|-------------------------|----------------------------------------|--------------------|------------------------------|
| Processing Toolbox      | ![](/fig/qgis_processing_toolbox.png) | `Ctrl` + `Alt` + `T` | Opens the Processing Toolbox |
| Python Console          | ![](/fig/qgis_python_console.png)     | `Ctrl` + `Alt` + `P` | Opens the Python Console     |

```

## Navigating on the Map Canvas

### Moving the map view

::::{margin}

```{tip}

Holding the `Space`-button on your keyboard activates the ![](/fig/qgis_pan_map.png) `Pan Map`-tool when you're mouse in on the map canvas. Simply move your mouse while holding `Space` and you can move the map view

```

::::

To move on the map canvas with your mouse cursor you need to toggle the hand button. 

![](/fig/qgis_move_symbol.png)

You can always move on the map canvas with arrow keys on your keyboard.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

### Zooming in the map view

::::{margin}

```{tip}
Holding `Ctrl` on windows, or `Cmd` on MacOS, while scrolling allows you to scroll in smaller increments (slower). Try adjusting the map canvas to your needs using this method. 
```

::::

The easiest way to zoom on Map Canvas is by __scrolling__.

Or with the hotkeys `Ctrl`+`+` and `Ctrl`+`-`

![](/fig/qgis_zoom_symbol.png)

Another way is to use the zoom buttons in the toolbox panel.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

## Toolbox & Toolbars

Basically, all the functionality, tools and applications of QGIS are organised in the Toolbox. Some Tools have their own toolbars which you can add to your QGIS interface.

### Open Toolbox

::::{margin}

```{tip}
Holding `Ctrl` + `Alt` + `T` opens and closes the toolbox. 
```

::::

To open the Toolbox in QGIS click on the gearwheel button. Or click on `Processing` -> `Toolbox`

![](/fig/Geschlossene_Toolbox_01.png)

You can use the search bar to find specific tools.

```{tip} There are cases when you want to do something in QGIS but do not know the exact tool. Sometimes it's worth just looking for what you think the name of the tool might be.
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

### Show and hide displays and toolbars

There are toolbars and panels for many different tasks. To avoid an overcrowded interface it is smart to only activate specific toolbars or panels only when you really need them.

To add or remove toolbars from your interface click on `View` -> `Toolbars` -> Check or uncheck the toolboxes you want to add or remove.

To add or remove  panels from your interface click on `View` -> `Panels` -> Check or uncheck the panels you want to add or remove.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video> 

### Move and arrange toolbars

At each toolbar there is a field of two dotted lines. If you move the mouse pointer over it until an arrow cross appears and then hold down the left mouse button, you can move the toolbar. This allows an individualised arrangement of your own tools. By compressing all toolbars into a few lines, the map view window can also be enlarged.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

___

## Save & Open QGIS Projects

To save progress or to open an existing project in QGIS is very similar to programs like MS Word. However, there is one __BIG__ difference. 
In QGIS, the geodata you work with is __not__ saved in your QGIS projectfile. Instead, the project file only contains the file paths where the geodata were located at the time the project was last saved on the PC. If the location of this geodata is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.

Good data organisation with a fixed and well-thought-out folder structure prevents such problems.

```{Warning} 
Always organize your data! Check out the Wiki article on [Standard Folder Structure](/content/Wiki/en_qgis_projects_folder_structure_wiki.md) for more info. 
```


### Open Projects

To open an existing QGIS project click on `Project` -> `Open…` -> Navigate to your project and open it.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

### Save Projects

* __When you save for the first time__: To save the QGIS project you are working on click on `Project` -> `Save as…`-> Navigate to the folder where you want to save the project -> Give the project a name -> `Save`
* __When saving your progress__: To save progress in a project that was already saved somewhere on your computer, there are two good options:
    * Use the hotkey `Ctrl`+ `s` on your keyboard. 
    * Click on `Project` -> `Save`. 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>


## Where to find help

There is a big and vibrant QGIS community



