# What is GIS? (Theory)

__🔙[Back to Homepage](/content/intro.md)__

At its core, GIS is a computer-based system to organise data with a spatial 
component (_geodata_). There are three core functions of GIS: 

1. Connecting data to maps 
2. Visualisation, organisation and processing of spatial data
3. Analysing spatial data


```{figure} /fig/GIS_Core_functunality.drawio.svg
---
height: 500px
name: GIS_Core_functunality
align: center
---
GIS core functunality
```
Around these core GIS features there are a wide range of techniques, tools and 
applications - some are listed in the graphic below. As a GIS user, you need to 
know which techniques and tools to use to achieve a specific result. Although 
there are lots of tools and techniques out there, a surprisingly small number of 
them are sufficient to fulfil most tasks you will have. This platform provides 
materials to teach the tools that will be most useful for the kinds of mapping 
that are used in the humanitarian sector. 

```{figure} /fig/GIS_SIMS.drawio.svg
---
height: 750px
width: 900px
name: en_qgis_GIS_HA
align: center
---
GIS in humanitarian assistance
```

In the world of GIS, the product of your work will be a map most of the times. 
The graphic above shows the huge range of mapping products used in the 
humanitarian sector. 

To get a better understanding of how GIS is used in the humanitarian sector, we 
have collected some examples from different organisations in the section below 
(click the different tabs to view the examples by organisation). 


## Examples of GIS used by humanitarian organisations

::::{tab-set}

:::{tab-item} Lebanese Red Cross
This video gives an overview of GIS use in the Lebanese Red Cross in their 
operations, including informing ambulance services and supporting blood donations.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BNOgW9Koz7A?si=gpXNpFRmjfoPV1dX" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>
:::

:::{tab-item} IFRC

