# QGIS Installation


QGIS is open source and therefore freely available to everyone at no cost. You can install QGIS for Windows, Mac and Linux computers. The actual __Long Term Release__ is __QGIS 3.28.11 Firenze__. Generally we recommend to use the __latest Long Term Release__, because it is the most stable and contains the fewest bugs. You can __download__ the latest version here: [https://www.qgis.org/en/site/forusers/download.html](https://www.qgis.org/en/site/forusers/download.html)

For our introduction, the standalone installers from OSGeo4W packages are sufficient for Windows.

## Windows

### 32 Bit or 64 Bit?
For __Windows operating systems__, there is always a 32-bit version and a 64-bit version of each QGIS version available for download. Which version to install depends on your computer and operating system. If it is not clear how many bits your operating system has, you can easily find out: Left-click on the __Windows icon at__ the bottom left of the screen (alternatively, open the Windows search function). Type __"System"__ on the keyboard, click on the entry __"System"__ in the search results. Under the item __"System type"__ you can read the bit number.

### Installation 
For the installation under Windows we use the __OSGeo4W network installer__. OSGeo4W is a project that offers __Open Geo related software for Windows__ easy to install. Visit the project page [https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/) select there _Download the ​OSGeo4W network installer_. 

* Make sure to select _Advanced Install_ / _Fortgeschrittene Installation_ during the installation process. 
   - QGIS Desktop
   - GRASS GIS
   - SAGA
  
Video tutorial: https://www.youtube.com/watch?v=pja_EX0tVZA

The selected software is then downloaded via the Internet and installed on-the-fly.


## Mac

__**From version 3.30 SAGA must be integrated via plugin**__

At https://qgis.org/en/site/forusers/download.html select _Download for macOS_. Then use the link  _Download QGIS_. 

More about how to install and activate plugins in QGIS can be found here:
[qgis-Interface#erweiterungen-plugins-installieren](https://courses.gistools.geog.uni-heidelberg.de/giscience/gis-einfuehrung/-/wikis/qgis-Interface#erweiterungen-plugins-installieren)

## Linux

__**From version 3.30 SAGA must be integrated via plugin**__

For installation on Linux systems with apt you can install QGIS:

```
sudo apt install qgis qgis-plugin-grass
```

In the conventional apt package sources, an older version of QGIS will probably be installed. If you are using the package source [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), observe the following installation notes on https://qgis.org/en/site/forusers/alldownloads.html#repositories

If you install a QGIS version >3.30 you have to install the plugin _Processing Saga NextGen Provider_ . 

More about how to install and activate plugins in QGIS can be found here:
[qgis-Interface#erweiterungen-plugins-installieren](https://courses.gistools.geog.uni-heidelberg.de/giscience/gis-einfuehrung/-/wikis/qgis-Interface#erweiterungen-plugins-installieren)
 
