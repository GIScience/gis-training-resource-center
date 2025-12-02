# Exercise 3: Assessing Accessibility to Vaccination Services

## Background

Following your analysis of measles incidence rates per district, the Ministry of Health now wants to identify which populations have limited access to vaccination services. In this exercise, you will use the **OpenRouteService (ORS)** tools developed by HeiGIT to model accessibility and determine how many people live **beyond a reasonable travel distance** from a vaccination point.

Accessibility to health services is a key determinant of vaccination coverage. In many rural parts of Chad, communities may not have access to motorised transport and rely on walking or infrequent public transport. Thus, distance alone is not always a good measure — **travel time** provides a more realistic assessment.

---

## Available Data

| Dataset name | Description | Source |
| :------------- | :----------- | :----------- |
| `QGIS project from Exercise 2` | Base project with administrative boundaries, health facility capacities, and incidence rates | — |
| `WorldPop_2025_TCD.tif` | 2025 population estimate raster (100 m resolution) | [WorldPop](https://www.worldpop.org) |
| `Healthsites_points_capacities.shp` | Vaccination points (healthsites with cold chain) | Derived in Exercise 1 |
| `tcd_admbnda_adm2_20250212_AB.shp` | Administrative boundaries (district level) | [HDX – OCHA](https://data.humdata.org/dataset/cod-ab-tcd) |

---

## Scenario

You have identified a number of health facilities equipped with a cold chain for vaccine storage. The goal now is to calculate how much of the population is **within reasonable reach** of these facilities, and how many people live **beyond the accessible range**.

To do this, you will use the **OpenRouteService (ORS)** plugin in QGIS to generate travel-time isochrones around vaccination points, and then use **WorldPop** to estimate the population covered within each accessibility zone.

---

## Task 1: Opening the Project and Preparing the Data

1. Open your QGIS project from **Exercise 2**.
2. Verify that the following layers are loaded:
   - `tcd_admbnda_adm2_20250212_AB.shp` (district boundaries)
   - `Healthsites_points_capacities` (vaccination points)
   - `WorldPop_2025_TCD.tif` (population raster)
3. Make sure the coordinate reference system (CRS) of your project is **EPSG:4326 – WGS 84**, as required by OpenRouteService.

---

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

1. In the **Processing Toolbox**, search for **ORS Tools → Isochrones from Point-Layer**.
2. Open the tool and set the parameters as follows:
   - **Travel mode:** `driving-car` *(for motorised travel)*
   - **Input point layer:** `Healthsites_points_capacities`
   - **Range type:** `time`
   - **Range (minutes):** `30, 60, 120, 240`
   - **Dissolve all isochrones:** ✅ (checked)
   - **Output layer name:** `Isochrones_vaccination_points`
3. Click `Run`. Once complete, a new polygon layer will appear showing areas reachable within 30, 60, 120, and 240 minutes of travel.

:::{note}
If motorised transport is limited, repeat the process using **`foot-walking`** as the travel profile. This allows you to compare accessibility for populations relying on walking only.
:::

---

## Task 4: Refining the Accessibility Threshold

In the first version of this analysis, we considered a **50 km distance threshold** as a measure of accessibility. However, 50 km represents 10–14 hours of walking, which is unrealistic for caregivers with children. A **travel-time threshold** provides a better understanding.

- For **routine vaccination teams** (motorised): 2 hours (≈ 120 minutes) is a practical maximum one-way travel time.
- For **on-foot access** (caregivers without transport): 30–60 minutes (≈ 3–5 km) is more realistic.

> For this exercise, we will define *populations beyond 120 minutes motorised travel time* as **underserved**.

---

## Task 5: Calculating Population Coverage Using WorldPop

1. In the **Processing Toolbox**, search for the tool **Zonal Statistics** and open it.
2. Configure the tool:
   - **Raster layer:** `WorldPop_2025_TCD.tif`
   - **Vector layer containing zones:** `Isochrones_vaccination_points`
   - **Statistics to calculate:** `Sum`
   - **Output column prefix:** `pop_`
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

