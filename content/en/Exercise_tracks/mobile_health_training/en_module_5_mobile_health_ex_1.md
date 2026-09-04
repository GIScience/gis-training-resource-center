::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


%% To Do:
%% SPECIFY 
%% --- ---
%% Cut from draft: Before proposing where an MHU should go, you first need to show, with evidence, who currently lacks reasonable access to primary healthcare (PHC) — and to be honest about what a GIS access model can and cannot tell you about that.

## Mobile Health Training - Exercise 1A: 


:::{card} 
:link: en_ex_track_mobile_health_overview.md
__Exercise track: Mobile Health Units__
^^^
This exercise is part of the Mobile Health Exercise track. You can find the overview of the training on [this page]()
:::

## Characteristics of the exercise <a id="characteristics-of-the-exercise"></a>

::::{grid} 
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training.
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__Exercise Track:__
^^^
This exercise is part of the [Colombia Mobile Health Unit (MHU) Deployment Planning Exercise Track](../Exercise_tracks/en_col_mhu.html)

:::

::::

::::{grid} 
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^


:::

:::{grid-item-card}
__Relevant Wiki Articles__
^^^

- ORS
- zonal stats
- extract
- 

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Aim of the exercise:__
^^^

In this exercise, we will design a potential Mobile Health Unit (MHU) route. We will start by assessing the Primary Health Care (PHC) gap and the target population. In a next step, we will assess the coverage of possible MHU stops and evaluate the priority of these stops in relation to existing healthcare systems and other narrative information (or qualitative information). Finally, we will draft potential routes and decide, how long the medical team should stay in the MHU stops. 


:::

### Instructions for the trainers <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Trainers Corner__ 

#### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md#how-to-do-trainings) for some general tips on facilitating trainings. 

#### Conduct the training <a id="conduct-the-training"></a>

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


## Scenario

:::{topic} Designing an MHU in the area of XX XX 

In the municipios XX and XX, it is confirmed that the local national society will run a mobile health programme to complement local health post and hospital system. The need is confirmed, and the donor signalled 

You are tasked to design the route of the programme and assess the population reached with this route. The funding for the first 12 months is secured with the aim to complete at least 10 deployments of the mobile health unit. 
%% AND REACH XXXX INHABITANTS?
%% ADD SOME MORE CONTEXTUAL INFORMATION ABOUT THE COL/VEN BORDER REGION?

:::


## Available Data

%% ADD LINK TO DATASETS 

:::{card}
:link: 
__Download all datasets [here] and save the folder on your computer and unzip the file.__
:::

| Dataset name | Original title | Publisher   | Source      |
|--------------|----------------|-------------|-------------|
| PLACEHOLDER  | PLACEHOLDER    | PLACEHOLDER | PLACEHOLDER |
|              |                |             |             |


## Tasks 

### Task 1: Getting an overview of the data and area of interest

Before we begin evaluating the MHU stops, we need to familiarise ourselves with the area of interest (AOI) and the available data. We will be working in the department of __XYZ__, so we can begin by clipping our data to the AOI. Before beginning with any processing, take the time to look at the available data and opening the [attribute tables](../../Wiki/en_qgis_attribute_table_wiki.md)

1. [Import the layers](../../wiki/en_qgis_import_geodata_wiki.md) in the `/data/input`-folder. 
    - `ABC.gpkg`
    - `XYZ.shp`
    - XYZ
2. Order the layers in the layers tab.
3. Extract the department of Cesar from the adm1 boundaries. (Tip: Extract selected features). 
%% OR Norte de Santander?
4. Extract all the municipios (adm2) in the department of Cesar. (Tip: Extract by location).
5. Clip the road and river network to the Cesar department (Tip: Clip by mask layer).
6. Clip the health points to the layer
7. Clip the population raster layer to the AOI.
7. Save the resulting layers in the `data/temp/`
8. Adjust the symbology of each layer so you can easily distinguish each layer

