# QGIS Trigger Workflow for Madagascar 

The QGIS workflow presented in this article was developed in the framework of the Forecast-based-Action (FbF) Project of the Croix-Rouge Malagasy (CRM), the German Red Cross (GRC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT).

The workflow is almost fully automated through a QGIS model, requiring no manual intervention. The chapter Automated Trigger Workflow outlines the process and its practical implementation. Each step included in the model is explained in detail to provide a complete understanding of the workflow and how the analysis was carried out.


## Background

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

## Trigger Statement

**Pre-Activation Trigger:** at least one of the meteorological forecasts from Meteo Madagascar, RMSC La Reunion, or ECMWF projects a greater than 50% likelihood of landfall by a tropical cyclone of tropical storm strength or higher within the next 7 days.

**Activation Trigger:** if the Meteo Madagascar (DGM) forecast indicates landfall of a tropical cyclone with wind speeds in excess of 118 km/h within the next 48-72 hours.

## Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be fixed in the near term, and variable data which describe the datasets that will be checked for triggering on a regular basis depending on the occurrence of anticipated cyclone events. 

### Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Description |
| ----- | --- | --- |
| Administrative Boundaries | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | The administrative boundaries on level 0-4 for Madagascar can be accessed via HDX provided by OCHA. For this trigger mechanism we provide the administrative boundaries on level 2 (district level) as a shapefile.  |
| Population Counts | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | The worldpop dataset in `.geotif` raster format provides the estimated total number of people per grid-cell for the year 2020. We will be working with the Constrained Individual countries 2020 at a resolution of 100m. |
| Buildings Counts | [Global ML Building Footprints](https://gee-community-catalog.org/projects/msbuildings/) | The building counts dataset in `.geotif` raster format counts the number of buildings per 100m grid cell. The workflow on how this dataset was created can be found in this [GitLab repo](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |
| Land Cover | [ Copernicus Land Cover](https://land.copernicus.eu/en/products/global-dynamic-land-cover/copernicus-global-land-service-land-cover-100m-collection-3-epoch-2019-globe) | The land cover dataset in `.geotif` raster format provides an overview over the dominant land cover type at a resolution of 100m. This dataset was downloaded using the Google Earth Engine. The workflow on how this dataset was downloaded can be found in this [GitLab repo](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar) |

:::{admonition} Master Raster
:class: note

The three raster datasets are joined together in a Master Raster which will be a raster layer with three channels and a resolution of 100 m. It will include the following information:
1. Population counts from Worldpop constrained (2020)
2. Building counts derived from ML Building Footprints (2021)
3. Land Cover derived from Copernicus Land Cover (2019)

:::

### Monitoring Data

The cyclone trigger mechanism is based on the data provided by NOAA (National Centers for Environmental Information). The cyclone storm tracks are provided within the [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) project. It is the most complete global collection of tropical cyclones available and merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset. IBTrACS was developed collaboratively with all the World Meteorological Organization (WMO) Regional Specialized Meteorological Centres, as well as other organizations and individuals from around the world.

Tropical cyclone track data is available in various subsets, depending on the temporal scale of interest. Regional subsets can also be generated, with data for the South Indian Ocean being particularly relevant for this trigger mechanism.

# Automated Trigger Workflow

As explained at the start of this chapter the developed trigger workflow is done automatically by a QGIS model. In this chapter it is explained how to run the automated model.

The [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.