# Non-Spatial Queries

## Manual selection
- Select the features manually in the __attribute table__ by clicking on it.

:::{dropdown} Example: Manually select countries with the attribute table
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_attribute_table_wiki.mp4"></video>
:::

## Select by expression
### Comparison operators 
- `>`, `<`, `=`, `!=`

:::{dropdown} Example: Select all cities with more than 20 million inhabitants in 2015: `"2015" > 20000`
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expresion_greater_wiki.mp4"></video>
:::

### Special operators
- `LIKE`

:::{dropdown} Example: Select all countries in Asia: `"continent" LIKE 'asia'`
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_like_wiki.mp4"></video>
:::

### Logical operators
- `AND`, `OR`
- Can be used to combine different queries or criteria.

:::{dropdown} Example: Cities, not having a population of one million inhabitants in 1950, had surged to over 10 million inhabitants by 2015: `"1950" < 1000 AND "2015" > 10000`
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_and_wiki.mp4"></video>
:::

### Save selected features as a new file
- `Layer-Properties` -> `Export` -> `Save only selected features`

:::{dropdown} Example: Export selected features as a new file
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_export_wiki.mp4"></video>
:::

## Further resources
You can access information about logical operators in QGIS documentation through the [following link](https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/attribute_table.html#selecting-features).