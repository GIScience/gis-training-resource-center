# Ejercicio: Preparación de datos (importar tablas en formato PDF a QGIS)

## Características del ejercicio

::::{grid} 4 2

:::{grid-item-card}
__Objetivo de este ejercicio:__
^^^

A lo largo de su carrera relacionada con los SIG, muchas veces se encontrará con datos a los que no es fácil acceder o con los que es difícil trabajar.
El objetivo de este ejercicio es entender cómo preparar y limpiar los datos que se encuentran en un archivo PDF para su uso en un proyecto QGIS.

:::


:::{card}
__Artículos relevantes en Wiki:__
^^^
* [Interfaz de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html)
* [Importar archivos CSV a QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#text-data-importl)
* [Tabla de atributos en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_attribute_table_wiki.md)

:::

::::


:::{Topic} Contexto

En 2024, las provincias de Punjab, Sindh y Baluchistán, en Pakistán, sufrieron inundaciones devastadoras debido a precipitaciones intensas y prolongadas. El impacto de las inundaciones en la infraestructura depende, en gran medida, de los materiales de construcción de las viviendas. Para determinar la vulnerabilidad de la infraestructura frente a los daños de las inundaciones, utilizaremos datos sobre el material de las paredes de las casas de cada provincia. El objetivo es elaborar un conjunto de datos que refleje qué provincias son más susceptibles a daños por inundaciones, en función del material de construcción utilizado.
En primer lugar, debemos extraer los datos del archivo PDF y guardarlos en un archivo `.csv`. A continuación, debemos limpiar y preparar el archivo `.csv` para eliminar errores e incoherencias. Ahora podemos importar el archivo `.csv` y realizar una unión de atributos para vincular la información sobre el material de las paredes a una capa vectorial que contenga los polígonos de las provincias paquistaníes.

:::


## Instrucciones para capacitadores

:::{attention}

Este ejercicio utiliza la herramienta [Tabula.technology](tabula.technology), una aplicación de código abierto que permite extraer fácilmente tablas de un archivo PDF. Para utilizar Tabula, es necesario tener instalado [Java](https://www.java.com/en/download/) en su equipo.

:::

:::{dropdown} __Rincón del instructor__


### Preparar la capacitación

- Tómese su tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser una pizarra blanca física, un rotafolio o una pizarra digital (por ejemplo, una pizarra Miro) donde los participantes puedan añadir sus conclusiones y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html#how-to-do-trainings) para obtener algunos consejos generales para impartirlas.

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

## Ejercicio

### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip

Descargue los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_7/Module_5_Exercise_7_data_cleaning.zip) y descomprímalos.

:::

| Conjunto de datos | Fuente | Descripción |
| ----- | --- | --- |
| Límites administrativos de Pakistán | [HDX](https://data.humdata.org/dataset/cod-ab-pak) | Se puede acceder a las fronteras administrativas (adm0-adm3) de Pakistán a través de Intercambio de Datos Humanitarios. Para este ejercicio, nos interesan los distritos (adm2) |
| Distribución porcentual de los hogares por tipo de material utilizado para las paredes | [Oficina de Estadísticas de Pakistán](https://www.pbs.gov.pk/content/statistical-tables-pslm-2019-20) | La tabla 7.7 de la *Encuesta de indicadores sociales y de nivel de vida de Pakistán (2019-20)* muestra los materiales utilizados en las paredes por hogar, expresados en porcentajes. |


### Tarea 1: Pasar los datos del archivo PDF a un archivo CSV

:::{Topic} Contexto

La [OFICINA DE ESTADÍSTICAS DE PAKISTÁN]publicó los datos de los materiales de las paredes en forma de tabla en un archivo PDF. La tabla del archivo PDF no puede importarse directamente a QGIS. Para empezar, es necesario convertir la tabla del archivo PDF a un archivo `.csv`.

:::

1. En su navegador, vaya a [Tabula.technology](https://tabula.technology) y descargue la aplicación.

:::{admonition} Tabula
:type: tldr
Tabula es una aplicación de código abierto que permite extraer tablas de datos de archivos PDF y guardarlas como archivos `.csv`. Los archivos `.csv` pueden importarse a Excel, QGIS u otros programas de manipulación de datos.

:::

:::{figure} /fig/en_tabula_website.png
---
name: en_tabula_website
width: 550 px
---
El sitio web Tabula.technology con los enlaces de descarga a la izquierda.
:::

2. Descomprima el archivo descargado en una ubicación de su elección (por ejemplo, Programas, Escritorio, etc.).
3. Abra la carpeta donde haya descomprimido el archivo y ejecute la aplicación “Tabula”.

:::{figure} /fig/en_tabula_folder.png
---
name: en_tabula_folder
width: 450 px
---

:::

4. Se abrirá una nueva ventana del navegador con esta dirección: http://localhost:8080. Esta es la aplicación. Si el navegador no se abre de forma automática, ábralo manualmente e ingrese esta dirección.


:::{figure} /fig/en_tabula_import.png
---
name: en_tabula_import
width: 550 px
---

:::

5. Ahora vamos a importar el archivo PDF con los tipos de pared en Tabula:
    1. Haga clic en `Browse` y vaya a la carpeta de datos del ejercicio: `...\data\input` y seleccione el PDF “pakistan_wall_type7.7”. Haga clic en `Open`.
    2. Haga clic en `Import` y espere a que se cargue el PDF. Una vez cargado, se abrirá automáticamente.

:::{figure} /fig/en_Tabula_main_view.png
---
name: en_Tabula_main_view
width: 550 px
---

:::

6. Aquí seleccionaremos la parte del PDF que contiene la tabla de datos. Tabula espera una tabla con una fila de encabezados en la parte superior para cada columna, seguida de las filas con los datos. Si arrastramos un rectángulo sobre el PDF, podemos crear una selección en la que Tabula buscará la tabla de datos. Arrastre un rectángulo y ajuste los bordes para que la tabla encaje con la mayor precisión posible en la selección. Asegúrese de capturar solo la información relevante. Dado que los encabezados de esta tabla tienen un formato poco convencional, es mejor omitirlos para que la tabla CSV resultante sea más fácil de ajustar. Añadiremos los encabezados manualmente una vez extraídas las tablas.

:::{figure} /fig/en_tabula_selection.png
---
name: en_tabula_selection
width: 550 px
---

:::

7. Una vez que esté satisfecho con la selección, puede hacer clic en `Repeat this Selection` para duplicar la selección en las páginas siguientes.
8. Compruebe en las páginas siguientes que la tabla siga estando completamente contenida en la selección.
9. Haga clic en `Preview & Export Extracted Data` en la parte superior derecha de la ventana.
10. Aparecerá una nueva ventana donde se mostrarán los datos. Al principio, no se verá nada. Haga clic en `Stream` a la izquierda.

:::{figure} /fig/en_tabula_preview_extracted_1.png
---
name: en_tabula_preview_extracted_1
width: 550 px
---

:::

11. Los datos de la tabla PDF aparecerán en la ventana principal. Revise la tabla.

:::{figure} /fig/en_tabula_data_preview.png
---
name: en_tabula_data_preview
width: 550 px
---

:::

12. Haga clic en `Export`; esto guardará el `.csv` en su carpeta de descargas.
13. Mueva el archivo a la carpeta `/data/interim/`.


¡Felicitaciones, los datos del PDF se han extraído a un archivo CSV!

### Tarea 2: Limpiar los datos de errores y entradas no deseadas

:::{topic} Contexto
Los datos se han extraído del PDF. Sin embargo, hay algunos errores de formato e información no deseada. Antes de cargar el CSV extraído en QGIS, debemos limpiar el formato y eliminar las entradas no deseadas. Esto puede hacerse de muchas maneras, por ejemplo, en un editor de hojas de cálculo, como Microsoft Excel o Libreoffice Calc.
:::

:::{note}
Los pasos necesarios para filtrar los datos pueden variar en función del editor que utilice. En este ejercicio, veremos el flujo de trabajo con la versión gratuita de Microsoft Excel.
:::

1. Abra el archivo CSV extraído en Excel. Podría verse así:

:::{figure} /fig/en_tabula_csv_excel.png
---
name: en_tabula_csv_excel
width: 300 px
---

:::

2. Excel no reconoce automáticamente el formato delimitado por comas. Para solucionarlo, seleccione la columna A y vaya a `Data` > `Text to Columns`. Se abrirá una nueva ventana. Deje la configuración como está y haga clic en `Ok`.

:::{note}
En la versión web de Excel, puede fijar las columnas seleccionando la columna A y luego yendo a `Data` > `Split Text to Columns`

:::

:::{figure} /fig/en_m5_data_cleaning_ex_task2.png
---
name: en_m5_data_cleaning_ex_task2
width: 450 px
---
La tabla de datos debería tener ahora este aspecto. Todavía faltan los encabezados de las columnas (en rojo).
:::

3. Tenemos que volver a añadir los nombres de las columnas, ya que no los extrajimos con Tabula. <kbd>Haga clic derecho</kbd> en la primera fila y seleccione `Insert 1 Row Above`. Debería aparecer una nueva fila.
4. Introduzca los encabezados de las columnas tal y como aparecen en el archivo PDF:

| Provincia y distrito | Bloques/ladrillos cocidos | Ladrillos de barro/lodo | Madera | Otros | Total |
| :------------------ | :------------------ | :------------- | :--- | :---- | :---- |

5. Ahora podemos formatear los datos en una tabla de Excel. Esto nos permitirá aplicar filtros para eliminar las entradas no deseadas. Seleccione las columnas A a F, vaya a `Home` > `Format as Table` y seleccione el estilo de tabla que desee.

Ahora tenemos un archivo .csv utilizable con la información. Sin embargo, todavía hay algunas entradas no deseadas y algunos errores de formato. En primer lugar, eliminemos todas las filas con los datos sobre la distribución rural y urbana. Queremos visualizar la distribución a nivel de distrito, por lo que no es necesario distinguir entre urbano y rural.

6. Haga clic en la flecha pequeña situada junto a la columna “Provincia y distrito”. Se abrirá un menú desplegable.
7. En el menú desplegable, desmarque la casilla `Select All` y desplácese hacia abajo para marcar todas las entradas con los valores `Urban` y `Rural`. Agregue también las entradas que tengan valores numéricos asociados a `Urban` o `Rural`. Haga clic en `Apply`.

:::::{grid} 2

::::{grid-item}
:::{figure} /fig/en_m5_data_cleaning_ex_filter_excel.png
---
name: en_m5_data_cleaning_ex_filter_excel
width: 350 px
---
:::
::::
::::{grid-item}
:::{figure} /fig/en_m5_data_cleaning_ex_filter_excel_2.png
---
name: en_m5_data_cleaning_ex_filter_excel_2
width: 350 px
---
:::
::::
:::::


8. La tabla debería mostrar ahora solo las entradas con la palabra rural o urbano en la columna “Provincia y distrito”. Selecciónelos todos y haga clic en `Remove selected rows`.

9. Ahora, debemos eliminar el filtro que hemos aplicado.

10. Repasemos la tabla resultante y veamos si tenemos que corregir más entradas. En algunas entradas los valores de los porcentajes no están formateados correctamente. Copie los valores de las columnas __Bloques/ladrillos cocidos__, __Ladrillos de barro/lodo__, __Madera__, __Otros__ en una celda a la derecha e introduzca el valor numérico que por error se añadió a la columna __Provincias y distritos__.

11. Guarde el archivo CSV formateado en la carpeta de datos de entrada (`.../module_5_ex_7_data_cleansing/data/input/`) con el nombre `tabula-pakistan_wall_type7.7`.

¡Estupendo! ¡Ahora podemos importar el archivo CSV a QGIS!

### Tarea 3: Importar los datos a QGIS

:::{topic}
Con los datos formateados como un archivo CSV utilizable, vamos a importarlos a QGIS y unirlos a una capa de polígonos que contenga los distritos (adm2) utilizando las columnas con los nombres de los distritos en inglés. Sin embargo, es posible que en este paso nos encontremos con el problema de que los nombres de los distritos estén escritos de forma diferente. En este caso, no podemos simplemente realizar una unión de atributos [LINK] ya que los atributos deben __coincidir exactamente__. Para solucionarlo, tenemos que realizar una __fusión difusa __.

:::


:::{note}
La fusión difusa es una técnica utilizada en el procesamiento de datos para combinar dos conjuntos de datos basándose en valores similares, pero no necesariamente idénticos. Esto es especialmente útil cuando se trata de datos que pueden presentar incoherencias, como errores tipográficos o formatos diferentes.

En lugar de buscar coincidencias exactas, la fusión difusa utiliza algoritmos para comparar valores y determinar su similitud. Por ejemplo, “Jon” y “John” podrían considerarse coincidentes debido a su similitud. Cada comparación genera una puntuación de similitud que indica el grado de coincidencia entre los dos valores.

:::

1. Abra QGIS y cree un nuevo proyecto.
2. Guarde el proyecto en la carpeta de ejercicios.
3. [Importe la capa CSV a QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#text-data-import).
4. Importe los límites administrativos situados en la carpeta de entrada de datos: `.../module_5_ex_7_data_cleansing/data/input/`
5. Ahora vamos a realizar una fusión difusa: Abra la [calculadora de campo ](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field) __para la capa denominada `tabula-pakistan_wall_type7.7`__ e introduzca la siguiente expresión:
    ```
    array_first(aggregate(
    layer:= 'pak_admbnda_adm2_wfp_20220909',
    aggregate:='array_agg',
    expression:=ADM2_EN,
    filter:=levenshtein(ADM2_EN, attribute(@parent, 'Province & Disctrict')) <= 2,
    order_by:=levenshtein(ADM2_EN, attribute(@parent, 'Province & Disctrict'))
    ))
    ```

6. Introduzca un `Output field name`, ajuste el `Output field type` a `Text (string)` y aumente la `output field length` a 40.

7. Haga clic en `Ok`. El archivo CSV debería tener ahora una nueva columna. En esta columna encontrará los valores de la capa de polígonos adm2 que se han emparejado utilizando el algoritmo de fusión difusa.

8. Ahora podemos realizar una unión de atributos seleccionando la columna `ADM2_EN` y la columna de fusión difusa recién creada como columna de identificación. En la caja de herramientas de procesos, busque la herramienta __“Join attributes by field value”__. <kbd>Haga doble clic</kbd> en ella.

9. Se abrirá una nueva ventana. Aquí, configure los siguientes parámetros:
    1. __Capa de entrada:__ Capa de polígonos ADM2
    2. __Campo de la tabla:__ `ADM2_EN`
    3. __Capa de entrada 2:__ `tabula-pakistan_wall_type7.7`
    4. __Campo de la tabla 2:__ `Fuzzy_match`
    5. __Campos de capa 2 a copiar:__ `Burnt Bricks/Blocks, Mud Bricks/Mud, Wood, Other`

:::{figure} /fig/en_3.36_m5_ex_7_attr_join.png
---
name: m5_ex7_attr_join
width: 450 px
---
Los parámetros “Join attributes by field value”
:::

10. Haga clic en `Run`.

¡Felicitaciones, ya hemos unido con éxito la información del archivo PDF a una capa de polígonos!

### Tarea 4: Visualización de los datos

:::{topic}

Hemos extraído los datos del PDF y ahora tenemos una capa de polígonos que contiene la información sobre el material de las paredes por distrito. Con la nueva columna, podemos crear un mapa que visualice la cantidad de edificios que tienen, por ejemplo, bloques o ladrillos cocidos como material de pared.

:::

1. Abra el panel de estilo de capas y seleccione el método de simbolización __Graduado__.
2. En `Value`, seleccione `Burnt Bricks/Blocks`.
3. Haga clic en `Classify`.

La simbolización resultante podría verse parecida a esto:

:::{figure} /fig/m5_ex_7_visualisation_result.png
---
name: m5_ex_7_visualisation_results
width: 600 px
---
Cuanto más oscuro sea el color, mayor es el porcentaje de edificios con paredes de bloques o ladrillos cocidos. Las zonas grises son los distritos de los que no se dispone de datos.
:::
