::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


%% To Do:
%% SPECIFY TARGET POPULATION
%% MAYBE ALSO ADD THAT WE ARE USING INCOMPLETE PROXY DATA (HDX), SOME AREAS DONT HAVE GOOD DATA AVAILABLE SO IT WOULD ALSO BE YOUR JOB TO IDENTIFY DATA GAPS AND IN A REAL OPERATION YOU WOULD IDEALLY BE ABLE TO FILL THE GAPS THROUGH INFORMANTS OR ...
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

- [Extract by Location / Selection](../Wiki/en_qgis_data_queries_wiki.md)
- [Clip](../Wiki/en_qgis_geoprocessing_wiki.md#clip)
- [Zonal Statistics](../Wiki/en_qgis_raster_basic_wiki.md)
- [Join Attributes by Field Value](../Wiki/en_qgis_attribute_data_wiki.md)
- Cost Distance / Friction Surfaces 
%% this wiki page doesn't exist yet — link once written, don't fake a URL in the meantime

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

:::{note}
The friction-surface tool in Task 3 uses GRASS's `r.cost`, which ships with QGIS but exact parameter labels can shift slightly between QGIS/GRASS versions — run through Task 3 yourself in your installed version before the training and adjust the field names in the instructions if needed.
:::

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

:::{topic} Designing an MHU in Tibú, Norte de Santander 

In the municipio of Tibú, Norte de Santander — an area along the Colombia/Venezuela border where armed conflict has repeatedly cut communities off from fixed health services — it is confirmed that the local national society will run a mobile health programme to complement the local health post and hospital system. The need is confirmed, and the donor has signalled that it will fund the first 12 months of operations, provided the National Society can show where the MHU will operate and roughly how many people it will reach. 

You are tasked to design the route of the programme and assess the population reached with this route, with the aim to complete at least 10 deployments of the mobile health unit over those 12 months. 

According to the SPHERE standards, a minimum of 80% of the population must live within a one hour walking distance from a primary healthcare facilities. Additionally, in rural areas, it is estimated that at least 1 primary healthcare facility is needed for 50 000 inhabitants. You will estimate the target population for your route in Task 2.

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

Before we begin evaluating the MHU stops, we need to familiarise ourselves with the area of interest (AOI) and the available data. We will be working in the municipio of __Tibú__, in the department of Norte de Santander, so we can begin by clipping our data to the AOI. Before beginning with any processing, take the time to look at the available data and opening the [attribute tables](../../Wiki/en_qgis_attribute_table_wiki.md)

1. [Import the layers](../../wiki/en_qgis_import_geodata_wiki.md) in the `/data/input`-folder. 
    - `ABC.gpkg`
    - `XYZ.shp`
    - XYZ
    - the walking-only friction surface raster
2. Order the layers in the layers tab.
3. Extract the department of Norte de Santander from the adm1 boundaries. (Tip: Extract selected features). 
4. Select the municipio of Tibú from the adm2 boundaries. (Tip: Extract by location, or Select by expression on the municipio name).
5. Clip the road and river network to Tibú (Tip: Clip by mask layer).
6. Clip the health points to the layer
7. Clip the population raster layer to the AOI.
8. Clip the friction surface raster to the AOI (Tip: Clip raster by mask layer, same as the population raster).
9. Save the resulting layers in the `data/temp/`
10. Adjust the symbology of each layer so you can easily distinguish each layer

%% ADD RESULT IMAGE 

### Task 2: Add demographic information 

In this step, we want to get an overview of the target population. On top of general population numbers, we want to know the demographic distribution of the population. With this information, we can assess the PHC needs of the population. For example, a high share of women in childbearing age will mean that there is a higher need for gynecological, maternal, and pre- and post-natal care. 
We will estimate the population distribution based on the population data provided by [WorldPop](https://hub.worldpop.org/). Keep in mind that these numbers are estimations, and not definitive numbers by a census. The analysis should be adapted with data from the field and the communities to better understand the actual needs of the population. 

1. Calculate the demographic distribution per municipio (Tip: using zonal statistics)
::::{margin}
:::{tip}
Worldpop offers population estimates by age groups and gender. In the data folder locate `col_agesex_structures_2026_R2025A_v1`. The folder has estimated population for age groups 0, 1, 5, and then in five year groups until 80+. 

:::
::::
%% Are almost 4 GB to much for the training/for the trainees to handle?

2. Calculate the population under 5 per municipio
    - Add the tif files for the age groups 0, and 1.
<details>
<summary>Hint</summary>

The correct layers are called:
    - `col_t_01_2026_CN_100m_R2025A_v1`
    - `col_t_00_2026_CN_100m_R2025A_v1`

The layer `col_t_05_2026_CN_100m_R2025A_v1` contains the population aged 5 and over. 

</details>

    - Clip the raster files to our AOI.
    - Open the [raster calcualtor](../../Module_8/en_qgis_raster_operations.md)
    - Add the clipped layers and save the file in `/data/temp/` under `AOI_pop_under_5_t_AOI.tif` 


3. Calculate the population of women in childbearing age (15 - 49) per municipio:
    
4. Take a look at the distribution of healthcare facilities in the AOI
%% 5. Take a look at the distribution of the the PHC Accessibility
%% Discussion point (see end of exercise): our facility dataset tells us a facility exists, not what it can treat or whether it has capacity — what would you want to know from the field before trusting this layer?



> RESULT: 

### Task 3: Calculate the potential coverage of the proposed MHU stops

We now have a first, quantitative picture of the health coverage in the AOI. In this step, we want to calculate the estimated coverage of the new MHU stops. This will help us assess the reach and priority of each stop. 

We want to calculate the area that the local population can reach __within 1 hour by foot__ of each proposed stop. Rather than routing on the road/path network directly, we'll use a pre-computed __walking-only friction surface__ (Malaria Atlas Project / Oxford — each pixel gives the time in minutes needed to cross it on foot, based on real terrain, land cover and existing paths). Starting from the MHU stop locations, we accumulate that cost outward to get a travel-time-from-nearest-stop raster — this is the same underlying idea as an isochrone, but it doesn't depend on having a complete road/path network for the AOI, which matters in an area like Tibú where the path network isn't fully mapped.

%% Add picture or explanation of what a friction surface / cumulative cost surface is

1. In the Processing Toolbox, search for `r.cost` (GRASS) and open it.
2. Set the parameters as follows:
    - `Input raster map containing grid cell cost information`: your clipped friction surface raster
    - `Starting points vector layer` (or `Starting points map`, depending on your QGIS version): `Tibu_potential_MHU_stops.gpkg`
    - Leave the other parameters at their defaults unless your trainer tells you otherwise.
3. Click `Run`. This produces a raster where every cell holds the estimated walking time, in minutes, from the nearest MHU stop.
4. Investigate the output: zoom in, check the value range, and sanity-check a few cells against the map (does a cell right next to a stop show a low value, roughly what you'd expect?).
5. Use the `Raster Calculator` to create a simple "within 1 hour" layer:
    ```
    "cost_raster@1" <= 60
    ```
    This gives you a binary raster: 1 where a location is within an estimated hour's walk of a proposed stop, 0 elsewhere.
6. Save both the cost raster and the "within 1 hour" raster to `/data/temp/`.

> Great! We now have an estimated walking-time coverage for the proposed MHU stops. In a next step, we need to calculate the population living inside that coverage.

:::{note}
This estimate is only as good as the friction surface itself — it's a real, peer-reviewed global dataset, but it's still a general model, not a survey of the actual paths people use around Tibú. Treat the resulting coverage as a planning estimate to validate with the National Society and local communities, not a precise measurement.
:::

%% If you'd rather teach network-based isochrones instead of (or alongside) the cost-surface approach, QGIS's native "Service area" tool or the ORS Tools plugin (openrouteservice.org, requires a free account and API key) can do this too — dropped from the main steps here to keep the tooling and setup to one method for a one-day training.

### Task 4: Estimate the demographic distribution for each proposed MHU stops

Stopping at each proposed stop wouldn't be logistically feasible. It is your task to find a route that can be done in approximately 14 days and adds substantial new coverage. Keep in mind that we do not want to duplicate existing healthcare coverage and it will be impossible to cover the entire population. Knowing which areas are not covered is also very valuable. In some cases, there is already a fixed primary healthcare facility present, so adding additional MHU stops. 

In this step, we want to calculate the demographic characteristics of the population living inside our new coverage layer:

1. Calculate the general population living inside the "within 1 hour" coverage layer using `Zonal statistics`. 
2. Calculate the zonal statistics for the population under 5.
3. We want to have all this information in a single layer. If the new columns are not in a single layer yet, we can combine the layers with the tool `Join layers by field value`. 

%% Review and fill in target population

> Great, we now have the demographic distribution for each stop, we can investigate the data by classifying the data in the symbolisation tab. 


### Task 5: Evaluating additional information

In this step, we want to evaluate which proposed MHU stops make the most sense. For this, we want to see where we can reach the largest population, and where we would not duplicate existing healthcare structures. We want a route that can be done within 14 days. Per day, we estimated that the MHU medical team can see about 20 patients. The MHU is equipped with a state of the art medical bus and can be operational within 2 hours upon arrival, so we can count the day of arrival as the start of the consultations. We assume that upon arrival, around 10% percent of the population will seek out primary healthcare services.   

---

## Discussion <a id="discussion"></a>

Your coverage layer only measures one thing: whether a location falls within an estimated hour's walk of a proposed stop. That's a useful, necessary starting point — and also only part of what actually decides whether an MHU stop works. Before finalising your route, discuss:

- __Availability, not just proximity.__ A stop being reachable doesn't mean the MHU can meet the need there — does your team have the right staff and supplies for what this population actually needs (Task 2's demographic breakdown is a first clue, not the full answer)?
- __Acceptability.__ Will people actually come? Trust, language, and past experience with outside organisations all shape whether a technically "covered" population is really served.
- __Coordination.__ Is another organisation already running health activities near one of your proposed stops? Placing an MHU stop where coverage already exists wastes the one resource you can't get back — your 14 days.
- __Site suitability.__ Can the medical bus actually reach and park at this location? Is there a safe, appropriate space to operate from once it arrives?
- __How current is your population data?__ A population raster is a snapshot. In an area with active displacement, the population actually living somewhere today can differ from what the dataset shows — how would you sense-check that before committing a route?

None of these can be answered from the datasets in this exercise alone — which is itself the point. Your map is evidence for a decision, not the decision.
