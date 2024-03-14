🚧 This training platform and the entire content is under ⚠️construction⚠️ and 
may not be shared or published! 🚧

# Data sources
To find the appropriate data you are looking for, you can search online data 
sharing platforms. Some important ones are highlighted below. 

<details>
<summary>What to look out for when looking for data:</summary>
<br> 

*Data source:* Always make sure to use data from trusted data sources. The 
organisation that shared the data is the best indicator. Apart from that, use of 
the data in trusted contexts or also download counts can be good indicators. 

*Data size:* Sometimes you can access data in different scales, resolutions etc. 
Make sure to select a data set that fits your purpose and can be easily processed 
by you. E.g. if you only need data about a specific region, if feasible only 
select the data of this admin area. 

*Data format:* Maybe there are different data formats available that you can 
choose from. Think about your needs and what is the most practical for your use 
and potentially also sharing purposes. 

*Data capture date:* Make sure to check when the data was collected and if the 
collection data is in line with your needs. Check if there is potentially more 
up-to-date data available from another source. 

*Data licence:* What kind of licence does the data have? How can you use and 
share it and how do you need to cite the data source? Make sure to check the 
licensing and to follow the respective regulations to avoid difficulties.
</details>
<!-- ADD: Would be nice to have a wiki page on licensing if possible -->


## Overview

### General geodata 

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| Natural Earth | Administrative and physical geography | https://www.naturalearthdata.com/ |
| Geonames | Administrative geodata | https://www.geonames.org/ |
| OpenAfrica | Open-source data on Africa | https://africaopendata.org/dataset |
| DivaGIS | Different data, e.g. administrative, roads, population, elevation, climate | http://www.diva-gis.org/gdata |
| Open Topography | Data on topography | https://opentopography.org/ |
| OSM Boundaries | Administrative boundaries (need to authenticate via your osm account) | https://osm-boundaries.com |

### Humanitarian data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| Humanitarian Data Exchange | Various open data from different humanitarian organisations | https://data.humdata.org |
| Healthsites | Locations of health facilities | https://healthsites.io/ |
| UNHCR Geoservices | Data on displaced populations | https://data.unhcr.org/en/situations |


### Disaster data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| MapAction | Emergency mapping resources | https://maps.mapaction.org/ | 
| Fieldmaps.io | Data and map download platform for humanitarian use | https://fieldmaps.io/ | 
<!-- CHECK: link doesn't work? -->
| Acled | Conflict data | https://acleddata.com/data-export-tool |
| GDACS | Disaster database | https://www.gdacs.org |
| ZKI/DLR | Flood extents, damage extents, earth observation data | https://activations.zki.dlr.de/en/activations/ |
| Waterpoint | Data on waterpoints | https://www.waterpointdata.org | 
<!-- is water points more appropriate under humanitarian / general? it's not disaster data -->
| WFP Vulnerability Analysis and Mapping | Data on food security, hazards, conflicts, climate | https://dataviz.vam.wfp.org/ |


### Population data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| WorldPop | Population estimates | https://wopr.worldpop.org/ |
| GHSL | Global settlement data | https://ghsl.jrc.ec.europa.eu/ |
| HRSL | Settlement layer based on earth observation and Facebook data | https://research.facebook.com/downloads/high-resolution-settlement-layer-hrsl/ |
| GRID3 Settlement extents and settlement points | Settlement extents data | https://grid3.org/ |
| Pangea | Environmental & biosciences data | https://www.pangaea.de/ |
| United Nations Population Fund | Data on sexual and reproductive health and population trends | https://www.unfpa.org/data

### Buildings data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| World Settlement Footprint | World Settlement Footprint | https://download.geoservice.dlr.de/WSF2019/ |
| VIDA building footprint | Combined Google and Microsoft building footprint datasets | https://beta.source.coop/repositories/vida/google-microsoft-open-buildings/download/ |
| Open-building | Google building footprints | https://sites.research.google/open-buildings/#download |

### Remote sensing/earth observation data

| Name | Data | Link |
| :-------------------- | :----------------- | :---------- |
| Global Forest Watch | Data on global forests | https://www.globalforestwatch.org/ |
| OpenAerialMap | Crowdsourced drone imagery | https://map.openaerialmap.org/ |
| USGS Earth Explorer | Satellite data from multiple sources, including Landsat and Sentinel | https://earthexplorer.usgs.gov/ |
| NASA Shuttle Radar Topography Mission (SRTM) | Global elevation data | http://srtm.csi.cgiar.org/srtmdata/ |
| Earth Observe | digital elevation model on a global scale | http://srtm.csi.cgiar.org/srtmdata/ | 
<!-- FIXME: wrong link for Earth Observe -->
| Copernicus | Earth observation data | https://scihub.copernicus.eu/ | 
| GlobCover | Raster data on land cover | http://due.esrin.esa.int/page_globcover.php |


## OpenStreetMap data
<!-- ADD: context/info about what OSM data is and why it's useful -->

### OpenStreetMap

If you are using version 3.4 or higher in QGIS, it is by default possible to add 
<!-- COMMENT: we have asked people to install 3.28 -->
the OSM base map to your project. Expand the XYZ tiles entry in the data sources 
browser panel, right-click on OpenStreetMap and select `Add Layer to Project`.

```{figure} /fig/en_add_osm_basemap.png
---
height: 500px
name:
align: center
name: add_osm_basemap
---
Screenshot of how to add OSM basemap
```
<!-- FIXME: This screenshot could be cropped -->

### QuickOSM plugin

The QuickOSM plugin makes it easy to download data from OpenStreetMap and add it 
to your QGIS project. To install it, open the plugin manager from the `Plugins` 
menu by choosing `Manage and Install Plugins`. 

