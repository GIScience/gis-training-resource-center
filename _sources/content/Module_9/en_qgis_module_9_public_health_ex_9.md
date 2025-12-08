# Exercise 3: Assessing Accessibility to Vaccination Services

## Background

Following your analysis of measles incidence rates per district, the Ministry of Health now wants to identify which populations have limited access to vaccination services. In this exercise, you will learn a simplified approach on how to model accessibility and determine how many people live **beyond a reasonable travel distance** from a vaccination point.

Accessibility to health services is a key determinant of vaccination coverage. In many rural parts of Chad, communities may not have access to motorised transport and rely on walking or infrequent public transport. Thus, distance alone is not always a good measure — **travel time** provides a more realistic assessment.

---

## Available Data

| Dataset name | Description | Source |
| :------------- | :----------- | :----------- |
| `QGIS project from Exercise 2 with .qgz extention` | Base project with administrative boundaries, health facility capacities, and incidence rates | — |
| `tcd_pop_2025_CN_100m_R2025A_v1.tif`| 2025 population estimate per grid-cell | [WorldPop](https://hub.worldpop.org/geodata/summary?id=72895) |
| `tcd_healthsites_points_capacities.gpkg` | Vaccination points (healthsites with cold chain) | Derived in Exercise 1 |
| `tcd_admbnda_adm2_20250212_AB.shp` | Administrative boundaries (district level) | [HDX – OCHA](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_roads_ocha.shp` (Lines) | Chad - Road Network | [HDX - OCHA](https://data.humdata.org/dataset/chad-roads-osm-ministry-of-transport) |

---

## Scenario

You have identified a number of health facilities equipped with a cold chain for vaccine storage. The goal now is to calculate how much of the population is **within reasonable reach** of these facilities, and how many people live **beyond the accessible range**.

To do this, you will generate travel-time surfaces around vaccination points and then use WorldPop data to estimate the population covered within each accessibility zone. This approach simplifies reality but provides a useful approximation of service coverage.

---

## Task 1: Opening the Project and Preparing the Data

1. Open your QGIS project from **Exercise 2**.
2. Verify that the following layers are loaded:
   - `tcd_admbnda_adm2_20250212_AB.shp` (district boundaries)
   - `tcd_healthsites_points_capacities.gpkg` (vaccination points)
   - `tcd_pop_2025_CN_100m_R2025A_v1.tif` (population raster)
   -  `tcd_roads_ocha.shp` (road network)
3. Now we need to filter the `tcd_healthsites_points_capacities` layer to only include healthsites with a cold chain for vaccine storage. We will do so by opening the "Attribute table" and clicking on "Select features using an expression" ![](/fig/mActionSelectbyExpression.png)
   - Now click on the "Fields and Values" section and double-click on cold_chain
   ```
   "cold_chain" = true
   ```
   - Now right click on the `tcd_healthsites_points_capacities` → `Export` → `Save Selected Features As...`
   - Save it as a "Geopackage" in your `/data/interim/`-folder. Use a name like `tcd_cold_chain_healthsites_points_capacities`. Now we have only the healthsites that also provide a cold chain for vaccine storage and could be considered for a vaccination campaign.

---

## Task 2: Creating Accessibility Area Around Vaccination Points

1. Open the "Service area (from layer)" tool in the Processing Toolbox.
2. Select the following parameters to run a Network Analysis. The algorithm creates a new vector with all the edges or parts of edges of a network line layer that can be reached within a distance or a time, starting from features of a point layer.
   - For the Vector layer representing network select the Chad road network `tcd_roads_ocha`
   - Path type to calculate should be `Fastest`, as we want to work with travel time
   - Vector layer with start points is the newly created `tcd_cold_chain_healthsites_points_capacities`
   - Travel cost will be `2` as the information for the fastest path type is given in hours. So 2 will correspond to 2 hours of travel time
   - The speed will be left at the Default speed of 50 km/h

```{Attention} Selecting the right CRS
The tool _Service area (from layer)_ requires the QGIS project running in an appropriate metric CRS to produce meaningful output.
Make sure to set your QGIS project via the menu in the lower right corner to a metric CRS, eg `ESRI:102022`. The layers don't necessarily need to be prjected in a metric system. 

* More info on the CRS menu in the QGIS UI is available [here](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_projections.html#how-to-choose-an-appropriate-projected-coordinate-system)
* More on CRS in general is available [here](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_projections.html#how-to-choose-an-appropriate-projected-coordinate-system)

```

:::{figure} /fig/en_3.40_m3_ex_3_service_area.png
---
name: en_3.40_m3_ex_3_service_area
width: 650 px
---
:::

3. The output will be called `Service area (lines)` and will include the road network accessible from a given healthsite within 2 hours of travel time at a travel speed of 50 km/h. To further process this data we need to reproject it to a metric CRS that depicts Chad without distorting too much. Select __EPSG: 102022__ and reproject the `Service area (lines)`. The output layer will be called `Reprojected`.
4. To produce a more realistic representation of the accessible area around each vaccination point, we will buffer the `Service area (lines)` layer. Before buffering, we first need to [`Dissolve`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#dissolve) the service-area lines so they form a single unified geometry.
   - Open the `Dissolve` tool and use the reprojected output as the __Input layer__
   - In Dissolve fields, we won't select anything

:::{Warning}
Both the `Dissolve` and `Buffer` operations can be computationally intensive. If your computer struggles to process the full dataset at once, try running the operations on smaller areas—for example, a few admin 1 states at a time. To do this, [select](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_data_queries.html#manual-selection) several states from the `tcd_admin1 layer`, then right-click the layer → `Export` → `Save Selected Features As…` and save the subset. Use the [`Clip`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#clip) tool to cut the service-area roads to this smaller region, and then run the `Dissolve` and `Buffer` operations on the reduced dataset.
:::

5. Now we can buffer the Dissolved Service area lines by 2 km, which corresponds to around 30 minutes of walking.
   - Input layer will be the result of the dissolving process (likely called `Dissolved`)
   :::{figure} /fig/pub_health_chad_buffer.png
   ---
   name: Buffer operation service area roads
   width: 350 px
   ---
   :::  
   - Set the buffer distance to 2 km. The output should look similar to the screenshot below: the green area represents the estimated 2-hour accessibility zone around the vaccination points along the road network.
   :::{figure} /fig/en_3.40_m3_ex_3_access_vaccination.png
   ---
   name: en_3.40_m3_ex_3_access_vaccination
   width: 350 px
   ---
   :::
   - Save the buffered service area by <kbd>right-clicking</kbd> on it and selecting `Make permament...`. Select "Geopackage" as the output format and save the layer to the `data/interim/`-folder and enter a file name such as `access_vaccination_points`. Click `Save`.

---

## Task 3: Calculating Population Coverage Using WorldPop

Next, we will generate several population statistics. First, use the admin boundaries together with the WorldPop raster to calculate the total population for each district. 

1. In the **Processing Toolbox**, search for the tool **Zonal Statistics** and open it.
   - **Input layer:** `tcd_admbnda_adm2_20250212_AB.shp`
   - **Raster layer:** `tcd_pop_2025_CN_100m_R2025A_v1.tif`
   - **Raster band:** only 1 possible selection
   - **Output column prefix:** `pop_total_`
   - **Statistics ot calculate:** `Sum`
   - **Output file name:** `pop_total_adm2`

Then, run an `Intersection` between the district boundaries with the total population information, and the service-area polygon. This step splits the single accessibility area into separate pieces that align with the district boundaries. 

2. In the **Processing Toolbox**, search for the tool **Intersection** and open it.
   - **Input layer:** `pop_total_adm2`
   - **Overlay layer:** `access_vaccination_points`
   - **Output file name:** `adm2_access_vaccination_points`
   - Then run the algorithm. The output will be the access-to-vaccination geometry with the district information added. In other words, the single access area is split into multiple parts where it intersects district boundaries, assigning each portion to the corresponding district.

With these intersected geometries, we can then calculate how many people fall within the 2-hour access zone across all districts, providing an estimate of district-level population coverage for vaccination services.
::::{grid} 2

:::{grid-item}
```{figure} /fig/pub_health_chad_intersection.png
---
name: 
width: 400
---
Intersection Operation 
```
:::

:::{grid-item} 

Smaller circles correspond to hospitals with few beds, while larger circles indicate facilities with higher capacity.
```{figure} /fig/pub_health_chad_intersection_results.png
---
name: Intersection Operation Results
width: 100
---
Intersection Operation Results
```
:::
::::



3. In the **Processing Toolbox**, now search again for the tool **Zonal Statistics** and open it.
   - **Raster layer:** `tcd_pop_2025_CN_100m_R2025A_v1.tif`
   - **Vector layer containing zones:** `adm2_access_vaccination_points`
   - **Statistics to calculate:** `Sum`
   - **Output column prefix:** `pop_vaccination_`
   - **Output file name:** `population_within_isochrones`
```{figure} /fig/pub_health_chad_intersection_zonal_statistics.png
---
name: Intersection Zonal Statistics
width: 100
---
Intersection Zonal Statistics
```
:::

   

Now we have calculated the total population located within the 2-hour travel-time access area (plus the buffered area), representing the population that can be reached for vaccination within each district.

4. In a final step we will estimate the number of people living more than 2 hours away from the nearest vaccination facility — a key metric for identifying areas where **mobile vaccination teams** or **temporary outreach sites** may be needed.
   - Open the Attribute table and access the Field Calculator
   - Give the Output field name `pop_beyond_2h`
   - Output field type will be `Decimal Number (real)`
   - And the expression
   ```
   "pop_total_sum" - "pop_vaccination_sum"
   ```
   :::{figure} /fig/en_3.40_m3_ex_3_pop_no_vacc.png
   ---
   name: en_3.40_m3_ex_3_pop_no_vacc
   width: 650 px
   ---
   :::   

---

% THIS IS STILL MISSING

## Task 4: Visualising Accessibility

1. To visualize the `population_within_isochrones` data we need to join it back onto the original admin 2 boundaries to have the original geometry. Open the __Join attributes by field value__ tool:
   - **Input layer:** `tcd_admbnda_adm2_20250212_AB.shp`
   - **Table field:** `ADM2_PCODE`
   - **Input layer 2:** `population_within_isochrones`
   - **Table field 2:** `ADM2_PCODE`
   - **Layer 2 fields to copy:** `pop_total_sum`, `pop_vaccination_sum`, `pop_beyond_2h`
   - **Output file name:** `population_vaccination_adm2`

Now we can visualise both the population that can be reached within 2 hours of a vaccination point and the population living beyond this 2-hour accessibility range.

2. Symbolise the population within 2 hours
   - Select the layer `population_vaccination_adm2` in the Layers panel.
   - Open the Layer Styling panel and switch to `Graduated` symbology.
   - Use the following inputs: `pop_vaccination_sum`, Color ramp: RdYlGn (find it under All Color Ramps), Mode: Equal Count, Classes: 5

3. Symbolise the population beyond 2 hours
   - <kbd>Right-click</kbd> the `population_vaccination_adm2` layer → Duplicate Layer.
   - Open the Layer Styling panel for the duplicate layer and set: Symbology: Graduated, Value: pop_beyond_2h, Color ramp: YlOrRd, Mode: Equal Count, Classes: 5

:::{tip}
The overall map layout follows the same steps as in the previous exercise. For a reminder, see the guide [here](https://giscience.github.io/gis-training-resource-center/content/Module_5/en_qgis_module_5_public_health_ex_2.html#task-7-2-print-layout)
:::

:::{figure} /fig/tcd_map_pop_access_vaccination.png
---
name: tcd_map_pop_access_vaccination
width: 650 px
---
Example map for Measles Vaccination: Population Wihin 2-Hour Access | Chad
:::   

---

## Discussion

The resulting map shows which districts and settlements are effectively served by fixed vaccination points, and which remain outside practical reach. In real-world scenarios, such analysis can help humanitarian planners:
- **Identify underserved areas** and plan **mobile vaccination campaigns**.
- **Estimate resource needs** for outreach teams.

:::{note}
Always interpret accessibility results and specifically estimations with caution — We used public road network data (OCHA), which may not reflect seasonal accessibility or informal paths. Field validation and coordination with local health teams are essential for operational planning.
:::

---


<!--

## Task 2: Installing and Connecting to OpenRouteService

1. If not yet installed, add the **OpenRouteService Plugin**:
   - Go to `Plugins → Manage and Install Plugins…`
   - Search for **OpenRouteService** and click `Install`.
2. Once installed, open the plugin from the toolbar or via `Web → OpenRouteService → Provider Settings`.
3. Create or log in to your [OpenRouteService account](https://openrouteservice.org/dev/#/signup) and obtain a **free API key**.
4. Copy your API key into the plugin under **Settings → API Key**.

---

## Task 3: Creating Isochrones Around Vaccination Points

> In order to calculate accessibility, we will generate travel-time isochrones (zones of equal travel time) around each vaccination facility.

> For this exercise, we will define *populations beyond 120 minutes motorised travel time* as **underserved**.

1. In the **Processing Toolbox**, search for **ORS Tools → Isochrones from Point-Layer**.
2. Open the tool and set the parameters as follows:
   - For **routine vaccination teams** (motorised): 1 hours (≈ 60 minutes) is a practical maximum one-way travel time (also caused due to API Restrictions of the OpenRouteService).
   - **Travel mode:** `driving-car` *(for motorised travel)*
   - **Input point layer:** `tcd_cold_chain_healthsites_points_capacities`
   - **Range type:** `time`
   - **Range (minutes):** `60`
   - **Output layer name:** `Isochrones_vaccination_points`
3. Click `Run`. Once complete, a new polygon layer will appear showing areas reachable within 30, 60, 120, and 240 minutes of travel.

:::{note}
If motorised transport is limited, repeat the process using **`foot-walking`** as the travel profile. This allows you to compare accessibility for populations relying on walking only. For **on-foot access** (caregivers without transport): 30–60 minutes (≈ 3–5 km) is more realistic.
:::

-->

