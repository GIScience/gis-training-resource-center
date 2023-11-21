# Data Classification

The attributes of geospatial data are stored in a specific column within the attribute table. 

## Single symbol classification

By default, QGIS visualizes all layers in the `Single symbol` setting. This means all the features of a layer are visualised the same. In this setting, you can change many parameters like colour or opacity __but you can not classify any data!__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>

__To adjust the style of a layer...__
1. Right-click on your layer
2. Click on `Symbology`
3. Confirm that the layer setting is on `Single Symbol`
4. Select the colour of your choice in the drop-down menu. For more colour options select in the drop-down menu `Choose Color`
5. *Optional*:. You can adjust the opacity/ transparency of the layer. This can be very useful when you want to show multiple overlapping layers.
6. *Optional*: Here you can set the unit type. This is usefull when you want for example visualize points in a certain size.
7. Optional. Here you can find standard and previously used styles quickly.
8. Click `Apply` to put your adjustment into effect.
9. Click `OK` to close the window.


```{figure} /fig/Single_symbol_classify.png
---
width: 900px
name: basic classification
align: center
---
```
## Categorized classification

Categorized classification in QGIS groups spatial data into distinct categories based on specific attributes. This classification enhances the organization and interpretation of geospatial information for clearer insights.

Categorized classification is usually used for __nominal__ and __ordinal__ scaled data.

| Data Scale | Definition| Example | Typical Data Format |
|---|---|---|---|
| Nominal Scale                | Categories without inherent order or ranking             | Land cover types, districts, livelihood zones | Text ("Desert") or Integer (5)      |
| Ordinal Scale                | Categories with a meaningful order or ranking            | Ranks (e.g., low, medium)   | Text ("high") or Integer (5)      |

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

__To classify data in categories…__
1.  Right-click on your layer
2. Click on `Symbology`
3. Click on `Categorized`
4. In the `Value` dropdown menu select the column based on which you want to categorize your data.
5. Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected column in `Value`. To add or delete single values use the `-` and `+` buttons. 
6. *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use
7. *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use
8. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
9. Click `Apply` to put your adjustment into effect.
10. Click `OK` to close the window.

```{figure} /fig/Categorized_district_map_SierraLeone.png
---
name: Categorized classification
align: center
---
```

## Graduated classification

Graduated classification in GIS involves categorizing spatial data into classes or ranges based on a progression of values. This method is particularly useful for visualizing quantitative data, allowing for the differentiation of intensity, density, or magnitude across a spectrum, facilitating a nuanced representation of geographic phenomena.

Graduated classification is used for quantitative data usually __interval__ or __ratio__ scaled.

| Data Scale                  | Definition                                               | Example                     | Typical Data Format  |
|-----------------------------|----------------------------------------------------------|-----------------------------|----------------------|
| Interval Scale               | Equal intervals between values, no true zero point       | Temperature (Celsius)       | Float (44.5 Degree)                |
| Ratio Scale                  | Equal intervals with a true zero point                    | Population, Length, Number of trees          | Integer (5 Trees) or Float (12.5 km of Road)     |

To classify quantitative data there are many methods how to set up the classes. There is no single best way to select a method or to decide how many classes you like to use. It all comes down to what you want to show.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classification.mp4"></video>

__To classify data in classes…__
1.  Right-click on your layer
2. Click on `Symbology`
3. Click on `Graduated`
 4. In the `Value` dropdown menu select the column based on which you want to classify your data.
5. Downright select the number of classes you want to use.
6. Under `Mode` select the classification method you want to use e.g. Equal count (Quantile).
7. Click on `Classify`.  Now you should see all classes and the distribution of values. To add or delete single classes use the `-` and `+` buttons. 
8. *Optional*: Click on `Histogram` -> `Load Values`. Now you can see the exact distribution of values over the classes. This is very practical to decide on a classification method. You can also check the mean value and standard deviation.
```{figure} /fig/Graduated_histogram.png
---
width: 900px
name: raduated classification
align: center
---
```
9. *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use.
10. *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use. To see all color ramps click on the down arrow of the `Color ramp` -> `All Color Ramps`.
11. *Optional*: Under `Legend Format` you can adjust how precise the range of the classes will be displayed in the legend. Usually, it is practical to not use too complicated numbers in the legend.
12. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
13. Click `Apply` to put your adjustment into effect.
14. Click `OK` to close the window.

