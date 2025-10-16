::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Digitisation

Digitisation is the process of converting geographic data from maps or images into a digital form commonly 
represented as vector data.
Proficiency in digitisation stands as a cornerstone for GIS specialists. It empowers them to convert spatial 
information into a digital format, facilitating more efficient data manipulation compared to traditional methods 
of interpreting images or paper maps. 

:::{admonition} Digitisation in humanitarian work
:class: tip

If you want to know how community mapping and digitisation can help improve the resilience of communities and facilitate humanitarian work, take a look at Paul Knight's blogpost [“This is the first time this community is on a map…” — Digital Community Mapping in Nigeria](https://medium.com/digital-and-innovation-at-british-red-cross/first-time-this-community-has-been-on-a-map-nigeria-f592906b7be1)

:::

```{figure} /fig/en_digitisation_concept.png
---
width: 900px
align: center
name: en_digitisation_concept
---
The concept of digitisation within GIS (Source: HeiGIT).
```

##  Digitising in QGIS

In QGIS,digitisation involves tracing features such as points, lines, or polygons directly on the map canvas to 
represent geographic elements like buildings, roads, or land parcels. Additionally, you can assign attributes to each 
feature during digitization, enabling further analysis and integration with other geospatial data. This digitized data 
becomes a valuable asset for spatial analysis and mapping.

:::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Real world Scenario 1/3__
^^^
There has been a flood in a village following heavy rains.  
To assess the needs of the household and the impact on the 
infrastructure, you are tasked to make an overview map of the region and mark the flood impacted buildings and 
roads. However, there are no datasets with the buildings or roads available. For the map, you will have to 
create two new layers with the road network and the buildings. However, there is recent satellite imagery available. 
With these images, you can create vector layers representing the key infrastructure, such as buildings and roads. 
Once you have created the layers, you can create a preliminary overview map of the village. 
This map will be given out to community members and voluntaries on the ground to map out the damaged infrastructure.
In a next step, the information collected by the ground team can be used to enrich the data and create an flood 
impact assessment. 
To create the map, you will need to create new vector layers. 

<!--ADD PICTURES -->
:::


### Digitisation toolbars

```{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
align: left
name: Activate digitising Toolbar 
---
The Digitisation Toolbar in QGIS 3.36.
```

Digitising is done with the `Digitizing Toolbar` and on the map canvas. 
First, you need to check if the `Digitizing Toolbar` is activated. To do that 
* Click on the `View` tab in the menu bar and click `Toolbars`. Check if the `Digitizing` and `Advanced Digitizing` toolbar is activated.

First, you need to check if the `Digitizing Toolbox` is activated. To do that 
1.  Click on the `View` tab in the menu bar and click `Toolbars`. Check if the `Digitizing` and `Advanced Digitizing` toolbox is activated.

2. A tool box like this should appear on top of the QGIS interface

<br>

<br>  

<br>  

The digitisation toolbar offers the basic tools to create, save, and edit features. However, for everything that 
goes above just creating new features and deleting features, the Advanced Digitization toolbar is needed (see {numref}`digitising_toolbar`). 
The Advanced Digitization toolbar allows you to move features, delete parts of features, and much more. All 
functions are listed in the two tables below.

```{figure} /fig/Toolbox.png
---
width: 700 px
name: digitising_toolbar
align: center
---
Digitizing Toolbar in QGIS 3.36
```

