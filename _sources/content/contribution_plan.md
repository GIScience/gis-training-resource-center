# Contribution Plan for the IFRC GIS Training Platform

## Introduction

Thank you for your interest in contributing to the IFRC GIS Training Resource Center.
This page <!--Document-->outline the contribution process and guideline for collaborating with the GIS Training Resource Center. It provides details for contributions and related best practices. Whether you're looking to add new content, contribute to existing material, or collaborate on enhancing the platform overall as a partner, this guide will help to understand the necessary steps.

:::{admonition} TEST
:class: note
:::

## Collaborations

### Content

Collaborators are encourages to propose new topics or content relevant to the GIS Training Resource Center. These topics should align with the training objectives for Anticipatory Action (AA), Information Management and focus on basic GIS operations. If you have a topic in mind, please send a brief introduction and key points to `gis-training-platform@heigit.org` to initiate collaboration.

To help us understand and evaluate your proposal, kindly consider the following three guiding questions: 

1. __What level of GIS expertise is required for the proposed content?__
2. __What is the main learning objective or added value of the proposed content?__
3. __Will you be adding the content to the training platform yourself (in markdown), or would you require support?__

We will review and assess each idea on a case-by-case basis.

### Interested in becoming a Partner or Supporter of the Training Resource Platform?

The GIS Training Working Group behind the IFRC GIS Training Resource Center was established by the British, German, and Netherlands Red Cross Societies, with technical support from the Heidelberg Institute for Geoinformation Technology (HeiGIT).

In addition to content contributions, this consortium welcomes new partners from the Red Cross and Red Crescent Movement. We also encourage contributions in the form on in-kind or financial support to help further develop and drive continuous improvement of the platform. 

## Content Contribution Guidelines

### Your contribution

