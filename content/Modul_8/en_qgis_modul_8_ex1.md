# Remote Sensing and Raster data 🛰️ Exercise

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧


# Geodata Classification Exercise 1: Basic Overview Map of Flood Risk in the Indus Basin in Pakistan

### Aim of the exercise
The aim of this exercise is to gain a basic understanding of working with raster data and its visualisation and advantages. To achieve this, several datasets such as a digital elevation model, population data and mapped flood extents are processed to create a simple flood risk map for the Indus River basin in Pakistan.

### Relevant Wiki Articles

* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Types of Geodata](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html)
* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Attribute table](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.html)
* [Table function - Add field](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#add-field)
* [Raster basics](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.md)


### Data
Download all datasets **DATA LINK** and save the folder on your computer. Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. Under "data > input" you find the following files:

**Vectordata**
- `Pakistan_indusbasin_streams.shp` (Lube Geometry)
- `Pakistan_borders.gpkg` (GeoPackage)
    - Pakistan_national_borders (Lines)
    - Pakistan_admin2 (Polygons)
- `Pakistan_floodextents_2023.shp`

**Rasterdata**
- `Pakistan_DEM_1km.tif` (Raster)
- `Pakistan_pop_dens_1km.tif` (Raster)
- `Pakistan_precips_1km.tif` (Raster)


### Tasks 1
Our first goal is to get a proper overview over the datasets and get familiar with the different visualisation options for raster data and how to ideally use them.

1. Open QGIS and create a [new project](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) by clicking on `Project` -> `New`

2. Once the project is created save the project in the “project” folder of the “Ex_Pakistan_floodrisk”. To do that click on `Project` -> `Save as` and navigate to the folder. Name the project “Pakistan_floodrisk”.

3. Import the GeoPackages `Pakistan_borders.gpkg` and the rasters `Pakistan_DEM_1km.tif`, `Pakistan_pop_dens_1km.tif` and `Pakistan_precips_1km.tif` into your project via drag and drop ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). 
Or by clicking `Layer`-> `Add Layer`-> `Add Vector Layer`/ `Add Raster Layer`

```{Attention}
If a raster is displayed mostly or completely black upon loading it into QGIS, most of the time the reason is not an error or corrupted data but just the initial visualisation style
```

4. First have a look at the DEM layer (`Pakistan DEM`). The rastercells of the DEM display the elevation above sea level, where are high and low lying areas located in Pakistan occording to the expandable layer legend on the left? Use the ![](/fig/mod8_ex1_informationtool.png) to click on a couple of rastercells to obtain their values, that are the displayed in a panel on the right. 
 - What do you think is the highest and lowest elevation approximately?

 ```{figure} /fig/mod8_ex1_informationpanel.png
---
width: 400px
name: 
align: center
---
```


5. to get some basic information about your raster right click on the layer and select  `Properties`. Unter the tab "Information" various different attributes of the raster like its Coordinate Reference Systeme (CRS), spazial resolution or basic statistical paramters are listed. 
    - What is the cellsize of the DEM?
    - What are the minimum and the maximum values?
    - Whats the used CRS?

6. Now we want to explore the different ways of visualizing a raster and find the optimal visualization for our DEM. Open the layer styling panel by riht clicking on the top toolbar and ticking the box "Layer Styling Panel". The panel very similar to the one dislayed when visualizing Vectordata.
    1. Open the visualzation mode dropdown menu. There are six visulisation modes you can choose from. Try each of them and take a guess which one would be suitable. You can find mor information about the visualization modes **here**

 ```{figure} /fig/mod8_ex1_visualisationmodes.png
---
width: 400px
name: 
align: center
---
```

    2. Choose "Singleband Pseudocolour" and selct a colour palette you like just like with vector visualization. Under the classification window you can choose from three classification modes (Continous, Equal interval, Quantile) (**Wiki article**) for the visual classification of the raster. Which one seems to suit the diplay of elevation the best?

    3. Finally you can choose between the interpolation methods "Linear" (smooth display) and "Discrete" (display in distinct classes). Choose one of them. If you choose "Discrete" you can alter the number of Classes with the "Classes" dropdown menu.

 ```{figure} /fig/mod8_ex1_symbologypanel.png
---
width: 400px
name: 
align: center
---
```

    4. your DEM could look something like this now (colour palette "Spectral" and interpolation "Linear")

 ```{figure} /fig/mod8_ex1_deml.png
---
width: 400px
name: 
align: center
---
```

  7. Now we want to have a look at a different raster: Make the "Pakistan_pop_density_1km" layer visible. This raster stores values of population density per km in 1km x 1km cells, so effectively the approximate population count per area. The initial visualisation seems not to display the information of the different population desities very well as it is mostly black. We will fix this with the following steps:
    1. Have a look of the value range of the raster in the raster properties and check some values in different areas with the ![](/fig/mod8_ex1_informationtool.png) tool. 
    2. The raster covers a very large value range from around 0,2 - 31300. This is the case because of the disparity in population between very remote areas and extremely densly populated megacities both being present in pakistan. To have a closer look at the value distribution among the cells of the raster generate a **histogramm link** in the layer styling panel by selcting the ![](/fig/mod8_ex1_histogrammicon.png) icon on the left and click on "compute histogramm". Have a closer Look at the histogramm by zoomin in to the range of "Pixel Value" = 5000 and "Frequency" = 2000. A few things are visible:
      - The Raster values are extremely tailed with very few cells higher than 2000 but extent into ay higher ranges.
      - There are extremely many values in the very low value range
      - The vast majority of the values seem to be between around 0 to 3000.

    3. Based on the exploration of the histogramm try a few value boundaries for visualisation at the top of your layer styling panel (under Symbology). Keep in mind that we look at population data and that population distribution very spatially heterogenic most of the time. Try the following combination and choose the one that suits the data best:
      - Min = 0    Max = 1000
      - Min = 0    Max = 3000
      - Min = 0    Max = 5000

    4. Have a look at the Histogramm of the DEM and adjust the visalization range for the DEM too if you deem it necessary.

    8. A common and easy method to enhance the visuals of a map you generate with QGIS is the addition of a trasparent "Hillshade" layer. You can generate it with the "Hillshade" tool that you can find in your toolbox panel or via "raster" > "Analyse" > "Hillshade". 

**HILLSHADE BILD**


```{Nice to know}
One advantage of rasterdata over vectordata is that that they are better suited for deriving further data sets such as a hillshade raster. There are a multitude of tools in QGIS for the derivation of topographical paramters such as slope or aspect, hydrological paramters such as stream networks or flow accumulaton and varius different indices.
```
