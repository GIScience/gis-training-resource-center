# Exercise: Security Peshawar
__🔙[Back to Homepage](/content/intro.md)__

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Modul_3/en_qgis_modul_3_exercises.html
__Click here to return to the exercise overview page for module 3__ 
:::
::::{grid} 2
:::{grid-item-card}
## Aim of the exercise:

#### Type of trainings exercise:
- This exercise can be used in online and presence training. 
:::
:::{grid-item-card}
#### These skills are relevant for 

- QGIS Essentials
- Working with multiple layers
- Conduct spatial queries
- Creation of geodata

:::
::::

::::{grid} 2
:::{grid-item-card}
#### Estimated time demand for the exercise.
- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.
:::

:::{grid-item-card}
### Relevant wiki articles

* [Geodata Import in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html)
* [Layer Concept](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_layer_concept_wiki.html)
* [Geodata Classification- Categorized](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_categorized_wiki.html)
* [Digitisation- Point data](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer)
:::
::::

::::{grid} 1
:::{grid-item-card}
#### Context

:::
::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) for some general tips on training conduction

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
### Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Exercise_4_Security_Peshawar/Modul_5_Exercise_4_Security_Peshawar.zip
__Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Exercise_4_Security_Peshawar/Modul_5_Exercise_4_Security_Peshawar.zip) and save the folder on your computer and unzip the file.__
:::

| Dataset name| Original title|Publisher|Download from| 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| 2024-01-01-2024-09-23-Pakistan.xlsx |Conflict data for Pakistan 01/2024-09/2024  |ACLAD| HDX |
| PAK_KP_admin_3.gpkg |Administrative Boundaries level 3 of KP |UN OCHA | HDX |
| Pak_adm2_Khyber Pakhtunkhwa.gpkg |Administrative Boundaries level 1 of KP |UN OCHA | HDX |
|20240605_PAK_MPI.xlsx|Pakistan Multi Poverty Index (MPI)|Pakistan Bureau of Statistics|Pakistan Bureau of Statistics|
|AOI_Peshawar.gpkg|Area of Interest (AOI) around Peshawar|||



## Task 1: Geolocate security-related information of the last days

:::{card} Context: 
In response to a recent cholera outbreak in Khyber Pakhtunkhwa (KP), the Pakistan Red Crescent Society (PRCS) and other Partner National Societies (PNS) have mobilized a team to this region. The primary objective of the team is to conduct a comprehensive assessment on the ground and facilitate coordination for any necessary future responses.
The team will be staying at the "Roomy Crossroad Hotel Peshawar" during their mission in the affected area.
:::

