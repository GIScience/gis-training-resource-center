# Graduated classification

Graduated classification in GIS involves categorizing spatial data into classes or ranges based on a progression of values. This method is particularly useful for visualizing quantitative data, allowing for the differentiation of intensity, density, or magnitude across a spectrum, facilitating a nuanced representation of geographic phenomena.

Graduated classification is used for quantitative data usually __interval__ or __ratio__ scaled.

| Data Scale                  | Definition                                               | Example                     | Typical Data Format  |
|-----------------------------|----------------------------------------------------------|-----------------------------|----------------------|
| Interval Scale               | Equal intervals between values, no true zero point       | Temperature (Celsius)       | Float (44.5 Degree)                |
| Ratio Scale                  | Equal intervals with a true zero point                    | Population, Length, Number of trees          | Integer (5 Trees) or Float (12.5 km of Road)     |

To classify quantitative data there are many methods how to set up the classes. There is no single best way to select a method or to decide how many classes you like to use. It all comes down to what you want to show.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Graduated_classification.mp4"></video>

__To classify data in classes…__
-  Right-click on your layer
- Click on `Symbology`
- Click on `Graduated`
- In the `Value` dropdown menu select the column based on which you want to classify your data.
- Downright select the number of classes you want to use.
- Under `Mode` select the classification method you want to use e.g. Equal count (Quantile).
- Click on `Classify`.  Now you should see all classes and the distribution of values. To add or delete single classes use the `-` and `+` buttons. 
- *Optional*: Click on `Histogram` -> `Load Values`. Now you can see the exact distribution of values over the classes. This is very practical to decide on a classification method. You can also check the mean value and standard deviation.
```{figure} /fig/Graduated_histogram.png
---
width: 900px
name: raduated classification
align: center
---
```
- *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use.
- *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use. To see all color ramps click on the down arrow of the `Color ramp` -> `All Color Ramps`.
- *Optional*: Under `Legend Format` you can adjust how precise the range of the classes will be displayed in the legend. Usually, it is practical to not use too complicated numbers in the legend.
- *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
- Click `Apply` to put your adjustment into effect.
- Click `OK` to close the window.

