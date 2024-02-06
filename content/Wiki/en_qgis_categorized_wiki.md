## Categorized classification

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

__🔙[Back to Homepage](/content/intro.md)__

Categorized classification in QGIS groups spatial data into distinct categories based on specific attributes. This classification enhances the organization and interpretation of geospatial information for clearer insights.

Categorized classification is usually used for __nominal__ and __ordinal__ scaled data.

| Data Scale | Definition| Example | Typical Data Format |
|---|---|---|---|
| Nominal Scale                | Categories without inherent order or ranking             | Land cover types, districts, livelihood zones | Text ("Desert") or Integer (5)      |
| Ordinal Scale                | Categories with a meaningful order or ranking            | Ranks (e.g., low, medium)   | Text ("high") or Integer (5)      |

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

__To classify data in categories…__
- Right-click on your layer
- Click on `Symbology`
- Click on `Categorized`
- In the `Value` dropdown menu select the column based on which you want to categorize your data.
- Further down the window click on `Classify`.  Now you should see all unique values or attributes of the selected column in `Value`. To add or delete single values use the `-` and `+` buttons. 
- *Optional*: In the `Symbol` dropdown menu you can select the colours and symbols you want to use
- *Optional*: In the `Color ramp` dropdown menu you can specify the range of colours you want to use
- *Optional*: You can open the panel `Layer Rendering` on the button of the window. Here you can adjust the opacity/ transparency of the layer.
- Click `Apply` to put your adjustment into effect.
- Click `OK` to close the window.

```{figure} /fig/Categorized_district_map_SierraLeone.png
---
name: Categorized classification
align: center
---
```
