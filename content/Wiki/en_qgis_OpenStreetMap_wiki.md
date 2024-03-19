# OpenStreetMap (OSM) Data

## Overpass Turbo

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
