# Exercise 7: Georeferencing a map of Somalia

:::{card}
__Aim of the exercise:__
^^^
The aim of this exercise is to learn how to georeference a map. In many cases, (governmental) institution might only 
publish data or maps in a pdf format. However, by georeferencing the map, we can import the map as a raster dataset into 
our QGIS-project. After that, we can either use it to digitise vector features, or use the raster values in raster data 
analysis. 
:::

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__These skills are relevant for__ 
^^^
- Digitising maps
- Preparing data for spatial analysis


:::
::::

::::{grid} 2
:::{grid-item-card}

__Estimated time demand for the exercise__
^^^
~ 90 minutes

:::

:::{grid-item-card}
__Relevant Articles__
^^^

* [Georeferencing](/content/Modul_3/en_qgis_georeferencing.md)
:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

### Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::

## Step by Step instructions

:::{card} 
:class-card: sd-text-justify sd-rounded-3 sd-border-2
:link: 

__Click [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_7/Module_3_Exercise_7_Georeferencing.zip) to download the datasets for this exercise.__

:::

:::{card}
__Available Data:__
^^^

- `SOM_soil_deg.png` - A picture of a soil degradation map of Somalia taken out of a PDF report (Source: [FAO SWALIM](https://www.faoswalim.org/resources/site_files/L-14%20Land%20Degradation%20and%20a%20Monitoring%20Framework%20in%20Somalia_0.pdf))
- `som_admbnda_adm1_ocha_20230308.gkpg` - A vector layer with the adkministrative boundaries of the regions (adm1) of somalia (Source: OCHA)
:::

### Preparing the data

1. Unzip the folder and familiarise yourself with the data by looking at the soil degradation map. The map is located in the `Module_3_Exercise_7_Georeferencing/data/input/`-Folder.
2. Create a new QGIS-project.

```{figure} /fig/SOM_Soil_deg.png
---
name: SOM_soil_deg
width: 500 px
---
Soil degradation in Somalia
```

### Step 1: Adding a basemap and loading the vector layer

Georeferencing is done by connecting the points on the map that will be georeferenced to coordinates on your map canvas in QGIS. Adding a basemap or a reference layer to your QGIS project will help you to identify the corresponding coordinates.

1. Add a basemap using either XYZ-tiles or the [QuickMapServices Plugin](/content/Wiki/en_qgis_basemaps_wiki.md)
2. Import the `som_admbnda_adm1_ocha_20230308`-layer to the QGIS project. 

### Step 2: Georeferencing the map

Now that we prepared our QGIS-project, let's start georeferencing the map.

3. Open the Georeferencer by navigating to the Top Bar > `Layer` > `Georeferencer` (see {numref}`open_georeferencer`)

```{figure} /fig/en_3.36_open_georefencer.png
---
name: open_georeferencer
width: 500 px
---
Opening the Georeferencer in QGIS 3.36
```

4. A new window will open. This is the __georeferencer__. To add an image to georeference, click on ![](/fig/3.36_add_raster_georef.png) `Open Raster`.
5. Select the image of the map you want to georeference. Click `Open` (`Module_3_Exercise_7_Georeferencing/data/input`). 
6. The image will appear in the middle of the georeferencer window. Click on ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. A new window will open. Here you can set the transformation type and the target CRS. For our purpose, we will use the linear transformation type. As the target CRS (Coordinate Reference System), we want to use the same as for our other data. In our case, we can use EPSG:4326. Below, you can set the name and save location of the file. Make sure that the `Load in project when done` is checked. 
::::{margin}

```{note}
In most cases, you can leave the transformation type on `linear`. Regional maps are usually in a conformal projection (i.e. the angles are preserved). Satellite imagery as well. If you realise that the angles are not true, or the map is deformed or distorted, you may need to choose `polynomial` as transformation type. Polynomial transformations need more Ground Control Points and the points need to be distributed evenly across the map.
```

::::
8. Click on `Ok`. 
9. Once you have set the transformation type, you can start adding Ground Control Points (GCP) by clicking on ![](/fig/3.36_georef_add_point.png) `Add Point`. Ground Control Points are points that you ascribe specific geographic coordinates. 
10. Click on a point on the map image. This will be the precise location that you can identify on both the basemap and the map you wish you georeference. 
11. Once you clicked on a position, a new window will appear. Here, you add the coordinates to the point you selected. There are two options to do this:  
    - Enter the coordinates manually. You will need to know the exact coordinate. Sometimes, you have a coordinate grid on maps where you can 
    - Select the points ![](/fig/en_3.36_georef_select_from_canvas.png). This mode will minimize the georeferencer and open the QGIS Map canvas. Zoom to the same location you selected on the non-georeferenced map and Click once.
    - Once the coordinates are entered, click `Ok`
12. The georeferencer window will open again. This time, below the map image, you can see a point in the table. These are the Ground Control Points. Continue adding more GCP. Spread them out over the entire map. Make sure that the `Mean error` in the bottom right corner of the georeferencer window is as low as possible (below 5 is ideal). 

```{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: georeferencer_dialogue
---
Georeferencer dialogue in QGIS 3.36
```

13. Once you have added enough points, click on ![](/fig/3.36_start_georef.png) `Start Georeferencing`. QGIS will use the Points you added to transform the image into a georeferenced image, where every pixel has GPS coordinates ascribed to it. 
14. You can close the georefencer window. Decide wether you want to save the GPC points in a file. If you are not sure if your georeferencing accuracy was precise enough, save the GPC points so you don't have to do all the work again. 
15. Congratulations, the georeferenced map will now appear as a raster layer in your QGIS-project


```{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: Som_georef_map
---
A georeferenced map of Somalia in the QGIS Map Canvas
```

### *Optional* Step 4: Adjusting the transparency of the georeferenced map

Now that we have the georeferenced map, we can __set the transparency__ so that we can see other layers or the basemap underneath: 

16. <kbd>Right-Click</kbd> on the layer of the georeferenced map. 
17. Select `Properties`.
18. Navigate to the __Transparency tab__.
19. Set the transparency to 50%.
20. Click on `Apply`.

Now we are able to see the underlying layers. We can also check the accuracy of our georeferencing by comparing the lines of the administrative boundaries of both layers.

### *Optional* Step 4: Digitising vector features using the georeferenced map

Now that we have the map georeferenced, we can use it as a background layer to digitise vector features, such as a polygon indicating a region where the soil degradation is severe.

21. Create a new shapefile layer (see [digitisation](https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_digitalisation.html#creating-new-datasets)). Click on `Layer` > `Create Layer` > `Create new Shapefile Layer` (You can also choose to create a new Geopackage Layer).
22. A new dialogue window will open. First, we need to specify the save location of the new dataset. 
    1. Click on ![](/fig/3.36_three_dots.png) to the right of the `File Name`-field. 
    2. Navigate to the data output folder (`Module_3_Exercise_7_Georeferencing/data/output`).
    3.  Enter a name for the dataset. 
    4. Click `Save`.
23. Set the `Geometry Type` to `Polygon`.
24. Let's add a field (column in the attribute table) so we can add information about the soil degradation type: 
    1. Under `New field`, add a name, for example, `soil_deg`. We want strangers to be able to identify the type of information stored in that column. 
    2. Leave the type on String (text).
    3. Click on `Add to field list`. 
25. Finish creating the dataset by clicking on `Ok`. The layer will be added to your layers-panel.
26. Now, let's create a new polygon feature: 
    1. Select the new layer in the layers-panel.
    2. Activate the editing mode by clicking on ![](/fig/en_editing_mode.png).
    3. Click on ![](/fig/mActionCapturePolygon.png) in the digitisation toolbar to create a new polygon.
    4. Start tracing the outline of a field where the soil degradation is severe (in red) by setting multiple points (<kbd>Left-Click</kbd>)
    5. Once you are done tracing the outline, finish creating the feature by <kbd>Right-Clicking</kbd>.
    6. A new dialogue window will pop up. Here you can enter the attributes for the newly created polygon feature. Under `soil_deg`, enter "severe". 
    7. Click ok.

Congratulations, we now have digitised a map and digitised vector features we can now use for further analysis!

