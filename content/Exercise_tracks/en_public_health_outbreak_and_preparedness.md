# Exercise Track: Outbreak and Preparedness in the Public Health Sector

🚧 Under Construction 🚧

This training module is designed for humanitarian public health professionals working with geospatial data to support outbreak detection, response planning, and operational decision-making.  
Using QGIS and openly available datasets, you will learn how to integrate health data, population estimates, and accessibility modelling to answer key epidemiological questions.

The exercises follow a realistic measles outbreak scenario in Chad and guide you step-by-step through data import, processing, visualization, and spatial analysis — all using methods applicable to real field operations and MoH workflows.

## Scenario: Measles Outbreak in Chad

:::{note}

The scenario and the measles data (cases, vaccination coverage, healthsites capacities) is __entirely fictional__ and does not represent any real-world data or trends. 

:::

Chad is experiencing a surge in suspected measles cases across several regions.  
The Ministry of Health, in coordination with humanitarian partners, is requesting geospatial analysis to support:

- mapping health infrastructure,
- estimating populations at risk,
- identifying high-incidence districts,
- assessing physical access to vaccination services,
- and guiding deployment of mobile vaccination teams.

Each exercise builds on the previous one, using real-world data workflows common in humanitarian settings.

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_3/en_module_3_public_health_ex_1.html
__Part 1: Creating an overview map of the health system and vaccination coverage__
^^^
The aim of this exercise is to produce a map showing the distribution of healthsites with the capacities to treat measle cases and coordinate a vaccination campaign

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_5/en_qgis_module_5_public_health_ex_2.html
__Part 2: Calculating affected population__
^^^
The Epidemiology Department has shared a line-list of suspected measles cases reported by health districts. Your task in this exercise is to combine this surveillance data with population estimates from WorldPop to identify districts with high measles incidence rates. This will help the response coordination team prioritise vaccination deployments and plan logistics for outreach activities.

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_9/en_qgis_module_9_public_health_ex_9.html
__Part 3: Assessing Accessibility to Vaccination Services__ 
^^^

Following your analysis of measles incidence rates per district, the Ministry of Health now wants to identify which populations have limited access to vaccination services. In this exercise, you will use the **OpenRouteService (ORS)** tools developed by HeiGIT to model accessibility and determine how many people live **beyond a reasonable travel distance** from a vaccination point.

Accessibility to health services is a key determinant of vaccination coverage. In many rural parts of Chad, communities may not have access to motorised transport and rely on walking or infrequent public transport. Thus, distance alone is not always a good measure — **travel time** provides a more realistic assessment.

:::

:::{card}
:link: 
__Part 4: Creating a situation map to help decision-making__
^^^

In this part, the print layout composer will be used to create an publishable and printable situation map of the vaccination coverage and accessibility to vaccination facilities. Additionally, we will prepare a map template, so updating the map will be easier!

:::

