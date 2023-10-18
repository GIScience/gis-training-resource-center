# QGIS manage Projects and Geodata

In this wiki article, best practices for the creation and management of QGIS projects and geodata is presented.

## Step-by-step: Setting up a new QGIS project from scratch

```{Tip}
It is good practice to use a standardized folder structure for QGIS projects in which the project, all used geodata, styling files and documentation is stored
```

1. Copy the standard folder structure for QGIS projects to the place you want to store your whole project. You can download the standard folder structure *here*.

2. Open QGIS and create a new project. Click on `Project` -> `New Project`

__Create a new QGIS Project__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>

3. Safe the new project in the `Project` folder in the standard folder structure and give the project a suitable name. Click on `Project` -> `Save As`
```{Tip}
Do not use spaces ` ` in the name. instet always use underscors `_`
```
__Save Project__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_as.mp4"></video>



4. Check the Coordinate Reference System (CRS)/EPSG code of the project to the CRS/EPSG you want to use. For more information check the wiki article on [Projection](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it).

__Check and change CRS/EPSG__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

```{Tip}
The layer data used in the project is not saved in the project file. Instead, the project file only contains the file paths where the layer data were located at the time the project was last saved on the PC. If the location of this layer data is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.
Good data organisation with a fixed and well thought-out folder structure prevents such problems.
```

## Open existing QGIS Projects 

Open QGIS -> `Project` -> `Open` -> Select your project 

__Open QGIS Project__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4"></video>

## Standard Folder Structure 

![](/fig/Standard_folder_structure.svg)
