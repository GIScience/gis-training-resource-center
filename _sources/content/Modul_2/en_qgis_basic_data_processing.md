# Geodata management

__🔙[Back to Homepage](/content/intro.md)__

In this chapter, we will have a close look at how to work with geodata in QGIS. 
Since vector data is the primary geodata type you will work with at the beginning 
of your GIS career, we will focus on vector geodata. 

**Competences:**

* Data import
* Geo features and attributes
* Feature selection

## Geodata management: Fundamentals

Working with geodata is not like working with data in programs such as Microsoft 
Excel or Word. Whenever you load an image in a Word file, the file will contain 
the image. If you delete the image on your computer, the Word file will still 
contain a copy of the image. 

This is not the case in QGIS! When you load geodata into QGIS, the system only 
establishes a link to the location where the data is stored on your computer. 
This means your QGIS project __does not contain__ the geodata, it only links to 
it. If you load data in your QGIS project and you change the location of the 
data or delete it, the data is no longer available in your QGIS project and you 
will get an error when you open it. 

Because you are working directly with the source data, rather than a copy, 
whenever you edit data in QGIS the changes replace the source data and can not 
be reversed. If you plan to make changes to your data, you should make a copy of 
it first so that you always have a 'clean' copy you can go back to. 

### Standard folder structure

The single most important geodata management practice is to use a standardised 
folder structure that contains all parts of the QGIS project. 

The paths from a QGIS project to the geodata are by default relative. This means 
when the data and the project are in a fixed folder structure, you can move the 
whole structure without impacting the QGIS project or the paths to the data.
The version of a standardized folder structure that is used for all exercises 
in this training is explained below. A template of the folder structure can be 
downloaded [__here__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).

 A standard folder structure has two principal advantages:

1. If we share the whole project folder, we can expect the project to run 
   without problems on a different computer
2. The folder structure supports the proper organisation of project data and 
   helps ensure the QGIS project will work as intended

```{figure} /fig/Standard_project_folder_structure.drawio.svg
---
width: 600px
name: 
align: center
name: Standard folder structure
---
Standard folder structure. Source: HeiGIT
```


### Geodata naming 

Naming your data correctly ensures that you can identify the layers and your computer does not run into any issues 
when working with your data files. The name of your files themselves need to be clear, meaning that you or others 
can identify what the data shows, where the data comes from, and to what time it refers. In QGIS, you should name 
your layers so you can identify the content, as well as what you have done with the layer. For example, if you have 
clipped a street layer of new york, do not name the layer "clipped", give it a name such as "streets_NYC_clipped".

There are some basic principles when it comes to naming geodata that you produce 
or manipulate:

* Do not use special characters like `!`,`?`, `/` or `-`.
* Do not use blank spaces, use underscores `_`
* Give layers meaningful names so that you can understand what they represent, 
  even if they are a temporary/intermediate step in a workflow. 

Below you can see an example of a workflow to process an admin boundary dataset 
(`adm0`). The purpose of the intermediate steps is not clear because the layer 
names are not meaningful. 

`adm0 >> adm0_temp >> adm0_temp2 >> adm0_temp3 >> facilities_final`

A good naming system for layers is shown below. In this workflow, it is clear what 
processing was performed at each step (reproject, clip layer, join with another layer, 
final result).  
In this way, other people can understand what purpose different layers serve and 
whether they are needed in the final project.  

`adm0 >> adm0_projUTM >> adm0_projUTM_clipUrban >> adm0_projUTM_clipUrban_intersectFacilities >> facilities_processed`

## Data import

Before you can start creating maps in QGIS, you will need to load your data into QGIS. Depending on which file format you want to import, the process differs slightly.

### Vector data import

