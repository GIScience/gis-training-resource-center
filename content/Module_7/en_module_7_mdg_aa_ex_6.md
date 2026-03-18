::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Exercise 6: Exporting Model Results for the Operations Team

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
^^^
Aina, the GIS expert at the Malagasy Red Cross (CRM), is preparing for the upcoming cyclone season. She wants to improve her team’s ability to act quickly once a storm is forecasted by automating key analyses in QGIS. These include estimating exposed populations, identifying impacted services like health and education, and assessing whether health posts can be reached from key warehouses within a critical 10-hour window.
The goal is to prepare an end-to-end analysis and visualization workflow that can support fast, data-driven anticipatory action before a cyclone makes landfall.

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

## Available data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_7_Exercise_4_AA_MDG_task_6-20250825T143514Z-1-001.zip

__Download all datasets here, save the folder on your computer and unzip the file.__ 
:::

**Context – Aina Supports Decision Makers**

After producing maps and visuals, Aina often gets requests from the operations team:  
> _“Can you send us the data in table format?”_

Instead of exporting these tables manually each time, Aina wants to automate this step within her model — ensuring that every run of the model produces clear, ready-to-use data files.

In this task, you’ll help Aina extend her existing model to export selected layers.

We will join the following layers step by step:

- `admin2_health_affected_pct`:  
  Contains the **total number of health facilities**, the **number of affected health facilities**, and the **percentage of affected health facilities**.

- `admin2_education_affected_pct`:  
  Contains the **total number of education facilities**, the **number of affected education facilities**, and the **percentage of affected education facilities**.

- `exposed_population`:  
  Contains the **total population per district** and the **exposed population** from the zonal statistics step.

---

# Tasks


1. Open your model
- Open `Estimate_Exposed_Population_Health_Education`
- Save a new version as:  
  ```
  Estimate_Exposed_Population_Health_Education_Spreadsheet_Export
  ```
2. Join Health and Education data into one layer
- In the **Algorithms**, search for `Join Attributes by Field Value`.
- Add a description: `Joindre santé et éducation dans une seule couche par ADM2`
- Configure the algorithm as follows:
  - **Input Layer**: `admin2_health_affected` (select from **Algorithm Output**)
  - **Input Layer 2**: `admin2_education_affected` (select from **Algorithm Output**)
  - **Table field**: 
   ```
   ADM2_PCODE
   ```
  - **Table field 2**: 
   ```
   ADM2_PCODE
   ```
  - **Layer 2 fields to copy**: Leave empty (all fields will be copied)
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**

:::{figure} /fig/fr_MDG_AA_model_join_affacted_pop.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de santé et d’éducation par le champ `ADM2_PCODE` afin de combiner les résultats dans une seule couche.
::: 
3. Join the result with the population data
Now join the result of the previous step (health + education) to the **exposed population** data.
- Add a second `Join Attributes by Field Value` algorithm to the model
- Add a description: `Joindre les données de population avec les indicateurs santé et éducation`
- Configure the algorithm as follows:
  - **Input Layer**: `exposed_population` (select from **Algorithm Output** of the Zonal Statistics step)
  - **Input Layer 2**: Output from Step 2 (health + education)
  - **Table field**: 
   ```
   ADM2_PCODE
   ```
  - **Table field 2**: 
   ```
   ADM2_PCODE
   ```
  - **Layer 2 fields to copy**: *(Enter the following field names exactly as shown — comma-separated, no spaces)*
    ```
    count_health_total;sum_exposed_health;pct_exposed_health;count_education_total;sum_exposed_education;pct_exposed_education
    ```
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**

:::{figure} /fig/fr_MDG_AA_model_join_affacted_pop_HS_ES.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de population avec les indicateurs de santé et d’éducation.
::: 

::::{tip} Where to find the column names  
Open the **attribute tables** of the outputs `health_total_per_admin2`, `sum_exposed_healthsites_POI`, and `admin2_health_affected_pct` in QGIS.  
Look at the **column headers** to find the exact names of the fields you want to copy.
::::
::::{warning} Invisible spaces will break the join  
If a column name like `count_health_total` has an invisible trailing space, the join will silently fail.  
Always copy field names **directly from the attribute table** to avoid errors.
::::


4. Export results to a spreadsheet
- In the **Processing Toolbox**, search for `Export to spreadsheet` and double-click to open.
- Add a description: `Exporter les données de population, d'éducation et de santé dans un seul tableau`
- Configure the tool as follows:
  - **Input Layer**: Select the output of Step 3 from **Algorithm Output**
  - **Destination spreadsheet**:
    ```
    exposure_indicators_spreadsheet
    ```

  - Click **OK** to add it to the model.
Once you run the model, this step will automatically generate a spreadsheet with all relevant indicators ready for the operations team!

:::{figure} /fig/fr_MDG_AA_model_export_as_table.PNG
---
width: 600px
name: the_world_result
align: center
---
Exporter tous les indicateurs (population, santé, éducation) vers un tableau unique au format tableur.
::: 



5. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
6. **Run the model**
   - Click the ▶️ **Run** button in the top-right corner of the Graphical Modeler window.
   - **Input:**
     - Click on the three dots for each input dataset and select the correct input:
       - `Cyclone Track` → select the GeoJSON of the storm path (e.g. `Harald_2025_Track.geojson`)
       - `Population Raster` → select the WorldPop raster file
       - `Admin Boundaries` → select the Admin 2 layer (e.g. `MDG_adm2.gpkg`)
       - `Health Facilities` → select the point dataset for health sites
       - `Education Facilities` → select the point dataset for schools
   - **Output:**
     - Save all output layers in the output folder and use the names below.
       - `admin2_health_affacted` -> 
        ```
        admin2_health_affected
        ```
       - `admin2_education_affected` ->
        ```
        admin2_education_affected
        ```
       - `cyclone_harald_buffer` ->  
        ```
        cyclone_harald_buffer
        ```
       - `exposed_population_sum` ->
        ```
        admin2_harald_Exposed_Population
        ```
       - `exposure_indicators_spreadsheet` ->
        ```
        exposure_indicators_harald
        ```
   - Click **Run** to execute the full model.

:::::{tab-set}

::::{tab-item} Graphic Modler

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task_6_export_spreadsheet__model.PNG
---
width: 600px
align: center
---
Vue du modeleur graphique avec l’étape d’exportation vers un tableau ajoutée au modèle.
:::
::::
::::{tab-item} Run Model Configuration
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_run_configurations.PNG
---
width: 600px
align: center
---
Fenêtre de configuration pour exécuter le modèle avec l’option d’export vers un tableau.
:::
::::
::::{tab-item} Model Output
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_results_AT.PNG
---
width: 600px
align: center
---
Résultats finaux du modèle exportés dans un tableau prêt à être utilisé.
:::
::::
:::::

---



