# Task 1 - Assess water distribution access
For Camp 18 in Kutupalong Refugee Camp, we have a dataset on the locations of water distribution points. Further we have data on the buildings (footprint and centroid) within camp 18. In the following task we will use the following dataset:
* Camp18.gpkg

## STEP 1: Catchments with openrouteservice isochrones
Make sure you installed the ORS Tools plugin and set it up already with an API Key. If not, consult Openrouteservice & QGIS Plugin before proceeding.

Open the **Processing Toolbox** and scroll down to **ORS Tools** choose **Isochrones** and **Isochrones from layer**. 
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Input Point Layer             | waterpoints                    |
| Travel mode                   | foot-walking                   |
| Dimension                     | distance                       |
| Comma separated ranges        | 500                            |


:::{dropdown} Watch here:
VIDEO
:::


The result layer shows for every waterpoint a 500m catchment area for pedestrian travel mode. 500m is the maximum distance from any household to the water point according to `The Sphere Handbook: Humanitarian Charter and Minimum Standards in Humanitarian Response` p. 106. There are other key indicators like maximum number of people using the facility, queuing time, etc. We will work on the distance as we miss further information like the flow rate per water point or the household size per building.

`````{admonition} Question
How is the coverage with water point catchments within camp 18? Any underserved areas?
`````

We proceed to find out how many water point options are there for each building given the 500m constraint. Basically we add a count aggregation of isochrones that intersect with each building.

Open the **Processing Toolbox** and scroll down to **Vector general** choose **Join attributes by location (summary)**.
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Base Layer                     | buildings_centroid             |
| Join Layer                     | Isochrones                     |
| Geometric Predicate            | Intersects                     |
| Fields to Summarize            | ID                             |
| Summaries to Calculate         | count                          |

:::{dropdown} Watch here:
VIDEO
:::

`````{admonition} Question
What is the min/max number of waterpoints available to the buildings in camp 18?
`````

## STEP 2: Catchments for operational facilities
Look into the attributes of the waterpoints layer. Filter for all waterpoints that are operational (`Extract by Attribute`). Redo the analysis for operational waterpoints only.

`````{admonition} Question
Is the general coverage different, any undersupplied areas?
What are the differences in the min/max number of waterpoints available to the buildings in camp 18 compared to using all waterpoints (non-operational, planned)
`````

## STEP 3: Waterpoint catchment by closest euclidean distance
There are other means to generate catchment areas, implemented in QGIS. In the next part we will use the hub distance to calculate the euclidean distance between every building and its closest waterpoint.

Open the **Processing Toolbox**, choose **Vector Analysis**,then choose **Distance to nearest hub (points)** [docs.qgis]
Leave all settings at default except:

|                                |                                |
|--------------------------------|--------------------------------|
| Source points                  | buildings_centroid             |
| Destination hubs layer         | waterpoints                    |
| Hub layer name attribute       | id_plastic                     |
| Measurement unit               | Meters                         |


:::{dropdown} Watch here:
VIDEO!
:::

The output layer has the same point geometry type like the input building_centroid layer. But it now features two attributes:
* HubName: The name/id of the closest waterpoint.
* HubDist: The euclidean distance from the building centroid to the closest waterpoint in meters.

`````{admonition} Question
What is the shortest / longest euclidean distance from a building to the closest waterpoint.
`````

## STEP 4: Hub distance based catchments

All buildings are assigned to their closest waterpoint. With the minimum bounding geometry tool in QGIS we can use this grouping information to create areas from.

Open the **Processing Toolbox**, choose **Vector Analysis**,then choose **Minimum Bounding Geometry** [docs.qgis]
Leave all settings at default except:

|                              |                              |
|------------------------------|------------------------------|
| Input layer                  | Hub distance                 |
| Field                        | Hubname                      |
| Geometry type                | Convex Hull                  |


:::{dropdown} Watch here:
VIDEO!
:::

`````{admonition} Question
  Have a close look at the hub distance based catchments. Can you tell that some buildings are quite far from a waterpoint when considering the paths connecting the two?
`````
