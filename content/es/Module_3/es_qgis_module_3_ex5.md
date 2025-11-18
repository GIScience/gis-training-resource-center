::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 5: Respuesta a las inundaciones en Larkana

::::{grid} 2
:::{grid-item-card}
__Programa de ejercicios de respuesta a las inundaciones en Larkana:__
^^^

Este es el tercer ejercicio en el [Programa de ejercicios de respuesta a las inundaciones en Larkana:](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_larkana_flood_response.html).

- [Ejercicio anterior](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_data_sources_ex4.html)
- [Siguiente ejercicio](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_I_ex4.html)
:::

:::{grid-item-card}
__Competencias abordadas en este ejercicio__
^^^

- Seleccionar entidad y exportar a un archivo nuevo
- Extraer por ubicación
- Reproyectar capa
- Editar la tabla de atributos
- Clasificación
- Digitalización de una capa de puntos

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
^^^

- El ejercicio dura alrededor de 3 horas, dependiendo de la cantidad de participantes y su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki y los capítulos del módulo__
^^^

* [Importación de datos geoespaciales en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_layer_concept_wiki.html)
* [Clasificación de datos geoespaciales: por categorías](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_categorized_wiki.html)
* [Clasificación de datos geoespaciales: graduado](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_graduated_wiki.html)
* [Consultas espaciales](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_queries_wiki.html)
* [Función de tabla: agregar campo](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#add-field)
* [Digitalización: datos de punto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#add-geometries-to-a-layer)
:::
::::

:::{topic} Objetivo del ejercicio

En 2024, las provincias de Punjab, Sindh y Baluchistán en Pakistán fueron azotadas por inundaciones devastadoras debido a las lluvias intensas y prolongadas. Como resultado, la infraestructura crítica, como los centros de salud, se vio afectada y el acceso por carretera a la ciudad de Larkana se vio limitado en gran medida. En los siguientes ejercicios se utilizarán datos reales de este desastre natural. El objetivo es identificar los centros médicos y centros de salud específicos que se vieron afectados por las inundaciones. Además, evaluaremos la viabilidad del acceso por carretera a la ciudad de Larkana el 12 de agosto de 2024.

Los participantes trabajarán con múltiples capas y realizarán consultas espaciales. Además, aprenderán a crear sus propios datos geoespaciales. El ejercicio consta de tres tareas. En la primera parte, exportaremos los límites administrativos en nuestra área de interés. En la segunda tarea, se extraerán los centros de salud que se encuentran en nuestra área de interés e identificaremos qué centros de salud se encuentran dentro de la capa de extensión de inundación. En la tercera tarea, se identificará qué carreteras pueden estar inundadas para poder determinar el acceso por carretera.
:::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra en Miro) en la que los participantes puedan agregar sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html) para obtener consejos generales sobre cómo impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos hayan descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y aplicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su propio proyecto de QGIS.

__Cierre de la sesión:__

- Dedique tiempo al final del ejercicio a cualquier problema o pregunta relacionada con las tareas que pueda surgir.
- Reserve tiempo para preguntas abiertas.

:::

## Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood.zip

__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood.zip), guarde la carpeta en su computadora y descomprima el archivo.__

:::


