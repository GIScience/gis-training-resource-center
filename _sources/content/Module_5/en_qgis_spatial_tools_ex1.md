::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Exercise 1: Health site distribution in the Saint Louis region

## Characteristics of the exercise

::::{grid} 2
:::{grid-item-card}
__Aim of the exercise:__
^^^

Become familiar with different types of spatial analysis and geoprocessing tools. Understand the process of discovering relationships and connections between features in spatial data. 

__Type of trainings exercise:__

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__Focus group (GIS-Knowledge Level):__
^^^

__These skills are relevant for:__


:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^ 

:::

:::{grid-item-card}
__Relevant Wiki Articles:__
^^^

* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Projections](/content/Wiki/en_qgis_projections_wiki.md)
* [Spatial Queries](/content/Wiki/en_qgis_spatial_queries_wiki.md)
* [Geoprocessing](/content/Wiki/en_qgis_geoprocessing_wiki.md)
* [Categorized classification](/content/Wiki/en_qgis_categorized_wiki.md)

:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

### Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::

### Data

Download the datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_1/Module_5_Exercise_1_Healthsite_distribution_Saint_Louis_region.zip) and unzip the files.

<!---Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `sen_healthsites.shp`: [Senegal health site data](https://data.humdata.org/dataset/senegal-healthsites)
- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Senegal boundary data (Admin level 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `EO4SD_SAINT_LOUIS_FLOOD_2018.shp`: [Saint Louis flood extend data](https://wbwaterdata.org/dataset/saint-louis-senegal-flood-risk-map-esa-eo4sd-urban)-->

```{Hint}
All files still have their original names. However, feel free to modify their names if necessary to identify them more easily.
```

### Task

The goal of this exercise will be to assess the health site distribution in the Saint Louis region in Senegal and determine which health sites are prone to flooding.

```{Hint}
The projected coordinate system for Senegal is `EPSG:32628 WGS 84 / UTM zone 28N`
```

1. Load the health sites layer (`sen_healthsites.shp`) and the administrative boundary data (`sen_admbnda_adm1_1m_gov_ocha_20190426.shp`) into your QGIS project. Add OpenStreetMap as a background layer (Hint: XYZ via the browser window or the QuickMapServices plugin).

```{attention} 
Always make sure that your datasets are provided in the correct projection. If this it not the case, it is necessary to reproject the data in the desired coordinates reference system. See the Wiki entry on [projections](/content/Wiki/en_qgis_projections_wiki.md) for further information.
```

2. Select all health sites which are located within the Saint Louis region:
    - Select the region `Saint Louis` in the boundary layer. You can just manually select the specific rows. See the Wiki entry on [spatial queries](/content/Wiki/en_qgis_spatial_queries_wiki.md) for further information.
    - Save the selection under the new name `Saint_Louis_region` in an extra layer. This can be done by right clicking on the boundary layer --> `Export` --> `Save Selected Features As...`

```{figure} /fig/en_ex2_export_selected.PNG
---
width: 40%
name: export_selected_features
---
Screenshot of how to export selected features
```

3. Use the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` or ![](/fig/mAlgorithmClip.png) `Clip` tool to select all health facilities within the `Saint_Louis_region` layer.
    - Save the new selection under the new name `healthsites_Saint_Louis` in an extra layer (Hint: right click on layer, Export, ...).

```{figure} /fig/en_ex2_select_by_location.PNG
---
width: 70%
name: select_by_location
---
Screenshot of the select by location tool
```

4. Investigate the flood risk in Saint Louis. Following the successful selection of all health sites in the Saint Louis region in the previous step, proceed to load the flood extent layer of Saint Louis into QGIS:
    - Add the flood extent layer (`EO4SD_SAINT_LOUIS_FLOOD_2018.shp`)
    - While the layer does not cover the entirety of the Saint Louis region, it extends beyond Saint Louis in the north. Use the ![](/fig/mAlgorithmClip.png) `Clip` tool to clip the flood extent layer to the Saint Louis region (Hint: as input use Saint Louis flood extent, use Saint_louis_region as the overlay) for a more concentrated focus on central Saint Louis. See the Wiki entry on [Geoprocessing](/content/Wiki/en_qgis_geoprocessing_wiki.md) for further information.
    - Save the selection as `Saint_Louis_flood_clipped`.

5. When looking at the attribute table of the `Saint_Louis_flood_clipped` layer (Watertype column), you will see that the layer includes flooded, non-flooded and water body areas. 

```{figure} /fig/en_ex1_attribute_table_floods.PNG
---
width: 40%
name: attribute_table_floods
---
Screenshot of the Saint_Louis_flood_clipped layer
```

6. Visualize only the flooded areas and water bodies in the dataset:
    - Go into `Symbology` and change the first selection from "Single symbols" to `Categorized`.
    - Select the column `Watertype` and click `Classify`.
    - Choose different colors for both the water bodies and the flooded areas. Leave non-flooded areas unmarked or make them transparent (opacity = 0%).
    - Visual exploration: Which areas are more and less prone to flooding?

```{figure} /fig/en_ex2_screenshot_flood.PNG
---
width: 40%
name: screenshot_flood
---
Screenshot of the water bodies and flooded areas    
```

7. Assess which health sites are prone to flood risk.
    - Make use of the `Select by expression` tool to select all flooded areas in the `Saint_Louis_flood_clipped` layer. You can access this tool through the attribute table by clicking on this symbol ![](/fig/mIconExpressionSelect_new.png)

```{figure} /fig/en_ex2_select_by_expression.PNG
---
width: 70%
name: select_by_expression
---
Screenshot of the Select by expression tool
```

8. Save the selection in a separate layer. Name it `Saint_Louis_flooded_areas`.

9. You can now remove the `Saint_Louis_flood_clipped` layer to avoid confusion.
    - Make use of the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` tool to assess which health sites are prone to flooding because they are located within the flooded areas in Saint Louis (Hint: Select features from: `healthsites_Saint_Louis`; By comparing to: `Saint_Louis_flooded_areas`).

```{figure} /fig/en_ex2_select_by_location_health.PNG
---
width: 70%
name: select_by_location
---
Screenshot of the Select by location tool
```

10. Check the attribute table of the `healthsites` layer for the selected features were one pharmacy and one hospital should be selected.

```{figure} /fig/en_ex1_selected_healthsites_senegal.PNG
---
width: 60%
name: selected_healthsites_senegal
---
Screenshot of the selected health sites in the flooded areas
```

11. Which health sites are located close to flooded zones?
    - Create a ![](/fig/mAlgorithmBuffer.png) buffer around the health sites in Saint Louis with a distance of `20 meters`. See the Wiki entry on [Geoprocessing](/content/Wiki/en_qgis_geoprocessing_wiki.md) for further information.

```{figure} /fig/en_ex2_buffer.PNG
---
width: 60%
name: buffer
---
Screenshot of the buffer process
```

```{Hint}
At this stage at the latest, you will be reminded to reproject your layers. Meaningful buffers can only be calculated in projected coordinate systems. The projected coordinate system for Senegal is `EPSG:32628 WGS 84 / UTM zone 28N`
```

12. Now make use of the ![](/fig/mAlgorithmSelectLocation.png) `Select by location` tool again to assess which buffers intersect with the flooded areas.

```{figure} /fig/en_ex1_select_healthsites_buffer.PNG
---
width: 60%
name: selected_healthsites_buffer
---
Screenshot of the Select by location tool for the buffered areas
```

13. How many health sites are selected? Check the attribute table. The selection should include five pharmacies and one hospital.
    - Feel free to experiment with additional buffer distances.

```{figure} /fig/en_ex1_selected_flooded_healthsites.PNG
---
width: 60%
name: selected_healthsites_flooded
---
Screenshot of the buffered and selected health sites in the flooded areas
```

The final result may be represented as follows: it will display the flooded areas, the buffered health sites, and the intersections between them. While these features might not be easily visible in QGIS, you can verify that everything worked correctly by checking the attribute table.

```{figure} /fig/en_ex1_final_result.PNG
---
width: 60%
name: ex1_final_result
---
Screenshot of the final result
```


