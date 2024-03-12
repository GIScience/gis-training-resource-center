# Task 5: Identifying critical road segments

For this task, we imagine that the city of Heidelberg is partially affected by flooding of the Neckar. Such scenarios are becoming increasingly likely in the future due to climate change. The flood has a major impact on the city's infrastructure. In this exercise, you will use QGIS to analyze the impact of the flood by determining the betweenness centrality of multiple nodes in the city before and after the flooding event.

Use the following files:
* highways.gpkg
* flood_area.gpkg

### STEP 1: Dissolve Layer

First we want to dissolve the `highways` layer to combine all the LineString geometries to one LineString. This is important for determining the betweenness centrality in the future steps.

Open the **Processing Toolbox** and search for **Dissolve**. Select the `highways` layer as the Input Layer and leave all other settings at default. 

### STEP 2: 

Make sure you installed the GRASS GIS provider Plugin. If you don't know how to install Plugins, click here:{ref}`content:references:wiki:plugins`




Valentins show

- dissolve layer
- GRASS v.net.centrality
- interpretieren zwischenresultate
- Difference mit Floodlayer (flood simulieren)
- Zentralität mit neuem layer
- interpretation der unterschiedlichen Layer
