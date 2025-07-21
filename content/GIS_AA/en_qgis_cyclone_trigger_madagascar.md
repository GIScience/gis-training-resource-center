# QGIS Trigger Workflow for Madagascar 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Croix-Rouge Malagasy (CRM), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow is almost fully automated through a QGIS model, requiring no manual intervention. The chapter Automated Trigger Workflow outlines the process and its practical implementation. Each step included in the model is explained in detail to provide a complete understanding of the workflow and how the analysis was carried out.

## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

## Trigger Statement

**Pre-Activation Trigger:** at least one of the meteorological forecasts from Meteo Madagascar, RMSC La Reunion, or ECMWF projects a greater than 50% likelihood of landfall by a tropical cyclone of tropical storm strength or higher within the next 7 days.

**Activation Trigger:** if the Meteo Madagascar (DGM) forecast indicates landfall of a tropical cyclone with wind speeds in excess of 118 km/h within the next 48-72 hours.

# Functionality of the Trigger Workflow

{ref}`fig-trigger-concept` is displayed in the figure below.

```{figure} /fig/MAD_Trigger_concept.png
---
width: 1000px
name: fig-trigger-concept
align: center
---
The Trigger Process concept.
```

The entire trigger workflow will be run in a QGIS model, which automates the spatial analysis for assessing the impact of tropical cyclones. It integrates cyclone storm track data with administrative boundaries, population data, infrastructure, and service locations to identify and quantify affected areas and resources. 

## Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be fixed in the near term, and variable data which describe the datasets that will be checked for triggering on a regular basis depending on the occurrence of anticipated cyclone events. 

### Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Description |
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

The cyclone trigger mechanism is based on the data provided by NOAA (National Centers for Environmental Information). The cyclone storm tracks are provided within the [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) project. It is the most complete global collection of tropical cyclones available and merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset. IBTrACS was developed collaboratively with all the World Meteorological Organization (WMO) Regional Specialized Meteorological Centres, as well as other organizations and individuals from around the world.

:::{admonition} Master Raster
:class: hint

Tropical cyclone track data is available in various subsets, depending on the temporal scale of interest. Regional subsets can also be generated, with data for the **South Indian Ocean** being particularly relevant for this trigger mechanism.

:::

# Automated Trigger Workflow

As explained at the start of this chapter the developed trigger workflow is done automatically by a QGIS model. In this chapter we will explain its functionality and in a subsequent step it is explained how to run the automated model.

## Functionality of the model

The following key processing steps are run inside the model:

1. Cyclone Buffering & Impact Area Extraction
The new cyclone track is buffered to create a zone of potential impact. This buffer is dissolved to form a single affected area polygon. The resulting layer is the output cyclone area, used throughout the rest of the model.

2. Administrative Units Affected
Admin 2 (district-level) polygons are intersected with the cyclone buffer to extract the Affected districts. Admin 1 (region-level) boundaries are also extracted and used to identify neighboring regions that may still be at risk.

3. Population Impact
Zonal statistics are used to calculate the total affected population within the cyclone area. The result is saved as Affected Population and exported to a spreadsheet.

4. Infrastructure Impact
The model intersects the cyclone area with:
- Building data to count number of affected buildings.
- POIs (Points of interest) to identify affected education facilities and health site infrastructure.
The results are exported as:
- Affected Buildings
- Affected POIs Table, including a count of impacted education and health sites.

5. Warehouse Accessibility
Using the affected regions and buffered road data, the model identifies:
- Relevant Technicians
- Warehouses within reach of the affected area.
The output layer is relevant warehouses, indicating logistical support readiness.


## How to run the model

