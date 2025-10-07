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

1. __Why can’t you style a raster layer by changing “fill” or “outline” in the way you do with vector data?__
2. __What is the default rendering style for a single‑band raster in QGIS, and into what style is it commonly changed for better visualisation?__
3. __What is a “colour ramp” (or gradient) in the context of raster symbology, and how does it help interpret the data?__
4. __Give an example of a raster dataset (e.g. digital elevation model, NDVI, precipitation) and propose a suitable colour ramp or palette you might use in QGIS__
5. __When designing a colour ramp for raster data (e.g. elevation, temperature), what should you watch out for in terms of lightness, hue, or perceptual uniformity?__


::::