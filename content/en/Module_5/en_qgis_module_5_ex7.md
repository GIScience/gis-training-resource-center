::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
:link-type: doc
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercise 12: Larkana Damage Assessment <a id="exercise-12-larkana-damage-assessment"></a>
id="exercise-7-larkana-damage-assessment"></a>

:::{attention}
The locations in this exercise are real and the flood extent is based on satellite data from UNOSAT (08–12 August 2024). However, __all messages, persons, numbers and damages are fictional__ and were created for training purposes only.
:::

:::{card}
__Aim of the exercise:__
^^^
After the floods in August 2024, the information manager of the Pakistan Red Crescent Society (PRCS) in Larkana receives a lot of information about damaged infrastructure, blocked roads and people in need. The reports come from volunteers, local organisations, authorities, partner organisations and the local population. Some of them are well structured, others are short messages written in a hurry.

Spatial information can be communicated in many different ways: as an address, a link, coordinates in different formats, a description, or a file from the field. In this exercise, you will collect all reports in __one__ point layer in QGIS. You will learn how to deal with different types of location information and how to bring them into a GIS.
:::

::::{grid} 2
:::{grid-item-card}
__Larkana Flood Response Exercise Track:__
^^^

This exercise is part of the [Larkana Flood Response Exercise Track](../Exercise_tracks/en_larkana_flood_response.md).

However, the exercise __can__ be done without completing the previous exercises.
:::

:::{grid-item-card}
__These skills are relevant for__
^^^

- Creation of geodata (digitisation)
- Working with coordinates and coordinate reference systems
- Using plugins (Lat Lon Tools, QuickMapServices, OSM Place Search)
- Importing GPX, Excel and geotagged photos

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 3 hours to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant wiki articles:__
^^^

* [Geodata Import in QGIS](../Wiki/en_qgis_import_geodata_wiki.md)
* [Digitisation](../Wiki/en_qgis_digitisation_wiki.md)
* [Projections](../Wiki/en_qgis_projections_wiki.md)
* [Basemaps](../Wiki/en_qgis_basemaps_wiki.md)
* [Plugins](../Wiki/en_qgis_plugins_wiki.md)
:::
::::

## Instructions for the trainers <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Trainers Corner__

### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions.
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Make sure that the participants have internet access. Several reports require a web browser (Google Maps, OpenStreetMap) and the basemaps are loaded from the internet.
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md) for some general tips on facilitating trainings.

### Conduct the training <a id="conduct-the-training"></a>

__Introduction:__

- Introduce the scenario and the aim of the exercise. Point out the disclaimer: the places are real, the messages are fictional.
- Show the different types of location information that the participants will encounter, but do not explain how to solve them yet.

__Working on the inbox:__

- Let the participants work on the reports individually or in pairs. The hints for each report are hidden in dropdowns. Encourage the participants to try first without opening them.
- Walk around and support. Typical difficulties are the order of latitude and longitude, coordinates in UTM, and finding places with different spellings.

__Wrap up:__

- Discuss the reflection questions in Task 2 together.
- Leave some time for open questions.

### Solution <a id="solution"></a>

| Report | Site | Type of location information | Latitude | Longitude | Flood extent |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | Rural Health Centre Bangul Dero | Address | 27.72794 | 68.28308 | ~610 m |
| 2 | Ratodero Bypass Chowk | OpenStreetMap link | 27.78815 | 68.29156 | ~2.3 km |
| 3 | Flooded fields between Lashari and Dhamrah | KoBo export (5 points) | 27.71280–27.72980 | 68.23370–68.24870 | inside |
| 4 | Seth Mola Bux Brohi Market, Ratodero | Informal message (landmark) | 27.80852 | 68.29580 | ~300 m |
| 5 | Indus Highway N-55, bridge over Warah Canal | UTM 42N (E 429526, N 3068408) | 27.73821 | 68.28497 | ~370 m |
| 6 | The City Hospital Larkana | Address | 27.55996 | 68.19762 | ~1.4 km |
| 7 | Khakhrani village | WhatsApp location | 27.51150 | 68.16342 | inside |
| 8 | Canal regulator (north) | DMS coordinates | 27.90509 | 68.23949 | ~210 m |
| 9 | Larkana Bypass Chowk | Description (landmark) | 27.60491 | 68.20858 | ~540 m |
| 10 | Farmstead near Jara Wah | Geotagged photo | 27.54900 | 68.17100 | inside |
| 11 | Sheikh Zaid Women Hospital | Address | 27.56201 | 68.20369 | ~1.6 km |
| 12 | Fuel station south of Larkana | Google Maps link | 27.47172 | 68.22040 | inside |
| 13 | Road bridge over Sajawal Distributary | Relative description | 27.62060 | 68.20537 | inside |
| 14 | Mahota Railway Station | Address (station) | 27.61792 | 68.27377 | ~540 m |
| 15 | Agham village | Informal message (village name) | 27.81396 | 68.26298 | inside |
| 16 | Road bridge over Rice Canal near Khakhrani | GPX waypoint `BRIDGE_BLOCKED` | 27.52241 | 68.17663 | ~470 m |
| 17 | Dargah Mashori Sharif | Plus Code (7JVCF4QX+8P) | 27.48837 | 68.14933 | ~440 m |
| 18 | Moenjodaro Airport | Address (airport) | 27.33470 | 68.14248 | ~1.8 km |

