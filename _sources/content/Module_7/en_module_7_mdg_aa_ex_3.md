::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Exercise 3: Identifying Affected Health Facilities and Schools – Aina Adds More Layers

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

## Tasks: 

After building her model to estimate exposed population, Aina wants to expand its usefulness. She decides to also **identify critical services** affected by cyclones — especially **health facilities** and **schools**. 

Not only does she want to know *which* facilities are affected, but also *how many in total exist* per district. That way, she can calculate the **percentage of services affected** in each area.

To achieve this, she will use two point datasets from OpenStreetMap:

- [Health facilities](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)  
- [Education facilities](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

1. **Load the health and education facilities datasets**
First, let's have a look at the data we want to work with.
- Navigate to your `input` data folder.  
- Drag and drop the following layers into your QGIS project:  
  - `hotosm_mdg_health_facilities`  
  - `hotosm_mdg_education_facilities`  
- Confirm that both layers are visible in the **Layers Panel** 
2. **Save your model under a new name**  
   - Open your existing model `Estimate_Exposed_Population.model3`.
   - Immediately save it under a new name:
     - Click `Model` → `Save As…`
     - Save it to the `project` folder as:
```  
Estimate_Exposed_Population_Health_Education
```
3. **Add new model inputs**  
   - In the **Inputs** section, add:
     - `Vector Layer`  
       - **Description**:
        ```
        Health Facilities
        ```
       - Set **Geometry Type** to `Point`
     - `Vector Layer`  
       - **Description**:
        ```
        Education Facilities
        ``` 
       - Set **Geometry Type** to `Point`
::::{tab-set}

:::{tab-item} Model Input: Health Facilities
```{figure} /fig/fr_MDG_AA_model_input_health_facilities.PNG
---
width: 300px
name: the_world_result
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements de santé
```
:::
:::{tab-item} Model Input: Education Facilities
```{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements d'éducation
```
:::
::::
3. **Count All Health Facilities per Admin 2**  
   - From the **Algorithms** panel, search for **Count Points in Polygon**.
   - Configuration:
     - Add a description: `Comptez le nombre d'établissements de santé dans chaque district.`
     - **Polygon layer**: `Admin Boundaries` (Model Input)
     - **Points layer**: `Health Facilities` (Model Input)
     - **Count field name**: 
      ```
      Count_health_total
      ```
     - Leave output as **Model Output**
```{figure} /fig/fr_MDG_AA_model_count_points_HF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements de santé dans chaque district.
```    
4. **Count All Education Facilities per Admin 2**  
   - Add another **Count Points in Polygon** step.
   - Configuration:
     - Add a description: `Comptez le nombre d'établissements de education dans chaque district`
     - **Polygon layer**: `Admin Boundaries` (Model Input)
     - **Points layer**: `Education Facilities` (Model Input)
     - **Count field name**: 
      ```
      count_education_total
      ```
     - Leave output as **Model Output**
```{figure} /fig/fr_MDG_AA_model_count_points_EF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements scolaires dans chaque district.
```
5. **Intersect Health Facilities with Cyclone Buffer**  
   - From the **Algorithms** panel, search for **Intersection**.
   - In the configuration window:
   - Add a description: 
      ```
      Établissements de santé dans la zone d'impact du cyclone
      ```  
     - **Input layer**: `Health Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output** 
   - Click **OK**
```{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de santé avec la zone d'impact du cyclone.
```
6. **Intersect Education Facilities with Cyclone Buffer**  
   - Add another **Intersection** algorithm.
   - Configuration:
     - Add a description:
       ```
       Établissements de education dans la zone d'impact du cyclone.
       ```  
     - **Input layer**: `Education Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output**
   - Click **OK**
```{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de education avec la zone d'impact du cyclone.
```
7. **Count Affected Health Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Add a description: `Compter les établissements de santé touchés par district`
   - Configuration: 
     - Add a description: Compter les établissements de santé touchés par district
       ```
       Compter les établissements de santé touchés par district
       ```  
     - **Polygon layer**: Count total health facilities output
     - **Points layer**: intersected health facilities output
     - **Count field name**: 
       ```
       sum_exposed_health
       ```  
```{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
8. **Count Affected Education Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Add a description: `Compter les établissements education touchés par district`
   - Configuration:
     - Add a description: 
       ```
       Compter les établissements education touchés par district
       ```   
     - **Polygon layer**: Count total education facilities output
     - **Points layer**: intersected education facilities output
     - **Count field name**: 
       ```
       sum_exposed_education
       ```  
```{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
9. **Calculate percentage of affected Health Facilities**
To compute the percentage of affected health sites per administrative area, we will use the **Field Calculator**:
- Add the  **Field Calculator**:
   - Add a description: `Calculer le pourcentage d’établissements de santé touchés par district`
   - Configuration:
     - Add a description:
       ```
       Calculer le pourcentage d’établissements de santé touchés par district
       ```  
    - **Input layer**: the output of Count Affected Health Facilities per Admin 2
    - **Output field name**:  
       ```
       pct_exposed_health
       ``` 
    - **Field type**: Decimal (real)
    - **Expression**:
    ```qgis
     CASE WHEN "count_health_total" > 0
     THEN "sum_exposed_health" / "count_health_total" * 100
     ELSE 0
     END
    ```
  - Set the output as **Model Output**
  - Name it:
   ```
   admin2_health_affected
   ```
```{figure} /fig/fr_MDG_AA_model_field_calc_pct_health_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements de santé touchés par district.
```
10. **Calculate percentage of affected Education Facilities**
To compute the percentage of affected education sites per administrative area, we will use the **Field Calculator**:  
- Add the **Field Calculator**:  
   - Add a description: `Calculer le pourcentage d’établissements d’éducation touchés par district`
   - Configuration:  
     - Add a description:  
       ```
       Calculer le pourcentage d’établissements d’éducation touchés par district
       ```  
     - **Input layer**: the output of Count Affected Education Facilities per Admin 2  
     - **Output field name**:  
       ```
       pct_exposed_education
       ```  
     - **Field type**: Decimal (real)  
     - **Expression**:  
       ```qgis
       CASE WHEN "count_education_total" > 0
       THEN "sum_exposed_education_POI" / "count_education_total" * 100
       ELSE 0
       END
       ```  
   - Set the output as **Model Output**  
   - Name it:  
     ```
     admin2_education_affected
     ```
```{figure} /fig/fr_MDG_AA_model_field_calc_pct_education_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements d’éducation touchés par district.
```
11. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
12. **Run the model**
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
   - Click **Run** to execute the full model.

::::{tab-set}

:::{tab-item} Graphic Modler

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model.PNG
---
width: 600px
align: center
---
Vue d’ensemble du Modèle Graphique de la tâche 3 montrant tous les algorithmes connectés et les sorties définies.
```
:::
:::{tab-item} Run Model Configuration
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_run_configurations.PNG
---
width: 600px
align: center
---
Configuration des paramètres pour exécuter le modèle de la tâche 3 avec toutes les couches d’entrée requises.
```
:::
:::{tab-item} Model Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model_results_AT.PNG
---
width: 600px
align: center
---
Résultats du modèle de la tâche 3 affichés dans QGIS, y compris les pourcentages d’établissements de santé et d’éducation touchés par district.
```
:::
::::

---
