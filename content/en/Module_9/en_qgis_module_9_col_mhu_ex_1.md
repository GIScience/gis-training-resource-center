::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

%% TO DO:
%% - REMOVE PUTUMAYO OR ONLY FOCUS ON PUTUMAYO?
%% INSTEAD OF USING A FLOOD LAYER, WHICH MIGHT COMPLICATE THE EX TRACK, CREATE A FLOODING SCENARIO AT A RIVER CROSSING (E.G., after designing the first route, we have been informed that this bridge is inpassable from XX to XX due to rains. Find an alternative route). 
%% HeiGIT PHC Accessibility might be off due to OSM data quality and it doesn't include hospitals either (maybe dissolve both? but then the pop data would be off.. but we will probably calculate that again)
%% SELECTING THE AOI IS OUT OF SCOPE. IT IS ALREADY GIVEN IN THE SCENARIO.


# Exercise 1: Mapping Today's Primary Healthcare Access Gap <a id="exercise-1-mapping-todays-primary-healthcare-access-gap"></a>

## Characteristics of the exercise <a id="characteristics-of-the-exercise"></a>

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training.
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__Exercise Track:__

This exercise is part of the [Colombia Mobile Health Unit (MHU) Deployment Planning Exercise Track](../Exercise_tracks/en_col_mhu.html)

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

