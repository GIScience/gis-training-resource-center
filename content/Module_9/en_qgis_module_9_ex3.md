🚧 This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

# Task 3: Larger scale accessibility analyses

There are two main approaches on accessibility analyses: network and cost raster based. In this task we will use both methods on the example of the country Rwanda. For the network based approach we will use the isochrone API of the openrouteservice to generate catchment areas for 5, 10 and 60 minute ranges. The cost raster approach will be conducted with the saga tool `Accumulated Cost` which is already part of the QGIS tools through the SAGA provider. 


Download all datasets __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_9/Modul_9_Exercise_3_larger_scale_access_analysis/Modul_9_Exercise_3.zip)__. 
 Save the folder on your computer. 
 Unzip the .zip file. The unzipped folder is structured according to the recommended folder structure for QGIS projects. 
 Under "data > input" you find the following datasets:

**Vectorlayer**

- `task3.gpkg`
  - `rwa_healthcare` (points): Hospital locations in Rwanda (based of OpenStreetMap)
  - `rwa_adm0_boundary` (polygons): Country boundary of Rwanda
  - `rwa_adm1_boundary` (polygons): Administrative boundaries for the second level of Rwanda. In Rwandas case these are called provinces
  - `rwa_adm2_boundary` (polygons):  Third level administrative boundaries of Rwanda. In Rwandas case these are called prefectures


**Rasterlayer**

Use the following files:
- `motorized.tif` : Friction layer for motorized travel profiles
- `Walking.tif` : Friction layer for walking mobility profiles
- `population.tif` : Population counts from WorldPop
 
## STEP 1: Network - Isochrones
We start with the isochrones gain. This time for a whole country - Rwanda. Use the layer `rwa_healthcare` as input point layer and 5, 10 and 60 minutes as ranges.

Click in the toolbar on the ORS Tools plugin Icon <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/icon_ORS_tools_plugin.png" alt="Icon" width="20" height="20">. Click on `Batch Jobs` -> `Isochrones from Layer`.
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Travel mode                  | driving-car                  |
| Input Point layer            | rwa_healthcare               |
| Comma separated ranges       | 5, 10, 60                    |


:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task3_1.mp4"></video>
:::


## STEP 2: Raster - accumulated cost (Requires SAGA)

Open the `Processing Toolbox` and scroll down to `SAGA` choose `Raster Analysis` and then `Accumulated Cost` or enter "Accumulated Cost" in the search bar. 
Leave all settings at default except:
|                              |                              |
|------------------------------|------------------------------|
| Destinations                 | rwa_healthcare               |
| Destinations                 | motorized                    |
| Local Cost                   | motorized                    |


:::{dropdown} Watch here:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/modul_9_task3_2.mp4"></video>
:::

Select the `Accumulated Cost` output layer and open the `Layer styling panel (F7)` choose `Singleband Pseudocolor`. Adjust the range from a minimum of 0 to a maximum of 60 minutes. Overlay the isochrone output layer. Compare the different catchment areas. Add an OpenStreetMap background layer to better understand the differences. May consider dissolving **(Vector Geometry >> Dissolve)** the isochrone output layer by range value, to get a more clear outline of intersecting ranges in areas with multiple healthcare facilities.
Take a look at the Attribute table of the Isochrone output layer. One of the attributes bears information on the population living within the boundary of the isochrone. The population estimates are based on the Global Human Settlement Layer project. 

`````{admonition} Question
How many people are covered within 5, 10, 60 minutes in Rwanda according to our Analysis?
How would you describe the differences? 
What are the advantages/disadvantages of the raster versus the network approach?
`````

