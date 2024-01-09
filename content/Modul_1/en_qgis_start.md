# Getting started with QGIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

**Competences:**

- What is QGIS?
- Introducing QGIS: Interface and further basic functionalities

## What is QGIS?

QGIS is an __open source geoinformation system software__. That means the source code is available for everyone, making QGIS a free application. 
You may __view, edit, capture and analyze spatial data or create printable maps__ with it. QGIS was created in 2002 and is a project of volunteers. And it is __constantly changing__.

## Introducing QGIS

- QGIS is a __desktop software__: that means you get a program that opens up on your computer as a window with buttons you can click, forms you can fill out to do tasks, and it's generally a visual interactive experience. 

- QGIS is backed by a __large community of users__, so it’s easy to find solutions to technical issues by using QGIS forums, blog and subreddit.

___


### Open QGIS

Open QGIS like any other program on your computer. 
The start screen of QGIS usually shows you the projects you worked on recently and the option to create a new project.

There are __two__ options to create a new project:

1. On the start screen click on `Project Template`
```{figure} /fig/en_project_template_BRC.png
---
height: 400
name: Project Template
align: Left
---
```
2. In the upper left corner click on `Project` -> ` New Project `

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>

```{tip} 
A QGIS Project file has the format ending `.qgz`
```

### Overview of QGIS Interface

The interface of QGIS is at first glance quite complex. However, once you know all the components you will be able to orientate yourself quickly. Here you can find a description of all components of the interface.

```{tip} When you hover with your mouse cursor over icons, text will appear which explains the function of the button
```

![QGIS_User_Interface](/fig/en_QGIS_GUI.png)


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

### Moving an orientation on the Map Canvas

#### Moving the map view

To move on the map canvas with your mouse cursor you need to toggle the hand button. 

![](/fig/qgis_move_symbol.png)

You can always move on the map canvas with arrow keys on your keyboard.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

#### Zooming in the map view

The easiest way to zoom on Map Canvas is by __scrolling__.

Or with the hotkeys `Ctrl`+`+` and `Ctrl`+`-`

![](/fig/qgis_zoom_symbol.png)

Another way is to use the zoom buttons in the toolbox panel.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

### Toolbox & Toolbars

Basically, all the functionality, tools and applications of QGIS are organised in the Toolbox. Some Tools have their own toolbars which you can add to your QGIS interface.

#### Open Toolbox

To open the Toolbox in QGIS click on the gearwheel button. Or click on `Processing` -> `Toolbox`

![](/fig/Geschlossene_Toolbox_01.png)

You can use the search bar to find specific tools.

```{tip} There are cases when you want to do something in QGIS but do not know the exact tool. Sometimes it's worth just looking for what you think the name of the tool might be.
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

#### Show and hide displays and toolbars

There are toolbars and panels for many different tasks. To avoid an overcrowded interface it is smart to only activate specific toolbars or panels only when you really need them.

To add or remove toolbars from your interface click on `View` -> `Toolbars` -> Check or uncheck the toolboxes you want to add or remove

To add or remove  panels from your interface click on `View` -> `TPanels` -> Check or uncheck the panels you want to add or remove

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video> 

#### Move and arrange toolbars

At each toolbar there is a field of two dotted lines. If you move the mouse pointer over it until an arrow cross appears and then hold down the left mouse button, you can move the toolbar. This allows an individualised arrangement of your own tools. By compressing all toolbars into a few lines, the map view window can also be enlarged.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

___

## Save & Open QGIS Projects

To save progress or to open an existing project in QGIS is very similar to programs like MS Word. However, there is one __BIG__ difference. 
In QGIS the geodata you work with is __not__ saved in your QGIS projectfile. Instead, the project file only contains the file paths where the geodata were located at the time the project was last saved on the PC. If the location of this geodata is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.

Good data organisation with a fixed and well-thought-out folder structure prevents such problems.

```{Warning} 
Always organize your data needly. Check out the Wiki article on [Standard Folder Structure](https://github.com/GIScience/gis-training-resource-center/raw/main//Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure) for more info. 
```


#### Open Projects

To open an existing QGIS project click on `Project` -> `Open…` -> Navigate to your project and open it.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

#### Save Projects

* __When you save the first time__: To save the QGIS project you are working on click on `Project` -> `Save as…`-> Navigate to the folder where you want to save the project -> Give the project a name -> `Save`
* __When you save progress__: To save progress in a project that was already saved somewhere on your computer there are two good options:
    * Use the hotkey `Ctrl`+ `s` on your keyboard. 
    * Click on `Project` -> `Save`. 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>




