# Basemaps

Basemaps are background maps. They are often very practical since they are easy to use, allow easy orientation on the map canvas and are diverse.

```{Note}
No interaction with the basemaps is possible. They are only “pictures” in the background!
```

## Standard QGIS Basemaps

You can always add the standard OpenStreetMap as a basemap to your map canvas. 

There are two ways to add the OpenStreetMap as a basemap.

1. Find in the `Browser` panel `XYZ Tiles`. Open the dropdown by clicking on it and select OpenStreetMap or another basemap.
2. `Layer` -> `Add Layer` -> `Add XYZ layer...` -> Select the OpenStreetMap or another basemap.

__Add standard OpenStreetMap as Basemap__
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>

### Add Google and Bing Basemaps

To add additional basemaps without using plugins you have to configure `XYZ Tiles`. 
In the `Browser Panel`, right-click on `XYZ Tiles` -> `New Connection`.

`Name` = The name of the new basemap.

`URL` = You can use any of the URLs in the table below.

Name| Info | URL |
| ----- | --- | --- |
|[OpenTopoMap](https://wiki.openstreetmap.org/wiki/OpenTopoMap)|Opensource topographic map based on OSM and SRTM|https://tile.opentopomap.org/{z}/{x}/{y}.png|
|Google Terrain||https://mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}|
|Google Hybrid||https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}|
|Google Satellite||https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}|
|Google Road||https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}|
|Google Roads only||https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}|
|Google alternative Road map||https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}|
|Bing Aerial||http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1|

Advantages of using basemaps from XYZ Tiles are:
* Load faster
* Support reprojection
* Support printing
*  Supported by online applications like [QField]( https://qfield.org/)

## Basemaps from [QuickMapServices](https://nextgis.com/blog/quickmapservices/) Plugin

The QuickMapServices Plugin allows to access a wide range of basemaps. 

```{Note}
There can be problems when printing some basemaps from the QuickMapServices!
```
`Web` -> `QuickMapServices` -> select provider e.g. NASA -> select basemap

__Functionality of QuickMapServices Plugin__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>

### Configuration of QuickMapServices
After installing the plugin (Plugin Wiki) you need to configure the plugin to access all basemaps.

`Web` -> `QuickMapServices` -> `Settings` -> Use the horizontal arrows to navigate to `More Services` -> `Get Contributed Pack`

## Navigation on Basemap with OSM Place Search Plugin

With the OSM Place Search Plugin, you can find places all around the world based on OpenStreetMap. This means the place search is independent from whatever basemap you are using, it is always based on OpenStreetMap.

```{Tip}
If the plugin is installed and activated but the panel is not visible check Wiki [Move and arrange toolbars and panels](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#show-and-hide-displays-and-toolbars)
```

__Functionality of OSM Place Search Plugin__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/OSM_Place_Search.mp4"></video>