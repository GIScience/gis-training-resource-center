# Geodata Classification

**Data Styling/ Classification**

Data classification is the process that allows you to assign different symbols to features. i.e. different objects in the same layer based on their properties. This allows users of the map to quickly see the properties of numerous features.

In QGIS, a style is a way of cartographic visualization that takes into account a layer’s individual and thematic features. It encompasses basic characteristics of symbology, such as the color and presence of fill, outline parameters, the use of markers, scale-dependent rendering, layer transparency, and interactions with other layers. [Source](https://hub.packtpub.com/style-management-qgis/)

* To style or classify in Qgis, you must have an existing shapefile in your Qgis layer or upload the shapefile of the data you want to classify via Layer menu, then add layer, then add vector layer and under source botton, upload the shapefile that you intends to classify or style, then click ok and you can now see it in the layer panel. 
The picture below shows the Sierra Leone food insecurity 2015 shapefile that we can to classify in the layers pannel.

![](/fig/SierraLeone_shapefile_in_layer_pannel.png)

* Right click on the shapefile in the layer pannel and then property 

![](/fig/View_of_properties_from_layer_pannel.png)

* Then a layer properties will pump up. Click on symbology and select the type of classification or style that you want from circle 1.

![](/fig/Layer_properties.png)


* You can choose from single symbol, categorized and graduated in order to classify your data. Just next to it you will see color where you can choose color of your choice. At the bottom left-down, there is classify icon which allow you to classify different features in the layer to your choice. This classify icon can only work if you choose categorized or graduated style from up.

![](/fig/Style_selection.png)

* Below the syle option, you can also select the value, symbol and the color ramp that you want

![](/fig/Value_and_Symbol_selection.png)

* Once you click on classify, you can then now see all the classify features of your data. You can change the color of any of this categorized features by right click and go to change color and select any color that you want. Apply and click ok

![](/fig/Change_feature_color.png)

* The below screenshot shows the overview of the categorized map

![](/fig/Categorized_district_map_SierraLeone.png)




