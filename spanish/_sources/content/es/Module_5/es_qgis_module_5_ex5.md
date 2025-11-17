::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Ejercicio 5: Consolidación y evaluación de las transferencias de dinero G2P en Pakistán

## Características del ejercicio

:::{card}
__Objetivo del ejercicio:__
^^^
El objetivo de este ejercicio es introducir un flujo de trabajo que combine el procesamiento espacial y no espacial. Un paso habitual es consolidar los datos en escalas administrativas como adm2 o adm3. Este ejercicio le enseñará cómo consolidar información sobre las transferencias de efectivo a nivel administrativo y luego unir las estadísticas con los datos de un polígono para los límites administrativos.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^
- Consolidar y analizar datos
- Crear informes de situación

:::
::::

::::{grid} 2
:::{grid-item-card}

__Duración estimada del ejercicio:__
^^^
~ 60 minutos

:::

:::{grid-item-card}
__Artículos relevantes en Wiki__
^^^

* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Estadísticas por categorías](/content/es/Module_5/es_qgis_non_spatial_tools.md)
* [Unión no espacial](/content/es/Wiki/es_qgis_joins_wiki.md)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese su tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser una pizarra blanca física, un rotafolio o una pizarra digital (por ejemplo, una pizarra Miro) donde los participantes puedan añadir sus conclusiones y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener algunos consejos generales para impartirlas.

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

## Instrucciones paso a paso

:::{card}
:class-card: sd-text-justify sd-rounded-3 sd-border-2
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_5/Module_5_Exercise_5_aggregating_adm.zip

__Haga clic [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_5/Module_5_Exercise_5_aggregating_adm.zip) para descargar los conjuntos de datos para este ejercicio.__

:::

:::{card}
__Datos disponibles:__
^^^

- `G2P_disbursement_report_cleaned.csv` - Tabla de datos con transacciones en efectivo. Se ha limpiado y se ha eliminado toda la información personal de este conjunto de datos.
- `pak_admbnda_adm2_wfp_20220909.shp` - Límites administrativos a nivel adm2 (distritos).
:::

::::{margin}
:::{tip}
Para cargar el archivo CSV, vaya a `Layer` > `Add Layer` > `Add delimited text layer`.
:::
::::

### Preparación de los datos

1. Descomprima los datos del ejercicio y cree un nuevo proyecto QGIS.
2. Cargue los datos en su proyecto QGIS.
3. Familiarícese con los datos. Abra la tabla de atributos de cada capa y vea qué tipo de información se almacena en los conjuntos de datos.

::::{note}
Queremos consolidar la información sobre transacciones monetarias a nivel de adm3 o adm2. ¿Puede ver que la columna de la capa `G2P_disbursement_report_cleaned` corresponde a adm2 y adm3?

:::{dropdown} Solución

Si comparamos los valores de la columna `admin2_EN` con la capa `pak_admbnda_adm2_wfp_20220909`, podemos ver que la columna `var_attr_03` corresponde al nivel admin2 de la capa `G2P_disbursement_report_cleaned`. Al ordenar las capas alfabéticamente, es más fácil encontrar valores coincidentes en ambas tablas de atributos.

:::

::::

### Paso 1: Consolidar la cantidad de dinero transferido en admin2

3. En la caja de herramientas de procesos, busque la herramienta `Aggregate` en `Vector Geometry`. <kbd>Haga doble clic</kbd> en ella. Se abrirá una nueva ventana (véase {numref}`aggregate_tool`).

:::{figure} /fig/en_3.36_aggregate.png
---
name: aggregate_tool
width: 600 px
---
La herramienta Aggregate en QGIS 3.36
:::

