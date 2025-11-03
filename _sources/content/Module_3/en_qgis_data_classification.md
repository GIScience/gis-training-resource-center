::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Geodata Classification

Spatial data classification in GIS involves categorising geographic information into distinct groups or classes based on shared characteristics or attributes. Each class can be assigned a distinct symbol or colour. This process enhances the organization and interpretation of spatial data.

The attributes of  geodata are stored in a specific column within the attribute table. Essentially, we choose a column containing the specific characteristics of interest, allowing QGIS to group the data based on these selected attributes ({numref}`classification_basic`). 

```{figure} /fig/classification_basic.drawio.png
---
width: 900px
name: classification_basic
align: center
---
Basic classification (Source: HeiGIT).
```

## Nominal, Ordinal and Metric scales

In geographic data classification, __nominal__, __ordinal__, and __metric__ scales are used to categorize and measure spatial features based on different levels of precision and hierarchy:

::::{margin}
```{attention}

"Scales" in this context does not refer to the zoom level or ratio of measurements between the real world and the cartographic representation. It refers to the relations between the different data values. 

```
::::

- The __nominal scale__ (categorical data) is the simplest form of measurement where features are grouped into distinct categories based on qualitative attributes. These categories don't have any inherent order or ranking. They don't have any numerical significance: Values or labels are just names or identifiers (in some cases landcover classes can be identified with numbers).
    - Examples: Land cover classes, vegetation types, soil types, amenity type (hospital, church, school, etc.)

    ```{figure} /fig/nominal_scale_examples.png
    ---
    name: nominal_scale_example
    width: 600 px
    ---
    Examples for nominal data and their representation (Source: Dickmann (2018) Kartographie, Westermann).
    ```

- The __ordinal scale__ (ranked data) involves categorizing data, but in this case, the categories have a meaningful order or rank. However, the intervals between the ranks are not necessarily equal or known. Rank order is important: Features can be ranked or ordered from lowest to highest, but the actual difference between ranks isn't measured. You can compare and rank data (i.e., which feature is ranked higher or lower).
    - Examples: Land suitability, hierarchical road network, population size classes, vulnerability classes (e.g. for administrative units)

    ```{figure} /fig/ordinal_scale_example.png
    ---
    name: ordinal_scale_example
    width: 600 px
    ---
    Examples for ordinal data and their representation (Source: Dickmann (2018) Kartographie, Westermann)
    ```

- The __metric scale__ (quantitative data) deals with data that have both order and exact differences between values. Data is represented with precise numerical values and the differences between values are consistent across the scale. Metric data can be further divided into:
    - Interval scale: Numerical data where the difference between values is meaningful, but there is no true zero point (e.g., temperature in Celsius).
    - Ratio scale: Numerical data where both differences and ratios are meaningful, and there is a true zero point (e.g., distance, area).
    - Examples: Elevation data, distance, area, population data.

    ```{figure} /fig/interval_ratio_scale_example.png
    ---
    name: interval_scale_example
    width: 600 px
    ---
    Examples for metric data and their representation (Source: Dickmann (2018) Kartographie, Westermann).
    ```

Depending on the type of scale, you will use different methods of classification. Below, we will go over the different types of classification that are available in QGIS, and when to use them for which data. We will also go over some scenarios you might come across in your GIS career. 


## Single Symbol Classification

By default, QGIS visualises all layers in the `Single symbol` setting. This means all the features of a layer are visualised the same. In this setting, you can change many parameters like colour or opacity __but you can not classify the data into multiple groups!__

Single Symbol classification is useful when you have a simple dataset. For example, you load a polygon layer with the administrative boundaries of a region, and a point layer with the major cities. In this case, you can choose a single symbol classification and adjust the symbol for each layer.

:::{dropdown} How to: Single symbol classification
:open: 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>

