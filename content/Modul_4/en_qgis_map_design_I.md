# Graphical Variables and Symbology

The representation of geodata in maps is crucial in order to provide useful location-based insights. This subchapter will cover the basics of good map design, how to create a map design in QGIS as well as common mistakes when designing or interpreting maps.

>Overview?

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
1. Right click on the layer you wish to style and select properties
2. Open the layer styling panel by enabling it under "View">"Panels">"Layer Styling"

On the left of the styling panel you can choose the different tabs to access different styling options.

In the styling panel you can change the styling for all features of a layer, set up categories for different symbols, create labels, and create colour ramps to differentiate between features with variable values.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_the_styling_panel.mp4"></video>


## Symbology

- Symbology is used to change the look of features on a map
- It makes maps more visually appealing and easier to read
- Colors and styles represent a specific information
- Symbology is applied to layers, but within the same layer we can assign multiple styles to features
- the symbology of a layer can be __changed based on one of its attributes__

## Colours

Colours are arguably the most striking visual variables as they are easily disinguishable. However, depending on the type of data and the information you wish to convey, there are a few things to consider when choosing a colour scheme for your map. The most important variables for colours are the __hue__, the __value__ (saturation) and the __transparency__. 

Colours schemes can be __categorial, sequential, or diverging__. If you wish to display different types of buildings or roads, the colour schemes should be categorial. Colour gradients, either sequential or diverging, are used for numerical data or data that can be ordered. For example, for the population sizes of districts a sequential colouring schemes is best to show the relative difference between the values. However, if the data has positive __and__ negative values, a diverging colour gradient should be used.

``` {figure} ../../fig/en_Colour_Gradients_6.png
---
name: Colouring schemes
width: 750px
---
Different types of colouring schemes
```

When choosing colour gradients, a clear gradient from lighter to darker colours is the best most of the times as the gradation is easily distinguishable and translates well into black and white. In the figure below, example A and B are not ideal as it is difficult to make out the gradation and it does not translate into black and white. You can achieve a clear sequence by grading the __saturation__ of the colour gradient.

``` {figure} ../../fig/en_colour_gradients_saturation.png
---
name: colour gradients saturation example
width: 800px
---
Examples for different colour gradients translated into black and white. Pay attention to the saturation gradient
```

Colour gradients can also encompass multiple hues:

```{figure} ../../fig/Colour_Gradients_2.png
---
name: colour gradient hues
width: 750px
---
Single hue gradient on the left; Multiple hue gradient on the right
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

In the dropdowns below you can find examples on how to set up common vector data styling. Make sure you have downloaded the Exercise XX data from the github repository if you want to follow along!

>Link the files and github repository

:::{dropdown} Exercise: Only display the outlines of polygons

In this example, wewant to change the symbology of a single layer so that __only the outlines of the polygons are visible__. 

To change the symbology of a single layer:
1. Open the styling panel and navigate to the symbology tab. By default, the symbology will be set to __Single Symbol__. This means that the same colours and contours will be applied to all the features in that layer.
2. Click on __"Simple Fill"__
3. Click on the arrow to the right of __Fill Colour__
4. Check the __"Transparent Fill"__ option

```{figure} ../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: layer styling transparent
width: 500 px
---
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

:::

:::{dropdown} Change the styling for multiple overlayed layers

>This is exercise 7 in the PPP. Participants will need the specific data. 

In this exercise, we will apply the same style to all features in a layer, but we will change multiple layers and overlay them so each is visible in a different style. We have the polygons for 3 administrative levels.

```{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: change layer style 1
height: 400px 
---
Order the layers and navigate to the styling panel of the topmost layer
```

1. Add the "Adm0", "Adm1" and "Adm2" shapefiles to your Session 2 project.
2. Order the layers so they are all visible: Put the Adm2 at the bottom, then the Adm1 then Adm0. At first, this might look weird because Adm0 will cover everything.
3. Change the symbology of the Adm0 layer by opening the stlying panel and navigating to the Symbology tab. 


```{figure} ../../fig/en_30.30.2_changing_layer_style_2.png
---
name: change layer style 2
width: 350px
align: left
---
Change the Fill type
```

