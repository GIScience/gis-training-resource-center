# Digitisation


__🔙[Back to Homepage](/content/intro.md)__

Digitisation is the process of converting geographic data from maps or images into digital form commonly represented as vector data.
During this procedure, spatial information from maps or images is traced, forming points, polylines, or polygons. 
To digitize data for a new dataset you always have to start with creating the dataset before filling it with digitized data.

## The Digitisation Toolbar in QGIS

![](/fig/Digitizing_Toolbar.png)

- Digitisation in QGIS is done primarily with the __digitisation toolbar__. To activate the toolbar, navigate to `View` -> `Toolbars` -> `Digitisation Toolbar`.

:::{figure} /fig/en_qgis_3.40_activate_digitisation_toolbar_wiki.png
---
name: en_qgis_3.40_activate_digitisation_toolbar_wiki
width: 550 px
---
:::

## Creating a new layer

1. In the top bar, navigate to `Layer` -> `Create Layer` -> `New GeoPackage Layer` or `New Shapefile Layer`.
2. A new window will open. Here you can specify the layer properties.
3. Under `Database`, click on the three points ![](/fig/Three_points.png) and navigate to the folder where you want to save the new dataset.
4. *shapefile specific*: Set the file encoding to `UTF-8`.
5. `Geometry type`: Select the type of geometry you want to digitise: points, lines or polygons.
::::{margin}
:::{tip}
If you plan to perform distance-based calculation with the new dataset, make sure to use a __metric__ CRS. The units of measurements for the layer will be in meters and not degrees (see [Metric and Geographic Coordinate Reference Systems](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_projections.html#metric-and-geographic-coordinate-reference-systems))
:::
::::
6. Select the CRS (Coordinate Reference System) you want to use for the new layer. By default it is set to the project CRS. If you want to change the CRS click on ![](/fig/mIconProjectionEnabled.png).
7. Under `New Field`, you can add columns to the new layer. Here you can define what kind of information/data will be available in the attribute table for each feature.
    - `Name`: Give the new column a name representing the information you want to store in it. 
    - `Type`: Here you can select the data type for the new column. For example, `Text` will add a new column with string (text) data. For numerical data you can choose `Whole number` or `Decimal number`. 
    - `Maximum Length` defines the maximum number of characters the field can have. This is relevant for the length of text or the precision of decimal numbers. For example, you might want to set a high maximum length for text fields if you want long street names such as "Martin Luther King Jr. Boulevard" (34 characters). 
    * Click on ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`. 
8. Once you are done adding the fields, click `OK`.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_create_layer.mp4"></video>

## Adding geometries to a layer

### Creating point data

1.	Select the point layer you want to add data to in the Layer panel
2.	Go to the digitisation toolbar and click on![](/fig/mActionToggleEditing.png). Now the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePoint.png). 
4.	Left-click on the feature you want to digitise.
5.	Once you click, a window named `[Your Layer Name]- Feature Attribute` will appear. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.

:::{figure} /fig/point_creation.png 
---
width: 700px
name: Point creation
align: center
---
:::
% Add another picture with more columns

5.	Once you are done with digitisation ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>


### Creating line data

The  method  is  similar  to  digitising  a  point  (see  above). First you have to create a new line layer or use an existing one. 

:::{attention} 
If you create a new line layer remember to change the geometry type into lines because we are creating lines data now.
:::

1. In the layers panel, select the line layer to which you want to add data.
2. In the digitisation toolbar, click on ![](/fig/mActionToggleEditing.png). Now the layer is in editing mode. 
3. Click on ![](/fig/mActionCaptureLine.png). 
4. Create the line on the map canvas by <kbd>left-clicking</kbd> to add vertices. When you are done, right-click on the last point to finish editing the geometry.
5. A new window titled `[Your Layer Name]- Feature Attribute` will appear. Here you can fill in the column information for the feature.  
6. Once you are done with digitisation, click on ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click on the ![](/fig/mActionToggleEditing.png) icon again to end the editing mode.


<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>

### Creating polygon data 

1. In the layers panel, select the polygon layer to which you want to add data.
2. Click on ![](/fig/mActionToggleEditing.png) to start the editing mode.
3. Click on `Capture Polygon`![](/fig/mActionCapturePolygon.png) to add polygons.
4. Draw a polygon in the map canvas using <kbd>Left-click</kbd>. <kbd>Right-click</kbd> will finish the polygon creation and join the first and the last point you have added. 
5. A new window will open. Here you can add the column information for this feature. 
4. Save edits by clicking on the ![](/fig/mActionSaveEdits.png) icon and exiting the edit mode by clicking on the ![](/fig/mActionToggleEditing.png) icon. 

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_add_feature.mp4"></video>



## Modifying existing geometries

1. In the layers panel, select the layer with the geometry you want to edit by clicking on it. It will appear blue.
2. In the digitising toolbar, click on ![](/fig/mActionToggleEditing.png) start `edit mode`. 
3. In the digitising toolbar, click on ![](/fig/qgis_3.40_vertex_tool.png). Now, you can move and edit vertices of geometries. 
4. Once you are done, don't forget to exit the editing mode by clicking on ![](/fig/mActionToggleEditing.png) and saving your edits. 

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_move_vertices.mp4"></video>

### Adding Ring to existing polygon layer

In QGIS, adding rings to polygons is done with the "Advanced Digitisation Toolbar". To activate the toolbar, navigate to `View` -> `Toolbars` -> `Advanced Digitisation Toolbar`.

![](/fig/Toolbox.png)


1. Click on ![](/fig/mActionToggleEditing.png) to start the editing mode of a polygon layer.
2. Click on ![](/fig/mActionAddRing.png) (e.g. map the inner courtyard of a building, or -  as shown in the video - create a circle to mark an isle in the lake).


<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_add_ring.mp4"></video>


## Further resources

The YouTube Video below shows the whole process of digitizing polygons in QGIS in some more detail. Note that the YouTuber is using an older version of QGIS, so things might be different in your version.

<iframe width="560" height="315" src="https://youtu.be/embed/Zer558SnKX4?si=ELKStx6y5_B_ilRe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
