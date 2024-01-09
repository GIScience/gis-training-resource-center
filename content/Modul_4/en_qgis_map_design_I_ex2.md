# Map design Exercise 1: Creating a Map of Ghana

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧


## Aim of the exercise

The aim of this exercise will be to create an overview map of Ghana with its subdistricts, main roads, settlements, as well as hospitals. Such information can always be of use in humanitarian work. The first part of the exercise will cover the symbolization of the data layers. The second part will focus on the design of the print layout.

## Data

It is always important to make yourself familiar with the data at your disposal. 
For this exercise, we will use the following layers:

- Ghana - Subnational Administrative Boundaries (https://data.humdata.org/dataset/cod-ab-gha)
- Ghana Health Facilities (OSM Export; https://data.humdata.org/dataset/hotosm_gha_health_facilities); This data has been cleaned up to only contain hospitals. 
- Ghana roads (OSM Export; https://data.humdata.org/dataset/hotosm_gha_roads)
- Ghana settlements (https://data.humdata.org/dataset/ghana-settlements); This data has already been modified. Only the regional, district and country capitals are available.

All data has been downloaded from the humanitarian data exchange. Download the Data from the Nexus, __unzip the folder__, and load the data into a new QGIS project.

## Wiki articles



## Tasks

### Preparation of the data

1. Look into the attribute table of the different layers and look what information is available and how the attributes are named.
2. We want to make a comprehensible map, think about which data we need and what data we can leave out. 
    - For example, the layer `hotosm_gha_roads_lines` contains too many roads for a map on a national scale. Let's open the attribute table and look at how the roads are classified. The data is using the conventional OpenStreetMap classification: The type of road is described under the attribute `highway`. In our case, it might be useful to only display the primary and secondary roads, so all the features where `highway=primary` OR `highway=secondary`.
    
### Symbolization

Now that we are familiar with the data at our disposal, let us start choosing the symbology for the different layers. Which information should be displayed on the map?

Let's start with the administrative boundaries. We want to show the names and outlines for the `adm_1`-layer, as well as the outlines for the `adm_2`-layer.

1. Put the layers for the administrative boundaries in an ascending order with `adm_0` at the bottom, followed by `adm_1` and `adm_2`
2. Open the __Symbology Tab__ for the `adm_2`-layer. Set the __Fill color__ to transparent and the __Stroke width__ to 0.16 Millimeters and the __Stroke style__ to a dashed line.
3. Open the __Symbology Tab__ for the `adm_1`-layer and set the colour as transparent. Leave the stroke width at 0,26 Millimeters and the stroke style as a solid line.
4.  Open the __Symboloy Tab__ for the `adm_0`-layer and set it to a neutral colour (such as a light gray).
5. We want to display the names of the districts. Open the __Labels Tab__ for the `adm_1`-layer. Select "Single Labels" and choose the attribute `ADM1_EN` for the values that are to be displayed.


Let's move on to the settlements.

The layer for the settlements has been cleaned up and only the towns, regional capitals, district capitals, and country capitals are available. 

1. Open the __Symbology Tab__ for the `gha_ppl_1m_NGA`-layer and select a categorized symbology.
2. Under "Value", select `popPlace1`
3. Click on "Classify"
4. A list of all the unique values will appear. Assign each a dark grey point marker. 
5. We want to be able to differentiate between country, regional, or district capital. The most important capital is the country capital, followed by regional capitals and finally the district capitals. Give each point marker a different size corresponding to its importance.
6. Let us add a label for the country capital and regional capitals next.
7. Navigate to the "__Label Tab__" and select __"Rule-based Labelling"__
8. Add a new rule and enter the following expression in the Filter: `(  "popPlace1"  =   'Country capital'  ) OR ( "popPlace1" = 'Regional capital' )`
9. Set the "Value" to `Name`.
10. Make the font italic and draw a text buffer in order to differentiate the settlement labels from the labels of the regions.

Let's move on to the road network.

1. The layer for the road network should sit on top of the administrative boundaries so the course and connections of roads is always visible. 
2. Open the __Symbology Tab__ for `hotosm_gha_roads_lines`. Select "__Rule-based__" and add a new filter by double clicking on `(no filter)`. 
3. Open the expression builder by clicking on the icon to the right of the filter option.
4. First, open a paranthese by double-clicking on `(`.
5. In the middle tab of the expression builder, expand the __"Fields and Values"__ list. Double click on `highway` to add it to the expression on your left. Next, on the right, click on `All Unique` to list all the possible values of that attribute.  
6.  Under the left window, click on the `=`-sign to add it to your expression.
7. In the list with all the unique values. Select `primary` and add it to your expression.
8. Close the parantheses by clicking on `)` under the expression field on the left. 
9. Add the Operator `OR` and repeat the same expression with the parantheses but select the unique value `secondary`
10. The finished expression should be  `(  "highway"  =  'primary' )  OR  ( "highway"  =  'secondary'  )`
11. Select a color and thickness for the line so it is distinguishable from the administrative boundaries (e.g. yellow; keep in mind that some colors have conventional associations; blue for water for example).

Now as a final touch, let's select a simble for the health facilities:

1. Open the __Symbology Tab__ and select the `Simple Marker`.
2. Under "Symbol Layer type", select SVG-Symbol.
3. Scroll down until you see the SVG-Symbol browser.
4. In the search bar, enter 'hospital'
5. Select one of the SVG-Symbols at your disposal
6. Adjust the color to red.
7. Click Apply and Ok.

Now we have assigned a symbol for each layer at our disposal. Look at the map you created and decide if you want to adjust any symbology to make the map easier to read. Do you need to change some colours? Are the layers ordered in a way that the information is available? Is the font size appropriate or do they cover up too much information?

Adding a basemap can help potential readers orienting themselves. 

1. Open the panel for QuickMapServices. The panel is called "Search QMS". If you have not installed the plugin yet, you can learn how to do it here `Link to BASEMAP WIKI ARTICLE!`
>Insert link
2. In the search field, search for OpenStreetMap.
3. Click add. A new layer will appear at the bottom of your layers.

Now the Map should be ready for a print layout.

### Creating the print layout

Once you are happy with the symbolization and colours of your data, the next step is to create a print layout. A map is never complete without adding the necessary elements such as 

1. Open a new print layout abd give it a name (e.g. Ghana Overview Map with hospitals)
2. Insert a new map
3. Move and position the map so that the entire country is visible at a reasonable scale
4. Add a title, scale bar, orientation, sources, author, and date. You may add additional text information to describe what can be seen on the map.
5. When you are happy with your print layout. You can export it as a PDF. You can save it in the project folder under "results".
6. Once you have exported the map. Look at the PDF and make sure it looks how you intended. Some things might look different in the PDF. If it does not look correct you may need to make some adjustments in the symbology.

The finished map could look something like this:

```{figure} ../../fig/en_map_design_exercise_1_results.pdf
---
name: Main road network and hospitals in Ghana, Africa
width: 600px
---
Some space has been left in the bottom-right corner for an overview map
```

What can we learn from this map? We can clearly identify areas that are harder to reach and where the travel time to a hospital is much longer than in the populated regions in southern Ghana. 

### Bonus Exercise!

If you are finished with the main map, click on the map and navigate to the item properties. In the layer section, check the box `Lock Layers`. Now you can start working on an overview map. 

- 