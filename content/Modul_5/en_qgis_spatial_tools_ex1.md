# Exercise 1: Healthsite distribution in Saint Louis region

## Aim of the exercise
Become familiar with different types of spatial analysis and geoprocessing tools. Understand the process of discovering relationships and connections between features in spatial data. 

### Links to Wiki articles
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Projections](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html)
* [Spatial Queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html)
* [Geoprocessing](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html)
* [Categorized classification](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)

### Data
Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `sen_healthsites.shp`: [Senegal healthsites data](https://data.humdata.org/dataset/senegal-healthsites)
- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Senegal boundary data (Admin level 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `EO4SD_SAINT_LOUIS_FLOOD_2018.shp`: [Saint Louis flood extend data](https://wbwaterdata.org/dataset/saint-louis-senegal-flood-risk-map-esa-eo4sd-urban)

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

### Task

The goal of this exercise will be to assess the healthsite distribution in the Saint Louis region in Senegal and which healthsites are prone to flooding.

```{Hint}
The projected coordinate system for Senegal is `EPSG:32628 WGS 84 / UTM zone 28N`
```

1. Load the healthsites layer (`sen_healthsites.shp`) and the administrative boundary data (`sen_admbnda_adm1_1m_gov_ocha_20190426.shp`) into your QGIS project. Add OpenStreetMap as a background layer (Hint: XYZ via the browser window or the QuickMapServices plugin).

2. Make sure to reproject the dataset with the __administrative boundaries__ and the dataset with the __healthsites__ into UTM zone 28N. Use the tool `Reproject layer` for this process. See the Wiki entry on [projections](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html) for further information.

3. Select all healthsites which are located within the Saint Louis region:
    - Select the region `Saint Louis` in the boundary layer. You can just manually select the specific rows. See the Wiki entry on [spatial queries](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_queries_wiki.html) for further information.
    - Save the selection under the new name `Saint_Louis_region` in an extra layer. This can be done by right clicking on the boundary layer --> `Export` --> `Save Selected Features As...`

```{figure} /fig/en_ex2_export_selected.PNG
---
width: 40%
name: export_selected_features
---
Screenshot of how to export selected features
```

4. Use the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` or ![](/fig/mAlgorithmClip.png) `Clip` tool to select all health facilities within the `Saint_Louis_region` layer.
    - Save the new selection under the new name `healthsites_Saint_Louis` in an extra layer (Hint: right click on layer, Export, ...).

```{figure} /fig/en_ex2_select_by_location.PNG
---
width: 70%
name: select_by_location
---
Screenshot of the select by location tool
```

5. Investigate the flood risk in Saint Louis. Following the successful selection of all healthsites in the Saint Louis region in the previous step, proceed to load the flood extent layer of Saint Louis into QGIS:
    - Add the flood extent layer (`EO4SD_SAINT_LOUIS_FLOOD_2018.shp`)
    - While the layer does not cover the entirety of the Saint Louis region, it extends beyond Saint Louis in the north. Utilize the ![](/fig/mAlgorithmClip.png) `Clip` tool to clip the flood extent layer to the Saint Louis region (Hint: as input use Saint Louis flood extent, use Saint_louis_region as the overlay) for a more concentrated focus on central Saint Louis. See the Wiki entry on [Geoprocessing](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html) for further information.
    - Save the selection as `Saint_Louis_flood_clipped`.

6. When looking at the attribute table of the `Saint_Louis_flood_clipped` layer (Watertype column), you will see that the layer includes flooded, non-flooded and water body areas. Visualize only the flooded areas and water bodies in the dataset:
    - Go into `Symbology` and change the first selection from "Single symbols" to `Categorized`.
    - Select the column `Watertype` and click `Classify`.
    - Choose different colors for both the water bodies and the flooded areas. Leave non-flooded areas unmarked or make them transparent (opacity = 0%).
    - Visual exploration: Which areas are more and less prone to flooding?

```{figure} /fig/en_ex2_screenshot_flood.PNG
---
width: 50%
name: screenshot_flood
---
Screenshot of the water bodies and flooded areas    
```

7. Assess which healthsites are prone to flood risk.
    - Make use of the `Select by expression` tool to select all flooded areas in the `Saint_Louis_flood_clipped` layer. You can access this tool through the attribute table by clicking on this symbol ![](/fig/mIconExpressionSelect_new.png)
    - Save the selection in a separate layer. Name it `Saint_Louis_flooded_areas`.
    - You can now remove the `Saint_Louis_flood_clipped` layer to avoid confusion.
    - Make use of the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` tool to assess which healthsites are prone to flooding because they are located within the flooded areas in Saint Louis (Hint: Select features from: `healthsites_Saint_Louis`; By comparing to: `Saint_Louis_flooded_areas`).
    - Check the attribute table of the `healthsites` layer for the selected features were one pharmacy and one hospital should be selected.

```{figure} /fig/en_ex2_select_by_expression.PNG
---
width: 70%
name: select_by_expression
---
Screenshot of the Select by expression tool
```

```{figure} /fig/en_ex2_select_by_location_health.PNG
---
width: 70%
name: select_by_location
---
Screenshot of the Select by location tool
```

8. Which healthsites are located close to flooded zones?
    - Create a ![](/fig/mAlgorithmBuffer.png) buffer around the healthsites in Saint Louis with a distance of `20 meters`. See the Wiki entry on [Geoprocessing](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geoprocessing_wiki.html) for further information.
    - Make use of the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` tool to assess which buffers intersect with the flooded areas.
    - How many healthsites are selected? Check the attribute table. The selection should include five pharmacies and one hospital.
    - Feel free to experiment with additional buffer distances.

```{Hint}
At this stage at the latest, you will be reminded to reproject your layers. Meaningful buffers can only be calculated in projected coordinate systems. The projected coordinate system for Senegal is `EPSG:32628 WGS 84 / UTM zone 28N`
```

```{figure} /fig/en_ex2_buffer.PNG
---
width: 60%
name: buffer
---
Screenshot of the buffer process
```