The [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.


## Step 1: Setting up folder structure !!NEEDS TO BE FIXED!!


```{figure} /fig/MAD_Trigger_workflow_Step1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ In this step we set up the correct folder structure to make the analysis easier and to ensure consistent results. 

__Tool:__ No special tools or programs are needed

``````{list-table}
:header-rows: 1
:widths: 10 25

* - Instruction
  - Folder Structure
* - 1. Open the Folder “FbF_Cyclone_Monitoring_Trigger"
    2. Open the subfolder "AA_Madagascar"
    3. Copy the Template folder “TEMPLATE_Year_Month” and change the name to the current year and month. The result could be the folder "2022_05"
    
  -
    ```{figure} /fig/Folder_structure_FbF_Drought_Monitoring_Trigger.drawio.svg
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

The Video below shows the process for setting up the folder for december 2023.


## Step 2: Download of the storm track data

```{figure} /fig/MAD_Trigger_workflow_Step2.png
---
width: 1000px
name: 
align: center
---
```

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


## Step 3: Open the project in QGIS and load the model in the QGIS Model Designer

```{figure} /fig/MAD_Trigger_workflow_Step3.png
---
width: 1000px
name: 
align: center
---
```

In this step we will open our Trigger project in QGIS and load the QGIS model which will automatically run the analysis for us.

1. Open the file `Trigger_Model.qgz` by double clicking it.
2. The QGIS project will open with lots of data pre-loaded. This data is required for running the QGIS model and create some output maps.

The data will be structured in three Groups:

IMAGE OF A SCREENSHOT OF THE THREE GROUPS WITH ALL THE PRE-LOADED DATA
```{figure} /fig/MAD_Trigger_stromtrack_download.PNG
---
width: 1000px
name: 
align: center
---
```

1. Group 1: Model_Input
This group will contain all the input data that is required to successfully run the model. All the data that is stored in this section is fixed except the storm track.

:::{attention}

Always ensure you are using the most recently updated storm track for this process. To import the new layer, simply drag and drop it into the `Layers panel`, and place it at the top of the **Model_Input** group for clarity.

For better data management, assign the storm track a descriptive name, such as `storm_track_eventname_year`. This naming convention clearly identifies the event and year, helping you stay organized and ensuring the correct data is used in the analysis.

:::

2. Group 2: Map_Cyclone_Impact_Overview
This group will contain all the layers needed to create the following map. 

SCREENSHOT OF THE OUTPUT MAP
```{figure} /fig/MAD_Trigger_stromtrack_download.PNG
---
width: 1000px
name: 
align: center
---
```

The following layers are required to create this map:
Pre-loaded:
- input storm track
- admin 1 boundaries

3. Group 3: Map_Cyclone_Impact_Assessment

3. Now open the QGIS Model Designer. The tool can be accessed under `Processing` -> `Modeler Designer`
4. In the upper panel click `Model` -> `Open Model` and navigate to your folder "FbF_Cyclone_Monitoring_Trigger", mark the "Cyclones_EAP_MAD_Trigger.model3" file an click on `Open`. The model will open and you will see yellow, white, green and grey boxes.


| Box | Significance | Description |
| ----- | --- | --- |
|Yellow| Model Input | Definition of the input data for the model the model will perform on. |
|White| Algorithms | Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering. |
|Green| Model Output| The results created by the model (Output layers) are automatically added to your layers panel in your QGIS project interface. |
|Grey| Comments| The boxes are used to further explain the specific processes. |


## Step 4: Run the model !!NAMES IN THIS SECTION NEED TO BE FINALIZED!!

```{figure} /fig/MAD_Trigger_workflow_Step4.png
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
2. The model needs the following 7 inputs:
    1. `mdg_admbnda_adm1_BNGRC_OCHA_20181031`: ADM1
    2. `ADM2_RISK`: ADM2 & Risk
    3. `Isochrones`: CRM warehouse isochrones
    4. `20240108_MAD_CRM_Warehouses_updated`: CRM warehouses
    5. `IBTrACS.ACTIVE.list.v04r01.lines`: Cyclone Tracks
    6. `hotosm_master_poi`: Master_POI
    7. `MAD_pop_constrained_buildings_landcover`: Master Raster

THIS ENTIRE LIST NEEDS UPDATED NAMES

3. Further down, you have to specify where to save the output: 
    1. `Affected_Districts`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    affected_districts
    ```
  
    2. `Relevant_Warehouses`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    relevant_warehouses
    ```

    3. `Affected_Cyclone_Area`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    affected_cyclone_area
    ```

    4. `Affected_Population`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    affected_population
    ```

    5. `Affected_Buildings`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    affected_buildings
    ```

    6. `Number_Affected_POIs`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Model_outputs` folder. Save the file in `.geojson` format. Give the output the name: 
    ```md
    number_affected_pois
    ```

4. Click `Run` to execute the model. The output result layers will be automatically added to the main QGIS window upon completion. Once the process has finished, you can close the `Model Designer` window.

```{dropdown} Video: Input and output Model
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/model_input_output.mp4"></video>
```

```{figure} /fig/SRCS_Model_input.png
---
width: 500px
name: 
align: center
---
```


## Step 5: Visualisation and Styling of the Model Outputs

:::{admonition} Output maps
:class: note

We will generate two output maps to support the analysis:
- Map 1 will provide an cyclone impact overview of the **affected districts, the extent of the cyclone event, and the locations of relevant warehouses**.
- Map 2 will focus on the impact to infrastructure and population, displaying the **number of affected people, buildings, health sites, and education facilities**.

:::

Additionally, a map showing the **warehouse isochrones** for all 13 warehouses will be provided by HeiGIT.

NEED NEW IMAGE

```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Definition of how features are represented visually on the map.

__Tool:__ [Symbology tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I.html#symbology-for-vector-data)

### Map 1: Cyclone Impact Overview: Affected Districts, Event Extent, and Warehouse Locations

Layers needed for this map:
- `Affected_Districts`
- `mdg_admbnda_adm1_BNGRC_OCHA_20181031`
- `Relevant_Warehouses`
- `Affected_Cyclone_Area`
- `Cyclone_track`

1. Right click on the Affected_Districts layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Cyclone_Monitoring_Trigger/layer_styles” folder and select the file __“affected_districts_style.qml”__.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” Window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | 
| ----- | --- |
|`mdg_admbnda_adm1_BNGRC_OCHA_20181031`| `adm1_style.qml` |
|`Relevant_Warehouses` | `relevant_warehouses_style.qml` |
|`Affected_Cyclone_Area`|`cyclone_area_style.qml`|
|`Cyclone_track`| `cyclone_area_style.qml`|

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

NEED NEW IMAGE

```{dropdown} Your final output should look like this after styling the layer
You will now see the affected districts and the locations of relevant warehouses clearly displayed on the map. Additionally, the original storm track line — used as input data — is highlighted, along with the buffered impact area, which serves as a proxy for identifying affected districts.

```{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: 
align: center
---
```

### Map 2: Impact Assessment: Affected Population and Critical Infrastructure

Layers needed for this map:
- `Relevant_Warehouses`
- `mdg_admbnda_adm1_BNGRC_OCHA_20181031`
- `Affected_Cyclone_Area`
- `Cyclone_track`
- `Affected_Population`
- `Affected_Buildings`
- `Number_Affected_POIs`

:::{attention}

If you already created Map 1 earlier in the process, you can reuse the first four layers with their existing styling for Map 2—and vice versa. This ensures consistency across both maps and saves time by avoiding duplicate styling efforts.

:::

1. Right click on the "Affected_Population" layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Cyclone_Monitoring_Trigger/layer_styles” folder and select the file __“affected_population.qml”__ style layer.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” Window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | 
| ----- | --- |
|`mdg_admbnda_adm1_BNGRC_OCHA_20181031`| `adm1_style.qml` |
|`Relevant_Warehouses` | `relevant_warehouses_style.qml` |
|`Affected_Cyclone_Area`|`cyclone_area_style.qml`|
|`Cyclone_track`| `cyclone_area_style.qml`|
|`Affected_Buildings`| `affected_buildings.qml`|
|`Number_Affected_POIs`| `affected_education_facilities.qml`|
|`Number_Affected_POIs`| `affected_healthsites.qml`|

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

NEED NEW IMAGE

```{dropdown} Your final output should look like this after styling the layer
You will now see the affected districts and the locations of relevant warehouses clearly displayed on the map. Additionally, the original storm track line — used as input data — is highlighted, along with the buffered impact area, which serves as a proxy for identifying affected districts.

```{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: 
align: center
---
```

## Step 6: Making the Print Map

```{figure} /fig/MAD_Trigger_workflow_Step6.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ Viualisation of the map features in a printable map layout

__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

### Map 1: Cyclone Impact Overview: Affected Districts, Event Extent, and Warehouse Locations

1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview`.
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "Feddy_2023_Overview".
3. Right click on the white canvas and select `Page Properties`. In the bottom right section of the print layout, you'll see the page specifications. Set the Size to `A3` and the Orientation to `Landscape` to ensure that the map template fits correctly within the page layout.
4. Go to the **FbF_Cyclone_Monitoring_Trigger and then Map_templates** folder and drag and drop the file `cyclone_impact_overview_map_template.qpt` into the print layout.
5. Change the title to fit the current Cyclone Event and also adapt the **List of Affected Districts** for the current event.
6. Adjust the Legend by clicking on it in the map layout and have a look at the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend be clicking on the item and then on the red minus icon below.
    * Add **Relevant_Warehouses**, **Affected_Cyclone_Area**, **Affected_Districts** and **mdg_admbnda_adm1_BNGRC_OCHA_20181031** to the legend by clicking on the green plus and click on the layer, then click `OK`
    * Change the names to fit with the names provided in the Print Layout.
 

```{dropdown} Video: Making print map
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
```

```{Attention}
Checklist for final map output:
- Map Information: Review and update all text elements as needed.
- Legend: Remove unnecessary items and rename layers with clear, meaningful descriptions.
- Affected Districts: Include only districts that are actually impacted in your "List of Affected Districts".
```

### Map 2: Impact Assessment: Affected Population and Critical Infrastructure

1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview`.
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "Feddy_2023_Impact".
3. Right click on the white canvas and select `Page Properties`. In the bottom right section of the print layout, you'll see the page specifications. Set the Size to `A2` and the Orientation to `Landscape` to ensure that the map template fits correctly within the page layout.
4. Go to the **FbF_Cyclone_Monitoring_Trigger and then Map_templates** folder and drag and drop the file `cyclone_impact_assessment_map_template.qpt` into the print layout.
5. Change the title to fit the current Cyclone Event and also adapt the **List of Affected Districts** for the current event.
6. Adjust the Legend by clicking on it in the map layout and have a look at the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend be clicking on the item and then on the red minus icon below.
    * Add **Relevant_Warehouses**, **Affected_Cyclone_Area**, **Affected_Districts** and **mdg_admbnda_adm1_BNGRC_OCHA_20181031** to the legend by clicking on the green plus and click on the layer, then click `OK`
    * Change the names to fit with the names provided in the Print Layout.
7. The map template includes four separate maps, each displaying the impact assessment for a different variable. These maps should be updated one at a time.
    * To ensure correct updates, first deactivate all other impact assessment layers (e.g., Affected Buildings, Affected Healthsites, etc.). Focus on one map at a time: identify the visualized layer, then locate the corresponding map in the impact template.
    * Click on the map frame and check the `Item Properties` panel in the bottom-right corner. Under the Layers section, you’ll see options for `Lock layers` and `Lock styles for layers`. These options should be disabled while updating the map — they prevent changes by locking the current layer and style.
    * Once the map is correctly updated, **re-enable both checkboxes** to lock the layer and style again. This ensures the map remains unchanged as you proceed to update the remaining three maps.
    * Repeat this process for all four maps, always remembering to: (1) Disable layer/style locks before editing. (2) Re-enable them after updating each map.

For easier visualization, we have created [map templates](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) for presenting the results of the trigger analysis. These templates serve as a base for your own visualizations and are available in the following directory: `.../FbF_Cyclone_Monitoring_Trigger/Map_templates`. You can customize the templates to suit your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```

The info box on the top right corner needs to be adapted manually. The list of the affected districts can be taken from the .csv output of the model.


## Step 7: Exporting the Map 


```{figure} /fig/MAD_Trigger_workflow_Step7.png
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
2. Choose the __Map_outputs__ folder. Give the file the name of the event e.g storm_track_Freddy_2023_overview (if its the impact map change insert this instead of overview).
3. Click on `Save`
4. The window `Image Export Options` will appear. Click `Save`
Now the image can be found in the result folder.


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Choose the __Map_outputs__ folder. Give the file the name of the event e.g storm_track_Freddy_2023_overview (if its the impact map change insert this instead of overview).
3. Click on `Save`
4. The window `PDF Export Options` will appear. For the best results, select the `lossless` image compression.
5. Click `Save`
Now the image can be found in the result folder in the folder you created in Step 1

```{dropdown} Video: Export image and PDF
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_trigger_export_image_pdf.mp4"></video>
```


```{figure} /fig/map_output_example2.png
---
width: 1000px
name: 
align: center
---
```