:::{dropdown} Digitisation Toolbar
| Tool | Purpose | Tool | Purpose |
|---|---|-----|---|
| ![](/fig/mActionAllEdits.png) | Access to save, rollback or cancel changes in all or selected layers simultaneously | ![](/fig/mActionToggleEditing.png) | Turn on or off edit status of selected layer(s) based on the active layer status |
| ![](/fig/mActionSaveEdits.png) |Save edits   | |
| ![](/fig/mActionDigitizeWithSegment.png) | Digitise using straight segments | ![](/fig/mActionDigitizeWithCurve.png) | Digitize using curve lines |
| ![](/fig/mActionStreamingDigitize.png) | Enable freehand digitising|![](/fig/mActionDigitizeShape.png) |Digitise polygon of regular shape  |
| ![](/fig/mActionNewTableRow.png)  | Add new record   | ![](/fig/mActionCapturePoint.png) | Add Feature: Capture Point |
| ![](/fig/mActionCaptureLine.png) | Add Feature: Capture Line   | ![](/fig/mActionCapturePolygon.png) | Add Feature: Capture Polygon |
| ![](/fig/mActionVertexTool.png) | Vertex Tool (All Layers) | ![](/fig/mActionVertexToolActiveLayer.png) |Vertex Tool (Current Layer) |
| ![](/fig/checkbox.png) | Set whether the vertex editor panel should auto-open | ![](/fig/mActionMultiEdit.png) | Modify the attributes of all selected features simultaneously |
| ![](/fig/mActionDeleteSelectedFeatures.png) | Delete selected features from the active layer | ![](/fig/mActionEditCut.png) | Cut features from the active layer |
| ![](/fig/mActionCopySelected.png) | Copy selected features from the active layer | ![](/fig/mActionEditPaste.png) | Paste features into the active layer |
| ![](/fig/mActionUndo.png) | Undo changes in the active layer | ![](/fig/mActionRedo.png) | Redo changes in active layer |

:::

For more complex digitisation procedures, you will use the advanced digitisation toolbar. However, for this chapter, we will focus on the normal digitisation toolbar. 

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


## Creating new datasets

To digitise new data, you always have to start with creating the dataset before filling it with digitised data. 
Keep in mind that one layer can only contain one type of geometry: either points, lines, or polygons. When you 
create a dataset, you will have to choose the type of geometry. Additionally, you can add further columns with 
attributes to add more data to the data table. 

:::{admonition} Now it's your turn!
:class: note

Think of a spatial dataset you could need in your humanitarian operations. What kind of additional information is 
useful? How would you collect it? This could range from type of road, crops planted, type of vegetation or social 
indicators. You can discuss in groups and write it down on paper or add it to a digital whiteboard. 

:::


:::{dropdown} Video: How to create a new dataset

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
    * Click on ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
8. Click `OK` to create the new data

<!---   ```{Note} 
    The number of options depends on the data format the layer will have. GeoPackage, for example, offers far more options than the Shapefile format.
    ```
    -->

```{figure} /fig/New_GeoPackage_Layer.png
---
width: 500px
name: new_gpgk_layer
align: center
---
The Layer Creation window in QGIS 3.36.
```

<!--ADD: add an explanation of the Layer creation window?-->

```{attention} 
An important concept to understand before starting to add data to datasets is, that, whenever you make changes 
to a dataset other than styling, you have to put it in editing mode. This is done by selecting the layer and 
clicking on ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Now, the buttons for many functions of the 
digitisation toolbar are clickable. 
After you are done manipulating the layer click on ![](/fig/mActionSaveEdits.png) `Save Layer Edits` to save 
your edits. 
```

Once you have set up the new layer, you can start adding geometrical features. The process for the three geometric 
types is basically the same: 

### Creating new data entries

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
5.	Once you are done with digitisation ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

:::{dropdown} Video: How to create point data
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>
:::

```{figure} /fig/point_creation.png 
---
width: 750 px
name: point_creation
align: center
---
Point creation.
```

 <!--REPLACE IMAGE showing a point creation window with more attributes and not just ID and type to show the 
information you can add at this stage-->



::::{admonition} Getting coordinates from google maps
:class: tip

Sometimes, the easiest way to get the coordinates for a location, such as the office of a national Red Cross or Red Crescent branch or simply ofa house, is to use google maps. In Google Maps, you can right click on any location to get the coordinates (in degrees). 

:::{figure} /fig/en_google_maps_rightclick_coords.png
---
width: 250 px
align: right
name: en_google_maps_rightclick_coords
---
:::

