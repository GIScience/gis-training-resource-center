::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_module_4_exercises.html 
{octicon}`undo;1.5em;sd-text-danger`
:::
::::

# Exercise 1: Flooding in Cambodia


This exercise is designed to apply the basics of map design from Chapters 1, 2, and 3. Make sure to go through these chapters before starting this exercise. The corresponding subchapters and wiki-pages are linked if you need to refresh your memory.

Read the guide carefully and download the exercise data from the Nexus.

In the data folder, you will find several datasets.  The objective is to create a comprehensive atlas with maps for each region in Cambodia showing the flood extent and road network (including affected roads), with all the necessary map elements. 

:::{dropdown} Context: Flooding in Cambodia  

The floodplains of the Mekong and the Tonle Sap System in Cambodia experience yearly flood pulses that bring nutrients which sustain agriculture and fisheries. With the changing climate, the water levels of these floods have decreased, leading to a reduced reverse flow and a decrease in the flood duration of about 26 days (De Xun Cha et al. 2022). This trend will strain the food security in the region, affecting the livelihoods of a large portion of the population. Combined with the decline of the yearly flood pulse, major flood events can cause national health crises, damage infrastructure, displace thousands of people, and further exacerbate food insecurity in the region.
In 2013, following continuous rainfall in September, the Mekong and Tonle Sap Deltas flooded, displacing 144 thousand people. In 2011, more than 200,000 people have been displaced due to floods. Cambodia has experienced major flood events in 2020, 2022 and 2023 (IDMC 2023). 

Sources: 
Chua, S. D. X., Lu, X. X., Oeurng, C., Sok, T., & Grundy-Warr, C. (2022). Drastic decline of flood pulse in the Cambodian floodplains (Mekong River and Tonle Sap system). Hydrology and Earth System Sciences, 26(3), 609–625. https://doi.org/10.5194/hess-26-609-2022  
IDMC (International Displacement Monitoring Centre). (2022). Cambodia - Internal displacements (New Displacements) - IDPs. https://data.humdata.org/dataset/idmc-idp-data-khm (accessed 04.12.2023)

:::

## Objectives

The data provided contains shapefiles detailing the flood extent in October 2023, the road network, administrative boundaries, the Mekong and Tonle Sap Systems, as well as health facilities and airports. The goal is to design a map where the flood extent, road accessibility, and important landmarks such as health facilities, settlements, and airports are visible.

## Available Datasets


```{Tip}
If you need inspiration on how to style certain elements of your map, make sure to check out the chapter [Examples for Flood Map Design](/gis-training-resource-center/content/Module_4/en_qgis_map_examples.md) 
```

## Step 1: Preparing the layers

1. Load the layers into QGIS and make yourself familiar with the data by opening the attribute table () 
2. Arrange the layers such that no layer is blocked 

## Step 2: Set the symbology for the individual layers

1. First, let's style the administrative boundaries. We want to keep it simple and keep the polygon of the adm1 with a transparent filling, but with a thicker outline. On top of that layer, we want to see the adm2 boundaries, but with a thinner (or even dashed) outline
2. The flood extent needs to be immediately recognizable. Choose a colour and filling style (Simple Fill or hashed line fill)
3. The river system and lake should be symbolised with a associative colour to be immediately recognizable.
4. The road network shapefile has the attribute `Flooded` with the Value `Y` if the extent of the flood crosses the road. Set the symbology of the road network so roads are easily distinguishable and that the reader can identify which roads are potentially flooded.
5. Decide how you want to display settlements and health facilities (link to SVG-symbols)
6. Set up the labels for the settlements and administrative districts
7. Set up the background to make the area of focus stand out.
8. In mountainous areas, it can be helpful to add a hillshade to determine the accessibility and travel time by car. 

```{Tip} Saving the styles
If you are happy with the styles you have set up for your layers, you can save the style and add it to your style library.
```

## Step 2: Starting the Print Layout

1. Add your Map to the Print Layout. Make sure to leave some space for the other map elements such as sources, legend, overview map, logo, etc.
2. Adjust the Scale of the Map in the Item properties (if possible to a round number)
3. Add a scale bar
5. Add a title. The title should make it clear what the map displays.
4. Add a legend. Make sure to remove layers which are not visible on the map and rename the elements accordingly.
5. Add a compass to show map orientation.

## Step 3: Setting up the Overview Map

1. Once you are done with the main map, __make sure to lock the layer and the styles for your main map (`Map 1`)__. Otherwise the map will update when setting up the overview map.
3. Navigate back to the main QGIS-Window.
4. Copy the layers for the overview map. In this case, the `Adm1`-layer. This way, you will not loose the style for the layers on your main map. Adjust the style on the copied layer for your overview map.
5. Navigate back to the print layout.
6. Add a second map as your overview map (preferably somewhere in the corner)
7. Set it up as an overview map.
8. Lock the layers and lock the styles.

## Step 5: Adding the other elements of a map


1. Add the sources of the datasets
2. Add a text to describe what the map shows.
3. Add your name and/or organisation as authors.


```{Tip}
If you are happy with the layout of your print layout, don't forget to save it as a preset for future use.
```

## Step 6: Exporting the map

Once you are happy with the print layout, it is time to export the map as a PDF-file (link). Once exported, open the file in your PDF viewer and check if everything looks as intended. In QGIS, some elements of the map might change slightly in the exporting process, so it is important to check before sending the map to your colleagues or publishing. 

```{Tip}
To avoid too many changes when exporting the map, set the 
```
