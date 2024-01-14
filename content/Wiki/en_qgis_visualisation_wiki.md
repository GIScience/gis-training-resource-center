# Visualisation

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧


## Visualisation of Vector data

### Symbology

QGIS offers various ways to visualize vector data. In the Symbology Tab, you can select between various symbolization methods

::::{tab-set}

:::{tab-item} Single-Symbol
- Assigns one symbol to every feature of the dataset, no matter if the attributes are different.

:::

:::{tab-item} Categorized  

- Classifies features into categories using an attribute (`Value`). 
- A category is created for each unique value of this attribute. 
- Each category can be assigned to a different symbol.
- This can be used for nominal as well as ordinal data.

__For example__, assign a different symbol for each type of building (industrial, commercial, public, residential,...) 

:::

:::{tab-item} Graduated

- Creates classes for numerical data.
- A colour gradient can be selected to represent the distribution of the data

__For example__, create 6 classes of population sizes and assign a color gradient from white to red to indicate the population size in a district.

:::

:::{tab-item} Rule-based

- Create rules using an expression and assign a symbol for the features where the rule applies.
- You can specify more accurately the features you want to symbolize.
- You can use values from different attributes (e.g. building type and city district).
- The expression builder helps you create rules by displaying the available values, fields, operators, etc...

__For example__, select a symbol for every health facility that is a hospital and has exceeded it's capacity.

:::

::::

----

### Labels

Labels can display information or value of the data. In QGIS, you can either select __Single Labels__ or __Rule-based Labelling__. For each option, an attribute (`value`) that will be displayed on the map. Additionally, you can __change the font, font size, colour and some other styling options__ for the label text. 

::::{tab-set}

:::{tab-item} Single Labels

- Creates a single label style for every feature in the layer.

:::

:::{tab-item} Rule-based Labelling

- Create rules using expressions to select accurately which features are to be labeled.
- Each rule can have a different text formatting

:::

::::

```{note} Label rendering

Sometimes the labels can obstruct other symbols. In that case, you can either adjust the placement of the labels in the __Label tab__, or use the `Move a Label, Diagram, or Callout`-tool in __Label toolbar__

By default, QGIS renders the labels in such a way that they don't overlap with other labels. This means that not all the labels will be visible if the data is dense or rendered close to each other. You can optimize the rendering under the rendering option. 

```

---

## Visualisation of Raster data

Raster data is visualised differently from vector data. 

