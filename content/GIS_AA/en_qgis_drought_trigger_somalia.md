# QGIS Trigger Workflow for Somalia 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Somalia Red Cresent Society (SRCS), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow consists of 15 steps of which 9 are automated in the form of a QGIS Model. In this article, we explain how all 15 steps can be done manually. In practice one needs to do only 6 steps manually, the rest is done by the QGSI Model.
The chapter Workflow Automated explains the process and how it is intended in practice. The chapter Workflow Manually is to understand what happens inside of the QGIS Model.

## Trigger Statment


## Trigger Workflow Manually 

### Step 1: Setting up folder structure 


```{figure} /fig/Drought_EAP_Worklow_Step_1_1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ 

__Tool:__

1. Open the Folder “FbF_Drought_Monitoring_Trigger
2. Open the subfolder "Monitoring"
3. Copy the Template folder “TEMPLATE_Year_Month” and change the name to the current year and month.
The result could be the folder "2022_05" 




### Step 2: Download of the forecast data

```{figure} /fig/Drought_EAP_Worklow_Step_2_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 


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

```{dropdown} Steps covered by the QGIS Model

### Step 4: Intersection of ML 1 & ML 2 data with the district polygons 

```{figure} /fig/Drought_EAP_Worklow_Step_4_1.png
---
width: 1000px
name: 
align: center
---
```
__Purpose:__ 

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__ [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)

1. Click on `Vector` -> `Geoprocessing Tools` -> [`Intersection`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html#intersection)
2. `Input Layer`: ML 1 or ML 2
3. `Overlay layer`: district_pop_sum



### Step 5: Calculation of Population per  Intersection Polygon

```{figure} /fig/Drought_EAP_Worklow_Step_5_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 
```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```
__Tool:__  [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)

1. Click `Processing`-> `Toolbox` -> Search for [`Zonal Statistics`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html#zonal-statistics)
2. `Input Layer`: Intersection Polygons
3. `Raster Layer`: som_ppp_2020_UNadj_constrained.tif
4. Statistics to calculate: `Sum`



### Step 6: Weighting of the Population based on IPC-Phase

```{figure} /fig/Drought_EAP_Worklow_Step_6_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```
__Tool:__  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)

1. Right-click on Intersection_population Polygons layer -> `Attribute Table`-> click on [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
2. Check “Create new field"
3. `Output field name`: Name the new column “pop_sum_weighted”
4. `Result field type`: Decimal
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
    END`
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
6. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table

### Step 7: Adding the total district population to Intersection Polygons

```{figure} /fig/Drought_EAP_Worklow_Step_7_1.png
---
width: 1000px
name: 
align: center
---
```


__Purpose:__ 
```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__[`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)

1. Click `Processing` -> `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
2. `Input Layer`: Select your Intersection_population_weighted_total_pop” layer
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select the layer “district_pop_som”
5. `Table field 2`: Select “admin2Name”
6. `Layer 2 field to copy`: Click on the three points and select “admin2Name” and “districtpop”
7. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)

### Step 8.: Calculation of Population Proportion per Intersection Polygon
```{figure} /fig/Drought_EAP_Worklow_Step_8_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 
```{Attention}
You need to perform this step two times. One time for ML 1 and a second time for ML 2.
```

__Tool:__[`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field)

1. Right-click on Intersection_population Polygons layer -> “Attribute Table”-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png)to open the field calculator
2. Check “Create new field"
3. “Output field name”: Name the new column “Index_per_IPCPolygon_ML1” (or "Index_per_IPCPolygon_ML2”)
4. “Result field type”: Decimal
5. Add the code: `"pop_sum_weighted"/"districtpo"` into the `Expression` field
6. Click `ok`
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table

### Step 9.: Calculate IPC Index per District
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 10.: Join ML1 and ML2 I
```{figure} /fig/Drought_EAP_Worklow_Step_10_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__ [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)

1. `Processing` -> `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
2. `Input Layer`: Select your “IPC_Index_district” layer for ML 1
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select your “IPC_Index_district” layer for ML 2
5. `Table field 2`: Select “admin2Name”
6. `Layer 2 field to copy`: Click on the three points and  select “Index_per_IPCPolygon_ML2_mean”
7. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)

### Step 11.: Calculation of SPI12 Mean per District
```{figure} /fig/Drought_EAP_Worklow_Step_11_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

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

__Purpose:__ 

__Tool:__[`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)


1. Click `Processing` -> `Toolbox`-> Search for [`Join attributes by field value`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_non_spatial_joins_wiki.html#join-attributes-by-field-value)
2. `Input Layer`: Select your “IPC_index_district_ML2_ML2”
3. `Table field`: Select “admin2Name”
4. `Input Layer 2`: Select your “SPI12_districts”
5. `Table field 2`: Select “admin2Name”
6. `Join type`: Select the option “Take attributes of the first matching feature only (one-to-one)

### Step 13.: Evaluate Trigger Activation 
```{figure} /fig/Drought_EAP_Worklow_Step_13_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__


1. Right-click on Intersection_population Polygons layer -> “Attribute Table”-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
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
6. Click "ok"
7. Save the new column by clicking on ![](/fig/mActionSaveEdits.png) in the attribute table

```

### Step 14.: Visualisation of results
```{figure} /fig/Drought_EAP_Worklow_Step_14_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__ [Symbology](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_I.html#symbology-for-vector-data)

1. Right cklick on the “Trigger_activation” layer -> `Properties` -> `Symbology`
2. In the drop-down menu on the top choose `Categorized`
3. In the down left corner click on `Style` -> `Load Style`
4. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “FbF_Drought_Monitoring_Trigger” folder and select the file “Style_Model_Output.qml”.
5. Click “Open”. Then click on “Load Style”
6. Back in the “Layer Properties” Window click `Apply` and `OK`

### Step 15.: Making print map
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 16.: Exporting Map 
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

# Trigger Workflow Automated 
