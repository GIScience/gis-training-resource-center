# Projections
```{Note}
Always check that the Coordinate Reference System (CRS)/EPSG code of your data is the same as the CRS/EPSG-code of your project!
```
## How to check EPSG-Code 

The default CRS/EPSG code of every QGIS project is the World Geodetic System 84 (EPSG: 4326). This CRS is optimized for world maps. So not perfect for most applications, because we mostly use maps for small areas.

### How to check EPSG-Code/CRS of your QGIS Project and change it
```{Tip}
To check and adjust the CRS/ EPSG-Code should be the first thing you should do when starting a new QGIS project
```

* Open a QGIS projeckt
* In the very down right corner of QGIS you find the butten "EPSG". The number next to it is the EPSG Code currently used in the project. Your more information click on the butten.
![](/fig/EPSG_Code.png)
* The window "Project Properties" will open. Here you can view all availbel CRS/EPSG-Code an there properties.
* To change the CRS/EPSG-code, select the one you want to use and click "Apply".

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>


## Changing the projection of a vector layer