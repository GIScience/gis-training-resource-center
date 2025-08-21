# QGIS Trigger Workflow for Madagascar 

<!-- Maybe have a final look over introduction and all the official stuff which should be included in the documentation -->

::::{admonition} French Translation 
:class: tip

The french version of this page can be found [here](/content/GIS_AA/fr_qgis_cyclone_trigger_madagascar.md).

La version française de cet article se trouve [ici](/content/GIS_AA/fr_qgis_cyclone_trigger_madagascar.md).

:::{card}
:class-card: sd-text-center sd-border-1
:link: https://giscience.github.io/gis-training-resource-center/content/GIS_AA/fr_qgis_cyclone_trigger_madagascar.html
Version française
:::

::::

The QGIS workflow presented in this article was developed in the framework of the Anticipatory-Action (AA) Project of the Croix-Rouge Malagasy (CRM), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow is almost fully automated through a QGIS model, requiring no manual intervention. The chapterFunctionality of the workflow outlines the process and its practical implementation. Each step included in the model is explained in detail to provide a complete understanding of the workflow and how the analysis was carried out.

## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In AA, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/06-develop-a-trigger-system/)).

## Trigger Statement

**Pre-Activation Trigger:** at least one of the meteorological forecasts from Météo Madagascar, RMSC La Reunion, or ECMWF projects a greater than 50% likelihood of landfall by a tropical cyclone of tropical storm strength or higher within the next 7 days.

**Activation Trigger:** if the Meteo Madagascar (DGM) forecast indicates landfall of a tropical cyclone with wind speeds in excess of 118 km/h within the next 48-72 hours.

# Downloading the report

<!-- This section will include information on how to download the final report as soon as its published -->

# Functionality of the Workflow

The Trigger Process concept is displayed in the figure below.

```{figure} /fig/MAD_model_concept.png
---
width: 1000px
name: fig-model-concept
align: center
---
```

The provided QGIS project contains the necessary layers and a QGIS model file to perform an assessment of the potential impact of the predicted cyclone event. The analysis workflow will be run in the QGIS model, which automates the steps for assessing the impact of a tropical cyclone event.  It integrates cyclone storm track data with administrative boundaries, population data, infrastructure, and service locations to identify and quantify exposed areas and resources. 
Based on the cyclone forecast by Météo Madagascar, the model calculates the area likely to be  exposed to the cyclone, the potentially exposed population, number of exposed buildings, exposed agricultural land, and potentially exposed health and education facilities. 

Additionally, the QGIS file includes layers with the CRM warehouses and the areas they can service, allowing for a quick accessibilty assessement. The provided folder also contains map templates and style files to generate map reports based on the model calculations. 

The documentation is separated into two parts. The first part covers the spatial analysis using the automated QGIS model. The second part documents how to create the map reports using the map templates and style files. 

<!--Insert image of report?-->

:::{attention}

The QGIS project and QGIS model have been created using QGIS version 3.40.9 (LTR) Bratislava. To ensure that the model is working correctly, do not use older QGIS versions. 

:::

## Available Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be static in the near term, and variable data which describe the datasets that will be checked for triggering on a regular basis depending on the occurrence of anticipated cyclone events. 

::::{admonition} Download the data and project files
:class: note

The QGIS project file, the model, and the datasets required for the model can be downloaded from HeiGITs Gitlab here:

:::{card}
:class-card: sd-text-center sd-rounded-2 sd-border-1
:link: https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar/-/tree/68e58a254f12406101a398e895436ccc198f8938/AA_Cyclone_Monitoring_Trigger_MAD
__Download the project.__
:::

::::


### Fixed Data

