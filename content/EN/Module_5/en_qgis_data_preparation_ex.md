# Exercise: Data preparation (Importing PDF tables into QGIS)

## Characteristics of the exercise

::::{grid} 4 2

:::{grid-item-card}
__Aim of this exercise:__
^^^

Many times in your GIS-career, you will come across data that is not easily accessible, or hard to work with. 
The objective of this exercise is to understand how to prepare and clean data that is in a PDf-file for usage in a QGIS-project. 

:::


:::{card}
__Relevant Wiki articles:__
^^^
* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Import CSV-files into QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-importl)
* [Attribute Table in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.md)

:::

::::


:::{Topic} Context

In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. The flood impact on infrastructure is highly dependent on the building material of houses.  To determine the vulnerability of the infrastructure to flood damage, we will use data on the wall material of the houses in each province. The objective is to create a dataset indicating which provinces are more prone to flood damage due to the durability of the material used for buildings. 
First, we need to extract the data from the PDF-file and save it to a `.csv`- file. Then, we need to clean and prepare the `.csv`-file to remove errors and inconsistencies. Finally, we can import the `.csv`-file and perform an attribute join to attach the information on wall material to a vector-layer containing the polygons of the pakistani provinces. 

:::


## Instructions for the Trainers

:::{attention}

This exercise makes use of the [tabula.technology tool](tabula.technology), an open source application which let's you easily extract tables from a PDF-file. Tabula requires you to have [Java](https://www.java.com/en/download/) installed on your device. 

:::

:::{dropdown} __Trainers Corner__ 


### Prepare the training

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) for some general tips on training conduction

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

## Exercise

### Available Data

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip

Download the datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip) and unzip them. 

:::

