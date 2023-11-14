# What is GIS? (Theory)

At its core GIS is a computer-based system to organises data with any spatial component. Also, called geodata. There are three core functions of GIS. 

```{figure} /fig/GIS_Core_functunality.drawio.svg
---
height: 500px
name: GIS_Core_functunality
align: center
---
GIS Core functunality
```
Around this core of GIS evolves a galaxy of techniques, tools and applications. Some are listed in the graphic below. As a GIS user, you need to know which techniques and tools you need to use to achieve a specific result. Although there are so many techniques and tools out there, a surprisingly small number of them are sufficient to fulfil most tasks in the field of GIS.
Here at our GIS Training Resource Center, you can learn exactly these basic techniques. 

```{figure} /fig/GIS_SIMS.drawio.svg
---
height: 750px
width: 900px
name: en_qgis_GIS_HA
align: center
---
GIS in Humanitarian Assistance
```
In the world of GIS, the product of your work will be most of the time a map. In the humanitarian work, the range of published maps is huge. Just have a look at the graphic above.
However, most of them can be produced with the basic techniques you will learn here, depending on the available data. 

To get a better understanding of the use of GIS in humanitarian assistance, we dot some example from different organisations for you. Some of the map products puplished by these organisation you will find in the graphic above.

__Examples of GIS used by Humanitarian Organisations__

::::{tab-set}

:::{tab-item} Lebanese Red Cross
The Lebanese Red Cross (LRC) has used GIS for years and produces stunning results. Here is talk of LBC staff, have a look.
<iframe width="560" height="315" src="https://www.youtube.com/embed/BNOgW9Koz7A?si=gpXNpFRmjfoPV1dX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
:::

:::{tab-item} IFRC

