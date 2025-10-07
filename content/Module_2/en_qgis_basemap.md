::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Basemaps


Base maps in QGIS serve as foundational layers that provide essential geographical context for other spatial data layers. They typically include features like roads, rivers, administrative boundaries, terrain information, and in some cases, satellite imagery. The primary purpose of base maps is to offer a visual reference for spatial analysis, data visualization, and map creation within QGIS projects.

Advantages of using base maps in QGIS, including satellite imagery, include:

* Contextual Reference: Base maps offer a backdrop against which other spatial data layers can be overlaid, providing users with valuable context for their analyses and visualizations.
* Enhanced Visualization: Incorporating satellite imagery as base maps adds an extra layer of detail and realism to maps created in QGIS. Satellite imagery provides high-resolution views of the Earth's surface, enabling users to visualize features such as land cover, vegetation, and urban areas with precision.
* Quick Project Setup: Incorporating pre-existing base maps, including satellite imagery, into QGIS projects allows users to quickly set up new projects without the need to digitise or create base layers from scratch.

Limitations of base maps, including satellite imagery, in QGIS may include:

* Limited Detail: While satellite imagery provides high-resolution views of the Earth's surface, it may not capture certain features or details visible in other types of base maps, such as topographic or thematic maps.
* Data Accuracy: Depending on the source of the satellite imagery, there may be variations in data accuracy, completeness, or currency, which can affect the reliability of analyses or visualizations.
* Dependency on Internet Connectivity: Some satellite imagery base maps, particularly those sourced from online mapping services, require an active internet connection to access and may not be available offline.

Overall, base maps, including satellite imagery, play a crucial role in QGIS projects by providing a foundational layer of geographic context and visual reference. Users should leverage the advantages of satellite imagery while being mindful of its limitations and considering complementary data sources for comprehensive analyses and visualizations.

The following section will provide an overview on how to access and add basemaps to your QGIS-project.

## Standard QGIS Basemaps

You can always add the standard OpenStreetMap as a basemap to your map canvas. 

```{tip}

The [wiki article on basemaps](content/wiki/en_qgis_basemaps_wiki.md), has a tutorial 
on adding more types of basemaps (e.g. from Google Maps) to the standard basemap 
options in QGIS.

```

There are two ways to add OpenStreetMap as a basemap:

1. Find in the `Browser` panel `XYZ Tiles`. Open the dropdown by 
   clicking on the arrow next to it and select OpenStreetMap
2. In the `Layer` menu -> `Add Layer` -> `Add XYZ layer...` -> Select OpenStreetMap 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>

## QuickMapServices

There are lots of plugins available for QGIS that provide additional tools not 
available in a standard installation. The [plugins page](/content/Wiki/en_qgis_plugins_wiki.md) on the wiki provides a more detailed example
information.
One useful plugin is [QuickMapServices](https://nextgis.com/blog/quickmapservices/). 
This plugin lets you access a wide range of basemaps that are not available in 
QGIS by default, such as Bing or Sentinel-2 satellite imagery.

:::{dropdown} Installation of plugins

To [install a plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html), in the top bar, navigate to `Plugins` -> `Manage and Install Plugins…` -> `All` -> 
Search for the plugin -> `Install Plugin`


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

```{Tip}

If you cannot find a specific extension, check that you have not used spaces in the plugin name where they don't belong (e.g., when looking for QuickMapServices, searching “Quick Map” will not return results, but “quickmap” will). You can use an asterisk (`*`) as a
wildcard in searches (so "quick*map" will return results with or without a space between "quick" and "map"). 

```

If you still cannot find an extension, you may need to allow experimental 
extensions in the options (see below).

```{figure} /fig/en_30.30.2_plugin_installation_experimental_checkbox.png
---
name: en_30.30.2_plugin_installation_experimental_checkbox
width 400 px
---
Plugin Manager settings to show experimental plugins
```

:::

To add a basemap from the QuickMapServices plugin:

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

When you are using QuickMapServices, be aware that some of these maps are under copyright laws, that restrict the reproduction of these maps. Be aware of these restrictions by looking up the copyright licenses for the basemaps you are using. In general, satellite imagery is not free to use. This means you can not publish maps with all of the available base maps!

```

## Self-Assessment Questions

::::{admonition} Check your skills

Check whether you know the key concepts from this chapter by answering the questions below.

1. __What is a basemap, and why is it useful in GIS projects?__
2. __How do you add a basemap to QGIS? Describe at least one method (plugin, XYZ tiles, etc.).__
3. __What are attribution requirements, and how should you handle them when using basemaps from third‑party providers?__

::::
