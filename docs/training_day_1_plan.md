# Intermediate training: plan for day 1

Status: draft, 29 October 2026.

Theme of the day: **getting data into shape and creating your own.** Trainees clean a table and join
it to admin boundaries, see what broken geometries are and how to fix them, digitise new data with
their own attribute fields, and finally think about which spatial data their own operations need.

## Overview

| # | Block                                       | Format                       | Time      |
|---|---------------------------------------------|------------------------------|-----------|
| 0 | Welcome and warm-up                         | Plenary                      | 30 min    |
| 1 | Cleaning a CSV and joining it to boundaries | Follow-along exercise        | 1.5 h     |
| 2 | Broken geometries and how to fix them       | Short theory + live demo     | 15 min    |
| 3 | Digitising and adding fields                | Follow-along exercise        | 1.5 h     |
| 4 | Group work: which spatial data do we need?  | Groups + short presentations | 30–40 min |
| 5 | Wrap-up                                     | Plenary                      | 15 min    |

That's about 4.5 h of content. With breaks and lunch it fills a training day; if the day is
shorter, shorten block 3 first (fewer features to digitise).

## 0. Welcome and warm-up (30 min)

- Introductions, goals of the training, programme of the day.
- Introduce the Community of Practice (CoP).

**Talking points for the introduction:**

> I'm glad to have the opportunity to be here with you. We want this training to be a space
> where everybody learns, including us. We're here in the role of GIS experts, but we'd like to
> learn from your experience too. We might know more about GIS, but you will most definitely know
> more about humanitarian operations. It's great when we can share that with each other.
>
> That's also what the Community of Practice is made for: a place to keep sharing questions,
> experiences and examples after this training is over.

This also sets up the group work in block 4, where trainees bring in examples from their own
operations.

- Check that everyone has QGIS installed and the data folder downloaded **and unzipped**.
- Quick baseline check: let trainees load a layer, open the attribute table and change the style.
  On day 1 of an intermediate training, levels vary a lot. This shows you who might need help.

## 1. Cleaning a CSV and joining it to boundaries (1.5 h)

Based on [Data preparation](../content/en/Module_5/en_qgis_data_preparation_ex.md) (Module 5),
**without the Tabula steps** (Task 1).

**Preparation:** extract the table from the PDF with Tabula yourself and give trainees the raw,
uncleaned CSV. Don't clean it: the errors in it are the exercise (missing headers, Urban/Rural rows,
values shifted into the wrong column).

**Steps:**

1. Open the raw CSV in a spreadsheet editor and clean it (Task 2 of the exercise): add the headers,
   remove the Urban/Rural rows, move the shifted values back into the right columns.
2. Import the cleaned CSV and the admin boundaries (adm2) into QGIS.
3. Try a plain attribute join on the district names first. Filter the result for `NULL` values:
   several districts did not join because the names are spelled differently.
4. Use the fuzzy-merge expression from the exercise (Task 3) to match the names, then join again
   and check the `NULL` values once more.
5. Style the result as a graduated map (Task 4).

**Key messages:**

- Data from reports and PDFs almost always needs cleaning before it can be used.
- Always check what did *not* join. A join that "worked" can still silently drop features.

## 2. Broken geometries and how to fix them (15 min)

No exercise for the trainees: you show it, they watch. Later in the training there is an exercise
where they have to fix a broken layer themselves.

**Preparation:** a flood extent layer with a few invalid polygons (see
[Preparing the broken layer](#preparing-the-broken-layer)). Check beforehand that the analysis below
fails with the broken layer and works after fixing it.

**Theory (about 5 min):**

- A polygon is *valid* if its outline is closed and doesn't cross itself, and its holes lie inside
  it without overlapping. The classic invalid polygon is the "bow-tie": an outline that crosses
  itself like a figure eight.
- Where broken geometries come from: converting rasters to polygons (flood extents are a typical
  example), careless digitising, simplifying or reprojecting data, and data passed between
  different programs and formats.
- What it means: many tools (Clip, Intersection, Dissolve, ...) stop with the error
  "Feature has invalid geometry". The errors are often tiny and not visible on the map.
- Gaps and overlaps between neighbouring polygons are a different problem: the polygons are each
  valid, so `Fix geometries` does not touch them. Snapping helps avoid them (block 3).

**Live demo (about 10 min):**

1. Run an analysis with the broken flood layer, e.g. `Intersection` with the districts from
   block 1 to get the flooded area per district. It fails with "Feature has invalid geometry".
2. Run `Check validity`. Show the output layer with the error locations and zoom to one of them.
3. Run `Fix geometries` on the flood layer.
4. Run the analysis again with the fixed layer: it works.
5. Briefly show the setting *Settings → Options → Processing → General → Invalid features
   filtering*. Warn against setting it to "Skip": the analysis then runs, but silently leaves out
   the broken features.

**Key message:** this happens often, it's not your fault, and it's an easy fix. When a tool
complains about invalid geometries, run `Fix geometries` and try again.

## 3. Digitising and adding fields (1.5 h)

Based on the digitising exercises in Module 3
([en_qgis_digitalisation_ex.md](../content/en/Module_3/en_qgis_digitalisation_ex.md),
[en_qgis_digitalisation_ex1.md](../content/en/Module_3/en_qgis_digitalisation_ex1.md)).

**Steps:**

1. **Plan the fields before digitising.** Decide what to collect and which field type each
   attribute needs (text, whole number, decimal, date).
2. Create a new GeoPackage layer with these fields.
3. Set up a dropdown (`Value Map` widget in the layer properties under `Attributes Form`) for at
   least one field, so values are chosen from a list instead of typed.
4. Digitise points, lines or polygons and fill in the attributes.
5. Add a field to the existing layer afterwards with the field calculator or the attribute table.
6. Digitise two neighbouring polygons once with snapping off and once with snapping on, and compare.
   Without snapping you get gaps and overlaps; this links back to block 2.

**Key messages:**

- The structure of your data (fields, types, allowed values) matters as much as the geometry.
  Define it before you start collecting.
- Dropdowns make data consistent: no different spellings of the same value.

## 4. Group work: which spatial data do we need? (30–40 min)

Groups of 3–5 people, 10–15 min of discussion, then about 3 min per group to present.

**Task:** think of an operation where you had to collect geodata, or where it would have helped to
have spatial data. Fill in the template for one dataset:

| Question                                    | Your answer |
|---------------------------------------------|-------------|
| Operation / situation                       |             |
| What objects do you want to map?            |             |
| Geometry type: point, line or polygon? Why? |             |
| Attributes (5–8) and their type             |             |
| Which attributes should be dropdowns?       |             |
| Who collects the data, how, and when?       |             |

The template keeps the discussion on *spatial* data: choosing the geometry type forces the groups
to think about where things are, not only what they are.

If the training covers mobile data collection later, keep the results: the groups can build these
data models in that session.

## 5. Wrap-up (15 min)

- Summary of the day: clean and join, fix geometries, digitise with a planned data structure.
- Open questions.
- Outlook on day 2.

## Preparing the broken layer

Two options:

- **By hand:** in QGIS, turn off snapping and set *Settings → Options → Digitizing → Validate
  geometries* to Off. Use the Vertex Tool to drag a vertex across the opposite edge of a polygon.
  Repeat for 5–10 features and save as a new file.
- **With a script:** a PyQGIS script that swaps two neighbouring vertices in a number of random
  polygons. This creates small bow-tie errors that are almost invisible on the map but make the
  analysis fail. Run it in the QGIS Python console with the clean flood layer selected.

Before you break anything, run `Check validity` on the original flood layer: flood extents
converted from rasters are often invalid already.
