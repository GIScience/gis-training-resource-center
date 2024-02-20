# Data Analysis with QGIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

__Competences__:

This Module covers a general understanding of data analysis, how to get statistics, create buffers, heatmaps, and how to break rivers, roads, or areas into segments. The following modules will cover more complex analysis methods 

## Data Analysis

Even in a single layer, a lot of analysis is possible. However, sometimes the things we want to analyse are __split across__ multiple layers. In order to get these insights we use the spatial and non spatial GIS-processing tools we learned in the previous modules. In this module, we will look how to apply these tools, collect and work with data to create meaningful insights. We will go over a few examples of data analysis that are common in humanitarian work. 

```{figure} ../../fig/multiple_layer_data_analysis.png
---
align: left
name: spatial analysis using multiple layers example
width: 300px
---
Overlaying layers is a spatial analysis
```

### Spatial Analysis

* A spatial analysis can be a result of combining several layers with different information in a single map.

__Geographic analysis helps us answer questions like__: 
* What __patterns__ are in the data?
* How can we __summarise__ any trends?
* What's __nearby__?
* Which areas are __affected__?
* What's __inside or outside__ a boundary?
* How do phenomenon __change with location__?
* How do locations __change over time__?

Before doing any sort of processing, you need to __familiarise yourself with the data__ and understand it. 

1. The first step is to read the metadata from the source and understand __what data was collected__, __who collected the data__, __and how the data was collected__. 
2. Next, open the attribute table and look at the different features and attributes available. What do the attributes show and what are they called?
3. Now you can start visualising the data:
    * You can visualize the data cartographically by assigning or categorizing the data using symbols
    * You can create charts from the attribute table
    * You can look for patterns, averages, outliers

We are usually looking for ways to __describe__ our data to an audience in some ways. Sometimes spatial analysis will be used to provide recommendations for activities. Considering the amount of data available online, it is always important to take a step back and gain perspective when facing this knowledge, these capacities, as well as the data itself before rushing in to manipulate it:
* __Reliability__: Can I trust this data?
* __Interest__: Do I need this data?
* __Usage__: Am I able to use this data?
* __Comprehensiveness__: Is this data complete?
* __Date__: How old is this data?
* __Sensitivity__: Is this data sensitive?

With spatial analysis, you can build predictive models to plan ahead of disasters. __BUT: Not all analysis is complex! Just knowing how many features are in a layer is useful.__ Simple analysis includes:
* Ranking
* Categorizing
* Above/below threshold
* Affected Areas
* Population distribution

It is important to know the __limitations__ of the data at your disposal - don't try to use unsuitable data for analysis (e.g. if you now a survey sample is not representative)

```{Attention} Spatial Representation and Analysis
There are some spatial analysis problems that are difficult to avoid completely. For example the __Modifiable Areal Unit Problem__ (pictured below), where the results look different depending on the unit of analysis.  
>INSERT LINK TO MODIFIABLE AREAL UNIT PROBLEM EXPLANATION
```

__There are two main types of data analysis__:  

```{figure} ../../fig/en_thematic_analysis.png
---
name: thematic analysis example
width: 500px
---
```

* __Thematic analyses__ focus on visual variation according to a given attribute of the data (one of its characteristics). They are performed on a specific field of the attribute table for the layer, whether textual or numerical. The graphical representation (symbology) changes according to the attribute.
    * For instance: variations in size depending on population numbers in a refugee camp area.


```{figure} ../../fig/thematic_analysis_map_example.png
---
name: thematic analysis example
width: 600px
---
Thematic analysis using different colours for the roads to discern health accessibility (Source: [UNHCR](https://reliefweb.int/map/bangladesh/rohingya-refugee-responsebangladesh-rohingya-population-location-30-june-2022))
```

```{figure} ../../fig/thematic_analysis_map_example_2.png
---
name: thematic analysis example 2
width: 600px
---
Thematic analysis using different sizes to distinguish the population number in each camp (Source: [WFP](https://reliefweb.int/map/somalia/somalia-physical-constraints-map-21-july-2022))
```

* __Spatial analyses__ are performed on spatialized phenomena such as: presence/absence of the phenomenon, its relationship with other phenomena or entities, distribution in space. They are performed on the geometry and position of elements, as well as on their relationship with other elements. Spatial analyses can create new values or elements.
    * For example: crossing two satellite images to extract flooded areas between two dates; or crossing latrine and water catchment areas in a refugee camp; using a digital elevation model to determine which buildings have a high flooding risk.


```{figure} ../../fig/en_flood_risk_map_example.png
---
name: flood risk map example
width: 600 px
---
Example of a flood risk map. Source: Frank, Enrico & Ramsbottom, David & Avanzi, Agostino. (2016). Flood risk assessment and prioritisation of measures: Two key tools in the development of a national programme of flood risk management measures in Moldova. International Journal of Safety and Security Engineering. 6. 475-484. 10.2495/SAFE-V6-N3-475-484. 
```

