# Exercise 3: Assessing Accessibility to Vaccination Services

## Background

Following your analysis of measles incidence rates per district, the Ministry of Health now wants to identify which populations have limited access to vaccination services. In this exercise, you will use the **OpenRouteService (ORS)** tools developed by HeiGIT to model accessibility and determine how many people live **beyond a reasonable travel distance** from a vaccination point.

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

To do this, you will generate travel-time isochrones around vaccination points and then use WorldPop data to estimate the population covered within each accessibility zone. This approach simplifies reality but provides a useful approximation of service coverage.

---

## Task 1: Opening the Project and Preparing the Data

1. Open your QGIS project from **Exercise 2**.
2. Verify that the following layers are loaded:
   - `tcd_admbnda_adm2_20250212_AB.shp` (district boundaries)
   - `tcd_healthsites_points_capacities.gpkg` (vaccination points)
   - `tcd_pop_2025_CN_100m_R2025A_v1.tif` (population raster)
   -  `tcd_roads_ocha.shp` (road network)
3. Now we need to filter the `tcd_healthsites_points_capacities` layer to only include healthsites with a cold chain for vaccine storage. We will do so by opening the "Attribute table" and clicking on "Select features using an expression" ![](mActionSelectbyExpression.png).
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
   - For the Vector layer representing network select `tcd_roads_ocha`
   - Path type to calculate should be `Fastest`
   - Vector layer with start points is `tcd_cold_chain_healthsites_points_capacities`
   - Travel cost will be `2` as the information for the fastest path type is given by hours. So 2 will correspond to 2 hours of travel time
   - The speed will be left at the Default speed of 50 km/h
   :::{figure} /fig/en_3.40_m3_ex_3_service_area.png
   ---
   name: en_3.40_m3_ex_3_service_area
   width: 650 px
   ---
   :::
3. The output will be called `Service area (lines)` and will include the road network accessible from a given healthsite within 2 hours travel time at a travel speed of 50 km/h. To further process this data we need to reproject it to a metric CRS that depicts Chad without distorting too much. Select __EPSG: 102022__ and reproject the `Service area (lines)`. The output layer will be called `Reprojected`.
4. To give a more realistic assessment of the accessibility area around the vaccination points we will buffer the `Service area (lines)`. Before running this operation, we will "Dissolve" the Service area lines to create one geometry. 
   - In Dissolve fields, we won't select anything
5. Now we can buffer the Dissolved Service area lines by 2 km, which corresponds to around 30 minutes of walking.
   - Input layer will be the result of the dissolving process (likely called `Dissolved`)
   - Distance should be 2 kilometers
   :::{figure} /fig/en_3.40_m3_ex_3_access_vaccination.png
   ---
   name: en_3.40_m3_ex_3_access_vaccination
   width: 650 px
   ---
   :::

---

## Task 4: Calculating Population Coverage Using WorldPop

1. In the **Processing Toolbox**, search for the tool **Zonal Statistics** and open it.
2. Configure the tool:
   - **Raster layer:** `tcd_pop_2025_CN_100m_R2025A_v1.tif`
   - **Vector layer containing zones:** `Isochrones_vaccination_points`
   - **Statistics to calculate:** `Sum`
   - **Output column prefix:** `pop_vaccination_`
   - **Output file name:** `population_within_isochrones.gpkg`
3. Run the tool.

This will calculate the total population within each travel-time zone.

4. Next, compute the total population per district using **Zonal Statistics** again, but use:
   - **Zones:** `tcd_admbnda_adm2_20250212_AB.shp`
   - **Output column prefix:** `pop_total_`
   - **Statistic:** `Sum`
5. Use the **Field Calculator** to compute the population *beyond* 120 minutes:
   ```
   "pop_total_sum" - "pop_240_sum"
   ```
   Rename the resulting field to `pop_beyond_2h`.

:::{tip}
This approach allows you to estimate the number of people living more than 2 hours away from the nearest vaccination facility — a key metric for identifying areas where **mobile vaccination teams** or **temporary outreach sites** may be needed.
:::

---

## Task 6: Visualising Accessibility

1. Symbolise your `Isochrones_vaccination_points` layer using graduated colours by travel time.
2. Overlay the population raster to highlight populated areas outside the 120-minute zone.
3. Optionally, apply hillshade from a Digital Elevation Model (DEM) for terrain context.
4. Label districts by their `pop_beyond_2h` value to identify priority areas for vaccination campaigns.

---

## Discussion

The resulting map shows which districts and settlements are effectively served by fixed vaccination points, and which remain outside practical reach. In real-world scenarios, such analysis can help humanitarian planners:
- **Identify underserved areas** and plan **mobile vaccination campaigns**.
- **Estimate resource needs** for outreach teams.
- **Compare access under different travel scenarios** (e.g. walking vs motorised).

:::{note}
Always interpret accessibility results with caution — **OpenRouteService** uses public road network data (OpenStreetMap), which may not reflect seasonal accessibility or informal paths. Field validation and coordination with local health teams are essential for operational planning.
:::

---

✅ **Deliverable:**  
A map and summary table showing the population within 30, 60, 120, and 240 minutes of travel to vaccination sites, and the proportion of population living beyond the 120-minute threshold per district.


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

