# Digitalisation



__🔙[Back to Homepage](/content/intro.md)__

Digitization is the process of converting geographic data from maps or images into digital form commonly represented as vector data.
During this procedure, spatial information from maps or images is traced, forming points, polylines, or polygons.
Proficiency in digitization stands as a cornerstone for GIS specialists. It empowers them to convert spatial information into a digital format, facilitating more efficient data manipulation compared to traditional methods of interpreting images or paper maps.

```{figure} /fig/Digitizsation_concept.drawio.svg
---
width: 900px
name: 
align: center
name: Digitalisation with GIS Concept
---
Digitalisation with GIS Concept. Source:
```

##  Digitizing in QGIS

Digitalizing data in QGIS is straightforward. In the following, you will learn all the steps in detail.


### Digitization toolbars

First, you need to check if the 'Digitizing Toolbox` is activated. To do that 
* Click on the `View` tab in the menu bar and click `Toolbars`. Check if the `Digitizing` and `Advanced Digitizing` toolbox is activated.

::::{grid} 2
:::{grid-item-card}  Activate `Digitizing Toolbox`
First, you need to check if the 'Digitizing Toolbox` is activated. To do that 
1.  Click on the `view` tab in the menu bar and click `Toolbars`. Check if the `digitizing` and `Advanced digitizing` toolbox is activated.

2. A tool box like this should appear on top of your Qgis 
 
 ![](/fig/Toolbox.png)
 
:::
:::{grid-item-card} How to: 

```{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
name: 
align: center
name: Digitalization Toolbar 
---
Digitalization Toolbar.
```
:::
::::

The normal digitalization toolbar offers all the necessary functions to do digitalization. However, for everything that goes above just creating new features and deleting features, the advanced digitalization toolbar is needed. 
The advanced digitalization toolbar allows you to move features, delete parts of features and much more. All functions are listed in the two tables below.

:::{dropdown} Digitalization Toolbar
|Tool|Purpose|Tool|Purpose|
|---|---|-----|---|
|![](/fig/mActionAllEdits.png) |Access to save, rollback or cancel changes in all or selected layers simultaneously | ![](/fig/mActionToggleEditing.png)|Turn on or off edit status of selected layer(s) based on the active layer status|
|![](/fig/mActionSaveEdits.png) |Save edits   | |
|![](/fig/mActionDigitizeWithSegment.png) |Digitize using straight segments |![](/fig/mActionDigitizeWithCurve.png)|Digitize using curve lines|
|![](/fig/mActionStreamingDigitize.png)|Enable freehand digitizing|![](/fig/mActionDigitizeShape.png) |Digitize polygon of regular shape  |
|![](/fig/mActionNewTableRow.png)  |Add new record   | ![](/fig/mActionCapturePoint.png)| Add Feature: Capture Point |
|![](/fig/mActionCaptureLine.png) |Add Feature: Capture Line   |![](/fig/mActionCapturePolygon.png)|Add Feature: Capture Polygon  |
|![](/fig/mActionVertexTool.png) |Vertex Tool (All Layers) | ![](/fig/mActionVertexToolActiveLayer.png)|Vertex Tool (Current Layer)  |
|![](/fig/checkbox.png)|Set whether the vertex editor panel should auto-open|![](/fig/mActionMultiEdit.png)|Modify the attributes of all selected features simultaneously |
|![](/fig/mActionDeleteSelectedFeatures.png) |Delete Selected features from the active layer   |![](/fig/mActionEditCut.png) |Cut Features from the active layer  |
|![](/fig/mActionCopySelected.png) |Copy selected Features from the active layer   |![](/fig/mActionEditPaste.png) |Paste Features into the active layer  |
|![](/fig/mActionUndo.png) |Undo changes in the active layer   | ![](/fig/mActionRedo.png)|Redo changes in active layer  |

:::


:::{dropdown} Advanced digitizing Toolbar

