# Visualisation of Geodata: Symbology and Colors

The representation of geodata in maps is crucial in order to provide useful location-based insights. This subchapter will cover the basics of good map design, how to create a map design in QGIS as well as common mistakes when designing or interpreting maps.

In this chapter we will go over the basics of symbology, colours and how to adjust individual layers in QGIS to create comprehensive maps.

:::{admonition} Recap: Types of Maps
:class: seealso

In general, there are two main types of maps: __topographic maps__ and __thematic maps__.

__Topographic maps__ are intended to be exhaustive, including elements fundamental to localisation (localities, road networks, terrain, hydrography). They represent the physical location of objects in the real world. The representation of elements in topographic maps is done via conventional signs (e.g.: blue for water, green for forests, yellow for agricultural land). 


```{figure} ../../fig/en_30.30.2_topographic_map_examples.png
---
width: 600px
name: Topographic Maps Examples
---
Examples for topographic maps
```

__Thematic maps__ address the distribution of phenomena, including sometimes statistically processed information, such as population size, disease cases, flooding risk, etc. The representation of elements on thematic maps is decided according to the rules of graphic semiology. 


```{figure} ../../fig/en_30.30.2_thematic_maps_examples.png
---
width: 600px
name: Thematic maps examples
---
Examples for thematic maps
```

These two maps use design elements differently. Topographic maps will use symbols and colors out of convention and readability, whereas in designing thematic maps, the symbols and colors you use depend on the context and the information you want to convey.

:::

<!--## Graphic Semiology

__Definition__: Graphic semiology refers to a set of rules allowing the use of a __graphic sign systems__ to convey information. Graphic semiology uses visual variables to construct a system of signs, allowing the graphic translation of information.

Our brain is capable of interpreting graphic relationships between entities in just seconds. Semiology attempts to theorise these interpretation to make the map more effective and relevant.

EDIT: Remove this part?-->

## Visual variables

```{figure} ../../fig/en_30.30.2_graphic_semiology_signs.png
---
width: 500px
name: Graphic information
---
Depending on the type of information you want to display, you can use different graphic signs
```

Visual variables are the __graphical means for visually transcribing information__. The visual variables are __shape, size, hue, value, texture, and orientation__. You can vary these variables to appropriately represent the data at your disposal.  
It allows for the expression of __relationship of difference, order, association, or quantity__ between each element and helps display information.

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

- You can change the 'styling' and color of the data.
- You can add text labels.
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
2. Open the layer styling panel by enabling it under `View`>`Panels`>`Styling Panel`. Usually, the panel will appear on the right side of map canvas.

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

<!---- To Do: add different visualisation for different types of data (discrete vs. continuous values, insert image). For example the amount of rainfall/temperature is a continuous value.-->

## Colours

Colours are arguably the most striking visual variables as they are easily distinguishable. However, depending on the type of data and the information you wish to convey, there are a few things to consider when choosing a colour scheme for your map. The most important variables for colours are the __hue__, the __value__ (saturation) and the __transparency__. 

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
Examples for different colour gradients translated into black and white. Pay attention to the saturation gradient under each example. Source: Stauffer, Reto & Mayr, Georg & Dabernig, Markus & Zeileis, Achim. (2014). Somewhere Over the Rainbow: How to Make Effective Use of Colors in Meteorological Visualizations. Bulletin of the American Meteorological Society. 96. 140710055335002. 10.1175/BAMS-D-13-00155.1.
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

```{note}
Remember that __the layer's symbology is saved within your project file, not within your shapefile!__ If you share a shapefile with a colleague, it will have a different style when they add it to their own project.
```

:::{card} 
### SVG-Symbols, Raster images, and Markers

QGIS let's you use different types markers for symbolization. These can be simple markers, raster images, or SVG-symbols.

- __Simple markers__ are simple shapes such as rectangles, circles, or crosses that can be adjusted in the symbolization layer (color, size, outline, etc.).
- If you select __raster images__, the resolution of the symbol is limited by the amount of pixels in the image. It is not advisable to use high resolution images as symbols on your map because it may overload your PC.
- __SVG-symbols__ are *scaleable vector graphic* symbols. As vector files, they can be scaled to any size while keeping the same resolution. In most cases, if you want to use a more complex symbol (e.g. hospital, school, train station), SVG-symbols are the best option as they let you adjust the symbol (colours, outline, size, etc.)

:::

#### Using Simple Markers

Simple Markers are generally used to create the symbols for most elements on a map. For example, simple markers are used to visualise streets, building outlines, waterbodies, administrative boundaries or other polygons.
Most simple markers consist of a __fill__ and an __outline__. The shape of the marker is generally dependent on the type of vector data (point, polygon, or line).

