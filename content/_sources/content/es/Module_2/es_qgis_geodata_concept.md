::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Introducción a los datos geoespaciales y las capas

**Competencias:**

En este capítulo, aprenderá qué son los __datos geográficos__ y comprenderá la diferencia entre __datos vectoriales y ráster__. Además, en este capítulo se explica el __concepto de capa __ del programa de sistema de información geográfica (SIG), que es fundamental para todos los mapas que vaya a crear.

## ¿Qué son los datos geoespaciales?

Los datos geoespaciales o datos geográficos son datos que contienen información geográfica. Esto significa que los datos se refieren a una ubicación, que se define por coordenadas. Es similar a otras formas de datos que pueden representarse en tablas (como las hojas de cálculo de Excel o los archivos CSV), pero cada elemento del conjunto de datos también contiene información de coordenadas (véase {numref}`en_vector_raster`). El programa SIG nos ayuda a visualizar y manipular datos geográficos en un espacio 2D (o incluso 3D). Existen dos tipos principales de datos geográficos: los **datos vectoriales y los datos ráster**. Ambos tipos representan cosas tangibles o intangibles del mundo real. Sin embargo, la forma en que almacenan estos datos es muy diferente. Por ello, la manipulación y representación de estos dos tipos difiere drásticamente. Comprender la diferencia entre estos dos tipos, y cómo trabajar con cada uno por separado, así como combinar ambos tipos, será una de las principales habilidades que adquirirá al aprender SIG.

