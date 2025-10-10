# Geodata Import in QGIS


__🔙[Back to Homepage](/content/intro.md)__

## Vector data Import 

```{Tip}
When importing a shapefile by drag-and-drop you have to use the file with the ending .shp!
```
### Open vector layer

#### Open vector data via Layer Tab

1. Click on `Layer`-> `Add Layer`-> `Add Vector Layer`. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your vector file.
3. Select the file and click `Open`
4. Back in QGIS click `Add`


<video width="70%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>


#### Open vector data via drag-and-drop

1. In your file browser, open the folder with the vector data you want to import.
2. Drag-and-drop it onto the QGIS map canvas.

<video width="70%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>

## Raster data Import 

### Open raster data via Layer Tab

1. Click on `Layer`-> `Add Layer`-> `Add Raster Layer`. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your raster file.
3. Select the file and click `Open`
4. Back in QGIS click `Add`

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

```{Note}
When loading vector data in text format like .csv or .txt in QGIS, these data has to have latitude and longitude columns. 
* `X field` =“LONGITUDE” 
* `Y field` = “LATITUDE”
```

1.  `Layer` -> `Add Layer` ->`Open Delimited Text Layer`.
2. Click on `File name` click on the three points ![](/fig/Three_points.png) and navigate to your csv. file and click `Open`.
3. In the window "Data Source manager| Delimited Text" in QGIS you can find multiple drop-down menus
    * `File Format`: Here you can specify which delimiter is used in the file you want to import. In a standard `.csv` file commas `,` is used. If this is not the case, select `Custom delimiters`. Here you can choose the exact delimiter used in your file. 
    ```{Tip}
    To find out which delimiter is used you can open your .csv file in Notepad or Excel. There you can check which delimiter is used to separate the information.
    ```
    * `Record and Fields Options`: Under this drop-down menu, you can instruct QGIS to detect the data type of the different columns of the field and to detect column headers. Usually, you do not have to make any adjustments here.
    * `Geometry definition`: In this section, you specify which columns of the file contain the spatial information to geo-referenced the data on the map. If the file has a column containing __latitude__ and another with __longitude__ data, you can use them to georeferenced the data. Check `Point Coordinates`. Select for `X field` “LONGITUDE” and for `Y field` “LATITUDE”.
    Under `Geometry CRS`select the coordinate reference system (CRS). By default, QGIS will select the CRS of the project. 
    If the file does not have spatial information choose the option `No geometry (attribute only table)`.
4. Click `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

### Open .xlsx files in QGIS

1. Drag and drop the .xlsx file in QGIS.
2. If the file contains multiple tables, select the table you want to work with. Click `add Layers`
3. click on the `Processing` tab -> `Toolbox` -> search for the tool `Create points layer from table`
4. Select you table as `Input Layer`
5. Select the  longitude column for `X field` and the latitude column for `Y field`
6. Click `Run`

```{Tip}
A other option is always to transform the .xlsx file into a .csv, which is easier to open in QGIS.
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_xlsx.mp4"></video>





