# QGIS common errors and issues

Here we are collecting common QGIS errors and issues as general QGIS training support.


## Different QGIS versions
The Wiki and in particular the videos it contains are only a snapshot in time. QGIS itself, as well as the installable extensions, are constantly being developed and improved. There may therefore be differences between the various versions in the appearance of the user interface or, in rare cases, even in the function. Consequently, there may be differences between the wiki and the QGIS installed on your PC.

## QGIS on Mac doesn't open
When opening QGIS for the first time on Mac you can get this error message:

```{figure} /fig/qgis_on_mac.png
---
width: 55%
name: qgis_on_mac.png
---

```

To solve this press the control button on your keyboard and right-click open.
    
If this problem persists, you can change the settings on your device. Go in the `Settings` > `Security & Privacy` and scroll down, click `Open Anyway`

```{figure} /fig/opening_qgis_mac.png
---
width: 55%
name: opening_qgis_mac.png
---

```


## A layer is not displayed in QGIS 

 __Solution:__ 
  1. Right click on the corresponding layer. 
  2. Activate the `Zoom to Layer` function in the pop-up window. 

```{figure} /fig/en_layer_display.png
---
width: 55%
name: en_layer_display.png
---

```

## A layer window has disappeared in QGIS

__Solution:__
 1. Open in the main tab `View`. 
 2. In the pop-up window select `Panels`. 
 3. In the sub-window hook the case `Layers`.   

```{figure} /fig/en_closed_layer_view.png
---
width: 75%
name: en_closed_layer_view.png
---

```

## Layers that should actually be in the same position are not on top of each other

__Solution:__

These sort of problems are usually due to a) *mismatching crs in layers and project*, or b) an *incorrect reprojection*. 

 a) 
 1. Check the layer properties (right-click on the corresponding layer).
 2. Select in the pop-up window `Properties`.
 3. In the next pop-up-window select `Information` and check which projection is defined there under the entry `Coordinate Reference System (CRS)`. 
 4. And additionally check if the same projection is set in the status bar at the bottom right.
 5. Correct any discrepancies by reprojecting the layers or changing the setting of the crs project. 

b) 

**Reprojecting:**  
When having two layers with different crs, then select one of the layers as the input layer having, f. e. the crs EPSG:32632 - WGS 84 and select EPSG:4326 - WGS 84 as the target crs. Start the algorithm and you will receive a new layer, identical to the input layer, but with a different crs. 

It is displayed in the workspace in the same place as the other layers, as QGIS reprojects it at runtime. However, its actual coordinates are different. 


```{figure} /fig/en_qgis_layer_with_different_KBS.png
---
width: 75%
name: en_qgis_layer_with_different_KBS.png
---
```

You can check this using the `Add Geometry Attributes`< `Geometry Tools` algorithm. The coordinates are different from the coordinates in the other two attribute tables of the other layers.

Detailed procedure:

1. Select the `Vector`tab.

2. Activate in the pop-up menue `Data Management Tools`.

3. And in the following pop-up menue `Reproject Layer`.


```{figure} /fig/en_qgis_reproject_vector_layer01.png
---
width: 75%
name: en_qgis_reproject_vector_layer01.png
---
```


```{figure} /fig/en_qgis_reprojected_layer.png
---
width: 75%
name: en_qgis_reprojected_layer.png
---
```

Always save your reprojected layers by the `Export` and `Save as` functions because they are only temporarily saved and will disappear after closing the project.

```{figure} /fig/en_qgis_reprojection_export.png
---
width: 75%
name: en_qgis_reprojection_export.png
---
```

Similar procedure for raster layers ...

1. Select the `Raster` tab.

2. Activate in the pop-up menue `Projections`.

3. And in the following pop-up menue `Warp (Reproject)`


```{figure} /fig/en_qgis_reproject_raster_layers01.png
---
width: 75%
name: en_qgis_reproject_raster_layers01.png
---
```
```{attention} 
 Errors often occur if the crs is set and no reprojection tool has been used. If you suspect that your reprojection has gone wrong, delete all affected layers from QGIS, reload the data and then reproject. 
```

## Layer file disappeared from the layer window

If a layer file is no more active in the layer window after reopening a QGIS project, it was only temporarily installed. Temporary layers have a symbol on the right of their name, as so:
 ![](/fig/en_qgis_temporary_Layer.png)

__Solution:__

Next time, save it: 
1. Click on the tab `Layer` and on `Save as` in the pop-up window.

```{figure} /fig/en_qgis_save_layer01.png
---
width: 65%
name: en_qgis_save_layer01.png
---

```

2. Put in a `file name` and click on the `three points` ![](/fig/Three_points.png) to save the file on the wished directory place.
3. Select the corresponding CRS.
4. Click `ok`.

```{figure} /fig/en_qgis_save_layer02.png
---
width: 85%
name: en_qgis_save_layer02.png
---

```

## Missing processing tools in the panels tool and incomplete vector tab

 __Solution:__
  
  1. Activate the `Processing Tools` by going to `Plugins` >
  `Manage and install Plugins`.
  2. Select `All`. 
  3. Rehook the `Processing Function` in the corresponding list.
  
```{figure} /fig/en_missing_processing_tools.png
---
width: 85%
name: en_missing_processing_tools.png
---

```
 See also: Geographic Information Systems
 https://gis.stackexchange.com/questions/202111/missing-processing-tools-in-vector-menu-of-qgis