- The fill determines the fill color of the symbol. You can change the color and transparency. You are also able to make more complex fills such as a line pattern fill, or an SVG-symbol fill.
- The outline determines the color, type, and thickness of the outline. Next to the color and transparency, the outline is significant to distinguish between the different elements. For example, thicker lines for roads usually signify roads of a higher order (such as highways), whereas thin dashed lines might signify footpaths, inaccessible to road vehicles.

<!--ADD: Examples-->

#### Using SVG-Symbols

1. Open the styling panel and open the `single marker` options.
2. Under `Symbol layer type`, select __"SVG Marker"__
3. Scroll down to the SVG-Browser. Here you will find all the folder of your installed SVG-libraries.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

#### Adding an external SVG-library

If you have a library of SVG-symbols as a folder you can add them to your Styling manager.

1. Open the style manager: `setting` > `style manager`
2. Click on `Import / Export` and select `Import items`
3. Navigate to the location where you have saved the library or style and select the file (in most cases .qml but the file type can also be .xml)
4. Now you can select which symbols you wish to import. In most cases, you can select all symbols.
5. Click on `Import`

The new SVG-symbols are in your SVG library.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

## Labels

Labels are text that display information or values of the data. In QGIS, you can either select __Single Labels__ or __Rule-based Labelling__. For each option, an attribute (`value`) that will be displayed on the map. For example, the name of a city or region.  Additionally, you can __change the font, font size, colour and some other styling options__ for the label text. When you create a map, you can add labels to help your reader understand the map quickly. However, be aware that too much text information can overload the map with too much information for the reader to process.

### Single Labels and Rule-based Labeling

QGIS offers two methods to display labels: __Single Labels__ and __Rule-based Labeling__

#### Single Labels

Creates a single label style for every feature in the layer. You can select a attribute (value) which will be displayed. For example, the name of a settlement. You need to know which attribute displays the information you want to display. Look at the attribute table of the dataset to find it out.

```{figure} /fig/labels_single_labels_example_nga_adm1.png
---
width: 600 px
name: single labels example
---
Single labels for each administrative region (adm1) in Nigeria. The reader is able to assign each label to the respective administrative entity.
```

```{figure} /fig/en_30.30.2_assigning_value_to_labels.png
---
width: 600 px
name: assigning value to labels
---
Assigning the correct attribute value in the labeling options. QGIS needs to know which attribute (column) of the attribute table should be displayed as a label. In this case, we want the name of the administrative region (`ADM1_EN`) to be displayed. 
```

#### Adding Single Labels to a Layer

1. In the styling panel, click on the `Labels`-tab underneath the Symbology tab.
2. Select ![](../../fig/en_30.30.2_icon_single_labels) `Single labels`.
3. `Value` is where you choose the attribute that will be displayed as a label. For example `*ADM1_EN*` will display the English names of Nigerian states for each feature in the data set.
4. Let's __change the font__: Open the Font dropdown menu and select Arial. Make the text `Bold` in the Style dropdown menu. Change the colour by clicking on `Colour`, and change the `Size` to 8 pt
5. Let's __add a white buffer__ around the label. In the `Labels` tab, you will find a list with different options to style the labels. Right now, we are in the `Text` menu. Select `Buffer` and check the `Draw text buffer` option. This will make the labels stand out more on dark or crowded maps.
7. Click `Apply` and `OK`.

