# Exercise 1: Creating an overview map of the health system

## Background 

Over the past month, health authorities in Chad have reported a surge in measles cases, particularly in Mandoul, Mayo-Kebbi Est, and Logone Oriental regions. The surveillance unit has provided line-list data and existing health facility data. Your first task is to create a base map showing health facility distribution and classify them by service capacity to understand the available response infrastructure.

## Available Data


| Dataset name | Original title | Publisher | Downloaded from | 
| :-------------- | :----------------- |:----------------- |:----------------- |
| `tcd_admbnda_adm0_20250212_AB.shp` (Polygons) | Chad Subnational Administrative Boundaries (level 0: country) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm1_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 1: regions) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm2_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 2: province) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd)
| `hotosm_tcd_health_facilities_points.csv` (Points) | Chad Health Facilities (OpenStreetMap Export) | Humanitarian OpenStreetMap Team | [HOTOSM](https://data.humdata.org/dataset/hotosm_tcd_health_facilities) | 
| `Healthsite_capacities.csv` | Healthsite Capacities | HeiGIT | This is a fictional dataset generated for the purpose of this exercise. | 

---

## Tasks

### Task 1: Creating a new QGIS project

1. Open QGIS and create a new project.
2. Save the project via `Project` → `Save As...`. Navigate to the folder for this training and save it in the `/project` subfolder. Give it a nam and click `Save`. 

### Task 2: Importing the datasets

3. [Import the following datasets](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop) via drag-and-drop:
    - `tcd_admbnda_adm0_20250212_AB.shp`
    - `tcd_admbnda_adm1_20250212_AB.shp`
    - `tcd_admbnda_adm2_20250212_AB.shp`
4. The file `hotosm_tcd_health_facilities_points.csv` contains point data, but it is in a delimited text format. QGIS won't automatically recognise the geographic information and display the dataset as points. We need to import it as a [delimited text layer]():
    - In the top bar, click on `Layer` → `Add Layer` → `Add Delimited Text Layer...`. A new window will open. Here we need to specify the file, the file format and define the geometry information
    - To the right of the `File name`-field, click on the ![](/fig/Three_points.png) three points to open the file browser. 
    - Navigate to the data input folder and select the file `hotosm_tcd_health_facilities_points.csv`. Click `Open`.
    - Make sure that QGIS uses the correct delimiter (e.g., comma, tab, semicolon, etc.). If it is the correct delimiter, a preview of the datatable should appear in the Sample Data field. 
    - Specify the `X-` and `Y-field` by selecting the respective column. 
    - Click `Add`. The healthsites should now appear as points on your map canvas. 


:::{caution}

Imported files are not saved within the QGIS project. If you move or delete the original file, QGIS will no longer find the respective dataset. 

:::

## Task 4: The layers panel and the layer concept

5. Once we've imported all the relevant layers, lets start by arranging the layers logically so we can work with them more easily. On the left, there is the `Layers`-panel. Here you can see all the datasets we've imported so far. 
    - QGIS displays geodata in layers, where each dataset is represented in one layer. The layers are stacked on top of each other. 
    - Lets arrange the layers so we work with them more easily:
        - The ADM0-layer should go at the bottom, followed by ADM1, then ADM2.
        - The healthsites should go on top. 
6. Lets investigate the layers that we have added so far. Each vector layer has an attribute table, where each row represents a geometric feature on the map canvas.
    - Open the attribute table by <kbd>right-clicking</kbd> on the ADM2 layer in the layers panel on the left → `Open Attribute Table`.
    - A new window will open. This is the attribute table. It shows the vector layer in a tabular format, allowing you to see the attribute values, sort the table, and edit the values using the tools in the top bar. 
    - Take a look at the different columns in the attribute table. What do they show?
    - Try sorting the attribute table by clicking on the ![](/fig/sort.png)
    - Open the attribute table for the layer `hotosm_tcd_health_facilities_points` and familiarise yourself with the data. 


## Task 5: Enriching the Healthsites dataset

In this step, we want to enrich the layer containing the healthsites with additional data on the capacity of the healthsites. The layer `Healthsite_capacities.csv` contains information about the bed capacity in the pediatric care unit as well as the cold chain capacity. This information is valuable to identify the capacity of the health sector to treat acute measles cases and coordinate a vaccination campaign. However, the dataset does not contain any geographic coordinates, so QGIS can't 

:::{admonition} Gathering the information on capacities

In a realistic scenario, ...

:::

1. Let's import the `Healthsite_capacities.csv` into your QGIS project:
    - In the top bar, navigate to `Layer` → `Add Layer` → `Add Delimited Text Layer...`
    - To the right of the `File name`-field, click on the ![](/fig/Three_points.png) three points and navigate to the `data/input/healthsite_capacities.csv` file and click `Open`.
    - In the import window, you will see sample data in the sample data field. Take a look at the columns and data available. What kind of data is present in each column? Unfortunately, there are no coordinates for the individual healthsites. 
    - There are no columns with the coordinates in this datatable. Under `Geometry Definition` select `No geometry (attribute only table)`.
    - Click `Add`. The layer will appear in your layers tab as a data table, but will not be shown in the map canvas.
2. Let's investigate the capacities table further. 
    - <kbd>Right-click</kbd> on the layer and open the attribute table. 
    - In the top bar, you can see how many entries the dataset contains (*148 features*)
    - The datatable includes a column called "name" which contains the name of the health facilities. These names are the same names that are also stored in the healthsites point layer we imported earlier.
    - This means that we can join both tables using the attribute values of the "name"-column.
3. In the [processing toolbox](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html#toolbox-toolbars), search for the tool `Join attributes by field value` and open it by <kbd>double-clicking</kbd> on it. 
    - A new window will open. Here we can specify the parameters for the `Join attributes by field value`-tool.
    ```{figure} /fig/en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value.png
    ---
    width: 550 px
    name: en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value
    ---
    Setting the parameters for the "Join Attributes by field value"-tool.
    ```
    - As `Input Layer`, select the 






4. Import the administrative boundaries, the road network and the healthsites to the project.
5. Take the time to familiarise yourself with the different datasets by opening the attribute table. 
6. Order the layers in a logical way (e.g., polygons at the bottom, lines in the middle, points on top).
7. Import the healthsites capacities layer. 
8. Join 



Now, lets configure the "Project Home" in the browser panel.

3. In the browser panel on the left, <kbd>right-click</kbd> on `Project Home` → `Set Project Home...` and set the project home folder to the training folder (with the subfolders `/data`, `/project`, etc.). Now you will be able to access all the datasets for this training through the browser.

:::{note}
Working with the browser panel allows a much quicker access to the files and keeps the folder view organised when working with shapefiles. 

:::
