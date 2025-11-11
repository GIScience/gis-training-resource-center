::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Exercise 5: Quick Map Creation - Aina Uses Map Templates

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
:link:  https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_4_Exercise_7_AA_MDG_task_5-20250825T143511Z-1-001.zip

__Download all datasets here, save the folder on your computer and unzip the file.__ 
:::


## Context

After all the hard work of analyzing data and styling layers, Aina is ready to **share her results**. But creating a professional-looking map from scratch every time would be slow and repetitive.  

To save time, she uses **map templates (.qpt files)** prepared by her team. These templates already contain the essential elements — map frames, legends, logos, titles, and scale bars. With them, Aina can turn her analysis into a **clean, consistent map** in just a few clicks.  

✅ **Goal**  
Apply a ready-made QGIS map template to quickly create and export maps that show cyclone impacts on population, health facilities, and schools.  


## Tasks: 



1. Load the pre-made print layout template

- Locate the template `cyclone_impact_population_map_template.qpt` in your project folder under:  
  `Map_Templates/`

- You can load the template **by drag-and-drop**:
  - Open your QGIS project.
  - Drag the `.qpt` file directly into QGIS — a new layout will be created automatically.

- Alternatively:
  - Go to `Project` → `New Print Layout`
  - Enter a name (e.g. `Harald_2025_population`)
  - Click `OK`
  - In the layout, go to `Layout` → `Import from Template…`
  - Select the file `cyclone_impact_overview_map_template.qpt` and click `Open`
 2. Check and set page size
- Right-click anywhere on the white canvas and choose `Page Properties`.
- On the right-side panel, ensure the following:
  - **Page Size**: A3
  - **Orientation**: Landscape

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_load_mpa_template.mp4"></video>

3. Update the attribute table of exposed districts
- In the **Print Layout**, click on the attribute table (right-hand side of the layout).
- In the **Item Properties** panel:
  - Ensure the correct layer is selected `Harald_Exposed_population`
  - Click `Refresh Table Data`
  - Click `Attributes…` → in the upper part under **Fields** click on `Clear`
    - Then add the following layer by clicking on ➕ :
    - **Attribute**: `ADM1_EN`; `ADM2_EN`; `ADM2_PCODE`; `exposed_population_sum`
    - To sort the tabel content, under the **Sorting**  clicking on ➕ and add the column `AMD1_EN`
    - **Sort Order**: Ascending
  - Click `OK`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_makingadjust_AT.mp4"></video>

  
```{admonition} ⚠️ Warning – Long Tables
If the attribute table you want to include is **longer than the map frame**, part of it will be cut off in the exported map.  
To fix this, open the table properties in the layout and **reduce the font size** until the full table fits.  
```


5. Adjust the legend
- In the layout, click on the **Legend** item.
- In the **Item Properties** panel:
  - Uncheck **Auto update**
  - Scroll to **Legend items** and remove all entries (🗑️)
  - Add the following relevant layers:
    - `example_Harald_2025_Track`
    - `cyclone_harald_buffer`
    - `Harald_Exposed_Population`
  - When selecting layers, check **Only visible layers**
  - Rename legend entries to match layout naming
    - `example_Harald_2025_Track` ->
     ```
     Cyclone Harald Track
     ```
    - `cyclone_harald_buffer`->
     ```
     Cyclone Harald 200 km Buffer
     ```
    - `Harald_Exposed_Population`->
     ```
     Number of exposed peopel
     ```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_adjust_map_making_Legend.mp4"></video>

6. **Update Logos and Icons**  
- The logos that need to be added to the map are represented by the red **X**.  
- Click on the image in the **Item List**.  
- Click on the three dots ![](/fig/Three_points.png) next to the file path.  
- Browse to the folder `logos_pictures` and select the correct logo file.  

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_making_update_logos.mp4"></video>


7. Review and update layout text elements
- Make sure all text elements are up to date, especially:
  - **Map title**
  - **Cyclone name and date**
  - **Author/Organization** (optional)
- Adjust font size or alignment if necessary

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_mak_making_adjust_title.mp4"></video>

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
The map now clearly displays the exposed population within the affected districts The original storm track line — used as input data — is highlighted, as well as the buffered impact area, which serves as a proxy for identifying exposed districts.

On the right-hand side of the map, a list shows all exposed districts, including data on total population and exposed population. The districts (Admin 2) are organized under their corresponding regions (Admin 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map_example.png
---
width: 1000px
name: 
align: center
---
```