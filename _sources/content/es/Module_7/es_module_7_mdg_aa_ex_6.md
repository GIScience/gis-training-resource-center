::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 6: Exportación de resultados de modelos para el equipo de operaciones

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}
__Programa de ejercicios:__

Este ejercicio forma parte del [programa de ejercicios de análisis de ciclones de acción anticipatoria de Madagascar.](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_mdg_aa_cyclones.html)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^


:::

:::{grid-item-card}
__Artículos relevantes en Wiki__
^^^

* [Estadísticas zonales](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_raster_basic_wiki.html)
* [Intersección](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Buffer](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Recorte](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Automatización](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_automation_wiki.html)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Objetivo del ejercicio:__
^^^
Aina, experta en SIG de la Cruz Roja Malgache (CRM), se prepara para la próxima temporada de ciclones. Quiere mejorar la capacidad de su equipo para actuar con rapidez una vez pronosticada una tormenta automatizando los análisis clave en QGIS. Esto incluye la estimación de las poblaciones expuestas, la identificación de los servicios afectados como la sanidad y la educación, y la evaluación de si se puede llegar a los puestos sanitarios desde los almacenes clave en un plazo crítico de 10 horas.
El objetivo es preparar un flujo de trabajo de análisis y visualización de principio a fin que pueda respaldar una acción anticipatoria rápida y basada en datos antes de que un ciclón toque tierra.

:::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede tratarse de una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra virtual de Miro) en la que los participantes pueden añadir sus hallazgos y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y, hayan descargado __y descomprimido__ la carpeta de datos.
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

## Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_7_Exercise_4_AA_MDG_task_6-20250825T143514Z-1-001.zip

__Descargue todos los conjuntos de datos aquí, guarde la carpeta en su ordenador y descomprima el archivo.__
:::

**Contexto: Aina apoya a los responsables de la toma de decisiones**

Después de producir mapas y elementos visuales, Aina a menudo recibe solicitudes del equipo de operaciones:
 _“Puede enviarnos los datos en formato de tabla?”_

En lugar de exportar estas tablas manualmente cada vez, Aina quiere automatizar este paso dentro de su modelo, asegurando que cada ejecución del modelo produzca archivos de datos claros y listos para usar.

En esta tarea, ayudará a Aina a ampliar su modelo para exportar capas seleccionadas.

Uniremos las siguientes capas paso a paso:

- `adm2_centros_salud_expuestos`: 
  Contiene el **número total de centros de salud**, el **número de centros de salud afectados** y el **porcentaje de centros de salud** afectados.

- `adm2_educación_expuesta`: 
  Contiene el **número total de instalaciones educativas**, el **número de instalaciones educativas afectadas** y el **porcentaje de instalaciones educativas afectadas**.

- `población_expuesta_suma`: 
  Contiene la **población total por distrito** y la **población expuesta** de la etapa de estadísticas zonales.

---

# Tareas


1. Abra su modelo
- `Estimación_Población_Expuesta_establecimientos_salud_y_educativas.model3`
- Guarde una nueva versión como:
  ```
  Estimate_Exposed_Population_Health_Education_Spreadsheet_Export
  ```
2. Una los datos de salud y educación en una sola capa
- En los **Algoritmos**, busque `Unir atributos por valor de campo`.
- Añada una descripción: `Unir datos de salud y educación en una sola capa por ADM2.`
- Configure el algoritmo de la siguiente manera:
  - **Capa de entrada**: `adm2_centros_salud_expuestos` (seleccionar de **Salida de algoritmo**)
  - **Capa de entrada 2**: `adm2_educación_expuesta` (seleccione de **Salida de algoritmo**)
  - **Campo de tabla**:
   ```
   ADM2_PCODE
   ```
  - **Campo de tabla 2**:
   ```
   ADM2_PCODE
   ```
   - **Campos de capa 2 para copiar**: Deje vacío (todos los campos serán copiados)
   - **Tipo de unión**: Tome los atributos de la primera característica coincidente solamente (uno a uno)
   - Deje la salida como **Salida del modelo**

:::{figure} /fig/fr_MDG_AA_model_join_affacted_pop.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuración de la operación: unir los datos de salud y educación mediante el campo ADM2_PCODE para combinar los resultados en una sola capa.
:::
3. Unir el resultado con los datos de población
Ahora, una el resultado del paso anterior (salud + educación) a los datos de **población expuestos**.
- Añada un segundo algoritmo `Unir atributos por valor de campo` al modelo
- Añada una descripción: `Unir los datos de población con los indicadores de salud y educación`
- Configure el algoritmo de la siguiente manera:
  - **Capa de entrada**: `población_expuesta_suma` (seleccionar de **Salida de algoritmo** del paso Estadísticas zonales)
  - **Capa de entrada 2**: Producto del Paso 2 (salud + educación)
  - **Campo de tabla**:
   ```
   ADM2_PCODE
   ```
  - **Campo de tabla 2**:
   ```
   ADM2_PCODE
   ```
  - **Campos de capa 2 para copiar**: *(Ingrese los siguientes nombres de campo exactamente como se muestra, separados por comas, sin espacios)*
    ```
    Total_centros_salud;Total_establc_educativas;sum_centros_salud_expuestas;sum_education_expuesta;pct_expuesto_centros_salud;pct_expuesto_educación
    ```
   - **Tipo de unión**: Tome los atributos de la primera característica coincidente solamente (uno a uno)
   - Deje la salida como **Salida del modelo**

