::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
:link-type: doc
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Mapping Typhoon Uwan’s Exposure – Operational Maps and a Province Atlas <a id="mapping-typhoon-uwan-exposure"></a>

## Characteristics of the exercise <a id="characteristics-of-the-exercise"></a>

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training.
- It can be done as a follow-along exercise or individually as a self-study.
- It works well as a scenario exercise: participants play the GIS team of a National Society in the first days of a typhoon emergency.

:::

:::{grid-item-card}
__Focus Group__
^^^

This exercise is aimed at IM personnel with intermediate QGIS skills. It is useful for Anticipatory Action analyses and disaster impact assessments. 

:::

::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise__
^^^

3 hours

:::

:::{grid-item-card}
__Relevant Wiki Articles__
^^^

* [Installing plugins](../Wiki/en_qgis_plugins_wiki.md#installation-of-plugins)
* [Basemaps from QuickMapServices](../Wiki/en_qgis_basemaps_wiki.md#basemaps-from-quickmapservices-plugin)
* [Layer concept](../Wiki/en_qgis_layer_concept_wiki.md)
* [Graduated classification](../Wiki/en_qgis_graduated_wiki.md)
* [Loading a style](en_qgis_working_with_styles.md#loading-a-style-into-a-qgis-project) (Module 4)
* [Rule-based labelling](en_qgis_labels_vector.md#rule-based-labelling) (Module 4)
* [Print Layout Composer](en_qgis_understanding_print_layout.md) (Module 4)
* [The Atlas function](en_qgis_understanding_print_layout.md#the-atlas-function-automatic-map-generation) (Module 4)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Aim of the exercise:__
In this exercise you will turn the results of the previous exercise into maps for the operations team. You will load prepared style files, use rule-based labels to highlight the provinces exposed to Typhoon Uwan (Fung-wong, November 2025), and generate an atlas with the print layout that creates a detailed map with the exposed population and hospitals for every exposed province.
^^^

:::

## Instructions for the trainers <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Trainers Corner__

### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material. Run through all tasks once yourself and export the atlas, so you can show participants what the result should look like.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions.
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Installing the QuickMapServices plugin requires an internet connection. Check beforehand that participants can install plugins on their computers (some organisations restrict this).
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md) for some general tips on facilitating trainings.

### Conduct the training <a id="conduct-the-training"></a>

__Introduction:__

- Briefly recap the previous exercise: which provinces were exposed to Typhoon Uwan, and how did we calculate the exposed population?
- Before opening QGIS, ask the group:
    - Who in the operation will use our maps, and what do they need to see at a glance?
    - Which information should be on a map for a single province, and which on an overview map?
    - Which maps have you seen in situation reports or from other organisations? What made them easy or hard to read?

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project.
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.
- Rule-based labels and atlas expressions are new for most participants. Take your time to explain what an expression is and where the expression editor can be found.
- Rendering the atlas pages can be slow on older laptops. Ask participants to switch off the atlas preview while they arrange the layout, and to turn it on only to check the pages.
- Faster participants can continue with the "Going further" dropdowns at the end of Task 3 while you support the others.

__Wrap up:__

- Use the questions in the [Discussion](#discussion) section.
- Point out that the atlas can be reused: when a new forecast or new data comes in, participants only need to update the layers and export the atlas again.
- Leave some time for open questions.

:::


## Available data 

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/module_5/module_5_phl_typhoon_ex_1.zip

__Download all datasets here, save the folder on your computer and unzip the file.__

:::

The folder contains the whole [standard folder structure](../Wiki/en_qgis_projects_folder_structure_wiki.md#standard-folder-structure) with all data in the input folder and the additional documentation in the documentation folder.

:::{note} Data from the previous exercise
This exercise is part of the Philippines cyclone impact exercise track and builds on [this exercise](../Module_5/en_qgis_module_5_phl_uwan_ex_1.md). The easiest way to do this exercise is by using the same QGIS project as for the last exercise. Simply drag the new datasets into your folder structure for the previous exercise. 

:::

| Dataset                             | File                                                                                       | Source                                                                                                                                                                                   | Description                                                                                                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Storm track of Typhoon Uwan         | `/data/interim/cyclone_track_uwan.gpkg`                                                    | [IBTrACS](https://www.ncei.noaa.gov/products/international-best-track-archive), prepared in the previous exercise                                                                        | The track of Typhoon Uwan (Fung-wong) as line segments. Each segment contains the time (`ISO_TIME`) and the wind speed reported by the different agencies.                                         |
| 200 km buffer                       | `/data/interim/Cyclone_Uwan_200km_buffer.gpkg`                                             | Result of the previous exercise                                                                                                                                                          | The area within 200 km of the storm track, which we treat as exposed.                                                                                                                              |
| Exposed population per province     | `/data/interim/phl_adm2_uwan_exposed_pop.gpkg`                                             | [HDX (COD-AB)](https://data.humdata.org/dataset/cod-ab-phl) and [WorldPop](https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-phl), prepared in the previous exercise | Province boundaries (admin level 2) with the total population (`total_pop_sum`), the exposed population (`exposed_pop_sum`) and the share of exposed people in % (`exposed_pop_pct`).              |
| Exposed population per municipality | `/data/interim/phl_adm3_uwan_exposed_pop.gpkg`                                             | [HDX (COD-AB)](https://data.humdata.org/dataset/cod-ab-phl) and [WorldPop](https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-phl)                                    | Municipality and city boundaries (admin level 3) with the total population (`total_pop_sum`) and the exposed population (`exposed_pop_sum`). We use this layer for the detailed maps in the atlas. |
| Exposed hospitals                   | `/data/interim/phl_uwan_exposed_hospitals.gpkg`                                            | OpenStreetMap via the [HOT Export Tool](https://export.hotosm.org/)                                                                                                                      | Hospitals within 200 km of the storm track. Completeness depends on how well an area has been mapped in OpenStreetMap.                                                                             |
| Style files                         | `/styles/phl_adm2_uwan_exposed_pop_total.qml`, `/styles/phl_adm2_uwan_exposed_pop_pct.qml` | Prepared for this exercise                                                                                                                                                               | Ready-made styles for the province layer: one for the number and one for the share of exposed people.                                                                                              |

:::{topic} Context
In the previous exercise, we assessed the impact of Typhoon Uwan on the Philippines by estimating the exposed population and hospitals. In this exercise, we want to create operational maps and generate an atlas that can help the operations team plan their interventions ahead of the landfall of the typhoon.
:::

## Tasks

### Task 1: Adding a basemap with QuickMapServices

We want to add labels to our maps, so our operational team can identify the exposed provinces at a glance. However, our basemap already has labels, which are being covered by our layers. Let's find a different basemap that we can use so our map becomes easier to read. 

#### Installing the QuickMapServices plugin

QGIS offers the generic OpenStreetMap as a basemap from the start, but you can also add more basemaps. One way to add more basemaps is with the QuickMapServices plugin, which lets you search for basemaps you can add to your project. To use it, we need to [install the QGIS plugin](../Wiki/en_qgis_plugins_wiki.md#installation-of-plugins). 

1. In the menu bar at the top of the QGIS window, navigate to `Plugins` → `Manage and Install plugins`. A new window will open. 
2. Here, you can find all the plugins that the QGIS community developed. In the search bar, search for __"QuickMapServices"__ and click `Install`.
3. Once the plugin is installed, you can browse the available basemaps by navigating to `Web` → `QuickMapServices` → `Search NextGIS QMS`. A new panel will open, probably on the bottom right.

:::{figure} ../../../fig/en_qgis_3.44_module_4_phl_uwan_open_search_qms.png
---
name: en_qgis_3.44_module_4_phl_uwan_open_search_qms
width: 100%
---
Opening the NextGIS QMS search from the QuickMapServices plugin in QGIS 3.44.
:::

4. In the search bar, enter `OpenFreeMap` and add "OpenFreeMap Bright" to your project by clicking on the `+`-symbol. Make sure that the basemap layer is not hidden by another layer (e.g., the standard OSM basemap).

> Great, we now have a more suitable basemap.

### Task 2: Preparing the layers

In this step, we want to prepare our QGIS project to create the overview map and the map atlas. We will be using the layers from our previous analysis by loading them from the `/data/interim` folder and we will add style files (`.qml`) to quickly style the layers. This will save us some time when creating the map. 

#### Loading the layers and applying style files

1. From the `/data/interim` folder, load the following layers:
    - `Cyclone_Uwan_200km_buffer.gpkg`
    - `phl_adm2_uwan_exposed_pop.gpkg`
    - `phl_adm3_uwan_exposed_pop.gpkg`
    - `phl_uwan_exposed_hospitals.gpkg`
    - `cyclone_track_uwan.gpkg`

2. Make sure to order the layers so we can style them correctly. They should be ordered as in the picture below: 

:::{figure} ../../../fig/en_qgis_module_5_phl_uwan_ex_2_layer_stack.png
---
name: en_qgis_module_5_phl_uwan_ex_2_layer_stack
width: 50%
---
The layer stack for this exercise. 
:::

3. Your colleague prepared a style file to style the administrative boundaries. Applying the style file will save us time when creating the map. To load a style file:
    - <kbd>Right-click</kbd> on the layer `phl_adm2_uwan_exposed_pop` → `Properties` → `Symbology`
    - At the bottom of the window, open the `Style`-menu → `Load style...`. A file browser will open. 
    - In the file browser, navigate to `../module_5_phl_typhoon_ex_2/styles/`-folder and open the file `phl_adm2_uwan_exposed_pop_total.qml`

:::{figure} ../../../fig/qgis_3.44_module_5_phl_uwan_ex_2_applied_style.png
---
name: qgis_3.44_module_5_phl_uwan_ex_2_applied_style
width: 90%
---
The administrative boundary layer with the applied style file. 
:::


4. Duplicate the layer `phl_adm2_uwan_exposed_pop` via <kbd>right-click</kbd> → `Duplicate layer`.

5. For the duplicated layer, load the style file `phl_adm2_uwan_exposed_pop_pct.qml`.
6. Compare both style files. What do they represent? 

:::{tip}
A style file saves the class breaks of a graduated symbology as fixed values. These classes were chosen for this dataset. If you load the style file onto other data (e.g., WorldPop data from another year, or another country), the classes might not fit anymore, and most features could end up in the same class. In that case, classify the data again.

Sometimes it is still better to keep the same classes, for example when you compare maps of different events or years, or when you create a series of maps such as an atlas. With fixed classes, the same colour always means the same value on every map.
:::

#### Applying rule-based labels to the admin layer

We want to make it easy to identify the provinces that are exposed to the typhoon. We can do this by applying rule-based labels to the layer, showing both the name and the sum of the exposed population. 

1. Open the layer styling panel by navigating to `View` → `Panels` → `Layer Styling`. 
2. Select the layer `phl_adm2_uwan_exposed_pop` (not the duplicate), navigate to the `Labels`-tab and select `Rule-based Labeling`.


:::{figure} ../../../fig/qgis_3.44_module_4_phl_uwan_ex_2_adding_labels_1.png
---
name: qgis_3.44_module_4_phl_uwan_ex_2_adding_labels_1
width: 100%
---
Opening the labels-menu for the layer.
:::


3. <kbd>Click</kbd> on the `+`-symbol to add a new rule
4. <kbd>Double-click</kbd> on the new rule to edit it.
5. Add a description (e.g., exposed province name + exposed pop count) to easily identify it.
6. Add a filter. We want to limit the labels to only appear for the exposed provinces.
    - Click on the `Expression editor`-icon ![](../../../fig/mIconExpression.png).
    - Enter this expression: `"exposed_pop_sum" > 0`. 
    - Under `Labels`, make sure to set the value to `adm2_name`
    - Finish editing the rule by clicking on ![back_icon](../../../fig/3.44_back_icon.png)
    - The labels should now only appear for the exposed provinces. 
7. Let's customize the label so it does not only show the name of the province, but also the number of exposed people. 
    - <kbd>Double-click</kbd> on the rule to edit it again. 
    - Click on the ![](../../../fig/mIconExpression.png)-icon next to the __Value__-field. 
    - Enter the following expression: `"adm2_name" || '\n' || format_number("exposed_pop_sum", 0)`
    - Click on `OK`. 

:::{figure} ../../../fig/qgis_3.44_module_4_phl_uwan_ex_2_advanced_labels.png
---
name: qgis_3.44_module_4_phl_uwan_ex_2_advanced_labels
width: 100%
---
Intermediary result showing the advanced labels. 
:::

> Great, we can use this to create a more advanced situation map! In your free time, try creating a new print layout for this map.

8. Save the project in the exercise folder as `phl_typhoon_overview_map`.


### Task 3: Creating a new print layout for the atlas

In this step we will use the [print layout](en_qgis_understanding_print_layout.md) to [generate an atlas](en_qgis_understanding_print_layout.md#the-atlas-function-automatic-map-generation). An atlas automatically produces a series of maps. We want to create a more detailed map for each province that is exposed to the typhoon. 

#### Preparing the layers

1. Adjust the symbology for the layer `phl_adm3_uwan_exposed_pop` so that the filling is transparent and only the outline is visible. 
2. Adjust the symbology for the layer `phl_adm2_uwan_exposed_pop` so that the fill is transparent as well. Give it a thicker, darker outline than the admin 3 boundaries, so the province borders stand out on every atlas page. Make sure the layer lies above `phl_adm3_uwan_exposed_pop` in the Layers panel, and hide the duplicated admin 2 layer.
3. Make sure that the layer `phl_uwan_exposed_hospitals` is at the top and symbolised accordingly (e.g., a small red cross on a white circle).
4. Save the project in the exercise folder as `phl_typhoon_atlas`.

#### Creating a new print layout for the atlas

1. Create a new print layout by navigating to `Project` → `New Print Layout`. Name it `Uwan_Province_Atlas` and click `OK`. The print layout window opens.
2. **Add the map.** Click on the `Add Map` icon ![add map](../../../fig/30.30.2_print_layout_insert_map_icon.png) and draw a rectangle on the page. Leave some space at the top for the title and on the right for the legend.
3. **Add a legend.** Click on the `Add Legend` icon ![add legend](../../../fig/30.30.2_print_layout_add_legend.png) and draw a rectangle next to the map.
    - In the `Item Properties` panel on the right, untick `Auto update`.
    - Remove the layers that are not needed on the map (e.g., the basemap, the duplicated admin 2 layer and the buffer) by selecting them and clicking the `−` button.
    - Double-click on a layer name to give it a clear name, e.g. `Exposed population`, `Province boundaries` or `Hospitals`.
4. **Add a title.** Click on the `Add Label` icon ![add label](../../../fig/30.30.2_print_layout_add_text.png) and draw a rectangle above the map.
    - In the `Item Properties` panel, replace the text `Lorem ipsum` with a title, e.g. `Typhoon Uwan – Exposed population and hospitals`.
    - Under `Appearance` → `Font`, increase the font size (e.g. 20 pt) and set it to bold.
    - We will make the title change automatically for every province once we have set up the atlas.
5. **Add a scale bar and a north arrow.** Click on the `Add Scale Bar` icon ![add scale bar](../../../fig/30.30.2_print_layout_add_scale_bar.png) and the `Add North Arrow` icon ![add north arrow](../../../fig/30.30.2_print_layout_add_orientation.png), and place them in a corner of the map.
6. Add a short text with the data sources (e.g. `Data: IBTrACS, WorldPop, OCHA COD-AB, OpenStreetMap`) using another label at the bottom of the page.


%% Picture 


#### Generating the atlas

Now we turn the layout into an atlas. QGIS will create one page for every feature of a layer, the __coverage layer__. In our case, this is the province layer, so we get one map per province. With a filter, we make sure that only the exposed provinces get a page.

:::{tip}
If you can't see the Atlas Toolbar, activate it under `View` → `Toolbars` → `Atlas Toolbar`. See the [Module 4 article on the atlas function](en_qgis_understanding_print_layout.md#the-atlas-function-automatic-map-generation) for more information.
:::

1. **Set up the atlas.** Click on the `Atlas Settings` button ![atlas settings](../../../fig/30.30.2_print_layout_atlas_settings.png) in the Atlas Toolbar. The `Atlas` panel opens on the right.
    - Tick `Generate an atlas`.
    - Coverage layer: `phl_adm2_uwan_exposed_pop`
    - Leave `Hidden coverage layer` unticked. Otherwise, the province outlines would disappear from the map.
    - Page name: `adm2_name`
    - Tick `Filter with` and enter the expression `"exposed_pop_sum" > 0`. Only the exposed provinces will get a page. This is the same expression we used for the labels in Task 2.
    - Tick `Sort by` and choose `exposed_pop_sum`. Untick the ascending order (the arrow button next to it), so the province with the most exposed people comes first.

2. **Let the atlas control the map.** Select the map item on the page and open the `Item Properties` panel.
    - Scroll down and tick `Controlled by Atlas`.
    - Select `Margin around feature` and set it to `10 %`. The map will zoom to each province and leave some space around it, so the neighbouring areas are still visible.

3. **Preview the atlas.** Click on the `Preview Atlas` button in the Atlas Toolbar. The map now zooms to the first province. Use the arrow buttons next to it to click through the pages. Rendering can take a few seconds per page.

4. **Make the title dynamic.** At the moment, every page has the same title. We want the title to show the name of the province.
    - Select the title label and open the `Item Properties` panel.
    - Replace the text with:

      ```
      Typhoon Uwan – Exposed population in [% "adm2_name" %]
      ```

    - Everything between `[%` and `%]` is an expression. QGIS evaluates it for the current atlas page, so the title now changes with every province.

5. **Add the key figures of the province.** Add a new label below the title or next to the legend and enter:

    ```
    Exposed population: [% format_number("exposed_pop_sum", 0) %] ([% "exposed_pop_pct" %] % of the province)
    ```

    Click through a few pages of the atlas preview to check that the text changes with every province.

6. **Check every page.** Click through all pages and check that the legend, title and other elements do not cover the province. If needed, move them or make the map smaller.

7. **Export the atlas.** Click on `Atlas` → `Export Atlas as PDF…`.
    - Make sure `Single file export when possible` is ticked in the `Atlas` panel if you want one PDF with all pages. If you untick it, QGIS creates one PDF per province. The file names are set with the `Output filename expression` in the `Atlas` panel, e.g. `'Uwan_exposure_' || "adm2_name"`.
    - Save the PDF in the `/results` folder.

> Great! You have created a map for every exposed province with a single layout. If the data changes (e.g. with a new forecast track), you only need to update the layers and export the atlas again.

:::{dropdown} Going further: Highlight the current province
On each atlas page, the neighbouring provinces are visible as well. You can highlight the province of the current page with a rule-based style:

1. Open the symbology of `phl_adm2_uwan_exposed_pop` and switch from `Single Symbol` to `Rule-based`.
2. Add a rule with the filter

    ```
    "adm2_pcode" = attribute(@atlas_feature, 'adm2_pcode')
    ```

    and give it a thick, dark outline and no fill.
3. Add a second rule, tick `Else` and give it a thin, grey outline.

`@atlas_feature` is the province of the current atlas page. The rule therefore only applies to the province that the page is about.
:::

:::{dropdown} Going further: Count the exposed hospitals per province
The hospital layer contains the province code of each hospital (`adm2_pcode`). You can count the hospitals of the current province directly in a label in the print layout:

```
Exposed hospitals: [% aggregate(layer:='phl_uwan_exposed_hospitals', aggregate:='count', expression:="fid", filter:="adm2_pcode" = attribute(@atlas_feature, 'adm2_pcode')) %]
```
:::

## Discussion <a id="discussion"></a>

- At the moment, the atlas only shows the outlines of the municipalities (admin level 3), but the layer `phl_adm3_uwan_exposed_pop` also contains the exposed population (`exposed_pop_sum`). How could you show it on the atlas pages?
    - Which symbology would you use? (Hint: a [graduated classification](../Wiki/en_qgis_graduated_wiki.md) on `exposed_pop_sum`.)
    - Should all atlas pages use the same classes, or should the classes adapt to each province? What are the advantages and disadvantages of each option for the operations team?
    - Would the absolute number of exposed people or the share of the population be more useful at municipality level? Which additional field would you need for the share?
    - How would you combine the choropleth with the province outlines and the hospitals so that the map stays readable?