1. In Google Maps, locate the point you wish to add to your QGIS project.
2. Right click on the point and select the coordinates. They will be copied to your clipboard automatically.
3. Navigate to your QGIS project and paste the coordinates into the search bar in the bottom left corner of the QGIS window.
4. Select `Go to [Your coordinates] (EPSG 4326: WGS 84)`. 
5. The coordinate point will flash red on the map canvas. 
::::




```{admonition} Now it's your turn!
 
Try digitising the RCRC branches in your country by following the steps below.

```
1. Create a new point dataset.
2. Add a [basemap](/content/Modul_2/en_qgis_basemap.md) (OSM or Bing Aerial, for example)
3. Search the RCRC branches in your country on google maps.
4. Once you have located the branches, right-click on a branch in google maps and click on the coordinates. The coordinates will be copied to your clipboard
5. Paste the coordinates into the search bar on the bottom left of the QGIS window. Select navigate to coordinates. The location will be marked by a red dot

6. Enable the editing mode ![](/fig/mActionToggleEditing.png) in in your new layer.
7. Click on ![](/fig/mActionCapturePoint.png)
8. Add the point feature at the location that was indicated.
9. Add the name of the RCRC branch.
10. Click `Ok`. 
11. Click on ![](/fig/mActionSaveEdits.png) to save your edits.
12. Click on ![](/fig/mActionToggleEditing.png) to exit the editing mode. 



### Creating line and polygon layers

The process of creating line or polygon layers is essentially the same as creating point data. The main difference is 
that instead of only adding one point, line and polygon geometries require several points (vertices). Each point you 
add is a vertex between two lines. In QGIS, you create lines and polygons by setting one point, and then another point 
connected to the previously added point. To finish adding the feature use the <kbd>Right mouse button</kbd>. 

```{attention} 
Remember to change the geometry type into lines if you want to create a new line layer.
```

::::{tab-set}

:::{tab-item} Creating line data

Creating line data works in the same way as creating point data (see above). First, you must create a new line 
layer or use an existing one. 

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

:::

:::{tab-item} Creating polygon data

The creation of polygon layers works in the same way as for point and line data.

1.	Select the polygon layer you want to add data to in the Layer panel.
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). Now, the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePolygon.png). 
4.	To digitise polygon features, left-click around the area you want do digitize. When you are done, right-click on the last point of the area to finish the feature.
5.	A window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitisation ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click on ![](/fig/mActionToggleEditing.png) `Toggle Editing` again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_feature.mp4"></video>

:::

::::

:::{card} 
:class-card: sd-text-justify sd-rounded-3 sd-border-2
__Real World Scenario 2/3__
^^^

The first thing you do is locate the village using GPS-coordinates that you enter in the bottom right corner of 
the QGIS window. 
Thankfully, the process of digitising is relatively easy since there is a recent satellite image provided by 
Microsoft Bing. You can load the satellite image using the __QuickMapServices__ and searching and adding the 
`Bing Aerial` Basemap. 
You can see the buildings and roads on the satellite image. The next step will be to create new layers: one for 
the roads and one for the buildings.

:::

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

:::{tab-item} Modifying geometries

1.	Select the line layer you want to add data to in the Layer panel.
2.	Navigate to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). 
3.	Click on ![](/fig/mActionVertexToolActiveLayer.png).
4.	Now you can now move every vertex (corner) of a feature. Click on the vertex/corner you want to move and 
then click on the location where you want to move the vertex to.
5.	Once you are done with editing click on ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click on ![](/fig/mActionToggleEditing.png) again to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_move_vertices.mp4"></video>

:::

:::{tab-item} Adding rings to polygon features

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

Sometimes, you will have to edit the values in the columns of the attribute table. For example, the name of an administrative district is written incorrectly or differently, or a value has not been entered correctly. To do this, you will have to:

::::{margin}

```{tip}
You can open the attribute table of the selected layer by pressing <kbd>F6</kbd>. 
```
::::

1. Open the [attribute table](/content/Module_2/en_qgis_attribute_table.md)
2. Click on ![](/fig/mActionToggleEditing.png) to enter into the editing mode.
3. Choose the field that you want to edit. 
4. Enter the corrected value.
5. Click on ![](/fig/mActionSaveEdits.png) to save your edits.
6. Click on ![](/fig/mActionToggleEditing.png) again to exit the editing mode. 

