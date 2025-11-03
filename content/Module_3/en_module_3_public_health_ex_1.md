# Exercise 1: Creating an overview map of the health system

## Background 

Over the past month, health authorities in Chad have reported a surge in measles cases, particularly in Mandoul, Mayo-Kebbi Est, and Logone Oriental regions. The surveillance unit has provided line-list data and existing health facility data. Your first task is to create a base map showing health facility distribution and classify them by service capacity to understand the available response infrastructure.

## Available Data


| Dataset name | Original title | Publisher | Downloaded from | 
| :-------------- | :----------------- |:----------------- |:----------------- |
| `tcd_admbnda_adm0_20250212_AB.shp` (Polygons) | Chad Subnational Administrative Boundaries (level 0: country) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm1_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 1: regions) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm2_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 2: province) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd)
| `hotosm_tcd_health_facilities_points_gpkg.gpkg` (Points) | Chad Health Facilities (OpenStreetMap Export) | Humanitarian OpenStreetMap Team | [HOTOSM](https://data.humdata.org/dataset/hotosm_tcd_health_facilities) | 
| `Healthsite_capacities.csv` | Healthsite Capacities | HeiGIT | This is a fictional dataset generated for the purpose of this exercise. | 

---

## Tasks

1. Open QGIS and create a new project.
2. Save the project via `Project` → `Save As...`. Navigate to the folder for this training and save it in the `/project` subfolder. Give it a name.
3. In the browser panel on the left, <kbd>right-click</kbd> on `Project Home` → `Set Project Home...` and set the project home folder to the training folder (with the subfolders `/data`, `/project`, etc.). Now you will be able to access all the datasets for this training through the browser.
4. Import the administrative boundaries, the road network and the healthsites to the project.
5. Take the time to familiarise yourself with the different datasets by opening the attribute table. 
6. Order the layers in a logical way (e.g., polygons at the bottom, lines in the middle, points on top).
7. Import the healthsites capacities layer. 
8. Join 
