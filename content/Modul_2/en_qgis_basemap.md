# Basemaps

<!-- CLARIFY: This section could be rewritten more clearly; 
EN: Added a bit more context. Is this enough? -->
Basemaps are background maps that help you visualise the geographic area you are working on. They are very practical since they are easy to use, allow easy orientation on the map canvas. QGIS offers 
OpenStreetMap and some other base maps by default, such as OpenStreetMap or MapZen Global Terrain.

However, there is a wide range of base maps that can be used via extra plugins 
or XYZ Tiles.

The following section will provide an overview on how to access and add basemaps to your QGIS-project.

## Standard QGIS Basemaps

You can always add the standard OpenStreetMap as a basemap to your map canvas. 

```{tip}
The [wiki article on basemaps](../Wiki/en_qgis_basemaps_wiki.md), has a tutorial 
on adding more types of basemaps (e.g. from Google Maps) to the standard basemap 
options in QGIS.
```
There are two ways to add OpenStreetMap as a basemap.

1. Find in the `Browser` panel `XYZ Tiles`. Open the dropdown by 
   clicking on the arrow next to it and select OpenStreetMap

2. In the `Layer` menu -> `Add Layer` -> `Add XYZ layer...` -> Select OpenStreetMap 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>


## QuickMapServices

There are lots of plugins available for QGIS that provide additional tools not 
available in a standard installation. The [plugins page](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html) on the wiki provides a more detailed example
information.
One useful plugin is [QuickMapServices](https://nextgis.com/blog/quickmapservices/). 
This plugin lets you access a wide range of basemaps that are not available in 
QGIS by default, such as Bing or Sentinel-2 satellite imagery.

:::{dropdown} Installation of plugins
To install a plugin `Plugins` -> `Manage and Install Plugins…` -> `All` -> 
Search for the plugin -> `Install Plugin`

<!-- FIXME: Plugin installation should be its own section, not nested under 
   QuickMapServices 
 -->

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

```{Tip}
If you cannot find a specific extension, check you have not used spaces where the 
plugin name doesn't (e.g. When looking for QuickMapServices, searching "Quick Map" 
will not return results but "quickmap" will). You can use an asterisk (`*`) as a
wildcard in searches (so "quick*map" will return results with or without a space
between "quick" and "map"). 
```

If you still cannot find an extension, you may need to allow experimental 
extensions in the options (see below).

```{figure} /fig/en_30.30.2_plugin_installation_experimental_checkbox.png
---
name: plugin manager allow experimental plugins
width 400 px
---
Plugin Manager settings to show experimental plugins
```

:::

To add a Basemap from the QuickMapServices Plugin:

1. In the main menu in the top bar of your screen, navigate to `Web` > `QuickMapServices` 
2. Click on `Search QMS`. A new panel will open, most likely at the bottom right.
3. Here, you can search for a basemap of your choice. For example, Bing Aerial, different versions of OpenStreetMap, Sentinel-2 satellite imagery. 

```{Tip}
A list of basemaps and useful search queries for the QMS-plugin can be found on [this website](https://qms.nextgis.com). This link can also be found in the "About" section of the QMS-plugin
```

:::{dropdown} Video: Functionality of the QuickMapServices Plugin__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>
:::

```{Note}
When you are using QuickMapServices, be aware that some of these maps are under copyright laws, that restrict the reproduction of these maps. Be aware of these restrictions by looking up the copyright licences for the basemaps you are using. In general, satellite imagery is not free to use. 
```


<!-- CLARIFY: What are the problems? Are there any fixes for them? DONE
EN: Is my understanding correct? -->