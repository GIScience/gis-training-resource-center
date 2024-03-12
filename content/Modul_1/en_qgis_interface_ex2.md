# Exercise 1: Understanding the Interface

__🔙[Back to Homepage](/content/intro.md)__


---
## Aim of the exercise

QGIS is a complex program with lots of functions, and the interface can be confusing. This exercise will get you familiar with the main toolbars, windows and panels in QGIS. You will create a new QGIS project and save it, and navigate through the different panels and toolbars.

The exercise covers: 

- Saving and loading a QGIS project
- Finding and using different toolbars
- Finding and using different panels 
- Moving panels around
- Activating new panels

---

## Related wiki articles

- [QGIS interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
- [Projects and folder structure](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)

---

## Data preparation

- Download the zipped template folder structure [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_1/Modul_1_Exercise_1_Understanding_the_interface/Modul_1_Exercise_1_Understanding_the_interface.zip)
- You should now have a folder structure looking like this:

```{figure} /fig/Standard_project_folder_structure.drawio.svg
---
width: 800px
name: 
align: center
name: Standard folder structure
---
Standard folder structure. Source: 
```

---

## Tasks

1. Create a new project. When opening QGIS, you will be greeted by 
the start layout, which shows the QGIS interface with no project loaded. On the 
left will be a panel with recent projects (this will probably be empty). To the 
right will be a news panel, showing posts from the QGIS blog, and beneath this 
is a `Project Templates` panel. 

```{figure} /fig/en_project_template_BRC.png
---
height: 400
name: Project Template
align: Left
---
```
- In the `Project Templates` panel, __Double click on the `New Empty Project` option__ (it should be the only template visible). You will see a blank canvas in the main interface since there is no data loaded yet. 

2. Get to know the QGIS interface: Above the canvas, you will find the 
__toolbar__ with a lot of different functions. To the left and right of the canvas 
you will find the panels. In QGIS, you will mostly access tools by finding them 
in the __toolbars__ or __panels__. 

- Toolbars are at the top of the screen by default. They include the controls that 
let you switch between different ways of interacting with the interface. 

- Panels are at the sides of the screen by default. They include the file browser 
and layer navigation panels to the left of the screen. Other panels can be 
toggled to search and use processing tools. In the layer panel, you will see the 
data we will add later on.
On the right of the screen, you will most likely have the __Processing Toolbox__ panel 
and __Layer Styling__ panels. If it is missing for you, check out this [wikipage](content/Wiki/en_qgis_common_errors_and_Issues.md).

```{figure} /fig/en_QGIS_GUI.png
---
width: 800px
name: 
align: center
name: QGIS User Interface
---
QGIS User Interface. Source:
```

You can undock panels from their location by clicking and dragging the panel 
title. You can either dock it to another panel (it will appear as another tab), 
or turn it into its own window. You can also resize the panels. 
<!-- FIXME: there is no exercise here - can we get people to try it? -->

```{TIP}
Depending on the screen you are working on, the QGIS  interface might look a little 
different. Sometimes elements can be hidden because it is not rendered correctly 
by default. Try resizing the panels and look at the different options and functions 
they offer. 
```
<!-- FIXME: Need a clearer explanation in this tip -->

QGIS has other panels you can use that aren't shown by default. Let's see how we 
can find and activate the other panels and toolbars.

- In the `View` menu, find the `panels` and `toolbar` options. Hovering over each 
will show a list of the available panels and toolbars, and which are activated. 
Give yourself a minute to look through the different toolbars and panels. 
There are lots of options but don't worry, you won't use most of them in this 
training. 

The panels we'll use the most are: 
- Browser
- Layers
- Layer Styling
- Processing Toolbox

Now, let's take a look at the toolbars. The toolbars we'll use the most are:  
- Attributes Toolbar
- Digitizing Toolbar
- Map Navigation Toolbar
- Project Toolbar
- Selection Toolbar
 

Take time to make yourself familiar with the different ways you can arrange 
the QGIS interface. Knowing where to find the different functions can save you a 
lot of time and frustration in the future!

---

1. Let's save the project now. Click on the save icon on the toolbar or 
open the  `Project` menu and choose `Save As...`
1. Choose a location for the project file. An ideal place would be in the project 
subfolder in the template folder. Navigate to the folder called `Module_1_Exercise_0` and open the subfolder called `Project`. Select this location and give the 
QGIS project a name (for example: `QGIS_Training_Exercise_0`). The project will 
be saved as a `.qqz` file.
1. Click `Save` 
2. Close the QGIS aplication and reopen it.
3. When QGIS restarts, the project we just saved will appear in the 
`Recent Projects` panel. You can double-click it to open it. You can 
also navigate to the `.qgz` file in your file explorer and double click on it. 
This will also launch QGIS and load the project. 

```{Tip}
Keeping your folder structure organised goes a long way in helping you work 
efficiently and without frustration.
```

```{Warning}
__Remember__: Project files in QGIS are saved separately from the data and style 
files you are using in the project, which is why it is advisable to keep all the 
files related to a project in a folder.
```
<!-- CLARIFY: Some styles are stored in the project file -->

If the icons do not display correctly, you may want to customize the interface. 
<!-- CLARIFY: what is meant by "correctly"> How will people know if it is showing
    correctly or not? -->

:::{dropdown} Opening the settings and customizing the interface. 

If the interface does not display correctly on your device, you can customize 
the font and symbol size to better fit your needs.

1. Navigating to the preferences via `Settings` > `Options` 
2. Navigate to the `General` tab on the left. 
3. Here, you can change the user interface theme, the icon size and font.  

:::

