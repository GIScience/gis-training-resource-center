# Non-Spatial Geodataprocessing

#### Introduction:
Non-spatial geodataprocessing in QGIS refers to the manipulation, subsetting and analysis of attribute data within a GIS environment without directly involving spatial components. It involves operations on the non-geometric attributes of geospatial datasets. This can include data cleaning, transformation, enrichment and analysis based on the associated attribute information, such as population statistics, land use classifications or economic indicators. Non-spatial geodataprocessing can be used to perform calculations, generate statistics and gain insights into the non-spatial aspects of geospatial datasets. QGIS offers a variety of tools for non-spatial geodataprocessing to assist users in managing and analyzing attribute data effectively.

This segment of Module 5 will start with the introduction of table functions. It will then progress into techniques for querying data, ultimately introducing the important concept of non-spatial joins.

## Table functions

### Add field
The information of a vector layer can be accessed through its attribute table, and it can be enriched by adding new fields to this table.

```{Attention}
Depending on the information that will be added to the created attribute field, the correct data type must be selected.
```
__Possible data types:__
- __Whole number: Integer (32 and 64 bit)__
- __Decimal number (real)__
- __Text (string)__
- Date and Date and time
- Boolean

The most common data types are the first three.

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

### Manual selection
It is possible to manually select specific rows by clicking on the number in front of it. This can be easily used to select a small number of rows. If they are selected successfully, they will appear in yellow.

# VIDEO?

### Select by expression



#### Querying data:
In GIS one can __query__ (filter) data based on specific information (attribute). After successfull filtering only the wanted features that represent the __attribute__ are displayed. Data filtering can be used to create a __subset__ of features and export them as a new layer.

#### Query Builder
* The Query Builder is a tool for querying (filtering) data or layers using their attributes to define a subset of the features in the layer.
* The querying is based on __SQL__ (Structured Query Language) expressions to use one or more conditions to filter a layer.

Built a drop-down menu for SQL: 
SQL is a standardized programming language that is used to manage databases and perform various operations on the data in them

* As long as a query is active, only the features corresponding to its result are available in the project.

```{Note} 
The Query Builder dialog is accessible through the Layer Properties dialog (maybe hint to Wiki?), at the bottom right of the Source section tab.
```
![Query Builder location](/fig/en_query_builder_location.png) Location of the Query Builder

#### Query operators
Within the Query Builder we use different __operators__ to build query expressions and filter our layers. Some operators are __mathematical__ and others are __logical__.

Important examples:
* "field" __=__ "value" : use the __=__ operator to show only features which include the value
* "field" __!=__ "value" : use the __!=__ operator to show all features that don’t include the value
* "field" = "value1" __OR__ "field" = "value2" : use __OR__ to show all features that include either value1 or value2
* "field1" = "value" __AND__ "field2" = "value" : use __AND__ to show all features that include both values indicated

![Query Builder](/fig/en_query_builder.png) Query Builder

## Non-spatial joins
A lot of analysis can be done with just a single layer. But sometimes the necessary information we need for our analysis is __split across__ different datasets/layers. With QGIS, these layers can be __combined__ to perform the analysis we want. The simplest way to combine layers is via an __attribute join__. This operation looks up information from a second data source based on a __shared attribute value__. This value functions as a common unique identifier, also known as an ID, UID or key.

In QGIS the tool __Join attributes by field value__ is often used for such operations:

![Join attributes by field value](/fig/en_join_attributes_by_field_values.png) Screenshot of the Join attributes by field value tool


```{Note} 
- An attribute join in QGIS only works properly, when the attributes **match exactly**.
- For example: **"S. Sudan"** will not match with **"South Sudan"**.
- Where possible it’s best to **use attributes that have been designed for joining**, such as **P-codes** or **ID's** which are not susceptible to spelling mistakes.
```

Test Test