```{figure} ../../fig/en_30.30.2_setting_up_labels.png
---
width: 600px
name: Setting up labels
---
Setting up labels in QGIS 30.30.2
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_labels
.mp4"></video>

:::{attention}
Single Labels are not always useful. For example, if the dataset is too big, or you only want to display certain features in the dataset. In the example below, there are too many settlements to display labels for each settlements. Instead, it might be useful to only display the regional and national capitals. For such a use case, Rule-based Labeling is ideal.

```{figure} /fig/single_labels_bad_example.png
---
name: single labels bad example
width: 400 px
---
Single Labels was selected to display the names of the settlements (red dots). A map with so much text information is unreadable and the information can hardly be understood. 
```

:::

#### Rule-based Labelling

Create rules using expressions to select accurately which features are to be labeled. Each rule can have a different text formatting. Use this if you want to have more control over the information that will be displayed as labels. For example, you can filter your data to only display the names of regional capitals.

```{figure} /fig/rule-based_labeling_example_settlements_nga.png
---
name: rule-based labeling example settlements nga
width: 500 px
---
Rule-based Labeling let's you apply a filter to datasets. This way, you can display the labels only for selected features without altering the dataset.
```

The rules, or filters, are based on an expression. You can use the ![](../../fig/expression_string_builder_icon.png) `Expression string builder` to the right of the __Filter__ option in the label panel.

#### Adding Rule-based Labels to a Layer

1. In the styling panel, click on the `Labels` tab underneath the Symbology tab.
2. Select ![](/../fig/30.30.2_Icon_rule_based_labeling.png) `Rule-based Labeling`.
3. Add a Rule by clicking on the `+`-button in the left corner of the styling panel. A new window will open in the styling panel. In this window, you will enter the rule (`Filter`) and customize the label font, size, and placement. Additionally, you can enter a description.
4. Enter a Filter (red box in the figure below). The easiest way is to use the `Expression string builder` to the right of the Filter option. Click on the ![](/../fig/expression_string_builder_icon.png)-Symbol. A new panel will open.
5. In the Expression String builder enter a rule. In the example in the video below, we want to only display settlements that are either national or regional capitals. This corresponds to the String `("CLASS" = 1 ) OR ("CLASS" = 2)`. We know this because we know our data and have looked at the attribute table beforehand.
6. Click `OK`
7. Set the font and font size.
8. Click `Apply`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_rule-based_labels.mp4"></video>

```{note}
To add rules to your labels, you need to be familiar with your data! Look at the metadata (in the properties or at the source) and take a look at the attribute table. Think about what the different columns mean and identify the attributes. This might not always be easy, as they might have abbreviated names, but as you work more with data, this will become easier.
```

Below are some further considerations to keep in mind when using labels:

- Only display information that serves the purpose of the map or is helpful to the reader. Useful information can be the name of a settlement or a place, so the reader can assign a certain symbol on the map to this particular place.

- If you want to display different types of information as labels, the font needs to be different so the reader can differentiate between the different types of information that is displayed. A good practice is to display the labels in a similar color to the objects it is referring to. For example, dark blue text for the labels of light blue bodies of water, or brown text for the labels of light-brown houses.

```{figure} ../../fig/good_labels_example.png
---
width: 400 px
name: Axis Maps good labels example
---
A good example of label placement and font. Pay attention to the text colors and orientation. Every label can easily be attributed to the correct cartographic feature. (Source: [Axis Maps](https://www.axismaps.com/guide/labeling))
```

```{Attention}

- In most cases, displaying numerical values as labels is confusing to the reader and makes the map to complex. In most cases, for numerical data, you can choose a different visualization such as colours or symbol size.

:::::{grid} 2
::::{card}

:::{figure} ../../fig/labels_numerical_values_bad_example.png
---
name: numerical labels bad example
---
Numerical Labels
:::

::::

::::{card}

:::{figure} /fig/labels_graduated_symbology_example.png
---
name: graduated symbology instead numerical values
---
[Graduated Symbology](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_data_classification.html#graduated-classification)
:::

::::

:::::

```

- QGIS places the labels automatically. Sometimes, if you are using a lot of black outlines or dark colours, black text is hard to read on the map. In that case, you can add white buffer around the text to make it visible.

```{figure} ../../fig/label_text_buffer_example.png
---
width: 500 px
name: label buffer example
---
A label without a text buffer (left) and a label with a white text buffer (right)
```

```{note}
QGIS renders the labels automatically.
Sometimes the labels can obstruct other symbols. In that case, you can either adjust the placement of the labels in the __Label tab__, or use the ![](../../fig/30.30.2_move_a_label_diagram_callout_icon.png) `Move a Label, Diagram, or Callout`-tool in __Label toolbar__

By default, QGIS renders the labels so that they don't overlap with other labels. This means that not all the labels will be visible if the data is dense or rendered close to each other. You can optimize the rendering under the rendering option. 

```

If you are interested in how to set up and style labels further, take a look at these wiki articles:

You can also read further in the article "[Labeling and text hierarchy in cartography](https://www.axismaps.com/guide/labeling)" by Axis Maps. 

## Symbology for raster data

As we have already learned, raster data are basically a grid of pixels with different (numerical) values. As such, you can't style the shape, fill or outline of raster data. Raster data is visualized by assigning a colour ramp to the pixel value. QGIS offers several options to visualise raster data. For example, you can create a hillshade with digital elevation model (DEM). 

### Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the `styling panel` for the raster layer
2. Navigate to the `Symbology tab`  
3. By default, the colour scheme is set to Singleband Gray (if you only have one colour band in the data set). Click on `Singleband Gray` and switch to `Singleband Pseudocolour`
4. Click on __the arrow to the right of the colour ramp__. Here you can choose a pre-made colour ramp
5. You can modify the colour ramp by __clicking on the colour ramp__.

``` {figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: raster data colour gradient
width: 600px
---
Colour Ramp Selector
```

In the colour ramp selector, you can adjust each colour step. On the bottom, you can see a plot for the Hue, __Saturation__, __Lightness__ and __Opacity__. Especially latter three are useful to see how your colour ramp will translate. Gradients from light to dark are easier to read: Check if the plot for the __Lightness__ has a more or less linear plot.

#### Styling a digital elevation model

Elevation data sets are frequently used to communicate the terrain on a map. By default, an elevation model will be displayed with a gray colour ramp. However, if you don't need the to know the elevation at certain points, you can choose to display the __hillshade__ of the terrain. Hillshading will simulate the shadow of the terrain as if it would be exposed to a light source. In this example, we will use the elevation raster data (.tiff) of Algeria from the Humanitarian Data Exchange platform (humdata.org) To achieve this,

 1. Open the `symbology` tab
 2. Click on `Render type` and select `Hillshade`. You will have an option to select the direction of the light. Conventionally, the light source is positioned in the North-West, so we can keep the default settings. In some cases with rough terrain, it can be useful to make the hillshade __Multidirectional__.
 3. The hillshade will be very dark and cover most of the map. We need to make it lighter...

<!--ADD: Video-->

### Inverting the colour ramp

In some cases, the colour ramp should be inverted to make it easier to read the map:

1. Click on the __arrow next to the Colour ramp__ to open the dropdown menu.
2. Click on `Invert Colour Ramp`.

## Exporting and Importing Styles

The layers in QGIS are saved separately from the settings and styles of a QGIS Project. This means that if you load the same layers into a different QGIS-project, the symbology and styling of the data will be different. QGIS lets you save the symbology and styling of a layer as a separate file (`.qml`-files). Working with `.qml`-files saves you a lot of work and assures consistency between your maps.

A `.qml`-file saves the information of a particular layer. This includes the colours, outlines, shapes, labelling, as well as the Layer configuration, attribute table settings, and other options you have set for a layer in your QGIS-project, that are not related done to the data files themselves. You can choose wether to save only the colour symbology or any additional information.
 
You can export a style into the same folder as the data so your colleagues can apply the same styling when loading the data into QGIS.
Some organisations may also use standarized symbols or colours in their maps. 

For example, if you want to send a layer to your colleague with the same styling as you, it is best to check the "__Layer properties__", "__Symbology__", and "__Labels__" categories (and any additional styling options you have set). If you only wish to save a certain colouring, line thickness, or labeling style, you only need to check the respective boxes.

## Saving or exporting styling settings

1. Open the styling panel and click on `styles`. A dropdown menu will open with the option to export the layer styling.
2. Since in this case, the styling is for exactly that dataset, you can leave all the boxes checked.
3. Select a location and name for the styling. The styling will be saved as a `.qml` file. __Make sure it is saved in the same folder as the dataset and give it the same name as the corresponding dataset. This way it will, when loading the data into QGIS, the styling will automatically be applied.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>

```{figure} ../../fig/en_30.30.2_save_layer_style_window.png
---
width: 350px
name: Save layer styling window
---
Save Layer styling window in QGIS 30.30.2.
```

When working with similar data (e.g.: building types or flooding risk), it is useful to have template styles, that can be quickly loaded into your QGIS-project or saved in your Styling Template library. 

```{Tip}
When a styling is saved in the same location as the data and has the same name as the corresponding dataset, the styling will be automatically applied to the layer when loading the data into QGIS!
```

## Loading a style into a QGIS-project

1. Open the style manager: `Settings` > `Style manager`
2. Click on `import/export` and select `import items`
3. Navigate to the folder where the style is saved and click import.
4. The style should now be available as a preset in the styling panel.

```{note}
You can also import styles directly in the styling panel of a layer. But it will not be added to your style library unless you save it into your library.
```

## Using IFRC-Symbols

With the plugin __"Plugin Resource Sharing"__, you can install symbol and icon libraries used by the Red Cross and UN, as well as other useful symbols.

1. Install the __"Plugin Resource Sharing"__ by opening the plugin installation window and searching for the plugin.
2. Once installed, open the plugin interface by clicking on `plugin` > `Plugin Resource Sharing`
3. Search for packages by the Red Cross and UN
4. Install the packages.

Now the symbols should be available in the styling manager in the SVG folder.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_resource_sharing_plugin.mp4"></video>

```{tip}
Make sure to check out the other resources available in the resource sharing plugin and see if they are useful to you.
```

## Further Resources

- [Cartography Guide](https://www.axismaps.com/guide) by [Axis Maps](axismaps.com)
- Tutorial on [how to import the SIMS Color Palette into QGIS](https://learn-sims.org/geospatial/importing-sims-color-palette-to-qgis/) 
- Tutorial on [how to create a shaded relief map in QGIS](https://learn-sims.org/geospatial/creating-a-shaded-relief-map-in-qgis/)
- [Creating a 3W (Who, What, Where) Infographic](https://learn-sims.org/information-design/creating-a-3w-who-what-where-infographic/)
