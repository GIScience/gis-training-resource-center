::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Estimating Exposed Population – Aina’s Manual Approach

## Characteristics of the exercise

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__Exercise Track:__

This exercise is part of the [Madagascar Anticipatory Action Cyclon Analysis Exercise Track](https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/en_mdg_aa_cyclones.html)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^


:::

:::{grid-item-card}
__Relevant Wiki Articles__
^^^

* [Zonal Statistics](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html)
* [Intersection](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Projections](/content/Wiki/en_qgis_projections_wiki.md)
* [Buffer](/content/Wiki/en_qgis_projections_wiki.md)
* [Clip](/content/Wiki/en_qgis_projections_wiki.md)
* [Automatisation](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Aim of the exercise:__
Aina, the GIS expert at the Malagasy Red Cross (CRM), is preparing for the upcoming cyclone season. She wants to improve her team’s ability to act quickly once a storm is forecasted by automating key analyses in QGIS. These include estimating exposed populations, identifying impacted services like health and education, and assessing whether health posts can be reached from key warehouses within a critical 10-hour window.
The goal is to prepare an end-to-end analysis and visualization workflow that can support fast, data-driven anticipatory action before a cyclone makes landfall.
^^^



:::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) for some general tips on training conduction

### Conduct the training

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

## Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_5_Exercise_8_AA_MDG_task_1-20250825T143512Z-1-001.zip


__Download all datasets here, save the folder on your computer and unzip the file.__ 

:::



