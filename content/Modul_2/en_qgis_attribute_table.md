# Attribute Table

__🔙[Back to Homepage](/content/intro.md)__

Each vector layer consists of geometric features (points, lines or polygons) and 
an __attribute table__. The attribute table contains information on each feature 
in the layer. The information is stored in rows and columns in the attribute table. 
Each __row__ in the table represents a __feature__, while __columns__ store 
__attributes__ of that feature. You can use the attribute table to search, sort, 
filter, edit and select data. 


```{figure} /fig/en_vector_data_overview.drawio.png
---
width: 600px
align: center
name: Vector Data overview
---
Vector Data overview. Source: HeiGIT
```

:::{dropdown} Trainer's corner

You can complement this chapter by doing the steps with a vector layer of your choice. 
You can also do exercise 2 from this module. 

:::

### Opening the attribute table

Having a look into the attribute table is essential to understand and get an overview of the 
data you are working with. After downloading and import a dataset into QGIS, you will most likely open the attribute table to understand the data and see what information is available. Understanding what kind of information is available is indispensable when working with GIS software.

You can open the attribute table in two ways. 

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

::::{margin}
```{tip}

You can also use the shortcut `F6` (in some cases `Fn` + `F6`) to open the attribute.

```
::::

:::{dropdown} Buttons of Attribute Table
|Icon|Description|Purpose|Shortcut|
|---|---|-----|---|
| ![](/fig/mActionToggleEditing.png)|__Toggle editing mode__ | Enable editing functionalities|`Ctrl+E`|
| ![](/fig/mActionMultiEdit.png)| Toggle multi-edit mode| Update multiple fields of many features          |  |
|![](/fig/mActionSaveEdits.png)| __Save edits__| Save current modifications                        | |
|![](/fig/mActionRefresh.png)| Reload the table  | | |
|![](/fig/mActionNewTableRow.png)| Add feature | Add new geometry-less feature |  |
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
|![](/fig/mActionCalculateField.png)| __Open field calculator__| Update field for many features in a row |`Ctrl+I`      |
|![](/fig/mActionConditionalFormatting.png)| Conditional formatting | Enable table formatting| |
|![](/fig/dock.png)| Dock attribute table | Allows to dock or undock the attribute table||
|![](/fig/mAction.png)| Actions | Lists the actions related to the layer           | |
:::

<!-- ADD: What will be the most important of these. Needs more explanation. EN-->


### Sort the attribute table

You can sort data in the attribute table by clicking on a column header. Text data will 
be sorted alphabetically and numeric data will be sorted by value. To reverse 
the sort order, click the header again. A small arrow in the column header 
indicates whether it is sorted in ascending or descending order. 

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_show_attribute_table.mp4"></video>

::::{grid} 2

:::{grid-item-card} 
```{figure} /fig/en_ascending.png
---
width: 300px
name: attribute table ascending sort
---
Attribute table sorted ascendingly. 
```
:::
:::{grid-item-card}
```{figure} /fig/en_descending.png
---
width: 300px
name: attribute table descending sort
---
Attribute table sorted descendingly.  
```
::::

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
* __Only show unselected features:__ Select features and click on ![](/fig/mActionInvertSelection.png)

:::{dropdown} Video: Manually select features in the attribute table
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>
:::

### Zoom to selected area
Now that you know how to select features, you can zoom onto your area of 
interest. To do so you can click on the symbol on the toolbar or right click 
on the layer and select `Zoom to Selection`.

```{figure} /fig/en_zoom_to_selection_1.png
---
width: 800px
align: center
name: Zoom to Selection, top panel.
---
Screenshot of how to zoom to Selection on the top.
```

```{figure} /fig/en_zoom_to_selection_2.png
---
width: 450px
align: center
name: Zoom to Selection, right-click.
---
Screenshot of how to zoom to Selection by clicking right.
```

### Save only selected features as a new file

After you have selected your data, you might want to proceed with only the 
selection. You can save your selection as new layer. To do so right click on the 
layer - `Export` -> `Save only selected features`

```{figure} /fig/en_save_selection.png
---
height: 500px
name:
align: center
name: Save selection, right-click.
---
Screenshot of how to save only selected features.
```

Now, you can choose the format, layer name and CRS.

<!--ADD IMAGE-->

```{tip}
We recommend use GeoPackage (.gpkg) instead of shapefile (.shp) in most cases. 
If you are unsure which format is most appropriate, check out the [geodata types](/content/Wiki/en_qgis_geodata_types_wiki.md)
page on the wiki.
```


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_export_wiki.mp4"></video>


