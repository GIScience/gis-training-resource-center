# Geodata Classification

## Data Styling/ Classification

Data classification is the process that allows you to assign different symbols to features. i.e. different objects in the same layer based on their properties. This allows users of the map to quickly see the properties of numerous features.

In QGIS, a style is a way of cartographic visualization that takes into account a layer’s individual and thematic features. It encompasses basic characteristics of symbology, such as the color and presence of fill, outline parameters, the use of markers, scale-dependent rendering, layer transparency, and interactions with other layers. [Source](https://hub.packtpub.com/style-management-qgis/)


## The Goal of Data Classification

The basic goal of a classification scheme is to group together similar observations and split apart observations that are substantially different. In more technical terms, the goal is to find the optimal number of classes and where to put the breaks between those classes so as to minimize within group variance and maximize between group differences. For instance, if I had a data set with 4 observations of 1.3, 1.6, 3.5 and 3.9, many folks would be inclined to split those observations into 2 groups with 1.3 and 1.6 in the first group and 3.5 and 3.9 in the second because that pairing makes sense given the large numerical gap in the middle of the data range. Such an approach is common and is called “maximum breaks.”

However, there are often other considerations when classifying our data and simply maximizing between group differences may not be the primary goal: In the example above, it might be possible that 1.5 is a critical value and all that matters is to distinguish between locations above and below that critical break point (e.g., if a location has a reading below 1.5 they might be eligible for emergency funding). In this case, external constraints over-ride our mathematical solutions and despite being fairly close together 1.3 and 1.6 would now be placed in different classes since they straddle that breakpoint.

```{Note} 
Remember:
```

If you are going to classify your data you must decide both the number of classes and the method for breaking your data into ranges.

[Source](https://www.axismaps.com/guide/data-classification)


## Importance of data classification

Data Classification is used to group a large number of observations into data ranges or classes. It is a useful tool to structure the data for choropleth maps automatically and it helps to reduce the information content. It allows to make the presentation of values much clearer. Individual observations are lost, small differences can be reduced and large ones can be emphasized and evaluated better. Distributional characteristics and the psychology of perception are taken into account. [Source](https://cartography-playground.gitlab.io/playgrounds/data-classification-methods/)

## How to classify data?

To style or classify in Qgis, you must have an existing shapefile in your Qgis layer or upload the shapefile of the data you want to classify via Layer menu, then add layer, then add vector layer and under source botton, upload the shapefile that you intends to classify or style, then click ok and you can now see it in the layer panel. 
The picture below shows the Sierra Leone food insecurity 2015 shapefile that we can to classify in the layers pannel.

![](/fig/SierraLeone_shapefile_in_layer_pannel.png)

* Right click on the shapefile in the layer pannel and then property 

![](/fig/View_of_properties_from_layer_pannel.png)

* Then a layer properties will pump up. Click on symbology and select the type of classification or style that you want from circle 1.

![](/fig/Layer_properties.png)


* Additionally, you can choose from single symbol, categorized and graduated in order to classify your data. Just next to it you will see color where you can choose color of your choice. At the bottom left-down, there is classify icon which allow you to classify different features in the layer to your choice. This classify icon can only work if you choose categorized or graduated style from up.

![](/fig/Style_selection.png)

* Below the syle option, you can also select the value, symbol and the color ramp that you want

![](/fig/Value_and_Symbol_selection.png)

* Once you click on classify, you can then now see all the classify features of your data. You can change the color of any of this categorized features by right click and go to change color and select any color that you want. Apply and click ok

![](/fig/Change_feature_color.png)


### Categorized classification

* The below screenshot shows the overview of the categorized map

![](/fig/Categorized_district_map_SierraLeone.png)

See video of classification by categorized

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>


### Graduated classification

Graduated styles are based on continuous values of an attribute field that define how each feature should be rendered. You can assign a range of symbols, colors, or sizes to each value, and QGIS will automatically classify your data into intervals or classes. Graduated symbols are most useful when you want to show clear differences between features with attribute values in different value ranges. The GIS Application will analyse the attribute data (e.g. height) and, based on the number of classes you request, create groupings for you.

See the below video of graduated classes classification

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classification.mp4"></video>

