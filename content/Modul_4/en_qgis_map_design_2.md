# Print layout

The print layout in QGIS is where you design and finalize the map in order to print or export it as a PDF or format of your choice. Here you can add important elements such as the legend, a title, an explanatory text and everything you need to create a comprehensive map. A QGIS project is not a map until all the layout elements (legend, title, scale bar, sources, etc.) are added. 

1. Go to __Project > New Print Layout > enter a name for the new print layout > click OK__
2. A new window witha blank print playout will appear.


```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

## Understanding the Print Layout Composer


```{figure} ../../fig/en_30.30.2_understanding_the_print_layout_composer.png
---
name: New Print Layout
---
The interface of the Print Layout Composer
```

1. __Layout Settings__ (Add pages, Export Map, manage panels)
2. __Dialer Tools__ (Save, New, Duplicate, Add items from template, Save template)
3.  __Navigation bar__ (Zoom, Refresh, Lock/Unlock elements)
4. __Toolbar__ (Zoom, Select, Move in Map, Add new map/image/text/legend/scale/shape/...)
5. __Feature Panel__: displays the elements added to the print layout
6. __Advanced Options__: customize each element of the layer

First of all, you should always set the size of your map:

- Right-click on the blank map > Page Properties
- Choose __the size of your document__ (A4, A3, A2)
- Choose the orientation (Landscape or Portrait)

_A4 and A3 are the most commonly used sizes for maps_

## Adding elements to the print layout

### Adding a new map

- Add a new map by clicking on the __Add map__ button on the __toolbar on the left__ and __drag a rectangle on the map canvas.  
- To move the map on the canvas, simply __select the map__ and __drag__ it with your mouse
- To move within a map select __Move item content__ button on the 
- To zoom in on the map, while using the __Move item content__ button, you can __Press CTRL + scroll the mouse wheel__ (gently) or enter the scale manually in the item properties


```{figure} ../../fig/en_30.30.2_adding_a_map.png
---
width: 750px
name: Add a new map
---
Adding a new map to the Print Layout
```
:::: {tab-set}
::: {tab-item} Adding a new map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_new_map
.mp4"></video>
:::

::: {tab-item} Moving and scaling the map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_moving_and_scaling_the_map
.mp4"></video>
:::
::::
### Adding a title or a text box

A title should describe the phenomenen represented on the map.

- To add text (title, explanations), use the __Add Label__ tool and draw a rectangle of the desired size.
- In the __Item Properties__ panel (on the right of your screen) you can __enter your text__ and __change the font, style, colour, etc.__ (_Remember to use the scroll bar in the window to see all the options). 

```{figure} ../../fig/en_30.30.2_print_layout_add_text.png
---
width: 750px
name: Add text to the print layout
---
Adding text to the print Layout
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_a_title
.mp4"></video>

### Adding an image

VIDEO

### Adding a legend

Before adding a legend, make sure that:

- All your layers have an explicit name ("rivers", "primary roads",...)
- You use the final version of your map (no more layers to add, move, rename or modify). You can still modify them later but you will have to redo the legend.

To add a legend, you can use the __add legend__ button on the __left toolbar__.


```{figure} ../../fig/en_30.30.2_print_layout_add_legend.png
---
width: 750px
name: Add a legend to the print layout
---
Adding a legend to the print layout
```

In the __item properties__ panel, if you keep the __'Auto update'__ option checked, new layers added to your project will automatically be added to the legend but you cannot control them individually (rename if necessary, reorder ot remove items).  
Once the option is unchecked, you can update the name of the layers, group them, reorganise them, etc.

:::: {tab-set}
::: {tab-item} Adding a legend

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_legend
.mp4"></video>

:::

:::{tab-item} Editing the legend

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_editing_the_legend
.mp4"></video>

:::
::::

### Adding a scale bar

Before adding a scale bar, select your main map and check in the __Item Properties__ panel that the __Scale__ fielld has a __round number__ 


```{figure} ../../fig/en_30.30.2_print_layout_scale.png
---
width: 750px
name: Round number for scale
---
Make sure that the scale is at a round number
```

To add a scale bar, you can use the __add scale bar__ button on the __left toolbar__. In the __Item Properties__ panel, customize the following functions

- Which Map __is related to the scale__
- __Unit system of the bar__ (metres, miles, degrees)
- __Segments on the left__: segments shown before 0 m (always set to 0). 
- __Fixed width__: define the width of each segment (e.g. 1 km, 10 km, 50 km, ...). 
- __Height__: height (thickness) of the scale bar

_There are many other options to customize the scale bar (change the font, colours, etc.)._ 

