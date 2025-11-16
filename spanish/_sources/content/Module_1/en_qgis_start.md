::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Getting started with QGIS

## Introducing QGIS

:::{figure} /fig/en_qgis_banner_website.png
---
name: en_qgis_banner_website
width: 300 px
align: right
---
[qgis.org](https://qgis.org/)
:::

:::{div} sd-text-justify
- QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, 
making QGIS a free application. The entire source code can be viewed and downloaded on https://github.com/qgis/QGIS.
- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons 
you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 
- You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 
and is a project of volunteers. And it is __constantly changing__.
- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blogs, or sub-reddits. The official QGIS community can be found [here](https://qgis.org/en/site/forusers/support.html#support). Additionally, a list of helpful websites can be found on the [wiki here](/content/Wiki/en_qgis_common_errors_and_Issues.md).
:::


:::{note}

Keep in mind that as QGIS gets developed further, the interface and functions of QGIS are subject to changes. The material written for this platform is referring to QGIS Version 3.36. If the training material is no longer up to date, take a look at the [QGIS Documentation](https://docs.qgis.org/3.34/en/docs/index.html).

:::

:::{attention}

QGIS is constantly changing, with new features being added. Because of this, the newer versions can have changes or even bugs (such as crashes). However, there is always a stable version available, which is supported for longer. This version is called __Long-term release (LTR)__. 

:::


## Working with QGIS


In QGIS, you create projects where you visualise and manipulate geodata. There are three main workflows you will use: __data collection and creation, data processing, and data visualisation__. Geodata is loaded into QGIS projects which will be represented as layers on a map canvas.

:::{hint}

There is a lot of complex math involved in the GIS, but QGIS takes care of it on it's own and you don't need to have a deep understanding of maths and algorithms to use QGIS. __As long as you can use Excel and Powerpoint, you shouldn't have trouble learning how to use QGIS__. 

:::

::::{tab-set}

:::{tab-item} Data Collection and Creation

QGIS offers tools to create your own geodata. For example, with the digitizing tools, you can create points, polygons, and lines with information which can represent spatial information. Furthermore, georeferencing lets you add geographic information to various types of data, such as satellite imagery or hand-drawn maps. You will learn how to create geodata and how to georeference data in __[module 2](/content/Module_2/en_module_2_overview.md)__. 

Sometimes working with GIS requires you to go and collect the data in the field. In this case, you can use [web and mobile apps](/content/Wiki/en_web_and_mobile_apps_wiki.md). 

:::

:::{tab-item} Data Processing

QGIS offers a wide range of algorithms to process geodata. In the following modules, you will get to know a number of algorithms that are especially useful for GIS in humanitarian work. You will learn more about data processing and manipulation in [module 2](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_module_2_overview.html) onwards. 


:::

:::{tab-item} Visualisation

QGIS lets you visualise geodata and create maps to communicate information. It does so by assigning symbols and colours to different elements in your geodata. Assigning a symbology to the geodata is one of the main skills you will develop as a GIS-user and a good visualisation of data is immensely useful when communicating insights. You will learn how to assign symbols in [Module 4: Visualisation of Geodata and Map Making](/content/Module_4/en_qgis_map_design_I.md)


:::
::::




:::{card}
__A note on plugins__
^^^

In addition to the algorithms included in the standard installation, QGIS offers plugins which add additional functionality to the QGIS application. These plugins are developed by independent organizations or the QGIS-community. For example, plugins let you connect to online services such as OpenStreetMap, or add more algorithms to process your data. These can be very useful for certain use cases. There are also plugins specifically designed for humanitarian work. You will learn more about plugins in the following modules. If you want to know how to install them, look into the [wiki](/content/Wiki/en_qgis_plugins_wiki.md). 

:::

## Opening a new project in QGIS

Open QGIS like any other program on your computer. The start screen of QGIS usually shows you the projects you worked on recently and the option to create a new project.

There are __two__ options to create a new project:

::::{margin}
:::{tip}

A QGIS project file has the format ending `.qgz`.

:::

::::
1. On the start screen click on `Project Template`

:::{figure} /fig/en_project_template_BRC.png
---
height: 400
name: en_project_template_BRC
align: center
---
:::

2. In the upper left corner click on `Project` -> ` New Project `

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>



## Overview of the QGIS Interface

The interface of QGIS is at first glance quite complex. However, once you know all the components you will be able to orientate yourself quickly. Here you can find a description of all components of the interface.

::::{margin}
:::{tip}

When you hover with your mouse cursor over icons, text will appear which explains the function of the button.

:::
::::

:::{figure} /fig/en_QGIS_GUI.png
---
width: 800px 
align: center
name: en_QGIS_GUI
---
QGIS User Interface. Source: BRC
:::

1. __Layers panel:__ The __layers list__ shows __all layers/files__ that are __loaded in the project__. You can show/hide layers and set other properties.

2. __Toolbars:__  __Toolbars__ are shortcuts to execute frequently used commands. For example, there are special toolbars for __vector and raster files__, but also general ones for saving your project, etc. The toolbar contains, among other things, a list of all the commands you can use. The toolbar also contains the __processing toolbox__, which is used later in many of the wiki videos.

:::{figure} /fig/en_Interface_02.png
---
height: 75 px
name: en_Interface_02
align: center
---
:::

3. __Map Canvas:__ The __map canvas__ is the __central component__ of every GIS programme. This is where the __geodata__ are displayed. The map view has a projection which does not always have to correspond to the projection of the layers.

4.  __Coordinates and Scale:__ Here you can find information about the scale of the map canvas, as well as read the coordinates of the mouse pointer.

5. __Browser panel:__ The browser panel let's you browse the files on your computer and load datasets into your QGIS project. 

6. __Search bar:__ Here you can __search for tools and layers__ in QGIS. If you don't know where to find a tool, you can try here. You can also type in coordinates to find them on the map canvas. 

:::{dropdown} Exercise: Create a new QGIS project

1. In your “GIS_Training” folder, create a __subfolder__ called "My_First_Project".
2. Open __QGIS__
3. Click on `Project` -> ` New Project `
4. In the top-left corner, click on `Project` -> `Save as`, browse to your Projects folder and save the project as "Session1”
5. Click on __Save as__, browse to your Projects folder and save the project as "My_First_Project"
6. Open your your folder and check the __.qgz file__ that you just created.

:::

:::{attention}

If you see a `*` in the title bar, to the left of the name of your project, this means that the project has changes which are __unsaved__. Since QGIS can crash from time to time, make sure to save your project periodically to avoid losing progress.

:::

## Buttons and Shortcuts

In QGIS, __mouse control__ allows users to interact with the map canvas, enabling functions such as panning, zooming, and selecting features.

__Hotkeys__ in the QGIS interface provide convenient shortcuts for various commands, enhancing efficiency and speeding up workflow. You can find all hotkeys below.

:::{dropdown} Navigation in the map view

| Name                      | Menu option                    | Shortcut                        | Description                                 |
|---------------------------|--------------------------------|---------------------------------|---------------------------------------------|
| Map pan                   | ![](/fig/qgis_pan_map.png)     | <kbd>Space</kbd>, <kbd>Page Up</kbd>,  <kbd>Page Down</kbd> or the <kbd>Arrow Keys</kbd> | Move the map                                 |
| Pan map to selection      | ![](/fig/qgis_pan_map_selection.png) |                                  | Pans the map to the selected element        |
| Zoom in                   | ![](/fig/qgis_zoom_in.png)     | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>+</kbd> or <kbd>mouse wheel</kbd>   | Zoom into the map                            |
| Zoom out                  | ![](/fig/qgis_zoom_out.png)    | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>-</kbd> or <kbd>mouse wheel</kbd>   | Zoom out of the map                          |
| Zoom full                 | ![](/fig/qgis_zoom_full.png)   | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>                  | Zoom to the selected element                |
| Zoom to selection         | ![](/fig/qgis_zoom_to_selection.png) | <kbd>Ctrl</kbd> + <kbd>J</kbd>     | Zoom to the selected element                |
| Zoom to layer             | ![](/fig/qgis_zoom_to_layer.png) |                                  | Zoom to the selected layer                   |
| Zoom to native resolution | ![](/fig/qgis_zoom_native_resolution.png) |                             | Zoom to the native resolution (100%)         |
| Zoom last                 | ![](/fig/qgis_zoom_last.png)   |                                 | Zoom to the last zoom                        |
| Zoom next                 | ![](/fig/qgis_zoom_next.png)   |                                 | Zoom to the next zoom                        |

:::

:::{dropdown} Project management

| Name            | Menu option                        | Shortcut         | Description                             |
|-----------------|------------------------------------|------------------|-----------------------------------------|
| New Project     | ![](/fig/qgis_new.png)             | <kbd>Ctrl</kbd> + <kbd>N</kbd>   | Create a new project                    |
| Open Project    | ![](/fig/qgis_open_project.png)   | <kbd>Ctrl</kbd> + <kbd>O</kbd>     | Open an existing project                |
| Save            | ![](/fig/qgis_save_project.png)   | <kbd>Ctrl</kbd> + <kbd>S</kbd>     | Save the project                        |
| Save as…        | ![](/fig/qgis_save_project_as.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd>  | Save the project as…           |
| Properties      |                                    | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>   | Open the project properties      |
| New print layout| ![](/fig/qgis_new_print_layerout.png) | <kbd>Ctrl</kbd> + <kbd>P</kbd>  | Opens the Dialog to create a new print layout |
| Search          |                                    | <kbd>Ctrl</kbd> + <kbd>K</kbd>        | Opens the search bar                    |

:::

:::{dropdown} Layer management

| Name                        | Menu option                                  | Shortcut            | Description                       |
|-----------------------------|----------------------------------------------|----------------------|-----------------------------------|
| Data source manager         | ![](/fig/qgis_data_source_manager.png)       | <kbd>Ctrl</kbd> + <kbd>L</kbd>        | Add a new layer                   |
| New GeoPackage layer        | ![](/fig/qgis_new_geopackage_layer.png)     | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> | Add a new GeoPackage Layer       |
| Add vector layer            | ![](/fig/qgis_add_vector_layer.png)         | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Add a new vector layer           |
| Add raster layer            | ![](/fig/qgis_add_raster_layer.png)         | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> | Add a new raster layer           |
| Remove selected layer       | ![](/fig/qgis_remove_selected_layer.png)    | <kbd>Ctrl</kbd> + <kbd>D</kbd>        | Remove the selected layer        |
| Toggle layers view          |                                              | <kbd>Ctrl</kbd> + <kbd>1</kbd>        | Toggle the layers view           |
| Toggle browser view         |                                              | <kbd>Ctrl</kbd> + <kbd>2</kbd>       | Toggle the browser view          |

:::

:::{dropdown} Analysis Tools

| Name                                     | Menu option                                 | Shortcut                   | Description                                            |
|------------------------------------------|---------------------------------------------|-----------------------------|--------------------------------------------------------|
| Identify Features | ![](/fig/qgis_identify_features.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>  | Identify features on the map view by clicking on them |
| Select feature   | ![](/fig/qgis_select_features.png) |  | Select a feature by area or single click  |
| Select feature by value | ![](/fig/qgis_select_features_by_value.png) | <kbd>F3</kbd> | Select features by value  |
| Open Attribute table    | ![](/fig/qgis_open_attribute_table.png)     | <kbd>F6</kbd>  | Open the Attribute table                              |
| Open Attribute table with selected features only | ![](/fig/qgis_open_attribute_table.png) | <kbd>Shift</kbd> + `F6`             | Open the Attribute table with selected features only  |
| Open Attribute table with visible features only | ![](/fig/qgis_open_attribute_table.png)  | <kbd>Ctrl</kbd> + `F6`               | Open the Attribute table with visible features only   |

:::

:::{dropdown} Advanced Tools

| Name                    | Menu option                            | Shortcut          | Description                  |
|-------------------------|----------------------------------------|--------------------|------------------------------|
| Processing Toolbox      | ![](/fig/qgis_processing_toolbox.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> | Opens the Processing Toolbox |
| Python Console          | ![](/fig/qgis_python_console.png)     | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>P</kbd> | Opens the Python Console     |

:::

## Navigating on the Map Canvas

::::{admonition} *Optional*: Now it's your turn!

You can follow the steps below in your own QGIS project. Download [this dataset](https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg) and drag and drop the `wb_countries_admin0_10m.gpkg` onto the map canvas. The data set are the official country boundaries by the [World Bank](https://datacatalog.worldbank.org/search/dataset/0038272/World-Bank-Official-Boundaries). 

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg

Download the Worldbank Official Boundaries

:::

::::

### Moving the map view

::::{margin}

:::{tip}

Holding the <kbd>Space</kbd>-button on your keyboard activates the ![](/fig/qgis_pan_map.png) `Pan Map`-tool when you're mouse in on the map canvas. Simply move your mouse while holding <kbd>Space</kbd> and you can move the map view

:::

::::

To move on the map canvas with your mouse cursor you need to toggle the hand button. 

:::{image} /fig/qgis_move_symbol.png
---
name: qgis_move_symbol
height: 40 px
---
:::

You can always move on the map canvas with arrow keys on your keyboard.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

### Zooming in the map view

::::{margin}

:::{tip}
Holding <kbd>Ctrl</kbd> while scrolling allows you to scroll in smaller increments (slower). Try adjusting the map canvas to your needs using this method. 
:::

::::

The easiest way to zoom on Map Canvas is by __scrolling__.

Or with the hotkeys <kbd>Ctrl</kbd> + <kbd>+</kbd> and <kbd>Ctrl</kbd> + <kbd>-</kbd>

![](/fig/qgis_zoom_symbol.png)

Another way is to use the zoom buttons in the toolbox panel.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

## Toolbox & Toolbars

Basically, all the functionality, tools and applications of QGIS are organised in the Toolbox. Some Tools have their own toolbars which you can add to your QGIS interface.

### Open Toolbox

::::{margin}
:::{tip}

Holding <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> opens and closes the toolbox. 

:::
::::

To open the Toolbox in QGIS click on the gearwheel button. Or click on `Processing` -> `Toolbox`

![](/fig/Geschlossene_Toolbox_01.png)

You can use the search bar to find specific tools.

:::{tip} 

There are cases when you want to do something in QGIS but do not know the exact tool. Sometimes it's worth just looking for what you think the name of the tool might be.

:::

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
In QGIS, the geodata you work with is __not__ saved in your QGIS project file. Instead, the project file only contains the file paths where the geodata were located at the time the project was last saved on the PC. If the location of this geodata is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.

Good data organisation with a fixed and well-thought-out folder structure prevents such problems.

:::{Warning} 
Always organize your data! Check out the Wiki article on [Standard Folder Structure](/content/Wiki/en_qgis_projects_folder_structure_wiki.md) for more info. 
:::


### Open Projects

::::{margin}

:::{tip}
Holding <kbd>Ctrl</kbd> + <kbd>O</kbd> also opens the `Open Project`-dialogue box.

:::

::::

To open an existing QGIS project click on `Project` -> `Open…` -> Navigate to your project and open it.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

### Save Projects

::::{margin}

:::{tip}
Pressing <kbd>Ctrl</kbd> + <kbd>S</kbd> saves the project, whereas pressing <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> let's you specify a save location on your computer. 

:::

::::

* __When you save for the first time__: To save the QGIS project you are working on click on `Project` -> `Save as…`-> Navigate to the folder where you want to save the project -> Give the project a name -> `Save`
* __When saving your progress__: To save progress in a project that was already saved somewhere on your computer:
    * Click on `Project` -> `Save`. 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>


## Warning icons

It can be that while working with QGIS, you come across orange warning icons. This indicates that you should pay attention. To understand what the warning icon means, __hover over it with your mouse__ and explanatory text will appear. For example, in {numref}`warning_icon_example`, the warning icon indicates that the units of measurements are degrees, which are not constant (the distance between 1⁰ of longitude is much greater at the equator than at the poles).

:::{figure} /fig/en_3.36_warning_icon_example.png
---
name: warning_icon_example
width: 700 px
---
An example of a warning icon while adjusting the parameters of a processing tool.
:::

## Where to find help

:::{admonition} Connect with us!
:class: tip
If you have more questions before or after the training or require assistance, do not hesitate to reach out to us by writing an email to `gis-training-platform@heigit.org`.
:::

:::{admonition} Common errors and issues
:class: tip
We have collected a list of __[Common errors and issues](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_common_errors_and_Issues.html)__. If you ever find yourself at your wits end (which can happen a lot when working with QGIS!), try finding the solution to your problem here. 
:::


There is also a big and vibrant QGIS community online. If you are struggling with a specific function, or have questions on how to achieve GIS operations that are not covered on this platform, you can find help on dedicated QGIS forums: 

- QGIS documentation: https://docs.qgis.org/3.34/en/docs/index.html 
- QGIS user forum on stackexchange: https://gis.stackexchange.com/?tags=qgis
- QGIS user groups: https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups
- QGIS telegram channel: https://t.me/joinchat/Aq2V5RPoxYYhXqUPoxRWPQ


Additionally, there is a large amount of youtube tutorials, online guides and learning material for specific 
GIS-operations, so it is always a good idea to do a quick google search. Amongst others, the [QGIS documentation](https://docs.qgis.org/3.34/en/docs/index.html) also offers Exercises and Training Material, as well as a [Gentle Introduction to QGIS](https://docs.qgis.org/3.34/en/docs/gentle_gis_introduction/index.html). 


## Self-Assessment Questions

::::{admonition} Test your knowledge
:class: note

Take a moment to recapitulate what you've learned in this chapter by answering the questions below:

1. __What is QGIS, and what does it mean that it is “open source”?__

:::{dropdown} Answer 
QGIS is a Geographic Information System (GIS) software that lets users view, edit, analyze, and produce maps from spatial (geographic) and attribute data.
Being open source means that its source code is freely available: anyone can inspect, modify, and distribute it (under license). It also implies that there is a community of users and developers contributing to it, and that the software is generally available at no cost.
:::

2. __Name three things you can do working with QGIS.__  

:::{dropdown} Answer

- Load spatial data (vector or raster), visualize it on a map
- Edit or digitize features (e.g. adding points, lines, polygons)
- Perform spatial analysis (e.g. buffer, overlay, join), or produce map outputs (export to PDF/image)
:::

3. __How do you know if a QGIS-project has been saved or not?__

:::{dropdown} Answer
Typically, QGIS will show an asterisk (*) next to the project name or in the window/tab title if there are unsaved changes. If no asterisk appears (or if “Save” is greyed out), that suggests the project is already saved (i.e. up to date).
:::

4. __How do you open a QGIS-project?__

:::{dropdown} Answer
You can open a QGIS project via the `File` menu → `Open Project` (or “Open Project” button in toolbar), then browse for a `.qgs` or `.qgz` file. Alternatively, double-clicking the project file (if associated on your system) may also open it in QGIS.
:::

5. __How do you show and hide panels or toolbars?__

:::{dropdown} Answer
In the top bar, use the `View` menu → `Panels` or `Toolbars` submenus to toggle (check/uncheck) specific panels or toolbars.
:::

6. __Where can you find help when you are encountering problems with QGIS?__

:::{dropdown} Answer

- On our [Common errors and issues](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_common_errors_and_Issues.html) page
- By looking into the [QGIS documentation](https://docs.qgis.org/3.34/en/docs/index.html)
- On the [QGIS user forum on stackexchange](https://gis.stackexchange.com/?tags=qgis)
- In [QGIS user groups](https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups)
- By searching for tutorials on youtube

:::

::::