## Missing toolbox
  __Solution:__

  1. To reactivate the `Toolbox` ![](/fig/mAction.png) click on the `View Tab`.
  2. Select in the pop-up window `Panels`. 
  3. Set in the following pop-up window a hook for the `Processing Toolbox`.  

```{figure} /fig/en_missing_toolbox.png
---
width: 75%
name: en_missing_toolbox.png
---

```

## The North arrow is not syncing with the corresponding map
__Solution:__

There are two places where you have to define with which map the N arrow should rotate with.

1. In the `Layout Tab` for the image under `General Settings` make sure that the reference map has the right map selected. 

2. Go to `Properties`, expand `Image Rotation`, select the `Sync with map option` and define here which map it should be.

See also: Geographic Information Systems
https://gis.stackexchange.com/questions/265095/north-arrow-not-syncing-with-map-qgis-2-18#:~:text=1%20Answer&text=2-,There%20are%20TWO%20places%20where%20you%20have%20to%20tell%20it,and%20tell%20it%20which%20map
 
## Invalid Geometry

If the error message `Invalid Geometries` appears, it may be that vector files have "slipped" during the processing or downloading process (e.g. the lines of polygons no longer fit together exactly).

__Solution:__

These errors in the geometries can be corrected by selecting `Fix Geometries` in the Processing Toolbox.

## Wrong data results or missing data

When you get wrong data results or missing data, please check your file names. You should not use file names with capitals, special characters or empty spaces. Always use underscores between the words for the file name.

## File Management Issues

There may be different reasons, f. ex. reopening your QGIS project, not all files will be displayed correctly because some got lost or were stored on different places, in any case, there is a solution: a clear folder structure.

__Solution:__

Recommended standard folder structure:

![](/fig/Standard_project_folder_structure.drawio.svg)

How it may look like on your pc:


```{figure} /fig/en_qgis_folder_structure_pc.png
---
width: 75%
name: en_qgis_folder_structure_pc.png
---

```
The standard folder structure has two principal advantages:
1. By sharing the whole project folder, we can be certain that the project will run without problems on a different computer.
2. The folder structure supports the proper organization of geodata and supports the stable function of a QGIS project. 

The folder structure template can be downloaded [__here__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).


```{Tip}
The layer data used in the project are not saved in the project file. Instead, the project file only contains the file paths where the layer data were located at the time the project was last saved on the PC. If the location of this layer data is subsequently changed, the error message "handle unavailable layers" will appear when the project is opened again.
Good data organisation with a fixed and well thought-out folder structure prevents such problems.
```

See also the following [__Wiki_Page__]: 

(https://github.com/GIScience/gis-training-resource-center/blob/main/content/Wiki/en_qgis_projects_folder_structure_wiki.md) for `How to create a new QGIS project` and `How to open an existing QGIS project`.

## Specific QGIS problems 
### Basic settings > Deactivating the automatic projection selection
After installing QGIS, some basic settings should be changed to avoid possible sources of error.
If a layer file does not have a projection, a projection must be defined for it when it is imported into QGIS. By deactivating the automatic projection selection, this projection can be defined manually. This prevents layers from accidentally being in the wrong projection.

1. Select the `Settings` tab.
2. Then activate in the nagivation menue `Options`.
3. In the pop-window select `CRS Handling`. 
4. Under `CRS for projects` activate `Use CRS from first layer added`. 
5. And under `CRS for layers` activate `Prompt for CRS`.

```{figure} /fig/en_qgis_CRS_settings.png
---
width: 95%
name: en_qgis_CRS_settings.png
---

```

### Regular saving
Unfortunately, GIS programs are notorious for freezing or crashing completely. Although there is a trend towards fewer complications with better hardware, even a "gaming PC" costing several thousand euros is not completely safe.
More complex tasks with longer calculation times may still cause problems. Regular saving is therefore recommended.

See also the following [__Wiki_Page__]:

(https://github.com/GIScience/gis-training-resource-center//content/Wiki/en_qgis_interface_wiki.html#save-open-qgis-projects) `Save and open QGIS Projects`. 

### GRASS applications

 QGIS also allows the use of tools from external GIS software, such as GRASS GIS. GRASS does not have to be downloaded separately, but is automatically installed when QGIS is installed. GRASS tools are identified by their icon. 

 ```{attention} 
  Please note that the GRASS software is not started when the standard QGIS application is started. Consequently, an error message may appear when using GRASS tools. This can be remedied by opening the QGIS with GRASS application (found via the computer's search function) instead of the standard application.
 ```

 ### SAGA with Linux

 SAGA is another external GIS software. SAGA tools are identified by their icon. When using Windows or MacOS as the operating system, SAGA is automatically implemented when QGIS is installed. With Linux, however, SAGA is not installed automatically and must be installed manually. Experience has shown that this installation is not always easy and can cause problems. Alternatively, you can either use a Windows or MacOS virtual box or refrain from using SAGA tools (you will then have to search for alternative tools yourself).

### Umlauts, special characters, spaces in file paths

If the file path contains umlauts (ä,ö,ü), special characters (!,?, ., etc.) or spaces, this can lead to problems when these files are processed by QGIS. It is therefore recommended that you avoid these characters in your file paths (write out umlauts, replace spaces with _).

```{attention} 
Temporary files are user-specific (if several people use one PC, each person has their own temporary files). The file path therefore contains your user name. If this contains problematic characters, it may therefore be advisable to change it.

 ```

## Help Access Links

Here you will find further Help access links or QGIS community links to address specific issues.

....



