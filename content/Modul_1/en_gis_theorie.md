# What is GIS? (Theory)

## General Information: 

- A Geographic Information System (GIS) is a __digital system that connects data to maps__.

- Geoinformatics in general focus on the __visualisation, organisation and processing of spatial data__. 

- Spatial analyses furthermore allow __to reveal circumstances and connections between spatial data features__: 

  - by making use of their spatial location, __information layers__ (or features within a layer) can be analyzed in regard to each other to obtain new information. 

## Why are Spatial Analyses important?

```{Note} 
Discuss in groups:
```

 - Situations in which you benefitted from spatial analyses.
 - Situations in which you could may be have benefitted from spatial analyses.
 - Main areas where you see potential for spatial analyses in your work.

## Introduction to GIS: 

### We use GIS for:

 - Creating interactive queries __(Querying)__
 - Analysing spatial information __(Spatial analysis)__
 - Editing and visualizing data in maps __(Editing)__
 - Present the results of all these operations __(Map making)__

### GIS in Humanitarian Responses

GIS has many applications in the __humanitarian field__:

 - Refugee/IDP camp planning
 - Mapping remote areas to facilitate access
 - Keep track of field operations
 - Support security decisions
 - Support operations planning
 - Identify areas most affected by disasters
  
```{Tip}
A few examples:
```

 - [REACH Initiative](https://www.reachresourcecentre.info/search/)  
 - [World Food Programme(WFP)](https://hungermap.wfp.org/) 
 - [Médecins Sans Frontières (MSF)](https://geo.msf.org/catalogue) 
 - [iMMAP](https://immap.org/products/) 
 - [MapAction](https://maps.mapaction.org/)


## A Galaxy of Tools
GIS comes with a __galaxy of tools__ that are constantly evolving. An increasing number of traditional tools are now capable of supporting geographic information (Excel, Power BI, Adobe Illustrator…)

### An Overview: 

- __Mobile Data Collection Tools__

The latter make it possible to collect data via mobile or tablet, and often to visualize and exchange it with other platforms according to a common format.

-  __Mapping Tools__

These tools provide a simple vizualisation of geographic data, and allow for the production of maps.

- __GIS Tools__

As opposed to the previous ones, these more advanced tools are very comprehensive and allow for advanced analyses to be carried out on the geographical components of data.

-  __Webmapping Tools__

These tools make it possible to manipulate and create maps online in a very simple way directly in a web browser.


## Paper Maps and Cartography 

### What is Spatial Analysis?

- Spatial analysis __studies entities and events__ using their topological, geometric, or geographic properties. 
- It includes a __variety of techniques__ to analyse geographic data. 
- Data can be __added to a map as layers and they can interact with each other__. 
- GIS enables you to work with these __layers__ to explore critically important questions and __find answers__ to those questions.

#### An Example from the Past: John Snows' Cholera Map

In 1854 an __outbreak of cholera__ occurred in London, England. The most common theory was that the disease was spread through the air. Dr.John Snow believed that the danger was __in the water__. He made a map to analyse the __number of deaths__ in Soho per house block. He added the __location of water pumps__ on the map.
He found a __correlation__ between one specific water pump and the number of infections.

__Dr. Snow's map of the Cholera outbreak of 1854__, and the reports that it accompanied, __won over the predominant "Miasma Theory"__ that the disease __was spread through the air__. Residents were now warned to __boil their water__, and so ended the last Cholera outbreak London has seen.

![John Snows' Map](/fig/en_John_Snows_Map.png) John Snows' Map

__Using GIS__, several measures of spatial central tendency have been applied to the dataset, revealing that the Spatial Mean (the geographic center of the distribution of deaths) of the outbreak lies __within 35 meters of the Broad Street Pump__, identified as the __source of contamination__ in the 1854 outbreak. 


```{Tip}
Further information:
```
 - [Let’s explore John Snow’s map](https://www.arcgis.com/apps/PublicInformation/index.html?appid=d7deb67f810d46dfacb80ff80ac224e9)

## GIS vs Cartography

- __Cartography__ is the study and practice of __making maps__.
- A GIS is a __modern extension__ of traditional cartography. 
- Both contain examples of a __base map__ to which additional data can be added. 
- The differences are that there is no limit to the __amount of additional data__ that can be added to a GIS map. 
- Cartographic maps are often extremely simplified as there are limits to the amount of data that can be physically and meaningfully stored on a small map. 
- GIS uses __analysis and statistics__ to present data in support of particular arguments which a cartographic map cannot do. 
- You can use GIS __for__ cartography.

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
- At a basic level, you can perform limited geospatial tasks with apps such as Google Earth or Google Maps.
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
- __OsmAnd__: [https://osmand.net/](https://osmand.net/).
Using OSM basemap, it’s a good app for __offline navigation__. You can upload kml-files to display on the map, as well as recording your trips and then export them to kml.
- __GeoODK__: [http://geoodk.com/index.html](http://geoodk.com/index.html)
Combines __ODK with a geo app__. You can collect data through ODK surveys and display them on a map, in addition to easily create polygons and add information to them.

<tagName>  <tagName>


### Non-Spatial Analyses in QGIS 


#### Geoprocessing Tools - Overview and Selection

![Geoprocessing icons](/fig/en_geoprocessing_icons.png)

![Geoprocessing tools](/fig/en_geoprocessing_tools.png)

```{Tip}
Example for a clip:
```
Creates a __selection__ based on the spatial relationship between each feature in the input layer and the features in an additional layer.

Step by step:
- __Input Layer__: Layer from which the selection is clipped 
- __Overlay Layer__: Area of interest that the input layer will be clipped to 

 <tagName>  <tagName>

![Clip](/fig/en_clip.png)

```{Tip}
Example for a buffer:
```
- __Computes (a) buffer area(s)__ for all the features in an input layer, using a specified distance

Step by step:
- __Input Layer__: Layer around which features the buffer(s) are to be created
- __Distance__: Choose a value and unit (make sure that your input data is projected)
- __Segments__: Add value
- Mark __„Dissolve result“__ to automatically dissolve the buffer outputs 
- If individual buffers are needed, leave __blank__

 <tagName>  <tagName>

![Buffer](/fig/en_buffer.png)

```{Tip}
Examples for buffer usage: 
```
Philippines: Taal Volcano, Base surge hazard map
[https://www.phivolcs.dost.gov.ph/vault/1BaseSurge_Layout-Jan2020_A0_v5.jpg](https://www.phivolcs.dost.gov.ph/vault/1BaseSurge_Layout-Jan2020_A0_v5.jpg)

![Taal Volcano](/fig/en_Taal_Volcano.png)

Nepal: Earthquake, april 2015
[https://reliefweb.int/sites/reliefweb.int/files/resources/reach_npl_map_earthquakeaffected_27apr2015_a3.pdf](https://reliefweb.int/sites/reliefweb.int/files/resources/reach_npl_map_earthquakeaffected_27apr2015_a3.pdf)

![Nepal Earthquake](/fig/en_Nepal_earthquake.png)

Fukushima: may 2011, Integrated doce results<br>
[https://www.emsics.com/five-years-fukushima-incident-management-considerations/](https://www.emsics.com/five-years-fukushima-incident-management-considerations/)

![Aerial measuring results](/fig/en_Aerial_measuring_results.jpg)

#### Buffer: with and without “Dissolve”

With dissolve results:

![With dissolve results](/fig/en_dissolve_results.png)

Without dissolve results:

![Without dissolve results](/fig/en_without_dissolve_results.png) 

#### Non-Spatial Joins in QGIS

- Choose __“Join Attributes by Field Value”__ Tool (use search tool):

- __Adds attributes__ of a non-spatial table to the layer

- Enables join using a __field/column__ that is present in both data sets

Step by step:
- Input layer: __Vector layer__ 
- Table field: Field/ column that exists in __both data sets__ (name of column in vector layer)
- Input layer 2: __Text/csv/xls data__ 
- Table field 2: Field/ column that exists in __both data sets__ (name of column in text/csv/xls)
- Join type: Select __„Take attributes of the first matching feature only (one-to-one)“__.
- Define __output layer name and destination__ or leave at temporary layer


 <tagName>  <tagName>

![Join attributes by field value](/fig/en_join_attributes_by_field_value.png)

```{Tip} 
Hint
```
If a table join does not work via the “Join Attributes by Field Value” tool, a join can also be performed via the __layer properties__ (right-click, Properties) under the Join tab.

 <tagName>  <tagName>

![Add vector join](/fig/en_add_vector_join.png)

#### Spatial Joins in QGIS

Choose __“Join Attributes by Location”__ Tool:
- Adds __additional attributes__ of the join layer to the input layer based on the spatial relationship
- __Input Layer__: Dataset you want to enrich
- __Join layer__: Dataset with additional information/attributes
(you can specify which fields of the join layer should be added)

 <tagName>  <tagName>

![Spatial joins](/fig/en_spatial_joins.png)


