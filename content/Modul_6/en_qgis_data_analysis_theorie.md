# Data Analysis with QGIS

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

__Competences__:

In this Module you will learn: 
* General understanding of data/spatial analysis
* Remote sensing/working with raster data
* Accessibility analysis
* Local data collection
* Data access

## Data Analysis

Even in a single layer, a lot of analysis is possible. However, sometimes the things we want to analyse are __split across__ multiple layers. In order to get these insights we use the spatial and non spatial GIS-processing tools we learned in the previous modules. In this module, we will look how to apply these tools, collect and work with data to create meaningful insights.

```{figure} ../../fig/multiple_layer_data_analysis.png
---
name: spatial analysis using multiple layers example
width: 500px
---

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

1. The first step is to read the metadata from the source and understand what data was collected, who collected the data, and how the data was collected 
2. Next, open the attribute table and look at the different features and attributes available. What do the attributes show?
3. Now you can start visualising the data:
    * You can visualize the data cartographically by assigning or categorizing the data using symbols
    * You can create charts from the attribute table
    * You can look for patterns, averages, outliers


We are usually looking for ways to __describe__ our data to an audience in some ways. Sometimes spatial analysis will be used to provide recommendations for activities. Considering the amount of data available online, it is always important to take a step back and gain perspective when facing this knowledge, these capacities, as well as the data itself before rushing in to manipulate it:
* Reliability: Can I trust this data?
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
![Modifiale Areal Unit Problem Example](/../../fig/en_modifiable_areal_unit_problem_example.png)
```

__There are two main types of data analysis__:
* __Thematic analyses__ focus on visual variation according to a given attribute of the data (one of its characteristics). They are performed on a specific field of the attribute table for the layer, whether textual or numerical. The graphical representation (symbology) changes according to the attribute.

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
Thematic analysis using different colours for the roads to discern health accessibility (Source: WFP)
```



    * For instance: variations in size depending on population numbers in a refugee camp area.
* __Spatial analyses__ are performed on spatialized phenomena such as: presence/absence of the phenomenon, its relationship with other phenomena or entities, distribution in space.
    * For example: crossing two satellite images to extract flooded areas between two dates; or crossing latrine and water catchment areas in a refugee camp.
