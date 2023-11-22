# Table function
## Add field

- Add a field to the attribute table.
- __Attention:__ depending on the information to be entered in the attribute field, the correct data type must be selected.

:::{dropdown} Example: Add a field for population density, data type: Float or Double or Real (floating point numbers)
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_add_field_wiki.mp4"></video>
:::

## Delete field

- Delete a field from the attribute table.

:::{dropdown} Example: Delete all unused/unnecessary fields from the layer.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_delete_field_wiki.mp4"></video>
:::

## Calculate Field

- Calculate the attribute values for a field, e.g. based on the values of other fields.
- In QGIS you can create a new field or update an existing field.

- __Attention:__ Check if the data type of the field and your calculation match. For example, if you are calculating a ratio (e.g. density), the field should not be of type integer.

:::{dropdown} Example: Calculate the population density using the already existing fields Population and Area.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_calculate_field_wiki.mp4"></video>
:::

## Basic Statistics for Fields

- Generates a statistic for a specific field in the attribute table.

:::{dropdown} Example: Statistics for the field population density for all countries, what is the maximum value, average, etc.?
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_field_stats_wiki.mp4"></video>
:::

## Statistics by Categories

- Create aggregated statistics for categories
- For which fields in the attribute table should statistics be calculated?
- Which field in the attribute table contains the category?

:::{dropdown} Example: How many cities with more than 300,000 inhabitants are there per country? For each country: How many people live in the largest agglomeration?
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_stats_by_category_wiki.mp4"></video>
:::