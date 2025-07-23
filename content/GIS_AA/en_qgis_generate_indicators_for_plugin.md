# Generating Risk Indicators

To conduct a meaningful risk assessment with the Risk Assessment QGIS Plugin, it is essential to prepare input indicator files that represent the three main dimensions:

- **Exposure** (mandatory)
- **Vulnerability** (mandatory)
- **Coping Capacity** (optional, but strongly recommended)

This page provides detailed video examples of how to generate each of these indicators using commonly available geospatial data of Ethiopia. The goal is to support users in creating well-structured and valid inputs that align with the plugin’s requirements.

---

## Exposure Indicators

The Expousre indicator was determined by combining the [Aridity index (AI)](https://data.humdata.org/dataset/icpac-geonode-ethiopia-aridity) and the [Palmer Drought Severity Index (PDSI)](https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024) from **HDX** to determine the drought risk of the administrative units.

### Aridity index (AI)

The raster file was opened in QGIS and the mean drought index per administrative unit was calculated using `Zonal statistics`:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/AI_exposure_indicator.mp4"></video>

### Palmer Drought Severity Index (PDSI)

First, the raw data was pivoted and processed in Excel to calculate the average PDSI between 2020 and 2024:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/PDSI_exposure_indicator.mp4"></video>

Then, the processed data was opened in QGIS and added to the exposure indicator file:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/PDSI_exposure_indicator_2.mp4"></video>


## Vulnerability Indicators

The Vulnerability indicator was determined by combining the [ACLED - Conflict Events](https://data.humdata.org/dataset/ethiopia-acled-conflict-data) and [Worldpop](https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-eth) datasets from **HDX**.

### ACLED - Conflict Events

The dataset was processed in QGIS to estimate the population affected by conflict in 2024 using the `Join Attributes by Location (Summary)` tool. Additionally the number of conflicts per administrative unit was calculated (`Count Points in Polygon`):

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/ACLED_vulnerability_indicator.mp4"></video>

### Worldpop

The dataset was processed in QGIS to estimate the vulnerable population (<15 years & >65 years) in 2024 using the `Raster Calculator` and the `Zonal statistics` tools: 
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/worldpop_vulnerability_indicator_1.mp4"></video>

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/worldpop_vulnerability_indicator_2.mp4"></video>



## Coping Capacity Indicators

The Coping Capacity indicator was determined by combining the [Health Facilities](https://data.humdata.org/dataset/hotosm_eth_health_facilities) and the [Education Facilities](https://data.humdata.org/dataset/hotosm_eth_education_facilities) from **HDX**.

### Health and Ecudation Facilities

The dataset was processed in QGIS to count the number of facilities per administrative unit using the `Count Points in Polygon` tool:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Coping_indicator.mp4"></video>

---

## Key Takeaways:
- Ensure the file contains an `ADM_PCODE` column.
- Only include indicator columns relevant for the specific dimension.
- Choose unique column names that describe the content of the column briefly but efficiently.
