I plan on using this exercise: https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_4?ref_type=heads
Exercise 4 with a few adaptions

## Exercise 

### Aim of the exercise
Becoming familiar with different types of spatial and non-spatial analysis and geoprocessing tools. Understand the process of discovering relationships and connections between features in spatial data.

### Links to Wiki articles

### Data
Download all datasets and save the folder on your computer and unzip the file.  The zip folder includes:
- `sen_healthsites.shp`: [Senegal healthsites data](https://data.humdata.org/dataset/senegal-healthsites)
- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Senegal boundary data (Admin level 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `EO4SD_SAINT_LOUIS_FLOOD_2018.shp`: [Saint Louis flood extend data](https://wbwaterdata.org/dataset/saint-louis-senegal-flood-risk-map-esa-eo4sd-urban)
- `DI_Stat924.xls`: [Senegal Desinventar Sendai data](https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=sen) showing effects of disasters in Senegal regions
- `sen_admpop_adm1_2020.csv`: Senegal administrative level 1 (région) 2019 [projection population statistics](https://data.humdata.org/dataset/senegal-population-statistics)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

### Task
Create an overview of the effects of disasters in different regions of Senegal. Use non-spatial joins, table functions and different symbology.

```{Hint}
The projected coordinate system for Senegal is `EPSG:32628-WGS 84/UTM zone 28N`
```

1. Load the Senegal administrative boundary layer (.shp), as well as population per subnational unit and the Desinventar Sendai data of Senegal into QGIS.
2. Make sure to reproject the dataset with the administrative boundaries into UTM zone 28N. See the Wiki entry on __Projections__ for further information.
3. Conduct non-spatial joins based on regions listed in two datasets and the PCODE listed in these same sets. See the Wiki entry on __Non-spatial joins__ for further information.
    - First, add the total population of each administrative area to the shapefiles. Select a suitable field name and field data type.
    - Then add the number of directly and indirectly affected people. Choose a suitable field name and field data type.