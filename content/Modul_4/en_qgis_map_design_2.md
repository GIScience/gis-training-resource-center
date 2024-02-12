# Print layout

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

The print layout in QGIS is where you design and finalize the map in order to print or export it as a PDF or format of your choice. Here you can add important elements such as the legend, a title, an explanatory text and everything you need to create a comprehensive map. A QGIS project is not a map until all the layout elements (legend, title, scale bar, sources, etc.) are added. 

1. Go to __Project > New Print Layout > enter a name for the new print layout > click OK__
2. A new window witha blank print playout will appear.


```{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Create a new Print Layout
```

## Understanding the Print Layout Composer


```{figure} ../../fig/en_30.30.2_understanding_the_print_layout_composer.png
---
name: New Print Layout
---
The interface of the Print Layout Composer
```

1. __Layout Settings__ (Add pages, Export Map, manage panels)
2. __Dialer Tools__ (Save, New, Duplicate, Add items from template, Save template)
3.  __Navigation bar__ (Zoom, Refresh, Lock/Unlock elements)
4. __Toolbar__ (Zoom, Select, Move in Map, Add new map/image/text/legend/scale/shape/...)
5. __Feature Panel__: displays the elements added to the print layout
6. __Advanced Options__: customize each element of the layer

First of all, you should always set the size of your map:

- Right-click on the blank map > Page Properties
- Choose __the size of your document__ (A4, A3, A2)
- Choose the orientation (Landscape or Portrait)

_A4 and A3 are the most commonly used sizes for maps_





# Map templates

Map templates can facilitate and reduce the creation of a print layout. Map templates save the arrangement of elements in the print layout. However, they do not save the layers and images of the project. These will need to be reconfigured again.
~~If you work for an organisation that frequently publishes maps, or you need to create several maps on the same topics but in different regions or times, you can use map templates to skip the arrangement of elements.~~ 

```{note}
The individual layers, maps and images are not saved in the template. However, if you have the same layers in the project you load the template into, the legend will update accordingly. 
```


# The Atlas function (automatic map generation)

In some cases, it can be necessary to create multiple maps for different locations with the same layers. For example, if you have a detailed dataset on affected flood areas in Nigeria, you can create a more detailed map for each subnational district. In QGIS, this can be done automatically with the __Atlas Function__. 

The Atlas Function can be found in the __Print Layout Composer__ on the toolbar. 

```{figure} ../../fig/en_atlas_toolbar.png
---
name: Atlas Toolbar
width: 500 px
---
Atlas Toolbar
```

If you can't see the Atlas Tools, you must first activate the Atlas Toolbar under `View` > `Toolbars` > `Atlas Toolbar`