This process is called __"Data cleaning"__ and is important when performing data analysis or manipulating data 
in any way. While collecting or digitising data, it is easy to make small mistakes, such as a wrong value, wrong 
value type, or a spelling mistake. When performing analyses, it is therefore important to investigate the 
attribute table for inconsistencies or errors. If these errors are not cleaned, the results will be incorrect 
and you might take the wrong conclusions!

:::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Real world Scenario 3/3__
^^^

With the new layers, you are ready to trace the buildings and roads in the new layers. 
You already have some knowledge about the condition of the roads (e.g., the road surface, quality, and if it is 
flooded) and the condition of the houses (e.g., if it is affected by a flood, if it has multiple stories, ...). 
This is useful information that can be stored in the additional attributes in the data table. 

```{figure} /fig/Building_damage_assessement_bangladesh.png
---
name: Building_damage_assessement
width: 750 px 
---
Building Damage Assessment in Paikgachha Upazila, Khulna District, Khulna Division, Bangladesh as of 4 June 2024 (Source: [Int'l Charter, UNOSAT](https://reliefweb.int/map/bangladesh/building-damage-assessment-paikgachha-upazila-khulna-district-khulna-division-bangladesh-4-june-2024-imagery-analysis-4-june-2024-published-7-june-2024-v1))
```

:::

## Spatial Digitisation Errors in QGIS

The accuracy of geodata is crucial for spatial analysis. Positional errors are inevitable when data are manually 
digitised. The most common examples include undershooting and overshooting.  When your coordinates do not 
connect as they should, and overshooting, when the lines go past where they should. Often these errors are not 
visible unless you zoom in quite a bit on the coordinates. Setting a fuzzy tolerance (snapping tolerance) is 
used to reduce undershoots and overshoots. The snapping tolerance is the minimum tolerated distance between 
nodes, lines and/or vertices.

```{figure} /fig/Digitization_Errors.PNG
---
width: 500px
align: center
name: Digitization_Errors
---
Digitising Errors (Source: SpatialPost).
```

## Self-Assessment Questions

::::{admonition} Recapitulate your knowledge
:class: note 

1. __What is digitisation in GIS? Why is converting features from maps or images into vector form useful?__

:::{dropdown} Answer
Digitisation (or “digitization”) in GIS is the process of tracing or capturing geographic features (points, lines, polygons) from maps, images (such as satellite or aerial imagery, scanned maps) __or reports__ and converting them into vector data.  
It is useful because it let's us perform spatial analyses and gain insights about the captured phenomenon in space. Furthermore, we can combine it with other spatial data and display it on informative maps.
:::

2. __How do you create a new vector dataset?__

:::{dropdown} Answer
1. In the top bar, navigate to the `Layer` menu → `Create Layer` → `New GeoPackage Layer` or `New Shapefile Layer`
2. Specify the layer properties:
    - Specify the file path and name
    - **Encoding**: UTF-8 (allows for special characters)
    - **Geometry type**: point, line, polygon (one layer supports only one geometry type)
    - **Coordinate Reference System (CRS)**
    - Define the __attribute fields__ (columns) that you want in the layer's attribute table.
3. Click `Ok` to create the create the layer. 
:::


3. __Imagine you’re digitising flood‑affected buildings from an aerial image. What attribute fields might you include, and what level of detail or accuracy would you try to maintain?__ 

:::{dropdown} Answer 
Which attributes you wish to digitise always depends on the goal of your mapping effort (e.g. emergency response, damage assessment, or planning) and if you are on the ground or rely on satellite imagery. 
__Potential attribute fields__: 
    - __Building type/usage__: e.g. residential, commercial, industrial, public
    - __Number of stories/floors__
    - __Roof material__
    - __Wall material__
    - __Damage status__: e.g. "no damage", "minor damage", "severe damage", "collapsed"
    - __Flood depth or water exposure__
    - __Date of assessment__
    - __Confidence/quality__
    - __Address__
    - ...
:::


::::

