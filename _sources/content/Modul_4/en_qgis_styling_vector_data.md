# Styling Vector Data

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

In the styling panel you can change the styling for all features of a layer, set up categories for different symbols, 
create labels, and create colour ramps to differentiate between features with variable values.

:::{dropdown} Video: Opening the styling panel
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_the_styling_panel.mp4"></video>
:::


## Symbology for Vector Data



You can use graphical variables to style vector data. As we have already learned, vector data can be either points, 
lines, or polygons. There are different options to symbolize these different types of vector data. In this subchapter, 
we will focus on a few common examples.

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

### Styling Vector data

QGIS offers various ways to visualize vector data. In the Symbology Tab, you can select between various symbolization 
methods:

<!--CONTINUE HERE-->

::::{tab-set}

:::{tab-item} Single-Symbol
- Assigns one symbol to every feature of the dataset, no matter if the attributes are different.

__For example__, assign a hospital symbol to a layer that only contains points showing the location of hospitals.
:::

:::{tab-item} Categorized  

- Classifies features into categories using an attribute (`Value`). 
- A category is created for each unique value of this attribute. 
- Each category can be assigned to a different symbol.
- This can be used for nominal as well as ordinal data.

__For example__, assign a different symbol for each type of building (industrial, commercial, public, residential,...) 

:::

:::{tab-item} Graduated

- Creates classes for numerical data.
- A colour gradient can be selected to represent the distribution of the data

__For example__, create 6 classes of population sizes and assign a color gradient from white to red to indicate the population size in a district.

:::

:::{tab-item} Rule-based

- Create rules using an expression and assign a symbol for the features where the rule applies.
- You can specify more accurately the features you want to symbolize.
- You can use values from different attributes (e.g. building type and city district).
- The expression builder helps you create rules by displaying the available values, fields, operators, etc...

__For example__, select a symbol for every health facility that is a hospital and has exceeded it's capacity.

:::

::::



<!--ADD: HOWTOS from the wiki-->

<!--ADD: Examples of simple markers for Points, Lines, Polygons
ALSO: With different thickness-->

:::{card} 
:class-card: sd-text-justify sd-text-black sd-border-2
__SVG-Symbols, Raster images, and Markers__
^^^
QGIS let's you use different types markers for symbolization. These can be simple markers, raster images, or 
SVG-symbols.

- __Simple markers__ are simple shapes such as rectangles, circles, or crosses that can be adjusted in the symbolization layer (colour, size, outline, etc.).
- If you select __raster images__, the resolution of the symbol is limited by the amount of pixels in the image. It is not advisable to use high resolution images as symbols on your map because it may overload your PC.
- __SVG-symbols__ are *scaleable vector graphic* symbols. As vector files, they can be scaled to any size while keeping the same resolution. In most cases, if you want to use a more complex symbol (e.g. hospital, school, train station), SVG-symbols are the best option as they let you adjust the symbol (colours, outline, size, etc.)

:::

### Using Simple Markers

Simple Markers are generally used to create the symbols for most elements on a map. For example, simple markers are 
used to visualise streets, building outlines, waterbodies, administrative boundaries or other polygons.
Most simple markers consist of a __fill__ and an __outline__. The shape of the marker is generally dependent on the 
type of vector data (point, polygon, or line).

- The fill determines the fill colour of the symbol. You can change the colour and transparency. You are also able to make more complex fills such as a line pattern fill, or an SVG-symbol fill.
- The outline determines the colour, type, and thickness of the outline. Next to the colour and transparency, the outline is the most critical for distinguishing between different elements. For example, thicker lines for roads usually signify roads of a higher order (such as highways), while thin dashed lines might signify footpaths, inaccessible to road vehicles.

```{admonition} Optional: Now it's your turn
:class: tip

Check out Paul Knight's [tutorial on how to create a proportional circle map](https://learn-sims.org/geospatial/creating-a-proportional-circle-map-in-qgis/) in the SIMS learning portal. 
```


### Using SVG-Symbols

In some cases, you might want to use more complex symbols in your map. For example, you want to use a cross to signify 
a hospital, a book to signify a library, or a plane to signify an airport. In these cases, you can use SVG-symbols. 
Keep in mind that, ordinarily, SVG-symbols work only for point data. 
To use SVG-symbols:

1. Open the styling panel and open the `single marker` options.
2. Under `Symbol layer type`, select __"SVG Marker"__
3. Scroll down to the SVG-Browser. Here you will find all the folder of your installed SVG-libraries.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

There is already a default library of SVG-symbols. If you are looking for a specific symbol, try searching for it in the search bar 

#### Adding an external SVG-library

QGIS also offers the option to add your own SVG-libraries, for example if your organisation uses a specific set of 
icons. 
If you have a library of SVG-symbols as a folder you can add them to your Styling manager.

1. Open the style manager: `Settings` > `Style Manager`
2. Click on `Import / Export` and select `Import items`
3. Navigate to the location where you have saved the library or style and select the file (in most cases .qml but the file type can also be .xml)
4. Now you can select which symbols you wish to import. In most cases, you can select all symbols.
5. Click on `Import`

The new SVG-symbols are in your SVG library.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

#### Using IFRC-Symbols

:::{admonition} IFRC- and UN-Symbols repositories
class: tip

