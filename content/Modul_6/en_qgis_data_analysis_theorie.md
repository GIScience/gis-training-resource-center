# Data Analysis with QGIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

__Competences__:

This Module covers a general understanding of data analysis, how to get statistics, create buffers, heatmaps, and how to break rivers, roads, or areas into segments. The following modules will cover more complex analysis methods 


## Data Analysis

Even in a single layer, a lot of analysis is possible. However, sometimes the things we want to analyse are __split across__ multiple layers. In order to get these insights we use the spatial and non spatial GIS-processing tools we learned in the previous modules. In this module, we will look how to apply these tools, collect and work with data to create meaningful insights.

```{figure} ../../fig/multiple_layer_data_analysis.png
---
align: left
name: spatial analysis using multiple layers example
width: 350px
---
A spatial analysis can be a result of combining several layers with different information in a single map
```

### Spatial Analysis

Geographic analysis helps us answer questions like: 
* What __patterns__ are in the data?
* How can we __summarise__ any trends?
* What's __nearby__?
* Which areas are __affected__?
* What's __inside or outside__ a boundary?
* How do phenomenon __change with location__?
* How do locations __change over time__?

Before doing any sort of processing, you need to familiarise yourself with the data and understand it. 

1. The first step is to read the metadata from the source and understand __what data was collected__, __who collected the data__, __and how the data was collected__. 
2. Next, open the attribute table and look at the different features and attributes available. What do the attributes show and what are they called?
3. Now you can start visualising the data:
    * You can visualize the data cartographically by assigning or categorizing the data using symbols
    * You can create charts from the attribute table
    * You can look for patterns, averages, outliers

We are usually looking for ways to __describe__ our data to an audience in some ways. Sometimes spatial analysis will be used to provide recommendations for activities. Considering the amount of data available online, it is always important to take a step back and gain perspective when facing this knowledge, these capacities, as well as the data itself before rushing in to manipulate it:
* Reliability: Can I trust this datagit c?
* Interest: Do I need this data?
* Usage: Am I able to use this data?
* Comprehensiveness: Is this data complete?
* Date: How old is this data?
* Sensitivity: Is this data sensitive?

> Insert Map example?

With spatial analysis, you can build predictive models to plan ahead of disasters. __BUT: Not all analysis is complex! Just knowing how many features are in a layer is useful.__ Simple analysis includes:
* Ranking
* Categorizing
* Above/below threshold
* Affected Areas
* Population distribution

It is important to know the __limitations__ of the data at your disposal - don't try to use unsuitable data for analysis (e.g. if you now a survey sample is not representative)

```{Attention} Spatial Representation and Analysis
There are some spatial analysis problems that are difficult to avoid completely. For example the __Modifiable Areal Unit Problem__ (pictured below), where the results look different depending on the unit of analysis.  
![Modifiable Areal Unit Problem Example](/../fig/en_modifiable_areal_unit_problem_example.png)
```

__There are two main types of data analysis__:
* __Thematic analyses__ focus on visual variation according to a given attribute of the data (one of its characteristics). They are performed on a specific field of the attribute table for the layer, whether textual or numerical. The graphical representation (symbology) changes according to the attribute.
    * For instance: variations in size depending on population numbers in a refugee camp area.
```{figure} ../../fig/en_thematic_analysis.png
---
name: thematic analysis example
width: 500px
---
```

```{figure} ../../fig/thematic_analysis_map_example.png
---
name: thematic analysis example
width: 600px
---
Thematic analysis using different sizes to distinguish the population number in each camp (Source: [WFP](https://reliefweb.int/map/somalia/somalia-physical-constraints-map-21-july-2022))
```

```{figure} ../../fig/thematic_analysis_map_example_2.png
---
name: thematic analysis example 2
width: 600px
---
Thematic analysis using different colours for the roads to discern health accessibility (Source: [UNHCR](https://reliefweb.int/map/bangladesh/rohingya-refugee-responsebangladesh-rohingya-population-location-30-june-2022))
```