| Conjunto de datos | Título original | Publicado por | Descargado de |
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_Sindh_adm1.gpkg | [Límites administrativos subnacionales](https://data.humdata.org/dataset/cod-ab-pak) | Oficina de la ONU para la Coordinación de Asuntos Humanitarios | HDX |
| PAK_Sindh_adm2.gpkg | [Límites administrativos subnacionales](https://data.humdata.org/dataset/cod-ab-pak) | Oficina de la ONU para la Coordinación de Asuntos Humanitarios | HDX |
| PAK_Sind_Health_Facilities.gpkg | [Centros de salud de Pakistán (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) | Equipo humanitario de OpenStreetMap (HOT) | HDX |
| VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [El satélite detectó extensiones de agua del 8 al 12 de agosto de 2024 sobre Pakistán)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) | UNO SAT | HDX |
| Roads_Larkana.gpkg | [Carreteras de Larkana](https://export.hotosm.org/v3/exports/7f1e78c7-f671-41e3-9ec3-6fc6ac31c929) | Equipo humanitario de OpenStreetMap | Herramienta de exportación HOT (exportación creada en septiembre de 2024) |

<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint}

__[Aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood_Day2.zip)__ se puede descargar la capa de extensión de la inundación reproyectada y fija

:::

:::{hint} Estructura de las carpetas
Para mantener sus datos organizados y de fácil acceso, es importante establecer una estructura de carpetas clara en su computadora para sus proyectos de QGIS y sus datos geoespaciales. Asegúrese de que los datos de su ejercicio se guardan en un lugar que permita una fácil recuperación y asociación con el proyecto QGIS correspondiente.
:::


<!---
:::{figure} /fig/M3_Ex5_workflow_chart.drawio.png
---
name: M5_Ex5_Workflow_chart
width: 450 px
---
:::
-->

## Tarea 1: Obtener una visión general de la situación en los alrededores de Larkana

::::{card}
__Contexto__
^^^

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
:::

Usted ha sido asignado como gestor de información en las regiones de Pakistán afectadas por las inundaciones. A su llegada recibió informes del equipo de operaciones que indican que la ciudad de [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) y sus alrededores han sido gravemente afectadas por las inundaciones. El equipo necesita una visión general de la ubicación de la ciudad.

::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_1.png
---
name: Task_1_workflow
width: 750 px
---

:::

::::{margin}
:::{admonition} Consejo
:class: note
No se puede interactuar con un mapa base.
:::
::::
1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) haciendo clic en `Project` -> `New`
2. Una vez creado el proyecto [guarde el proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#save) en la carpeta del ejercicio “Modul3_Exercise_2_Flood_Larkana”. Para hacer esto, haga clic en `Project` -> `Save as` y navegue hasta la carpeta. Nombre el proyecto “PAK_Larkana_flood_2024”.
3. Primero, queremos agregar el OpenStreetMap como mapa base para la orientación. Para añadir el OSM como mapa base, haga clic en `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Elija `OpenStreetMap` y haga clic en `Add`.
4. A continuación, cargue el GeoPackage __“PAK_Sindh_adm2.gpkg”__ en su proyecto. Para hacerlo, debe arrastrar y soltar ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html)). O haga clic en `Layer`-> `Add Layer`-> `Add Vector Layer`. Haga clic en los tres puntos ![](/fig/Three_points.png) de tres puntos y navegue hasta __"PAK_Sindh_adm2.gpkg"__. Seleccione el archivo y hacer clic en `Open`. De vuelta en QGIS, haga clic en `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html)).


:::{Attention}
Los archivos GeoPackage pueden contener varios archivos e incluso proyectos QGIS completos. Cuando cargue un archivo de este tipo en QGIS aparecerá una ventana en la que deberá seleccionar los archivos que desea cargar en su proyecto de QGIS.
:::

