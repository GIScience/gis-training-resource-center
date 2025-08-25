::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Exercise 7: Reachability of health Posts from CRM Warehouses

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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_9_Exercise_7_AA_MDG_task_7-20250825T143515Z-1-001.zip

__Download all datasets here, save the folder on your computer and unzip the file.__ 
:::


## Context

When a cyclone is forecast to make landfall, Aina works with the logistics and health teams to decide **where to send prepositioned medical kits**. However, not all CRM warehouses stock the needed items — only three do.

To make fast, data-driven decisions, Aina wants to know **which health posts are reachable** from those warehouses **within 10 hours**. This analysis helps ensure that kits are sent to facilities **that can actually be reached in time**.

Her goal is to create a clear visual map showing reachable vs. non-reachable health posts — and share this with decision-makers as quickly as possible.

## Tasks

## 1. Filter Health Posts from the National Health Facility Dataset

Before checking which facilities are reachable, Aina needs to isolate **health posts** from the broader dataset of all health facilities.

1. **Load the health facilities dataset**  
   - File: `hotosm_mdg_health_facilities_points.gpkg` (or the respective GeoPackage you are using)  
   - Load it via drag and drop or through `Layer` → `Add Vector Layer`.
2. **Open the attribute table** and check the column named `amenity`.
3. **Filter by expression** to keep only health posts:  
   - Right-click the layer → `Filter…`  
   - Use the following expression:
     ```qgis
     "amenity" = 'health_post'
     ```
4. **Export the filtered layer**  
   - Right-click the filtered layer in the Layers Panel → `Export` → `Save Features As…`  
   - Format: `GeoPackage`  
   - Save to your `project` folder as:
     ```
     health_posts_only.gpkg
     ```
   - Click `OK` to confirm export.
5. **Remove the filter** or original layer from your project to avoid confusion.
> 💡 **Tip**: Filtering directly in QGIS lets you work with a specific subset of features without modifying the original dataset.

## 2. Load Isochrone Layers for the Three CRM Warehouses

Aina knows that only **three warehouses** stock the necessary medical supplies:  
**Antananarivo**, **Maroantsetra**, and **Tolanaro**. She will now load the isochrone layers for each of these warehouses to begin analyzing service areas.

1. **Load the individual isochrone layers** for each warehouse:
   - `CRM_warehouse_Isochrones_Antananarivo.gpkg`
   - `CRM_warehouse_Isochrones_Maroantsetra.gpkg`
   - `CRM_warehouse_Isochrones_Tolanaro.gpkg`

   You can drag and drop each file into QGIS or go to `Layer` → `Add Layer` → `Add Vector Layer`.

2. **Inspect the attribute table** of each isochrone layer  
   Confirm that each record has a `traveltime_h` field showing the estimated travel time in **hours**.

3. **Remove all features where travel time is above 10 hours**:  
   - Right-click each layer → `Filter…`
   - Apply the expression:
     ```qgis
     "traveltime_h" <= 10
     ```

4. **Export each filtered layer** to the `temp` folder :
   At this point, Aina also ensures all exported layers are saved in the same CRS as the health post dataset — `EPSG:4326` — to avoid problems in the spatial join.
   - Save each as:
     ```
     CRM_isochrones_Antananarivo_upto10h.gpkg
     CRM_isochrones_Maroantsetra_upto10h.gpkg
     CRM_isochrones_Tolanaro_upto10h.gpkg
     ```

5. **Style the isochrones for clarity** 
   Aina can apply predefined style file to color the layer based on `traveltime_h` to visualize different time bands (4h, 6h, 8h, 10h) later in Step 5.
   - Right-click each filtered layer → `Properties` → `Symbology`
   - Click `Style` at the bottom → `Load Style…`
   - Select the file:  
     `CRM_warehouse_isochrones_style.qml`
   - Click `Open`, then `Apply` and `OK`

## 3. Visualizing Health Post Reachability from CRM Warehouses

Aina needs to identify which health posts can be reached by road from three key CRM warehouses (Antananarivo, Maroantsetra, and Tolanaro) **within 10 hours of travel time**. She will do this manually by combining the 10-hour isochrones from these warehouses and comparing them to the national health post dataset.
1. **Merge the Isochrone Layers from the Three Warehouses**  
   - In the **Processing Toolbox**, search for `Merge Vector Layers`.  
   - **Input layers**:  
     - `CRM_isochrones_Antananarivo_upto10h.gpkg`  
     - `CRM_isochrones_Maroantsetra_upto10h.gpkg`  
     - `CRM_isochrones_Tolanaro_upto10h.gpkg`  
   - **CRS**: `EPSG:4326`  
   - **Save to file**:  
     ```
     merged_isochrones_10h.gpkg
     ```  
   - Click **Run**.
2. **Select Health Posts Reachable Within 10 Hours**  
   - In the **Processing Toolbox**, search for `Select by Location`.  
   - Set the following parameters:  
     - **Input layer**: `health_posts_only.gpkg`  
     - **Predicate**: `intersects`  
     - **Intersect layer**: `merged_isochrones_10h.gpkg`  
   - Click **Run**.
   > 💡 The selected points are those within the 10-hour service areas of the warehouses.
3. **Create a Reachability Field for Selected Health Posts**  
   - Open the **Field Calculator** ![](/fig/mActionCalculateField.png) on the `health_posts_only` layer.  
   - Check ✅ `Only update selected features`  
   - **Output field name**: `Reachability_time`  
   - **Output field type**: `Text (string)`  
   - **Expression**:
     ```qgis
     'reachable in 10 hours'
     ```  
   - Click **OK** to create and populate the new field for selected features.
4. **Mark the Remaining Health Posts as Not Reachable**  
   - Invert the selection:  
     Go to `Edit` → `Invert Feature Selection` ![](/fig/mActionInvertSelection.png)  
     or right-click the layer and select `Invert Selection`.  
   - Open the **Field Calculator** again.  
   - Check ✅ `Only update selected features`  
   - Use the same field: `Reachability_time`  
   - **Expression**:
     ```qgis
     'not reachable in 10 hours'
     ```  
   - Click **OK** to apply the update.

> ✅ Now all health posts are labeled as either **reachable** or **not reachable** in the `Reachability_time` column.

