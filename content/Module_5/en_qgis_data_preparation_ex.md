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


<!---::::{grid} 2
:::{grid-item-card}
__Type of trainings exercise:__
^^^

- This exercise can be used in online and presence training. 
- It can be done as a follow-along exercise or individually as a self-study.

:::

:::{grid-item-card}
__These skills are relevant for:__ 
^^^

- QGIS Essentials
- Preparing secondary data to use in your own QGIS-projects

:::
::::

::::{grid} 2
:::{grid-item-card}
__Estimated time demand for the exercise:__
^^^

- The exercise takes around 1 hour to complete, depending on the number of participants and their familiarity with computer systems.

:::

:::{grid-item-card}
__Relevant Wiki articles:__
^^^
* [QGIS Interface](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html)
* [Import CSV-files into QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#text-data-importl)
* [Attribute Table in QGIS](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_attribute_table_wiki.md)

:::

::::
-->

:::{Topic} Context

In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. The flood impact on infrastructure is highly dependent on the building material of houses.  To determine the vulnerability of the infrastructure to flood damage, we will use data on the wall material of the houses in each province. The objective is to create a dataset indicating which provinces are more prone to flood damage due to the durability of the material used for buildings. 
First, we need to extract the data from the PDF-file and save it to a `.csv`- file. Then, we need to clean and prepare the `.csv`-file to remove errors and inconsistencies. Finally, we can import the `.csv`-file and perform an attribute join to attach the information on wall material to a vector-layer containing the polygons of the pakistani provinces. 

:::

:::{attention}
This exercise has two different solution methods:
- The first one uses Microsoft Excel with an active Microsoft 365 Subscription, making use of the advanced features "Get Data From PDF" and the Fuzzy Merge Function in the Power Query Editor.
- The second solution uses Open-Source Software to achieve the same result. However, the workflow is quite different.

:::

## Instructions for the Trainers

:::{attention}

This exercise makes use of the [tabula.technology tool](tabula.technology), an open source application which let's you easily extract tables from a PDF-file. Keep in mind that 

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

- Administrative Boundaries for pakistan
- Excel files

### Workflow 1: Tabula and QGIS

#### Task 1: Get the data from the PDF file into a CSV file

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
name: tabula_website
width: 550 px
---
The Tabula.technology website with the download links to the left
```

2. Unzip the downloaded file into a location of your choosing (e.g., Programs, Desktop, ...).
3. Open the folder where you unzipped the file and open the "Tabula" application

```{figure} /fig/tabula_folder.png
---
name: Tabula_folder
width: 450 px
---

```

4. A new browser window will open with this address: http://localhost:8080. This is the application. If the browser does not open automatically, you can open the browser and enter this go to this address manually.


```{figure} /fig/en_tabula_import.png
---
name: Tabula_import
width: 550 px
---

```

5. Now let's import the PDF file with the wall types into tabula:  
    1. Click on `Browse` and navigate to the exercise data folder: `...\data\input` and select the PDF "pakistan_wall_type7.7". Click `Open`.
    2. Click `Import` and wait for the PDF to load. Once loaded, it will open automatically.

```{figure} /fig/en_Tabula_main_view.png
---
name: Tabula_main_view
width: 550 px
---

```

6. Here we will select the portion of the PDF that contains the data table. Tabula expects a table with one row of headers at the top for each column, followed by the rows with the data. By dragging a rectangle on the PDF, we can create a selection where tabula should look for the data table. Drag a rectangle and adjust the boarders so the table fits as precisely as possible into selection. Make sure to only capture the relevant information. Since the headers in this table has an unconventional formatting, it should be left out so the resulting csv table is easier to adjust. We will add the headers manually once extracted. F

```{figure} /fig/en_tabula_selection.png
name: tabula_selection
width: 550 px
---

```

7. Once you are satisfied with the selection, you can click on `Repeat this Selection` to duplicate the selection on the next pages. 
8. Take a look on the following pages and make sure the table is still fully contained by the selection.
9. Click on `Preview & Export Extracted Data` on the top right of the window.
10. A new window will appear where the data will show up. At first, nothing will be visible. First, click on `Stream` on the left.

```{figure} /fig/en_tabula_preview_extracted_1.png
name: tabule_preview_1
width: 550 px
---

```

11. The data from the PDF table will appear in the main window. Review the table.
12. Click on `Export`, this will save the `.csv` into your downloads folder. 
13. Move the file to the `/data/interim/`-folder.

```{figure} /figure/en_tabula_data_preview.png
---
name: tabula_data_preview
width: 550 px
---

```

Congratulations, the data from the PDF has been extracted into a CSV file!


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

### Step 2: Prepare and clean the data for import into QGIS

:::{topic} Context
The data has been extracted from the PDF-file, but cannot be used for an attribute join in QGIS yet. First, we need to make sure that the attribute values are formatted correctly and correspond to the attribute values of the identifying key in the vector layer.
:::

:::{caution}
The key identifiers need to __match exactly__. Otherwise, QGIS will not be able to join two layers. We need to prepare the files so the attributes will match.
:::


12. Delete each row with the value "Urban" and "Rural" in the column "Province & District". Check for district names where the "Urban" or "Rural" has been added at the end.
>Image
9. 
