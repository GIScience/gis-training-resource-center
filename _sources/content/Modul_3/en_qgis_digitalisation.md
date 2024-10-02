# Digitisation



__🔙[Back to Homepage](/content/intro.md)__


Digitisation is the process of converting geographic data from maps or images into a digital form commonly 
represented as vector data.
Proficiency in digitisation stands as a cornerstone for GIS specialists. It empowers them to convert spatial 
information into a digital format, facilitating more efficient data manipulation compared to traditional methods 
of interpreting images or paper maps. 


```{figure} /fig/Digitizsation_concept.drawio.svg
---
width: 900px
align: center
name: Digitisation with GIS Concept
---
Digitisation with GIS Concept. Source: HeiGIT
```

##  Digitising in QGIS

In QGIS, digitization is the process of creating digital vector layers from scanned maps or aerial images. It 
involves tracing features such as points, lines, or polygons directly on the map canvas to represent geographic 
elements like buildings, roads, or land parcels. Additionally, you can assign attributes to each feature during 
digitization, enabling further analysis and integration with other geospatial data. This digitized data becomes 
a valuable asset for spatial analysis and mapping.

:::{card}
### Real world Scenario

There is a flood relief operation in a village. To assess the needs of the household and the impact on the 
infrastructure, you are tasked to make an overview map of the region and mark the flood impacted buildings and 
roads. However, there are no datasets with the buildings or roads available. For the map, you will have to 
create two new layers with the road network and the buildings. 

:::


### Digitisation toolbars

Digitising is done with the `Digitizing Toolbar` and on the map canvas. 
First, you need to check if the `Digitizing Toolbar` is activated. To do that 
* Click on the `View` tab in the menu bar and click `Toolbars`. Check if the `Digitizing` and `Advanced Digitizing` toolbar is activated.

::::{grid} 2
:::{grid-item-card}  Activate `Digitizing Toolbox`
First, you need to check if the `Digitizing Toolbox` is activated. To do that 
1.  Click on the `View` tab in the menu bar and click `Toolbars`. Check if the `Digitizing` and `Advanced Digitizing` toolbox is activated.

2. A tool box like this should appear on top of the QGIS interface
 
 ![](/fig/Toolbox.png)
 
:::
:::{grid-item-card} How to: 

```{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
name: 
align: center
name: Activate digitising Toolbar 
---
The Digitisation Toolbar in QGIS 3.36.
```
:::
::::

The digitisation toolbar offers the basic tools to create, save, and edit features. However, for everything that 
goes above just creating new features and deleting features, the Advanced Digitalization toolbar is needed. 
The Advanced Digitalization toolbar allows you to move features, delete parts of features, and much more. All 
functions are listed in the two tables below.

:::{dropdown} Digitalization Toolbar
|Tool|Purpose|Tool|Purpose|
|---|---|-----|---|
|![](/fig/mActionAllEdits.png) |Access to save, rollback or cancel changes in all or selected layers simultaneously | ![](/fig/mActionToggleEditing.png)|Turn on or off edit status of selected layer(s) based on the active layer status|
|![](/fig/mActionSaveEdits.png) |Save edits   | |
|![](/fig/mActionDigitizeWithSegment.png) |Digitise using straight segments |![](/fig/mActionDigitizeWithCurve.png)|Digitize using curve lines|
|![](/fig/mActionStreamingDigitize.png)|Enable freehand digitising|![](/fig/mActionDigitizeShape.png) |Digitise polygon of regular shape  |
|![](/fig/mActionNewTableRow.png)  |Add new record   | ![](/fig/mActionCapturePoint.png)| Add Feature: Capture Point |
|![](/fig/mActionCaptureLine.png) |Add Feature: Capture Line   |![](/fig/mActionCapturePolygon.png)|Add Feature: Capture Polygon  |
|![](/fig/mActionVertexTool.png) |Vertex Tool (All Layers) | ![](/fig/mActionVertexToolActiveLayer.png)|Vertex Tool (Current Layer)  |
|![](/fig/checkbox.png)|Set whether the vertex editor panel should auto-open|![](/fig/mActionMultiEdit.png)|Modify the attributes of all selected features simultaneously |
|![](/fig/mActionDeleteSelectedFeatures.png) |Delete selected features from the active layer   |![](/fig/mActionEditCut.png) |Cut features from the active layer  |
|![](/fig/mActionCopySelected.png) |Copy selected features from the active layer   |![](/fig/mActionEditPaste.png) |Paste features into the active layer  |
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