By fixed data we mean datasets that are needed to create the map reports, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Descriptions |
| ----- | --- | --- |
| Administrative Boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | The administrative boundaries on level 0-4 for Madagascar can be accessed via HDX provided by OCHA. For this trigger mechanism we provide the administrative boundaries on level 1 (regional level) and 2 (district level) as a shapefile. |
| POI counts | [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | The POI data (education facilities and health sites) is downloaded using the HOT Export Tool based on OpenStreetMap data. |
| CRM Warehouses | Croix-Rouge Malagasy | This layer contains points representing the locations of the CRM warehouses  |
| CRM Warehouse Isochrones | HeiGIT | Using the [Global Friction Surface](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_friction_surface_2019#bands), we calculated the area which can be reached within a specific amount of time from a given warehouse by car.  | 
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

## Estimating the impact of the cyclone using the QGIS model

As explained at the start of this chapter the developed trigger workflow is done automatically by a QGIS model. In this chapter we will explain its functionality and in a subsequent step it is explained how to run the automated model. 

### Functionality of the model

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

<!---5. Warehouse Accessibility
    * Warehouses are filtered based on proximity to exposed regions. The model uses road data and spatial filters to determine accessible warehouses relevant to the response.
-->

### How to run the model

The [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner, while ensuring reproducibility. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.


### Step 1: Explanation of the folder structure


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


### Step 2: Open the project in QGIS and load the model in the QGIS Model Designer

```{figure} /fig/MAD_Trigger_workflow_Step2.png
---
width: 1000px
name: 
align: center
---
```

In this step we will open our Trigger project in QGIS and load the QGIS model which will automatically run the analysis for us.

1. Open the file `AA_Cyclone_Monitoring_Trigger_MAD.qgz` by double clicking on it.
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
This map will be created using the layers in group 3.
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
This map will be created using the layers in group 4
```

<!--EDIT: ADD THE CORRECT PICTURE FOR THIS MAP-->

**Group 5: CRM_Warehouse_Isochrones**

This group includes isochrones for all warehouses, calculated for time intervals up to 24 hours. These layers are useful for assessing accessibility of locations in emergency response planning.
This group is used to create the CRM warehouse accessibility matrix map. 
It is also possible to add a specific warehouse isochrone to one of the previous maps. We will cover this further below. 


----

#### Opening the model in QGIS

Let's open the QGIS model:
1. In the tob bar of your QGIS window, navigate to `Processing` -> `Model Designer`. A new window will open. This is the model designer.
2. In the upper panel click `Model` -> `Open Model` and navigate to your folder "AA_Cyclone_Monitoring_Trigger_MAD/trigger_model".
3. Select the "Cyclones_EAP_MAD_Trigger.model3" file and click on `Open`. The model will open and you will see yellow, white, green and grey boxes.

<!--ADD PICTURE
-->

:::{figure} /fig/AA/fr_qgis_3.44_opening_model_builder.png
---
width: 600 px
name: fr_qgis_ouvrir_modeleur
---
Opening the graphical modeler in QGIS 3.44
:::

| Box | Significance | Description |
| ----- | --- | --- |
|Yellow| Model Input | Definition of the input data for the model the model will perform on. |
|White| Algorithms | Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering. |
|Green| Model Output| The results created by the model (Output layers) are automatically added to your layers panel in your QGIS project interface. |
|Grey| Comments| The boxes are used to further explain the specific processes. |

<!-- Do we need a video here? -->

### Step 3: Run the model

```{figure} /fig/MAD_Trigger_workflow_Step3.png
---
width: 1000px
name: 
align: center
---
```

__Model Inputs & Outputs__


1. A QGIS model can be run by navigating to the top bar > `Model` (`Modèle`) > `Run Model` (`Exécuter le modèle`) or by clicking on the ![](/fig/Module_7/qgis_3.44_run_model.png) icon. 


2. A new window will open. Here you need to define the model's inputs and outputs. For each of these mandatory inputs, you click on the dropdown arrow and choose the respective file.

:::{figure} /fig/AA/fr_qgis_3.44_executer_modele.png
---
width: 600 px
name: fr_qgis_executer_modele
---
Selecting the inputs and defining the outputs before running the model.
:::

::::{margin}
:::{note}  
In the dropdown list, only layers that are currently loaded in your QGIS Project will be displayed.
:::
::::

3. To run the model, select the following 5 input layers:
    1. ADM1 = `mdg_admbnda_adm1_BNGRC_OCHA_20181031`
    2. ADM2 & Risk = `mdg_adm2_risk - mad_adm2_risk`
    3. Cyclone_monitoring_data = `cyclone track of the current event` 
    4. Madagascar_Health_and_Education_Facilities = `Madagascar_Health_and_Education_Facilities`
    5. Master Raster = `MAD_pop_constrained_buildings_landcover`


<!-- Names should be the final ones. They are given after the last model from Elias -->

::::{margin}
:::{attention}
If you don't specify the location to save the output files, the outputs will be loaded as __temporary layers__ after running the model and __disappear even after saving the project file__.
:::
::::

3. Further down, you have to specify where to save the outputs. For each output, click on the three points ![](/fig/Three_points.png) > `Save to Geopackage` (`Enregistrer dans un Geopackage...`). A File explorer window will open. Navigate to the folder `.../AA_Cyclone_Monitoring_Trigger_MDG/model_outputs/` and give it the __name of the output layer and the date__ (YYYYMMDD). 
    1. `Exposed_Cyclone_Area_YYYYMMDD`, for example, `Exposed_Cyclone_Area_YYYYMMDD_20250805`
    2. One output is called `Spreadsheet_Exposed_District` for which the model will ouput a `.csv`-file. For this layer, choose `Save to file` (`Enregistrer vers un fichier...`), navigate to the folder `.../AA_Cyclone_Monitoring_Trigger_MDG/model_outputs/` and give it the name `Spreadsheet_Exposed_Districts_YYYYMMDD`
    3. `Exposed_Education_Facilities_points_YYYYMMDD`
    4. `Exposed_Health_Facilities_points_YYYYMMDD`
    5. `Exposed_Regions_YYYYMMDD`
    6. `Exposed_Districts_YYYYMMDD`
    7. `Exposed_Population_YYYYMMDD`
    8. `Exposed_Buildings_YYYYMMDD`
    9. `Exposed_Agricultural_Landcover_YYYYMMDD`
    10. `Exposed_Education_Facilities_YYYYMMDD`
    11. `Exposed_Health_Facilities_YYYYMMDD`


4. Once you have set the names and saving locations for the output layers, click `Run` to execute the model. The output result layers will be automatically added to the main QGIS window upon completion. Once the process has finished, you can close the `Model Designer` window. 



5. You will see new layers added to the map canvas and the layers panel (on the bottom left). Move the new layers to the group "Model_Outputs".

:::{figure} /fig/AA/mdg_aa_model_outputs_canvas.png
---
name: mdg_model_output_canvas
width: 700 px
---
:::


<!-- Do we need a video here to show how to run the model? -->

```{dropdown} Video: Input and output Model
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/model_input_output.mp4"></video>
```

:::{card}
Results
^^^
We have all the necessary layers to create the individual maps. The next section will cover how to use the predetermined and calculated layers to create the maps using the map templates and layer style files. 
:::

## Creating the map reports using the map templates

### Visualization and Styling of the Model Outputs and creating the Print Map

<!-- Is a video necessary for this chapter? -->

:::{admonition} Output maps
:class: note

We will generate three different types of output maps to support the analysis:
- Map 1 will provide an cyclone impact overview of the **affected districts, the extent of the cyclone event, and the locations of relevant warehouses**.
- Map 2 will focus on the impact to infrastructure and population. We will create 5 different impact maps displaying the following information:
    - **exposed population**
    - **exposed buildings**
    - **exposed health sites**
    - **exposed education facilities**
    - **exposed agricultural landcover**

Additionally, a map showing the **warehouse isochrones** for all 13 warehouses will be provided. The map and the map template can be found in the **warehouse_isochrone_matrix** folder.
:::

We will create the maps in two steps:
First, we will use the __[layer styling panel](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#styling-panel)__ and the __layer style files (.qml)__ to adjust the visualisation of the layers on the map canvas.

In a second step, we will use the __[print layout composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)__ to create printable maps with additional datatables. 

<!---

```{figure} /fig/MAD_Trigger_workflow_Step4a.png
---
width: 1000px
name: 
align: center
---
```

__Tool:__ [Symbology tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I.html#symbology-for-vector-data)

```{figure} /fig/MAD_Trigger_workflow_Step4b.png
---
width: 1000px
name: 
align: center
---
```


__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

### Map 1: Cyclone Impact Overview: Affected Districts, Event Extent, and Warehouse Locations

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::

Layers needed for this map:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Admin1_Impact_Overview_Map` already loaded and styled in QGIS 
- `Exposed_Districts`

__Right-click on each of the layers and select `Duplicate this layer`. Move the copy to the group "Map_Cyclone_Impact_Overview".__ 

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
|`CRM_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| pre-loaded |

6. The styling for the layer `CRM_warehouses` is not fixed yet. Right-click on the layer `CRM_warehouses` > `Properties` and navigate to the symbology tab.
  :::{figure} /fig/AA/mdg_aa_fix_warehouse_icon.png
  ---
  name: fix_warehouse_icon
  width: 550px
  ---
  :::
  * Select `Raster Image Marker` and then click on the three points ![](/fig/Three_points.png).
  * In the project folder, navigate to the subfolder called `logo_pictures`. Here you will find a png-file called "ngo-office". Select it and click `Open`.


<!--EDIT: Add that the picture location for the CRM warehouse icon needs to specified again. It is located in the logos_pictures folder.-->

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

#### Making the Print Layout

For easier visualization, we have created these [map templates](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) for presenting the results of the trigger analysis. These templates serve as a base for your own visualizations and are available in the following directory: `AA_Cyclone_Monitoring_Trigger_MAD/map_templates`. You can customize the templates to suit your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).


1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview` and the `OpenStreetMap` basemap.
2. Open a new print layout by clicking on `Project` -> `Layout Manager`. A small new window will appear. Here you can select an existing layout or create a new layout from a template. 
3. We want to create a new layout from a template. Click on the `Empty Layout` dropdown menu and select `Specific`. 
4. Below, click on the three dots ![](/fig/Three_points.png) and navigate to the folder `../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` and select the file with the name `cyclone_impact_overview_map_template`. Click `Open`, then `Create`. 
5. QGIS will ask you to name the new layout. Give it a name such as "Cyclone_Overview_Map_Freddy_2023". Click `OK`. A new window will open. This is the print layout composer. It should look similar to the figure below.

:::{figure} /fig/AA/overview_map_template.png
---
name: overview_map_template
width: 700 px
---
The print layout composer after opening the template file.
:::

The print layout will automatically load the map canvas. However, to finish the report, we need to adjust and update some of the elements on the print layout. For example, on the right side of the map, the attribute table is not displayed correctly, the legend seems to be wrong, and the logos of the CRM and HeiGIT are displayed as red crosses.

6. **Update the Map Title**  
   - Click on the title text element at the top of the map.
   - In the `Item Properties` panel, edit the **Main Label** text to match your event, e.g. `Cyclone Harald – 2025`.
   - Adjust font size or alignment as needed.



7. **Update the Attribute Table on the Right-Hand Side of the Map**  
:::{figure} /fig/AA/mdg_aa_map_1_update_attribute_table.png
---
name: mdg_aa_map_1_update_attribute_table
width: 600 px
---
:::
   - On the right side, there is a attribute table that did not fully load. We want to update the attribute table to display the exposed districts.
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

8. **Adjust the Legend**
    * Select the legend item, navigate to the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend by clicking on each item and then the red minus icon
        * In the pop-up, check **Only show visible layers** to help you find the correct ones
        * To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name  
    * ➕ Add the following layers by clicking the green plus:
        * `Admin1_Impact_Overview_Map`
        * `exposed_districts`
        * `Cyclone Track`
        * `Exposed_Cyclone_Area`
        * `CRM_warehouses`  
        * `OpenStreetMap`
      * Now, let's rename the layers in the legend. In the __Item properties__, below the list of the legend layers, there is a ![](/fig/AA/mdg_aa_edit_legend.png) `Edit selected item properties`-button. By clicking on it, you can edit the label of the icon in the legend. Rename the layers as follows:
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

9. Adjust the icons by clicking on the <Picture> field in the items list or on the red cross in the map template. 
  * In the Item Properties, correct the path to the CRM logo by clicking on the three dots ![](/fig/Three_points.png) and navigate to `\aa_madagascar\AA_Cyclone_Monitoring_Trigger_MAD\logos_pictures` and selecting the CRM logo file.
  * Repeat the process for the second missing image. This time, select the HeiGIT Logo


10. Below the logos, adjust the information in the text box by selecting the text box and navigating to the Item properties.

11. Finally, let's lock the layers and layer styles so that changes in the main QGIS window do not affect our print layout:
  * In the item list, select __Map 1__.
  * In the item properties, check the boxes for __lock layers__ and __lock styles for layers__. This will prevent the map to automatically when we make changes to the map canvas

```{figure} /fig/AA/mdg_aa_lock_layers.png
---
name: mdg_aa_lock_layers
width: 600 px
---
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

::::{dropdown} Your final output should look like this after styling the layer
You will now see the exposed districts and the locations of relevant warehouses clearly displayed on the map. Additionally, the original storm track line — used as input data — is highlighted, along with the buffered impact area, which serves as a proxy for identifying exposed districts.

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::
::::


#### Exporting the Map 

<!--Exporting the map should be done after each layout. If the maps are not locked, it will break the layouts and the work will have to be repeated-->


<!---
```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order to print it as a pdf or format of your choice.


__Tool:__ [Print Layout Composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

When you have finished the design of your map, you can export it as pdf or image file in different data formats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. 
3. Click on `Save`
4. The window `Image Export Options` will appear. Click `Save`.
Now the image can be found in the result folder.


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.
3. Click on `Save`.
4. The window `PDF Export Options` will appear. For the best results, select the `lossless` image compression.
5. Click `Save`.
Now the image can be found in the result folder.

### Map 2: Impact Assessment: Exposed Population and Critical Infrastructure

Layers needed for this map:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Exposed_Population`
- `Admin1_Impact_Assessment_Map` already loaded and style in QGIS

Right click on each layer > `Duplicate this layer` and move the copies to the group "Map_Cyclone_Impact_Assessment"

```{figure} /fig/MAD_Trigger_layer_order_impact_map.PNG
---
width: 300px
name: 
align: center
---
```

<!--Remove the comment as duplicating and loading the style ensures that previous map layouts are not broken. also add that you can fix layer styles and layers in the map items-->


#### Map 2: Styling of the layers

1. Deactivate all the layers except gor the group "Map_Cyclone_Impact_Assessment" and the OpenStreetMap Basemap.
2. Right click on the "exposed_population - copy" layer -> `Properties` -> `Symbology`
3. In the down left corner click on `Style` -> `Load Style`
4. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” folder and select the file __“exposed_population_style.qml”__ style layer.
5. Click `Open`. Then click on `Load Style`
6. Back in the “Layer Properties” window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | Comment
| ----- | --- | --- |
|`Admin1_Impact_Assessment_Map`| `adm1_style.qml` | pre-loaded |
|`CRM_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| loaded by user |

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

::::{admonition} Other Impact Assessment Maps
:class: hint

The documentation covers the exposed population impact assessment map. However, the model also estimates the exposed buildings, landcover, and health and education facilities. These variables can also be displayed on the map using the following style files. To keep the map easily understandable, use only one of the 


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
<!--Move this somewhere else where it is easier to understand OR add pictures to illustrate the different maps?-->
::::

#### Map 2: Making the Print Layout

```{tip}
The same workflow applies to all five impact variables: population, buildings, education facilities, health sites, and agricultural landcover. The following example demonstrates the process for creating the population impact map. The remaining maps can be generated by following the same steps.
```


1. Open a new print layout by clicking on `Project` -> `Layout Manager`. A small new window will appear. Here you can select an existing layout or create a new layout from a template. 
2. We want to create a new layout from a template. Click on the `Empty Layout` dropdown menu and select `Specific`. 
3. Below, click on the three dots ![](/fig/Three_points.png) and navigate to the folder `../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` and select the file with the name `cyclone_impact_population_map_template`. Click `Open`, then `Create`. 
4.  QGIS will ask you to name the new layout. Give it a name such as "Cyclone_Overview_Map_Freddy_2023". Click `OK`. A new window will open. This is the print layout composer. It should look similar to the figure below.

:::{figure} /fig/AA/mdg_aa_pop_impact_template.png
---
name: mdg_aa_pop_impact_template
width: 600 px
---
:::

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
     - ➕ Add the columns: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE` and `exposed_population` **or any other layer you are working with**
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

#### Exporting the Map 

<!--Exporting the map should be done after each layout. If the maps are not locked, it will break the layouts and the work will have to be repeated

```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order to print it as a pdf or format of your choice.


__Tool:__ [Print Layout Composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

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
3. Click on `Save`.
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

## Working with the warehouse isochrones

The project includes isochrones for each warehouse. The warehouse isochrones correspond to one warehouse and are identifiable by their location name. If you want to add an isochrone to one of the  It is possible to add individual isochrones to the map templates by simply duplicating the isochrone layer and moving it to the desired map group.

<!--INSERT EXAMPLE PICTURE-->

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

