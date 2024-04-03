# Geodata Classification



__🔙[Back to Homepage](/content/intro.md)__


Spatial data classification in GIS involves categorizing geographic information into distinct groups or classes based on shared characteristics. This process enhances the organization and interpretation of spatial data.

The attributes of geospatial data are stored in a specific column within the attribute table. Essentially, we choose a column containing the specific characteristics of interest, allowing QGIS to group the data based on these selected attributes.

```{figure} /fig/classification_basic.drawio.png
---
width: 900px
name: basic classification
align: center
---
Basic classification. Source:
```

## Single symbol classification

By default, QGIS visualizes all layers in the `Single symbol` setting. This means all the features of a layer are visualized the same. In this setting, you can change many parameters like colour or opacity __but you can not classify any data!__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>


__To adjust the style of a layer...__
1. Right-click on your layer.
2. Click on `Symbology`.
3. Confirm that the layer setting is on `Single Symbol`.
4. Select the colour of your choice in the drop-down menu. For more colour options select in the drop-down menu `Choose Color`.
5. *Optional*:. You can adjust the opacity/ transparency of the layer. This can be very useful when you want to show multiple overlapping layers.
6. *Optional*: Here you can set the unit type. This is useful when you want to visualize points in a certain size, for example.
7. *Optional:* Here you can find standard and previously used styles quickly.
8. Click `Apply` to put your adjustment into effect.
9.  Click `OK` to close the window.



