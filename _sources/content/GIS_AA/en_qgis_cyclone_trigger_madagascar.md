# QGIS Trigger Workflow for Madagascar 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Croix-Rouge Malagasy (CRM), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow is almost fully automated through a QGIS model, requiring no manual intervention. The chapter Automated Trigger Workflow outlines the process and its practical implementation. Each step included in the model is explained in detail to provide a complete understanding of the workflow and how the analysis was carried out.

## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

## Trigger Statement

**Pre-Activation Trigger:** at least one of the meteorological forecasts from Meteo Madagascar, RMSC La Reunion, or ECMWF projects a greater than 50% likelihood of landfall by a tropical cyclone of tropical storm strength or higher within the next 7 days.

**Activation Trigger:** if the Meteo Madagascar (DGM) forecast indicates landfall of a tropical cyclone with wind speeds in excess of 118 km/h within the next 48-72 hours.

## Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be fixed in the near term, and variable data which describe the datasets that will be checked for triggering on a regular basis depending on the occurrence of anticipated cyclone events. 

### Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Description |
| ----- | --- | --- |
| Administrative Boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | The administrative boundaries on level 0-4 for Madagascar can be accessed via HDX provided by OCHA. For this trigger mechanism we provide the administrative boundaries on level 2 (district level) as a shapefile.  |
| Population Counts | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | The worldpop dataset in `.geotif` raster format provides the estimated total number of people per grid-cell for the year 2020. We will be working with the Constrained Individual countries 2020 at a resolution of 100m. |
| Buildings Counts | [Global ML Building Footprints](https://gee-community-catalog.org/projects/msbuildings/) | The building counts dataset in `.geotif` raster format counts the number of buildings per 100m grid cell. The workflow on how this dataset was created can be found in this [GitLab repo](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |
| Land Cover | [ Copernicus Land Cover](https://land.copernicus.eu/en/products/global-dynamic-land-cover/copernicus-global-land-service-land-cover-100m-collection-3-epoch-2019-globe) | The land cover dataset in `.geotif` raster format provides an overview over the dominant land cover type at a resolution of 100m. This dataset was downloaded using the Google Earth Engine. The workflow on how this dataset was downloaded can be found in this [GitLab repo](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |

:::{admonition} Master Raster
:class: note

The three raster datasets are joined together in a Master Raster which will be a raster layer with three channels and a resolution of 100 m. It will include the following information:
1. Population counts from Worldpop constrained (2020)
2. Building counts derived from ML Building Footprints (2021)
3. Land Cover derived from Copernicus Land Cover (2019)

:::

### Monitoring Data

The cyclone trigger mechanism is based on the data provided by NOAA (National Centers for Environmental Information). The cyclone storm tracks are provided within the [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) project. It is the most complete global collection of tropical cyclones available and merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset. IBTrACS was developed collaboratively with all the World Meteorological Organization (WMO) Regional Specialized Meteorological Centres, as well as other organizations and individuals from around the world.

Tropical cyclone track data is available in various subsets, depending on the temporal scale of interest. Regional subsets can also be generated, with data for the South Indian Ocean being particularly relevant for this trigger mechanism.


# Functionality of the Trigger Workflow

The Trigger Process concept is displayed in {ref}`fig-trigger-concept`.

```{figure} /fig/MAD_Trigger_concept.png
---
width: 1000px
name: fig-trigger-concept
align: center
---
```

# Automated Trigger Workflow

As explained at the start of this chapter the developed trigger workflow is done automatically by a QGIS model. In this chapter it is explained how to run the automated model.

The [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.


## Step 1: Setting up folder structure 


```{figure} /fig/Drought_EAP_Worklow_Step_1_1.png
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

The International Best Track Archive for Climate Stewardship (IBTrACS) v04r01 data is updated three times a week (usually on Sunday, Tuesday, and Thursday), and could be updated more frequently to address specific needs and use cases. The latest updates in the correct file format can be found on their [website](https://www.ncei.noaa.gov/products/international-best-track-archive):

1. Look for the `Access Methods` section and click on the `Shapefiles` section. The link leads to the following [website](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/shapefile/).
2. As we don't need the storm track data for the entire world and the entire archive we will only download a subset of the data. Look for the file named `IBTrACS.ACTIVE.list.v04r01.lines.zip` and click on it. The download will start automatically. This subset includes all the **storms active in the last 7 days**.
3. Unzip this file and open it in QGIS.
4. Open the attribute table and delete all the storm tracks that are not relevant for this analysis. Safe the updated storm track file.


## Step 3: Open the project in QGIS and load the model in the QGIS Model Designer

In this step we will open our Trigger project in QGIS and load the QGIS model which will automatically run the analysis for us.

1. Open the file `Trigger_Model.qgz` by double clicking it.
2. The file will open and you will lots of data pre-loaded. This data is required for running the QGIS model.
3. Now open the QGIS Model Designer. The tool can be accessed under `Processing` -> `Modeler Designer`
4. In the upper panel click `Model` -> `Open Model` and navigate to your folder "FbF_Cyclone_Monitoring_Trigger", mark the "Cyclones_EAP_MAD_Trigger.model3" file an click on `Open`. The model will open and you will see yellow, white, green and grey boxes.


| Box | Significance | Description |
| ----- | --- | --- |
|Yellow| Model Input | Definition of the input data for the model the model will perform on. |
|White| Algorithms | Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering. |
|Green| Model Output| The results created by the model (Output layers) are automatically added to your layers panel in your QGIS project interface. |
|Grey| Comments| The boxes are used to further explain the specific processes. |


## Step 4: Run the model

```{figure} /fig/Drought_EAP_Worklow_Step_5_1_automated_model.png
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

3. Further down, you have to specify where to save the output: 
    1. `Trigger_activation`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Results`folder in the folder you created in step 1 (Year_month). Give the output the name: 
    ```md
    Trigger_activation
    ```

    2. `Indices`: Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Results`folder in the folder you created in step 1 (Year_month). Give the output the name: 
    ```md
    Indices
    ```

    3. `IPC_Phase_C`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Results`folder in the folder you created in step 1 (Year_month). Give the output the name: 
    ```md
    IPC_Phase_C
    ```

    4. `IPC_Phase_P`:Click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to `Results`folder in the folder you created in step 1 (Year_month). Give the output the name: 
    ```md
    IPC_Phase_P
    ```

4. Click `Run`. Your results layer will appear in the main QGIS window. You can close the graphical modeller window.

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


## Step 5: Visualisation of results

We will create two output maps.

```{figure} /fig/Drought_EAP_Worklow_Step_14_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Definition of how features are represented visually on the map.

__Tool:__ [Symbology tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I.html#symbology-for-vector-data)

__Impact of the Cyclone Event__



1. Right click on the “Affected_districts” layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Cyclone_Monitoring_Trigger/layer_styles” folder and select the file __“affected_districts_style.qml”__.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” Window click `Apply` and `OK`

Do this same process for the following outputs:
- relevant warehouses
- the input storm track

```{dropdown} Info: Trigger Activation Layer
You will now see districts where no trigger is activated in green and districts with trigger activation in pink.

The “Style_Trigger_Activation.qml” style layer is configured to show the district names only where the trigger is actually activated. If there is no trigger activation you can activate the admin 1 boundary layer for better map orientation (see __Administrative 2 Boundaries__ below)

```{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: 
align: center
---
```

__Risk Assessment__


7. Right click on the "risk_assessment_districts" layer -> `Properties` -> `Symbology`
8. In the down left corner click on `Style` -> `Load Style`
9. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger/layer_styles” folder and select the file __“somalia_risk_assessment_style.qml”__ style layer.
10. Move the "risk_assessment_district" layer __below__ "Trigger_Activation" layer ([Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_concept.html?highlight=layer#layer-concept)).
11. Back in the “Layer Properties” Window click `Apply` and `OK`


```{dropdown} Info: Risk Assessment Layer
For the creation of an __Intervention Map__ we will have to add the risk assessment data and the respective style file.
For this first of all load from "FbF_Drought_Monitoring_Trigger/Fixed_data/Risk_Assessment" the file "risk_assessment_districts.gpkg". This file is the output of the conducted risk assessment and contains a risk value for each district of Somaliland and Somalia.  In order to visualize it 
```

__Administrative 2 Boundaries (Regions)__

12. Right click on the "Som_Admbnda_Adm1_UNDP" (Regiond) layer -> `Properties` -> `Symbology`
13. In the down left corner click on `Style` -> `Load Style`
14. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger/layer_styles” folder and select the file __“somalia_risk_assessment_style.qml”__.
15. Click `Open`. Then click on `Load Style` 
16. Back in the “Layer Properties” Window click `Apply` and `OK`
17. Add a the OpenStreetMap basemap by clicking on `Layer` -> `Add Layer` -> `Add XYZ layer...` -> Select the OpenStreetMap. Click `Add`. ([Wiki basemap](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html?highlight=osm#basemaps))
18. Place the OpenStreetMap basemap on the bottom.
19. Delet all layers exept:
    * Trigger_activation
    * risk_assessment_districts
    * Som_Admbnda_Adm1_UNDP
    * OpenStreetMap

```{dropdown} Video: Visualisation of results
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Trigger_model_style.mp4"></video>
```

``````{list-table}
:header-rows: 1
:widths: 20 20

* - Intervention Map __without__ Trigger activation
  - Intervention Map __with__ Trigger activation
* - 
    ```{figure} /fig/Map_no_trigger.PNG
    ---
    width: 1000px
    name: 
    align: center
    ---
    ```
    
  -
    ```{figure} /fig/Map_yes_trigger.PNG
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

```{Attention}
Remember the [layer concept](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_concept.html?highlight=layer#layer-concept) and make sure the basemap layer is at the bottom of your layers panel.
```



## Step 6: Making the Print Map

```{figure} /fig/Drought_EAP_Worklow_Step_15_1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ Viualisation of the map features in a printable map layout

__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)


1. If not done before, delet all layers expect __Trigger_activation__, __risk_assessment_districts__ and __OpenStreetMap__
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "2022_04".
3. Go the the __FbF_Drought_Monitoring_Trigger__` folder and drag and drop the file `Trigger_activation_Intervention_map.qpt` in the print layout
4. Change the date to the current date by clicking on "Further map info…" in the items panel. Click on the `Item Properties` tab and scroll down. Here you can change the date in the `Main Properties` field.
5. Adjust the Lgend by clicking on the legend in the  `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there check if you have to open the dropdown. Make sure `Auto update` is not checked.
    * Remove all itemes in the legend be clicking on the item and then on the red minus icon below.
    * Add __Trigger_activation__ and __risk_assessment_districts__ to the legend by clicking on the green plus and click on the layer and click `ok`
 

```{dropdown} Video: Making print map
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
```

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```


In order to easily visualize the output of the trigger analysis we provide you with a 
[map template](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) that can be used as a base for your visualization. You can find the template in the following directory: ".../FbF_Drought_Monitoring_Trigger/maps_somalia_template_risk_assessment.qpt".

You can also adapt the template to your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```

## Step 7: Exporting the Map 


```{figure} /fig/Drought_EAP_Worklow_Step_16_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order tp print it as a pdf or format of your choice.


__Tool:__ [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

When you have finished the design of you map you can export it as pdf or image file in different datafromats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Chose the __Result__ folder in the folder you have created in step 1. Give the file the name of the project e.g 2022_04
3.  Click on `Save`
4. The window "Image Export Options" will appear. Click `Save`
Now the image can be found in the result folder in the folder you created in Step 1


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Chose the __Result__ folder in the folder you have created in step 1. Give the file the name of the project e.g 2022_04
3.  Click on `Save`
4. The window "PDF Export Options" will appear.  For the best results, select the `lossless` image compression.
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
