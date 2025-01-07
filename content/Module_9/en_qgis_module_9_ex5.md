🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

# Task 5: Identifying critical road segments

For this task, we imagine that the city of Heidelberg is partially affected by flooding of the Neckar. Such scenarios are becoming increasingly likely in the future due to climate change. The flood has a major impact on the city's infrastructure. In this exercise, you will use QGIS to analyze the impact of the flood by determining the betweenness centrality of multiple nodes in the city before and after the flooding event.

Download all datasets __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_9/Modul_9_Exercise_5_Identifying_critical_road_segments/Modul_9_Exercise_5.zip)__. 
 Save the folder on your computer. 
 Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. 
 Under "data > input" you find the following datasets:


- `highways.gpkg` (points): Road network of Heidelberg
- `flood_area.gpkg` (polygons): Flood simulation of Heidelberg



### STEP 1: Dissolve Layer

First we want to dissolve the `highways` layer to combine all the LineString geometries to one LineString. This is important for determining the betweenness centrality in the future steps.

Open the **Processing Toolbox** and search for **Dissolve**. Select the `highways` layer as the Input Layer and leave all other settings at default. 

### STEP 2: Betweenness Centrality - Before Flood

Make sure you installed the GRASS GIS provider Plugin. If you don't know how to install Plugins, click here: {ref}`content:references:wiki:plugins`

To determine the betweenness centrality open the **Processing Toolbox**, choose **GRASS**, then choose **Vector** and finally scroll down to **v.net.centrality**. Select the `Dissolved` Layer from Step 1 and leave all other settings at default. After the calculation you receive a new Point layer called `Network Centrality`.

Now you want to make the difference between the values visible for interpretation. Therefore click **F7** to open the **Layer Styling**. There you can choose the new `Network Centrality` Layer and change `Single Symbol` to `Graduated`.  You must select **betweenness** as your `Value` and finally click `Classify`. 

```{Tip}
To make the differences of the values more visible, you can change the Classification `Mode` from **Equal Count (Quantile)** to **Natural Breaks (Jenks)**.
```
`````{admonition} Question
Can you identify critical road segments of the city with higher centrality values by looking at the different nodes? What does this mean for the infrastructure of Heidelberg?
`````

### STEP 3: Betweenness Centrality - After Flood

In a next step, we want to carry out the same analysis after the flood event in order to determine the impact of the flood on the infrastructure in Heidelberg. To do so, we first have to delete the part of the `highways` layer that is flooded. 

Open the **Processing Toolbox** and search for **Difference**. Select the `Dissolved` layer as the Input Layer and the `flood_area` layer as the Overlay Layer. Leave all other settings at default. After the calculation you receive a new LineString layer called `Difference`.

Repeat the analysis from Step 2 to determine the betweenness centrality of the `Difference` Layer. 

```{Tip}
To make the values of the two Point Layers more comparable, right click on your second `Network Centrality` Layer, choose `Styles`, `Copy Styles` and then `All Style Categories`. Then right click on your first `Network Centrality` Layer, choose `Styles`, `Paste Styles` and then `All Style Categories`. Now the two layers share the same classification for comparison.
```
`````{admonition} Question
Can you identify new critical road segments of the city with high centrality values? How did the range of the values change due to the flood? How did the flood event influence the infrastructure of Heidelberg in general?
`````
