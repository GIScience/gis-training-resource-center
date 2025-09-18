# Visualisation


__🔙[Back to Homepage](/content/intro.md)__

## Visualising vector data

### Symbology

QGIS offers various ways to visualize vector data. In the Symbology Tab, you can select between various symbolization methods

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

:::{dropdown} Only display the outlines of polygons

In this example, we want to change the symbology of a single layer so that __only the outlines of the polygons are visible__. 

To change the symbology of a single layer:
1. Open the `Styling panel` and navigate to the symbology tab. By default, the symbology will be set to `Single Symbol`. This means that the same colours and contours will be applied to all the features in that layer.
2. Click on `Simple Fill`
3. Click on the arrow to the right of `Fill Colour`
4. Check the `Transparent Fill` option.

```{figure} ../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: en_30.30.2_vector_layer_styling_transparent_wiki
width: 500 px
---
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

:::

:::{dropdown} Change the styling for multiple overlayed layers

In this exercise, we will apply the same style to all features in a layer, but we will change multiple layers and overlay them so each is visible in a different style. We have the polygons for 3 administrative levels.

```{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: en_30.30.2_changing_layer_style_1_wiki
height: 400 px 
---
Order the layers and navigate to the styling panel of the topmost layer
```

1. Add the `Adm0`, `Adm1` and `Adm2` shapefiles to your Session 2 project.
2. Order the layers so they are all visible: Put the `Adm2` layer at the bottom, then the `Adm1` then `Adm0`. At first, this might look weird because `Adm0` will cover everything.
3. Change the symbology of the Adm0 layer by opening the stlying panel and navigating to the Symbology tab. 


```{figure} ../../fig/en_30.30.2_changing_layer_style_2.png
---
name: en_30.30.2_changing_layer_style_2_wiki
width: 350 px
align: left
---
Change the Fill type
```

4. Click on `Simple Fill` to open the style options.
5. Expand the `Fill Colour` menu and check the `Transparent Fill` option. This will make only the boundaries visible, so __we will be able to see the layer under this one__.
6. Choose a `Stroke Colour`, and make the `Stroke Width` 0.66 Millimeters.
7. Click OK
8. __Repeat the same process__ for the Adm1 layer, using the same colour as for Adm0 (it will be in "Recent colors) and leave the stroke width at 0.26.
9. Now we can see the boundaries of the country and its states, and behind that we can see the districts (Adm2).
10. Let's make the districts layer's style consistent with the others.

<br/><br/>

11. Choose a `Fill Color`
12. Use the same Stroke Colour` as for Adm0 and Adm1, but make the width 0.1 Millimeters and the Stroke Style a __Dash Line__
13. Click OK and look at your map: hopefully it's starting to look nicer!

```{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
name: en_30.30.2_changing_layer_style_3_wiki
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
name: en_30.30.2_categorized_layer_symbology_1_wiki
width: 500 px
---
Change the symbology type to "categorized" and choose the Value (variable) you wish to display
```
3. Now we need to __choose which attributes we want to display through the symbology__. In this case, it could be the number of casualtiees, or the actor who perpetrated the act. Let's categorize the features by `event_type`
4. Click on `Classify` to __list all the unique values contained__ in the `event_type` field (i.e. all the possible types of security incidents recorded in our table)
5. Now we can __change the style of each single value__
6. Double click on the value `Explosions`
7. At the bottom of the __Symbol selector__ window, choose a symbol to make Explosion points stand out.
8. Click on `OK`, then Apply to preview what the layer will look like.
9. Click `OK` again.

```{figure} ../../fig/en_30.30.2_categorized_layer_symbology_2.png
---
name: en_30.30.2_categorized_layer_symbology_2_wiki
width: 500 px
---
By double clicking on the __unique values__ in the classified list, you can change the symbol for each value
```

Now we have a map of Nigeria where you can locate the areas, that are affected by explosions more than others. On the map below, we also added text labels, which will be explained below.

```{figure} ../../fig/en_exercise_map_design_example_Nigeria.png
---
name: en_exercise_map_design_example_Nigeria_wiki
width: 500px
---
Regions affected by explosions in Nigeria
```
:::

:::{dropdown} Style data based on variable ranges ("__Graduated__" styling)

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
name: en_30.30.2_symbology_variable_ranges_wiki
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
name: en_30.30.2_symbology_variable_ranges_2_wiki
width: 500 px
---
You can categorize the continuous values into classes and assign a colour ramp 
```

The following map shows the most populated States of Nigeria using a graduated colour categorization. These types of maps are called __choropleth maps__. 

```{figure} ../../fig/en_map_design_example_variable_ranges.png
---
name: en_map_design_example_variable_ranges_wiki
width: 500px
---
A map showing the population of Nigerian states
```
:::


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
width: 500 px
name: en_30.30.2_setting_up_labels_wiki
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
width: 500 px
name: en_30.30.2_adding_rule-based_labels_wiki
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
width: 500 px
name: en_30.30.2_adding_rule-based_labels_expression_builder_wiki
---
The expression builder: Expression (left); building blocks, operators, fields and values(center); unique values (right)
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_labelling
.mp4"></video>

:::

:::{dropdown} Add underlined labels

1. Set up the labels by following the same steps as before.
2. TO underline labels, click on the underline-button

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

## Visualising raster data

### Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the `styling panel` for the raster layer
2. Navigate to the `Symbology tab`  
3. By default, the colour scheme is set to Singleband gray (if you only have one colour band in the data set). Click on `Singleband Gray` and switch to `Singleband pseudocolour`
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

:::{dropdown} Styling a digital elevation model

Elevation data sets are frequently used to communicate the terrain on a map. By default, an elevation model will be displayed with a gray colour ramp. However, if you don't need the to know the elevation at certain points, you can choose to display the __hillshade__ of the terrain. Hillshading will simulate the shadow of the terrain as if it would be exposed to a lightsource. In this example, we will use the elevation raster data (.tiff) of Algeria from the Humanitarian Data Exchange platform (humdata.org) To achieve this,

 1. Open the `symbology` tab
 2. Click on `Render type` and select `Hillshade`. You will have an option to select the direction of the light. Conventionally, the light-source is positioned in the North-West, so we can keep the default settings. In some cases with rough terrain, it can be useful to make the Hillshade __Multidirectional__.
 3. The Hillshade will be very dark and cover most of the map. We need to make it lighter...

<!--ADD: Video-->

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