- __Markdown MyST and Jupyter Book:__ In addition to CommonMark Markdown, Jupyter Book also supports a more fully-featured version of Markdown called __MyST Markdown__. This is a superset of CommonMark that includes syntactic pieces that are useful for publishing computational narratives. For more information about MyST Markdown, see [MyST Markdown overview].(https://jupyterbook.org/en/stable/content/myst.html).
- __Changes on the Dev-Branch:__
    - All changes must be pushed to the `dev` branch. These changes will be reviewed by HeiGIT and/or RC before a pull request is merged.
    - Currently, only HeiGIT or RC are authorized to create pull requests and contributors can request reviews from HeiGIT and/or RC via GitHub.
- __New Content:__
    - If you have ideas for new content (either as new sections in existing modules or new standalone modules), send us an email or submit an issue in github using the appropriate tags. A proposal may also include a markdown page or suggested structure. 
    - New content proposals will undergo review, and contributors are encouraged to actively engage with reviewers via GitHub issues. For deeper discussions about content or collaborations, HeiGIT/RC are happy to schedule video calls.
- __External Data Submission:__
    - If you need to send data or other materials, you can email them to `gis-training-platform@heigit.org` to be uploaded to the Nexus Data Repository.

### Licences

- __Copyright and Data Sources:__ Always provide clear citations for any external material, including articles, books, and web content. For articles and books, include the full citation with DOI. For webpages, include the source URL (external links must be maintained)
- All content within the platform will be published under the __[CC 4.0 BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)__ license

### Ideal Structure for New Content

The structure of new modules/chapters should ideally include:

1. __Theory:__ Introduction to key concepts.
2. __Practical Examples:__ Demonstrate how to apply concepts in Anticipatory Action, Information Management, and QGIS.
3. __Exercises:__ Hands-on practice with follow-along exercises.
4. __Synthesis:__ A more complex exercise or example that synthesizes the module content
5. __Self-Assessment Questions:__ To test comprehension of the module's main concepts

### Types of Content

- __Theory:__ Explanation of concepts. 
- __Real World Examples:__ Include practical examples that are relevant to the GIS field (preferably related to IM, AA, or humanitarian work in general). 
- __Exercises:__ Follow-along or self-guided exercises to reinforce learning.
- __Discussion Questions:__ Promote interaction and connection to real-world scenarios. 
- __Wiki:__ Brief articles that provide explanations or instructions related to the platform.
- __Figures:__ Pictures or figures to illustrate theoretical concepts, real world examples or show screenshots 
- __Videos:__ The platform uses short videos without commentary to show how to perform certain steps (e.g., edit the attribute table, import layers, or set the symbology of a layer)

```{note}
Keep in mind that there are many detailed GIS resources as well as official documentation. Explain the necessary theory for trainees to perform the tasks. You can also refer to external resources. 
```

### Exercise Guidelines

- __Instructions:__ Provide step-by-step instructions.
- __Facilitator Notes:__ Include notes for facilitators on how to guide the exercise.
- __Data:__ Always provide a link to the dataset(s) used in the exercise. Ensure the dataset is cleaned of personal data and errors unless data cleaning is part of the exercise.

:::{note}
Contributors are encouraged to upload videos for step-by-step guides where useful.
:::

## File naming and Formatting Guidelines

Follow these guidelines for naming files and structuring directories: 

- __Naming:__ Choose descriptive names. Ensure that exercises are numbered correctly (e.g. `module_#_ex#_title`). The exercise number should be the next available number
- __Folder Structure:__ Ensure that exercise data follows the [correct folder structure](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projects_folder_structure_wiki.html#standard-folder-structure) and is zipped correctly (avoid excessive folder nesting as this can lead to problems when unzipping)
- __Language and QGIS Version:__ Always include the QGIS version and language in the file names.
- __Pictures:__ All pictures and figures have to be stored in the folder `/fig/`.
    - General common pictures just have to have a sort and informative title.
        - Picture name example: HeiGIT_logo_compact.svg
    - In the case of a screenshot of QGIS or another program, additional rules apply.  First, the abbreviation of the used language has to be included (e.g. en). Second, the QGIS version (e.g. 3.28).
        - Screenshots name example: en_3.29_clip_tool.png
    - In instances of pictures of the OSM or satellite imagery, one has to include the year and place.
        - Picture of maps or satellite imagrey example: OSM_Heidelberg_2023.png

Follow these guidelines when creating and formatting content: 

- __Spelling:__ Use British English spelling.
- __Headings:__ 
    - `# Title` for the main titles of markdown pages
    - `## Title` for sections
    - `### Title` for subsections
    - Avoid headings deeper than H3 (`### Title`). Use bold, underlining or put it into cards to achieve a similar effect.
- __Links:__
    - In Markdown, you can embed links into text by using `[text/name](link)`
- __Figures and Images:__
    - Images and videos are saved to the `/fig/`-folder.
    - Use the figure directive for images:
        ```
        :::{figure} /fig/example.png
        ---
        name: example_figure
        width: 750 px
        align: center/left/right
        ---
        Descriptive Caption including source of the image
        :::
        ```
    - `name` must indicate a unique descriptive name. You can refer to figure in text by using: 
        ```
        {numref}`name`
        ```
        - This does not work in pages that are not included in the `TOC.yml`-file
    - ``width` specifies the pixel width. The maximum amount of pixels for width is 750 px. Alternatively, you can use `height`. Be careful to set high values as this will distort the image once it reaches the 750 px width cap.
    - align specifies where the image should be rendered on the markdown page. E.g., `align: left` can be used to align the image to the left part of the page and leave space for text on the right.
    - The caption should describe what is seen on the figure in the context of the section. The image sources must be specified as precisely as possible.
    - It is possible to embed icons into the text by using `![](/fig/FILENAME)`. Make sure the icon height does not exceed 30 pixels. 
- __Admonitions:__
    - Use admonitions such as note, caution, tip, tldr for additional notes such as
    ```
    :::{admonition} TITLE
    :class: tip, caution, note, tldr, note
    CONTENT
    :::
    ```
- __Dropdowns:__ For optional content (e.g. videos or supplementary information), use dropdowns: 
    ```
    :::{dropdowns} TITLE
    CONTENT
    :::
    ```
- __Cards:__ Use the card directives to highlight content in a "card": 
```
:::{card}
HEADER
^^^
CONTENT
:::
```
- __Grids:__ To create several columns to display content or images side by side, you can create grids:
```
::::{grid} 2

:::{card}

:::

:::{card}

:::

::::
```

- __Margins:__ Sometimes, it can be useful to put hints or additional information into the margin to the right. This can be achieved with the following directive:
    ```
    ::::{margin}
    CONTENT (can include other directives)
    ::::
    ```

:::::{admonition} Nesting directives
:class: tip 
It is possible to nest directives such as figures inside of cards or admonitions. Simply use more colons around directives that enclose other such as:

```

::::{card}
HEADER
^^^
CONTENT

:::{figure} /fig/figure.png
---
name:
width:
align:
---
CAPTION
:::

::::

```

:::::


- __Embedding Videos:__ Videos need to be embedded using HTML-code: 
    ```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>
    ```
    - copy the code and enter the name of the video file you want to embed.

- __Text formatting standards:__
    - When describing a process, use numbers. For example:
        ```
        1. Right-click on "ML1_IPC_Index" layer -> `Attribute Table`-> click on  [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) to open the field calculator
        2. Check `Create new field`
        3. `Output field name`: Name the new column “Trigger_activation”
        4. `Result field type`: Text (string)
        ```
    - __All clickable surface has to be written as code snippets e.g. `Attribute Table`__
    - If a special icon is used in QGIS, place it next to the code snippets e.g `Field Calculator` ![](/fig/icon_scratch_layer.png).
    - If an option needs to be selected, write the click surface name in code snippet and the option as normal text e.g. `Result field type`: Text (string)
    - If something like a file name has to be named in a certain way use quotation marks e.g. `Output field name`: Name the new column “Trigger_activation”
    - Where it makes sense add the link to the relevant wiki video when the participants should use a tool or a functionality that is not in detail described in your current step-by-step guide either by linking the tool name e.g. [drag and drop](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop) or by using something like ([Wiki basemap](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html))