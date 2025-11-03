::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Styling Vector Data

The previous chapter went over the fundamentals of graphical symbolisation and the visual variables. In this chapter, we want to apply our understanding of visual representation and learn how to use the styling panel in QGIS to customize how the layers in your QGIS project are visualised.

## Styling Panel

```{figure} ../../fig/en_30.30.2_styling_panel.png
---
height: 400px
name: en_30.30.2_styling_panel
align: left
---
Styling panel in QGIS 3.30.2.
```

For each layer in QGIS, there is a styling panel where you can change the symbology, colour and label for the features in that layer. There are two ways to open the layer styling options in QGIS:  

1. Right click on the layer you wish to style and select `properties`. A new window will open up with a vertical tab section on the left. Navigate to the `symbology` tab. 
2. Open the layer styling panel by enabling it under `View`>`Panels`>`Styling Panel`. Usually, the panel will appear on the right side of the map canvas.

On the left of the styling panel you can choose the different tabs to access different styling options.

In the styling panel you can change the styling for all features of a layer, set up categories for different symbols, 
create labels, and create colour ramps to differentiate between features with variable values.

:::{dropdown} Video: Opening the styling panel
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_the_styling_panel.mp4"></video>
:::

## Symbology for Vector Data

You can use graphical variables to style vector data. As we have already learned, vector data can be either points, 
lines, or polygons. There are different options to symbolize these different types of vector data. 

```{figure} ../../fig/en_symbolization_vector_data.png
---
name: en_symbolization_vector_data
width: 750px
---
Symbolization for vector data; Source: White, T. (2017). Symbolization and the Visual Variables. *The Geographic Information Science & Technology Body of Knowledge (2nd Quarter 2017 Edition), John P. Wilson (ed.). DOI: 10.2222/gistbok/2017.2.3 .
```

```{note}
Remember that __the layer's symbology is saved within your project file, not within your shapefile!__ If you share a shapefile with a colleague, it will have a different style when they add it to their own project.
```

QGIS let's you visualise data using simple markers, SVG-files or Raster-files. Most commonly, you will work with simple markers. These are generally used to create the symbols for most elements on a map. For example, simple markers are used to visualise streets, building outlines, waterbodies, administrative boundaries or other polygons.
Most simple markers consist of a __fill__ and an __outline__. Depending on the type of geometry in the layer, you will have to use have different symbology options. 


- The fill determines the fill colour of the symbol. You can change the colour and transparency. You are also able to make more complex fills such as a line pattern fill, or an SVG-symbol fill.
- The outline determines the colour, type, and thickness of the outline. Next to the colour and transparency, the outline is the most critical for distinguishing between different elements. For example, thicker lines for roads usually signify roads of a higher order (such as highways), while thin dashed lines might signify footpaths, inaccessible to road vehicles.
- You can either style a single symbol for each layer or use different styles based on a [categorisation method](/content/Module_3/en_qgis_data_classification.md). 

In the Symbology Tab, you can select between various symbolization methods (see {numref}`en_3.36_m4_symbolisation_methods`). The most important ones are __Single Symbol__, __Categorised__, __Graduated__, and __Rule-based__. 

```{figure} /fig/en_3.36_m4_symbolisation_methods.png
---
name: en_3.36_m4_symbolisation_methods
width: 500 px
---

```

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
- A colour gradient can be selected to represent the distribution of the data.

__For example__, create 6 classes of population sizes and assign a color gradient from white to red to indicate the population size in a district (see [Module 3: Geodata Classifification](/content/Module_3/en_qgis_data_classification.md)).

:::

:::{tab-item} Rule-based

- Create rules using an expression and assign a symbol for the features where the rule applies.
- You can specify more accurately the features you want to symbolize.
- You can use values from different attributes (e.g. building type and city district).
- The expression builder helps you create rules by displaying the available values, fields, operators, etc...

__For example__, select a symbol for every health facility that is a hospital and has exceeded it's capacity.

:::

::::

