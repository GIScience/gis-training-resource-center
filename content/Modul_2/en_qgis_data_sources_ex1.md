# Data Sources Exercise 1

### Aim of the exercise
The objective of this exercise is to navigate different data sources, develop an understanding of where and how to access relevant data and what to look out for.

### Links to Wiki articles
will be done when Wiki is finished

### Data
Since the exercises aim is for you to find data, there won't be any data to download. Instead download the usual folder structure [here](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip) and add in your data.

### Tasks

We want to see how many hospitals are in Bolivia. 

1. Find a data source to download the administrative boundaries and the healthsites of Bolivia.

:::{dropdown} Examplary data sources
Try downloading the administrative boundaries on [OSM Boundaries](https://osm-boundaries.com) and the healthsites on [healthsites.io](https://healthsites.io).
:::

2. Download and save them as `bolivia` and `healthsides_bolivia` into the `data` - `input` folder. Only use points as healthsites.

3. Load both files into your QGIS.  

4. Optional: You can add the OpenStreetMap base map via the browser window --> XYZ Tiles. 

5. Get familiar with the data by opening the attribute table.

6. Filter the healthsites for hospitals.

```{Hint}
To filter by an expression check out this __[Wiki article on the attribute table](/content/Wiki/en_qgis_attribute_table_wiki.md)__
```

7. To only view the selected features (hospitals), export only selected features and save as `hospitals_bolivia` in your `data` - `output` folder.

8. As you can see, there are significantly less hospitals in the north and east of Bolivia.

8. Save your project.


### Result

```{figure} /fig/en_result_data_sources_exercise.png
---
width: 80%
name: en_result_data_sources_exercise
---
This is how your output could look like in the end
```