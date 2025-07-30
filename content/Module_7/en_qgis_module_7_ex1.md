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

## Tasks: Estimating Exposed Population – Aina’s Manual Approach

Before developing the automated model, Aina used to estimate the exposed population manually whenever a cyclone approached Madagascar. In this task, you will follow the steps she used in the past by working with the historical track of **Cyclone Harald**, WorldPop raster data, and administrative boundaries.

You will manually buffer the cyclone track, clip the population raster, and calculate exposed population using zonal statistics.




1. **Open QGIS** and create a [new project](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. **Save the project** in the “project” folder. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Cyclon_Harald_Exposure”.

3. **Load the GeoJOSN** file "Harald_2025_Track.geojson" in your project by drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) .


4. **Reproject the cyclone track** to use meters instead of degrees (important for accurate buffering):
   - In the **Processing Toolbox**, search for `Reproject Layer`.
   - Input: `Harald_2025_Track`
   - Target CRS: `EPSG:29738` or another meter-based CRS appropriate for Madagascar.
   - Save the result in the `temp` folder as: **`Harald_Track_Reprojected`**
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
6. **Reproject the buffer back to EPSG:4326 (to match the raster's CRS):**
   - In the Processing Toolbox, search for Reproject Layer.
   - Input: Harald_Buffer_200km_29738
   - Target CRS: EPSG:4326 – WGS 84
   - Save the output in the temp folder as: Harald_Buffer_200km_4326
7. **Load the administrative boundaries**:
   - File: `MDG_adm2.gpkg`
   - Add using drag and drop or `Add Vector Layer`.
8. **Load the population raster**:
   - File: `MDG_WorldPop_2020_constrained.tif`
   - Add using `Layer` → `Add Raster Layer`.
9. **Clip the population raster** using the buffered impact zone:
   - In the **Processing Toolbox**, search for `Clip Raster by Mask Layer`.
   - Input raster: `MDG_WorldPop_2020_constrained.tif`
   - Mask layer: `Harald_Buffer_200km`
   - Save output in the `temp` folder as: **`Harald_Pop_Clip.tif`**
10. **Calculate total exposed population**:
   - In the **Processing Toolbox**, search for `Zonal Statistics`.
   - Input vector layer: `MDG_adm2.gpkg`
   - Raster layer: `Harald_Pop_Clip.tif`
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


## 🛠️ Task 2: Automatisation of Estimating Exposed Population – Aina's Model

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
     - Set **Output column prefix** to `pop_`.
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


## 🛠️ Task 3: Identifying Affected Health Facilities and Schools – Aina Adds More Layers

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
     - Output name: `sum_exposed_healthsites_POI`
8. **Count Affected Education Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Configuration:
     - **Points layer**: intersected education facilities output
     - **Count field name**: `count_education_affected`
     - Output name: `sum_exposed_education_POI`
9. **Calculate percentage of affected Health Facilities**
To compute the percentage of affected health sites per administrative area:
- Add **Join Attributes by Field Value**:
  - **Target layer**: `health_total_per_admin2` (output from the total count)
  - **Join layer**: `health_affected_per_admin2` (output from the affected count)
  - **Table field** and **Join field**: Use the shared ID field (e.g. `ADM2_PCODE`)
  - Leave the output unnamed (as intermediate result)

- Then add **Field Calculator**:
  - **Input layer**: the joined layer from above
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
- Add **Join Attributes by Field Value**:
  - **Target layer**: `education_total_per_admin2`
  - **Join layer**: `education_affected_per_admin2`
  - **Table field** and **Join field**: Use the common ID field (e.g. `ADM2_PCODE`)
  - Leave the output unnamed (as intermediate result)
- Then add **Field Calculator**:
  - **Input layer**: the joined education layer
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

## 🖼️ Task 4: Visualizing Cyclone Impact Results – Aina Styles Her Maps

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

## 🗺️ Task 5: Quick Map Creation – Aina Uses Map Templates
Background: Aina Gets Map-Ready in Minutes
After preparing all the analysis and styling, Aina wants to present her results quickly and professionally. She doesn’t want to recreate map layouts every time — she needs a quick way to generate clean, consistent maps.

That’s why she’s using map templates (.qpt files) already prepared by her team. These templates include map frames, legends, logos, titles, scale bars, and more — everything Aina needs to finish her product in just a few clicks.

✅ Goal
Use a provided QGIS map template to visualize and export maps showing cyclone exposure results, including population, health, and education impacts.

### 🧩 1. Load the pre-made print layout template

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

  
### 🖨️ 2. Check and set page size

- Right-click anywhere on the white canvas and choose `Page Properties`.
- On the right-side panel, ensure the following:
  - **Page Size**: A3
  - **Orientation**: Landscape

---


### 🧾 3. Update the attribute table of exposed districts

- In the **Print Layout**, click on the attribute table (right-hand side of the layout).
- In the **Item Properties** panel:
  - Ensure the correct layer is selected (e.g. `Exposed_Districts`)
  - Click `Refresh Table Data`
  - Click `Attributes…` → ➕ Add:
    - **Attribute**: `ADM1_EN`
    - **Sort Order**: Ascending
  - Click `OK`

---

### 🧭 5. Adjust the legend

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
---

### 📝 6. Review and update layout text elements

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