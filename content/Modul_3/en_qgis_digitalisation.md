# Digitalisation

Digitization is a process of converting raster data to vector data. For this task QGIS provides many tools for efficient digitization. Digitization is one of the important tasks for a GIS specialist. Digitization (or vectorization) should be clean and a copy of the raster data so that the information of the map does not change.

Firstly, you need to check if Digitizing Toolbox is activated in your QGIS in order to digitize. If not then you can activate it using following process.
 1. Click view tab in the menu bar and click toolbar and then check digitizing and advance digitizing tool box.![](/fig/Activate_digitizing_toolbox.png)

 A tool box like this should appear on top of your Qgis ![](/fig/Toolbox.png)
 
 2. **Create Layer:**

Now add some layers for drawing. Click layer in the menu bar, select create layer and select **new spatialite layer** or select **new shapefile layer** if you have to digitize a single feature like some places or roads or buildings. We are choosing new spatialite layer because we want to draw more than one feature in single file and it is easy to transfer this file.

**Next**

Click ‘…’ browse button and save your database. Give name to your layer, select type of layer and specify attributes and their type such as text or numerals and click add attributes to the list and click OK. Specify CRS of the layer same as the CRS of Raster data.


 ![](/fig/New_spatialite_layer.png)

**Competences:**
**Feature attribute selection and editing**

The first group of tools in the Attributes toolbar allows us to select features on the map using the mouse. The following screenshot shows the Select Feature(s) tool. We can select a single feature by clicking on it, or select multiple features by drawing a rectangle.

![](/fig/Select_Feature(s)_tool.png)

How to export selected features 
![](/fig/Export_selected_features.png)


**Attributes table editing**

The attribute table displays information on features of a selected layer. Features in the table can be searched, selected, moved or even edited. It is also possible to right-click on the layer and choose openTable Open Attribute Table from the drop-down menu, or to click on the openTable Open Attribute Table button in the Attributes toolbar. 

If you prefer shortcuts, **F6** will open the attribute table. **Shift+F6** will open the attribute table filtered to selected features and **Ctrl+F6** will open the attribute table filtered to visible features.

![](/fig/Opening_attribute_table.png)

* Right click the layer in the Layers Panel then click the Open Attribute Table menu option. Click the Toggle Editing Mode button. Click the New Field button. Input the field's Name, Type, and Length, then click the OK button.

![](/fig/New_fieldcolumn_creation_in_attribute_table.png)

![](/fig/Input_newfield_and_to_save_editing.png)


**Digital data creation**
* Digital can be created in points, lines, polygons and in shapefiles.

* Creation of point data
Click on the following numbers bottons as seen in the picture below. Number **1** will switch to edit mode, number **2** is to create a new entry point, number **3** is to move or copy point and number **4** is to delete entry point.

![](/fig/New_point_creation_data.png)

* Create  a  new  point:  Use  the  "Create  a  new  entity"  button  >  left-click  on  the  map > enter the attributes > click OK > a new point is created.
![](/fig/Naming_of_point_created.png)
You can name the point as you want and enter any number in the ID and click ok. The new point feature has been created and named which can be easily seen on the map.

* Creation of line data
The  method  is  similar  to  digitising  a  point  (see  above).This can be possible when you have firstly created a new line shapefiles layer. Remember to change the geometry type into lines because we are creating lines data now.

![](/fig/Creation_of_line_data.png)
Use  the  "Create  new  line"  button  and  click  several  times  on  the  map  (left  button)  to  draw  the  different parts of your line. When this is done, right-click to complete your line and access the Attributes window.> Complete the attributes and click OK

* Creation of polygon data
The method is similar to digitising a point or a line (see above).  Only  the  fourth  icon  changes  slightly:  this  one  corresponds to "Create a new polygon"
![](/fig/polygon_data_creation.png)
Please remember to firstly created a new polygon shapefiles layer so thatthe icon to create a polygon can be active and ensure you change the geometry type into polygons because we are creating polygon data now.


* Creation of new shapefile data
+ Go to Layer, Create Layer, New Shapefile Layer in the top menu.
+ In the New Shapefile dialog, specify the name and location for the new shapefile.
+ Select the geometry type for the shapefile from the Type dropdown (e.g. Point, line, Polygon).
+ Click the OK button to create the shapefile

![](/fig/New_shapefile_layer_creation.png)

* The new shapefile layer

![](/fig/New_shapefile_layer_naming.png)



** Digital data editing**

Select the layer in the Layers panel and click on Toggle Editing under Layer. Alternatively, you can right-click on a layer in the Layers panel and choose Toggle Editing from the context menu. Multiple layers can be edited at a time. The layer currently being edited is the one selected in the Layers panel.

![](/fig/Toggle_editingbox.png)

**Editing data - Data creation and deletion**
* To create or delete a field in your attribute table you need to be in edit mode, click on the Switch to edit mode button.

![](/fig/Switch_to_edit_mode_of_attribute_table.png)


* To add new data field; click on symbol circle 1 and to delete a data field; click on symbol circle 2

![](/fig/add_delete_data_in_attribute_table.png)