| Dataset| Source | Description |
| ----- | --- | --- |
| Administrative boundaries for pakistan | [HDX](https://data.humdata.org/dataset/cod-ab-pak) | The administrative boundaries (adm0-adm3) for pakistan can be accessed via the humanitarian data exchange. For this exercise, we are interested in the districts (adm2) | 
| Percent distribution of households by material used for walls | [Pakistan Bureau of Statistics](https://www.pbs.gov.pk/content/statistical-tables-pslm-2019-20) | Table 7.7 in the *Pakistan Social and living Standards Measurement Survey (2019-20)* shows the materials used for walls per household in percents. | 


### Task 1: Get the data from the PDF file into a CSV file

:::{Topic} Context

The data on wall materials has been published by the [STATISTICAL BUREAU PAKISTAN] as a table in a pdf-file. The table in the pdf-file cannot be imported into QGIS as is. First, the table in the PDF needs to be converted into a `.csv`-file. 

:::

1. In your web-browser, go to [Tabula.technology](https://tabula.technology) and download the application.

:::{admonition} Tabula
:type: tldr
Tabula is an open source application that let's you extract data tables from PDF-files as `.csv`-files. The `.csv`-files can be imported into excel, QGIS, or other data manipulation programs. 

:::

```{figure} /fig/en_tabula_website.png
---
name: en_tabula_website
width: 550 px
---
The Tabula.technology website with the download links to the left
```

2. Unzip the downloaded file into a location of your choosing (e.g., Programs, Desktop, ...).
3. Open the folder where you unzipped the file and open the "Tabula" application

```{figure} /fig/en_tabula_folder.png
---
name: en_tabula_folder
width: 450 px
---

```

4. A new browser window will open with this address: http://localhost:8080. This is the application. If the browser does not open automatically, you can open the browser and enter this go to this address manually.


```{figure} /fig/en_tabula_import.png
---
name: en_tabula_import
width: 550 px
---

```

5. Now let's import the PDF file with the wall types into tabula:  
    1. Click on `Browse` and navigate to the exercise data folder: `...\data\input` and select the PDF "pakistan_wall_type7.7". Click `Open`.
    2. Click `Import` and wait for the PDF to load. Once loaded, it will open automatically.

```{figure} /fig/en_Tabula_main_view.png
---
name: en_Tabula_main_view
width: 550 px
---

```

6. Here we will select the portion of the PDF that contains the data table. Tabula expects a table with one row of headers at the top for each column, followed by the rows with the data. By dragging a rectangle on the PDF, we can create a selection where tabula should look for the data table. Drag a rectangle and adjust the boarders so the table fits as precisely as possible into selection. Make sure to only capture the relevant information. Since the headers in this table has an unconventional formatting, it should be left out so the resulting csv table is easier to adjust. We will add the headers manually once extracted. F

```{figure} /fig/en_tabula_selection.png
---
name: en_tabula_selection
width: 550 px
---

```

7. Once you are satisfied with the selection, you can click on `Repeat this Selection` to duplicate the selection on the next pages. 
8. Take a look on the following pages and make sure the table is still fully contained by the selection.
9. Click on `Preview & Export Extracted Data` on the top right of the window.
10. A new window will appear where the data will show up. At first, nothing will be visible. First, click on `Stream` on the left.

```{figure} /fig/en_tabula_preview_extracted_1.png
---
name: en_tabula_preview_extracted_1
width: 550 px
---

```

11. The data from the PDF table will appear in the main window. Review the table.

```{figure} /fig/en_tabula_data_preview.png
---
name: en_tabula_data_preview
width: 550 px
---

```

12. Click on `Export`, this will save the `.csv` into your downloads folder. 
13. Move the file to the `/data/interim/`-folder.


Congratulations, the data from the PDF has been extracted into a CSV file!

### Task 2: Clean the data from errors and unwanted entries

:::{topic} Context
The data has been extracted from the PDF. However, there are a few formatting errors and unwanted information. Before loading the extracted CSV into QGIS, we need to clean the formatting and remove unwanted entries. This can be done in many ways, for example in a spreadsheet editor such as Microsoft Excel or Libreoffice Calc.
:::

:::{note} 
The necessary steps to filter the data might be different depending on the editor you use. In this exercise, we will go through the workflow with the free version of Microsoft Excel. 
:::

1. Open the extracted CSV file in Excel. It might look like this:

```{figure} /fig/en_tabula_csv_excel.png
---
name: en_tabula_csv_excel
width: 300 px
---

```

2. Excel does not automatically recognise the comma delimited format. We can fix this by selecting the column A, navigating to `Data` > `Text to Columns`. A new window will open. Leave the settings as they are and click `Ok`. 

```{note}
In the web version of excel, you can fix the columns by selecting column A, navigating to `Data` > `Split Text to Columns`

```

```{figure} /fig/en_m5_data_cleaning_ex_task2.png
---
name: en_m5_data_cleaning_ex_task2
width: 450 px
---
The data table should now look like this. It is still missing column headers (red)
```

3. We have to add the column names back, as we did not extract them with tabular. <kbd>Right-click</kbd> on the first row and select `Insert 1 Row Above`. A new row should appear.
4. Enter the column headings as they are in the PDF-file:

| Province & District | Burnt Bricks/Blocks | Mud Bricks/Mud | Wood | Other | Total |  
| :------------------ | :------------------ | :------------- | :--- | :---- | :---- | 

5. Now we can format the data into an excel table. This will allow us to apply filters to remove the unwanted entries. Select the columns A to F and navigate to `Home` > `Format as Table` and select a table styling of your choosing. 

Now we have a usable .csv file with the information. However, there are still some unwanted entries and a few formatting mistakes. First, let's remove all the rows with the data on rural and urban distribution. We want to visualise the distribution on district level, so a distinction between urban and rural is not necessary. 

6. Click on the small arrow next to the "Province & District" column. A dropdown-menu will open.
7. In the dropdown-menu, uncheck the `Select All`-Box and scroll down to check all the entries with the value `Urban` and `Rural`. Also add the entries that have numerical values attached to `Urban` or `Rural`. Click `Apply`. 

:::::{grid} 2

::::{grid-item}
:::{figure} /fig/en_m5_data_cleaning_ex_filter_excel.png
---
name: en_m5_data_cleaning_ex_filter_excel
width: 350 px
---
:::
::::
::::{grid-item}
:::{figure} /fig/en_m5_data_cleaning_ex_filter_excel_2.png
---
name: en_m5_data_cleaning_ex_filter_excel_2
width: 350 px
---
:::
::::
:::::


8. The table should now only show the entries with rural or urban in the "Province & District". Select them all and click on `Remove selected rows`. 

9. Now, we have to remove the filter we applied. 

10. Lets go through the resulting table and see if we need to fix more entries. There are a few entries where the the values for the percentages are not formatted correctly. Copy the values from the columns __Burnt Bricks/Blocks__, __Mud Bricks/Mud__, __Wood__, __Other__ one cell to the right and enter the numerical value that mistakenly got added to the __Provinces & District__ column. 

11. Save the formatted csv file in the input data folder (`.../module_5_ex_7_data_cleansing/data/input/`) under the name `tabula-pakistan_wall_type7.7`. 

Great! Now we are ready to import the CSV-file into QGIS!

### Task 3: Import the Data into QGIS

:::{topic}
With the data formatted as a usable CSV-file, we can import it into QGIS and join it with a polygon layer containing the districts (adm2) by using the columns containing the district names in english. However, in this step, we might encounter the problem that the district names are written differently. In this case, we can't simply perform a attribute join [LINK] as the attributes need to __match exactly__. To fix this, we have to perform a __fuzzy merge__. 

:::


:::{note}
Fuzzy merge is a technique used in data processing to combine two datasets based on similar, but not necessarily identical, values. This is particularly useful when dealing with data that may have inconsistencies, such as typos or different formats. 

Instead of looking for exact matches, fuzzy merge uses algorithms to compare values and determine how similar they are. For example, "Jon" and John" might be considered a match because how similar they are. Each comparison generates a similarity score, which indicates how closely the two values match. 

:::

1. Open QGIS and create a new project.
2. Save the project in the exercise folder.
3. [Import the CSV layer into QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-import).
4. Import the administrative boundaries located in the data input folder: `.../module_5_ex_7_data_cleansing/data/input/`
5. Now let's perform a fuzzy merge: Open the [field calculator](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) __for the layer called `tabula-pakistan_wall_type7.7`__ and enter the following expression: 
    ```
    array_first(aggregate(
    layer:= 'pak_admbnda_adm2_wfp_20220909',
    aggregate:='array_agg',
    expression:=ADM2_EN,
    filter:=levenshtein(ADM2_EN, attribute(@parent, 'Province & Disctrict')) <= 2,
    order_by:=levenshtein(ADM2_EN, attribute(@parent, 'Province & Disctrict'))
    ))
    ```

6. Enter an `Output field name`, set the `Output field type` to `Text (string)` and increase the `output field length` to 40.

7. Click `Ok`. The CSV file should now have a new column. In this column you will find the values from the adm2 polygon layer which have been matched using the fuzzy merge algorithm. 

8. We can now perform an attribute join by selecting the `ADM2_EN` and newly created fuzzy merge column as identifying column. In the processing toolbox, search for the tool __"Join attributes by field value"__. <kbd>Double-click</kbd> on it. 

9. A new window will open. Here, set the following parameters:
    1. __Input layer:__ ADM2 polygon layer
    2. __Table field:__ `ADM2_EN`
    3. __Input layer 2:__ `tabula-pakistan_wall_type7.7`
    4. __Table field 2:__ `Fuzzy_match`
    5. __Layer 2 fields to copy:__ `Burnt Bricks/Blocks, Mud Bricks/Mud, Wood, Other`

```{figure} /fig/en_3.36_m5_ex_7_attr_join.png
---
name: m5_ex7_attr_join
width: 450 px
---
The "Join attributes by field value" parameters
```

10. Click `Run`.

Congratulations, we have now successfully joined the information from the PDF file to a polygon layer!

### Task 4: Visualisation of the Data

:::{topic}

We extracted the data from the PDF and now have a polygon layer containing the information on the wall material per district. With the new column, we can create a map visualising the amount of buildings that have, for example, burnt bricks or blocks as wall material. 

:::

1. Open the layer styling panel and select the __Graduated__ symbolisation method.
2. Under `Value`, select `Burnt Bricks/Blocks`. 
3. Click on `Classify`.

The resulting symbolisation could look something like this:

```{figure} /fig/m5_ex_7_visualisation_result.png
---
name: m5_ex_7_visualisation_results
width: 600 px
---
The darker the colour, the higher the percentage of buildings having burnt bricks or blocks as wall type. The grey areas are the districts where we there is no data available.
```

<!---
### Workflow 2: Microsoft Excel and Power Query

#### Task 1: Get the data from the PDF file into Excel

:::{Topic} Context
The data on the wall materials has been published by the [STATISTICAL BUREAU PAKISTAN] as a table in a pdf-file. The table in the pdf-file cannot be imported into QGIS as is, but needs to be converted into a `.csv`-file beforehand. 
We can extract the table from the PDF-file using the Microsoft Excel, and then save it as a `.csv`-file. 
:::

:::{note}
Before starting manipulating the data, make yourself familiar with the PDF-file. Open it and look at how the data is presented. How are the columns & rows organised? What kind of measurements units have been used? On how many pages is the data distributed? 
:::



1. Open Microsoft Excel and open a new workbook.
2. In the navigation bar, navigate to `Data` and click on the tool `Get Data` > `From file` > `From PDF`. 
3. A new window will open. Select the file from your download folder and click `Open`.
4. Another window called "Navigator" will open. Here you can select the page from which excel will extract the data.
5. Check the box `Select Multiple Items` and select the tables  __Select Page 1__ and click `Load`. 
5. The data will be loaded onto a new Excel-sheet. 

    :::{note}
    You will notice that the table is not formatted correctly. This has to be fixed manually.
    >Insert Image
    :::

6. Give the columns the correct names, as they are presented in the PDF file (Province & District, Burnt Bricks/Blocks, Mud Bricks/Mud, Wood, Other, Total) on __each page__.
7. Delete the first two rows so the table starts with the provinces and the percentage values.




11. Save the file as a "Comma delimited text"-file (`.csv`). Click `Yes`.

Congratulations, the data from the PDF has been extracted and saved to a usable `.csv`-file!

#### Task 2: Prepare and clean the data for import into QGIS

:::{topic} Context
The data has been extracted from the PDF-file, but cannot be used for an attribute join in QGIS yet. First, we need to make sure that the attribute values are formatted correctly and correspond to the attribute values of the identifying key in the vector layer.
:::

:::{caution}
The key identifiers need to __match exactly__. Otherwise, QGIS will not be able to join two layers. We need to prepare the files so the attributes will match.
:::


12. Delete each row with the value "Urban" and "Rural" in the column "Province & District". Check for district names where the "Urban" or "Rural" has been added at the end.
>Image
9. 
-->