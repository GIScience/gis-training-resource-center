# Exercise 1: Creating an overview map of the health system and vaccination coverage

% MISSING:  - MAKE ENRICHED DATASET PERMANENT
%           - BASEMAP
%           - SMALL SELECTION EXPORT/QUERIES?
%           - PROJECTIONS
%           - ADD SMALLER EASIER EXERCISES EARLIER (INCLUDING IMPORTING DATA SO HERE WE CAN INTRODUCE THE PROJECT  HOME)
%           - ADD MORE PICTURES
%           - REMOVE STEPS TO CLEAN HEALTHSITES AS HEALTHSITES WITHOUT INFORMATION COULD STILL BE GOOD; E.G., TO REACH OUT
%           - ADD STEP FOR COUNT POINTS IN POLYGONS FOR HEALTHSITES
%           - ADD STEP FOR JOIN BY LOCATION
%           - MAKE THEM PLAN MEASLES VACCINATION CAMPAIGN
%               - WHERE TO PUT VACCINATION CENTERS WITH HOW MUCH POP TO SERVE
%               - WHERE TO DEPLOY MOBILE VACCINATION CENTERS -> DIGITISATION
%           - IM COORDINATION INSRTUCTED TO GET DATA ON HEALTHSITE CAPACITIES
%           - MAKE THEM DOWNLOAD HDX
%           - ADD SMALL STEPS UNDER DROPDOWN, AS NOTES, ETC. 

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
| `measles_vaccination_coverage.csv` | Measles vaccination coverage | HeiGIT | This is a fictional dataset generated for the purpose of this exercise. | 

:::{note}

In this exercise, we will download real datasets from the [Humanitarian Data Exchange (HDX)](humdata.org) to identify and analyse relevant information. However, the Healthsite Capacities and Vaccination Coverage datasets used here are fictional and created solely for training purposes. They do not represent real-world data.

:::


---

## Tasks

### Task 1: Setting up the folder structure and creating a new QGIS project

:::{admonition} Standard Folder Structure
:class: tip

The single most important geodata management practice is to use a standardised folder structure that contains all parts of the QGIS project. We will save all of our data that we use or create within our QGIS project inside of this folder structure.
The paths from a QGIS project to the geodata are by default relative. This means when the data and the project are in a fixed folder structure, you can move the whole structure without impacting the QGIS project or the paths to the data.

A standard folder structure has two principal advantages:
1. If we share the whole project folder, we can expect the project to run without problems on a different computer.
2. The folder structure supports the proper organisation of project data and helps ensure the QGIS project will work as intended.
:::

1. Create a new folder on your computer with the name "GIS_Training_Public_Health_Day_1-2". In the folder create the following folder structure:

```
GIS_Training_Public_Health
├── project
├── results
├── styles
└── data
    ├── input
    ├── interim
    └── output
```

1. Open QGIS and create a new project.
2. Save the project via `Project` → `Save As...`. Navigate to the folder for this training and save it in the `/project` subfolder. Give it a name (e.g., `GIS_Training_Public_Health_Part_1`) and click `Save`. 
3. Now we should set up the Project CRS.
    - In the bottom right corner of the QGIS window, click on the ![](/fig/3.40_projection_icon.png) Projection icon. Let's choose a metric CRS that depicts Chad without distorting too much. For this exercise, we will use __"Albers Equal Area Conic" (EPSG: 102022)__. In the `Filter` bar, enter the name or the EPSG number. The CRS should appear in the "Prefedined Coordinate Reference Systems" Box. Select it and click `Apply` and `OK`. 
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_project_crs.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_project_crs.png
    width: 450 px
    ---
    Setting the Project CRS in QGIS
    :::

::::{admonition} How to choose the correct CRS
:class: dropdown, note

Choosing a suitable Coordinate Reference System for your GIS project is crucial. In general, you want to use a CRS that best displays your area of interest. You want to choose a Secondly, you need to think about what kind of calculations you plan to do in your project. CRS exist in two varieties: geographic and metric coordinate reference systems. Geographic CRS use longitude and latitude (degrees) as their coordinates and units of measurements. These are angular measurements and don't depict distances linearly. Metric coordinate reference systems use coordinates that are given in __linear units of measurements__ (such as meters), which means they represent actual distances on the Earth's surface. Metric coordinate reference systems, such as UTM, are designed for local and regional mapping and can introduce distortion when applied to larger areas. For very large regions, projections like Albers Equal Area or Mercator are often used to reduce distortion

