::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 2: Automatización de la estimación de la población expuesta: el modelo de Aina

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

Este ejercicio forma parte del [Programa de ejercicios para el análisis de acción anticipatoria de ciclones en Madagascar.](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_mdg_aa_cyclones.html)

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
Aina, experta en SIG de la Cruz Roja Malgache (CRM), se prepara para la próxima temporada de ciclones. Quiere mejorar la capacidad de su equipo para actuar con rapidez una vez pronosticada una tormenta automatizando los análisis clave en QGIS. Esto incluye la estimación de las poblaciones expuestas, la identificación de los servicios afectados como la sanidad y la educación, y la evaluación de si se puede llegar a los puestos sanitarios desde los almacenes clave en un plazo crítico de 10 horas.
El objetivo es preparar un flujo de trabajo de análisis y visualización de principio a fin que pueda respaldar una acción anticipatoria rápida y basada en datos antes de que un ciclón toque tierra.
^^^



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




Tras estimar manualmente las poblaciones expuestas en temporadas ciclónicas anteriores, Aina decidió preparar un **modelo automatizado** utilizando el **modelador gráfico QGIS**. Esto la ayudará a actuar con mayor rapidez y evitar la repetición manual de los mismos pasos cada vez que se prevea un ciclón.

En esta tarea, ayudarás a Aina a construir una versión sencilla de ese modelo utilizando las herramientas de la Tarea 1. El modelo debe:

- Reproyectar la trayectoria del ciclón a EPSG:29738
- Buffer de la trayectoria del ciclón
- Reproyectar el buffer de nuevo en EPSG:4326
- Recortar el ráster de población
- Ejecutar las estadísticas zonales para obtener la población expuesta por distrito

---


## Tareas
1. **Configuración de la estructura del modelo**:
   - Abra el **Modelador gráfico** desde el menú superior: 
   `Procesos` → `Diseñador de modelos`

2. **Denominación del modelo**:
   - Se abrirá una nueva ventana de modelo. En la **parte izquierda**, haga clic en **`Propriedades del modelo`** para definir la información básica sobre el modelo:
     - **Nombre del modelo**: `Estimación_Población_Expuesta`
     - **Grupo**: `Herramientas de Activación Ante Ciclones`
     - Deje el campo de la descripción en blanco o escriba: _“Modelo automatizado para estimar la población expuesta en función de la zona de influencia del ciclón”._

3. **Guarde el modelo**
   - Para guardar el modelo:
     - Haga clic en el icono **Guardar** (💾) o vaya a `Modelo` → `Guardar modelos`.
     - Navegue hasta la **carpeta `modelos`** de su estructura de capacitación.
     - Guarde el modelo como: 
     **`Estimación_Población_Expuesta`** e añada la fecha (por ejemplo: 250916)

4. **Añadir entradas del modelo**:
   - En el **panel izquierdo**, expanda la sección **Entradas**.
   - Añada las siguientes capas de entrada con restricciones de tipo:
     - `+ Capa vectorial`
       - **Etiqueta**: `Trayectoria del ciclón`
       - En el **panel avanzado**, configure el **tipo de geometría** en `Línea`
     - `+ Capa Ráster`
       - **Etiqueta**: `Raster de población`
     - `+ Capa vectorial`
       - **Etiqueta**: `límites administrativos`
       - En el **panel avanzado**, configure el **tipo de geometría** en `Polígono`
   - Aparecerán en la parte superior del lienzo del modelo y servirán como datos de entrada cuando se ejecute el modelo.

     :::{tip}
     Todas las entradas deben configurarse como **obligatorio**, de modo que el modelo siempre reciba los datos necesarios para funcionar correctamente.
     :::

:::::{tab-set}

::::{tab-item} Entrada Trayectoria del ciclón
:::{figure} /fig/fr_MDG_AA_model_input_cyclon_track.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Trayectoria del ciclón
:::
::::

