# Digitalisation

## What is Digitization?

Digitization is the process of converting geographic (raster) data into digital form (vector data). During this process, spatial data on maps or images are traced as points, polylines or polygons. Digitization is one of the important tasks for a GIS specialist and it has many uses in GIS, including recording and displaying geographic information, generating map layers, and storing data. Digital datasets usually contain data that can be represented as numbers or symbols such as text or graphics. The process can also involve converting analogue images into digital ones. Digitization in GIS can be integrated with many other software applications like CAD (Computer-Aided Design), 3D modelling, etc. [Source](https://www.spatialpost.com/what-is-digitization-in-gis/#0-types-of-digitization-in-gis-what-is-digitization-in-gis)


## Uses of Digitizing in QGIS

•	The digital map has become one of the most efficient tools for surveying and analyzing data across industries especially for geologists, geographers, urban planners, etc.

•	It allows managers and staff members to easily access information when needed.

•	Digitization often make it easier for companies to make the edits by importing the digitized data into a PDF or jpg format whenever there are changes that need to be made to the QGIS file.

•	It also gives decision-makers access to maps in their preferred format such as PDF and jpg when needed.

•	Digitization has made it possible to store and process data at a much faster rate.

•	It also provides more flexible data input and improve efficiency of ever-changing spatial information.

## Digitization toolbars

Firstly, you need to check if Digitizing Toolbox is activated in your QGIS in order to digitize. If not then you can activate it using following process.

 1. Click view tab in the menu bar and click toolbar and then check digitizing and advance digitizing tool box.
 
 ![](/fig/Activate_digitizing_toolbox.png)

 A tool box like this should appear on top of your Qgis 
 
 ![](/fig/Toolbox.png)


 ## Digital data creation

* Digital can be created in points, lines, polygons and in shapefiles.

### Creation of point data

Click on the following numbers bottons as seen in the picture below. Number **1** will switch to edit mode, number **2** is to create a new entry point, number **3** is to move or copy point and number **4** is to delete entry point.

![](/fig/New_point_creation_data.png)

* Create  a  new  point:  Use  the  "Create  a  new  entity"  button  >  left-click  on  the  map > enter the attributes > click OK > a new point is created.

![](/fig/Naming_of_point_created.png)

You can name the point as you want and enter any number in the ID and click ok. The new point feature has been created and named which can be easily seen on the map.


### Creation of line data

The  method  is  similar  to  digitising  a  point  (see  above).This can be possible when you have firstly created a new line shapefiles layer. Remember to change the geometry type into lines because we are creating lines data now.

![](/fig/Creation_of_line_data.png)


See video of line data creation

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Line_data_creation.mp4"></video>


```{Note} 
Try:
```
Use  the  "Create  new  line"  button  and  click  several  times  on  the  map  (left  button)  to  draw  the  different parts of your line. When this is done, right-click to complete your line and access the Attributes window.> Complete the attributes and click OK

### Creation of polygon data

The method is similar to digitising a point or a line (see above).  Only  the  fourth  icon  changes  slightly:  this  one  corresponds to "Create a new polygon"

![](/fig/polygon_data_creation.png)

```{Tip}
Caution:
```

Please remember to firstly created a new polygon shapefiles layer so thatthe icon to create a polygon can be active and ensure you change the geometry type into polygons because we are creating polygon data now.


See video of polygon data creation

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/polygon_data_creation.mp4"></video>


### Creation of new shapefile data

+ Go to Layer, Create Layer, New Shapefile Layer in the top menu.
+ In the New Shapefile dialog, specify the name and location for the new shapefile.
+ Select the geometry type for the shapefile from the Type dropdown (e.g. Point, line, Polygon).
+ Click the OK button to create the shapefile

![](/fig/New_shapefile_layer_creation.png)

* The new shapefile layer

![](/fig/New_shapefile_layer_naming.png)

## Create Layer

Now add some layers for drawing. Click layer in the menu bar, select create layer and select **new spatialite layer** or select **new shapefile layer** if you have to digitize a single feature like some places or roads or buildings. We are choosing new spatialite layer because we want to draw more than one feature in single file and it is easy to transfer this file.

**Next**

Click ‘…’ browse button and save your database. Give name to your layer, select type of layer and specify attributes and their type such as text or numerals and click add attributes to the list and click OK. Specify CRS of the layer same as the CRS of Raster data.

 ![](/fig/New_spatialite_layer.png)


## Digital data editing

Select the layer in the Layers panel and click on Toggle Editing under Layer. Alternatively, you can right-click on a layer in the Layers panel and choose Toggle Editing from the context menu. Multiple layers can be edited at a time. The layer currently being edited is the one selected in the Layers panel.

![](/fig/Toggle_editingbox.png)


### Feature attribute selection and editing

The first group of tools in the Attributes toolbar allows us to select features on the map using the mouse. The following screenshot shows the Select Feature(s) tool. We can select a single feature by clicking on it, or select multiple features by drawing a rectangle.

![](/fig/Select_Feature(s)_tool.png)

* How to export selected features

![](/fig/Export_selected_features.png)


## Editing data - Data creation and deletion

* To create or delete a field in your attribute table you need to be in edit mode, click on the Switch to edit mode button.

![](/fig/Switch_to_edit_mode_of_attribute_table.png)


* To add new data field; click on symbol circle 1 and to delete a data field; click on symbol circle 2

![](/fig/add_delete_data_in_attribute_table.png)


## Attributes table editing

The attribute table displays information on features of a selected layer. Features in the table can be searched, selected, moved or even edited. It is also possible to right-click on the layer and choose openTable Open Attribute Table from the drop-down menu, or to click on the openTable Open Attribute Table button in the Attributes toolbar. 

If you prefer shortcuts, **F6** will open the attribute table. **Shift+F6** will open the attribute table filtered to selected features and **Ctrl+F6** will open the attribute table filtered to visible features.

![](/fig/Opening_attribute_table.png)

* Right click the layer in the Layers Panel then click the Open Attribute Table menu option. Click the Toggle Editing Mode button. Click the New Field button. Input the field's Name, Type, and Length, then click the OK button.

![](/fig/New_fieldcolumn_creation_in_attribute_table.png)

![](/fig/Input_newfield_and_to_save_editing.png)


## Digitization Errors in QGIS

Positional errors are inevitable when data are manually digitized. The most common examples include undershooting and overshooting.  When your coordinates do not connect as they should, and overshooting, when the lines go past where they should. Often these errors are not visible unless you zoom in quite a bit on the coordinates. Setting a fuzzy tolerance (snapping tolerance) is used to reduce undershoots and overshoots. The snapping tolerance is the minimum tolerated distance between nodes, lines and/or vertices.

![](/fig/Digitization_Errors.PNG)


