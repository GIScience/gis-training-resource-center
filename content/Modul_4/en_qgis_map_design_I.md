# Map design- Basic
**Competences:**
* Map design


# Representation

The representation of geodata in maps is crucial in order to provide useful location-based insights. This subchapter will cover the basics of good map design, how to create a map design in QGIS as well as common mistakes when designing or interpreting maps.

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


### Visual variables

Visual variables are the __graphical means for visually transcribing information__. The visual variables are __shape, size, hue, value, texture, and orientation__. You can vary these variables to appropriately represent the data at your disposal.  
It allows for the expression of __relationship of difference, order, association, or quantity__ between each element. 

```{figure} ../../fig/en_visual_variables.png
---
width: 500px
name: Visual variables
---
Visual variables according to Bertin (1967)
```

```{Caution} 
Visual perception varies from one person to the next according to various capabilities:
- Physiological (e.g.: colour blindness)
- Transcultural (green = nature, blue = water)
```

> Check Uni HD cartography slides

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

~~In the styling panel, you can change the symbology (1) and the labels (2).~~

## Colors


## Symbology

- Symbology is used to change the look of features on a map
- It makes maps more visually appealing and easier to read
- Colors and styles represent a specific information
- Symbology is applied to layers, but within the same layer we can assign multiple styles to features
- the symbology of a layer can be __changed based on one of its attributes__

### Symbology for Vector data

As we have already learned, vector data can be either points, lines, or polygons. There are multiple ways these 


---
> Move these exercises into the excercise.md? 



### Symbology for raster data



### Labels

- Labels are text that show a specific attribute of features. 
- It is useful to add labels to features to easily identify them. For example, the name of a settlement.
- You can change the font, colour and size of labels
- When you create a map you always add labels to help the final user reading the map

#### Adding labels to a layer
>This is exercise 2 in the PPP

1. In the styling panel, click on the "Labels" tab.
2. Select *Single Labels*. 
3. "Value" is where you choose the attribute that will be displayed as a label. For example "NAME". This will display the "NAME" attribute for each feature. In the example (figure X), *ADM1_EN* will display the English names of Nigerian states.
>change figure number
4. Let's change the font: make it Arial, bold, dark grey, 8 pt
5. Let's add a white buffer around the label.
7. Click Apply and Ok.

```{figure} ../../fig/en_30.30.2_setting_up_labels
---
width: 750px
name: Setting up labels
---
Setting up labels in QGIS 30.30.2
```

#### Adding 2 different label styles to the same layer
>This is exercise 3 in PPP

Sometimes you will need to create two different label styles for different features of a single layer. In this example, we will create one label style for the *Country Capital*, and another one for the *State Capitals*

1. Open the styling panel and click on the Labels tab
2. Select __Rule-based Labeling__
3. Click on the __Add Rule__ button at the bottom (the "+"-sign) and create the first rule
4. For __Value__, select __"NAME"__ (so that the labels will show the name of each city), then click on the "ε"-button next to the "Filter" bar.

```{figure} ../../fig/en.30.30.2_adding_rule-based_labels
---
width: 500px
name: adding rule-based labels
---
To add rule-based labels, you need to enter an expression
```

5. In the central column, expand ==__Fields and Values__== to display a list of all the fields in your layer and double-click on _Class__ to add it to the expression frame on the left.
6. In the right column, click on __All unique__ to list all unique values contained in the Class field
7. Click on the "`=`" operator, then doube-click on the _value 1_ (which represent the Country capital in this case). Click OK.
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

