# Exercise 2: Part 2: Calculate vulnerability index

### Aim of the exercise
We want to create an overview of different vulnerability indicators. From the Covid-19 risk indicators dataset we take `% permanent wall type`, `% permanent roof type` and `poverty incidence`. From the Uganda population statistics we calculate the `% of under fives` and `% of elderly`. We combine the data and we are now able to visualize the areas in Uganda that are most vulnerable.

### Links to Wiki articles
will be done when Wiki is finished

### Data
Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Senegal boundary data (Admin level 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `DI_Stat924.xls`: [Senegal Desinventar Sendai data](https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=sen) showing effects of disasters in Senegal regions
- `sen_admpop_adm1_2020.csv`: Senegal administrative level 1 (région) 2019 [projection population statistics](https://data.humdata.org/dataset/senegal-population-statistics)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

### Task
This exercise aims to create an overview of the impact of disasters in various regions of Senegal using the prepared datasets from the previous exercise. To achieve this, non-spatial joins, table functions, and different symbology will be utilized.

1. We will start by using the tool `Join attributes by field value` and join the population statistics onto the output from task 9 from the first part (`uga_adm2_covid_risk`) of the exercise.

```{figure} /fig/en_ex3_2_join_attribute_field_value.PNG
---
width: 60%
name: join_attribute_field_value
---
Screenshot from the Join attribute by field value operation using the ADM2_PCODE for joining
```

2. For the following calculations use the output layer from the previous operation and name it `uga_adm2_covid_risk_pop`. First, we will calculate the `% of under fives`. Open the `Field calculator` to calculate a new field of type decimal number: 
> `%Under5 = ( "M_00" + "M_01" + "M_02" + "M_03" + "M_04" + "F_00" + "F_01" + "F_02" + "F_03" + "F_04" ) / "Total"`

```{Hint}
You can access the field calculator through your attribute table by activating ![](/fig/mActionToggleEditing.png) `Toggle editing mode` and clicking on this symbol ![](/fig/mActionCalculateField.png) to `Open field calculator`.
```

```{figure} /fig/en_ex3_2_field_calculator.PNG
---
width: 60%
name: field_calculator
---
Screenshot of the field calculator which will be used for the subsequent calculations
```

3. Again, open the `Field calculator` to calculate another new field of type decimal number. This time we will calculate the `% of elderly`, defined as those aged 65 and above.
> `%Above65 = ( "M_65" + "M_66" + "M_67" + "M_68" + "M_69" + "M_70" + "M_71" + "M_72" + "M_73" + "M_74" + "M_75" + "M_76" + "M_77" + "M_78" + "M_79" + "M_80plus" + "F_65" + "F_66" + "F_67" + "F_68" + "F_69" + "F_70" + "F_71" + "F_72" + "F_73" + "F_74" + "F_75" + "F_76" + "F_77" + "F_78" + "F_79" + "F_80plus" ) / "Total"`

4. Next, open the field calculator again to calculate a new field of type decimal number.
> `%Under5indicator = ( "%Under5" - minimum( "%Under5" )) / (maximum( "%Under5" ) - minimum( "%Under5" )) * 10`

5. Again, open the `Field calculator` to calculate a new field of type decimal number.
> `%Above65indicator = ( "%Above65" - minimum( "%Above65" )) / (maximum( "%Above65" ) - minimum( "%Above65" )) * 10`

6. Delete unnecessary fields from the attribute table.

7. Again, open the `Field calculator` to calculate the average of vulnerabilities as the field type decimal number.
> `AvgVulnerability = ((10 - "%permrooft" ) + (10 - "%permwallt" ) + "Povertyinc" + "%Under5indicator" + "%Above65indicator" ) / 5`

Now you can save the changes and stop editing by clicking on this symbol ![](/fig/mActionToggleEditing.png).

8. Create a symbology on the field `AvgVulnerability` to visualise the different vulnerabilities.

```{Hint}
Use `Graduated` and select the correct field. Create a reasonable amount of classes and use the `Equal Interval` mode.
```

```{figure} /fig/en_ex3_2_example_final.PNG
---
width: 60%
name: final_results
---
This is how your output could look like in the end
```