* [Select by Expression](../Wiki/en_qgis_data_queries_wiki.md)
* [Select by Location](../Wiki/en_qgis_spatial_joins_wiki.md#join-attributes-by-location-summary)
* [Clip](../Wiki/en_qgis_geoprocessing_wiki.md#clip)
* [Zonal Statistics](../Wiki/en_qgis_raster_basic_wiki.md)
* [Field Calculator](../Wiki/en_qgis_attribute_data_wiki.md)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Aim of the exercise:__
^^^
The Colombian Red Cross has been asked by a donor to design a 12-month Mobile Health Unit (MHU) programme bringing primary healthcare to geographically isolated rural communities in Cauca, Nariño, Norte de Santander and Putumayo — departments where armed conflict and forced displacement have cut communities off from fixed health facilities. Before proposing where an MHU should go, you first need to show, with evidence, who currently lacks reasonable access to primary healthcare (PHC) — and to be honest about what a GIS access model can and cannot tell you about that.
:::

## Instructions for the trainers <a id="instructions-for-the-trainers"></a>

::::{dropdown} __Trainers Corner__
### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board (physical, flip-chart, or digital) where participants can add their findings and questions.
- Before starting, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md#how-to-do-trainings) for general tips on training conduction.

:::{note}
__Two open data questions to resolve before running this exercise for real:__
1. Confirm the exact field names in `COL_primary_healthcare_access.gpkg` (the isochrone × admin-level × range-value layer). This draft assumes fields along the lines of `pop_total`, `pop_within_60min_drive`, `pop_share_within_60min_drive` per adm2 unit — rename in the tasks below to match the real schema before delivering.
2. Confirm whether the Health Cluster attribute table (`Health_Facilities_ES.dbf`) has a facility type/level field, and what its values are. Task 2 below is written to let participants discover this themselves, but you should know the answer in advance.
:::

### Conduct the training <a id="conduct-the-training"></a>

__Introduction:__

- Introduce the donor scenario and the aim of the exercise.
- Say explicitly: __"Your map is evidence for a decision. It is not the decision."__ Sphere's access indicator (80% of a population within one hour of PHC) is a useful quantitative target, but Sphere itself notes that access also depends on availability, acceptability and affordability — a GIS model only measures the physical-reach part of that.

__Follow-along:__

- Show and explain each step yourself at least twice, slowly enough that everybody can follow in their own QGIS project.
- Periodically check that nobody has fallen behind.
- Be patient with data-quality surprises in Task 2 — they are the point of the task, not a distraction from it.

__Wrap up:__

- Leave time for the discussion questions at the end — they matter as much as the map.

::::

__Context:__

Before an MHU can be justified to a donor, the Colombian Red Cross team needs to answer a simple question with real numbers: **how many people currently live beyond a reasonable travel time from primary healthcare, and where are they?**

You have been given a prepared data package: a 2026 population raster, official administrative boundaries, two health-facility datasets (an official 2021 government/Health Cluster list and a 2026 OpenStreetMap snapshot), and a pre-computed accessibility layer built by HeiGIT from one-hour drive-time isochrones. Your job in this exercise is not to build a new accessibility model from scratch — it's to use, question, and adjust the one you've been given.

# Tasks <a id="tasks"></a>

## 1. Set Up Your Study Area <a id="1-set-up-your-study-area"></a>

The datasets you've been given cover all of Colombia. Working at national scale would be slow and distracting as the layers contain a lot of data, so the first step is narrowing everything down to the four departments in scope.

1. **Load the admin boundaries**
   - `col_admbnda_adm1_mgn_20200416.shp` (departments)
   - `col_admbnda_adm2_mgn_20200416.shp` (municipios)
   

2. **Select the four target departments** on the adm1 layer:
   - Open the attribute table → `Select features using an expression`
   ```qgis
   "ADM1_ES" IN ('Cauca', 'Nariño', 'Norte de Santander', 'Putumayo')
   ```
   - Right-click the layer → `Export` → `Save Selected Features As…` → GeoPackage → save to `data/temp/` as `study_area_adm1.gpkg`#
   

3. **Select the municipios inside those departments** the same way, using `"ADM1_ES" IN (...)` on the adm2 layer, and export as `study_area_adm2.gpkg`.

%% THIS SHOULD BE DONE WITH EXTRACT BY LOCATION. 

4. **Clip the population raster** to the study area:
   - Processing Toolbox → `Clip raster by mask layer`
   - **Input layer:** `col_pop_2026_CN_100m_R2025A_v1.tif`
   - **Mask layer:** `study_area_adm1.gpkg`
   - **Output file name:** save to `data/temp/col_pop_2026_study_area.tif`


5. **Select by location** on both health-facility datasets and on `COL_primary_healthcare_access.gpkg` (adm2 layer), using `study_area_adm1.gpkg` as the intersecting layer, and export each filtered result to `data/temp/`.

> 💡 **Tip**: Keep working in `data/temp/` for anything you might redo. Only export finished layers to `data/output/`.

%% ADD STEPS TO ADD ROAD NETWORK AND RIVERS?, RAILS?
%% ADD A SHORT RESULT FOR THIS STEP (IMAGE: NOW WE HAVE A FIRST OVERVIEW OF THE REGION)

## 2. Get to Know Your Two Health-Facility Datasets <a id="2-get-to-know-your-two-health-facility-datasets"></a>

You have two facility lists that disagree with each other, and neither is perfect. Before using either one, look at what's actually in them.

1. **Open the attribute table of `Health_Facilities_ES` (2021, official)** and look for a field describing facility type or level (e.g. hospital vs. health post vs. clinic). Note it on the whiteboard — you will need it in Task 4.


2. **Check the geometry quality of `Health_Facilities_ES`.**
   - Right-click the layer → `Filter…` and try:
     ```qgis
     "geom" IS NULL OR NOT ST_IsValid($geometry)
     ```
   - If that doesn't surface anything, zoom to the full layer extent and look for points far outside Colombia — a small share of records in this dataset have coordinate values that look like facility ID codes rather than actual coordinates. Decide as a group whether to drop or investigate these before using the layer further.
%% THIS STEP CAN BE SKIPPED, IT IS MORE A EX DESIGN CHOICE. 

3. **Open the attribute table of the OSM export** (`hotosm_col_health_facilities_osm_gpkg`) and look at the `amenity` and `healthcare` fields. Filter to keep only clinically relevant facilities:
   ```qgis
   "amenity" IN ('hospital', 'clinic', 'doctors', 'health_post')
   ```
   Export this filtered layer as `data/temp/osm_health_facilities_clinical.gpkg`.
4. **Compare the two datasets by eye** in the map canvas, zoomed to one department. You should notice the official list has many more points than OSM — and that in more remote areas, OSM often has none at all where the official list does.

:::{note}
This isn't just a training artefact. Checking geometrically, roughly one in five official facilities (about 21%) has no OSM-mapped clinical facility within 1km of it — OSM's health data is noticeably thinner in exactly the remote, conflict-affected areas this exercise is about. That's a reason to treat the official 2021 list as the primary source for "what exists today," and OSM as a secondary layer for cross-checking and filling specific gaps (like facility type, discussed in Task 4) — not the other way around.
:::

## 3. Read the Existing Accessibility Layer <a id="3-read-the-existing-accessibility-layer"></a>

`COL_primary_healthcare_access.gpkg` already contains the answer to "who can reach a primary healthcare facility by car within one hour" — HeiGIT built it by generating drive-time isochrones from every primary healthcare facility and intersecting them with population and administrative boundaries.

1. **Load the adm2 layer** from `COL_primary_healthcare_access.gpkg` (already filtered to your study area from Task 1).
2. **Open its attribute table** and identify the fields holding total population, population reached within the 60-minute drive isochrone, and the percentage reached. *(Field names to confirm with your trainer — this exercise assumes something like `pop_total`, `pop_within_60min_drive`, `pop_share_within_60min_drive`.)*
3. **Calculate the population outside 60-minute drive access** per municipio using the Field Calculator:
   - **Output field name:** `pop_beyond_60min_drive`
   - **Expression:**
     ```qgis
     "pop_total" - "pop_within_60min_drive"
     ```
4. **Symbolise the layer** by `pop_share_within_60min_drive`: Graduated, color ramp RdYlGn, Mode: Equal Count, 5 classes. Municipios in red are where the current fixed-facility network, reachable by car, leaves the most people behind.

## 4. Stress-Test the Layer's Assumption About Hospitals <a id="4-stress-test-the-layers-assumption-about-hospitals"></a>

HeiGIT built the accessibility layer from *primary healthcare* facilities only. But a hospital can also provide primary care — so a municipio whose only facility is a hospital may be marked "unserved" in Task 3's map even though it isn't, in practice.

1. **Select the hospitals** in your clinical OSM layer from Task 2:
   ```qgis
   "amenity" = 'hospital'
   ```
   Export as `data/temp/osm_hospitals.gpkg`.
2. **Select by location**: find municipios (from Task 3's layer) that contain at least one hospital **and** have a low `pop_share_within_60min_drive` value.
3. **Discuss as a group**: should these municipios be removed from your underserved shortlist, downgraded in priority, or kept as-is with a caveat? There's no single correct answer — Sphere doesn't specify how many patients per day a hospital can absorb as "primary care overflow," so this is a judgement call your team needs to make and justify, not something the GIS layer can decide for you.

> ⚠️ **Don't try to re-run the isochrone analysis with hospitals added in this exercise.** That would mean regenerating HeiGIT's drive-time model from scratch, which is out of scope here. Instead, treat Task 3's map as a first draft and Task 4 as a manual sense-check on top of it.

%% OUT OF SCOPE BECAUSE IT WOULD TAKE TOO LONG

## 5. Select Your Priority Underserved Clusters <a id="5-select-your-priority-underserved-clusters"></a>

1. Rank the municipios in your study area by `pop_beyond_60min_drive`, adjusted for your Task 4 judgement calls.
2. As a team, agree on **two or three priority underserved clusters** to carry forward — not the entire four-department area. The next exercise in this track will design MHU stops for these clusters specifically.
3. Record, for each chosen cluster: total population, population within 60-minute drive access, population outside it, and the percentage figure. You'll present this exact set of numbers again at the end of the track.

---

## Discussion <a id="discussion"></a>

- **What does this map tell us, and what can it definitely not tell us?** It tells you where the *existing, car-reachable, primary-care-only* health system leaves people behind. It does not tell you whether people without a vehicle could reach that same facility on foot, whether the facility has the staff or medicine to actually treat them, or whether conflict/security conditions make the "reachable" route usable in practice.
- The next exercise switches from *diagnosing the gap* (car access to existing facilities) to *designing a response* (walking access to a new MHU stop) — these are deliberately two different travel modes, because an MHU comes to the community rather than the other way around.

:::{note}
Always interpret accessibility results with caution. Population raster estimates, administrative boundary vintages, and facility datasets are all snapshots with their own margins of error, and none of them capture availability, acceptability, or affordability of care. Field validation and coordination with local health teams remain essential before any operational decision.
:::

---
