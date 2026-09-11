# Geodata Management with Sharepoint <a id="geodata-management-with-sharepoint"></a>


Small organisations often struggle to keep geospatial data consistent and accessible.  
A simple, well-structured geodata hub helps **standardise GIS work**, **prepare for responses**, and **onboard new staff** efficiently.  
This guide outlines a practical approach using **SharePoint**, which many organisations already use for document management.

## Purpose & Audience <a id="purpose-and-audience"></a>
- **Who**: Small organisations starting or formalising GIS work.
- **Why**: Establish a lightweight, standardised structure for **data, projects, and templates**.
- **Outcome**: Faster onboarding, fewer broken links, consistent maps and analyses.

### The role of the Data Steward <a id="the-role-of-the-data-steward"></a>

A **data steward** is a designated person (or small team) responsible for:
- Approving and uploading new datasets into `10_Data` and `20_Raster_Data/`.  
- Managing permissions (e.g. who can edit vs. who can only view).  
- Supporting colleagues with questions about dataset quality or standards.  

Having a clear steward role prevents accidental overwrites and ensures that all staff work with **trusted, consistent data**.


:::{tip}
If your organisation outgrows this setup (many editors, heavy edits, very large rasters), keep SharePoint for distribution and documentation, and add a spatial database (e.g., PostGIS) for multi-user editing.
:::

## Example Folder Structures <a id="example-folder-structures"></a>

Below are three possible structures, from simple to more advanced.  
Choose the one that matches your organisation’s size and capacity.

### 1. Minimalist Setup (very small teams) <a id="1-minimalist-setup-very-small-teams"></a>
```
GIS_Hub/
│
├── Data/ # All geodata in one place
│ ├── Boundaries/ # Admin boundaries
│ ├── Roads/ # Road networks
│ ├── Hydro/ # Rivers, lakes
│ ├── Exposure/ # Health facilities, schools
│ └── Hazards/ # Cyclones, floods, droughts
│
├── Projects/ # Project work and outputs
│ ├── Project_A/
│ ├── Project_B/
│ └── Project_C/
│
└── Templates/ # QGIS styles, layouts, symbols
```


💡 **Use when:** The team is very small, with limited data and little overlap between users. This structure is quick to set up and easy for non-technical colleagues.  

⚠️ **Limitation:** Everything is mixed into one `Data/` folder — it is not obvious which datasets are authoritative vs. drafts, and scaling up later can get messy.  

**Naming conventions for Minimalist Setup**
- Keep filenames simple and descriptive, e.g.:  
  - `Boundaries_ADM2_MDG_2024.gpkg`  
  - `HealthFacilities_SOM_2025.csv`  
- For projects, prefix deliverables with project name, e.g.:  
  - `ProjectA_Map_202501.pdf`  
  - `ProjectB_QGISProject.qgz`  
- Dates can be optional here, since the dataset volume is low.  

---
### 2. Balanced Setup (general small organisations) <a id="2-balanced-setup-general-small-organisations"></a>

```
GIS_Hub/
│
├── 00_Admin/                 # SOPs, guidelines, notes
├── 10_Data/                  # All shared datasets (authoritative + thematic, read-only; managed by stewards)
│   ├── Boundaries/           # Admin boundaries, settlement boundaries
│   ├── Roads/                # Road networks, tracks
│   ├── Hydro/                # Rivers, lakes, catchments
│   ├── Settlements/          # Villages, towns, cities
│   ├── Health/               # Health facilities, clinics
│   ├── Logistics/            # Warehouses, airstrips
│   └── Hazards/              # Cyclone tracks, flood zones, drought indicators
├── 20_Raster_Data/           # WorldPop, DEM, land cover, satellite images, hazard rasters
├── 30_Styles_Templates/      # Shared QGIS styles & layouts
│   └── Generic_Styles/       # Standard symbology and layout templates
├── 40_Working_Data/          # Drafts & temporary edits (restricted access)
└── 50_Projects/              # Sorted by topic
    ├── Disaster_Preparedness/
    ├── Health/
    └── Climate_Risk/
```
**💡 Use when:**
The organisation wants to keep all curated data together in `10_Data/`, while separating raster data (`20_Raster_Data/`), shared styles (`30_Styles_Templates/`), drafts (`40_Working_Data/`), and project outputs (`50_Projects/`). This setup works well for most small NGOs.

