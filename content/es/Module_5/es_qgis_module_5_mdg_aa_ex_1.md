::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Estimar de la población expuesta: enfoque manual de Aina

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

Este ejercicio forma parte del [Programa de ejercicios de análisis de acción anticipatoria ante ciclones en Madagascar](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_mdg_aa_cyclones.html)

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
* [Automatización](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_automatisation_wiki.html)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Objetivo del ejercicio:__
Aina, experta en SIG de la Cruz Roja Malgache (CRM), se prepara para la próxima temporada de ciclones. Quiere mejorar la capacidad de su equipo para actuar con rapidez una vez que se pronostica una tormenta, mediante la automatización de análisis clave en QGIS. Esto incluye la estimación de las poblaciones expuestas, la identificación de los servicios afectados como la sanidad y la educación, y la evaluación de si se puede llegar a los puestos sanitarios desde los almacenes clave en un plazo crítico de 10 horas.
El objetivo es preparar un flujo de trabajo de análisis y visualización de principio a fin de que pueda respaldar una acción anticipatoria rápida y basada en datos antes de que un ciclón toque tierra.
^^^



:::

## Instrucciones para capacitadores

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

## Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_5_Exercise_8_AA_MDG_task_1-20250825T143512Z-1-001.zip


__Descargue todos los conjuntos de datos aquí, guarde la carpeta en su computadora y descomprima el archivo.__

:::



