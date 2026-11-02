# Exercise: Data preparation (Importing PDF tables into QGIS) <a id="exercise-data-preparation-importing-pdf-tables-into-qgis"></a>

## Characteristics of the exercise <a id="characteristics-of-the-exercise"></a>

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
* [QGIS Interface](../Wiki/en_qgis_interface_wiki.md)
* [Import CSV-files into QGIS](../Wiki/en_qgis_import_geodata_wiki.md#text-data-import)
* [Attribute Table in QGIS](../Wiki/en_qgis_attribute_table_wiki.md)
* [Non-spatial joins](../Wiki/en_qgis_non_spatial_joins_wiki.md)

:::

::::


:::{Topic} Context

In 2024, the provinces of Punjab, Sindh, and Balochistan in Pakistan experienced devastating floods due to intense and prolonged rainfall. The flood impact on infrastructure is highly dependent on the building material of houses.  To determine the vulnerability of the infrastructure to flood damage, we will use data on the wall material of the houses in each province. The objective is to create a dataset indicating which provinces are more prone to flood damage due to the durability of the material used for buildings. 
First, we need to extract the data from the PDF-file and save it to a `.csv`- file. Then, we need to clean and prepare the `.csv`-file to remove errors and inconsistencies. Finally, we can import the `.csv`-file and perform an attribute join to attach the information on wall material to a vector-layer containing the polygons of the  provinces. 

:::


## Instructions for the Trainers <a id="instructions-for-the-trainers"></a>

:::{attention}

This exercise makes use of the [tabula.technology tool](https://tabula.technology), an open source application which let's you easily extract tables from a PDF-file. Tabula requires you to have [Java](https://www.java.com/en/download/) installed on your device. 

:::

:::{dropdown} __Trainers Corner__ 


### Prepare the training <a id="prepare-the-training"></a>

- Take the time to familiarise yourself with the exercise and the provided material.
- Prepare a white-board. It can be either a physical whiteboard, a flip-chart, or a digital whiteboard (e.g. Miro board) where the participants can add their findings and questions. 
- Before starting the exercise, make sure everybody has installed QGIS and has downloaded __and unzipped__ the data folder.
- Check out [How to do trainings?](../Trainers_corner/en_how_to_training.md) for some general tips on facilitating trainings. 

### Conduct the training <a id="conduct-the-training"></a>

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

## Exercise <a id="exercise"></a>

### Available Data <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip

Download the datasets [here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip) and unzip them. 

:::

| Dataset                                                       | Source                                                          | Description                                                                                                                                                             |
|---------------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrative boundaries for pakistan                        | [HDX](https://data.humdata.org/dataset/cod-ab-pak)              | The administrative boundaries (adm0-adm3) for pakistan can be accessed via the humanitarian data exchange. For this exercise, we are interested in the districts (adm2) |
| Percent distribution of households by material used for walls | [Pakistan Bureau of Statistics](https://www.pbs.gov.pk/pslm-3/) | Table 7.7 in the *Pakistan Social and living Standards Measurement Survey (2019-20)* shows the materials used for walls per household in percents.                      |


### Task 1: Get the data from the PDF file into a CSV file <a id="task-1-get-the-data-from-the-pdf-file-into-a-csv-file"></a>

:::{Topic} Context

The data on wall materials has been published by the [STATISTICAL BUREAU PAKISTAN] as a table in a pdf-file. The table in the pdf-file cannot be imported into QGIS as is. First, the table in the PDF needs to be converted into a `.csv`-file. 

:::

1. In your web-browser, go to [Tabula.technology](https://tabula.technology) and download the application.

:::{admonition} Tabula
:type: tldr
Tabula is an open source application that let's you extract data tables from PDF-files as `.csv`-files. The `.csv`-files can be imported into excel, QGIS, or other data manipulation programs. 

:::

:::{figure} ../../../fig/en_tabula_website.png
---
name: en_tabula_website
width: 550 px
---
The Tabula.technology website with the download links to the left.
:::

2. Unzip the downloaded file into a location of your choosing (e.g., Programs, Desktop, ...).
3. Open the folder where you unzipped the file and open the "Tabula" application.

:::{figure} ../../../fig/en_tabula_folder.png
---
name: en_tabula_folder
width: 450 px
---

:::

4. A new browser window will open with this address: http://localhost:8080. This is the application. If the browser does not open automatically, you can open the browser and enter this go to this address manually.


:::{figure} ../../../fig/en_tabula_import.png
---
name: en_tabula_import
width: 550 px
---

:::

5. Now let's import the PDF file with the wall types into tabula:  
    1. Click on `Browse` and navigate to the exercise data folder: `...\data\input` and select the PDF "pakistan_wall_type7.7". Click `Open`.
    2. Click `Import` and wait for the PDF to load. Once loaded, it will open automatically.

:::{figure} ../../../fig/en_Tabula_main_view.png
---
name: en_Tabula_main_view
width: 550 px
---

:::

6. Here we will select the portion of the PDF that contains the data table. Tabula expects a table with one row of headers at the top for each column, followed by the rows with the data. By dragging a rectangle on the PDF, we can create a selection where tabula should look for the data table. Drag a rectangle and adjust the boarders so the table fits as precisely as possible into selection. Make sure to only capture the relevant information. Since the headers in this table has an unconventional formatting, it should be left out so the resulting csv table is easier to adjust. We will add the headers manually once extracted.

:::{figure} ../../../fig/en_tabula_selection.png
---
name: en_tabula_selection
width: 550 px
---

:::

7. Once you are satisfied with the selection, you can click on `Repeat this Selection` to duplicate the selection on the next pages. 
8. Take a look on the following pages and make sure the table is still fully contained by the selection.
9. Click on `Preview & Export Extracted Data` on the top right of the window.
10. A new window will appear where the data will show up. At first, nothing will be visible. First, click on `Stream` on the left.

:::{figure} ../../../fig/en_tabula_preview_extracted_1.png
---
name: en_tabula_preview_extracted_1
width: 550 px
---

:::

11. The data from the PDF table will appear in the main window. Review the table.

:::{figure} ../../../fig/en_tabula_data_preview.png
---
name: en_tabula_data_preview
width: 550 px
---

:::

12. Click on `Export`, this will save the `.csv` into your downloads folder. 
13. Move the file to the `/data/interim/`-folder.


Congratulations, the data from the PDF has been extracted into a CSV file!

### Task 2: Clean the CSV file <a id="task-2-clean-the-data-from-errors-and-unwanted-entries"></a>

:::{topic} Context
Tabula reads the table line by line from the PDF. Where the columns in the PDF are close together, it doesn't always split the values correctly. It also copies everything in the table, including rows we don't need. Before we load the CSV into QGIS, we need to check it and fix these problems. Otherwise, QGIS reads some columns wrongly, or some districts can't be joined to the district polygons later.
:::

:::{attention}
For this task, use the prepared file `tabula-pakistan_wall_type7.7_training.csv` from the exercise data folder (`data/input/`). It's the Tabula output where most of the problems have already been fixed, so you only have to fix a few rows.

If you extracted the table yourself in Task 1, your file has more problems. See the dropdown "If you extracted the CSV yourself" at the end of this task.
:::

1. Open `tabula-pakistan_wall_type7.7_training.csv` in a spreadsheet editor such as Microsoft Excel or LibreOffice Calc.

:::{note}
If Excel shows all values in column A, select column A and go to `Data` → `Text to Columns` (in the web version of Excel: `Data` → `Split Text to Columns`). Leave the settings as they are and click `OK`.
:::

2. Go through the table and look for these problems:

:::{admonition} What went wrong in the extraction?
:class: note

| Problem                                  | Rows affected                                                                           | Example                                                                                                                                                              | How to fix it                                                                                                                             | What happens in QGIS if you don't fix it                                                                                                                 |
|:-----------------------------------------|:----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Column headers split over three rows** | The first three rows                                                                    | `PROVINCE & DISTRICT, BURNT BRICKS, MUD` in one row, `/BLOCKS, BRICKS/MUD, WOOD, OTHER, TOTAL` in the next, and `MATERIAL USED FOR WALLS` above them                 | Make one header row: `Province & District`, `Burnt Bricks/Blocks`, `Mud Bricks/Mud`, `Wood`, `Other`, `Total`. Delete the other two rows. | QGIS takes the first row as column names, so the columns get the wrong names. The other header rows become data, so all number columns are read as text. |
| **Two numbers in one cell**              | Faisalabad, Lahore                                                                      | `Faisalabad, 97.91, , 1.73 .22, 0.14, 100`: the **Mud** cell is empty, and the values for Mud and Wood are both in the **Wood** cell.                                | Move the first number into **Mud** and keep the second in **Wood**.                                                                       | QGIS reads the whole **Wood** column as text instead of numbers. You can't use it for a map.                                                             |
| **Name and number in one cell**          | Nushki, Sohbatpur                                                                       | `Nushki 24.64, 74.6, 0.76, 0, , 100`: the value for Burnt Bricks/Blocks is attached to the district name, so Mud, Wood and Other are one column too far to the left. | Move **Mud**, **Wood** and **Other** one column to the right, then move the number from the name into **Burnt Bricks/Blocks**.            | The district name is `Nushki 24.64`, so it can't be joined to the district `Nushki`.                                                                     |
| **A name split over two rows**           | Tando Muhammad Khan (Sindh)                                                             | `Tando Muhammad, 35.48, 51.95, 12.02, 0.56, 100` and, in the next row, `Khan` with no values                                                                         | Write the full name `Tando Muhammad Khan` in the first row and delete the second.                                                         | `Tando Muhammad` doesn't join to the district `Tando Muhammad Khan`, and `Khan` is an empty row.                                                         |
| **Rows that are not districts**          | `Pakistan`, `Punjab`, `Sindh`, `Khyber Pakhtunkhwa`, `Balochistan`, the note at the end | `Punjab, 91.72, 7.06, 0.37, 0.85, 100`                                                                                                                               | Delete these rows. We only want one row per district. Read the note first: it lists the districts that are missing from the survey.       | Extra rows that don't belong to any district.                                                                                                            |

Values such as `.22` are fine: they mean `0.22`.
:::

3. Fix the rows with these problems. To check your work, add a column that adds up __Burnt Bricks/Blocks__, __Mud Bricks/Mud__, __Wood__ and __Other__, e.g. `=SUM(B2:E2)`. For every district, the result should be about 100. If it isn't, the values in that row are still in the wrong columns. Delete the check column when you're done.

4. Save the file as CSV (`File` → `Save As`, file type `CSV (Comma delimited)`) in the folder `data/interim/` under the name `pakistan_wall_type_clean.csv`. If Excel asks whether to keep the format, choose to keep CSV.

Great! Now we are ready to import the CSV-file into QGIS!

::::{dropdown} If you extracted the CSV yourself

Your own Tabula output has the same problems as the prepared file, but in more rows, and some more:

- **No column headers:** we didn't select the headers in Tabula. Insert a new first row and enter the headings:

  | Province & District | Burnt Bricks/Blocks | Mud Bricks/Mud | Wood | Other | Total |
  |:--------------------|:--------------------|:---------------|:-----|:------|:------|

- **Urban and Rural rows:** below every district, there is one row for urban and one for rural areas. We only need the district totals. Select the table, go to `Home` → `Format as Table`, then click the arrow next to "Province & District" and use `Text Filters` → `Begins With...` to show all rows that begin with `Urban`, and then all that begin with `Rural`. Some of these rows have a number attached to the word (e.g. `Urban 55.06`), so "Equals" would miss them. Select the filtered rows, delete them and remove the filter.
- **More district names that don't match the boundaries,** e.g. `Layyah` (in the boundaries: `Leiah`) or `Karachi East` (`East Karachi`). You will find them in Task 4.

Your file may also look slightly different depending on how you drew the selection in Tabula.

:::{figure} ../../../fig/en_m5_data_cleaning_ex_filter_excel.png
---
name: en_m5_data_cleaning_ex_filter_excel
width: 350 px
---
Filtering the rows in Excel.
:::

::::

### Task 3: Import the data into QGIS <a id="task-3-import-the-data-into-qgis"></a>

1. Open QGIS, create a new project and save it in the exercise folder.
2. [Import the cleaned CSV file](../Wiki/en_qgis_import_geodata_wiki.md#text-data-import) `data/interim/pakistan_wall_type_clean.csv`. In the Data Source Manager:
    1. Under `Geometry Definition`, select `No geometry (attribute only table)`. Our CSV has no coordinates, only district names.
    2. Under `Record and Fields Options`, make sure `Detect field types` is checked.
    3. Click `Add`.
3. Import the administrative boundaries `pak_admbnda_adm2_wfp_20220909.shp` from the folder `data/input/pak_adm_wfp_20220909_shp/`.
4. Check that QGIS has read the numbers as numbers: <kbd>Right-click</kbd> on the CSV layer → `Properties` → `Fields`. __Burnt Bricks/Blocks__, __Mud Bricks/Mud__, __Wood__ and __Other__ should have the type `double` (a decimal number). If one of them is `text` or `string`, a cell in that column still has a problem. Fix it in the spreadsheet, save the CSV, remove the layer and import it again.

### Task 4: Join the data to the districts <a id="task-4-join-the-data-to-the-districts"></a>

:::{topic} Context
To show the data on a map, we attach the CSV to the district polygons with a [non-spatial join](../Wiki/en_qgis_non_spatial_joins_wiki.md). QGIS links the rows where the district name in the CSV is __exactly__ the same as the district name in the boundary layer (`ADM2_EN`). `D.G Khan` doesn't join with `Dera Ghazi Khan`, and nothing tells you so: the district is just empty. That's why we first check which districts don't join.
:::

1. Open the processing toolbox, search for __"Join attributes by field value"__ and <kbd>double-click</kbd> on it.
2. Set the following parameters:
    1. __Input layer:__ `pakistan_wall_type_clean` (the CSV)
    2. __Table field:__ `Province & District`
    3. __Input layer 2:__ `pak_admbnda_adm2_wfp_20220909`
    4. __Table field 2:__ `ADM2_EN`
    5. __Layer 2 fields to copy:__ `ADM2_PCODE`
    6. __Unjoinable features from first layer:__ click on the arrow next to the field and select `Create Temporary Layer`.
3. Click `Run`. In the `Log` tab, you can see how many rows were joined and how many weren't.
4. Open the attribute table of the new layer `Unjoinable features from first layer`. These are the districts whose name in the CSV doesn't exist in the boundary layer. You should find four:
    - `D.G Khan` and `Karachi central`
    - `Chitral` and `Kohistan`
5. Open the attribute table of `pak_admbnda_adm2_wfp_20220909` and click on the column header `ADM2_EN` to sort the names. Look for the correct names:
    - `D.G Khan` is `Dera Ghazi Khan`, and `Karachi central` is `Central Karachi`.
    - `Chitral` and `Kohistan` don't exist anymore: in the boundary layer, they have been split into smaller districts (`Chitral Lower`, `Chitral Upper`, `Kohistan Lower`, `Kohistan Upper`, `Kolai Palas Kohistan`). The boundaries changed after the survey, so we can't fix this by changing the name. We leave these two as they are.
6. QGIS can't edit CSV files directly, so we first save the table in an editable format: <kbd>Right-click</kbd> on the CSV layer → `Export` → `Save Features As...`. Set `Format` to `GeoPackage` and save it as `data/interim/pakistan_wall_type_clean.gpkg`. Click `OK`. The new layer is added to your project.
7. Select the new layer, click on the pencil icon (`Toggle Editing`) and open its [attribute table](../Wiki/en_qgis_attribute_table_wiki.md#attribute-table-data-editing). <kbd>Double-click</kbd> on `D.G Khan` and change it to `Dera Ghazi Khan`. Change `Karachi central` to `Central Karachi`. Click on `Save Edits` and turn off the editing mode.
8. Now join the data to the district polygons. Open __"Join attributes by field value"__ again and set:
    1. __Input layer:__ `pak_admbnda_adm2_wfp_20220909`
    2. __Table field:__ `ADM2_EN`
    3. __Input layer 2:__ `pakistan_wall_type_clean` (the GeoPackage layer)
    4. __Table field 2:__ `Province & District`
    5. __Layer 2 fields to copy:__ `Burnt Bricks/Blocks`, `Mud Bricks/Mud`, `Wood`, `Other`
    6. __Joined layer:__ save it as `data/output/pakistan_wall_type_districts.gpkg`
9. Click `Run`.

Congratulations, we have now joined the information from the PDF file to the district polygons!

:::{note}
The `Log` tab still shows quite a few polygons that weren't joined. That's expected: these districts have no data in the survey. They are
- the districts in Azad Kashmir and Gilgit-Baltistan, which the survey doesn't cover,
- the five districts in the note at the end of the CSV,
- Chitral and Kohistan, and the districts Chaman and Lehri, which were created after the survey.

Not every missing value is a mistake. But always check *why* something didn't join.
:::

### Task 5: Visualisation of the Data <a id="task-5-visualisation-of-the-data"></a>

:::{topic}

We now have a polygon layer containing the information on the wall material per district. We can create a map showing the share of households that have, for example, burnt bricks or blocks as wall material.

:::

1. Open the layer styling panel for the joined layer and select the __Graduated__ symbolisation method.
2. Under `Value`, select `Burnt Bricks/Blocks`.
3. Click on `Classify`.

The resulting symbolisation could look something like this:

:::{figure} ../../../fig/m5_ex_7_visualisation_result.png
---
name: m5_ex_7_visualisation_results
width: 600 px
---
The darker the colour, the higher the percentage of households having burnt bricks or blocks as wall type. The grey areas are the districts where there is no data available.
:::
