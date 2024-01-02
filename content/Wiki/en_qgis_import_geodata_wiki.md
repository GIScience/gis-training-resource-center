# Geodata Import in QGIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Vector data Import 



```{Tip}
When importing a shapefile by drag-and-drop you have to use the file with the ending .shp!
```
### Open vector layer

#### Open vector data via Layer Tab

1. `Layer` Tab -> `Vecctor`
2. Select file
3. Click `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>


#### Open vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>

## Raster data Import 

### Open raster data via Layer Tab

1. `Layer` Tab -> `Raster`
2. Select file
3. Click `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>


### Open raster data via drag-and-drop

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

### Open NetCDF raster files

1. `Layer` -> `Add Layer` -> `Add Raster Layer` -> Select your file -> click `add` 
2. A window will open and you have to select the exact dataset you want to use. -> Click `add Layers`
3. Click on the ? in the Layers window. The window `Coordination Reference System Select` will open. -> Select the correct reference system-> Click `OK`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_NetCDF_raster.mp4"></video>



## Text data import

```{Tip}
To directly load .csv or EXCEL data into QGIS, the datasets need to have columns containing geometry in the form of latitude (Y-field) and longitude (X-field). 
```

### Open csv. data in QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

### Open .xlsx files in QGIS

1. Drag and drop the .xlsx file in QGIS.
2. If the file contains multible tables, select the table you want to work with. Click `add Layers`
3. click on the `Processing` tab -> `Toolbox` -> search for the tool `Creat points layer from table`
4. Select you table as `Input Layer`
5. Select the  longitude column for `X field` and the latitude column for `Y field`
6. Click `Run`

```{Tip}
A other option is always to transform the .xlsx file into a .csv, which is eaysier to open in QGIS.
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_xlsx.mp4"></video>




*QGGIS Version 3.22.15*