If you wish to perform distance calculations, you should use a metric CRS. 

If you want to know more about Projections and Coordinate Reference Systems, check out this __[module chapter](/content/Module_2/en_qgis_projections.md)__.

::::


:::{attention}

The project CRS determines which coordinate reference system is being used to display the geodata on the QGIS map canvas. However, it does not change the CRS of layers. Each layer, or dataset, is encoded with a CRS. QGIS reprojects these layers "on the fly" to display layers with different CRS on the map canvas. This does not change the units of measurements or distortion of the actual layers. To perform distance calculations, you will need to [reproject the layer](/content/wiki/en_qgis_projections_wiki.md) to a metric coordinate reference system. 

Setting the Project CRS to your desired CRS can help you choosing the correct CRS quicker when running algorithms. 
:::
% SET UP PROJECT HOME IN NEXT EXERCISE


### Task 2: Downloading the relevant data

1. In your browser, head over to __humdata.org__ 
2. Search for the following datasets 
    - Chad Administrative Boundaries (OCHA): ADM0, ADM1, ADM2 
    - Chad Health Facilities (OpenStreetMap Export)
    - Chad Roads (OCHA)
:::{figure} /fig/en_m3_ex_8_public_health_part_1_hdx_search.png
---
width: 600 px
name: en_m3_ex_8_public_health_part_1_hdx_search
---
:::
3. Download the layers.
    - On the download page, you can usually select different data formats. The formats are indicated by their file endings (e.g., `.shp`, `.gpkg`, `.gdb`)
    - Choose the following formats: 
        - Chad Administrative Boundaries (OCHA): __Shapefile__
        - Chad Health Facilities (OpenStreetMap Export): __GeoPackage__ for __Points__, we don't need the polygons information for this example
        - Chad Roads (OCHA): __Shapefile__
        :::{figure} /fig/en_m3_ex_8_public_health_part_1_hdx_data_formats.png
        ---
        name: en_m3_ex_8_public_health_part_1_hdx_data_formats
        width: 600 px
        ---
        :::
4. Unzip the folders and make sure to save them in the standard folder structure into the `data/input/`-folder. 


% ADD IMAGE AND EXPAND THIS SECTION: DONE


### Task 2: Importing the datasets

3. In your QGIS, project, [import the following datasets](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop) via drag-and-drop:
    - `tcd_admbnda_adm0_20250212_AB.shp`
    - `tcd_admbnda_adm1_20250212_AB.shp`
    - `tcd_admbnda_adm2_20250212_AB.shp`
    - `hotosm_tcd_health_facilities_points_gpkg.gpkg`
    - `tcd_trs_roads_OCHA.shp`
::::{margin}
:::{tip}
A shapefile consists of several, interrelated files. The geometric information is stored in the `.shp`-file. To make the import process easier, you can order the folder by "File type" and only drag the  
:::
::::

:::{dropdown} Video: Importing Shapefiles into a QGIS project via drag-and-drop
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

% THIS STEP NEEDS REVISING: THEY ARE DOWNLOADING THE DATASET THEMSELVES AS GEOPACKAGE

% THE FOLLOWING SECTION IS NOT NEEDED THEN?

<!--
4. The file `hotosm_tcd_health_facilities_points.csv` contains point data, but it is in a delimited text format. QGIS won't automatically recognise the geographic information and display the dataset as points. We need to import it as a [delimited text layer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-import):
    - In the top bar, click on `Layer` → `Add Layer` → `Add Delimited Text Layer...`. A new window will open. Here we need to specify the file, the file format and define the geometry information
    - To the right of the `File name`-field, click on the ![](/fig/Three_points.png) three points to open the file browser. 
    - Navigate to the data input folder and select the file `hotosm_tcd_health_facilities_points.csv`. Click `Open`.
    - Make sure that QGIS uses the correct delimiter (e.g., comma, tab, semicolon, etc.). If it is the correct delimiter, a preview of the datatable should appear in the Sample Data field. 
    - Specify the `X-` and `Y-field` by selecting the respective column. 
    - Click `Add`. The healthsites should now appear as points on your map canvas. 

