::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 3: Fuentes de datos

<!--This exercise is quite minimal with the explanation of steps (most should be looked up) so it is not suited for a follow along session -->

## Características del ejercicio

:::{card}
:class-card: sd-text-justify
__Objetivo del ejercicio:__
^^^

El objetivo de este ejercicio es navegar por diversas fuentes de datos, comprender en
dónde y cómo acceder a los datos pertinentes e identificar posibles problemas. Es importante **utilizar fuentes de datos fiables, actualizadas y apropiadas** que se ajusten al propósito del análisis para garantizar resultados satisfactorios y significativos. Tenga siempre en cuenta sus objetivos y requisitos de análisis y busque los datos en consecuencia.

:::

::::{grid} 2
:::{grid-item-card}
__Serie de ejercicios para la respuesta ante inundaciones en Larkana__
^^^

Este ejercicio forma parte de la [serie de ejercicios para la respuesta ante inundaciones en Larkana](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_larkana_flood_response.html).

:::

:::{grid-item-card}
__Competencias abordadas en este ejercicio__
^^^

- Fundamentos de QGIS
- Buscar y descargar conjuntos de datos pertinentes y prepararlos para su posterior análisis
- Alfabetización en datos

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura aproximadamente una hora, dependiendo del número de participantes y de su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki y capítulos del módulo__
^^^

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Tipos de datos geoespaciales](/content/es/Wiki/es_qgis_geodata_types_wiki.md)
* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Concepto de capa](/content/es/Wiki/es_qgis_layer_concept_wiki.md)
* [Clasificación de datos geoespaciales: graduado](/content/es/Wiki/es_qgis_graduated_wiki.md)
* [Fuentes de datos](https://giscience.github.io/gis-training-resource-center/content/es/Module_2/es_data_sources.html)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__
## Preparar la capacitación:

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos los participantes hayan instalado QGIS y que hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener algunos consejos generales para impartirlas.

## Impartir la capacitación

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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Backup/Module_2_Exercise_3_Data_Sources.zip

Descargue los datos y el archivo del proyecto para este ejercicio [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Backup/Module_2_Exercise_3_Data_Sources.zip) y descomprima la carpeta.


:::


::::{dropdown} Estructura de carpetas estándar
:::{figure} /fig/standard_folder_structure_new_2025.drawio.png
name: standard_folder_struc
width: 500 px
---
Estructura de carpetas estándar. Fuente: HeiGIT
:::
::::

### Tarea 1: Descargar los límites administrativos y los centros de salud de Pakistán

Para nuestro mapa de respuesta a inundaciones, necesitaremos algunos conjuntos de datos de la web. En este ejercicio, buscaremos los __límites administrativos__ de Pakistán, los __centros de salud__, así como la __extensión de la inundación__ durante la inundación en Pakistán, en 2024.
En primer lugar, configuraremos un nuevo proyecto en QGIS junto con la estructura de carpetas estándar:

::::{margin}
:::{tip}
Observe la estructura de carpetas estándar y guarde el archivo del proyecto de QGIS en el lugar correcto.
:::
::::

1. Descargue la estructura de carpetas y descomprímala.
2. Cree una copia de la estructura de carpetas y nombre la carpeta `module_2_exercise_3_data_sources`.
3. Abra un nuevo proyecto en QGIS y guárdelo en la carpeta.

Ahora que tenemos el proyecto de QGIS configurado, podemos empezar a buscar los conjuntos de datos

4. Busque una fuente de datos para descargar los **límites administrativos** y **los centros de salud** de Pakistán. Las siguientes instrucciones están diseñadas para el ejemplo de Pakistán. Si desea realizar el mismo análisis para otro país, algunas instrucciones pueden diferir, pero el flujo de trabajo general seguirá siendo el mismo.

:::{dropdown} Posibles fuentes de datos

En Internet hay muchos repositorios de datos diferentes donde puede encontrar datos adecuados. Puede encontrar una lista de posibles fuentes de datos [aquí](https://giscience.github.io/gis-training-resource-center/content/es/Module_2/es_data_sources.html).

Para la mayoría de los datos humanitarios, puede buscar en __[Intercambio de Datos Humanitarios/HDX](https://data.humdata.org/)__.
El Intercambio de Datos Humanitarios (HDX) es una plataforma primaria para acceder y compartir datos geoespaciales relevantes para las crisis humanitarias. Se trata de un repositorio centralizado que ofrece una amplia gama de conjuntos de datos de diversas fuentes, lo que lo convierte en un recurso invaluable para las organizaciones de ayuda humanitaria y los investigadores.

:::

:::{admonition} Qué formato de datos elegir

La mayoría de los conjuntos de datos de HDX están disponibles en varios formatos, como xlsx, csv, shapefile o GeoJSON. Buscamos datos espaciales que podamos utilizar en QGIS, por lo que necesitaremos un formato de datos espaciales como `.shp` (Shapefile), `.gpkg` (GeoPackage), `.geojson` (GeoJSON) o `.gdb` (GeoDatabase).

:::

<!-- SUGGESTION: some of the instructions below assume that these are the datasets
   that are being used, instead of just examples. Can we just ask people to use these
   datasets, so that the rest of the instructions make sense? -->

5. Descargue los datos y guarde los **límites administrativos** y los **centros de salud** en la carpeta `data\input`.

:::{Note}
Asegúrese de utilizar únicamente los datos de puntos del conjunto de datos de los centros de salud. En este ejemplo pueden ignorarse otras formas de datos, como líneas o polígonos. Dependiendo de la fuente de datos, la información puede proporcionarse como puntos, pero también como líneas o
polígonos.
:::

::::{margin}
:::{tip}
La mayoría de las veces, los conjuntos de datos que se descargan de Internet están comprimidos como archivos `.zip`. Antes de poder utilizarlos en QGIS, __es necesario descomprimir los conjuntos de datos__.
:::
::::

6. [Cargue ambos archivos vectoriales en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_geodata_concept.html#data-import).


7. Ahora añada el mapa base de OpenStreetMap a través de la ventana del navegador >
`XYZ Tiles`. Añadir mapas base puede ayudarle a orientarse, comprender mejor el área de interés y crear mapas más informativos.

8. Familiarícese con los datos abriendo la tabla de atributos e identifique los distintos tipos de asistencia médica que se incluyen en el conjunto de datos. Obtenga una visión general de la información que se almacena en cada columna. Por ejemplo, podría haber información que indique el tipo de centro de salud.


9. Si su conjunto de datos contiene información sobre el tipo de centro de salud (p. ej., clínica, hospital, médico, etc.), podemos extraerla y guardarla en una nueva capa. Para ello, seleccionamos los hospitales y los copiamos en una nueva capa.

:::{Hint}

Para obtener información sobre cómo filtrar fácilmente sus datos seleccionando manualmente entidades en la tabla de atributos después de haberla ordenado en función de una columna concreta, consulte la página __[tabla de atributos](/content/es/Wiki/es_qgis_attribute_table_wiki.md)__ en la wiki.

:::

### Tarea 2: Descargar la extensión de la inundación en Pakistán en agosto de 2024

Ahora, descarguemos la extensión de la inundación en Pakistán del 8 al 12 de agosto de 2024.

1. Regrese al Intercambio de Datos Humanitarios y busque __“Inundación en Pakistán”__. Encontrará una lista de conjuntos de datos que contienen las extensiones de agua detectadas por satélite para diferentes períodos.
2. Elija el conjunto de datos con el título __“El satélite detectó extensiones de agua del 8 al 12 de agosto de 2024 sobre Pakistán”__ y descargue la carpeta comprimida.
3. Descomprima la carpeta y mire su contenido. Existen varios shapefiles diferentes. Buscamos la __extensión mínima de la inundación__. Localice los archivos llamados `VIIRS_20240721_20240803_MinimumFloodExtent_PAK` y cópielos en la carpeta `data\input`.

:::{admonition} Trabajar con shapefiles
:class: attention
Los archivos shapefiles constan de varios archivos (`.shp`, `.shx`, `.sbx`, `.sbn`, `.prj`, `cpg`). Para copiar todo el archivo shapefile a la nueva ubicación, __asegúrese de copiar todos los archivos con el nombre exacto a la nueva carpeta__.

:::

