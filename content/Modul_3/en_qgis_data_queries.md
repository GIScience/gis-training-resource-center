# Geodata Selection and Queries

## Geodata queries

Spatial queries allows you to select features in layers by their spatial relationships (intersect, contain, touch etc.) with features from another layer. In Qgis, this functionality is available via the selection by location and extract by location processing tools.

### Spatial queries: select by click

This section demonstrate how to select an area or location by just a click and view its spatial features. Below is a map of Nigeria. Click on the icon number 1 which is the select feature and click on any part of the map that you want to select. See point number 2 which has already shown yellow as the selected area. Open the attribute table through the layer pannel, number 3 and click on number 4 to just view the feature of the selected part by clicking on selected features, then you arrive at number 6 which display only selected features.

![](/fig/Select_by_click.png)

See video of select by click

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Select_by_click.mp4"></video>



### Spatial queries: select by polygon

This section is similar to selection by click. Only that you will select features by polygon from number 1 and draw the polygon on the area you want to cover or view and then right click. you will see that the polygon area will be selected in yellow color just like number 3. View the attribute table and click on number 6 to show only selected features in the polygon that you have created. You can use icon number 7 to deselect features. 

![](/fig/Select_by_polygon.png)

See video of select by radius

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Select_by_radius.mp4"></video>


### Spatial queries: select by location

This section can not only be used to show the features but also to get visual idea of the spatial relationship of different areas together. It has several spatial query operations which includes intersect, contain, disjoint, equal, touch, overlap, are within and cross.

 * Example below shows how to select by location by intersect. We want to see the spatial relationship between Nigeria and its neighboring countries in term of intersect by location.

* Click on icon number 1 and select by location. You will select features from which area or shapefile you want from icon 3 and icon 5 as the shapefile you want to intersect with. Icon 4 shows the various operations that can be down with select by location. Then click on run - icon 6, and and close to see the intersect on display.

![](/fig/Select_by_location_intersect.png)

* The below screenshot shows the four countries that intersect Nigeria in yellow color. You can as well check the features of these four countries by opeing attribute table and view selected features.

![](/fig/Select_by_location_intersect_output.png)


See video of select by location with intersect

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Select_by_location_intersect.mp4"></video>


Additionally, you can play around all the geometric predictions of the features to be familiar with them. The example below shows selection by location by disjoint. We loaded neighboring countires to be disjointed from Nigerian map and now you can see all the disjointed countries in yellow color. 

![](/fig/Select_by_location_disjoint.png)

You can see the features of those countries by attribute table and show selected features.



## Non-spatial queries

Non-spatial queries describe characteristics of the features and this query show a place or feature irrespective of its location i.e. **what** instead of **where**. It is totally independent of geographic location and not relating to, occupying, or having the character of space. Non-spatial queries are crucial for analyzing and understanding the data associated with the spatial features in a GIS project, providing insights and facilitating decision-making based on non-spatial attributes. Non-spatial data is also known as attribute data.

There are two ways by which you can select and show the features of non-spatial data. Among which are manual selection or just by click and select by expression (arithmetic operators, string operators, logical operator etc.).


### Manual selection

We want to manually select three regions in the below vector layer through the attribute table. Open the attribute table, select any of the place you would like to select, press control bottom on your PC and click on any other features you would like to select. Then, you can click on show selected features and it will be automatically highlighted in yellow color on the Qgis display panel.


![](/fig/Manual_select_by_attribute_table.png)


See video
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Manual_selection.mp4"></video>




### Select by Expression

You can use the “Select by expression” option in the **layer properties** (see icon 1) or through the **Select** menu in the attribute table (see icon 2) to apply an expression to a layer. Sometimes, you can also find the icon of select by expression at (see icon 3) by click on it and choose select features by expression or just by Ctrl plus F3 on your key board. This option can be used to select features based on attribute data. Icon 4 is the select by expression command prompt where your expression will be written.

![](/fig/Opening_Select_by_Expression.png)



