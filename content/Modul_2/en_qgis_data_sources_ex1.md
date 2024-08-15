# Exercise 3: Data sources
## Characteristics of the exercise

<!--This exercise is quite minimal with the explanation of steps (most should be looked up) so it is not suited for a follow along session -->

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_modul_2_exercises.html

__Click here to return to the exercise overview page for module 2__ 

:::

::::{grid} 2
:::{grid-item-card}
#### Aim of the exercise
The aim of this exercise is to navigate various data sources, gain an 
understanding of where and how to access relevant data, and identify potential problems. It is important to use reliable, up-to-date, and appropriate data sources** that fit the purpose of the analysis to ensure a successful and meaningful results. Always consider your analysis objectives and requirements and search for data accordingly.


#### Type of trainings exercise:

- This exercise can be used in online and presence training. 

:::

:::{grid-item-card}

#### Focus group (GIS-Knowlege Level)

- QGIS Beginners
- The skills tested in this exercise are necessary for all GIS-users.

#### These skills are relevant for 

- Finding and downloading relevant datasets and preparing them for further analysis

:::
::::

::::{grid} 2
:::{grid-item-card}

#### Estimated time demand for the exercise.

- The exercise takes around 1 hour to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}

### Relevant Wiki articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification - Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)

:::

::::



## Exercise 
### Available Data

Since the exercise is about finding data, there won't be any data to download. 
Instead download the usual folder structure [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) and insert your data as you download it.

### Tasks

The objective of this exercise is to find out how many hospitals are located in **Bolivia** and how they are distributed across the country. 

1. Find a data source to download the **administrative boundaries** and **healthsites** of Bolivia. The following instructions are designed for the example of Bolivia. If you wish to perform the same analysis for another country, some instructions may differ, but the general workflow will remain the same.

:::{dropdown} Possible data sources
Test downloading the administrative boundaries on [OSM Boundaries](https://osm-boundaries.com) 
and the healthsites on [healthsites.io](https://healthsites.io).
:::
<!-- SUGGESTION: some of the instructions below assume that these are the datasets
   that are being used, instead of just examples. Can we just ask people to use these
   datasets, so that the rest of the instructions make sense? -->

2. Download the data and save the administrative boundaries as `bolivia` and the healthsites `healthsites_bolivia` into the 
   `data\input` folder.

```{Note}
Make sure to only use the point data from the healthsites dataset. Other data shapes such as lines or polygons can be ignored in this example. Depending on the data source, information can be provided as points, but also as lines or polygons.
```

3. Load both vector files into QGIS.  

4. Now add the OpenStreetMap basemap via the browser window > 
   `XYZ Tiles`. Adding basemaps can help you orient yourself, gain a better understanding of the area of interest, and create more informative maps. 

5. Familiarise yourself with the data by opening the attribute table and identify the different types of healthcare that are included in the dataset. Get an overview of the information that is stored in each column. For example, there could be information indicating the type of healthsite.

<!--ADD: Context: Having this exercise in the 
   context of a scenario could help with things like this --> 

6. If your dataset contains information about the type of healthsite (e.g. clinic, hospital, doctor, etc.), we can extract these and save them in a new layer. We can do this by selecting the hospitals and then copying them to a new layer.

```{Hint}
For information on how to easily filter your data by manually selecting features in the attribute table after it has been sorted based on a particular column, see the __[attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)__ page on the wiki.
```
<!-- Should we direct people to instructions on filters rather than attribute table?
EN: The information on how to filter is in this wiki page. Add the heading to the link -->

7. To view only the selected features (hospitals) and apply the filtering, we can first display these features in the attribute table by clicking on `Show Selected Features` in the bottom left corner, and then export only the selected features and save them as `hospitals_bolivia` in your `data\output` folder.

8. Save your project and display your results. Ensure that both the country of Bolivia and the hospitals are visible.


### Result

```{figure} /fig/en_result_data_sources_exercise.png
---
width: 80%
name: en_result_data_sources_exercise
---
Your map could look like this when you have finished the exercise. 
```

The distribution of hospitals across Bolivia is uneven. It is noticeable that there are significantly less hospitals in the northern and eastern parts of Bolivia.

<!-- FIXME: if the aim of the exercise is to understand the distribution of hospitals
   in Bolivia, this should be clear in the introduction so that people can understand
   why they are performing the steps.  --> 