The IFRC publishes a wide variety of maps in many different contexts. You can find some of those on [RelifeWeb](https://reliefweb.int/updates?advanced-search=%28S1242%29_%28F12%29).
:::

:::{tab-item} ICRC
The ICRC has a specialised GIS Support Unit. They run the [GIS Resource Center](https://gisupporticrc.github.io/GISResourceCenter/) and ICRC GeoPortal. ICRC utilized the ArcGIS of Esri. ArcGIS is not free, however, very versatile.
:::

:::{tab-item} REACH Initiative
The REACH initiative provides humanitarian actors with maps reports and Web-maps & online dashboards. 
REACH is a joint initiative of IMPACT Initiatives, ACTED and the United Nations Operational Satellite Applications Programme (UNOSAT). 
[Here](https://www.reachresourcecentre.info/search/?search=1&initiative%5B%5D=reach&ptype%5B%5D=map&dates=&keywords=) you can have a look at the maps REACH publishes.
:::

:::{tab-item} Médecins Sans Frontières
MSF is very big when it comes to GIS. They run the [MSF GIS Unit](https://geo.msf.org/home) and the GeoMSF Platform, which is an extensive online GIS platform which supports MSF missions.
Have a look at their catalogue of maps [here](https://geo.msf.org/catalogue)

MSF uses GIS in these four principal areas:
* Operations, Emergency Preparedness and Response
* Healthcare
* Advocacy, Communication and Reporting
* Environmental Healt

One very impressive use case of GIS during the Ebola outbreak in Sierra Leone in 2015 was documented in the video below.
<iframe width="560" height="315" src="https://www.youtube.com/embed/XxW_e9o0lA8?si=xS36hYai0rgmQW6J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

:::

:::{tab-item} World Food Programme (WFP)
WFP is BIG in the are of GIS. The provide a lot od geodata on [HDX](https://data.humdata.org/organization/wfp?) and pluisch many maps on [RelifeWeb](https://reliefweb.int/updates?advanced-search=%28S1741%29_%28F12%29).  Here you can check out the [WFP Geospatial Activities Catalogue]( https://www.wfp.org/publications/wfp-geospatial-activities-catalogue). WFP provides dashboards for local context like this one [Cash Assistance during the COVID-19 Pandemic in Jordan]( https://www.arcgis.com/apps/webappviewer/index.html?id=93b4605fff13415bb8d2decd0e9158e0).

WFP also runs shiny Dashboards for advocacy like the Live HungerMap below.
%%html
<iframe src="https://hungermap.wfp.org/" width="750" height="500"></iframe>
:::

:::{tab-item} iMMAP
[iMMAP](https://immap.org/products/) 
:::

:::{tab-item} MapAction
[MapAction](https://maps.mapaction.org/)
:::

::::

 ## GIS vs Cartography

 __Cartography__ is the study and practice of __making maps__. A GIS is a __modern extension__ of traditional cartography. Both contain examples of a __base map__ to which additional data can be added. The differences are that there is no limit to the __amount of additional data__ that can be added to a GIS map. Cartographic maps are often extremely simplified as there are limits to the amount of data that can be physically and meaningfully stored on a small map. GIS uses __analysis and statistics__ to present data in support of particular arguments which a cartographic map cannot do. You can use GIS __for__ cartography.


## What is Spatial Analysis?

Many map products relay on spatiall analysis. And indeed, the ability to use analysis tool allows us to get the most out of the data we have and to solve a wide variety of problems. The points below give you an simple definition of the concept.

However, the example of John Snows Colera Map of 1854 is THE example of what spatial Analysis actually is.


- Spatial analysis __studies entities and events__ using their topological, geometric, or geographic properties. 
- It includes a __variety of techniques__ to analyse geographic data. 
- Data can be __added to a map as layers and they can interact with each other__. 
- GIS enables you to work with these __layers__ to explore critically important questions and __find answers__ to those questions.


### An Example from the Past: John Snows' Cholera Map

In 1854 an __outbreak of cholera__ occurred in London, England. The most common theory was that the disease was spread through the air. Dr.John Snow believed that the danger was __in the water__. He made a map to analyse the __number of deaths__ in Soho per house block. He added the __location of water pumps__ on the map.
He found a __correlation__ between one specific water pump and the number of infections.

__Dr. Snow's map of the Cholera outbreak of 1854__, and the reports that it accompanied, __won over the predominant "Miasma Theory"__ that the disease __was spread through the air__. Residents were now warned to __boil their water__, and so ended the last Cholera outbreak London has seen.

```{figure} /fig/John_snow_zoom_map2.png
---
height: 600px
name: Snow_cholera_map_original
align: center
---
John Snow Cholera map of London (1854)
```
__Using GIS__, several measures of spatial central tendency have been applied to the dataset, revealing that the Spatial Mean (the geographic center of the distribution of deaths) of the outbreak lies __within 35 meters of the Broad Street Pump__, identified as the __source of contamination__ in the 1854 outbreak. 

%%html
<iframe src="https://www.arcgis.com/apps/PublicInformation/index.html?appid=d7deb67f810d46dfacb80ff80ac224e9" width="750" height="500"></iframe>



# Most used map types in humanitarian responses?

Now you now the concept of GIS and Spatial Analysis, we want to have a closer look at typical map products in humanitariann assistance.


### General Reference Maps

-  Show important __physical features__ of an area
-  Include __natural and man-made features__
-  Usually meant to help for __navigation__ or discovery of locations
-  Usually fairly __simple__
-  Can be __stylized__ based on the intended audience


![Reference map of Iraq](/fig/en_Reference_Map_Iraq.png)  Reference map of Iraq

### Infrastructure Maps

 - Display relevant features and __structures__ in a specific area
 - Help __planning__ and navigation
 - High level of __detail__
 - Produced after field __data collection__


![Infrastructure map of Nigeria](/fig/en_Infrastructure_Map_Nigeria.png) 
Infrastructure map of Nigeria
 
### Thematic Maps

  - Focus on a __specific theme__ or subject
  - Features on the map __represent the subject__ being mapped
  - Use __colours and shapes__ to display quantitative and qualitative data
  - Rise __awareness__ about a specific subject


![Thematic map of Africa](/fig/en_Thematic_Map_Africa.png) Thematic map of Africa

### Analysis Maps

  - __Analyse data__ in respect to their geographic location
  - Create __new layers of information__ from the interaction between multiple features
  - Use colours and shapes __to help users__ understand specific events
  - __Support__ decision makers
  - Generally display a greater __level of detail__

  <tagName>  <tagName>
  
![Analysis map of Yemen](/fig/en_Analysis_Map_Yemen.png) Analysis map of Yemen

### Situation/Descriptive Maps

  - Used to __better visualize__ a specific ongoing and/or past situation 
  - Maps can include __narrative__ and graphic elements 
  - Can be used in reports and/or to __raise awareness__ on a specific event 

<tagName>  <tagName>

![Situation map from Tilkaif to Mosul](/fig/en_Situation_Map_Tilkaif_Mosul.png)Situation map from Tilkaif to Mosul

 ## Web & Mobile GIS Applications


You can use GIS through __multiple applications__, from desktop software, to online platforms, to mobile apps. At a basic level, you can perform limited geospatial tasks with apps such as __Google Earth__ or __Google Maps__.
As a GIS professional, you will mostly use a __desktop software__, which could be either: Proprietary e.g ArcGIS or Open source e.g. QGIS.
However, web applications can be relevant for obtaining data or to share data and maps with others.
 
Below we have listed some applications you should know. With some of those, you will work in other training modules.


- __[Open Street Maps (OSM)](https://www.openstreetmap.org/#map=14/49.4192/8.7235)__: An __open geographic database__ updated and maintained by a community of volunteers via open collaboration. It works using a tag system (each feature is categorized through tags).
- __[uMap](https://umap.openstreetmap.fr/en/)__: 
An online GIS application based on OpenStreetMap. You can upload standard geodata formats and do nice visualisation. Umap is very good for sharing maps and presenting basic interactive maps.
- __[Felt](https://felt.com/)__: 
Felt is similar to uMap but even pritteier. An __easy tool__ to create maps. You can draw, create feature and upload shapefiles. Plus, you can connect it to you QGIS with an plugin. In this way, you can use Felt for collaborative work.
- __[Wikimapia](https://wikimapia.org/#lang=de&lat=49.402500&lon=8.633100&z=12&m=w)__: 
Online editable map service. Updated and maintained by contributors all over the world. It uses __local knowledge__, making it particularly useful in remote areas.
- __[Google Maps](https://www.google.com/maps/d/)__:
Limited, but it allows to upload layers, create and export features, __share simple maps__.

### Geo Mobile Apps Overview 

Mobil GIS Apps are highly important for navigation and mobil data collection. Some of the most important free and open-source apps are listed below. 

- __[Qfield](https://docs.qfield.org/)__: Through QFieldCloud, you can __open your QGIS projects__ on Qfield on your mobile device. Any edit made on the map in the app can then be synced and displayed in QGIS.
- __[OsmAnd](https://osmand.net)__: Using OSM basemap, it’s a good app for __offline navigation__. You can upload kml-files to display on the map, as well as recording your trips and then export them to kml.
- __[GeoODK](http://geoodk.com/index.htm)__: Combines __ODK with a geo app__. You can collect data through ODK surveys and display them on a map, in addition to easily create polygons and add information to them.






