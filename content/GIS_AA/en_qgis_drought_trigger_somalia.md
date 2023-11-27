# QGIS Trigger Workflow for Somalia 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Somalia Red Cresent Society (SRCS), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow consists of 15 steps of which 9 are automated in the form of a QGIS Model. In this article, we explain how all 15 steps can be done manually. In practice one needs to do only 6 steps manually, the rest is done by the QGSI Model.
The chapter Workflow Automated explains the process and how it is intended in practice. The chapter Workflow Manually is to understand what happens inside of the QGIS Model.

## Trigger Statment


## Trigger Workflow Manually 

### Step 1.: Setting up folder structure 


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




### Step 2.: Download of the forecast data

```{figure} /fig/Drought_EAP_Worklow_Step_2_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 


### Step 3.: Loading data into QGIS

```{figure} /fig/Drought_EAP_Worklow_Step_3_1.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on “Project” -> “New”
2. Once the project is created save the project in the folder you created in Step 1 (e.g. 2022_05). To do that click on ”Project” -> “Save as” and navigate to the folder. Give the project the same name as the folder you created (e.g. 2022_05). Then click “Save”
3. Load all input data in QGIS by drag and drop. Click on “Project” -> “Save” 

### Step 4.:Intersection of ML 1 & ML 2 data with the district polygons 

```{figure} /fig/Drought_EAP_Worklow_Step_4_1.png
---
width: 1000px
name: 
align: center
---
```


Click on “Vector” -> “Geoprocessing Tools” -> “Intersection”
“Input Layer”: ML 1 or ML 2
“Overlay layer”: district_pop_sum

__Purpose:__ 

__Tool:__


### Step 5.:Calculation of Population per  Intersection Polygon

```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__


### Step 6.:Weighting of the Population based on IPC-Phase

```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__


### Step 7.:Adding the total district population to Intersection Polygons

```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 8.: Calculation of Population Proportion per Intersection Polygon
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

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
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 11.: Calculation of SPI12 Mean per District
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 12.: Join SPI12 Mean to the IPC Index
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 13.: Evaluate Trigger Activation 
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

### Step 14.: Visualisation of results
```{figure} /fig/
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ 

__Tool:__

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
