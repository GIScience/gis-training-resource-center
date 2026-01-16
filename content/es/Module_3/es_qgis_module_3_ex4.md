::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Ejercicio 4: Inundaciones en Nigeria

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Objetivo del ejercicio__
^^^

En este ejercicio, aprenderá a digitalizar las posiciones de los asentamientos al crear nuevos conjuntos de datos. Además, aprenderá a enriquecer el conjunto de datos geoespaciales simples con información adicional.

__Tipo de ejercicio de capacitación__

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Los conocimientos que se ponen a prueba en este ejercicio son necesarios para todos los usuarios de SIG.

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
^^^

- El ejercicio dura aproximadamente una hora, dependiendo del número de participantes y capacitadores.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki__:
^^^

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Tipos de datos geoespaciales](/content/es/Wiki/es_qgis_geodata_types_wiki.md)
* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Concepto de capa](/content/es/Wiki/es_qgis_layer_concept_wiki.md)
* [Tabla de atributos](/content/es/Wiki/es_qgis_attribute_table_wiki.md)
* [Función de tabla: agregar campo](/content/es/Wiki/es_qgis_table_functions_wiki.md)
* [Clasificación de datos geoespaciales: por categorías](/content/es/Wiki/es_qgis_categorized_wiki.md)
* [Clasificación de datos geoespaciales: graduado](/content/es/Wiki/es_qgis_graduated_wiki.md)
* [Digitalización: datos de punto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#agregar-geometrias-a-una-capa)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra en Miro) en la que los participantes puedan agregar sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener consejos generales sobre cómo impartirlas.

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

## Fuentes de datos

Descargue la carpeta de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_1/Module_3_Exercise_1_Flood_Nigeria.zip) y guárdela en su PC. Descomprima el archivo .zip.
La carpeta se llama “Module_3_Exercise_1_Flood_Nigeria” y contiene toda la [estructura de carpetas estándar](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#standard-folder-structure) con todos los datos en la carpeta de entrada y la documentación adicional en la carpeta de documentación.

* [Nigeria: División administrativa con población agregada (“kontur_boundaries_NG_20230628.gpkg”)](https://data.humdata.org/dataset/kontur-boundaries-nigeria)-Kontor
* [Nigeria: Datos de inundaciones (“Nigeria_flood_2022_affacted_population”)](https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas)- UN OCHA. Este conjunto de datos se manipuló con fines de formación.
* [Extensiones de agua detectadas por satélite entre el 1 y el 25 de octubre de 2022 sobre Nigeria (VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp)](https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria?force_layout=desktop) UNOSAT


## Tareas

Nuestro objetivo es elaborar una visión general del impacto de las inundaciones de 2022 en el estado de Burco, en Nigeria. Para ello, visualizaremos el estado y los distritos afectados, además de digitalizar las comunidades supuestamente afectadas.

1. Abra QGIS y cree un [nuevo proyecto](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#cree-un-nuevo-proyecto-en-qgis) haciendo clic en `Proyecto` → `Nuevo Proyecto`

2. Una vez creado el proyecto [guarde el proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#cree-un-nuevo-proyecto-en-qgis) en la carpeta “project” del ejercicio “Modul3_Exercise_1_Flood_Nigeria”. Para hacer esto, haga clic en `Projecto` → `Guardar Como` y navegue hasta la carpeta. Nombre al proyecto de la siguiente manera: “Nigeria_Borno_flood_2022”.

3. Cargue el GeoPackage "kontur_boundaries_NG_20230628.gpkg" en su proyecto mediante arrastrar y soltar ([Wiki Video](/content/es/Wiki/es_qgis_import_geodata_wiki.md#abra-los-datos-ráster-mediante-arrastrar-y-soltar)). O haga clic en `Capa` -> `Añadir Capa`-> `Añadir capa vectorial`. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta “kontur_boundaries_NG_20230628.gpkg”. Seleccione el archivo y hacer clic en `Abrir`. De vuelta en QGIS, haga clic en `Añadir` ([Wiki Video](/content/es/Wiki/es_qgis_import_geodata_wiki.md#abrir-datos-vectoriales-mediante-la-pestaña-layer)).
Este conjunto de datos contiene todas las áreas de división administrativa (admin 0 a 5) con la población respectiva de las áreas.

:::{Attention}
Los archivos GeoPackage pueden contener varios archivos e incluso proyectos QGIS completos. Cuando cargue un archivo de este tipo en QGIS aparecerá una ventana en la que deberá seleccionar los archivos que desea cargar en su proyecto de QGIS.
:::

4. En primer lugar, queremos exportar el estado de Borno desde kontur_boundaries_NG_20230628 para tenerlo como capa vectorial independiente. Para hacer esto,
    * Abra la tabla de atributos de "kontur_boundaries_NG_20230628" al hacer clic derecho en la capa → `Abrir tabla de atributos`([Wiki Video](/content/es/Wiki/es_qgis_attribute_table_wiki.md)).
    * Busque la fila del estado de Borno y márquela al hacer clic en el número que aparece en el extremo izquierdo de la tabla de atributos. La fila aparecerá en azul y la zona del estado de Borno se volverá amarilla en el lienzo del mapa. Puede hacer clic con el botón derecho en la fila y hacer clic en `Acercar el mapa a las filas seleccionadas`([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#acercar-el-zoom-a-una-entidad-especifica)).
    * Ahora haga clic derecho en la capa en el Panel de Capas y luego haga clic en `Exportar` → `Guardar objetos seleccionados como`. Debemos guardar Borno como GeoPackage, así que ajuste `Formato` de manera correspondiente. Haga clic en los tres puntos y navegue hasta su carpeta `temp`. Aquí puede darle el nombre a la capa “AOI_Borno_admin1” y hacer clic en `Guardar`. Ahora debería ver el mismo nombre en el campo `Layer name`. Haga clic en `Aceptar` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_non_spatial_queries_wiki.html#guardar-las-entidades-seleccionadas-como-un-archivo-nuevo)).

5. En los siguientes pasos, debemos crear una capa vectorial con áreas admin 2 o en Nigeria llamadas Local Government Areas (LGA) con la población en nuestro proyecto.
Como solo necesitamos las LGA, tenemos que exportarlas del conjunto de datos original.
    * Abra la tabla de atributos de la capa "kontur_boundaries_NG_20230628" al hacer clic derecho en la capa → `Tabla de atributos` ([video en Wiki](/content/es/Wiki/es_qgis_attribute_table_wiki.md)). Consulte la tabla de atributos. Se verán dos columnas de niveles de administrador “admin levels” y “[osm_admin_levels](https://wiki.openstreetmap.org/wiki/Key:admin_level)”. Ambos tienen valores diferentes. En los [metadatos](https://data.humdata.org/dataset/kontur-boundaries-nigeria) del conjunto de datos en HDX, podemos ver que la columna "osm_admin_levels" se refiere a los niveles de administración utilizados en OpenStreetMaps (OSM). Hay una [lista](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#10_admin_level_values_for_specific_countries) de qué niveles de administración oficiales corresponden a qué niveles de administración OSM. Las LGA corresponden a osm admin __nivel 6__. Esto significa que debemos exportar todas las entidades con `osm_admin_level` = `6`.
    * Para exportar exactamente estas entidades utilizaremos la herramienta `Extraer por atributo`. Abra la página `Caja de herramientas de Procesos` ([así se hace](/content/es/Wiki/es_qgis_interface_wiki.md#barras-de-herramientas)) y busque la herramienta.
        Abra la herramienta y elija como `Capa de entrada` la capa "kontur_boundaries_NG_20230628.gpkg". En `Atributo de seleccíon` elija la columna `osm_admin_level`. El `Operador` tiene que ser `=` y como `valor` utilizamos `6` ya que los LGA tienen el osm_admin_level 6.
    * En `Extraído (atributo)`, haga clic en los tres puntos → `Guardar en GeoPackage`, navegue hasta su carpeta `temp`, y dele nombre a la nueva capa "Nigeria_admin2_pop". Haga clic en `Guardar`. Nombre la capa con el mismo nombre ("Nigeria_admin2_pop"). Haga clic en `Aceptar` y luego en `Ejecutar`.

6. Ahora tenemos que extraer todas las LGA de Borno. Para hacer esto, utilizaremos la herramienta `Extraer por ubicacion` ([Wiki Video](/content/es/Wiki/es_qgis_non_spatial_queries_wiki.md#seleccionar-por-expresión)). Busque la herramienta en `Caja de herramientas de Procesos` y ábrala.
    * En `Capa de entrada` utilizaremos “Nigeria_admin2_pop”.
    * Para `Comparando con los objetos de` utilizamos la capa “AOI_Borno_admin1”.
    * Como `Donde los objetos (predicado geométrico)` utilizamos `están dentro`.
    * Para guardar el resultado, haga clic en los tres puntos de `Extraído (localización)` → `Guardar en GeoPackage` y vaya a la carpeta `temp`. Guarde la nueva capa con el nombre “Borno_admin2_pop”. Dé a la nueva capa el mismo `Layer name` y haga clic en `Ejecutar`.
    * Abra la tabla de atributos de la nueva capa. Debería haber 27 entidades.

:::{figure} /fig/en_qgis_extract_by_location_nigeria_flood.png
---
width: 400px
name: m3ex4_extract_by_location
align: center
---
:::

7. Ya tenemos nuestras áreas de administración y ahora podemos empezar a enriquecer estas capas con datos adicionales relacionados con la inundación de 2022.
Abra el archivo de Excel o PDF “Nigeria_flood_2022_affacted_population” y abra la hoja Borno. Encontrará una tabla con las LGA y las comunidades que se vieron afectadas por la inundación. Ahora queremos añadir parte de la información a nuestra capa "Borno_admin2_pop". Para hacer esto, hay dos modos. Uno sencillo, pero más lento, y otro más complicado, pero mucho más rápido. Vamos a mostrar el modo fácil, pero en el menú desplegable de abajo puede encontrar el tutorial para el modo avanzado también.
    * Abra la tabla de atributos de "Borno_admin2_pop" y active el modo de edición al hacer clic en ![](/fig/mActionToggleEditing.png) ([Wiki Video](/content/es/Wiki/es_qgis_attribute_table_wiki.md#tabla-de-atributos---edición-de-datos)). Ahora puede editar los datos directamente en la tabla.
    * En primer lugar, debemos agregar una nueva columna con el nombre “Flood_afffected”. Para hacer esto, haga clic en ![](/fig/mActionNewAttribute.png). En la ventana `Añadir campo`, tiene que agregar el nombre y establecer el `Tipo` a `Texto (cadena)`. Haga clic en `Aceptar` ([Wiki Video](/content/es/Wiki/es_qgis_attribute_table_wiki.md#add-new-column)).
    * En el siguiente paso, revise en la tabla Excel/PDF qué LGA se han visto afectadas y seleccione “Sí” en la tabla de atributos para esas LGA.
    * Cuando haya terminado, haga clic en ![](/fig/mActionSaveEdits.png) para guardar sus ediciones y desactive el modo de edición haciendo clic de nuevo en ![](/fig/mActionToggleEditing.png)([Wiki Video](/content/es/Wiki/es_qgis_attribute_table_wiki.md#modificar-datos-en-la-tabla-de-atributos)).

8. Para visualizar el conjunto de datos enriquecidos, utilizamos la función "Clasificación por categorías". Esto significa que seleccionamos una columna de la tabla de atributos y utilizamos el contenido como categorías para ordenar y mostrar los datos ([Wiki Video](/content/es/Wiki/es_qgis_categorized_wiki.md)).
    * Haga clic derecho en la capa "Borno_admin2_pop" en `panel de capas` -> `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Simbología`.
    * En la parte superior encontrará un menú desplegable. Ábralo y elija `Categorizado`. En `Valor` seleccione “Flood_affected”.
    * Más abajo, haga clic en `Clasificar`.  Ahora debería ver todos los valores únicos o atributos de la columna “Flood_affected” seleccionada. Puede ajustar los colores al hacer doble clic en una fila del campo central. Una vez que haya terminado, haga clic en `Aplicar` y `Aceptar` para cerrar la ventana de simbología.

:::{figure} /fig/en_qgis_categorized_classification_nigeria_flood_exercise.png
---
width: 600px
name: m3ex4_classification
align: center
---
:::

9. A continuación, debemos visualizar las comunidades afectadas que se indican en la tabla Nigeria_flood_2022_affected_population. Para encontrar estas comunidades en QGIS, necesitamos dos cosas. Un mapa base de OpenStreetMap y el complemento `OSM Place Search`.
    * Para añadir el OSM como mapa base, haga clic en `Capa` -> `Añadir capa` -> `Añadir capa SYZ...`. Elija `OpenStreetMap` y haga clic en `Añadir`.
        Organice su capa en `panel de capas` de forma que el OSM esté en la parte inferior ([Wiki Video](/content/es/Wiki/es_qgis_basemaps_wiki.md)).
    :::{Tip}
        No se puede interactuar con un mapa base.
    :::
    * Para añadir el complemento `OSM Place Search`, haga clic en `Complementos` -> `Administrar e instalar complementos` -> `Todos` y busque `OSM Place Search`. Una vez que lo haya encontrado, haga clic sobre él y luego en `Instalar complemento`. Puede abrir `OSM Place Search Panel` como cualquier otro panel, haciendo clic en `Ver` -> `Paneles` y marcando `OSM Place Search Panel`([video en Wiki](/content/es/Wiki/es_qgis_plugins_wiki.md#instalación-de-complementos)).
    * En el panel, puede buscar lugares en OpenStreetMap escribiendo el nombre del lugar en la barra de búsqueda. A menudo tiene sentido añadir información adicional, como el nombre del país. Por ejemplo, pruebe con "Laujeri Bulama, Nigeria".

10. Ahora ya tenemos todas nuestras herramientas. En el siguiente paso, creamos una nueva capa de vectores de puntos desde cero para digitalizar la ubicación de las comunidades afectadas.
    * Haga clic en `Capa` --> `Crear capa` -> `Nueva capa GeoPackage`([video en Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#crear-una-nueva-capa))
    - En `Base de datos`, haga clic en ![](/fig/Three_points.png) y vaya a la carpeta `temp`. Asigne al nuevo conjunto de datos el nombre “Borno_affected_communities_point”. Haga clic en `Guardar`.
    * `Tipo de geometría`: Seleccione `Punto`
    - Seleccione el sistema de referencia de coordenadas (SRC) “EPSG:4326-WGS 84”. Por defecto, QGIS selecciona el SRC del proyecto.
    - En `Nuevo campo` puede añadir columnas a la nueva capa. Añada la columna “Name”.
        * `Nombre` = “Name”
        * `Tipo`: Seleccione `Texto (cadena)`
        * Haga clic en `Añadir a la lista de campos` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Lista de campos`.
        * Haga clic en `Aceptar`.
    * La nueva capa aparecerá en `panel de capas`

:::{figure} /fig/en_qgis_create_point_layer_nigeria_flood_exercise.png
---
width: 400px
name: m3ex4_create_point_layer
align: center
---
:::

11. Actualmente el nuevo “Borno_affected_communities_point” está vacío. Para añadir entidades podemos utilizar la `Digitizing Toolbar`. Si no puede ver la barra de herramientas, utilice `Ver` -> `Barras de herramientas` y compruebe la barra de herramientas `digitalización` ([video en Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#creación-de-datos-de-punto)). ![](/fig/Digitizing_Toolbar.png)
    * Seleccione la capa de puntos “Borno_affected_communities_point” en el panel de capas. Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png). Ahora la capa está en el modo de edición.
    * Buscar una comunidad afectada según la tabla “Nigeria_flood_2022_affacted_population”. Una vez que haya encontrado uno, haga clic en ![](/fig/mActionCapturePoint.png). Haga clic izquierdo en la entidad que desea digitalizar.
    * Al hacer clic, aparecerá una ventana `Borno_affected_communities_point Feature Attribute`. Aquí puede añadir el nombre de la ubicación.
    * Repita el mismo proceso para tantas comunidades como quiera.
    * Cuando haya terminado de digitalizar, haga clic en ![](/fig/mActionSaveEdits.png) para guardar sus modificaciones.
    * Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

12. En este paso, queremos añadir al mapa información sobre la población. Esto nos ayudará a visualizar dónde hay más personas potencialmente afectadas.
Dado que la capa "Borno_admin2_pop" contiene esta información, podemos publicar esta capa.
    * Para hacer esto, haga clic derecho en la capa -> `Duplicar capa`. El nombre de la nueva capa será "Borno_admin2_pop_copy".

13. Dado que los números absolutos de población son números naturales, no podemos utilizar la clasificación por categorías. En su lugar, utilizamos la opción `Graduado` ([video en Wiki](/content/es/Wiki/es_qgis_graduated_wiki.md)).
    * Haga clic derecho en la capa "Borno_admin2_pop_copy" en `Panel de capas` -> `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Simbología`.
    * En la parte superior hay un menú desplegable. Ábralo y elija `Graduado`.
    * En `Valor` seleccionar "Population".
    * `Rampa de color`: Seleccionar una rampa de color de blanco a verde. Como queremos visualizar la población, es importante utilizar colores neutros.
    * `Modo`: Conteo igual (cuantil)
    * `Clases`: 5
    * Haga clic en `Clasificar`
    * Haga clic en `Aplicar`

:::{figure} /fig/en_qgis_graduated_classification_nigeria_flood_exercise.png
---
width: 600px
name: es_m3ex4_graduated_classif
align: center
---
:::

14. QGIS creó ahora cinco clases que cubren toda la gama de cifras de población del estado de Borno. Haga clic en la `Histograma` pestaña -> `Cargar valores`. Aquí puede ver la distribución de los valores en el conjunto de datos y los límites de las clases. Vemos que la mayoría de las LGA tienen una población inferior a 300 habitantes. Pruebe otros modos de clasificación, como los cortes naturales o los intervalos equitativos.

:::{figure} /fig/en_qgis_graduated_classification_Histogram_nigeria_flood_exercise.png
---
width: 400px
name: es_m3ex4_histogram
align: center
---
:::

15. Para visualizar “Borno_admin2_pop” (que muestra las LGA afectadas) y “Borno_admin2_pop_copy” (que muestra los datos de población) juntos, tenemos que cambiar la simbología de “Borno_admin2_pop”.
En primer lugar, haga clic derecho en la capa “Borno_admin2_pop” en `Pandel de capas` -> `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Simbología`.
Actualmente, utilizamos la clasificación `Categorizado`. Debemos mantenerlo. Sin embargo, solo queremos mostrar las LGA afectadas. Por lo tanto, desmarcamos la fila que corresponde a las LGA sin `Affected` = `Yes`.
    * Haga clic derecho en la capa "Borno_admin2_pop" en `Panel de capas` -> `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Simbología`.
    * A continuación, haga doble clic en la fila `Yes`. Aquí tenemos dos opciones. Podemos utilizar una cuadrícula o solo los bordes.
    * Para utilizar una cuadrícula, desplácese hacia abajo y seleccione la que más le convenga. A continuación, haga clic en `Aceptar`.

:::{figure} /fig/en_qgis_grid_flood_exercise.png
---
width: 600px
align: center
---
:::

* Para utilizar solo los bordes, hacer clic en `Relleno simple` -> `Estilo de relleno` y seleccionar `Sin relleno`. Ajuste el `Color de marca` a rojo o a otro color brillante. Aumente la `Anchura de marca` para agrandar los bordes. A continuación, haga clic en `Aceptar`.

:::{figure} /fig/en_qgis_now_brush_nigeria_flood_exercise.png
---
width: 400px
align: center
---
:::

16. Para tener una idea más detallada de la extensión de la inundación podemos cargar la capa “VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp” que muestra la extensión máxima de agua superficial entre el 9 y el 30 de octubre de 2022. Si lo desea también puede cargar “VIIRS_20220901_20220930_PermanentWater_Nigeria.shp”. En esta capa se muestran las entidades de lagos y otras aguas superficiales permanentes.
Una vez cargadas las capas en QGIS, podrá comprobar si se muestran correctamente. Sin embargo, al comprobar la información de las capas, puede ver que las nuevas capas tienen un Sistema de Referencia de Coordenadas (SRC) diferente. Tienen el código EPSG 9707, mientras que nuestro proyecto tiene el 4326 ([video en Wiki](/content/es/Wiki/es_qgis_projections_wiki.md#cómo-hacer-para-verificar-y-modificar-el-código-epsgsrc-de-su-proyecto-de-qgis)).
    * Haga clic derecho en la capa de datos y hacer clic en “Propiedades”.
    * Se abrirá la ventana “Propiedades de capa” de la capa de datos. Haga clic en “Información”.
    * En el título “Sistema de referencia de coordenadas” encontrará toda la información sobre el SRC. Los más importantes son:
    - __Nombre:__ Aquí encontrará el código EPSG
    - __Unidades:__ Aquí puede averiguar si es posible utilizar metros con esta capa de datos o latitud y longitud.

17. Esto se convertirá en un problema tan pronto como hagamos algo diferente de solo mostrar las capas. Puesto que debemos manipular las capas en el siguiente paso, necesitamos reproyectarlas primero ([video en Wiki](/content/es/Wiki/es_qgis_projections_wiki.md#modificación-de-la-proyección-cartográfica-de-una-capa-vector)).
    * Haga clic en la pestaña `Vectorial` -> `Data Management Tools` -> `Reprojectar capa` o buscar la herramienta en [`Caja de herramientas de Procesos`]().
    * Como `Capa de entrada` seleccione “VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp”
    * Seleccione como destino CRS/EPSG-Code __4326__.
    * Guarde el nuevo archivo en su carpeta `temp` haciendo clic en los tres puntos ![](/fig/Three_points.png) junto a `Reproyectado`, especifique el nombre del archivo como “Flood_extand_Nigeria_october_2022_reprojected”.
    * Haga clic en `Ejecutar`
    * Elimine la capa antigua del panel de capas al hacer clic derecho en la capa -> `Eliminar capa`.

18. La capa de extensión de la inundación cubre la totalidad de Nigeria. Podemos utilizar la herramienta `Cortar (Superposición vectorial)` para cortarlo con la forma del estado de Borno ([video en Wiki](/content/es/Wiki/es_qgis_geoprocessing_wiki.md#clip)).
    * Abra `Caja de herramientas de Procesos` ([así se hace](/content/es/Wiki/es_qgis_interface_wiki.md#barras-de-herramientas)) y buscar la herramienta `Cortar (Superposición vectorial)`.
    :::{Note}
    Hay __dos__ versiones de la herramienta `Cortar`. Dado que trabajamos con datos vectoriales, asegúrese de utilizar el que se encuentra en "Superposición vectorial".
    :::
    * `Capa de entrada`: "VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp”
    * `Capa de superposición`: “AOI_Borno_admin1”
    * Para guardar el resultado, haga clic en los tres puntos de `Cortado`-> `Guardar en GeoPackage` e ir a su carpeta `temp`. Guardar la capa nueva con el nombre “Flood_extend_october_2022_reprojected_Borno”. Dé a la nueva capa el mismo `Nombre de la capa` y haga clic en `Ejecutar`.

:::{figure} /fig/en_qgis_clip_flood_exercise.png
---
width: 400px
align: center
---
:::

Genial, ya hemos hecho nuestra visualización. ¡BIEN HECHO!
Los resultados deberían parecerse a los de la imagen siguiente.

:::{figure} /fig/en_qgis_result_flood_exercise.png
---
width: 600px
align: center
---
:::