## Length, Surface, Circumference

Knowing how big an area is, or how long road sections is already an importand analysis. For example, you can know how much of a road network is inaccessible, or how much area is affected by flooding.

These geometrical attributes can be calculated using the [__field calculator__](https://giscience.github.io/gis-training-resource-center/content/Modul_5/en_qgis_non_spatial_tools.html?highlight=field+calculator#calculate-field) or the processing tool __"Add geometry attributes"__. 

The field calculators has the following functions to calculate geometry attributes as new fields in the attribute table:

| *Function* | *Description* | 
| -------- | ---|
| `$area` | Returns the area of the current feature. The area calculated by this function respects both the current project's ellipsoid setting and area unit settings.| 
| `$length` | Returns the length of a linestring. If you need the length of a border of a polygon, use $perimeter instead. The length calculated by this function respects both the current project's ellipsoid setting and distance unit settings.| 
| `$perimeter` | Returns the perimeter length of the current feature. The perimeter calculated by this function respects both the current project's ellipsoid setting and distance unit settings.| 

For example, to calculate the area of polygons: 

1. Open the attribute table
2. Open the field calculator
3. Check the box `Create a new field`
4. Enter a `Output field name`: "Area"
5. Select the `Output field type`: In this case we want a number with decimals. So we select either "decimal number".
6. Enter `$Area` into the expression window.
7. Select `OK`.

In the attribute table, you will find a new column called `Area` with the respective area for each feature. 

```{Note}
The __unit of measurement__ of the calculated area depends on the __distance unit settings__ of the current __project's CRS__ (metrical or geographic). In most cases you want metres or kilometers. Make sure the units of your CRS are metres to get the correct values. 

You can check this by opening the CRS selector (bottom right corner) and reading the information of your selected CRS. 
```

:::{dropdown} Example: Calculating the length of roads

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2__fieldcalc_calculating_length
.mp4"></video>

:::
## Basic statistics

In the field calculator, we can calculate the length, area, perimeter for each feature of a dataset. However, we might want to have __aggregate statistics__ on a dataset (average length/area, total length/area).   
QGIS comes with two basic processing tools to generate statistics:

| *Processing tool* | *Description* |
|---------- | ---|
|"__Basic statistics for fields__" | This algorithm generates basic statistics (count, sum, mean, median, standard deviation, quartiles, ...) from the analysis of a values in a field in the attribute table of a vector layer. Numeric, date, time and string fields are supported. The statistics returned will depend on the field type. Statistics are generated as an HTML file.|
| "__Statistics by categories__" | This algorithm calculates statistics of fields depending on a parent class. In the option `Field to calculate statistics on`, you must select the column that you wish to create statistics for (for example, area/length). In the option `Field(s) with categories` you select the values that will be used as categories in the statistics (for example, flooding=Y/N, type of road, type of building/amenity). | 


:::{dropdown} Example: Statistics by categories
In this example we have a road network which has been intersected with a flood extent. A new field ("Flood") has been calculated containing information wether the road is flooded or not (Y=flooded, N=not flooded). The length of each road has been calculated using the `$length` function in the field calculator as new column called "Length".  
We want to calculate the total length of flooded and unflooded road respectively. 

1. Open the "Statistics by category"-tool
2. Select the road network layer.
3. Under `Field to calculate statistics on`, select `Length`
4. Under `Field(s) with categories`, select `Flood`
5. Specify a location to save the statistics file.
6. Click `Run`
8. After completion, a new layer will appear in your layer tab. This will not contain spatial attributes and is a simple attribute table with the statistics. In our case, we will have the basic statistics (min, max, range, sum, median, sd, etc.) for all the road features with the flooding value "Y", and "N". 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_statistics_by_categories_example
.mp4"></video>
:::

> Insert statistics examples

## Buffer analysis

Creating a [buffer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#buffer) is a helpful analysis to determine __what lies in proximity__ of, for example, a contaminated water source or other hazards and determine vulnerability. Buffer analysis is often used to map the riparian zones along rivers to devise environmental protection zones or estimate vulnerability.

- Proximity analysis
- Estimated vulnerability analysis

## Density Map Analysis

Density maps are very useful in communicating the __intensity of a phenomenon in an area__. Point data is __spatially aggregated__ to show the amount of incidents in that area.
__For example__, number of schools or number of disease cases. 

It is important to consider that most demographic or economic data needs to be __normalized__ (e.g. number of inhabitants). To assess the significance of the number of schools, you will need to know how the population of the area; so the amount of schools per 1,000 inhabitants, or the number of disease cases per 100 persons, for example. 

There are a few different types of density maps. The most common are heatmaps and hexagon grid maps. In both cases, the intensity of a phenomenon is calculcated with point data (rarely with lines or polygons). 

>discrete vs. continuous?

### Heatmaps

Heat maps use features in a dataset to calculate the __relative density of points__ on a map. The density is displayed as a colour ramp with colors ranging from "cool" (low density) to "hot" (high density). Heatmaps are useful when you have a large number of features covering an area with areas __where these features cluster together__ and help us visualize __spatial patterns__ of a layer. 

```{figure} ../../fig/point_map_to_heat_map_example.png
---
name: point map to heat map example
height: 300px
---
Example of a point map (left) to a heat map (right)
```

To create a heatmap you first need a layer containing data points or 'samples'. These points are distributed in an area with some areas containing more than others. The __density__ of the points in space determines the intensity of the color on the heat map. 

In QGIS, there are two methods to create heatsmaps. The first method uses the symbology tab and is generally a lot faster. The second method uses the interpolation tool __"Heatmap (Kernel Density Estimation)"__ and offers more parameters to adjust. The advantage of the processing tool is that you can set a radius using metric units (for example the number of points in a __100 Meters__ radius compared to using the millimeters or pixels of your computer screen) and set a variable radius that is determined by another attribute. The next section will discuss the creation of heatmaps using the symbology tab. A guide on how to create a heatmap using the processing tool can be found [here](link)

> insert link

#### Using the symbology tab to create a heatmap

You can create a heatmap in the __symbology tab__ of a point or polyline layer. Navigate to the symbology tab and select the `Heatmap` symbolization method. Here, you can adjust the __color ramp, radius, and maximum value__. The __radius__ (in Millimeters on your screen) determines the size of the circle that is used to aggregate the points. If it gets bigger more points can be aggregated and the 'heat' increases. The __maximum value__ determines the value that is given the 'hottest' color. By default, it is set to the highest number of aggregated points. For example, you can __set a threshold__ above which everything has the "hottest" color. Reducing it changes the visualization drastically.

```{figure} ../../fig/en_heatmap_radius_max_value_conf_example.png
---
name: heatmap example with different radii and max value
width: 700 px
---
Examples of heatmaps with different configurations for the radius and the maximum value. 
```

As you can see, the information communicated through the different maps changes drastically. This is why you need to be transparent on what parameters you have set to create the heatmap.

:::{dropdown} Assigning a weight to the samples

Assigning weight to samplepoints can be useful when your dataset has additional information (such as the type of incident, or sampled amount of rainfall) and you want to integrate this information into your heatmap. 

:::


### Hex Maps (Hexagon Grids)

Hexagon grids are used to aggregate point incidents in order to normalize geographic data or to mitigate the modifiable area unit problem (problems arising from using irregular shaped polygons). In GIS, we commonly use rectangles (e.g. raster data) or __hexagons__, as these geometries can be repeat in an evenly spaced grid without leaving gaps. 

The advantage of using hexagons is that it is a polygon that closely resembles a __circle__ (where the distance to the centre is equal at every point along the outline), but still __leaves no gaps__ when placed as a __grid__. This means that it is also possible to use absolute values (no normalizations), since the spatial units have the same size. 

> WIKI: __Hexagon grids__ are especially useful for density maps. For example, the number of conflict events or water points in an area. 

To create a hexagon grid map, you will first need to [create a hexagon grid](link), by using the "__Create Grid__" vector tool. 

Next, you will need to join the point data with the hexagon grid. We want to know the amount of points that are inside of a hexagon cell. To count the number of points, we need to use the vector tool "__Count points in polygon__". The result will be a hexagonal grid where each polygon has the a value for the number of points in that area. 

The final step will be to __visualize__ the data by assigning a __graduated symbology__ to the polygons. You can play around with the transparency of your layers to make more information visible. 

```{figure} ../../fig/point_to_hex_map_example.png
---
name: point map to hex map example
width: 700 px
---
Point map (left) to hex map (right)
```

```{TIP} 
You can remove the hexagon cells that are not overlapping with the reference layer:  
1. Select by location all the cells that intersect with your reference polygon/layer.
2. Invert the selection.
3. Delete the selected hexagon cells.
4. Save the changes you made to the layer. 
```

:::{dropdown} Example video: Creating a hex map

1. Create a Hexagon grid with the tool "__Create Grid__". 
2. Select `Hexagon (Polygon)` as __Grid type__. 
3. The Grid extent should be set to the layer/area of interest. 
4. Select the horizontal and vertical spacing according to the scale of your map. 
5. Optional: Remove the unnecessary Polygons.
6. Use the tool "__Count points in Polygon__" to add an attribute field with the number of points that are *inside* each hexagon cell. The __Polygons__ field should be your reference layer. The new layer will have an attribute field called "__NUMPOINTS__"
7. Assign a __graduated__ symbology to the `Count`-layer. Select "__NUMPOINTS__" as the value and categorize the classes as you wish.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_creating_a_hex_map
.mp4"></video>
:::


## Analysis by joining attributes