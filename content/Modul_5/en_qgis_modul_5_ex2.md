# Trigger & Intervention Map for Forecast-based-Action

__🔙[Back to Homepage](/content/intro.md)__

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Aim of the exercise:

This exercise is based on the monitoring and triggering process used by the Somalia Red Cresent Society (SRCS) in the framework of a drought Early Action Protocol (EAP).

Within this exercise, you will build a simplified version of the monitoring and trigger mechanism for the FEWSNET projection pillar.

## Background 

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

For the development of the Somaliland-Somalia Drought Trigger mechanism various datasources were thoroughly analysed.
Finally, the main parameters chosen for the trigger based on the historical impact assessment are the twelve month Standard Precipitation Index (SPI12) and the IPC acute food insecurity classification. The exact data used are the documented and forecasted SPI12 (source: ICPAC) and the forecasted IPC classification (8 month forecast, source: FEWSNET), that is used to calculate a population weighted index of food insecurity. The trigger thresholds for both components were optimised towards the most favourable proportion of hit rate and false alarm rate. The emerging thresholds were <-1 for the SPI12 and >=0,7 for the IPC based index. The triggering is done on district level and per district just one trigger initiation per year is possible.

```{admonition} Trigger Statement
When ICPAC issues a SPI-12 forecast of less than -1 for a district AND the current FEWSNET food insecurity projection reaches at least 0.7 in its 
derived population weighted index in the same district, then we will act in this district. We expect the lead-time to be 90 days.
```



## Relevant Wiki Articles

* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Intersection](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)
* [Zonal Statistics](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)
* [Join Attributes by location (summary](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Tabel functions](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)


## Data

### Food Insecurity Projection data

The drought trigger mechanism is based on two variable monitoring datasets. One of them Food Insecurity projection produced by FEWSNET which is updated ruffly every month.

| Dataset| Source | Description |
| ----- | --- | --- |
|IPC Projections| [FEWSNET](https://fews.net/) | five-phase scale providing common standards for classifying the severity of acute or anticipated acute food insecurity. |

#### What is IPC Food Security Projection Data?
 
The IPC is a commonly acceepted measure and classification to describe the current and anticipated severity of acute food insecurity. 
The classification is based on a convergence of available data and evidence, including indicators related to food consumption, livelihoods, malnutrition and mortality. Food Insecurity is one of the prioritized impacts of droughts in Somalia which is why it is also used for the triggering mechanism, in a population-weighted index. 

Three times a year (February, June, and October) FEWSNET estimates most likely IPC classes for the upcoming 8 month (near-term and mid-term projection), available from 2019-current. The near-term projection is called ML1 and is a projection for the upcoming 4 month, the mid-term projection is called ML2 and projects the IPC classes for the 4 subsequent months. For the triggering ML1 (near-term) as well as ML2 (mid-term) projections will be considered. 

Outlook updates are produced almost every month and are also taken into account.

| Colour| Phase | Descriptions |
| ----- | --- | --- |
|![](/fig/IPC_Class_1.drawio.svg)|1. Minimal   |Households are able to meet essential food and non-food needs without engaging in atypical and unsustainable strategies to access food and income.   |
|![](/fig/IPC_Class_2.drawio.svg)|2. Stressed   |Households have minimally adequate food consumption but are unable to afford some essential non-food expenditures without engaging in stress-coping strategies.  |
|![](/fig/IPC_Class_3.drawio.svg)|3. Crisis   |Households either have food consumption gaps that are reflected by high or above-usual acute malnutrition __OR__ are marginally able to meet minimum food needs but only by depleting essential livelihood assets or through crisis-coping strategies.  |
|![](/fig/IPC_Class_4.drawio.svg)|4. Emergency|Households either have large food consumption gaps which are reflected in very high acute malnutrition and excess mortality; __OR__ are able to mitigate large food consumption gaps but only by employing emergency livelihood strategies and asset liquidation.|
|![](/fig/IPC_Class_5.drawio.svg)|5. Famine |Households have an extreme lack of food and/or other basic needs even after full employment of coping strategies. Starvation, death, destitution, and extremely critical acute malnutrition levels are evident. (For Famine Classification, area needs to have extreme critical levels of acute malnutrition and mortality.)  |

### Training Data

Download the data folder __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Modul_5_Exercise2_Drought_Monitoring_Trigger/Modul_5_Exercise2_Drought_Monitoring_Trigger.zip)__ and save it on your PC. Unzip the .zip file!

For this particular exercise, we will use a combination of pre-processed data and the download of real data from FEWS.net.
The preprocessed datasets are:

| Dataset| Source | Description |
| ----- | --- | --- |
|Adminstrative bounderies | [HDX](https://data.humdata.org/dataset/cod-ab-som?) |The administrative bounderies on level 0-2 for Somalia and Somaliland can be accessed via HDX. For this trigger mechanism we provide the administrative bounderies on level 2 (district level) as a shapefile. We have added the population number for each district derived from Worldpop.|
|Population Counts| [Worldpop](https://hub.worldpop.org/doi/10.5258/SOTON/WP00534) |The worldpop dataset in .geotif rasterformat provides population estimates per hectar for the year 2020 |

Whereas the IPC-Projections data will be downloaded by the participants directly from FEWS.net.

| Dataset| Source | Description |
| ----- | --- | --- |
|IPC Projections| [FEWSNET](https://fews.net/) | five-phase scale providing common standards for classifying the severity of acute or anticipated acute food insecurity. |

## Task


```{Attenation}
Some of the images and videos are not 100 % accurate for this particular exercise since they were take from the real trigger workflow of SRCS, which is more complex.
```

### Step 1: Setting up folder structure 

__Purpose:__ In this step we set up the correct folder structure to make the analysis easier and to ensure consitent results. 

__Tool:__ No special tools or programs are needed

``````{list-table}
:header-rows: 1
:widths: 10 25

* - Instruction
  - Folder Structure
* - 1. Open the Folder “Modul_5_Exercise2_Drought_Monitoring_Trigger"
    2. Open the subfolder "Monitoring"
    3. Copy the Template folder “TEMPLATE_Year_Month” and change the name to the current year and month `2024_01`.
    
  -
    ```{figure} /fig/Exercise_Folder_structure_Drought_Monitoring_Trigger.drawio.svg
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

The Video below shows the process for setting up the folder for decmber 2023.

```{dropdown} Video: Setting up folder structure 
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_folder_setup.mp4"></video>
```

### Step 2: Download of the forecast data


__Purpose:__ 

__Tool:__ Interent Browser

The IPC data will be pulled from the FEWSNET website. FEWS NET publishes IPC data on its website. 
The main data publications plus the updates of the IPC data amount to the publication of new data almost monthly.

### IPC Data

The IPC Projection data is provided and regulary updated on the [FEWSNET Website](https://fews.net/).
On the website you will have to click on Somalia to acess the data. Alternativley, you can  navigate through `Data` -> `Acute Food Insecurity Data` and enter „Somalia". In the menu you will see different dataformats for different timestamps. Once you find out which timestamp is the most current one find the ZIP download. We need the data in shapefile (.shp) format, which is only included in the ZIP file and not provided as single download file. 


```{Warning}
The FEWSNET pages change often !
```

1. Go to [FEWSNET Website](https://fews.net/). Click on `Data` -> `Acute Food Insecurity`.
2. Scroll down. In `Geograhic Area` typ in “Somalia” and click `Apply`
3. Choose the newest dataset.

```{figure} /fig/IPC_Projections_website.png
---
height: 250px
name: FEWSNET IPC - Download IPC Projections
align: center
---
```
4. Download the one with the __ZIP__ Data
5. When you have downloaded the data, right-click on the file and click on `Extract all` -> `Extract`
6. Open the extracted folder and copy the ML1 data in the IPC_ML1 folder you have created in step 1. 
  * The filename is composed of "SO" for Somalia, year and month of the report month e.g `SO_202308_ML1.shp`
  Example path: `.../Modul_5_Exercise2_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/IPC_ML1`
```{Warning}
Make sure to __not__ use the ML1_IDP data which comes in the .zip folder as well!
```

```{Warning}
Remember that you need to copy over all components that the respective [shapefile](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html#vector-data) is composed of. Most probably it has 5 components: .cpg, .dbf, .prj, .shp, and .shx.
```{figure} /fig/IPC_zip.PNG
---
height: 300px
name: Content of .zip file downloaded containing ML1 and ML2 IPC projections
align: center
---
```

```{tip}
On the [main FEWSNET page](https://fews.net/) you can also sign up for information on latest updates via email. For this option scroll down to the end of the page and click on `Sign up for Emails`. You will then get the option to choose updates only for Somalia.

```{figure} /fig/IPC_Newsletter.png
---
height: 60px
name: FEWSNET Newsletter
align: center
---
```


### Step 3: Loading data into QGIS



__Purpose:__ In this step, all the data needed will be loaded into QGIS.

__Tool:__ No specific tools are needed, only QGIS.

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created save the project in the folder you created in Step 1 (e.g. 2022_05). To do that click on `Project` -> `Save as` and navigate to the folder. Give the project the same name as the folder you created (e.g. 2022_05). Then click `Save`
3. Load all input data in QGIS by [drag and drop](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-raster-data-via-drag-and-drop). Click on `Project` -> `Save` 
  * From the folder you created in step 1
    * ML1
  * From the `Fixes_data` folder:
    * district_pop_som
    * WorldPop_som.tif

__Result:__ QGIS project with all necessary data ready to be analysed. 

### Step 4: Intersection of ML 1 data with the district polygons 

__Purpose:__ The goal is to receive polygon layers which share both the borders and the attributes of both input layers.


__Tool:__ [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)


``````{list-table}
:header-rows: 1
:widths: 20 25

* - Instruction
  - Intersection
* - 1. Click on `Vector` -> `Geoprocessing Tools` -> [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)
    2. `Input Layer`: ML 1 
    3. `Overlay layer`: district_pop_sum
    4. Under `Intersection` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_Intersection" and click `Save`
    5. Click `Run`
  -
    ```{figure} /fig/SRCS_Trigger_step_4_Intersection.png
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

__Result:__ After doing this for ML1 you should have one polygon layer,  containing all columns of ML1 and district_pop_sum.

```{Note}
The resulting layer can have more rows than the original layers.
```

```{dropdown} Video: Intersection of ML 1 data with the district polygons 
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_4_Intersection.mp4"></video>
```

### Step 5: Calculation of Population per Intersection Polygon

__Purpose:__ Here we calculate the population in each polygon of the intersection layer from step 4.


__Tool:__  [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)

``````{list-table}
:header-rows: 1
:widths: 20 25

* - Instruction
  - Zonal Statistics
* - 1.  In the `Toolbox` -> Search for [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)
    * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox`
    2. `Input Layer`: "ML1_Intersection" 
    3. `Raster Layer`: "som_ppp_2020_UNadj_constrained.tif"
    4. Statistics to calculate: Only `Sum`
    5.  Under `Zonal Statistics` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_zonal_statistic" and click `Save`
    5. Click `Run
  -
    ```{figure} /fig/SRCS_Trigger_step_5_zonal_statistic.png
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

__Result:__ The result should be the “ML1_zonal_statistic” a polygon layer. This layer should have the same columns in the attribute table like ML1_Intersection __plus__ the column “_sum”, which is the number of people living in the single parts of the polygons.


```{dropdown} Video:  Calculation of Population per Intersection Polygon
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_5_zonal_statistic.mp4"></video>
```
### Step 6: Weighting of the Population based on IPC-Phase


__Purpose:__ The purpose of this step is the weighting of the population in the five IPC phases as described in [IPC Data](https://giscience.github.io/gis-training-resource-center/content/GIS_AA/en_qgis_drought_trigger_somalia.html#ipc-population-weighted-index).

```{Note} 
The IPC Index represents low-population districts equal to high-population districts. No underrepresentation of high food insecurity of small districts occurs.
```

```{dropdown}  IPC-Population Weighted Index

To better operationalise the IPC data a simple population-weigthed index was developed. Relative population numbers are weighted based on the respective IPC class they fallin, in order to give the amount of people in a certain IPC class the importance instead of the IPC class only.
Furthermore, population located in a higher IPC class is more important than population located in a lower class. The index is calculated as follows:

$ IPC\ Index =  Weights \times \frac{District\ Pop\ per\ IPC\ Phase}{Total\ District\ Pop}$

Where the weights are defined as:

| IPC Pahse| Weight |
| ----- | --- |
|IPC 1  |0  |
|IPC 2  |0  |
|IPC 3  |1  |
|IPC 4  |3  |
|IPC 5  |6  |

The IPC Index represents low-population districts equal to high-population districts. No underrepresentation of high food insecurity of small districts occurs.
```
__Tool:__  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)


1. Right-click on the layer “ML1_zonal_statistic”  -> `Open Attribute Table`-> click on [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
2. Check `Create new field`
3. `Output field name`: Name the new column “pop_sum_weighted”
4. `Result field type`: Decimal number (real)
5. Add the code block from Input into the `Expression` field
Click `ok`

```md
CASE

WHEN "ML1" = 3 THEN "_sum" * 1
WHEN "ML1" = 4 THEN "_sum" * 3
WHEN "ML1" = 5 THEN "_sum" * 6
ELSE "_sum"

END
```
6.  When you are down click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#attribute-table-data-editing)). 

## Step 8: Calculation of Population Proportion per Intersection Polygon

__Purpose:__ In this step we calculating the [IPC-Population Weighted Index](https://giscience.github.io/gis-training-resource-center/content/GIS_AA/en_qgis_drought_trigger_somalia.html#ipc-population-weighted-index) for every small part of the polygon layer. 


__Tool:__[`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)

1. Right-click on "ML1_zonal_statistic" layer -> “Attribute Table”-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png)to open the field calculator
2. Check `Create new field`
3. `Output field name`: Name the new column “Index_per_IPCPolygon_ML1”
4. `Result field type`: Decimal number (real)
5. Add the code into the `Expression` field
```md
"pop_sum_weighted"/"districtpo"
```
6. Click `ok`
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table and end the editing mode by clicking on ![](/fig/mActionToggleEditing.png)

```{figure} /fig/SRCS_Trigger_step_8_field_calculator.png
---
width: 500px
name: 
align: center
---
```

__Result:__ The layer “ML1_zonal_statistic”  should now have the column “Index_per_IPCPolygon_ML1”. The numbers in this column have to be smaller than in the “district” column.


```{dropdown} Video: Calculation of Population Proportion per Intersection Polygon
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_TRigger_step_8_field_calculator.mp4"></video>
```

### Step 9: Calculate IPC Index per District

__Purpose:__ The purpose of this step is to calculate a population-weighted mean over the IPC classes per district. In this way, the amount of people living in a certain IPC class will be given more importance than just the area affected by a certain IPC class. The result is an IPC Index value for each district.

__Tool:__ `Join attribute by location (summary)`

``````{list-table}
:header-rows: 1
:widths: 20 25

* - Instruction
  - Join attribute by location (summary)
* - 1. In the `Toolbox`-> Search for `Join attribute by location (summary)`
      * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox` 
    2. `Input Layer`: Select your “district_pop_som” layer
    3. `Input Layer 2`: Select “ML1_join” 
    4. `Geometric predicate`: Select “Intersection”
    5. `Field to summarise`: Select “Index_per_IPCPolygon_ML1” 
    6. `Summaries to calculate`: Chose only the option “mean”
    7. Under `Join Layer` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_IPC_Index" and click `Save`
    8. Click `Run`
  -
    ```{figure} /fig/Exercise_trigger_join_attributes_location.png
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

__Result:__ As a result, your layer "ML1_IPC_Index"  should have the column “Index_per_IPCPolygon_ML1_mean”. Furthermore, the number of rows should be the exact number of districts in Somalia and the polygons should have the exact shape of the districts.

```{dropdown} Video: Calculate IPC Index per District
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_9_join_location.mp4"></video>
```
### Step 10: Evaluate Trigger Activation 

__Purpose:__ The purpose of this step is to gain a quick overview of possible trigger activation without having to revise the actual data. Instead we will have a binary column with trigger = yes or trigger=no values.

__Tool:__ [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)

1. Right-click on "ML1_IPC_Index" layer -> `Attribute Table`-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
2. Check `Create new field`
3. `Output field name`: Name the new column “Trigger_activation”
4. `Result field type`: Text (string)
5. Add the code below into the `Expression` field
6. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table and end the editing mode by clicking on ![](/fig/mActionToggleEditing.png)
``````{list-table}
:header-rows: 1
:widths: 15

* - Code
* - ```md
    CASE

    WHEN "Index_per_IPCPolygon_ML1_mean" >0.7 
    THEN 'yes'
    ELSE 'no'

    END
    ```
``````
6. Click `ok`
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table and end the editing mode by clicking on ![](/fig/mActionToggleEditing.png)

__Result:__ A layer with all districts of Somalia with a column of "Yes" and "No" values indicating whether the trigger levels have been reached or not.

```{figure} /fig/Exercise_trigger_evaluation.png
---
width: 600px
name: 
align: center
---
```

```{dropdown} Video: Evaluate Trigger Activation 
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_13_trigger_activation.mp4"></video>
```

### Step 11.: Visualisation of results

__Purpose:__ Definition of how features are represented visually on the map.

__Tool:__ [Symbology](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_I.html#symbology-for-vector-data)

__Trigger Activation__

1. Right cklick on the “ML1_IPC_Index” layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger/layer_styles” folder and select the file __“Style_Trigger_Activation_ex.qml”__.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” Window click `Apply` and `OK`

```{dropdown} Info: Trigger Activation Layer
You will now see districts where no trigger is activated in green and districts with trigger activation in pink.

The “Style_Trigger_Activation.qml” style layer is configured to show the district names only where the trigger is actually activated. If there is no trigger activation you can activate the admin 1 boundary layer for better map orientation (see __Administrative 2 Boundaries__ below)

```{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: 
align: center
---
```

__Administrative 2 Boundaries (Regions)__

6. Right click on the "Som_admin1_regions_UNDP.gqkp" (Regions) layer -> `Properties` -> `Symbology`
7. In the down left corner click on `Style` -> `Load Style`
8. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger/layer_styles” folder and select the file __“SOM_regions_style_ex.qml”__.
9. Click `Open`. Then click on `Load Style` 
10. Back in the “Layer Properties” Window click `Apply` and `OK`
11. Add a the OpenStreetMap basemap by clicking on `Layer` -> `Add Layer` -> `Add XYZ layer...` -> Select the OpenStreetMap. Click `Add`. ([Wiki basemap](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html?highlight=osm#basemaps))
12. Place the OpenStreetMap basemap on the bottom.
13. Delet all layers __exept__:
    * Trigger_activation
    * Som_admin1_regions_UNDP
    * OpenStreetMap

```{dropdown} Video: Visualisation of results
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Trigger_model_style.mp4"></video>
```

``````{list-table}
:header-rows: 1
:widths: 20 20

* - Intervention Map __without__ Trigger activation
  - Intervention Map __with__ Trigger activation
* - 
    ```{figure} /fig/Map_no_trigger.PNG
    ---
    width: 1000px
    name: 
    align: center
    ---
    ```
    
  -
    ```{figure} /fig/Map_yes_trigger.PNG
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````

```{Attention}
Remember the [layer concept](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept.html?highlight=layer#layer-concept) and make sure the basemap layer is at the bottom of your layers panel.
```

### Step 12: Making print map

__Purpose:__ Viualization of the map features in a printable map layout

__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)


1. If not done before, delet all layers expect __Trigger_activation__, __Som_admin1_regions_UNDP__ and __OpenStreetMap__
2. Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "2024_01".
3. Go the the `Modul_5_Exercise2_Drought_Monitoring_Trigger` folder and drag and drop the file `Trigger_activation_Intervention_map_ex.qpt` in the print layout
4. Change the date to the current date by clicking on "Further map info…" in the items panel. Click on the `Item Properties` tab and scroll down. Here you can change the date in the `Main Properties` field.
5. If necessary, adjust the lgend by clicking on the legend in the  `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there check if you have to open the dropdown. Make sure `Auto update` is not checked.
    * Remove all itemes in the legend be clicking on the item and then on the red minus icon below.
    * Add __Trigger_activation__ to the legend by clicking on the green plus and click on the layer and click `ok`
    * Add __Som_admin1_regions_UNDP__ to the legend by clicking on the green plus and click on the layer and click `ok`
 

```{dropdown} Video: Making print map
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
```

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```

You can also adapt the template to your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#print-layout).

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```

### Step 13.: Exporting Map 


__Purpose:__ Export the designed and finalized map layout in order tp print it as a pdf or format of your choice.


__Tool:__ [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

When you have finished the design of you map you can export it as pdf or image file in different datafromats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Chose the __Result__ folder in the folder you have created in step 1. Give the file the name of the project e.g 2022_04
3.  Click on `Save`
4. The window "Image Export Options" will appear. Click `Save`
Now the image can be found in the result folder in the folder you created in Step 1


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Chose the __Result__ folder in the folder you have created in step 1. Give the file the name of the project e.g 2022_04
3.  Click on `Save`
4. The window "PDF Export Options" will appear.  For the best results, select the `lossless` image compression.
5. Click `Save`
Now the image can be found in the result folder in the folder you created in Step 1


```{figure} /fig/map_output_example_ex.png
---
width: 1000px
name: 
align: center
---
```