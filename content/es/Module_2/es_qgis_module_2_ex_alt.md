::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 5: El mundo

## Características del ejercicio

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Objetivo del ejercicio:__
^^^

Este ejercicio le ayudará a conocer un poco mejor la interfaz de QGIS. Además, cargará sus primeros datos en QGIS y obtendrá experiencia práctica con el concepto de capa y aprenderá a reproyectar las capas.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Competencias abordadas en este ejercicio:__
^^^
- Creación y guardado de un nuevo proyecto QGIS
- Importación de datos vectoriales (.shp y .gpkg) así como también de datos tabulares (.txt)
- Comprensión del concepto de capa
- Navegación por la interfaz QGIS y el lienzo del mapa


:::

::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
^^^
- El ejercicio dura unos 30 minutos, dependiendo del número de participantes y capacitadores.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki__
^^^

* [Interfaz de QGIS](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_interface_wiki.html)
* [Tipos de datos geoespaciales](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_geodata_types_wiki.html)
* [Importación de datos geoespaciales en QGIS](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_layer_concept_wiki.html)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos los participantes hayan instalado QGIS y que hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html) para obtener algunos consejos generales para impartirlas.

### Impartir la capacitación

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

## Datos disponibles

:::{card}
:class-card: sd-text-center
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Module_2_Exercise_5_The_World.zip

__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Module_2_Exercise_5_The_World.zip), guarde la carpeta en su computadora y descomprima el archivo.__

:::

