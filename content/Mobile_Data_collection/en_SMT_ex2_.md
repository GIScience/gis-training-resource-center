# Sketch Map Tool Exercise 2 - Traffic light

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

This exercise focuses on exploring the basemaps and discussing challenges of map literacy and orientation on the maps, as well as the characteristics, strengths, accuracy or need for updated data, and differences basemaps based on satellite images or OpenStreetMap data.


```{figure} /../fig/SMT_Idee_traffic_light_exerices.png
---
height: 450px
name: SMT traffic light exercise
align: center
---
SMT Traffic light
```

## Characteristics of the exercise 
::::{grid} 2
:::{grid-item-card}

#### Aim of this exercise:
- Get familiar with the OSM and Satellite-image base maps and the Quality reports.
- Get a feeling about how to assess the suitability of a basemaps and familiarise yourself with possible problems.

#### Type of trainings exercise:
This exercise can be used in online and in presence, and is focused on group discussions.
:::

:::{grid-item-card}

#### Focus group (GIS-Knowlege Level)
Planners/Facilitators  (Beginners-level: no knowledge required about QGIS)

#### Phase of participatory/community mapping 
preparing participatory mapping

:::
::::

::::{grid} 2
:::{grid-item-card}

#### Estimated time demand for the exercise.
In general: about 1:15 h to 1:35 h (depending on number of groups) 
- Introduction: 10 min
- Groupe exercise: 35 min ( about 10 min for creating the maps and 25 min group discussion)
- Wrap-up (with presentations) each group about 5 min to present and 10 min general discussion, aswell as a bit buffer time for the change of the groups

:::

:::{grid-item-card}
#### Available data

