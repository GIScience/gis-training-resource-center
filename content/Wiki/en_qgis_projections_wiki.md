# Projections

## How to check EPSG-Code 

```{Note}
Always check that the Coordinate Reference System (CRS)/EPSG code of your data is the same as the CRS/EPSG-code of your project!
```

The default CRS/EPSG code of every QGIS project is the World Geodetic System 84 (EPSG: 4326). This CRS is optimized for world maps. So not perfect for most applications, because we mostly use maps for small areas.

### How to check EPSG-Code/CRS of your QGIS Project and change it
```{Note}
To check and adjust the CRS/ EPSG-Code should be the first thing you should do when starting a new QGIS project.
```

1.  Open a QGIS projeckt
2. In the very down right corner of QGIS you find the butten "EPSG". The number next to it is the EPSG Code currently used in the project. For more information click on the button.
![](/fig/EPSG_Code.png)
3. The window "Project Properties" will open. Here you can view all availble CRS/EPSG-Code and their properties.
4. To change the CRS/EPSG-code, select the one you want to use and click "Apply".

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

### How to check EPSG-Code/CRS of layer/ data
```{Note}
After loading any spatial data in QGIS, check the CRS/EPSG code of the data to make sure it is the same as the CRS/EPSG code of the project.
```
1. Right click on the data layer, click on  “Properties”.
2. The “Layer Properties” Window of the data layer will open. Click on “Information”.
3. Under the headline “Coordinate Reference System (CRS)” you find all information about the CRS. The most important are:
    - __Name:__     Here you find the EPSG Code
    - __Unites:__    Here you can find wether it is possible to use meters with this data layer or latitude and longitude.


## Changing the projection of a vector layer

1. "Vector" Tab -> "Data Management Tools" -> "Reproject Layer"
2. Select target CRS/ EPSG-Code.
3. Save the new file by clicking on the three dots next to "Reprojected", specify the file name and the location where you want to save the file.
Click "Run"
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>


## Changing the projection of a raster layer

1. "Raster" Tab -> "Projections" -> "Warp (Reproject)"
2. Select target CRS/EPSG-Code
3. Select resampling method
4. Save the new file by clicking on th three dots nest to "Reprojected", specify the file name and the location where you want to save the file.
Click "Run"

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>
