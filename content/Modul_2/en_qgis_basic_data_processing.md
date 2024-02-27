🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

# Geodata and Geodata processing
**Competences:**
* Data Import
* Geo features and attributes
* Feature selection
* Basemap selection

In this chapter, we will have a close look at how to work with geodata in QGIS. Since vector data is the primer geodata type you will work with at the beginning of your GIS carrier, we will focus on vector geodata.

## Geodata mananagemnet 

Working with geodata is unlike working with data in programs like Excel or MS Word. Whenever you load an image in a Word file, the file will contain the image. When you delete the image on your computer, the Word file will still contain a copy of the image. 

This is not the case in QGIS! When you load geodata into QGIS, the system only establishes a path to the location where your geodata is stored on your computer. This means your QGIS project __does not contain__ the geodata, it only links to the data on your computer. Once you have loaded the geodata in your QGIS project and you change the location of the geodata or delete it on your computer, the data is no longer available in your QGIS project. 

Ok, QGIS projects only link to geodata, they do not contain the data. This means that whenever you edit geodata, the changes persistent and can not be reversed.

These circumstances make working with geodata special. To handle this, the only solution is good data management practices!

### Standard Folder Structure

The single most important geodata management practice is to use a standardized folder structure that contains all elements of the particular QGIS project. 
The paths from a QGIS project to the geodata are by default relative. That means when the data and the project are in a fixed folder structure, you can move the whole structure without impacting the QGIS project or the paths to the geodata.
The version of a standardized folder structure, that is used for all exercises in this training is explained below. A template of the folder structure can be downloaded [__here__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).

 A standard folder structure has two principal advantages:
1. By sharing the whole project folder, we can be certain that the project will run without problems on a different computer.
2. The folder structure supports the proper organization of geodata and supports the stable function of a QGIS project. 

```{figure} /fig/Standard_project_folder_structure.drawio.svg
---
width: 600px
name: 
align: center
name: Standard folder structure
---
Standard folder structure. Source: ???
```
### Geodata naming 

There are some basic principles when it comes to naming geodata that you produce or manipulate:

* Do not use special characters like `!`,`?` etc., slash or dash `/` or `-`.
* Do not use blank spaces, use underscores `_`
* Make sure you can relate every output / intermediate result to a step in your workflow. Below you can see a geodata set representing the borders of a country evolving during geodata processing. It is not apparent what was done with the original dataset.

`adm0 >> adm0_temp >> adm0_temp2 >> adm0_temp3 >> facilities_final`

In the version below, it is clear what was done. In this way, other people can understand the process behind a final result like a map. 

`adm0 >> adm0_projUTM >> adm0_projUTM_clipUrban >> adm0_projUTM_clipUrban_intersectFacilities >> facilities_processe`


## Data import

Before you can start visualizing and analysing in QGIS, you need to import your data. 

Depending on which file format you want to import, the process differs slightly.

::::{tab-set}

:::{tab-item} Vector data import

Typical vector data formats are Shapefile and GeoPackage. The process of importing vector data in either of the two formats is the same. 
[Here](../../content/Modul_2/en_qgis_geodata_concept.md) is a list of possible vector data formats.

```{Note}
GeoPackage file can contain multiple files and even whole QGIS projects. When you load such a file in QGIS a window will appear in which you have to select the files you want to load in your QGIS project.
```

There are two ways how to load vector data in QGIS. Via the `Layer` tab or via drag-and-drop.

### Open vector data via Layer Tab

1. Click on `Layer`-> `Add Layer`-> `Add Vector Layer`. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your vector file.
3. Select the file and click `Open`
4. Back in QGIS click `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>


### Open vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::


:::{tab-item} Delimited text import

### Open  Delimited Text Layer (.csv, .txt)

```{Tip}
To directly load .csv or EXCEL data into QGIS, the datasets need to have columns containing geometry in the form of latitude (Y-field) and longitude (X-field). 
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

1.  `Layer` -> `Add Layer` ->`Open Delimited Text Layer`.
2. Click on `File name` click on the three points ![](/fig/Three_points.png) and navigate to your csv. file and click `Open`.
3. `File Format`: Here you can specify which delimiter is used in the file you want to import. In a standard .csv file commas `,` is used. If this is not the case, select `Costume delimiters`. Here you can choose the exact delimiter used in your file. 
```{Tip}
To find out which delimiter is used you can open your .csv file in Notepad or Excel. There you can check which delimiter is used to separate the information.
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
4.  `Geometry definition`: In this section, you specify which columns of the file contain the spatial information to geo-referenced the data on the map. If the file has a column containing __latitude__ and another with __longitude__ data, you can use them to georeferenced the data. Check `Point Coordinates`. Select for `X field` “LONGITUDE” and for `Y field` “LATITUDE”.
5. Under `Geometry CRS`select the coordinate reference system (CRS). By default, QGIS will select the CRS of the project. 
If the file does not have spatial information choose the option `No geometry (attribute only table)`.
6. Click `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>
:::

