# Digitalisation


Digitization is the process of converting geographic data from maps or images into digital form commonly represented as vector data.
During this procedure, spatial information from maps or images is traced, forming points, polylines, or polygons.
Proficiency in digitization stands as a cornerstone for GIS specialists. It empowers them to convert spatial information into a digital format, facilitating more efficient data manipulation compared to traditional methods of interpreting images or paper maps.

```{figure} /fig/Digitizsation_concept.drawio.svg
---
width: 900px
name: Digitalisation with GIS Concept 
align: center
---
```

##  Digitizing in QGIS

Digitalizing data in QGIS is straightforward. In the following, you will learn all the steps in detail.


### Digitization toolbars

Firstly, you need to check if the 'Digitizing Toolbox` is activated. To do that 
* Click on the `view` tab in the menu bar and click `Toolbars`. Check if the `digitizing` and `Advanced digitizing` toolbox is activated.

::::{grid} 2
:::{grid-item-card}  Activate `Digitizing Toolbox`
Firstly, you need to check if the 'Digitizing Toolbox` is activated. To do that 
1.  Click on the `view` tab in the menu bar and click `Toolbars`. Check if the `digitizing` and `Advanced digitizing` toolbox is activated.

2. A tool box like this should appear on top of your Qgis 
 
 ![](/fig/Toolbox.png)
 
:::
:::{grid-item-card} How to: 

```{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
name: Digitalisation Toolbar 
align: center
---
```
:::
::::

The normal digitalisation toolbar offers all the necessary functions to do digitalisation. However, for everything that goes above just creating new features and deleting features, the advanced digitalisation toolbar is needed. 
The advanced digitalisation toolbar allows you to move features, delete parts of features and much more. All functions are listed in the two tables below.

:::{dropdown} Digitalisation Toolbar
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
|![](/fig/mActionMoveFeature-1.png)![](/fig/mActionMoveFeatureLine.png)![Alt text](/fig/mActionMoveFeaturePoint.png)|Move Feature(s)|![Alt text]/fig/(mActionMoveFeatureCopy.png) ![Alt text](/fig/mActionMoveFeatureCopyLine.png)![Alt text](/fig/mActionMoveFeatureCopyPoint-2.png)|Copy and Move Feature(s)|
|![Alt text](/fig/mActionRotateFeature.png)|Rotate Feature(s)|![Alt text](/fig/mActionSimplify.png)|Simplify Feature|
|![Alt text](/fig/mActionScaleFeature.png)|Scale Feature||
|![Alt text](/fig/mActionCapturePolygon.png)|Add Ring|![Alt text](/fig/mActionAddPart.png)|Add Part|
|![Alt text](mActionFillRing.png)|Fill Ring|![Alt text](/fig/mActionReverseLine.png)|Swap direction|
|![Alt text](/fig/mActionDeleteRing-1.png)|Delete Ring|![Alt text](/fig/mActionDeletePart.png)|Delete Part|
|![Alt text](/fig/mActionOffsetCurve.png)|Offset Curve|![Alt text](/fig/mActionReshape.png)|Reshape Features|
|![Alt text](/fig/mActionSplitParts.png)|Split Parts|![Alt text](/fig/mActionSplitFeatures.png)|Split Features|
|![Alt text](/fig/mActionMergeFeatureAttributes.png)|Merge Attributes of Selected Features|![Alt text](/fig/mActionMergeFeatures.png)|Merge Selected Features|
|![Alt text](/fig/mActionRotatePointSymbols.png)|Rotate Point Symbols|![Alt text](/fig/mActionOffsetPointSymbols.png)|Offset Point Symbols|
|![Alt text](/fig/mActionTrimExtend.png)|Trim or Extend Feature|||
:::


 ## Digital data creation

