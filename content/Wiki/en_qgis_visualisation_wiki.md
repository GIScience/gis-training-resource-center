# Visualisation

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

__🔙[Back to Homepage](/content/intro.md)__

## Visualisation of Vector data

### Symbology

QGIS offers various ways to visualize vector data. In the Symbology Tab, you can select between various symbolization methods

::::{tab-set}

:::{tab-item} Single-Symbol
- Assigns one symbol to every feature of the dataset, no matter if the attributes are different.

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

----

### Labels

Labels are text that display information or values of the data. In QGIS, you can either select __Single Labels__ or __Rule-based Labelling__. For each option, an attribute (`value`) that will be displayed on the map. Additionally, you can __change the font, font size, colour and some other styling options__ for the label text. 

::::{tab-set}

:::{tab-item} Single Labels

- Creates a single label style for every feature in the layer. You can select a attribute (value) which will be displayed. For example, the name of a settlement. You need to know which attribute displays the information you want to display. Look at the attribute table of the dataset to find it out. 

:::

:::{tab-item} Rule-based Labelling

- Create rules using expressions to select accurately which features are to be labeled.
- Each rule can have a different text formatting

:::

::::

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

:::{dropdown} Adding different label styles to the same layer

Sometimes you will need to create two different label styles for different features of a single layer. In this example, we will create one label style for the *Country Capital*, and another one for the *State Capitals*

1. Open the styling panel for the `"NGA_settlements_nga"` layer and click on the `Labels` tab
2. Select `Rule-based Labelling`
3. Click on the __Add Rule__ button at the bottom (the "+"-sign) and __create the first rule__
4. For __Value__, select `"NAME"` (so that the labels will show the name of each city), then click on the `"ε"-button` next to the __Filter__ bar.

```{figure} ../../fig/en_30.30.2_adding_rule-based_labels.png
---
width: 500px
name: adding rule-based labels
---
To add rule-based labels, you need to enter an expression
```

5. In the central column, expand `Fields and Values` to display a list of all the fields in your layer and double-click on `"CLASS"` to __add it to the expression frame__ on the left.
6. In the right column, click on `All unique` to list all unique values contained in the Class field. In this dataset, `"CLASS"=1` designates the capital city, whereas `"CLASS"=2` designate other major cities. Make sure to familiarise yourself with the dataset at your disposal, so you know what the different attributes represent.
7. Click on the `"="` operator, then doube-click on the `value 1` (which represent the Country capital in this case). Click `OK`.
8. Scroll down to __change the label style__. Make it Arial, bold, black, 12pt and add a white buffer.
9. __Repeat steps 4 to 9__, but select `Value 2` (State capitals) and make the label black, bold, 10pt, no buffer.
10. Click `Apply`, the `OK`.

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

1. On the `label toolbar`, there is an option to __move labels independently__. Click on it to activate the tool. (Note: In some cases, the label toolbar might not be visible. In this case, turn it on by navigating to `View`>`Toolbars`>activate the Label toolbar)
2. Click on the __label you want to move__.
3. You will be prompted to select the primary key for joining with internal data storage. __You do not need to change it__ (you can select the ID field of the dataset) and click `OK`.
4. Click on the label again, now you can move it freely.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_move_labels_independently
.mp4"></video>

:::

:::{dropdown} Add labels to roads
>When working with line features, the labels will align themselves parallel to the line representing the feature. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_add_road_labels
.mp4"></video>

:::


---

## Visualisation of Raster data

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


:::{dropdown} Styling an elevation model

Elevation data sets are frequently used to communicate the terrain on a map. By default, an elevation model will be displayed with a gray colour ramp. However, if you don't need the to know the elevation at certain points, you can choose to display the __hillshade__ of the terrain. Hillshading will simulate the shadow of the terrain as if it would be exposed to a lightsource. In this example, we will use the elevation raster data (.tiff) of Algeria from the Humanitarian Data Exchange platform (humdata.org) To achieve this,

 1. Open the `symbology` tab
 2. Click on `Render type` and select `Hillshade`. You will have an option to select the direction of the light. Conventionally, the lightsource is positioned in the North-West, so we can keep the default settings. In some cases with rough terrain, it can be useful to make the Hillshade __Multidirectional__.
 3. The Hillshade will be very dark and cover most of the map. We need to make it lighter...

>Example Video and continue explanation, maybe an algorithm would be better?

:::

### Inverting the colour ramp

In some cases, the colour ramp should be inverted to make it easier to read the map:
1. Click on the __arrow next to the Colour ramp__ to open the dropdown menu.
2. Click on `Invert Colour Ramp`.

## Exporting and Importing styles

::::{tab-set}
:::{tab-item} Saving or exporting styling settings

1. Open the styling panel and click on `styles`. A dropdown menu will open with the option to export the layer styling.
2. Since in this case, the styling is for exactly that dataset, you can leave all the boxes checked.
3. Select a location and name for the styling. The styling will be saved as a `.qml` file. __Make sure it is saved in the same folder as the dataset and give it the same name as the corresponding dataset. This way it will, when loading the data into QGIS, the styling will automatically be applied.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>
:::

:::{tab-item} Loading a style into your QGIS-project

1. Open the style manager: `Settings` > `Style manager`
2. Click on `import/export` and select `import items`
3. Navigate to the folder where the style is saved and click import.
4. The style should now be available as a preset in the styling panel.

```{note} 
You can also import styles directly in the styling panel of a layer. But it will not be added to your style library unless you save it into your library.
```
:::

:::{tab-item} Using IFRC symbols

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
:::

:::{tab-item} Using SVG-symbols

1. Open the styling panel and open the `single marker` options.
2. Under `Symbol layer type`, select __"SVG Marker"__
3. Scroll down to the SVG-Browser. Here you will find all the folder of your installed SVG-libraries.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

:::

:::{tab-item} Adding an external SVG-library or other style libraries

If you have a library of SVG-symbols as a folder you can add them to your Styling manager.

1. Open the style manager: `setting` > `style manager`
2. Click on `Import / Export` and select `Import items`
3. Navigate to the location where you have saved the library or style and select the file (in most cases .qml but the file type can also be .xml)
4. Now you can select which symbols you wish to import. In most cases, you can select all symbols.
4. Click on `Import`
The new SVG-symbols are in your SVG library.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

:::
::::