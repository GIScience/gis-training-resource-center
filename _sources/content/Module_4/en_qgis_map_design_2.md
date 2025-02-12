# 4.6. The Print layout

The print layout in QGIS is where you design and finalise the map in order to print or export it as a PDF (or file format of your choice). Here you can add important elements such as the legend, title, explanatory text, and anything you need to create a comprehensive map. By adding layout elements (legend, title, scale bar, sources, etc.) to a map, you provide your audience with the necessary information to contextualise and evaluate the information shown on the map.

1. Go to __Project > New Print Layout > enter a name for the new print layout > click OK__
2. A new window with a blank print layout will appear.

```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

## Map Composition

A good map guides the reader in understanding the information available on the map, makes the information easily accessible, and is not overloaded with information.

In general, there are a few things to keep in mind when creating a map:

- The main map should cover the largest portion of the page and be centred.
- A complete map must have a legend, sources, title, scale, and necessary other information to contextualize the information presented on the map.
- Additional information, such as title, sources, scale bar, legend, orientation, etc. should be scaled accordingly.
    - Titles should be large so the reader can identify it as the main topic of the map.
    - Additional information should be smaller and moved out of the main focus of the page (e.g. at the bottom, to the sides, or in the corners).
- A well-structure page layout helps the reader discern the different information on the map and makes it easier to know where to look for certain information. Frames and boxes can structure the page layout. For example, a legend can be put on the bottom or to the right of the map.

In order to produce good maps, there are some __basic rules__ to follow and __semiological mistakes__ to avoid. The following subchapter will go over the key elements of a map as well as common design mistakes 

### Key elements of a map

In order to provide your audience and readers with sufficient information so they can contextualise the map, it is important to add these key map elements:

- __Title__
- __Legend__
- __Scale__
- __Orientation__
- __Source__
- __Overview Map__
- __Author__

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

---

```{admonition} Now it's your turn!
:class: tip

Take a look at the maps below and pay close attention to how the cartographers arranged the different elements. You can also take a look at maps you encountered in your work or daily life. 

```

::::{dropdown} __Map Example 1__

```{figure} /fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: map_example_ethiopia
width: 750 px
---
Flood affected areas and roads in the Somali Region, Ethiopia (Source: OCHA)
``` 

::::

::::{dropdown} __Map Example 2__

```{figure} /fig/proportional_circles_example.png
---
name: prop_circles_example
width: 500 px
---
Internally Displaced Persons (IDPs), 30 September 2024 (Soure: [UNHCR](https://reliefweb.int/map/sudan/regional-bureau-east-horn-africa-and-great-lakes-region-internally-displaced-persons-idps-30-september-2024)).
```

::::

::::{dropdown} __Map Example 3__

```{figure} /fig/choropleth_hum_example.png
---
name: hum_sit_monitoring_choro_example
width: 700 px
---
South Sudan: Humanitarian Situation Monitoring, April-May 2024 - Damaged shelters (Source: [REACH](https://repository.impact-initiatives.org/document/impact/897badb8/REACH_SSD_Map_HSM_AprilMay2024_DamagedShelters_June2024-1.pdf))
```

::::


::::{dropdown} __Map Example 4__

```{figure} /fig/en_m4_operational_overview_example.png
---
name: operational_overview_example
width: 650 px
---
Operational overview or response activity map (Source: [Shelter Cluster Vanuata](https://reliefweb.int/map/vanuatu/vanuatu-tropical-cyclone-lola-distribution-and-gap-map-malampa-13022024))
```

::::


Now that we have covered what to keep in mind when designing maps, let's take a look at how to create maps with the print layout composer in QGIS.