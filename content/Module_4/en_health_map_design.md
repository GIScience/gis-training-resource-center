::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Visualising health facility capacity with multi-variable point symbols

Maps of health facilities are often used to answer very practical questions:

- **Where can people access care in an emergency?**
- **Which areas depend on just one hospital or health centre?**
- **Where are the gaps between population needs and available services?**

A simple point map with one symbol per facility is a good start, but it quickly becomes limiting.  
Decision-makers usually need to see **several pieces of information at once**, for example:

- Is the facility **functional or non-functional**?
- How many **beds** are available?
- What **type** of facility is it (hospital, health centre, dispensary, health post)?
- Who is the **owner** or managing authority (Government,  private, etc.)?


In this tutorial, we focus on **two key attributes** of hospitals:

- **Number of beds** – a simple proxy for *capacity*  
- **Status (Functional / Non-functional)** – a simple proxy for *availability*

By combining these in a **single point symbol**, we can show:

- **Size** → how many beds the hospital has  
- **Colour** → whether the hospital is functional or not  
- **symbols** → Additional informations


```{note}
The goal of this exercise is not to produce a “perfect” health system analysis,  
but to practice **cartographic techniques** that help you present multiple dimensions  
of health capacity clearly on a single map.
```

## Dataset overview  
**[Malawi - Health Facility Registry](https://data.humdata.org/dataset/malawi-health-facility-registry)**

| **Field name**      | **Description**                                      | **Example values** |
|---------------------|------------------------------------------------------|---------------------|
| **OWNERSHIP**       | Who owns or operates the facility                    | Government, Private, CHAM, NGO, Mission/Faith-based, Other |
| **TYPE**            | Type/classification of the facility                  | Central Hospital, District Hospital, Hospital, Health Centre, Dispensary, Health Post |
| **STATUS**          | Operational status                                   | Functional, Non-functional |
| **ZONE**            | Health zone                                          | North Zone, Central East Zone, South West Zone |
| **DISTRICT**        | District name                                        | Lilongwe, Mzimba, Blantyre |
| **DATE OPENED**     | Opening date (text format in this dataset)           | 1957, 2004, 2018 |
| **LATITUDE**        | Geographic latitude (WGS84)                          | –13.9831 |
| **LONGITUDE**       | Geographic longitude (WGS84)                         | 33.7701 |
| **Number_Beds**     | Number of beds (mainly available for hospitals)      | 10, 35, 120 |

 

> ⚠️ **Note:** For the purpose of this tutorial, the dataset has been **manipulated**.
---

### Fields used in this tutorial  

| **Field**                 | **Purpose in tutorial** |
|--------------------------|--------------------------|
| **TYPE**                 | To extract hospitals from the full facilities dataset |
| **STATUS**               | To map Functional vs Non-functional facilities using colour |
| **Number_Beds**          | To represent hospital capacity using graduated symbol sizes |
| **LATITUDE & LONGITUDE** | To create point geometries in QGIS |


### Import the Malawi health facilities CSV into QGIS

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

### Inspect the data briefly and create a “hospitals only” layer

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

### Visualise hospital capacity using proportional (graduated-size) circles

Now that your layer is filtered to show only hospitals, you can create a map that shows **hospital capacity** using **proportional circles**.  
The number of beds (`Number_Beds`) will control the **size** of each symbol.

Follow the steps below:


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

## 2. Adjust the classes manually (recommended)

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

## 2. Add a data-defined override to the colour

1.  Select your hospital layer (the filtered `Malawi_health_facilities_raw`).  
2. Right-click the layer → **Properties…** → **Symbology**.
3. Nex to `Symbol` Tab click on the dropdown menue, then click at the top click on `Configure Symbol`. In the new window click on `Simpel Marker` and then on the data-defined override symbol![](en_data_defined_overried_icon.png)
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_edit.mp4"></video>
4. This expression tells QGIS to automatically choose a colour for each hospital based on its `STATUS` attribute.  
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
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_code - Made with Clipchamp.mp4"></video>

Your resulting layer should look like this:


```{figure} /fig/en_data_defined_overried_calculator_Malwai_Exampel.png
---
name: import_health_facilities_csv
width: 700px
---
```


