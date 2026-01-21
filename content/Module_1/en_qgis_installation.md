::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Setting up

In this chapter, we will prepare the setup for the training. This includes installing QGIS, setting up a folder structure for all the data in the training, and how to manage the downloaded material. The first step will be to install QGIS. After that, we will set up a folder structure for the training, as well as go over a few steps to keep your data management clean.

## Quick guide QGIS 3.34.12 - installation and basic setup

<iframe width="800" height="515" src="https://youtube.com/embed/ck4PjoOIwMQ?si=8HHR03VzpyuhXOmr" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## QGIS Download and Installation

QGIS is open source and therefore freely available to everyone at no cost. You can install QGIS for Windows, Mac and Linux computers. The installation of QGIS is very simple. Depending on your system (Windows, Mac or Linux) there are some things to look out for. You can find advice below on how to install QGIS on different operating systems. 

:::{Warning} 

There are several versions of QGIS available to download. It is recommended to use the __Long Term Release__ versions because it is the most stable and contains the fewest bugs.
The current __Long Term Release__ is __[QGIS 3.40.4. 'Bratislava'](https://qgis.org/download/)__

:::

### QGIS Download

1. Go to the [__QGIS download page__](https://www.qgis.org/en/site/forusers/download.html).
2. Select `Download for Windows`, `Download for macOS` or `Download for Linux`, depending on your operating system.
3. Click on `Looking for the most stable version? Get QGIS 3.34 LTR`

:::{figure} /fig/QGIS_download_LTR_version.png
---
width: 600 px
name: QGIS_download_LTR_version
align: center
---
The download page for QGIS 3.34.
:::

4. The download will start.
5. Locate the downloaded file (usually in your Downloads folder) and run it to start the installer
6. Follow the installer instructions to install QGIS!

## Operating System specific considerations

:::::{tab-set}

::::{tab-item} Windows installation

__32 Bit or 64 Bit?__
For __Windows operating systems__, there is always a 32-bit version and a 64-bit version of each QGIS version available for download. Which version to install depends on your computer and operating system. If it is not clear how many bits your operating system has, you can easily find out: Left-click on the __Windows icon__ at the bottom left of the screen (alternatively, open the Windows search function). Type __"System"__ on the keyboard, click on the entry __"System"__ in the search results. Under the item __"System type"__ you can read the bit number.

:::{Note}

Since QGIS 3.20 there are only 64-bit Windows executables.

:::

::::

::::{tab-item} Linux installation

For installation on Linux systems with `apt` you can install QGIS:

```
sudo apt install qgis qgis-plugin-grass
```


In the conventional apt package sources, an older version of QGIS will probably be installed. If you are using the package source [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), observe the following installation [notes](https://qgis.org/en/site/forusers/alldownloads.html#repositories).

If you install a QGIS version 3.30 or higher you have to install the plugin 
_Processing Saga NextGen Provider_.

::::

:::::

## Setting up a folder structure for the training

Keeping your data and project-files organised is the key to successfully working with GIS-software. This exercises on this platform require you to download geodata and process them on your own. In order to keep everything organised, we advise you to create a folder structure for all the data and material downloaded in the course of this training.

- Create a folder in the location of your choosing with the name `GIS_Training`. 
- When downloading data for the exercises, create subfolders for each module and training exercise (e.g. `/GIS_Training/Module_1/Exercise_1`).
- Save all of the QGIS-projects as well as the downloaded material for the exercises in these folders. 

[Module 2](/content/Modul_2/en_qgis_geodata_concept.md) will go into more into depth about geodata management and introduce a standard folder structure for QGIS-projects. 

:::{note}

Make sure to unzip the exercise files before starting the exercises. 

:::

## Self-Assessment Questions

:::{admonition} Test what you've learned
:class: note
Take a moment to recapitulate what you've learned in this module by making sure you possess the competences below:

1. __You know how to download the newest version of QGIS.__
2. __You know how to set up your own standard folder structure.__

:::