:::{card} 
### Real World Scenario

The first thing you do is locate the village using GPS-coordinates that you enter in the bottom right corner of 
the QGIS window. 
Thankfully, the process of digitising is relatively easy since there is a recent satellite image provided by 
Microsoft Bing. You can load the satellite image using the __QuickMapServices__ and searching and adding the 
`Bing Aerial` Basemap. 
You can see the buildings and roads on the satellite image. The next step will be to create new layers: one for 
the roads and one for the buildings.

:::

## Creating new datasets

To digitise new data, you always have to start with creating the dataset before filling it with digitised data. 
Keep in mind that one layer can only contain one type of geometry: either points, lines, or polygons. When you 
create a dataset, you will have to choose the type of geometry. Additionally, you can add further columns with 
attributes to add more data to the data table. Further information can be...
<!--ADD meaningful example for IM-->

:::{card} 
### Video: How to create a new layer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_create_layer.mp4"></video>
:::

1. `Layer` --> `Create Layer` -> `New GeoPackage Layer` or `New Shapefile Layer`
2. Click on ![](/fig/Three_points.png) next to the `file name` input field and navigate to the folder where you want to save the dataset.
3. `File encoding`: Make sure this is set to UTF-8
4. `Geometry type`: Select the type of feature you want to digitise e.g. points or lines.
5. Under `Additional dimension` you should always make sure that you check `None`. Except if there is the possibility to collect the Z-values (elevation) as well. But this is mostly not the case.
6. CRS dropdown: Select the EPSG/CRS you want to set for the new layer. By default, the QGIS selects the project CRS. If you want to change the CRS click on ![](/fig/mIconProjectionEnabled.png).
7. Under `New Field` you can add columns to the new layer. Here you can set up what other type of data you want to collect in this dataset.
    * `Type`: Select the data type the column will have e.g. `Text`, `Whole number`, `Decimal Number`, `Date`.
    ```{Note} 
    The number of options depends on the data format the layer will have. GeoPackage, for example, offers far more options than the Shapefile format.
    ```
    * Click on ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
8. Click `OK` to create the new data

```{figure} /fig/New_GeoPackage_Layer.png
---
width: 500px
name: Digitalisation Toolbar 
align: center
name: Digitalization Toolbar 
---
The Layer Creation window in QGIS 3.36.
```

```{attention} 
An important concept to understand before starting to add data to datasets is, that, whenever you make changes 
to a dataset other than styling, you have to put it in editing mode. This is done by selecting the layer and 
clicking on ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Now, the buttons for many functions of the 
digitisation toolbar are clickable. 
After you are done manipulating the layer click on ![](/fig/mActionSaveEdits.png) `Save Layer Edits` to save 
your edits. 
```

Once you have set up the new layer, you can start adding geofeatures. The process for the three geometric types 
is basically the same: 

### Creating new data entries

:::{card}

### Real World Scenario

With the new layers, you are ready to trace the buildings and roads in the new layers. 
You already have some knowledge about the condition of the roads (e.g., the road surface, quality, and if it is 
flooded) and the condition of the houses (e.g., if it is affected by a flood, if it has multiple stories, ...). 
This is useful information that can be stored in the additional attributes in the data table. 

<!--INSERT: Picture of this step-->

:::

1. Select the layer you want to add data to in the Layer panel.
2. Go to the digitisation toolbar and click on ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Make sure 
the the layer is in the editing mode. If not, click on the ![](/fig/mActionToggleEditing.png) icon in the 
digitisation toolbar. 

### Creating point data

1.	Select the point layer you want to add data to in the Layer panel.
2.	Go to the digitisation toolbar and click on ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Make sure 
the the layer is in the editing mode. If not, click on the ![](/fig/mActionToggleEditing.png) icon in the 
digitisation toolbar. 
3.	Click on ![](/fig/mActionCapturePoint.png). 
4.	Left-click on the feature you want to digitise.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the 
information about this feature to the different columns, based on the attribute table of the layer.
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

<!--REPLACE IMAGE showing a point creation window with more attributes and not just ID and type to show the 
information you can add at this stage-->

#### Creating line data

Creating line data works in the same way as creating point data (see above). First, you must create a new line 
layer or use an existing one. 