|Tool|Purpose|Tool|Purpose|
|---|---|-----|---|
|![](/fig/cad.png)|Enable Advanced Digitizing Tools|||
|![](/fig/mActionMoveFeature-1.png)![](/fig/mActionMoveFeatureLine.png)![](/fig/mActionMoveFeaturePoint.png)|Move Feature(s)|![Alt text](/fig/mActionMoveFeatureCopy.png) ![](/fig/mActionMoveFeatureCopyLine.png) ![](/fig/mActionMoveFeatureCopyPoint-2.png)|Copy and Move Feature(s)|
|![Alt text](/fig/mActionRotateFeature.png)|Rotate Feature(s)|![Alt text](/fig/mActionSimplify.png)|Simplify Feature|
|![Alt text](/fig/mActionScaleFeature.png)|Scale Feature||
|![Alt text](/fig/mActionAddRing.png)|Add Ring|![Alt text](/fig/mActionAddPart.png)|Add Part|
|![Alt text](/fig/mActionFillRing.png)|Fill Ring|![Alt text](/fig/mActionReverseLine.png)|Swap direction|
|![Alt text](/fig/mActionDeleteRing.png)|Delete Ring|![Alt text](/fig/mActionDeletePart.png)|Delete Part|
|![Alt text](/fig/mActionOffsetCurve.png)|Offset Curve|![Alt text](/fig/mActionReshape.png)|Reshape Features|
|![Alt text](/fig/mActionSplitParts.png)|Split Parts|![Alt text](/fig/mActionSplitFeatures.png)|Split Features|
|![Alt text](/fig/mActionMergeFeatureAttributes.png)|Merge Attributes of Selected Features|![Alt text](/fig/mActionMergeFeatures.png)|Merge Selected Features|
|![Alt text](/fig/mActionRotatePointSymbols.png)|Rotate Point Symbols|![Alt text](/fig/mActionOffsetPointSymbols.png)|Offset Point Symbols|
|![Alt text](/fig/mActionTrimExtend.png)|Trim or Extend Feature|||
:::


 ## Digital data creation

To digitize data for a new dataset you always have to start with creating the dataset before filling it with digitised data.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_create_layer.mp4"></video>

1. `Layer` --> `Create Layer` -> `New GeoPackage Layer` or `New Shapefile Layer`
2. Click on ![](/fig/Three_points.png) and navigate to the folder where you want to save the dataset.
3. `File encoding`: Make sure this is set to UTF-8
4. `Geometry type`: Select the type of feature you want to digitalise e.g. points or lines.
5. Under `Additional dimension` you should always make sure that you check `None`. Except if there is the possibility to collect the Z-values (Elevation) as well. But this is mostly not the case.
6. CRS dropdown: Select the EPSG/CRS you want to set for the new layer. By default, the QGIS selects the project CRS. If you want to change the CRS click on ![](/fig/mIconProjectionEnabled.png).
7. Under `New Field` you can add columns to the new layer. 
    * `Typ`: Select the data type the column will have e.g. `Text`, `Whole number`, `Decimal Number`, `Date`.
    ```{Note} 
    The number of options depends on the data format the layer will have. GeoPackage for example offers far more options than the Shapefileformat.
    ```
    * Click on ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
8. Click `OK`

```{figure} /fig/New_GeoPackage_Layer.png
---
width: 500px
name: Digitalisation Toolbar 
align: center
name: Digitalization Toolbar 
---
Digitalization Toolbar.
```

```{attention} 
One important concept to understand before starting to add data to datasets is that whenever you make changes to a dataset other than styling, you have to put it in editing mode. This is done by selecting the layer and clicking on![](/fig/mActionToggleEditing.png). Now the buttons for many functions of the digitalization toolbar are clickable. 
After you are done manipulating the layer click on ![](/fig/mActionSaveEdits.png) to save your edits. 

```

### Creation of point data

