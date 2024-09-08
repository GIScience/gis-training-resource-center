# Examples of Good Map Design

🚧This page on the training platform and the entire content is under ⚠️construction⚠️🚧

In this chapter we will discuss well designed maps and give examples of how to recreate specific design elements in QGIS. A second part of this chapter will focus on common mistakes and good practices when designing maps.

<!--TO DO:  
Insert Overview  
Insert links to the tutorial content/wiki
Insert examples in the 4 semiological errors part
-->

In this section, we will present some well-designed maps and discuss how to create similar maps. If you need further examples for good map design, check out these websites/repositories:

- [researchresourcecentre.info maps](https://www.reachresourcecentre.info/search/?search=1&initiative%5B%5D=reach&ptype%5B%5D=map&dates=&keywords)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://response.reliefweb.int)

## Map Examples

### Map Example 1: Flood-affected areas and roads in the Somali Region, Ethiopia

```{figure} ../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: Flood affected Areas in Somali
width: 800 px
---
Flood affected areas and roads in the Somali Region, Ethiopia (Source: OCHA)
```

:::{dropdown} Context: Situation in Ethiopia
The Greater Horn of Africa receives 20 to 70 percent of the annual total rainfall in the months from October to December. The IFRC reports a exceptionally high forecast probability (over 80%) of experiencing wetter than normal rainfall condition. Additionally, El Niño conditions started between July and August, which further accrued the possibility of high rainfall conditions in Ethiopia.

Since October, floods have affected at least 763,000 people in the region, taken 33 lives in the Somali Region alone, and killed 4,806 livestock. The flooding has also resulted in immense damage to infrastructure, transportation, and schooling. The population's livelihood and health have been greatly affected.
The impact of flooding is projected to increase in the next years, which will lead to more flash and river floods.

Access maps, such as the one above, play a crucial role in helping informing information manager and ground staff which areas are accessible. This is especially important as a timely deployment of relief or aid operations is essential in flooding disasters.

(Source: [IFRC](https://go.ifrc.org/emergencies/6773/details))
:::

The map above shows the flood-affected areas, as well as the important road networks in the Somali Region, Ethiopia in November 2023. Maps such as these are crucial for humanitarian aid workers when planning relief or aid operations and need to be up-to-date. They display important settlements and, most importantly, the accessibility of roads and airstrips. 

This is a thematic map with a clear purpose, featuring only the most essential elements relevant to that purpose.

- A shapefile for the flood affected areas was given a hashed fill. In QGIS, you can find this symbology.
- A layer with the road network has been put above the layer with the flood-affected areas. The road symbology has been __categorised__ into three categories: Accessible road (green), partially accessible road (grey), and hard-to-reach road (red).
- The topmost layer is a point-layer with information on unaccessible roads or bridges as well as the location of airstrips and which airstrips are accessible. The points have been symbolized with SVG-symbols. 
- (The administrative boundaries of Ethiopia are set apart from the surrounding countries by making the polygon a clear white and the surrounding countries in a shade of grey. This can be achieved by copying the polygon of Ethiopia into a new layer, and changing the symbology respectively)

```{note} 
The colour scheme of the roads makes it possible to read the map intuitively, as red is typically associated with negative qualities and green with positive qualities. It should be noted, however, that people with colourblindness will have trouble reading the map.
```

---

### Map Example 2: Flooding Risk in the Ouham Region, Central African Republic

```{figure} ../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
---
name: REACH Flooding Risk Ouhman Region, Central African Republic
width: 720 px
---
Flooding risk in the Ouham Region, Central African Republic (Source: REACH)
```
:::{dropdown} Context: Situation in the Central African Republic

The Central African Republic has been hit by destructive floods in late 2019, which displaced over 100,000 people and caused considerable damage to infrastructure. The floods have destroyed shelters, obstructed transportation routes, and have led to disease outbreaks such as cholera and malaria. Due to climate change, such floods will become more frequent, leading to increased vulnerability for towns and villages. Since natural hazards are hard to predict, the changing climate reduces community resilience.

Source: [REACH Initiative](https://reliefweb.int/report/central-african-republic/central-african-republic-flood-susceptibility-risk)
:::

This map displays the flooding risk using a raster image. The raster data was calculated using several factors, including the precipitation intensity, the maximum duration of precipitation, the height of the nearest drainage, the flow direction and river network, the topographic humidity, a digital elevation model, and the ground cover.

- The raster data is displayed using a diverging colour ramp. (Here you can see how to assign a colour ramp)
- The surrounding administrative districts have been overlayed with a transparent grey.
- The river network has been added in blue.
- The main roads as well have been added in black.
- Settlements are displayed as black dots. This helps to identify areas with a higher population density in the areas most at risk.

---

<!--### Map Example 3:

```{figure} ../../fig/REACH_AFG_Map_ABR_infrastructure_mapping_Kunduz_Kunduz_PD-07_17May2022_A3P.png
---
name: Infrastructure Map Kunduz District Afghanistan
width: 800 px
---
Infrastructure Map Kunduz Province 
```
-->

## Good Practices and Common Mistakes in Mapping

In order to produce good maps, there are some __basic rules__ to follow and common __semiological mistakes__ to avoid. 

### Map composition

#### Key elements of a map

In order to provide your audience and readers with sufficient information so they can contextualise the map, it is important to add these key map elements:

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

---

__The title__ summarises in a few words the information represented on the map, giving the reader useful contextual information. Titles should include the following information:

- __The place__, with several degrees of precision according to the scale (Country, Region, Township, ...)
- __The subject__ intelligible by all (make sure that any acronyms used are specified elsewhere on the map)
- __the date__ of the represented data

_Examples:_

- _"Access to health care in Maputo, Mozambique in 2022"_
- _"Flooding Risk in Ghardaïa, Algeria"_

__The legend__ is key to interpreting the information represented on the map. Without it, it is impossible to understand the meaning of the different symbols and colours used map. In order to guide the reader, the legend must be:

- __Comprehensive__: All the data on the map must be presented in the legend.
- __Representative__: The figures on the map and in the legend must match (same size, same color, ...).
- __Organized__: The data in the legend can be grouped by thematic categories (health, environment, background map, ...) or by type of figure (point, line, surface) to facilitate reading.

```{figure} ../../fig/en_legend_good_practice.png
---
width: 750px
name: Organized Legend
---
Example of a well organized legend
```

__The scale bar__ is essential to a map since it gives the correspondence between a distance measured on the map and the distance in the real world. There are two types of scales:

- __The numerical scale__ is expressed as a fraction (1/25000 or 1:25000) that indicates the ratio between 1 centimetre on the map and the actual distance. It is a scale that can be calculated with GIS software, and is often found in topographic maps. A scale of 1:25000 means that 1 cm represents 25,000 cm (or 250 meters) on the ground.

- __the graphical scale__ is expressed by a line on the map, with an associated distance value. This scale is very useful for understanding distances on the ground. The graphical scale will always be the correct size, even if a different printing format is used, since it will undergo the same transformation as the rest of the map

```{figure} ../../fig/example_scale_bar.png
---
name: scale bar
---
Scale bar examples
```

### Orientation

Even though the majority of the maps are oriented towards the north, it is still necessary to specify the orientation of your map. This is often indicated by an arrow pointing to the north, as sometimes a non-northwards orientation is used to represent the study area.

### Sources

Any data represented on a map should have its sources indicated. This provides a record of the data used, but also credits the author of the data. The reader will then be able to look for more information on the sources if he wishes. Open access geographic data, such as OpenStreetMap, are increasingly population and must also be cited on maps.  

It is possible to give the source of each data under the legend, or to do so in a dedicated space in the map. The level of precision of the sources varies according to the author or the precision of the data.

## The Four Semiological Errors

<!---ADD: Insert Image examples for these errors-->

### 1. Proportional circles vs. solid colors

```{caution}
DO NOT represent __quantitative__ stock character/data with a __solid colour__.
```

This is one of the most common mistakes in mapping. While this representation is graphically appealing, it is still false and distracts from the message of the map.

It is a mistake because:

- You lose the __order relationship between the data__ (a circle can be twice as big as another one, a colour cannot be "twice as dark")
- Countries with a large surface area stand out visually (e.g. Russia in the example below)
- We are trying to represent __data that has nothing to do with the area of a country__

<!---Add different example-->

### 2. Color gradient vs. distinct color palette

```{caution}
DO NOT use a __separate__ colour palette to represent __ordered entities__
```

A representation that "feels right" because it seems logical that a "low" rate would be represented differently than a "high" rate.

It is a mistake because:

- By using a differentiating colour variable, __you lose the ordinal relationship between entities__. Instead, a __gradient of the same colour__ that should be used.
- Different colours are used to differentiate between distinct entities.

### 3. Gradient in a single colour vs. Gradient between two colours

```{Caution}
DO NOT use a gradient across two different colours for data that is always positive (or negative).
```

This is a mistake that often occurs because our brains are used to prioritising certain colours, especially green to red, or blue to red. We must remember that __if our values do not have a meaningful zero point, we must stay in the same single colour and use different shades of that colour to indicate different values.
<!--What about height?-->

A gradient between two colours can be used when it is necessary to show a gradation that can go from negative to positive. As for temperatures, it makes sense to distinguish negative values (in shades of blue for example) and positive values (in shades of red).

It is a mistake because:

- By choosing different colours for values that are linked to each other, our eyes perceive a difference between the elements, and not an order.
- Darker colours stand out more than lighter colours, and can be perceived as more important.
- The map will send a message of divergence, of opposition between certain values, when we are simply trying to represent a hierarchy between values
- In this way, the colour itself directly indicates information about the trend (positive/negative or increasing/decreasing).

### 4. Limited geometric symbols vs. complex icons and symbols

```{Caution}
DO NOT use __too many symbols__ in a thematic map
```

Incorporating a multitude of symbols (and data) for a informative map is a common desire. However, too many symbols can __overload the map__ and __reduce the readability__ of the map. Using too many symbols (especially geometric ones) can make it difficult to read and understand the map.  
__The eye can easily distinguish between four to five different symbols. Beyond that, it is difficult to tell elements apart. However, This is a less serious error because it does not convey false information on the map.

It is a mistake because:

- It complicates the map and limits its impact.
- Sometimes you are forced to represent several symbols, so you must be careful about overlapping points and overloading the map.

<!-- ![](/../fig/en_modifiable_areal_unit_problem_example.png) -->