**⚠️ Limitation:**
Staff need to understand that `10_Data/` and `20_Raster_Data/` are read-only. If edits are saved there, datasets can be overwritten or corrupted.
:::{note}
Large raster files (e.g., DEMs, satellite scenes, wind or rainfall rasters) can slow down OneDrive sync and fill local drives quickly. 

To reduce issues:  
- Keep only the most important raster layers in `20_Raster_Data/`.  
- Archive old raster versions in a separate library if needed.  
:::
**Naming conventions for Balanced Setup (general use)**

To keep files easy to find and avoid duplication, use a consistent naming pattern:  

- **Data (all shared):**  
  Pattern: `[Theme]_[Location/ADMlevel]_[Source]_[YYYYMM].[ext]`  
  *Example:* `Boundaries_ADM2_MDG_GADM_202407.gpkg`  

- **Raster data:**  
  Pattern: `[Theme]_[Location]_[Source]_[YYYYMM].[ext]`  
  *Example:* `Rainfall_MDG_CHIRPS_202502.tif`  

- **Projects:**  
  Pattern: `[ProjectName]_[OutputType]_[Region]_[YYYYMM]_vX.[ext]`  
  *Example:* `HealthAssessment_Report_SOM_202503_v1.pdf`  


### 3. Extended Setup (with EAP workflows) <a id="3-extended-setup-with-eap-workflows"></a>
```
GIS_Hub/
│
├── 00_Admin/                 # SOPs, guidelines, notes
├── 10_Data/                  # All shared datasets (authoritative + thematic, read-only; managed by stewards)
│   ├── Boundaries/
│   ├── Roads/
│   ├── Hydro/
│   ├── Settlements/
│   ├── Health/
│   ├── Logistics/
│   └── Hazards/
├── 20_Raster_Data/           # DEM, land cover, satellite data, hazard rasters (read-only)
├── 30_Styles_Templates/      # Shared QGIS styles & layouts
│   ├── Generic_Styles/       
│   └── Cyclone_EAP_Styles/   # Templates for cyclone-specific outputs
├── 40_Working_Data/          # Drafts & edits (restricted)
├── 50_Cyclone_EAP/           # Anticipatory Action (cyclone) workflows
│   ├── Fixed_Data/           # Baseline exposure layers
│   ├── Models/               # Trigger models, track buffers, forecast files
│   └── Activations/          # One subfolder per cyclone activation
│       ├── Cyclone_Freddy_2023/
│       ├── Cyclone_Batsirai_2022/
│       └── Cyclone_X_YYYY/
└── 60_Projects/              # Sorted by topic
    ├── Disaster_Preparedness/
    ├── Health/
    └── Climate_Risk/

```


💡 **Use when:**  
The organisation wants to keep all curated data together in `10_Data/`, while separating **heavy raster data** (`20_Raster_Data/`), **shared styles** (`30_Styles_Templates/`), and **project-specific or EAP workflows**.

⚠️ **Limitation:**  
Staff need to understand that `10_Data/` and `20_Raster_Data/` are **read-only**. If users save edits there, datasets can be overwritten or corrupted.

:::{note}
Large raster files (e.g. DEMs, cyclone wind or flood depth grids) can slow down OneDrive sync and fill local disks.  
To reduce problems:  
- Keep only the most important raster layers in `20_Raster_Data/`.  
- Archive older rasters in `30_Snapshots/` if you need to keep historical versions.
:::

**Naming conventions for Balanced Setup (with EAPs)**

To keep files easy to find and avoid duplicates, use a consistent naming pattern.  
Below are suggested conventions with examples:

- **Data (all shared):**  
  Pattern: `[Theme]_[Location/ADMlevel]_[Source]_[YYYYMM].[ext]`  
  Example: `Boundaries_ADM2_MDG_GADM_202407.gpkg`

- **Raster data:**  
  Pattern: `[Theme]_[Location]_[Source]_[YYYYMM].[ext]`  
  Example: `Rainfall_MDG_CHIRPS_202502.tif`

- **EAP Models:**  
  Pattern: `Model_[Hazard]_[Version]_[YYYYMM].[ext]`  
  Example: `Model_CycloneTrigger_v3_202502.model3`

- **Activations:**  
  Pattern: `Cyclone_[Name]_[Year]_[OutputType]_[Region].[ext]`  
  Example: `Cyclone_Freddy_2023_ImpactMap_ADM2_MDG.pdf`

