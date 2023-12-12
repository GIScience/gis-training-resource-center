# Data Analysis with QGIS
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

~~(* The purpose of spatial analysis in humanitarian IM is usually to describe a changing situation or toorient people to a new crisis)~~

We are usually looking for ways to __describe__ our data to an audience in some ways. Sometimes spatial analysis will be used to provide recommendations for activities. 

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

Considering the amount of data available online, it is always important to take a step back and gain perspective when facing this knowledge, these capacities, as well as the data itself before rushing in to manipulate it:
* Reliability: Can I trust this data?
* Interest: Do I need this data?
* Usage: Am I able to use this data?
* Comprehensiveness: Is this data complete?
* Date: How old is this data?
* Sensitivity: Is this data sensitive?
