::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exporting and Importing Styles

The layers in QGIS are saved separately from the settings and styles of a QGIS Project. This means that if you load the same layers into a different QGIS project, the symbology and styling of the data will be different. QGIS lets you save the symbology and styling of a layer as a separate file (`.qml`-files). Working with `.qml`-files saves you a lot of work and assures consistency between your maps.

A `.qml`-file saves the information of a particular layer. This includes the colours, outlines, shapes, labelling, as well as the Layer configuration, attribute table settings, and other options you have set for a layer in your QGIS project that are not related to the data files themselves. You can choose whether to save only the colour symbology or any additional information.
 
You can export a style into the same folder as the data so your colleagues can apply the same styling when loading the data into QGIS.
Some organisations may also use standardised symbols or colours in their maps. 

For example, if you want to send a layer to your colleague with the same styling as you, it is best to check the "__Layer properties__", "__Symbology__", and "__Labels__" categories (and any additional styling options you have set). If you only wish to save a certain colouring, line thickness, or labeling style, you only need to check the respective boxes.

### Saving or Exporting Styling Settings

1. Open the styling panel and click on `Styles`. A dropdown menu will open with the option to export the layer styling.
2. Since in this case, the styling is for exactly that dataset, you can leave all the boxes checked.
3. Select a location and name for the styling. The styling will be saved as a `.qml` file. __Make sure it is saved in the same folder as the dataset and give it the same name as the corresponding dataset. This way, when loading the data into QGIS, the styling will automatically be applied.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>

:::{figure} ../../fig/en_30.30.2_save_layer_style_window.png
---
width: 350px
name: en_30.30.2_save_layer_style_window
---
Save Layer styling window in QGIS 30.30.2.
:::

When working with similar data (e.g. building types or flooding risk), it is useful to have template styles that can be quickly loaded into your QGIS-project or saved in your Styling Template library. 

:::{Tip}
When a styling is saved in the same location as the data and has the same name as the corresponding dataset, the styling will be automatically applied to the layer when loading the data into QGIS!
:::

### Loading a Style into a QGIS-project

1. Open the style manager: `Settings` > `Style manager`.
2. Click on `import/export` and select `import items`.
3. Navigate to the folder where the style is saved and click import.
4. The style should now be available as a preset in the styling panel.

:::{note}
You can also import styles directly in the styling panel of a layer. But it will not be added to your style library unless you save it into your library.
:::


:::{tip}
You can copy styles from one layer to another:
1. Right-click on the styled layer → `Styles` → `Copy Style` → `All Style Categories`.
2. Right-click on the second layer → `Styles` → `Paste Style` → `All Style Categories`.

:::


## Self-Assessment Questions


::::{admonition} Test your knowledge
:class: note

1. __What are the advantages of creating and using styles?__

:::{dropdown} Answer
- __Consistency:__ ensures uniform symbology across maps and projects.
- __Reusability:__ you can apply the same style to different layers or across projects without re-building from scratch.
- __Efficiency:__ saves time when styling many layers (by just loading the style file).
- __Shareabilty:__ you can share your visual designs (symbols, colour ramps, label settings) with colleagues. 
:::

2. __How do you import or export a style?__

:::{dropdown} Answer
1. In QGIS, right-click on the layer → `Properties` → `Symbology`
2. In the bottom left corner, there is a dropdown menu called `Style` with options to import or export styles. 
:::

3. __How would you share styles with colleagues or across different machines? What should you watch out for (e.g. file paths, resource dependencies)?__

:::{dropdown} Answer
1. Open the `Symbology` tab in the `Properties` window.  
2. In the bottom left corner, click on `Style` → `Save Style`.
3. Specify the name and saving location.
4. In the file browser, find the `.qml`-file and share it with your colleague.

__Things to watch out for:__
- __File paths/references:__ If the style references external files (SVGs, images) with absolute paths, those paths may break on another machine. 
- __Missing resources:__ If an external resource (symbol, image) is absent or moved, the style may fail or fall back to default symbols.
- __Version compatibility__: Styles created in one version of QGIS may not fully work or may degrade in another version.
- __Data compability:__ If you have set rules or classification based on a layer's attributes, the column names and attributes must be present in the dataset on the second computer. 
:::
 

::::