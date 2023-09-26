# Basic Geodata  processing

**Competences:**
* Projections
* Layer concept
* Vector and raster data (basic concepts)
* Vector file formats


Die kartographische Darstellung von Vektor-Layern im GIS ist ein weites und komplexes Themenfeld. Wir betrachten hier daher nur einige grundlegende Funktionen.  







The earth is a sphere and cannot be represented on a flat map without being distorted. For this translation, from a curved on a flat surface, thousands of different methods exist. These are called **Coordinate Reference Systems (CRS)**.

![Different Coordinate Reference Systems](../../fig/en_different_crs.gif)

The different types of CRS should be used for different use cases. For example, Mercator projections don´t represent the area correctly. This table shows an overview on which projections to use for which needed characteristic:

| Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :--------------------: | :-----------------: | :----------: |
| [x] shape              | [ ] shape           | [x] shape    |
| [x] rotation           | [x] rotation        | [ ] rotation |
| [ ] area               | [x] area            | [x] area     |

For smaller areas local coordinate systems should be used since they give a more accurate display at the expense of more distortion at the global level. 

![Local Coordinate Reference Systems](../../fig/en_local_crs.png)

To change the projection of a **vector file**, click on *Vector*, *Data Management Tools*, *Reproject Layer*. Select your input layer and the target crs. Click on the three dots to *Save to File...* and click *Run*. For a detailed instruction click on this [video](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/7e7a28698859062d1b832b558b2721c6/qgis_reproject_vector.mp4).

To change the projection of a **raster file**, clickclick on *Raster*, *Projections*, *Warp (Reproject)*. Choose your input layer and target crs. Click on the three dots to *Save to File...* and click *Run*. For a detailed instruction click on this [video](https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/wikis/uploads/3b7a1bb2408f4453f22d73f54156888b/qgis_reproject_raster.mp4).


## Layer concept

```{admonition}

## Vector and raster data


## Vector file formats





* [Single Symbol](qgis-Vektorsignaturen#single-symbol)
* [Nominale Daten - Categorized](qgis-Vektorsignaturen#nominale-daten-categorized)
* [Intervallskalierte Daten - Graduated](qgis-Vektorsignaturen#intervallskalierte-daten-graduated)
* [Signaturen speichern und laden](qgis-Vektorsignaturen#signaturen-speichern-und-laden)
* [Beschriftung](qgis-Vektorsignaturen#beschriftung)
* [Weitere Ressourcen](qgis-Vektorsignaturen#weitere-ressourcen)


**Hinweis:**  
Die getätigten Veränderungen bei der Darstellung eines Layers werden nur lokal in eurer Projektdatei gespeichert und nicht in der Layer-Datei direkt. Wird die Layer-Datei also außerhalb eures Projektes geöffnet (zum Beispiel wenn ihr sie als Teil einer Abgabe in Moodle hochgeladen habt), sind die Darstellungseinstellungen verloren.  
Ihr könnt die Darstellung jedoch getrennt als Datei abspeichern (siehe [Signaturen speichern und laden](qgis-Vektorsignaturen#signaturen-speichern-und-laden)). Für die Abgaben empfehlen sich aber stattdessen Screenshots in der Dokumentation.

## Single Symbol
* alle Features im Layer werden auf die gleiche Art und Weise (Farbe, Größe, etc.) dargestellt
* Rechtsklick auf Layer --> Symbology --> Single Symbol

### Farbe ändern
![qgis_change_color_point_video](uploads/QGIS/videos/qgis_change_color_point.mp4)

### Größe ändern
![qgis_change_size_point_video](uploads/QGIS/videos/qgis_change_size_point.mp4)
* diese Einstellung gibt es nur für Punkte und Linien

### Punkt-Icon ändern
![qgis_change_icon_point_video](uploads/QGIS/videos/qgis_change_icon_point.mp4)
* auch für Linien könnt ihr unterschiedliche bestehende Styles wählen

### Polygon Füllung ändern
![qgis_change_polygon_fill_video](uploads/QGIS/videos/qgis_change_polygon_fill.mp4)
* auch hier könnt ihr unterschiedliche bestehende Styles wählen

### Transparenz einstellen
![qgis_layer_opacity_video](uploads/QGIS/videos/qgis_layer_opacity.mp4)

## Nominale Daten - Categorized
* alle Feature einer Kategorie sollen auf gleiche Art und Weise dargestellt werden
* Rechtsklick auf Layer --> Symbology --> Categorized
* für jede Kategorie kann die Darstellung angepasst werden (auf ähnliche Art und Weise wie im Abschnitt *Single Symbol* dargestellt)

![qgis_symbology_categorized_polygon_video](uploads/QGIS/videos/qgis_symbology_categorized_polygon.mp4)

## Intervallskalierte Daten - Graduated
* Features sollen entsprechend einer Skala dargestellt werden
* Darstellung über Farbverlauf oder Größe
* Daten werden in Klassen eingeteilt nach einer bestimmten Methode (z.B. `equal interval` oder `equal count`) oder manuell
* Für jede Klasse kann die Darstellung angepasst werden (auf ähnliche Art und Weise wie im Abschnitt *Single Symbol* dargestellt)

![qgis_symbology_graduated_point_video](uploads/QGIS/videos/qgis_symbology_graduated_point.mp4)

## Signaturen speichern und laden
In QGIS könnt ihr die Signaturen auch als Datei speichern und so für verschiedene Projekte und Layer nutzen.
* Rechtsklick auf Layer --> Export --> Save as QGIS Layer Style File

Für ein neues Layer könnt ihr dann die Signatur wie folgt laden, möglicherweise müsst ihr dann noch den Namen des Feldes mit den Attributen anpassen.

![qgis_symbology_load_style_video](uploads/QGIS/videos/qgis_symbology_load_style.mp4)

## Beschriftung
* jedes Feature kann mit Werten aus der Attributtabelle beschriftet werden
* Rechtsklick auf Layer --> Labels

### Automatische Platzierung
* automatische Platzierung von Labels funktioniert manchmal nur semi-optimal, geht dafür aber sehr einfach und schnell

![qgis_labels_video](uploads/QGIS/videos/qgis_labels.mp4)

### Manuelle Platzierung
* man startet mit einer automatischen Platzierung und passt dann die Position manuell an
* ermöglicht kartographisch besser platzierte Label, nimmt aber oft sehr viel Zeit in Anspruch
* Nutzung der *Labeling Toolbar*

![labeling_toolbar](uploads/QGIS/labeling_toolbar.PNG)


![qgis_labels_by_hand_video](uploads/QGIS/videos/qgis_labels_by_hand.mp4)

---
# Weitere Ressourcen
* [QGIS Doku: Symbology](https://docs.qgis.org/testing/en/docs/training_manual/basic_map/symbology.html)