```{attention} 
If you create a new line layer, remember to change the geometry type into lines.
```
1.	Select the line layer you want to add data to in the Layer panel
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). Now, the layer is in the 
editing mode.
3.	Click on ![](/fig/mActionCaptureLine.png). 
4.	To digitise line features, click along the line. When you are done, right-click on the last point of the 
line to finish the feature.
5.	A window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this 
feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitisation, click on ![](/fig/mActionSaveEdits.png) `Save Layer Edits` to save your 
edits.
7.	Click on ![](/fig/mActionToggleEditing.png) `Toggle Editing` again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>


#### Creating polygon data

The creation of polygon layers works in the same way as for point and line data.

1.	Select the polygon layer you want to add data to in the Layer panel.
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). Now, the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePolygon.png). 
4.	To digitise polygon features, left-click around the area you want do digitize. When you are done, right-click on the last point of the area to finish the feature.
5.	A window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitisation ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click on ![](/fig/mActionToggleEditing.png) `Toggle Editing` again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_feature.mp4"></video>


## Editing the Data

In some cases, you might want to modify or correct vector data because of inaccuracies or changes. Editing 
vector data is done with digitisation toolbar. In QGIS, you can edit both the geometries and the values in the 
attribute table. 

### Editing Geometries

For all cases:

1. Select the layer you want to edit.
2. Click on ![](/fig/mActionToggleEditing.png) to activate the editing mode.
3. Do your changes.
4. Save your edit by clicking on ![](/fig/mActionSaveEdits.png).
5. Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

```{Tip} 
You can use the ![](/fig/mActionUndo.png) & ![](/fig/mActionRedo.png) buttons to reverse changes easily.

Note that this is only possible __before__ you save the changes.
```

::::{tab-set}
:::{tab-item} Deleting features

1.	Select the layer you want to modify.
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png) `Toggle Editing`. 
3.	Click on ![](/fig/mActionSelectRectangle.png) and select the feature you want to delete (see the [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html#manual-selection)).
4.	Once you have selected the features, click on ![](/fig/mActionDeleteSelectedFeatures.png) to delete the feature.
5.	Once you are done with editing, click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

```{note}
Keep in mind that once you save the changes ![](/fig/mActionSaveEdits.png), you can no longer undo or recover the deleted features. The changes permanently change the datafile in your folder. 
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/delet_feature_geometry.mp4"></video>

:::

:::{tab-item} Moving features

There are multiple methods to move features. Here we show the method that works the same for point, line, and polygon features.
To do this, you need the Advanced Digitisation Toolbox.

1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![](/fig/mActionMoveFeaturePoint.png) and click on the feature you want to move. Then, click on the location where you want to move the feature.
4.	Once you are done with editing, click on ![](/fig/mActionSaveEdits.png) to save your edits.
5.	Click on ![](/fig/mActionToggleEditing.png) again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/move_feature_geometry.mp4"></video>

:::

:::{tab-item} __Modifying geometries__

1.	Select the line layer you want to add data to in the Layer panel.
2.	Navigate to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![](/fig/mActionVertexToolActiveLayer.png).
4.	Now you can now move every vertex (corner) of a feature. Click on the vertex/corner you want to move and 
then click on the location where you want to move the vertex to.
5.	Once you are done with editing click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click on ![](/fig/mActionToggleEditing.png) again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_move_vertices.mp4"></video>

:::

:::{tab-item} __Adding a ring to a polygon feature__

A ring in QGIS is a part inside a polygon that is not part of the polygon. Image a polygon representing a lake. 
The ring is an island in the lake. For a better understanding, watch the video below.

1.	Select the line layer you want to add data to in the Layer panel.
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![add ring icon](/fig/mActionAddRing.png).
4.	Create a ring by clicking the area you want to exclude. Right-click to close the ring.
5.	Once you are done with editing, click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click on ![](/fig/mActionToggleEditing.png) again to end the editing mode.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_ring.mp4"></video>

:::

::::

### Editing the attribute values

Sometimes, you will have to edit the values in the columns of the attribute table. 


## Digitisation Errors in QGIS

The accuracy of geodata is crucial for spatial analysis. Positional errors are inevitable when data are manually 
digitised. The most common examples include undershooting and overshooting.  When your coordinates do not 
connect as they should, and overshooting, when the lines go past where they should. Often these errors are not 
visible unless you zoom in quite a bit on the coordinates. Setting a fuzzy tolerance (snapping tolerance) is 
used to reduce undershoots and overshoots. The snapping tolerance is the minimum tolerated distance between 
nodes, lines and/or vertices.

```{figure} /fig/Digitization_Errors.PNG
---
width: 500px
name: 
align: center
name: Digitizing Errors in QGIS
---
Digitising Errors in QGIS. Source: SpatialPost.
```
