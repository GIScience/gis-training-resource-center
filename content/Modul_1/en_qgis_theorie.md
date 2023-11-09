# What is GIS? (Theory)

At its core GIS is a computer-based system to organises data with any spatial component. Also, call geodata. There are three core functions of GIS. 

```{figure} /fig/GIS_Core_functunality.drawio.svg
---
height: 1000px
name: GIS_Core_functunality
align: center
---
GIS COre functunality
```
Around this core of GIS evolves a galaxy of techniques, tools and applications. Some are listed in the graphic below. As a GIS user, you need to know which techniques and tools you need to use to achieve a specific result. Although there are so many techniques and tools out there, a surprisingly small number of them are sufficient to fulfil most tasks in the field of GIS.
At the GIS Training Resource Center, you can learn exactly these basic techniques. 

```{figure} /fig/GIS_SIMS.drawio.svg
---
height: 1000px
name: en_qgis_GIS_HA
align: center
---
GIS in Humanitarian Assistance
```
In the world of GIS, the product of your work will be most of the time a map. In the humanitarian work, the range of published maps is huge. Just have a look at the graphic above.
However, most of them can be produced with the basic techniques you will learn here, depending on the available data. 

Here you can find the map products of important humanitarian organisations that use GIS. You will find many examples of maps shown in the graphic above.

::::{tab-set}

:::{tab-item} IFRC

The IFRC publishes a wide variety of maps in many different contexts. You can find some of those on [RelifeWeb](IFRC Maps on RelifeWeb).
:::

:::{tab-item} ICRC
The ICRC has a specialised GIS Support Unit. They run the GIS Resource Center and ICRC GeoPortal. ICRC utilized the ArcGIS of Esri. ArcGIS is not free, however, very versatile.
:::

:::{tab-item} Lebanese Red Cross
The Lebanese Red Cross (LRC) has used GIS for years and produces stunning results. Here is talk of LBC staff, have a look.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BNOgW9Koz7A?si=gpXNpFRmjfoPV1dX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


> **A few examples:** 

 - 
 - 
 -  
 - 
 - 



 ## Paper Maps and Cartography 

### What is Spatial Analysis?

- Spatial analysis __studies entities and events__ using their topological, geometric, or geographic properties. 
- It includes a __variety of techniques__ to analyse geographic data. 
- Data can be __added to a map as layers and they can interact with each other__. 
- GIS enables you to work with these __layers__ to explore critically important questions and __find answers__ to those questions.

<tagName>  <tagName>

> **An Example from the Past: John Snows' Cholera Map**  

In 1854 an __outbreak of cholera__ occurred in London, England. The most common theory was that the disease was spread through the air. Dr.John Snow believed that the danger was __in the water__. He made a map to analyse the __number of deaths__ in Soho per house block. He added the __location of water pumps__ on the map.
He found a __correlation__ between one specific water pump and the number of infections.

__Dr. Snow's map of the Cholera outbreak of 1854__, and the reports that it accompanied, __won over the predominant "Miasma Theory"__ that the disease __was spread through the air__. Residents were now warned to __boil their water__, and so ended the last Cholera outbreak London has seen.

