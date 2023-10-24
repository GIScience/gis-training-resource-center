# Map design Exercise 1


### Exercise: Change the symbology of a layer
>This is exercise 7 in the PPP. Participants will need the specific data.

In this exercise, we will apply the same style to all features in the layer. We have the polygons for 3 administrative levels

1. Add the "Adm0", "Adm1" and "Adm2" shapefiles to your Session 2 project.
2. Order the layers so they are all visible: Put the Adm2 at the bottom, then the Adm1 then Adm0. At first, this might look weird because Adm0 will cover everything.
3. Change the symbology of the Adm0 layer by opening the stlying panel and navigating to the Symbology tab. By default, the symbology type will be __Single Symbol__. This means that the same colours and contours will be applied to all the features in that layer.

```{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: change layer style 1
height: 400px 
align: left
---
Order the layers and navigate to the styling panel of the topmost layer
```
```{figure} ../../fig/en_30.30.2_changing_layer_style_2.png
---
name: change layer style 2
width: 300 px
align: right
---
Change the "Simple Fill"
```

4. Click on "__Simple Fill__" to open the style options.
5. Expand the "__Fill Color__" menu and check the __Transparent Fill__ option. This will make only the boundaries visible, so __we will be able to see the layer under this one__.
6. Choose a __Stroke color__, and make the __Stroke width__ 0.66 Millimeters.
7. Click OK

```{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
name: change layer style 3
---
The styling of a vector data consists of the colour and the outline
```

8. __Repeat the same process__ for the Adm1 layer, using the same colour as for Adm0 (it will be in "Recent colors) and leave the stroke width at 0.26.
9. Now we can see the boundaries of the country and its states, and behind that we cann see the districs (Adm2).
10. Let's make the districs layer's style consistent with the others.
11. Choose a __Fill Color__
12. Use the same __Stroke color__ as for Adm0 and Adm1, but make the width 0.1 Millimeters and the Stroke Style a __Dash Line__
13. Click OK and look at yout map: hopefully it's starting to look nicer!

```{note} 
Remember that __the layer's symbology is saved within your project file, not within your shapefile!__ If you share a shapefile with a colleague, it will have a different style when they add it to their own project.
```

### Exercise: Use different styles in a single layer

We can use symbology to __show the difference between features__ in the same layer. For example, it could be different types of buildings, quantities of Covid cases by district, or types of roads. We can choose a specific attribute of a dataset to assign different colors, outlines, or sizes to features:

1. From your shapefile folder, __drag te ACLED security incidents shapefile onto your map__
2. Open the layer __Symbology__ and choose __Categorized__ instead of Single Symbol.   
> Categorized symbology is used when you have ***discrete*** variables.
```{figure} ../../figure/en_30.30.2_categorized_layer_symbology_1.png
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

``` {figure} ../../fig/en_30.30.2_categorized_layer_symbology_2
---
name: categorized layer symbology 2
width: 500 px
---
By double clicking on the __unique values__ in the classified list, you can change the symbol for each value
```

Now we have a map of Nigeria where you can locate the areas, that are affected by explosions more than others. On the map below, we also added text labels, which will be explained below.

``` {figure} ../../fig/en_exercise_map_design_example_Nigeria.png
---
name: map design example regions affected by explosions in Nigeria
width: 500px
---
Regions affected by explosions in Nigeria
```

### Exercise: Style data based on variable ranges

If a layer contains numeric values that are continuous, they can be organized in intervals. These intervals can be displayed in graduated colours. In this exercise, we assign colours to Adm1 polygons based on the total population of each State.

> Don't forget to check that they have access to the data

1. From __Sharepoint__, download the NGA_Adm1_Pop shapefile and save it in your shapefile folder
2. In QGIS, turn off the Adm1 and Adm2 layer, leaving only Adm0
3. Drag the shapefile you just downloaded into your map
4. Open its Symbology options and choose "__Graduated__"
5. Select the value you want to use to assign colours, in this case, it will be "__population__"

``` {figure} ../../fig/en_30.30.2_symbology_variable_ranges_1.png
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

The following map shows the most populated States of Nigeria using a graduated colour categorization.

```{figure} ../../fig/en_map_design_example_variable_ranges
---
name: map design example_state population Nigeria
width: 500px
---
An unfinished map showing the population of Nigerian states
```