Download the data for this exercise [here](https://nexus.heigit.org/repository/gis-training-resource-center/mobile_data_collection/sketch_map_tool_training/Exercise_2.zip) and unzip the folder

In the data subfolder (\data\input), you will find the data you need to start the exercise.


:::

::::




## Instructions for the trainers 

:::{dropdown} Trainers Corner
### Preparation and material 
- Online access and devices (PC) to be able to use the Sketch Map Tool and create maps online.
- For each group one individual set of the Sketch Maps (OSM + satellite) digitally or as a print and reports of one area OSM + satellite-map and the fitting report.
- Take a look and make yourself familiar on the provided material for the exercise and the Sketch Map Tool in general. 
- Prepare a board (it can be a white board/flipchart/or digital e.g. mirro-board) where the participants can add their findings.

### Available Material: 

https://nexus.heigit.org/repository/gis-training-resource-center/mobile_data_collection/sketch_map_tool_training/Exercise_2.zip

- Introduction Slides to the Sketch Map Tool
- [5 prepared cases](https://nexus.heigit.org/repository/gis-training-resource-center/mobile_data_collection/sketch_map_tool_training/Exercise_2.zip) if you like to save time (with Sketch Maps and Map Quality Check) 


### During the exercise:  
#### Introduction: 
- Make sure everyone is familiar with the basic understanding about OSM and satellite maps. Introduce the aim of the exercise and the idea of the traffic lights and the analysis before you start the exercise!
- Provide access the needed material and build groups of 3 to 6 people in order to discuss the findings. 

#### Time for group work: 
- Check-in with the groups to see if there are any questions or problems.
- Prepare the presentation tool (e.g. Miro, White-board, etc.) for the wrap-up.


#### Wrap up: 
- All groups present their findings (each 5 min, make it short but display the maps they are talking about).
- Discuss benefits, as well as challenges and problems in the use of the Sketch Map Tool. 
- Time to for open questions.
::::



## What you need to know - background information

### Benefits of the Sketch Map

#### During the data collection: 
- Maps provide orientation and can guide discussions
- With the sketching, you achieve an immediate visualization of local knowledge.

#### After the data collection:
- Displaying and sharing the result. 

### Characteristics of the two base maps 

| | Satellite imagery| OSM data|
| :-------------------- |:-------------------- | :----------------- | 
| Data source | [World Imagery ESRI](https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9#!) |  [OpenStreetMap Community](https://www.openstreetmap.org/#map=6/51.330/10.453)  | 
| example map | ![](/fig/SMT_Satelite_Heidelberg_empty.jpg) | ![](/fig/SMT_Heidelberg_empty.jpg) | 
| curentness | The satelite imagery is typically within 3-5 years of currency. | Current OSM-data is used in the base map. | 
| Biggest benefit | Impression of the landscape and topography | Clear outlines and at times labels especially of important infrastructure e.g. hospitals, possibilty to improve the map by contributing to OSM.| 

### What does georeferenced mean?

| non-georeferenced image | georeferenced image – GeoTIFF |
| :-------------------- | :----------------- | 
| This is just an image, even if you load it in QGis and give it a coordination system it can´t be located and the image is shown somewhere in the Atlantic. | The file contains information about its coordinate system and its location, so you can combine it other geodata e.g. with GPS data.| 
| ![](/fig/SMT_Map_Not_georefferenced.png) | ![](/fig/SMT_Geofrefference_map.png) | 

### Map Quality Check

```{figure} /../fig/SMT_Heidelberg_report_1.jpg
---
height: 450px
name: SMT Heidelberg report
align: center
---
Map Quality Check; Sketch Map Tool Heidelberg report
```
The Sketch Map Tool can evaluate how well-suited an area of the OpenStreetMap (OSM) basemap is for participatory mapping based on a quality analysis of the [OpenStreetMap (OSM)](https://www.openstreetmap.org/#map=6/51.330/10.453) basemap data through the [HeiGIT ohsome quality analyst](https://heigit.org/big-spatial-data-analytics-en/ohsome/ohsome-quality-analyst-oqt/).

The Map Quality Check assists in evaluating the suitability of the area of interest for participatory mapping through a quality analysis of the OpenStreetMap data with the HeiGIT ohsome quality analyst. The fitness report can be downloaded as a PDF file by clicking on the blue button. It provides an evaluation of the suitability of the local OSM data and recommendations for subsequent field data collection.

## Step-by step introduction for participants 

link where you can download this part as a short pdf to hand it to participants

If you expieriences any problems during your use of the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) please take a look at the [Help page](https://sketch-map-tool.heigit.org/help).


### 1.	Create the maps and reports

- Open the [Sketch Map Tool](https://sketch-map-tool.heigit.org/)
- With you group, decide on an area fitting to your case-study. You can also choose an area you know very well or find interesting.
- Zoom in and select your map area: Try different zoom levels and change the orientation. 
- Create several maps of the same area with different orientation, zoom-level or basemaps. 

| Sketch Map with a satelite base map| Sketch Map with a OSM base map | Map Quality Check |
| :-------------------- | :----------------- | :------------------ |
| ![](/fig/SMT_Satelite_Heidelberg_empty.jpg) | ![](/fig/SMT_Heidelberg_empty.jpg) | ![](/fig/SMT_Heidelberg_report_1.jpg)|

```{Tip}
To shorten the time, you can work with [prepared cases](https://nexus.heigit.org/repository/gis-training-resource-center/mobile_data_collection/sketch_map_tool_training/Exercise_2.zip).
```

### 2.	Collect your insights to the following questions
Add your insights to a presentation or on a (digital) board to share it later.
  
Discuss with your group: 
- What are the main characteristics of the area you see on the basemap? Describe, separately, both basemaps (satellite image vs. OSM basemap). 
- Could you orient yourself on the basemap? Are there points of interests or something you could use as a orientation point?
- Would you say that the basemaps are suited for participatory mapping? Reason your answer and think about participants that are not familiar with basemaps.  
- Which difference can you detect between satellite and OSM basemaps?
- In which uses cases would you prefer a OSM basemap? 
- In which uses cases would you prefer a satellite imagery basemap?
- What traffic light colour would you give the satellite imagery and OSM basemap individually for this area?
- Discuss the OSM-Mapping-suitability-report:
- What is the overall result of the basemap? (Which colour of the traffic light?)
- What are your most important findings from the OSM-Mapping-suitability-report?
- Would it make sense to organise a mapathon beforehand in order to improve the OSM data to use with your Sketch Map?

### 3.	Wrap-up: 

Make some notes and prepare yourself for a short presentation of your maps to share with the other participants:
- Prepare your Presentation and decide who is going to present.
- Think about open questions, as well as feedback to the exercise