The International Federation of Red Cross and Red Crescent Societies (IFRC) 
publishes a wide variety of maps to support active operations. You can 
find some of those on [ReliefWeb](https://reliefweb.int/updates?advanced-search=%28S1242%29_%28F12%29)
or on the IFRC GO platform's [Emergency pages](https://go.ifrc.org/emergencies/all).
:::

:::{tab-item} ICRC
The International Committee of the Red Cross (ICRC) has a specialised GIS Support 
Unit that runs their [GIS Resource Center](https://gisupporticrc.github.io/GISResourceCenter/#portfolio) 
and ICRC GeoPortal. The ICRC resource centre portfolio gives an idea of the 
kinds of analysis the GIS unit produces, although much of it is not public. 
:::

:::{tab-item} REACH Initiative
REACH Initiative is a humanitarian data collection and analysis NGO that has a 
strong GIS specialism. The [REACH Resource Centre](https://www.impact-initiatives.org/resource-centre/) 
is where the organisation publishes content, including 
[standalone maps](https://www.impact-initiatives.org/resource-centre/?category[]=information_products&category[]=data_methods&type[]=281&order=latest&limit=10) 
and [reports](https://www.impact-initiatives.org/resource-centre/?category[]=information_products&category[]=data_methods&order=latest&limit=10) 
which also often include maps and spatial analysis. 
:::

:::{tab-item} Médecins Sans Frontières
Médecins Sans Frontières (MSF) has a [GIS Unit](https://geo.msf.org/home) that 
publishes geospatial products on the [GeoMSF platform](https://geo.msf.org/catalogue) 
to support MSF activities. 

MSF uses GIS in four main areas:
* Operations, emergency preparedness and response
* Healthcare
* Advocacy, communication and reporting
* Environmental health

This short video outlines the role of GIS in MSF's response to the 2015 Ebola 
outbreak in Sierra Leone. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/XxW_e9o0lA8?si=xS36hYai0rgmQW6J" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen></iframe>

:::

:::{tab-item} World Food Programme (WFP)
The World Food Programme (WFP) produces maps and publishes geodata both on their 
own data platform - [WFP Geonode](https://geonode.wfp.org/) and on the 
[Humanitarian Data Exchange (HDX)](https://data.humdata.org/organization/wfp?). 
You can find maps published by WFP on [RelifeWeb](https://reliefweb.int/updates?advanced-search=%28S1741%29_%28F12%29).  
WFP's [Geospatial Activities Catalogue](https://www.wfp.org/publications/wfp-geospatial-activities-catalogue)
outline's to organisation's geospatial services, which includes developing dashboards like this one one [cash assistance during the COVID-19 pandemic in Jordan](https://www.arcgis.com/apps/webappviewer/index.html?id=93b4605fff13415bb8d2decd0e9158e0).

WFP also builds dashboards for advocacy, like HungerMap Live:

%%html
<iframe src="https://hungermap.wfp.org/" width="750" height="500"></iframe>
:::

:::{tab-item} iMMAP
iMAAP is an information management NGO that provides support to the UN and 
international NGOs. Their [product portfolio](https://immap.org/products/) 
includes examples of maps used in sitaution overviews, interactive dashboards 
and sector-specific analysis.
:::

:::{tab-item} MapAction
MapAction produces maps and geospatial data support decision-making in emergency 
response. Their [maps and data](https://maps.mapaction.org/) page shows recent products they have published, and their [product catalogue](https://guides.mapaction.org/) 
gives an overview of the types of services they provide. 
:::

::::

 ## GIS vs cartography

 __Cartography__ is the study and practice of __making maps__. A GIS is a 
 __modern extension__ of traditional cartography. Both contain examples of a 
 __base map__ to which additional data can be added. The differences are that 
 there is no limit to the __amount of additional data__ that can be added to a 
 GIS map. Cartographic maps are often extremely simplified as there are limits 
 to the amount of data that can be physically and meaningfully stored on a small 
 map. GIS uses __analysis and statistics__ to present data in support of particular 
 arguments which a cartographic map cannot do. You can use GIS __for__ cartography.


## What is spatial analysis?

Many map products rely on spatial analysis. And indeed, the ability to use 
analysis tools allows us to get the most out of the data we have and to solve a 
wide variety of problems. The points below give you an simple definition of the 
concept.

However, the example of John Snow's cholera map of 1854 is a popular example of 
how spatial analysis can help to solve problems. 

- Spatial analysis __studies entities and events__ using their topological, 
  geometric, or geographic properties. 
- It includes a __variety of techniques__ to analyse geographic data. 
- Data can be __added to a map as layers and they can interact with each other__. 
- GIS enables you to work with these __layers__ to explore critically important 
  questions and __find answers__ to those questions.


### An example from the past: John Snow's cholera map

In 1854, an __outbreak of cholera__ occurred in the Soho area of London, England. 
The most common theory was that the disease was spread through the air. 
Dr. John Snow believed that the danger was __in the water__. He made a map to 
analyse the __number of deaths__ in every housing block in Soho. He added the 
__location of water pumps__ on the map. He found a __correlation__ between one 
specific water pump and the number of infections.

__Dr. Snow's map of the cholera outbreak of 1854__, and the reports that it 
accompanied, __won over the predominant "miasma theory"__ that the disease __was 
spread through the air__. Residents were now warned to __boil their water__, and 
so ended the last cholera outbreak London has seen.

This interactive version of the cholera map shows it overlaid on a basemap of 
modern London. 

```{figure} /fig/John_snow_zoom_map2.png
---
height: 600px
name: Snow_cholera_map_original
align: center
---
John Snow Cholera map of London (1854). Source: https://giscience.github.io/gis-training-resource-center/_images/John_snow_zoom_map2.png
```
__Using GIS__, several measures of spatial central tendency have been applied to 
the dataset, revealing that the Spatial Mean (the geographic center of the 
distribution of deaths) of the outbreak lies __within 35 meters of the Broad 
Street Pump__, identified as the __source of contamination__ in the 1854 outbreak. 

%%html
<iframe src="https://www.arcgis.com/apps/PublicInformation/index.html?appid=d7deb67f810d46dfacb80ff80ac224e9" width="750" height="500"></iframe>


# Common map types in humanitarian response

The humanitarian sector tends to use certain types of maps regularly. These are
outlined below. 

### General reference maps

-  Show important __physical features__ of an area
-  Include __natural and man-made features__
-  Usually meant to help for __navigation__ or discovery of locations
-  Usually fairly __simple__
-  Can be __styled__ based on the intended audience

![Reference map of Iraq](/fig/en_Reference_Map_Iraq.png) _Reference map of Iraq 
by REACH Initiative ([source]())_ <!-- FIXME: add source! -->

### Infrastructure maps

 - Display relevant features and __structures__ in a specific area
 - Help __planning__ and navigation
 - High level of __detail__
 - Produced after field __data collection__

![Infrastructure map of Nigeria](/fig/en_Infrastructure_Map_Nigeria.png) 
_Infrastructure map of a displaced persons camp in Borno State, Nigeria, produced 
by Reach Initiative. ([source]())_ <!-- FIXME: add source! -->

### Thematic maps

  - Focus on a __specific theme__ or subject
  - Features on the map __represent the subject__ being mapped
  - Use __colours and shapes__ to display quantitative and qualitative data
  - Rise __awareness__ about a specific subject

![Thematic map of Africa](/fig/en_Thematic_Map_Africa.png) 
_Thematic map of Africa_
<!-- FIXME: explain the map and add source -->

### Analysis maps

  - __Analyse data__ in respect to their geographic location
  - Create __new layers of information__ from the interaction between multiple features
  - Use colours and shapes __to help users__ understand specific events
  - __Support__ decision makers
  - Generally display a greater __level of detail__
  
![Analysis map of Yemen](/fig/en_Analysis_Map_Yemen.png) 
_Analysis map showing areas affected by flooding in Yemen, produced by Reach 
Initiative. ([source]())_ <!-- FIXME: add source -->

### Situation/descriptive maps

  - Used to __better visualize__ a specific ongoing and/or past situation 
  - Maps can include __narrative__ and graphic elements 
  - Can be used in reports and/or to __raise awareness__ on a specific event 

![Situation map from Tilkaif to Mosul](/fig/en_Situation_Map_Tilkaif_Mosul.png) 
_Situation map from Tilkaif to Mosul_ <!-- FIXME: explain the map and add source -->


 ## Web & mobile GIS applications

You can use GIS through __multiple applications__, from desktop software, to 
online platforms, to mobile apps. At a basic level, you can perform limited 
geospatial tasks with apps such as __Google Earth__ or __Google Maps__.
As a GIS professional, you will mostly use a __desktop software__, which could 
be either proprietary (requiring a license, e.g ESRI's ArcGIS) or open-source 
(available to use for free, e.g. QGIS). However, web applications can be relevant 
for obtaining data or to share data and maps with others.
 
Here are some online GIS platforms and tools you should be aware of; we'll use 
some of them later in the training. 

- __[OpenStreetMap (OSM)](https://www.openstreetmap.org/)__: 
An __open geographic database__ updated and maintained by a community of volunteers 
via open collaboration. It works using a tag system (each feature is categorized 
through tags).
- __[uMap](https://umap.openstreetmap.fr/en/)__: 
An online GIS application based on OpenStreetMap. You can upload standard geodata 
formats and do nice visualisation. Umap is very good for sharing maps and 
presenting basic interactive maps.
- __[Felt](https://felt.com/)__: 
Felt is similar to uMap but even pretteier. An __easy tool__ to create maps. You 
can draw, create feature and upload shapefiles. Plus, you can connect it to you 
QGIS with an plugin. In this way, you can use Felt for collaborative work.
- __[Wikimapia](https://wikimapia.org/)__: 
Online editable map service. Updated and maintained by contributors all over the 
world. It uses __local knowledge__, making it particularly useful in remote areas.
- __[Google Maps](https://www.google.com/maps)__:
Limited, but it allows to upload layers, create and export features, __share 
simple maps__.

### Mobile apps overview 

Mobile GIS apps are important for navigation and mobile data collection. 
Some of the most important free and open-source apps are listed below. 

- __[Qfield](https://docs.qfield.org/)__: Through QFieldCloud, you can __open 
your QGIS projects__ on Qfield on your mobile device. Any edit made on the map 
in the app can then be synced and displayed in QGIS.
- __[OsmAnd](https://osmand.net)__: Using OSM basemap, it’s a good app for 
__offline navigation__. You can upload `.kml` files to display on the map, as well 
as recording your trips and then exporting them.
- __[GeoODK](http://geoodk.com/index.htm)__: Combines __OpenDataKit (ODK) with a geo app__. 
You can collect data through ODK surveys and display them on a map, in addition 
to easily create polygons and add information to them.