- **Projects:**  
  Pattern: `[ProjectName]_[OutputType]_[Region]_[YYYYMM]_vX.[ext]`  
  Example: `ClimateRiskAssessment_Map_MDG_202502_v1.pdf`



## Advantages, Limitations, and Permissions <a id="advantages-limitations-and-permissions"></a>

When setting up a geodata hub in SharePoint, there are clear benefits, but also some important boundaries to be aware of.  
Below is a short overview of the **advantages**, the **limitations**, and how to handle **permissions** effectively.

---

### Advantages <a id="advantages"></a>

Using SharePoint for geodata management gives small organisations a strong starting point:

- **Standardisation** — all staff work with the same datasets, style files, and map templates, which reduces confusion and ensures consistent outputs.  
- **Easy onboarding** — new colleagues don’t waste time hunting for files; the folder structure makes it obvious where to look.  
- **Built-in versioning** — SharePoint automatically stores file history, so it’s easy to recover previous versions if mistakes happen.  
- **Flexible permissions** — you can decide who can only view, who can edit, and who has full control.  
- **Integration with QGIS** — through OneDrive sync, datasets can be accessed locally and reliably within QGIS projects.  

---

### Limitations <a id="limitations"></a>

However, SharePoint is not a GIS database, and this introduces some constraints:

- **Concurrency issues** — file-based geodata formats (like GeoPackage) can corrupt if multiple people try to edit them simultaneously.  
- **Performance bottlenecks** — very large rasters or high-frequency edits will quickly become slow; in these cases, a spatial database such as PostGIS is better.  
- **Discipline required** — the system relies on users consistently following folder structures and naming conventions; otherwise, the hub loses its value.  

:::{important}
Think of SharePoint as a **distribution and coordination hub**.  
For **multi-user editing** or **large-scale storage**, you’ll need a database backend.
:::

### Permissions <a id="permissions"></a>

Managing access well is essential to protect authoritative data while allowing collaboration.  
A good practice is to differentiate between **authoritative data**, **working data**, and **project outputs**:

- **Authoritative_Data** — read-only for most staff; only designated data stewards can upload or edit.  
- **Working_Data** — restricted to editors; enable check-in/check-out so files aren’t overwritten accidentally.  
- **Projects** — editable by project teams, but can be read-only for others to avoid unwanted edits.  
- **Sensitive datasets** — if distribution needs to be controlled, use *View-only* links combined with *Block download*.  

---

**Keep permissions simple.**  
Instead of assigning rights to individuals, create SharePoint groups such as:  
- *Owners* (Full Control)  
- *Editors* (Edit)  
- *Viewers* (Read)  

This makes management much easier when staff join or leave the organisation.  


## Metadata & Cataloguing <a id="metadata-and-cataloguing"></a>

Even if your files are well-organised in folders, it can still be hard for new staff to know **which dataset is the latest** or **what each file is used for**.  
This is where *metadata* comes in. In SharePoint, you can add extra information fields (columns) to your libraries. These fields make it easy to filter, sort, and search across all data — without relying only on file names.

### Why use metadata? <a id="why-use-metadata"></a>
- **Clarity**: Staff can quickly see which dataset is authoritative, draft, or outdated.  
- **Consistency**: Everyone uses the same standard fields.  
- **Search & filter**: Instead of browsing dozens of folders, users can filter by country, hazard, or date updated.  
- **Documentation**: Key context (like source and update cycle) is stored with the file itself, not just in someone’s memory.

### Suggested metadata fields <a id="suggested-metadata-fields"></a>
When creating or editing a SharePoint library, you can add simple columns such as:
- **Theme** (e.g. Boundaries, Health, Logistics, Hazards)  
- **Location / ISO3 code** (e.g. MDG, SOM, region name)  
- **Source** (e.g. WFP, UNOCHA, OSM)  
- **DateUpdated** (YYYYMMDD)  
- **Contact / Owner** (responsible person or team)
- **URL** (link to the original data source or documentation) 

:::{tip}
You don’t need to tag *everything*. Start with 3–4 core fields that help your team find data quickly.  
For example: *Theme*, *Location*, *Source*, and *DateUpdated*. More can be added later if needed.
:::

<iframe width="560" height="315" src="https://www.youtube.com/embed/qB2acPUSF_o?si=JyjVHEqcTNHqTKUK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Implementation Guide (Quick Start) <a id="implementation-guide-quick-start"></a>

Setting up a geodata hub in SharePoint is straightforward.  
Follow these steps to get started:

