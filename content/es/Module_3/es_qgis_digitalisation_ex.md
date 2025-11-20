::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 1 (Digitalización): Acceso a instituciones financieras

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Objetivo del ejercicio:__
^^^

En este ejercicio, aprenderá a digitalizar puntos, líneas y polígonos de entidades en asentamientos por medio de la creación de nuevos conjuntos de datos.

__Tipo de ejercicio de capacitación:__

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para:__
^^^

- Recopilar y digitalizar datos.
- Fijar la información espacial.

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura unas 2 horas, dependiendo del número de participantes y de su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Tipos de datos geoespaciales](/content/es/Wiki/es_qgis_geodata_types_wiki.md)
* [Digitalización](/content/es/Wiki/es_qgis_digitisation_wiki.md)
* [Mapas base](/content/es/Wiki/es_qgis_basemaps_wiki.md)

:::

::::

## Instrucciones para capacitadores

:::{admonition} Nota sobre los complementos
:class: attention

Este ejercicio emplea un complemento que no está instalado por defecto: `OSM Place Search`. Asegúrese de instalarlo. Además, en lugar de utilizar XYZ Tiles para el mapa base, puede optar por utilizar el complemento __QuickMapServices__.

:::

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra en Miro) en la que los participantes puedan agregar sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](/content/es/Trainers_corner/es_how_to_training.mdhow-to-do-trainings) para obtener consejos generales sobre cómo impartirlas.

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


