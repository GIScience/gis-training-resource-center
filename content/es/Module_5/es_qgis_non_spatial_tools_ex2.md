::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

## Ejercicio 2: Impacto de los desastres en diferentes regiones de Senegal

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}

### Objetivo del ejercicio
Familiarizarse con los distintos tipos de análisis no espacial y las herramientas de geoprocesamiento. Comprender el proceso de descubrimiento de relaciones y conexiones entre entidades en datos espaciales.

#### Tipo de ejercicio de capacitación:

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}

#### Grupo focal (Nivel de conocimientos SIG)


#### Estas habilidades son relevantes para


:::
::::

::::{grid} 2
:::{grid-item-card}

#### Duración estimada del ejercicio.



:::

:::{grid-item-card}

## Artículos relevantes en Wiki

* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Consultas espaciales](/content/es/Wiki/es_qgis_spatial_queries_wiki.md)
* [Geoprocesamiento](/content/es/Wiki/es_qgis_geoprocessing_wiki.md)
* [Clasificación por categorías](/content/es/Wiki/es_qgis_categorized_wiki.md)

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese su tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser una pizarra blanca física, un rotafolio o una pizarra digital (por ejemplo, una pizarra Miro) donde los participantes puedan añadir sus conclusiones y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md#how-to-do-trainings) para obtener algunos consejos generales para impartirlas.

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

### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Modul_5_Exercise1_Disaster_effects_in_different_regions_Senegal/Modul5_Exercise1_Disaster_effects_in_different_regions_Senegal.zip
__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Modul_5_Exercise1_Disaster_effects_in_different_regions_Senegal/Modul5_Exercise1_Disaster_effects_in_different_regions_Senegal.zip), guarde la carpeta en su ordenador y descomprima el archivo.__
:::

- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Datos de los límites de Senegal (Nivel administrativo 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `DI_Stat924.xls`: [Datos de Desinventar Sendai de Senegal](https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=sen) que muestran los efectos de los desastres en las regiones senegalesas
- `sen_admpop_adm1_2020.csv`: Senegal nivel administrativo 1 (región) 2019 [proyección cartográfica de estadísticas de población](https://data.humdata.org/dataset/senegal-population-statistics)

:::{Hint}
Todos los archivos conservan sus nombres originales. No obstante, no dude en modificar sus nombres si fuera necesario para identificarlos más fácilmente.
:::

### Tarea
Crear un resumen general de los efectos de los desastres en las distintas regiones de Senegal. Utilice uniones no espaciales, funciones de tabla y diferente simbología.

:::{Hint}
El sistema de coordenadas previsto para Senegal es `EPSG:32628 WGS 84 / UTM zone 28N`
:::

1. Cargue la capa de límites administrativos de Senegal (`sen_admbnda_adm1_1m_gov_ocha_20190426.shp`), así como la población por unidad subnacional (`sen_admpop_adm1_2020.csv`) y los datos de Desinventar Sendai de Senegal (`DI_Stat924.xls`) en QGIS.

2. Asegúrese de reproyectar el conjunto de datos con los límites administrativos en la zona UTM 28N. Para obtener más información, consulte la entrada de Wiki sobre [proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md).

3. Realice uniones no espaciales basadas en las regiones que figuran en dos conjuntos de datos y el PCODE que figura en estos mismos conjuntos. Consulte la entrada de Wiki sobre [uniones no espaciales](/content/es/Wiki/es_qgis_non_spatial_joins_wiki.md) para obtener más información.

:::{figure} /fig/en_ex1_AT_admin_pop_sen.png
---
width: 100%
name: es_attributes_all
---
Captura de pantalla de las diferentes tablas de atributos con las columnas correspondientes resaltadas.
:::

4. En primer lugar, añada la población total de cada área administrativa a los archivos shapefiles. Seleccione la columna correcta que deberá añadirse (sugerencia: busque la columna denominada `Total`).
5. A continuación, sume el número de personas afectadas directa e indirectamente. Seleccione también las columnas correctas que deberán añadirse (sugerencia: busque los nombres de las columnas `Directly affected` y `Indirectly Affected`).

:::::{tab-set}

::::{tab-item} Captura de pantalla de la tarea 4
:::{figure} /fig/en_ex1_Join_field.png
---
width: 80%
name: es_join_field
---
Captura de pantalla de la herramienta Unir atributos por valor de campo para la población total
:::
::::

::::{tab-item} Captura de pantalla de la tarea 5
:::{figure} /fig/en_ex1_Join_field_2.PNG
---
width: 80%
name: es_join_field
---
Captura de pantalla de la herramienta Unir atributos por valor de campo para las personas afectadas directa e indirectamente
:::
::::

:::::

6. Utilice las funciones de tabla para calcular la superficie de cada región en kilómetros cuadrados y la densidad de población. Para obtener más información, consulte la entrada de Wiki sobre las [funciones de la tabla](/content/es/Wiki/es_qgis_table_functions_wiki.md).
    - Cree una nueva columna/campo con el nombre `"area_sqkm"` utilizando la calculadora de campos. Asegúrese de que se utilicen números decimales como tipo de campo. Para el cálculo utilice la expresión: `$area / (1000 * 1000)`
    - Cree otra columna/campo con el nombre `"pop_per_sqkm"` con números decimales como tipo de campo. Utilice la expresión: `"Total" / "area_sqkm"` para el cálculo.

Puede acceder a la calculadora de campo a través de su tabla de atributos activando ![](/fig/mActionToggleEditing.png) `Conmutar edición` y haciendo clic en este símbolo ![](/fig/mActionCalculateField.png) para abrir la `calculadora de campo`.

:::::{tab-set}

::::{tab-item} Capturas de pantalla del cálculo `"area_sqkm"`
:::{figure} /fig/en_ex1_area_sqkm.png
---
width: 80%
name: es_field_calculator
---
Captura de pantalla del cálculo del área utilizando la calculadora de campo.
:::
::::

::::{tab-item} Capturas de pantalla del cálculo `"pop_per_sqkm"`
:::{figure} /fig/en_ex1_pop_per_sqkm.png
---
width: 80%
name: es_field_calculator_2
---
Captura de pantalla del cálculo de la población por km2 mediante la calculadora de campo.
:::
::::

:::::

7. Ahora, debemos cambiar el nombre de las columnas `Indirectly Affected` y `Directly Affected` para que no contengan espacios. Esto garantiza que la calculadora de campo funcione correctamente. Para esta tarea utilizaremos la herramienta `Cambiar nombre de campo`.

:::{figure} /fig/en_ex1_Rename_field.PNG
---
width: 80%
name: es_rename_field
---
Captura de pantalla de la herramienta Renombrar campo.
:::

5. Determinemos ahora la proporción de la población afectada directa o indirectamente en relación con la población total por región.
    - Utilice la calculadora de campo. Utilice la expresión: `"Indirectly Affected" / ("Total"/100)`
    - Utilice la calculadora de campo. Utilice la expresión: `"Directly Affected" / ("Total"/100)`

:::::{tab-set}

::::{tab-item} Captura de pantalla afectados indirectamente
:::{figure} /fig/en_ex1_per_indirect_affected.PNG
---
width: 80%
name: es_per_indirect_affected
---
Cálculo de la proporción de la población indirectamente afectada en relación con la población total de cada región.
:::
::::

::::{tab-item} Captura de pantalla afectados directamente
:::{figure} /fig/en_ex1_per_direct_affected.PNG
---
width: 80%
name: per_direct_affected
---
Cálculo de la proporción de la población directamente afectada en relación con la población total de cada región.
:::
::::

:::::

6. Seleccione un esquema de colores utilizando `Simbología` para visualizar la proporción de personas directamente afectadas en las diferentes regiones (sugerencia: `Categorizado`).
    - Juegue con diferentes modos para encontrar un esquema de color/categorización útil para la visualización.
    - ¿Qué regiones están más afectadas directamente y cuáles menos? ¿Existen diferencias en los datos?

7. Exporte el mapa en formato png (sugerencia: `Proyecto, Importar/Exportar, Exportar mapa a imagen`).

8. Repita los pasos anteriores, pero esta vez visualice las personas indirectamente afectadas en cada región (sugerencia: `Categorizado`, columna `Indirectly affected`).

9. ¿Qué diferencias se observan entre las regiones directamente afectadas y las indirectamente afectadas?

