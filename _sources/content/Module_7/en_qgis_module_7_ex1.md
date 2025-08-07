::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Exercises 1: Automatisation

🚧This part of training platform is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Characteristics of the exercise



::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}


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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip

__Download all datasets [here](), save the folder on your computer and unzip the file.__ 

:::

The folder is called “ and contains the whole [standard folder structure](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#standard-folder-structure) with all data in the input folder and the additional documentation in the documentation folder.

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
name: IFRC Surge Icon
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

## Task 1: Estimating Exposed Population – Aina’s Manual Approach

Before developing the automated model, Aina used to estimate the exposed population manually whenever a cyclone approached Madagascar. In this task, you will follow the steps she used in the past by working with the historical track of **Cyclone Harald**, WorldPop raster data, and administrative boundaries.

You will manually buffer the cyclone track, clip the population raster, and calculate exposed population using zonal statistics.




1. **Open QGIS** and create a [new project](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. **Save the project** in the “project” folder. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Cyclon_Harald_Exposure”.

3. **Load the GeoJOSN** file "Harald_2025_Track.geojson" in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) . Open the folder `data` -> `input`


4. **Reproject the cyclone track** to use meters instead of degrees (important for accurate buffering):
   - In the **Processing Toolbox**, search for `Reproject Layer`.
   - Input: `Harald_2025_Track`
   - Target CRS: `EPSG:29738` or another meter-based CRS appropriate for Madagascar.
   - Save the result in the `temp` folder as: **`Harald_Track_Reprojected`**
```{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reprojetter la trajectoire du cyclone
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
Tamponner la trajectoire du cyclone
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
Reprojetter la tamponner trajectoire du cyclone
```
   
7. **Load the administrative boundaries**:
   - File: `MDG_adm2.gpkg`
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
Découpez la population ratser selon la zone affectée par le cyclone (trajectoire tampon du cyclone)
```

10. **Calculate total exposed population**:
   - In the **Processing Toolbox**, search for `Zonal Statistics`.
   - Input vector layer: `MDG_adm2.gpkg`
   - Raster layer: `Harald_Pop_Clip`
   - Statistic to calculate: `Sum`
   - Field prefix: e.g., `pop_`
   - Save the updated vector layer in the `result` folder as: **`Harald_Exposed_Population.gpkg`**
   - The result will be a new column in the attribute table of the `MDG_adm2.gpkg` layer, showing the total population within the cyclone buffer per district.
11. **Visualise the affected population by classifying the results**:
Now that Aina has estimated the exposed population in each district, she wants to clearly show the differences across regions on the map.
To do this, we'll apply a **graduated classification** to the `Harald_Exposed_Population.gpkg` layer using the new population field created by the Zonal Statistics tool.
- In the **Layers panel**, right-click on the layer `Harald_Exposed_Population` and choose `Properties`.
- Go to the **Symbology** tab on the left.
- At the top of the window, change the style from `Single Symbol` to `Graduated`.
- In the **Value** drop-down menu, select the field that contains the population sum. It typically starts with the prefix you defined earlier, e.g. `pop_sum`.
- Set the **color ramp** to one that suits your map (e.g. `Reds`).
- Choose a **classification mode** (e.g. `Quantile`, `Natural Breaks`, or `Equal Interval`) and select the number of classes (e.g. 5).
- Click `Classify` to generate the classification.
- Click `Apply` and then `OK` to display the classified map.

```{tip}
You can adjust class boundaries or labels by double-clicking on each class entry.
```


Your results should look something like this: 

```{figure} /fig/
---
width: 600px
name: the_world_result
align: center
---
```


## Task 2: Automatisation of Estimating Exposed Population – Aina's Model

After manually estimating exposed populations in past cyclone seasons, Aina has decided to prepare an **automated model** using the **QGIS Graphical Modeller**. This will help her move faster and avoid repeating the same steps manually each time a cyclone is forecasted.

In this task, you will help Aina build a simple version of that model using the tools from Task 1. The model should:

- Reproject the cyclone track to EPSG:29738  
- Buffer the cyclone track  
- Reproject the buffer back to EPSG:4326  
- Clip the population raster  
- Run Zonal Statistics to get exposed population per district

---

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
     - Navigate to the **`project` folder** of your training structure.
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

5. **Reproject the cyclone track to EPSG:29738**  
   - From the **Algorithms** panel, search for **Reproject Layer** and drag it into the model canvas.
   - In the configuration window:
     - Set **Input layer** to `Cyclone Track` (from **Model Input**).
     - Set **Target CRS** to `EPSG:29738 – Madagascar / Laborde Grid`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.

6. **Buffer the reprojected cyclone track**  
   - From the **Algorithms** panel, search for **Buffer** and drag it into the model canvas.
   - In the configuration window:
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Distance** to `200000` (200 km).
     - Leave **Segments** at the default value (`5`).
     - Set **Dissolve result** to `Yes`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.

7. **Reproject the buffer back to EPSG:4326**  
   - From the **Algorithms** panel, search for **Reproject Layer** and drag it into the model canvas.
   - In the configuration window:
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Target CRS** to `EPSG:4326 – WGS 84`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.

8. **Clip the population raster using the buffered area**  
   - From the **Algorithms** panel, search for **Clip Raster by Mask Layer** and drag it into the model canvas.
   - In the configuration window:
     - Set **Input layer** to `Population Raster` (from **Model Input**).
     - Set **Mask layer** to the output from the previous step (from **Algorithm Output**).
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.

9. **Calculate zonal statistics to estimate exposed population**  
   - From the **Algorithms** panel, search for **Zonal Statistics** and drag it into the model canvas.
   - In the configuration window:
     - Set **Input layer** to `Admin Boundaries` (from **Model Input**).
     - Set **Raster layer** to the output of the previous step (from **Algorithm Output**).
     - Set **Output column prefix** to `exposed_population_`.
     - Under **Statistics to calculate**, select `Sum`.
     - Set the output to **Model Output** and name it: `exposed_population_sum`
   - Click **OK** to add the step to the model.

10. **Validate your model (recommended)**
   - Before saving or running, click the ✔️ **Validate Model** button in the top toolbar.
   - Fix any warnings or errors shown in the log panel.
   - This helps ensure your model is complete and won't break during execution.

11. **Save your completed model**  
   - Once your model is finished and the final output is set, save your work.
   - Click the **Save** icon (💾) or go to `Model` → `Save`.
   - Navigate to the **`project` folder** of your training structure.
   - Save the model as:  
     **`Estimate_Exposed_Population.model3`**

You can now run this model any time a new cyclone track becomes available.


## Task 3: Identifying Affected Health Facilities and Schools – Aina Adds More Layers

After building her model to estimate exposed population, Aina wants to expand its usefulness. She decides to also **identify critical services** affected by cyclones — especially **health facilities** and **schools**. 

Not only does she want to know *which* facilities are affected, but also *how many in total exist* per district. That way, she can calculate the **percentage of services affected** in each area — a valuable insight for prioritizing early actions.

To achieve this, she will use two point datasets from OpenStreetMap:

- [Health facilities](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)  
- [Education facilities](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

1. **Save your model under a new name**  
   - Open your existing model `Estimate_Exposed_Population.model3`.
   - Immediately save it under a new name:
     - Click `Model` → `Save As…`
     - Save it to the `project` folder as:  
       **`Estimate_Exposed_Population_Health_Education.model3`**
2. **Add new model inputs**  
   - In the **Inputs** section, add:
     - `Vector Layer`  
       - **Label**: `Health Facilities`  
       - Set **Geometry Type** to `Point`
     - `Vector Layer`  
       - **Label**: `Education Facilities`  
       - Set **Geometry Type** to `Point`
3. **Count All Health Facilities per Admin 2**  
   - From the **Algorithms** panel, search for **Count Points in Polygon** and drag it in.
   - Configuration:
     - **Polygon layer**: `Admin Boundaries` (Model Input)
     - **Points layer**: full `Health Facilities` input
     - **Count field name**: `count_health_total`
     - Leave output as **Model Output**
4. **Count All Education Facilities per Admin 2**  
   - Add another **Count Points in Polygon** step.
   - Configuration:
     - **Points layer**: full `Education Facilities` input
     - **Count field name**: `count_education_total`
     - Leave output as **Model Output**
5. **Intersect Health Facilities with Cyclone Buffer**  
   - From the **Algorithms** panel, search for **Intersection** and drag it into the model.
   - In the configuration window:
     - **Input layer**: `Health Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output** 
   - Click **OK**
6. **Intersect Education Facilities with Cyclone Buffer**  
   - Add another **Intersection** algorithm.
   - Configuration:
     - **Input layer**: `Education Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output**
   - Click **OK**
7. **Count Affected Health Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Configuration:
     - **Polygon layer**: `Admin Boundaries`
     - **Points layer**: intersected health facilities output
     - **Count field name**: `count_health_affected`
8. **Count Affected Education Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Configuration:
     - **Points layer**: intersected education facilities output
     - **Count field name**: `count_education_affected`
9. **Calculate percentage of affected Health Facilities**
To compute the percentage of affected health sites per administrative area, we will use the **Field Calculator**:
- Add the  **Field Calculator**:
  - **Input layer**: the output of Count Affected Health Facilities per Admin 2
  - **Output field name**: `pct_health_affected`
  - **Field type**: Decimal (real)
  - **Expression**:
    ```qgis
    CASE WHEN "count_health_total" > 0
    THEN "sum_exposed_healthsites_POI" / "count_health_total" * 100
    ELSE 0
    END
    ```
  - Set the output as **Model Output**
  - Name it: `admin2_health_affected_pct`
10. **Calculate percentage of affected Education Facilities**
Repeat the process for schools:
- Add the **Field Calculator**:
  - **Input layer**: the output of Count Affected Education Facilities per Admin 2
  - **Output field name**: `pct_education_affected`
  - **Field type**: Decimal (real)
  - **Expression**:
    ```qgis
    CASE WHEN "count_education_total" > 0
    THEN "sum_exposed_education_POI" / "count_education_total" * 100
    ELSE 0
    END
    ```
  - Set the output as **Model Output**
  - Name it: `admin2_education_affected_pct`
11. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
12. **Run the model**
   - Click the ▶️ **Run** button in the top-right corner of the Graphical Modeler window.
   - In the popup dialog:
     - Browse to select the required input layers:
       - `Cyclone Track` → select the GeoJSON of the storm path (e.g. `Harald_2025_Track.geojson`)
       - `Population Raster` → select the WorldPop raster file
       - `Admin Boundaries` → select the Admin 2 layer (e.g. `MDG_adm2.gpkg`)
       - `Health Facilities` → select the point dataset for health sites
       - `Education Facilities` → select the point dataset for schools
     - Choose a location to save the output for the final layers (you can leave intermediate layers in temporary memory).
   - Click **Run** to execute the full model.
   - When finished, you should see all final output layers loaded into your QGIS workspace.

## Task 4: Visualizing Cyclone Impact Results – Aina Styles Her Maps

After completing her model, Aina wants to **communicate the results clearly** — both to her Red Cross colleagues and external partners.

She’s **tired of manually restyling every layer** every time new cyclone data comes in. Instead, she wants:
- ✅ **Clear and consistent visuals**
- 🔁 **Reusable templates**
- 📂 **Standardized .qml files** shared across projects

In this task, you will help Aina apply existing `.qml` styles and create new ones for layers that currently have no preset style.

---

### 1. **Load Required Layers (if not already loaded)**

Make sure the following layers are already loaded into your QGIS project. These are outputs from **Task 3**:

- `Harald_2025_Track`
- `Harald_Buffer_200km`
- `Harald_Exposed_Population`
- `sum_exposed_healthsites_POI`
- `sum_exposed_education_POI`
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

If any are missing:
- Load them using **drag & drop** from your `results` folder, or
- Use `Layer` → `Add Layer` → `Add Vector Layer` or `Add Raster Layer`

---

### 2. **Apply Predefined Style Files**
Apply the following `.qml` style files to the respective layers:

| **Layer**                              | **Style File**                            |
|----------------------------------------|-------------------------------------------|
| `Harald_2025_Track`                    | `storm_track_cyclone_style.qml`           |
| `Harald_Buffer_200km`                  | `exposed_cyclone_area_style.qml`          |
| `Harald_Exposed_Population`            | `exposed_population_style.qml`            |
| `sum_exposed_healthsites_POI`          | `exposed_healthsites_style.qml`           |
| `sum_exposed_education_POI`            | `exposed_education_facilities_style.qml`  |

**Steps:**
- Open the **Layer Styling Panel**
- Click the `Style` button → `Load Style…`
- Navigate to the corresponding `.qml` file
- Click **OK** to apply the style

> 💡 *If the style doesn’t load correctly, double-check the column names and make sure the column name used in the `.qml` file matches the one in your layer. To do this, open the **Attribute Table** of the layer and compare field names.*

---

### 3. **Style Percentage Layers Manually**

Now let’s style the two **percentage layers** that don’t yet have `.qml` files:
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

**Steps:**
- Select the layer and open the **Layer Styling Panel**
- Set **Symbology** to `Graduated`
- Choose the correct **field**:
  - `pct_health_affected` or `pct_education_affected`
- Open the **Histogram** tab to view the value distribution
- Set:
  - **Mode**: `Equal Interval`
  - **Classes**: `4`
  - **Breaks**: `0–25%`, `25–50%`, `50–75%`, `75–100%`
- Choose a color ramp (e.g., light yellow → dark red)
- Optionally customize class labels for clarity

> 🧠 *Why 4 equal classes?*  
> This helps visualize severity across districts using simple and interpretable risk categories. However, you can experiment with **Natural Breaks** if data is unevenly distributed.

---

### 4. **Save Your New Styles for Reuse**

Save your manually created styles as `.qml` files for future reuse.

**Steps:**
- In the **Styling Panel**, click `Style` → `Save Style…`
- Save the file in the same folder as the corresponding dataset
- Use these filenames:
  - `health_pct_affected_style.qml`
  - `education_pct_affected_style.qml`
---

### 5. *(Optional)* Import Styles into Your QGIS Library

To reuse your styles in any future project:

- Go to `Settings` → `Style Manager`
- Click `Import/Export` → `Import Items`
- Browse to and select your saved `.qml` files

The styles will now appear as presets in the **Layer Styling Panel**.

---

## Task 5: Quick Map Creation – Aina Uses Map Templates
Background: Aina Gets Map-Ready in Minutes
After preparing all the analysis and styling, Aina wants to present her results quickly and professionally. She doesn’t want to recreate map layouts every time — she needs a quick way to generate clean, consistent maps.

That’s why she’s using map templates (.qpt files) already prepared by her team. These templates include map frames, legends, logos, titles, scale bars, and more — everything Aina needs to finish her product in just a few clicks.

✅ Goal
Use a provided QGIS map template to visualize and export maps showing cyclone exposure results, including population, health, and education impacts.

1. Load the pre-made print layout template

- Locate the template `cyclone_impact_overview_map_template.qpt` in your project folder under:  
  `Map_Templates/`

- You can load the template **by drag-and-drop**:
  - Open your QGIS project.
  - Navigate to the Print Layout area in the browser panel.
  - Drag the `.qpt` file directly into QGIS — a new layout will be created automatically.

- Alternatively:
  - Go to `Project` → `New Print Layout`
  - Enter a name (e.g. `Harald_2025_Overview`)
  - Click `OK`
  - In the layout, go to `Layout` → `Import from Template…`
  - Select the file `cyclone_impact_overview_map_template.qpt` and click `Open`
 2. Check and set page size
- Right-click anywhere on the white canvas and choose `Page Properties`.
- On the right-side panel, ensure the following:
  - **Page Size**: A3
  - **Orientation**: Landscape
3. Update the attribute table of exposed districts
- In the **Print Layout**, click on the attribute table (right-hand side of the layout).
- In the **Item Properties** panel:
  - Ensure the correct layer is selected (e.g. `Exposed_Districts`)
  - Click `Refresh Table Data`
  - Click `Attributes…` → ➕ Add:
    - **Attribute**: `ADM1_EN`
    - **Sort Order**: Ascending
  - Click `OK`
5. Adjust the legend
- In the layout, click on the **Legend** item.
- In the **Item Properties** panel:
  - Uncheck **Auto update**
  - Scroll to **Legend items** and remove all entries (🗑️)
  - Add the following relevant layers:
    - `Relevant_Warehouses`
    - `Exposed_Cyclone_Area`
    - `Exposed_Districts`
    - `Admin1_Impact_Overview_Map`
  - When selecting layers, check **Only visible layers**
  - Rename legend entries to match layout naming
6. Review and update layout text elements
- Make sure all text elements are up to date, especially:
  - **Map title**
  - **Cyclone name and date**
  - **Author/Organization** (optional)
- Adjust font size or alignment if necessary


### ✅ Final Checklist

| Task                                           | Done |
|------------------------------------------------|------|
| Page set to A3 Landscape                       | ☐    |
| Only relevant layer group active               | ☐    |
| Exposed districts attribute table updated      | ☐    |
| Legend cleaned and renamed                     | ☐    |
| All text elements updated                      | ☐    |

---



```{dropdown} Your final output should look like this after styling the layer
The map now clearly displays the exposed population within the affected districts, along with the locations of relevant warehouses. The original storm track line — used as input data — is highlighted, as well as the buffered impact area, which serves as a proxy for identifying exposed districts.

On the right-hand side of the map, a list shows all exposed districts, including data on total population and exposed population. The districts (Admin 2) are organized under their corresponding regions (Admin 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map.png
---
width: 1000px
name: 
align: center
---
```

## Task 6: Exporting Model Results for the Operations Team

**Background – Aina Supports Decision Makers**

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

1. Open your model
- Open `Estimate_Exposed_Population_Health_Education.model3`
- Save a backup as:  
  `Estimate_Exposed_Population_Health_Education_Export.model3`
2. Join Health and Education data into one layer
- In the **Algorithms**, search for `Join Attributes by Field Value`.
- Configure the algorithm as follows:
  - **Input Layer**: `admin2_health_affected_pct` (select from **Algorithm Output**)
  - **Input Layer 2**: `admin2_education_affected_pct` (select from **Algorithm Output**)
  - **Table field**: `ADM2_PCODE`
  - **Table field 2**: `ADM2_PCODE`
  - **Layer 2 fields to copy**: Leave empty (all fields will be copied)
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**
3. Join the result with the population data
Now join the result of the previous step (health + education) to the **exposed population** data.
- Add a second `Join Attributes by Field Value` algorithm to the model
- Configure the algorithm as follows:
  - **Input Layer**: `exposed_population` (select from **Algorithm Output** of the Zonal Statistics step)
  - **Input Layer 2**: Output from Step 2 (health + education)
  - **Table field**: `ADM2_PCODE`
  - **Table field 2**: `ADM2_PCODE`
  - **Layer 2 fields to copy**: *(Enter the following field names exactly as shown — comma-separated, no spaces)*
    ```
    count_health_total,sum_exposed_healthsites_POI,health_affected_precentage,count_education_total,sum_exposed_education_POI,pct_education_affected
    ```
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**
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
- Configure the tool as follows:
  - **Input Layer**: Select the output of Step 3 from **Algorithm Output**
  - **Destination spreadsheet**:
    ```
    exposed_indicators_spreadsheet.xlsx
    ```

  - Click **OK** to add it to the model.
Once you run the model, this step will automatically generate a spreadsheet with all relevant indicators ready for the operations team!

## Task 7: Reachability of health Posts from CRM Warehouses
When a cyclone is forecast to make landfall, Aina works with the logistics and health teams to decide **where to send prepositioned medical kits**. However, not all CRM warehouses stock the needed items — only three do.

To make fast, data-driven decisions, Aina wants to know **which health posts are reachable** from those warehouses **within 10 hours**. This analysis helps ensure that kits are sent to facilities **that can actually be reached in time**.

Her goal is to create a clear visual map showing reachable vs. non-reachable health posts — and share this with decision-makers as quickly as possible.


### 1. Filter Health Posts from the National Health Facility Dataset

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

### 2. Load Isochrone Layers for the Three CRM Warehouses

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

### 3. Visualizing Health Post Reachability from CRM Warehouses
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





