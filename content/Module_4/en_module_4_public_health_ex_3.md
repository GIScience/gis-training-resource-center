# Exercise 3: Visualising Health Infrastructure, Population and Measles Incidence in QGIS

## Background

Now that you have prepared and enriched your datasets in Exercises 1 and 2, it is time to create clear, visually compelling maps for decision-makers.
These maps will help the Ministry of Health and partners understand:

Which health facilities have cold-chain capacity

Where population is concentrated

Which districts have the highest measles incidence rate

In this exercise, you will create two publication-ready maps using the QGIS Print Layout Composer.

## Objectives

By the end of this exercise, you will be able to:

- Configure map symbology for clear visualisation
- Create two separate map layouts using the Print Layout
- Add essential map elements (title, legend, scale bar, north arrow, logos)
- Export maps as high-quality PDF or PNG outputs

## Available Data

From the previous exercises: 

| Dataset                                                               | Description                                                  |
| --------------------------------------------------------------------- | ------------------------------------------------------------ |
| `Healthsites_points_capacities`                                       | Health facilities enriched with cold-chain and capacity info |
| `tcd_admbnda_adm2_20250212_AB` (adm2_pop / adm2_population_incidence) | Adm2 boundaries enriched with population & measles incidence |
| `OpenStreetMap basemap (XYZ tiles)`                                   | Background context                                           |
| `tcd_admbnda_adm1_20250212_AB`                                        | Administrative reference boundaries                          |

## Tasks

### Task 1: Visualise the Health Facilities Capacities

1. In the *Layers Panel*, <kbd>right-click</kbd> on `Healthsites_points_capacities` → `Properties`.
2. Navigate to the **Symbology** tab.
3. Change the style from `Single Symbol` to `Categorized`.
4. Under **Value**, select `cold_chain`.
5. Click `Classify`.
6. Adjust the symbols (e.g., blue for “yes”, grey for “no”).
7. Click `Apply`.

### Task 2: Prepare the Measles Incidence Layer


1. <kbd>Right-click</kbd> on the `adm2_incidence` layer → `Properties`.
2. Open the **Symbology** tab.
3. Set:
   - **Style:** Graduated  
   - **Column:** `incidence_rate`  
   - **Mode:** Quantile or Natural Breaks
4. Choose a sequential or red–yellow colour ramp.
5. Click `Classify` → `Apply`.

### Task 3: Create a Map in the Print Layout Composer

:::{admonition}
:class: tip

The print layout composer is a separate QGIS window where you can design a printable or publishable map by adding map canvases, legend items, text boxes, attribute tables, etc. to create a finished map product.  

:::

1. First, we need to create a new print layout:
    - Top menu: `Project` → `New Print Layout…` 
    - Name it: **Health_Facilities_Capacity_Map**
    - A new window will open, this is the [print layout composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html). Take the time to  [understand the interface and the different tools](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_understanding_print_layout.html).

2. Adding a new map frame:
    - Select `Add Map` ![](/fig/30.30.2_print_layout_insert_map_icon.png) from the toolbar on the left.
    - Draw a rectangle on the blank page canvas.
    - Adjust the extent (pan and zoom) using the `Move item content` ![](/fig/30.30.2_print_layout_move_content_icon.png). 

    