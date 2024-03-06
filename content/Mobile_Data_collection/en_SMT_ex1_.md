# Sketch Map Tool Exercise 1 - Workflow Exercise

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

Explore the whole workflow of mapping with the Sketch Map Tool, from first ideas about what you like to map to the possible digital results.


```{figure} /fig/SMT_workflow_Satelite.png
---
height: 50px
name: T
align: center
---
Picutre of the workflow
```

## Characteristics of the exercise 
#### Aim of this exercise:
Get familiar with the Sketch Map Tool and its whole workflow from map creation to the results.

#### Phase of participatory /community mapping 
preparing participatory mapping / facilitating participatory mapping/ analysing participatory mapping
#### Focus group (GIS-Knowlege Level)
planners/ facilitators as well as practitioners how are involved in the preparation of the filed campaign or collecting the data themselves (Beginners-level: no specific knowledge about QGIS /Umap required)
#### Type of trainings exercise:
This exercise can be used in online and presence training and is focused on an hands-on experience with the Sketch Map Tool
#### Estimated time demand for the exercise.
In general: 2:20 h till 2:45h (depending on number of groups)

```
? maybe as a tabel
Introduction: 10 min
Groupe exercise: 1: 35h 
•	15 min group reading and discussion the case
•	10 min for creating the maps 
•	buffer time for printing about 5 min 
•	15 min for marking 
•	10 min for digitalisation
•	20 min to open the files in QGIS or Umap 
•	20 min preparation of a short-presentation

Wrap-up (with presentations): 
- each group about 5 min to present 
- 10 min general discussion
- a bit buffer time for the change of the groups
```
```{Tip}
To shorten the time you can also just focus the hands-on-exploration on specific parts of the workflow. You can for example work with pre-marked maps to focus on the second half of the workflow or just focus on the first parts and show the final parts with prepared examples by sharing your screen. 
```

## Instructions for the trainers
:::{dropdown} Trainers Corner 
### Preparation and material 
- Online access and devices (PC) to be able to use the Sketch Map Tool to create maps online, upload and download them.
- Possibility to print the maps and smart phones to take the photos and a way to upload them to the Sketch Map Tool later. 
- Take a look and make yourself familiar on the provided material for the exercise and the Sketch Map Tool in general. 
- Prepare a board (it can be a white board /flipchart / or digital e.g. mirro-board) where the participants can add their findings.


```
Alternatives 
- If you conduct this training online, make sure your participants 
have a printer or are able to mark the maps digitally. 
- If you like to skip parts of the workflow, make sure you have alternative material (like preprinted, or already marked Sketch maps) prepared.
- If you like to adapt this exercise to your specific use case, create your own case-description. 
```

### Available Material: needs to be linked directly 
•	Introduction Slides about the Sketch Map Tool available
•	X EVCA-case studies as examples available 
•	Alternative files based on OSM- and satellite-based Sketch Maps from 5 regions.
o	Just the created maps for (pre-printing)
o	Pre-marked and photographed maps 
o	Geodata of the results and some pictures 


### During the exercise:  
#### Introduction: 
- Introduce the idea, the aim and the general workflow of the Skecht Map Tool beforehand 
- Provide access the needed material and build groups (in groups at least 3 people each to discuss together) best Groups of 3-6 participants)

#### Time for group work: 
- Check-in with the groups if there are questions or problems.
- Prepare the presentation tool for the Wrap-Up.

#### Wrap up: 
- All groups present their findings (each 5 min, make it short but show the maps they are talking about).
- Discuss Benefits as well as challenges and problems in the use of the sketch Map Tool 
- Time to for Open questions.
::::

## What you need to know - background information

### Basic functionalities of the SMT
The Sketch Map Tool (-linked) is an easy-to-use tool for participatory mapping through offline collection, digitisation and georeferencing of local data. The low-tech solution is designed to simplify the collection and analysis of local spatial knowledge and perceptions with pens and paper maps, the so-called Sketch Maps. The Sketch Map Tool is an open-source web application. It facilitates the creation, usage and afterwards the digitisation and analysis of paper-based maps with OpenStreetMap and satellite data. 
 
```{figure} /fig/SMT_workflow_Satelite.png
---
height: 50px
name: T
align: center
---
Picutre of the workflow
```

The first step is the creation of the paper-based maps. Users can choose between two basemap containing OpenStreetMap (OSM) Data and basemaps containing satellite images. In addition, the tool can evaluate how well-suited an area of the OpenStreetMap (OSM) basemap is for participatory mapping based on a quality analysis of the OpenStreetMap (OSM) basemap data through the HeiGIT ohsome quality analyst.  (→ Hyperlinks are missing to OSM and ohsome quality analyst). 
For the data collection through offline participatory mapping you  only need  your participants, the printed Sketch maps and some pens. 
After mapping, the Sketch map Tool supports the digitalizion of the Sketch Maps. Uploading of pictures and scans of the marked Sketch Maps initiates an automatic georefferencing and coloure-detection process, and the results can be downloaded in various geodata formats. The tool employes a fusion of computer vision algorithms and novel AI models to extract Sketch Maps from photos and detect markings on them. The results can then be used for further analysis in Geographic Information System software.


### What does georefferenced means?

| A not georeferenced image | A georeferenced image – GeoTIFF |
| :-------------------- | :----------------- | 
| Just an image, even if you load it in QGis and give it a coordination system it can´t be located and the image is shown somewhere in the Atlantic. | The file contains information about its coordinate system and its location, so you can combine it other geodata e.g. with GPS data.| 
| ```{figure} /fig/SMT_Map_Not_georefferenced.png``` | ```{figure} /fig/SMT_Geofrefference_map.png``` | 