__To adjust the style of a layer...__
1. Right-click on your layer.
2. Click on `Symbology`.
3. Confirm that the layer setting is on `Single Symbol`.
4. Select the colour of your choice in the drop-down menu. For more colour options select in the drop-down menu `Choose Color`.
5. *Optional*: You can adjust the opacity/transparency of the layer. This can be very useful when you want to show multiple overlapping layers.
6. *Optional*: Here you can set the unit type. This is useful when you want to visualise points in a certain size, for example.
7. *Optional:* Here you can find standard and previously used styles quickly.
8. Click `Apply` to put your adjustment into effect.
9.  Click `OK` to close the window.


```{figure} /fig/Single_symbol_classify.png
---
width: 900px
name: Single_symbol_classify
align: center
---
Adjusting the style of a layer.
```
:::


## Categorised Classification

Categorised classification in QGIS groups spatial data into distinct categories based on specific attributes. 

This classification organises the features into categories based on specific values in the attribute table.
By specifying a symbol to each category, you can facilitate the interpretation of geospatial information on your map for clearer insights.

```{figure} /fig/fr_simple_classification_example_map.png
---
name: fr_simple_classification_example_map
width: 750px
---
Niger – Régions de Tillabéri et de Tahoua Éducation: infrastructures scolaires fermées ou endommagées pour cause d'insécurité entre 2019 et 2022 (Source: [REACH](https://repository.impact-initiatives.org/document/impact/e6174a66/REACH_NER_Map_Ecoles_fermees_mai2022_tillaberi_tahoua.pdf)).
```

In the map above, the main roads have been assigned a single symbol. The schools have been classified into two categories: primary school (fr.: *école primaire*) and secondary school (fr.: *école secondaire*). 


Categorised classification is usually used for __nominal__ and __ordinal__ scaled data.

| Data Scale | Definition| Example | Typical Data Format |
|---|---|---|---|
| Nominal Scale                | Categories without inherent order or ranking             | Land cover types, districts, livelihood zones | Text ("Desert") or Integer (5)      |
| Ordinal Scale                | Categories with a meaningful order or ranking            | Ranks (e.g., low, medium)   | Text ("high") or Integer (5)      |

```{figure} /fig/Categorized_district_map_SierraLeone.png
---
width: 750 px
name: Categorized_district_map_SierraLeone
align: center
---
Example for a map using categorised classification.
```

:::{dropdown} How To: Categorised classificatation
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

__To classify data in categories…__
1.  Right-click on your layer.
2. Click on `Symbology`.
3. Click on `Categorized`.
4. In the `Value` dropdown menu, select the column based on which you want to categorise your data.
5. Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected column in `Value`. To add or delete single values use the `-` and `+` buttons. 
6. *Optional*: In the `Symbol` dropdown menu, you can select the colours and symbols you want to use.
7. *Optional*: In the `Color ramp` dropdown menu, you can specify the range of colours you want to use.
8. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/transparency of the layer.
9. Click `Apply` to put your adjustment into effect.
10. Click `OK` to close the window.

:::

## Graduated Classification

Graduated classification in GIS involves categorising spatial data into classes or ranges based on a progression of values. This method is particularly useful for visualising quantitative data, allowing for the differentiation of intensity, density, or magnitude across a spectrum, facilitating a nuanced representation of geographic phenomena. 

::::{card}

```{figure} /fig/example_classification_hexagons.png
---
name: example_classification_hexagons
width: 750 px
---
REACH, Ukraine, IDP Collective Site Monitoring Map, Actives, July 2024 (Source: [Reach](https://repository.impact-initiatives.org/document/impact/192097a8/REACH_UKR_Map_CSM_SituationOverview_ActiveSites_JULY2024_ENG_A4-1.pdf)).
```

In {numref}`example_classification_hexagons`, each hexagonal cell holds a value for "Number of sites per 150km²" ranging from 1 to 91. The cells have been organised into 5 categories, making it easy to distinguish between the different values in each cell. By keeping the amount of classes to a minimum, the reader can read and understand the map quicker. 

::::

Graduated classification is usually used for quantitative data that is __interval__ or __ratio__ scaled.