:::{tab-item} Raster data import

There are two ways how to load vector data in QGIS. Via the `Raster` tab or via drag-and-drop.

### Open raster data via Layer Tab

1. Click on `Layer`-> `Add Layer`-> `Add Raster Layer`. 
2. Click on the three points ![](/fig/Three_points.png) and navigate to your raster file.
3. Select the file and click `Open`
4. Back in QGIS click `Add` 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>


### Open raster data via drag-and-drop

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

:::

::::


## Geo features and attributes

Each vector layer consists of geometric elements (points, lines or polygons) and an __attribute table__. The attribute table contains information on each element of the layer. The information is stored in rows and columns in the attribute table. Each __row__ in the table represents a __feature__, while __columns__ store specific __attributes__. This table facilitates searching, selection, sorting, filtering, and editing of features.


```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 600px
name: 
align: center
name: Vector Data overview
---
Vector Data overview. Source: HeiGIT
```

:::{dropdown} Buttons of Attribute Table
|Icon|Description|Purpose|Shortcut|
|---|---|-----|---|
| ![](/fig/mActionToggleEditing.png)|Toggle editing mode | Enable editing functionalities|`Ctrl+E`|
| ![](/fig/mActionMultiEdit.png)| Toggle multi-edit mode| Update multiple fields of many features          |  |
|![](/fig/mActionSaveEdits.png)| Save edits| Save current modifications                        | |
|![](/fig/mActionRefresh.png)| Reload the table  | | |
|![](/fig/mActionNewTableRow.png)| Add feature | Add new geometryless feature |  |
|![](/fig/mActionDeleteSelectedFeatures.png)| Delete selected features| Remove selected features from the layer|  |
|![](/fig/mActionEditCut.png)| Cut selected features to clipboard    |  | `Ctrl+X` |
|![](/fig/mActionCopySelected.png)| Copy selected features to clipboard   |   | `Ctrl+C`      |
|![](/fig/mActionEditPaste.png)| Paste features from clipboard| Insert new features from copied ones |`Ctrl+V`|
|![](/fig/mIconExpressionSelect.png)| Select features using an Expression|| | 
|![](/fig/mActionSelectAll.png)| Select All| Select all features in the layer|`Ctrl+A`      |
|![](/fig/mActionInvertSelection.png)| Invert selection| Invert the current selection in the layer |`Ctrl+R`|
|![](/fig/mActionDeselectActiveLayer.png)| Deselect all| Deselect all features in the current layer|`Ctrl+Shift+A`|
|![](/fig/mActionFilterMap.png)|Filter/Select features using form     | |`Ctrl+F`|
|![](/fig/mActionSelectedToTop.png)| Move selected to top| Move selected rows to the top of the table|  |
|![](/fig/mActionPanToSelected.png)| Pan map to the selected rows|  | `Ctrl+P`|
|![](/fig/mActionZoomToSelected.png)| Zoom map to the selected rows | |`Ctrl+J`      |
|![](/fig/mActionNewAttribute.png)| New field | Add a new field to the data source | `Ctrl+W`|
|![](/fig/mActionDeleteAttribute.png)| Delete field  | Remove a field from the data source | |
|![](/fig/mActionEditTable.png)| Organize columns | Show/hide fields from the attribute table||
|![](/fig/mActionCalculateField.png)| Open field calculator| Update field for many features in a row |`Ctrl+I`      |
|![](/fig/mActionConditionalFormatting.png)| Conditional formatting | Enable table formatting| |
|![](/fig/dock.png)| Dock attribute table | Allows to dock/undock the attribute table||
|![](/fig/mAction.png)| Actions | Lists the actions related to the layer           | |
:::

Having a look into the attribute table can be helpful to get an overview on the data you are working with. It can also be used to select, filter or edit data.

### Open the attribute table

One can open the attribute table in two ways. Either click right on the chosen layer and select `open attribute table` or click on the symbol on the top.

```{figure} /fig/en_attributetable_right_click.png
---
height: 500px
name:
align: center
name: Open Attribute Table with right click
---
Screenshot of Opening the Attribute Table with right click
```

```{note} 
If you have multiple layers, only the attribute table of the layer selected in the layer panel on the left will open. 
```