5. Para obtener una visión general de la situación, debemos exportar los límites administrativos para nuestra Área de Interés (AOI). Para hacerlo, debemos exportar el distrito de __Larkana__, así como los distritos vecinos, desde la capa `PAK_adm2_Sindh`.
    - Haga <kbd>clic derecho</kbd> en la capa `PAK_adm2_Sindh` y seleccionar [Abrir tabla de atributos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html).
    - Busque la columna `ADM2_EN` y la fila para el distrito de Larkana.
    - <kbd>Haga clic</kbd> en los números a la izquierda de la ventana de la tabla de atributos para seleccionar la entidad Larkana. La fila aparecerá de azul y el área de Larkana se volverá amarilla en el lienzo del mapa.
    - <kbd>Haga clic</kbd> en `Zoom Map to selected rows` en la barra superior de la ventana de la tabla de atributos. ![](/fig/qgis_3.36_zoom_to_selected_rows_at.png)
    - Cierre la tabla de atributos.
    ::::{margin}
    :::{tip}
    Mantener <kbd>Ctrl</kbd> mientras selecciona entidades geográfica le permite agregar más entidades a su selección actual. De lo contrario, anulará la selección del polígono anterior.
    Tenga en cuenta que solo puede seleccionar entidades geográficas de la capa que ha seleccionado actualmente en el panel capas.
    ::::
    - En la barra de herramientas en la parte superior de la ventana de QGIS, seleccione la herramienta `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png). Mantenga presionado <kbd>Ctrl</kbd> y <kbd>haga clic</kbd> en los distritos que rodean el distrito de Larkana ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_queries_wiki.html#manual-selection)). Los seis distritos seleccionados se verán de color amarillo en el lienzo del mapa.
    <!--FIX: The districts named are not the only ones surrounding the -->
    - Desactive la herramienta `Select Feature(s)`. Para hacerlo, haga clic en el icono ![](/fig/qgis_move_symbol.png) en la barra de herramientas en la parte superior de la ventana de QGIS.
    - Ahora podemos exportar las entidad geográfica seleccionadas y guardarlas en un nuevo archivo. Haga clic derecho en la capa de `PAK_adm2_Sindh` y seleccione `Export` > `Save Selected Features as`.
    - Se abrirá una nueva ventana. Aquí, puede seleccionar cómo y dónde se guardan las entidades seleccionadas.
    :::{figure} /fig/en_qgis_3.36_m3_ex5_export_features.png
    ---
    name: m3_ex5_export_selection
    width: 450 px
    ---
    Asegúrese de guardar el GeoPackage en la ubicación correcta haciendo clic en los tres puntos a la derecha del campo `File name`.
    :::
    - En `Format`, seleccionar GeoPackage.
    - A la derecha del campo de `File name`, haga clic en los tres puntos. Vaya a la carpeta con los datos del ejercicio y guárdelos en la carpeta `data/temp/`.
    - Introduzca un nombre de capa. Por ejemplo, “__Flood_2024_AOI__”.
    - Haga clic en `Ok`. La capa exportada debe aparecer en el panel Capas.

::::{margin}
:::{Tip}
¡Recuerde guardar su proyecto de vez en cuando!
:::
::::

:::{topic} Logro

Ahora tiene una visión general de dónde se encuentra el distrito de Larkana en Sindh. El equipo de operaciones puede utilizar esta información.

:::



## Tarea 2: Estimación del impacto de las inundaciones en el sector de la salud en Larkana

::::{card}
__Contexto__
^^^

:::{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
:::

Las publicaciones en redes sociales han señalado un impacto significativo en el sistema sanitario de la región. Se le ha encomendado recabar toda la información posible sobre la situación y, si fuera factible, estimar el impacto sobre el sistema de salud.

::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_2.png
---
name: task_2_workflow
width: 750 px
---

:::

1. En primer lugar, debemos averiguar dónde se encuentran los centros de salud en la zona. Podemos encontrar conjuntos de datos mediante una búsqueda rápida en el [Intercambio de Datos Humanitarios (HDX)](https://data.humdata.org). Allí puede encontrarse el conjunto de datos denominado “Centros de salud de Pakistán (exportado de OpenStreetMap)”. Usaremos este conjunto de datos. El conjunto de datos ya está disponible en la carpeta de descargas para este ejercicio.
    - Importe el GeoPackage `PAK_Health_Facilities_complete.gpgk` en su proyecto. Puede arrastrarlo al lienzo del mapa o abrir la ventana de importación haciendo clic en `Layer` > `Add Layer` > `Add Vector Layer` en la barra superior de QGIS ([consulte la página](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html) Wiki). Aparecerá una nueva capa con datos de punto en el lienzo del mapa.
    - Una vez que hayamos importado los centros de salud, podremos extraer aquellos que se encuentren dentro de nuestra área de interés. Podemos lograrlo con la herramienta `Extract by Location`.
    - En la __caja de herramientas de Procesos__ ([abriendo la caja](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html#open-toolbox)), busque la herramienta “Extraer por ubicación”. <kbd>Haga doble clic</kbd> en ella. Se abrirá una nueva ventana.
    :::{figure} /fig/PAK_extract_locatio_HS.png
    ---
    width: 400px
    name: Extract by location Pakistan
    align: center
    ---
    Extraer las instalaciones sanitarias de nuestra área de interés mediante la herramienta “Extraer por ubicación”.
    :::
    - Como `Input Layer`, seleccione la capa `PAK_Health_Facilities_complete`.
    - El `Geometric predicate` debe establecerse en `Intersect`
    - En `By comparing to the features from`, seleccione la capa de área de interés “__Flood_2024_AOI__”.
    - En `Extracted (location)`, haga clic en los tres puntos y seleccione `Save to Geopackage`.
    - Vaya a la carpeta `/Module_3_Exercise_5_Larkana_Flood/data/temp/`.
    - Asigne al archivo el nombre __“Health_Facilities_Flood_2024_AOI”__ y haga clic en `Save`.
    - Se le pedirá que introduzca un nombre de capa. Use el mismo nombre que el archivo y haga clic en `Ok`.
    - Haga clic en `Run`. La nueva capa aparecerá en la pestaña Capas.


Ahora tenemos una visión general de la ubicación de los centros de salud. Sin embargo, queremos saber qué centros de salud se ven afectados por la inundación. Afortunadamente, la ONU acaba de compartir un conjunto de datos sobre el alcance de las inundaciones del 8 al 12 de agosto, que podemos superponer con nuestra capa con los sitios de salud para identificar los sitios de salud que están en la zona inundada.

2. Importe el conjunto de datos __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ en su proyecto QGIS.
3. Una vez cargadas las capas en QGIS, podrá comprobar si se muestran correctamente. Sin embargo, al comprobar la información de las capas, puede ver que las nuevas capas tienen un Sistema de Referencia de Coordenadas (SRC) diferente. Tienen el código EPSG 9707, mientras que nuestro proyecto tiene el 4326 ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projections_wiki.html)).
    * <kbd>Haga clic derecho</kbd> en la capa y seleccione `Properties`. Se abrirá la ventana de propiedades.
    -  En la barra de pestañas vertical de la izquierda, vaya hasta `Information`. Aquí encontrará información adicional sobre el conjunto de datos seleccionado.
    * Bajo el título “Sistema de referencia de coordenadas (SRC)", encontrará toda la información sobre el SRC. Los más importantes son:
    - __Nombre:__ aquí encontrará el código EPSG.
    - __Unidades:__ aquí encontrará información sobre las unidades de medida utilizadas en el conjunto de datos. Por ejemplo, metros o grados. <!--ADD: Why is it a problem? Add explanation-->
4. Esto se convertirá en un problema tan pronto como hagamos algo diferente de solo mostrar las capas. Ya que queremos manipular las capas en el siguiente paso, primero necesitamos reproyectarlas ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projections_wiki.html)).
    * En la parte superior de la ventana de QGIS, </kbd>haga clic</kbd> en la pestaña `Vector` > `Data Management Tools` -> `Reproject Layer` o busque la herramienta en la `Processing Toolbox`.
    * Como `Input layer`, seleccione __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__
    * Como destino, seleccione el código SRC/EPSG __4326__.
    * Guarde el nuevo archivo en su carpeta de `temp` haciendo clic en los tres de puntos ![](/fig/Three_points.png) junto a `Reprojected`, especifique el nombre del archivo como __“2024_MinFloodExtend_reprojected”__.
    * Haga clic en `Run`.
    * Elimine la capa antigua del panel de capas haciendo clic derecho sobre la capa -> `Remove layer`.
    * Ajuste la opacidad de la capa de inundación haciendo clic derecho sobre la capa __“2024_MinFloodExtend_reprojected”__ en el Panel de capas y seleccionando `Properties`. La ventana de propiedades se abrirá con una sección de pestaña vertical a la izquierda.
    - Vaya a la pestaña `Symbology`.
    - Mueva el control deslizante y ajuste la opacidad a alrededor del 60 %.

<!--Symbology tab has not been covered in the modules yet.-->

Hemos observado que ciertas centros de salud han sido afectados por las inundaciones. Para visualizar esta información en el mapa, planeamos incluir un nuevo atributo llamado __“Flood_affected”__ en la tabla de atributos de __“Health_Facilities_Flood_2024_AOI”__. Para lograr esto, seleccionaremos todas los centros de salud que se encuentran dentro de la extensión de la inundación utilizando la herramienta “Seleccionar por ubicación”. En un siguiente paso, agregaremos una nueva columna a la tabla de atributos y agregaremos información a nuestros centros de salud seleccionados.

5. Abra el `Processing Toolbox` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html)) y busque la herramienta __“Seleccionar por ubicación”__.
    * `Select features from` = __“Health_Facilities_Flood_2024_AOI”__.
    * Como `Geometric predicate` utilizamos `intersect`.
    * Para `By comparing to the features from`, usamos la capa __“2024_MinFloodExtent_reprojected”__.
    * `Modify current selection by` = `creating new selection`.
    * Haga clic en `Run`.

:::{figure} /fig/PAK_flood_select_by_location.PNG
---
width: 400px
name: Select flood affected health facilities
align: center
---
Selección de los centros de salud afectados por las inundaciones mediante la herramienta “Seleccionar por ubicación”
:::

::::{admonition} Mensaje de posible error
:class: warning, dropdown
En caso de que encuentre el error:

```
Feature (1) from “2024_MinFloodExtend_reprojected” has invalid geometry. 
Please fix the geometry or change the Processing setting to the “Ignore 
invalid input features” option.
Execution failed after 0.07 seconds
```

Primero debe usar la herramienta __“Corregir geometría”__ antes de repetir el paso 5 fallido anteriormente de usar la herramienta __“Seleccionar por ubicación”__.

* Para ello, abra el [`Processing Toolbox`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html) y busque la herramienta __“Arreglar geometrías”__.
* `Input layer` = `2024_MinFloodExtend_reprojected`
* Guarde el nuevo archivo en su carpeta de `temp` haciendo clic en el ![](/fig/Three_points.png) de tres puntos, especifique el nombre del archivo como __“2024_MinFloodExtend_reprojected_fix”__.
* Haga clic en `Run`.

:::{figure} /fig/ PAK_flood_ngeomertrie_error.PNG
---
width: 400px
name: Fix Geometry
align: center
---
El mensaje de error indica geometrías no válidas.
:::

::::

6. Podemos editar la tabla de atributos para las entidades que hemos seleccionado:
    - Abra la tabla de atributos de __“Health_Facilities_Flood_2024_AOI”__ haciendo clic derecho sobre la capa -> `Open Attribute Table`([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html))
    - Active el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png) ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html)). Ahora puede editar los datos directamente en la tabla.
    - Queremos agregar una nueva columna con el nombre __"Flood_affected"__ para identificar qué centros de salud se encuentran dentro de la extensión de la inundación. Haga clic en ![](/fig/mActionNewAttribute.png). Se abrirá una nueva ventana.
    - En la ventana de `Add field`, agregue el nombre de la columna y especifique el `Type` a `Text (string)` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#add-new-column)).
    - Haga clic en `Ok`.


:::{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column Pakistan
align: center
---
Agregar una nueva columna a la tabla de atributos para la capa de centros de salud
:::

7. A continuación, queremos editar las filas de la tabla de atributos para las entidades que hemos seleccionado.
    - Busque la opción `Show all Features` en la esquina inferior izquierda y haga clic en ella.
    - Seleccione la opción `Show selected features` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). Esto filtrará la tabla para mostrar solo las filas que representan los centros de salud directamente afectados por la inundación.
    - Escriba `Yes` en la columna __“Flood_affected”__ en cada fila seleccionada.
    - Cuando haya terminado, haga clic en ![](/fig/mActionSaveEdits.png) para guardar sus ediciones y desactive el modo de edición haciendo clic de nuevo en ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
    - Haga clic en el icono ![](/fig/selection_toolbar_feature_deselection.png) en la barra de herramientas para finalizar la selección de entidades.

8. Podemos mostrar el conjunto de datos enriquecido y visualizarlo mediante el método de simbolización de clasificación por categorías. Esto significa que seleccionamos una columna de la tabla de atributos y usamos los valores o el contenido como categorías para ordenar y mostrar los datos ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_categorized_wiki.html)):
    - En el panel de capas, haga clic derecho en la capa __“Health_Facilities_Flood_2024_AOI”__ y seleccione `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda.
    - Vaya a la pestaña `Symbology`.
    - En la parte superior de la ventana, encontrará un menú desplegable. Ábralo y elija `Categorized`.
    - En `Value`, seleccione la columna que añadimos, “Flood_affected”.
    - Más abajo en la ventana, haga clic en `Classify`. Deben aparecer los valores únicos de la columna “Flood_affected”.
    - Puede hacer doble clic en cada color de la tabla para ajustar la simbolización y el color de cada valor.
    - Una vez que haya terminado de ajustar los colores, haga clic en `Apply` y, a continuación, en `Ok` para cerrar la ventana de simbolización.