| Data Scale     | Definition                                         | Example                             | Typical Data Format                          |
|----------------|----------------------------------------------------|-------------------------------------|----------------------------------------------|
| Interval Scale | Equal intervals between values, no true zero point | Temperature (Celsius)               | Float (44.5 Degree)                          |
| Ratio Scale    | Equal intervals with a true zero point             | Population, Length, Number of trees | Integer (5 Trees) or Float (12.5 km of Road) |

To classify quantitative data there are many methods on how to set up the classes. There is no single best way to select a method or to decide how many classes you like to use. It all comes down to what you want to show.

```{tip} 
A good range for the number of classes is __3 to 7__. Do not use more than __9__ classes, as it becomes difficult to distinguish between the classes, making the map harder to understand. 
```

Take the example below. You see a histogram of the district population. That means we have a dataset with districts and how many people live in each district. Just based on the histogram we can make a few general statements.

1. There are no districts with no or zero population.
2. There are just a few districts with very low population.
3. It seems that there are three general groups of districts.

```{figure} /fig/Histogramm_example.drawio.svg
---
width: 900px 
align: center
name: Histogram_example.drawio
---
Histogram of population data. Source: [Axis Maps](https://www.axismaps.com/guide/data-classification).
```

However, if we want to show which districts have a higher population than others on a map, we need to classify the districts.

There are __seven__ ways in QGIS to split quantitative data into classes. The four most important ones are: __Equal intervals__, __Quantile__, __Natural breaks__, __Manual__.Let's have a look at how the classes of the district population would look like if we split the data into three classes using these methods.