La carpeta contiene toda la [estructura de carpetas estándar](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#standard-folder-structure) con todos los datos en la carpeta de entrada y la documentación adicional en la carpeta de documentación.

| Conjunto de datos | Fuente | Descripciones |
| ----- | --- | --- |
| Límites administrativos | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Se puede acceder a los límites administrativos de nivel 0-4 para Madagascar a través del Intercambio de Datos Humanitarios (HDX) proporcionado por OCHA. Para este mecanismo de activación proporcionamos los límites administrativos de los nivel 1 (nivel regional) y 2 (nivel de distrito) en forma de archivo shapefile. |
| Trayectoria de ciclones | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) | El proyecto IBTrACS es la recopilación global más completa de ciclones tropicales que hay disponible. Combina datos recientes e históricos de ciclones tropicales de numerosos organismos para crear un conjunto de datos unificado, disponible públicamente y con la mejor trayectoria, que mejora las comparaciones entre organismos. |
| Centros educativos y de salud | [Herramienta de exportación HOT](https://export.hotosm.org/vi/v3/exports/new/describe) | Los datos de los puntos de interés (centros educativos y de salud) se descargan por medio de la herramienta de exportación HOT, que se basa en datos de OpenStreetMap. |
| Población | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | El conjunto de datos de WorldPop en formato ráster proporciona el número total estimado de personas por celda de cuadrícula para el año 2020. Trabajaremos con el conjunto de datos de países individuales con restricciones de 2020, con una resolución de 100 m. |




::::{card}
__Contexto__
^^^

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC-icons-colour_SURGE
---
:::

**Aina** es la experta en SIG de la **Cruz Roja Malgache (CRM)**. Con la inminente llegada de la temporada de ciclones, sabe que el tiempo apremia una vez que se pronostica una tormenta. Cada hora cuenta cuando se trata de proteger a las comunidades en riesgo.

Este año, Aina quiere adelantarse a los acontecimientos. En lugar de analizar manualmente los datos del ciclón bajo presión, decide **preparar un modelo QGIS automatizado** que le ayude a responder de forma rápida y eficiente.

**Su objetivo:**
> Crear un flujo de trabajo que estime automáticamente las poblaciones expuestas y la infraestructura en riesgo.

::::

:::{figure} /fig/Module_7/en_ex_m7_cylone_automatisation.drawio.png
---
name: Task_1_workflow
width: 750 px
---

:::

# Tareas:

Antes de diseñar el modelo automatizado, Aina solía estimar manualmente la población expuesta cada vez que un ciclón se acercaba a Madagascar. En esta tarea, seguirá los pasos que ella utilizó en el pasado trabajando con el registro histórico del **ciclón Harald**, los datos ráster de WorldPop y los límites administrativos.

Deberá crear manualmente un buffer de la trayectoria del ciclón, recortar el ráster de población y calcular la población expuesta utilizando estadísticas zonales.




1. **Abra QGIS** y cree un [nuevo proyecto](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) haciendo clic en `Project` -> `New`

2. **Guarde el proyecto** en la carpeta “Project”. Para ello, haga clic en `Project` -> `Save as` y vaya a la carpeta. Asigne el nombre “Cyclon_Harald_Exposure” al proyecto.

3. **Cargue el archivo GeoJOSN** "example_Harald_2025_Track.geojson" en su proyecto por medio de arrastrar y soltar ([Video Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Abra la carpeta `data` -> `input`


4. **Reproyecte la trayectoria del ciclón** para utilizar metros en lugar de grados (importante para la precisión del buffer):
   - En la **caja de herramientas de Procesos**, busque `Reproject Layer`.
   - Entrada: `example_Harald_2025_Track`
   - SRC objetivo: `EPSG:29738` u otro SRC basado en metros adecuado para Madagascar.
   - Guarde el resultado en la carpeta `temp` como: **`Harald_Track_Reprojected`**
:::{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reproyectar la trayectoria del ciclón
:::

:::{Attention}
Las distancias de buffer deben calcularse en metros. Muchos conjuntos de datos (como las trayectorias de ciclones GeoJSON) utilizan sistemas de coordenadas geográficas como EPSG:4326, que miden en grados, no en metros. Para calcular correctamente un buffer de 200 km, primero debemos reproyectar la trayectoria en un SRC proyectado que utilice metros.
:::
5. **Aplique un buffer a la trayectoria del ciclón**:
   - En la **caja de herramientas de Procesos**, busque `Buffer`.
   - Entrada: `Harald_Track_Reprojected`
   - Distancia de buffer: `200000` (metros)
   - Segmentos: Deje el valor predeterminado (5)
   - Disolver: `Yes`
   - Guarde la salida en la carpeta `temp` como: **`Harald_Buffer_200km`**
:::{figure} /fig/fr_MDG_AA_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Aplicar un buffer a la trayectoria del ciclón
:::

::::{dropdown} Resultado intermedio: Buffer
:::{figure} /fig/fr_MDG_AA_intermediate_result_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Les résultats intermédiaires doivent montrer la trajectoire du cyclone et la zone tampon de 200 kilomètres autour de celui-ci. La zone tampon doit être une seule entité.
:::
::::
6. **Reproyecte el buffer de nuevo a EPSG:4326 (para que coincida con el SRC de ráster):**
   - En la caja de herramientas de Procesos, busque "Reproject Layer".
   - Entrada: Harald_Buffer_200km_29738
   - SRC objetivo: EPSG:4326 – WGS 84
   - Guarde el resultado en la carpeta temporal como: Harald_Buffer_200km_4326
:::{figure} /fig/fr_MDG_AA_reproject_cyclon_buffer.PNG
---
width: 600px
align: center
---
Reproyectar el buffer del ciclón
:::

7. **Cargue los límites administrativos**:
   - Archivo: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Añada por medio de arrastrar y soltar o `Add Vector Layer`.
8. **Cargue el ráster de población**:
   - Archivo: `MDG_WorldPop_2020_constrained.tif`
   - Agregue usando `Layer` → `Add Raster Layer`.
9. **Recorte el ráster de población** utilizando la zona buffer de impacto:
   - En la **caja de herramientas de Procesos**, busque `Clip Raster by Mask Layer`.
   - Ráster de entrada: `MDG_WorldPop_2020_constrained`
   - Capa de máscara: `Harald_Buffer_200km`
   - Guarde la salida en la carpeta `temp` como: **`Harald_Pop_Clip`**
:::{figure} /fig/fr_MDG_AA_clip_pop_raster.PNG
---
width: 600px
align: center
---
Recortar el ráster de población con el buffer del ciclón
:::
::::{dropdown} Resultado intermedio: Recorte de Capa ráster de población
:::{figure} /fig/fr_MDG_AA_intermediate_result_clip_pop_raster.PNG
---
width: 600px
align: center
---
Resultados intermedios
:::
::::

10. **Calcular la población total expuesta**:
   - En la **caja de herramientas de Procesos**, busque `Zonal Statistics`.
   - Capa vectorial de entrada: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Capa ráster: `Harald_Pop_Clip`
   - Estadística por calcular: `Sum`
   - Prefijo de campo: p. ej., `exposed_population_`
   - Guarde la capa vectorial actualizada en la `result` carpeta como: **`Harald_Exposed_Populationg`**
   - El resultado será una nueva columna en la tabla de atributos de la capa `mdg_admbnda_adm2_BNGRC_OCHA_201810312.gpkg`, que muestra la población total dentro del buffer del ciclón por distrito.
:::{figure} /fig/fr_MDG_AA_pop_zonal_statistic.PNG
---
width: 600px
align: center
---
Calcular la población expuesta al ciclón por distrito utilizando el ráster WorldPop.
:::

11. **Visualice la población afectada clasificando los resultados**:
Ahora que Aina ha estimado la población expuesta en cada distrito, quiere mostrar claramente las diferencias entre las regiones en el mapa.
Para ello, aplicaremos una **clasificación graduada** a la capa `Harald_Exposed_Population` que ocupa el nuevo campo de población creado por la herramienta de estadísticas zonales.
- En el **panel de capas**, haga clic con el botón derecho en la capa `Harald_Exposed_Population` y elija `Properties`.
- Vaya a la pestaña **Symbology** a la izquierda.
- En la parte superior de la ventana, cambie el estilo de `Single Symbol` a `Graduated`.
- En el menú desplegable de **Value**, seleccione el campo que contiene la suma de la población. Normalmente comienza con el prefijo que determinó anteriormente, por ejemplo `exposed_population_sum`.
- Configure la **rampa de color** a uno que sea adecuado para su mapa (por ejemplo `Reds`).
- Elija un **modo de clasificación** (por ejemplo, `Quantile`, `Natural Breaks` o `Equal Interval`) y seleccione el número de clases (por ejemplo, 5).
- Haga clic en `Classify` para generar la clasificación.
- Haga clic en `Apply` y luego en `OK` para visualizar el mapa clasificado.

:::{tip}
Puede ajustar los límites o etiquetas de las clases haciendo doble clic en cada entrada de clase.
:::

:::{figure} /fig/fr_MDG_AA_pop_graduadt_classification_exposed_population.PNG
---
width: 600px
align: center
---
Clasificar la población expuesta en cinco clases.
:::

# Resultados

Sus resultados deberían tener un aspecto similar a este:

:::{figure} /fig/fr_MDG_AA_intermediate_result_visualisation_exposed_population.PNG
---
width: 600px
name: the_world_result
align: center
---
Visualizar las 5 clases.
:::
