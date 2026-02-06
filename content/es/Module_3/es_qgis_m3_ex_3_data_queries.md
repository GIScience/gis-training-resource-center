::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

:::{grid-item-card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_module_3_exercises.html

__Haga clic aquí para volver al resumen de ejercicios del módulo 3.__
:::
::::

# Ejercicio 3: Consultas de datos

## Características del ejercicio

:::{topic}
__Objetivo del ejercicio:__
^^^
El objetivo de este ejercicio es aprender a manipular datos secundarios para generar ideas. En este ejercicio, determinaremos qué edificios se han visto afectados por una inundación y aplicaremos un filtro para determinar qué edificios forman parte de las infraestructuras críticas.
:::


### Enlaces a artículos de la Wiki

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Tipos de datos geográficos](/content/es/Wiki/es_qgis_geodata_types_wiki.md)
* [Importación de datos geográficos en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Concepto de capa](/content/es/Wiki/es_qgis_layer_concept_wiki.md)
* [Consultas no espaciales](/content/es/Wiki/es_qgis_non_spatial_queries_wiki.md)
* [Consultas espaciales](/content/es/Wiki/es_qgis_spatial_queries_wiki.md)
* [Función de tabla: agregar campo](/content/es/Wiki/es_qgis_table_functions_wiki.md)
* [Geoprocesamiento: recorte](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_geoprocessing_wiki.html#recorte)


## Datos

Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_3/Module_3_Exercise_3_Data_Queries.zip), guarde la carpeta en su computadora y descomprima el archivo. La carpeta zip incluye lo siguiente:

- `som_admbnda_adm2_ocha_20230308.shp`: Este archivo contiene información sobre el nivel administrativo somalí 0-2, el estado y los límites de las zonas operacionales de nivel 1 y 2 en forma de shapefiles. Los datos también pueden consultarse en [HDX](https://data.humdata.org/dataset/cod-ab-som).
- `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`: En este shapefile se ilustran las aguas superficiales detectadas por satélite en la ciudad de Beledweyne, distrito de Beledweyne, región de Hiraan, Somalia, el 12 de noviembre de 2023 a las 07:32 UTC. Los datos también están disponibles en [HDX](https://data.humdata.org/dataset/water-extent-in-beledweyne-city-beledweyne-district-hiraan-region-somalia-12-november-2023).
- `buildings_belet_weyne.geojson`: Este conjunto de datos se descarga con la [herramienta de exportación HOT](https://export.hotosm.org/v3/exports/new/describe) y contiene información sobre los edificios del distrito de Beledweyne.


La carpeta se llama **Module_3_Exercise_3_Data_Queries** y contiene toda la [estructura de carpetas estándar](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#estructura-de-carpetas-estandar) con todos los datos de la carpeta de entrada.

:::{Note}
La denominación de los distritos y estados no es coherente en los distintos conjuntos de datos. Encontrará diferentes grafías para el nombre del distrito **Beledweyne** en el que nos centraremos. Otras grafías podrían ser **Belet Weyne** o **Belete Weyne**. En muchos casos, tendrá que editar los valores de los conjuntos de datos para eliminar las distintas faltas de ortografía. Este proceso se denomina "limpieza de datos".
:::

## Tareas

1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#paso-a-paso-creacion-de-un-nuevo-proyecto-qgis-desde-cero) haciendo clic en `Proyecto` → `Nuevo proyecto`.

2. Una vez que se haya creado el proyecto, [guarde el proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#guarde-el-proyecto) en la **carpeta del proyecto** del ejercicio **Module_3_Exercise_1_Queries_Somalia**. Para hacer esto, haga clic en `Proyecto` → `Guardar como` e ir hasta la carpeta. Nombre el proyecto de esta manera: **Somalia_flood_affected_Beledweyne_2023**.

3. Para cargar los siguientes archivos en su proyecto, arrastre y suelte ([video en Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#abra-los-datos-vectoriales-mediante-la-funcion-arrastrar-y-soltar)). O haga clic en `Capa` → `Añadir capa` → `Añadir capa vectorial`. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta el archivo. Seleccione el archivo y hacer clic en `Abrir`. De vuelta en QGIS, haga clic en `Añadir` ([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#abrir-datos-vectoriales-mediante-la-pestana-layer)).
    - `som_admbnda_adm2_ocha_20230308.shp`
    - `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`
    - `Buildings_Belete_Weyne.geojson`: Aparecerá una ventana emergente para este archivo y tendrá que decidir qué datos importar. Seleccione los polígonos.

:::{tip}
Asegúrese de __descomprimir__ la carpeta del ejercicio antes de cargar las capas en QGIS. QGIS no acepta archivos comprimidos.
:::

### Extraiga el distrito (adm2) de la capa de límites administrativos

4. En primer lugar, queremos exportar el distrito __Beledweyne__ de la región de Hiraan desde `som_admbnda_adm2_ocha_20230308.shp` para tenerlo como capa vectorial independiente. Para hacer esto:
    1. Abra la tabla de atributos de `som_admbnda_adm2_ocha_20230308.shp` al hacer clic con el botón derecho en la capa --> `Abrir tabla de atributos`([video en Wiki](/content/es/Wiki/es_qgis_attribute_table_wiki.md)).
    2. Busque la fila de `Belet Weyne` y márquela al hacer clic en el número que está en el extremo izquierdo de la tabla de atributos. La fila se resaltará en azul y el distrito se volverá amarillo en el lienzo del mapa. Puede hacer clic con el botón derecho en la fila y hacer clic en `Acercar mapa el mapa a las filas seleccionadas`([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#acercar-el-zoom-a-una-entidad-especifica)).
    3. Ahora haga clic derecho en la capa en el Panel de Capas y luego haga clic en `Exportar` → `Guardar objetos seleccionados como`. Queremos guardar Beledweyne como GeoPackage, así que ajuste `Formato` en consecuencia. Haga clic en los tres puntos y navegue a su **carpeta temporal**. Aquí puede asignar a la capa el nombre **AOI_Beledweyne** y hacer clic en `Guardar`. Ahora haga clic en `Aceptar`([Wiki Video](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file)). En este ejercicio, no reproyectaremos las capas y trabajaremos con los datos en `ESPG:4326 - WGS84`.

### Identifique el edificio que podría verse afectado por la inundación

5. En los pasos siguientes, queremos identificar todos los edificios que puedan verse afectados por las recientes inundaciones. Para hacer esto utilizaremos la herramienta `Extraer por ubicación`.
    :::{figure} /fig/Extract_by_location_Belet_Weyne.png
    ---
    width: 500 px
    name: es_extract_by_location
    align: center
    ---
    La ventana de extracción por extracción en QGIS 3.36
    :::
    1. En la __"caja de herramientas de procesos"__ → Buscar `Extraer por ubicación`
    2. __"Extraer entidades de"__: `Buildings_Belete_Weyne.geojson`
    3. __"Donde las entidades (predicado geométrico)"__: `están dentro`
    4. __"Al comparar con las entidades de"__: `GF2_20231123_FloodExtent_BeledweyneCity_HiraanRegion.shp`
    5. En `Extraído (ubicación)` haga clic en los tres puntos ![](/fig/Three_points.png) → `Guardar a archivo` y navegue a su **carpeta temporal** y guarde la capa nueva con el nombre **Beledweyne_buildings_affected** y haga clic `Guardar`.
    6. Ahora, haga clic en `Ejecutar`.
    7. Ajusta sus capas de forma que solo vea las zonas inundadas y su nueva capa **Beledweyne_buildings_affected**. Elimine la capa `som_admbnda_adm2_ocha_20230308.shp` y `Buildings_Belete_Weyne.geojson`.

    :::{Attention}
    La herramienta [`Seleccionar por ubicación`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_queries_wiki.html#seleccionar-por-ubicacion) es muy similar. Esta herramienta funciona de la misma manera, pero en lugar de extraer directamente las entidades, las selecciona.
    :::

### Identifique las infraestructuras críticas afectadas por las inundaciones

6. En el siguiente paso, queremos identificar edificios especiales entre los edificios afectados. Abra la tabla de atributos y revise qué tipo de edificios se encuentran en la capa. Esta información se encuentra en la columna "edificio". Puede ordenar esta columna.
Para extraer "hospitales", "escuelas" y "mezquitas", podemos utilizar la herramienta `Extraer por expresión`.
    1.  Busque la herramienta `Extraer por expresión` en la __[caja de herramientas de procesos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html#caja-de-herramientas-de-procesos)__.
    2. Haga clic en `Expression`![](/fig/miconexpression.png).
    3. Se abrirá la ventana "Expresión". Aquí podemos construir una consulta muy específica. En el panel central, abra `Campos y valores`. Aquí se pueden ver todas las columnas de la capa. Haga clic en `building`. A la derecha, debería aparecer la opción `Todos únicos`. Haga clic en esta. Aquí puede ver ahora todos los valores únicos de la columna "edificio".
    4. En el campo `Expresión`, introduzca la siguiente expresión (consultar la figura siguiente):
        ```
        "building" = 'hospital' OR
        "building" = 'school' OR
        "building" = 'mosques'
        ```
    5. Haga clic en `Aceptar`. La ventana se cerrará y verá la expresión que ha creado en el campo `Expresión` de la ventana `Extraer por expresión` (véase la figura siguiente).
    6. Haga clic en `Ejecutar`. Se agregará una nueva capa temporal llamada `Objetos coincidentes` a su proyecto QGIS. Cierre la ventana `Extraer por expresión`.

:::{figure} /fig/en_extract_by_expression_som.png
---
name: es_extract_by_expression1
width: 400 px
---
La ventana de expresión en QGIS 3.36 con una expresión para extraer los polígonos con el valor "building" 'hospital', 'school', y 'mosque'.
:::


:::{figure} /fig/en_extract_by_expression_som2.png
---
name: es_extract_by_expression2
width: 400 px
---
La ventana `Extract by Expression` en QGIS 3.36
:::

:::{attention}
Una capa temporal no se guardará en su proyecto QGIS, incluso después de guardar el proyecto. Las capas temporales se marcan con un ![](/fig/icon_scratch_layer.png). Para guardar la capa de forma permanente, <kbd>Haga clic derecho</kbd> en la capa que desea hacer permanente. A continuación, seleccione la ubicación para guardar la capa nueva. Asegúrese de guardarla en la carpeta correcta (consulte [estructura de carpeta estándar](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md)).
:::


7. Explore la nueva capa abriendo la tabla de atributos, activando y desactivando la capa en el panel Capas.
8. Haga <kbd>clic derecho</kbd> en la capa `Objetos coincidentes` y guarde en su carpeta de proyecto en `/data/output/` con el nombre `Belet_Weyne_POI_affected.gpkg`.

¡Felicitaciones! La información extraída puede utilizarse ahora para realizar otros análisis o crear mapas completos de los puntos de interés afectados.

<!--ADD picture of this step-->

<!---:::{note}
This exercise has an optional part 2 in module 4, covering the visualisation of the processed data. 

You can find the exercise [here].

:::
--->