:::{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Clasificación de los centros de salud afectados por las inundaciones.
:::

:::{card}
__Logro:__
^^^

Hemos localizado los centros de salud específicos que han sido afectados por las inundaciones. Nuestras conclusiones indican que un total de cuatro instalaciones han quedado completamente inundadas y actualmente no están operativas. Considerando que evaluamos el impacto mínimo de las inundaciones, es muy probable que más centros de salud también se vean afectados. Estos datos son fundamentales para nuestro equipo operativo, ya que les permitirán elaborar estrategias y ejecutar una respuesta eficaz.

:::

## Tarea 3: Acceso logístico a la ciudad de Larkana

::::{card}
__Contexto__
^^^

:::{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
align: right
name: IFRC Logistics Icon
---
:::

El equipo de operaciones está haciendo planes para entregar suministros muy necesarios a la región afectada alrededor de Larkana. Actualmente, hay incertidumbre sobre cómo se pueden transportar los suministros allí. El equipo de operaciones ha pedido más información sobre este tema.

Necesitan respuestas a las tres preguntas siguientes:
* ¿Cuáles de las carreteras que conducen a Larkana están bloqueadas y en qué lugares específicos están bloqueadas?
* ¿Hay algún puente que se pueda cruzar desde el lado oriental del Indo hasta el lado occidental, y dónde se encuentran estos puentes?
* Si no es posible transportar suministros por carretera a la región, ¿qué método alternativo podría utilizarse para entregarlos?

Para tener una imagen más clara, necesitamos importar los datos de la red vial de la región a QGIS. Busque el archivo en la carpeta de entrada. La red vial se muestra inicialmente sin ningún tipo de carretera ni otros detalles relevantes. Debemos aplicar una técnica de clasificación categorizada solo para mostrar las carreteras específicas que nos interesan.
::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_3.png
---
name: Task_3_workflow
width: 750 px
---

:::


1. Cargue el conjunto de datos __“Roads_Larkana.gpkg”__ desde la carpeta de entrada en su proyecto QGIS.
2. Configuremos la clasificación por categorías. En los datos de OpenStreetMap se distingue entre diferentes tipos de carreteras utilizando la columna “autopista”.
    - Haga clic derecho en la capa __“Roads_Larkana”__ y seleccione `Properties`. Se abrirá la ventana de propiedades.
    - Vaya a la pestaña `Symbology`.
    - En la parte superior, seleccione `Categorized` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_categorized_wiki.html)).
    - En `Value`, seleccione “autopista”.
    - Haga clic en `Classify`. Debería ver todos los valores únicos de la columna “autopista”.
    - Quite las marcas de verificación de todas las categorías excepto de `motorway`, `primary`, `secondary` y `trunk`.
    - Para ajustar los colores, puede hacer doble clic en las categorías.
    :::{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Ventana de simbolización para la capa Roads_Larkana.gpkg.
    :::
    - Tiene la opción de personalizar el ancho de las líneas de las carreteras principales para mejorar la visualización. Abra la ventana de simbología y seleccione `Symbol`. En la nueva ventana, se puede ajustar el ancho de las líneas según su preferencia.
    :::{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Ajuste de la simbolización de los diferentes tipos de carreteras
    :::
    - Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.

::::{margin}
:::{tip}
Existen métodos para automatizar el proceso de digitalización que se tratarán en el [módulo 5: Operaciones intermedias del SIG](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_5/es_module_5_overview.html).
:::
::::

3. Por último, queremos visualizar las carreteras que están inundadas. Para simplificar el proceso, buscaremos manualmente las carreteras que se intersecan con la capa de extensión de inundación y las marcaremos con puntos. Para ello, crearemos un nuevo conjunto de datos de puntos que representen las carreteras bloqueadas.
    * Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#create-a-new-layer))
    - En `Database`, haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp`. Asigne al nuevo conjunto de datos el nombre __“PAK_flood_2024_blocked_road”__. Haga clic en `Save`.
    - `Geometry type`: Seleccione `Point`
    - En `Additional dimension` debe asegurarse siempre de que `None` está marcada.
    - Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”. Por defecto, QGIS selecciona el SRC del proyecto.
    - En `New Field` puede añadir columnas a la nueva capa. Agregue la columna __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: Seleccione `Text(string)`
        * Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
        * Cree otro campo con el `name` __"Blocked_bridge"__ y el `Type`: Seleccione `Text(string)`.
        * Haga clic en `OK`.
    * Su nueva capa aparecerá en el panel de capas.
    :::{figure} /fig/PAK_blocked_road_new_layer.png
    ---
    width: 400px
    name: Pakistan road classification
    align: center
    ---
    Creación de una nueva capa de puntos. Asegúrese de especificar una ubicación utilizando los tres puntos en la parte superior.
    :::

::::{margin}
:::{tip}
Si no puede ver la barra de herramientas, haga clic en la pestaña `View` -> `Toolbars` y marque `Digitizing Toolbar` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#creation-of-point-data)).
:::
::::

4. Ahora puede crear un punto para cada lugar donde la capa de inundación cubre las carreteras principales que conducen a Larkana ([Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#creation-of-point-data)).
    * Actualmente la nueva capa __“PAK_flood_2024_blocked_road”__ está vacía. Para agregar entidades, podemos usar `Digitizing Toolbar`. ![](/fig/Digitizing_Toolbar.png).
    * Active el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png). A continuación, active la opción de agregar nuevos puntos haciendo clic en ![](/fig/mActionCapturePoint.png) `Add Point Feature`.
    * Esté atento a los lugares donde la capa de inundación cubre las carreteras principales o puentes que salen de Larkana. Una vez que haya encontrado uno, haga clic con el botón izquierdo en la ubicación que desea digitalizar.
    * Una vez que haga clic en un lugar, aparecerá una ventana. Escriba `Yes` en el `Blocked_road` de campo para indicar que la carretera está bloqueada.
    * Repita este paso con todas las ubicaciones que encuentre.

    :::{figure} /fig/PAK_blocked_road_digitalise.png
    ---
    width: 400px
    name: Digitising blocked roads
    align: center
    ---
    Esta ventana emergente se abrirá una vez que haya seleccionado una ubicación para agregar un punto. Asegúrese de introducir la información pertinente en las columnas.
    :::

    * Una vez que haya terminado la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
    * Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

5. Ahora, ya hemos mapeado todas las carreteras principales bloqueadas de acceso a Larkana. Podemos usar iconos en lugar de solo puntos para mostrar la capa __“PAK_flood_2024_blocked_road”__ y visualizar mejor este hecho ([Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_single_symbol_wiki.html)).

    * Haga clic derecho en la capa __“PAK_flood_2024_blocked_road”__ en el panel de Capas y haga clic en `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Symbology`.
    * Mantenga la opción `Single Symbol`. Seleccione cualquier símbolo de la lista, que sea adecuado para marcar carreteras bloqueadas.
    * Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.
    * Después de que haya terminado, haga clic en el icono ![](/fig/qgis_move_symbol.png) para cerrar el modo de selección de entidades.

    :::{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visualising blocked roads with icons
    align: center
    ---
    Ajuste de la simbolización para la nueva capa de puntos. Asegúrese de elegir un marcador que pueda identificarse fácilmente.
    :::

Parte de su tarea era señalar posibles alternativas al transporte por carretera. ¿Puede identificar alguno?

::::{dropdown} __Respuesta__

En el suroeste de la ciudad de Larkana, se encuentra el [Aeropuerto de Mohenjodaro](https://www.google.com/search?q=Larkana&rlz=1C1GCEA_enDE1048DE1048&oq=Larkana&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORjjAhiABDIHCAEQLhiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIGCAYQRRg9MgYIBxBFGD2oAgiwAgE&sourceid=chrome&ie=UTF-8#vhid=0x0:0xf59fc8243b2b9d0e&vssid=lclsmap&eim=CAEQDhoRMjcuMzI4NDM3NTc5NDIyNjIiETY4LjE0MjA5NTk3MDUzNTQ4KhQxNzY5OTA4NTExODUyNjQzMDQ3OA). Actualmente, la carretera que va de la ciudad de Larkana al aeropuerto parece estar abierta y accesible. Esto significa que los suministros esenciales podrían transportarse desde el aeropuerto a la ciudad sin encontrar ningún bloqueo en la carretera.

:::{figure} /fig/PAK_road_access_airport.png
---
width: 600px
name: Road access to Mohenjodaro Airport
align: center
---
Acceso por carretera al aeropuerto de Mohenjodaro
:::
::::

:::{card}

El equipo de operaciones tiene ahora toda la información que necesita para planificar su logística. Buen trabajo.

:::


::::{admonition} Continúe con el programa de ejercicios
:class: note

:::{figure} /fig/IFRC-icons-colour_Map.png
---
width: 100px
align: right
name: IFRC map icon
---
:::

Este ejercicio forma parte del __Programa de ejercicios de respuesta a las inundaciones en Larkana__ y continúa con un ejercicio en el módulo 4.

Haga clic [aquí](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_I_ex2.html) si desea continuar con el siguiente ejercicio de este programa.

::::
