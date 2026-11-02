---
orphan: true
---

# Intermediate training: Day 1 <a id="intermediate-training-day-1"></a>

Welcome to the first day of the training! Today is about **getting data into shape and creating your own**: we clean a table and join it to administrative boundaries, look at what broken geometries are and how to fix them, digitise new data, and think together about which spatial data your own operations need.

::::{grid} 1
:gutter: 2

:::{grid-item-card} A space to learn from each other
:img-top: ../../../_static/icons/ifrc-icon-community.svg
:class-img-top: ifrc-card-icon
:img-alt:
Let's use this space to learn from each other. The training is mainly about GIS skills, but these go hand in hand with your knowledge of humanitarian operations: without knowing the context, we can't develop GIS solutions that really help. So bring your experience, your questions and examples from your own work.

To keep sharing after the training, join the **[Community of Practice](https://communities.ifrc.org/group/6a01da67c5a0bc3411f33cda/timeline)**.
:::

:::{grid-item-card} Before we start
:img-top: ../../../_static/icons/ifrc-icon-laptop.svg
:class-img-top: ifrc-card-icon
:img-alt:
* Install [QGIS](../Wiki/en_qgis_installation_wiki.md) on your laptop.
* Download the exercise data and **unzip** the folder before the first exercise.
:::

::::

## Programme <a id="programme"></a>

| # | Session                                              | Format                        |
|---|------------------------------------------------------|-------------------------------|
| 0 | Welcome, introductions and the Community of Practice | Plenary                       |
| 1 | Cleaning a CSV file and joining it to boundaries     | Exercise                      |
| 2 | Broken geometries and how to fix them                | Short input and demonstration |
| 3 | Digitising and adding fields                         | Exercise                      |
| 4 | Which spatial data do we need?                       | Group work                    |
| 5 | Wrap-up and questions                                | Plenary                       |

## Sessions <a id="sessions"></a>

:::::{grid} 1
:gutter: 2

::::{grid-item-card} 1. Cleaning and joining data
:img-top: ../../../_static/icons/ifrc-icon-checklist.svg
:class-img-top: ifrc-card-icon
:img-alt:
Data from reports and PDFs is rarely ready to use. You clean a table on household wall materials in Pakistan, import it into QGIS and join it to the district boundaries. Afterwards, you check which districts did *not* join, and why.

* [Data preparation exercise](../Module_5/en_qgis_data_preparation_ex.md)
* [Import CSV files](../Wiki/en_qgis_import_geodata_wiki.md#text-data-import)
* [Join attributes by field value](../Wiki/en_qgis_non_spatial_joins_wiki.md#join-attributes-by-field-value)

:::{figure} ../../../fig/m5_ex_7_visualisation_result.png
---
width: 500px
name: en_training_day_1_wall_material_map
---
The result of session 1: share of households with walls made of burnt bricks or blocks per district in Pakistan. The grey districts have no data after the join. Finding out why is part of the exercise.
:::

:::{tip} Names that don't match
District names are often spelled slightly differently in two datasets, so the join leaves them out. A **fuzzy merge** finds names that are almost the same, using the `levenshtein()` function in the field calculator. See [Task 3 of the data preparation exercise](../Module_5/en_qgis_data_preparation_ex.md#task-3-import-the-data-into-qgis).
:::

:::{dropdown} Using AI for data cleaning
AI assistants such as ChatGPT, Claude or Copilot in Excel can save a lot of time when cleaning data. They are good at:

* writing an Excel formula, a QGIS expression or a small script
* explaining an error message
* suggesting which differently spelled names probably mean the same place
* reading a table from a screenshot or a scanned PDF

Keep these cautions in mind:

* **Check the result.** AI can make up values or quietly change them. Always compare with the original data.
* **Protect sensitive data.** Don't upload personal or sensitive data, such as beneficiary lists or household locations, unless your organisation's policy allows it.
* **Let AI write the steps, not clean the data for you.** A formula or script can be checked and run again on new data. Data that AI cleaned for you can't.
:::
::::

::::{grid-item-card} 2. Broken geometries
:img-top: ../../../_static/icons/ifrc-icon-plaster.svg
:class-img-top: ifrc-card-icon
:img-alt:
Sometimes a layer contains invalid geometries, for example a polygon whose outline crosses itself. Tools such as Clip or Intersection then stop with an error. This happens often, it's not your fault, and it's an easy fix: run `Fix geometries` and try again.

* **What is a valid polygon?** Its outline is closed and doesn't cross itself, and any holes lie inside it without overlapping. The classic invalid polygon is the "bow-tie": an outline that crosses itself like a figure eight.
* **Where do broken geometries come from?** Converting rasters to polygons (flood extents are a typical example), careless digitising, simplifying or reprojecting data, and passing data between different programs and formats.
* **How do you find them?** The errors are often tiny and not visible on the map. `Check validity` shows you where they are.
* **Gaps and overlaps** between neighbouring polygons are a different problem: each polygon is valid, so `Fix geometries` doesn't change them. Snapping helps to avoid them (session 3).

* [Invalid geometry](../Wiki/en_qgis_common_errors_and_Issues.md#invalid-geometry)
::::

::::{grid-item-card} 3. Digitising and adding fields
:img-top: ../../../_static/icons/ifrc-icon-map-pin.svg
:class-img-top: ifrc-card-icon
:img-alt:
You create a new layer, plan its attribute fields, set up a dropdown list for consistent values, and draw your own features. You also see how snapping helps to avoid gaps and overlaps.

* [Digitisation](../Wiki/en_qgis_digitisation_wiki.md)
* [Creating a new layer](../Wiki/en_qgis_digitisation_wiki.md#creating-a-new-layer)
::::

::::{grid-item-card} 4. Which spatial data do we need?
:img-top: ../../../_static/icons/ifrc-icon-idea.svg
:class-img-top: ifrc-card-icon
:img-alt:
In small groups, think of an operation where you had to collect geodata, or where spatial data would have helped. Design one dataset with these questions and present it to the others.

| Question                                    | Your answer |
|---------------------------------------------|-------------|
| Operation / situation                       |             |
| What objects do you want to map?            |             |
| Geometry type: point, line or polygon? Why? |             |
| Attributes (5–8) and their type             |             |
| Which attributes should be dropdowns?       |             |
| Who collects the data, how, and when?       |             |

**Some ideas:** damaged buildings after an earthquake, flooded areas or areas that flood regularly, roads and bridges that can or can't be used, water points and latrines, health facilities, or evacuation centres.

**How to collect it?** Some things can only be known on site, such as whether a water point works. A form in KoboToolbox is good for that. Other things can be seen from above, such as buildings or flooded areas, and can be digitised in QGIS from imagery. Often the best answer combines both.
::::

::::{grid-item-card} 5. Wrap-up and questions
:img-top: ../../../_static/icons/ifrc-icon-question.svg
:class-img-top: ifrc-card-icon
:img-alt:
We look back at the day together. There are no silly questions: ask during the sessions, in the breaks, or here in the wrap-up. And if a question comes up after the training, bring it to the [Community of Practice](https://communities.ifrc.org/group/6a01da67c5a0bc3411f33cda/timeline).
::::

::::{grid-item-card} What's next
:img-top: ../../../_static/icons/ifrc-icon-graduation-cap.svg
:class-img-top: ifrc-card-icon
:img-alt:
In the next session, Alexei and Melanie will work with you on attribute tables: how to edit fields, perform calculations, filter the data, join the data and reclassify it.

* [Attribute table](../Wiki/en_qgis_attribute_table_wiki.md)
* [Data classification](../Wiki/en_qgis_data_classification_wiki.md)
::::

:::::
