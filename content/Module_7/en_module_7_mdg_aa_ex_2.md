::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Exercise 2: Automation of Exposed Population Estimation – Aina's Model

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
* [Automation](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automation_wiki.html)

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




After manually estimating exposed populations in past cyclone seasons, Aina has decided to prepare an **automated model** using the **QGIS Graphical Modeller**. This will help her move faster and avoid repeating the same steps manually each time a cyclone is forecasted.

In this task, you will help Aina build a simple version of that model using the tools from Task 1. The model should:

- Reproject the cyclone track to EPSG:29738  
- Buffer the cyclone track  
- Reproject the buffer back to EPSG:4326  
- Clip the population raster  
- Run Zonal Statistics to get exposed population per district

---


## Tasks
1. **Set up the model structure**:
   - Open the **Graphical Modeler** from the top menu:  
     `Processing` → `Graphical Modeler…`

2. **Naming the model**:   
   - A new model window will open. On the **left side**, click on **`Model Properties`** to define basic information about the model:
     - **Model Name**: `Estimate_Exposed_Population`
     - **Group**: `Cyclone Trigger Tools`
     - Leave the description empty or write: _“Automated model to estimate exposed population based on cyclone buffer.”_

3. **Save the model**
   - To save the model:
     - Click the **Save** icon (💾) or go to `Model` → `Save`.
     - Navigate to the **`models` folder** of your training structure.
     - Save the model as:  
       **`Estimate_Exposed_Population`**

4. **Add model inputs**:  
   - On the **left panel**, expand the **Inputs** section.
   - Add the following input layers with type constraints:
     - `+ Vector Layer`  
       - **Label**: `Cyclone Track`  
       - In the **Advanced panel**, set **geometry type** to `Line`
     - `+ Raster Layer`  
       - **Label**: `Population Raster`
     - `+ Vector Layer`  
       - **Label**: `Admin Boundaries`  
       - In the **Advanced panel**, set **geometry type** to `Polygon`
   - These will appear at the top of your model canvas and serve as the input data when the model is run.

     ```{tip}
     All inputs should be set as **mandatory**, so the model always receives the necessary data to run correctly.
     ```

::::{tab-set}

:::{tab-item} Input Cyclon Track
```{figure} /fig/fr_MDG_AA_model_input_cyclon_track.PNG
---
width: 600px
align: center
---
Definition of the model input: Cyclon Track
```
:::

:::{tab-item} Input Admin Boundaries 
```{figure} /fig/fr_MDG_AA_model_input_admin_bounderies.PNG
---
width: 600px
align: center
---
Definition of the model input: Admin Bounderies
:::

:::{tab-item} Population Raster
```{figure} /fig/fr_MDG_AA_model_input_population_raster.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
```
:::
::::
**Intermediate Result**

```{figure} /fig/fr_MDG_AA_intermediate_result_model_input.PNG
---
width: 600px
name: the_world_result
align: center
---
Résultat intermédiaire de la définition des données d'entrée du modèle
```

5. **Reproject the cyclone track to EPSG:29738**  
   - From the **Algorithms** panel, search for **Reproject Layer** .
   - In the configuration window:
     - Add a description: `Reprojecter la couche de trajectoire du cyclone a EPSG : 29738`
     - Set **Input layer** to `Cyclone Track` (from **Model Input**).
     - Set **Target CRS** to `EPSG:29738 – Madagascar / Laborde Grid`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_reporject_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter la couche de trajectoire du cyclone vers un système de référence de coordonnées métrique (CRS) EPSG : 29738
```
6. **Buffer the reprojected cyclone track**  
   - From the **Algorithms** panel, search for **Buffer**.
   - In the configuration window:
    - Add a description:  `Mettre en mémoire tampon la couche Cyclone reprojetée`
     - Add a description: 
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Distance** to `200000` (200 km).
     - Leave **Segments** at the default value (`5`).
     - Set **Dissolve result** to `Yes`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_buffer_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Mettre en mémoire tampon la couche Cyclone reprojetée