::::{tab-item} Entrada de límites administrativos
:::{figure} /fig/fr_MDG_AA_model_input_admin_bounderies.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Límites administrativos
:::
::::

::::{tab-item} Ráster de población
:::{figure} /fig/fr_MDG_AA_model_input_population_raster.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
:::
::::
:::::

**Resultado intermedio**

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_input.PNG
---
width: 600px
name: the_world_result
align: center
---
Résultat intermédiaire de la définition des données d'entrée du modèle
:::

5. **Reproyección de la trayectoria del ciclón a EPSG:29738**
   - En el panel **Algoritmos**, busque la **Reproyectar capa**.
   - En la ventana de configuración:
     - Añada una descripción: `Reprojectar la capa de la trayectoria del ciclón a EPSG : 29738`
     - Configure la **Capa de entrada** a `Trayectoria del ciclón` (desde **Entrada del modelo**).
     - Configure **SRC de destino** a `EPSG:29738 – Madagascar / Laborde Grid`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en **Aceptar** para añadir el paso al modelo.
:::{figure} /fig/fr_MDG_AA_model_reporject_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reproyectar la capa de trayectoria del ciclón a un sistema de referencia de coordenadas métrico (SRC/CRS) EPSG:29738
:::
6. **Crear un buffer de la trayectoria del ciclón reproyectada**
   - En el panel **Algoritmos**, busque **Buffer**.
   - En la ventana de configuración:
    - Añada una descripción: `Generar un buffer de la capa de ciclón reproyectada`
     - Añada una descripción:
     - Configure **Capa de entrada** en la salida del paso anterior (desde **Algoritmo de salida**).
     - Configure **Distancia** en `200000` (200 km).
     - Deje **Segmentos** en el valor predeterminado (`5`).
     - Configure **Dissolver Resultado** en `Si`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en **Aceptar** para añadir el paso al modelo.
:::{figure} /fig/fr_MDG_AA_model_buffer_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Generar un buffer de la capa de ciclón reproyectada.
:::
7. **Reproyectar la amortiguación de vuelta en EPSG:4326**
   - En el panel **Algoritmos**, busque **Reproyectar capa**.
   - En la ventana de configuración:
    - Añada una descripción: `Reprojectar el buffer al SRC EPSG:4326`
   - En la ventana de configuración:
     - Configure **Capa de entrada** en la salida del paso anterior (desde **Algoritmo de salida**).
     - Configure **SRC de destino** a `EPSG:4326 – WGS 84`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en **Aceptar** para añadir el paso al modelo.
:::{figure} /fig/fr_MDG_AA_model_reporject_bufferd_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojectar el buffer al SRC EPSG:4326
:::
8. **Recorte el ráster de población utilizando el área amortiguada.**
   - En el panel **Algorithms**, busque **Cortar ráster por capa de máscara**.
   - En la ventana de configuración:
     - Añada una descripción: `Cortar la capa ráster de población para ajustarla al buffer del ciclón`
   - En la ventana de configuración:
     - Configure la **Capa de entrada** a `Raster de población` (desde **Entrada del modelo**).
     - Configure la **Capa de máscara** en la salida del paso anterior (de **Salida del algoritmo**).
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en **Aceptar** para añadir el paso al modelo.
   :::{figure} /fig/fr_MDG_AA_model_clip_pop_raster.PNG
---
width: 600px
name: the_world_result
align: center
---
Cortar la capa ráster de población para ajustarla al buffer del ciclón
:::
9. **Calcule las estadísticas zonales para estimar la población expuesta.**
   - En el panel **Algorithms**, busque **Estadísticas de zona**.
   - En la ventana de configuración: Cálculo de la población expuesta a ciclones por distrito
     - Añada una descripción: `Cálculo de la población expuesta a los ciclones por distrito`
     - Configure la **Capa de entrada** a `limites administrativas` (desde **Entrada del modelo**).
     - Configure **Capa de ráster** en la salida del paso anterior (desde **Salida del algoritmo**).
     - Configure **Prefijo de columna de salida** en `población_expuesta_`.
     - En **Estadísticas para calcular**, seleccione `Suma`.
     - Configure la salida en **Modelo de salida** y asígnele un nombre:
      ```
      población_expuesta_suma
      ```
   - Haga clic en `Ok` para añadir el paso al modelo.
