# QGIS common errors and issues

Here we are collecting common QGIS errors and issues as general QGIS training support.


## Different QGIS versions
 __Main items__ (to add for example different screen views)


## A layer is not displayed in QGIS 

 __Solution:__ 
  1. Right click on the corresponding layer. 
  2. Activate the `Zoom to Layer` function in the pop-up window. 

```{figure} /fig/en_layer_display.png
---
width: 55%git push
git  push
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

These sort of problems are usually due to a) *mismatching KBS in layers and project*, or b) an *incorrect reprojection*. 

 a) 
 1. Check the layer properties (right-click on the corresponding layer).
 2. Select in the pop-up window `Properties`.
 3. In the next pop-up-window select `Information` and check which projection is defined there under the entry `Coordinate Reference System (CRS)`. 
 4. And additionally check if the same projection is set in the status bar at the bottom right.
 5. Correct any discrepancies by reprojecting the layers or changing the setting of the KBS/CRS project. 

b) 

Reprojecting: When having two layers with different KBS/CRS, then select one of the layers as the input layer having, f. ex. the KBS EPSG:32632 - WGS 84 and select EPSG:4326 - WGS 84 as the target KBS. Start the algorithm and you will receive a new layer, identical to the input layer, but with a different KBS. 

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
 Errors often occur if the KBS is set and no reprojection tool has been used. If you suspect that your reprojection has gone wrong, delete all affected layers from GIS, reload the data and then reproject. 
```

## Layer file disappeared from the layer window

If a layer file is no more active in the layer window after reopening a QGIS project, it was only temporarily installed: ![](/fig/en_qgis_temporary_Layer.png)

__Solution:__

Next time do it in a correct way: 
1. Click on the tab `Layer` and on `Save as` in the pop-up window.

```{figure} /fig/en_qgis_save_layer01.png
---
width: 65%
name: en_qgis_save_layer01.png
---

```

2. Put in a `file name` and click on the `three points` ![](/fig/Three_points.png) to save the file on the wished directory place.
3. Select the corresponding CRS/KBS.
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

There may me different reasons, f. ex. reopening your QGIS project, not all files will be displayed correctly because some got lost or were stored on different places, in any case, there is a solution: a clear folder structure.

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

See also the following [__Wiki_Page__]: (https://github.com/GIScience/gis-training-resource-center/blob/main/content/Wiki/en_qgis_projects_folder_structure_wiki.md) for `How to create a new QGIS project` and `How to open an existing QGIS project`.

