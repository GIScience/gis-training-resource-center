::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Ejercicio 2 (clasificación de datos geoespaciales): Mapa de la inseguridad alimentaria en Sierra Leona

## Características del ejercicio

:::{card}
__Objetivo del ejercicio:__
^^^

Este ejercicio pretende crear un mapa general de la distribución de la inseguridad alimentaria en Sierra Leona a nivel de distrito. Para ello, visualizaremos tanto la distribución de la inseguridad alimentaria como elementos clave de las infraestructuras, como hospitales, aeropuertos y rutas.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio:__
^^^

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Fundamentos de QGIS
- Los conocimientos que se ponen a prueba en este ejercicio son necesarios para todos los usuarios de SIG.
- Clasificación de datos geográficos

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura aproximadamente una hora, dependiendo del número de participantes y capacitadores.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki__:
^^^

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Tipos de datos geográficos](/content/es/Wiki/es_qgis_geodata_types_wiki.md)
* [Importación de datos geográficos en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Concepto de capa](/content/es/Wiki/es_qgis_layer_concept_wiki.md)
* [Tabla de atributos](/content/es/Wiki/es_qgis_attribute_table_wiki.md)
* [Función de tabla: agregar campo](/content/es/Wiki/es_qgis_table_functions_wiki.md)
* [Clasificación de datos geoespaciales: por categorías](/content/es/Wiki/es_qgis_categorized_wiki.md)
* [Clasificación de datos geoespaciales: graduado](/content/es/Wiki/es_qgis_graduated_wiki.md)
* [Digitalización: datos de punto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#creacion-de-datos-de-punto)

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


### Datos disponibles

Descargue todos los conjuntos de datos __[aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_2/Module_3_Exercise_2_Sierra_Leone_Food_Insecurity.zip)__ y guarde la carpeta en su computadora. Descomprima el archivo .zip. La carpeta descomprimida se estructura según la estructura de carpetas recomendada para los proyectos de QGIS. En “data > input” encontrará los siguientes archivos:

- `Sierra_leone_foodinsecurity_2015.shp` (Polígono) Shapefile
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra_Leone_national_borders (Líneas)
    - Sierra_Leone_provinces (Líneas)
- `Sierra_leone_roads.gpd` (Líneas) GeoPackage
- `Sierra_leone_healthsites.gpkg` (Puntos) GeoPackage
- `sl_airports.gpkg` (Puntos) GeoPackage

### Tareas

Nuestro objetivo es elaborar una visión general de la situación de la inseguridad alimentaria en Sierra Leona en 2015 junto con la visualización de los principales elementos de infraestructura. Para hacer esto, visualizaremos en un mapa las clasificaciones totales de inseguridad alimentaria junto a aeropuertos, hospitales y carreteras principales.

1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#cree-un-nuevo-proyecto-en-qgis) haciendo clic en `Proyecto` → `Nuevo proyecto`.

2. Una vez creado el proyecto, guardarlo en la carpeta “project” de “Ex_Sierra_Leone_foodinsecurity”. Para hacer esto, haga clic en `Proyecto` → `Guardar como...` y navegue hasta la carpeta. Nombre el proyecto con el nombre “Sierra_Leone_foodinsecurity”.

3. Importe los GeoPackages `Sierra_leone_borders.gpkg`, `Sierra_leone_airports`, `Sierra_leone_healthsites` y `Sierra_leone_roads.gpkg` así como el shapefile `Sierra_leone_foodinsecurity_2015.shp` a su proyecto mediante arrastrar y soltar ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#abra-los-datos-raster-mediante-arrastrar-y-soltar)).
O al hacer clic en `Capa` → `Añadir capa` → `Añadir capa vectorial`: Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta "Sierra_leone_borders.gpkg" en su explorador de archivos. Seleccione el archivo y hacer clic en `Abrir`. De vuelta en QGIS, haga clic en `Añadir` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#abrir-datos-raster-mediante-la-pestana-layer)).

:::{Attention}
Los GeoPackage pueden contener varios archivos e incluso proyectos QGIS completos. Cuando cargue un archivo de este tipo en QGIS aparecerá una ventana en la que deberá seleccionar los archivos que desea cargar en su proyecto de QGIS.
:::

4. En primer lugar, vamos a añadir un mapa base al lienzo del mapa utilizando el complemento `QuickMapServices` haciendo clic en el símbolo ![](/fig/QMS_search_icon.png) de la barra de herramientas del proyecto. Busque “Bing Maps Satellite Imagery” en el panel de QMS y agregue la capa del mapa base haciendo doble clic. Para obtener una vista optimizada [ajuste la opacidad](https://www.youtube.com/watch?v=WguUkN1YRzY&ab_channel=GISBigfootAnswers) de sus capas para optimizar el uso del mapa base.

5. Utilizando la tabla de atributos de la capa de aeropuertos, haga zoom hasta el aeropuerto de Tongo haciendo clic derecho en la fila de la tabla de atributos y seleccionando `Zoom a la selección`([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#acercar-el-zoom-a-una-entidad-especifica)). Revise el mapa base. ¿Cree que la pista de aterrizaje sigue en funcionamiento? La respuesta es no, según Wikipedia. Eliminar el aeropuerto Tongo en la [tabla de atributos](/content/es/Wiki/es_qgis_attribute_table_wiki.md). Eliminar también el aeropuerto de Kabala, que ya no funciona.

6. Ahora queremos comprobar los aeropuertos de las ciudades de Bo y Kenema. ¿Están estas pistas de aterrizaje en mejor estado? En caso afirmativo, agregarlos a la capa del aeropuerto. Para encontrar estas ciudades en la interfaz de su mapa, utilice el complemento de QGIS `OSM Place Search`.
Para agregar el complemento `OSM Place Search`, haga clic en `Complementos` → `Administrar e instalar complementos` → `Todos` y busque “OSM Place Search”. Una vez que lo haya encontrado, haga clic en este y seleccionar `Instalar complementos`. Puede abrir `OSM Place Search Panel` como cualquier otro panel, haciendo clic en `Ver` → `Paneles` y marcando `OSM Place Search Panel`([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_plugins_wiki.html)).
    * En el panel, puede buscar lugares en OpenStreetMap escribiendo el nombre en la barra de búsqueda. A menudo tiene sentido añadir información adicional, como el nombre del país. Pruebe, por ejemplo, con "Bo, Sierra Leona".

:::{figure} /fig/mod3_classification_ex_OSMsearch.png
---
width: 400px
align: center
name: es_mod3_classification_ex_OSMsearch
---
Búsqueda de lugares OSM.
:::

Agregue los aeropuertos de Bo y Kenema como puntos a la capa `Sierra_Leone_airports`. Encuentre ayuda sobre cómo agregar entidades a una capa de puntos [aquí](/content/es/Wiki/es_qgis_digitisation_wiki.md).


8. *Opcional:* En la tabla de atributos, cree una nueva columna `Runway_length` y agregue la longitud de las pistas de Bo y Kenema al medirlas aproximadamente con la herramienta de medición ![](/fig/measuring_tool_icon.png).

9. Ahora debemos crear una visualización intuitiva de las diferencias en inseguridad alimentaria. Para ello utilizamos la opción de visualización "[Clasificación graduada](/content/es/Wiki/es_qgis_graduated_wiki.md)" para la capa `Sierra_leone_foodinsecurity_2015` mostrando los polígonos según las clases creadas a partir de la columna "Total_FI" de la tabla de atributos.
    * Haga clic derecho en la capa `Sierra_leone_foodinsecurity_2015.shp` en el panel de capas -> `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas verticales a la izquierda. Vaya a la pestaña `Simbología`.
    * En el menú desplegable superior, seleccione `Graduado`. En `Valor` seleccionar “Total_FI”.
    * Más abajo, haga clic en `Clasificar`. Ahora debería ver varias clases basadas en el intervalo de valores de la columna “TotalFI” representadas con distintos colores. Puede ajustar los colores al eligir diferentes paletas de colores en el menú desplegable `rampa de color`. Además, puede modificar la distribución de valores de las clases seleccionando diferentes modos de clasificación ([Wiki](/content/es/Wiki/es_qgis_graduated_wiki.md)) en el menú desplegable `Modo`.
    * Juegue con estas opciones para conseguir una combinación de colores que se adapte a los datos. Una vez que haya terminado, haga clic en `Aplicar` y `Aceptar` para cerrar la ventana de simbología.

:::{figure} /fig/mod3_classification_ex_Graduatedclassification.png
---
width: 900px
name: es_basic classification
align: center
---
Clasificación de la inseguridad alimentaria en Sierra Leona.
:::

1. Para dar a los hospitales y aeropuertos una visualización más distintiva, abra de nuevo la pestaña `Symbology` para las capas respectivas y elegir “Topología” en el menú desplegable situado encima del panel superior del panel inferior. Busque el símbolo del aeropuerto/hospital y selecciónelo al hacer clic en este. Una vez más, aplique los cambios al hacer clic en `Aplicar` y `Aceptar`.

:::{figure} /fig/mod3_classification_ex_Topology.png
---
width: 900px
name: es_basic classification
align: center
---
Símbolo de hospital.
:::

11. Como último paso de visualización, abra la pestaña `Simbología`, `Sierra_Leone_roads (Lines)` y, al igual que en el paso 9, abra el menú desplegable superior. Ahora, en lugar de `Graduado`, elija [Clasificación por categorías](/content/es/Wiki/es_qgis_categorized_wiki.md) y seleccione "autopista" en el menú `Valor`. Haga clic en `Clasificar` para obtener una clasificación con colores individuales para todos los valores únicos de la columna "carretera". En las casillas situadas junto a las clases, deseleccione todas las clases excepto “primaria”. Puede cambiar el color de las clases al hacer clic manualmente y ajuste el color en el menú desplegable "Símbolo" que está en la parte superior de la ventana.

:::{figure} /fig/mod3_classification_ex_Categorizedclassification.png
---
width: 900px
name: es_basic classification
align: center
---
autopistas por categorías de Sierra Leona.
:::

12. Coloque todas las capas que se han cargado en su proyecto en visibles y dispóngalas en un orden adecuado para una buena visualización de la inseguridad alimentaria, así como de los elementos de infraestructura. Elija un mapa base que le parezca adecuado. El resultado final podría ser el siguiente:

:::{figure} /fig/mod3_classification_ex_Result.png
---
width: 900px
name: es_basic classification
align: center
---
Ejemplo del resultado de este ejercicio.
:::

El orden de las capas aquí de arriba a abajo es:
- `Sierra_Leone_health`
- `Sierra_Leone_airports`
- `Sierra_Leone_roads`
- `Sierra_Leone_national_borders`
- `Sierra_leone_foodinsecurity_2015`
- Mapa base: `OpenStreetMap`

:::{figure} /fig/mod3_classification_ex_LayerOrder.png
---
width: 600px
name: basic classification
align: center
---
Orden de capas.
:::