:::{dropdown} Video: Importing CSV files via the Data Source Manager
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>
:::
-->

:::{attention}

Imported files __are not saved within__ the QGIS project. If you move or delete the original file, QGIS will no longer find the respective dataset. 

:::

### Task 3: The layers panel and the layer concept

5. Once we've imported all the relevant layers, lets start by arranging the layers logically so we can work with them more easily. On the left, there is the `Layers`-panel. Here you can see all the datasets we've imported so far. 
    - QGIS displays geodata in layers, where each dataset is represented in one layer. The layers are stacked on top of each other. 
    - Lets arrange the layers so we work with them more easily:
        - The ADM0-layer should go at the bottom, followed by ADM1, then ADM2.
        - Then we can add the road network.
        - The healthsites should go on top. 
6. Let's add a basemap:
    - In the file browser, scrool down until you see `XYZ-Tiles`
    - Uncollapse it and <kbd>double-click</kbd> on `OpenStreetMap`. A new layer will be added to your layers-panel, usually at the bottom. Make sure the layer sits at the bottom of the layers panel so all your other layers are visible.

> Your QGIS window should look similar to this (with different colours for the layers).

:::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_ordering_layers.png
---
name: en_3.40_m3_ex_8_pub_health_1_ordering_layers
width: 750 px
---
:::

7. Let's investigate the layers that we have added so far. Each vector layer has an attribute table, where each row represents a geometric feature on the map canvas.
    - Open the attribute table by <kbd>right-clicking</kbd> on the ADM2 layer in the layers panel on the left → `Open Attribute Table`.
    - A new window will open. This is the attribute table. It shows the vector layer in a tabular format, allowing you to see the attribute values, sort the table, and edit the values using the tools in the top bar. 
    - Take a look at the different columns in the attribute table. What do they show?
    - Try sorting the attribute table by clicking on the ![](/fig/sort.png)
    - Open the attribute tables for the layers `hotosm_tcd_health_facilities_points_gpkg` and `tcd_admbnda_adm2_20250212_AB.shp` familiarise yourself with the data. 
    - <kbd>Right-click</kbd> on each layer and select 

<!--- ADD SOME ADDITIONAL INFO HERE?
:::{dropdown} Familiarise yourself with the QGIS interface

Familiarise yourself with the map canvas by zooming in and out (<kbd>Mouse-wheel</kbd> or <kbd>Ctrl</kbd> + <kbd>+</kbd> and <kbd>Ctrl</kbd> + <kbd>-</kbd>). 
Holding <kbd>Space</kbd> automatically switches to the ![](/fig/qgis_pan_map.png) `Pan Map`-tool. 

:::
-->


### Task 4: Joining Vaccination Coverage Data with administrative boundaries

% ADD A DISCLAIMER MAKING TRAINEES THINK WHERE THE DATA CAME FROM

In our `data/input`-folder, we can find a csv file called `vaccination_coverage_adm2`. This file includes the vaccination coverage of both the mcv1 and mcv2 vaccine. Thankfully, the dataset includes the district name (`amd2_name`) and the adm2 pcode. With this information, we can perform a [non-spatial join](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html) in order to add the vaccination coverage data to our district boundaries layer (adm2). 

:::{attention}
Admin Pcodes are best for non-spatial joins in QGIS because they provide unique, standardized identifiers that avoid name mismatches and ensure accurate, reliable data linking.
:::

% ADD ADM2 PCODE TO DATASET AND HAVE THE ADM2 NAMES IN ENGLISH SO THEY CAN'T JOIN WITH ADM2 NAMES BUT USE PCODES: DONE

8. Import the `vaccination_coverage_adm2` into your QGIS project:
    - In the top bar, navigate to `Layer` → `Add Layer` → `Add Delimited Text Layer...`
    - To the right of the `File name`-field, click on the ![](/fig/Three_points.png) three points and navigate to the `data/input/vaccination_coverage.csv` file and click `Open`.
    - In the import window, you will see sample data in the sample data field. Take a look at the columns and data available. What kind of data is present in each column? 
    - Unfortunately, there are no columns with the coordinates for the individual healthsites in this data table. Under `Geometry Definition` select `No geometry (attribute only table)`.
    - Click `Add`. The layer will appear in your layers tab as a data table, but will not be shown in the map canvas.
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_add_vacc_coverage_csv.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_add_vacc_coverage_csv
    width: 700 px
    ---
    :::