:::{figure} /fig/fr_MDG_AA_model_zonal_statistic_pop_admin2.PNG
---
width: 600px
name: the_world_result
align: center
---
Cálculo de la población expuesta a ciclones por distrito
:::

**Los resultados deberían ser parecidos a los siguientes:**

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms.PNG
---
width: 600px
name: the_world_result
align: center
---
Su modelo debería verse así. Todos los algoritmos están correctamente conectados y la salida del modelo está definida.
:::

10. **Valide su modelo (recomendado)**
   - Antes de guardar o ejecutar, haga clic en el botón ✔️ **Validar modelo** en la barra de herramientas superior.
   - Corrija cualquier advertencia o error que aparezca en el panel de registro.
   - Esto ayuda a garantizar que el modelo esté completo y no se rompa durante la ejecución.

11. **Ejecute el modelo**
   - Ejecute el modelo haciendo clic en `Modelo` -> `Ejectar Modelo`
   - Configure **Límites administrativos** en `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Configure **Trayectoria del ciclón** en `example_Harald_2025_Track`
   - Configure **Ráster de población** en `MDG_WorldPop_2020_constrained.tif`
   - Configure la salida del modelo **exposed_population_sum** en `Harald_Exposed_Population`y guárdela en `data` -> `output`


Ahora puede ejecutar este modelo cada vez que esté disponible una nueva trayectoria de ciclón.

:::{figure} /fig/fr_MDG_AA_model_run_model_M7_e1_task2.PNG
---
width: 600px
name: the_world_result
align: center
---
Para ejecutar el modelo, especifique la entrada tal y como se muestra en la imagen y defina el nombre de la casilla de salida.
:::

**Los resultados deberían ser parecidos a los siguientes:**
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_basics.PNG
---
width: 600px
name: the_world_result
align: center
---

:::
12. **Añada la amortiguación del ciclón como salida del modelo adicional**
   - Haga doble clic en el algoritmo del paso 7 (**Reproyectar el buffer de nuevo a EPSG:4326**) para abrir su configuración.
   - En el campo **Capa de salida**, marque la casilla **Salida del modelo**.
   - Asigne un nombre claro al resultado, por ejemplo:
     ```
     cyclone_harald_buffer
     ```
   - Haga clic en **Aceptar** para guardar el cambio.
   - Esto permitirá que el modelo genere tanto los resultados de la población expuesta como la zona buffer de impacto del ciclón cuando se ejecute.

:::{figure} /fig/fr_MDG_AA_model_output_buffer.PNG
---
width: 600px
name: the_world_result
align: center
---
:::

13. **Ejecute el modelo otra vez**
   - Ejecute el modelo haciendo clic en `Modelo` -> `Ejecutar Modelo`
   - Configure **Límites administrativos** en `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Configure **Trayectoria del ciclón** en `example_Harald_2025_Track`
   - Configure **Ráster de población** en `MDG_WorldPop_2020_constrained.tif`
   - Configure la salida del modelo **cyclone_harald_buffer** en `cyclone_harald_buffer`y guárdela en `data` -> `output`
   - Configure la salida del modelo **exposed_population_sum** en `Harald_Exposed_Population`y guárdela en `data` -> `output`


:::::{tab-set}


::::{tab-item} Buffer de salida del modelador gráfico

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_graphic.PNG
---
width: 600px
name: the_world_result
align: center
---
:::
Definición de la entrada del modelo: Límites administrativos
::::

::::{tab-item} Ejecute modelo con salida de buffer
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_model_exicution.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
:::
::::

::::{tab-item} Salida del modelo
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_extended_buffer.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
:::
::::

:::::