:::{dropdown} How to install QuickOSM
<!-- FIXME: These instructions and screenshots could be clearer -->


```{figure} /fig/managa_install_plugins.png
---
width: 400px
name: 
align: center
name: Manage and Install Plugins
---
Manage and Install Plugins.
```

```{figure} /fig/install_quickosm.png
---
width: 800px
name: 
align: center
name: Installing QuickOSM
---
Installing QuickOSM.
```
:::

To launch the newly installed plugin, click on ![](fig/quickosmplugin.png) or 
click under `vector` -> `QuickOSM`. 

Follow the steps to fetch for data:

1. Select a Key and Value from the dropdown list. If you are unsure, check here: 
   [taginfo](https://taginfo.openstreetmap.org). 

<!-- CLARIFY: this needs more explanation for beginners -->

```{figure} /fig/key_value_quickosm.png
---
width: 800px
name: 
align: center
name: Choosing key and value
---
Choosing key and value in QuickOSM.
```

2. Limit the area by typing in the name of your area of interest. You can also 
   choose from the dropdown `Canvas Extent` or `Layer Extent` instead of a name 
   of a city or country.

3. Unfold the tab `Advanced`. Only select the datatypes you are expecting to 
   minimize errors.
   <!-- CLARIFY: would be useful to have an example here --> 

```{figure} /fig/quickosm_usage.png
---
width: 800px
name: 
align: center
name: Running the QuickOSM plugin.
---
Running the QuickOSM plugin.
```

4. Click on `Run query`.

:::{dropdown} How to fetch data for multiple queries

If you want to get more data in the same area, you can add a query by clicking 
on the ![](fig/plus_quickosm.png). Be careful choosing the right logical operator 
`And` or `Or`. If you are unsure check the page [non-spatial queries](/content/Wiki/en_qgis_non_spatial_queries_wiki) 
on the wiki. There is an example of this in the Module 2 [OSM exercise](https://giscience.github.io/gis-training-resource-center/content/Modul_2/en_qgis_data_sources_ex2.html#task-quickosm)

:::

### HOT Export Tool

With the [Humanitarian OpenStreetMap Team (HOT) Export Tool](https://export.hotosm.org/v3/) 
you can download customized extracts of up-to-date OSM data in different file 
formats. It offers a browser-based tool to download OSM data with good options 
to specify region, time, feature type and data format.

1. Go to the HOT Export tool. To use the tool you need a OSM account. 

   If you have an OSM account you can log in directly into the HOT Export tool by 
   clicking on `Log in`.
   
   If you don’t have one, you'll need to create one: click on `Log in` and in the 
   new window select the option to create a new account.
2. After logging in, click the `Start Exporting` button on the homepage to load 
   the Export Tool 

```{figure} /fig/hot_export.png
---
height: 400px
name:
align: center
name: HOT Export Tool
---
The HOT Export Tool.
```

4. First add a name and a brief description of your export. Then click on `Next`.
5. Choose the file format fitting to your needs. Most likely Geojson, Shapefile or 
   GeoPackage will be fit for the use with QGIS. Click on `Next`.
   <!-- COMMENT: As earlier, suggest we recommend GPKG for consistency -->
6. The easiest way to choose the feature type you want to download is using the 
   tag tree. (The YAML option is more flexible but more advanced, so we will 
   focus on the first option.)
7. There are multiple ways to select your area of interest. 
   1. You can search for it in the search bar in the top right corner. 
   2. Zoom in the map to your area and click on `This view`.
   3. Zoom in and draw a bounding box by clicking on `Box`.
   4. Zoom in and draw free hand a polygon by clicking on `Draw`.
   5. Or you can upload a layer as extent (only .geojson in the crs WGS84!). 
      Click on `Import`.
8. Then click on `Next`. It will look something like this:

```{figure} /fig/hot_export_example.png
---
height: 400px
name:
align: center
name: HOT Export Tool Example
---
An Example for the HOT Export Tool.
```

9. Click on `Create Export`. It will then run for a few minutes, looking like 
   this:

```{figure} /fig/hot_export_running.png
---
height: 400px
name:
align: center
name: HOT Export Tool running
---
The HOT Export Tool is running.
```
10. After being finished, the status will change to `COMPLETED` and you can 
    download your file by clicking on the link:

```{figure} /fig/hot_export_done.png
---
height: 400px
name:
align: center
name: HOT Export Tool done
---
Downloading data from HOT Export Tool.
```

### Overpass Turbo

[Overpass Turbo](https://overpass-turbo.eu) is a web-based data export tool for 
OSM. By running a query, you can download the data and import it into your project. 
You can either run it by writing your query on the left or by using the wizard 
which will assist you in writing your queries. 
***Example***  
To search for schools in your bounding box or search area you can either write 
the query yourself or get it build by the wizard.  
**1. Check Tagging Guidelines**  
Search for it in the [OSM wiki](https://wiki.openstreetmap.org/wiki/Tags) and/or 
[taginfo](https://taginfo.openstreetmap.org). In our example it is: *amenity=school*  
**2.  Write or build the query**  
Either use the wizard by tiping in *amenity=school in Heidelberg* or write your 
own query (f. e. for your bounding box):  
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
By exporting the data as f.e. GeoJSON you can later on import them in your QGIS 
project.

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
By exporting your query you can get the text or convert it to an OverpassXML or 
OverpassQL formated query.

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

### Ohsome tools

[The Ohsome tools](https://heigit.org/big-spatial-data-analytics-en/ohsome/) 
provide OpenStreetMap data analytics and downloads by HeiGIT. You can also 
investigate the OSM history. 
<!-- CLARIFY: how should this be used? -->