### Background Information on UMAP

UMAP is an online platform that allows users to create custom maps with OpenStreetMap (OSM) as basemap layer. No installation nor registration is necessary. This enables users to quickly gain an intuitive overview of their data.
Users can customize the appearance of the map and share it with others. It's particularly useful for collaborative mapping projects, quick visualization of geographic data, and creating custom maps tailored to specific needs.

| Feature| QGIS | UMAP |
| :-------------------- | :----------------- | :---------- |
| Type | Desktop Geographic Information System (GIS) software | Online mapping platform|
| Accessibility| Requires installation on a desktop computer | Accessible online via web browser |
| Purpose |Comprehensive GIS software for spatial data analysis | Interactive mapping tool for creating custom maps |
| Data Import | Supports various data formats (shapefiles, geodatabases, etc.) | Vector data only, user input via map canvas, some geo formats (geojson, .gpx, .kml, .osm) |
| Data Visualization and Analysis|Offers extensive visualization and analysis capabilities, Provides a wide range of geospatial analysis tools  | Focuses on creating interactive maps with custom elements; No analysis tools |
| Output | Printable map with all necesary map elements | URL so share map online |


```{Hint}
The Geojson output of the Sketch Map Tool cannot be opened and inspected with commonly available tools. If you use the Sketch Map Tool and do not have QGIS installed but quickly want to examine your result, UMAP is a simple and quick way to do so. But be aware as it is an online platform, an internet connection is required.
```

## Step-by step introduction for participants 

link where you can download this part as a short pdf to hand it to participants

If you expieriences any problems during your use of the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) please take a look at the [Help page](https://sketch-map-tool.heigit.org/help).



### 1.	Start discussion
Prepare and discuss in your small group.
- Take a look at information about your case-study. The images included might give you an idea how the community might look like.
- What do you like to map? You can decide if you like to map the hazzard (e.g. in the flood extent), vulnerablities or capacetise.
- Scroll through the help-page of the Sketch Map Tool

### 2.	Create a map in the Sketch Map Tool
- Open the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) 
- Zoom in and select your map area: Try different zoom levels and change the orientation. 
- For the test create a map as A4.

### 3.	Mapping

- Discuss in your group what and how you would like to map, decide if you make larger areas, the streets, … so your mapping is similar, and the results can be compared. Please take a look at our help page (-> Link) for tips on mapping.

- Try to identfy realtic paces for what ever you like to map. Or alternatively just mark the map with different shapes in different sizes and colours to explore how the digitalisation will look like. 

```
Print your maps and mark with real pens to experience the real use of the Sketch Map Tool. Or if it is not possible use alternatives with pre-printed maps or digital markings. Take a look at the mapping tips on the help page.
```

### 4.	Digitalise
- Take a photo of your map. Please take a look at our help page (-> Link) for tips on how to take the picutre.
- Upload the photo to the Sketch Map Tool.
- Download the results to the Sketch Map Tool.

### 5.	Open your results in QGIS or umap
- Upload or open your results in QGIS or umap. 
- Take a look at the detected markings, compare it with your map which differences can you see?


#### A. Open your results in QGIS

1. __Open QGIS__

    Open QGIS and navigate to `Project` -> `New` and click on `Save`. Naviagte to where you want to save your project, give it a name and click `Save` again. When working in QGIS always remember to save your project every now and then.

2. __Add a Basemap__

    For a better overview and orientation it is always helpful to add a basemap to your project and put your situation in a spatial context. Find in the `Browser` Panel `XYZ Tiles`, open the dropdown by clicking on it and select OpenStreetMap or another basemap.

    Click [here](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html#standard-qgis-basemaps) for more information on basemaps and how toa dd them to your project.

2. __Load your results (the Downloads from the Sketch Map Tool) in QGIS__
    Now load your download from the Sketch Map Tool: the vector file (the geojson) and geotiff files (they are all in one folder, which you need to  un-zipp) by dragging and dropping them into the layer panel. Be aware which files are at the top, because you might not be abel to see

#### B. Open your results in UMap

1. Open the Browser of your choice and navigate to the [UMAP Website](https://umap.openstreetmap.fr/en/) and click on the large green button `Create a Map`.

2. Right above your map canvas, you can click in "Untitled Map" in order to edit your map properties. Give your Map a title and a short description.


```{figure} /fig/en_SMT_ex4_UMAP_Properties.PNG
---
width: 350px
name: SMT Ex4B Umap properties
align: center
---
Editing the map properties
```

3. You can load your data into the map frame by clicking on the arrow button. The `Import data` window will open on the right hand side. CLick on `Select file` and navigate to your vector output from the SKetch Map Tool ("Schuld_Ahr-tal_sketch-map_Ex4.geojson") and click on `Open`. UMAP will automatically detect that your vector is a geojason format. Click on `Import` to load your data to your map canvas.

```{figure} /fig/en_SMT_ex4_UMAP_Data_Loaded.PNG
---
height: 400px
name: UMAP Data Loaded
align: center
---
UMAP interface with the Sketch Map vectors
```

4. Click in the upper right corner on `Save`. If you are not logged in you will be provided with an URL where you can access and your map any time lateron. Save it somewhere or send it to your email. 


### 6.	For Wrap-up: What are your experiences with the Sketch Map Tool? 
- Make some notes and prepare a short presentation about your map area, there markings and how the results look like at the endand bring them back in the big group to wrap the exercise together
- Did you discover any problems or challenges during this exercise?
- What is the greatest benefit of the Sketch Map Tool from your perspective? 
- Are their any open questions? 