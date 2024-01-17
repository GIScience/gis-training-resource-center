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






## Part 1: Indicator Processing

### Task
In the second part of the exercise we will showcase the steps how to come from indicators to a risk analysis.



 