%% ADD RESULT IMAGE 

### Task 2: Add demographic information 

In this step, we want to get an overview of the target population. On top of general population numbers, we want to know the demographic distribution of the population. With this information, we can assess the PHC needs of the population. For example, a high share of women in childbearing age will mean that there is a higher need for gynecological, maternal, and pre- and post-natal care. 
We will estimate the population distribution based on the population data provided by [WorldPop](https://hub.worldpop.org/). Keep in mind that these numbers are estimations, and not definitive numbers by a census. The analysis should be adapted with data from the field and the communities to better understand the actual needs of the population. 

1. Calculate the demographic distribution per municipio (Tip: using zonal statistics)
2. Calculate the population under 5 per municipio
3. Calculate the population of women in childbearing age (15 - 46) per municipio
4. Take a look at the distribution of healthcare facilities in the AOI
%% 5. Take a look at the distribution of the the PHC Accessibility
%% Also might be interesting to already categorise the health facilities to identify gaps
%% Here it might also be good to add additional information about the health facilities (maybe invent them)

> RESULT: 

### Task 3: Calculate the potential coverage of the proposed MHU stops

We now have a first, quantitative picture of the health coverage in the AOI. In this step, we want to calculate the estimated coverage of the new MHU stops. This will help us assess the reach and priority of each stop. 

We will be using the OpenRouteService developed by HeiGIT in order to calculate isochrones depicting the new service area for each potential MHU stop. There are also other methods to calculate the service area of the MHU stops (for example, QGIS' native "service area"-tool or using [Friction Surface Layers](https://developers.google.com/earth-engine/datasets/catalog/projects_malariaatlasproject_assets_accessibility_friction_surface_2019_v5_1_walking_only?hl=en))

We want to calculate the area that the local population can reach __within 1 hour by foot__. To calculate this, we can use the isochrone algorithm from the OpenRouteService tools and specify the travel mode as 

%% Add picture or explanation for isochrones?

1. [Install the __"ORS tools"__ plugin](../../wiki/en_qgis_plugins_wiki.md) in QGIS.
::::{margin}
:::{tip}
If it is your first time using the ORS, you will need to create an account at https://openrouteservice.org/.  
Next, navigate to your account, find the "Basic key" and copy it.  
In your QGIS window, in the top bar, navigate to `Web` → `ORS tools` → `Provider Settings`, paste your key into the API key field and click on `Save`.
:::
::::
2. In the [processing toolbox](../../wiki/), search for "ORS" and open the tool `Isochrones from Point-Layer". 
%% ADD CORRECT LINK
3. In the ORS parameter-window, set the parameters as follows:
    - `Provider`: OpenRouteService
    - `Travel mode`:  foot-walking
    - `Input Point layer`: `COL_Cesar_Pot_MHU_Stops`
    - `Dimension`: Time
    - `Comma-separated ranges`: 60
4. Click `Run`. The ORS will send a request to the ORS server to compute the isochrones.
5. A new layer will appear in your layers tab. Investigate it by zooming to the layer and opening its attribute table. 
    - If you don't find any errors, you can save the layer via <kbd>right-click</kbd> → `Make permanent` and saving it in the `/data/temp/`-folder

> Great! We now have the coverage of the proposed MHU stops. In a next step, we need to calculate the distribution of the population inside the isochrones.

%% MAYBE ADD SOMETHING ABOUT THE SPHERE STANDARDS? OR SOME OTHER REQUIREMENTS FOR OUR ANALYSIS? PUT IN THE BEGINNING

### Task 4: Estimate the demographic distribution for each proposed MHU stops

Stopping at each proposed stop wouldn't be logistically feasible. Furthermore, in some cases, there is already a fixed primary healthcare facility present, so adding additional MHU stops 



### Task 5: Evaluating additional information

From the communities, we have received additional information on the current healthcare system and coverage. Below, you will find short summaries of the reports


:::{card} 

In the 

:::

