# Datos de OpenStreetMap (OSM)

## Geofabrik

El [sitio web Geofabrik](https://download.geofabrik.de/) ofrece descargas de datos de OSM por regiones. Puede seleccionar una región de interés y descargar todos los datos de OSM dentro de esa región. Es el método más extenso. Recomendamos utilizar este método si desea explorar los datos de OSM o si necesita muchos datos de OSM. Sin embargo, si solo necesita datos específicos, como caminos, puntos de asentamientos o edificios, puede ser mejor elegir la herramienta de exportación HOT o QuickOSM.

***Ejemplo***

1. Vaya a __https://download.geofabrik.de/__ y navegue hasta Mauricio  
   haciendo clic en `Africa` -> ` Mauritius`
2. En __Formatos más usados__ seleccione la opción `mauritius-latest-free.shp.zip`
   y descargue el archivo. Guárdelo en algún lugar de su computadora donde pueda encontrarlo
   y descomprímalo.
3. Verifique el contenido de la carpeta. Existen muchos shapefiles diferentes,
   cada uno contiene un solo tipo de datos OSM. Toda la lista de capas y lo que
   incluyen puede consultarse [aquí](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf).

4. Abra un nuevo proyecto QGIS y guárdelo en la carpeta `project` de la
   carpeta del ejercicio.
5. Cargue el archivo `gis_osm_places_a_free_1.shp`. Esta capa de polígonos
   contiene los límites de las distintas entidades. Tómese un tiempo para explorar
   los datos mediante la tabla de atributos.
6. (Opcional) Puede seleccionar todas las entidades de la capa con la tecla
   “fclass” = “island” y exportarlos como una nueva capa.  Esto le permitirá
   empezar a crear un mapa de las islas Mauricio.
7. Cargue el archivo `gis_osm_buildings_a_free_1.shp`. Esta capa de polígonos
   contiene todos los edificios de Mauricio mapeados en OSM. Tómese un tiempo
   para explorar la capa.
8. Añada un mapa base por satélite utilizando el complemento [QuickMapServices](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_basemaps_wiki.html#basemaps-from-quickmapservices-plugin)
   para comprobar si hay edificios sin cartografiar.
8. Cargue el archivo `gis_osm_landuse_a_free_1.shp`. Consulte el
    conjunto de datos y utilice la función de clasificación para obtener una mejor visión de conjunto.
    * Haga clic derecho en la capa `gis_osm_landuse_a_free_1` en el panel `Layer Panel`
          -> `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales
          a la izquierda. Vaya a la pestaña `Symbology`.
    * En la parte superior encontrará un menú desplegable. Despliéguelo y elija `Categorized`.
          En `Value` seleccione “fclass” (abreviatura de _featureclass [clase de entidad]_).
    * Más abajo, haga clic en `Classify`.  Verá todos los valores únicos
          de la columna “fclass”.  Puede ajustar los
          colores haciendo doble clic en una fila del campo central. Una vez que haya
          terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.

Como puede ver, Geofabrik es ideal si desea obtener conjuntos de datos de OSM
completos para países o regiones enteros.

## QuickOSM

El complemento QuickOSM le permite cargar datos de OSM desde su ventana de QGIS. Es un método rápido y fácil, pero requiere conocimientos más profundos sobre el modelo de datos de OSM en comparación con las otras opciones.  
Para encontrar los datos que busca, deberá formular una consulta de datos. Existen dos excelentes recursos que le permitirán adaptar su consulta en función de la clave y el valor exactos que necesita:

1. [Wiki de OSM](https://wiki.openstreetmap.org/wiki/Main_Page) y, especialmente, el artículo
   [Map features (Entidades del mapa)](https://wiki.openstreetmap.org/wiki/Map_features).
2. [Taginfo](https://taginfo.openstreetmap.org/)

Este método tiene la ventaja de que se pueden descargar los datos que se necesitan específicamente, pero debe saber formular las consultas. Para utilizar QuickOSM, debe [instalar el complemento de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_plugins_wiki.html).

## Overpass turbo

[Overpass Turbo](https://overpass-turbo.eu) es una herramienta de exportación de datos basada en web para
OSM. Mediante la ejecución de una consulta, puede descargar los datos e importarlos a su proyecto.
Para ejecutarlo, puede escribir su consulta a la izquierda o utilizar el asistente
que le ayudará con la redacción de las consultas.
***Ejemplo*** 
Para buscar escuelas en su área de búsqueda, puede redactar usted mismo
la consulta o utilizar el asistente para hacerlo. 
**1. Verificar las directrices de etiquetado** 
Busque en la [wiki de OSM](https://wiki.openstreetmap.org/wiki/Tags) o en
[taginfo](https://taginfo.openstreetmap.org). En nuestro ejemplo es: *amenity=school* 
**2. Escribir o formular la consulta** 
Utilice el asistente y escriba *amenity=school en Heidelberg* o redacte su
propia consulta (por ejemplo, para su área de búsqueda): 
**Asistente:**
:::{figure} /fig/en_wizard_overpassturbo.png
---
height: 250px
align: center
name: en_wizard_overpassturbo_wiki
---
Captura de pantalla del asistente en overpass turbo
:::

:::{figure} /fig/en_wizard_result.png
---
height: 250px
align: center
name: en_wizard_result_wiki
---
Captura de pantalla del resultado
:::  
**Consulta:**
```sql
[out:json];  
(  
  node ["amenity"="school"](49.35,8.553,49.481,8.756);
  way ["amenity"="school"](49.35,8.553,49.481,8.756);
  relation ["amenity"="school"](49.35,8.553,49.481,8.756);
);
out; 
```
**Cuadro delimitador** 
Para consultar con un cuadro delimitador se necesita un formato especial. Especifíquelo de la siguiente manera:
 + s (límite sur en grados decimales, latitud más baja)
 + w (límite occidental en grados decimales, longitud más baja)
 + n (límite norte en grados decimales, latitud más alta)
 + e (límite oriental en grados decimales, longitud máxima)
     + Por ejemplo:
```sql
node ["key"="value"] (s, w, n, e);
         out;
```

:::{tip}
Para más información sobre el lenguaje de las consultas, lea la [Guía del lenguaje](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide).
:::
**3. Descarga de datos** 
Los resultados se pueden exportar de varias formas.

:::::{tab-set}

::::{tab-item} Datos
Exportando los datos como GeoJSON se pueden importar posteriormente en el proyecto
QGIS.

:::{figure} /fig/en_overpass_turbo_data.png
---
height: 250px
align: center
name: en_overpass_turbo_data_wiki
---
Captura de pantalla de cómo exportar datos en overpass turbo
:::

::::

::::{tab-item} Mapa
Al exportar la consulta como mapa, puede compartir su vista actual como enlace o imagen.

:::{figure} /fig/en_overpass_turbo_map.png
---
height: 150px
name: en_overpass_turbo_map_wiki
align: center
---
Captura de pantalla de cómo exportar el mapa en overpass turbo
:::
::::

::::{tab-item} Consulta
Al exportar su consulta puede obtener el texto o convertirlo en un archivo OverpassXML o
consulta con formato OverpassQL.

:::{figure} /fig/en_overpass_turbo_query.png
---
height: 250px
align: center
name: en_overpass_turbo_query_wiki
---
Captura de pantalla de cómo exportar una consulta en overpass turbo
:::
::::

:::::

:::{tip}
Para más información, consulte la[Wiki](https://wiki.openstreetmap.org/wiki/Overpass_turbo).
:::
<!---
### Ohsome tools
-->