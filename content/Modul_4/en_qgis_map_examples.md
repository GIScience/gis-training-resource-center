# Examples for Good Map Design

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

In this chapter we will be discuss well designed maps and give examples on how to recreate the design elements in QGIS.

> TO DO:  
Insert Overview  
Insert links to the tutorial content/wiki

In this section, we will present some well designed maps and discuss how to create similar maps. If you need further examples for good map design, check out these websites/repositories: 
- [researchresourcecentre.info maps](https://www.reachresourcecentre.info/search/?search=1&initiative%5B%5D=reach&ptype%5B%5D=map&dates=&keywords)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://reliefweb.int/updates?advanced-search=%28S1242%29_%28F12%29)


## Map Examples
### Map Example 1: Flood-affected areas and roads in the Somali Region, Ethiopia

```{figure} ../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: Flood affected Areas in Somali
width: 800 px
---
Flood affected areas and roads in Somali Region, Ethiopia (Source: OCHA)
```

The map above shows the flood affected areas, as well as the important road networks in the Somali Region, Ethtopia, in November 2023. Maps such as these are crucial for humanitarian aid workers when planning relief or aid operations and need to be up to date. They display important settlements, and most importantly, the accessibility of roads and airstrips. 

This is a thematic map with a clear purpose and the elements on the map are reduced to the most necessary elements relevant to the purpose of the map.


- A shapefile for the flood affected areas was given a hashed fill. In QGIS, you can find this symbology 
- A layer with the road network has been put above the layer with the flood-affected areas. The road symbology has been __categorized__ into three categories: Accessible road (green), partially accessible road (grey), and hard to reach road (red).
- The topmost layer is a point-layer with information on unaccessible roads or bridges as well as the location of airstrips and which airstrips are accessible. The points have been symbolized with SVG-symbols. 
- (The administrative boundaries of Ethiopia are set apart from the surrounding countries by making the polygon a clear white and the surrounding countries in a shade of grey. This can be achieved by copying the polygon of Ethiopia into a new layer, and changing the symbology respectively)

```{note} 
The colour scheme of the roads makes an intuitive reading of the map possible, as red is associated with negative qualities, whereas green with positive qualities. It should be noted, however, that persons with colourblindness will have trouble reading the map.
```

:::{dropdown} Context: Situation in Ethiopia

:::

---

### Map Example 2: Flooding Risk in the Ouham Region, Central African Republic

```{figure} ../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
---
name: flooding risk
width 800 px
---
Flooding risk in the Ouham Region, Central African Republic (Source: REACH)
```

This map displays the flooding risk using a raster image. The raster data was calculated using several factors, including the precipitation intensity, the maximum duration of precipiation, the height of the nearest drainage, the flow direction and river network, the topographic humidity, a digital elevation model and the ground cover. 

- The raster data is displayed using a diverging colour ramp. (Here you can check out how to assign a colour ramp) 
- The surrounding administrative districts have been overlayed with a transparent grey. 
- The river network has been added in blue
- The mainroads as well have been added in black
- Settlements are displayed i black dots. This helps to identify areas whith a higher population density in the areas most at risk

:::{dropdown} Context: Situation in the Central African Republic

:::

---
### Map Example 3:

```{figure} ../../fig/REACH_AFG_Map_ABR_infrastructure_mapping_Kunduz_Kunduz_PD-07_17May2022_A3P.png
---
name: Infrastructure Map Kunduz District Afghanistan
width: 800 px
---
Infrastructure Map Kunduz Province 
```