```{figure} /fig/Single_symbol_classify.png
---
width: 900px
name: basic classification
align: center
---
Adjust the style of a layer.
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
1.  Right-click on your layer.
2. Click on `Symbology`.
3. Click on `Categorized`.
4. In the `Value` dropdown menu, select the column based on which you want to categorize your data.
5. Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected column in `Value`. To add or delete single values use the `-` and `+` buttons. 
6. *Optional*: In the `Symbol` dropdown menu, you can select the colours and symbols you want to use
7. *Optional*: In the `Color ramp` dropdown menu, you can specify the range of colours you want to use
8. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
9. Click `Apply` to put your adjustment into effect.
10. Click `OK` to close the window.


```{figure} /fig/Categorized_district_map_SierraLeone.png
---
name: Categorized classification
align: center
---
Categorized classification.
```

## Graduated classification

Graduated classification in GIS involves categorizing spatial data into classes or ranges based on a progression of values. This method is particularly useful for visualizing quantitative data, allowing for the differentiation of intensity, density, or magnitude across a spectrum, facilitating a nuanced representation of geographic phenomena.

### Graduated classification statistic one-o-one

Graduated classification is used for quantitative data usually __interval__ or __ratio__ scaled.

| Data Scale                  | Definition                                               | Example                     | Typical Data Format  |
|-----------------------------|----------------------------------------------------------|-----------------------------|----------------------|
| Interval Scale               | Equal intervals between values, no true zero point       | Temperature (Celsius)       | Float (44.5 Degree)                |
| Ratio Scale                  | Equal intervals with a true zero point                    | Population, Length, Number of trees          | Integer (5 Trees) or Float (12.5 km of Road)     |

To classify quantitative data there are many methods how to set up the classes. There is no single best way to select a method or to decide how many classes you like to use. It all comes down to what you want to show.

```{tip} 
A good range for number of classes is __3 to 7__. Do not use more than __9__ classes. 
```

Take the example below. You see a histogram of the district population. That means we have a dataset with districts and how many people living in each district. Just based on the histogram we can make a few general statements.

1. There are no districts with no or zero population
2. There are just a few districts with very low population
3. It seems that there are three general groups of districts

```{figure} /fig/Histogramm_example.drawio.svg
---
width: 900px
name: 
align: center
---
Histogramm of population data. Source:
```
However, if we want to show on a map which districts have a higher population than others, we need to classify the districts.


There are __seven__ ways in QGIS to split quantitative data into classes.  The four most important ones are: __Equal intervals__, __Quantile__, __Natural breaks__, __Manual__.
Let's have a look at how the classes of the district population would look like if we split the data into three classes using these methods.


```{figure} /fig/classification_method_map.drawio.svg
---
width: 900px
name:
align: center
---
Different classifications. Source:
```
::::{tab-set}

:::{tab-item} Equal Interval
Equal Interval classification divides data into uniform size classes, such as 0-10, 10-20, 20-30, and so on. It is effective for evenly distributed data across the entire range. However, caution is advised when data is skewed or has significant outliers, as this may result in empty classes. The population data used here, lacking large outliers, is suitable for Equal Interval classification.
:::

:::{tab-item} Equal Count (Quantile)
Quantiles classification ensures an equal number of observations in each class, creating visually appealing maps. However, it may result in classes with significantly different numerical ranges, and in some cases, similar rates may be separated while different rates are grouped together. It's advisable to use a histogram to assess potential issues. In the district population example, the quantile classification produced a questionable break, combining a portion of the third cluster with class 2 despite its closer numerical proximity to other observations in class 3.
:::

:::{tab-item} Natural Breaks
Natural Breaks is an optimal classification method that aims to minimize within-class variance and maximize between-class differences for a given number of classes. However, it produces a unique classification solution for each dataset, which can be a drawback when making comparisons across maps, such as in a series or atlas. In such cases, a consistent classification scheme applied across all maps might be preferable.
:::

:::{tab-item} Manual
Manual classification allows users to set one or all of the class breaks based on specific needs. This approach is useful when certain break points need to be predetermined, such as aligning with the mean or maintaining consistency across a series of maps. Manual classification is recommended when other methods provide a good solution but may benefit from slight adjustments to better suit specific requirements or visualizations.
:::

:::{tab-item} Logarithmic scale
Logarithmic scale classification is employed when the data spans multiple orders of magnitude, and a linear scale may not effectively represent the variations. This scale applies logarithmic transformation to the data, compressing larger values while expanding smaller ones. It is useful for visualizing data with exponential growth or decay. However, interpreting values on a logarithmic scale may require a nuanced understanding. Consider using a logarithmic scale when there is a wide range of values, and a linear scale may obscure important patterns or trends.
:::

:::{tab-item} Pretty Breaks
Pretty Breaks is a classification method designed to create visually appealing and easily interpretable maps. This approach seeks to generate class breaks that align with "round" numbers, making the map more intuitive for viewers. Pretty Breaks is particularly useful when communicating complex spatial data to a broad audience, as it enhances the clarity and understandability of the map. Keep in mind that the choice of 'pretty' breaks may depend on the specific context and the preferences of the intended audience."
:::

:::{tab-item} Standard Deviation
Standard Deviation classification is a method that determines class breaks based on the standard deviation of the data values. This approach organizes data into classes by considering the distribution of values around the mean. Each class represents a certain number of standard deviations from the mean, providing a statistical basis for categorizing data. Standard Deviation classification is effective when wanting to highlight variability within the dataset. However, it's important to consider the nature of the data distribution and whether this method aligns with the analytical goals of the map
:::

::::
___

### How to Graduated classification in QGIS

To perform a graduated classification in QGIS is easy. However, unlike the categorised classification, here you have to decide on how many classes and which method you want to use. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classification.mp4"></video>

__To classify data in classes…__
1.  Right-click on your layer.
2. Click on `Symbology`.
3. Click on `Graduated`.
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
Graduated classification. Source: 
```
9. *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use.
10. *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use. To see all color ramps click on the down arrow of the `Color ramp` -> `All Color Ramps`.
11. *Optional*: Under `Legend Format` you can adjust how precise the range of the classes will be displayed in the legend. Usually, it is practical to not use too complicated numbers in the legend.
12. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
13. Click `Apply` to put your adjustment into effect.
14. Click `OK` to close the window.



```{figure} /fig/classification_graduated_basic.png
---
width: 900px
name: raduated classification
align: center
---
Graduated calssification in QGIS.
```



