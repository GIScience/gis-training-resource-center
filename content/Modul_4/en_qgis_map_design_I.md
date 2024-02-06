# Graphical Variables and Symbology

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

The representation of geodata in maps is crucial in order to provide useful location-based insights. This subchapter will cover the basics of good map design, how to create a map design in QGIS as well as common mistakes when designing or interpreting maps.

In this chapter we will go over the basics of symbology, colours and how to adjust individual layers in QGIS to create comprehensive maps.

## Types of maps

In general, there are two main types of maps: __topographic maps__ and __thematic maps__.

__Topographic maps__ are intended to be exhaustive, including elements fundamental to localisation (localities, road networks, terrain, hydrography). They represent the physical location of objects in the real world. The representation of elements in topographic maps is done via conventional signs (e.g.: blue for water, green for forests, yellow for agricultural land). 


```{figure} ../../fig/en_30.30.2_topographic_map_examples.png
---
width: 500px
name: Topographic Maps Examples
---
Examples for topographic maps
```

__Thematic maps__ adress the distribution of phenomena, including sometimes statistically processed information, such as population size, disease cases, flooding risk, etc. The representation of elements on thematic maps is decided according to the rules of graphic semiology. 


```{figure} ../../fig/en_30.30.2_thematic_maps_examples.png
---
width: 500px
name: Thematic maps examples
---
Examples for thematic maps
```

## Graphic Semiology

__Definition__: A set of rules allowing the use of a __graphic sign systems__ to convey information. Graphic semiology uses visual variables to construct a system of signs, allowing the graphic translation of information.

Our brain is capable of interpreting graphic relationships between entities in just seconds. Semiology attempts to theorise these interpretation to make the map more effective and relevant.

```{figure} ../../fig/en_30.30.2_graphic_semiology_signs.png
---
width: 500px
name: Graphic information
---
Depending on the type of information you want to display, you can use different graphic signs
```


## Visual variables

Visual variables are the __graphical means for visually transcribing information__. The visual variables are __shape, size, hue, value, texture, and orientation__. You can vary these variables to appropriately represent the data at your disposal.  
It allows for the expression of __relationship of difference, order, association, or quantity__ between each element. 

```{figure} ../../fig/en_visual_variables.png
---
name: Visual variables
width: 500px
---
Visual variables according to Bertin (1967)
```

```{Caution} 
Visual perception varies from one person to the next according to various capabilities:
- Physiological (e.g.: colour blindness)
- Transcultural (green = nature, blue = water)
```

# Symbology and styling

Depending on the use case and type of geodata at your disposal, there are multiple ways to visualise geodata in a comprehensive format:

- You can change the 'styling' and color of the data
- You can add textlabels 
- Vector and raster data is visualized differently in GIS-Software. 


## Styling Panel

```{figure} ../../fig/en_30.30.2_styling_panel.png
---
height: 400px
name: styling panel
align: left
---
Styling panel in QGIS 3.30.2
```



For each layer in QGIS, there is a styling panel where you can change the symbology, colour and label for the features in that layer. There are two ways to open the layer styling options in QGIS:  
1. Right click on the layer you wish to style and select `properties`. A new window will open up with a vertical tab section on the left. Navigate to the `symbology` tab. 
2. Open the layer styling panel by enabling it under `View`>`Panels`>`Styling Panel`. Usually, the 

On the left of the styling panel you can choose the different tabs to access different styling options.

In the styling panel you can change the styling for all features of a layer, set up categories for different symbols, create labels, and create colour ramps to differentiate between features with variable values.

:::{dropdown} Video: Opening the styling panel
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_the_styling_panel.mp4"></video>
:::

## Symbology

- Symbology is used to change the look of features on a map
- It makes maps more visually appealing and easier to read
- Colors and styles represent a specific information
- Symbology is applied to layers, but within the same layer we can assign multiple styles to features
- the symbology of a layer can be __changed based on one of its attributes__

> To Do: add different visualisation for different types of data (discrete vs. continuous values, insert image). For example the amount of rainfall/temperature is a continuous value.

