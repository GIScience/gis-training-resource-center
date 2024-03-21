# Data Sources Exercise 1

### Aim of the exercise
The objective of this exercise is to navigate different data sources, develop an 
understanding of where and how to access relevant data and what to look out for.
<!-- CLARIFY: what to look out for for what? -->

## Relevant wiki articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Graduated](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_graduated_wiki.html)

### Data
Since the exercises aim is for you to find data, there won't be any data to download. 
Instead download the usual folder structure [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_2/Modul_2_Exercise_Data_sources/Modul2_data_sources_exercise.zip) and add in your data as you download it.

### Tasks

We want to see how many hospitals are in Bolivia. 

1. Find a data source to download the administrative boundaries and the 
health sites of Bolivia.

:::{dropdown} Example data sources
Try downloading the administrative boundaries on [OSM Boundaries](https://osm-boundaries.com) 
and the healthsites on [healthsites.io](https://healthsites.io).
:::
<!-- SUGGESTION: some of the instructions below assume that these are the datasets
   that are being used, instead of just examples. Can we just ask people to use these
   datasets, so that the rest of the instructions make sense? -->

2. Download and save them as `bolivia` and `healthsides_bolivia` into the 
   `data\input` folder. Only use the point data from the healthsites dataset.

3. Load both files in QGIS.  

4. Optional: You can add the OpenStreetMap base map via the browser window --> 
   XYZ Tiles. 

<!-- CLARIFY: what is the purpose of this being an optional step? -->

5. Get familiar with the data by opening the attribute table.
<!-- FIXME: this instruction could be more specific. what sorts of things should 
   people try to understand from the attribute table? Having this exercise in the 
   context of a scenario could help with things like this --> 

6. Filter the health sites layer so that it only hospitals.

```{Hint}
To find out how to filter by an expression see the __[attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)__
page on the wiki.
```
<!-- Should we direct people to instructions on filters rather than attribute table? -->

7. To only view the selected features (hospitals), export only selected features 
and save as `hospitals_bolivia` in your `data\output` folder.
<!-- CLARIFY: are we asking people to filter or select? it's not clear to me from
   these instructions -->

8. As you can see, there are significantly less hospitals in the north and east 
of Bolivia.
<!-- FIXME: if the aim of the exercise is to understand the distribution of hospitals
   in Bolivia, this should be clear in the introduction so that people can understand
   why they are performing the steps. 

   this point no. 8 is not a step, so could be moved under the exercise steps as 
   "Results" or "Discussion" or something --> 

9. Save your project.


### Result

```{figure} /fig/en_result_data_sources_exercise.png
---
width: 80%
name: en_result_data_sources_exercise
---
Your map should look like this when you have finished the exercise. 
```