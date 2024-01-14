🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

# Data Sources
To find the appropriate data you are looking for, you can search online data sharing platforms. In the following some important ones are highlighted below. 

<details>
<summary>What to look out for when looking for data:</summary>
<br> 

*Data source:* Always make sure to use data from trusted data sources. The organisation that shared the data is the best indicator. Apart from that, use of the data in trusted contexts or also download counts can be good indicators. 

*Data size:* Sometimes you can access data in different scales, resolutions etc. Make sure to select a data set that fits your purpose and can be easily processed by you. E.g. if you only need data about a specific region, if feasible only select the data of this admin area. 

*Data format:* Maybe there are different data formats available that you can choose from. Think about your needs and what is the most practical for your use and potentially also sharing purposes. 

*Data capture date:* Make sure to check when the data was collected and if the collection data is in line with your needs. Check if there is potentially more up-to-date data in another framework. 

*Data licence:* What kind of licence does the data have? How can you use and share it and how do you need to cite the data source? Make sure to check the licensing and to follow the respective regulations to avoid difficulties.
</details>


## Overview

| Name | Data | Link |
|---------|----------|---------|--------|
| The Humanitarian Data Exchange | Various openly available (geo)data sets from different organisations, including the datasets, meta information and stats/overviews | https://data.humdata.org |
| Test | Test 1 | Test 2 |



## OpenStreetMap data


### OpenStreetMap

If you are using version 3.4 or higher in QGIS, it is by default possible to add the OSM base map to your project. Unfold the XYZ tiles, right-click on OpenStreetMap and select add layer to project.

```{figure} /fig/en_add_osm_basemap.png
---
height: 500px
name: add_osm_basemap
---
Screenshot of how to add OSM basemap
```

### overpass turbo

[Overpass turbo](https://overpass-turbo.eu) is a web based data mining tool for OSM. By running a query, you can download the data and import it into your project. You can either run it by writing your query on the left or by using the wizard which will assist you in writing your queries. 
***Example***  
To search for schools in your bounding box or search area you can either write the query yourself or get it build by the wizard.  
**1. Check Tagging Guidelines**  
Search for it in the [OSM wiki](https://wiki.openstreetmap.org/wiki/Tags) and/or [taginfo](https://taginfo.openstreetmap.org). In our example it is: *amenity=school*  
**2.  Write or build the query**  
Either use the wizard by tiping in *amenity=school in Heidelberg* or write your own query (f. e. for your bounding box):  
**Wizard:**
```{figure} /fig/en_wizard_overpassturbo.png
---
height: 250px
name: overpass_turbo_wizard
---
Screenshot of the Wizard in overpass turbo
```
```{figure} /fig/en_wizard_result.png
---
height: 250px
name: overpass_turbo_wizard_result
---
Screenshot of the result
```  
**Query:**
```sql
[out:json];  
(  
  node ["amenity"="school"](49.35,8.553,49.481,8.756);
  way ["amenity"="school"](49.35,8.553,49.481,8.756);
  relation ["amenity"="school"](49.35,8.553,49.481,8.756);
);
out; 
```
**Bounding Box**  
To query with a bounding box you need a special format. Specify it like so:
 + s (southern limit in decimal degrees, lowest latitude)
 + w (western limit in decimal degrees, lowest longitude)
 + n (northern limit in decimal degrees, highest latitude)
 + e (eastern limit in decimal degrees, highest longitude)
     + for example:  
```sql
node ["key"="value"] (s, w, n, e);
         out;
```

```{tip} 
For more information on the query language check out the [Language Guide](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide).
```
**3. Download the data**  
One can export the results in various ways.

::::{tab-set}

:::{tab-item} Data
By exporting the data as f.e. GeoJSON you can later on import them in your QGIS project.
```{figure} /fig/en_overpass_turbo_data.png
---
height: 250px
name: overpass_turbo_data
---
Screenshot of how to export data in overpassturbo
```

:::

:::{tab-item} Map
By exporting the query as map, you can share your current view as link or image.

```{figure} /fig/en_overpass_turbo_map.png
---
height: 150px
name: overpass_turbo_map
---
Screenshot of how to export map in overpassturbo
```
:::

:::{tab-item} Query
By exporting your query you can get the text or convert it to an OverpassXML or OverpassQL formated query.

```{figure} /fig/en_overpass_turbo_query.png
---
height: 250px
name: overpass_turbo_query
---
Screenshot of how to export query in overpassturbo
```
:::

::::

```{tip} 
For more information, check out the [wiki](https://wiki.openstreetmap.org/wiki/Overpass_turbo).
```


### Geofabrik

[This platform](http://download.geofabrik.de) contains data extracts from OpenStreetMap. You can select the continent, country and region of interest to download the data you need.


### OSM Boundaries

### HOT export tool


### ohsome tools

## Humanitarian data

### The Humanitarian Data Exchange

[The Humanitarian Data Exchange](https://data.humdata.org) is a platform that has various openly available (geo)data sets from different organisations, including the datasets, meta information and stats/overviews. It is the go-to datasource for humanitarian data. You can navigate the page by searching for your location or the data needed. 


## General Geodata
Free GIS data
Geoboundaries


## Data on disaster

GDACS

## Population

## Building

## Different sectors


## Remote Sensing / Earth Observation data

