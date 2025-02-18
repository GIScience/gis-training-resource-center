::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/Module_5/en_qgis_module_5_exercises.html 
{octicon}`undo;1.5em;sd-text-danger`
:::
::::

# Risk Assessment

## Characteristics of the exercise

::::{grid} 2
:::{grid-item-card}

## Aim of the exercise:

In this exercise, you will go through the different steps requiring QGIS in order to conduct a spatial risk assessment.

#### Type of trainings exercise:

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}

#### These skills are relevant for 


:::
::::

::::{grid} 2
:::{grid-item-card}

#### Estimated time demand for the exercise.

 

:::

:::{grid-item-card}

## Relevant Wiki Articles

* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Intersection](/content/Wiki/en_qgis_geoprocessing_wiki.md#intersection)
* [Zonal Statistics](/content/Wiki/en_qgis_raster_basic_wiki.md#zonal-statistics)
* [Join Attributes by location (summary](/content/Wiki/en_qgis_spatial_joins_wiki.md#join-attributes-by-location-summary)
* [Table functions](/content/Wiki/en_qgis_raster_basic_wiki.md#zonal-statistics)

<!--FIME: Check if these wiki articles are relevant-->

:::

::::

## Background 

In the context of the Forecast based Financing methodology the conduction of a robust risk assessment is a crucial step towards the development of an Early Action Protocol. A risk analysis serves to understand what kinds of disaster impacts can be expected from a particular type of hazard and to identify who and what is exposed and vulnerable to this hazard and why. By overlaying the information on exposure, vulnerability, and coping capacity, it will become clear which areas are predicted to be most severely impacted. These areas can then be targeted as priority areas for early action to ensure the most at-risk communities receive assistance before the event happens.
The collection and processing of this information varies based on the problem, but the calculation scheme to combine the information to a risk score remains consistent.

Somalia is significantly exposed to droughts. We will showcase a risk assessment for a drought Early Action protocol.

## Part 1: Indicator Processing

### Task
The first part of the exercise will prepare the data in order to serve as indicator values. Raw data will be processed into meaningful indicators, and the vulnerability index will be calculated. Finally, all risk relevant data will be joined into a single vector layer using spatial data geoprocessing.


## Data


Download the data folder for "Modul_5_Exercise2_Drought_Monitoring_Trigger.zip" __[Here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Modul_5_Exercise1_Risk_Assessment/Modul_5_Exercise1_Risk_Assessment.zip)__. In the folder, you can find two folders. One for the first part ("Modul_5_Ex1_Part_1") of the exercise and one for the second part ("Modul_5_Ex1_Part_2").

Download the data folder for the first part of the exercise: "Modul_5_Ex1_Part_1".



Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `som_admbnda_adm2_ocha_20230308.shp`: [Somalia district boundaries (Admin level 2)](https://data.humdata.org/dataset/cod-ab-som)
- `WHO_health_sites.shp`: [Healthsites Somalia](https://data.humdata.org/dataset/somalia-health-facilities-data )
- `som_ppp_2020_UNadj_constrained.tif` : [Worldpop Population Counts Somalia ](https://hub.worldpop.org/geodata/summary?id=28892)
- `Somalia_malnutrion_district_2022_2023.xlsx`:[Somalia: Acute Malnutrition](https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence?)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```



1. Load the Somalia district boundaries (admin level 2) (`som_admbnda_adm2_ocha_20230308.shp`) and Healthsites Somalia (`WHO_health_sites.shp)  into QGIS.

2. Make sure to that both datasets are in the same projection. In this case we have two different projections and we will reproject  __Healthsites Somalia__ into EPSG 4326. Use the tool `Reproject layer` for this process. See the Wiki entry on __Projections__ for further information.


```{Attention}
Before you start doing any GIS operations, __always explore the data__. Always check if the projections of the different layers are the same.
```

3. In order to bring the information of the health sites point layer into a usable indicator value we can now count the health sites per district. We can use the tool __Count points in polygon__ from the Processing Toolbox. Take a look on the tools description and the further features it brings. For our task we only have to specify polygon and point input layer, the count field name (e.g. __Num_healtsites__) and choose name and directory of the output layer. Explore the output.

```{figure} /fig/Count_points_polygon.PNG
---
width: 100%
name: count_points_polygon
---
Count healthsites per district
```

4. Now we have the number of health sites per district. Nevertheless, it would be interesting to know how many health sites exist per 10.000 people. For this task we firstly need to know how many inhabitants has each district. We can process this information by using the __Zonal statistics__ tool from the Processing Toolbox. See the Wiki entry for [Zonal Statistics](/content/Wiki/en_qgis_raster_basic_wiki.md#basic-raster-operations) for further information. Specify your inout layer (Output of step 3 e.g. __Num_healtsites__) and your raster layer (Worldpop Raster), specify the column prefix (e.g. ___wpop__) and select the statistics to caclulate (__sum__). For each district all pixel values of the Worldpop Raster that fall inside of it will be summed up. Explore the output.



```{figure} /fig/en_qgis_modul_5_ex1_zonal_statistics.PNG
---
width: 100%
name: czonal_statistics
---
Summarise population counts per district
```

```{Hint}
Throughout the indicator processing process you will have several interim results. Make sure to save them in a "temp" folder.
```

5. Now we know the numbers of health sites and the number of population per district. We are ready to calculate our final indicator __Number of health sites per 10.000 inhabitants. 
* Open the attribute table of “Num_healthsites_wpop” (Output of step 4) and Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png). By checkin the box for `Create a new field` we can conduct calculation and saving them right away in a new attribute column.
* define the output field name as "healthsites_10000" and set the `Type` to `Decimal Number(real)`.
* Now we will calculate in the expression field the number of health sites per 10.000 inhabitants:

```md

("Num_healthsites"/"_wpopsum")*10000

```
    

* When you are down click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](/content/Wiki/en_qgis_attribute_table_wiki.md#attribute-table-data-editing)).

```{figure} /fig/en_qgis_modul_5_ex1_field_calc.PNG
---
width: 80%
name: Field Calculator
---
Calculate health sites per 10000 inhabitants
```


#### 6. Land Degradation

A very important factor for areas vulnerable to drought is the level of land degradation. It is an important factor not only for agriculture, but also for livestock herds, as both are primary sources of income. We will try to add this information to our dataset:

-[Somalia Land degradation](https://spatial.faoswalim.org/layers/geonode:SOM_Land_Degradation_FAOSWALIM#/)

```{figure} /fig/land_degradation.PNG
---
width: 60%
name: land_degradation
---
Land Degradation
```

You will see that we can only download the information as an image. This is a very common case when working with open data. We have to digitise the information in order to be able to use it for further processing. Find the digitised version in "Modul_5_Ex1_Part_1\land_degradation_somalia".

Explore the data. We have a column "LandD_CLas" which indicators the severity of land degradation from 0 to 3. We now want to join each respective land degradation class to its correct district by calculating the largest overlapping area.

* Open the tool `Join attributes by location` from the Processing Toolbox.
* define `Input Layer` (layer you want to enrich) and `Join Layer` (dataset with the additional information)
* select `intersects` as geometric predicate and add only the `LandD_class` as field to add to our base layer.
* as `Join Type` set `Take attributes of the feature with largest overlap only (one-to-one)`
* Save as Layer

See the Wiki entry [Spatial Joins ](/content/Wiki/en_qgis_spatial_joins_wiki.md#spatial-joins) for further information.



```{figure} /fig/en_qgis_modul_5_ex1_join.PNG
---
width: 100%
name: Join attributes by location
---
Join Attributes by Location
```


#### 7. Malnutrition

Another very important indicator to describe vulnerability in a district is acute malnutrition, especially for children under 5 years old.

Download the data we need:
`Somalia_malnutrion_district_2022_2023.xlsx`:[Somalia: Acute Malnutrition](https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence?)

Explore the data. In which resolution is the data available? Do you have ideas as to how we can add it to our indicator dataset?

*Save the Excel file as a CSV by clicking on `Save file as` and choosing `CSV (delimiter-separated)`

* Load the CSV file into you QGIS by drag and drop
* Open the tool `Join attributes by field value` from the Processing Toolbox
 * specify our two datasets we want to join as well as the common field available for joining (`ADM2_EN` and `adm2name`)
* as `join type` set `Take attributes of the first matching feature only (one-to-one)`
* Save the Layer to File

```{figure} /fig/en_qgis_modul_5_ex1_joinbyvalue.PNG
---
width: 100%
name: Join attributes by field value
---
Join attributes by field value
```

In the Log file you will get a message: "6 feature(s) from input layer could not be matched"

``` {Attention}
It is possible that the CSV file the column headers of the attribute table will not have the correct names (instead they may have "field 1", "field 2" etc.) after importing. In this case, the correct field names is usually located below the header.
```

```{figure} /fig/en_qgis_module_5_ex1_error.PNG
---
width: 100%
name: Join attributes by field value
---
Log File Join Attribute by Field Value
```

Open the attribute tables from both, your output layer and the CSV file in order to find out the roots of the problem. In the output layer double-click on `affunderfive` and bring `NULL` Values to the top. Check the joining attribute "ADM2_EN" and compare it with the joining attribute "adm2name" from the CSV file.
The Spelling of the district names differs. Since we are using the admin-2-boundaries as the base layer for all indicators, we can now adapt the names in the CSV file. 
You can edit the names in 6 cases in the Attribute Table of the CSV file by toggling editing mode, or you can manually edit the CSV file in Excel and then load it into QGIS.


* Make sure to call your final layer "vulnerability_districts".


## Part 2: Risk Calculation

### Task
In the second part of the exercise we will showcase the steps how to come from indicators to a risk analysis.


You can find all the data for the second part of the exercise in the "Modul_5_Ex1_Part_2".
Download the data folder for the second part of the exercise: "Modul_5_Ex1_Part_2". We processed the vulnerability layer in the first part of the exercise; simplified exposure and lack of coping capacity layers have been prepared in advance for this exercise. These layers have only 3 to 4 indicators for complexity reasons. See below an example of indicators that were used for Somalia:

```{figure} /fig/Indicators_Rsik_Assessment_Somalia.png
---
width: 80%
name: Indicators Risk Assessment
---
Indicators Risk Assessment
```



#### 1. Normalisation

In order to perform further calculation on the indicators, we need to make them comparable. To do this, we can normalise them to be within a range of 0-1.

$ Normalised\ Value\ = \frac{value\ -\ min value}{max\ value \ - \ min } $


* Open the attribute table of “vulnerability_districts” and Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png). By checkin the box for `Create a new field` we can conduct calculation and saving them right away in a new attribute column.
* start with the first indicator `LandD_class`
* define the output field name as "LandD_class_norm" and set the `Type` to `Decimal Number(real)`.
* Now we will calculate in the expression field the normalisation of the indicator:

```md
("LandD_Clas" - minimum( "LandD_Clas" ))/( maximum( "LandD_Clas") - minimum( "LandD_Clas" ))
```
* When you are done click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](/content/Wiki/en_qgis_attribute_table_wiki.md#attribute-table-data-editing)).

```{figure} /fig/en_qgis_modul_5_ex1_Part2_normalization.PNG
---
width: 80%
name: Join attributes by field value
---
Normalisation of indicators
```

* Repeat this step for the other indicators
* For each indicator you have now the original column and the normalised column. 

#### 2. Directions 

The direction indicates whether or not an indicator follows the predefined logic: “the higher the value, the worse the circumstances”, meaning that higher values imply a higher risk. The logic is adapted for all three dimensions, since it is generally intuitive to think that high values = high risk. If a respective indicator follows this logic, the direction would be 1; if it does not, the direction would be = -1.
* In order to understand the directions of our indicators we first have to assign them to one of the dimensions (exposure, vulnerability, coping capacity).
* To which dimension would you assign the processed indicators and what would their direction be?

Depending on the direction the next step will vary:

If the __direction is 1__ (indicating a positive weight), the formula is straightforward:

$ weighted=   value  \times weight $

If the __direction is -1__ (indicating a negative weight), the formula adjusts the value by subtracting it from 1 before applying the weight:

$ weighted=   (1 - value)  \times weight $

The second formula inverts the value $(1 - value)$ before applying the weight, resulting in a different calculation for variables with negative weights.

 We will not go further into this in this module but you can find more information [here](/content/GIS_AA/en_qgis_risk_assessment_plugin.md#risk).

```{Hint}
It is recommended to properly check the logic of each indicator. Often the indicators of a certain dimension follow the same logic but there are always exceptions. After the directions have been applied to the data, we can using the language “lack of coping capacity” instead of “coping capacity” since we have forced the respective indicators to another direction following the predefined logic (the higher the value = the worse the circumstances).
```


#### 3. Weighting of Indicators

In the next step we can weight the indicators based on their relevance to our risk assessment. It is recommended to do surveys or workshops with the local staff in oder to find out the importance of the respective indicators.

We have used so far the following weighting scale:

| Weight| Definition | 
| ----- | --- | 
|0| Not Important|
|0.25| Slightly Important| 
|0.5|Moderately Important|
|0.75|Fairly Important|
|1|Very Important|

* In the attribute table of your layer we can calculate the weighted indicators for each normalised indicator. For this we have to follow the same steps as above: Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png), and create a new field with the suffix "_weighted" in the expression field.

```md

"LandD_clas_norm" * 0.75

```


```{figure} /fig/en_qgis_module_5_ex1_part2_weigthed.PNG
---
width: 80%
name: Add new field to weight indicators
---
Add new field to weight indicators
```

* For each indicator we now have the normalised and weighted version:

```{figure} /fig/en_qgis_modul_5_ex1_part2_weighted_attribute.PNG
---
width: 100%
name: Attribute Table with "_norm" and "_weighted" indicators
---
Attribute Table with "_norm" and "_weighted" indicators
```

#### 4. Vulnerability Score / Index

We are now ready to calculate the vulnerability score for each district:
* Open the attribute table -> open the `Field Calculator`![](/fig/mActionCalculateField.png) and create a new field with the name "vulnerability_score" and field type "Decimal Number (real)". In the expression window, sum up all weighted indicator values:

```md

("LandD_clas_weigthed"  +  "perc_elderly_weighted"  +  "affunderfive_weighted") / 3 

```

#### 5. Prepare Risk Assessment

In order to calculate the risk we have to bring our 3 dimension exposure, vulnerability and coping capacity together.

* Right click om one of the layer and select `Properties` -> Go the `Joins` tab
* Click on the `+` button, add a new join and select the layer you want to join. Define "admin2Name" as `Join Field`:

```{figure} /fig/en_qgis_modul_5_ex1_part2_join_risk.PNG
---
width: 90%
name: Join Layers 
---
Join Layers by Join Field
```
* Right click on the layer -> `Export` -> `Save feature as` and save the layer as "risk" layer into your temp folder.
* We will now work with the "risk" layer: Delete all fields but the normalised scores: Open the Attribute Table of your risk layer `Toggle editing mode `![](/fig/mActionToggleEditing.png) -> `Delete field` ![](/fig/mActionDeleteAttribute.png) and select all the indicator fields. In the end your layer look should like this:

```{figure} /fig/en_qgis_modul_5_ex1_part2_risklayer_attributetable.PNG
---
width: 70%
name: Risk Layer Attribute Table normalised Scores
---
Risk Layer Attribute Table normalised Scores
```

#### 6. Risk Calculation


Finally, the risk is calculated by the geometric mean of the dimensions Exposure and Susceptibility, while Susceptibility is defined by the geometric mean of Vulnerability and the Lack of Coping Capacity. The geometric mean is chosen since it offers the advantage of rewarding balanced developments and equal reduction of deficits at all levels of the model:

$ susceptibility =   \sqrt vulnerability  \times lack\ of\ coping\ capacity $

$ risk=   \sqrt exposure  \times susceptibility $


*  Open the Attribute table -> `Field Calculator`![](/fig/mActionCalculateField.png) and create a field "Susceptibility" and type in the formula. Do the same to create a field called "risk" and employ the appropriate expression.

```md

sqrt("Susceptibility" * "exposure_norm")

```

```{figure} /fig/en_qgis_modul_5_ex1_part2_risk.PNG
---
width: 80%
name: Calculate risk 
---
Risk Calculation
```

```{Note}
The geometric mean is a specific type of average that is calculated by multiplying together all the values in a dataset and then taking the nth root of the product, where n is the number of values. For two values, the geometric mean is the square root of their product. For three values, it is the cube root, and so on.
```
#### 6. Visualisation of the Results


* Right click on the “risk” layer -> `Properties` -> `Symbology`
* In the down left corner click on `Style` -> `Load Style`
* In the new window click on the three points ![](/fig/Three_points.png). Navigate to the “Map Template” folder and select the file __“somalia_risk_assessment_style.qml”__.
* Click `Open`. Then click on `Load Style`
* Back in the “Layer Properties” Window click `Apply` and `OK`


Print Layout:

* Open a new print layout by clicking on `Project` -> `New Print Layout` -> enter the name of your current Project e.g "2024_01".
* Go the the `Ex_Part_2` folder and drag and drop the file `maps_somalia_template_risk_assessment.qpt` in the print layout
* Change the date to the current date by clicking on "Further map info…" in the items panel. Click on the `Item Properties` tab and scroll down. Here you can change the date in the `Main Properties` field.
* If necessary, adjust the legend by clicking on the legend in the  `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there check if you have to open the dropdown. Make sure `Auto update` is not checked.
* Remove all items in the legend be clicking on the item and then on the red minus icon below.

    
```{figure} /fig/en_qgis_mondul_5_ex1_possible_result.PNG
---
width: 90%
name: Possible Map Result
---
Possible Map Result
```
    


#### 7. Automating the Process

HeiGIT has developed a a QGIS Risk Assessment Plugin in order to simplify this process and safe time.
You can find more information about the risk methodology and the usage of the plugin [here](/content/GIS_AA/en_qgis_risk_assessment_plugin.md#risk-assessment-qgis-plugin).


In order to try out the plugin and see the result, use the provided input data in your folder: "Modul_5_Ex1_Part_2\Input data\QGIS Plugin Risk Assessment\input"