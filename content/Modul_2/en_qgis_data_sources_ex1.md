# Data Sources Exercise 1

### Aim of the exercise
The aim of this exercise is to **navigate various data sources**, gain an 
understanding of where and **how to access relevant data**, and **identify potential problems**. It is important to **use reliable, up-to-date, and appropriate data sources** that fit the purpose of the analysis to ensure a successful and meaningful results. **Always consider your analysis objectives and requirements** and search for data accordingly.
<!-- CLARIFY: what to look out for for what? -->

## Relevant wiki articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)

### Data
Since the exercise is about finding data, there won't be any data to download. 
Instead download the usual folder structure [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise_Data_sources/Modul2_data_sources_exercise.zip) and add in your data as you download it.

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

2. Download the data and save the administrative boundaries as `bolivia` and the healthsites `healthsides_bolivia` into the 
   `data\input` folder.

```{Note}
Make sure to only use the point data from the healthsites dataset. Other data shapes such as lines or polygons can be ignored in this example. Depending on the data source, information can be provided as points, but also as lines or polygons.
```

3. Load both vector files into QGIS.  

4. Now add the OpenStreetMap base map via the browser window --> 
   XYZ Tiles. Performing this step is beneficial for gaining an understanding of the location of the area of interest and creating more informative maps in the process. 

<!-- CLARIFY: what is the purpose of this being an optional step? -->

5. Familiarise yourself with the data by opening the attribute table and identify the different types of healthcare that are included in the dataset. Gain an understanding of the additional information provided alongside the healthsites and their type.
<!-- FIXME: this instruction could be more specific. what sorts of things should 
   people try to understand from the attribute table? Having this exercise in the 
   context of a scenario could help with things like this --> 

6. We now need to filter the healthsites layer to display only hospitals.

```{Hint}
For information on how to easily filter your data by manually selecting features in the attribute table after it has been sorted based on a particular column, see the __[attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)__ page on the wiki.
```
<!-- Should we direct people to instructions on filters rather than attribute table? -->

7. To view only the selected features (hospitals) and apply the filtering, we can first display these features in the attribute table by clicking on `Show Selected Features` in the bottom left corner, and then export only the selected features and save them as `hospitals_bolivia` in your `data\output` folder.
<!-- CLARIFY: are we asking people to filter or select? it's not clear to me from
   these instructions -->

8. Save your project and display your results. Ensure that both the country of Bolivia and the hospitals are visible and styled appropriately.


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
   why they are performing the steps. 

   this point no. 8 is not a step, so could be moved under the exercise steps as 
   "Results" or "Discussion" or something --> 