# Digitalization

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

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/fig/raw/main/en_qgis_create_layer.mp4"></video>

## Add geometries to a layer

- Open a new `polygone layer`.
- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode` and Add Feature: `Capture Polygone`![](/fig/mActionCapturePolygon.png)|. 
- Draw geometries and enter `feature attributes`, like *id* and *name*.
- Save edits ![](/fig/mActionSaveEdits.png) , exit `edit mode`. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/fig/raw/main/en_qgis_digitize_add_feature.mp4"></video>

- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode`.
- Add Feature: `Add Ring`![](/fig/mActionAddRing.png) (e.g. map the inner courtyard of a building, or -  as shown in the video - create a cercle to mark an isle in the lake).
- To open the `Advanced Digitizing Toolbar` go to `View > Toolboxes > Advanced Digitizing Toolbar`.
- To add rectangles 'automatically' go to `View > Toolbars > Shape Digitizing Toolbar`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/fig/raw/main/en_qgis_digitize_add_ring.mp4"></video>

## Modify existing geometries in the layer

- Clicking on ![](/fig/mActionToggleEditing.png) start `edit mode`. 
- `Move vertices` and `add new vertices`.
- Save edits ![](/fig/mActionSaveEdits.png), exit `edit mode`. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/fig/raw/main/en_qgis_digitize_move_vertices.mp4"></video>

__Further resources:__

[![Digitizing shapefile QGIS](/fig/en_digitizing_shapefiles.png)](https://www.youtube.com/watch?v=Zer558SnKX4)

