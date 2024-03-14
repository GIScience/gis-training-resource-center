🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

# Task 1 - Assess water distribution access
For Camp 18 in Kutupalong Refugee Camp, we have a dataset on the locations of water distribution points. Further we have data on the buildings (footprint and centroid) within camp 18. In the following task we will use the following dataset:


Download all datasets __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_9/Modul_9_Exercise_1_Assess_water_distribution_access/Modul_9_Exercise_1.zip)__. 
 Save the folder on your computer. 
 Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. 
 Under "data > input" you find the geopackage file `task1.gpkg` which contains the following vector layers:

- `camp18_waterpoints` (points): Water point locations within camp 18 
- `camp18_buildings_centroid` (points): Centroids of all building objects inside camp 18
- `camp18_buildings_footprint` (polygons): Actual footprints of all buildings
- `camp18_boundary` (polygons): The camps legal boundary


## STEP 1: Catchments with openrouteservice isochrones
Make sure you installed the ORS Tools plugin and set it up already with an API Key. If not - see the how to here {ref}`content:references:module9:ors-tools-plugin`

Click in the toolbar on the ORS Tools plugin Icon <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/icon_ORS_tools_plugin.png" alt="Icon" width="20" height="20">. Click on `Batch Jobs` -> `Isochrones from Layer`. 
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Travel mode                   | foot-walking                   |
| Input Point Layer             | waterpoints                    |
| Dimension                     | distance                       |
| Comma separated ranges        | 500                            |


:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task1_1.mp4"></video>
:::


The result layer shows for every waterpoint a 500 meter catchment area for pedestrian travel mode. 500 meter is the maximum distance from any household to the water point according to [The Sphere Handbook: Humanitarian Charter and Minimum Standards in Humanitarian Response](https://spherestandards.org/wp-content/uploads/Sphere-Handbook-2018-EN.pdf) p. 106. There are other key indicators like maximum number of people using the facility, queuing time, etc. We will work on the distance as we miss further information like the flow rate per water point or the household size per building.

`````{admonition} Question
How is the coverage with water point catchments within camp 18? Any underserved areas?
`````

We proceed to find out how many water point options are there for each building given the 500m constraint. Basically we add a count aggregation of isochrones that intersect with each building.

Open the `Processing Toolbox` and scroll down to `Vector general` choose `Join attributes by location (summary)` or enter "Join attributes by location (summary)" in the search bar.
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Base Layer                     | buildings_centroid             |
| Join Layer                     | Isochrones                     |
| Geometric Predicate            | Intersects                     |
| Fields to Summarize            | ID                             |
| Summaries to Calculate         | count                          |

:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task1_2.mp4"></video>
:::

`````{admonition} Question
What is the min/max number of waterpoints available to the buildings in camp 18?
`````

## STEP 2: Catchments for operational facilities
Look into the attributes of the waterpoints layer. Filter for all waterpoints that are operational (search for `Extract by Attribute`). Redo the analysis for operational waterpoints only.

:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task1_3.mp4"></video>
:::

`````{admonition} Question
Is the general coverage different, any undersupplied areas?
What are the differences in the min/max number of waterpoints available to the buildings in camp 18 compared to using all waterpoints (non-operational, planned)
`````

## STEP 3: Waterpoint catchment by closest euclidean distance
There are other means to generate catchment areas, implemented in QGIS. In the next part we will use the hub distance to calculate the euclidean distance between every building and its closest waterpoint.

Open the `Processing Toolbox`, choose `Vector Analysis`,then choose `Distance to nearest hub (points)`or enter "Distance to nearest hub (points)" in the search bar.
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Source points                  | buildings_centroid             |
| Destination hubs layer         | waterpoints                    |
| Hub layer name attribute       | id_plastic                     |
| Measurement unit               | Meters                         |


:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task1_4.mp4"></video>
:::

The output layer has the same point geometry type like the input building_centroid layer. But it now features two attributes:
* HubName: The name/id of the closest waterpoint.
* HubDist: The euclidean distance from the building centroid to the closest waterpoint in meters.

`````{admonition} Question
What is the shortest / longest euclidean distance from a building to the closest waterpoint.
`````

## STEP 4: Hub distance based catchments

All buildings are assigned to their closest waterpoint. With the minimum bounding geometry tool in QGIS we can use this grouping information to create areas.

Open the `Processing Toolbox`, choose `Vector Analysis`, then choose `Minimum Bounding Geometry` or enter "Minimum Bounding Geometry" in the search bar.
Leave all settings at default except:

|                              |                              |
|------------------------------|------------------------------|
| Input layer                  | Hub distance                 |
| Field                        | Hubname                      |
| Geometry type                | Convex Hull                  |


:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task1_5.mp4"></video>
:::

`````{admonition} Question
  Have a close look at the hub distance based catchments. Can you tell that some buildings are quite far from a waterpoint when considering the paths connecting the two?
`````
