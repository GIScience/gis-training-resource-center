# Projects and Folder Structure 

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

In this wiki article, best practices for the creation and management of QGIS projects and geodata is presented.

## Step-by-step: Setting up a new QGIS project from scratch

```{Tip}
It is good practice to use a __standard folder structure__ for QGIS projects in which the project, all used geodata, styling files and documentation is stored.
```

1. Copy the standard folder structure for QGIS projects to the place you want to store your whole project. You can download the standard folder structure *here*.

2. Open QGIS and create a new project. Click on `Project` -> `New Project`

### Create a new QGIS Project

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>

3. Safe the new project in the `Project` folder in the standard folder structure and git push. 
4. Give your project a name and click
```{Tip}
Do not use spaces ` ` in the name, instead always use underscores `_`
```
#### Save Project

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_as.mp4"></video>



4. Check the Coordinate Reference System (CRS)/EPSG code of the project to the CRS/EPSG you want to use. For more information check the wiki article on [Projection](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it).

### Check and change CRS/EPSG

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

```{Tip}
The layer data used in the project are not saved in the project file. Instead, the project file only contains the file paths where the layer data were located at the time the project was last saved on the PC. If the location of this layer data is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.
Good data organisation with a fixed and well thought-out folder structure prevents such problems.
```

## Open existing QGIS Projects 

Open QGIS -> `Project` -> `Open` -> Select your project 

__Open QGIS Project__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4"></video>

## Standard Folder Structure 

The standard folder structure has two principal advantages:
1. By sharing the whole project folder, we can be certain that the project will run without problems on a different computer.
2. The folder structure supports the proper organization of geodata and supports the stable function of a QGIS project. 

The folder structure template can be downloaded [__here__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).

![](/fig/Standard_project_folder_structure.drawio.svg)

