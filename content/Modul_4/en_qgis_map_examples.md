# Map Example

In this chapter we will go over some common mistakes and good practice in map design. A second part of this chapter will be dedicated to discuss well designed maps and give examples on how to recreate the design in QGIS.

## Map Examples

In this section, we will present some well designed maps and discuss how to create similar maps. If you need further examples for good map design, check out these websites/repositories: 
- [researchresourcecentre.info maps](https://www.reachresourcecentre.info/search/?search=1&initiative%5B%5D=reach&ptype%5B%5D=map&dates=&keywords)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://reliefweb.int/updates?advanced-search=%28S1242%29_%28F12%29)

```{figure} ../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name:Somali Ethiopia Flood Areas 2023
width:750 px
---
```

The map above shows the flood affected areas, as well as the important road networks in the Somali Region, Ethtopia, in November 2023. Maps such as these are crucial for humanitarian aid workers when planning relief or aid operations and need to be up to date. They display important settlements, and most importantly, the accessibility of roads and airstrips. 

This is a thematic map with a clear purpose and the elements on the map are reduced to the most necessary elements relevant to the purpose of the map.

>Insert links to the tutorial content/wiki

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

```{figure} ../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
```
