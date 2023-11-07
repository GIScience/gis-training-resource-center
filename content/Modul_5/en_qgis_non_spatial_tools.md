# Non-Spatial Geodataprocessing

#### Introduction:
Non-spatial geodataprocessing in QGIS refers to the manipulation, subsetting and analysis of attribute data within a GIS environment without directly involving spatial components. It involves operations on the non-geometric attributes of geospatial datasets. This can include data cleaning, transformation, enrichment and analysis based on the associated attribute information, such as population statistics, land use classifications or economic indicators. Non-spatial geodataprocessing can be used to perform calculations, generate statistics and gain insights into the non-spatial aspects of geospatial datasets. QGIS offers a variety of tools for non-spatial geodataprocessing to assist users in managing and analyzing attribute data effectively.

This segment of Module 5 will start with the introduction of table functions. It will then progress into techniques for querying data, ultimately introducing the important concept of non-spatial joins.

```{figure} /fig/en_attribute_table_large.PNG
---
height: 500px
name: attribute_table_all
---
Screenshot of an attribute table for QGIS version 3.28.4
```
## Table functions

For a comprehensive overview on the attribute table's functionality and its purpose, you're invited to explore the [Wiki](/content/Wiki/en_qgis_attribute_table_wiki.md) article on it.

### Add field
The information within a vector layer can be accessed through its attribute table, and it can be enhanced by introducing new fields to this table. These additional fields may be derived from calculations, as exemplified in the following case where population density is computed to provide deeper insights into spatial population distribution.

```{Attention}
Depending on the information that will be added to the created attribute field, the correct data type must be selected.
```
__Possible data types:__

The most common ones are:
- __Whole number: Integer (32 and 64 bit)__
- __Decimal number (real)__
- __Text (string)__

Additional options:
- Date and Date and time
- Boolean

````{dropdown} Add a field for population density; the data type should be Decimal number (real)
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_add_field.mp4"></video>
````

### Delete field
It is also possible to __delete fields__ from the attribute table. A commonly used practice is to __remove all unused or unnecessary fields__ from a layer before starting to work on it. This __makes the dataset much more organized__.

````{dropdown} Delete all unused/unnecessary fields from the vector layer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_delete_field.mp4"></video>
````

### Calculate field
An important practice is to calculate the attribute values for a field, e.g., based on the values of other fields. In QGIS, you can __create a new field or update an existing field__.

```{Note}
It is necessary to __check if the data type of the field__ (new or updated) __and your calculation match__. For example: if you are calculating a ratio (e.g. density), the field should not be of type integer but rather of type decimal number.
```
An example could be to calculate the population density based on the already existing fields Population and Area.

A very important tool for such calculations is the __Field Calculator__. It allows you to __perform calculations based on existing attribute values or defined functions__, for example, to calculate the length or area of a geometry feature. The results of these calculations can be written into a new field or update an existing field.


```{figure} /fig/en_field_calculator_red_boxes.png
---
height: 350px
name: field_calculator
---
Screenshot of the Field calculator
```

The most important groups and their respective functionality that are provided with the field calculator are listed below:
- __Fields and Values__
    - Contains a list of fields from the layer
- __Geometry__
    - Calculates the area of a polygon feature: `$area`
    - Calculates the length of a line feature: `$length`
    - Calculates the centroid of a polygon feature: `centroid($geometry)`
    - Calculates the bounding box of a feature: `bounds($geometry)`
    - Calculates the distance between two points: `distance(point_a, point_b)`
- __Maths__
    - Calculates the square root of a field: `sqrt("field")`
    - Calculate `min` and `max`

````{dropdown} Calculate the population density based on the already existing fields Population and Area
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_calculate_field.mp4"></video>
````

### Basic statistics for fields
The tool __Basic statistics for fields__ generates statistics for a specific field of the attribute table of a vector layer. The results are generated as an HTML file and can be accessed by using the __file path link__ in the __Results Viewer__. 

````{dropdown} Calculate statistics for the field population density for all the countries. What are the max./min. values, average, etc.?
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_field_stats.mp4"></video>
````

### Statistics by categories
To calculate statistics of a field depending on a parent class you can use the tool __Statistics by catergories__. The parent class is a combination of values from other fields.

__Questions that need to be considered when doing these calculations:__
* For which fields should the statistics be calculated in the attribute table?
* Which field in the attribute table contains which information?

