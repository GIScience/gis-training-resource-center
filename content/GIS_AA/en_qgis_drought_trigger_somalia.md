# QGIS Trigger Workflow for Somalia 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Somalia Red Cresent Society (SRCS), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow consists of 15 steps of which 9 are automated in the form of a QGIS Model. In this article, we explain how all 15 steps can be done manually. In practice one needs to do only 6 steps manually, the rest is done by the QGSI Model.
The chapter Workflow Automated explains the process and how it is intended in practice. The chapter Workflow Manually is to understand what happens inside of the QGIS Model.

## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

For the development of the Somaliland-Somalia Drought Trigger mechanism various datasources were thoroughly analysed.
Finally, the main parameters chosen for the trigger based on the historical impact assessment are the twelve month Standard Precipitation Index (SPI12) and the IPC acute food insecurity classification. The exact data used are the documented and forecasted SPI12 (source: ICPAC) and the forecasted IPC classification (8 month forecast, source: FEWSNET), that is used to calculate a population weighted index of food insecurity. The trigger thresholds for both components were optimised towards the most favourable proportion of hit rate and false alarm rate. The emerging thresholds were <-1 for the SPI12 and >=0,7 for the IPC based index. The triggering is done on district level and per district just one trigger initiation per year is possible.

## Trigger Statement

When ICPAC issues a SPI-12 forecast of less than -1 for a district AND the current FEWSNET food insecurity projection reaches at least 0.7 in its 
derived population weighted index in the same district, then we will act in this district. We expect the lead-time to be 90 days.


##  Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be fixed in the near term, and variable data which describe the datasets that will be checked for triggering on a monthly base. 

### Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Description |
| ----- | --- | --- |
|Adminstrative bounderies | [HDX](https://data.humdata.org/dataset/cod-ab-som?) |The administrative bounderies on level 0-2 for Somalia and Somaliland can be accessed via HDX. For this trigger mechanism we provide the administrative bounderies on level 2 (district level) as a shapefile. We have added the population number for each district derived from Worldpop.|
|Population Counts| [Worldpop](https://hub.worldpop.org/doi/10.5258/SOTON/WP00534) |The worldpop dataset in .geotif rasterformat provides population estimates per hectar for the year 2020 |



### Monitoring Data

The drought trigger mechanism is based on two variable monitoring datasets updated monthly: The SPI-12 forecast produced by ICPAC and the Food Insecurity projection produced by FEWSNET. The SPI-12 is used to capture hazard forecasts while the Food Insecurity Projection captures the dynamic vulnerability. 
In this way upcoming drought events (SPI) that most probably will lead to food insecurity (IPC) will be captured.

| Dataset| Source | Description |
| ----- | --- | --- |
|SPI-12 forecast| [ICPAC](https://www.icpac.net/) |meteorological drought indicator to monitor precipitation anomalies over 12-month accumulation periods|
|IPC Projections| [FEWSNET](https://fews.net/) | five-phase scale providing common standards for classifying the severity of acute or anticipated acute food insecurity. |



### What is the Standarized Precipitation Index (SPI-12)?

The Standardized Precipitation Index (SPI) is a widely used index to characterize meteorological drought.
The Standarized Precipitation Index (SPI-12) compares the total rainfall received at a particular location during the last 12 months with the long-term rainfall mean (42 years) for the same period of time at that location.




### What is IPC Food Security Projection Data?
 
The IPC is a commonly acceepted measure and classification to describe the current and anticipated severity of acute food insecurity. 
The classification is based on a convergence of available data and evidence, including indicators related to food consumption, livelihoods, malnutrition and mortality. Food Insecurity is one of the prioritized impacts of droughts in Somalia which is why it is also used for the triggering mechanism, in a population-weighted index. 

| Colour| Phase | Descriptions |
| ----- | --- | --- |
|![](/fig/IPC_Class_1.drawio.svg)|1. Minimal   |Households are able to meet essential food and non-food needs without engaging in atypical and unsustainable strategies to access food and income.   |
|![](/fig/IPC_Class_2.drawio.svg)|2. Stressed   |Households have minimally adequate food consumption but are unable to afford some essential non-food expenditures without engaging in stress-coping strategies.  |
|![](/fig/IPC_Class_3.drawio.svg)|3. Crisis   |Households either have food consumption gaps that are reflected by high or above-usual acute malnutrition __OR__ are marginally able to meet minimum food needs but only by depleting essential livelihood assets or through crisis-coping strategies.  |
|![](/fig/IPC_Class_4.drawio.svg)|4. Emergency|Households either have large food consumption gaps which are reflected in very high acute malnutrition and excess mortality; __OR__ are able to mitigate large food consumption gaps but only by employing emergency livelihood strategies and asset liquidation.|
|![](/fig/IPC_Class_5.drawio.svg)|5. Famine |Households have an extreme lack of food and/or other basic needs even after full employment of coping strategies. Starvation, death, destitution, and extremely critical acute malnutrition levels are evident. (For Famine Classification, area needs to have extreme critical levels of acute malnutrition and mortality.)  |


#### IPC Food Security Projection:

Three times a year (February, June, and October) FEWSNET estimates most likely IPC classes for the upcoming 8 month (near-term and mid-term projection), available from 2019-current. The near-term projection is called ML1 and is a projection for the upcoming 4 month, the mid-term projection is called ML2 and projects the IPC classes for the 4 subsequent months. For the triggering ML1 (near-term) as well as ML2 (mid-term) projections will be considered. 

Outlook updates are produced almost every month and are also taken into account.


#### IPC-Population Weighted Index

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



## Trigger Workflow Manually 

### Step 1: Setting up folder structure 


```{figure} /fig/Drought_EAP_Worklow_Step_1_1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ In this step we set up the correct folder structure to make the analysis easier and to ensure consitent results. 

__Tool:__ No special tools or programs are needed


::::{grid} 2
:::{grid-item-card} Instructions
1. Open the Folder “FbF_Drought_Monitoring_Trigger"
2. Open the subfolder "Monitoring"
3. Copy the Template folder “TEMPLATE_Year_Month” and change the name to the current year and month. The result could be the folder "2022_05" 

The Video below shows the process for setting up the folder for decmber 2023.
 :::
:::{grid-item-card} Folder structure FbF_Drought_Monitoring_Trigger

```{figure} /fig/Folder_structure_FbF_Drought_Monitoring_Trigger.drawio.svg
---
width: 450px
name: 
align: center
---
```
:::
::::

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_folder_setup.mp4"></video>




### Step 2: Download of the forecast data

```{figure} /fig/Drought_EAP_Worklow_Step_2_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__ FileZilla

The current plans provide that ICPAC will monthly provide the SPI-12 Forcast whereas the IPC data will be pulled from the FEWSNET website. FEWS NET publishes IPC data on its website. 
The main publications plus the updates of the IPC data amount to the publication of new data almost monthly.

### SPI-12 Data


ICPAC will provide the SPI-12 forecasts on their FTP (File Transfer Protocol). There are different ways to access the FTP-Server. We recommend to install and once set up [FileZilla](https://filezilla-project.org/download.php?platform=win64). This will make your work easily repeatable on a monthly basis.

1. Download Filezilla [here](https://filezilla-project.org/download.php?platform=win64).
2. Install the `.exe` file you have downloaded 
3. Open FileZilla


4. Establish a connection to the FTP Server by insterting the credentials you have been passed (Host, Username and Password) and clicking "Quickconnect".


In FileZilla you have four windows. On the left hand side you will see the folder on your computer in the upper window. By clicking on a folder, the documents in the folder will be shown in the lower left window.
On the right hand side, you will see in the upper window the FTP data folder and by clicking on it, the data will be shown in the lower right window.

In order to pass the data from the FTP Server to your own machine you can simply drag and drop the folder or data from the righthandside windows (FTP-Server) to the lefthandside windows (your Computer). To do so, firstly navigate to your folder where you wneed the latest SPI-12 data to be located `.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/SPI_12`. Then drag and drop the latest SPI-12 into the folder.



```{figure} /fig/FileZilla.PNG
---
height: 400px
name: FileZilla Interface
align: center
---
```

### IPC Data

The IPC Projection data is provided and regulary updated on the [FEWSNET Website](https://fews.net/).
On the website you will have to click on Somalia to acess the data. Alternativley, you can  navigate through `Data` -> `Acute Food Insecurity Data` and enter „Somalia". In the menu you will see different dataformats for different timestamps. Once you find out which timestamp is the most current one find the ZIP download. We need the data in shapefile (.shp) format, which is only included in the ZIP file and not provided as single download file. 


```{figure} /fig/IPC_Projections_website.png
---
height: 400px
name: FEWSNET IPC - Download IPC Projections
align: center
---
```

Once downloaded the ZIP folder, right click on it and unzip it. You will see various datasets. We are interested in the ML1 and ML2 projections. The filename is composed of "SO" for Somalia, year and month of the report month of the respective projection and _ML1 or _ML2 forn the respective projection. This is what the the dataname for ML1 and ML2 projections published in August would look like:

`"SO_202308_ML1.shp"`,
`"SO_202308_ML2.shp"`

You can then copy the respective shapefiles to you folder 

`.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/IPC_ML1` and
`.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template//IPC_ML2`

Remember that you need to copy over all components that the respective [shapefile](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html#vector-data) is composed of. Most probably it has 5 components: .cpg, .dbf, .prj, .shp, and .shx.


```{figure} /fig/IPC_zip.PNG
---
height: 400px
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

```{figure} /fig/Drought_EAP_Worklow_Step_3_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`
2. Once the project is created save the project in the folder you created in Step 1 (e.g. 2022_05). To do that click on `Project` -> `Save as` and navigate to the folder. Give the project the same name as the folder you created (e.g. 2022_05). Then click `Save`
3. Load all input data in QGIS by [drag and drop](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-raster-data-via-drag-and-drop). Click on `Project` -> `Save` 

This video shows how to setup the QGIS project for April 2022 and how to import all data into the project.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_3.mp4"></video>


### Step 4: Intersection of ML 1 & ML 2 data with the district polygons 

```{figure} /fig/Drought_EAP_Worklow_Step_4_1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ The goal is to receive polygon layers which share both the borders and the attributes of both input layers.

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__ [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)



::::{grid} 2
:::{grid-item-card} Instructions

1. Click on `Vector` -> `Geoprocessing Tools` -> [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)
2. `Input Layer`: ML 1 or ML 2
3. `Overlay layer`: district_pop_sum
4. Under `Intersection` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_Intersection" or "ML2_Intersection" and click `Save`
5. Click `Run`

__Result:__ After doing this for ML1 and ML2 you should have two polygon layers, each containing all columns of ML1 (or ML2) and district_pop_sum.

The resulting layer can have more rows than the original layers.

:::

:::{grid-item-card} Intersection for ML 1

```{figure} /fig/SRCS_Trigger_step_4_Intersection.png
---
width: 500px
name: 
align: center
---
```

:::
::::



::::{grid} 2
:::{grid-item-card} Instructions

:::
:::{grid-item-card} 
```{figure} /fig/SRCS_Trigger_step_4_Intersection.png
---
width: 500px
name: 
align: center
---
```
:::
::::

The video shows the whole process on the example of ML 1.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_4_Intersection.mp4"></video>

### Step 5: Calculation of Population per  Intersection Polygon

```{figure} /fig/Drought_EAP_Worklow_Step_5_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Here we calculate the population in each polygon of the intersection layer from step 4.

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__  [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)

::::{grid} 2
:::{grid-item-card} Instructions
1.  In the `Toolbox` -> Search for [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)
  * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox`
2. `Input Layer`: "ML1_Intersection" or "ML2_Intersection"
3. `Raster Layer`: "som_ppp_2020_UNadj_constrained.tif"
4. Statistics to calculate: Only `Sum`
5.  Under `Zonal Statistics` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_zonal_statistic" or "ML2_zonal_statistic" and click `Save`
5. Click `Run`

__Result:__ The result should be the “ML1_zonal_statistic” and “ML2_zonal_statistic” polygon layers. These layers should have the same columns in the attribute table __plus__ the column “_sum”, which is the number of people living in the single parts of the polygons.
:::
:::{grid-item-card} Zonal statistics for ML1
```{figure} /fig/SRCS_Trigger_step_5_zonal_statistic.png
---
width: 1000px
name: 
align: center
---
```
:::
::::

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_5_zonal_statistic.mp4"></video>


### Step 6: Weighting of the Population based on IPC-Phase

```{figure} /fig/Drought_EAP_Worklow_Step_6_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ The purpose of this step is the weighting of the population ins the five IPC pahses as discribt in [IPC Data](file:///C:/HeiGIT/RCRC_GIS_Training/gis-training-resource-center/_build/html/content/GIS_AA/en_qgis_drought_trigger_somalia.html#ipc-data).

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```
__Tool:__  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)


1. Right-click on the layer “ML1_zonal_statistic” (or “ML2_zonal_statistic”) -> `Open Attribute Table`-> click on [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
2. Check “Create new field"
3. `Output field name`: Name the new column “pop_sum_weighted”
4. `Result field type`: Decimal number (real)
5. Add the code block from Input into the `Expression` field
Click `ok`

``````{list-table}
:header-rows: 1
:widths: 15 15

* - ML 1
  - ML 2
* - ```md
    CASE

    WHEN "ML1" = 3 THEN "_sum" * 1
    WHEN "ML1" = 4 THEN "_sum" * 3
    WHEN "ML1" = 5 THEN "_sum" * 6
    ELSE "_sum"

    END
    ```
  - ```md
    CASE

    WHEN "ML2" = 3 THEN "_sum" * 1
    WHEN "ML2" = 4 THEN "_sum" * 3
    WHEN "ML2" = 5 THEN "_sum" * 6
    ELSE "_sum"

    END
    ```
``````
6. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table and end the editing mode by clicking on ![](/fig/mActionToggleEditing.png)

Here is the `Field Calculator` window of how it should look to calculate pop_sum_weighted for ML1.

```{figure} /fig/SRCS_Trigger_step_6_field_calculator.png
---
width: 700px
name: 
align: center
---
```
__Result:__ The two layers “ML1_zonal_statistic” and “ML2_zonal_statistic” should now both have the column “pop_sum_weighted”.


The video shows the whole process with the the example of ML 1.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_6_field_calculators.mp4"></video>


### Step 7: Adding the total district population to Intersection Polygons

```{figure} /fig/Drought_EAP_Worklow_Step_7_1.png
---
width: 1000px
name: 
align: center
---
```


__Purpose:__ Now we want to add a column with the total district population to “ML1_zonal_statistic” and “ML2_zonal_statistic”.

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__ [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)

::::{grid} 2
:::{grid-item-card} Instructions
1. In the `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
  * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox`
2. `Input Layer`: Select “ML1_zonal_statistic” (or “ML2_zonal_statistic”)
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select the layer “district_pop_som”
5. `Table field 2`: Select “admin2Name”
6. `Layer 2 field to copy`: Click on the three points ![](/fig/Three_points.png) and select “admin2Name” and “districtpo”
7. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)
8. Under `Join Layer [optional]` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_join" or "ML2_join" and click `Save`
9. Click `Run`

__Result:__ Now you should have to new polygon layer named “ML1_join” and ML2_Join” containing the column districtpo.
:::
:::{grid-item-card} 
```{figure} /fig/SRCS_Trigger_step_7_join.png
---
width: 500px
name: 
align: center
---
```
:::
::::



<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_7_join.mp4"></video>


### Step 8.: Calculation of Population Proportion per Intersection Polygon
```{figure} /fig/Drought_EAP_Worklow_Step_8_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ In this step we calculating the [IPC-Population Weighted Index](file:///C:/HeiGIT/RCRC_GIS_Training/gis-training-resource-center/_build/html/content/GIS_AA/en_qgis_drought_trigger_somalia.html#ipc-population-weighted-index)for every small part of the polygon layer. 
```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__[`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)

1. Right-click on Intersection_population Polygons layer -> “Attribute Table”-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png)to open the field calculator
2. Check “Create new field"
3. “Output field name”: Name the new column “Index_per_IPCPolygon_ML1” (or "Index_per_IPCPolygon_ML2”)
4. “Result field type”: Decimal number (real)
5. Add the codeinto the `Expression` field
```md
"pop_sum_weighted"/"districtpo"
```
6. Click `ok`
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table and end the editing mode by clicking on ![](/fig/mActionToggleEditing.png)

```{figure} /fig/SRCS_Trigger_step_8_field_calculator.png
width: 500px
name: 
align: center
---
```


__Result:__ Both layer “ML1_join” and ML2_Join” should now have the column “Index_per_IPCPolygon_ML1” or “Index_per_IPCPolygon_ML2”. The numbers in this column have to be smaller than in the “district” column.

The video shows the whole process with the the example of ML 1.
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_TRigger_step_8_field_calculator.mp4"></video>




### Step 9.: Calculate IPC Index per District
```{figure} /fig/Drought_EAP_Worklow_Step_9_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__  The purpose of this step is to calculate a population weighted mean over the IPC classes that fall within a district, in order to give the amount of people living in a certain IPC class more importance than just the area affected by a certain IPC class. The result is a IPC Index value for each district.

__Tool:__

1. In the `Toolbox`-> Search for `Join attribute by location (summary)`
  * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox` 
2. `Input Layer`: Select your “district_pop_som” layer
3. `Input Layer 2`: Select “ML1_join” (or ML2_Join”)
4. `Geometric predicate`: Select “Intersection”
5. `Field to summarise`: Select “Index_per_IPCPolygon_ML1” (or “Index_per_IPCPolygon_ML2” )
6. `Summaries to calculate`: Chose only the option “mean”
7. Under `Join Layer` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "ML1_join_location" or "ML2_join_location" and click `Save`
8. Click `Run`


```{figure} /fig/SRCS_Trigger_step_9_join_location.png
width: 400px
name: 
align: center
---
```
__Result:__ As a result, your two layers "ML1_join_location" and "ML2_join_location" should have the column “Index_per_IPCPolygon_ML1_mean” or “Index_per_IPCPolygon_ML2_mean”. Furthermore, the number of rows should be the exact number of districts in Somalia and the polygons should have the exact shape of the districts.


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_9_join_location.mp4"></video>





 

### Step 10.: Join ML1 and ML2 I
```{figure} /fig/Drought_EAP_Worklow_Step_10_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ The purpose of this step is to merge “ML1_join_location" and "ML2_join_location” into one layer so that it can be jointly analysed.

__Tool:__ [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)

1. In the `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
  * Tip: If the `Toolbox` is not opne click `Processing`-> `Toolbox` 
2. `Input Layer`: Select your "ML1_join_location" layer 
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select your "ML2_join_location" layer 
5. `Table field 2`: Select “admin2Name”
6. `Layer 2 field to copy`: Click on the three points and  select “Index_per_IPCPolygon_ML2_mean”
7. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)
7. Under `Join Layer` click on the three points ![](/fig/Three_points.png)-> `Save to File` and navigate to you monitoring folder [Year_Month]. Give the output the name "IPC_index_district" and click `Save`
8. Click `Run`


SRCS_Trigger_step_10_IPC_Index_district.png
### Step 11.: Calculation of SPI12 Mean per District
```{figure} /fig/Drought_EAP_Worklow_Step_11_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Calculate the mean value over the SPI-12 values of all pixels that fall within a scertain districts area, in order to have one SPI-12 value for each district.

__Tool:__ [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)

1. Click `Processing`-> `Toolbox` -> Search for  [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)
2. `Input Layer`: district_pop_som
3. `Raster Layer`: SPI Forecast
4. `Output column prefix`: Use  "SPI12_"
5. `Statistics to calculate`: “Mean”

### Step 12.: Join SPI12 Mean to the IPC Index
```{figure} /fig/Drought_EAP_Worklow_Step_12_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ The purpose of this step is to merge data from two different data sources into one data frame so that it can be jointly analysed.

__Tool:__[`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)


1. Click `Processing` -> `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
2. `Input Layer`: Select your “IPC_index_district_ML2_ML2”
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select your “SPI12_districts”
5. `Table field 2`: Select “admin2Name”
6. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)"

### Step 13.: Evaluate Trigger Activation 
```{figure} /fig/Drought_EAP_Worklow_Step_13_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ The purpose of this step is to gain a quick overview of possible trigger activation without having to revise the actual data. Instead we will have a binary column with trigger = yes or no values.

__Tool:__ [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)


1. Right-click on Intersection_population Polygons layer -> `Attribute Table`-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
2. Check `Create new field`
3. `Output field name`: Name the new column “Trigger_activation”
4. `Result field type`: Text
5. Add the code below into the `Expression` field
``````{list-table}
:header-rows: 1
:widths: 15

* - Code
* - ```md
    `CASE
    WHEN "Index_per_IPCPolygon_ML1_mean" >0.7 AND "Index_per_IPCPolygon_ML2_mean" > 0.7
    AND
    "SPI12_mean" < -1
    THEN 'yes'
    ELSE 'no'
    END`
    ```
``````
6. Click `ok`
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table



### Step 14.: Visualisation of results
```{figure} /fig/Drought_EAP_Worklow_Step_14_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Definition of how features are represented visually on the map.

__Tool:__ [Symbology](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_I.html#symbology-for-vector-data)

__Trigger Activation__

1. Right cklick on the “Trigger_activation” layer -> `Properties` -> `Symbology`
2. In the drop-down menu on the top choose `Categorized`
3. In the down left corner click on `Style` -> `Load Style`
4. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger/layer_styles” folder and select the file “Style_Trigger_Activation.qml”.
5. Click `Open`. Then click on `Load Style`
6. Back in the “Layer Properties” Window click `Apply` and `OK`


You will now see districts where no trigger is activated in green and districts with trigger activation in pink.

The “Style_Trigger_Activation.qml” style layer is configured to show the district names only where the trigger is actually activated. If there is no trigger activation you can activate the admin 1 boundary layer for better map orientation (see __Administrative 2 Boundaries__ below)

```{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: 
align: center
---
```


__Risk Assessment__

For the creation of an __Intervention Map__ we will have to add the risk assessment data and the respective style file.
For this first of all load from "FbF_Drought_Monitoring_Trigger/Fixed_data/Risk_Assessment" the file "risk_assessment_districts.gpkg". This file is the output of the conducted risk assessment and contains a risk value for each district of Simaliland and Somalia.  In order to visualize it 
1. Right click on the "risk_assessment_districts" layer -> `Properties` -> `Symbology`
2. Repeat the steps from above for loading the style layer, but choose the “somalia_risk_assessment_style.qml” style layer.

For the final visualization and right overlay of the risk assessment and the Trigger activation, make sure you "Trigger Activation" layer is above the
"risk_assessment_districts" layer in the Layers Panel ([Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept.html?highlight=layer#layer-concept)).


__Administrative 2 Boundaries__

For better orientation in the map, especially if no trigger is activated you can optionally load the regions boundaries with regions names:

Navigate to "...\FbF_Drought_Monitoring_Trigger\Fixed_data\Regions" and load the "Som_Admbnda_Adm1_UNDP.shp" file into your layers panel.

1. Right click on the "risk_assessment_districts" layer -> `Properties` -> `Symbology`
2. Repeat the steps from above for loading the style layer, but choose the “somalia_risk_assessment_style.qml” style layer.

```{figure} /fig/Map_no_trigger.PNG
---
width: 1000px
name: 
align: center
---
```

__Basemap__

Add a basemap to your map in order to have a nice background. We recommend to use OpenStreetMap as a baselayer, but you can also choose another basemap if you prefer.

Find out [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html?highlight=osm#basemaps) how to add a basemap.



```{Attention}
Remember the [layer concept](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_geodata_concept.html?highlight=layer#layer-concept) and make sure the basemap layer is at the bottom of your layers panel.
```



### Step 15.: Making print map

```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ Viualization of the map features in a printable map layout

__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)


In order to easily visualize the output of the trigger analysis we provide you with a 
[map template](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#map-templates) that can be used as a base for your visualization. You can find the template in the following directory: ".../FbF_Drought_Monitoring_Trigger/maps_somalia_template_risk_assessment.qpt".

Check [here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#map-templates) how to open templates and how to use them in QGIS.

You can also adapt the template to your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#print-layout).

```{Attention}
Make sure you edit the Map Information on the template, e.g. current date. Also make sure to check the legend items: Remove unnecessary items and eventually change the names to meaning descriptions.
```

### Step 16.: Exporting Map 


```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order tp print it as a pdf or format of your choice.


__Tool:__ [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)


```{figure} /fig/map_output example2.png
---
width: 1000px
name: 
align: center
---
```

When you have finished the design of you map you can export it as pdf or image file in different datafromats.

[Click here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html?highlight=export#exporting-the-print-layout) to find the step by step on how to export your map.


# Trigger Workflow Automated 