Typical [vector data formats](/content/Modul_2/en_qgis_geodata_concept.md#vector-file-formats) are Shapefile (`.shp`) and GeoPackage (`.gpkg`). 
The process of importing vector data in either of the two formats is the same. 

QGIS offers a few ways to load vector data into QGIS. The most immediate is via drag-and-drop, where you simply 
drag the data files you want to add to your QGIS project from your file browser into the QGIS window. Another 
method is via the "__Data Source Manager__" (`Layer` > `Data Source Manager`). You can also open the Data Source 
Manager with the keyboard-shortcut `CTRL + L`. 

```{Note}
GeoPackage files can contain multiple datasets and even whole QGIS projects. 
When you load a GeoPackage in QGIS, a window will appear where you can select 
the datasets you want to load.
```

#### Open vector data via the Data Source Manager

1. Click on `Layer`-> `Add Layer`-> `Add Vector Layer...`. This will open the Data Source Manager. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your 
   vector file
3. Select the file and click `Open`. More options will appear. In most cases, you can leave these options as they are.
4. Back in QGIS click `Add`

```{Attention}
QGIS only lets you import __unzipped__ shapefiles. Make sure to unzip your data files before importing them into QGIS.
```

:::{dropdown} Video: Importing vector data via the Data Source Manager
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>
:::

#### Open vector data via drag-and-drop

QGIS lets you open data in your QGIS-project by simply dragging the files from your file browser onto your QGIS window. Shapefiles contain only 1 layer per `.shp`-files, which will be added automatically into you layer-panel. Geopackage files (`.gpk`) can contain multiple layers in a single file. If you add a geopackage file, a new window will open where you will be prompted to select the layers you want to add to your project. 

:::{dropdown} Video: Importing vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

### Delimited text import (.csv, .txt)

In your GIS-career, you will come across geodata in the  format of delimited text files, such as `.csv`-files (Comma-Separated-Values). These files contain tabular data, which can be opened by programs such as Microsoft Excel. They contain geographical or positional information as point coordinates in separated columns (for example, latitude and longitude, or x- and y-coordinates), or as "Well-known-text" (WKT), which represents complex geometries, such as polygons or lines.  

#### Open Delimited Text Layer 

```{Tip}
To load data from spreadsheets such as Comma Separated Value (`.csv`) or 
Excel (`.xlsx`), the datasets need to have columns containing geometry - this is 
most often in the form of latitude (Y field) and longitude (X field), but might 
also be in other formats, such as WKT. In this case, you can also have complex geometries in your delimited text file.  
```

```{figure} /fig/en_import_delimeted_text.png
---
width: 600px
name: 
align: center
name: Import delimited text
---
Import delimited text.
```

1. `Layer` -> `Add Layer` -> `Open Delimited Text Layer`.
2. Click on `File name` click on the three points ![](/fig/Three_points.png) and 
   navigate to your csv file and click `Open`.
3. `File Format`: Here you can specify which delimiter is used in the file you 
   want to import. In a standard .csv file commas `,` is used. If this is not the 
   case, select `Custom delimiters`. Here you can choose the exact delimiter 
   used in your file. 

```{Tip}
To find out which delimiter is used you can open your .csv file in Notepad or 
Excel. There you can check which delimiter is used to separate the information.
```

```{figure} /fig/en_delimited_text_fileformat.png
---
width: 600px
name: 
align: center
name: Import delimited text - file format
---
Import delimited text - file format.
```

4. `Geometry definition`: In this section, you specify which columns of the file 
   contain the spatial information to georeference the data on the map. If the 
   file has a column containing __latitude__ and another with __longitude__ data, 
   you can use them to georeferenced the data. Check `Point Coordinates` if the `.csv`-file contains point data. 
   Select for `X field` “LONGITUDE” and for `Y field` “LATITUDE”.
5. Under `Geometry CRS` select the coordinate reference system (CRS). By default, 
   QGIS will select the CRS of the project. 

   If the file does not have spatial information choose the option `No geometry 
   (attribute only table)`.
6. Click `Add`

:::{dropdown} Video: Opening delimited text files in QGIS
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>
:::

### Raster data import

The import of raster data works in the same way as for vector data. You can either drag-and-drop the raster-files 
onto your QGIS-window, or open then through the "Data Source Manager".

:::{dropdown} Video: Open raster data via the Data Source Manager

1. Click on `Layer`-> `Add Layer`-> `Add Raster Layer`
2. Click on the three points ![](/fig/Three_points.png) and navigate to your 
   raster file
3. Select the file and click `Open`
4. Back in QGIS click `Add` 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>

:::

:::{dropdown} Video: Open raster data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>
:::



