::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Ejercicio 6: Respuesta a las inundaciones de Sava

::::{grid} 2
:::{grid-item-card}
__Objetivo del ejercicio:__
^^^

Los participantes trabajarán con múltiples capas y realizarán consultas espaciales. Además, aprenderán a crear sus propios datos geoespaciales.

__Tipo de ejercicio de capacitación:__

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Fundamentos de QGIS
- Trabajar con varias capas
- Realizar consultas espaciales
- Creación de datos geoespaciales

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura alrededor de 3 horas, dependiendo de la cantidad de participantes y su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Importación de datos geoespaciales en QGIS](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_layer_concept_wiki.html)
* [Clasificación de datos geoespaciales: por categorías](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_categorized_wiki.html)
* [Clasificación de datos geoespaciales: graduado](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_graduated_wiki.html)
* [Consultas espaciales](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_spatial_queries_wiki.html)
* [Función de tabla: agregar campo](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_table_functions_wiki.html#add-field)
* [Digitalización: datos de punto](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_digitisation_wiki.html#add-geometries-to-a-layer)

:::
::::

::::{grid} 1
:::{grid-item-card}
__Contexto:__
^^^

“El 3 de abril, luego del paso del ciclón tropical (ST) Gamane, que azotó el norte y el noreste de Madagascar el 27 de marzo, el Gobierno declaró emergencia nacional” [Madagascar: Actualización Rápida No. 2 sobre el Ciclón Tropical Gamane, 4 de abril de 2024 (ReliefWeb)](https://reliefweb.int/report/madagascar/madagascar-tropical-cyclone-gamane-flash-update-no-2-4-april-2024). El siguiente análisis utilizará datos reales de esta catástrofe natural. El objetivo es identificar los centros médicos y centros de salud específicos que se vieron afectados por las inundaciones. Además, evaluaremos la viabilidad del acceso por carretera a los lugares poblados.

:::
::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra en Miro) en la que los participantes puedan agregar sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](https://giscience.github.io/gis-training-resource-center/content/es/Trainers_corner/es_how_to_training.html#how-to-do-trainings) para obtener consejos generales sobre cómo impartirlas.

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

### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip

__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip), guarde la carpeta en su computadora y descomprima el archivo.__

:::

<!--:::{hint}
Reprojected and fixed Flood extend layer can be downloaded __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/______________.zip)__
:::-->