Below, we will go over some common styling methods used in cartography. 

### Styling administrative boundaries (Polygons)

When creating situational reports, you will frequently use administrative boundaries. In the example below, we want to create an overview map using the administrative boundaries of Nigeria. In order to visualise all the three administrative boundaries at the same time, we need to set the symbology for each layer so the layers below are visible, and the hierarchy of the administrative levels is distinguishable. 

```{admonition} *Optional*: Now it's your turn

You can follow along by downloading the [administrative boundaries of Nigeria](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/nga_adm_osgof_20190417.zip) by [OCHA Nigeria](https://data.humdata.org/dataset/cod-ab-nga).

```

#### Only display the outlines of polygons

Now, we want to change the symbology of a layer so that __only the outlines of the polygons are visible__. This is necessary to make layers below this one visible.

To change the symbology of a single layer:
1. Open the `Styling panel` and navigate to the symbology tab. By default, the symbology will be set to `Single Symbol`. This means that the same colours and contours will be applied to all the features in that layer.
2. Click on `Simple Fill`.
3. Click on the arrow to the right of `Fill Colour`.
4. Check the `Transparent Fill` option.

```{figure} ../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: en_30.30.2_vector_layer_styling_transparent
width: 500 px
---
```

:::{dropdown} Video: Making the fill colour transparent

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

:::

#### Adjusting the Styles of Multiple Overlaying Layers

__Step 1: Ordering the layers__

1. Import the administrative boundaries into your QGIS-project.
2. We need to order the layers in the Layers panel so that the `adm0`-layer sits on top, followed by `adm1` and `adm2`. At first, this might look weird because `Adm0` will cover everything.

```{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: en_30.30.2_changing_layer_style_1
height: 400px 
---
Order the layers and navigate to the styling panel of the topmost layer
```

