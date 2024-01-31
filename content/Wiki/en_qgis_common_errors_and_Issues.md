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

These sort of problems are usually due to a) *mismatching KBS in layers and project*, or b) an *incorrect reprojection*. 

 a) 
 1. Check the layer properties (right-click on the corresponding layer).
 2. Select in the pop-up window `Properties`.
 3. In the next pop-up-window select `Information` and check which projection is defined there under the entry `Coordinate Reference System (CRS)`. 
 4. And additionally check if the same projection is set in the status bar at the bottom right.
 5. Correct any discrepancies by reprojecting the layers or changing the setting of the KBS/CRS project. 

b) 

When reprojecting, follow exactly the procedure described in the Wiki under *Projections* (to add). Errors often occur if KBS is set and no reprojection tool is used. If you suspect that your reprojection has gone wrong, delete all affected layers from GIS, reload the data and then reproject. 


```{figure} /fig/en_CRS_projection_check.png
---
width: 85%
name: en_CRS_projection_check.png
---

```

## Missing processing tools in the panels tool and incomplete vector tab

 __Solution:__
  
  1. Activate the `processing tools` by going to `Plugins` >
  `Manage and install Plugins`.
  2. Select `All`. 
  3. Rehook the `Processing function` in the corresponding list.
  
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

## Layer file disappeared from the layer window

If a layer file is no more active in the layer window after reopening a QGIS project, it was only temporarily installed.

__Solution:__

Next time do it in a correct way: 
1. Click on the tab `layer` and on `save as` in the pop-up window.

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
