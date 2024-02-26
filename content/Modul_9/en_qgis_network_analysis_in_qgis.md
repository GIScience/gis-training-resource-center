# Network Analysis in QGIS

## Task 1 - assess water distribution access
For Camp 18 in Kutupalong Refugee Camp, we have a dataset on the locations of water distribution points. Further we have data on the buildings (footprint and centroid) within camp 18. In the following task we will use the following dataset:
* Camp18.gpkg

### Catchments with openrouteservice isochrones
Make sure you installed the ORS Tools plugin and set it up already with an API Key. If not, consult Openrouteservice & QGIS Plugin before proceeding.
Hier Tabelle!
The result layer shows for every waterpoint a 500m catchment area for pedestrian travel mode. 500m is the maximum distance from any household to the water point according to `The Sphere Handbook: Humanitarian Charter and Minimum Standards in Humanitarian Response` p. 106. There are other key indicators like maximum number of people using the facility, queuing time, etc. We will work on the distance as we miss further information like the flow rate per water point or the household size per building.

:::{exercise}
How is the coverage with water point catchments within camp 18? Any underserved areas?
:::

We proceed to find out how many water point options are there for each building given the 500m constraint. Basically we add a count aggregation of isochrones that intersect with each building.

:::{exercise}
What is the min/max number of waterpoints available to the buildings in camp 18?
:::

### Catchments for operational facilities
Look into the attributes of the waterpoints layer. Filter for all waterpoints that are operational (`Extract by Attribute`). Redo the analysis for operational waterpoints only.

:::{exercise}
Is the general coverage different, any undersupplied areas?
What are the differences in the min/max number of waterpoints available to the buildings in camp 18 compared to using all waterpoints (non-operational, planned)
:::

### Waterpoint catchment by closest euclidean distance
There are other means to generate catchment areas, implemented in QGIS. In the next part we will use the hub distance to calculate the euclidean distance between every building and its closest waterpoint.

:::{dropdown} Watch here:
TABELLE!
:::
The output layer has the same point geometry type like the input building_centroid layer. But it now features two attributes:
* HubName: The name/id of the closest waterpoint.
* HubDist: The euclidean distance from the building centroid to the closest waterpoint in meters.

:::{exercise}
What is the shortest / longest euclidean distance from a building to the closest waterpoint.
:::

All buildings are assigned to their closest waterpoint. With the minimum bounding geometry tool in QGIS we can use this grouping information to create areas from.

:::{dropdown} Watch here:
TABELLE!
:::
:::{exercise}
  Have a close look at the hub distance based catchments. Can you tell that some buildings are quite far from a waterpoint when considering the paths connecting the two?
:::


## Task 2 - access healthcare - avoid areas
For the main area of Kutupalong Refugee Camp, we have the boundary, the path and road network, water streams and health facilities. The boundary is available on `HDX`. Healthcare facilities, the road & path network, streams as well as the health facilities were extracted from `OpenStreetMap`. In this task we will compare openrouteservice isochrone and QGIS built-in service area catchments. Also we will showcase the avoid area feature in openrouteservice to account for a simple simulated flooding.

Use the following file:
* camp.gpkg

### Healthcare catchment - Isochrones

:::{dropdown} Watch here:
TABELLE!
:::
### Healthcare catchment - QGIS Service area
Isochrones in QGIS can be generated via the service area tool in combination with the minimum bounding geometry tool. Based on a road network, we define origins, a default speed, and a maximum cost. 

:::{dropdown} Watch here:
TABELLE!
:::
QGIS on-the-fly creates a network graph from the road and path network. The graph is rather simple. All edges can be traveled in both ways, there are no weights included. Travel cost is represented by the length of a segment and the default average speed. The output is a simplification of the input road & path geometry but with the attributes of the healthcare facilities. For every healthcare facility we see a multiline geometry object in the output. We can style it according to the attribute “@osmId” to see which segments are assigned to which facility.

:::{exercise}
Can you already spot areas that are not reachable within 10 minutes by foot within
the camp?
:::

In order to better compare the result of the service areas and isochrones we will again compute the minimum bounding geometry. But this time for the multiline output of the service area tool.

:::{exercise}
Compare the results of both catchments. What differences can you spot?
:::

### Healthcare catchment - Isochrones avoid flood
In this part we will again calculate catchments based on the same configured isochrones. But we will include a polygon for the avoid area functionality in openrouteservice. For the **avoid area** we will use the water streams that run through the main camp area. Make sure to buffer the camp_stream layer by 2 meters. The avoid areas function only allows for polygons, not for line geometries. If you have buffered the streams, go ahead with the Isochrones tool again.

:::{dropdown} Watch here:
TABELLE!
:::
:::{exercise}
Compare the output of the flooded isochrones with the isochrones from before. What differences are apparent for you?
:::

## Task 3 - approaches on accessibility analyses
There are two main approaches on accessibility analyses: network and cost raster based. In this task we will use both methods on the example of the country Rwanda. For the network based approach we will use the isochrone API of the openrouteservice to generate catchment areas for 5, 10 and 60 minute ranges. The cost raster approach will be conducted with the saga tool **Accumulated Cost** which is already part of the QGIS tools through the SAGA provider. 

Use the following files:
* rwa.gpkg
* motorized.tif
* Walking.tif
* population.tif

### Network - Isochrones
We start with the isochrones gain. This time for a whole country - Rwanda. Use the layer `rwa_healthcare` as input point layer and 5, 10 and 60 minutes as ranges.

:::{dropdown} Watch here:
TABELLE!
:::
### Raster - accumulated cost
`https://saga-gis.sourceforge.io/saga_tool_doc/6.1.0/grid_analysis_0.html`

:::{dropdown} Watch here:
TABELLE!
:::
Select the **Accumulated Cost** output layer and open the **Layer styling panel (F7)** choose **Singleband Pseudocolor**. Adjust the range from a minimum of 0 to a maximum of 60 minutes. Overlay the isochrone output layer. Compare the different catchment areas. Add an OpenStreetMap background layer to better understand the differences. May consider dissolving **(Vector Geometry >> Dissolve)** the isochrone output layer by range value, to get a more clear outline of intersecting ranges in areas with multiple healthcare facilities.
Take a look at the Attribute table of the Isochrone output layer. One of the attributes bears information on the population living within the boundary of the isochrone. The population estimates are based on the Global Human Settlement Layer project. 

:::{exercise}
How many people are covered within 5, 10, 60 minutes in Rwanda according to our Analysis?
How would you describe the differences? 
What are the advantages/disadvantages of the raster versus the network approach?
:::


https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/networkanalysis.html?highlight=network