### Select by Expression- Arithmetic operators (integer, float fields)

•	>, <, =, !=

•	Note that your command in the select by expression depend on the attribute features on the shape file you want express.

•	For example, imagine that you want to show the State that has more than 10 million **shape-length** in the below map of Nigeria showing its 37 States.

1.	Firstly, select your file from the layer panel, open the select by expression table, click on Fields and Values (don’t forget that these fields and values depends on the characteristics of the file you are opening).
2.	Scroll down to shape length and double click on it, you can then see it at the expression layer display.
3.	Go back to the search bar layer by click on the operators to select the arithmetic command you would like to use. In this case, we are using > sign because we want to figure out the state that has more than 10 million for instance.
4.	After double click on the greater than sign, then input the numeric command that you want to use. In this case we enter 10.
5.	Lastly, click on select features. It will automatically select all the states that have more than 10 million in its shape length. You can as well see the number of selected features at the top of the select by expression command prompt layer. Then open the attribute table to see the selected features.


![](/fig/Select_by_Expression_greater_a.png)


The below are the thelve features selected.

![](/fig/Select_by_Expression_greater_b.png)


See video

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Select_by_expression_arithmetic_operators.mp4"></video>



### Select by Expression- String operators (text fields e.g “Like”)

•	Imagine you want to select a country like Nigeria.

![](/fig/Select_by_Expression_like.png)

To select by expression by like, please follow this steps:
1.	Select the file you would like to run
2.	Click on select by expression
3.	Click on Fields and Values
4.	Select admin0Name (This means names of the countries according to the attribute table fields names)
5.	Click on Operators to select the command you would like to use
6.	Select ‘Like’
7.	Click again on the Fields and Values
8.	Click on All Unique
9.	Select Nigeria i.e. we want to express to select a country like Nigeria
10.	Click on select features
11.	You call all see the expression command here
12.	A country like Nigeria has been selected and you can open the attribute table to see the selected feature(s).



### Select by Expression- Placeholder (e.g %)

•	Imagine you want to select all the countries that ends with **’a’**

![](/fig/Select_by_Expression_placeholder.png)

1.	Follow the previous steps.
2.	You have three input to express here. Click on Fields and Values to select admin0RefName (Name of the countries title as per the attribute table)
3.	Go to operators to select Like
4.	You can enter manually at the expression layer ‘%a’ (i.e. the countries that ends with a)
5.	Click on Select features to see all the countries that ends with **a**.


### Select by Expression- Logical operators (AND, OR)

This selection adds one or two command expression together. For example, you want to select the state that has more than 12 million in shape length AND that has more than 3 million shape area simultaneously from the map of 37 States of Nigeria. Then this command holds: **"Shape Length" > 12 AND  "Shape_Area" > 3** .


![](/fig/Select_by_Expression_AND.png)


You can get it down by a click on Fields and Values, proceed to click on Shape length and input your arithmetic operator > with the figure of your choice via Operators, then add the connector which is **AND** and go back to Fields and Values to input the second command of Shape area and add the arithmetic operator of > with the figure you want. Lastly, click on select features to see the states that have shape length of more than 12 million and at the same time having shape area of more than 3 million. Visit the attribute table to see the selected features.


## Save selected features

How to save selected features as a new file?

You can save the selected features as a new shape file.
1.	Click on Layer properties
2.	Click on Export
3.	Save only selected features

![](/fig/Save_selected_features_by_export.png)

•	Right click on the shape file you want to save the selected features from in the Layers panel
•	Click on export
•	Save selected features as
•	A save vector layer will pump up and you can change the Format if you want but in this case we are using GeoPackage format
•	Click on file name to properly save it in the folder of your choice on your PC
•	Click on save only selected features
•	Click on Ok.
•	Then, it will automatically appear on your Layer panel as seen below.

![](/fig/Save_selected_features_by_export_a.png)


The video below shows how to export and save selected features.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Saved_selected_features.mp4"></video>