## Colours

Colours are arguably the most striking visual variables as they are easily disinguishable. However, depending on the type of data and the information you wish to convey, there are a few things to consider when choosing a colour scheme for your map. The most important variables for colours are the __hue__, the __value__ (saturation) and the __transparency__. 

Colours schemes can be __categorial, sequential, or diverging__. If you wish to display different types of buildings or roads, the colour schemes should be categorial. Colour gradients, either sequential or diverging, are used for numerical data or data that can be ordered. For example, for the population sizes of districts a sequential colouring schemes is best to show the relative difference between the values. However, if the data has positive __and__ negative values, a diverging colour gradient should be used.

``` {figure} ../../fig/en_colour_gradients_qualities.png
---
name: Colouring schemes
width: 750px
---
Different types of colouring schemes
```

When choosing colour gradients, a clear gradient from lighter to darker colours is the best most of the times as the gradation is easily distinguishable and translates well into black and white. In the figure below, example A and B are not ideal as it is difficult to make out the gradation and it does not translate into black and white. You can achieve a clear sequence by grading the __saturation__ of the colour gradient.

```{figure} ../../fig/de_colour_gradients_saturation.png
---
name: colour gradients saturation example
width: 750px
---
Examples for different colour gradients translated into black and white. Pay attention to the saturation gradient under each example.
```

Colour gradients can also encompass multiple hues:

```{figure} ../../fig/colour_gradients_hues.png
---
name: colour gradients with multiple hues
width: 750px
---
Single hue gradient on the left; Multiple hue gradient on the right
```

```{tip}
The [Colourbrewer website](colorbrewer2.org) is a quick and useful tool to select and generate colour palettes for your use case. 
```

### Colour Blindness

When choosing the colours, you have to keep in mind that colour gradients (especially diverging Red-Green gradients) can be hard or impossible to distinguish for persons with colour blindness.

``` {figure} ../../fig/Colour_Blindness.png
---
name: colour blindness examples
width: 750px
---
Different Colour schemes for the Colour Vision Impaired; Source: Jenny, Bernhard, and Nathaniel Vaughn Kelso. (2007). Color Design for the Color Vision Impaired. *Cartographic Perspectives*, no. 58 (September 1, 2007): 61-67. https://doi.org/10.14714/CP58.270 
```


## Symbology for Vector data

You can use graphical variables to style vector data. As we have already learned, vector data can be either points, lines, or polygons. There are different options to symbolize these different types of vector data. In this subchapter, we will focus on a few common examples.


``` {figure} ../../fig/en_symbolization_vector_data.png
---
name: symbolization for vector data
width: 750px
---
Symbolization for vector data; Source: White, T. (2017). Symbolization and the Visual Variables. *The Geographic Information Science & Technology Body of Knowledge (2nd Quarter 2017 Edition), John P. Wilson (ed.). DOI: 10.2222/gistbok/2017.2.3 
```

In the dropdowns below you can find examples on how to set up common vector data styling.

>To Do: Provide the example data for follow along

:::{dropdown} Exercise: Only display the outlines of polygons

In this example, wewant to change the symbology of a single layer so that __only the outlines of the polygons are visible__. 

To change the symbology of a single layer:
1. Open the `Styling panel` and navigate to the symbology tab. By default, the symbology will be set to `Single Symbol`. This means that the same colours and contours will be applied to all the features in that layer.
2. Click on `Simple Fill`
3. Click on the arrow to the right of `Fill Colour`
4. Check the `Transparent Fill` option

