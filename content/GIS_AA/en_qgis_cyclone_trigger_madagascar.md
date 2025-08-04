# QGIS Trigger Workflow for Madagascar 

<!-- Maybe have a final look over introduction and all the official stuff which should be included in the documentation -->

The QGIS workflow presented in this article was developed in the framework of the Anticipatory-Action (AA) Project of the Croix-Rouge Malagasy (CRM), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow is almost fully automated through a QGIS model, requiring no manual intervention. The chapter Automated Trigger Workflow outlines the process and its practical implementation. Each step included in the model is explained in detail to provide a complete understanding of the workflow and how the analysis was carried out.

## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In AA, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/06-develop-a-trigger-system/)).

## Trigger Statement

**Pre-Activation Trigger:** at least one of the meteorological forecasts from Meteo Madagascar, RMSC La Reunion, or ECMWF projects a greater than 50% likelihood of landfall by a tropical cyclone of tropical storm strength or higher within the next 7 days.

**Activation Trigger:** if the Meteo Madagascar (DGM) forecast indicates landfall of a tropical cyclone with wind speeds in excess of 118 km/h within the next 48-72 hours.

# Downloading the report

<!-- This section will include information on how to download the final report as soon as its published -->

# Functionality of the Trigger Workflow

The Trigger Process concept is displayed in the figure below.

```{figure} /fig/MAD_Trigger_concept.png
---
width: 1000px
name: fig-trigger-concept
align: center
---
```

The entire trigger workflow will be run in a QGIS model, which automates the spatial analysis for assessing the impact of tropical cyclones. It integrates cyclone storm track data with administrative boundaries, population data, infrastructure, and service locations to identify and quantify exposed areas and resources. 

## Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be static in the near term, and variable data which describe the datasets that will be checked for triggering on a regular basis depending on the occurrence of anticipated cyclone events. 

### Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Descriptions |
| ----- | --- | --- |
| Administrative Boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | The administrative boundaries on level 0-4 for Madagascar can be accessed via HDX provided by OCHA. For this trigger mechanism we provide the administrative boundaries on level 1 (regional level) and 2 (district level) as a shapefile. |
| POI counts | [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | The POI data (education facilities and health sites) is downloaded using the HOT Export Tool based on OpenStreetMap data. |
| CRM Warehouses | Croix-Rouge Malagasy |  |
| Population Counts | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | The worldpop dataset in raster format provides the estimated total number of people per grid-cell for the year 2020. We will be working with the Constrained Individual countries 2020 dataset at a resolution of 100m. |
| Buildings Counts | [Global ML Building Footprints](https://gee-community-catalog.org/projects/msbuildings/) | The building counts dataset in raster format counts the number of buildings per 100m grid cell. The workflow on how this dataset was created can be found on [GitLab](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |
| Land Cover | [ Copernicus Land Cover](https://land.copernicus.eu/en/products/global-dynamic-land-cover/copernicus-global-land-service-land-cover-100m-collection-3-epoch-2019-globe) | The land cover dataset in raster format provides an overview over the dominant land cover type at a resolution of 100m. The workflow on how this dataset was downloaded can be found on [GitLab](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |

:::{admonition} Master Raster
:class: note

The three raster datasets are combined into a **Master Raster** — a multi-band raster layer with a spatial resolution of 100 meters. This composite layer includes the following information across three channels:
1. Population counts per grid cell from Worldpop constrained (2020)
2. Building counts per grid cell derived from ML Building Footprints (2021)
3. Land Cover type per grid cell derived from Copernicus Land Cover (2019)

:::

### Monitoring Data

```{admonition} Attention
:class: attention

The forecast information will be sourced from DGM (Météo Madagascar), which will provide tropical cyclone track data for the trigger workflow.
```

For an analysis of past events, data provided by NOAA (National Centers for Environmental Information) can be used. The cyclone storm tracks are provided within the [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) project. It is the most complete global collection of tropical cyclones available and merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset. IBTrACS was developed collaboratively with all the World Meteorological Organization (WMO) Regional Specialized Meteorological Centres, as well as other organizations and individuals from around the world.

:::{admonition} Cyclone tracks
:class: hint

Tropical cyclone track data is available in various subsets, depending on the temporal scale of interest. Regional subsets can also be generated, with data for the **South Indian Ocean** being particularly relevant for this trigger mechanism.

:::

# Automated Trigger Workflow

As explained at the start of this chapter the developed trigger workflow is done automatically by a QGIS model. In this chapter we will explain its functionality and in a subsequent step it is explained how to run the automated model.

## Functionality of the model

<!-- Have a final look over this section to see if all the important information is covered -->

The following key processing steps are run inside the model:

1. Cyclone Buffering & Impact Area Extraction
    * The input cyclone track is buffered to create an estimated zone of impact. The buffer is dissolved to generate a single polygon representing the exposed cyclone area. This layer serves as the base for subsequent exposure calculations.

2. Exposed Administrative Units
    * The buffered cyclone area is intersected with district (Admin 2) boundaries to extract the exposed districts. These are further linked with regions (Admin 1) using the region (Admin 1) names attribute to structure exposed districts by region. This hierarchy is used for reporting and map layout purposes.

3. Population Impact
    * The model uses the population raster to calculate zonal statistics over the exposed districts. This determines the total population per district and the exposed population, which is then exported to a table.

4. Infrastructure Impact
    * The cyclone buffer is intersected with:
        * Buildings to extract exposed buildings.
        * Health sites and education facilities layers to extract and summarize exposed points of interest.
    These datasets are combined into a table, summarizing exposed infrastructure.

5. Warehouse Accessibility
    * Warehouses are filtered based on proximity to exposed regions. The model uses road data and spatial filters to determine accessible warehouses relevant to the response.

## How to run the model

The [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner, while ensuring reproducibility. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.


## Step 1: Explanation of the folder structure


```{figure} /fig/MAD_Trigger_workflow_Step1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ This step outlines the recommended folder structure to simplify the analysis and ensure consistent, reproducible results. 

__Tool:__ No special tools or programs are needed

``````{list-table}
:header-rows: 1
:widths: 10 25

* - Instruction
  - Folder Structure
* - 1. Open the folder “AA_Cyclone_Monitoring_Trigger_MAD".
    2. Input data is located in the folder "fixed_input_data".
    3. The QGIS model can be found in the "trigger_model" folder.
    4. Resources for styling and map creation are located in:
        - layer_styles – predefined layer symbology
        - logos_pictures – logos and visual elements
        - map_templates – templates for final map layouts
        - example_map_results – example outputs for orientation
        - Save your own results in the "map_outputs" folder.
    5. To start the process, open the QGIS project file "AA_Cyclone_Monitoring_Trigger_MAD.qgz" by double-clicking it. This will launch the full analysis workflow.

  -
    ```{figure} /fig/MAD_trigger_Folder_Structure_MAD_Trigger.png
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````


## Step 2: Open the project in QGIS and load the model in the QGIS Model Designer

```{figure} /fig/MAD_Trigger_workflow_Step2.png
---
width: 1000px
name: 
align: center
---
```

In this step we will open our Trigger project in QGIS and load the QGIS model which will automatically run the analysis for us.

1. Open the file `AA_Cyclone_Monitoring_Trigger_MAD.qgz` by double clicking it.
2. The QGIS project will open with lots of data pre-loaded. This data is required for running the QGIS model and create some output maps.

The data will be structured into five groups:

```{figure} /fig/MAD_trigger_QGIS_project_structure.PNG
---
width: 500px
name: 
align: center
---
```

**Group 1: Fixed_Input_data**

This group contains all the **fixed input data** required to successfully run the model. These datasets remain constant and do not change between events. The only additional input needed is the **storm track** for the event under investigation, which should be added **before** this data group in the layer panel.

:::{attention}

Always ensure you are using the **most up-to-date storm track** for the event being analyzed. To add the layer, simply drag and drop it into the Layers panel, placing it directly above the **Fixed_Input_data** group for clarity.

For better data management, give the storm track a descriptive name, such as `storm_track_eventname_year` (e.g. storm_track_freddy_2023). This naming convention helps keep your workspace organized and ensures the correct data is used during the analysis.

:::

**Group 2: Model_outputs**

This group is used to organize all **output layers generated by the model** after it has been run. You can review the outputs here and identify which layers are relevant for specific maps. Once identified, move them to the appropriate map group for visualization and layout.

**Group 3: Map_Cyclone_Impact_Overview**

This group includes all the layers required to create the **Cyclone Impact Overview Map** (shown below). The storm track and region (Admin1) boundaries (`Admin1_Impact_Overview_Map`) are pre-loaded to help you get started quickly.
Make sure you're working with the **correct and updated storm track** for the event under investigation.

```{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
```

**Group 4: Map_Cyclone_Impact_Assessment**

This group contains all the necessary layers to generate **detailed impact assessment maps**. As with the overview map, both the storm track and region (Admin1) boundaries are pre-loaded.
Ensure you're using the correct event data to maintain consistency and accuracy in the assessment. In this section we can create 5 different maps for different impacts:
- exposed population
- exposed buildings
- exposed education facilities
- exposed health sites
- exposed agricultural land cover

The final map outputs will look like the following.

```{figure} /fig/MAD_Trigger_Impact_Population_Map.png
---
width: 1000px
name: 
align: center
---
```

**Group 5: CRM_Warehouse_Isochrones**

This group includes isochrones for all warehouses, calculated for time intervals up to 24 hours. These layers are useful for assessing accessibility of locations in emergency response planning.

Now we continue working with the model:
1. Now open the QGIS Model Designer. The tool can be accessed under `Processing` -> `Model Designer`
2. In the upper panel click `Model` -> `Open Model` and navigate to your folder "AA_Cyclone_Monitoring_Trigger_MAD/trigger_model", mark the "Cyclones_EAP_MAD_Trigger.model3" file and click on `Open`. The model will open and you will see yellow, white, green and grey boxes.


| Box | Significance | Description |
| ----- | --- | --- |
|Yellow| Model Input | Definition of the input data for the model the model will perform on. |
|White| Algorithms | Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering. |
|Green| Model Output| The results created by the model (Output layers) are automatically added to your layers panel in your QGIS project interface. |
|Grey| Comments| The boxes are used to further explain the specific processes. |

<!-- Do we need a video here? -->

## Step 3: Run the model

```{figure} /fig/MAD_Trigger_workflow_Step3.png
---
width: 1000px
name: 
align: center
---
```

__Model Input & Output__

```{Attention}  
In the dropdown list, only layers that are currently loaded in your QGIS Project will be displayed.
```

For each of these mandatory inputs, you click on the dropdown arrow and choose the respective file.

1. In the upper panel click on `Model` -> `Run Model`. A new window will open where you need to define the model input and output.
2. The model needs the following 7 input layers:
    1. ADM1 = `mdg_admbnda_adm1_BNGRC_OCHA_20181031`
    2. ADM2 & Risk = `mdg_adm2_risk - mad_adm2_risk`
    3. CRM_warehouse_isochrones_250709_ALL = `crm_warehouse_isochrones_250709_ALL`
    4. CRM warehouses = `20240108_MAD_CRM_Warehouses_updated`
    5. Cyclone_monitoring_data = `cyclone track of the current event` 
    6. Madagascar_Health_and_Education_Facilities = `Madagascar_Health_and_Education_Facilities`
    7. Master Raster = `MAD_pop_constrained_buildings_landcover`
    8. Max_traveltime in 2 hour intervals (lead time) = `enter a number between 2 and 24`

<!-- Names should be the final ones. They are given after the last model from Elias -->

3. Further down, you have to specify where to save the outputs: 

    1. `Exposed_Cyclone_Area`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_cyclone_area
    ```

    2. `Exposed_Education_Facilities`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_education_facilities_points
    ```

    3. `Exposed_Health_Facilities`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_health_facilities_points
    ```
    4. `Exposed_Regions`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_regions
    ```

    5. `Relevant_Warehouses`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    relevant_warehouses
    ```

    6. `Exposed_Districts`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_districts
    ```

    7. `Exposed_Population`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_population
    ```

    8. `Exposed_Buildings`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_buildings
    ```

    9. `Exposed_Agricultural_Landcover`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_agricultural_landcover
    ```
    10. `Exposed_Education_Facilities_Points`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_health_education
    ```
    11. `Exposed_Health_Facilities_Points`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    exposed_health_facilities
    ```

4. Click `Run` to execute the model. The output result layers will be automatically added to the main QGIS window upon completion. Once the process has finished, you can close the `Model Designer` window. Make sure to add all newly created layers to the **Model_outputs** group in QGIS. Afterwards, relocate them to their appropriate final groups for further processing.

<!-- Do we need a video here to show how to run the model?

```{dropdown} Video: Input and output Model
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/model_input_output.mp4"></video>
```
-->

```{figure} /fig/MAD_Trigger_model_inputs.PNG
---
width: 500px
name: 
align: center
---
```

## Step 4: Visualization and Styling of the Model Outputs and creating the Print Map

<!-- Is a video necessary for this chapter? -->

:::{admonition} Output maps
:class: note

We will generate two different types of output maps to support the analysis:
- Map 1 will provide an cyclone impact overview of the **affected districts, the extent of the cyclone event, and the locations of relevant warehouses**.
- Map 2 will focus on the impact to infrastructure and population. We will create 5 different impact maps displaying the following information:
    - **exposed population**
    - **exposed buildings**
    - **exposed health sites**
    - **exposed education facilities**
    - **exposed agricultural landcover**
:::

Additionally, a map showing the **warehouse isochrones** for all 13 warehouses will be provided. The map and the map template can be found in the **warehouse_isochrone_matrix** folder.

We will do the following steps in this section:

```{figure} /fig/MAD_Trigger_workflow_Step4a.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Definition of how features are represented visually on the map.

__Tool:__ [Symbology tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I.html#symbology-for-vector-data)

```{figure} /fig/MAD_Trigger_workflow_Step4b.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Viualization of the map features in a printable map layout

__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

### Map 1: Cyclone Impact Overview: Affected Districts, Event Extent, and Warehouse Locations

Layers needed for this map:
- `Relevant_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Admin1_Impact_Overview_Map` already loaded and styled in QGIS 
- `Exposed_Districts`

The layers should be arranged as shown in the figure below.

```{figure} /fig/MAD_Trigger_layer_order_overview_map.PNG
---
width: 300px
name: 
align: center
---
```

#### Styling of the layers

1. Right click on the exposed_districts layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” folder and select the file __“exposed_districts_style.qml”__.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | Comment
| ----- | --- | --- |
|`Admin1_Impact_Overview_Map`| `adm1_style.qml` | pre-loaded |
|`relevant_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| pre-loaded |

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

#### Making the Print Layout
For easier visualization, we have created these [map templates](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) for presenting the results of the trigger analysis. These templates serve as a base for your own visualizations and are available in the following directory: `AA_Cyclone_Monitoring_Trigger_MAD/map_templates`. You can customize the templates to suit your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).


1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview`.
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "Feddy_2023_Overview".
3. Right click on the white canvas and select `Page Properties`. In the bottom right section of the print layout, you'll see the page specifications. Set the Size to `A3` and the Orientation to `Landscape` to ensure that the map template fits correctly within the page layout.
4. Go to the **AA_Cyclone_Monitoring_Trigger_MAD and then map_templates** folder and drag and drop the file `cyclone_impact_overview_map_template.qpt` into the print layout.
5. **Update the Map Title**  
   - Click on the title text element at the top of the map.
   - In the `Item Properties` panel, edit the **Main Label** text to match your event, e.g. `Cyclone Harald – 2025`.
   - Adjust font size or alignment as needed.

6. **Update the Attribute Table on the Right-Hand Side of the Map**  
   To update the attribute table displaying the exposed districts:
   - In the `Item Properties` panel, select the `Exposed_Districts` layer and click **Refresh Table Data**
   - Click on `Attributes...`
   - In the **Columns** section:
     - Click `Clear`
     - ➕ Add the columns: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE`
   - In the **Sorting** section:
     - ➕ Add `ADM1_EN` and set the sort order to `Ascending`
   - Click **OK** to apply

```{note}
💡 If too many districts are affected, the attribute table might not fit the page. Reduce the font size in the table’s item properties to make everything visible — but be aware that this may reduce readability.
```
6. Adjust the Legend by clicking on it in the map layout and have a look at the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend by clicking on each item and then the red minus icon
        * In the pop-up, check **Only show visible layers** to help you find the correct ones
        * To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name  
    * ➕ Add the following layers by clicking the green plus:
        * `Admin1_Impact_Overview_Map` → rename to  
      ```md
      Regions
      ```
        * `exposed_districts` → rename to  
      ```md
      Exposed Districts
      ```
        * `Cyclone Track` → rename to  
      ```md
      Projected Cyclone Track
      ```
        * `Exposed_Cyclone_Area` → rename to  
      ```md
      Exposed Cyclone Area
      ```
        * `relevant_warehouses` → rename to  
      ```md
      Relevant Warehouses
      ```
        * `Background Map: OpenStreetMap` → rename to  
      ```md
      Background Map:
      OpenStreetMap
      ```
 
<!-- Maybe add a video on how the Print Layout is created 

```{dropdown} Video: Making print map
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
```

-->

```{Attention}
Checklist for final map output:
- Map Information: Review and update all text elements as needed.
- Legend: Remove unnecessary items and rename layers with clear, meaningful descriptions.
- Exposed Districts: Include only districts that are actually impacted in your "List of Exposed Districts". Update them according to the event.
```

```{dropdown} Your final output should look like this after styling the layer
You will now see the exposed districts and the locations of relevant warehouses clearly displayed on the map. Additionally, the original storm track line — used as input data — is highlighted, along with the buffered impact area, which serves as a proxy for identifying exposed districts.

```{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
```

### Map 2: Impact Assessment: Affected Population and Critical Infrastructure

Layers needed for this map:
- `Relevant_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Exposed_Population`
- `Admin1_Impact_Assessment_Map` already loaded and style in QGIS

```{figure} /fig/MAD_Trigger_layer_order_impact_map.PNG
---
width: 300px
name: 
align: center
---
```

:::{attention}

If you already created Map 1 earlier in the process, you can reuse the first four layers with their existing styling for Map 2—and vice versa. This ensures consistency across both maps and saves time by avoiding duplicate styling efforts.

:::

#### Styling of the layers

1. Right click on the "exposed_population" layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” folder and select the file __“exposed_population_style.qml”__ style layer.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | Comment
| ----- | --- | --- |
|`Admin1_Impact_Assessment_Map`| `adm1_style.qml` | pre-loaded |
|`relevant_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| loaded by user |

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

:::{admonition} Other Impact Assessment Maps
:class: hint

The layer styling used in Map 2 can be applied to the following additional variables available in the model outputs:

| Layer name | Style | Comment
| ----- | --- | --- |
|`exposed_population`|`exposed_population_style.qml`|model output|
|`exposed_building`|`exposed_building_style.qml`|model output|
|`exposed_health_facilities`| `exposed_health_facilities_style.qml` | model output |
|`exposed_education_facilities`| `exposed_education_facilities_style.qml` | model output |
|`exposed_agricultural_landcover`| `exposed_agriculture_landcover_style.qml` | model output |
|`exposed_health_facilities_points`| `points_exposed_health_facilities_style.qml` | model output |
|`exposed_education_facilities_points`| `points_exposed_education_facilities_style.qml` | model output |
|`relevant_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| loaded by user |

:::

#### Making the Print Layout
```{Attention}
The same workflow applies to all five impact variables: population, buildings, education facilities, health sites, and agricultural landcover. The following example demonstrates the process for creating the population impact map. The remaining maps can be generated by following the same steps.
```

1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview`.
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "Feddy_2023_Impact_Population".
3. Right click on the white canvas and select `Page Properties`. In the bottom right section of the print layout, you'll see the page specifications. Set the Size to `A3` and the Orientation to `Landscape` to ensure that the map template fits correctly within the page layout.
4. Go to the **AA_Cyclone_Monitoring_Trigger_MAD and then map_templates** folder and drag and drop the file `cyclone_impact_population_map_template.qpt` into the print layout.
5. **Update the Map Title**  
   - Click on the title text element at the top of the map.
   - In the `Item Properties` panel, edit the **Main Label** text to match your event, e.g. `Cyclone Harald – 2025`.
   - Adjust font size or alignment as needed.
6. **Update the Attribute Table on the Right-Hand Side of the Map**  
   To update the attribute table displaying the exposed districts:
   - In the `Item Properties` panel, select the `exposed_population`**Or any other layer you are working with** layer and click **Refresh Table Data**
   - Click on `Attributes...`
   - In the **Columns** section:
     - Click `Clear`
     - ➕ Add the columns: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE` and `exposed_population`**Or any other layer you are working with**
   - In the **Sorting** section:
     - ➕ Add `ADM1_EN` and set the sort order to `Ascending`
   - Click **OK** to apply

```{note}
If too many districts are affected, the attribute table might not fit the page. Reduce the font size in the table’s item properties to make everything visible — but be aware that this may reduce readability.
```
7. Adjust the Legend by clicking on it in the map layout and have a look at the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend by clicking on each item and then the red minus icon
        * In the pop-up, check **Only show visible layers** to help you find the correct ones
        * To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name  
    * ➕ Add the following layers by clicking the green plus:
   - In the pop-up, check **Only show visible layers** to help you find the correct ones
   - 💡 To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name
   - Ensure all legend entries use **clear and meaningful labels**
::::{tab-set}

:::{tab-item} Exposed Population
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_population` → rename to  
```md
Exposed Population
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Buildings 
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_building` → rename to  
```md
Exposed Buildings
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Facilities
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_health_facilities` → rename to  
```md
Exposed Health Facilities
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Education Facilities
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_education_facilities` → rename to  
```md
Exposed Education Facilities
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Agriculture in Hectare
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_agricultural_landcover` → rename to  
```md
Exposed Agriculture in Hectare
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Facilities Points
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_health_facilities_points` → rename to  
```md
Exposed Health Facilities Points
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Education Points
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_education_facilities_points` → rename to  
```md
Exposed Health Education Points
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

::::




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

## Step 5: Exporting the Map 

```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order to print it as a pdf or format of your choice.


__Tool:__ [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

When you have finished the design of you map you can export it as pdf or image file in different data formats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. For the specific impact assessment change the name to something like **MDG_Trigger_Impact_Population_Map_Freddy_2023**.
3. Click on `Save`
4. The window `Image Export Options` will appear. Click `Save`.
Now the image can be found in the result folder.


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. For the specific impact assessment change the name to something like **MDG_Trigger_Impact_Population_Map_Freddy_2023**.
3. Click on `Save`
4. The window `PDF Export Options` will appear. For the best results, select the `lossless` image compression.
5. Click `Save`.
Now the image can be found in the result folder.

<!-- Maybe add a video. Might not be necessary

```{dropdown} Video: Export image and PDF
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_trigger_export_image_pdf.mp4"></video>
```
-->

```{figure} /fig/MAD_Trigger_Impact_Buildings_Map.png
---
width: 1000px
name: Impact of Cyclone Event Freddy 2023
align: center
---
```

# Historical Analysis of Cyclone Impacts

To run the full trigger process using historical cyclone track data, you can assess the impacts of past events and gain insights into what occurred in similar scenarios. The storm track data is available from the **International Best Track Archive for Climate Stewardship (IBTrACS)**. Instructions on how to access this data are provided in the following section.

## Download of historical storm track data

The **International Best Track Archive for Climate Stewardship (IBTrACS)** v04r01 data is updated three times a week (usually on Sunday, Tuesday, and Thursday), and could be updated more frequently to address specific needs and use cases. The latest updates in the correct file format can be found on their [website](https://www.ncei.noaa.gov/products/international-best-track-archive):

1. Look for the `Access Methods` section and click on `Shapefiles`. The link leads to the following [website](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/shapefile/) which can also be seen in the figure below.
2. Since we don’t need storm track data for the entire world or the full archive, we will download only a relevant subset. Locate for the file named `IBTrACS.ACTIVE.list.v04r01.lines.zip` and click on it - the download should begin automatically.
3. Unzip the file and open it in QGIS.
4. Open the attribute table and delete all the storm tracks that are not relevant for this analysis. Safe the updated storm track file.

:::{note}

The storm track subset `IBTrACS.ACTIVE.list.v04r01.lines.zip` contains all **storms active in the last 7 days**. If more comprehensive data is needed, it is advisable to download a subset by basin. For Madagascar, the most relevant region is **SI – South Indian**, which includes our Area of Interest. This dataset can be downloaded from the same website under the name `IBTrACS.SI.list.v04r01.lines.zip`. 

:::


```{figure} /fig/MAD_Trigger_stromtrack_download.PNG
---
width: 1000px
name: MAD_Trigger_stromtrack_download
align: center
---
```