The IFRC provides icons and symbols that can be used in your maps. You can find them under [this link](https://go-user-library.ifrc.org/brand-design/iconography). 

There is also a library with humanitarian icons by the [United Nations Office for the Coordination of Humanitarian affairs](https://www.unocha.org) which can be found [here](https://github.com/mapaction/ocha-humanitarian-icons-for-gis?tab=readme-ov-file). The files are available in different formats you can use in QGIS. 

:::

## Labels

Labels are text that display information or values of the data. In QGIS, you can either select __Single Labels__ or 
__Rule-based Labelling__. For each option, an attribute (`value`) that will be displayed on the map. For example, the 
name of a city or region.  Additionally, you can __change the font, font size, colour and some other styling options__ 
for the label text. When you create a map, you can add labels to help your reader understand the map quickly. However, 
be aware that too much text information can overload the map with too much information for the reader to process.

### Single Labels and Rule-based Labeling

QGIS offers two methods to display labels: __Single Labels__ and __Rule-based Labeling__

#### Single Labels

Creates a single label style for every feature in the layer. You can select a attribute (value) which will be 
displayed. For example, the name of a settlement. You need to know which attribute displays the information you want to 
display. Look at the attribute table of the dataset to find it out.

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
4. Let's __change the font__: Open the font dropdown menu and select Arial. Make the text `Bold` in the Style dropdown menu. Change the colour by clicking on `Colour`, and change the `Size` to 8 pt
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

Create rules using expressions to select accurately which features are to be labeled. Each rule can have a different 
text formatting. Use this if you want to have more control over the information that will be displayed as labels. For 
example, you can filter your data to only display the names of regional capitals.

```{figure} /fig/rule-based_labeling_example_settlements_nga.png
---
name: rule-based labeling example settlements nga
width: 500 px
---
Rule-based labeling allows you to filter datasets. This way, you can display the labels only for selected features without altering the dataset.
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

- If you want to display different types of information as labels, the font needs to be different so the reader can differentiate between the different types of information that is displayed. A good practice is to display the labels in a similar colour to the objects it is referring to. For example, dark blue text for the labels of light blue bodies of water, or brown text for the labels of light-brown houses.

```{figure} ../../fig/good_labels_example.png
---
width: 400 px
name: Axis Maps good labels example
---
A good example of label placement and font. Pay attention to the text colours and orientation. Every label can easily be attributed to the correct cartographic feature. (Source: [Axis Maps](https://www.axismaps.com/guide/labeling))
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
QGIS renders labels automatically.
Sometimes labels can obstruct other symbols. In that case, you can either adjust the placement of the labels in the __Label tab__, or use the ![](../../fig/30.30.2_move_a_label_diagram_callout_icon.png) `Move a Label, Diagram, or Callout`-tool in __Label toolbar__

By default, QGIS renders the labels so that they don't overlap with other labels. This means that not all the labels will be visible if the data is dense or rendered close to each other. You can optimize the rendering under the rendering option. 

```

:::{admonition} Now it's your turn!

Take the time to apply what we've learned yourself by doing one or two of the [exercises of module 4](/content/Modul_4/en_qgis_modul_4_exercises.md).

```{card}
:link: 
```

:::

<!--MOVE: move admonition a bit up?--->






:::{Attention}

Check out the [wiki article](/content/Wiki/en_qgis_representation_wiki.md) for detailed, step-by-step tutorials on how to use the different features of the styling panel.

You can also read further in the article "[Labeling and text hierarchy in cartography](https://www.axismaps.com/guide/labeling)" by Axis Maps. 


:::

## Exporting and Importing Styles

The layers in QGIS are saved separately from the settings and styles of a QGIS Project. This means that if you load the same layers into a different QGIS project, the symbology and styling of the data will be different. QGIS lets you save the symbology and styling of a layer as a separate file (`.qml`-files). Working with `.qml`-files saves you a lot of work and assures consistency between your maps.

A `.qml`-file saves the information of a particular layer. This includes the colours, outlines, shapes, labelling, as well as the Layer configuration, attribute table settings, and other options you have set for a layer in your QGIS project that are not related done to the data files themselves. You can choose whether to save only the colour symbology or any additional information.
 
You can export a style into the same folder as the data so your colleagues can apply the same styling when loading the data into QGIS.
Some organisations may also use standarized symbols or colours in their maps. 

For example, if you want to send a layer to your colleague with the same styling as you, it is best to check the "__Layer properties__", "__Symbology__", and "__Labels__" categories (and any additional styling options you have set). If you only wish to save a certain colouring, line thickness, or labeling style, you only need to check the respective boxes.

### Saving or exporting styling settings

1. Open the styling panel and click on `Styles`. A dropdown menu will open with the option to export the layer styling.
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

When working with similar data (e.g. building types or flooding risk), it is useful to have template styles, that can be quickly loaded into your QGIS-project or saved in your Styling Template library. 

```{Tip}
When a styling is saved in the same location as the data and has the same name as the corresponding dataset, the styling will be automatically applied to the layer when loading the data into QGIS!
```

### Loading a style into a QGIS-project

1. Open the style manager: `Settings` > `Style manager`
2. Click on `import/export` and select `import items`
3. Navigate to the folder where the style is saved and click import.
4. The style should now be available as a preset in the styling panel.

```{note}
You can also import styles directly in the styling panel of a layer. But it will not be added to your style library unless you save it into your library.
```


## Further Resources

- [Cartography Guide](https://www.axismaps.com/guide) by [Axis Maps](axismaps.com)
- Tutorial on [how to import the SIMS Colour Palette into QGIS](https://learn-sims.org/geospatial/importing-sims-color-palette-to-qgis/) 
- Tutorial on [how to create a shaded relief map in QGIS](https://learn-sims.org/geospatial/creating-a-shaded-relief-map-in-qgis/)
- [Creating a 3W (Who, What, Where) Infographic](https://learn-sims.org/information-design/creating-a-3w-who-what-where-infographic/)