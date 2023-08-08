# Geodatenformate
Auf dieser Seite werden die für dieses Tutorium wichtigsten Geodatenformate behandelt, um einen allgemeinen Überblick für die Teilnehmenden zu schaffen. Dabei werden folgende Themen angesprochen: 
- [Unterschiede bei der Arbeit mit Raster- und Vektordaten](#unterschiede-bei-der-arbeit-mit-raster-und-vektordaten)
- [verschiedene Vektordatenformate](#vektordatenformate) (Shapefiles und GeoJSON)
- [Rasterdatenformate](#rasterdatenformate) (GeoTiff)
- [Datenformate für Raster- und Vektordaten](#datenformate-für-raster-und-vektordaten) (Geopackage), und
- [Web Map Service (WMS)](#web-map-service-wms)
 
# Unterschiede bei der Arbeit mit Raster- und Vektordaten
Tools für Vektordaten **sind nicht** für die Verarbeitung von Rasterdaten geeignet, und umgekehrt.

# Vektordatenformate
## Shapefiles
Shapefiles werden in **mehreren verschiedenen Dateien** aufgeteilt gespeichert. Dabei trägt jede "Teil-Datei" ganz bestimmte Informationen, wie in der Darstellung hier gesehen werden kann. Dateien mit der Endung .shp, zum Beispiel, sind die hauptsächliche Datei und beinhalten die Geometrien, während dbf-Dateien die Attributtabelle enthalten.

![Shapefile_Dateiformate_1](uploads/43feaa0744cd1a6b29d52a6639730b2c/Shapefile_Dateiformate_1.png)  
  
Shapefiles können immer **nur einen Geometrietyp beinhalten,** das heißt sie enthalten entweder ausschließlich Punkt, Linien, oder Polygon Features, niemals eine Mischung der drei.

## Textuelle Austauschformate, wie z.B. GeoJSON

Vektordaten können auch in textuellen Austauschformaten, wie zum Beispiel GeoJSON, vorhanden sein. 
GeoJSON ist ein offenes Standardaustauschformat für räumliche Daten und basiert auf JSON (JavaScript Object Notation). Daten, die in diesem Format dargestellt werden, beziehen sich auf das geographische Koordinatenbezugssystem "World Geodetic System 1984". Zur Veranschaulichung finden sich in der folgenden Darstellung Beispiele für gültige GeoJSON-Dateien.

![GeoJSON_Dateiformat](uploads/db464273a2aecd3cf0c9d53a1e7325ed/GeoJSON_Dateiformat.PNG)

*Quelle: ArcGIS Online. o.J. GeoJSON. Online unter: https://doc.arcgis.com/de/arcgis-online/reference/geojson.htm, abgerufen am 19.10.2020.*

Weitere Informationen zu GeoJSON und der Verwendung in GIS finden sich unter: https://doc.arcgis.com/de/arcgis-online/reference/geojson.htm.

GeoJSON-Daten können zudem unter der Adresse geojson.io leicht **selbst erstellt** werden.

# Rasterdatenformate
## GeoTiff
* GeoTiffs beinhalten georeferenzierte Bilddateien, zum Beispiel Luft- oder Satellitenbilder.
* GeoTiff (**Geo**graphic **T**agged **I**mage **F**ile **F**ormat) wird heute nahezu standardmäßig als Speicherformat für Rasterdaten verwendet.
* In die Bilddatei eingebettete Metadaten enthalten Informationen zur Georeferenz des Bildes, wie etwa Koordinaten zur Georeferenzierung oder das Koordinatenbezugssystem.

Weitere Informationen finden sich unter folgendem Link des OGC (Open Geospatial Consortium): http://docs.opengeospatial.org/is/19-008r4/19-008r4.html#_geotiff.

# Datenformate für Raster- und Vektordaten
## Geopackages
Ein Geopackage (standardisiert durch das *Open Geospatial Consortium (OGC)*) ist ein Format zur Speicherung von Vektor- und Rasterdaten, das von den meisten GIS unterstützt wird.
- Idee: Eine dateibasierte Datenbank (SQLite), in welcher auf standardisierte Weise alle Daten gespeichert werden.
- Dateibasierte Datenbank = eine Datei, welche in strukturierter Weise abgefragt werden kann

**Probleme mit Geopackages:**

Beim Arbeiten mit Geopackages kann es zuweilen zu dem Dateiformat spezifischen Problemen kommen. So kann die Verarbeitung mit Tools wie Clip, oder anderen Wekrzeugen, besonders wenn Änderungen in der Attributtabelle vorgenommen werden, Fehlermeldungen hervorrufen. Lösen lässt sich dieses Problem, wenn das Dateiformat *Geopackage* nur zum Speichern, also zum Exportieren ausgewählt wird (der Vorteil liegt hier besonders im Vergleich zu Shapefiles darin, dass ein Geopackage nur aus einer Datei, und nicht mehreren besteht und so keine Teildatei verloren gehen kann). Während der Arbeit im Projekt, sollte dagegen besser mit GeoTiffs oder Shapefiles gearbeitet werden, um Fehlerquellen zu minimieren.

Herunterladen werden können leere Geopackages zum Weiterverarbeiten unter folgendem Link: http://www.geopackage.org/data/empty.gpkg

# Web Map Service (WMS)

**W**eb **M**ap **S**ervices (WMS) erlauben es euch, Geodaten aus dem Web mit eurem GIS zu verknüpfen und abzurufen. Als Ergebnis wird euch dabei dann ein georeferenziertes Kartenbild angezeigt. Dieses Prinzip wird beispielsweise auch bei [Basemaps](qgis-Basemaps) angewendet. Im zugehörigen Wikibeitrag finden sich Informationen darüber, wie sich WMS Daten in QGIS hereinladen lassen, und welche Funktionen genutzt werden können. 

*Further Resources:* Weitere Informationen zu WMS finden sich auch unter: https://www.ogc.org/standards/wms.