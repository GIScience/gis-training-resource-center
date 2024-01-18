# Risk Assessment

__🔙[Back to Homepage](/content/intro.md)__

## Aim of the exercise:

In this exercise, you will learn how to digitise the positions of settlements by creating new datasets. Furthermore, you will learn how to enrich the simple geodata set with additional information.

## Background 


## Data

Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `som_admbnda_adm2_ocha_20230308.shp`: [Somalia district boundaries (Admin level 2)](https://data.humdata.org/dataset/cod-ab-som)
- `WHO_health_sites.shp`: [Healthsites Somalia](https://data.humdata.org/dataset/somalia-health-facilities-data )
- `som_ppp_2020_UNadj_constrained.tif` : [Worldpop Population Counts Somalia ](https://hub.worldpop.org/geodata/summary?id=28892)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

## Part 1: Indicator Processing

### Task
This first part of the exercise will prepare the data in order to serve as indicator values. We will work on vulnerability indicators and to calculate the vulnerability index, we will finally join all the relevant data using spatial geodataprocessing into a single vector layer.

1. Load the Somalia district boundaries (admin level 2) (`som_admbnda_adm2_ocha_20230308.shp`) and the Healhsites Somalia (`WHO_health_sites.shp)  into QGIS.

2. Make sure to that both datasets are in the same projection. In this case we have two different projections and we will reproject the __Healthsites Somalia__ into EPSG 4326. Use the tool `Reproject layer` for this process. See the Wiki entry on __Projections__ for further information.


```{Attention}
Before you start doing any GIS operations, __always explore the data__. Always check if the projections of the different layers are the same.
```

3. In order to bring the information of the healthsites point layer into a usable indicator value we can now count the healthsites per district. We can use the tool __Count points in polygon__ from the Processing Toolbox. Take a look on the tools description and the further features it brings. For our task we only have to specify polygon and point input layer, the count field name (e.g. __Num_healtsites__) and choose name and directory of the output layer. Explore the output.

```{figure} /fig/Count_points_polygon.PNG
---
width: 100%
name: count_points_polygon
---
Screenshot of different sizes of the attribute tables
```

4. Now we have the number of healthsites per district. Nevertheless, it would be interesting to know how mnay healthsites exist per 10.000 people. For this task we firstly need to know how many inhabitants has each district. We can proces this information by using the __Zonal statistics__ tool from the Processing Toolbox. See the Wiki entry for [Zonal Statistics](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html?highlight=zonal+statistics#basic-raster-operations) fur further information. Specify your inout layer (Output of step 3 e.g. __Num_healtsites__) and your raster layer (Worldpop Raster), specify the column prefix (e.g. ___wpop__) and select the statistics to caclulate (__sum__). For each distrcit all pixel values of the Worldpop Raster that fall inside of it will be summed up. Explore the output.



```{figure} /fig/en_qgis_modul_5_ex1_zonal_statistics.PNG
---
width: 100%
name: czonal_statistics
---
Screenshot of different sizes of the attribute tables
```

5. Now we know the numbers of healthsites and the number of population per district. We are ready to caclulate our final indicator __Number of healthsites per 10.000 inhabitants. 
    *Open the attribute table of “Num_healthsites_wpop” (Output of step 4) and Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png). By checkin the box for `Create a new field` we can conduct calculation and saving them right away in a new attribute column.
    *define the output field name as "healthsites_10000" and set the `Type` to `Decimal Number(real)`.
    *Now we will caclulate in the expression field the number of healthsites per 10.000 inhabitants:
     > `("Num_healthsites"/"_wpopsum")*10000`

     *When you are down click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#attribute-table-data-editing)).

```{figure} /fig/en_qgis_modul_5_ex1_field_calc.PNG
---
width: 100%
name: Field Calculator
---
Screenshot of different sizes of the attribute tables
```
    

6. Land Degradation

A very important factor of areas vulnerable to drought is the siuation with regards to land degradation. It is an important factor not only for agriculture but also livestock herds, both as main sources of livelihood. We will try to add this information to our dataset:

-[Somalia Land degradation](https://spatial.faoswalim.org/layers/geonode:SOM_Land_Degradation_FAOSWALIM#/)

You will see that we can only download the information as image. This is a very common case when working with open data. We would have to digitize the information in order to be able to use it for further processing. Find the digitized version here.

Explore the data. We have a column "LandD_CLas" which indicators the severity of land degradation from 0 to 3. We now want to join the respective land degradation class to its belongig district by considering the largest overlapping area.

    *Open the tool `Join attributes by location` from the Processing Toolbox.
    *define `Input Layer` (layer you want to enrich) and `Join Layer` (dataset with the additional information)
    *select `ìnteresects` as geometric predicate and add only the `LandD_class` as field to add to our base layer.
    *as `Join Type` set `Take attributes of the feature with largest overlap only (one-to-one)`
    *Save as Layer

See the Wiki entrey [Spatial Joins ](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_joins_wiki.html#spatial-joins) for further information.



```{figure} /fig/en_qgis_modul_5_ex1_join.PNG
---
width: 100%
name: Join attributes by location
---
Screenshot of Join attribute to location s
```


7. Malnutrition

Another very important indicator to describe vulnerability in a distrcit is the acute malnutirion, especially in children under 5 years old.

Dowload the data we need:
`Somalia_malnutrion_district_2022_2023.xlsx`:[Somalia: Acute Malnutrition](https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence?)

Explore the data. In which resolution is the data avalaible? DO you have ideas how we can add it to our indicator dataset?

*Save the Excel file as csv by clicking on `Save file as` and choosing `csv (delimiter-separated)`

*Load the csv-file into you QGIS by drag and drop
    *Open the tool `Join attributes by field value` from the Processing Toolbox
    *specify our two datasets we want to join as well as the common field available for joining (`ADM2_EN` and `adm2name`)
    *as `join type` set `Take attributes of the first matching feature only (one-to-one)`
    *Save the Layer to File

```{figure} /fig/en_qgis_modul_5_ex1_joinbyvalue.PNG
---
width: 100%
name: Join attributes by field value
---
Screenshot of Join attributes by field value
```

In the Log file you will get ba message: "6 feature(s) from input layer could not be matched"


```{figure} /fig/en_qgis_module_5_ex1_error.PNG
---
width: 100%
name: Join attributes by field value
---
Screenshot of Join attributes by field value
```

Open the attribute tables from both, your output layer and the csv file in order to find out the roots of the problem. In the output layer doble-click on `affunderfive` and bring `NULL` Values to the top. Check the joining attribute "ADM2_EN" and compare it with the joining attribute "adm2name" from the csv-file.
The Spelling of the distrcit anmes differs. Since we take the admin-2-boundaries as base layer for all indicators we can now adapt the names in the csv file. 
You can edit the names in 6 cases in the Attribute Table of the csv-file by toggling editing mode, or you can simply edit the csv file in excel an load it again into QGIS.




## Part 1: Risk Caclulation

### Task
In the second part of the exercise we will showcase the steps how to come from indicators to a risk analysis.

Download the data for the seccond part of the exercise.


1. Nomalization

For further caclulations with the indicatords we need to make them comparable. For this reason we normalize them to a range of 0-1.


* Open the attribute table of “vulnerability_districts_23” and Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png). By checkin the box for `Create a new field` we can conduct calculation and saving them right away in a new attribute column.
* start with the first indicator `LandD_class`
    *define the output field name as "LandD_class_norm" and set the `Type` to `Decimal Number(real)`.
    *Now we will caclulate in the expression field the normalization of the indicator:

     > ("LandD_Clas"  -  minimum(  "LandD_Clas" ))/( maximum(  "LandD_Clas") - minimum(  "LandD_Clas" ))

* When you are down click ![](/fig/mActionSaveEdits.png) to save your edits and switch off the editing mode by again clicking on ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html#attribute-table-data-editing)).

```{figure} /fig/en_qgis_modul_5_ex1_Part2_normalization.PNG
---
width: 100%
name: Join attributes by field value
---
Nomrlalization of indicators
```

* Repeat this step for the other indicators
* For each indicator you have now the original column and the normalized column. 



2. Weighting of Indicators

In the next step we can weight the indicators based on their relevance to our risk assessment. It is recommended to do surveys or workshops with the local staff in oder to find out the importance of the respective indicators.

We have used so far the following weighting scale:

|Weigtt|Description|
|---|---|
|0|Not relevant|
|0.25|Low relevance|
|0.5|Low-medium relevance|
|0.75|Low-mhigh relevance|
|1|Highly relevant|

* In the attribute table of your layer we can calculate the weighted indicators for each normalized indicators, respectively. FOr this we have to follow the same steps as above: Open the `Field Calculator` by clicking on the button ![](/fig/mActionCalculateField.png), create a new field with the suffix "_weighted" and in the expression field.



```{figure} /fig/en_qgis_moudl_5_ex1_part2_weigthed.PNG
---
width: 100%
name: Add new field to weight indicators
---
Nomrlal
```

* For each indicator we now have the normalied and weighted version:

```{figure} /fig/en_qgis_modul_5_ex1_part2_weighted_attribute.PNG
---
width: 100%
name: Attribute Table 
---
Nomrlal
```

3. Vulnerability Score / Index

We arenow ready to calculate the vulnerability score for each distrcit:
* Open the attribute table -> open the `Field Calculator`![](/fig/mActionCalculateField.png) and creat a new field with the name "vulnerability_score" and field type "Decimal Numnber (real)". In the expression window sum up all weighted indicator values:

>  "LandD_clas_weigthed"  +  "perc_elderly_weighted"  +  "affunderfive_weighted" 


4. Prepare Risk Assessment

In order to calculate the risk we have to bring our 3 dimension exposure, vulnerability and coping capacity together.

* Right click om one of the layer and select `Properties` -> Go the`Joins` tab
* Click on the `+` button, add a new join and select the layer you want to join. Define "admin2Name" as `Join Field`:

```{figure} /fig/en_qgis_modul_5_ex1_part2_join_risk.PNG
---
width: 100%
name: Attribute Table 
---
Nomrlal
```
* Right click on the layer -> `Export` -> `Save feature as` and save the layer as "risk" layer into your temp folder.
* We will now work with the "risk" layer: Open the Attribute table -> `Field Calculator`![](/fig/mActionCalculateField.png) and normalize ths scores to a range from 0-1:

 > ( "vulnerability_districts_vulnerability_score"   -  minimum(  "vulnerability_districts_vulnerability_score"  ))/( maximum(   "vulnerability_districts_vulnerability_score" ) - minimum(   "vulnerability_districts_vulnerability_score" )

* Delete all fields but the normalized scores: Open the Attribute Table of your risk layer `Toggle editing mode `![](/fig/mActionToggleEditing.png) -> `Delete field` ![](/fig/mActionDeleteAttribute.png) and select all the indicator fields. In the end your layer look should like this:

```{figure} /fig/en_qgis_modul_5_ex1_part2_risklayer_attributetable.PNG
---
width: 100%
name: Risk Layer Attribute Table normalized Scores
---
Nomrlal
```

5. Risk Calculation


Finally, the risk is calculated by the geometric mean of the dimensions Exposure and Susceptibility, while Susceptibility is defined by the geometric mean of Vulnerability and the Lack of Coping Capacity. The geometric mean is chosen since it offers the advantage of rewarding balanced developments and equal reduction of deficits at all levels of the model:

$ susceptibility =   \sqrt vulnerability  \times lack\ of\ coping\ capacity $

$ risk=   \sqrt exposure  \times susceptibility $


*  Open the Attribute table -> `Field Calculator`![](/fig/mActionCalculateField.png) and create a field "Susceptibility" and type in the formula. Do the same creating a field named "risk" and the respective expression.

```{figure} /fig/en_qgis_modul_5_ex1_part2_risk.PNG
---
width: 100%
name: Calculate risk 
---
Nomrlal
```

```{Note}
    The geometric mean is a specific type of average that is calculated by multiplying together all the values in a dataset and then taking the nth root of the product, where n is the number of values. For two values, the geometric mean is the square root of their product. For three values, it's the cube root, and so on.
```


6. Automatization of the Process

HeiGIT has developed a a QGIS Risk Assessment Plugin in order to simplify this process and safe time.
You can find more information about the risk methodology and the usage of the plugin [here](https://giscience.github.io/gis-training-resource-center/content/GIS_AA/en_qgis_risk_assessment_plugin.html#risk-assessment-qgis-plugin).