```{figure} /fig/en_attributetable_top_right.png
---
height: 500px
name: 
align: center
name: Open Attribute Table top right
---
Screenshot of Opening the Attribute Table
```


### Sort the attribute table

Now that the attribute table is opened, it is possible to sort the data within. By clicking on the tab of the column, you can sort the data (alphabetically) in ascending or descending order.
The small arrow indicates whether it is sorted ascending or descending. 

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_show_attribute_table.mp4"></video>

``````{list-table}
:header-rows: 1
:widths: 25 25

* - Sorted ascending
  - Sorted descending
* - ```{figure} /fig/en_ascending.png
    ---
    height: 600px
    name:
    align: center
    ---
    The data is sorted ascending. 
    ```
    
  -
    ```{figure} /fig/en_descending.png
    ---
    height: 600px
    name: 
    align: center
    ---
    The data is sorted descending.  
    ```
``````

### Zoom in on a specific feature via attribute table

* __Zoom:__ Right click on your feature --> `Zoom To Feature`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom_to_feature.mp4"></video>

### Manually select features in the attribute table

To interact with features in a layer you have to select these features. One way to select features is via the attribute table.

* __Select:__ Click on the lines of the features. 
* __Multi Select:__ To select multiple features press `Ctrl` and select `features`.
* __Show only selected features:__ In the bottom left of the attribute table open the dropdown menu and select `Show selected features`. To show again all features click on `Show all features`. 
* __Only show unselected features__ Select features and click on ![](/fig/mActionInvertSelection.png)


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>

### Zoom to selected area
Now that you learned how to select features, you can zoom onto your area of interest. To do so you can click on the symbol on the top pannel or click right on the layer and select `Zoom to Selection`

```{figure} /fig/en_zoom_to_selection_1.png
---
width: 800px
name:
align: center
name: Zoom to Selection, top pannel.
---
Screenshot of how to zoom to Selection on the top.
```

```{figure} /fig/en_zoom_to_selection_2.png
---
width: 600px
name:
align: center
name: Zoom to Selection, right-click.
---
Screenshot of how to zoom to Selection by clicking right.
```

### Save only selected features as a new file

After you selected your data, you might want to proceed with only the Selection. It is possible to save your Selection as new layer. To do so click right on the layer -`Export` -> `Save only selected features`

You can then choose the format, layername and crs.

```{tip}
Use GeoPackage (.gpkg) instead of Shapefile (.shp)!
If you are unsure which format is best, check out the wiki [Geodata types](../Wiki/en_qgis_geodata_types_wiki.md)
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_export_wiki.mp4"></video>


```{figure} /fig/en_save_selection.png
---
height: 500px
name:
align: center
name: Save selection, right-click.
---
Screenshot of how to save only selected features.
```




## Base maps

Basemaps are background maps. They are often very practical since they are easy to use, allow easy orientation on the map canvas and are diverse. QGIS offers OpenStreetMap and some other base maps by default. 

However, there is a wide range of base maps that can be used via extra plugins or XYZ Connections.

Here we give you an overview of ways to access base maps in QGIS.

### Standard QGIS Basemaps

You can always add the standard OpenStreetMap as a basemap to your map canvas. 

```{tip}
In the [wiki article on base maps](../Wiki/en_qgis_basemaps_wiki.md), you can find a tutorial to add more base maps e.g. from google to the standard base map list of your QGIS.
```
There are two ways to add the OpenStreetMap as a basemap.

__Option 1:__ Find in the `Browser` panel `XYZ Tiles`. Open the dropdown by clicking on it and select OpenStreetMap or another basemap.

__Option 2:__ `Layer` -> `Add Layer` -> `Add XYZ layer...` -> Select the OpenStreetMap or another basemap.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>



### QuickMapServices

There are numerous extensions for QGIS, also called plugins, which provide extended functionalities. In the wiki article about plugins, you can learn all about them.
One of the most important plugins is the [QuickMapServices](https://nextgis.com/blog/quickmapservices/) plugin.

The QuickMapServices Plugin allows to access a wide range of basemaps. 

:::{dropdown} Installation of plugins
To install a plugin `Plugins` -> `Manage and Install Plugins…` -> `All` -> Search for the plugin -> `Install Plugin`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

```{Tip}
If you cannot find a specific extension, check your capitalisation and correct use of spaces. If you still cannot find an extension, you may need to allow the experimental extensions in the options (see below).
```
:::


`Web` -> `QuickMapServices` -> select provider e.g. NASA -> select basemap

__Functionality of QuickMapServices Plugin__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>

```{Note}
There can be problems when printing some basemaps from the QuickMapServices!
```


