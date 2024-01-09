# Basic Raster operations

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Zonal statistics

The `Zonal Statistics` allows the combination of vector and raster data.

It calculates the statistics for each vector feature on the basis of the raster layer (see table below).



| Statistic              | Description                                     |
|------------------------|-------------------------------------------------|
| Count                  | Number of cells with valid values in each zone. |
| Sum                    | Total sum of values within each zone.           |
| Mean                   | Average value within each zone.                 |
| Median                 | Middle value in the distribution within zones.  |
| Standard Deviation     | Measure of the amount of variation or dispersion.|
| Minimum                | Lowest value within each zone.                   |
| Maximum                | Highest value within each zone.                  |
| Range                  | Difference between the maximum and minimum values.|
| Minority               | Least frequently occurring value within zones.  |
| Majority               | Most frequently occurring value within zones.   |
| Variety                | Number of unique values within each zone.        |
| Variance               | Measure of the spread of values within each zone.|





1.	Click `´Processing` -> `Toolbox` -> Search for `Zonal Statistics`
2.	`Input Layer`: Select your vector layer
3.	`Raster Layer`: Select your raster layer
4.	`Statistics to calculate`: Here you can select the statistic you want to calculate. For example the mean temperature of SPI.
5.	`Zonal Statistics`: Speficiy where you want to save the results and give it a good name.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zonal_stats.mp4"></video>




