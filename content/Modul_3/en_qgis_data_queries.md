# Geodata Selection and Queries

**Geodata queries**

Spatial queries allows you to select features in layers by their spatial relationships (intersect, contain, touch etc.) with features from another layer. In Qgis, this functionality is available via the selection by location and extract by location processing tools.

**Spatial queries**: select by click

This section demonstrate how to select an area or location by just a click and view its spatial features. Below is a map of Nigeria. Click on the icon number 1 which is the select feature and click on any part of the map that you want to select. See point number 2 which has already shown yellow as the selected area. Open the attribute table through the layer pannel, number 3 and click on number 4 to just view the feature of the selected part by clicking on selected features, then you arrive at number 6 which display only selected features.

![](/fig/Select_by_click.png)




**Spatial queries**: select by polygon

This section is similar to selection by click. Only that you will select features by polygon from number 1 and draw the polygon on the area you want to cover or view and then right click. you will see that the polygon area will be selected in yellow color just like number 3. View the attribute table and click on number 6 to show only selected features in the polygon that you have created. You can use icon number 7 to deselect features. 

![](/fig/Select_by_polygon.png)


**Spatial queries**: select by location

This section can not only be used to show the features but also to get visual idea of the spatial relationship of different areas together. It has several spatial query operations which includes intersect, contain, disjoint, equal, touch, overlap, are within and cross.

 * Example below shows how to select by location by intersect. We want to see the spatial relationship between Nigeria and its neighboring countries in term of intersect by location.

* Click on icon number 1 and select by location. You will select features from which area or shapefile you want from icon 3 and icon 5 as the shapefile you want to intersect with. Icon 4 shows the various operations that can be down with select by location. Then click on run - icon 6, and and close to see the intersect on display.

![](/fig/Select_by_location_intersect.png)

* The below screenshot shows the four countries that intersect Nigeria in yellow color. You can as well check the features of these four countries by opeing attribute table and view selected features.

![](/fig/Select_by_location_intersect_output.png)

Additionally, you can play around all the geometric predictions of the features to be familiar with them. The example below shows selection by location by disjoint. We loaded neighboring countires to be disjointed from Nigerian map and now you can see all the disjointed countries in yellow color. 

![](/fig/Select_by_location_disjoint.png)

You can see the features of those countries by attribute table and show selected features.




* Non-spatial queries (I/basic)