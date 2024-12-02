# Examples of Good Map Design

🚧This page on the training platform and the entire content is under ⚠️construction⚠️🚧

In this chapter we will discuss well designed maps and give examples of how to recreate specific design elements in QGIS. A second part of this chapter will focus on common mistakes and good practices when designing maps.

<!--TO DO:  
Insert Overview  
Insert links to the tutorial content/wiki
Insert examples in the 4 semiological errors part
-->

In this section, we will present some well-designed maps and discuss how to create similar maps. If you need further examples for good map design, check out these websites/repositories:

- [impact-initiatives.org/resource-centre maps](https://www.impact-initiatives.org/resource-centre/?category%5B%5D=information_products&category%5B%5D=data_methods&type%5B%5D=281&order=latest&limit=10)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://reliefweb.int/updates?list=Maps%20/%20Infographics&view=maps)

## Map Examples

### Map Example 1: Flood-affected areas and roads in the Somali Region, Ethiopia

```{figure} ../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: Flood affected Areas in Somali
width: 800 px
---
Flood affected areas and roads in the Somali Region, Ethiopia (Source: OCHA)
```

:::{dropdown} Context: Situation in Ethiopia
The Greater Horn of Africa receives 20 to 70 percent of the annual total rainfall in the months from October to December. The IFRC reports a exceptionally high forecast probability (over 80%) of experiencing wetter than normal rainfall condition. Additionally, El Niño conditions started between July and August, which further accrued the possibility of high rainfall conditions in Ethiopia.

Since October, floods have affected at least 763,000 people in the region, taken 33 lives in the Somali Region alone, and killed 4,806 livestock. The flooding has also resulted in immense damage to infrastructure, transportation, and schooling. The population's livelihood and health have been greatly affected.
The impact of flooding is projected to increase in the next years, which will lead to more flash and river floods.

Access maps, such as the one above, play a crucial role in helping informing information manager and ground staff which areas are accessible. This is especially important as a timely deployment of relief or aid operations is essential in flooding disasters.

(Source: [IFRC](https://go.ifrc.org/emergencies/6773/details))
:::

The map above shows the flood-affected areas, as well as the important road networks in the Somali Region, Ethiopia in November 2023. Maps such as these are crucial for humanitarian aid workers when planning relief or aid operations and need to be up-to-date. They display important settlements and, most importantly, the accessibility of roads and airstrips. 

This is a thematic map with a clear purpose, featuring only the most essential elements relevant to that purpose.

- A shapefile for the flood affected areas was given a hashed fill. In QGIS, you can find this symbology.
- A layer with the road network has been put above the layer with the flood-affected areas. The road symbology has been __categorised__ into three categories: Accessible road (green), partially accessible road (grey), and hard-to-reach road (red).
- The topmost layer is a point-layer with information on unaccessible roads or bridges as well as the location of airstrips and which airstrips are accessible. The points have been symbolized with SVG-symbols. 
- (The administrative boundaries of Ethiopia are set apart from the surrounding countries by making the polygon a clear white and the surrounding countries in a shade of grey. This can be achieved by copying the polygon of Ethiopia into a new layer, and changing the symbology respectively)

```{note} 
The colour scheme of the roads makes it possible to read the map intuitively, as red is typically associated with negative qualities and green with positive qualities. It should be noted, however, that people with colourblindness will have trouble reading the map.
```

---

### Map Example 2: Flooding Risk in the Ouham Region, Central African Republic

```{figure} ../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
---
name: REACH Flooding Risk Ouhman Region, Central African Republic
width: 720 px
---
Flooding risk in the Ouham Region, Central African Republic (Source: REACH)
```
:::{dropdown} Context: Situation in the Central African Republic

The Central African Republic has been hit by destructive floods in late 2019, which displaced over 100,000 people and caused considerable damage to infrastructure. The floods have destroyed shelters, obstructed transportation routes, and have led to disease outbreaks such as cholera and malaria. Due to climate change, such floods will become more frequent, leading to increased vulnerability for towns and villages. Since natural hazards are hard to predict, the changing climate reduces community resilience.

Source: [REACH Initiative](https://reliefweb.int/report/central-african-republic/central-african-republic-flood-susceptibility-risk)
:::

This map displays the flooding risk using a raster image. The raster data was calculated using several factors, including the precipitation intensity, the maximum duration of precipitation, the height of the nearest drainage, the flow direction and river network, the topographic humidity, a digital elevation model, and the ground cover.

- The raster data is displayed using a diverging colour ramp. (Here you can see how to assign a colour ramp)
- The surrounding administrative districts have been overlayed with a transparent grey.
- The river network has been added in blue.
- The main roads as well have been added in black.
- Settlements are displayed as black dots. This helps to identify areas with a higher population density in the areas most at risk.

---

<!--### Map Example 3:

```{figure} ../../fig/REACH_AFG_Map_ABR_infrastructure_mapping_Kunduz_Kunduz_PD-07_17May2022_A3P.png
---
name: Infrastructure Map Kunduz District Afghanistan
width: 800 px
---
Infrastructure Map Kunduz Province 
```
-->

