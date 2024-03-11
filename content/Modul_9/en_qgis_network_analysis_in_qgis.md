# Task 3: Approaches on accessibility analyses

There are two main approaches on accessibility analyses: network and cost raster based. In this task we will use both methods on the example of the country Rwanda. For the network based approach we will use the isochrone API of the openrouteservice to generate catchment areas for 5, 10 and 60 minute ranges. The cost raster approach will be conducted with the saga tool **Accumulated Cost** which is already part of the QGIS tools through the SAGA provider. 

Use the following files:
* rwa.gpkg
* motorized.tif
* Walking.tif
* population.tif

### STEP 1: Network - Isochrones
We start with the isochrones gain. This time for a whole country - Rwanda. Use the layer `rwa_healthcare` as input point layer and 5, 10 and 60 minutes as ranges.

Open the **Processing Toolbox** and scroll down to **ORS Tools** choose **Isochrones** and **Isochrones from layer**. 
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Travel mode                  | driving-car                  |
| Input Point layer            | rwa_healthcare               |
| Comma separated ranges       | 5, 10, 60                   |


:::{dropdown} Watch here:
VIDEO!
:::


### STEP 2: Raster - accumulated cost (Requires SAGA)

Open the **Processing Toolbox** and scroll down to **SAGA** choose **Raster Analysis** and then **Accumulated Cost**. 
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Destinations                 | rwa_healthcare               |
| Destinations                 | motorized                    |
| Local Cost                   | motorized                    |


:::{dropdown} Watch here:
VIDEO!
:::

Select the **Accumulated Cost** output layer and open the **Layer styling panel (F7)** choose **Singleband Pseudocolor**. Adjust the range from a minimum of 0 to a maximum of 60 minutes. Overlay the isochrone output layer. Compare the different catchment areas. Add an OpenStreetMap background layer to better understand the differences. May consider dissolving **(Vector Geometry >> Dissolve)** the isochrone output layer by range value, to get a more clear outline of intersecting ranges in areas with multiple healthcare facilities.
Take a look at the Attribute table of the Isochrone output layer. One of the attributes bears information on the population living within the boundary of the isochrone. The population estimates are based on the Global Human Settlement Layer project. 

`````{admonition} Question
How many people are covered within 5, 10, 60 minutes in Rwanda according to our Analysis?
How would you describe the differences? 
What are the advantages/disadvantages of the raster versus the network approach?
`````

https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/networkanalysis.html?highlight=network
