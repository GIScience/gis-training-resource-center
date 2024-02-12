# Sketch Map Tool Exercise 5 - Heat Map Visualization

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧




## Characteristics of the exercise 
#### Aim of this exercise:
Learn 

#### Phase of participatory /community mapping 
analysing participatory mapping results
#### Focus group (GIS-Knowlege Level)
Medium-Advanced level (participants have worked with QGIS before)
#### Type of trainings exercise:
This exercise can be used in online and presence training and is focused on an hands-on experience with QGIS spatial analysis tools.
#### Estimated time demand for the exercise.


## Instructions for the trainers 

:::{dropdown} Trainers Corner
### Preparation and material 
- Online access and devices (PC)
- QGIS installed on the computer
- Take a look and make yourself familiar on the provided material for the exercise and the Sketch Map Tool in general. 

```
Alternatives  
- If you like to skip parts of the workflow, make sure you have alternative material (like preprinted, or already marked Sketch maps) prepared.
- If you like to adapt this exercise to your specific use case, create your own case-description. 
```



### Available Material: needs to be linked directly 
•	Introduction Slides about the Sketch Map Tool available
•	5 Pre-marked and photographed maps to be use as input for Sketch Map Tool for Exercise B
o	Geodata of the results and some pictures 


### During the exercise:  
#### Introduction: 
- Introduce the idea, the aim and the general workflow of the Skech Map Tool beforehand 
- Provide access to the needed material 
- check-in if there are questions or problems.

#### Wrap up: 
- Take some time at the end to wrap up and that several people present their result map
- Discuss Benefits of showing results as a heatmap and think about further thematic areas where this could be useful
- Time to for Open questions.

## Step-by step introduction for participants 

link where you can download this part as a short pdf to hand it to participants

If you expieriences any problems during your use of the [Sketch Map Tool](https://sketch-map-tool.heigit.org/) please take a look at the [Help page](https://sketch-map-tool.heigit.org/help).
::::




### Exercise A: Complement your Sketch Map Tool data

Szenarien: 
- Eine eingezeichnete Fläche wurde nicht erkannt, ich möchte sie auf Grundlage des GeoTiffs digitalisieren und dem geojson hinzufügen

- Ich möchte den verschiedenen Polygonen eine weitere Information/column hinzufügen


To do: map erstellen und ein Polygon mit Bleistift einzeichen, sodass es nicht erkannt wird. Vielleicht flood risk - vulnerabilities and capacities
--> dann eine spalte mit angeben wo description steht -> culnerability oder capacity je nach Farbe


- Ich habe mehrere geojson outputs von mehreren Sketch Maps


### Exercise B: Heat Map Visualization: Past Flood Delineation

### Scenario and Background

Flood maps hold immense importance, especially in less privileged regions with limited regular surveying by official bodies. In these areas, where access to sophisticated technology and resources is often limited, flood maps provide a vital resource for understanding and managing flood risks. They empower communities to identify vulnerable areas, plan emergency response strategies, and implement mitigation measures. Flood maps facilitate informed decision-making, enabling communities to allocate resources effectively, prioritize infrastructure development, and implement early warning systems. By filling the gap in official surveying, flood maps play a crucial role in enhancing resilience, minimizing damages, and safeguarding lives and livelihoods in these vulnerable regions.

The sketch map tool is a valuable tool for delineating flood areas within a community. It enables users to create hand-drawn or digitally generated maps to identify and outline areas prone to flooding. By incorporating local knowledge and observations, the tool empowers community members to actively participate in flood risk assessment and mitigation efforts. The Sketch Map Tool serves as a user-friendly and accessible solution for mapping flood areas, facilitating community engagement, and informing decision-making processes to enhance resilience and response strategies against flooding events.



#### 1. Data Collection

Imagine you have had a field trip in order to talk to people in the affected areas and let them draw flood prone areas in their community. You are now back to your office and have 5 different flood maps that you have already scanned in. Please download the prepared maps [here]().

Optional: You find the empty map [here](). Feel free to draw some additional flood maps by printing the template out and drawing on it or by using a simple graphics editor.


#### 2. Georeferencing and autoextraction with the Sketch Map tool

Upload the sketch maps back to the tool’s website. Head to [sketch-map-tool.heigit.org](https://sketch-map-tool.heigit.org/) and choose 'Digitize your Sketch maps' on the right. Upload all your sketches in .png or .jpg format. You can mark your sketches and simply drag and drop them into the window.

The sketch maps are now being processed and georeferenced with the annotations extracted and vectorized. Download the vectors. You may use the ones we have prepared [here]().

#### 3. Start your QGIS Project

Open QGIS and load your vector files by dragginf and dropping them into the layer panel. Explore the file by opening the attribute table. 

```{Note}
When you upload a several marked Sketch Maps simultaneously, you will get one vector output containing all the markings of all Sketch Maps, while uploading your Sketch Maps one by one will provide you with one vector file for the marking in each Sketch Map. This information can be important for the planning phase of your p mapping process.
```


#### 3. Rasterize

#### 4. Raster Calculator









## Optional or for near future: Connection of Sketch Map Tool and in field Surveys (f.ex. Kobo)

vielleicht noch bessere Ideen?



