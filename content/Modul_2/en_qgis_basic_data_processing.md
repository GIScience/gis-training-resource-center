🚧 This training platform and the entire content is under ⚠️construction⚠️ and 
may not be shared or published! 🚧

# Geodata management

<!-- no geodata processing? fix title-->

**Competences:**

* Data import
* Geo features and attributes
* Feature selection
* Basemap selection

This chapter will focus on how to manage geodata on your computer and in QGIS, in order to have a clean and 
structured workflow. Working in such a way can save you a lot of headaches when working with GIS-software. 

<!-- In this chapter, we will have a close look at how to work with geodata in QGIS. 
Since vector data is the primary geodata type you will work with at the beginning 
of your GIS career, we will focus on vector geodata. -->

## Geodata management 

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
<!-- CHECK: add source 
I think Probably HeiGIT/Alec
 -->

### Geodata naming 

Naming your data correctly ensures that you can identify the layers and your computer does not run into any issues 
when working with your data files. The name of your files themselves need to be clear, meaning that you or others 
can identfify what the data shows, where the data comes from, and to what time it refers. In QGIS, you should name 
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
output). <!-- CHECK: Is this understanding correct? --> 
In this way, other people can understand what purpose different layers serve and 
whether they are needed in the final project.  

`adm0 >> adm0_projUTM >> adm0_projUTM_clipUrban >> adm0_projUTM_clipUrban_intersectFacilities >> facilities_processed`

## Data import

Before you can start creating maps in QGIS, you will need to load your data into QGIS. Depending on which file format you want to import, the process differs slightly.

### Vector data import