3. Change the symbology of the Adm0 layer by opening the styling panel and navigating to the Symbology tab. 
4. Click on `Simple Fill` to open the style options.
5. Expand the `Fill Colour` menu and check the `Transparent Fill` option. This will make only the boundaries visible, so __we will be able to see the layer under this one__.
6. Choose a `Stroke Colour`, and make the `Stroke Width` 0.66 Millimeters.
7. Click OK.
8. __Repeat the same process__ for the Adm1 layer, using the same colour as for Adm0 (it will be in "Recent colors) and leave the stroke width at 0.26.
9. Now we can see the boundaries of the country and its states, and behind that we can see the districts (Adm2).
10. Let's make the district layer's style consistent with the others.
11. Choose a `Fill Color`.
12. Use the same Stroke Colour` as for Adm0 and Adm1, but make the width 0.1 Millimeters and the Stroke Style a __Dash Line__.
13. Click OK and look at your map: hopefully it's starting to look nicer!

```{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
width: 500 px
name: en_30.30.2_changing_layer_style_3
---
The styling of a vector data consists of the colour and the outline.
```

:::{dropdown} Video: Adjusting the style for multiple layers
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_change_style_for_multiple_layers
.mp4"></video>
:::


#### Creating a Choropleth Map ("Gradudated Styling)


If a layer contains numeric values that are continuous, they can be organized in intervals. These intervals can be displayed in graduated colours. In this exercise, we assign colours to Adm1 polygons based on the total population of each State.


1. Download the [NGA_Adm1_Pop shapefile](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/NGA_adm1_pop.zip) and save it in your shapefile folder.
2. In QGIS, turn off the Adm1 and Adm2 layer, leaving only Adm0.
3. Drag the shapefile NGA_Adm1_Pop into your map.
4. Open its `Symbology` options and choose `Graduated`.
5. __Select the value you want to use to assign colours__, in this case, it will be `total_pop`.

```{figure} ../../fig/en_30.30.2_symbology_variable_ranges.png
---
name: en_30.30.2_symbology_variable_ranges
width: 550px
---
With variable ranges, select __Graduated__ symbology and choose the attribute with continuous values
```

6. Click on `Classify` to __list all values divided in classes__.
7. Choose __how many classes__ you want the data to be divided into ‒ let's say 4.
8. By default, the colour ramp will be red. However, red is not the right colour to use for population count, as it is generally used to communicate negative elements, such as food insecurity or cholera cases.
9. Click on __the arrow next to the colour ramp__ to choose another combination of colours - let's say a color ramp from white to blue.
10. Click `Apply` to preview the look of your layer, then `OK`.

```{figure} ../../fig/en_30.30.2_symbology_variable_ranges_2.png
---
name: en_30.30.2_symbology_variable_ranges_2
width: 500px
---
You can categorize the continuous values into classes and assign a colour ramp .
```

The following map shows the most populated States of Nigeria using a graduated colour categorization. These types of maps are called __Choropleth maps__. 

```{figure} ../../fig/en_map_design_example_variable_ranges.png
---
name: en_map_design_example_variable_ranges
width: 500px
---
A map showing the population of Nigerian states.
```

:::{dropdown} Video: How to create a choropleth map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_graduated_styling
.mp4"></video>
:::

#### Creating a graduated symbols map

Graduated Symbols are useful when you have more information on your map, and creating a choropleth map is not possible, 
or in situations when you want to communicate two variables on a single map. For example, it is easy to combine 
choropleth maps with graduated symbols.
Creating graduated symbol maps is done in a similar way to creating choropleth maps, but it involves one extra step: 
Creating Centroids of the administrative boundaries. Centroids are points that are placed at the calculated centre of 
polygons (see [Module 5](/content/Modul_5/en_qgis_non_spatial_tools.md)).  
We will be using the same layer as for the choropleth map (see {numref}`en_map_design_example_variable_ranges`): 
`NGA_Adm1_Pop`.

1. In the [processing toolbox](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html?highlight=processing+toolbox#toolbox-toolbars), search for the tool `centroids`. <kbd>Double-Click</kbd> on it. A new window will open (see {numref}`en_3.36_m4_centroids`)

```{figure} /fig/en_3.36_m4_centroids.png
---
name: en_3.36_m4_centroids
width: 500 px
---
Creating centroids in QGIS 3.36.
```

2. Under `Input Layer`, select the `NGA_Adm1_Pop`-layer. Click on `Run`.
3. A new point layer called `Centroids` will appear in your layers panel. Open its styling panel and navigate to the symbology tab.
4. Set the symbolisation method to `Graduated`.
5. Under __Value__, select `total_pop`.
6. Change the __Method__ from `Colour` to `Size`.
7. Click on `Classify`. 
8. *Optional*: Change the Colour and Transparency of the Circles. 

```{figure} /fig/en_m4_graduated_symbols_example.png
---
name: en_m4_graduated_symbols_example
width: 550 px
---
A map of Nigeria displaying the same data. Once using graduated colours (choropleth) and graduated symbols (proportional circles). 
```

:::{dropdown} Video: How to create a proportional circles map

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_3.36_graduated_symbols.mp4"></video>

:::


### Using different styles in a single layer

By categorizing or classifying data in a single layer, we are able to assign different styles to each classification. 
We can use symbology to __show the difference between features__ in the same layer. For example, it could be different types of buildings, quantities of Covid cases by district, or types of roads. We can choose a specific attribute of a dataset to assign different colors, outlines, or sizes to features:

#### Setting different point symbols for different features

1. Download the [ACLED security incidents geopackage](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/NGA_ACLED_security_incidents.zip) and load it into your QGIS-project. It is a point layer with each point indicating a distinct security incident.
2. Open the `Symbology tab` for that layer and choose `Categorized` instead of Single Symbol.   

```{note} 
Categorized symbology is used when you have ***discrete*** variables.
```

```{figure} ../../fig/en_30.30.2_categorized_layer_symbology_1.png
---
name: en_30.30.2_categorized_layer_symbology_1
width: 500px
---
Change the symbology type to "categorised" and choose the Value (variable) you wish to display.
```

3. Now we need to __choose which attributes we want to display through the symbology__. In this case, it could be the number of casualties, or the actor who perpetrated the act. Let's categorize the features by `event_type`.
4. Click on `Classify` to __list all the unique values contained__ in the `event_type` field (i.e. all the possible types of security incidents recorded in our table).
5. Now we can __change the style of each single value__.
6. Double click on the value `Explosions`.
7. At the bottom of the __Symbol selector__ window, choose a symbol to make Explosion points stand out.
8. Click on `OK`, then Apply to preview what the layer will look like.
9. Click `OK` again. 

```{figure} ../../fig/en_30.30.2_categorized_layer_symbology_2.png
---
name: en_30.30.2_categorized_layer_symbology_2
width: 500px
---
By double clicking on the __unique values__ in the classified list, you can change the symbol for each value.
```

Now we have a map of Nigeria where you can locate the areas that are affected by explosions more than others. On the map below, we also added text labels, which will be explained below.

```{figure} ../../fig/en_exercise_map_design_example_Nigeria.png
---
name: en_exercise_map_design_example_Nigeria
width: 500px
---
Regions affected by explosions in Nigeria.
```

:::{dropdown} Video: Set up different symbols in a single layer

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_styling
.mp4"></video>

:::



:::{card} 
:class-card: sd-text-justify sd-text-black sd-border-0
__Simple Markers, SVG-Symbols and Raster images__
^^^
On top of simple markers, QGIS lets you also use SVG-symbols and raster images as symbols for your vector data.

- __Simple markers__ are simple shapes such as rectangles, circles, or crosses that can be adjusted in the symbolization layer (colour, size, outline, etc.). Most of your styling in QGIS will be done with these markers.
- __SVG-symbols__ are *scalable vector graphic* symbols. As vector files, they can be scaled to any size while keeping the same resolution. In most cases, if you want to use a more complex symbol (e.g. hospital, school, train station), SVG-symbols are the best option as they let you adjust the symbol (colours, outline, size, etc.).
- If you select __raster images__, the resolution of the symbol is limited by the amount of pixels in the image. It is not advisable to use high resolution images as symbols on your map because it may overload your PC.

:::

#### __Using SVG-Symbols and IFRC symbols__

### Using SVG-Symbols

In some cases, you might want to use more complex symbols in your map. For example, you want to use a cross to signify a hospital, a book to signify a library, or a plane to signify an airport. In these cases, you can use SVG-symbols. Keep in mind that, ordinarily, SVG-symbols work only for point data. 
To use SVG-symbols:

1. Open the styling panel and open the `single marker` options.
2. Under `Symbol layer type`, select __"SVG Marker"__.
3. Scroll down to the SVG-Browser. Here you will find all the folders of your installed SVG-libraries.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

There is already a default library of SVG-symbols. If you are looking for a specific symbol, try searching for it in the search bar.

#### Adding an external SVG-library

QGIS also offers the option to add your own SVG-libraries, for example if your organisation uses a specific set of icons. 
If you have a library of SVG-symbols as a folder you can add them to your Styling manager.

1. Open the style manager: `Settings` > `Style Manager`.
2. Click on `Import / Export` and select `Import items`.
3. Navigate to the location where you have saved the library or style and select the file (in most cases .qml but the file type can also be .xml).
4. Now you can select which symbols you wish to import. In most cases, you can select all symbols.
5. Click on `Import`.

The new SVG-symbols are in your SVG library.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

#### Using IFRC-Symbols

:::{admonition} IFRC- and UN-Symbols repositories
:class: tip

The IFRC provides icons and symbols that can be used in your maps. You can find them under [this link](https://go-user-library.ifrc.org/brand-design/iconography). 

There is also a library with humanitarian icons by the [United Nations Office for the Coordination of Humanitarian affairs](https://www.unocha.org) which can be found [here](https://github.com/mapaction/ocha-humanitarian-icons-for-gis?tab=readme-ov-file). The files are available in different formats you can use in QGIS. 

:::

## Self-Assessment Questions

::::{admonition} Test your knowledge
:class: note

1. __Name and describe the four main symbolisation methods used for vector layers.__

:::{dropdown} Answer
1. __Single Symbol__
    - All features use the same symbol (same colour, size, stroke) regardless of their attributes.
2. __Categorised (Unique Values/Categorical)__
    - Features are styled by discrete categories (attribute values). Each unique value (or class) gets its own symbol (hue, shape, etc.).
3. __Graduated Symbols__
    - Numeric (continuous) attributes are divided into classes (value ranges), and each class is given a symbol (often with a colour ramp). This is used to show variation in quantitative data.
4. __Rule-based__
    - Users define one or more rules using the expression builder that determine which features get which symbol. Rules can combine attribute and spatial logic, allowing complex conditional styling.

:::

2. __Where is a layer's symbology saved?__

:::{dropdown} Answer
- The symbology of a layer is not saved in the dataset. If you share only the dataset with a colleague, the layer will not appear as on your computer.
- The symbology is stored in the __QGIS project file__ (`.qgz` or `.qgs`).
- It is also possible to __export__ or __save__ the style externally (as a `.qml` file) so that it can be reused or shared.
:::
3. __When styling polygon layers (e.g. administrative boundaries), what is the purpose of using transparent fill and visible outlines?__

:::{dropdown} Answer
- __Context:__ The transparent fill allows underlying layers (e.g. basemap, imagery, labels) to show through giving spatial context.
- __Boundary emphasis:__ The visible outlines (strokes) clearly indicate the polygon borders, even if the fill is subtle.
- __Hierarchy and legibility:__ If many overlapping polygons or adjacents regions are shown, transparent fills prevent areas from blocking each other, while outlines keep boundaries distinct.
:::


4. __Explain how to create a choropleth map in QGIS using graduated colours. What do you need to choose (e.g. attribute, number of classes, colour ramp)?__

:::{dropdown} Answer
1. <kbd>Right-Click</kbd> on the layer and select `Properties` and navigate to the `Symbology`-tab.
2. Change the symbolisation method from `Single-Symbol` to `Graduated`.
3. Next to `Value`, choose the numeric attribute you want to visualise in the choropleth map (e.g. population density, percentage, precipitation, normalised diseased cases, etc.). The value of this attribute will determine the colouring.
4. Choose a classification method and set the number of classe (e.g. equal interval, quantile, natural breaks, etc.).
5. Pick a colour ramp suitable for the information you want to visualise (light → dark).
6. Click `Classify` and `Apply`.
7. Take a look at the map canvas and make necessary adjustments (e.g. remove the polygon outlines).
:::

5. __What are SVG symbols, and what advantages do they offer over raster images for point symbology?__

:::{dropdown} Answer
- __SVG (Scalable Vector Graphics)__ symbols are vector‑based icons or graphics that can be used for symbolising points in QGIS.
- __Advantages:__
    - __Scalability without loss:__ SVGs scale smoothly (zoom in or out) without pixelation or blurring, whereas raster images degrade when resized.
    - __Editable/styleable:__ You can change colour, stroke, fill, size dynamically because the symbol is vector-based.
    - __Sharpness on print:__ They maintain crisp edges at any resolution, making them better for cartographic output.
:::


::::

## Further Resources

- [Cartography Guide](https://www.axismaps.com/guide) by [Axis Maps](axismaps.com)
- Tutorial on [how to import the SIMS Colour Palette into QGIS](https://learn-sims.org/geospatial/importing-sims-color-palette-to-qgis/) 
- Tutorial on [how to create a shaded relief map in QGIS](https://learn-sims.org/geospatial/creating-a-shaded-relief-map-in-qgis/)
- [Creating a 3W (Who, What, Where) Infographic](https://learn-sims.org/information-design/creating-a-3w-who-what-where-infographic/)
- [Official IFRC color palette](https://learn-sims.org/style-guidance/color-palettes/)