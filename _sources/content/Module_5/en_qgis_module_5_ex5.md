::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Exercise 5: Aggregate and Assess G2P Money Transfers in Pakistan

## Characteristics of the exercise

:::{card}
__Aim of the exercise:__
^^^
The aim of this exercise is to introduce a workflow that combines both spatial and non-spatial processing. A common step is to aggregate data on administrative scales such as adm2 or adm3. This exercise will teach you how to aggregate information about cash transfers on administrative levels and then join the statistics with a polygon data for the administrative boundaries. 

:::

::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__These skills are relevant for__ 
^^^
- Aggregating and analysing data
- Creating situational reports

:::
::::

::::{grid} 2
:::{grid-item-card}

__Estimated time demand for the exercise__
^^^
~ 60 minutes

:::

:::{grid-item-card}
__Relevant Wiki Articles__
^^^

* [Geodata Import in QGIS](/content/Wiki/en_qgis_import_geodata_wiki.md)
* [Statistics by Categories](/content/Module_5/en_qgis_non_spatial_tools.md)
* [Non-Spatial Join](/content/Wiki/en_qgis_joins_wiki.md)

:::

::::

## Instructions for the trainers

:::{dropdown} __Trainers Corner__ 

### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](/content/Trainers_corner/en_how_to_training.md) for some general tips on training conduction

### Conduct the training

__Introduction:__

- Introduce the idea and aim of the exercise.
- Provide the download link and make sure everybody has unzipped the folder before beginning the tasks.

__Follow-along:__

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

__Wrap up:__

- Leave time for any issues or questions concerning the tasks at the end of the exercise.
- Leave some time for open questions. 

:::

## Step-by-step instructions

:::{card} 
:class-card: sd-text-justify sd-rounded-3 sd-border-2
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_5/Module_5_Exercise_5_aggregating_adm.zip

__Click [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_5/Module_5_Exercise_5_aggregating_adm.zip) to download the datasets for this exercise.__

:::

:::{card}
__Available Data:__
^^^

- `G2P_disbursement_report_cleaned.csv` - Data table with cash transactions. This dataset has been cleaned and all personal information has been removed. 
- `pak_admbnda_adm2_wfp_20220909.shp` - Administrative boundaries on adm2 level (districts).
:::

::::{margin}
```{tip}
To load the CSV-file, navigate to `Layer` > `Add Layer` > `Add delimited text layer`.
```
::::

### Preparing the data

1. Unzip the exercise data and create a new QGIS-project.
2. Load the data into your QGIS-project.
3. Let's familiarise ourselves with the data. Open the attribute table of each layer and see what kind of information is stored in the datasets. 

```{note}
We want to aggregate the information about money transactions on adm3- or adm2-level. Can you identify which column in the `G2P_disbursement_report_cleaned`-layer corresponds to adm2 and adm3? 

:::{dropdown} Solution

By comparing the values in the column `admin2_EN` from the `pak_admbnda_adm2_wfp_20220909`-layer, we can see that the column `var_attr_03` corresponds to the admin2-level in the `G2P_disbursement_report_cleaned`-layer. By sorting the layers alphabetically, it is easier to find matching values in both attribute tables. 

:::

```

### Step 1: Aggregating the amount of transferred money on admin2

3. In the processing toolbox, search for the tool `Aggregate` under `Vector Geometry`. <kbd>Double-Click</kbd> on it. A new window will open (see {numref}`aggregate_tool`).

```{figure} /fig/en_3.36_aggregate.png
---
name: aggregate_tool
width: 600 px
---
The Aggregate-tool in QGIS 3.36
```

4. In the "Aggregate"-window,
    1. Select the `G2P_disbursement_report_cleaned`-layer as input layer.
    2. `Group by Expression` is where we select which column we want to have grouped (or selected as category). We want to identify the amount of money transferred to each district (admin2-level), so we need to select the corresponding column. In our case, this is the column `var_attr_03`.
    3. This box is where we select how the tool aggregates the different columns:
        - We want to calculate the `Sum` for the column "Amount".
        - For the column "var attr 03" we want to select `Concatenate_unique`. This returns all unique strings from a field.  
        - The other columns can be set to `concatenate_unique`
    4. Click `Run`. A new layer called "Aggregated" will appear in the layers-panel. Close the "Aggregate"-window.
 

    ```{figure} /fig/en_3.36_aggregate_settings.png
    ---
    name: aggregate_settings
    width: 650 px
    ---
    Adjust the aggregation function for the relevant columns. Pay attention that the `Type` for the amount is set to "Integer". If you have imported the table correctly into QGIS, this should be set automatically. 
    ```

    ```{admonition}
    :type: note
    If the `Type` for the amount column is set to "Text (string)", this means that QGIS reads the data format for this column as being a string value. QGIS can't perform mathematic operations on string values because they are being read as non-numeric data. Make sure to import the layer through the `Add delimited text layer`-dialogue (`Layer` > `Add Layer` > `Add delimited text layer...`) and make sure the `Type` for the column "Amount" is set to Integer.
    ```

    5. Let's take a look at the new layer by opening the attribute table. If you have done everything correctly, the table should look like {numref}`aggregate_results`. We can see on row for each distinct value in the `var attr 03` column (Gwardar, Jamshoro, Dadu, Kambar Shahdadkot, Shiparpur). In the column `Amount` we see the sum of all the individual transfers. In the other columns, we can see a string with the different values of the original table separated by commas (e.g. the different admin3-units, Thesils, under the column `var attr 04`). 
    
    ```{figure} /fig/en_aggregate_results.png
    ---
    name: aggregate_results
    width: 650 px
    ---
    The aggregated data from `G2P_disbursement_report_cleaned`
    ```


### Step 2: Joining the aggregated data with administrative boundaries

In this step, we want to add the aggregated information we gained from the CSV file to the administrative boundaries. We need to join the aggregated table with the `pak_admbnda_adm2_wfp_20220909`-layer. 

1. In the processing toolbox, search for `Join attributes by field value`. <kbd>Double click</kbd> on it. A new window will open. 

    ```{figure} /fig/en_3.36_join_by_attr.png
    ---
    name: join_by_attr
    width: 700 px
    ---
    The Join attributes by field value dialogue box in QGIS 3.36.
    ```

    1. The input layer should be `pak_admbnda_adm2_wfp_20220909`-layer. This will be the layer that will receive additional information. The geometries of the input layer will be preserved. The `Table field` should be set to "ADM2_EN". These are english names for the admin2-level.
    2. The second input layer should be the `Aggregated` layer from the previous step. `Table field 2` should also be the english names for the administrative boundaries. In our case, the corresponding column is "var attr 03". Under `Layer 2 fields to copy`, only select `amount` as we are not interested in the other values. 
2. Click `Run`. A new layer `Joined Layer` will appear in the layer-panel.
3. Close the joining dialogue window and investigate the new layer by opening it's attribute table. Scroll the right to find the new column "amount" that has been joined. 
4. Notice how most of the rows have `NULL` as their value in this column? This is because the aggregated table only has 5 distinct districts (adm2) that received money. You can sort the table by clicking on the column header. 

Congratulations, we have successfully joined a CSV-file with a polygon layer!

```{figure} /fig/en_m5_ex5_results.png
---
name: aggregation_ex_results
width: 750 px
---
The aggregated amount joined to a layer of the administrative boundaries.
```