1. **Create a new SharePoint document library**  
   - Name it clearly, e.g., `GIS_Hub`.  
   - This will be the root space for all your geodata folders.  

2. **Set up the folder structure**  
   - Recreate the agreed structure (Minimalist, Balanced, or Extended) inside the library.  
   - Example for the Balanced Setup:  
     - `00_Admin/`  
     - `10_Data/`  
     - `20_Raster_Data/`  
     - `30_Styles_Templates/`  
     - `40_Working_Data/`  
     - `50_Projects/`  

3. **Configure permissions**  
   - Use SharePoint groups: *Owners* (Full Control), *Editors* (Edit), *Viewers* (Read).  
   - Set `10_Data/` and `20_Raster_Data/` as read-only for most users.  
   - Restrict `40_Working_Data/` to editors only.  

4. **Add initial content**  
   - Upload authoritative datasets into `10_Data/` (boundaries, roads, exposure layers).  
   - Upload a few DEMs or land cover rasters into `20_Raster_Data/`.  
   - Add shared QGIS styles (`.qml`) and layouts (`.qpt`) into `30_Styles_Templates/`.  

5. **Enable OneDrive sync for offline access**  
   - Staff can sync the `GIS_Hub` library to their laptops.  
   - This allows QGIS to use local file paths (more stable than online links).  

6. **Document SOPs in **`00_Admin/`**  
   - Add a simple `ReadMe.md` or `SOPs.pdf` explaining:  
     - Which folders are read-only.  
     - How to name files.  
     - Where to save drafts vs. final outputs.  

7. **Onboard staff**  
   - Show new staff where to find data, projects, and styles.  
   - Emphasise that only data stewards update the `10_Data/` and `20_Raster_Data/` folders.  

:::{tip}
Start small. Don’t upload everything at once. Begin with the datasets most often used in your projects (e.g., admin boundaries, health facilities, WorldPop).  
You can expand later as the team gets used to the system.
:::

## Standard Operating Procedures (SOPs) <a id="standard-operating-procedures-sops"></a>

A clear folder structure is only useful if everyone applies it consistently.  
To avoid confusion and data loss, organisations should agree on a few simple rules.  
These **Standard Operating Procedures (SOPs)** can serve as a starting point:

1. **Data upload**  
   Only data stewards may add or update files in `10_Data/` and `20_Raster_Data/`.  
   Other staff can download these datasets but not modify them.  

2. **File naming**  
   Always follow the agreed naming convention (see section on naming).  
   This ensures datasets are easy to find and avoids duplication.  

3. **Working data**  
   - Use `40_Working_Data/` only for drafts, intermediate processing, or temporary edits.  
   - To avoid sync problems (especially with large files), staff can also keep working files **locally on their own computer**.  
   - Before weekends, or whenever results need to be shared with the team (for backup and contingencies), upload the relevant files to `40_Working_Data/`.  

4. **Project folders**  
   Each project must have its own subfolder in `50_Projects/` (e.g., `FloodResponse_2025/`).  
   Store there:  
   - QGIS projects (`.qgz`)  
   - Final analysis outputs (maps, reports, tables)  
   - A copy of the **datasets actually used in the project** (so the work can be reproduced later).  

5. **Templates**  
   Always apply the shared QGIS styles and layouts from `30_Styles_Templates/` when producing maps or analyses.  
   This keeps outputs consistent across the organisation.  

6. **EAP workflows (if relevant)**  
   For anticipatory action, store baseline data in `50_Cyclone_EAP/Fixed_Data/`, models in `50_Cyclone_EAP/Models/`,  
   and create a new folder for each activation under `50_Cyclone_EAP/Activations/`.  

7. **Change log**  
   Keep a simple log in `00_Admin/` (e.g., `Change_Log.xlsx`) where stewards record updates to data or templates.  

8. **Permissions**  
   Manage access through SharePoint groups, not individuals:  
   - *Owners* → Full Control  
   - *Editors* → Edit (e.g., for `40_Working_Data/` and project folders)  
   - *Viewers* → Read-only (for most data folders)  

:::{tip}
Short SOPs are most effective if they fit on **one page**.  
Keep them simple and review once a year to make sure they are still relevant.  
Emphasise that **day-to-day work files can stay on individual laptops**.  
Only upload to `40_Working_Data/` before weekends, handovers, or when results need to be shared for team use and contingency.
:::