To digitise data for a new dataset you always have to start with creating the dataset before filling it with digitised data.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Create_new_vector_data.mp4"></video>

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
---
```

### Creation of point data

Click on the following numbers bottons as seen in the picture below. Number **1** will switch to edit mode, number **2** is to create a new entry point, number **3** is to move or copy point and number **4** is to delete entry point.

![](/fig/New_point_creation_data.png)

* Create  a  new  point:  Use  the  "Create  a  new  entity"  button  >  left-click  on  the  map > enter the attributes > click OK > a new point is created.

![](/fig/Naming_of_point_created.png)

You can name the point as you want and enter any number in the ID and click ok. The new point feature has been created and named which can be easily seen on the map.


#### Creation of line data

The  method  is  similar  to  digitising  a  point  (see  above).This can be possible when you have firstly created a new line shapefiles layer. Remember to change the geometry type into lines because we are creating lines data now.

![](/fig/Creation_of_line_data.png)


See video of line data creation

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Line_data_creation.mp4"></video>


```{Note} 
Try:
```
Use  the  "Create  new  line"  button  and  click  several  times  on  the  map  (left  button)  to  draw  the  different parts of your line. When this is done, right-click to complete your line and access the Attributes window.> Complete the attributes and click OK

#### Creation of polygon data

The method is similar to digitising a point or a line (see above).  Only  the  fourth  icon  changes  slightly:  this  one  corresponds to "Create a new polygon"

![](/fig/polygon_data_creation.png)

```{Tip}
Caution:
```

Please remember to firstly created a new polygon shapefiles layer so thatthe icon to create a polygon can be active and ensure you change the geometry type into polygons because we are creating polygon data now.


See video of polygon data creation

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/polygon_data_creation.mp4"></video>


### Creation of new shapefile data

+ Go to Layer, Create Layer, New Shapefile Layer in the top menu.
+ In the New Shapefile dialog, specify the name and location for the new shapefile.
+ Select the geometry type for the shapefile from the Type dropdown (e.g. Point, line, Polygon).
+ Click the OK button to create the shapefile

![](/fig/New_shapefile_layer_creation.png)

* The new shapefile layer

![](/fig/New_shapefile_layer_naming.png)

## Create Layer

Now add some layers for drawing. Click layer in the menu bar, select create layer and select **new spatialite layer** or select **new shapefile layer** if you have to digitize a single feature like some places or roads or buildings. We are choosing new spatialite layer because we want to draw more than one feature in single file and it is easy to transfer this file.

**Next**

Click ‘…’ browse button and save your database. Give name to your layer, select type of layer and specify attributes and their type such as text or numerals and click add attributes to the list and click OK. Specify CRS of the layer same as the CRS of Raster data.

 ![](/fig/New_spatialite_layer.png)


## Digital data editing

Select the layer in the Layers panel and click on Toggle Editing under Layer. Alternatively, you can right-click on a layer in the Layers panel and choose Toggle Editing from the context menu. Multiple layers can be edited at a time. The layer currently being edited is the one selected in the Layers panel.

![](/fig/Toggle_editingbox.png)


### Feature attribute selection and editing

The first group of tools in the Attributes toolbar allows us to select features on the map using the mouse. The following screenshot shows the Select Feature(s) tool. We can select a single feature by clicking on it, or select multiple features by drawing a rectangle.

![](/fig/Select_Feature(s)_tool.png)

* How to export selected features

![](/fig/Export_selected_features.png)


## Editing data - Data creation and deletion

* To create or delete a field in your attribute table you need to be in edit mode, click on the Switch to edit mode button.

![](/fig/Switch_to_edit_mode_of_attribute_table.png)


* To add new data field; click on symbol circle 1 and to delete a data field; click on symbol circle 2

![](/fig/add_delete_data_in_attribute_table.png)


## Attributes table editing

The attribute table displays information on features of a selected layer. Features in the table can be searched, selected, moved or even edited. It is also possible to right-click on the layer and choose openTable Open Attribute Table from the drop-down menu, or to click on the openTable Open Attribute Table button in the Attributes toolbar. 

If you prefer shortcuts, **F6** will open the attribute table. **Shift+F6** will open the attribute table filtered to selected features and **Ctrl+F6** will open the attribute table filtered to visible features.

![](/fig/Opening_attribute_table.png)

* Right click the layer in the Layers Panel then click the Open Attribute Table menu option. Click the Toggle Editing Mode button. Click the New Field button. Input the field's Name, Type, and Length, then click the OK button.

![](/fig/New_fieldcolumn_creation_in_attribute_table.png)

![](/fig/Input_newfield_and_to_save_editing.png)


## Digitization Errors in QGIS

Positional errors are inevitable when data are manually digitized. The most common examples include undershooting and overshooting.  When your coordinates do not connect as they should, and overshooting, when the lines go past where they should. Often these errors are not visible unless you zoom in quite a bit on the coordinates. Setting a fuzzy tolerance (snapping tolerance) is used to reduce undershoots and overshoots. The snapping tolerance is the minimum tolerated distance between nodes, lines and/or vertices.

![](/fig/Digitization_Errors.PNG)