4. Click on "__Simple Fill__" to open the style options.
5. Expand the "__Fill Color__" menu and check the __Transparent Fill__ option. This will make only the boundaries visible, so __we will be able to see the layer under this one__.
6. Choose a __Stroke color__, and make the __Stroke width__ 0.66 Millimeters.
7. Click OK
8. __Repeat the same process__ for the Adm1 layer, using the same colour as for Adm0 (it will be in "Recent colors) and leave the stroke width at 0.26.
9. Now we can see the boundaries of the country and its states, and behind that we cann see the districs (Adm2).
10. Let's make the districs layer's style consistent with the others.

<br/><br/>

11. Choose a __Fill Color__
12. Use the same __Stroke color__ as for Adm0 and Adm1, but make the width 0.1 Millimeters and the Stroke Style a __Dash Line__
13. Click OK and look at yout map: hopefully it's starting to look nicer!

```{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
name: change layer style 3
---
The styling of a vector data consists of the colour and the outline
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_change_style_for_multiple_layers
.mp4"></video>

```{note} 
Remember that __the layer's symbology is saved within your project file, not within your shapefile!__ If you share a shapefile with a colleague, it will have a different style when they add it to their own project.
```

:::

:::{dropdown} Use different styles in a single layer

```{note}For this exercise, you must have convertet the excel-spreadsheet "ACLED_Nigeria_2022-2023" into a .csv-file. Read how you can do this [here](/gis-training-resource-center/content/Modul_2/en_qgis_basic_data_processing.html#delimited-text-import). 

>Check if the others have the same issue with importing the .csv file (excel export as csv delimits with ";" instead of ",". QGIS expects ",", if you replace all the ";" with "," the coordinates do not work any longer because the degree are delimited with a "," as well. You can fix it in VSC)
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_styling
.mp4"></video>

We can use symbology to __show the difference between features__ in the same layer. For example, it could be different types of buildings, quantities of Covid cases by district, or types of roads. We can choose a specific attribute of a dataset to assign different colors, outlines, or sizes to features:

1. From your shapefile folder, __drag te ACLED security incidents shapefile onto your map__
2. Open the layer __Symbology__ and choose __Categorized__ instead of Single Symbol.   
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
3. Now we need to __choose which attributes we want to display through the symbology__. In this case, it could be the number of casualtiees, or the actor who perpetrated the act. Let's categorize the features by **event_type**
4. Click on __"Classify" to list all the unique values contained in the event_type field__ (i.e. all the possible types of security incidents recorded in our table)
5. Now we can __change the style of each single value__
6. Double click on Explosions
7. At the bottom of the __Symbol selector__ window, choose a symbol to make Explosion points stand our
8. Click on OK, then Apply to preview what the layer will look like
9. Click OK again

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

> Don't forget to check that they have access to the data

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_graduated_styling
.mp4"></video>

1. Download the NGA_Adm1_Pop shapefile [link!!] and save it in your shapefile folder
2. In QGIS, turn off the Adm1 and Adm2 layer, leaving only Adm0
3. Drag the shapefile NGA_Adm1_Pop into your map
4. Open its Symbology options and choose "__Graduated__"
5. Select the value you want to use to assign colours, in this case, it will be "__population__"

```{figure} ../../fig/en_30.30.2_symbology_variable_ranges_1.png
---
name: symbology of variable ranges 1
width: 500px
---
With variable ranges, select __Graduated__ symbology and choose the attribute with continuous values
```

6. Click on __Classify__ to list all valued, divided in classes
7. Choose __how many classes__ you want the data to be divided into ‒ let's say 4
8. By default, the colour ramp will be red. However, red is not the rivht colour to use for population count, as it is generally used to communicate negative elements, such as food insecurity or cholera cases
9. Click on the arrow next to __Color Ramp__ to choose another combination of colours - let's say a color ramp from white to blue
10. Click Apply to preview the look of your layer, then OK

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

## Labels

- Labels are text that show a specific attribute of features. 
- It is useful to add labels to features to easily identify them. For example, the name of a settlement.
- You can change the font, colour and size of labels
- When you create a map you always add labels to help the final user reading the map

:::{dropdown} Adding labels to a layer
>This is exercise 2 in the PPP, also review 

1. In the styling panel, click on the "Labels" tab.
2. Select *Single Labels*. 
3. `"Value"` is where you choose the attribute that will be displayed as a label. For example `*ADM1_EN*` will display the English names of Nigerian states for each feature in the data set.
4. Let's change the font: make it Arial, bold, dark grey, 8 pt
5. Let's add a white buffer around the label.
7. Click Apply and Ok.

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

:::{dropdown} Adding different label styles to the same layer

Sometimes you will need to create two different label styles for different features of a single layer. In this example, we will create one label style for the *Country Capital*, and another one for the *State Capitals*

1. Open the styling panel for the `"NGA_settlements_nga"` layer and click on the Labels tab
2. Select __Rule-based Labeling__
3. Click on the __Add Rule__ button at the bottom (the "+"-sign) and create the first rule
4. For __Value__, select __"NAME"__ (so that the labels will show the name of each city), then click on the "ε"-button next to the "Filter" bar.

```{figure} ../../fig/en_30.30.2_adding_rule-based_labels.png
---
width: 500px
name: adding rule-based labels
---
To add rule-based labels, you need to enter an expression
```

5. In the central column, expand __Fields and Values__ to display a list of all the fields in your layer and double-click on __Class__ to add it to the expression frame on the left.
6. In the right column, click on __All unique__ to list all unique values contained in the Class field. In this dataset, `"CLASS"=1` designates the capital city, whereas `"CLASS"=2` designate other major cities. 
7. Click on the `"="` operator, then doube-click on the _value 1_ (which represent the Country capital in this case). Click OK.
8. Scroll down to *change the label style*. Make it Arial, bold, black, 12pt and add a white buffer.
9. Repeat steps 4 to 9, but select *Value 2* (State capitals) and make the label black, bold, 10pt, no buffer.
10. Click **Apply**, the OK.

```{figure} ../../fig/en_30.30.2_adding_rule-based_labels_expression_builder.png
---
width: 500px
name: rule-based labels expression builder
---
The expression builder: Expression (left); building blocks, operators, fields and values(center); unique values (right)
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_labelling
.mp4"></video>

:::

:::{dropdown} Add underligned labels

1. Set up the labels by following the same steps as before.
2. TO underlign labels, click on the underlign-button

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_underlign_labels
.mp4"></video>

:::

:::{dropdown} Move labels independently
Sometimes the placement of labels is not ideal and can obstruct the readability of the map. In this case, you can move labels independently. 

1. On the label toolbar, there is an option to move labels independently. Click on it to activate it. (Note: In some cases, the label toolbar might not be visible. In this case, turn it on by navigating to "View">"Toolbars">activate the Label toolbar)
2. Click on the label you want to move.
3. You will be prompted to select the primary key for joining with internal data storage. You do not need to change it (you can select the ID field of the dataset) and click OK.
4. Click on the label again, now you can move it freely.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_move_labels_independently
.mp4"></video>

:::

:::{dropdown} Add labels to roads
>When working with line features, the labels will align themselves parallel to the line representing the feature. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_add_road_labels
.mp4"></video>

:::

## Symbology for raster data

As we have already learned, raster data are basically a grid of pixels with different (numerical) values. As such, you can't style the shape, fill or outline of raster data. It is only possible to assign colours to the different values of the pixels.

### Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the styling panel for the raster layer
2. Navigate to the Symbology tab  
3. By default, the colour scheme is set to Singleband gray (if you only have one colour band in the data set). Click on __Singleband gray__ and switch to __Singleband pseudocolour__
4. Click on the arrow to the right of the colour ramp. Here you can choose a premade colour ramp
5. You can modify the colour ramp by clicking on the colour ramp itself

``` {figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: raster data colour gradient
width: 600px
---
Colour Ramp Selector
```

In the colour ramp selector, you can adjust each colour step. On the bottom, you can see a plot for the Hue, __Saturation__, __Lightness__ and __Opacity__. Especially latter three are useful to see how your colour ramp will translate. Gradients from light to dark are easier to read: Check if the plot for the __Lightness__ has a more or less linear plot. 

>Examples Video! and how to invert ramp


# Exporting and Importing Styles

As we have already learned, the layers in QGIS are saved separately from the settings and styles of a QGIS Project. Therefore, it can be useful to 

# Examples for Map design

>insert maps and discuss how to achieve this