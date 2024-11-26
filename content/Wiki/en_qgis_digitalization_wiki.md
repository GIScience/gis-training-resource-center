# Digitization


__🔙[Back to Homepage](/content/intro.md)__

Digitization is the process of converting geographic data from maps or images into digital form commonly represented as vector data.
During this procedure, spatial information from maps or images is traced, forming points, polylines, or polygons. 
To digitize data for a new dataset you always have to start with creating the dataset before filling it with digitized data.

## Create a new layer

- `Layer` --> `Create Layer` -> `New GeoPackage Layer` or `New Shapefile Layer`
- Click on ![](/fig/Three_points.png) and navigate to the folder where you want to save the dataset.
- `File encoding`: Make sure this is set to UTF-8
- `Geometry type`: Select the type of feature you want to digitalise e.g. points, lines or polygones.
- Under `Additional dimension` you should always make sure that you check `None`. 
- Select the coordinate system you want to set for the new layer. By default, the QGIS selects the project CRS. If you want to change the CRS click on ![](/fig/mIconProjectionEnabled.png).

- Under `New Field` you can add columns to the new layer. 
    * `Type`: Select the data type the column will have e.g. `Text`, `Whole number`, `Decimal Number`, `Date`.
    * Click on ![](/fig/mActionNewAttribute.png) to add the new column to the `Fields List`.
- Click `OK`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_create_layer.mp4"></video>

## Add geometries to a layer

### Creation of point data

To digitalise points, first you need an existing point layer or you need to create one (check out [Digital Data Creation]( https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html#digital-data-creation) above).

1.	Select the point layer you want to add data to in the Layer panel
2.	Go to the digitalisation toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode.
3.	Click on ![](/fig/mActionCapturePoint.png). 
4.	Left-click on the feature you want to digitalise.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
5.	Once you are done with digitalisation ![](/fig/mActionSaveEdits.png) to save your edits.
6.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>



```{figure} /fig/point_creation.png 
---
width: 500px
name: Point creation
align: center
---
```

### Creation of line data

The  method  is  similar  to  digitising  a  point  (see  above). First you have to created a new line layer or use an existing one. 

```{attention} 
If you create a new line layer remember to change the geometry type into lines because we are creating lines data now.
```
1.	Select the line layer you want to add data to in the Layer panel
2.	Go to the digitalisation toolbar and click on![](/fig/mActionToggleEditing.png). No the layer is in the editing mode.
3.	Click on ![](/fig/mActionCaptureLine.png). 
4.	To digitalise line features, click along the line. When you are done, right-click on the last point of the line to finish the feature.
5.	Once you click, a window will appear `[Your Layer Name]- Feature Attribute`. Here you can add the information about this feature to the different columns, based on the attribute table of the layer.
6.	Once you are done with digitalisation ![](/fig/mActionSaveEdits.png) to save your edits.
7.	Click again on ![](/fig/mActionToggleEditing.png) to end the editing mode.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>

### Creation of polygon data 

- Open a new `polygone layer`.
- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode` and Add Feature: `Capture Polygone`![](/fig/mActionCapturePolygon.png)|. 
- Draw geometries and enter `feature attributes`, like *id* and *name*.
- Save edits ![](/fig/mActionSaveEdits.png) , exit `edit mode`. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_add_feature.mp4"></video>



## Modify existing geometries in the layer

- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode`. 
- `Move vertices` and `add new vertices`.
- Save edits ![](/fig/mActionSaveEdits.png), exit `edit mode`. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_move_vertices.mp4"></video>

### Adding Ring to existing polygon layer

- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode`.
- Add Feature: `Add Ring`![](/fig/mActionAddRing.png) (e.g. map the inner courtyard of a building, or -  as shown in the video - create a cercle to mark an isle in the lake).
- To open the `Advanced Digitizing Toolbar` go to `View > Toolboxes > Advanced Digitizing Toolbar`.
- To add rectangles 'automatically' go to `View > Toolbars > Shape Digitizing Toolbar`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_digitize_add_ring.mp4"></video>


## Further resources

The YouTube Video below shows the whole process of digitizing polygons in QGIS in some more detail. Note that the YouTuber is using an older version of QGIS, so things might be different in your version.

<!---
<video width="100%" controls src="https://www.youtube.com/embded/watch?v=Zer558SnKX4"></video>
-->

<iframe width="560" height="315" src="https://www.youtube.com/embded/watch?v=Zer558SnKX4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
