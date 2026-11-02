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
4. Match the names with the fuzzy-merge expression from
   [Task 3 of the exercise](../content/en/Module_5/en_qgis_data_preparation_ex.md#task-3-import-the-data-into-qgis)
   (steps 5–8): in the field calculator, `levenshtein()` finds the district name in the boundaries
   that differs by at most 2 characters. Join again on this new field and check the `NULL` values
   once more.
5. Style the result as a graduated map (Task 4).

**Key messages:**

- Data from reports and PDFs almost always needs cleaning before it can be used.
- Always check what did *not* join. A join that "worked" can still silently drop features.

**Other cleaning tools (mention, about 5 min):**

- **Getting tables out of PDFs:** Tabula, or *Get Data → From PDF* in Excel (Microsoft 365).
- **Spreadsheets:** Excel or LibreOffice Calc (`TRIM`, Text to Columns, Remove Duplicates, filters).
  Power Query in Excel records the steps, so the same cleaning can be repeated on next month's
  report.
- **[OpenRefine](https://openrefine.org/):** free; its *clustering* finds and merges different
  spellings of the same name ("D.G. Khan" / "Dera Ghazi Khan"), the problem from this block.
- **QGIS:** field calculator, `levenshtein()` and `soundex()` for names, `Fix geometries` for
  shapes.
- **Python or R** (pandas, GeoPandas, tidyverse): for large or repeated jobs.
- **AI assistants:** useful to write a formula, QGIS expression or script. Always check the result,
  and don't upload personal or sensitive data unless your organisation allows it.

Better than cleaning: avoid the problem. Collect data with **P-codes** from the Common Operational
Datasets (on HDX) instead of place names, and use dropdowns in Kobo forms (block 3).

### 1.2 More Data cleaning

Data people usually talk about three groups of tools: tools that get the data out of a PDF, tools that clean it, and tools that keep it from getting messy in the first place.

1. Getting data out of PDFs and reports

Tabula: good for simple tables, and free.
Excel's "Get Data from PDF" (Power Query): built into Microsoft 365 Excel on Windows, so many trainees already have it. It often works as well as Tabula.
Camelot or pdfplumber (Python): for people who write code and need to extract the same report every month.
2. Cleaning

Excel or LibreOffice Calc: functions like TRIM and CLEAN, Text to Columns, Remove Duplicates, Flash Fill and filters. Everyone has a spreadsheet, so this is the realistic starting point.
Power Query in Excel: records each cleaning step, so you can repeat it on next month's report in one click. This is the step up for people who clean the same data again and again.
OpenRefine: its standout feature is clustering, which finds spellings like "Dera Ghazi Khan" and "D.G. Khan" and merges them. That's exactly the district-name problem in block 1, so a 5-minute demo would fit well. It also has facets to spot odd values and a full undo history.
QGIS itself:
the field calculator and Refactor Fields
name-matching functions like levenshtein() and soundex(), which the block 1 exercise already uses
Fix Geometries, Check Validity and Delete Duplicate Geometries for the spatial side
Python (pandas, GeoPandas) or R (tidyverse, sf): what analysts use for large or repeated jobs, together with fuzzy-matching packages like rapidfuzz (Python) or fuzzyjoin (R). Worth mentioning, but probably beyond this group.
3. Preventing dirty data (humanitarian-specific)

P-codes and the Common Operational Datasets (CODs) on HDX: if data is collected with P-codes instead of place names, the joining problem in block 1 doesn't happen. This is probably the most important message for humanitarian work.
Kobo form design: dropdowns, constraints and required questions stop errors at the source. This links to block 3 and the Kobo discussion.
HXL (Humanitarian Exchange Language): hashtags added to spreadsheet columns, like #adm2+name, so tools and other organisations know what each column means.
A cleaning log: not a tool, but standard practice at REACH/IMPACT. Write down every change you made to the raw data. It makes your cleaning checkable and repeatable.
4. AI (ChatGPT, Claude, Copilot in Excel)

**Good uses:**
- writing an Excel formula, a QGIS expression, a regex or a small Python script
- explaining an error message
- suggesting which names probably belong together
- reading a table from a screenshot or a scanned PDF
**Cautions to mention:** 
AI can make up or quietly change values, so always check the results against the source.
Don't upload personal or sensitive data, like beneficiary lists or household locations, unless your organisation's policy allows it.
A rule of thumb: let AI write the steps (a formula or script you can check and run again) rather than clean the data for you. That keeps the work checkable.
For the training: I'd show Excel, which they already have, and OpenRefine's clustering, which solves the problem they just hit in block 1. Then mention P-codes and Kobo form design as the way to avoid the problem altogether, and AI with the cautions above.

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

If a group gets stuck, give them one of the [examples below](#examples-for-the-group-work). After
the presentations, use the [Kobo or QGIS discussion](#discussion-collect-in-the-field-or-digitise-at-the-desk)
if time allows (about 10 min).

### Examples for the group work

| Situation                      | What to map                             | Geometry                         | Example attributes                                                                  | Collected by                                      |
|--------------------------------|-----------------------------------------|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| Earthquake                     | Damaged buildings                       | Point (or polygon for footprint) | Damage level (none / minor / major / destroyed), building use, still occupied, date | Field teams with Kobo; remote from imagery        |
| Flood response                 | Flooded areas                           | Polygon                          | Date observed, water depth (classes), source (satellite / field / community)        | Remote from satellite imagery; field checks       |
| Flood preparedness             | Areas that flood regularly              | Polygon                          | How often, last flood, typical depth, who reported it                               | Community mapping, e.g. Sketch Map Tool           |
| Access and infrastructure      | Roads and bridges                       | Line                             | Passable (yes / 4x4 only / no), surface, date checked                               | Field teams; digitised from imagery               |
| WASH                           | Water points, latrines                  | Point                            | Type, functional (yes / no), users per day, water tested, separate for women/men    | Field teams with Kobo                             |
| Health                         | Health facilities                       | Point                            | Type, functional, beds, services offered, wheelchair accessible                     | Field teams; existing lists joined to coordinates |
| Displacement                   | Evacuation centres, distribution points | Point                            | Capacity, current occupancy, WASH facilities, contact person                        | Field teams with Kobo                             |
| Camps and informal settlements | Settlement outline                      | Polygon                          | Name, estimated households, date of the outline                                     | Digitised from imagery                            |

Real-world examples to mention:

- **Türkiye earthquakes, February 2023:** HOT and the local OpenStreetMap community
  (Yer Çizenler) mapped buildings and roads. The IFRC asked for building-level data for damage
  assessments. The damaged and destroyed buildings are on HDX as
  [HOTOSM Turkey Destroyed Buildings](https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings),
  and HeiGIT [analysed how OSM changed after the earthquake](https://heigit.org/how-to-become-ohsome-pat-15-analysing-changes-in-osm-after-the-earthquake-in-syria-and-turkiye-in-february-2023/).
- **Flood extents from satellite imagery:** the [Copernicus Emergency Management Service](https://emergency.copernicus.eu/)
  publishes flood extents and damage grading after activations. Block 2 uses a flood extent layer
  like this.
- **On the platform:** the [Sketch Map Tool](../content/en/Mobile_Data_collection/en_SMT.md) for
  community maps of flood-prone areas, and the
  [Larkana flood response exercise track](../content/en/Exercise_tracks/en_larkana_flood_response.md),
  which includes importing Kobo exports.

### Discussion: collect in the field or digitise at the desk?

Ask the groups how they would collect their dataset: with a Kobo form in the field, or by
digitising in QGIS. Most good answers combine both.

|               | Kobo form in the field                                                                                                            | Digitising in QGIS                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Good for**  | Things you can only know on site: is the water point working, is the house still occupied, how deep was the water                 | Things you can see from above: building footprints, flooded areas, roads, settlements                   |
| **Strengths** | Many people collect at once, also offline; non-GIS staff can do it; dropdowns and required questions keep data consistent; photos | Fast for large areas; precise shapes; no field access needed; easy to combine with other layers         |
| **Limits**    | You need to get there (access, safety, time); phone GPS is only accurate to a few metres; walking lines and areas is slow         | Needs GIS skills and up-to-date imagery; can't show what isn't visible (function, damage inside, needs) |

**Key message:** use each for what it does best. For example, digitise the buildings from imagery,
then let field teams pick the building in Kobo and add the damage level.

### How to add geodata to a Kobo form

- **Point, Line and Area questions** (`geopoint`, `geotrace`, `geoshape` in XLSForm): record the
  GPS position, or tap it on a map. You can set an accuracy threshold for points.
- **Automatic location:** the `start-geopoint` metadata records where the form was opened, without
  a question.
- **Select from a map:** a `select_one_from_file` question with a GeoJSON file and the appearance
  `map` lets collectors pick an existing feature on a map, e.g. a building or water point you
  digitised in QGIS. This only works in XLSForm and in the KoboCollect app, not in web forms.
- **Checks in the form:** `area()` and `distance()` calculate the size or length of a shape;
  `geofence()` checks whether a point lies inside an area.
- **No coordinates needed?** A dropdown of admin areas or P-codes is often enough. Join the results
  to the boundaries in QGIS later, as in block 1.

**Into QGIS:** export as GeoJSON to keep points, lines and polygons. A CSV export has separate
latitude and longitude columns for points (import as delimited text), but lines and areas end up as
text in a single column. The map in KoboToolbox itself shows points only.

Sources: KoboToolbox documentation on [collecting GPS data](https://support.kobotoolbox.org/collect_gps.html),
[selecting options from a map](https://support.kobotoolbox.org/select_from_map_xls.html) and
[mapping GPS data](https://support.kobotoolbox.org/mapping_gps.html).

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