![John Snows' Map](/fig/en_John_Snows_Map.png) John Snows' Map

__Using GIS__, several measures of spatial central tendency have been applied to the dataset, revealing that the Spatial Mean (the geographic center of the distribution of deaths) of the outbreak lies __within 35 meters of the Broad Street Pump__, identified as the __source of contamination__ in the 1854 outbreak. 

<tagName>  <tagName>

> **Further information**:

 - [Let’s explore John Snow’s map](https://www.arcgis.com/apps/PublicInformation/index.html?appid=d7deb67f810d46dfacb80ff80ac224e9)

## GIS vs Cartography

- __Cartography__ is the study and practice of __making maps__.
- A GIS is a __modern extension__ of traditional cartography. 
- Both contain examples of a __base map__ to which additional data can be added. 
- The differences are that there is no limit to the __amount of additional data__ that can be added to a GIS map. 
- Cartographic maps are often extremely simplified as there are limits to the amount of data that can be physically and meaningfully stored on a small map. 
- GIS uses __analysis and statistics__ to present data in support of particular arguments which a cartographic map cannot do. 
- You can use GIS __for__ cartography.

## Why are Spatial Analyses important?

> **Discuss in groups**  
- Situations in which you benefitted from spatial analyses.
- Situations in which you could may be have benefitted from spatial analyses.
- Main areas where you see potential for spatial analyses in your work.

<tagName>  <tagName>

![GIS vs Cartography](/fig/en_GIS_vs_Cartography.png) GIS vs Cartography

### General Reference Maps

-  Show important __physical features__ of an area
-  Include __natural and man-made features__
-  Usually meant to help for __navigation__ or discovery of locations
-  Usually fairly __simple__
-  Can be __stylized__ based on the intended audience

<tagName>  <tagName>

![Reference map of Iraq](/fig/en_Reference_Map_Iraq.png)  Reference map of Iraq

### Infrastructure Maps

 - Display relevant features and __structures__ in a specific area
 - Help __planning__ and navigation
 - High level of __detail__
 - Produced after field __data collection__

<tagName>  <tagName>

![Infrastructure map of Nigeria](/fig/en_Infrastructure_Map_Nigeria.png) 
Infrastructure map of Nigeria
 
### Thematic Maps

  - Focus on a __specific theme__ or subject
  - Features on the map __represent the subject__ being mapped
  - Use __colours and shapes__ to display quantitative and qualitative data
  - Rise __awareness__ about a specific subject

  <tagName>  <tagName>


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

 ## Web GIS platforms

### GIS Applications

- You can use GIS through __multiple applications__, from desktop software, to online platforms, to mobile apps. 
- At a basic level, you can perform limited geospatial tasks with apps such as __Google Earth__ or __Google Maps__.
- As a GIS professional, you will mostly use a __desktop software__, which could be either: Proprietary or Open source.

- __Open Street Maps (OSM)__: 
[https://www.openstreetmap.org/#map=14/49.4192/8.7235](
https://www.openstreetmap.org/#map=14/49.4192/8.7235)
An __open geographic database__ updated and maintained by a community of volunteers via open collaboration. It works using a tag system (each feature is categorized through tags).
- __uMap__: [https://umap.openstreetmap.fr/en/](https://umap.openstreetmap.fr/en/)
Online tool to create maps __using OSM layers__.
- __Felt__: [https://felt.com/](/https://felt.com/)
An __easy tool__ to create maps. You can draw, create feature and upload shapefiles.
- __Wikimapia:__ [https://wikimapia.org/#lang=de&lat=49.402500&lon=8.633100&z=12&m=w](
https://wikimapia.org/#lang=de&lat=49.402500&lon=8.633100&z=12&m=w)
Online editable map service. Updated and maintained by contributors all over the world. It uses __local knowledge__, making it particularly useful in remote areas.
- __Google Maps:__ [https://www.google.com/maps/d/](https://www.google.com/maps/d/)
Limited, but it allows to upload layers, create and export features, __share simple maps__.

### Geo Mobile Apps Overview (General Understanding)

- __Qfield__: [https://docs.qfield.org/](https://docs.qfield.org/)
Through QFieldCloud, you can __open your QGIS projects__ on Qfield on your mobile device. Any edit made on the map in the app can then be synced and displayed in QGIS.
- __OsmAnd__: [https://osmand.net/](https://osmand.net/)
Using OSM basemap, it’s a good app for __offline navigation__. You can upload kml-files to display on the map, as well as recording your trips and then export them to kml.
- __GeoODK__: [http://geoodk.com/index.html](http://geoodk.com/index.html)
Combines __ODK with a geo app__. You can collect data through ODK surveys and display them on a map, in addition to easily create polygons and add information to them.

<tagName>  <tagName>