Typical [vector data formats](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept.html#vector-file-formats) are Shapefile (`.shp`) and GeoPackage (`.gpkg`). 
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
QGIS only let's you import __unzipped__ shapefiles. Make sure to unzip your data files before importing them into QGIS.
```

:::{dropdown} Video: Importing vector data via the Data Source Manager
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>
:::

#### Open vector data via drag-and-drop

QGIS let's you open data in your QGIS-project by simply dragging the files from your file browser onto your QGIS window. Shapefiles contain only 1 layer per `.shp`-files, which will be added automatically into you layer-panel. Geopackage files (`.gpk`) can contain multiple layers in a single file. If you add a geopackage file, a new window will open where you will be prompted to select the layers you want to add to your project. 

:::{dropdown} Video: Importing vector data via drag-and-drop
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

### Delimited text import (.csv, .txt)

In your GIS-career, you will come across geodata in the  format of delimited text files, such as `.csv`-files (Comma-Separated-Values). These files contain tabular data, which can be opened by programs such as Microsoft Excel. They contain geographical or positional information as point coordinates in separated columns (for example, latitude and longitue, or x- and y-coordinates), or as "Well-known-text" (WKT), which represents complex geometries, such as polygons or lines.  

#### Open Delimited Text Layer 

```{Tip}
To load data from spreadheets such as Comma Separated Value (`.csv`) or 
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

### The Browser-panel

<!-- ADD: Browser Panel workflow-->

## The attribute table

Each vector layer consists of geometric features (points, lines or polygons) and 
an __attribute table__. The attribute table contains information on each feature 
in the layer. The information is stored in rows and columns in the attribute table. 
Each __row__ in the table represents a __feature__, while __columns__ store 
__attributes__ of that feature. You can use the attribute table to search, sort, 
filter, edit and select data.


```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 600px
name: 
align: center
name: Vector Data overview
---
Vector Data overview. Source: HeiGIT
```

### Opening the attribute table

Having a look into the attribute table is essential to understand and get an overview of the 
data you are working with. You can open the attribute table in two ways. 

1. Right click on a layer in the Layers panel and select `Open Attribute Table` 
2. Select a layer in the Layers panel and click on the attribute table symbol in 
   the toolbar. 

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
If you have multiple layers, only the attribute table of the layer currently 
selected in the layer panel will open. 
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

<!-- ADD: WHat will be the most important of these. Needs more explanation. EN-->


### Sort the attribute table

You can sort data in the attribute table by clicking on a column header. Text data will 
be sorted alphabetically and numeric data will be sorted by value. To reverse 
the sort order, click the header again. A small arrow in the column header 
indicates whether it is sorted in ascending or descending order. 

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

You can zoom in on a specific feature if you need to locate it geographically or you want to get a closer look: 

1. __Zoom:__ Right click on a feature --> `Zoom To Feature`
2. Close your attribute table. The map canvas will now show the selected feature. 

:::{dropdown} Video: Zoom in on a feature
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom_to_feature.mp4"></video>
:::

### Manually select features in the attribute table

To interact with features in a layer you have to select these features. One way 
to select features is via the attribute table.

* __Select:__ Click on the lines of the features. 
* __Multi Select:__ To select multiple features press `Ctrl` and select `features`.
* __Show only selected features:__ In the bottom left of the attribute table open 
  the dropdown menu and select `Show selected features`. To show again all 
  features click on `Show all features`. 
* __Only show unselected features__ Select features and click on ![](/fig/mActionInvertSelection.png)

:::{dropdown} Video: Manually select features in the attribute table
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>
:::

### Zoom to selected area
Now that you know how to select features, you can zoom onto your area of 
interest. To do so you can click on the symbol on the toolbar or right click 
on the layer and select `Zoom to Selection`

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

After you have selected your data, you might want to proceed with only the 
selection. You can save your selection as new layer. To do so right click on the 
layer - `Export` -> `Save only selected features`

You can then choose the format, layer name and CRS.

```{tip}
We recommend use GeoPackage (.gpkg) instead of Shapefile (.shp) in most cases. 
If you are unsure which format is most appropriate, check out the [geodata types](../Wiki/en_qgis_geodata_types_wiki.md)
page on the wiki.
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

## Basemaps

<!-- CLARIFY: This section could be rewritten more clearly; 
EN: Added a bit more context -->
Basemaps are background maps that help you visualise the geographic area you are working on. They are very practical since they are easy to use, allow easy orientation on the map canvas. QGIS offers 
OpenStreetMap and some other base maps by default, such as OpenStreetMap or MapZen Global Terrain.

However, there is a wide range of base maps that can be used via extra plugins 
or XYZ Tiles.

Here we give you an overview of ways to access base maps in QGIS.

### Standard QGIS Basemaps

You can always add the standard OpenStreetMap as a basemap to your map canvas. 

```{tip}
The [wiki article on basemaps](../Wiki/en_qgis_basemaps_wiki.md), has a tutorial 
on adding more types of basemaps (e.g. from Google Maps) to the standard basemap 
options in QGIS.
```
There are two ways to add OpenStreetMap as a basemap.

1. Find in the `Browser` panel `XYZ Tiles`. Open the dropdown by 
   clicking on the arrow next to it and select OpenStreetMap

2. In the `Layer` menu -> `Add Layer` -> `Add XYZ layer...` -> Select OpenStreetMap 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>



### QuickMapServices

There are lots of plugins available for QGIS that provide additional tools not 
available in a standard installation. The [plugins page](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html) on the wiki provides a more detailed example
information.
One useful plugin is [QuickMapServices](https://nextgis.com/blog/quickmapservices/). 
This plugin lets you access a wide range of basemaps that are not available in 
QGIS by default, such as Bing or Sentinel-2 satellite imagery.

:::{dropdown} Installation of plugins
To install a plugin `Plugins` -> `Manage and Install Plugins…` -> `All` -> 
Search for the plugin -> `Install Plugin`

<!-- FIXME: Plugin installation should be its own section, not nested under 
   QuickMapServices 
 -->

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

```{Tip}
If you cannot find a specific extension, check you have not used spaces where the 
plugin name doesn't (e.g. When looking for QuickMapServices, searching "Quick Map" 
will not return results but "quickmap" will). You can use an asterisk (`*`) as a
wildcard in searches (so "quick*map" will return results with or without a space
between "quick" and "map"). 
```

If you still cannot find an extension, you may need to allow experimental 
extensions in the options (see below).

```{figure} /fig/en_30.30.2_plugin_installation_experimental_checkbox.png
---
name: plugin manager allow experimental plugins
width 400 px
---
Plugin Manager settings to show experimental plugins
```

:::

To add a Basemap from the QuickMapServices Plugin:

1. In the main menu in the top bar of your screen, navigate to `Web` > `QuickMapServices` 
2. Click on `Search QMS`. A new panel will open, most likely at the bottom right.
3. Here, you can search for a basemap of your choice. For example, Bing Aerial, different versions of OpenStreetMap, Sentinel-2 satellite imagery. 

```
{Tip}
A list of basemaps and useful search queries for the QMS-plugin can be found on [this website](https://qms.nextgis.com). This link can also be found in the "About" section of the QMS-plugin
```

:::{dropdown} Video: Functionality of the QuickMapServices Plugin__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>

```{Note}
When you are using QuickMapServices, be aware that some of these maps are under copyright laws, that restrict the reproduction of these maps. Be aware of these restrictions by looking up the copyright licences for the basemaps you are using. In general, satellite imagery is not free to use. 
```
<!-- CLARIFY: What are the problems? Are there any fixes for them? DONE
EN: Is my understanding correct? -->