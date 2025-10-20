::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Symbology for Raster Data

As we have already learned, raster data are basically a grid of pixels with different (numerical) values. As such, you can't style the shape, fill or outline of raster data. Raster data is visualized by assigning a colour ramp to the pixel value. QGIS offers several options to visualise raster data. For example, you can create a hillshade with digital elevation model (DEM). This small chapter only covers the basics of visualising raster data. If you want to learn more about raster data and how to work with raster layers, take a look at [module 8](/content/Module_8/en_module_8_overview.md). 

## Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the `styling panel` for the raster layer
2. Navigate to the `Symbology tab`  
3. By default, the colour scheme is set to Singleband Gray (if you only have one colour band in the data set). Click on `Singleband Gray` and switch to `Singleband Pseudocolour`
4. Click on __the arrow to the right of the colour ramp__. Here you can choose a pre-made colour ramp
5. You can modify the colour ramp by __clicking on the colour ramp__.

``` {figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: en_30.30.2_raster_data_colour_gradient
width: 600px
---
Colour Ramp Selector in QGIS 3.36.
```

In the colour ramp selector, you can adjust each colour step. On the bottom, you can see a plot for the Hue, __Saturation__, __Lightness__ and __Opacity__. The last three in particular are useful to understand how your colour ramp will appear. Gradients from light to dark are easier to read: Check if the plot for the __Lightness__ has a more or less linear plot.

## Inverting the colour ramp

In some cases, the colour ramp should be inverted to make it easier to read the map:

1. Click on the __arrow next to the Colour ramp__ to open the dropdown menu.
2. Click on `Invert Colour Ramp`.

## Using better colour palettes

```{note}

The default colour ramps available in QGIS are limited and do not fit a lot of cartography purposes. However, QGIS includes the `cpt-city` colour palette catalogue with many carefully crafted colour ramps and palettes. Amongst other, you can find colour ramps specifically created for terrain or elevation models. 

```

```{figure} /fig/en_3.36_cpt-city_cat_1.png
---
name: en_3.36_cpt-city_cat_1
width: 350 px
---
Accessing the colour catalogue.
```

To access the `cpt-city` catalogue, 

1. Open the raster layers symbology tab and select `Singleband Pseudocolor` as the symbolisation method.
2. Navigate to the dropdown arrow next to the colour ramp, a dropdown menu with different colour ramps will open.
3. Click on `Create New Color Ramp`. A small dialogue box will open.
    ```{figure} /fig/en_3.36_cpt-city_cat_2.png
    ---
    name: en_3.36_cpt-city_cat_2
    width: 200 px
    ---
    Selecting the colour ramp catalogue
   ```
4. A new window will open. Here you can find a multitude of colour palettes. For example, for a digital elevation model you can select a colour ramp for topography or specifically digital elevation models. 

```{figure} /fig/en_3.36_cpt-city_cat_3.png
---
name: en_3.36_cpt-city_cat_3
width: 600 px
---
The cpt-city colour ramp catalogue in QGIS 3.36
```

<!--Add small exercise to add a DEM and style it (maybe adjust on or two colour so it looks better?)-->

```{tip}
The cpt-city colour catalogue also offers colour ramps for other applications such as precipitation, NDVI, or surface temperature.
```

<!---
#### Styling a terrain model

Elevation data sets are frequently used to communicate the terrain on a map. By default, an elevation model will be displayed with a gray colour ramp. However, if you don't need the to know the elevation at certain points, you can choose to display the __hillshade__ of the terrain. Hillshading will simulate the shadow of the terrain as if it would be exposed to a light source. In this example, we will use the elevation raster data (`.geotiff`) of [Ecuador from the MERIT DEM](https://developers.google.com/earth-engine/datasets/catalog/MERIT_DEM_v1_0_3#description). 

To achieve this,

1. Add the OSM Standard as a [basemap](/content/Module_2/en_qgis_basemap.md)
2. Open the Symbology-tab of the .
3. Click on `Render type` and select `Hillshade`. You will have an option to select the direction of the light. Conventionally, the light source is positioned in the North-West, so we can keep the default settings. In some cases with rough terrain, it can be useful to make the hillshade __Multidirectional__.
3. The hillshade will be very dark and cover most of the map. We need to make it lighter. Set the `Blending mode` to "Overlay". 