4. En la ventana “Aggregate”,
    1. Seleccione la capa `G2P_disbursement_report_cleaned` como capa de entrada.
    2. `Group by Expression` es donde seleccionamos qué columna queremos tener agrupada (o seleccionada como categoría). Queremos identificar la cantidad de dinero transferida a cada distrito (nivel admin2), por lo que tenemos que seleccionar la columna correspondiente. En nuestro caso, se trata de la columna `var_attr_03`.
    3. En esta casilla es donde seleccionamos cómo la herramienta consolida las distintas columnas:
        - Queremos calcular el `Sum` para la columna “Amount”.
        - Para la columna “var attr 03” queremos seleccionar `Concatenate_unique`. Esto obtiene todas las cadenas únicas de un campo.
        - Las demás columnas pueden ajustarse a `concatenate_unique`
    4. Haga clic en `Run`. Aparecerá una nueva capa llamada “Aggregated” en el panel de capas. Cierre la ventana "Aggregate".


    :::{figure} /fig/en_3.36_aggregate_settings.png
    ---
    name: aggregate_settings
    width: 650 px
    ---
    Ajuste la función “aggregation” para las columnas pertinentes. Preste atención a que el `Type` para el importe esté configurado como “Integer”. Si ha importado correctamente la tabla en QGIS, esto debería establecerse automáticamente.
    :::

    :::{admonition}
    :type: note
    Si el `Type` para la columna de cantidad se establece en “Text (string)”, QGIS leerá el formato de datos para esta columna como un valor de cadena. QGIS no puede realizar operaciones matemáticas sobre valores de cadena porque los lee como datos no numéricos. Asegúrese de importar la capa a través del diálogo `Add delimited text layer`(`Layer` > `Add Layer` > `Add delimited text layer...`) y de que `Type` para la columna “Amount” está configurada como Integer.
    :::

    5. Echemos un vistazo a la nueva capa abriendo la tabla de atributos. Si ha hecho todo correctamente, la tabla debería tener el siguiente aspecto: {numref}`aggregate_results`. Podemos ver una fila por cada valor distinto en la columna `var attr 03` (Gwardar, Jamshoro, Dadu, Kambar Shahdadkot, Shiparpur). En la columna `Amount` vemos la suma de todas las transferencias individuales. En las demás columnas, podemos ver una cadena con los distintos valores de la tabla original separados por comas (por ejemplo, las distintas unidades admin3, Thesils, bajo la columna `var attr 04`).

    :::{figure} /fig/en_aggregate_results.png
    ---
    name: aggregate_results
    width: 650 px
    ---
    Los datos consolidados de `G2P_disbursement_report_cleaned`
    :::


### Paso 2: Unir los datos consolidados con los límites administrativos

En este paso, agregaremos la información consolidada que hemos obtenido del archivo CSV a los límites administrativos. Tenemos que unir la tabla consolidada con la capa `pak_admbnda_adm2_wfp_20220909`.

1. En la caja de herramientas de procesos, busque `Join attributes by field value`. <kbd>Haga doble clic</kbd> en ella. Se abrirá una nueva ventana.

    :::{figure} /fig/en_3.36_join_by_attr.png
    ---
    name: join_by_attr
    width: 700 px
    ---
    El cuadro de diálogo “Join attributes by field value” en QGIS 3.36.
    :::

    1. La capa de entrada debe ser la capa `pak_admbnda_adm2_wfp_20220909`. Esta será la capa que recibirá información adicional. Se conservarán las geometrías de la capa de entrada. La dirección `Table field` debe ajustarse a "ADM2_EN". Estos son los nombres en inglés para el nivel admin2.
    2. La segunda capa de entrada debe ser la capa `Aggregated` del paso anterior. `Table field 2` también deben ser los nombres en inglés de los límites administrativos. En nuestro caso, la columna correspondiente es "var attr 03". En `Layer 2 fields to copy`, seleccione únicamente `amount`, ya que no nos interesan los demás valores.
2. Haga clic en `Run`. Aparecerá una nueva capa `Joined Layer` en el panel de capas.
3. Cierre el cuadro de diálogo de unión e investigue la nueva capa abriendo su tabla de atributos. Desplácese a la derecha para encontrar la nueva columna “amount” que se ha unido.
4. ¿Puede notar que la mayoría de las filas tienen `NULL` como valor en esta columna? Esto se debe a que la tabla consolidada solo tiene 5 distritos (adm2) que recibieron dinero. Puede ordenar la tabla haciendo clic en la cabecera de la columna.

¡Felicitaciones, hemos unido con éxito un archivo CSV con una capa de polígonos!

:::{figure} /fig/en_m5_ex5_results.png
---
name: aggregation_ex_results
width: 750 px
---
El importe consolidado se ha unido a una capa de las fronteras administrativas.
:::

