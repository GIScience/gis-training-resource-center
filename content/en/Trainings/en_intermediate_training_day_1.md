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
We are here as GIS experts, but you know much more about humanitarian operations than we do. We want this training to be a place where everybody learns, including us. This is also the idea behind the **[Community of Practice](https://communities.ifrc.org/group/6a01da67c5a0bc3411f33cda/timeline)**: a place to keep sharing questions, experiences and examples after the training.
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

::::{grid} 1
:gutter: 2

:::{grid-item-card} 1. Cleaning and joining data
:img-top: ../../../_static/icons/ifrc-icon-checklist.svg
:class-img-top: ifrc-card-icon
:img-alt:
Data from reports and PDFs is rarely ready to use. You clean a table on household wall materials in Pakistan, import it into QGIS and join it to the district boundaries. Afterwards, you check which districts did *not* join, and why.

* [Data preparation exercise](../Module_5/en_qgis_data_preparation_ex.md)
* [Import CSV files](../Wiki/en_qgis_import_geodata_wiki.md#text-data-import)
* [Join attributes by field value](../Wiki/en_qgis_non_spatial_joins_wiki.md#join-attributes-by-field-value)
:::

:::{grid-item-card} 2. Broken geometries
:img-top: ../../../_static/icons/ifrc-icon-plaster.svg
:class-img-top: ifrc-card-icon
:img-alt:
Sometimes a layer contains invalid geometries, for example a polygon whose outline crosses itself. Tools such as Clip or Intersection then stop with an error. This happens often, it's not your fault, and it's an easy fix: run `Fix geometries` and try again.

* [Invalid geometry](../Wiki/en_qgis_common_errors_and_Issues.md#invalid-geometry)
:::

:::{grid-item-card} 3. Digitising and adding fields
:img-top: ../../../_static/icons/ifrc-icon-map-pin.svg
:class-img-top: ifrc-card-icon
:img-alt:
You create a new layer, plan its attribute fields, set up a dropdown list for consistent values, and draw your own features. You also see how snapping helps to avoid gaps and overlaps.

* [Digitisation](../Wiki/en_qgis_digitisation_wiki.md)
* [Creating a new layer](../Wiki/en_qgis_digitisation_wiki.md#creating-a-new-layer)
:::

:::{grid-item-card} 4. Which spatial data do we need?
:img-top: ../../../_static/icons/ifrc-icon-idea.svg
:class-img-top: ifrc-card-icon
:img-alt:
In small groups, think of an operation where you had to collect geodata, or where spatial data would have helped. Design one dataset with the [questions below](#group-work-questions) and present it to the others.
:::

::::

:::{figure} ../../../fig/m5_ex_7_visualisation_result.png
---
width: 500px
name: en_training_day_1_wall_material_map
---
The result of session 1: share of households with walls made of burnt bricks or blocks per district in Pakistan. The grey districts have no data after the join. Finding out why is part of the exercise.
:::

### Group work questions <a id="group-work-questions"></a>

| Question                                    | Your answer |
|---------------------------------------------|-------------|
| Operation / situation                       |             |
| What objects do you want to map?            |             |
| Geometry type: point, line or polygon? Why? |             |
| Attributes (5–8) and their type             |             |
| Which attributes should be dropdowns?       |             |
| Who collects the data, how, and when?       |             |

## Questions? <a id="questions"></a>

<img src="../_static/icons/ifrc-icon-question.svg" class="ifrc-side-icon" alt="">There are no silly questions. Ask during the sessions, in the breaks, or at the end of the day in the wrap-up. And if a question comes up after the training, bring it to the Community of Practice.