La carpeta se llama “Module_2_Exercise_5_The_World” y contiene toda la [estructura de carpetas estándar](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_geodata_management.html#estructura-de-carpetas-estandar) con todos los datos en la carpeta de entrada y la documentación adicional en la carpeta de documentación.

- [Países del mundo (generalizado)](https://hub.arcgis.com/datasets/2b93b06dc0dc4e809d3c8db5cb96ba69_0/explore) (Polígono/Shapefile)
- [Conjunto de datos de terremotos significativos](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ngdc.mgg.hazards:G012153) (CSV)
- [Conjunto de datos globales de centrales eléctricas](https://datasets.wri.org/dataset/globalpowerplantdatabase) (Puntos/GeoPackage)

## Tareas

::::{margin}
:::{tip}
Asegúrese de __descomprimir__ la carpeta de ejercicios antes de comenzar las actividades. De lo contrario, no podrá importar los conjuntos de datos a QGIS.
:::
::::

1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#paso-a-paso-creacion-de-un-nuevo-proyecto-qgis-desde-cero) haciendo clic en `Proyecto` -> `Nuevo proyecto`

2. Una vez creado el proyecto, guárdelo en la `/Project`-subcarpeta en la `/Module_2_Exercise_5_The_World`/. En la barra superior, haga clic en `Proyecto` -> `Guardar como...` y navegue hasta la carpeta. Nombre al proyecto “Module_2_Ex_5_The_World”.


3. Cargue el shapefile `World_countries_generalized.shp` en su proyecto arrastrando y soltando ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#abra-los-datos-vectoriales-mediante-la-funcion-arrastrar-y-soltar)). O haga clic en `Capa` → `Añadir capa` → `Añadir capa vectorial`. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta "World_countries__generalized". Seleccione el archivo y haga clic en `Abrir`. De vuelta en QGIS, haga clic `Añadir` ([Video de la Wiki](/content/es/Wiki/es_qgis_import_geodata_wiki.md#open-vector-data-via-layer-tab)).

    :::{Attention}
        Con ambos métodos, debe seleccionar el archivo con la terminación `.shp`! Un [shapefile consta de varios archivos](https://giscience.github.io/gis-training-resource-center/content/es/Module_2/es_qgis_geodata_concept.html#shapefile-structure) que se referencian entre sí. El archivo que contiene la información de geometría es el archivo que termina con `.shp`.
        :::

4. Cargue el archivo GeoPackage `global_power_plant_database_nuclear.gpkg` en el proyecto QGIS. Puede utilizar uno de los métodos utilizados en el paso anterior: Arrastre y suelte ([video en Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) el archivo o haga clic en `Capa`-> `Añadir capa`-> `Añadir capa vectorial`. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta `/data/input/`. Seleccione el archivo y haga clic en `Abrir`. De vuelta en QGIS, haga clic `Añadir`([Video de la Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).

    :::{Note}
        Los archivos GeoPackage pueden contener múltiples archivos e incluso proyectos QGIS completos. Cuando cargue un archivo de este tipo en QGIS, aparecerá una ventana en la que debe seleccionar los archivos que desea cargar en su proyecto QGIS.
    :::

5. A continuación, queremos cargar el archivo `Significant_earthquake_data.txt` en QGIS. Dado que se trata de datos vectoriales en formato de texto, debemos seguir pasos específicos ([Video de la Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-csv-data-in-qgis)).
    * Haga clic en `Capa`-> `Añadir capa`-> `Añadir capa de texto delimitado`. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta `Significant_earthquake_data.txt` en la `data/input/`-subcarpeta. Seleccione el archivo y haga clic en `Abrir`.
    * En la ventana “Administrador de fuentes de datos| Texto delimitado” en QGIS, abra el menú desplegable `Formato de archivo` verifique `Delimitadores personalizados` y `Tabulador`
    * Abra el menú desplegable `Definición de geometría`. Asegúrese de que la opción `Coordenadas del punto` esté marcada. Además, seleccione para `Campo X` “LONGITUD” y para `Campo Y` “LATITUD”.
    * Seleccione el SRC "EPSG:4326-WGS 84".
    * Hacer clic en `Añadir`.
    :::{Note}
    Al cargar datos vectoriales en formato de texto como .csv o .txt en QGIS, estos datos deben tener columnas de latitud y longitud.
    * `Campo X` =“LONGITUD”.
    * `Campo Y` = “LATITUD”.
    :::

    :::{figure} /fig/en_ex_The_world_add_text_layer_import.png
    ---
    width: 600px
    name: es_ex5_import_text_layer
    align: center
    ---
    :::

6. En el panel de capas de la izquierda, organice las tres capas en un orden práctico. Recuerde el [Concepto de capas](/content/es/Wiki/es_qgis_layer_concept_wiki.md). La capa de países deberá estar situada debajo de las capas de terremotos y centrales eléctricas.

:::{figure} /fig/Module_2/en_m2_ex_5_interface_explanation.png
---
name: es_m2_ex_5_interface_explanation
width: 750 px
---
:::

::::{margin}
:::{tip}
También puede mover el mapa, haciendo clic en el lienzo del mapa y manteniendo presionada la <kbd>barra espaciadora</kbd>. Esto activará automáticamente la herramienta manual, mientras presiona la barra espaciadora. Desplazarse con el mouse también le permite acercar y alejar el lienzo del mapa. Mantener presionadas la tecla<kbd>Ctrl</kbd> en Windows o la tecla<kbd>Cmd</kbd> en MacOS, le permite acercar el zoom en pasos más pequeños.
:::
::::

7. Interactúe con el mapa y explore los conjuntos de datos. Utilice la herramienta de zoom y mueva el mapa. ¿Dónde se pueden encontrar muchos terremotos y dónde se encuentran la mayoría de las centrales eléctricas?

::::{margin}
:::{Tip}
Si observa un `*` antes del nombre de su proyecto en la esquina superior izquierda de QGIS, esto significa que hay cambios no guardados en su proyecto. ¡Guarde su progreso!
:::
::::

8. Guarde el proyecto haciendo clic en el botón ![](/fig/mActionFileSave.png) o use la combinación de teclas de acceso rápido <kbd>Ctrl</kbd> + <kbd>G</kbd>.

9. Sus resultados deberían verse así:

:::{figure} /fig/en_ex_The_world_result.png
---
width: 600px
name: es_the_world_result
align: center
---
:::