To digitalize points, first you need an existing point layer or you need to create one (check out [Digital Data Creation]( https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html#digital-data-creation) above).

1.	Select the point layer you want to add data to in the Layer panel
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePoint.png). 
4.	Left-click on the feature you want to digitalize.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
5.	Once you are done with digitalization ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>



```{figure} /fig/point_creation.png 
---
width: 500px
name: Point creation
align: center
name: Point creation
---
Point creation.
```

#### Creation of line data

The  method  is  similar  to  digitizing  a  point  (see  above). First you have to created a new line layer or use an existing one. 

```{attention} 
If you create a new line layer remember to change the geometry type into lines because we are creating lines data now.
```
1.	Select the line layer you want to add data to in the Layer panel
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode.
3.	Click on ![](/fig/mActionCaptureLine.png). 
4.	To digitalize line features, click along the line. When you are done, right-click on the last point of the line to finish the feature.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitalisation ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>


#### Creation of polygon data

The method is similar to digitizing a point or a line (see above).

1.	Select the polygon layer you want to add data to in the Layer panel
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePolygon.png). 
4.	To digitalize polygon features, left-click around the area you want do digitize. When you are done, right-click on the last point of the area to finish the feature.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitalization ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_feature.mp4"></video>


## Digital data editing

For editing existing geodata you use the same toolbars as for the creation. This chapter will cover the change of geometries of data, not covering changing data in the attribute table.

For all cases...

1. You first have to select the layer you want to edit.
2. Click on ![](/fig/mActionToggleEditing.png) to activate editing mode.
3. Do your changes.
4. Save your edit by clicking on ![](/fig/mActionSaveEdits.png).
5. Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

```{Tip} 
You can use the ![](/fig/mActionUndo.png) & ![](/fig/mActionRedo.png) buttons to reverse changes easily.

Note that this is only possible __before__ you save the changes.
```

### Deleting features

1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitalisation toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Clicking on ![](/fig/mActionSelectRectangle.png) and selecting the feature you want to delete (see [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#manual-selection)).
4.	Once you have selected the features click on ![](/fig/mActionDeleteSelectedFeatures.png) to delete the feature.
5.	Once you are done with editing click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/delet_feature_geometry.mp4"></video>

### Moving features

There are multiple methods to move features. Here we show the method that works for point, line and polygon features the same.
For that you need the Advanced Digitalization Toolbox.


1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![](/fig/mActionMoveFeaturePoint.png) and click on the feature you want to move. Then click on the location you want to move the feature to.
4.	Once you are done with editing click on ![](/fig/mActionSaveEdits.png) to save your edits.
5.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/move_feature_geometry.mp4"></video>

### Modifying geometries of feature

1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![](/fig/mActionVertexToolActiveLayer.png).
4.	Now you can now move every vertex (corner) of a feature. Click on the vertex/corner you want to move and then click on the location where you want to move the vertex to.
5.	Once you are done with editing click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_move_vertices.mp4"></video>


### Add a ring to a polygon feature

A ring in QGIS is a part inside a polygon that is not part of the polygon. Image a polygon representing a lake. The ring is an island in the lake. For a better understanding, watch the video below.

1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitalization toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![Alt text](/fig/mActionAddRing.png).
4.	Create a ring by clicking the area you want to exclude. To close the ring do a right-click.
5.	Once you are done with editing ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_ring.mp4"></video>




## Digitization Errors in QGIS

Positional errors are inevitable when data are manually digitized. The most common examples include undershooting and overshooting.  When your coordinates do not connect as they should, and overshooting, when the lines go past where they should. Often these errors are not visible unless you zoom in quite a bit on the coordinates. Setting a fuzzy tolerance (snapping tolerance) is used to reduce undershoots and overshoots. The snapping tolerance is the minimum tolerated distance between nodes, lines and/or vertices.

```{figure} /fig/Digitization_Errors.PNG
---
width: 500px
name: 
align: center
name: Digitizing Errors in QGIS
---
Digitizing Errors in QGIS. Source: SpatialPost.
```



