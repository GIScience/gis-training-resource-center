# Examples for Good Map Design

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

In this chapter we will go over some common mistakes and good practice in map design. A second part of this chapter will be dedicated to discuss well designed maps and give examples on how to recreate the design in QGIS.

> TO DO:  
Insert Overview  
Insert links to the tutorial content/wiki

In this section, we will present some well designed maps and discuss how to create similar maps. If you need further examples for good map design, check out these websites/repositories: 
- [researchresourcecentre.info maps](https://www.reachresourcecentre.info/search/?search=1&initiative%5B%5D=reach&ptype%5B%5D=map&dates=&keywords)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://reliefweb.int/updates?advanced-search=%28S1242%29_%28F12%29)


## Map Examples
### Map Example 1: Flood-affected areas and roads in the Somali Region, Ethiopia

```{figure} ../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: Flood affected Areas in Somali
width: 800 px
---
Flood affected areas and roads in Somali Region, Ethiopia (Source: OCHA)
```

The map above shows the flood affected areas, as well as the important road networks in the Somali Region, Ethtopia, in November 2023. Maps such as these are crucial for humanitarian aid workers when planning relief or aid operations and need to be up to date. They display important settlements, and most importantly, the accessibility of roads and airstrips. 

This is a thematic map with a clear purpose and the elements on the map are reduced to the most necessary elements relevant to the purpose of the map.


- A shapefile for the flood affected areas was given a hashed fill. In QGIS, you can find this symbology 
- A layer with the road network has been put above the layer with the flood-affected areas. The road symbology has been __categorized__ into three categories: Accessible road (green), partially accessible road (grey), and hard to reach road (red).
- The topmost layer is a point-layer with information on unaccessible roads or bridges as well as the location of airstrips and which airstrips are accessible. The points have been symbolized with SVG-symbols. 
- (The administrative boundaries of Ethiopia are set apart from the surrounding countries by making the polygon a clear white and the surrounding countries in a shade of grey. This can be achieved by copying the polygon of Ethiopia into a new layer, and changing the symbology respectively)

```{note} 
The colour scheme of the roads makes an intuitive reading of the map possible, as red is associated with negative qualities, whereas green with positive qualities. It should be noted, however, that persons with colourblindness will have trouble reading the map.
```

:::{dropdown} Context: Situation in Ethiopia

:::

---

### Map Example 2: Flooding Risk in the Ouham Region, Central African Republic

```{figure} ../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
---
name: flooding risk
width 800 px
---
Flooding risk in the Ouham Region, Central African Republic (Source: REACH)
```

This map displays the flooding risk using a raster image. The raster data was calculated using several factors, including the precipitation intensity, the maximum duration of precipiation, the height of the nearest drainage, the flow direction and river network, the topographic humidity, a digital elevation model and the ground cover. 

- The raster data is displayed using a diverging colour ramp. (Here you can check out how to assign a colour ramp) 
- The surrounding administrative districts have been overlayed with a transparent grey. 
- The river network has been added in blue
- The mainroads as well have been added in black
- Settlements are displayed i black dots. This helps to identify areas whith a higher population density in the areas most at risk

:::{dropdown} Context: Situation in the Central African Republic

:::

---
### Map Example 3:

```{figure} ../../fig/REACH_AFG_Map_ABR_infrastructure_mapping_Kunduz_Kunduz_PD-07_17May2022_A3P.png
---
name: Infrastructure Map Kunduz District Afghanistan
width: 800 px
---
Infrastructure Map Kunduz Province 
```

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
