# Task 2 - Access healthcare - avoid areas
For the main area of Kutupalong Refugee Camp, we have the boundary, the path and road network, water streams and health facilities. The boundary is available on `HDX`. Healthcare facilities, the road & path network, streams as well as the health facilities were extracted from `OpenStreetMap`. In this task we will compare openrouteservice isochrone and QGIS built-in service area catchments. Also we will showcase the avoid area feature in openrouteservice to account for a simple simulated flooding.

Use the following file:
* camp.gpkg

## STEP 1: Healthcare catchment - Isochrones

Open the **Processing Toolbox** and scroll down to **ORS Tools** choose **Isochrones** and **Isochrones from layer**. 
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Input Point layer            | camp_healthcare              |
| Travel mode                  | foot-walking                 |
| Comma separated ranges       | 5, 10                        |

:::{dropdown} Watch here:
VIDEO!
:::

## STEP 2: Healthcare catchment - QGIS Service area
Isochrones in QGIS can be generated via the service area tool in combination with the minimum bounding geometry tool. Based on a road network, we define origins, a default speed, and a maximum cost. 

Open the **Processing Toolbox**  and scroll down to **Network Analysis**, choose **Service area (from layer)**.
Leave all settings at default except:
|                                      |                                     |
|--------------------------------------|-------------------------------------|
| Vector layer representing network   | camp_ways                           |
| Vector layer with start points       | camp_healthcare                     |
| Path type to calculate               | fastest                             |
| Travel cost                          | 0.15 (~9 min.)                      |
| **Advanced Parameters**                  |                                     |
| Default speed                        | 5.0 (pedestrian)                    |
| Topology tolerance                   | 50.0                                |


:::{dropdown} Watch here:
VIDEO!
:::

QGIS on-the-fly creates a network graph from the road and path network. The graph is rather simple. All edges can be traveled in both ways, there are no weights included. Travel cost is represented by the length of a segment and the default average speed. The output is a simplification of the input road & path geometry but with the attributes of the healthcare facilities. For every healthcare facility we see a multiline geometry object in the output. We can style it according to the attribute “@osmId” to see which segments are assigned to which facility.

`````{admonition} Question
Can you already spot areas that are not reachable within 10 minutes by foot within
the camp?
`````
## STEP 3: Service area by minimum bounding box

In order to better compare the result of the service areas and isochrones we will again compute the minimum bounding geometry. But this time for the multiline output of the service area tool.

Open the **Processing Toolbox**, choose **Network Analysis**,then choose **Minimum Bounding Geometry**.
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Input layer                  | Service area (lines)         |
| Field                        | @osmId                       |
| Geometry type                | Convex Hull                  |

:::{dropdown} Watch here:
VIDEO!
:::

`````{admonition} Question
Compare the results of both catchments. What differences can you spot?
`````

## STEP 4: Healthcare catchment - Isochrones avoid flood
In this part we will again calculate catchments based on the same configured isochrones. But we will include a polygon for the avoid area functionality in openrouteservice. For the **avoid area** we will use the water streams that run through the main camp area. Make sure to buffer the camp_stream layer by 2 meters. The avoid areas function only allows for polygons, not for line geometries. If you have buffered the streams, go ahead with the Isochrones tool again.

Open the **Processing Toolbox** and scroll down to **ORS Tools** choose **Isochrones**  and  **Isochrones from layer**. 
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Travel mode                  | foot-walking                 |
| Input Point layer            | camp_healthcare              |
| **Advanced Parameters**         |                              |
| Polygons to avoid            | stream_buffer                |
| Comma separated ranges       | 5, 10                        |


:::{dropdown} Watch here:
VIDEO!
:::

`````{admonition} Question
Compare the output of the flooded isochrones with the isochrones from before. What differences are apparent for you?
`````