```{figure} ../../fig/en_30.30.2_print_layout_add_scale_bar.png
---
width: 750px
name: Add scale bar
---
Add and customize the scale bar
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_scale_bar
.mp4"></video>

### Adding an overview map

Adding an overview map in the corner of your map will help locate the area you are viewing on the main map.

To create an overview map, you need to follow these steps:

1. Prepare a __layer with national or subnational borders or important landmarks__ in your project (e.g: Administrative boundaries, Capitals)
2. __Insert the overview map__ into your print layout (in the bottom right corner for example)
3.  __Lock the new map__ in the Item properties panel
4. Add a rectangle to display the extent of your main map

    1. Go to the __properties__ of your Main map > scroll down until you see __"Overviews"__ 
    2. Add an Overview by clicking on the __"+" icon__
    3. __Link the main map__ by selecting it in the __"Map frame"__ option


```{figure} ../../fig/en_30.30.2_print_layout_overview_map_preparations.png
---
width: 500px
name: Overview map preparation
---
An overview map should show important landmarks and borders
```


```{figure} ../../fig/en_30.30.2_print_layout_add_overview_map.png
---
width: 750px
name: Add Overview map
---
Add an overview map and __lock the layer__
```


```{figure} ../../fig/en_30.30.2_print_layout_add_map_extent_overview_map.png
---
width: 750px
name: Create an Overview
---
Add a the extent of the main map to your overview map (the red rectangle on the overview)
```

:::{dropdown} Video: Setting up an overview map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_overview_maps
.mp4"></video>
:::

``` {Caution}
This method requires you to be sure that you are not going to modify the oveview map, as once the layers are locked, they will keep the style, and any updates will not affect the overview map.
```

## Exporting the print layout

Once you are finished with the map composition, it is time to export export the print layout as a PDF or SVG file. 

1. On the Toolbar click on the `Export as PDF`-button.
2. Give the new file a name and select the location you want to save it.
3. Click on `Save`.
4. A new window "PDF Export Options" will open. Here you can adjust the compression algorithm. For the best results, select the lossless image compression. 
5. Click `Save` again.
6. A new green bar will pop up underneath the toolbars. Click on the file link to __review the exported map__.

```{note}
Make sure to check the map after exporting the PDF as some design elements might have changed in the exporting process.
```

# The Atlas function (automatic map generation)

In some cases, it can be necessary to create multiple maps for different locations with the same layers. For example, if you have a detailed dataset on affected flood areas in Nigeria, you can create a more detailed map for each subnational district. In QGIS, this can be done automatically with the __Atlas Function__. 

The Atlas Function can be found in the __Print Layout Composer__ on the toolbar. 

```{figure} ../../fig/en_atlas_toolbar
---
name: Atlas Toolbar
width: 500 px
---
Atlas Toolbar
```

If you can't see the Atlas Tools, you must first activate the Atlas Toolbar under `View` > `Toolbars` > `Atlas Toolbar`

## Generate an Atlas

An Atlas will generate a new page with the same map layout for each feature in a layer. For most purposes, it useful to first create a map layout with the elements such as legend, sources and overview map and then insert the map item that will be controlled by the Atlas. To generate an Atlas:

1. Click on the Atlas Settings icon in the Atlas Toolbar
2. In the new window, activate the __Generate an Atlas__ option
3. Select the __Coverage Layer__. This will determine the features or polygons that will be displayed on a page. In our example, we will use the subnational administrative districts in Nigeria (`Adm1`). 
4. Select the __Page Name__. This should be the name of the subnational district or location that is displayed on that page. To display the name of the district, we will choose `ADM1_REF`.
5. Now let's add a map to the empty print layout.
6. Click on the map and navigate to the __Layer Properties__ window on the right.
7. Scroll down until you see the option `Controlled by Atlas` and activate it.
8. Now activate the preview of the Atlas in the __Atlas Toolbar__. Otherwise, the print layout will not update to show you the atlas page. You can click through each page to see how it looks. Depending on the amount of features on your map, they may take a while to render.
9. Now you can adjust the __Margin options__ to best fit the readibility of the map. By default, it is set to 10% and this should fit most purposes.
10. Before printing or exporting the atlas make sure to check every page that other elements of the map do not cover the represented region.

```{Note} 
For now the only item in the print layout that is being controlled by the Atlas is the Map we added. The other elements of the Map are the same on every page.
```

:::{dropdown} Video: Setting up an Atlas
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_an_atlas
.mp4"></video>
:::

## Setting up Overview maps with an atlas

Setting up Overview maps with an atlas works in the same way as setting it up for a normal map. As long as you select the Map controlled by the atlas as the `map frame`, it will update automatically.

# Good practices and common mistakes in mapping

In order to produce good maps, there are some __basic rules__ to follow and common __semiological mistakes__ to avoid. 

## Map composition

### Key elements of a map

A map is __never complete without the following elements__: 
- Title
- Legend
- Scale
- Orientation
- Source
- Localization (Overview) Map
- Author

```{figure} ../../fig/en_good_map_composition_example.png
---
name: good map composition example
width: 750px
---
Elements of good map composition
```

----

__The title__ summarizes in a few words the information represented on the map, giving the reader useful contextual information. Titles should include the following information:

- __The place__, with several degrees of precision according to the scale (Country, Region, Township,...)
- __The subject__ intelligible by all (make sure that the acronyms used are detailed elsewhere on the map)
- __the date__ of the represented data

_Examples:_ 

- _"Access to health care in Maputo, Mozambique in 2022"_
- _"Flooding Risk in Ghardaia, Algeria"_

__The legend__ is key to interpreting the information represented on the map. Without it, it is impossible to understand the meaning of the different symbols and colours used map. In order to guide the reader, the legend must be:

- __Comprehensive__: All the data on the map must be presented in the legend.
- __Representative__: the figures on the map and in the legend must match (same size, same color, ...).
- __Organized__: the data in the legend can be grouped by thematic categories (health, environment, background map, ...) or by type of figure (point, line, surface) to facilitate reading.

```{figure} ../../fig/en_legend_good_practice.png
---
width: 750px
name: Organized Legend
---
Example of a well organized legend
```

__The scale bar__ is essential to a map since it gives the correspondence between a distance measured on the map and the distance in the real world. There are two types of scales:
- __The numerical Scale__ is expressed as a fraction (1/25000 or 1:25000) which indicates the equivalence between 1 centimeter on the map and the real distance. It is a scale that can be calculated with GIS software, and is often found in topographic maps
    - A scale of 1:25000 means that 1 cm represents 25000 cm (or 250 meters) on the gound. 

- __the graphical scale__ is expressed by a line on the map, with an associated distance value. This scale is very useful to have an idea of the distances on the ground. The graphical scale will always be the correct size, even if a different printing format is used, since it will undergo the same transformation as the rest of the map

```{figure} ../../fig/example_scale_bar.png
---
name: scale bar
---
Scale bar examples
``` 
### Orientation

Even if by default the majority of the maps are oriented to the North, it is still necessary to specify the orientation of the map. It is often indicated by an arrow to the North. Sometimes the orientation of different in order to optimize the representation of the study area on the map.

### Sources

Any data represented on a map should have its sources indicated. This provides a record of the data used, but also references the author of the data. The reader will then be able to look for more information on the sources if he wishes. Open access geographic data, such as OpenStreetMap, are more and more numerous and must also be cited on the maps.  

It is possible to give the source of each data under the legend, or to do it in a dedicated space in the map. The level of precision of the sources varies according to the author or the precision of the data.


## The 4 semiological errors

### 1. Proportional circles vs. solid colors

```{caution}
DO NOT represent __quantitative__ stock character/data with a __solid color__.
```

This is one of the most common mistakes in mapping. While this representation is graphically appealing, it is still false and distracts from the message of the map.

It is a mistake because:

- You lose the __order relationship between the data__ (a circle can be twice as big as another one, a color cannot be "twice as dark")
- Countries with a large surface area stand out visually (eg.: Russia in the example below)
- We are trying to represent __data that has nothing to do with the area of a country__, but rather speaks of individual elements 

>Add different example

### 2. Color gradient vs. distinct color palette

```{caution}
DO NOT use a __separate__ color palette to represent __ordered entities__
```
A representatin that "feels right" because it seems logical that a "low" rate would be represented differently than a "high" rate.

It is a mistake because:
- By using a differentiating color variable, __you lose the ordinal relationship between entities__. Instead, a __gradient of the same color__ that should be used.
- Different colors are used to differentiate between distinct entities.

### 3. Gradient in a single color vs. Gradient between two colors
```{Caution}
DO NOT use a gradient across two colors for an always positive data.
```
This is a mistake that is often found because our brais are used to prioritizing certain colors, especially green to red, or blue to red. We must remember that __if our values are always positive, we must stay in the same color that will degrade into several shades. 
>What about height?

A gradient between two colors can be used when it is necessary to show a gradation that can go from negative to positive. As for temperatures, it makes sense to distinguish negative values (in shades of blue for example) and positive values (in shades of red). 

It is a mistake because: 
- By choosing different colors for values that are linked to each other, our eyes perceive a difference between the elements, and not an order.
- Darker colors stand out more than lighter colors, and can be perceived as more important.
- The map will send a message of divergence, of opposition between certain values, when we are simply trying to represent a hierarchy between values
- In this way, the color itself directly indicates information about the trend (positive/negative or increasing/decreasing).

### 4. Limited geometric symbols vs. complex icons and symbols
```{Caution}
DO NOT use __too many symbols__ in a thematic map
```
Incorportating a multitude of symbols (and data) for a informative map is a common desire. However, too many symbols can __overload the map__ and __reduce the readability__ of the map. Using too many symbols (especially geometric ones) can make it difficult to read and understand the map.  
__The eye can easily distinguish 4 to 5 different symbols. Beyond that, it is difficult to dinstinguish the elements. This is a less serious error because it does not convey false information on the map. 

It is a mistake because:
- It complicates the map and limits its impact. 
- Sometimes you are forced to represent several symbols, so you must be careful about overlapping points and overloading the map.