1. We will use the plugin in "Quick Map Service" to locate places precisely.
To install the plugin click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `Quick Map Service`. Once you have found it, click on it and click `Install Plugin`([Wiki Video](/content/Wiki/en_qgis_plugins_wiki.md#installation-of-plugins)).
2. Open the plugin by clicking on `Web` -> `Quick Map Service` -> `ESRI` -> `ESRI Satellite`. Now you should have a Settelite image base map in your `Layer Panel`.
3. Add the `Google Road` base map from the `Quick Map Service` as well.
4. Place the `Google Road` above the satellite image map and turn the layer transparent by opening the symbology window and adjusting the opacity.
5. You will need the plugin "Lat Lon tools" to locate the coordinates you receive from the field. To install the plugin click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `Lat Lon tools`. Once you have found it, click on it and click `Install Plugin`([Wiki Video](/content/Wiki/en_qgis_plugins_wiki.md#installation-of-plugins)).

Now you are ready, check the information from the field below and capture it in a new point layer. Use Google in your browser, the base maps and the Lat Lon tools plugin to locate the exact positions.

```{Warning}
When creating the point and polygon layer use the CRS UTM 42 N __EPSG: 32642__
```


In case the information states an exact area, create a new polygon layer and map it exactly.

| Number| Description |
| :-------------------- | :----------------- |
|1 | An IED explosion on the road N45 between Seri-Bahlol and Tableeghi Markaz Mardina near Jandy has been reported by local radio stations. | 
|2|In a conversation with a PRCS driver, a local teacher shared that the vicinity of the Government __Girls Primary School__ in __Takkar__ is notorious for being a minefield. Specifically, the area between the main road and a smaller dirt road behind the school is known to be heavily mined. Due to this danger, local farmers are extremely reluctant to work on this particular piece of land.|
|3|Following the recent events, it has been decided that the vicinity surrounding the __Arbab Niaz Cricket Stadium Peshawar__ is now designated as a no-go area for all staff members. This area encompasses the region bordered by the __N5__ road to the south, the __Afghan Colony road__ to the north and east, and the __Charsadda Road__ to the west.|
|4|GPS Coordinates __(33.99519949518549, 71.66217873936723)__: A humanitarian worker was transporting medical supplies through the region when they were approached by a local farmer. The farmer mentioned that a nearby abandoned well, located at these coordinates, has become a gathering point for unexploded ordnance. Due to its proximity to a residential area, this site is now flagged as high-risk and needs immediate attention from demining teams.|
|5| Address: __(11, Jinnah Road, Peshawar)__ :A government building at this address has recently been vacated after a bomb threat was called in. Police and bomb squads searched the premises but didn’t find any explosives. However, local business owners reported unusual activity around the building in the weeks leading up to the threat. This location  is now under surveillance, and it needs to be marked as a temporary no-go zone.|
|6| __Qissa Khwani Bazaar, Peshawar__: A popular historical market at this address has become a focal point for local community gatherings, but recent intelligence reports suggest that the site could be at risk for political protests that have turned violent in the past. Authorities are now considering setting up temporary barriers to manage the flow of people, and it's crucial that this location is marked as a high-risk area for potential crowd control measures.|

The current SOP states that the sides of recent violent incidents are to be avoided in a 1 km radius. To reflect this on the map, we will use the buffer tool.

6.  Create a ![](/fig/mAlgorithmBuffer.png) buffer around the points of violent incidents with a distance of `2.000 meters`. See the Wiki entry on [Geoprocessing](/content/Wiki/en_qgis_geoprocessing_wiki.md) for further information.
7. Next, merge the no-go areas polygon layer and the buffer point layer.
Use the tool `Merge vector layer`.
8. Clip the newly created polygon out of the AOI to create a "Green" area in which the team are allowed to travel. Use the tool `Symmetrical difference`.



### Task 2: Load Excel File containing conflict data into QGIS

1. Drag and Drop the ACLED conflict excel table '2024-01-01-2024-09-23-Pakistan.xlsx' into your QGIS project
2. Navigate in the Processing Toolbox to the Tool 'Create points layer from table'.
    - Choose as 'X Field' "longitude" and as 'Y Field' "latitude".
    - Under 'Points from Table' , click on the three dots, choose 'Save to GeoPackage' and navigate to you temp folder. Save the layer with the name "Pak_Conflict_points_2024".

```{figure} ../../fig/Create_ponts_from_table.PNG
---
width: 700px
name: SVG Marker
---
Create points from table
```

3. Get number of events per thesil
    - Load the "KP admin 3" layer.
4. We are now interested to know the number of conflict incidents per thesil. For this:
    - Go to the Processing Toolbox and search for the Tool 'Count points in polygon'. Choose 'KP_adm3' layer as Polygon input and the 'Pak_Conflict_points_2024' layer as Points input

    - Under `Count` save your new layer under "Pak_num_events_adm3".

```{figure} ../../fig/count_point_polygon.PNG
---
width: 700px
name: SVG Marker
---
Count points from polygon
```

5. Open the attribute of your 'Pak_num_events_adm3' layer and scroll to the right. You will find a column with the name "NUMPOINTS". Here you find the number of events per thesil.
    - Right-click on the layer and navigate to 'Properties' --> 'Symbology'. On the top change Single Symbol to "Graduated".
    	- In the 'Value' field choose "NUMPOINTS". 
	- Then below click on "Classify"
	- You can adjust the Mode and the number of classes if wanted. Also you can choose your preferred color ramp.You can play around a bit here.
	- Click 'Apply' and then 'OK'

Your result could look similar to this.

```{figure} ../../fig/Number_events_graduated.PNG
---
width: 700px
name: SVG Marker
---
Number of conflict events per thesil

```


### Task 3: MPI data 

1. Open the excel file and export it as CSV UTF-8:
	* Click on `File` -> `Save As` 
	* Chosse an output folder, where it will be saved (the `data` > `temp` folder is recommended here) and give the file a meaningful name, for instance __20240605_PAK_MPI__.
	* Choose the option __CSV UTF-8 (Comma delimited) (*.csv)__ and `Save` 
	
	```{figure} /fig/PAK_Excel_to_CSV.png
	---
	width: 400px
	name: Convert Excel to CSV
	align: center
	---
	Convert Excel to CSV
	```
	
2. Open QGIS and create a new project. Save the project in your project folder. 
3. Add the __20240605_PAK_MPI.csv__ file to QGIS by: 
	* Click on the `Layer` tab -> `Add Layer` > `Add Delimited Text` 
	* Browse for your __20240605_PAK_MPI.csv__ file. 
	* Choose the correct `File Fromat`: `Custom delimters` -> `Semicolon` 
	* Go to	the tab `Geometry Definition` and choose `No geometry`. We don't have a column with coordinates or geoemtry information, but only the admin2 name and P-Code.
	* Add layer and close the window. 
	
	```{figure} /fig/PAK_Load_CSVfile.PNG
	---
	width: 400px
	name: Load CSV file to QGIS
	align: center
	---
	Load CSV file to QGIS
	```
	
To visualize the data now on the map we have to link it to existing geometries and district boundaries. To do that: 

3. Open the attribute table of the attribute table and detect the column which contains the information you want to use to join the data with the location. E.g. City name, district name, or best the P-Code. In our case it is `ADM2_PCODE`.
	* __Hint__: Each administrative level and area contains a worldwide unique code number. This helps to determine the exact administrative boundary without misspelling the name of the area.
4. We now need an admin layer with an column containing the exact same information as the column of our CSV file. This is needed to link the information provided in the CSV to the district areas. 
	* Load the layer __Pak_adm2_Khyber Pakhtunkhwa.gpkg__ via drag and drop to QGIS. 
4. To link the two layers, open the Toolbox and search for the tool __Join attributes by field value::. Open it. 
	* Input layer: __Pak_adm2_Khyber Pakhtunkhwa.gpkg__
	* Table field: __admin2Pcode__
	* Input layer 2: __20240605_PAK_MPI.csv__
	* Table field 2: __ADM2_PCOCDE__
	* Choose a location to save the file as GeoPackachge and give it a meaningful name, for instance __MPI_Admin2_joined.gpkg__
	* Run and close.
	
	```{figure} /fig/PAK_joined_MPI_csv_admin2.PNG
	---
	width: 400px
	name: Join the districts with the MPI data
	align: center
	---
	Join the districts with the MPI data
	```
	
	Info: You can see that not all areas are visible. Since we don't have data for all districts, only the districts were linked with the csv on which we have MPI data. 
	
	```{figure} /fig/PAK_joined_MPI_csv_admin2_info.PNG
	---
	width: 400px
	name: Information of not joined and linked data
	align: center
	---
	Information of not joined and linked data
	```
	
5. Visualize __MPI_Admin2_joined.gpkg__ file: We have a new file, showing the district boundaries, but having the MPI information in the attribute table. The MPI value per district we now want to visualize. 
	* Open the `Symbology` window of the file __MPI_Admin2_joined.gpkg__.
	* Decide which column you want to visualize. For instance the values of the year 2014 in the column __A_2014_15__. 
	* Choose `Graduate` visualization. 
	* Choose Value __A_2014_15__.
	* Click `Classify`
	* Choose Mode `Pretty Breaks`
	* Click okay and close the window. 
6. Visualize __Pak_adm2_Khyber Pakhtunkhwa.gpkg__ layer for districts we don't have MPI data on. 
	* Open the `Symbology` window of the file __Pak_adm2_Khyber Pakhtunkhwa.gpkg__
	* Change the color, maybe to dark grey, so we can differentiate between the districts we have and don't have MPI data for. 
7. Add OpenStreetMap as a baselayer for better orientation. 


```{figure} /fig/PAK_visualized_MPI.PNG
---
width: 400px
name: Visualized MPI data on district level
align: center
---
Visualized MPI data on district level
```