:::{figure} /fig/en_vector_raster.png
---
width: 500px
align: center
name: en_vector_raster
---
Concepto ráster/vectorial (fuente: adaptado de [WikiMedia](https://commons.wikimedia.org/wiki/File:Raster_vector_tikz.png)).
:::

El tipo de información que puede almacenarse en los datos geográficos es casi infinito. Puede contener información sobre el mundo físico, tal como:

* datos de elevación (altura)
* datos ambientales (suelos, clima, temperatura, precipitaciones, información sobre
eventos meteorológicos o fenómenos naturales, como la extensión de las inundaciones)
* datos sobre la infraestructura, edificios, transporte, etc.
* datos socioculturales o económicos, como datos demográficos, límites administrativos, acontecimientos sociales, delincuencia, etc.

Los datos geográficos, por lo general, simbolizan las entradas de datos como __geometrías__ en lienzos 2D. Estas geometrías pueden ser puntos, líneas, polígonos o incluso píxeles y pueden representar diversos objetos que existen en el mundo físico, como carreteras, lagos, árboles, etc., o representar objetos intangibles, como límites administrativos, cifras de población, indicadores sanitarios, acontecimientos históricos, etc.


### Datos vectoriales

Los datos vectoriales son entidades digitales y pueden almacenar información geográfica/espacial, así como otros atributos de datos. Como tales, son ideales para visualizar información en un mapa. Cada entidad geográfica puede visualizarse en un mapa con el uso de una de las siguientes tres geometrías: __puntos, líneas o polígonos__ (véase {numref}`en_vector_data_overview`). Una capa sólo puede contener entidades geográficas con el mismo tipo de geometría.


:::{figure} /fig/en_vector_data_overview.png
---
width: 650px
align: center
name: en_vector_data_overview
---
Perspectiva general de los datos vectoriales (fuente: HeiGIT).
:::

- Los datos de punto normalmente solo tienen un conjunto de coordenadas por entrada de datos (longitud, latitud y a veces elevación, generalmente denominadas x, y, y z).
- Las líneas se construyen mediante la conexión de varios puntos, que se guardan como una única entrada de datos.
- Los polígonos también se construyen con la conexión de varios puntos, pero forman una geometría cerrada. Cada geometría está representada con una única entrada de datos.


Cada entidad geográfica almacena la ubicación (como dirección o coordenadas) y otros atributos, p.ej., nombre, ID o cualquier otro tipo de información ({numref}`en_geodata_example_2`). La geometría que se utilice dependerá del tipo de datos que se representen. Por ejemplo, una carretera podría representarse con una línea, la superficie de construcción, con un polígono y un árbol con un punto.


:::{figure} /fig/en_geodata_example_2.png
---
name: en_geodata_example_2
width: 700px
---
La información geográfica puede ser una dirección y/o coordenadas GPS (fuente: Cruz Roja Británica).
:::

- Las entidades geográficas se exponen en los mapas con una representación geométrica, pero se componen de información organizada en tablas (véase {numref}`Geodata_attribute_table_example`).
- Cada fila de la tabla será una entidad geográfica del mapa, mientras que cada columna contendrá una información de atributo (campo).
- Se pueden asociar múltiples atributos a cada entidad.


:::{figure} /fig/Geodata_attribute_table_example.png
---
name: Geodata_attribute_table_example
width: 750px
---
Una tabla de datos en Microsoft Excel con información geográfica. (Fuente: Cruz Roja Británica).
:::

{numref}`example_geometric_vs_attribute_view` muestra el mismo conjunto de datos representado tanto geométricamente como en forma de tabla de atributos.

:::{figure} /fig/example_geometric_and_attribute_view.png
---
name: example_geometric_vs_attribute_view
width: 700 px
---
Cada polígono de la izquierda representa una fila (entidad geográfica) de la derecha. (Fuente: Cruz Roja Británica).
:::

#### Formatos de los archivos vectoriales

Existen varios formatos de archivo para datos vectoriales. Cada uno de ellos difiere en cómo se almacenan las geometrías y los atributos. Sin embargo, todos ellos siguen conteniendo únicamente puntos, líneas o polígonos. Algunos formatos tienen ventajas sobre otros, mientras que otros todavía se utilizan por convención, aunque estén desfasados.
La siguiente tabla ofrece una breve descripción de los formatos de archivos vectoriales más utilizados.

| Extensión de nombre de archivo | Nombre | Descripción |
| ----------- | ---------------------- | --------------------------------------------------------- |
| `.shp` | Shapefile | Shapefile es un formato de archivo de datos vectoriales utilizado habitualmente para el análisis geoespacial. Los formatos Shapefile almacenan la ubicación, la geometría y los atributos de entidades de punto, lineales y poligonales. Es un formato de archivo común utilizado por la mayoría de los programas de SIG y de las plataformas cartográficas en línea. Se trata de un formato de datos geográficos antiguo pero aún ampliamente utilizado. Un shapefile solo puede contener un conjunto de datos. Un shapefile completo debe constar de al menos tres archivos diferentes (.shp, .shx, .dbf) |
| `.gpkg` | GeoPackage | La nueva norma para los datos geográficos. Los archivos GPKG son un formato abierto y portátil basado en SQLite para almacenar datos geoespaciales vectoriales y ráster, compatible con diversas plataformas SIG en ordenadores de escritorio, web y dispositivos móviles. Puede contener varios archivos de datos (vectoriales, ráster y datos no espaciales, como las tablas) |
| `.kml`/`.kmz.` | Lenguaje de marcado Keyhole | Formato de datos geográficos para su uso con [Google Earth](https://earth.google.com/web/). Los archivos KMZ son versiones comprimidas de archivos KML (Lenguaje de marcado Keyhole) que se utilizan para almacenar datos geográficos, como puntos, rutas y polígonos, junto con cualquier medio asociado, como imágenes e iconos. Utilizados habitualmente con Google Earth y otros programas de cartografía, los archivos KMZ agrupan datos espaciales y recursos en un archivo compacto, lo que facilita el intercambio de mapas interactivos y visualizaciones. |
| `.gpx` | Formato de intercambio GPS | Formato de datos geográficos para el intercambio de coordenadas. Por ejemplo, para los puntos de referencia de las rutas. |
| `.geojson` | GeoJSON | Formato de datos abierto que utiliza Notación de objetos de JavaScript (JSON) para almacenar los datos geográficos. Puede almacenar varios tipos de geometrías en un solo archivo y es ampliamente compatible con aplicaciones web y móviles. |
| `.gdb` | Geodatabase | Diseñado para la gestión eficaz de datos, el análisis espacial y los flujos de trabajo geoespaciales complejos. Los archivos de Geodatabase son un formato propietario de Esri para almacenar y gestionar grandes volúmenes de datos espaciales, incluidas clases de entidades geográficas, tablas y relaciones en una base de datos estructurada. |


:::{note}

Los distintos formatos de archivo tienen diferentes casos de uso, así como ventajas o inconvenientes.

- Por ejemplo, los archivos __GeoJSON__ no pueden almacenar información de la proyección cartográfica y se limitan de forma convencional al elipsoide WGS84. Esto dificulta el uso de archivos GeoJSON en proyectos en los que se utilizan proyecciones cartográficas específicas de una región o proyecciones basadas en elipsoides diferentes.

- __Geodatabase__ y __Geopackage__ son, a diferencia de los otros formatos, bases de datos. En SIG, las bases de datos almacenan datos espaciales en sistemas estructurados y escalables que admiten el acceso de múltiples usuarios, consultas complejas y grandes conjuntos de datos, lo que las hace ideales para el análisis y la gestión de datos a nivel empresarial. Los archivos, por su parte, almacenan los datos en formatos individuales y portátiles como Shapefile, GeoJSON o GeoPackage, que son más fáciles de compartir y utilizar fuera de línea, pero carecen de capacidades avanzadas de consulta y escalabilidad.

:::

#### Estructura del Shapefile

Un shapefile es una colección de archivos independientes que suelen estar en una única carpeta/directorio. Algunos archivos son obligatorios, otros son opcionales (véase {numref}`en_shapefile_structure`). Para que un shapefile funcione, es necesario tener todos los archivos obligatorios en la misma carpeta.

:::{figure} /fig/en_shapefile_structure.png
---
name: en_shapefile_structure
width: 400 px
---
__SHP, SHX__ y __DBF__ son los archivos __obligatorios__ que todo shapefile debe contener para funcionar correctamente. El SHP es el archivo principal y contiene la geometría.  
:::


### Datos ráster

Otro tipo de datos geoespaciales son los datos ráster. Los datos ráster están formados por celdas que se organizan en una cuadrícula con filas y columnas, formando así un ráster. Cada celda, o píxel, contiene un valor que contiene información (por ejemplo, la temperatura o la densidad de población). Dado que los datos ráster están formados por píxeles, las fotografías aéreas o las imágenes satelitales, también pueden utilizarse como datos ráster, si tienen las coordenadas geográficas (véase el [módulo 3: Georreferenciación](/content/es/Module_3/es_qgis_georeferencing.md)).

Los usos típicos de los datos ráster son:

* datos de elevación (a menudo, denominados Modelo Digital de Elevación o DEM)
* datos de precipitación
* datos de temperatura interpolados
* densidad de población

El valor de cada celda suele visualizarse mediante la asignación de un color a un valor. Para los datos de elevación, por ejemplo, se suele utilizar una rampa de color. Para los datos categóricos, como el uso del suelo, categorías de color (como el verde = bosque; amarillo = uso del suelo agrícola, rojo = residencial).

:::::{grid} 2
::::{grid-item-card}

:::{figure} /fig/raster_data_example_corine_LC.png
---
name: raster_data_example_corine_LC
width: 350 px
align: left
---
El conjunto de datos de cobertura terrestre CORINE de Copernicus (fuente: [AEMA/Copernicus](https://land.copernicus.eu/en/map-viewer?product=130299ac96e54c30a12edd575eff80f7)).
:::

::::

::::{grid-item-card}

:::{figure} /fig/NASADEM_Alps_example.png
---
name: NASADEM_Alps_example
width: 300 px
---
El NASA DEM que muestra los Alpes (fuente: [NASA/USGS/JPL-CALTECH](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)).
:::

::::
:::::

Los valores ráster suelen tener un único valor por celda, sin embargo, también pueden tener múltiples bandas (de color). Las imágenes satelitales suelen ofrecer varias bandas para representar los datos recopilados de distintas partes del espectro de luz, que podemos utilizar para analizar distintos fenómenos, como la humedad de las plantas. Las múltiples bandas significan que usted tiene más de un valor por celda.

Las principales características espaciales son la extensión, el área que la cuadrícula representa en el mundo real (10km², 100km²), y la resolución ráster: el tamaño de cada píxel. En {numref}`en_quality_raster`, puede ver dos conjuntos de datos ráster con resoluciones diferentes.

:::{figure} /fig/en_quality_raster.png
---
width: 800px
align: center
name: en_quality_raster
---
Dos conjuntos de datos ráster con diferente resolución que cubren la misma región. (Fuente: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_3_vector_raster_data)).
:::

En {numref}`Vector` y {numref}`Raster` puede ver la misma ubicación, a la izquierda como datos vectoriales, con la visualización de las calles y de la zona urbana y a la derecha, como datos ráster (imagen satelital), que muestra la cubierta terrestre.


:::::{grid} 2
::::{card} Vectorial

:::{figure} /fig/en_same_location_vector.png
---
width: 400px
name: Vector
align: center
---
Entidad geográfica representada con datos vectoriales. (Fuente: Cruz Roja Británica).
:::

::::

::::{card} Ráster

:::{figure} /fig/en_same_location_raster.png
---
width: 400px
name: Raster
align: center
---
La misma ubicación representada como imagen ráster. (Fuente: Cruz Roja Británica).
:::

::::
:::::

#### Formatos de datos ráster

Los datos ráster pueden tener los siguientes formatos de datos:

| Extensión de nombre de archivo | Nombre | Descripción |
| ----- | --- | --- |
| `.tif`/`.tiff`/`.geotiff` | Formato de Archivo de Imagen Etiquetada | Formato común de datos ráster e imagen. No tiene necesariamente datos georreferenciados. Si un`.tif` archivo está georreferenciado, se denomina GeoTIFF. |
| `.nc` | netCDF | Formato de datos estándar para datos científicos como la velocidad o la temperatura. Puede ser un archivo ráster. Puede contener varios conjuntos de datos |
| `.asc` | Archivos de cuadrícula ASCII de Esri | Formato de archivo ráster antiguo y sencillo, siempre con datos georreferenciados |

:::{admonition} La ventaja de geodatabases

Las bases de datos como Geodatabase (`.gdb`) o GeoPackage (`gkpg`) también pueden contener capas ráster.

:::

----


## El concepto de capa

El programa SIG nos ayuda a visualizar los datos geográficos. Para ello, muestra las geometrías o celdas ráster en un lienzo 2D. Sin embargo, al crear un mapa, estamos utilizando varios conjuntos de datos a la vez. Cada tipo de dato geográfico, como datos ráster, polígonos, puntos o líneas, se suele almacenar dentro de una __capa__. Cada capa está formada por objetos geográficos del mismo tipo (línea, polígono, ráster, ...). El programa SIG muestra estas capas unas encima de otras y permite reorganizar el orden de las mismas, con el fin de crear mapas perspicaces (véase {numref}`en_layer`).


Con la incorporación de diferentes capas, construye su mapa y puede combinar información de distintas fuentes. Con ellos, podrá realizar análisis o adaptar la representación con el uso de símbolos y colores.

:::{figure} /fig/en_layer.png
---
width: 800px
align: center
name: en_layer
---
Capas en un SIG (fuente: [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers)).
:::


::::{admonition} ¡Ahora es su turno!
:class: note

La experiencia práctica es clave para dominar los SIG. Ahora es un buen momento para aplicar lo que hemos aprendido en el primer ejercicio del módulo 2.

:::{card}
:class-card: sd-text-center sd-rounded-2 sd-border-1
:link: https://giscience.github.io/gis-training-resource-center/content/es/Module_2/es_qgis_geodata_concept_ex1.html

__Módulo 2, ejercicio 1: Comprensión de los datos geográficos__

:::
::::

## Importaciones de datos

Antes de empezar a crear mapas en QGIS, tendrá que cargar sus datos en QGIS. Dependiendo del formato de archivo que desee importar, el proceso difiere ligeramente.

### Importación de datos vectoriales

Los formatos típicos de datos vectoriales son Shapefile (`.shp`) y GeoPackage (`.gpkg`). El proceso de importación de datos vectoriales en cualquiera de los dos formatos es el mismo.

QGIS ofrece varias formas de cargar datos vectoriales. La más inmediata es la de arrastrar y soltar, en la que basta con arrastrar los archivos de datos que desea añadir desde el explorador de archivos a la ventana de QGIS. Otro método es a través del “__Administrador de fuentes de datos__” (`Layer` > `Data Source Manager`).

:::{Note}
Los archivos GeoPackage pueden contener múltiples conjuntos de datos e incluso proyectos completos de QGIS. Cuando cargue un GeoPackage en QGIS, aparecerá una ventana donde podrá seleccionar los conjuntos de datos que desea cargar.
:::

#### Abrir datos vectoriales a través del administrador de fuentes de datos

1. Haga clic en `Layer`-> `Add Layer`-> `Add Vector Layer...`. Se abrirá el administrador de fuentes de datos.
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su
   archivo vectorial
3. Seleccione el archivo y haga clic en `Open`. Aparecerán más opciones. En la mayoría de los casos, puede dejar estas opciones como están.
4. De vuelta en QGIS, haga clic en `Add`

:::{Attention}
QGIS sólo le permite importar shapefile __descomprimidos__. Asegúrese de descomprimir los archivos de datos antes de importarlos a QGIS.
:::

:::{dropdown} Video: Importación de datos vectoriales a través del administrador de fuentes de datos

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>

:::

#### Abrir datos vectoriales mediante arrastrar y soltar

QGIS le permite abrir datos en su proyecto QGIS simplemente arrastrando los archivos desde su explorador de archivos a su ventana QGIS. Los shapefile sólo contienen una capa por shapefile, que se añadirá automáticamente a su panel de capas. Los archivos GeoPackage (`.gpkg`) pueden contener varias capas en un único archivo. Si añade un archivo GeoPackage, se abrirá una nueva ventana, donde se le pedirá que seleccione las capas que desea añadir al proyecto.

:::{dropdown} Video: Importación de datos vectoriales mediante arrastrar y soltar
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

### Importación de texto delimitado (.csv, .txt)


En su trayectoria en SIG, encontrará datos geográficos en formato de archivos de texto delimitados, como los archivos `.csv` (Valores separados por comas). Estos archivos contienen datos tabulares que pueden abrirse con programas como Microsoft Excel. Contienen información geográfica o de posición como coordenadas de puntos en columnas separadas (por ejemplo, latitud y longitud, o coordenadas x, y) o como "Well Known Text" (WKT), que representa geometrías complejas, como polígonos o líneas.


#### Abrir capa de texto delimitado

:::{Tip}
Para cargar datos de hojas de cálculo como Valores separados por comas (`.csv`) o Excel (`.xlsx`), los conjuntos de datos tienen que tener columnas que contengan geometría; ésta suele ser en forma de latitud (campo Y) y longitud (campo X), pero también puede estar en otros formatos, como WKT. En este caso, también puede tener geometrías complejas en su archivo de texto delimitado.  
:::

:::{figure} /fig/en_import_delimeted_text.png
---
width: 600px
align: center
name: en_import_delimeted_text
---
Importación de texto delimitado en QGIS 3.36.
:::

1. `Layer` -> `Add Layer` -> `Open Delimited Text Layer`.
2. Haga clic en `File name` haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo CSV y haga clic en `Open`.
3. `File Format`: Aquí puede especificar qué delimitador se utiliza en el archivo que desea importar. En un archivo CSV estándar se utilizan las comas `,`. Si no es el caso, seleccione `Custom delimiters`. Aquí puede elegir el delimitador exacto utilizado en su archivo.

:::{Tip}
Para averiguar qué delimitador se utiliza, puede abrir el archivo .csv en el Bloc de notas o en Excel. Allí puede comprobar qué delimitador se utiliza para separar la información.
:::

:::{figure} /fig/en_delimited_text_fileformat.png
---
width: 600px
align: center
name: en_delimited_text_fileformat
---
Ajuste de los parámetros de formato de archivo al importar una capa de texto delimitado en QGIS.
:::

4. `Geometry definition`: En esta sección se especifica qué columnas del archivo contienen la información espacial para georreferenciar los datos en el mapa. Si el archivo tiene una columna con datos de __latitud__ y otra con datos de __longitud__, puede utilizarlas para georreferenciar los datos. Compruebe `Point Coordinates` si el archivo `.csv` contiene datos de puntos. Seleccione para `X field` “LONGITUD” y para `Y field` “LATITUD”.
5. Debajo de`Geometry CRS` seleccione el sistema de referencia de coordenadas (SRC). Por defecto, QGIS seleccionará el SRC del proyecto. Si el archivo no contiene información espacial, elija la opción `No geometry (attribute only table)`.
6. Haga clic en `Add`

:::{dropdown} Video: Abrir archivos de texto delimitados en QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

:::

### Importación de datos ráster

La importación de datos ráster funciona del mismo modo que la de los datos vectoriales. Puede arrastrar y soltar los archivos ráster en la ventana de QGIS o abrirlos a través del “Administrador de fuentes de datos”.


:::{dropdown} Video: Abrir datos ráster a través del administrador de fuentes de datos

1. Haga clic en `Layer`-> `Add Layer`-> `Add Raster Layer`
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo ráster
3. Seleccione el archivo y haga clic en `Open`
4. De vuelta en QGIS, haga clic en `Add`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>

:::

:::{dropdown} Video: Abrir datos ráster mediante arrastrar y soltar

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

:::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

Compruebe si conoce los conceptos clave de este capítulo respondiendo a las preguntas siguientes.

1. __Defina datos geográficos. ¿En qué se diferencian de los datos tabulares regulares?__

:::{dropdown} Respuesta
Los datos geográficos, o datos espaciales, se refieren a la información asociada a un lugar concreto de la superficie terrestre. Incluye tanto la geometría (el componente espacial) como los atributos (los datos descriptivos). A diferencia de los datos tabulares regulares, que constan únicamente de filas y columnas sin ninguna referencia espacial, los datos geográficos tienen un componente geográfico que permite cartografiarlos y analizarlos en un contexto espacial.
:::

2. __¿Cuáles son los dos tipos principales de datos geoespaciales y cómo almacenan la información?__

:::{dropdown} Respuesta
Los dos tipos principales de datos geoespaciales son:
- Datos vectoriales: Representan las entidades geográficas con el uso de puntos, líneas y polígonos. Cada entidad geográfica tiene asociados datos de los atributos almacenados en una tabla. Los formatos más habituales son Shapefile (.shp), GeoPackage (.gpkg) y GeoJSON (.geojson).
- Datos ráster: Representa datos geográficos como una matriz de celdas (píxeles), cada una con un valor que representa información, como la temperatura o la elevación. Los formatos más habituales son GeoTIFF (.tif), JPEG2000 (.jp2) y Archivos de cuadrícula ASCII de Esri (.asc).

:::

3. __Proporcione ejemplos de fenómenos o entidades geográficas del mundo real que se representen mejor como datos vectoriales que como datos ráster.__

:::{dropdown} Respuesta
__Datos vectoriales:__ Son adecuados para representar entidades geográficas específicas con límites bien definidos, tales como:
   - Límites administrativos (países, distritos)
   - Carreteras y ríos
   - Parcelas de tierra
   - Edificios e infraestructuras
   __Datos ráster:__ Adecuado para datos continuos que varían en el espacio, como
   - imagen satelital
   - Los modelos de elevación (p.ej., modelos digitales de elevación o modelos de terreno)
   - Los mapas de temperatura o de precipitaciones
   - Los sistemas de clasificación de la cobertura terrestre
   :::

4. __Describa la estructura de un shapefile. ¿Qué archivos de componentes obligatorios deben acompañarlo?__

:::{dropdown} Respuesta

Un Shapefile es un formato de datos vectoriales ampliamente utilizado que consta de al menos tres archivos componentes obligatorios:
- `.shp`: Contiene los datos geométricos (puntos, líneas o polígonos).
- `.shx`: Contiene los datos del índice de forma, lo que permite realizar consultas espaciales rápidas.
- `.dbf`: Contiene datos de atributos en formato tabular, correspondientes a cada geometría.

También puede contener archivos adicionales como `.prj`. Estos archivos, que comparten un mismo nombre, conforman el shapefile
:::

5. __Explique el concepto de “capa” en los SIG. ¿Por qué los SIG utilizan capas para construir mapas?__

:::{dropdown}
En los SIG, una capa es un conjunto de datos geográficos que representan un tipo específico de información, como carreteras, ríos o usos del suelo. Las capas se apilan unas sobre otras para crear un mapa completo. El uso de capas permite:
- __Gestión organizada de datos__: Cada capa puede editarse o analizarse de forma independiente.
- __Visualización clara__: Se pueden estilizar y mostrar por separado diferentes tipos de datos.
- __Análisis eficaz__: Las capas pueden activarse o desactivarse para centrarse en aspectos concretos de los datos.
:::

6. __¿Sabe cómo importar datos vectoriales en un proyecto QGIS?__

:::{dropdown} Respuesta
Los datos vectoriales pueden importarse a un proyecto QGIS de la siguiente manera:
- En la barra superior, utilice el `Layer` menú → `Add vector layer`.
- Arrastre y suelte el archivo vectorial directamente en el lienzo del mapa de QGIS.
:::

7. __¿Dónde se guardan las capas importadas a un proyecto QGIS?__

:::{dropdown} Respuesta
Las capas no se almacenan dentro de un proyecto QGIS. Cuando las capas se importan en un proyecto QGIS, no se mueven ni se copian. En su lugar, QGIS almacena la ruta a la fuente de datos en el archivo del proyecto (.qgz). Si la fuente de datos se mueve o se elimina, QGIS no podrá localizarla a menos que se actualice la ruta.
Además, la manipulación de la capa modificará el conjunto de datos original.
:::


8. __Si tiene un archivo `.csv` u otro archivo de texto delimitado, ¿qué información debe contener para importarlo a QGIS como capa de puntos?__

:::{dropdown} Respuesta
Para importar un archivo `.csv` o de texto delimitado como capa de puntos en QGIS, el archivo debe:
- Contener un encabezado con los nombres del campo
- Incluir, al menos, dos columnas, que representen las coordenadas X (longitud) e Y (latitud).
- Asegúrese de que los valores de las coordenadas sean numéricos y tengan el formato correcto.

QGIS utiliza las columnas de coordenadas para trazar los puntos en el lienzo del mapa.

:::

::::
