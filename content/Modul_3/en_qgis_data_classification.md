# Geodata Classification

## Data Styling/ Classification

The process of data classification lets you give features distinct symbols. i.e., various things in the same layer according to their characteristics. **This makes it possible for users to view the qualities of many features on the map rapidly**. Cartographic visualization that considers the individual and thematic elements of each layer is called data style. **It includes fundamental symbology features including fill color and presence, outline parameters, marker use, scale-dependent rendering, transparency of layers, and interactions with other layers**.
 [Source](https://hub.packtpub.com/style-management-qgis/)


## Single symbol classification

This is the default rendering, where all of the features in a layer are displayed using a single symbol. Additionally, it lets you select a single style that will be used for all of the layer's characteristics. 

This video demonstrate a single symbol classification.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>

Additionally, the below screenshot shows the steps from number 1 to number 10 on how to classify data from the Layer menu.

![](/fig/Single_symbol_classify.png)


## Categorized classification

The discrete values of an attribute field that specify how each feature should be presented serve as the basis for categorized stylings. The layer's characteristics will display in various color tones according to distinct values in an attribute field. **Each category can have a different label, color, or symbol applied to it**, and QGIS will automatically divide your data into discrete groups.

This video demonstrate how the categorized classification can be done.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

The below screenshot shows the overview of the steps of the categorized classification.

![](/fig/Categorized_district_map_SierraLeone.png)


## Graduated classification

Graduated styles dictate how each feature should be presented based on continuous values in an attribute field. Your data will be automatically classified into intervals or classes by QGIS, allowing you to give a variety of symbols, colors, or sizes to each value. When you want to clearly distinguish between features with attribute values in various value ranges, graduated symbols come in handy. The GIS Application will analyze the attribute data (height, for example) and construct groups for you based on how many classes you require.

See the below video of graduated classes classification

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classification.mp4"></video>

* This screenshot shows the steps of graduated classification by classes. 

![](/fig/Graduated_classify_classes.png)

From **step 1** where you select graduated uptill **step 13** where you can see the classified outcome. You can play and change variables within the stages and use any parameter that suits your goal. 

More so, there is no single correct number of classes, there is no single best way to classify you data into ranges. To acheive the goal of classification, the data can be best classify by **equal interval, quantile, natural breaks and or manual** depending on what suits your purpose.

![](/fig/Classification_methods.PNG)

* Graduated classification by histogram

![](/fig/Graduated_classify_histogram.png)
You can show the mean value and standard deviation through this classification. 
See outlook of histogram by graduated classification.

![](/fig/Graduated_histogram.png)


See the video of graduated classes and histogram classification.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classes_histogram.mp4"></video>