```{figure} /fig/classification_method_map.drawio.svg
---
width: 900px
align: center
name: classification_method_map
---
Different classifications. Source: HeiGIT  (adapted from [Axis Maps](https://www.axismaps.com/guide/data-classification)) 
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
Manual classification allows users to set one or all of the class breaks based on specific needs. This approach is useful when certain break points need to be predetermined, such as aligning with the mean or maintaining consistency across a series of maps. Manual classification is recommended when other methods provide a good solution but may benefit from slight adjustments to better suit specific requirements or visualisation methods.
:::

:::{tab-item} Logarithmic scale
Logarithmic scale classification is employed when the data spans multiple orders of magnitude, and a linear scale may not effectively represent the variations. This scale applies logarithmic transformation to the data, compressing larger values while expanding smaller ones. It is useful for visualising data with exponential growth or decay. However, interpreting values on a logarithmic scale may require a nuanced understanding. Consider using a logarithmic scale when there is a wide range of values, and a linear scale may obscure important patterns or trends.
:::

:::{tab-item} Pretty Breaks
Pretty Breaks is a classification method designed to create visually appealing and easily interpretable maps. This approach seeks to generate class breaks that align with "round" numbers, making the map more intuitive for viewers. Pretty Breaks is particularly useful when communicating complex spatial data to a broad audience, as it enhances the clarity and understandability of the map. Keep in mind that the choice of 'pretty' breaks may depend on the specific context and the preferences of the intended audience.
:::

:::{tab-item} Standard Deviation
Standard Deviation classification is a method that determines class breaks based on the standard deviation of the data values. This approach organizes data into classes by considering the distribution of values around the mean. Each class represents a certain number of standard deviations from the mean, providing a statistical basis for categorising data. Standard Deviation classification is effective when wanting to highlight variability within the dataset. However, it's important to consider the nature of the data distribution and whether this method aligns with the analytical goals of the map.
:::

::::


:::{dropdown} How To: Graduated classification in QGIS
:open:

Setting up a graduated classification in QGIS is similar to setting up a categorised classification. However, unlike the categorised classification, here you have to decide on how many classes and which method of graduation you want to use. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/graduated_classification.mp4"></video>

__To classify data in classes…__
1.  Right-click on your layer.
2. Click on `Symbology`.
3. Click on `Graduated`.
4. In the `Value` dropdown menu select the column based on which you want to classify your data.
5. Downright select the number of classes you want to use.
6. Under `Mode` select the classification method you want to use e.g. Equal count (Quantile).
7. Click on `Classify`.  Now you should see all classes and the distribution of values. To add or delete classes use the `-` and `+` buttons. 
8. *Optional*: Click on `Histogram` -> `Load Values`. Now you can see the exact distribution of values over the classes. This is very practical to decide on a classification method. You can also check the mean value and standard deviation.

```{figure} /fig/Graduated_histogram.png
---
width: 900px
name: Graduated_histogram
align: center
---
Graduated classification. Source: [Axis Maps](https://www.axismaps.com/guide/data-classification).
```

9. *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use.
10. *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use. To see all color ramps click on the down arrow of the `Color ramp` -> `All Color Ramps`.
11. *Optional*: Under `Legend Format` you can adjust how precise the range of the classes will be displayed in the legend. Usually, it is practical to not use too complicated numbers in the legend.
12. *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/transparency of the layer.
13. Click `Apply` to put your adjustment into effect.
14. Click `OK` to close the window.

```{figure} /fig/classification_graduated_basic.png
---
width: 900px
name: classification_graduated_basic
align: center
---
Graduated classification in QGIS 3.36.
```
:::

## Self-Assessment Questions

::::{admonition} Check your knowledge
:class: note

1. __What is geodata classification, and why is it useful in GIS?__

:::{dropdown} Answer
- Geodata classification is the process of grouping or categorizing geographic data features by shared attribute values (or ranges), and then assigning each class its own symbol or colour.
- It helps in visualising patterns, making maps more interpretable, distinguishing differences in data, and communicating spatial variation more clearly (especially for quantitative or categorical attributes).
:::

2. __What are the three most common classification methods available in QGIS? Explain their differences.__

:::{dropdown} Answer
QGIS supports these three common classification modes:

| Method            | Use case / data type                                               | How it works / difference                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Single symbol** | For simple datasets or when you want all features to look the same | All features receive the same symbol (colour, size). No differentiation by attribute.                                                                                                                                                                |
| **Categorised**   | For **nominal** or **ordinal** (categorical) data                  | Features are grouped by unique attribute values (categories). Each category gets its own symbol.                                                                                                                                                     |
| **Graduated**     | For **quantitative / metric** data                                 | Numeric values are divided into numeric classes (ranges). Each class is symbolised differently (often by a ramp). You choose a number of classes and classification methods (e.g. equal interval, quantile, natural breaks). |



:::

3. __Name three different methods to divide quantitative data into classes. What are their differences?__

:::{dropdown} Answer
| Method                     | Description / how breaks are determined                                                                                    | Strengths & drawbacks                                                                                                                 |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Equal Interval**         | Divide the full range of data into intervals of equal size (e.g. dividing [min, max] into n equal-width bins)              | Straightforward and intuitive, but can lead to many empty or sparsely populated classes if data are skewed or have outliers.          |
| **Quantile (Equal Count)** | Each class gets (roughly) the same number of features (i.e. equal counts per class)                                        | Good visual balance—but the numerical ranges of classes may vary greatly, and similar values may be split across classes.             |
| **Natural Breaks (Jenks)** | Uses an algorithm to minimize within-class variance and maximize between-class differences (i.e. find “natural” groupings) | Often gives visually meaningful breaks tailored to the data distribution. But breaks depend on the dataset (less comparable across maps). |


:::

4. __What are the trade‑offs or challenges involved in choosing the number of classes in a graduated classification?__

:::{dropdown} Answer
- More classes = more detail, but too many makes the map confusing (hard to distinguish colours or subtle differences). The module suggests keeping classes between 3 and 7, and not more than 9.
- If classes are too few, you may oversimplify and mask important variation or extremes.
- If classes are too many, the map becomes cluttered, colours too similar, and it’s harder to interpret or compare.
- The distribution of the data matters: highly skewed data or outliers can distort class ranges, making most features fall into a few classes and leaving others nearly empty.
- For comparative maps (e.g. series of maps), using different breaks for each map (because the data differ) may reduce comparability; fixed breaks can help consistency but may not suit each dataset’s distribution equally.
:::

::::

