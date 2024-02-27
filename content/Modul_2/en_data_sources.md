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

### General Geodata 

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| Natural Earth | administrative and physical maps | https://www.naturalearthdata.com/ |
| Geonames | administrative geodata | https://www.geonames.org/ |
| OpenAfrica | Open source data on Africa | https://africaopendata.org/dataset |
| DivaGIS | different data, e.g. administrative, roads, population, elevation, climate | http://www.diva-gis.org/gdata |
| Open Topography | data on topography | https://opentopography.org/ |
| OSM Boundaries | administrative boundaries (need to authenticate via your osm account) | https://osm-boundaries.com |

### Humanitarian Data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| The Humanitarian Data Exchange | Various openly available (geo)data sets from different organisations, including the datasets, meta information and stats/overviews | https://data.humdata.org |
| Healthsites | Location of health facilities | https://healthsites.io/ |
| UNHCR Geoservices | information and data on refugee-related emergencies for humanitarian help regarding displaced persons | https://data.unhcr.org/en/situations |


### Data on disaster

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| MapAction | Emergency mapping resources | https://maps.mapaction.org/ |
| Fieldmaps.io | Data and Map download platform for humanitarian use | https://fieldmaps.io/ |
| Acled | data on armed conflicts and other events | https://acleddata.com/data-export-tool |
| GDACS | data on all major ongoing disasters | https://www.gdacs.org |
| ZKI/DLR | Flood extends, damage extends, earth observation data | https://activations.zki.dlr.de/en/activations/ |
| Waterpoint | data on waterpoints | https://www.waterpointdata.org |
| DataViz | data on food security, hazards, conflicts, climate | https://dataviz.vam.wfp.org/version2/ |


### Population data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| WorldPop | population estimates | https://wopr.worldpop.org/ |
| GHSL | settlement data on global scale | https://ghsl.jrc.ec.europa.eu/ |
| HRSL | Settlement layer based on earth observation data and Facebook data | https://research.facebook.com/downloads/high-resolution-settlement-layer-hrsl/ |
| GRID3 Settlement extents and settlement points | Settlement extents data sets based on Digitise Africa building footprints, boundaries, infrastructure, population, risk analysis and social distancing | https://grid3.org/ |
| Pangea | environmental data | https://www.pangaea.de/ |
| United Nations Population Fund | data on sexual and reproductive health and population trends | https://www.unfpa.org/data

### Building

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| World Settlement Footprint | World Settlement Footprint with global cover | https://download.geoservice.dlr.de/WSF2019/ |
| VIDA building footprint | combined Google and Microsoft building footprint | https://beta.source.coop/repositories/vida/google-microsoft-open-buildings/download/ |
| Open-building | Google building footprint | https://sites.research.google/open-buildings/#download |

### Remote sensing/Earth observation data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| Global Forest Watch | data on global forests | https://www.globalforestwatch.org/ |
| OpenAerialMap | Drone images | https://map.openaerialmap.org/ |
| USGS Earth Explorer | data on Landsat, Sentinel, SRTM, Aster, Land Cover | https://earthexplorer.usgs.gov/ |
| SRTM | elevation data | http://srtm.csi.cgiar.org/srtmdata/ |
| Earth Observe | digital elevation model on a global scale | http://srtm.csi.cgiar.org/srtmdata/ |
| Copernicus | earth observation data | https://scihub.copernicus.eu/ | 
| GlobCover | raster data on land cover | http://due.esrin.esa.int/page_globcover.php |
| Copernicus | Earth observation data | https://scihub.copernicus.eu/ |



## OpenStreetMap data


### OpenStreetMap

If you are using version 3.4 or higher in QGIS, it is by default possible to add the OSM base map to your project. Unfold the XYZ tiles, right-click on OpenStreetMap and select add layer to project.

```{figure} /fig/en_add_osm_basemap.png
---
height: 500px
name:
align: center
name: add_osm_basemap
---
Screenshot of how to add OSM basemap
```

### Quick OSM plugin

tba

### HOT Export Tool

tba


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
name:
align: center
name: overpass_turbo_wizard
---
Screenshot of the Wizard in overpass turbo
```
```{figure} /fig/en_wizard_result.png
---
height: 250px
name:
align: center
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
name:
align: center
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
name:
align: center
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
name:
align: center
name: overpass_turbo_query
---
Screenshot of how to export query in overpassturbo
```
:::

::::

```{tip} 
For more information, check out the [wiki](https://wiki.openstreetmap.org/wiki/Overpass_turbo).
```

### ohsome tools

[The ohsome tools](https://heigit.org/big-spatial-data-analytics-en/ohsome/) provide OpenStreetMap data analytics and downloads by HeiGIT. You can also investigate the OSM history. 