| Nombre del conjunto de datos | Título original | Publicado por | Descargar desde |
| :-------------------- | :----------------- |:----------------- |:----------------- |
| mdg_admin1.shp | [Límites administrativos subnacionales](https://data.humdata.org/dataset/cod-ab-mdg) | Oficina de la ONU para la Coordinación de Asuntos Humanitarios | HDX |
| mdg_admin2.shp | [Límites administrativos subnacionales](https://data.humdata.org/dataset/cod-ab-mdg) | Oficina de la ONU para la Coordinación de Asuntos Humanitarios | HDX |
| hotosm_mdg_health_facilities.gpkg | [Centros de salud de Madagascar (exportado de OpenStreetMap)]([https://data.humdata.org/dataset/hotosm_pak_health_facilities](https://data.humdata.org/dataset/madagascar-healthsites)) | Equipo humanitario de OpenStreetMap (HOT) | HDX |
| TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp | [Extensión de agua detectada por satélite sobre los distritos de Sambava y Vohemar, región de Sava, Madagascar al 1 de abril de 2024]([[https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024))) | UNOSAT | HDX |
| roads_sava.gpkg | Carreteras de Sava | Equipo humanitario de OpenStreetMap | Herramienta de exportación HOT |


<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint} Estructura de las carpetas

Para mantener sus datos organizados y de fácil acceso, es importante establecer una estructura de carpetas clara en su computadora para sus proyectos de QGIS y sus datos geoespaciales. Asegúrese de que los datos de su ejercicio se guardan en un lugar que permita una fácil recuperación y asociación con el proyecto QGIS correspondiente.

:::


## Tarea 1: Obtener una visión general de la situación en los alrededores de Sambava y Vehomar

::::{card}

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
name:
align: right
name: IFRC Surge Icon
---
:::

__Contexto:__

Usted ha sido enviado como gestor de información a las regiones de Madagascar afectadas por las inundaciones. A su llegada recibió informes del equipo de operaciones que indican que los distritos de [Sambava y Vohemar](https://www.openstreetmap.org/search?query=Sava%2C%20Madagascar#map=8/-14.374/49.795) de la región de Sava están afectados por las inundaciones. El equipo necesita una visión general de los lugares afectados.

::::

1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) haciendo clic en `Project` -> `New`
2. Una vez creado el proyecto [guárdelo](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#save) en la carpeta “proyecto” del ejercicio “Modul3_Exercise_2_Flood_Larkana”. Para hacer esto, haga clic en `Project` -> `Save as` y navegue hasta la carpeta. Nombre el proyecto “MDG_Sava_flood_2024”.
3. Primero, queremos agregar el OpenStreetMap como mapa base para la orientación. Para añadir el OSM como mapa base, haga clic en `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Elija `OpenStreetMap` y haga clic en `Add`.

:::{Tip}
No se puede interactuar con un mapa base.
:::

4. A continuación, cargue el GeoPackage __"mdg_admin2.gpkg"__ en su proyecto. Para hacerlo, solo tiene que arrastrar y soltar ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). O haga clic en `Layer`-> `Add Layer`-> `Add Vector Layer`. Haga clic en los tres puntos ![](/fig/Three_points.png) y vaya hasta __"mdg_admin2.gpkg"__. Seleccione el archivo y hacer clic en `Open`. De vuelta en QGIS, haga clic en `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


:::{Attention}
Los archivos GeoPackage pueden contener varios archivos e incluso proyectos QGIS completos. Cuando cargue un archivo de este tipo en QGIS aparecerá una ventana en la que deberá seleccionar los archivos que desea cargar en su proyecto de QGIS.
:::

5. En primer lugar, queremos exportar el distrito __Sambava__ y el distrito vecino __Vohemar__ desde __mdg_admin2__ para tenerlo como capa vectorial independiente. Para hacer esto:
    * Abra la tabla de atributos de __mdg_admin2__ haciendo clic derecho en la capa -> `Open Attribute Table`([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html)).
    * Busque la fila de Sambava en la columna __ADM2_ES__ y márquela haciendo clic en el número situado en el extremo izquierdo de la tabla de atributos. La fila aparecerá en color azul y la zona de Sambava se volverá de color amarilla en el lienzo del mapa. Puede hacer clic con el botón derecho en la fila y hacer clic en `Zoom to Feature`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
        Para seleccionar el distrito de Vohemar, haga clic en el icono `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) de la barra de herramientas de QGIS, mantenga presionado el botón `Shift` del teclado y haga clic en los distritos, ya sea en el mapa o en la tabla de atributos ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_spatial_queries_wiki.html#manual-selection)).
    * Cuando haya terminado de seleccionar los distritos, haga clic en el icono ![](/fig/qgis_move_symbol.png) para finalizar el modo de selección de entidades geográficas.
    * Ahora haga clic derecho en la capa en el Panel de Capas y luego haga clic en `Export` -> `Save Selected Features as`. Queremos guardar los distritos seleccionados como un GeoPackage, así que elija la opción `Format` en consecuencia. Haga clic en los tres puntos y navegue hasta su carpeta `temp`. Aquí puede nombrar la capa como __“Flood_2024_AOI”__ y haga clic en `Save`. Ahora debería ver el mismo nombre en el campo `Layer name`. Haga clic en `Ok`([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))
    * Haga clic en el icono ![](/fig/selection_toolbar_feature_deselection.png) en la barra de herramientas para finalizar la selección de entidades.

:::{card}
__Logro:__
^^^

Ahora tiene una visión general de dónde se encuentran los distritos de Sambava y Vohemar en Sava. El equipo de operaciones puede utilizar esta información.

:::

:::{Tip}
¡Recuerde guardar su proyecto de vez en cuando!
:::

## Tarea 2: Estimación del impacto de las inundaciones en el sector sanitario de Sambava y Vohemar

::::{card}

:::{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
:::

__Contexto:__

Las publicaciones en las redes sociales han indicado un impacto significativo en el sistema sanitario de Madagascar. Se le ha encargado que averigüe todo lo que pueda sobre la situación en Sava y, si es posible, que calcule el impacto en el sistema sanitario.

::::

1. Lo primero que hay que hacer es averiguar dónde se encuentran los centros de salud de la zona. Para ello, haga una búsqueda rápida en HDX. Encontrará el conjunto de datos con los Centros de salud de Madagascar (exportado de OpenStreetMap). Esto bastará por ahora.

    * Cargue el GeoPackage __“hotosm_mdg_health_facilities.gpkg”__ en su proyecto. Para hacerlo, solo tiene que arrastrar y soltar ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). O haga clic en `Layer`-> `Add Layer`-> `Add Vector Layer`. Haga clic en los tres puntos ![](/fig/Three_points.png) y vaya hasta __"mdg_admin2.gpkg"__. Seleccione el archivo y hacer clic en `Open`. De vuelta en QGIS, haga clic en `Add` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    * En primer lugar, debemos extraer los centros de salud que se encuentran en nuestra área de interés. Para ello utilizaremos la herramienta __“Extract by Location”__.
    * Abra la página `Processing Toolbox` ([así se hace](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_interface_wiki.html#open-toolbox)) y busque la herramienta.
        * Como `Input Layer` usaremos “hotosm_mdg_health_facilities”.
        * Para `By comparing to the features from` utilizamos la capa “Flood_2024_AOI”.
        * Como `Geometric predicate` utilizamos `intersect`.
        * Para guardar el resultado, haga clic en los tres puntos de `Extract (location)` -> `Save to GeoPackage` y vaya a la carpeta `temp`. Guarde la nueva capa con el nombre __“Health_Facilities_Flood_2024_AOI”__. Dé a la nueva capa el mismo `Layer name` y haga clic en `Run`.
    * Abra la tabla de atributos de la nueva capa y eche un vistazo.

:::{figure} /fig/m3_ex6_qgis_task2_1.png
---
width: 400px
name: m3_ex6_qgis_task2_1
align: center
---
Extraiga por ubicación.
:::

Bien, ahora tenemos una buena visión general de la ubicación de los centros de salud. Necesitamos mucha más información sobre la zona inundada para identificar los centros sanitarios afectados por la inundación. Afortunadamente, la ONU acaba de compartir un conjunto de datos sobre el alcance de las inundaciones. Extensión de agua detectada por satélite sobre los distritos de Sambava y Vohemar, región de Sava, Madagascar al 1 de abril de 2024

2. Cargue el conjunto de datos __“TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp”__ en QGIS.
   * Ajuste la opacidad de la capa de inundación haciendo clic con el botón derecho en la capa __“TDX_20240401_FloodExtent_SambavaDistrict_MDG”__ en el Panel de Capas y haga clic en `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Symbology`. Debe mover el control deslizante y ajustar la opacidad a alrededor del 60 %.
<!--3. Once you have loaded the layers in QGIS, you can see that they are correctly displayed. However, upon checking the layer information, you can see that the new layers have a different Coordinate Reference System (CRS). They have the EPSG Code 9707 whereas our project has 4326 ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * Right click on the data layer, click on “Properties”.
    * The “Layer Properties” Window of the data layer will open. Click on “Information”.
    * Under the headline “Coordinate Reference System (CRS)” you find all information about the CRS. The most important are:
    - __Name:__     Here you find the EPSG Code.
    - __Unites:__    Here you can find whether it is possible to use meters with this data layer, degrees or latitude and longitude.
4. This will be a problem as soon as we do something different then just displaying the layers. Since we want to manipulate the layers in the next step we need to reproject them first ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)).
    * Click on the `Vector` tab -> `Data Management Tools` -> `Reproject Layer` or search for the tool in the `Processing Toolbox`.
    * As `Input layer` select __"TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp"__
    * Select as target CRS/ EPSG-Code __4326__.
    * Save the new file in your `temp` folder by clicking on the three dots ![](/fig/Three_points.png) next to `Reprojected`, specify the file name as __"2024_MinFloodExtend_reprojected"__.
    * Click `Run`
    * Delete the old layer from the layer panel by right click on the layer -> `Remove layer`.
    * Adjust the opacity of the flood layer by right-clicking on layer __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__ in the Layer Panel and click on `Properties`. A new window will open up with a vertical tab section on the left. Navigate to the `Symbology` tab. Adjusted the opacity to around 60 % by moving the   slider.-->

Hemos observado que algunos centros de salud se encuentran dentro de la zona inundada. Para visualizar esta información en el mapa, planeamos incluir un nuevo atributo llamado __“afectado”__ en la tabla de atributos de __“Health_Facilities_Flood_2024_AOI”__.
Para ello, nuestro primer paso consistirá en seleccionar todos los centros sanitarios afectados. A continuación, se agrega una nueva columna con esta información a la tabla de atributos __“Health_Facilities_Flood_2024_AOI”__.

5. Abra `Processing Toolbox` ([aquí se explica cómo](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_interface_wiki.html#open-toolbox)) y busque la herramienta __“Select by Location”__.
    * `Select features from` = __“Health_Facilities_Flood_2024_AOI”__.
    * Como `Geometric predicate` utilizamos `intersect`.
    * Para `By comparing to the features from` utilizamos la capa __“TDX_20240401_FloodExtent_SambavaDistrict_MDG”__.
    * `Modify current selection by` = `creating new selection`.
    * Haga clic en `Run`.

:::{card}
Tenga en cuenta lo siguiente: Basándonos en los datos originales, ningún centro de salud se vio afectado por la inundación, pero a efectos de aprendizaje de QGIS, hemos colocado tres centros de salud ficticios en las zonas inundadas.
:::


:::{figure} /fig/m3_ex6_qgis_task2_5.png
---
width: 400px
name: m3_ex6_qgis_task2_5
align: center
---
Selección de centros de salud afectados por las inundaciones
:::

::::{warning}

En caso de que encuentre el error:

La entidad (1) de “TDX_20240401_FloodExtent_SambavaDistrict_MDG” tiene una geometría no válida. Corrija la geometría o cambie la configuración de Procesamiento a la opción “Ignorar entidades de entrada no válidas”.
Falló la ejecución después de 0,07 segundos

Primero debe usar la herramienta __“Corregir geometría”__ antes de repetir el paso 5 fallido anteriormente de usar la herramienta __“Seleccionar por ubicación”__.

* Para ello, abra `Processing Toolbox` ([aquí se explica cómo](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_interface_wiki.html#open-toolbox)) y busque la herramienta __"Reparar geometrías"__.
* `Input layer` = `TDX_20240401_FloodExtent_SambavaDistrict_MDG`
* Guarde el nuevo archivo en su carpeta `temp` haciendo clic en los tres puntos ![](/fig/Three_points.png), especifique el nombre del archivo como __“TDX_20240401_FloodExtent_SambavaDistrict_MDG_fix”__.
* Haga clic en `Run`.

:::{figure} /fig/ m3_ex6_qgis_fix.png
---
width: 400px
name: m3_ex6_qgis_fix
align: center
---
Corregir geometría
:::

::::

6.  Abra la tabla de atributos de __“Health_Facilities_Flood_2024_AOI”__ haciendo clic con el botón derecho en la capa -> `Open Attribute Table`([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html)) y active el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png) ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Ahora puede editar los datos directamente en la tabla.
7. En primer lugar, agregamos una nueva columna con el nombre __“Flood_affected”__. Para hacer esto, haga clic en ![](/fig/mActionNewAttribute.png). En la ventana `Add field`, tiene que agregar el nombre y establecer el `Type` a `Text(string)`. Haga clic en `OK` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html#add-new-column))


:::{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column
align: center
---
Agregar nueva columna
:::

8. Ahora busque la opción `Show all Features` en la esquina inferior izquierda y haga clic en ella. A continuación, seleccione la opción `Show selected features` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). Esto filtrará la tabla para mostrar solo las filas que representan los centros de salud directamente afectados por la inundación.
Afortunadamente, ningún centro de salud se ha visto directamente afectado por la inundación.
9. Si alguno se ha visto afectado: Escriba `Yes` en la columna __“Flood_affected”__.
 * Cuando haya terminado, haga clic en ![](/fig/mActionSaveEdits.png) para guardar sus ediciones y desactive el modo de edición haciendo clic de nuevo en ![](/fig/mActionToggleEditing.png)([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
 * Haga clic en el icono ![](/fig/selection_toolbar_feature_deselection.png) en la barra de herramientas para finalizar la selección de entidades.

* Para visualizar el conjunto de datos enriquecidos, utilizamos la función "Clasificación por categorías". Esto significa que seleccionamos una columna de la tabla de atributos y utilizamos el contenido como categorías para ordenar y mostrar los datos ([Wiki Video](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_categorized_wiki.html)).
    * Haga clic con el botón derecho en la capa __“Health_Facilities_Flood_2024_AOI”__ en el Panel de capas y haga clic en `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Symbology`.
    * En la parte superior encontrará un menú desplegable. Ábralo y elija `Categorized`. En `Value` seleccione “Flood_affected”.
    * Más abajo, haga clic en `Classify`. Ahora debería ver todos los valores únicos o atributos de la columna “Flood_affected” seleccionada. Puede ajustar los colores haciendo doble clic en cada color del campo central. Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.

:::{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Clasificación de los centros de salud afectados por las inundaciones
:::

:::{card}
__Logro:__
Hemos localizado 3 centros de salud afectados por las inundaciones.
:::

## Tarea 3: Acceso logístico

::::{card}

:::{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
align: right
name: IFRC Logistics Icon
---
:::

Contexto:

El equipo de operaciones está haciendo planes para entregar los suministros que tanto necesitan las regiones afectadas de Sambava y Vohemar. Actualmente, hay incertidumbre sobre cómo se pueden transportar los suministros allí. El equipo de operaciones ha pedido más información sobre este tema.
Necesitan respuestas a las tres preguntas siguientes:

* ¿Cuáles de las carreteras que conducen a las regiones afectadas están bloqueadas y en qué lugares se encuentran los bloqueos?
<!--* Are there any bridges that can be crossed from the eastern side of the Indus to the western side, and where are these bridges located?-->
* Si no es posible transportar suministros por carretera a la región, ¿qué método alternativo podría utilizarse para entregarlos?


Para tener una imagen más clara, necesitamos importar los datos de la red vial de la región a QGIS. Busque el archivo en la carpeta de entrada. La red vial se muestra inicialmente sin ningún tipo de carretera ni otros detalles relevantes. Debemos aplicar una técnica de clasificación categorizada solo para mostrar las carreteras específicas que nos interesan.
::::

1. Cargue el conjunto de datos __"roads_sava.gpkg"__ de su carpeta de entrada en su QGIS.
2. Para la clasificación por categorías, haga clic con el botón derecho en la capa __"roads_sava"__ en el Panel de capas y haga clic en `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Symbology` ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_categorized_wiki.html)).
    * En la parte superior encontrará un menú desplegable. Ábralo y elija `Categorized`. En `Value`, seleccione “autopista”.
    * Más abajo, haga clic en `Classify`. Ahora debería ver todos los valores únicos o atributos de la columna “Flood_affacted” seleccionada. Puede ajustar los colores haciendo doble clic en los colores de cada fila del campo central.
    * Elimine la marca de todas las categorías excepto: `motorway`, `primary`, `secondary`, `trunk`
    :::{figure} /fig/m3_ex6_qgis_task3_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2
    align: center
    ---
    Clasificación de las carreteras
    :::
    * Tiene la opción de personalizar el ancho de las líneas de las carreteras principales para mejorar la visualización. Abra la ventana de simbología y seleccione `Symbol`. En la nueva ventana, se puede ajustar el ancho de las líneas según su preferencia.
    :::{figure} /fig/m3_ex6_qgis_task3_2_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2_2
    align: center
    ---
    Clasificación de las carreteras
    :::
    * Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.
3. Para simplificar el proceso, buscaremos visualmente las carreteras bloqueadas y las marcaremos con puntos. Para ello, crearemos un conjunto de datos de puntos completamente nuevo que represente las carreteras bloqueadas.
    * Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([video en Wiki](https://giscience.github.io/gis-training-resource-centeres/Wiki/es_qgis_digitisation_wiki.html#create-a-new-layer))
    - En `Database`, haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp`. Asigne al nuevo conjunto de datos el nombre __“MDG_flood_2024_blocked_road”__. Haga clic en `Save`.
    - `Geometry type`: Seleccione `Point`
    - En `Additional dimension` siempre debe asegurarse de que no marcar ninguno de estos.
    - Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”. Por defecto, QGIS selecciona el SRC del proyecto.
    - En `New Field` puede añadir columnas a la nueva capa. Agregue la columna __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: Seleccione `Text (string)`
        * Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
        * Cree otro campo con el `name` __"Blocked_bridge"__ y el `Type`: Seleccione `Text (string)`.
        * Haga clic en `OK`.
    * La nueva capa aparecerá en `Layer Panel`
    :::{figure} /fig/m3_ex6_qgis_Task3_3.png
    ---
    width: 400px
    name: m3_ex6_qgis_Task3_3
    align: center
    ---
    Nueva capa con las carreteras bloqueadas.
    :::
4. Ahora puede crear un punto para cada lugar en el que la capa de inundación cubra las carreteras principales que atraviesan el área de interés [wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_digitisation_wiki.html#creation-of-point-data). Actualmente la nueva capa __“MDG_flood_2024_blocked_road”__ está vacía. Para añadir entidades podemos utilizar la `Digitizing Toolbar`. Si no puede ver la barra de herramientas, haga clic en la pestaña`View` -> `Toolbars` y marque `Digitizing Toolbar` ([video en Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#creation-of-point-data)). ![](/fig/Digitizing_Toolbar.png)
    * Active el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png). A continuación, active la opción para agregar nuevos puntos haciendo clic en ![](/fig/mActionCapturePoint.png).
    * Busque lugares donde la capa de inundación cubra las carreteras principales o los puentes. Una vez que haya encontrado uno, haga clic con el botón izquierdo en la ubicación que desea digitalizar.
    * Una vez que haga clic en un lugar, aparecerá una ventana. Escriba `Yes` en el `Blocked_road` de campo para indicar que la carretera está bloqueada.
    * Repita este paso con todas las ubicaciones que encuentre.
    :::{figure} /fig/m3_ex6_qgis_task3_4.png
    ---
    width: 200px
    name: m3_ex6_qgis_task3_4
    align: center
    ---
    Digitalización de carreteras bloqueadas
    :::
    * Una vez que haya terminado la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
    * Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.
5. Ahora, hemos mapeado todas las carreteras de nuestra AOI que están bloqueadas por la inundación. Podemos utilizar iconos en lugar de solo puntos para mostrar la capa __“MDG_flood_2024_blocked_road”__ para visualizar mejor este hecho [wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_single_symbol_wiki.html).

    * Haga clic derecho en la capa __“MDG_flood_2024_blocked_road”__ en el panel de Capas y haga clic en `Properties`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Symbology`.
    * Mantenga la opción `Single Symbol`. Seleccione cualquier símbolo de la lista que sea apropiado para señalizar carreteras bloqueadas (asegúrese de que el filtro está configurado en `Favourites` o `All Symbols`).
    * Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.
    * Después de que haya terminado, haga clic en el icono ![](/fig/qgis_move_symbol.png) para cerrar el modo de selección de entidades.
    :::{figure} /fig/m3_ex6_qgis_task3_5.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_5
    align: center
    ---
    Visualización de carreteras bloqueadas con iconos
    :::

:::{card}

El equipo de operaciones tiene ahora toda la información que necesita para planificar su logística. Buen trabajo.

:::
