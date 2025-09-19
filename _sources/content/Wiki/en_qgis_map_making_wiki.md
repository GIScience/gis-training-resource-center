# The Print Layout Composer

## Adding elements to the print layout

### Adding a new map

- Add a new map by clicking on the __Add map__ button on the __toolbar on the left__ and __drag a rectangle on the map canvas.  
- To move the map on the canvas, simply __select the map__ and __drag__ it with your mouse
- To move within a map select __Move item content__ button on the 
- To zoom in on the map, while using the __Move item content__ button, you can __Press CTRL + scroll the mouse wheel__ (gently) or enter the scale manually in the item properties

```{figure} ../../fig/en_30.30.2_adding_a_map.png
---
width: 750px
name: Add a new map
---
Adding a new map to the Print Layout
```

:::: {tab-set}
::: {tab-item} Adding a new map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_new_map
.mp4"></video>
:::

::: {tab-item} Moving and scaling the map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_moving_the_map
.mp4"></video>
:::
::::

### Adding a title or a text box

A title should describe the phenomenen represented on the map.

- To add text (title, explanations), use the __Add Label__ tool and draw a rectangle of the desired size.
- In the __Item Properties__ panel (on the right of your screen) you can __enter your text__ and __change the font, style, colour, etc.__ (_Remember to use the scroll bar in the window to see all the options). 

```{figure} ../../fig/en_30.30.2_print_layout_add_text.png
---
width: 750px
name: Add text to the print layout
---
Adding text to the print Layout
```
:::{dropdown} Video: Adding a textbox
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_a_title
.mp4"></video>
:::

### Adding an image or logo

If you are working for an organisation, most likely you will add the logo of that organization on the maps you produce. 

1. Click on `Add image` in the left toolbar.
2. Drag a rectangle on the canvas.
3. In the `Item properties` tab, you will have the option to choose an SVG image from your SVG-library in QGIS or choose a __Raster image__. Most image files are Raster images. 
4. Select `Raster image` and click on the `...` to choose the location of the image.
5. Your image will appear in the print layout. In order to make sure that the image does not get distorted, leave the `Resize Mode` on "Zoom".

:::{dropdown}
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_raster_image.mp4"></video>
:::

### Adding a legend

Before adding a legend, make sure that:

- All your layers have an explicit name ("rivers", "primary roads",...)
- You use the final version of your map (no more layers to add, move, rename or modify). You can still modify them later but you will have to redo the legend.

To add a legend, you can use the __add legend__ button on the __left toolbar__.


```{figure} ../../fig/en_30.30.2_print_layout_add_legend.png
---
width: 750px
name: Add a legend to the print layout
---
Adding a legend to the print layout
```

In the __item properties__ panel, if you keep the __'Auto update'__ option checked, new layers added to your project will automatically be added to the legend but you cannot control them individually (rename if necessary, reorder ot remove items).  
Once the option is unchecked, you can update the name of the layers, group them, remove or reorganise them, etc. 

If you have to many items on your legend, and they don't fit on your map horizontally, you can also split the legend into several columns by navigating through the `Item Properties`-panel, expand the `Columns`-section and increase the __Count__.

:::: {tab-set}
::: {tab-item} Adding a legend

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_legend
.mp4"></video>

:::

:::{tab-item} Editing the legend

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_editing_the_legend
.mp4"></video>

:::

:::{tab-item} 2-Column legend

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_multiple_columns_legend
.mp4"></video>

:::

::::

### Adding a scale bar

Before adding a scale bar, select your main map and check in the __Item Properties__ panel that the __Scale__ fielld has a __round number__.

```{figure} ../../fig/en_30.30.2_print_layout_scale.png
---
width: 750px
name: en_30.30.2_print_layout_scale_2
---
Make sure that the scale is at a round number.
```

To add a scale bar, you can use the __add scale bar__ button on the __left toolbar__. In the __Item Properties__ panel, customize the following functions

- Which Map __is related to the scale__
- __Unit system of the bar__ (metres, miles, degrees)
- __Segments on the left__: segments shown before 0 m (always set to 0). 
- __Fixed width__: define the width of each segment (e.g. 1 km, 10 km, 50 km, ...). 
- __Height__: height (thickness) of the scale bar

_There are many other options to customize the scale bar (change the font, colours, etc.)._ 

```{figure} ../../fig/en_30.30.2_print_layout_add_scale_bar.png
---
width: 750px
name: en_30.30.2_print_layout_add_scale_bar_2
---
Adding and customising the scale bar.
```
:::{dropdown}
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_scalebar
.mp4"></video>
:::

### Adding an overview map

Adding an overview map in the corner of your map will help locate the area you are viewing on the main map.

To create an overview map, you need to follow these steps:

1. Prepare a __layer with national or subnational borders or important landmarks__ in your project (e.g: Administrative boundaries, Capitals)
2. __Insert the overview map__ into your print layout (in the bottom right corner for example)
3. __Lock the new map__ in the Item properties panel
4. Add a rectangle to display the extent of your main map

    1. Go to the __properties__ of your Main map > scroll down until you see __"Overviews"__ 
    2. Add an Overview by clicking on the __"+" icon__
    3. __Link the main map__ by selecting it in the __"Map frame"__ option


```{figure} ../../fig/en_30.30.2_print_layout_overview_map_preparations.png
---
width: 500px
name: en_30.30.2_print_layout_overview_map_preparations_2
---
An overview map should show important landmarks and borders.
```


```{figure} ../../fig/en_30.30.2_print_layout_add_overview_map.png
---
width: 750px
name: en_30.30.2_print_layout_add_overview_map_2
---
Adding an overview map and __locking the layers__
```


```{figure} ../../fig/en_30.30.2_print_layout_add_map_extent_overview_map.png
---
width: 750px
name: en_30.30.2_print_layout_add_map_extent_overview_map_2
---
Add the extent of the main map to your overview map (the red rectangle on the overview)
```

:::{dropdown} Video: Setting up an overview map
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_overview_maps
.mp4"></video>
:::

``` {Caution}
This method requires you to be sure that you are not going to modify the oveview map, as once the layers are locked, they will keep the style, and any updates will not affect the overview map.
```


## Exporting the print layout

Once you are finished with the map composition, it is time to export export the print layout as a PDF or SVG file. 

1. On the Toolbar click on the `Export as PDF`-button.
2. Give the new file a name and select the location you want to save it.
3. Click on `Save`.
4. A new window "PDF Export Options" will open. Here you can adjust the compression algorithm. For the best results, select the lossless image compression. 
5. Click `Save` again.
6. A new green bar will pop up underneath the toolbars. Click on the file link to __review the exported map__.

```{note}
Make sure to check the map after exporting the PDF as some design elements might have changed in the exporting process.
```


## Map templates

::::{tab-set}
:::{tab-item} Saving a template

1. Once you are satisfied with your map layout, click on the ![](../../fig/en_30.30.2_save_as_template.png)-symbol to save it as a new template.
2. Choose a location where you want to save the template. Ideally, you should choose the template directory (see tip).
3. Click `Save`. 
4. You can open the template by dragging it into a QGIS-project.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_saving_layout_template
.mp4"></video>

:::

:::{tab-item} Opening a template

You can drag and drop template-files (`.qpt`, QGIS template file) into QGIS or use the __Layout manager__.

1. Open the Layout manager under `Layout` > `Layout Manager`
2. Navigate to the section "__New from Template__"
3. Choose `Specific` and select the location where you saved your template
4. Click open.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_template
.mp4"></video>

:::

:::{tab-item} Template directory

The template directory is where QGIS is looking for layout templates. If you have templates saved here, you can load templates directly through the layout manager without selecting the file.   
On windows, the file path is `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.
On mac, 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_template_directory
.mp4"></video>

:::

::::

```{tip}
The layout manager in QGIS already has a dedicated location for map templates. On windows, the file path is `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.
On mac, 
If you save templates here, you can load templates directly through the layout manager without looking for the file.
You can also add file paths in the QGIS-template setting
```

## Generating an Atlas

An Atlas will generate a new page with the same map layout for each feature in a layer. For most purposes, it useful to first create a map layout with the elements such as legend, sources and overview map and then insert the map item that will be controlled by the Atlas. To generate an Atlas:

1. Click on the Atlas Settings icon in the Atlas Toolbar
2. In the new window, activate the __Generate an Atlas__ option
3. Select the __Coverage Layer__. This will determine the features or polygons that will be displayed on a page. In our example, we will use the subnational administrative districts in Nigeria (`Adm1`). 
4. Select the __Page Name__. This should be the name of the subnational district or location that is displayed on that page. To display the name of the district, we will choose `ADM1_REF`.
5. Now let's add a map to the empty print layout.
6. Click on the map and navigate to the __Layer Properties__ window on the right.
7. Scroll down until you see the option `Controlled by Atlas` and activate it.
8. Now activate the preview of the Atlas in the __Atlas Toolbar__. Otherwise, the print layout will not update to show you the atlas page. You can click through each page to see how it looks. Depending on the amount of features on your map, they may take a while to render.
9. Now you can adjust the __Margin options__ to best fit the readibility of the map. By default, it is set to 10% and this should fit most purposes.
10. Before printing or exporting the atlas make sure to check every page that other elements of the map do not cover the represented region.

```{Note} 
For now the only item in the print layout that is being controlled by the Atlas is the Map we added. The other elements of the Map are the same on every page.
```

:::{dropdown} Video: Setting up an Atlas
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_an_atlas
.mp4"></video>
:::


### Setting up Overview maps with an atlas

Setting up Overview maps with an atlas works in the same way as setting it up for a normal map. As long as you select the Map controlled by the atlas as the `map frame`, it will update automatically.


