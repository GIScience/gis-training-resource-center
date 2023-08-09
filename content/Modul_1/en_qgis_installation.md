# Installation
QGIS ist Open Source und daher frei und ohne Kosten für jeden verfügbar. Ihr könnt QGIS für Windows, Mac und Linux Rechner installieren. 

## Windows
Für die Installation unter Windows verwenden wir den OSGeo4W Netzwerkinstaller. OSGeo4W ist ein Projekt, das Open Geo bezogene Software für Windows einfach zu installieren anbietet. Besucht die Projektseite [https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/) und klickt dort auf den link `Download the ​OSGeo4W network installer`. 

* Achtet darauf während des Installationsprozesses _Advanced Install_ / _Fortgeschrittene Installation_ zu wählen. Nur dann können die für diesen Kurs relevante Software präzise wählen:
   - QGIS Desktop
   - GRASS GIS
   - SAGA
  
Videotutorial: https://www.youtube.com/watch?v=pja_EX0tVZA

Die gewählte Software wird dann über das Internet heruntergeladen und on-the-fly installiert.


## Mac

__**Ab Version 3.30 muss SAGA per plugin eingebunden werden**__

 Unter https://qgis.org/en/site/forusers/download.html `Download for macOS` wählen. Dann den Link _Download QGIS_ nutzen. 

In QGIS dann das Plugin _Processing Saga NextGen Provider_ installieren. 

Mehr zu wie man Plugins in QGIS installiert und aktiviert findet ihr hier:
[qgis-Interface#erweiterungen-plugins-installieren](https://courses.gistools.geog.uni-heidelberg.de/giscience/gis-einfuehrung/-/wikis/qgis-Interface#erweiterungen-plugins-installieren)

## Linux

__**Ab Version 3.30 muss SAGA per plugin eingebunden werden**__

Für die installation unter Linux Systemen mit apt könnt ihr QGIS installieren:

```
sudo apt install qgis qgis-plugin-grass
```

In den herkömmlichen apt Paketquellen wird vermutlich eine ältere Version von QGIS installiert sein. Solltet ihr die Paketquelle [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa) nutzen, beachtet die folgenden installations Hinweise auf https://qgis.org/en/site/forusers/alldownloads.html#repositories

Solltet ihr hierüber eine QGIS Version >3.30 installieren müsst ihr das Plugin _Processing Saga NextGen Provider_ noch installieren. 

Mehr zu wie man Plugins in QGIS installiert und aktiviert findet ihr hier:
[qgis-Interface#erweiterungen-plugins-installieren](https://courses.gistools.geog.uni-heidelberg.de/giscience/gis-einfuehrung/-/wikis/qgis-Interface#erweiterungen-plugins-installieren)
 