:::{admonition} Los nombres de las columnas en el modelo
:class: tip
Si la capa resultante no contiene estas columnas, o las columnas están vacías, __abra los algoritmos individuales__ en su modelo y verifique cómo ha nombrado las columnas.
También se pueden encontrar en las __tablas de atributos__ de las salidas del modelo.

:::

:::{figure} /fig/fr_MDG_AA_model_join_affacted_pop_HS_ES.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuración de la operación: unir los datos de población con los indicadores de salud y educación.
:::

::::{warning} Los espacios invisibles romperán la union. 
Si un nombre de columna como `count_health_total` tiene un espacio final invisible, la unión fallará silenciosamente. 
Copie siempre los nombres de los campos **directamente de la tabla** de atributos para evitar errores.
::::


4. Exporte resultados a una hoja de cálculo
- En la **caja de herramientas**, busque `Exportar a hoja de cálculo` y haga doble clic para abrir.
- Añada una descripción: `Exportar los datos de población, educación y salud en una sola tabla`
- Configure la herramienta de la siguiente manera:
  - **Capa de entrada**: Seleccione la salida del Paso 3 de **Salida de algoritmo**
  - **Hoja de cálculo**:
    ```
    tabla_de_indicadores_de_exposición
    ```

  - Haga clic en `Aceptar` para agregarlo al modelo.
Una vez que ejecute el modelo, este paso generará automáticamente una hoja de cálculo con todos los indicadores relevantes listos para el equipo de operaciones.

:::{figure} /fig/fr_MDG_AA_model_export_as_table.PNG
---
width: 600px
name: fr_MDG_AA_model_export_as_table
align: center
---
Exportar todos los indicadores (población, salud, educación) a una única tabla en formato de hoja de cálculo.
:::



5. **Valide su modelo ampliado y guárdelo.**
   - Haga clic en el botón ✔️ **Validate Model** para verificar si hay errores.
   - Guarde de nuevo en: 
   **`Estimación_Población_Expuesta_Salud_Educación.model3`** (también puedes __añadir el número de versión o la fecha al nombre del archivo__.)
6. **Ejecute el modelo**
   - Haga clic en el botón ▶️ **Run** en la esquina superior derecha de la ventana del modelador gráfico.
   - **Entrada:**
     - Haga clic en los tres puntos de cada conjunto de datos de entrada y seleccione la entrada correcta:
       - `Cyclone Track` → seleccione el GeoJSON de la trayectoria de la tormenta (por ejemplo, `Harald_2025_Track.geojson`).
       - `Ráster de población` → seleccione el archivo ráster WorldPop
       - `Limites administrativos` → seleccione la capa Admin 2 (por ejemplo, `MDG_adm2.gpkg`)
       - `Centros de salud` → seleccione el conjunto de datos de puntos para los centros de salud.
       - `Establecimientos educativos` → seleccione el conjunto de datos de puntos para las escuelas
   - **Salida:**
     - Guarde todas las capas de salida en la carpeta de salida y utilice los nombres que se indican a continuación.
       - `adm2_centros_salud_expuestos` -> 
        ```
        adm2_centros_salud_expuestos
        ```
       - `adm2_educación_expuesta` ->
        ```
        adm2_educación_expuesta
        ```
       - `trayectoria_harald_buffer` -> 
        ```
        trayectoria_harald_buffer
        ```
       - `población_expuesta_suma` ->
        ```
        población_expuesta_suma_harald
        ```
       - `tabla_de_indicadores_de_exposición` ->
        ```
        tabla_de_indicadores_de_exposición
        ```
   - Haga clic en **Ejecutar** para ejecutar el modelo completo.

:::::{tab-set}

::::{tab-item} Modelador gráfico

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task_6_export_spreadsheet__model.PNG
---
width: 600px
align: center
---
Vista del modelador gráfico con la etapa de exportación a una tabla añadida al modelo
:::
::::
::::{tab-item} Configuración del modelo de ejecución
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_run_configurations.PNG
---
width: 600px
align: center
---
Ventana de configuración para ejecutar el modelo con la opción de exportación a una tabla
:::
::::
::::{tab-item} Salida del modelo
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_results_AT.PNG
---
width: 600px
align: center
---
Resultados finales del modelo exportados en una tabla lista para usar.
:::
::::
:::::

---



