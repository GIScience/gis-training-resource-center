::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercise 3: Data sources

<!--This exercise is quite minimal with the explanation of steps (most should be looked up) so it is not suited for a follow along session -->

## Characteristics of the exercise

:::{card}
:class-card: sd-text-justify
__Aim of the exercise:__
^^^

The aim of this exercise is to navigate various data sources, gain an 
understanding of where and how to access relevant data, and identify potential problems. It is important to **use reliable, up-to-date, and appropriate data sources** that fit the purpose of the analysis to ensure a successful and meaningful results. Always consider your analysis objectives and requirements and search for data accordingly.

:::

::::{grid} 2
:::{grid-item-card}
__Larkana Flood Response Exercise Track__
^^^

This exercise is part of the [Larkana Flood Response Exercise Track](https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/en_larkana_flood_response.html).

:::

:::{grid-item-card}
__Competences covered in this exercise__
^^^ 

- QGIS essentials
- Finding and downloading relevant datasets and preparing them for further analysis
- Data literacy

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 1 hour to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant Wiki articles and module chapters__
^^^

* [QGIS Interface](/content/Wiki/en_qgis_interface_wiki.md)
* [Types of Geodata](/content/Wiki/en_qgis_geodata_types_wiki.md)
* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Layer Concept](/content/Wiki/en_qgis_layer_concept_wiki.md)
* [Geodata Classification - Graduated](/content/Wiki/en_qgis_graduated_wiki.md)
* [Data Sources](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_data_sources.html)

:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 
## Prepare the training:

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

## Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::

## Exercise 

### Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip

Since the exercise is about finding data, there won't be any data to download. 
Instead download the __[standard folder structure](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_management.html#standard-folder-structure)__ [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) and insert your data as you download it.

:::

::::{dropdown} Standard folder structure
```{figure} /fig/standard_folder_structure_new_2025.drawio.png
name: standard_folder_struc
width: 500 px
---
Standard folder structure. Source: HeiGIT
```
::::

### Task 1: Download the administrative boundaries and healthsites for Pakistan 

For our flood response map, we will need a few datasets from the web. In this exercise, we will be looking for the __administrative boundaries__ of Pakistan, the __healthsites__, as well as the __flood extent__ of the flood in Pakistan in 2024. 
First, let us set up a new QGIS project along with the standard folder structure: 

::::{margin}
:::{tip}
Take a look at the standard folder structure and save the QGIS project file in the correct place.
:::
::::

1. Download the folder structure and unzip it.
2. Create a copy of the folder structure and name the folder `module_2_exercise_3_data_sources`.
3. Open a new QGIS project and save it into the folder. 

Now that we have the QGIS project set up, we can start looking for the datasets

4. Find a data source to download the **administrative boundaries** and **healthsites** of Pakistan. The following instructions are designed for the example of Pakistan. If you wish to perform the same analysis for another country, some instructions may differ, but the general workflow will remain the same.

:::{dropdown} Possible data sources

There are many different data repositories on the web where you can find suitable data. You can find a list of possible data sources [here](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_data_sources.html).

For most humanitarian data, you can search on the __[Humanitarian Data Exchange/HDX](https://data.humdata.org/)__
The Humanitarian Data Exchange (HDX) is a primary platform for accessing and sharing geospatial data relevant to humanitarian crises. It's a centralized repository offering a wide range of datasets from various sources, making it an invaluable resource for aid organizations and researchers.

:::

:::{admonition} Which data format to choose

Most datasets on HDX are available in various dataformats such as xlsx, csv, shapefile, or GeoJSON. We are looking for spatial data that we can use in QGIS, so we will need a spatial data format such as `.shp` (Shapefile), `.gpkg` (GeoPackage), `.geojson` (GeoJSON), or `.gdb` (GeoDatabase)

:::

<!-- SUGGESTION: some of the instructions below assume that these are the datasets
   that are being used, instead of just examples. Can we just ask people to use these
   datasets, so that the rest of the instructions make sense? -->

5. Download the data and save the **administrative boundaries** and the **healthsites** into the `data\input` folder.

```{Note}
Make sure to only use the point data from the healthsites dataset. Other data shapes such as lines or polygons can be ignored in this example. Depending on the data source, information can be provided as points, but also as lines or 
polygons.
```

::::{margin}
:::{tip}
Most of the times, the datasets you download from the web are compressed as `.zip`-files. Before you can use them in QGIS, __you need to unzip the datasets__.
:::
::::

6. [Load both vector files into QGIS](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_concept.html#data-import).


7. Now add the OpenStreetMap basemap via the browser window > 
   `XYZ Tiles`. Adding basemaps can help you orient yourself, gain a better understanding of the area of interest, and create more informative maps. 

8. Familiarise yourself with the data by opening the attribute table and identify the different types of healthcare that are included in the dataset. Get an overview of the information that is stored in each column. For example, there could be information indicating the type of healthsite.


9. If your dataset contains information about the type of healthsite (e.g. clinic, hospital, doctor, etc.), we can extract these and save them in a new layer. We can do this by selecting the hospitals and then copying them to a new layer.

```{Hint}

For information on how to easily filter your data by manually selecting features in the attribute table after it has been sorted based on a particular column, see the __[attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)__ page on the wiki.

```

### Task 2: Download the flood extent for Pakistan for August 2024

Now, let us download the flood extent for Pakistan from the 8 to 12 August 2024.

Go back to the humanitarian data exchange and search for __"Pakistan Flood"__. You will find a list of datasets containing the satellite detected water extents for different periods. Choose the dataset with the title __"Satellite detected water extents from 08 to 12 August 2024 over Pakistan"__ and download the shapefile. 



<!---
10. To view only the selected features (hospitals) and apply the filtering, we can first display these features in the attribute table by clicking on `Show Selected Features` in the bottom left corner, and then export only the selected features and save them as `hospitals_bolivia` in your `data\output` folder.

11. Save your project and display your results. Ensure that both the country of Bolivia and the hospitals are visible.

-->

<!---
### Result

```{figure} /fig/en_result_data_sources_exercise.png
---
width: 80%
name: en_result_data_sources_exercise
---
Your map could look like this when you have finished the exercise. 
```

The distribution of hospitals across Bolivia is uneven. It is noticeable that there are significantly less hospitals in the northern and eastern parts of Bolivia.
-->

<!-- FIXME: if the aim of the exercise is to understand the distribution of hospitals
   in Bolivia, this should be clear in the introduction so that people can understand
   why they are performing the steps.  --> 