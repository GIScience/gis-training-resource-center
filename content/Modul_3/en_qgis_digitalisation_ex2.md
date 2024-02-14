# Digitization Exercise 2

## Aim of the exercise:

In this exercise, you will learn how to digitise point, line, and polygon layer of a position or feature in a settlements by creating new datasets. Additionally, you will learn how to name the simple layers created.

## How to create a point layer?
There is a new policy of Nigerian Naira Notes Redesign in Nigeria. The new policy became effective on the 26th of October, 2022 and it has caused many problems for the people of Nigeria not only in the business or health sector but in all works of life. See the article about how businesses groan as cash crunch hits Banks in Abuja, the capital city of Nigeria. [No cash article in Abuja](https://businessday.ng/news/article/business-groan-as-cash-crunch-hits-banks-in-abuja/).

Our goal is to create a point layers at the three Banks closed to each other in the Central Business District (CBD) of Abuja in Nigeria.This is to let people easily identify the banks in the CBD of Abuja for their transaction purposes. 

To this end, we will visualize the digitisation of the First Bank, Bank of Industrie Building and Zenith Bank Abuja. 

1.  Add the OSM as a base map. To add the OSM as a base map click on `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Choose `OpenStreetMap` and click `Add`. 
    Arrange your layer in the `Layer Panel` so the OSM is at the bottom ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html))

    ```{Tip}
    You can not interact with a base map!
    ```
2. To add the plugin `OSM Place Search`, click on `Plugins` -> `Manage and Install Plugins…` -> `All` and search for `OSM Place Search`. Once you have found it click on it and click `Install Plugin`. You can open the `OSM Place Search Panel` like every other panel by clicking on `View` -> `Panels` and checking `OSM Place Search Panel`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html#installation-of-plugins)).


3. In the panel, search Abuja via the OSM Place Search in QGIS and choose Abuja Municipality Area council, City. Zoom to the Central Business District and create a point on each of the three banks in the CBD of Abuja.

4. See [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#add-geometries-to-a-layer) for a guide.

This is how your result should look like. ![](/fig/Abuja_Banks_Point_Layers.png)

## How to create a line layer?
A business man named Mr John who droves all the way from the North of Herbert Macauley Way in the CBD of Abuja to do transaction at the Bank of Indusrie on Monday morning. Unfortunately, he found out that the network server of the bank is down and needed to proceed to the Zenith Bank as the only functioning Bank. He later discovered that there is an heavy road blocked at the junction of Indepence avenue and Tafawa Balewa way due to road construction. 

'Please' create a road line layer for Mr John that will allow him to get to Zenith Bank easily.

1.  See [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-line-data) for a guide.

This is how your result should look like.![](/fig/Abuja_Banks_Lines_Layers.png)

## How to create a polygon layer?

Now that you have created both point and line data. It is time to create a polygon layer.


Create a polygon layer covering the entire area of the First bank, Zenith bank and Industrie bank in the CBD of Abuja. 


1. See [wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_digitalization_wiki.html#creation-of-polygon-data) for a guide.

2.  Follow this step if you want to show the name of the data created.![](/fig/Show_label_name.png)


3. Right click on the data created on the layer panel, then click on show labels and the name of the data created will be showned either point, line or polygon data.


This is how your result should look like. ![](/fig/Abuja_Banks_Polygons_Layers.png)