9. Investigate the new vaccination coverage further:
    - <kbd>Right-click</kbd> on the new layer and open the attribute table. What information is available? How is the table structured. We can see that we are able to use the column `ADM2_PCODE` to perform a [non-spatial join]
10. In the [processing toolbox](/content/Module_1/en_qgis_start.md#toolbox--toolbars) on the right, search for the tool __"Join attributes by key value"__ and <kbd>double-click</kbd> on it. 
    - A new window will open. Here we can specify the parameters for the `Join attributes by field value`-tool.
    - As "Input layer", select the layer `tcd_admbnda_adm2_20250212_AB`.
    - Under "Table field", select `ADM2_PCODE`.
    - As "Input layer 2", select `vaccination_coverage_adm2`.
    - Under "Table field 2", select `adm2_pcode`.
    - Under "Layer 2 fields to copy", we can select which columns we want to copy. Click on the ![](/fig/Three_points.png) three dots to the right of the field and select `vaccination_rate_mcv1` and `vaccination_rate_mcv2`. Then, click `OK`.
    - Finally, to execute the algorithm, click on `Run`. 
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_join_attr_vaccine_coverage.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_join_attr_vaccine_coverage
    width: 650 px
    ---
    :::
11.  A new layer called "Joined Layer" will appear in the layers panel. To the right of it, you will see a ![](/fig/qgis_3.40_temp_layer.png) symbol. This symbol indicates that the layer is a temporary scratch layer. This means it will be deleted once you close your QGIS project, even if you save the project. __We can save the scratch layer__ by <kbd>right-clicking</kbd> on it and selecting `Make permament...`.
    - A new window will open. Here we need to specify the file location and the layer name. 
    - Leave the `Format` on "GeoPackage".
    - Click on the three dots ![](/fig/Three_points.png), navigate to the `data/interim/`-folder and enter a file name such as `tcd_adm2_vacc_coverage`. Click `Save`. 
    - Enter the same name into `Layer name` field (This will be the name of the layer in the layers panel).
    - Leave the rest as it is and click `Ok`.

> Great! We have added the information on vaccination coverage to our adm2-layer. Now, we can visualise the information by adding a graduated symbology to the layer

### Task 5: Visualising the vaccination coverage

:::{Admonition} Saving your progress
:class: tip

Remember to save your project intermittently to keep your progress. QGIS is constantly being developed by the open source community and is known to crash from time to time. 

:::

Now that we have the vaccination coverage information in our adm2-layer, we can visualise the information in order to understand the spatial distribution of the vaccination coverage. 
::::{margin}
:::{tip}
QGIS offers various ways to [visualise vector data](/content/Module_4/en_qgis_styling_vector_data.md). If you want to learn more about these different methods, check out [module 4](/content/Module_4/en_module_4_overview.md).
:::
::::

::::{margin}
:::{tip}
You can move the properties window to the side so you can see the changes in symbology on your map canvas.
:::
::::
12. Open the symbology tab via the Properties window for the layer: 
    - <kbd>Right-click</kbd> on the `tcd_adm2_vacc_coverage`-layer → `Properties`. 
    - Navigate to "Symbology" in the tab section on the left.
    - Here we can change the symbology method from `Single Symbol` to `Categorized`.
    - Next, we need to select the value which will be used for the classification. Under `Value`, select the column

% ADD CLASSIFICATION STEPS AND RESULT IMAGE

### Task 4: Enriching the Healthsites dataset

% HERE MAYBE HAVE SOME ENTRIES IN THE ADM2 COLUMN USE FRENCH NAMES OR HAVE SOME TYPOS (MAX 2 or 3). BUT SHOW HOW YOU HAVE TO CLEAN DATA TO MAKE THINGS WORK. CHECK THE LOG AND THEN RERUN 

In this step, we want to enrich the layer containing the healthsites with additional data on the capacity of the healthsites. The layer `Healthsite_capacities.csv` contains information about the bed capacity in the pediatric care unit as well as the cold chain capacity. This information is valuable to identify the capacity of the health sector to treat acute measles cases and coordinate a vaccination campaign. 

:::{admonition} Gathering the information on capacities
In a realistic scenario, these data might have been collected during a rapid facility assessment led by the Ministry of Health and Red Cross volunteers.
Because data collection was decentralised and partially paper-based, some facility names differ slightly across datasets (e.g., spelling variants, abbreviations).
When performing joins, pay attention to such inconsistencies.
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
    - As "Input layer", select the layer `hotosm_tcd_health_facilities_points`.
    - Under "Table field", select `name`.
    - As "Input layer 2", select `healthsite_capacities`.
    - Under "Table field 2", select `name`.
    - Under "Layer 2 fields to copy", we can select which columns we want to copy. Click on the ![](/fig/Three_points.png) three dots to the right of the field and select `cold_chain`, `measles_vaccination`, `measles_treatment`, `beds_total`, `pediatric_beds`, `staff_total`, and `remarks`. Then, click `OK`.
    - Finally, to execute the algorithm, click on `Run`. 
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value.png
    ---
    width: 550 px
    name: en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value
    ---
    Setting the parameters for the "Join Attributes by field value"-tool.
    :::
    :::{note}
    After running the algorithm, the window will switch to the log file. Here you can see if the algorithm encountered any problem. In our case, we can see that 149 features were successfully joined while 183 features were unable to be joined. This happens when the identifying value (Table field) is not present in the respective column in layer 2. This can be either because there is not data available, or because there are inconsistencies in the identifying value (e.g., typos, different spelling).
    :::
    - After reviewing the log, we can close the tool-window. A new layer called `Joined layer` should appear in your layers panel. Rename it to "`Healthsites_points_capacities`" and move it to the top. 

> We now have a new point layer with the capacities of relevant healthsites. With this information, we can create a map showing the capacities of the health sector. 

### Task 5: Cleaning the Healthsite Data

% This step is not necessary

4. Let's take a look at the new layer by opening the attribute table. 
    - <kbd>Right-Click</kdd> on the layer and open the attribute table.
    - In the attribute table, if you scroll to the right, you will see the new columns with the information we added using the "join attributes by field value"-tool.
    - Sort the attribute table for the new columns. As you can see, not every feature has information about the capacity. 
    - We can remove the healthsites without additional information, as they are already available in the original dataset.
    - Sort the `total_beds` column ascendingly, so the features with "NULL"-values appear at the top. 
    - Click on row column (on the left), and select the first feature. If selected, the feature should appear blue.
    - Now scroll down until you see the first feature with a value different then "NULL" in the `total_beds` column.
    - Hold <kbd>Shift</kbd> and click on the row number of the last feature with the value NULL. 
    - In the toolbar of the attribute table, click on the ![](/fig/mActionToggleEditing.png) `Toggle Editing Mode`-button to enter the editing mode for the attribute table. 
    - Next, click on ![](/fig/attribute_table_delete_feature.png) `Delete selected features` to delete the points with no capacity information. 
    - Click on ![](/fig/mActionToggleEditing.png) to save and exit the editing mode.

% Adjust the cleaning instructions to decide on cold capacity = NULL

> Our new healthsites point layer now includes only the healthsites for which we received additional data.

### Task 6: Classifying the Healthsites

5. Now, we can classify the healthsites points to indicate which healthsites have a cold chain in order to store measles vaccines.
    - <kbd>Right-click</kbd> on the `Healthsites_points_capacities` and select `Properties`. A new window will open.
    - On the left, navigate to the symbology-tab.
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_classifying_healthpoint_capacity.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_classifying_healthpoint_capacity
    width: 600 px
    ---
    Classifying the symbology for the healthsites in QGIS 3.40
    - Instead of `Single Symbol`, select `Categorised` as the visualisation method.
    - As "Value", select `cold_chain`
    - Next, click on `Classify`. 
    - If you want, you can adjust the symbology for the classes by double clicking on one. 
    - Click `Apply`, then close the properties window. 

% Also remove the NULL values from the categorisation

% Optionally, add DEM here and style the raster layer. This will be used for a overview map. 

### Task 7: Add Digital elevation model