* __Spatial analyses__ are performed on spatialized phenomena such as: presence/absence of the phenomenon, its relationship with other phenomena or entities, distribution in space. They are performed on the geometry and position of elements, as well as on their relationship with other elements. Spatial analyses can create new values or elements.
    * For example: crossing two satellite images to extract flooded areas between two dates; or crossing latrine and water catchment areas in a refugee camp; using a digital elevation model to determine which buildings have a high flooding risk.

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

```{Note}Measurement Units
The unit of measurement of the calculated area depends on the distance unit settings of the current project's CRS (metrical or geographic). In most cases you want metres or kilometers. Make sure the units of your CRS are metres to get the correct values. 

You can check this by opening the CRS selector (bottom right corner) and reading the information of your selected CRS. 
```

:::{dropdown} Example: Calculating the length of roads

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2__fieldcalc_calculating_length
.mp4"></video>

:::
## Basic statistics

In the field calculator, we can calculate the length, area, perimeter for each feature of a dataset. However, we might want to have aggregate statistics on a dataset (average length/area, total length/area).   
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

## Buffer analysis

Creating a [buffer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#buffer) is a helpful analysis to determine what lies in proximity of, for example, a contaminated water source or other hazards and determine vulnerability. Buffer analysis is often used to map the riparian zones along rivers to devise environmental protection zones or estimate vulnerability.

- Proximity analysis
- Estimated vulnerability analysis

## Density Map Analysis

Density maps are very useful in communicating the __intensity of a phenomenon in an area__. Point data is aggregated to show the amount of incidents in that area.
__For example__, number of schools or number of disease cases. 

It is important to consider that most demographic or economic data needs to be normalized (e.g. number of inhabitants). To assess the significance of the number of schools, you will need to know how the population of the area; so the amount of schools per 1,000 inhabitants, or the number of disease cases per 100 persons, for example. 

There are a few different types of density maps. The most common are heatmaps and hexagon grid maps. In both cases, the intensity of a phenomenon is calculcated with point data (rarely with lines or polygons). 

>discrete vs. continuous?

### Heatmap

Heat maps use features in a dataset to calculate the relative density of points on a map. The density is displayed as a colour ramp with colors ranging from "cool" (low density) to "hot" (high density). Heatmaps are useful when you have a large number of features covering an area with areas where these features cluster together. 

```{figure} ../../point_map_to_heat_map_example.png
---
name: point map to heat map example
height: 300 px
---
Example of a point map (left) to a heat map (right)
```



>look at slides

### Hexagon grid

Hexagon grids are used to aggregate point incidents in order to normalize geographic data or to mitigate the modifiable area unit problem (problems arising from using irregular shaped polygons). In GIS, we commonly use rectangles (e.g. raster data) or __hexagons__, as these geometries can be repeat in an evenly spaced grid without leaving gaps. 

The advantage of using hexagons is that it is a polygon that closely resembles a __circle__ (where the distance to the centre is equal at every point along the outline), but still __leaves no gaps__ when placed as a __grid__. This means that it is also possible to use absolute values (no normalizations), since the spatial units have the same size. 

> WIKI: __Hexagon grids__ are especially useful for density maps. For example, the number of conflict events or water points in an area. 

To create a hexagon grid map, you will first need to [create a hexagon grid](link), by using the "__Create Grid__" vector tool. 

Next, you will need to join the point data with the hexagon grid. We want to know the amount of points that are inside of a hexagon cell. To count the number of points, we need to use the vector tool "__Count points in polygon__". The result will be a hexagonal grid where each polygon has the a value for the number of points in that area. 

The final step will be to __visualize__ the data by assigning a __graduated symbology__ to the polygons. You can play around with the transparency of your layers to make more information visible. 

```{TIP} 
You can remove the hexagon cells that are not overlapping the reference layer:  
1. Select by location all the cells that intersect with your reference polygon/layer.
2. Invert the selection.
3. Delete the selected hexagon cells.
```

:::{dropdown} Example video: Creating a hex map

:::


## Analysis by joining attributes