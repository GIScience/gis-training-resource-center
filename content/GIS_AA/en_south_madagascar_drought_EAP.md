# Drought EAP for southern Madagascar: Hazard and Vulnerability analysis


:::{topic} Context
For the Drought Early Action Protocol (EAP) by the Malagasy Red Cross (CRM), we developed a hazard and vulnerability analysis. The result ware reproducible maps showing a composite drought vulnerability combining hazard recurrence (rainfall deficits) and documented humanitarian impacts (IPC phase 3 or above). The two indicators are combined and classified into three levels of drought vulnerability (High/Medium/Low).

__Geographic focus:__ Androy, Anosy, Atsimo-Andrefana

:::

:::{card}
__QGIS Project__
^^^
The QGIS project and the datasets used in this project can be found here: 
[MDG_DROUGHT_EAP.qgz](link)

Note: Copyrighted datasets (CHIRPS and IPC) must be downloaded from the respective publishers. 

:::


## Part 1: A historical rainfall deficit recurrence map (CHIRPS-based, 2000–2024) aggregated at district level.
 

__Objective:__

Show spatial recurrence of significant rainfall deficits in southern Madagascar over a long reference period (ideally 2000–2024).
Suggested approach (open to your advice):

- Use CHIRPS monthly or seasonal data.
- Calculate anomalies relative to long-term averages.
- Define a threshold for severe deficit (e.g. ≤ -30% or ≤ -40%).
- Count frequency of deficit events over the reference period.
- Aggregate at district level (ADM2).

__Output:__

- District-level choropleth (High / Medium / Low recurrence).
- Clear, simple methodological note explaining threshold and aggregation.


__Questions:__

- CHIRPS monthly or seasonal data: How to define seasons? -> look at rain seasons in mdg or simply DJF, MAM


### Workflow

1. Use GEE to aggregate the daily CHIRPS v3 to monthly totals for the time period 2000 to 2024.
2. Calculate the monthly climatology (mean per month across all years).
3. Compute the percentage anomaly per month  %anom=100×(P−Pˉm​)/Pˉm​ (per cell)
4. Flag severe deficit months (e.g. <= -30%)
6. Count how often each district is in deficit (frequency or count) = recurrence value
7. Aggregate to admin level:
    - __Options:__
        - A: Mean pixel recurrence (can also be normalised by dividing with the total number of months -> %)
        - B: Percent of area affected (need to define a threshhold of recurring deficit months, e.g., more than 30 deficit month in time period)
            - "65% of district had more than 30 deficit months".

- Monthly rainfall totals were derived from CHIRP v3 daily data hosted on Google Earth Engine. Monthly anomalies were calculated relative to the 2000–2024 climatological mean for each calendar month. Rainfall deficit events were defined as months with precipitation ≤30% (moderate) or ≤40% (severe) below the long-term mean. The frequency of deficit events was aggregated at district (ADM2) level to characterize historical recurrence.

- Rainfall deficit recurrence was defined as the number of months between 2000 and 2024 in which monthly rainfall fell below the deficit threshold. Recurrence was first calculated at the pixel level and then spatially averaged within administrative districts to characterize the typical frequency of deficit conditions across each district.

:::{card}
__Calculated indicators__
^^^
| Level | Variable           | Interpretation                         |
| ----- | ------------------ | -------------------------------------- |
| Pixel | (D_t(x))           | Deficit this month? (0/1)              |
| Pixel | (R(x))             | # of deficit months at that location   |
| ADM2  | mean (R(x))        | Typical deficit recurrence in district |
| ADM2  | % area ≥ threshold | Spatial extent of recurrent deficits   |
:::


8. Select thresholds for choropleth map
    - quantiles: 3 classes (high/medium/low)
    - absolute thresholds: 


__Output:__

- a district layer with fields:
    - `def_count`: number of deficit months, 2000-2024
    - `def_freq`: def count / number of months
    - maybe: counts by season (DJF, MAM, etc.) 