```
7. **Reproject the buffer back to EPSG:4326**  
   - From the **Algorithms** panel, search for **Reproject Layer**.
   - In the configuration window:
    - Add a description:  `Reprojecter le tampon vers EPSG:4326`
   - In the configuration window:
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Target CRS** to `EPSG:4326 – WGS 84`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_reporject_bufferd_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter le tampon vers EPSG:4326
```
8. **Clip the population raster using the buffered area**  
   - From the **Algorithms** panel, search for **Clip Raster by Mask Layer** .
   - In the configuration window:
     - Add a description: `Découper la couche raster de population pour l'étendre au tampon Cyclon`
   - In the configuration window:
     - Set **Input layer** to `Population Raster` (from **Model Input**).
     - Set **Mask layer** to the output from the previous step (from **Algorithm Output**).
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_clip_pop_raster.PNG
---
width: 600px
name: the_world_result
align: center
---
Découper la couche raster de population pour l'étendre au tampon Cyclon
```
9. **Calculate zonal statistics to estimate exposed population**  
   - From the **Algorithms** panel, search for **Zonal Statistics** .
   - In the configuration window: Calcul de la population exposée aux cyclones par district
     - Add a description: `Calcul de la population exposée aux cyclones par district`
     - Set **Input layer** to `Admin Boundaries` (from **Model Input**).
     - Set **Raster layer** to the output of the previous step (from **Algorithm Output**).
     - Set **Output column prefix** to `exposed_population_`.
     - Under **Statistics to calculate**, select `Sum`.
     - Set the output to **Model Output** and name it: 
      ```
      exposed_population_sum
      ```
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_zonal_statistic_pop_admin2.PNG
---
width: 600px
name: the_world_result
align: center
---
Calcul de la population exposée aux cyclones par district
```

**Your results should look something like this:** 

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms.PNG
---
width: 600px
name: the_world_result
align: center
---
Votre modèle devrait ressembler à ceci. Tous les algorithmes sont correctement connectés et la sortie du modèle est définie.
```

10. **Validate your model (recommended)**
   - Before saving or running, click the ✔️ **Validate Model** button in the top toolbar.
   - Fix any warnings or errors shown in the log panel.
   - This helps ensure your model is complete and won't break during execution.

11. **Run the model**  
   - Run the model by clicking on `Model` -> `Run Model`
   - Set **Admin Bounderies** to `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Set **Cyclone Track** to `example_Harald_2025_Track`
   - Set **Population Raster** to `MDG_WorldPop_2020_constrained.tif`
   - Set the model output **exposed_population_sum** to `Harald_Exposed_Population`and save it in the `data` -> `output`


You can now run this model any time a new cyclone track becomes available.

```{figure} /fig/fr_MDG_AA_model_run_model_M7_e1_task2.PNG
---
width: 600px
name: the_world_result
align: center
---
Pour exécuter le modèle, spécifiez l'entrée comme indiqué dans l'image et définissez le nom de la couche de sortie.
```

**Your results should look something like this:**
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_basics.PNG
---
width: 600px
name: the_world_result
align: center
---

``` 
12. **Add the cyclone buffer as an additional model output**  
   - Double-click on the algorithm from step 7 (**Reproject the buffer back to EPSG:4326**) to open its configuration.  
   - In the **Output layer** field, check the box for **Model Output**.  
   - Give the output a clear name, for example:
     ```
     cyclone_harald_buffer
     ```  
   - Click **OK** to save the change.  
   - This will allow the model to produce both the exposed population results and the buffered cyclone impact zone when it is run.

```{figure} /fig/fr_MDG_AA_model_output_buffer.PNG
---
width: 600px
name: the_world_result
align: center
---
```

13. **Run the model again**  
   - Run the model by clicking on `Model` -> `Run Model`
   - Set **Admin Bounderies** to `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Set **Cyclone Track** to `example_Harald_2025_Track`
   - Set **Population Raster** to `MDG_WorldPop_2020_constrained.tif`
   - Set the model output **cyclone_harald_buffer** to `cyclone_harald_buffer`and save it in the `data` -> `output`
   - Set the model output **exposed_population_sum** to `Harald_Exposed_Population`and save it in the `data` -> `output`


::::{tab-set}


:::{tab-item} Graphic Modler Output Buffer 

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_graphic.PNG
---
width: 600px
name: the_world_result
align: center
---
```
Definition of the model input: Admin Bounderies
:::

:::{tab-item} Run Model with Buffer Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_model_exicution.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
```
:::

:::{tab-item} Model Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_extended_buffer.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
```
:::

::::

