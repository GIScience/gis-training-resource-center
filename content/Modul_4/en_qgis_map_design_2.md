# Print layout

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

The print layout in QGIS is where you design and finalize the map in order to print or export it as a PDF or format of your choice. Here you can add important elements such as the legend, a title, an explanatory text and everything you need to create a comprehensive map. A QGIS project is not a map until all the layout elements (legend, title, scale bar, sources, etc.) are added. 

1. Go to __Project > New Print Layout > enter a name for the new print layout > click OK__
2. A new window with a blank print playout will appear.


```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

## Map composition

A good map guides the reader in understanding the information available on the map, makes the information easily accessible and is not overloaded with information. 

In General, there are a few things to keep in mind when creating a map:
- The main map should cover the largest portion of the page and be centred.
- A complete map must have a legend, the sources, a title, the scale, as well as other information to contextualize the information presented on the map.
- Additional information, such as title, sources, scale bar, legend, orientation, etc. should be scaled accordingly. 
    - Titles should be large so the reader can identify it as the main topic of the map.
    - Additional information should be smaller and moved out of the main focus of the page (e.g. at the bottom, to the sides, or in the corners).
- A well structure page layout helps the reader discern the different information on the map and makes it easier to know where to look for certain information. Frames and boxes can structure the page layout. For example, a legend can be put on the bottom or to the right of the map. 

In the [next chapter](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_examples.html), we will take a look at good map design and discuss how to recreate design elements. 

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


# Map templates

Map templates can facilitate and reduce the creation of a print layout. Map templates save the arrangement of elements in the print layout. However, they do not save the layers and images of the project. These will need to be reconfigured again.
If you work for an organisation that frequently publishes maps, or you need to create several maps on the same topics but in different regions or times, you can use map templates to skip the arrangement of elements.

```{note}
The individual layers, maps and images are not saved in the template. However, if you have the same layers in the project you load the template into, the legend will update accordingly. 
```

# The Atlas function (automatic map generation)

In some cases, it can be necessary to create multiple maps for different locations with the same layers. For example, if you have a detailed dataset on affected flood areas in Nigeria, you can create a more detailed map for each subnational district. In QGIS, this can be done automatically with the __Atlas Function__. 

The Atlas Function can be found in the __Print Layout Composer__ on the toolbar. 

```{figure} ../../fig/en_atlas_toolbar.png
---
name: Atlas Toolbar
width: 500 px
---
Atlas Toolbar
```

If you can't see the Atlas Tools, you must first activate the Atlas Toolbar under `View` > `Toolbars` > `Atlas Toolbar`

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

__The scale bar__ is essential to a map since it gives the correspondence between a distance meas ured on the map and the distance in the real world. There are two types of scales:
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

### 4. Limited Geometric Symbols vs. Complex Icons and Symbols
```{Caution}
DO NOT use __too many symbols__ in a thematic map
```
Incorportating a multitude of symbols (and data) for a informative map is a common desire. However, too many symbols can __overload the map__ and __reduce the readability__ of the map. Using too many symbols (especially geometric ones) can make it difficult to read and understand the map.  
__The eye can easily distinguish 4 to 5 different symbols. Beyond that, it is difficult to dinstinguish the elements. This is a less serious error because it does not convey false information on the map. 

It is a mistake because:
- It complicates the map and limits its impact. 
- Sometimes you are forced to represent several symbols, so you must be careful about overlapping points and overloading the map.
