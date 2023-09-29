# Non-Spatial Geodataprocessing
**Competences:**

## Table functions

### Field Calculator:
The __Field Calculator__ is a tool for querying (filtering) your data or layers using their attributes. 

## Non-spatial queries (II)

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