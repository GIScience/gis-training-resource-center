# Non-Spatial Geodataprocessing

#### Introduction:
Non-spatial geodataprocessing in QGIS refers to the manipulation, subsetting and analysis of attribute data within a GIS environment without directly involving spatial components. It involves operations on the __non-geometric attributes__ of geospatial datasets. This can include data cleaning, transformation, enrichment and analysis based on the associated attribute information, such as population statistics, land use classifications or economic indicators. Non-spatial geodataprocessing can be used to perform calculations, generate statistics and gain insights into the non-spatial aspects of geospatial datasets. QGIS offers a variety of tools for non-spatial geodataprocessing to assist users in managing and analyzing attribute data effectively.

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
The information within a vector layer can be accessed through its __attribute table__, and it can be enhanced by __introducing new fields__ to this table. These additional fields may be derived from calculations, as exemplified in the following case, where population density is computed to provide deeper insights into spatial population distribution.

```{Attention}
The selection of the appropriate data type should align with the information being added to the new attribute field. Please keep this in mind while watching the example video.
```
__Possible data types:__

The most common ones are:
- __Whole number: Integer (32 and 64 bit)__
- __Decimal number (real)__
- __Text (string)__

Additional options:
- Date and Date and time
- Boolean

````{dropdown} Example: Add a field for population density
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_add_field.mp4"></video>
````

### Delete field
It is also possible to __delete fields__ from the attribute table. A commonly used practice is to __remove all unused or unnecessary fields__ from a layer before starting to work on it. This __makes the dataset much more organized__.

````{dropdown} Example: Delete all unused/unnecessary fields from a vector layer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_delete_field.mp4"></video>
````

### Calculate field
An important practice is to calculate the attribute values for a field, e.g., based on the values of other fields. In QGIS, you can __create a new field or update an existing field__.

```{Note}
It is necessary to __check if the data type of the field__ (new or updated) __and your calculation match__. For example, if you are calculating a ratio (e.g. density), the field should not be of type integer but rather of type decimal number.
```

An example could be to calculate the population density based on the already existing fields Population and Area.

A very important tool for such calculations is the __Field Calculator__. It allows you to __perform calculations based on existing attribute values or defined functions__, for example, to calculate the length or area of a geometry feature or in the given example, could be used to calculate the population density based on the already existing fields Population and Area. The results of these calculations can be written into a new field or update an existing field.

```{figure} /fig/en_field_calculator_red_boxes.png
---
width: 100%
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

````{dropdown} Example: Calculate the population density
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_calculate_field.mp4"></video>
````

### Basic statistics for fields
The tool __Basic statistics for fields__ generates statistics for a specific field of the attribute table of a vector layer. The results are generated as an HTML file and can be accessed by using the __file path link__ in the __Results Viewer__. This operation is highly valuable for gaining a comprehensive understanding of the data you intend to work with. It allows you to determine the range of values, pinpoint the minimum and maximum values. In the provided example, this operation is applied to calculate the global population density, enabling you to easily identify the most densely populated region worldwide.

````{dropdown} Example: Calculate statistics for the field population density for countries worldwide.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_field_stats.mp4"></video>
````

### Statistics by categories
To calculate statistics of a field depending on a parent class you can use the tool __Statistics by catergories__. The parent class is a combination of values from other fields.

__Questions that need to be considered when doing these calculations:__
* For which fields should the statistics be calculated in the attribute table?
* Which field in the attribute table contains which information?

For greater precision in these calculations, statistics by categories offer more comprehensive insights than those mentioned earlier. In this case, it becomes simple to determine the number of cities per country with over 300,000 inhabitants and, for each country, the population living in the largest urban agglomeration.

````{dropdown} Example: Cities with more than 300.000 inhabitants and the amount of population in the largest agglomerations
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_stats_by_category.mp4"></video>
````

## Non-spatial queries
In GIS, you can __query__ (filter) data based on specific attribute information. Once the filtering is successful, only the desired features that __correspond__ to the chosen attribute are displayed. Data filtering is a valuable technique for creating __subsets__ of features that can be exported as a new layer.

### Manual selection
It is possible to manually select specific rows by clicking on the number on the left side of it. This can be easily used to select a small number of rows. If they are selected successfully, they will appear in __yellow__.

````{dropdown} Example: Manual selection of rows
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

Querying your data to answer more complex question is of great importance. This can be accomplished using the "Select by expression" tool. In the provided example, we aim to answer the question: Which cities, not having a population of one million inhabitants in 1950, had surged to over 10 million inhabitants by 2015?

````{dropdown} Example: Cities, not having a population of one million inhabitants in 1950, had surged to over 10 million inhabitants by 2015?
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_and.mp4"></video>
````

##### SQL

Another possibility to build your expressions is to utilize SQL.

::::{tab-set}

:::{tab-item} SQL introduction
SQL (Structured Query Language) is a standardized programming language that is used to manage databases and perform various operations on the data in them. In the Query Builder in QGIS, you can use SQL expressions to use one or more conditions to filter a layer.
:::

:::{tab-item} SQL Cheat Sheet
You can easily access essential SQL statements by referring to this handy [Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/). This offers a concise overview of the core functionalities.
:::

::::

### Query Builder

The Query Builder provides an interface that allows you to define a __subset of the features__ in the layer using SQL-like statements and to display the results in the main window. As long as the query is active, only the __features corresponding__ to its result are available in the project. You can use one or more layer attributes to define the filter in the Query Builder. The Query Builder is built as follows:

```{figure} /fig/en_query_builder_comment.png
---
width: 100%
name: query_builder
---
Screenshot of the Query Builder
```

1. The __Fields list__ contains all the fields of the layer. To add an attribute column to the expression window, double-click its name or just type it into the box.
2. The __Values__ frame lists the values of the currently selected field. 
    - To list __all unique values__ of a field, click the __All__ button.
    - To list the __first 25__ unique values of the column, click the __Sample__ button.
    - To add a value to the expression window, double click it in the Values list. You can use the __search box__ at the top of the "Values"-panel to easily browse and find attribute values in the list.
3. The __Operators__ section contains all usable operators. To add an operator, click the appropriate button.
4. The __Test__ button helps you to check your query and __displays a message box with the number of features__ satisfying the current query. 
5. Use the __Clear__ button to revert the layer to its original state.

```{Note}
When a filter is applied with the Query Builder, QGIS treats the resulting subset as if it were the __entire layer__.
```

In this short video, you'll discover the location of the query builder and learn how to create a straightforward query for isolating a particular state from a dataset that covers the entire country. The example focuses on a dataset related to South Sudan and serves as a basic illustration.

````{dropdown} Example: Simple usage of the Query Builder.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_query_builder.mp4"></video>
````

## Non-spatial joins
A lot of analysis can be done with just a single layer. But, sometimes, the necessary information we need for our analysis is __split across__ different datasets/layers. With QGIS, these layers can be __combined__ to perform the analysis we want. The simplest way to combine layers is via an __attribute join__. This operation looks up information from a second data source based on a __shared attribute value__. This value functions as a common unique identifier, also known as an ID, UID or key.

In QGIS the tool __Join attributes by field value__ is often used for such operations:

```{figure} /fig/en_join_attributes_by_field_values.PNG
---
width: 75%
name: join_attributes_by_field_value
---
Screenshot of the Join attributes by field value tool
```

```{Attention} 
- An attribute join in QGIS only works properly, when the attributes **match exactly**.
- For example: **"S. Sudan"** will not match with **"South Sudan"**.
- Where possible it’s best to **use attributes that have been designed for joining**, such as **P-codes** or **ID's** which are not susceptible to spelling mistakes.
```