# Visualisation of Geodata: Symbology and Colours

The representation of geodata in maps is essential for providing useful location-based insights. This subchapter will 
cover the basics of good map design, how to create a map design in QGIS, as well as common mistakes when designing or 
interpreting maps.

In this chapter we will go over the basics of symbology, colours, and how to adjust individual layers in QGIS to create 
comprehensive maps.

:::{admonition} Recap: Types of Maps
:class: seealso

In general, there are two main types of maps: __topographic maps__ and __thematic maps__.

__Topographic maps__ are intended to be exhaustive, including elements fundamental to localisation (localities, road 
networks, terrain, hydrography). They display the physical location of objects in the real world. The representation of 
elements in topographic maps is done using conventional signs (e.g. blue for water, green for forests, yellow for 
agricultural land). 

```{figure} ../../fig/en_30.30.2_topographic_map_examples.png
---
width: 600px
name: Topographic Maps Examples
---
Examples for topographic maps
```

__Thematic maps__ display the distribution of specific data or statistically processed information, such as population 
size, disease incidence, flooding risk, etc. The representation of elements on thematic maps is decided according to 
the rules of graphic semiology. 


```{figure} ../../fig/en_30.30.2_thematic_maps_examples.png
---
width: 600px
name: Thematic maps examples
---
Examples for thematic maps
```

These two maps use design elements differently. Topographic maps will use symbols and colours out of convention and 
readability, whereas in designing thematic maps, the symbols and colours you use depend on the context and the 
information you want to convey.

:::

## Visual Variables

```{figure} ../../fig/en_30.30.2_graphic_semiology_signs.png
---
width: 500px
name: Graphic information
---
You can use different graphic signs depending on the type of information you want to display.
```

Visual variables are the __graphical means for visually transcribing information__. The visual variables are __shape, 
size, hue, value, texture, and orientation__. You can adjust these variables to appropriately represent the data at 
your disposal. They allows for the expression of __relationship of difference, order, association, or quantity__ 
between each element, helping to display different information.

```{figure} ../../fig/en_visual_variables.png
---
name: Visual variables
width: 500px
---
Visual variables according to Bertin (1967)
```

```{Caution} 
Visual perception varies from one person to the next according to various capabilities:
- Physiological (e.g. colour blindness)
- Transcultural (green = nature, blue = water)
```

## Choropleth and Graduated Symbol Maps

Based on these visual variables, cartographers are able to interpret and communicate information crucial to 
humanitarian operations. Choropleth and Graduated symbol maps are two common thematic map types used in humanitarian 
work. 


### __Choropleth Maps__
^^^

A choropleth map is a type of map that shows data using colors or shading within specific geographic areas, like 
countries, states, or counties. It helps to visualize data patterns or distributions across regions. For example, a 
choropleth map could show population density, where darker shades indicate higher densities and lighter shades indicate 
lower densities.

In essence:

- Data is divided into areas on the map.
- Colors or shades represent different values for each area.
- Easy to interpret – darker or more intense colors often mean higher values, and lighter colors mean lower values.

Choropleth maps are ideal for showing patterns over large areas but should be used carefully, as they don’t show exact 
values within each region, just an overall gradient or level of intensity and they are used in almost every application 
of mapping and GIS.

```{figure} /fig/choropleth_intro_example.png
---
name: choropleth_intro_example
width: 600 px
---
An example of a choropleth map (Source: [AxisMaps](https://www.axismaps.com/guide/choropleth))
```

__Use cases__:

__Humanitarian Action__

In humanitarian action, choropleth maps are used to:

- Identify vulnerable regions: Maps can show areas with high poverty rates, conflict, or disaster impact, helping responders prioritize regions most in need of aid.
- Track disease outbreaks: For instance, during an epidemic, choropleth maps can show areas with high infection rates, helping to direct medical resources and prevent further spread.
- Monitor food insecurity and famine risks: Maps that illustrate food scarcity help humanitarian organizations focus on regions where food aid is needed the most.