````{dropdown} How many cities per country have more than 300.000 inhabitants? For each country: how many people live in the largest agglomeration?
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_stats_by_category.mp4"></video>
````


## Non-spatial queries
In GIS you can __query__ (filter) data based on specific attribute information. Once the filtering is successful, only the desired features that __correspond__ to the chosen attribute are displayed. Data filtering is a valuable technique for creating __subsets__ of features that can be exported as a new layer.

### Manual selection
It is possible to manually select specific rows by clicking on the number on the left side of it. This can be easily used to select a small number of rows. If they are selected successfully, they will appear in __yellow__.

````{dropdown} Manual selection of rows
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_attribute_table.mp4"></video>
````

### Select by expression
In this dialog, you can build your expressions to query the data. There are several operators that can be used to filter your vector layer.

::::{tab-set}

:::{tab-item} Arithmetic operators
| operator | functionality          |
|----------|------------------------|
| __+__    | addition               |
| __-__    | substraction           |
| __*__    | multiplication         |
| __/__    | division               |
| __%__    | remainder of division  |
:::

:::{tab-item} Comparison operators
| operator | functionality            |
|----------|--------------------------|
| __=__    | equals                   |
| __!=__   | not equal                |
| __<__    | less than                |
| __>__    | greater than             |
| __<=__   | less than or equal to    |
| __>=__   | greater than or equal to |
:::

:::{tab-item} Logical operators
Operators such as AND, OR can be used to combine different queris or criteria
| operator | functionality          |
|----------|------------------------|
| __AND__  | logical AND            |
| __OR__   | logical OR             |
| __NOT__  | logical NOT            |
:::

:::{tab-item} Special operators
| operator      | functionality                                  |
|---------------|------------------------------------------------|
| __LIKE__      | pattern matching                               |
| __IN__        | checks if a value is in a list of values       |
| __IS NULL__   | checks for null values                         |
| __BETWEEN__   | checks if a value is within a specified range  |
| __CASE WHEN__ | conditional expressions                        |
:::

::::

##### SQL

Another possibility to build your expressions is to utilize SQL.

::::{tab-set}

:::{tab-item} SQL introduction
SQL in QGIS, often referred to as "Spatial SQL" or "Spatial Query Language," is a specialized version of SQL used for querying and manipulating geospatial data. It allows users to interact with geographic information by writing SQL queries that can filter, analyze, and visualize spatial data. With Spatial SQL in QGIS, you can work with various types of geospatial datasets and perform operations specific to geographic data, such as selecting features within a certain area, calculating spatial relationships, and much more. This capability makes SQL a valuable tool for geospatial data management and analysis in the QGIS environment.
:::

:::{tab-item} SQL Cheat sheet
SQL in QGIS, often referred to as "Spatial SQL" or "Spatial Query Language," is a specialized version of SQL used for querying and manipulating geospatial data. It allows users to interact with geographic information by writing SQL queries that can filter, analyze, and visualize spatial data. With Spatial SQL in QGIS, you can work with various types of geospatial datasets and perform operations specific to geographic data, such as selecting features within a certain area, calculating spatial relationships, and much more. This capability makes SQL a valuable tool for geospatial data management and analysis in the QGIS environment.
:::

::::

````{dropdown} Build query for the question: Cities that were not yet cities of one million inhabitants in 1950 but already had more than 10 million inhabitants in 2015.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_and.mp4"></video>
````

## Non-spatial joins
A lot of analysis can be done with just a single layer. But sometimes the necessary information we need for our analysis is __split across__ different datasets/layers. With QGIS, these layers can be __combined__ to perform the analysis we want. The simplest way to combine layers is via an __attribute join__. This operation looks up information from a second data source based on a __shared attribute value__. This value functions as a common unique identifier, also known as an ID, UID or key.

In QGIS the tool __Join attributes by field value__ is often used for such operations:

```{figure} /fig/en_join_attributes_by_field_values.PNG
---
height: 500px
name: join_attributes_by_field_value
---
Screenshot of the Join attributes by field value tool
```


```{Attention} 
- An attribute join in QGIS only works properly, when the attributes **match exactly**.
- For example: **"S. Sudan"** will not match with **"South Sudan"**.
- Where possible it’s best to **use attributes that have been designed for joining**, such as **P-codes** or **ID's** which are not susceptible to spelling mistakes.
```