:::

### Available Data <a id="available-data"></a>

<!--TODO: upload the data folder to nexus and update the link.-->
:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7_Larkana_Damage_Assessment/Module_5_Exercise_7_Larkana_Damage_Assessment.zip
__Download all datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7_Larkana_Damage_Assessment/Module_5_Exercise_7_Larkana_Damage_Assessment.zip) and save the folder on your computer and unzip the file.__
:::

| Dataset name | Original title | Publisher | Download from |
| :-------------------- | :----------------- | :----------------- | :----------------- |
| PAK_Sindh_adm2.gpkg | Administrative Boundaries level 2 of Sindh | UN OCHA | HDX |
| PAK_2024_Minimum_Flood_Extend_reprojected_fix.gpkg | Satellite detected water extents from 08 to 12 August 2024 over Pakistan | UNOSAT | HDX |
| PRCS_team_track_Khakhrani.gpx | GPS track of an assessment team | fictional | – |
| KoBo_agri_assessment_export.xlsx | KoBo export of an agricultural damage assessment | fictional | – |
| IMG_1032.jpg | Photo of a volunteer | fictional | – |

## Preparation <a id="preparation"></a>

1. Create a new QGIS project and save it into the exercise folder.
2. Load the layers `PAK_Sindh_adm2.gpkg` and `PAK_2024_Minimum_Flood_Extend_reprojected_fix.gpkg` into your project ([Wiki Video](../Wiki/en_qgis_import_geodata_wiki.md#open-vector-data-via-drag-and-drop)).
3. Install the plugins __QuickMapServices__, __Lat Lon Tools__ and __OSM Place Search__ ([Plugin installation](../Wiki/en_qgis_plugins_wiki.md#installation-of-plugins)).
4. Add a satellite basemap via `Web` → `QuickMapServices`. If you cannot find `ESRI` or `Google` in the list, you first have to [configure QuickMapServices](../Wiki/en_qgis_basemaps_wiki.md#configuration-of-quickmapservices) and click on `Get contributed pack`.
5. [Create a new point layer](../Wiki/en_qgis_digitisation_wiki.md#creating-a-new-layer) with the name `damage_reports` and save it in the folder `data/results/`. Use the CRS __EPSG:32642__ and add the following fields (all of type text):
    - `report_id`
    - `source`
    - `category`
    - `description`
    - `location_method`

:::{tip}
EPSG:32642 (UTM zone 42N) is a suitable coordinate reference system for Larkana. The __units of measurement are in meters__, which makes it easy to measure distances.
:::

## Task 1: The inbox <a id="task-1-the-inbox"></a>

:::{card}
__Context:__
^^^
August 2024. After days of heavy monsoon rain, large parts of Larkana district are flooded. You are the information manager of the PRCS emergency operation in Larkana. Over the last two days, the following messages arrived in your inbox. Tomorrow, there will be a coordination meeting and all partners need a map of the reported damages and needs.
:::

For every report:

1. Read the message and find out __where__ the reported location is.
2. Locate the place in QGIS.
3. Add a point to the layer `damage_reports` ([Creating point data](../Wiki/en_qgis_digitisation_wiki.md#creating-point-data)): click on ![](../../../fig/mActionToggleEditing.png) `Toggle Editing`, then ![](../../../fig/mActionCapturePoint.png) `Add Point Feature`, and click on the location. Fill in the attributes. In `location_method`, write down how you found the location (e.g. "address", "coordinates", "link").
4. Save your edits regularly with ![](../../../fig/mActionSaveEdits.png) `Save Layer Edits`.

Try to locate the reports without help first. If you get stuck, open the dropdown below the report.

---

:::{card}
__Report 1: Email from the District Health Office__
^^^
"The Rural Health Centre Bangul Dero, Bagnuldero Road, Bangul Dero, Taluka Ratodero reports that the water supply has been out for two days. The facility is running on water tankers and urgently needs water purification tablets. Patient numbers have doubled because people from the flooded villages to the west are arriving."
:::

:::{dropdown} How to locate this report
- The message contains an address. Search for "Bangul Dero" with the `OSM Place Search` plugin ([Wiki](../Wiki/en_qgis_basemaps_wiki.md#navigation-on-basemap-with-osm-place-search-plugin)) or in your web browser on [OpenStreetMap](https://www.openstreetmap.org).
- Zoom in and look for the health centre on the map. Compare the basemap with the description.
:::

:::{card}
__Report 2: WhatsApp message from a truck driver__
^^^
"Brother, stuck at this junction, police not letting trucks go towards Shikarpur. https://www.openstreetmap.org/?mlat=27.78815&mlon=68.29156#map=17/27.78815/68.29156"
:::

:::{dropdown} How to locate this report
- The link contains the coordinates: `mlat` is the latitude and `mlon` is the longitude of the marker.
- Copy the coordinates and use the `Lat Lon Tools` plugin: `Plugins` → `Lat Lon Tools` → `Zoom to Coordinate`. Enter `27.78815, 68.29156` (latitude first, then longitude).
- The part after `#map=` describes the map view (zoom level / latitude / longitude), not necessarily the marker.
:::

:::{card}
__Report 3: Data from the agriculture assessment team__
^^^
"Our team interviewed farmers between Lashari and Dhamrah. Rice fields are fully submerged just before harvest. Please find the export of our KoBo survey attached: `KoBo_agri_assessment_export.xlsx`"
:::

:::{dropdown} How to locate this report
- Open the Excel file in QGIS ([Open .xlsx files in QGIS](../Wiki/en_qgis_import_geodata_wiki.md#open-xlsx-files-in-qgis)) and look at the attribute table. The table has no geometry yet.
- KoBo stores the location in the column `geopoint` in the format `latitude longitude altitude accuracy`. The same values are also split into the columns `_geopoint_latitude` and `_geopoint_longitude`.
- Open the `Processing Toolbox` and search for `Create points layer from table`. Use `_geopoint_longitude` as `X field`, `_geopoint_latitude` as `Y field` and `EPSG:4326` as `Target CRS`.
- Add one point for the reported fields to `damage_reports`.
:::

:::{card}
__Report 4: WhatsApp message from a shopkeeper__
^^^
"Hello, I run a small grocery shop in the Mola Bux Brohi market on Jacobabad Road in Ratodero. Last night the flood water broke through the back wall of my shop. Almost all of my stored rice, flour and lentils are soaked and spoiled, more than 40 bags. The shops next to mine are also damaged. Can someone come and see?"
:::

:::{dropdown} How to locate this report
- Search for Ratodero and find the Jacobabad Road.
- Names can be written differently. Look for a market along the road on the basemap and on [OpenStreetMap](https://www.openstreetmap.org).
:::

:::{card}
__Report 5: Inspection report from the National Highway Authority__
^^^
"Structure: Indus Highway N-55, bridge over Warah Canal. Location: UTM 42N, E 429526, N 3068408. Finding: erosion at the southern abutment, load restriction to 15 t until further notice."
:::

:::{dropdown} How to locate this report
- The coordinates are given in __UTM zone 42N__ (EPSG:32642) in meters, not in degrees.
- Open `Plugins` → `Lat Lon Tools` → `Settings`. Set the input coordinate system for `Zoom to Coordinate` to UTM or to the CRS EPSG:32642 ([How to check the CRS](../Wiki/en_qgis_projections_wiki.md#how-to-check-epsg-codecrs-of-layer-data)).
- Enter the easting (E) and northing (N) values.
- Check the result on the basemap: is there a bridge over a canal?
:::

:::{card}
__Report 6: Email from an INGO health partner__
^^^
"Our mobile clinic team will operate from The City Hospital, Shah Nawaz Road, Larkana from tomorrow. The hospital is seeing a rise in diarrhoea cases among children from Khakhrani and Jara Wah. Please mark it as a coordination point for health partners."
:::

:::{dropdown} How to locate this report
- Search for the address in OSM Place Search or on [OpenStreetMap](https://www.openstreetmap.org).
- Find the Shah Nawaz Road in Larkana first, then look for the hospital along the road.
:::

:::{card}
__Report 7: WhatsApp message from a local NGO volunteer__
^^^
"Location: 27.5115, 68.1634. Khakhrani neighbourhood fully under water, people moved towards Larkana, around 200 persons. Children sick with diarrhoea."
:::

:::{dropdown} How to locate this report
- The volunteer shared a WhatsApp location. The coordinates are in decimal degrees: latitude first, then longitude.
- Use `Lat Lon Tools` → `Zoom to Coordinate` and enter `27.5115, 68.1634`.
:::

:::{card}
__Report 8: Notice from the Irrigation Department__
^^^
"NOTICE: Regulator at 27°54'18.3"N 68°14'22.2"E has been partly opened to relieve the canal system. Downstream villages should expect rising water levels over the next 24 hours."
:::

:::{dropdown} How to locate this report
- The coordinates are given in degrees, minutes and seconds (DMS).
- `Lat Lon Tools` → `Zoom to Coordinate` can read DMS coordinates directly. Copy the coordinates into the input field.
- Alternatively, convert the coordinates into decimal degrees: degrees + minutes/60 + seconds/3600.
:::

:::{card}
__Report 9: Radio log of the traffic police__
^^^
"Heavy traffic jam at Larkana Bypass Chowk (Indus Highway / bypass) because trucks are being diverted around flooded roads. Relief convoys are advised to plan an extra 2 hours."
:::

:::{dropdown} How to locate this report
- "Chowk" means junction. Find the Indus Highway north of Larkana and follow it to the junction with the bypass road.
- Use the basemap and OpenStreetMap to find the junction.
:::

:::{card}
__Report 10: Photo from a PRCS volunteer__
^^^
"Family of 7 on the roof of the house next to it, near Jara Wah. Boat needed!" Attached: `IMG_1032.jpg`
:::

::::{dropdown} How to locate this report
- The location is not written in the message, but the photo contains GPS coordinates in its metadata (EXIF).
- Open the `Processing Toolbox` and search for `Import geotagged photos`. As `Input folder`, select the folder with the photo and click `Run`. QGIS creates a point layer at the location where the photo was taken.
- Add a point at this location to `damage_reports`.

:::{dropdown} Watch here:
<iframe width="560" height="315" src="https://www.youtube.com/embed/TTxcnIWt6mg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
:::

::::

:::{card}
__Report 11: Letter from the hospital administration__
^^^
"Sheikh Zaid Women Hospital, Qambar Road, Larkana: the maternity ward is at 160 % capacity. Many pregnant women from the flooded areas west of the city are being referred to us. Diesel for the generators will last about 3 more days."
:::

:::{dropdown} How to locate this report
- Search for the hospital and the Qambar Road in Larkana with OSM Place Search or on [OpenStreetMap](https://www.openstreetmap.org).
- Several hospitals are located close to each other. Check the name of the building.
:::

:::{card}
__Report 12: WhatsApp message from a logistics officer__
^^^
"Fuel station here still has diesel but the access road is under knee-deep water, only tractors and trucks can reach it: https://www.google.com/maps?q=27.47172,68.22040"
:::

:::{dropdown} How to locate this report
- The Google Maps link contains the coordinates after `q=`: latitude first, then longitude.
- Use `Lat Lon Tools` → `Zoom to Coordinate` and enter `27.47172, 68.22040`.
:::

:::{card}
__Report 13: SMS from a PRCS volunteer__
^^^
"Road bridge approx. 1.8 km north of Bypass Chowk, where the road to Sattar Dino Sangi crosses the Sajawal canal: the approach on the north side has been washed away, cars cannot pass, only motorbikes."
:::

:::{dropdown} How to locate this report
- Start at the Larkana Bypass Chowk (see report 9).
- Use the `Measure Line` tool to measure about 1.8 km to the north.
- Look for the place where a road crosses a canal on the basemap.
:::

:::{card}
__Report 14: Press release from Pakistan Railways__
^^^
"Due to submerged tracks, trains between Larkana and Dadu will not stop at Mahota Railway Station (Larkana–Dadu section, Taluka Larkana) until further notice. The station building is being used as a temporary storage site for relief goods."
:::

:::{dropdown} How to locate this report
- Search for "Mahota" with OSM Place Search or on [OpenStreetMap](https://www.openstreetmap.org).
- Follow the railway line on the basemap to find the station.
:::

:::{card}
__Report 15: SMS from a village elder__
^^^
"Aagham village near Ratodero, water inside all houses. 60 families sitting on the canal bank, need tents and medicine. Pls help."
:::

:::{dropdown} How to locate this report
- The message only contains the name of the village.
- Place names are often written differently. Try different spellings (e.g. "Agham") and search near Ratodero.
:::

:::{card}
__Report 16: GPS track from a PRCS assessment team__
^^^
"Track recorded on our way to Khakhrani. We had to turn back at the bridge over the Rice Canal, water over the deck about 30 cm. See the file `PRCS_team_track_Khakhrani.gpx`."
:::

:::{dropdown} How to locate this report
- Load the GPX file into QGIS via drag-and-drop ([Wiki](../Wiki/en_qgis_import_geodata_wiki.md#open-vector-data-via-drag-and-drop)). QGIS asks which layers to add: select `waypoints` and `tracks`.
- The waypoint `BRIDGE_BLOCKED` marks the location of the blocked bridge.
:::

:::{card}
__Report 17: Voice message from a local NGO (transcript)__
^^^
"About 80 families have taken refuge in the courtyard of the Dargah Mashori Sharif, about 1.5 km west of the Mashori Sharif railway station. Address from Google: F4QX+8P, Lashari Goth. They need cooked food and drinking water."
:::

:::{dropdown} How to locate this report
- `F4QX+8P` is a __Plus Code__, an address format used by Google Maps.
- Copy `F4QX+8P Lashari Goth` into the search bar of [Google Maps](https://www.google.com/maps). Right-click on the marker to copy the coordinates.
- Use `Lat Lon Tools` → `Zoom to Coordinate` to locate the coordinates in QGIS.
:::

:::{card}
__Report 18: Situation report from the NDMA liaison cell__
^^^
"Relief flights land at Moenjodaro Airport, Taluka Dokri. Goods are handed over at the cargo apron. Daily capacity: 2 C-130 flights."
:::

:::{dropdown} How to locate this report
- Search for "Moenjodaro Airport" with OSM Place Search. Note that the name is often also written "Mohenjo-daro".
- Find the apron (the area where the aircraft park) on the satellite basemap.
:::

## Task 2: Overview and reflection <a id="task-2-overview-and-reflection"></a>

1. Style the layer `damage_reports` by the field `category` ([Categorised styling](../Wiki/en_qgis_categorised_wiki.md)).
2. Put the flood extent below the reports and compare the locations of the reports with the flood extent.

`````{admonition} Question
Which reports were easy to locate, and which were difficult? Why?
`````

:::{dropdown} Answer
Reports with coordinates or links (e.g. reports 2, 7, 12) can be located quickly and precisely, as long as you know the order of latitude and longitude. Addresses and descriptions (e.g. reports 4, 9, 13, 15) need more interpretation: names are written differently, and descriptions like "approx. 1.8 km north" are not precise. Coordinates in other formats (UTM, DMS) are precise, but you need to know the format or the coordinate reference system.
:::

`````{admonition} Question
Which reports are located inside the flood extent? Does this match the content of the messages?
`````

:::{dropdown} Answer
Reports 3, 7, 10, 12, 13 and 15 are located inside the flood extent. Other locations, such as the health facilities, are outside the flood extent, but they are still affected: people from the flooded areas come to them, and water supply or access roads are interrupted. A flood extent from satellite data alone does not show the full impact.
:::

Congratulations! You have collected reports from many different sources and formats in one layer. This layer can now be used for the coordination meeting.