```{figure} /fig/choropleth_hum_example.png
---
name: hum_sit_monitoring_choro_example
width: 700 px
---
South Sudan: Humanitarian Situation Monitoring, April-May 2024 - Damaged shelters (Source: [REACH](https://repository.impact-initiatives.org/document/impact/897badb8/REACH_SSD_Map_HSM_AprilMay2024_DamagedShelters_June2024-1.pdf))
```

__Environmental Science__

- Show pollution levels: Choropleth maps can depict air or water quality across regions, helping to identify polluted areas.
- Track deforestation: Maps highlighting forest coverage changes make it easy to spot deforestation trends.
- Climate impact: Regions prone to temperature rise or extreme weather can be highlighted to aid climate adaptation efforts.

__Public Health__

- Visualize health disparities: Choropleth maps can show regions with high rates of disease, poor access to healthcare, or varying vaccination rates.
- Resource allocation: Health authorities use these maps to allocate medical resources based on areas with higher health needs.

__Urban Planning and Infrastructure__

- Display population density: Maps show where populations are concentrated, helping in city planning and infrastructure development.
- Identify socioeconomic patterns: Urban planners use these maps to see income, employment, and education levels across neighborhoods.

---

Choropleth maps are usually created by [classifying](/content/Modul_3/en_qgis_data_classification.md) geodata into 
distinct groups, either using categorised or graduated classification. The effectiveness of a choropleth map is 
dependent on the __colouring scheme__.  


### __Proportional Circles/Graduated Symbols Map__

Another very useful type of map in humanitarian action is the proportional circle or graduated symbol map. This type of 
map uses circles of varying sizes to represent data values across different locations. The larger the circle, the 
higher the data value it represents. This makes it useful for showing quantities or comparing values across different 
points on a map. 


```{figure} /fig/proportional_circles_example.png
---
name: prop_circles_example
width: 500 px
---
Internally Displaced Persons (IDPs), 30 September 2024 (Soure: [UNHCR](https://reliefweb.int/map/sudan/regional-bureau-east-horn-africa-and-great-lakes-region-internally-displaced-persons-idps-30-september-2024)).
```

```{figure} /fig/proportional_circles_example_2.png
---
name: prop_circles_example_2
width: 450 px
---
Cholera cases in Malawi (Source [Paul Knight](https://learn-sims.org/geospatial/creating-a-proportional-circle-map-in-qgis/)).
```

:::

# Symbology and styling

Depending on the use case and type of geodata at your disposal, there are multiple ways to visualise geodata in a 
comprehensive format. For example, you can:

- You can change the 'styling' and colour of the data
- Change the thickness, colour of lines, or assign a dash pattern 
- Change the colour and outlines of polygons
- You can assign symbols or pictures to geodata
- Change the size, colour and orientation of symbols
- You can add text labels
- You can change the font, colour and orientation of the text label
- For raster data, you can assign a colour gradient for the different values

The styling of a layer is how you communicate the information to your audience. Each data-layer in your QGIS-project 
has it's own styling rules. These can range from simple (e.g. display line data as black lines, assigning a colour to 
polygons) to more complex (e.g. differentiate between different types of roads, add complex fill-patterns to polygons, 
or add SVG-symbols of varying sizes to ). 

<!-- Vector and raster data is visualized differently in GIS-Software. -->


## Symbology

- Symbology is used to change the look of features on a map
- It makes maps more visually appealing and easier to read
- Colours and styles represent a specific information
- Symbology is applied to layers, but within the same layer we can assign multiple styles to features
- The symbology of a layer can be __changed based on one of the layer's attributes__.

<!---- To Do: add different visualisation for different types of data (discrete vs. continuous values, insert image). For example the amount of rainfall/temperature is a continuous value.-->

## Colours

Colours are arguably the most striking visual variables as they are easily distinguishable. However, depending on the 
type of data and the information you wish to convey, there are a few things to consider when choosing a colour scheme 
for your map. The most important variables for colours are the __hue__, the __value__ (saturation) and the 
__transparency__. 

