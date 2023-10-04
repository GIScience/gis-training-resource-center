# Geodata concept

**Competences:**
* Projections
* Layer concept
* Vector and raster data (basic concepts)
* Vector file formats





## Projections 
### Theory

The earth is a sphere and cannot be represented on a flat map without being distorted. To able able to display the earth on a flat map for example as a rectangle it needs to be projected. For further explanation, watch this [video](https://www.youtube.com/watch?v=kIID5FDi2JQ). 

For this translation, from a curved on a flat surface, thousands of different methods exist. These are called **Coordinate Reference Systems (CRS)**.

![Different Coordinate Reference Systems](../../fig/en_examples_projections.png)

Every projection comes with a trade-off in shape, direction, distance and area. That's why it is important to choose different types of CRS for different use cases.
For example, Mercator projections don´t represent the area correctly. Google Maps still uses the Mercator to be able to represent streets correctly, since it works well on a small scale. On a big scale, the shape of the countries stay the same but the area is mispresented. You can check the true size in comparison to different placements on the map on this [website](https://www.thetruesize.com). A popular example is Greenland in comparison with Africa, which seem on the map to be about the same size, but in reality Africa is a lot bigger.

![Comparison Greenland - Africa](../../fig/en_greenland_africa.png)

It's important to work with the right projections, if not we will produce wrong results!

This table shows an overview on which projections to use for which needed characteristic:

| Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :--------------------: | :-----------------: | :----------: |
| [x] shape              | [ ] shape           | [x] shape    |
| [x] rotation           | [x] rotation        | [ ] rotation |
| [ ] area               | [x] area            | [x] area     |

For smaller areas local projections should be used, since they give a more accurate display at the expense of more distortion at the global level. 

![Local Coordinate Reference Systems](../../fig/en_local_crs.png)

### Application

You can find all the projections and their CRS code at this [website](http://epsg.io). 


To change the projection of a **vector file**, click on *Vector*, *Data Management Tools*, *Reproject Layer*. Select your input layer and the target crs. Click on the three dots to *Save to File...* and click *Run*. For a detailed instruction click on this [video](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/7e7a28698859062d1b832b558b2721c6/qgis_reproject_vector.mp4).

To change the projection of a **raster file**, clickclick on *Raster*, *Projections*, *Warp (Reproject)*. Choose your input layer and target crs. Click on the three dots to *Save to File...* and click *Run*. For a detailed instruction click on this [video](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/3b7a1bb2408f4453f22d73f54156888b/qgis_reproject_raster.mp4).

It is crucial that you are aware of the difference in data projection and project projection. They should always be the same, or else you will get wrong results! You can change the data projection by following the steps explained above. The project projection is on the bottom left corner, as seen [here](../../fig/en_QGIS_User_Interface.png). The interface then will be the same and by searching for the right EPSG you can change the projection. 

## Excercises

Now it's your turn! 

You can apply your knowledge on this excercise by getting used to the interface and changing the projections. 

[Exercise 1](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/tree/main/Exercise_1) 
--> in future link to HeiCloud



==explain and show often made mistakes?==

This [Website](https://ihatecoordinatesystems.com/) provides explanations und solutions for often made mistakes.

In the [Wiki](../../content/Wiki/en_qgis_projections_wiki.md) are further tips.




## Layer concept



## Vector and raster data


## Vector file formats





