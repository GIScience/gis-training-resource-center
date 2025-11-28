::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Visualising health facility capacity with multi-variable point symbols

A health facility capacity map is a practical and valuable tool for health preparedness and response. These maps help responders quickly identify the locations of health services, assess their capacity, and determine whether they are operational. In many situations, this information is crucial for making decisions about resource allocation, referral pathways, surge support, and identifying service gaps. The maps are typically based on datasets provided by governments or partner organizations. If official datasets are not available, OpenStreetMap can serve as a good starting point.

Health capacity maps usually combine multiple attributes into a single symbol by utilizing size, color, and different shapes. 


```{figure} /fig/HS_capacity_map_examepls.drawio.svg
---
name: Building a Multi-Variable Hospital Capacity Map Step by Step
width: 800
---
Building a Multi-Variable Hospital Capacity Map Step by Step
```

In this tutorial, you will learn how to create a multi-variable point map of hospitals in Malawi using QGIS. You will work with a modified version of the Malawi Master Health Facility Registry (with fictitious figures and hospital bed counts added for training purposes) and apply a combination of proportional symbol size, manual classification, and data-defined color overrides to effectively communicate both capacity and operational status at a glance.

## About the Dataset

The data used in this exercise comes from the Malawi Master Health Facility Registry (MHFR), the official national database of all health facilities in Malawi. **[Malawi - Health Facility Registry](https://data.humdata.org/dataset/malawi-health-facility-registry)**
It exists to provide a single, up-to-date source of information for planning and monitoring health services.

> ⚠️ **Note:** For the purpose of this tutorial, the dataset has been **manipulated**.
---
Download the data folder [**here**](https://nexus.heigit.org/repository/gis-training-resource-center/module_4/exercise_6/Module_4_Exercise_Malawi_Health_Facilities_Registry.zip) and save it on your PC. Unzip the .zip file.
### Fields used in this tutorial

| **Field**                 | **Purpose in tutorial** |
|--------------------------|--------------------------|
| **TYPE**                 | To extract hospitals from the full facilities dataset |
| **STATUS**               | To map Functional vs Non-functional facilities using colour |
| **Number_Beds**          | To represent hospital capacity using graduated symbol sizes |
| **LATITUDE & LONGITUDE** | To create point geometries in QGIS |

These fields are enough to build a clear, multi-variable point map.

## Health Facilit Capacity Map Tutorial

### Data preparation
First, we need to load the Malawi - Health Facility Registry dataset into QGIS

::::{dropdown} Import the Malawi health facilities CSV into QGIS.

#### Import the Malawi health facilities CSV into QGIS

1. In the top menu, go to  
   **Layer → Add Layer → Add Delimited Text Layer…**

2. Next to the **File name** field, click the three dots ![](/fig/Three_points.png)   
    and browse to your **Malawi health facilities CSV** file and click `Open`.


3. After selecting the file, QGIS will show a preview of the table.  
   Take a moment to review the columns:
   - `OWNERSHIP`  
   - `TYPE`  
   - `STATUS`  
   - `ZONE`, `DISTRICT`  
   - `DATE OPENED`  
   - `LATITUDE`, `LONGITUDE`  
   - `Number_Beds`  
   These fields contain all information needed for the mapping exercise.

4. Under **Geometry Definition**:
   - Select **Point coordinates**.  
   - Set **X field** = `LONGITUDE`.  
   - Set **Y field** = `LATITUDE`.  
   - Ensure the **Geometry CRS** is set to **EPSG:4326 – WGS 84**.

5. Click **Add**.  
   The layer will now appear in your **Layers** panel and the points will display on the map canvas.

```{figure} /fig/en_point_visualisation_malawi_HS_csv_import.png
---
name: import_health_facilities_csv
width: 700px
---
```
::::


Next, we need to reduce the points visualised on the map to the facilities that actually have hospital beds. In this tutorial, these are `Central Hospital`, `District Hospital`, and `Hospital`.

::::{dropdown} Filter the dataset to see only hospitals

#### Filter the dataset to see only hospitals

1. **Open the attribute table**  
   - Right-click `Malawi_health_facilities_raw` → **Open Attribute Table**.  
   - Look briefly at the key fields:
     - **TYPE** – identifies facility type. Hospitals usually appear as `Central Hospital`, `District Hospital`, or `Hospital`.  
     - **STATUS** – should contain `Functional` or `Non-functional`.  
     - **Number_Beds** – mostly fill

2. Filter the dataset to include only hospitals
    - Right-click Malawi_health_facilities_raw → Filter…
    - Enter the expression:
   ```
   "TYPE" IN ('Central Hospital', 'District Hospital', 'Hospital')
   ```
    - Click Test to check how many rows match, then OK.
    - QGIS will now hide all non-hospital facilities.
    - Your filtered layer now shows only hospital facilities.

    <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_malwai_exampel_hospital_filter.mp4"></video>

::::
### Visualising the number of beds with proportional circle methods

Now that your layer is filtered to show only hospitals, you can create a map that shows hospital capacity using proportional circles.  
The number of beds (`Number_Beds`) will control the **size** of each symbol.


::::{dropdown} Visualise hospital capacity using proportional (graduated-size) circles (video)

### Visualise hospital capacity using proportional circles (graduated-size)


1. **Open the Layer Styling panel**  
   - Select your hospital layer (the filtered `Malawi_health_facilities_raw`).  
   - Right-click the layer → **Properties…** → **Symbology**.

2. **Change the renderer to Graduated**
   - At the top of the Symbology window, change the style from **Single Symbol** to **Graduated**.

3. **Select the attribute for symbol size**
   - Under **Value**, choose **`Number_Beds`**.  
     This is the field that will control the size of each circle.

4. **Change the Method to “Size”**
   - Next to **Method**, change the default (usually “Color”) to **Size**.  
     This turns the graduated classification into a **proportional circle map**.

5. **Generate the classes**
   - Click **Classify**.  
     QGIS will create size classes based on the range of bed numbers in your dataset.

#### Adjust the classes manually (recommended)

The data range is **1–200 beds**, but only a few hospitals have more than **80 beds**.  
Most hospitals are small or medium-sized.

Automatic classification would cluster most facilities into one or two classes.  
To avoid this, we create **balanced, domain-informed classes**:

| Class | Bed Range | Meaning |
|-------|-----------|---------|
| 1 | **1–20** | Very small hospitals |
| 2 | **21–40** | Small hospitals |
| 3 | **41–60** | Medium hospitals |
| 4 | **61–80** | Large hospitals |
| 5 | **81–200** | Very large / referral hospitals |

Adjust the Lower/Upper values for each class accordingly.


```{note}
Why these ranges?  
- Most hospitals fall in the **1–60** bed range → we break this into three meaningful groups.  
- Few hospitals exceed **80 beds**, so the top class isolates the rare high-capacity referral facilities.  
- This ensures **variation in symbol size** is visible and not compressed into one tiny class. 
(See [Graduated Classification](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_data_classification.html#graduated-classification))
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_proportionla_circel_map_malawi_exampel.mp4"></video>

::::

The resulting map displays hospitals as circles of different sizes, each size representing one of the bed-capacity classes you defined earlier.  This gives a quick visual impression of where smaller and larger hospitals are located. However, at this stage the map only shows capacity: it does not yet communicate whether a hospital is functional or non-functional.


::::{grid} 2

:::{grid-item} **Proportional circle map showing the number of beds**
```{figure} /fig/en_Malwai_Exampel_proportional_circel_result.png
---
name: Proportional circles: beds 
width: 400
---
Proportional circles: beds 
```
:::

:::{grid-item} **Classes of proportional circle map**

Smaller circles correspond to hospitals with few beds, while larger circles indicate facilities with higher capacity.
```{figure} /fig/en_Malwai_Exampel_proportional_circel_result_legend.png
---
name: Proportional circles: beds classes
width: 100
---
Proportional circles: beds classes
```
:::
::::
### Adding visualisation of operational status with colour

To visualise the operational status of each hospital (operational or non-operational) alongside its bed capacity, we can use QGIS’s data-defined override functionality. A **data-defined override** allows you to control a symbol property—such as colour, size, rotation, or opacity—using an expression or an attribute value from the layer. This means QGIS adjusts the symbol automatically for each feature, based on the data rather than manual styling. Using this technique, we can assign a colour to each hospital according to its status while keeping the proportional circle sizes for bed capacity.

First, we need to open the **data-defined override Expression Builder**.

::::{dropdown} Open data-defined override to adjust colour based on operational status (Video)

### Open data-defined override to adjust colour based on operational status

1.  Select your hospital layer (the filtered `Malawi_health_facilities_raw`).  
2. Right-click the layer → **Properties…** → **Symbology**.
3. Nex to `Symbol` Tab click on the dropdown menue, then click at the top click on `Configure Symbol`.
4. In the new window click on `Simpel Marker` and then next to `fill colour`on the `data-defined override` symbol![](en_data_defined_overried_icon.png)
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_edit.mp4"></video>
::::

To make this work, we now need to tell QGIS which colour to use for each hospital. Data-defined overrides use the QGIS expression language, which lets you write short rules that are applied automatically to every feature in the layer. In this step, we will write a small expression that checks the value in the STATUS field and assigns the correct colour based on whether the hospital is functional or not.

::::{dropdown} Use an Expression to Colour Hospitals by Status (Video)
### Use an Expression to Colour Hospitals by Status

1. This expression tells QGIS to automatically choose a colour for each hospital based on its `STATUS` attribute.  
Functional hospitals become green, non-functional ones become red, and any missing values receive a neutral grey.
The `CASE` statement works like an “if–else” rule: QGIS checks the value in the `STATUS` field and assigns the corresponding RGB colour ([RGB Color Picker](https://share.google/mYczZipa9EqVWFvyD)), ensuring every point is styled consistently without manual editing.
You can copy the complete code here:
```
CASE
  WHEN "STATUS" = 'Functional' THEN color_rgb(0, 130, 0)     -- green
  WHEN "STATUS" = 'Non-functional' THEN color_rgb(190, 0, 0) -- red
  ELSE color_rgb(150, 150, 150)                               -- fallback for missing/unknown
END
```
Or write the code yourself using the help of the functionality of the expression builder:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_code - Made with Clipchamp.mp4"></video>

```{figure} /fig/en_data_defined_overried_calculator_Malwai_Exampel.png
---
name: Expression in data-defined override Expression Builder
width: 700px
---
Expression in data-defined override Expression Builder
```
::::


::::{grid} 2

:::{grid-item} **Proportional circle map showing the number of beds AND operational status**
```{figure} /fig/en_Malwai_Exampel_proportional_data_difined_override_circel_result.png
---
name: Proportional circles: beds + operational status
width: 400
---
Proportional circles: beds + operational status
```
:::

:::{grid-item} **Classes of proportional circle map**
This new visualisation shows the size of the circle, the number of beds, the colour (Green: Operational; Red: Non-Operation), and the operational status of the hospitals.

```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_legend.png
---
name: Legend proportional circles: beds + operational status
width: 400
---
Legend proportional circles: beds + operational status
```
:::
::::

### Making the Legend Match Your Map

> ⚠️ **Note:** When you use a data-defined override to colour your symbols, QGIS does not automatically update the legend. 
---

To make sure your map readers understand the meaning of the colours, you need to customise the legend manually. Here are two practical ways to do this.

::::{dropdown} Option 1: Duplicate the Layer to Create a Legend Helper

A straightforward workaround is to duplicate your hospital layer and use these copies solely as legend helpers. Rename the duplicate for easy identification and change its color in the visualization. Make sure to hide this layer in the map view. 

In the `Print layout`, you can add this layer to the legend. This way, the legend will display the correct colors, while your original layer, which contains the data-defined overrides, will still be responsible for the actual map styling.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_helper_layer.mp4"></video>
::::

::::{dropdown} Option 2: Edit Legend Colours Directly in the Print Layout

Another option works only in the `Print Layout`. In the Legend, just add your hospital layer twice. The secound one, you can adjust the colour of each symbol directly in the Legend. Set each item to green. Using the option `Start a new column before this term`, you can place the two layers next to each other.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_print_layout_costum_symbol.mp4"></video>
::::



```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_map.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status 
width: 800
---
Exampel Map Proportional circles: Hospital Beds + Operational Status 
```

### Adding a Third Variable Using Stroke Style (Facility Type)

Your hospital capacity map now contains a rich amount of information, and it is already useful in its current form. However, QGIS allows us to add an additional layer of meaning without creating new layers or changing the existing size and colour logic. One way to do this is by using the stroke—the outline of each symbol—which can be styled or patterned dynamically. In the next section, you will learn how to use the stroke style to represent a third attribute, making your visualisation even more informative while keeping it easy to read.

::::{dropdown} Adding a Third Variable Using Stroke Style (Video)

1.  Select your hospital layer (the filtered `Malawi_health_facilities_raw`).  
2. Right-click the layer → **Properties…** → **Symbology**.
3. Nex to `Symbol` Tab click on the dropdown menue, then click at the top click on `Configure Symbol`.
4. In the new window click on `Simpel Marker` and then on the 
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_edit.mp4"></video>

4. You will see:
- Fill colour
- `Outline/stroke colour`
- `Outline width`
- `Stroke style` ← we will use this
5. Add a Data-Defined Override for Stroke Style
- Next to `Stroke style`, click the small `data-defined override` symbol![](en_data_defined_overried_icon.png)
- Choose `Edit` → This opens the QGIS Expression Editor.
6. Write an Expression to Assign Stroke Styles for `TYPE`

Here is an example that distinguishes three hospital categories using clear and readable stroke patterns:

```
CASE
  WHEN "TYPE" = 'Central Hospital' THEN 'solid'
  WHEN "TYPE" = 'District Hospital' THEN 'dash'
  WHEN "TYPE" = 'Hospital' THEN 'dot'
  ELSE 'solid'
END
```
QGIS applies the rule automatically to each feature.

**How this works:**

- `Central Hospital` → solid outline
- `District Hospital` → dashed outline
- `Hospital` → dotted outline
- `All others` → solid (fallback)

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>

::::

By adding stroke styles to your symbols, the map now carries a third layer of information while keeping the overall design compact and readable. This works best when you limit stroke styles to just a few meaningful categories; using too many patterns will quickly make the map visually noisy. Make sure your legend clearly explains what each pattern represents, and avoid combining stroke style with additional outline colours unless it is absolutely necessary—too many variations can overwhelm the reader. With these principles in mind, your updated map should now communicate three attributes at once in a clear and balanced way.

::::{grid} 2

:::{grid-item} 
```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map.png
---
name: Proportional circles: beds + operational status + Owner status
width: 400
---
Proportional circles: beds + operational status + Owner status
```
:::

:::{grid-item} 


```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_strock_style_legend.png
---
name: Legend 
Proportional circles: beds + operational status + Owner status
width: 200
---
Legend 
Proportional circles: beds + operational status + Owner status
```
:::
::::
With three visual variables now shown in a single symbol, it’s important that the legend reflects all of them clearly. QGIS does not automatically update legend entries when data-defined overrides or stroke styles are used, so a few extra steps are needed to ensure the legend matches what appears on your map. In the next section, you will learn simple ways to adjust the legend so that all size classes, colours, and stroke styles are represented accurately.



::::{dropdown} Option 1: Duplicate the Layer to Create a Legend Helper
A straightforward workaround is to duplicate your hospital layer and use the copy solely as legend helpers. Rename the duplicated layer so it’s easy to recognise in the legend. Use 'categorised' classification. Adjust the stroke style (solid, dashed, dotted) to match the categories you used in your map. Make sure to hide the helper layer in the map view so it doesn’t appear on the actual map.

In the Print layout, add the helper layer to the legend. This ensures the legend shows the correct stroke patterns, while your original layer—with its data-defined overrides—continues to control the real map symbology.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>
::::

::::{dropdown} Option 2: Edit Legend Colours Directly in the Print Layout
Another option works entirely within the Print Layout. In the legend, add your hospital layer a second time. On this second copy, you can manually adjust the stroke style of each legend item directly in the legend settings—changing them to the solid, dashed, or dotted patterns you used on the map. Using the option Start a new column before this term, you can place the two legend entries next to each other for a cleaner layout. This method leaves your map unchanged and allows you to customise the legend exactly as needed.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>
::::

```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map_complet.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status 
width: 800
---
Exampel Map Proportional circles: Hospital Beds + Operational Status 
```