Colours schemes can be __categorial, sequential, or diverging__. If you wish to display different types of buildings or 
roads, the colour schemes should be categorial. Colour gradients, either sequential or diverging, are used for 
numerical data or data that can be ordered. For example, for the population sizes of districts a sequential colouring 
schemes is best to show the relative difference between the values. However, if the data has positive __and__ negative 
values, a diverging colour gradient should be used.

``` {figure} ../../fig/en_colour_gradients_qualities.png
---
name: Colouring schemes
width: 750px
---
Different types of colouring schemes
```

When choosing colour gradients, a clear gradient from lighter to darker colours is usually the most appropriate, as the 
gradation is easily distinguishable and translates well into black and white. In the figure below, examples A and B are 
not good colour schemes, as it is difficult to make out the gradation and it does not translate well into black and 
white. You can achieve a clear sequence by grading the __saturation__ of the colour gradient.

```{figure} ../../fig/de_colour_gradients_saturation.png
---
name: colour gradients saturation example
width: 750px
---
Examples for different colour gradients translated into black and white. Pay attention to the saturation gradient under 
each example. Source: Stauffer, Reto & Mayr, Georg & Dabernig, Markus & Zeileis, Achim. (2014). Somewhere Over the 
Rainbow: How to Make Effective Use of Colours in Meteorological Visualizations. Bulletin of the American Meteorological 
Society. 96. 140710055335002. 10.1175/BAMS-D-13-00155.1.
```

Colour gradients can also encompass multiple hues:

```{figure} ../../fig/colour_gradients_hues.png
---
name: colour gradients with multiple hues
width: 750px
---
Single hue gradient on the left; Multiple hue gradient on the right.  
```

```{tip}
The [Colourbrewer website](colorbrewer2.org) is a quick and useful tool to select and generate colour palettes for your use case. 
```

### Colourblindness

When choosing the colours, you have to keep in mind that colour gradients (especially diverging Red-Green gradients) can be hard or impossible to distinguish for people with colour blindness.

``` {figure} ../../fig/Colour_Blindness.png
---
name: colour blindness examples
width: 750px
---
Different Colour schemes for the Colour Vision Impaired; Source: Jenny, Bernhard, and Nathaniel Vaughn Kelso. (2007). Color Design for the Color Vision Impaired. *Cartographic Perspectives*, no. 58 (September 1, 2007): 61-67. https://doi.org/10.14714/CP58.270 
```

## Complex Maps

The different symbolisation methods discussed in this chapter can be combined in different ways to create sophisticated reports and maps. By combining several methods, you can communicate different phenomena intuitively to the reader. A classical example is a combination of a choropleth map (graduated colours) with a proportional circles map (see {numref}`bivariate_map_example_lebanon`). 


```{figure} /fig/en_complex_map_lebanon.png
name: bivariate_map_example_lebanon
width: 550 px
---
A complex map using graduated colours and proportional circles (Source: [REACH Initiative](https://reliefweb.int/map/lebanon/lebanon-conflict-and-displacement-overview-30-september-2024))
```


```{figure} /fig/en_complex_bivariate_map.png
---
name: complex_bivariate_map_example
width: 750 px
---
A complex map combining layer styling and different visual variables to communicate a complex situation (Source: [SIMS](https://rcrcsims.org/portfolio/view/18))
```


:::{admonition} Now it's your turn!
:class: tip
{numref}`bivariate_map_example_lebanon` and {numref}`complex_bivariate_map_example` both make use of graduated colours as well as graduated symbols. What other symbolisation principles can you detect on these maps? 
:::

Now that we have learned the different visual variables, and know how to use them to create complex maps, the next chapter [Symbology for Vector data](/content/Modul_4/en_qgis_styling_vector_data.md) will explain how to set up different symbolisation and styling methods in QGIS. 