-->

## Self-Assessment Questions

::::{admonition} Test your knowledge
:class: note

1. __Why can’t you style a raster layer by changing “fill” or “outline” in the way you do with vector data?__

:::{dropdown} Answer
- Raster data are made of __pixels (cells)__, each with a value (e.g. elevation, reflectance), not discrete geometries. So there is no “outline” to stroke, nor a single “fill” for the whole polygon.
- Styling rasters is about mapping pixel values to colours, rather than applying boundary or fill styling to features.
- Vector styling operates on geometric features (points, lines, polygons) and you can control fills, strokes, shapes etc.; but raster styling works by symbology/rendering algorithms (colour ramping, stretching, classification) on the continuous grid of values.
:::

2. __What is the default rendering style for a single‑band raster in QGIS, and into what style is it commonly changed for better visualisation?__

:::{dropdown} Answer
- The default rendering for a single‑band raster is __Singleband gray (grayscale)__ — low values are darker, high values are lighter.
- For better visualization, it's common to change it to __Singleband pseudocolor__ (i.e. assign a color ramp) so that variations in values are more visually distinct.
:::

3. __What is a “colour ramp” (or gradient) in the context of raster symbology, and how does it help interpret the data?__

:::{dropdown} Answer
- A colour ramp (or gradient) is a continuous range of colours that are mapped to the range of raster values (from minimum to maximaum). 
- By mapping increasing (or decreasing) values to a progression of colours, the reader can visually interpret the magnitude, gradients, and spatial patterns of the underlying numeric data.
- The use of colour (rather than just grey) can help emphasise meaningful thresholds, critical values (e.g., very high or low), and improve readability and visual appeal.
- A well‐designed colour ramp can highlight differences (e.g., higher vs lower values), reveal spatial structure (e.g., peaks, valleys, clusters), and make the raster meaningful rather than just a grey blob.


:::

4. __Give an example of a raster dataset (e.g. digital elevation model, NDVI, precipitation) and propose a suitable colour ramp or palette you might use in QGIS__

:::{dropdown} Answer
__Example:__ A digital elevation model (DEM) representing terrain elevation (in metres)
__Proposed suitable colour ramp/palette:
- Lower elevations: dark green (lowland)
- Mid elevations: light green → yellow (gentle slopes)
- Higher elevations: orange → brown (steep slopes/upper terrain)
- Highest elevations/peaks: white (snow/ice caps)

In QGIS you might choose a ramp like “Terrain (elevation)” or a custom ramp from the cpt‑city catalogue (the module mentions that QGIS includes the cpt‑city colour palette catalogue with many carefully crafted colour ramps, including ones for elevation models).

:::

5. __When designing a colour ramp for raster data (e.g. elevation, temperature), what should you watch out for in terms of lightness, hue, or perceptual uniformity?__

:::{dropdown} Answer 

- __Lightness/darkness progression:__ A progression from lighter to darker colours are easier to read. QGIS has a lightness plot in the colour ramp editor. If lightness jumps up and down irregularly, some segments may appear visually more prominent than others. Additionally, colours ramps with irregular lightness do not translate to black and white prints. In general, irregular colour ramps are less intuitive to read. 
- __Hue shifts:__ Sudden changes in hue may draw undue attention and may imply categorical rather than continuous differences. If hues change dramatically while lightness remains constant, it may mislead the reader into thinking there are discrete classes.
- __Avoiding misleading associations:__ Colours carry cultural or intuitive meanings (e.g. red = hot/danger, blue = cold, green = vegetation). If you ramp uses unusual colour, the meaning may confuse.
- __Contrast and readability:__ Very dark segments may hide detail; very light segments may fade out. Also consider how the ramp will appear when printed, in greyscale, or by colour‐impaired readers.
- __Interpretation of extremes and middle ranges:__ If the ramp has extreme jumps at the ends or very flat mid‐range, you might lose nuance in important segments. Also avoid ramps that place extremes at colours that are visually “loud” and overshadow moderate values.

::::