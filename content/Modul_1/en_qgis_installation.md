# QGIS Installation

## 🚀Quick guide QGIS 3.28 - installation and basic setup

[![QGIS 3.28 - installation and basic setup](/fig/image_QGIS_3.28_download.png)](https://www.youtube.com/watch?v=tSJMT96HsAo)


## QGIS Download and Installation

QGIS is open source and therefore freely available to everyone at no cost. You can install QGIS for Windows, Mac and Linux computers.
The installation of QGIS is very simple. Depending on your system (Windows, Mac or Linux) there are some things to look out for. Futher below you can find more information on your system specialites. 

```{Warning} 
There are many versions of QGIS. It is recommended to use the __Long Term Release__ versions  because it is the most stable and contains the fewest bugs.

The current __Long Term Release__ is __QGIS 3.28.11 Firenze__
```

### QGIS Download

1. Go to the [__QGIS download page__](https://www.qgis.org/en/site/forusers/download.html).
2. Select `Download for Windows`, `Download for macOS` or `Dowload for Linus`, depending on your system.
3. Click on `Looking for the most stable version? Get QGIS 3.28 LTR`

```{figure} /fig/QGIS_download_LTR_version.png
---
height: 100px
name: QGIS LTR Version
align: center
---
```
4. The download will start.
5. Install QGIS!

## Windows specialties

### 32 Bit or 64 Bit?
For __Windows operating systems__, there is always a 32-bit version and a 64-bit version of each QGIS version available for download. Which version to install depends on your computer and operating system. If it is not clear how many bits your operating system has, you can easily find out: Left-click on the __Windows icon at__ the bottom left of the screen (alternatively, open the Windows search function). Type __"System"__ on the keyboard, click on the entry __"System"__ in the search results. Under the item __"System type"__ you can read the bit number.

```{Note} 
Since QGIS 3.20 there are only 64-bit Windows executables.
```


## Mac specialties

```{Note} 
From version 3.30 SAGA must be integrated via plugin.
```

## Linux specialties

```{Note} 
From version 3.30 SAGA must be integrated via plugin.
```

For installation on Linux systems with apt you can install QGIS:

```
sudo apt install qgis qgis-plugin-grass
```

In the conventional apt package sources, an older version of QGIS will probably be installed. If you are using the package source [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), observe the following installation [notes](https://qgis.org/en/site/forusers/alldownloads.html#repositories)

If you install a QGIS version 3.30 or higher you have to install the plugin _Processing Saga NextGen Provider_ . 