:::{Attention}
Intente utilizar siempre la estructura de carpetas estándar. Puede encontrar una plantilla __[aquí](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.mf#standard-folder-structure)__.
:::

## Antecedentes: Escasez de efectivo en Abuja

En 2022 hubo escasez de efectivo en Nigeria. Las pequeñas empresas dependen en gran medida de las transacciones y los servicios en efectivo. Esto provocó una crisis de liquidez en Abuja, la capital de Nigeria. [Artículo sobre la crisis de efectivo en Abuja](https://businessday.ng/news/article/business-groan-as-cash-crunch-hits-banks-in-abuja/). 

## Tarea: Mapear los bancos

Nuestro objetivo es crear capas de puntos en los tres bancos cercanos entre sí en el distrito central de negocios (DCN) de Abuja (Nigeria). De este modo, los ciudadanos podrán identificar fácilmente los bancos del DCN de Abuja para realizar sus transacciones.

Para ello, visualizaremos la digitalización del First Bank, el edificio del Bank of Industry y el Zenith Bank Abuja.

### Añadir un mapa base

1. Añada el OSM como mapa base. Para añadir el OSM como mapa base, haga clic en `Layer` -> `Add Layer` -> `Add XYZ Layer…`. Elija `OpenStreetMap` y haga clic en `Add`.
Organice la capa en `Layer Panel` de forma que el OSM esté en la parte inferior ([video en Wiki](/content/es/Wiki/es_qgis_basemaps_wiki.md))

:::{Tip}
No se puede interactuar con un mapa base.
:::

2. Para añadir el complemento `OSM Place Search`, haga clic en `Plugins` -> `Manage and Install Plugins…` -> `All` y busque `OSM Place Search`. Una vez que lo haya encontrado, haga clic sobre él y luego en `Install Plugin`. Puede abrir `OSM Place Search Panel` como cualquier otro panel, haciendo clic en `View` -> `Panels` y marcando `OSM Place Search Panel`([video en Wiki](/content/es/Wiki/es_qgis_plugins_wiki.md)).
3. En el panel `OSM place search`, busque “Abuja Central Business District” y elija “Abuja Municipality Area Council, City”. Acérquese al distrito central de negocios (Central Business District). Queremos digitalizar la ubicación de los bancos en esta zona.
Para ello, tendremos que crear una nueva capa de puntos:
    1. Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([video en Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md)).
    - En `Database` haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp` de la carpeta de su proyecto. Asigne al nuevo conjunto de datos el nombre “Abuja_bank_point”. Haga clic en `Save`.
    - En `Geometry type`: Seleccione `Point`.
    - Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”. Por defecto, QGIS selecciona el SRC del proyecto.
    - En `New Field` puede añadir columnas a la nueva capa. Añada la columna “Name”.
        * `Name` = “Name”
        * `Type`: Seleccione `Text (string)`.
        * Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
        * Haga clic en `OK`.
    * La nueva capa aparecerá en `Layer Panel`.


:::{admonition} Añadir más información
:class: tip

Es posible digitalizar aún más información añadiendo más columnas. Por ejemplo, puede agregar una columna en `amenity` para indicar el tipo de servicio (banco). Piense qué tipo de datos puede añadir.

:::

:::{figure} /fig/new_layer_abuja.png
---
height: 400px
name: New point layer Abuja
align: center
---
Creación de una nueva capa de puntos.
:::

4. Ahora puede crear un punto para cada uno de los tres bancos de la zona [Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#add-geometries-to-a-layer). Actualmente el nuevo “Abuja_bank_point” está vacío. Para añadir entidades podemos utilizar la `Digitizing Toolbar`. Si no puede ver la barra de herramientas `View` -> `Toolbars` y compruebe `Digitizing Toolbar` ([video de Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#creation-of-point-data)). ![](/fig/Digitizing_Toolbar.png)
    1. Seleccione la capa de puntos “Abuja_bank_point” en el panel Layer. Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png). Ahora, la capa está en modo de edición.
    2. Busque bancos en el mapa o utilice el panel de búsqueda OSMPlace. Una vez que haya encontrado uno, haga clic en ![](/fig/mActionCapturePoint.png). Haga clic izquierdo en la entidad que desea digitalizar.
    3. Una vez que haga clic, aparecerá una ventana “Abuja_bank_point”. Aquí puede añadir el nombre del banco.
    4. Repita el mismo proceso con todos los bancos que encuentre.
    5. Una vez que haya terminado la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
    6. Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

El resultado debería verse de esta manera.

:::{figure} /fig/Abuja_Banks_Point_Layers.png
---
height: 200px
name: Result Digitisation exercise
align: center
---
Las entidades digitalizadas podrían tener este aspecto.
:::

## Mapear bloqueos de carreteras

Hay información fiable de que hay un corte de carretera debido a obras en el cruce de “Independent Avenue” y “Tafawa Balewa Way”. Para visualizar esto en nuestro mapa queremos crear un polígono de este bloqueo. El polígono debe cubrir todo el cruce.

1. Para ello necesitamos de nuevo una nueva capa. En este caso, una capa de polígonos. La creación es básicamente la misma que para el punto.
    1. Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md)).
    2. En `Database`, haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp`. Asigne al nuevo conjunto de datos el nombre “Abuja_roadblock_polygon”. Haga clic en `Save`.
    3. `Geometry type`: Seleccione `Polygon`.
    4. Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”.
    5. En `New Field` puede añadir columnas a la nueva capa. Añada la columna “Roadblock_type”.
        * `Name` = “Roadblock_type”
        * `Type`: Seleccione `Text (string)`.
        * Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
        * Haga clic en `OK`.

    6. La nueva capa aparecerá en `Layer Panel`.
2. Para digitalizar esta zona, haga clic en la nueva capa “Abuja_roadblock_polygon” ([Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md)).
    - Haga clic en ![](/fig/mActionToggleEditing.png) para activar el `edit mode` y añada el objeto espacial: `Capture Polygon`![](/fig/mActionCapturePolygon.png)|.
    - Dibuje geometrías e ingrese `feature attributes`, “Roadblock_type” = “Construction_site”.
    - Guarde los cambios ![](/fig/mActionSaveEdits.png), salga `edit mode`.


## Mapear las rutas de conexión

Un hombre de negocios condujo desde el norte de Herbert Macauley Way hasta el distrito central de negocios de Abuja, para hacer una transacción en el Bank of Industry el lunes por la mañana. Por desgracia, se encontró con que el servidor de red del banco no funcionaba y tuvo que dirigirse al Zenith Bank, el único que funcionaba. Luego descubrió que había una carretera bloqueada en el cruce de la avenida Independence y el camino Tafawa Balewa debido a obras en la carretera.

Cree una capa de línea de carretera que le permita llegar fácilmente al Zenith Bank.

1. Para ello necesitamos de nuevo una nueva capa. En este caso, una capa de línea. Su proceso de creación es casi el mismo que el de punto.
    - Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md)).
    - En `Database`, haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp`. Asigne al nuevo conjunto de datos el nombre “Abuja_bank_road_connection_line”. Haga clic en `Save`.
    - `Geometry type`: Seleccione `Line`.
    - Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”.
    - En `New Field` puede añadir columnas a la nueva capa. Añada la columna “Road_type”.
        * `Name` = “Road_type”
        * Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
        * Haga clic en `OK`.
            :::{admonition} Añadir más información
            :class: tip

            De nuevo, al añadir más campos, puede añadir más información. Por ejemplo, puede añadir el tipo de carretera (pavimentada, sin pavimentar, autopista, residencial, etc.), el límite de velocidad o el número de carriles. Piense qué información podría añadir y qué `Type` utilizaría. Tenga en cuenta que no puede realizar cálculos con datos de cadena.

            :::
    * La nueva capa aparecerá en `Layer Panel`.
2. Seleccione la capa de línea “Abuja_bank_road_connection_line” para añadir datos en el panel Layer [Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md).
    1. Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png). Ahora la capa está en modo de edición.
    2.	Haga clic en ![](/fig/mActionCaptureLine.png).
    3.	Para digitalizar entidades de línea, haga clic a lo largo de la línea. Cuando haya terminado, haga clic derecho en el último punto de la línea para finalizar la entidad.
    4.	Una vez que haga clic, aparecerá una ventana “Abuja_bank_road_connection_line- Feature Attribute”. Añada el tipo de carretera “Secondary_road”.
    5.	Una vez que haya terminado la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
    6.	Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

:::{figure} /fig/Abuja_Banks_final.png
---
height: 400px
name: Abuja final
align: center
---
Los resultados podrían verse de la siguiente manera.
:::


