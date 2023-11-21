# Attribute Table in QGIS

The attribute table, a core component of Geographic Information Systems (GIS), __organizes and presents__ detailed information about features in a selected layer. Each __row__ in the table represents a __feature__, while __columns__ store specific __attributes__. This table facilitates searching, selection, sorting, filtering, and editing of features.

## Buttons of Attribute Table

![Example of an attribute table](/fig/attribute_table.png)

Below all buttons of the attribute table are listed. 

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

## Attribute Table-Basics

### Display attribute table and sort features

* __Open Attribute Table:__ Right click on your layer --> `Open Attribute Table`
* __Sort column:__ Click on a column header.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_show_attribute_table.mp4"></video>


### Manually select features in the attribute table

* __Select:__ Click on the lines of the features. 
* __Multi Select:__ To select multiple features press `Ctrl` and select `features`.
* __Show only selected features:__ In the bottom left of the attribute table open the dropdown menu and select `Show selected features`. To show again all features click on `Show all features`. 

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>

### Unselect feature

* __Unselect:__ Click on ![](/fig/mActionDeselectActiveLayer.png) or use `Ctrl+Shift+A`.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_unselect.mp4"></video>

### Zoom in on a specific feature

* __Zoom:__ Right click onyour feature --> `Zoom To Feature`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom_to_feature.mp4"></video>

## Table view vs Form view
QGIS provides two view modes to easily manipulate data in the attribute table:

* __Table View:__ ![](/fig/mActionOpenTable.png)This mode presents the values of multiple features in a tabular format, where each row corresponds to a feature, and each column represents a field.
* __Form view:__! [](/fig/mActionFormView.png) This mode shows all attributes of _one_ selected feature.

To switch between these modes use the ![](/fig/mActionFormView.png) ![](/fig/mActionOpenTable.png) buttons in the down right corner of the attribute table.

___

## Attribute Table- Data Editing

### Change data in the attribute table

* __Open Attribute table:__ Right click on your layer --> `Open Attribute Table`
* __Edit Data:__ Activate editing mode by clicking on ![](/fig/mActionToggleEditing.png) --> Do your edits
* __Save edits:__ Click on ![](/fig/mActionSaveEdits.png) __or__ deactivate editing mode by clicking on ![](/fig/mActionToggleEditing.png) --> `Save`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Attributtabel_edit.mp4"></video>

### Add new column

* __Add new column:__ Activate editing mode by clicking on ![](/fig/mActionToggleEditing.png) --> click on ![](/fig/mActionNewAttribute.png), the window `Add Field` will open.
* __Specify column variables:__ Fill the window and click `OK`.
    * `Name`        = Name of column
    * `Comment`     = Additional info about column
    * `Type`        = Select the type of data the column will have.Table of data types below.


| Type                        | Property                                           |
|-----------------------------|----------------------------------------------------|
| Whole number (integer)     | Whole numbers like counts, quantities, or IDs.    |
| Whole number (integer 64-bit) | Larger whole numbers for very big counts.     |
| Decimal number (real)      | Numbers with decimal points, useful for measurements and fractions. |
| Text (string)               | Alphanumeric characters, such as names and descriptions.  |
| JSON (string)               | Structured text data often used for complex information. |
| Date                        | Specific calendar dates.                             |
| Date & Time                 | Dates and times together |
| Binary object (BLOB)       | For storing binary data like images, audio, or files.  |
| Boolean                     | Simple true/false or yes/no values.              |

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_add_column.mp4"></video>

### Delete column

* __Delet column:__ Activate editing mode by clicking on ![](/fig/mActionToggleEditing.png) --> click on ![](/fig/mActionDeleteAttribute.png) --> Select the columns you want to delete --> Click on `OK` -->  Click on ![](/fig/mActionSaveEdits.png)

```{Hint}
To select multiple columns press `Ctrl` and select columns.
```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_delet_column.mp4"></video>