The folder contains the whole [standard folder structure](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#standard-folder-structure) with all data in the input folder and the additional documentation in the documentation folder.

| Dataset| Source | Descriptions |
| ----- | --- | --- |
| Administrative Boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | The administrative boundaries on level 0-4 for Madagascar can be accessed via HDX provided by OCHA. For this trigger mechanism we provide the administrative boundaries on level 1 (regional level) and 2 (district level) as a shapefile. |
| Cyclone Tracks | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive)  | IBTrACS project is the most complete global collection of tropical cyclones available. It merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset that improves inter-agency comparisons.  |
| education facilities and health sites| [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | The POI data (education facilities and health sites) is downloaded using the HOT Export Tool based on OpenStreetMap data. |
| Population | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | The worldpop dataset in raster format provides the estimated total number of people per grid-cell for the year 2020. We will be working with the Constrained Individual countries 2020 dataset at a resolution of 100m. |




:::{card} 
__Context__
^^^

```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC-icons-colour_SURGE
---
```

**Aina** is the GIS expert at the **Croix-Rouge Malagasy (CRM)**. With the cyclone season approaching, she knows that time is of the essence once a storm is forecasted. Every hour counts when it comes to protecting communities at risk.

This year, Aina wants to be one step ahead. Instead of manually analyzing cyclone data under pressure, she decides to **prepare an automated QGIS model** that will help her respond quickly and efficiently.

**Her goal:**  
> Build a workflow that automatically estimates exposed populations and infrastructure at risk.

:::

```{figure} /fig/Module_7/en_ex_m7_cylone_automatisation.drawio.png
---
name: Task_1_workflow
width: 750 px
---

```

# Tasks: 

Before developing the automated model, Aina used to estimate the exposed population manually whenever a cyclone approached Madagascar. In this task, you will follow the steps she used in the past by working with the historical track of **Cyclone Harald**, WorldPop raster data, and administrative boundaries.

You will manually buffer the cyclone track, clip the population raster, and calculate exposed population using zonal statistics.




1. **Open QGIS** and create a [new project](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. **Save the project** in the “project” folder. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Cyclon_Harald_Exposure”.

3. **Load the GeoJOSN** file "example_Harald_2025_Track.geojson" in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) . Open the folder `data` -> `input`


4. **Reproject the cyclone track** to use meters instead of degrees (important for accurate buffering):
   - In the **Processing Toolbox**, search for `Reproject Layer`.
   - Input: `example_Harald_2025_Track`
   - Target CRS: `EPSG:29738` or another meter-based CRS appropriate for Madagascar.
   - Save the result in the `temp` folder as: **`Harald_Track_Reprojected`**
```{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reproject the cyclone track
```

```{Attention}
Buffer distances must be calculated in meters. Many datasets (like GeoJSON cyclone tracks) use geographic coordinate systems like EPSG:4326, which measure in degrees — not meters. To correctly calculate a 200 km buffer, we must first reproject the track into a projected CRS that uses meters.
```
5. **Buffer the cyclone track**:
   - In the **Processing Toolbox**, search for `Buffer`.
   - Input: `Harald_Track_Reprojected`
   - Buffer distance: `200000` (meters)
   - Segments: Leave default (5)
   - Dissolve: `Yes`
   - Save output in the `temp` folder as: **`Harald_Buffer_200km`**
```{figure} /fig/fr_MDG_AA_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Buffering the cyclone track
```

:::{dropdown} Intermediate Result: Buffer
```{figure} /fig/fr_MDG_AA_intermediate_result_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Les résultats intermédiaires doivent montrer la trajectoire du cyclone et la zone tampon de 200 kilomètres autour de celui-ci. La zone tampon doit être une seule entité.
```
:::
6. **Reproject the buffer back to EPSG:4326 (to match the raster's CRS):**
   - In the Processing Toolbox, search for Reproject Layer.
   - Input: Harald_Buffer_200km_29738
   - Target CRS: EPSG:4326 – WGS 84
   - Save the output in the temp folder as: Harald_Buffer_200km_4326
```{figure} /fig/fr_MDG_AA_reproject_cyclon_buffer.PNG
---
width: 600px
align: center
---
Reprojecting the cyclone buffer
```
   
7. **Load the administrative boundaries**:
   - File: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Add using drag and drop or `Add Vector Layer`.
8. **Load the population raster**:
   - File: `MDG_WorldPop_2020_constrained.tif`
   - Add using `Layer` → `Add Raster Layer`.
9. **Clip the population raster** using the buffered impact zone:
   - In the **Processing Toolbox**, search for `Clip Raster by Mask Layer`.
   - Input raster: `MDG_WorldPop_2020_constrained`
   - Mask layer: `Harald_Buffer_200km`
   - Save output in the `temp` folder as: **`Harald_Pop_Clip`**
```{figure} /fig/fr_MDG_AA_clip_pop_raster.PNG
---
width: 600px
align: center
---
Clipping the population raster with the cyclone buffer
```
:::{dropdown} Intermediate Result: Clip Population Raster Alyer
```{figure} /fig/fr_MDG_AA_intermediate_result_clip_pop_raster.PNG
---
width: 600px
align: center
---
Intermediate Results
```
:::

10. **Calculate total exposed population**:
   - In the **Processing Toolbox**, search for `Zonal Statistics`.
   - Input vector layer: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Raster layer: `Harald_Pop_Clip`
   - Statistic to calculate: `Sum`
   - Field prefix: e.g., `exposed_population_`
   - Save the updated vector layer in the `result` folder as: **`Harald_Exposed_Populationg`**
   - The result will be a new column in the attribute table of the `mdg_admbnda_adm2_BNGRC_OCHA_201810312.gpkg` layer, showing the total population within the cyclone buffer per district.
```{figure} /fig/fr_MDG_AA_pop_zonal_statistic.PNG
---
width: 600px
align: center
---
Calculating the population exposed to the cyclone per district using the worldpop raster.
```
   
11. **Visualise the affected population by classifying the results**:
Now that Aina has estimated the exposed population in each district, she wants to clearly show the differences across regions on the map.
To do this, we'll apply a **graduated classification** to the `Harald_Exposed_Population` layer using the new population field created by the Zonal Statistics tool.
- In the **Layers panel**, right-click on the layer `Harald_Exposed_Population` and choose `Properties`.
- Go to the **Symbology** tab on the left.
- At the top of the window, change the style from `Single Symbol` to `Graduated`.
- In the **Value** drop-down menu, select the field that contains the population sum. It typically starts with the prefix you defined earlier, e.g. `exposed_population_sum`.
- Set the **color ramp** to one that suits your map (e.g. `Reds`).
- Choose a **classification mode** (e.g. `Quantile`, `Natural Breaks`, or `Equal Interval`) and select the number of classes (e.g. 5).
- Click `Classify` to generate the classification.
- Click `Apply` and then `OK` to display the classified map.

```{tip}
You can adjust class boundaries or labels by double-clicking on each class entry.
```
```{figure} /fig/fr_MDG_AA_pop_graduadt_classification_exposed_population.PNG
---
width: 600px
align: center
---
Classifying the exposed population into five classes.
```

# Results

Your results should look something like this: 

```{figure} /fig/fr_MDG_AA_intermediate_result_visualisation_exposed_population.PNG
---
width: 600px
name: the_world_result
align: center
---
Visualising the 5 classes. 
```