```{figure} ../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: layer styling transparent
width: 500 px
---
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

:::

:::{dropdown} Change the styling for multiple overlayed layers

In this exercise, we will apply the same style to all features in a layer, but we will change multiple layers and overlay them so each is visible in a different style. We have the polygons for 3 administrative levels.

```{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: change layer style 1
height: 400px 
---
Order the layers and navigate to the styling panel of the topmost layer
```

1. Add the `Adm0`, `Adm1` and `Adm2` shapefiles to your Session 2 project.
2. Order the layers so they are all visible: Put the `Adm2` layer at the bottom, then the `Adm1` then `Adm0`. At first, this might look weird because `Adm0` will cover everything.
3. Change the symbology of the Adm0 layer by opening the stlying panel and navigating to the Symbology tab. 


```{figure} ../../fig/en_30.30.2_changing_layer_style_2.png
---
name: change layer style 2
width: 350px
align: left
---
Change the Fill type
```

4. Click on `Simple Fill` to open the style options.
5. Expand the `Fill Colour` menu and check the `Transparent Fill` option. This will make only the boundaries visible, so __we will be able to see the layer under this one__.
6. Choose a `Stroke Colour`, and make the `Stroke Width` 0.66 Millimeters.
7. Click OK
8. __Repeat the same process__ for the Adm1 layer, using the same colour as for Adm0 (it will be in "Recent colors) and leave the stroke width at 0.26.
9. Now we can see the boundaries of the country and its states, and behind that we cann see the districs (Adm2).
10. Let's make the districs layer's style consistent with the others.

<br/><br/>

11. Choose a `Fill Color`
12. Use the same Stroke Colour` as for Adm0 and Adm1, but make the width 0.1 Millimeters and the Stroke Style a __Dash Line__
13. Click OK and look at yout map: hopefully it's starting to look nicer!

```{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
name: change layer style 3
---
The styling of a vector data consists of the colour and the outline
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_change_style_for_multiple_layers
.mp4"></video>


:::

:::{dropdown} Use different styles in a single layer

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_styling
.mp4"></video>

We can use symbology to __show the difference between features__ in the same layer. For example, it could be different types of buildings, quantities of Covid cases by district, or types of roads. We can choose a specific attribute of a dataset to assign different colors, outlines, or sizes to features:

1. From your shapefile folder, __drag te ACLED security incidents shapefile onto your map__
2. Open the `Symbology tab` for that layer and choose `Categorized` instead of Single Symbol.   
```{note} 
Categorized symbology is used when you have ***discrete*** variables.
```

```{figure} ../../fig/en_30.30.2_categorized_layer_symbology_1.png
---
name: categorized layer symbology 1
width: 500px
---
Change the symbology type to "categorized" and choose the Value (variable) you wish to display
```
3. Now we need to __choose which attributes we want to display through the symbology__. In this case, it could be the number of casualtiees, or the actor who perpetrated the act. Let's categorize the features by `event_type`
4. Click on `Classify` to __list all the unique values contained__ in the `event_type` field (i.e. all the possible types of security incidents recorded in our table)
5. Now we can __change the style of each single value__
6. Double click on the value `Explosions`
7. At the bottom of the __Symbol selector__ window, choose a symbol to make Explosion points stand our
8. Click on `OK`, then Apply to preview what the layer will look like
9. Click `OK` again

```{figure} ../../fig/en_30.30.2_categorized_layer_symbology_2.png
---
name: categorized layer symbology 2
width: 500px
---
By double clicking on the __unique values__ in the classified list, you can change the symbol for each value
```

Now we have a map of Nigeria where you can locate the areas, that are affected by explosions more than others. On the map below, we also added text labels, which will be explained below.

```{figure} ../../fig/en_exercise_map_design_example_Nigeria.png
---
name: map design example regions affected by explosions in Nigeria
width: 500px
---
Regions affected by explosions in Nigeria
```
:::

:::{dropdown} Style data based on variable ranges (graduated styling)

If a layer contains numeric values that are continuous, they can be organized in intervals. These intervals can be displayed in graduated colours. In this exercise, we assign colours to Adm1 polygons based on the total population of each State.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_graduated_styling
.mp4"></video>

1. Download the NGA_Adm1_Pop shapefile [link!!] and save it in your shapefile folder
2. In QGIS, turn off the Adm1 and Adm2 layer, leaving only Adm0
3. Drag the shapefile NGA_Adm1_Pop into your map
4. Open its `Symbology` options and choose `Graduated`
5. __Select the value you want to use to assign colours__, in this case, it will be `Population`

```{figure} ../../fig/en_30.30.2_symbology_variable_ranges.png
---
name: symbology of variable ranges
width: 550px
---
With variable ranges, select __Graduated__ symbology and choose the attribute with continuous values
```

6. Click on `Classify` to __list all values divided in classes__
7. Choose __how many classes__ you want the data to be divided into ‒ let's say 4
8. By default, the colour ramp will be red. However, red is not the right colour to use for population count, as it is generally used to communicate negative elements, such as food insecurity or cholera cases
9. Click on __the arrow next to the colour ramp__ to choose another combination of colours - let's say a color ramp from white to blue
10. Click `Apply` to preview the look of your layer, then `OK`

```{figure} ../../fig/en_30.30.2_symbology_variable_ranges_2.png
---
name: symbology of variable ranges 2
width: 500px
---
You can categorize the continuous values into classes and assign a colour ramp 
```

The following map shows the most populated States of Nigeria using a graduated colour categorization. These types of maps are called __Coropleth maps__. 

```{figure} ../../fig/en_map_design_example_variable_ranges.png
---
name: map design example_state population Nigeria
width: 500px
---
A map showing the population of Nigerian states
```
:::

```{note} 
Remember that __the layer's symbology is saved within your project file, not within your shapefile!__ If you share a shapefile with a colleague, it will have a different style when they add it to their own project.
```

## Labels

Labels are text that display information or values of the data. In QGIS, you can either select __Single Labels__ or __Rule-based Labelling__. For each option, an attribute (`value`) that will be displayed on the map. For example, the name of a city or region.  Additionally, you can __change the font, font size, colour and some other styling options__ for the label text. When you create a map, you can add labels to help your reader understand the map quickly. However, be aware that too much text information can overload the map with too much information for the reader to process.

- QGIS offers two methods to display labels:
    - Single labels: Creates a single label style for every feature in the layer. You can select a attribute (value) which will be displayed. For example, the name of a settlement. You need to know which attribute displays the information you want to display. Look at the attribute table of the dataset to find it out.
    - Rule-based Labelling: Create rules using expressions to select accurately which features are to be labeled. Each rule can have a different text formatting. Use this if you want to have more control over the information that will be displayed as labels. For example, you can filter your data to only display the names of regional capitals. 
- Only display information that is helpful to the reader. Useful information can be the name of a settlement or a place, so the reader can assign a certain symbol on the map to this particular place.
- In most cases, displaying numerical values as labels is confusing to the reader. For numerical data, you can choose a different visualization such as colours or symbol size (don't forget to add a legend).
- If you want to display different types of information as labels, the font needs to be different so the reader can differentiate between the different types of information that is displayed.
- QGIS places the labels automatically. Sometimes, if you are using a lot of black outlines or dark colours, black text is hard to read on the map. In that case, you can add white buffer around the text to make it visible. 


```{figure} ../../fig/label_text_buffer_example.png
---
width: 300 px
name: label buffer example
---
A label without a text buffer (left) and a label with a white text buffer (right)
```


```{note} Label rendering

Sometimes the labels can obstruct other symbols. In that case, you can either adjust the placement of the labels in the __Label tab__, or use the `Move a Label, Diagram, or Callout`-tool in __Label toolbar__

By default, QGIS renders the labels so that they don't overlap with other labels. This means that not all the labels will be visible if the data is dense or rendered close to each other. You can optimize the rendering under the rendering option. 

```

:::{dropdown} Adding labels to a layer 

1. In the styling panel, click on the `Labels` tab underneath the Symbology tab.
2. Select `Single labels`. 
3. `"Value"` is where you choose the attribute that will be displayed as a label. For example `*ADM1_EN*` will display the English names of Nigerian states for each feature in the data set.
4. Let's __change the font__: Open the Font dropdown menu and select Arial. Make the text `Bold` in the Style dropdown menu. Change the colour by clicking on `Colour`, and change the `Size` to 8 pt
5. Let's __add a white buffer__ around the label. In the `Labels` tab, you will find a list with different options to style the labels. Right now, we are in the `Text` menu. Select `Buffer` and check the `Draw text buffer` option. This will make the labels stand out more on dark or crowded maps.
7. Click `Apply` and `OK`.

```{figure} ../../fig/en_30.30.2_setting_up_labels.png
---
width: 500px
name: Setting up labels
---
Setting up labels in QGIS 30.30.2
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_labels
.mp4"></video>

:::



## Symbology for raster data

As we have already learned, raster data are basically a grid of pixels with different (numerical) values. As such, you can't style the shape, fill or outline of raster data. Raster data is visualized by assigning a colour ramp to the pixel value. QGIS offers several options to visualise raster data. For example, you can create a hillshade with digital elevation model (DEM). 

### Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the `styling panel` for the raster layer
2. Navigate to the `Symbology tab`  
3. By default, the colour scheme is set to Singleband gray (if you only have one colour band in the data set). Click on `Singleband Gray` and switch to `Singleband pseudocolour`
4. Click on __the arrow to the right of the colour ramp__. Here you can choose a premade colour ramp
5. You can modify the colour ramp by __clicking on the colour ramp__.

``` {figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: raster data colour gradient
width: 600px
---
Colour Ramp Selector
```

In the colour ramp selector, you can adjust each colour step. On the bottom, you can see a plot for the Hue, __Saturation__, __Lightness__ and __Opacity__. Especially latter three are useful to see how your colour ramp will translate. Gradients from light to dark are easier to read: Check if the plot for the __Lightness__ has a more or less linear plot. 

# Exporting and Importing Styles

The layers in QGIS are saved separately from the settings and styles of a QGIS Project. This means that if you load the same layers into a different QGIS-project, the symbology and styling of the data will be different. QGIS lets you save the symbology and styling of a layer as a seperate file (`.qml`-files). Working with `.qml`-files saves you a lot of work and assures consistency between your maps. 

A `.qml`-file saves the styling information of a particular layer. You can choose wether to save only the colour symbology or all the options you assigned 

You can also export a style into the same folder as the data so your colleagues can apply the same styling when loading the data into QGIS.
Some organisations may also use standarized symbols or colours in their maps. 

:::{dropdown} Saving or exporting styling settings

1. Open the styling panel and click on `styles`. A dropdown menu will open with the option to export the layer styling.
2. Since in this case, the styling is for exactly that dataset, you can leave all the boxes checked.
3. Select a location and name for the styling. The styling will be saved as a `.qml` file. __Make sure it is saved in the same folder as the dataset and give it the same name as the corresponding dataset. This way it will, when loading the data into QGIS, the styling will automatically be applied.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>
:::

When saving a style, you can choose what information and settings you want to save in the `.qml`-file. For example, if you want to send a layer to your colleague with the same styling as you, it is best to check the "__Layer properties__", "__Symbology__", and "__Labels__" categories (and any additional styling options you have set). If you only wish to save a certain colouring, line thickness, or labeling style, you only need to check the respective boxes.

```{figure} ../../fig/en_30.30.2_save_layer_style_window.png
---
width: 350px
name: Save layer styling window
---
Save Layer styling window in QGIS 30.30.2.
```

When working with similar data (e.g.: building types or flooding risk), it is useful to have template styles, that can be automatically or quickly loaded into your QGIS-project.


```{Tip}
When a styling is saved in the same location as the data and has the same name as the corresponding dataset, the styling will be automatically applied to the layer when loading the data into QGIS!
```


- [Exporting a styling](link)
- [Loading a style into your QGIS-project](link)
- [Using IFRC Symbols](link)
- [Using and adding SVG-symbols](link)
- [Adding an external SVG-library](link)

# Further Resources

- Tutorial on [how to import the SIMS Color Palette into QGIS](https://learn-sims.org/geospatial/importing-sims-color-palette-to-qgis/) 
- Tutorial on [how to create a shaded relief map in QGIS](https://learn-sims.org/geospatial/creating-a-shaded-relief-map-in-qgis/)
- [Creating a 3W (Who, What, Where) Infographic](https://learn-sims.org/information-design/creating-a-3w-who-what-where-infographic/)
