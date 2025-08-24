# Exercise Track: Anticipatory Action Analysis for Cyclones in Madagascar


This exercise track focuses on the preliminary assessment of a cyclone event in Madagascar. The goal is to create 
an analytical workflow as a QGIS model that estimates the exposed population, exposed infrastructure, and exposed 
agriculture land. Additionally, the accessibility of exposed regions can be assessed using pre-calculated 
isochrones. 
In this track, you will build an analytical workflow as a QGIS model and visualise the results using map templates 
and style files. 

::::{admonition} French version - Version française
:class: note

The french version of this exercise track can be found here: 

La version française de cet article se trouve ici:

```{card}
:class-card: sd-text-center sd-border-1
:link: https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/fr_mdg_aa_cyclones.html
__Piste d'Exercice : Analyse d’Action Anticipative pour les Cyclones à Madagascar__ 
```

::::

::::{card} 
Context
^^^

```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

Madagascar is frequently exposed to intense tropical cyclones, which can lead to widespread damage, displacement, and loss of life. Anticipatory analysis is essential to reduce the impact of these extreme weather events. By using forecast data and geospatial tools to predict the likely areas of impact, humanitarian actors and local authorities can take early action, such as pre-positioning supplies and issuing warnings, to protect lives and livelihoods before disaster strikes. This proactive approach strengthens preparedness and response capacities, ultimately saving time, resources, and lives.

Aina, the GIS expert at the Malagasy Red Cross (CRM), is preparing for the upcoming cyclone season. She wants to improve her team’s ability to act quickly once a storm is forecasted by automating key analyses in QGIS. These include estimating exposed populations, identifying impacted services like health and education, and assessing whether health posts can be reached from key warehouses within a critical 10-hour window.
The goal is to prepare an end-to-end analysis and visualization workflow that can support fast, data-driven anticipatory action before a cyclone makes landfall.

::::

---


:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_5/en_qgis_module_5_mdg_aa_ex_1.html
__Exercise 1: Estimating the Exposed Population - Aina's Manual Approach (Module 5)__
^^^


- importing datasets into QGIS
- reprojecting layers
- buffering vector layers
- clipping raster layers
- calculating zonal statistics
- applying graduated classification to results


:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_7/en_module_7_mdg_aa_ex_2.html
__Exercise 2: Automation of Exposed Population Estimation – Aina's Model (Module 7)__
^^^

- Using the model builder
- reprojecting layers
- buffering vector layers
- clipping raster layers
- calculating zonal statistics
- applying graduated classification to results

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_5/Module_7/en_module_7_mdg_aa_ex_2.html
__Exercise 3: Identifying Affected Health Facilities and Schools – Aina Adds More Layers (Module 7)__
^^^

- extending the model 
- Counting points in polygon
- using the field calculator

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_4/en_module_4_mdg_aa_ex_4.html
__Exercise 4: Visualizing Cyclone Impact Results – Aina Styles Her Layers (Module 4)__
^^^

- using the styling panel
- applying style files to layers
- saving style files

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_4/en_module_4_mdg_aa_ex_5.html
__Exercise 5: Quick Map Creation – Aina Uses Map Templates (Module 4)__
^^^

- using the print layout composer to create a map
- using map templates
- using attribtue tables in the print layout composer

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_7/en_module_7_mdg_aa_ex_6.html
__Exercise 6: Exporting Model Results for the Operations Team (Module 7)__
^^^

- expanding the model
- joining model results
- exporting the model output in spreadsheet (.csv) format

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_9/en_qgis_module_9_mdg_aa_ex_7.html
__Exercise 7: Reachability of health Posts from CRM Warehouses__
^^^

- filtering datasets
- performing a accessibility analysis
- updating datasets with new information
- visualising the accessibility of healthsites

:::

