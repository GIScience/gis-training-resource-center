# Spatial Queries


__🔙[Back to Homepage](/content/intro.md)__

## Manual selection

- In the toolbar, select the ![](/fig/selection_toolbar_feature_selection.png) `Select Features` tool.
- Select features individually by clicking on a feature.
- To select several features, you can press and hold <kbd>Ctrl</kbd> (<kbd>Cmd</kbd> on MacOS) and select one feature after the other. 
- Selected features will be highlighted in bright yellow. 
- If you open the [attribute table](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html), the selected feature will appear in blue.



:::{dropdown} Example: Manually select countries
:open:
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_features_by_click_wiki.mp4"></video>
:::


## Select by Location

- QGIS lets you select features based on their location using the tool `Select by Location`.
- The tool uses spatial queries to select features. These look at the spatial relations between a set of features. 
- For example two features can intersect, or another feature is fully contained within another, or two features do not touch each other (disjoint). 
- QGIS uses the following spatial relations: Intersect, Contain, Disjoint, Equal, Touch, Overlap, Are Within, Cross.
- Check out the [QGIS documentation on spatial relations](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectorselection.html#exploring-spatial-relations) to learn the differences between each spatial relation.

:::{dropdown} Example: Select all cities in China (`intersect`)
:open:
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_intersect_wiki.mp4"></video>
:::

:::{dropdown} Example: Select all neighboring countries of China (`touch`)
:open:
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_touch_wiki.mp4"></video>
:::


## Export Selection

- Once selected, you can further manipulate the features by, for example, exporting them to a new layer:
    - <kbd>Right-click</kbd> on the layer with the selected features -> `Export` -> `Save selected features as..`

