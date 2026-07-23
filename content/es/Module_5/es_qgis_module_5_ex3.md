::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 3: Mapa de activación e intervenciones para acciones anticipatorias


## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Objetivo del ejercicio:__
^^^

Este ejercicio toma como referencia el proceso de supervisión y activación utilizado por la Sociedad de la Media Luna Roja Somalí (SRCS, por sus siglas en inglés) en el marco de un Protocolo de Acción Temprana contra la sequía.

En este ejercicio, usted construirá una versión simplificada del mecanismo de supervisión y activación para el pilar de proyección de FEWSNET.

__Tipo de ejercicio de capacitación:__

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para:__
^^^


:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^



:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Intersección](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Estadísticas zonales](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_raster_basic_wiki.html)
* [Unir atributos por ubicación (resumen](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Funciones de la tabla](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#attribute-table-data-editing)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese su tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser una pizarra blanca física, un rotafolio o una pizarra digital (por ejemplo, una pizarra Miro) donde los participantes puedan añadir sus conclusiones y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener consejos generales sobre cómo impartir una capacitación.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes hayan descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre cada paso y explíquelo al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y aplicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su propio proyecto de QGIS.

__Cierre de la sesión:__

- Dedique tiempo al final del ejercicio a cualquier problema o pregunta relacionada con las tareas que pueda surgir.
- Reserve algo de tiempo para preguntas abiertas.

:::



## Antecedentes

Establecer los desencadenantes es uno de los pilares fundamentales del sistema de __Financiamiento Basado en Pronósticos (FbF, por sus siglas en inglés)__. Para que una Sociedad Nacional tenga acceso a fondos liberados automáticamente para sus acciones anticipatorias, su Protocolo de Acción Anticipatoria debe definir claramente dónde y cuándo se asignarán los fondos y se prestará la asistencia. En el FbF, esto se decide según valores umbrales específicos, los llamados __desencadenantes__, basados en pronósticos meteorológicos y climáticos, los cuales se definen para cada región (ver [Manual de FbF](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

Para el desarrollo del mecanismo de activación de la sequía de Somalilandia-Somalia, se analizaron a fondo diversas fuentes de datos.
Finalmente, los principales parámetros elegidos para la activación basada en la __evaluación del impacto histórico__ son el índice estandarizado de precipitación de doce meses (SPI12) y la clasificación de inseguridad alimentaria aguda de la IPC. Los datos exactos utilizados son los SPI12 documentados y previstos (fuente: ICPAC) y la clasificación IPC prevista (previsión a 8 meses, fuente: FEWSNET), que se utiliza para calcular un índice de inseguridad alimentaria ponderado por la población. Los umbrales de activación de ambos componentes se optimizaron buscando la proporción más favorable de tasa de aciertos y tasa de falsas alarmas. Los umbrales emergentes fueron <-1 para el SPI12 y >=0,7 para el índice basado en la IPC. La activación se realiza por distrito y solo es posible una activación al año.

:::{admonition} Declaración de activación
Cuando el ICPAC emite una previsión SPI-12 inferior a -1 para un distrito Y la proyección actual de inseguridad alimentaria FEWSNET alcanza al menos 0,7 en su
índice ponderado de población derivado en el mismo distrito, entonces actuaremos en este distrito. Esperamos que el plazo de entrega sea de 90 días.
:::


## Datos disponibles

### Datos sobre la proyección cartográfica de la inseguridad alimentaria

El mecanismo de activación de la sequía se basa en dos conjuntos de datos de vigilancia de variables. Uno de ellos es la proyección cartográfica de inseguridad alimentaria elaborada por FEWSNET, que se actualiza mensualmente.

| Conjunto de datos | Fuente | Descripción |
| ------- | ------ | ----------- |
| Proyecciones cartográficas de la IPC | [FEWSNET](https://fews.net/) | escala de cinco fases que proporciona normas comunes para clasificar la gravedad de la inseguridad alimentaria aguda o prevista. |

#### ¿Qué son los datos de proyección de seguridad alimentaria de la IPC?

La IPC es una medida y clasificación comúnmente aceptada para describir la gravedad actual y prevista de la inseguridad alimentaria aguda.
La clasificación se basa en una convergencia de datos y pruebas disponibles, incluidos indicadores relacionados con el consumo de alimentos, los medios de subsistencia, la malnutrición y la mortalidad. La inseguridad alimentaria es uno de los impactos prioritarios de las sequías en Somalia, por lo que también se utiliza como mecanismo de activación, en un índice ponderado por la población.

Tres veces al año (febrero, junio y octubre) FEWSNET estima las clases de IPC más probables para los próximos 8 meses (proyección a corto y medio plazo), disponibles desde 2019 hasta la actualidad. La proyección a corto plazo se denomina ML1 y es una proyección para los próximos 4 meses, la proyección a medio plazo se denomina ML2 y proyecta las clases IPC para los 4 meses siguientes. Para la activación se tendrán en cuenta las proyecciones ML1 (a corto plazo) y ML2 (a medio plazo).

Las actualizaciones de Outlook se producen casi todos los meses y también se tienen en cuenta.

| Color | Fase | Descripciones |
| ----- | --- | --- |
| ![](/fig/IPC_Class_1.drawio.svg) | 1. Mínima | Los hogares son capaces de satisfacer las necesidades alimentarias y no alimentarias esenciales sin recurrir a estrategias atípicas e insostenibles para acceder a los alimentos y los ingresos. |
| ![](/fig/IPC_Class_2.drawio.svg) | 2. Estrés | Los hogares tienen un consumo de alimentos mínimamente adecuado, pero no pueden hacer frente a algunos gastos no alimentarios esenciales sin recurrir a estrategias de afrontamiento por estrés. |
| ![](/fig/IPC_Class_3.drawio.svg) | 3. Crisis | Los hogares tienen carencias en el consumo de alimentos que se reflejan en una malnutrición aguda elevada o superior a la habitual __O__ apenas son capaces de satisfacer las necesidades alimentarias mínimas, pero solo pueden hacerlo agotando activos esenciales para su subsistencia o mediante estrategias para hacer frente a la crisis. |
| ![](/fig/IPC_Class_4.drawio.svg) | 4. Emergencia | Los hogares tienen grandes carencias de consumo alimentario que se reflejan en una malnutrición aguda y una tasa de mortalidad muy elevada; __O__ son capaces de mitigar las grandes carencias de consumo alimentario, pero solo empleando estrategias de subsistencia de emergencia y liquidación de activos. |
| ![](/fig/IPC_Class_5.drawio.svg) | 5. Hambruna | Los hogares presentan una falta extrema de alimentos y/o de otras necesidades básicas, incluso después de haber empleado por completo todas las estrategias de afrontamiento. El hambre, la muerte, la indigencia y los niveles de desnutrición aguda extremadamente críticos son evidentes. (Para la clasificación de hambruna, la zona debe tener niveles críticos extremos de desnutrición aguda y mortalidad). |

### Datos de capacitación

Descargue la carpeta de datos __[aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Modul_5_Exercise2_Drought_Monitoring_Trigger/Modul_5_Exercise2_Drought_Monitoring_Trigger.zip)__ y guárdela en su PC. ¡Descomprima el archivo .zip!

Para este ejercicio en particular, utilizaremos una combinación de datos preprocesados y la descarga de datos reales de FEWS.net.
Los conjuntos de datos preprocesados son los siguientes:

| Conjunto de datos | Fuente | Descripción |
| ----- | --- | --- |
| Límites administrativos | [HDX](https://data.humdata.org/dataset/cod-ab-som?) | A través de HDX se puede acceder a los límites administrativos del nivel 0-2 de Somalia y Somalilandia. Para este mecanismo de activación, proporcionamos los límites administrativos en el nivel 2 (nivel de distrito) como archivo shapefile. Hemos agregado el número de habitantes de cada distrito obtenido de Worldpop. |
| Recuentos de población | [Worldpop](https://hub.worldpop.org/doi/10.5258/SOTON/WP00534) | El conjunto de datos worldpop en formato ráster .geotif proporciona estimaciones de población por hectárea para el año 2020 |

Mientras que los datos de proyecciones de la IPC serán descargados por los participantes directamente desde FEWS.net.

| Conjunto de datos | Fuente | Descripción |
| ----- | --- | --- |
| Proyecciones cartográficas de la IPC | [FEWSNET](https://fews.net/) | escala de cinco fases que proporciona normas comunes para clasificar la gravedad de la inseguridad alimentaria aguda o prevista. |


## Tarea

:::{Attention}
Algunas de las imágenes y videos no son 100 % precisos para este ejercicio en particular, ya que se tomaron del flujo de trabajo de activación real de SRCS, que es más complejo.
:::

### Paso 1: Configurar la estructura de carpetas

__Propósito:__ En este paso, establecemos la estructura de carpetas correcta para facilitar el análisis y garantizar la coherencia de los resultados.

__Herramienta:__ No se necesitan herramientas ni programas especiales.

::::::{list-table}
:header-rows: 1
:widths: 10 25

* - Instrucciones
  - Estructura de carpetas
* - 1. Abra la carpeta "Modul_5_Exercise2_Drought_Monitoring_Trigger"
    2. Abra la subcarpeta "Monitoring"
    3. Copie la carpeta de plantillas "TEMPLATE_Year_Month" y cámbiele el nombre por el del año y mes actuales `2024_01`.

  -
    :::{figure} /fig/Exercise_Folder_structure_Drought_Monitoring_Trigger.drawio.svg
    ---
    width: 450px
    name: es_Exercise_Folder_structure_Drought_Monitoring_Trigger
    align: center
    ---
    :::
::::::

El siguiente video muestra el proceso para configurar la carpeta para diciembre de 2023.

:::{dropdown} Video: Configurar la estructura de carpetas
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_folder_setup.mp4"></video>
:::

### Paso 2: Descargue los datos de previsión


__Propósito:__ En este paso, descargaremos los datos de previsión en los que se basarán nuestros desencadenantes.

__Herramienta:__ Navegador de Internet

Los datos de la IPC se extraerán del sitio web de FEWSNET. FEWS NET publica los datos de la IPC en su sitio web.
Las principales publicaciones de datos, así como las actualizaciones de los datos de la IPC, suponen la publicación de nuevos datos casi mensualmente.

### Datos de la ICP

Los datos de la proyección de la ICP se publican y actualizan periódicamente en el sitio web [FEWSNET](https://fews.net/).
En el sitio web, tendrá que hacer clic en Somalia para acceder a los datos. Alternativamente, puede acceder a ellos a través de `Data` -> `Acute Food Insecurity Data` e introducir "Somalia". En el menú verá diferentes formatos de datos para diferentes marcas de tiempo. Una vez que sepa qué marca de tiempo es la más actual, busque la descarga ZIP. Necesitamos los datos en formato shapefile (.shp), que solo se incluye en el archivo ZIP y no se proporciona como archivo de descarga individual.


:::{Warning}
¡Las páginas de FEWSNET cambian con frecuencia!
:::

1. Visite el [Sitio web de FEWSNET](https://fews.net/). Haga clic en `Data` -> `Acute Food Insecurity`.
2. Desplácese hacia abajo. En `Geographic Area`, escriba "Somalia" y haga clic en `Apply`.
3. Elija el conjunto de datos más reciente.

:::{figure} /fig/IPC_Projections_website.png
---
height: 250px
name: es_IPC_Projections_website
align: center
---
:::

4. Descargue el que contiene los datos __ZIP__.
5. Cuando haya descargado los datos, haga clic derecho sobre el archivo y luego haga clic en `Extraer Todo` →  `Extraer`.
6. Abra la carpeta extraída y copie los datos ML1 en la carpeta IPC_ML1 que ha creado en el paso 1.
  * El nombre del archivo se compone de "SO" para Somalia, año y mes del mes del informe, por ejemplo `SO_202308_ML1.shp`.
    Ejemplo de ruta: `.../Modul_5_Exercise2_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/IPC_ML1`.
  :::{Warning}
  ¡Asegúrese de __no__ utilizar los datos ML1_IDP incluidos también en la carpeta .zip!
  :::

::::{Warning}
Recuerde que debe copiar todos los componentes del [shapefile](/content/es/Wiki/es_qgis_geodata_types_wiki.md#vector-data) correspondiente. Lo más probable es que tenga 5 componentes: .cpg, .dbf, .prj, .shp y .shx.
::::

:::{figure} /fig/IPC_zip.PNG
---
height: 300px
name: es_IPC_zip 
align: 
Contenido del archivo .zip descargado que contiene las proyecciones IPC de ML1 y ML2.
:::

:::{tip}
Puede suscribirse [en la página principal de FEWSNET](https://fews.net/), para recibir información sobre las últimas actualizaciones por correo electrónico. Para ello, desplácese hasta el final de la página y haga clic en `Sign up for Emails`. Tendrá la opción de elegir actualizaciones solo para Somalia.

:::{figure} /fig/IPC_Newsletter.png
---
height: 60px
name: es_FEWSNET Newsletter
align: center
---
:::


### Paso 3: Carga de datos en QGIS

__Propósito:__ En este paso, todos los datos necesarios se cargarán en un proyecto QGIS para que podamos analizarlos.

__Herramienta:__ No se necesitan herramientas específicas, solo QGIS.

1. Abra QGIS y cree un [nuevo proyecto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) haciendo clic en `Proyecto` → `Nuevo`
2. Una vez creado el proyecto, guárdelo en la carpeta que creó en el paso 1 (por ejemplo, 2022_05). Para ello, haga clic en `Proyecto` → `Guardar como...` y vaya hasta la carpeta. Asigne al proyecto el mismo nombre que la carpeta que ha creado (por ejemplo, 2022_05). A continuación, haga clic en `Guardar`
3. Cargue todos los datos de entrada en QGIS mediante [arrastrar y soltar](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop). Haga clic en `Proyecto` → `Guardar`
  * Desde la carpeta creada en el paso 1
    * ML1
  * En la carpeta `Fixed_data`:
    * district_pop_som
    * WorldPop_som.tif

__Resultado:__ Proyecto QGIS con todos los datos necesarios listos para ser analizados.

### Paso 4: Intersección de los datos de ML 1 con los polígonos del distrito

__Propósito:__ El objetivo es recibir capas de polígonos que compartan tanto los bordes como los atributos de ambas capas de entrada.


__Herramienta:__ [`Intersection`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_geoprocessing_wiki.html#intersection)


::::::{list-table}
:header-rows: 1
:widths: 20 25

* - Instrucciones
  - Captura de pantalla de la ventana Intersección
* - 1. Haga clic en `Vectorial` → `Geoprocessing Tools` → [`Intersección`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_geoprocessing_wiki.html#intersection)
    2. `Capa de entrada`: ML 1
    3. `Capa de superposición`: district_pop_sum
    4. En `Intersección` haga clic en los tres puntos ![](/fig/Three_points.png) → `Guardar a archivo` y vaya hasta su carpeta de seguimiento [Año_Mes]. Asigne a la salida el nombre "ML1_Intersección" y haga clic en `Guardar`
    5. Haga clic en `Ejecutar`
  -
    :::{figure} /fig/SRCS_Trigger_step_4_Intersection.png
    ---
    width: 450px
    name: es_SRCS_Trigger_step_4_Intersection
    align: center
    ---
    :::
::::::

__Resultado:__ Después de hacer esto para ML1, debería tener una capa de polígonos que contenga todas las columnas de ML1 y district_pop_sum.

:::{Note}
La capa resultante puede tener más filas que las capas originales.
:::

:::{dropdown} Video: Intersección de los datos de ML 1 con los polígonos del distrito
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_4_Intersection.mp4"></video>
:::

### Paso 5: Cálculo de la población por polígono de intersección

__Propósito:__ Aquí calculamos la población en cada polígono de la capa de intersección del paso 4.


__Herramienta:__ [Estadísticas de zona`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_raster_basic_wiki.html#zonal-statistics)

::::::{list-table}
:header-rows: 1
:widths: 20 25

* - Instrucciones
  - Captura de pantalla de la ventana de estadísticas zonales
* - 1. En la Caja de herramientas de Procesos → Buscar [`Estadísticas de zona`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_raster_basic_wiki.html#zonal-statistics)
    * Consejo: Si la página `Caja de herramientas de Procesos` no está abierta, haga clic en `Procesos` → `Caja de herramientas`
    2. `Capa de entrada`: "ML1_Intersection"
    3. `Capa ráster`: "som_ppp_2020_UNadj_constrained.tif"
    4. Estadísticas para calcular: Solo `Suma`
    5. En `Estadísticas zonal`, haga clic en los tres puntos ![](/fig/Three_points.png) → `Guardar a archivo` y vaya hasta su carpeta de supervisión [Año_Mes]. Asigne a la salida el nombre "ML1_zonal_statistic" y haga clic en `Guardar`
    5. Haga clic en `Ejecutar`.
  -
    :::{figure} /fig/SRCS_Trigger_step_5_zonal_statistic.png
    ---
    width: 450px
    name: es_SRCS_Trigger_step_5_zonal_statistic
    align: center
    ---
    :::
::::::

__Resultado:__ El resultado debería ser la "ML1_zonal_statistic" como capa de polígonos. Esta capa debe tener las mismas columnas en la tabla de atributos como ML1_Intersection __más__ la columna "_suma", que es el número de personas que viven en las partes individuales de los polígonos.


:::{dropdown} Video: Cálculo de la población por polígono de intersección
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_5_zonal_statistic.mp4"></video>
:::

### Paso 6: Ponderación de la población en función de la fase IPC


__Propósito:__ La finalidad de este paso es la ponderación de la población en las cinco fases de la IPC, tal como se describe en [IPC Data](https://giscience.github.io/gis-training-resource-center/spanish/content/es/GIS_AA/es_qgis_drought_trigger_somalia.html#ipc-population-weighted-index).

:::{Note}
El Índice IPC trata a los distritos de baja población igual que a los de alta población, garantizando que los distritos pequeños con alta inseguridad alimentaria no estén subrepresentados.
:::

:::{dropdown} Índice IPC ponderado por la población

Para aprovechar mejor los datos IPC, se creó un índice sencillo ponderado por la población. Este índice asigna ponderaciones a los números relativos de población según sus respectivas clases IPC, enfatizando la cantidad de personas en cada clase IPC en lugar de considerar únicamente la clase en sí. Además, se da más importancia a las poblaciones de las clases más altas de la IPC que a las de las clases más bajas. El índice se calcula del siguiente modo:

`$ IPC\ Index =  Weights \times \frac{District\ Pop\ per\ IPC\ Phase}{Total\ District\ Pop}$`

Donde las ponderaciones se definen como:

| Fase IPC | Ponderación |
| ----- | --- |
| IPC 1 | 0 |
| IPC 2 | 0 |
| IPC 3 | 1 |
| IPC 4 | 3 |
| IPC 5 | 6 |

El índice IPC trata a los distritos con poca población de la misma manera que a los distritos con alta población. No se produce una subrepresentación de la alta inseguridad alimentaria de los distritos pequeños.
:::
__Herramienta:__ [`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field)


1. Haga clic con el botón derecho en la capa "ML1_zonal_statistic" → `Abrir tabla de atributos` → haga clic en [`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) para abrir la calculadora de campos
2. Verifique `Crear un nuevo campo`
3. `Nombre del campo de salida`: Nombre la nueva columna “pop_suma_ponderada”
4. `Tipo del campo de salida`: Número decimal (real)
5. Añada el bloque de código de la entrada en el `Expresión` campo.
6. Haga <kbd>clic</kbd> en `Aceptar`.

```md
CASE

WHEN "ML1" = 3 THEN "_sum" * 1
WHEN "ML1" = 4 THEN "_sum" * 3
WHEN "ML1" = 5 THEN "_sum" * 6
ELSE "_sum"

END
```
6. Cuando haya terminado, haga clic en ![](/fig/mActionSaveEdits.png) para guardar sus ediciones y desactive el modo de edición haciendo clic de nuevo en ![](/fig/mActionToggleEditing.png)([Wiki Video](/content/es/Wiki/es_qgis_attribute_table_wiki.md#attribute-table-data-editing)).

## Paso 7: Cálculo de la proporción de población por polígono de intersección

__Propósito:__ En este paso, calculamos el [Índice IPC ponderado por la población](/content/GIS_AA/en_qgis_drought_trigger_somalia.md#ipc-population-weighted-index) para cada pequeña parte de la capa de polígonos.


__Herramienta:__[`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#attribute-table-data-editing)

1. Haga clic con el botón derecho en la capa "ML1_zonal_statistic" → `Abrir tabla de atributos` → haga clic en [`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.html#attribute-table-data-editing) ![](/fig/mActionCalculateField.png) para abrir la calculadora de campos
2. Verifique `Crear un campo nuevo`
3. `Nombre del campo de salida `: Nombre la nueva columna “Index_per_IPCPolygon_ML1”
4. `Tipo del campo de salida`: Número decimal (real)
5. Añada el siguiente código en el campo `Expresión`.
```md
"pop_sum_weighted"/"districtpo"
```
6. Haga <kbd>clic</kbd> en `Aceptar`.
7. Guarde la nueva columna haciendo clic en ![](/fig/mActionSaveEdits.png) la tabla de atributos y desactive el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png).

:::{figure} /fig/SRCS_Trigger_step_8_field_calculator.png
---
width: 500px
name: es_SRCS_Trigger_step_8_field_calculator
align: center
---
:::

__Resultado:__ La capa "ML1_zonal_statistic" debería tener ahora la columna "Index_per_IPCPolygon_ML1". Las cifras de esta columna tienen que ser menores que las de la columna "distrito".


:::{dropdown} Video: Cálculo de la proporción de población por polígono de intersección
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_TRigger_step_8_field_calculator.mp4"></video>
:::

### Paso 8: Calcular el índice IPC por distrito

__Propósito:__ El propósito de este paso es calcular una media ponderada por la población sobre las clases IPC por distrito. De este modo, se dará más importancia a la cantidad de personas que viven en una determinada clase de IPC que a la superficie afectada por una determinada clase de IPC. El resultado es un valor del Índice IPC para cada distrito.

__Herramienta:__ `Unir atributos por localización (resumen)`

::::::{list-table}
:header-rows: 1
:widths: 20 25

* - Instrucciones
  - Unir atributos por ubicación (resumen)
* - 1. En la caja de herramientas de Procesos → Busque `Unir atributos por localización (resumen)`.
      * Consejo: Si la página caja de herramientas de Procesos no está abierta, haga clic en `Procesos` → `caja de herramientas`.
    2. `Unirse a las funciones en`: Seleccione su capa "district_pop_som".
    3. `Comparando con`: Seleccione "ML1_zonal_statistic".
    4. `Donde los objetos`: Seleccione "intersecan".
    5. `Campos a resumir`: Seleccione "Index_per_IPCPolygon_ML1".
    6. `Resúmenes a calcular`: Marque solo la opción "media".
    7. En `Capa unida`, haga clic en los tres puntos ![](/fig/Three_points.png) → `Guardar a archivo` y vaya hasta su carpeta de supervisión [Año_Mes]. Asigne a la salida el nombre "ML1_IPC_Index" y haga clic en `Guardar`.
    8. Haga clic en `Ejecutar`.
  -
    :::{figure} /fig/Exercise_trigger_join_attributes_location.png
    ---
    width: 450px
    name: es_Exercise_trigger_join_attributes_location
    align: center
    ---
    :::
::::::

__Resultado:__ Como resultado, su capa "ML1_IPC_Index" debería tener la columna "Index_per_IPCPolygon_ML1_mean". Además, el número de filas debe ser exactamente igual al número de distritos en Somalia y los polígonos deben tener la forma exacta de los distritos.

:::{dropdown} Video: Calcular el índice IPC por distrito
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_9_join_location.mp4"></video>
:::

### Paso 9: Evaluar la activación del desencadenante

__Propósito:__ El objetivo de este paso es obtener una visión general rápida de la posible activación del desencadenante sin tener que revisar los datos reales. En su lugar, tendremos una columna binaria con valores trigger = sí o trigger=no.

__Herramienta:__ [`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field)

1. Haga clic con el botón derecho en la capa "ML1_IPC_Index" → `Abrir tabla de atributos` → haga clic en [`Calculadora de campo`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) para abrir la calculadora de campos
2. Verifique `Crear un campo nuevo`
3. `Nombre del campo de salida`: Nombre la nueva columna "Activación_desencadenante".
4. `Tipo del campo de salida`: Texto (cadena).
5. Añada el código siguiente en el campo `Expresión`.
6. Guarde la nueva columna haciendo clic en ![](/fig/mActionSaveEdits.png) la tabla de atributos y finalice el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png).

::::::{list-table}
:header-rows: 1
:widths: 15

* - Código
* - ```md
    CASE

    WHEN "Index_per_IPCPolygon_ML1_mean" >0.7 
    THEN 'yes'
    ELSE 'no'

    END
    ```
::::::

6. Haga clic en `Aceptar`.
7. Guarde la nueva columna haciendo clic en ![](/fig/mActionSaveEdits.png) la tabla de atributos y finalice el modo de edición haciendo clic en ![](/fig/mActionToggleEditing.png).

__Resultado:__ Una capa con todos los distritos de Somalia con una columna que contiene valores "Sí" y "No" que indica si se han alcanzado o no los niveles de activación.

:::{figure} /fig/Exercise_trigger_evaluation.png
---
width: 600px
name: es_Exercise_trigger_evaluation
align: center
---
:::

:::{dropdown} Video: Evaluar la activación del desencadenante
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_step_13_trigger_activation.mp4"></video>
:::

### Paso 10.: Visualización de los resultados

__Propósito:__ Definición de cómo se representan visualmente las entidades en el mapa.

__Herramienta:__ [Simbología](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#symbology-for-vector-data)

__Activación del desencadenante__

1. Haga clic con el botón derecho en la capa "ML1_IPC_Index" →  `Propriedades` →  `Simbología`.
2. En la esquina inferior izquierda, haga clic en `Estilo` →  `Cargar estilo`.
3. En la nueva ventana, haga clic en los tres puntos ![](/fig/Three_points.png). Vaya hasta la carpeta "FbF_Drought_Monitoring_Trigger/layer_styles" y seleccione el archivo __"Style_Trigger_Activation_ex.qml"__.
4. Haga clic en `Abrir`. A continuación, haga clic en `Cargar estilo`.
5. De nuevo en la ventana “Layer Properties”, haga clic en `Aplicar` y `Aceptar`.

::::{dropdown} Información: Capa de activación del desencadenante
:open:
Ahora verá los distritos en los que no hay activación en verde y los distritos con activación en rosa.

La capa de estilo "Style_Trigger_Activation.qml" está configurada para mostrar los nombres de los distritos en donde el disparador esté realmente activado. Si no hay activación de un desencadenante puede activar la capa de límites del administrador 1 para una mejor orientación del mapa (véase __Límites del administrador 2__ más abajo).
::::

:::{figure} /fig/Map_yes_trigger.PNG
---
width: 1000px
name: es_Map_yes_trigger
align: center
---
:::


__Fronteras administrativas 2 (Regiones)__

6. Haga clic con el botón derecho en la capa "Som_admin1_regions_UNDP.gqkp" (Regiones) →  `Propriedades` →  `Simbología`.
7. En la esquina inferior izquierda, haga clic en `Estilo` →  `Cargar estilo`.
8. En la nueva ventana, haga clic en los tres puntos ![](/fig/Three_points.png). Vaya hasta la carpeta "FbF_Drought_Monitoring_Trigger/layer_styles" y seleccione el archivo __"SOM_regions_style_ex.qml"__.
9. Haga clic en `Abrir`. A continuación, haga clic en `Cargar estilo`.
10. De nuevo en la ventana “Layer Properties”, haga clic en `Aplicar` y `Aceptar`.
11. Añada un mapa base de OpenStreetMap haciendo clic en `Capa` →  `Añadir capa` →  `Añadir capa XYZ...` →  Seleccione OpenStreetMap. Haga clic en `Add`. ([Wiki mapa base](/content/es/Wiki/es_qgis_basemaps_wiki.md)).
12. Ponga el mapa base de OpenStreetMap en la parte inferior.
13. Borre todas las capas __excepto__:
    * Activación_desencadenante
    * Som_admin1_regions_UNDP
    * OpenStreetMap

:::{dropdown} Video: Visualización de resultados
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Trigger_model_style.mp4"></video>
:::

::::::{list-table}
:header-rows: 1
:widths: 20 20

* - Mapa de intervención __sin__ Activación del desencadenante
  - Mapa de intervención __con__ Activación del desencadenante
* - 
    :::{figure} /fig/Map_no_trigger.PNG
    ---
    width: 1000px
    name: es_Map_no_trigger
    align: center
    ---
    :::

  -
    :::{figure} /fig/Map_yes_trigger.PNG
    ---
    width: 450px
    name: es_Map_yes_trigger
    align: center
    ---
    :::
::::::

:::{Attention}
Recuerde el [concepto de capa](es/Module_2/es_qgis_geodata_concept.md) y asegúrese de que la capa de mapa base esté en la parte inferior de su panel de capas.
:::

### Paso 11: Mapa de impresión

__Propósito:__ Visualización de las características del mapa en un esquema imprimible.

__Herramienta:__ [Diseño de impresión](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_2.html)


1. Si no lo ha hecho antes, elimine todas las capas excepto __Trigger_activation__, __Som_admin1_regions_UNDP__ y __OpenStreetMap__.
2. Abra una nueva composición de impresión haciendo clic en `Proyecto` → `Nueva composición de impresión` → introduzca el nombre de su proyecto actual, por ejemplo, “2024_01”.
3. Vaya a la carpeta `Modul_5_Exercise2_Drought_Monitoring_Trigger` y arrastre y suelte el archivo `Trigger_activation_Intervention_map_ex.qpt` en el diseño de impresión.
4. Cambie la fecha a la actual haciendo clic en “Further map information” en el panel de elementos. Haga clic en la pestaña `Propriedades del elemento` y desplácese hacia abajo. Aquí puede cambiar la fecha en el campo `Propriedades principales`.
5. Si es necesario, ajuste la leyenda haciendo clic en la leyenda en la pestaña `Propriedades del elemento` y desplácese hacia abajo hasta que vea el campo `elementos de la leyenda`. Si no está visible, verifique si necesita abrir el menú desplegable. Asegúrese de que `Auto actualizar` no esté marcada.
    * Elimine todos los elementos de la leyenda haciendo clic en el elemento y luego en el icono rojo con el signo menos que aparece debajo.
    * Añada __Trigger_activation__ a la leyenda haciendo clic en el signo más verde y haga clic en la capa y haga clic en `Aceptar`.
    * Añada __Som_admin1_regions_UNDP__ a la leyenda haciendo clic en el signo más verde y haga clic en la capa y haga clic en `Aceptar`.


:::{dropdown} Video: Hacer un mapa impreso
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
:::

:::{Attention}
Asegúrese de editar la información del mapa en la plantilla, por ejemplo, la fecha actual. Asegúrese también de comprobar los elementos de la leyenda: Elimine los elementos innecesarios y, con el tiempo, cambie los nombres por descripciones con sentido.
:::

También puede adaptar la plantilla a sus necesidades y preferencias. Puede encontrar ayuda [aquí](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_2.html).

:::{Attention}
Asegúrese de editar la información del mapa en la plantilla, por ejemplo, la fecha actual. Asegúrese también de comprobar los elementos de la leyenda: Elimine los elementos innecesarios y, con el tiempo, cambie los nombres por descripciones con sentido.
:::

### Paso 13.: Exportar mapa


__Propósito:__ Exporte el mapa diseñado y finalizado para imprimirlo en formato PDF o en el formato que prefiera.


__Herramienta:__ [Diseño de impresión](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_2.html)

Cuando haya terminado el diseño de su mapa, puede exportarlo como archivo PDF o de imagen en diferentes tipos de datos.

__Exportar como imagen__

1. En el diseño de impresión, haga clic en `Diseño` → `Exportar como imagen`.
2. Elija la carpeta __Result__ en la carpeta que ha creado en el paso 1. Asigne al archivo el nombre del proyecto, por ejemplo 2022_04.
3. Haga clic en `Guardar`.
4. Aparecerá la ventana "Opciones de exportación de imágenes". Haga clic en `Guardar`.
Ahora la imagen se puede encontrar en la carpeta de resultados en la carpeta que creó en el paso 1.


__Exportar como PDF__

1. En el diseño de impresión, haga clic en `Diseño` → `Exportar como PDF`.
2. Elija la carpeta __Result__ en la carpeta que ha creado en el paso 1. Asigne al archivo el nombre del proyecto, por ejemplo 2022_04.
3. Haga clic en `Guardar`.
4. Aparecerá la ventana "Opciones de exportación PDF". Para obtener los mejores resultados, seleccione la compresión de imagen `lossless`.
5. Haga clic en `Guardar`.

Ahora la imagen se puede encontrar en la carpeta de resultados en la carpeta que creó en el paso 1.


:::{figure} /fig/map_output_example_ex.png
---
width: 1000px
name: es_map_output_example_ex
align: center
---
:::
