::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 2: Procesamiento básico de datos geoespaciales

## Características del ejercicio

:::{card}
__Objetivo de este ejercicio:__
^^^

El objetivo de este ejercicio es familiarizarse con los datos geoespaciales y empezar a trabajar
con ellos. Comprender la tabla de atributos, ordenarla, seleccionar manualmente y exportar la
selección, así como cargar un mapa base.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Fundamentos de QGIS
- Navegación por la interfaz de QGIS
- Orden y manipulación de conjuntos de datos mediante la tabla de atributos
- Selección de las proyecciones cartográficas correctas
- Ejecución de análisis espaciales básicos y avanzados

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura aproximadamente una hora, dependiendo del número de participantes y de su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Interfaz de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html)
* [Importación de datos geoespaciales en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_layer_concept_wiki.html)
* [Tabla de atributos en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.md)
* [Proyecciones cartográficas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projections_wiki.html)
<!-- FIXME: to be updated -->

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__
__Preparar la capacitación:__

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos los participantes hayan instalado QGIS y que hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html#como-planificar-una-capacitacion-en-sig) para obtener algunos consejos generales para impartirlas.

__Impartir la capacitación:__

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes han descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y replicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio para asegurarse de que todos comprenden y realizan los pasos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Esencialmente, los participantes están realizando varias tareas a la vez, prestando atención a sus instrucciones y orientándose en su propio proyecto QGIS.

__Cierre de la sesión:__

- Reserve tiempo para cualquier cuestión o pregunta relacionada con las tareas al final del ejercicio.
- Reserve tiempo para preguntas abiertas.

:::

## Ejercicio

### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_2/Module_2_Exercise_2_Basic_Geodata_Processing.zip

__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_2/Module_2_Exercise_2_Basic_geodata_processing.zip), guarde la carpeta en su computadora y descomprima el archivo.__

:::

La carpeta comprimida incluye:

| Nombre del conjunto de datos | Título original | Publicado por | Descargado de |
| :-------------- | :----------------- |:----------------- |:----------------- |
| `nigeria_populated_places.shp` | Lugares poblados de Nigeria (Exportación de OpenStreetMap) | Equipo Humanitario de OpenStreetMap (HOT) | [HDX](https://data.humdata.org/dataset/hotosm_nga_populated_places) |
| `nigeria_boundaries.geojson` |   |   |   |

<!---The zip folder includes:

- `nigeria_populated_places.shp` (Points) Shapefile
- `nigeria_boundaries.geojson` GeoJSON
--->

El archivo shapefile de lugares poblados contiene __datos de puntos__ sobre asentamientos humanos en Nigeria, incluyendo ciudades, pueblos y otros. El archivo GeoJSON de los límites de Nigeria contiene información sobre los límites administrativos en los niveles 2 y 4; el nivel 2 representa todo el país y el nivel 4 los estados.

:::{note}

Los archivos GeoJSON no admiten múltiples capas, por lo que los polígonos de los límites de los países y los estados se fusionan en una sola capa __en la que los distintos polígonos se superponen__.

:::

<!--ADD: Explanation about how GeoJSON apparently merges different layers?-->

### Tareas

1. Cargue ambos archivos en QGIS.

2. Añada el mapa base de OpenStreetMap a través del panel del navegador →
   XYZ Tiles.

3. Familiarícese con los datos abriendo la tabla de atributos. Determinar la ubicación de los datos y el tipo de información que contienen. Comprenda las distintas columnas y los datos que contienen en su tabla de atributos e intente hacerse una idea general de qué columnas serán relevantes e importantes para su análisis.

4. En la capa `nigeria_populated_places`, abra la tabla de atributos, seleccione
   el objeto para **Zuyel** y haga zoom al punto seleccionado.

:::{Hint}
El lugar comienza con una *Z* por lo que podría ser de ayuda ordenar la columna `name` en
orden descendente.
:::

5. Exportar **Zuyel** como GeoPackage independiente. Compruebe la proyección cartográfica y elija un
   SRC adecuado. Nómbrelo `zuyel.gpkg`.

:::{Note}
Dado que no se realizan cálculos, p. ej., de área, WGS84 (EPSG:4326) es una buena elección.
:::


6. Repita los pasos para la capa `nigeria_boundaries.geojson` y exporte únicamente
el distrito en el que se encuentra **Zuyel**. Nómbrelo como corresponda. Para encontrar el distrito utilice la herramienta ![](/fig/qgis_identify_features.png) `Identificar objetos espaciales` y después seleccione manualmente el distrito correcto en la tabla de atributos.

7. Elimine todas las capas iniciales y, a continuación, abra la tabla de atributos de cada una de las nuevas capas y compruebe que cada capa solo contiene una entidad.

8. Guarde su proyecto.

### Resultado

:::{figure} /fig/en_result_geodata_processing_exercise.png
---
width: 80%
name: en_result_geodata_processing_exercise
---
Este es el aspecto que podría tener el resultado final
:::

<!-- FIXME: We have not asked people to remove the initial layers so they would
	also show in the layers list -->