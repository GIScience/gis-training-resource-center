## Symbology for Raster Data

As we have already learned, raster data are basically a grid of pixels with different (numerical) values. As such, you can't style the shape, fill or outline of raster data. Raster data is visualized by assigning a colour ramp to the pixel value. QGIS offers several options to visualise raster data. For example, you can create a hillshade with digital elevation model (DEM). 

### Assigning a colour gradient to raster data

To assign a colour gradient for raster data, you need to:

1. Open the `styling panel` for the raster layer
2. Navigate to the `Symbology tab`  
3. By default, the colour scheme is set to Singleband Gray (if you only have one colour band in the data set). Click on `Singleband Gray` and switch to `Singleband Pseudocolour`
4. Click on __the arrow to the right of the colour ramp__. Here you can choose a pre-made colour ramp
5. You can modify the colour ramp by __clicking on the colour ramp__.

``` {figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: raster data colour gradient
width: 600px
---
Colour Ramp Selector
```

In the colour ramp selector, you can adjust each colour step. On the bottom, you can see a plot for the Hue, __Saturation__, __Lightness__ and __Opacity__. The last three in particular are useful to understand how your colour ramp will appear. Gradients from light to dark are easier to read: Check if the plot for the __Lightness__ has a more or less linear plot.

### Creating new colour gradients 



#### Styling a digital elevation model

Elevation data sets are frequently used to communicate the terrain on a map. By default, an elevation model will be displayed with a gray colour ramp. However, if you don't need the to know the elevation at certain points, you can choose to display the __hillshade__ of the terrain. Hillshading will simulate the shadow of the terrain as if it would be exposed to a light source. In this example, we will use the elevation raster data (.tiff) of Algeria from the Humanitarian Data Exchange platform (humdata.org) To achieve this,

 1. Open the `symbology` tab
 2. Click on `Render type` and select `Hillshade`. You will have an option to select the direction of the light. Conventionally, the light source is positioned in the North-West, so we can keep the default settings. In some cases with rough terrain, it can be useful to make the hillshade __Multidirectional__.
 3. The hillshade will be very dark and cover most of the map. We need to make it lighter...

<!--ADD: Video-->

### Inverting the colour ramp

In some cases, the colour ramp should be inverted to make it easier to read the map:

1. Click on the __arrow next to the Colour ramp__ to open the dropdown menu.
2. Click on `Invert Colour Ramp`.


