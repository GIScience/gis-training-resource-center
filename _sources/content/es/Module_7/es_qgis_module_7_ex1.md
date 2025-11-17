::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Ejercicios 1: Automatización

🚧¡Esta parte de la plataforma de capacitación está en ⚠️construcción⚠️ y no se puede compartir ni publicar! 🚧

## Características del ejercicio



::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}


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

## Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip

__Descargue todos los conjuntos de datos [aquí](), guarde la carpeta en su computadora y descomprima el archivo.__

:::

La carpeta se llama “ y contiene toda la [estructura de carpetas estándar](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#standard-folder-structure) con todos los datos de la carpeta de entrada y la documentación adicional en la carpeta de documentación.

| Conjunto de datos | Fuente | Descripciones |
| ----- | --- | --- |
| Límites administrativos | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Se puede acceder a los límites administrativos de nivel 0-4 para Madagascar a través del Intercambio de Datos Humanitarios (HDX) proporcionado por OCHA. Para este mecanismo de activación, proporcionamos los límites administrativos en los niveles 1 (nivel regional) y 2 (nivel de distrito) como un shapefile. |
| Trayectoria de ciclones | [Archivo internacional del mejor programa para la administración del clima (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive) | El proyecto IBTrACS es la colección global más completa de ciclones tropicales disponible. Combina datos recientes e históricos de ciclones tropicales de numerosos organismos para crear un conjunto de datos unificado, disponible públicamente y con la mejor trayectoria, que mejora las comparaciones entre organismos. |
| Centros educativos y centros de salud | [Herramienta de exportación HOT](https://export.hotosm.org/vi/v3/exports/new/describe) | Los datos de POI (instalaciones educativas y centros de salud) se descargan utilizando la herramienta de exportación HOT basada en datos de OpenStreetMap. |
| Población | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | El conjunto de datos worldpop en formato ráster proporciona el número total estimado de personas por celda de cuadrícula para el año 2020. Trabajaremos con el conjunto de datos de países individuales restringidos 2020 con una resolución de 100 m. |




:::{card}
__Contexto__
^^^

```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

**Aina** es la experta en SIG en el **Croix-Rouge Malagasy (CRM)**. Con la temporada de ciclones acercándose, sabe que el tiempo es esencial una vez que se pronostica una tormenta. Cada hora cuenta cuando se trata de proteger a las comunidades en riesgo.

Este año, Aina quiere adelantarse a los acontecimientos. En lugar de analizar manualmente los datos de ciclones bajo presión, decide **preparar un modelo QGIS automatizado** que la ayudará a responder de manera rápida y eficiente.

**Su objetivo:**
> Crear un flujo de trabajo que calcule automáticamente las poblaciones expuestas y la infraestructura en riesgo.

:::

```{figure} /fig/Module_7/en_ex_m7_cylone_automatisation.drawio.png
---
name: Task_1_workflow
width: 750 px
---

```

## Tarea 1: Estimación de la población expuesta: el enfoque manual de Aina

Antes de desarrollar el modelo automatizado, Aina solía estimar la población expuesta manualmente cada vez que un ciclón se acercaba a Madagascar. En esta tarea, seguirá los pasos que usó en el pasado trabajando con la trayectoria histórica del **Ciclón Harald**, datos ráster de WorldPop y límites administrativos.

Deberá crear manualmente una zona de amortiguación para la trayectoria del ciclón, recortar el ráster de población y calcular la población expuesta mediante estadísticas zonales.




1. **Abra QGIS** y cree un [Nuevo proyecto](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) haciendo clic en `Project` -> `New`

2. **Guarde el proyecto** en la carpeta "proyecto". Para ello, haga clic en `Project` -> `Save as` y navegue hasta la carpeta. Asigne el nombre “Cyclon_Harald_Exposure”.

3. **Cargue el GeoJOSN** archivo "example_Harald_2025_Track.geojson" en su proyecto arrastrando y soltando ([Video de Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Abra la carpeta `data` -> `input`


4. **Reproyectar la trayectoria del ciclón** para usar metros en lugar de grados (importante para una amortiguación precisa):
   - En **Caja de herramientas de procesamiento**busque `Reproject Layer`.
   - Entrada: `example_Harald_2025_Track`
   - CRS objetivo: `EPSG:29738` u otro SRI basado en medidores apropiado para Madagascar.
   - Guarde el resultado en el archivo `temp` carpeta como: **`Harald_Track_Reprojected`**
```{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reprojetter la trajectoire du cyclone
```

```{Attention}
Las distancias de zona de amortiguación deben calcularse en metros. Muchos conjuntos de datos (como las trayectorias de ciclones GeoJSON) utilizan sistemas de coordenadas geográficas como EPSG:4326, que miden en grados, no en metros. Para calcular correctamente un amortiguador de 200 km, primero debemos reproyectar el programa en un CRS proyectado que use metros.
```
5. **Amortiguación de la trayectoria del ciclón**:
   - En **Caja de herramientas de procesamiento**busque `Buffer`.
   - Entrada: `Harald_Track_Reprojected`
   - Distancia del amortiguador: `200000` (metros)
   - Segmentos: Dejar por defecto (5)
   - Disolver: `Yes`
   - Guarde la salida en el archivo `temp` carpeta como: **`Harald_Buffer_200km`**
```{figure} /fig/fr_MDG_AA_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Tamponner la trajectoire du cyclone
```

:::{dropdown} Resultado intermedio: Amortiguación
```{figure} /fig/fr_MDG_AA_intermediate_result_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Les résultats intermédiaires doivent montrer la trajectoire du cyclone et la zone tampon de 200 kilomètres autour de celui-ci. La zone tampon doit être une seule entité.
```
:::
6. **Vuelva a proyectar la zona de amortiguación en EPSG:4326 (para que coincida con el CRS del ráster):**
   - En la caja de herramientas de procesamiento, busque Reproyectar capa.
   - Entrada: Harald_Buffer_200km_29738
   - CRS objetivo: EPSG:4326 – WGS 84
   - Guarde la salida en la carpeta temporal como: Harald_Buffer_200km_4326
```{figure} /fig/fr_MDG_AA_reproject_cyclon_buffer.PNG
---
width: 600px
align: center
---
Reprojetter la tamponner trajectoire du cyclone
```

7. **Carga de los límites administrativos**:
   - Archivo: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Agregue usando arrastrar y soltar o `Add Vector Layer`.
8. **Cargar el ráster de población**:
   - Archivo: `MDG_WorldPop_2020_constrained.tif`
   - Agregue usando `Layer` → `Add Raster Layer`.
9. **Recorte el ráster de población** usando la zona de impacto amortiguada:
   - En **Caja de herramientas de procesamiento**busque `Clip Raster by Mask Layer`.
   - Ráster de entrada: `MDG_WorldPop_2020_constrained`
   - Capa de máscara: `Harald_Buffer_200km`
   - Guarde la salida en el archivo `temp` carpeta como: **`Harald_Pop_Clip`**
```{figure} /fig/fr_MDG_AA_clip_pop_raster.PNG
---
width: 600px
align: center
---
Découpez la population ratser selon la zone affectée par le cyclone (trajectoire tampon du cyclone)
```
:::{dropdown} Resultado intermedio: Recorte de Capa ráster de población
```{figure} /fig/fr_MDG_AA_intermediate_result_clip_pop_raster.PNG
---
width: 600px
align: center
---
Résultat intermédiaire du découpage de la couche raster de population à l'étendue de la trajectoire tamponnée du cyclone.
```
:::

10. **Calcular la población total expuesta**:
   - En **Caja de herramientas de procesamiento**busque `Zonal Statistics`.
   - Capa vectorial de entrada: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Capa ráster: `Harald_Pop_Clip`
   - Estadística por calcular: `Sum`
   - Prefijo de campo: p. ej., `exposed_population_`
   - Guarde la capa vectorial actualizada en la `result` carpeta como: **`Harald_Exposed_Populationg`**
   - El resultado será una nueva columna en la tabla de atributos de la `mdg_admbnda_adm2_BNGRC_OCHA_201810312.gpkg` capa, que muestra la población total dentro de la zona de amortiguación del ciclón por distrito.
```{figure} /fig/fr_MDG_AA_pop_zonal_statistic.PNG
---
width: 600px
align: center
---
Calcul de la population exposée aux cyclones par district sur la base du raster de population.
```

11. **Visualizar la población afectada clasificando los resultados**:
Ahora que Aina calculó la población expuesta en cada distrito, quiere mostrar claramente las diferencias entre regiones en el mapa.
Para ello, aplicaremos una **clasificación graduada** a la `Harald_Exposed_Population` capa con el nuevo campo de población creado por la herramienta Estadísticas zonales.
- En el **panel Capas**, haga clic con el botón derecho en la capa `Harald_Exposed_Population` y seleccione `Properties`.
- Vaya a la pestaña **Simbología** a la izquierda.
- En la parte superior de la ventana, cambie el estilo de `Single Symbol` a `Graduated`.
- En **Valor**, seleccione el campo que contiene la suma de la población. Por lo general, comienza con el prefijo que definió anteriormente, p. ej. `exposed_population_sum`.
- Configure el parámetro **Rampa de color** en uno que se adapte a su mapa (p. ej. `Reds`).
- Elija un **Modo de clasificación** (p. ej. `Quantile`, `Natural Breaks`o `Equal Interval`) y seleccione el número de clases (p. ej., 5).
- Haga clic en`Classify` para generar la clasificación.
- Haga clic en `Apply` y luego en `OK` para mostrar el mapa clasificado.

```{tip}
Puede ajustar los límites o las etiquetas de clase haciendo doble clic en cada entrada de clase.
```
```{figure} /fig/fr_MDG_AA_pop_graduadt_classification_exposed_population.PNG
---
width: 600px
align: center
---
Configuración de la visualización de la población expuesta en cinco clases.
```

Sus resultados deberían verse así:

```{figure} /fig/fr_MDG_AA_intermediate_result_visualisation_exposed_population.PNG
---
width: 600px
name: the_world_result
align: center
---
Visualisation de la population exposée en cinq classes.
```


## Tarea 2: Automatización de la estimación de la población expuesta: el modelo de Aina

Tras estimar manualmente las poblaciones expuestas en temporadas ciclónicas anteriores, Aina decidió preparar un **modelo automatizado** utilizando el **modelador gráfico QGIS**. Esto la ayudará a actuar con mayor rapidez y evitar la repetición manual de los mismos pasos cada vez que se prevea un ciclón.

En esta tarea, ayudarás a Aina a construir una versión sencilla de ese modelo utilizando las herramientas de la Tarea 1. El modelo debe:

- Reproyectar la trayectoria del ciclón a EPSG:29738
- Buffer de la trayectoria del ciclón
- Reproyectar el buffer de nuevo en EPSG:4326
- Recortar el ráster de población
- Ejecutar las estadísticas zonales para obtener la población expuesta por distrito

---

1. **Configuración de la estructura del modelo**:
   - Abra el **Modelador gráfico** desde el menú superior: 
     `Processing` → `Graphical Modeler…`

2. **Denominación del modelo**:
   - Se abrirá una nueva ventana de modelo. En la **parte izquierda**, haga clic en **`Model Properties`** para definir la información básica sobre el modelo:
     - **Nombre del modelo**: `Estimate_Exposed_Population`
     - **Grupo**: `Cyclone Trigger Tools`
     - Deje el campo de la descripción en blanco o escriba: _“Modelo automatizado para estimar la población expuesta en función de la zona de influencia del ciclón”._

3. **Guarde el modelo**
   - Para guardar el modelo:
     - Haga clic en el icono **Guardar** (💾) o vaya a `Model` → `Save`.
     - Navegue hasta la **`models`carpeta** de su estructura de capacitación.
     - Guarde el modelo como: 
       **`Estimate_Exposed_Population`**

4. **Añadir entradas del modelo**:
   - En el **panel izquierdo**, expanda la sección **Entradas**.
   - Añada las siguientes capas de entrada con restricciones de tipo:
     - `+ Vector Layer`
       - **Etiqueta**: `Cyclone Track`
       - En el **panel avanzado**, configure el **tipo de geometría** en `Line`
     - `+ Raster Layer`
       - **Etiqueta**: `Population Raster`
     - `+ Vector Layer`
       - **Etiqueta**: `Admin Boundaries`
       - En el **panel avanzado**, configure el **tipo de geometría** en `Polygon`
   - Aparecerán en la parte superior del lienzo del modelo y servirán como datos de entrada cuando se ejecute el modelo.

     ```{tip}
     Todas las entradas deben establecerse como **obligatorias**, para que el modelo siempre reciba los datos necesarios para ejecutarse correctamente.
     ```

::::{tab-set}

:::{tab-item} Entrada Trayectoria del ciclón
```{figure} /fig/fr_MDG_AA_model_input_cyclon_track.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Trayectoria del ciclón
```
:::

:::{tab-item} Entrada de límites administrativos
```{figure} /fig/fr_MDG_AA_model_input_admin_bounderies.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Límites administrativos
:::

:::{tab-item} Ráster de población
```{figure} /fig/fr_MDG_AA_model_input_population_raster.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
```
:::
::::
**Resultado intermedio**

```{figure} /fig/fr_MDG_AA_intermediate_result_model_input.PNG
---
width: 600px
name: the_world_result
align: center
---
Résultat intermédiaire de la définition des données d'entrée du modèle
```

5. **Reproyección de la trayectoria del ciclón a EPSG:29738**
   - En el panel **Algoritmos**, busque la **Capa de reproyección**.
   - En la ventana de configuración:
     - Añada una descripción: `Reprojecter la couche de trajectoire du cyclone a EPSG : 29738`
     - Configure la **Capa de entrada** a `Cyclone Track` (desde **Entrada del modelo**).
     - Configure **SRC de destino** a `EPSG:29738 – Madagascar / Laborde Grid`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en **Aceptar** para añadir el paso al modelo.
```{figure} /fig/fr_MDG_AA_model_reporject_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter la couche de trajectoire du cyclone vers un système de référence de coordonnées métrique (CRS) EPSG : 29738
```
6. **Amortiguación de la trayectoria del ciclón reproyectada**
   - En el panel **Algoritmos**, busque **Buffer**.
   - En la ventana de configuración:
    - Añada una descripción: `Mettre en mémoire tampon la couche Cyclone reprojetée`
     - Añada una descripción:
     - Configure **Capa de entrada** en la salida del paso anterior (desde **Algoritmo de salida**).
     - Configure **Distancia** en `200000` (200 km).
     - Deje **Segmentos** en el valor predeterminado (`5`).
     - Configure **Resultado de disolución** en `Yes`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en ``Ok`` para añadir el paso al modelo.
```{figure} /fig/fr_MDG_AA_model_buffer_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Mettre en mémoire tampon la couche Cyclone reprojetée
```
7. **Reproyectar la amortiguación de vuelta en EPSG:4326**
   - En el panel **Algoritmos**, busque **Reproyectar capa**.
   - En la ventana de configuración:
    - Añada una descripción: `Reprojecter le tampon vers EPSG:4326`
   - En la ventana de configuración:
     - Configure **Capa de entrada** en la salida del paso anterior (desde **Algoritmo de salida**).
     - Configure **SRC de destino** a `EPSG:4326 – WGS 84`.
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en ``Ok`` para añadir el paso al modelo.
```{figure} /fig/fr_MDG_AA_model_reporject_bufferd_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter le tampon vers EPSG:4326
```
8. **Recorte el ráster de población utilizando el área amortiguada.**
   - En el panel **Algorithms**, busque **Clip Raster by Mask Layer**.
   - En la ventana de configuración:
     - Añada una descripción: `Découper la couche raster de population pour l'étendre au tampon Cyclon`
   - En la ventana de configuración:
     - Configure la **Capa de entrada** a `Population Raster` (desde **Entrada del modelo**).
     - Configure la **Capa de máscara** en la salida del paso anterior (de **Salida del algoritmo**).
     - Configure la salida como **Salida del modelo** (deje el nombre de la salida **en blanco** ).
   - Haga clic en ``Ok`` para añadir el paso al modelo.
```{figure} /fig/fr_MDG_AA_model_clip_pop_raster.PNG
---
width: 600px
name: the_world_result
align: center
---
Découper la couche raster de population pour l'étendre au tampon Cyclon
```
9. **Calcule las estadísticas zonales para estimar la población expuesta.**
   - En el panel **Algorithms**, busque **Zonal Statistics**.
   - En la ventana de configuración: Calcul de la population exposée aux cyclones par district
     - Añada una descripción: `Calcul de la population exposée aux cyclones par district`
     - Configure la **Capa de entrada** a `Admin Boundaries` (desde **Entrada del modelo**).
     - Configure **Capa de ráster** en la salida del paso anterior (desde **Salida del algoritmo**).
     - Configure **Prefijo de columna de salida** en `exposed_population_`.
     - En **Estadísticas para calcular**, seleccione `Sum`.
     - Configure la salida en **Modelo de salida** y asígnele un nombre:
      ```
      exposed_population_sum
      ```
   - Haga clic en ``Ok`` para añadir el paso al modelo.
```{figure} /fig/fr_MDG_AA_model_zonal_statistic_pop_admin2.PNG
---
width: 600px
name: the_world_result
align: center
---
Calcul de la population exposée aux cyclones par district
```

**Los resultados deberían ser parecidos a los siguientes:**

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms.PNG
---
width: 600px
name: the_world_result
align: center
---
Votre modèle devrait resssemler à ceci. Tous les algorithmes sont correctement connectés et la sortie du modèle est définie.
```

10. **Valide su modelo (recomendado)**
   - Antes de guardar o ejecutar, haga clic en el botón ✔️ **Validar modelo** en la barra de herramientas superior.
   - Corrija cualquier advertencia o error que aparezca en el panel de registro.
   - Esto ayuda a garantizar que el modelo esté completo y no se rompa durante la ejecución.

11. **Ejecute el modelo**
   - Ejecute el modelo haciendo clic en `Model` -> `Run Model`
   - Configure **Límites administrativos** en `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Configure **Trayectoria del ciclón** en `example_Harald_2025_Track`
   - Configure **Ráster de población** en `MDG_WorldPop_2020_constrained.tif`
   - Configure la salida del modelo **exposed_population_sum** en `Harald_Exposed_Population`y guárdela en `data` -> `output`


Ahora puede ejecutar este modelo cada vez que esté disponible una nueva trayectoria de ciclón.

```{figure} /fig/fr_MDG_AA_model_run_model_M7_e1_task2.PNG
---
width: 600px
name: the_world_result
align: center
---
Pour exécuter le modèle, spécifiez l'entrée comme indiqué dans l'image et définissez le nom de la couche de sortie.
```

**Los resultados deberían ser parecidos a los siguientes:**
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_basics.PNG
---
width: 600px
name: the_world_result
align: center
---

``` 
12. **Añada la amortiguación del ciclón como salida del modelo adicional**
   - Haga doble clic en el algoritmo del paso 7 (**Reproyectar el buffer de nuevo a EPSG:4326**) para abrir su configuración.
   - En el campo **Capa de salida**, marque la casilla **Salida del modelo**.
   - Asigne un nombre claro al resultado, por ejemplo:
     ```
     cyclone_harald_buffer
     ``` 
   - Haga clic en ``Ok`` para guardar el cambio.
   - Esto permitirá que el modelo genere tanto los resultados de la población expuesta como la zona buffer de impacto del ciclón cuando se ejecute.

```{figure} /fig/fr_MDG_AA_model_output_buffer.PNG
---
width: 600px
name: the_world_result
align: center
---
```

13. **Ejecute el modelo otra vez**
   - Ejecute el modelo haciendo clic en `Model` -> `Run Model`
   - Configure **Límites administrativos** en `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Configure **Trayectoria del ciclón** en `example_Harald_2025_Track`
   - Configure **Ráster de población** en `MDG_WorldPop_2020_constrained.tif`
   - Configure la salida del modelo **cyclone_harald_buffer** en `cyclone_harald_buffer`y guárdela en `data` -> `output`
   - Configure la salida del modelo **exposed_population_sum** en `Harald_Exposed_Population`y guárdela en `data` -> `output`


::::{tab-set}


:::{tab-item} Buffer de salida del modelador gráfico

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_graphic.PNG
---
width: 600px
name: the_world_result
align: center
---
```
Definición de la entrada del modelo: Límites administrativos
:::

:::{tab-item} Ejecute modelo con salida de buffer
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_model_exicution.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
```
:::

:::{tab-item} Salida del modelo
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_extended_buffer.PNG
---
width: 600px
align: center
---
Definición de la entrada del modelo: Ráster de población
```
:::

::::



## Tarea 3: Identificación de centros de salud y escuelas afectados: Aina añade más capas

Tras construir su modelo para estimar la población expuesta, Aina quiere ampliar su utilidad. Asimismo, decide **identificar los servicios críticos** afectados por los ciclones, especialmente los **centros de salud** y las **escuelas**.

No solo quiere saber *qué instalaciones* están afectadas, sino también *cuántas hay en total* en cada distrito. De ese modo, puede calcular el porcentaje **de servicios afectados** en cada zona.

Para ello, utilizará dos conjuntos de datos de puntos de OpenStreetMap:

- [Centros de salud](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)
- [Establecimientos educativos](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

1. **Cargue los conjuntos de datos de los centros de salud y los establecimientos educativos.**
En primer lugar, echemos un vistazo a los datos con los que queremos trabajar.
- Navegue hasta su `input` carpeta de datos.
- Arrastre y suelte las siguientes capas en su proyecto de QGIS:
  - `hotosm_mdg_health_facilities`
  - `hotosm_mdg_education_facilities`
- Confirme que ambas capas estén visibles en el **Panel de capas**
2. **Guarde su modelo con un nuevo nombre**
   - Abra su modelo existente `Estimate_Exposed_Population.model3`.
   - Guárdelo inmediatamente con un nuevo nombre:
     - Haga clic en `Model` → `Save As…`
     - Guárdelo en la `project` carpeta como:
```  
Estimate_Exposed_Population_Health_Education
```
3. **Añada nuevas entradas de modelo**
   - En la sección **Entradas**, añada:
     - `Vector Layer`
       - **Descripción**:
        ```
        Centros de salud
        ```
       - Configure **Tipo de geometría** en `Point`
     - `Vector Layer`
       - **Descripción**:
        ```
        Establecimientos educativos
        ``` 
       - Configure **Tipo de geometría** en `Point`
::::{tab-set}

:::{tab-item} Entrada del modelo: Centros de salud
```{figure} /fig/fr_MDG_AA_model_input_health_facilities.PNG
---
width: 300px
name: the_world_result
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements de santé
```
:::
:::{tab-item} Entrada del modelo: Establecimientos educativos
```{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements d'enseignement
```
:::
::::
3. **Conteo de todas las instalaciones sanitarias por Admin 2**
   - En el panel **Algoritmos**, busque **Contar puntos en polígono**.
   - Configuración:
     - Añada una descripción: `Comptez le nombre d'établissements de santé dans chaque district.`
     - **Capa de polígonos**: `Admin Boundaries` (Entrada del modelo)
     - **Capa de puntos**: `Health Facilities` (Entrada del modelo)
     - **Nombre del campo de conteo**:
      ```
      Count_health_total
      ```
     - Deje la salida como **Salida del modelo**
```{figure} /fig/fr_MDG_AA_model_count_points_HF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements de santé dans chaque district.
```
4. **Conteo de todas las instalaciones educativas por Admin 2**
   - Añada otro paso **Contar puntos en polígono**.
   - Configuración:
     - Añada una descripción: `Comptez le nombre d'établissements de education dans chaque district`
     - **Capa de polígonos**: `Admin Boundaries` (Entrada del modelo)
     - **Capa de puntos**: `Education Facilities` (Entrada del modelo)
     - **Nombre del campo de conteo**:
      ```
      count_education_total
      ```
     - Deje la salida como **Salida del modelo**
```{figure} /fig/fr_MDG_AA_model_count_points_EF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements scolaires dans chaque district.
```
5. **Intersección de las instalaciones sanitarias con zona de influencia ciclónica**
   - En el panel de **Algoritmos**, busque **Intersección**.
   - En la ventana de configuración:
   - Añada una descripción:
      ```
      Établissements de santé dans la zone d'impact du cyclone
      ```  
     - **Capa de entrada**: `Health Facilities` (Entrada del modelo)
     - **Capa superpuesta**: zona de influencia ciclónica (utilice "Reproyectado a EPSG:4326" desde **Salida del algoritmo**)
     - Deje la salida como **Salida del modelo**
   - Haga clic en `Ok`
```{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de santé avec la zone d'impact du cyclone.
```
6. **Intersección de las instalaciones educativas con amortiguación del ciclón**
   - Añada otro algoritmo **Intersección**.
   - Configuración:
     - Añada una descripción:
       ```
       Établissements de education dans la zone d'impact du cyclone.
       ```
     - **Capa de entrada**: `Education Facilities` (Entrada del modelo)
     - **Capa superpuesta**: zona de influencia ciclónica (utilice "Reproyectado a EPSG:4326" desde **Salida del algoritmo**)
     - Deje la salida como **Salida del modelo**
   - Haga clic en `Ok`
```{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de education avec la zone d'impact du cyclone.
```
7. **Conteo de centros sanitarios afectados por Admin 2**
   - Añada **Contar puntos en polígono**
   - Añada una descripción: `Compter les établissements de santé touchés par district`
   - Configuración:
     - Añada una descripción: Compter les établissements de santé touchés par district
       ```
       Compter les établissements de santé touchés par district
       ``` 
     - **Capa de polígonos**: Conteo total de la producción de los centros de salud
     - **Capa de puntos**: salida de centros de salud intersecados
     - **Nombre del campo de conteo**:
       ```
       sum_exposed_health
       ``` 
```{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
8. **Conteo de centros educativos afectados por Admin 2**
   - Añada **Contar puntos en polígono**
   - Añada una descripción: `Compter les établissements education touchés par district`
   - Configuración:
     - Añada una descripción:
       ```
       Compter les établissements education touchés par district
       ``` 
     - **Capa de polígonos**: Conteo de la producción total de instalaciones educativas
     - **Capa de puntos**: salida de instalaciones educativas intersecadas
     - **Nombre del campo de conteo**:
       ```
       sum_exposed_education
       ``` 
```{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
9. **Calcule el porcentaje de centros sanitarios afectados**
Para calcular el porcentaje de centros de salud afectados por área administrativa, utilizaremos la **Calculadora de Campo** :
- Añada la **Calculadora de Campo**:
   - Añada una descripción: `Calculer le pourcentage d’établissements de santé touchés par district`
   - Configuración:
     - Añada una descripción:
       ```
       Calculer le pourcentage d'établissements de santé touchés par district
       ``` 
    - **Capa de entrada**: la salida de Conteo de centros de salud afectados por Admin 2
    - **Nombre del campo de salida**:
       ```
       pct_exposed_health
       ```
    - **Tipo de campo**: Decimal (real)
    - **Expresión**:
    ```qgis
     CASE WHEN "count_health_total" > 0
     THEN "sum_exposed_health" / "count_health_total" * 100
     ELSE 0
     END
    ```
    - Configure la salida como **Salida del modelo**
    - Nómbrelo:
    ```
    admin2_health_affected
    ```
```{figure} /fig/fr_MDG_AA_model_field_calc_pct_health_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements de santé touchés par district.
```
10. **Calcule el porcentaje de centros educativos afectados**
Para calcular el porcentaje de centros educativos afectados por zona administrativa, utilizaremos la **calculadora de campos** :
- Añada la **calculadora de campos**:
   - Añada una descripción: `Calculer le pourcentage d’établissements d’éducation touchés par district`
   - Configuración:
     - Añada una descripción:
       ```
       Calculer le pourcentage d’établissements d’éducation touchés par district
       ``` 
     - **Capa de entrada**: la salida de Conteo de establecimientos educativos afectados por Admin 2
     - **Nombre del campo de salida**:
       ```
       pct_exposed_education
       ``` 
     - **Tipo de campo**: Decimal (real)
     - **Expresión**:
       ```qgis
       CASE WHEN "count_education_total" > 0
       THEN "sum_exposed_education_POI" / "count_education_total" * 100
       ELSE 0
       END
       ``` 
   - Configure la salida como **Salida del modelo**
   - Nómbrelo:
     ```
     admin2_education_affected
     ```
```{figure} /fig/fr_MDG_AA_model_field_calc_pct_education_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements d’éducation touchés par district.
```
11. **Valide su modelo ampliado y guárdelo.**
   - Haga clic en el botón ✔️ **Validate Model** para verificar si hay errores.
   - Guarde de nuevo en: 
   **`Estimate_Exposed_Population_Health_Education.model3`**
12. **Ejecute el modelo**
   - Haga clic en el botón ▶️ `Run` en la esquina superior derecha de la ventana del modelador gráfico.
   - **Entrada:**
     - Haga clic en los tres puntos de cada conjunto de datos de entrada y seleccione la entrada correcta:
       - `Cyclone Track` → seleccione el GeoJSON de la trayectoria de la tormenta (por ejemplo, `Harald_2025_Track.geojson`).
       - `Population Raster` → seleccione el archivo ráster WorldPop
       - `Admin Boundaries` → seleccione la capa Admin 2 (por ejemplo, `MDG_adm2.gpkg`)
       - `Health Facilities` → seleccione el conjunto de datos de puntos para los centros de salud.
       - `Education Facilities` → seleccione el conjunto de datos de puntos para las escuelas
   - **Salida:**
     - Guarde todas las capas de salida en la carpeta de salida y utilice los nombres que se indican a continuación.
       - `admin2_health_affacted` -> 
        ```
        admin2_health_affected
        ```
       - `admin2_education_affected` ->
        ```
        admin2_education_affected
        ```
       - `cyclone_harald_buffer` -> 
        ```
        cyclone_harald_buffer
        ```
       - `exposed_population_sum` ->
        ```
        admin2_harald_Exposed_Population
        ```
   - Haga clic en `Run` para ejecutar el modelo completo.

::::{tab-set}

:::{tab-item} Modelador gráfico

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model.PNG
---
width: 600px
align: center
---
Vue d’ensemble du Modèle Graphique de la tâche 3 montrant tous les algorithmes connectés et les sorties définies.
```
:::
:::{tab-item} Configuración del modelo de ejecución
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_run_configurations.PNG
---
width: 600px
align: center
---
Configuration des paramètres pour exécuter le modèle de la tâche 3 avec toutes les couches d’entrée requises.
```
:::
:::{tab-item} Salida del modelo
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model_results_AT.PNG
---
width: 600px
align: center
---
Résultats du modèle de la tâche 3 affichés dans QGIS, y compris les pourcentages d'établissements de santé et d'éducation touchés par district.
```
:::
::::

---

## Tarea 4: Visualización de los resultados del impacto del ciclón: Aina estiliza sus capas

Aina ahora tiene todos los resultados de análisis que necesita, pero los números y las tablas por sí solos no convencerán a sus colegas ni a los responsables de la toma de decisiones. Lo que necesitan son mapas claros y fáciles de leer que puedan usarse directamente en reuniones e informes.

Para ahorrar tiempo, Aina no quiere ajustar los colores y las leyendas manualmente cada vez que llega un nuevo ciclón. En su lugar, utilizará archivos de estilo listos para usar (.qml) que instantáneamente le dan a las capas un aspecto profesional y consistente. Donde aún no exista un estilo, ella misma creará uno, para que la próxima vez el mapa se pueda actualizar con solo unos pocos clics.

En esta tarea, ayudará a Aina a hacer que sus mapas de impacto de ciclones sean informativos y visualmente atractivos mediante la aplicación y creación de archivos de estilo QGIS.

### 1. **Cargar capas necesarias (si aún no están cargadas)**

Asegúrese de que las siguientes capas ya estén cargadas en su proyecto QGIS. Estas son salidas de **Tarea 3**:

- `example_Harald_2025_Track`
- `cyclone_harald_buffer`
- `Harald_Exposed_Population`
- `admin2_health_affected`
- `admin2_education_affected`

Si falta alguna:
- Cárguelos mediante la función de**arrastrar y soltar** desde su carpeta `results`; o bien
- Use `Layer` → `Add Layer` → `Add Vector Layer` o `Add Raster Layer`

---

### 2. **Aplicación de archivos de estilo predefinidos**
Aplique los siguientes archivos de estilo`.qml` a las capas correspondientes:

| **Capa** | **Archivo de estilos** |
|----------------------------------------|-------------------------------------------|
| `example_Harald_2025_Track` | `storm_track_cyclone_style.qml` |
| `cyclone_harald_buffer` | `exposed_cyclone_area_style.qml` |
| `Harald_Exposed_Population` | `exposed_population_style.qml` |
| `admin2_health_affected` | `exposed_healthsites_style.qml` |
| `admin2_education_affected` | `exposed_education_facilities_style.qml` |

```{note}
⚠️ Para las **instalaciones de salud** y **educación**, los archivos de estilo proporcionados están vinculados a la columna que contiene la **suma de las instalaciones expuestas**.  
**No** se basan en la columna de porcentaje. 
```


**Pasos:**
- Haga clic con el botón derecho en la capa en el **Panel de capas**
- Seleccione **Propiedades**
- En la ventana que se abre, vaya a la pestaña **Simbología**.
- En la parte inferior izquierda, haga clic en **Style** → **Load Style…**
- Haga clic en los tres puntos ![](/fig/Three_points.png)
- Navegue hasta el archivo `.qml` correspondiente en la carpeta `layer_sytle` y selecciónelo.
- Haga clic en **Abrir**,luego en **Aplicar** y **Aceptar** para confirmar

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_output_style.mp4"></video>

> 💡 *Si el estilo no se carga correctamente, vuelva a comprobar los nombres de las columnas y asegúrese de que el nombre de columna utilizado en el `.qml` coincide con el de la capa. Para ello, abra el comando **Tabla de atributos** de la capa y comparar nombres de campo.*

---


::::{tab-set}

:::{tab-item} Resultado intermedio: Población expuesta

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_pop_style.PNG
---
width: 600px
align: center
---
Carte montrant le nombre de personnes exposées par district après l’application du style .qml.
```
:::
:::{tab-item} Resultado intermedio: Instalaciones de salud expuestas
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_HS_sum_style.PNG
---
width: 600px
align: center
---
Carte indiquant le nombre total d’établissements de santé exposés par district, représentés avec le style prédéfini.
```
:::
:::{tab-item} Resultado intermedio: Instalaciones educativas expuestas
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_ES_sum_style.PNG
---
width: 600px
align: center
---
Carte affichant le nombre total d’établissements scolaires exposés par district, après application du fichier de style .qml.
```
:::
::::



### 3. **Estilizar capas porcentuales manualmente**

Aina también quiere visualizar el porcentaje de instalaciones sanitarias y educativas expuestas. Sin embargo, dado que no hay un estilo preparado disponible, debe completar el proceso manualmente.

**Pasos:**
- **Haga clic con el botón derecho** en la capa `admin2_health_affected` → seleccione **Duplicar capa**
- **Cambie el nombre** de la capa duplicada a:
  ```
  admin2_health_affected_percentage
  ```
- Haga clic con el botón derecho en la capa en el **Panel de capas**
- Seleccione **Propiedades**
- En la ventana que se abre, vaya a la pestaña **Simbología**.
- Configure **Simbología** en `Graduated`
- Elija el **campo** correcto:
  - `pct_health_affected`
- Abra la pestaña **Histograma** para ver la distribución de valores haciendo clic en `calculate histogram`
- A continuación, vuelve a `Classes` y establezca la siguiente configuración:
  - **Modo**: `Equal Interval`
  - **Clases**: `4`
- Haga clic en `OK`. Se crearán cuatro clases (`0–25%`, `25–50%`, `50–75%`, `75–100%`)
- Elija una rampa de color (por ejemplo, amarillo claro → rojo oscuro)
- Opcionalmente, personalice las etiquetas de clase para mayor claridad
- Haga clic en `Apply`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_affacted_HS_pct.mp4"></video>

- Repite el mismo proceso para la capa `admin2_education_affected`.
Después de duplicar la capa, cambie el nombre de la nueva a:
 ```
 admin2_health_affected_percentage
```


 🧠 *¿Por qué 4 clases iguales?* 
 Esto ayuda a visualizar la gravedad en todos los distritos mediante categorías de riesgo sencillas e interpretables. Sin embargo, puede experimentar con **Natural Breaks** si los datos están distribuidos de manera desigual.

---

 ### 4. **Guarde sus nuevos estilos para reutilizarlos**

 Guarde sus estilos creados manualmente como `.qml` para reutilizarlos en el futuro.

 **Pasos:**
 - Haga clic con el botón derecho en la capa en el **Panel de capas**
 - Seleccione **Propiedades**
 - En la ventana que se abre, vaya a la pestaña **Simbología**.
 - Haga clic en `Style` → `Save Style…`
 - Guarde el archivo en la carpeta `layer_sytle`
 - Utilice estos nombres de archivo:
   ```
   health_pct_affected_style
  ```
  ```
  education_pct_affected_style
  ```


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_save_new_style.mp4"></video>


### 5. *(Opcional)* Importar estilos a su biblioteca QGIS

Para reutilizar sus estilos en cualquier proyecto futuro:

- Vaya a `Settings` → `Style Manager`
- Haga clic en `Import/Export` → `Import Items`
- Busque sus archivos guardados `.qml` y selecciónelos.

Los estilos aparecerán ahora como ajustes preestablecidos en **Panel de estilos de capa**.

---

## Tarea 5: Creación rápida de mapas: Aina utiliza plantillas de mapas

Después del arduo trabajo de analizar datos y capas de estilo, Aina está lista para **compartir sus resultados**. Aunque crear un mapa de aspecto profesional desde cero cada vez sería lento y repetitivo.

Para ahorrar tiempo, utiliza las plantillas de mapas **(archivos .qpt)** preparadas por su equipo. Estas plantillas ya contienen los elementos esenciales: marcos de mapa, leyendas, logotipos, títulos y barras de escala. Con ellas, Aina puede convertir su análisis en un **mapa limpio y coherente** en unos pocos clics.

✅ **Objetivo** 
Utilice una plantilla de mapas de QGIS predefinida para crear y exportar rápidamente mapas que muestren los impactos de los ciclones en la población, los centros sanitarios y las escuelas.


1. Cargue la plantilla de diseño de impresión prefabricada

- Localice la plantilla `cyclone_impact_population_map_template.qpt` en la carpeta de su proyecto en: 
 `Map_Templates/`

- Puede cargar la plantilla mediante la función de **arrastrar y soltar**:
  - Abra su proyecto QGIS.
  - Arrastre el archivo `.qpt` directamente a QGIS: se creará automáticamente un nuevo diseño.

- Alternativamente:
  - Vaya a `Project` → `New Print Layout`
  - Ingrese un nombre (p. ej. `Harald_2025_population`)
  - Haga clic en `OK`
  - En el diseño, vaya a `Layout` → `Import from Template…`
  - Seleccione el archivo `cyclone_impact_overview_map_template.qpt` y haga clic en `Open`
 2. Compruebe y configure el tamaño de la página
- Haga clic derecho en cualquier parte del lienzo blanco y elija `Page Properties`.
- En el panel del lado derecho, asegúrese de lo siguiente:
  - **Tamaño de página**: A3
  - **Orientación**: Apaisado

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_load_mpa_template.mp4"></video>

3. Actualizar la tabla de atributos de los distritos expuestos
- En el **diseño de impresión**, haga clic en la tabla de atributos (parte derecha del diseño).
- En el panel de **Propiedades del elemento**:
  - Asegúrese de que está seleccionada la capa correcta `Harald_Exposed_population`.
  - Haga clic en `Refresh Table Data`
  - Haga clic en `Attributes…` → en la parte superior debajo **Campos** haga clic en `Clear`
    - Luego agregue la siguiente capa haciendo clic en ➕ :
    - **Atributo**: `ADM1_EN`; `ADM2_EN`; `ADM2_PCODE`; `exposed_population_sum`
    - Para ordenar el contenido de la tabla, en el menú **Ordenar** haga clic en ➕ y agregue la columna `AMD1_EN`
    - **Orden de clasificación**: Ascendente
  - Haga clic en `OK`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_makingadjust_AT.mp4"></video>


```{admonition} ⚠️ Advertencia – Tablas Largas
Si la tabla de atributos que desea incluir es **más larga que el marco del mapa**, parte de ella se cortará en el mapa exportado.  
Para solucionar esto, abra las propiedades de la tabla en el diseño y **reduzca el tamaño de fuente** hasta que quepa toda la tabla completa.  
```


5. Ajustar la leyenda
- En el diseño, haga clic en el elemento **Leyenda**.
- En el panel de **Propiedades del elemento**:
  - Desmarque **Actualización automática**
  - Desplácese hasta **Elementos de leyenda** y elimine todas las entradas (🗑️)
  - Agregue las siguientes capas relevantes:
    - `example_Harald_2025_Track`
    - `cyclone_harald_buffer`
    - `Harald_Exposed_Population`
  - Al seleccionar capas, marque **Solo capas visibles**
  - Cambie el nombre de las entradas de leyenda para que coincidan con la nomenclatura del diseño.
    - `example_Harald_2025_Track` ->
     ```
     Trayectoria del ciclón Harald
     ```
    - `cyclone_harald_buffer`->
     ```
     Ciclón Harald, amortiguador de 200 km
     ```
    - `Harald_Exposed_Population`->
     ```
     Número de personas expuestas
     ```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_adjust_map_making_Legend.mp4"></video>

6. **Actualice logotipos e iconos**
 - Los logotipos que hay que añadir al mapa están representados por la **X** roja.
 - Haga clic en la imagen de la **lista de elementos**.
 - Haga clic en los tres puntos ![](/fig/Three_points.png) junto a la ruta del archivo.
 - Vaya a la carpeta `logos_pictures` y seleccione el archivo del logotipo correcto.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_making_update_logos.mp4"></video>


7. Revisión y actualización de los elementos de texto del diseño
- Asegúrese de que todos los elementos de texto estén actualizados, especialmente:
  - **Título del mapa**
  - **Nombre y fecha del ciclón**
  - **Autor/Organización** (opcional)
- Ajuste el tamaño de fuente o la alineación si es necesario

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_mak_making_adjust_title.mp4"></video>

### ✅ Lista de verificación final

| Tarea | Hecho |
|------------------------------------------------|------|
| Página establecida en A3 horizontal | ☐ |
| Solo el grupo de capas relevante está activo | ☐ |
| Actualización de la tabla de atributos de los distritos expuestos | ☐ |
| Leyenda limpia y renombrada | ☐ |
| Todos los elementos de texto actualizados | ☐ |

---



```{dropdown} El resultado final después de aplicar el estilo a la capa debería ser el siguiente
 El mapa muestra ahora claramente la población expuesta dentro de los distritos afectados. Se resalta la línea original de la trayectoria de la tormenta, utilizada como datos de entrada, y la zona de amortiguación de impacto, que sirve como indicador para identificar los distritos expuestos.
 En la parte derecha del mapa, una lista muestra todos los distritos expuestos, con datos sobre la población total y la población expuesta. Los distritos (Admin 2) están organizados en sus regiones correspondientes (Admin 1).
```{figure} /fig/MAD_Trigger_Impact_Population_Map_example.png
---
width: 1000px
name:
align: center
---
```

## Tarea 6: Exportación de resultados de modelos para el equipo de operaciones

**Antecedentes: Aina apoya a los responsables de la toma de decisiones**

Después de producir mapas y elementos visuales, Aina a menudo recibe solicitudes del equipo de operaciones:
 _“Puede enviarnos los datos en formato de tabla?”_

En lugar de exportar estas tablas manualmente cada vez, Aina quiere automatizar este paso dentro de su modelo, asegurando que cada ejecución del modelo produzca archivos de datos claros y listos para usar.

En esta tarea, ayudará a Aina a ampliar su modelo para exportar capas seleccionadas.

Uniremos las siguientes capas paso a paso:

- `admin2_health_affected_pct`: 
  Contiene el **número total de centros de salud**, el **número de centros de salud afectados** y el **porcentaje de centros de salud** afectados.

- `admin2_education_affected_pct`: 
  Contiene el **número total de instalaciones educativas**, el **número de instalaciones educativas afectadas** y el **porcentaje de instalaciones educativas afectadas**.

- `exposed_population`: 
  Contiene la **población total por distrito** y la **población expuesta** de la etapa de estadísticas zonales.

---

1. Abra su modelo
- Abierto`Estimate_Exposed_Population_Health_Education`
- Guarde una nueva versión como:
  ```
  Estimate_Exposed_Population_Health_Education_Spreadsheet_Export
  ```
2. Una los datos de salud y educación en una sola capa
- En los **Algoritmos**, busque `Join Attributes by Field Value`.
- Añada una descripción: `Joindre santé et éducation dans une seule couche par ADM2`
- Configure el algoritmo de la siguiente manera:
  - **Capa de entrada**: `admin2_health_affected` (seleccionar de **Salida de algoritmo**)
  - **Capa de entrada 2**: `admin2_education_affected` (seleccione de **Salida de algoritmo**)
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

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de santé et d’éducation par le champ `ADM2_PCODE` afin de combiner les résultats dans une seule couche.
```
3. Una el resultado con los datos de población
Ahora, una el resultado del paso anterior (salud + educación) a los datos de **población expuestos**.
- Añada un segundo algoritmo `Join Attributes by Field Value` al modelo
- Añada una descripción: `Joindre les données de population avec les indicateurs santé et éducation`
- Configure el algoritmo de la siguiente manera:
  - **Capa de entrada**: `exposed_population` (seleccionar de **Salida de algoritmo** del paso Estadísticas zonales)
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
    count_health_total;sum_exposed_health;pct_exposed_health;count_education_total;sum_exposed_education;pct_exposed_education
    ```
  - **Tipo de unión**: Tome los atributos de la primera característica coincidente solamente (uno a uno)
  - Deje la salida como **Salida del modelo**

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop_HS_ES.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de population avec les indicateurs de santé et d’éducation.
```

::::{tip} Dónde encontrar los nombres de las columnas 
Abra las **tablas de atributos** de las salidas `health_total_per_admin2`, `sum_exposed_healthsites_POI` y `admin2_health_affected_pct` en QGIS.  
Observe los **encabezados de columna** para encontrar los nombres exactos de los campos que desee copiar.
::::
::::{warning} Los espacios invisibles romperán la unión 
Si un nombre de columna como `count_health_total` tiene un espacio final invisible, la unión fallará silenciosamente.  
Copie siempre los nombres de los campos **directamente de la tabla** de atributos para evitar errores.
::::


4. Exporte resultados a una hoja de cálculo
- En la **caja de herramientas**, busque `Export to spreadsheet` y haga doble clic para abrir.
- Añada una descripción: `Exporter les données de population, d'éducation et de santé dans un seul tableau`
- Configure la herramienta de la siguiente manera:
  - **Capa de entrada**: Seleccione la salida del Paso 3 de **Salida de algoritmo**
  - **Hoja de cálculo**:
    ```
    exposure_indicators_spreadsheet
    ```

  - Haga clic en `Ok` para agregarlo al modelo.
Una vez que ejecute el modelo, este paso generará automáticamente una hoja de cálculo con todos los indicadores relevantes listos para el equipo de operaciones.

```{figure} /fig/fr_MDG_AA_model_export_as_table.PNG
---
width: 600px
name: the_world_result
align: center
---
Exportador tous les indicaurs (población, sanidad, educación) vers un tableau unique au format tableur.
```



5. **Valide su modelo ampliado y guárdelo.**
   - Haga clic en el botón ✔️ **Validate Model** para verificar si hay errores.
   - Guarde de nuevo en: 
     **`Estimate_Exposed_Population_Health_Education.model3`**
6. **Ejecute el modelo**
   - Haga clic en el botón ▶️ `Run` en la esquina superior derecha de la ventana del modelador gráfico.
   - **Entrada:**
     - Haga clic en los tres puntos de cada conjunto de datos de entrada y seleccione la entrada correcta:
       - `Cyclone Track` → seleccione el GeoJSON de la trayectoria de la tormenta (por ejemplo, `Harald_2025_Track.geojson`).
       - `Population Raster` → seleccione el archivo ráster WorldPop
       - `Admin Boundaries` → seleccione la capa Admin 2 (por ejemplo, `MDG_adm2.gpkg`)
       - `Health Facilities` → seleccione el conjunto de datos de puntos para los centros de salud.
       - `Education Facilities` → seleccione el conjunto de datos de puntos para las escuelas
   - **Salida:**
     - Guarde todas las capas de salida en la carpeta de salida y utilice los nombres que se indican a continuación.
       - `admin2_health_affacted` -> 
        ```
        admin2_health_affected
        ```
       - `admin2_education_affected` ->
        ```
        admin2_education_affected
        ```
       - `cyclone_harald_buffer` -> 
        ```
        cyclone_harald_buffer
        ```
       - `exposed_population_sum` ->
        ```
        admin2_harald_Exposed_Population
        ```
       - `exposure_indicators_spreadsheet` ->
        ```
        exposure_indicators_harald
        ```
   - Haga clic en `Run` para ejecutar el modelo completo.

::::{tab-set}

:::{tab-item} Modelador gráfico

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task_6_export_spreadsheet__model.PNG
---
width: 600px
align: center
---
Vue du modeleur graphique avec l’étape d’exportation vers un tableau ajoutée au modèle.
```
:::
:::{tab-item} Configuración del modelo de ejecución
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_run_configurations.PNG
---
width: 600px
align: center
---
Fenêtre de configuration pour exécuter le modèle avec l’option d’export vers un tableau.
```
:::
:::{tab-item} Salida del modelo
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task6_export_spreadsheet_results_AT.PNG
---
width: 600px
align: center
---
Résultats finaux du modèle exportés dans un tableau prêt à être utilisé.
```
:::
::::

---





## Tarea 7: Accesibilidad de los puestos de salud desde almacenes de CRM

__Contexto:__

Cuando se pronostica que un ciclón tocará tierra, Aina trabaja con los equipos de logística y salud para decidir **dónde enviar botiquines preposicionados**. Sin embargo, no todos los almacenes de CRM guardan los artículos necesarios, solo tres lo hacen.

Para tomar decisiones rápidas y basadas en datos, Aina quiere saber **¿Qué puestos de salud son accesibles?** de esos almacenes **dentro de las 10 horas**. Este análisis ayuda a garantizar que los kits se envíen a las instalaciones **a las que realmente se pueda acceder a tiempo.**.

Su objetivo es crear un mapa visual claro que muestre los puestos de salud accesibles frente a los no accesibles, y compartirlo con los responsables de la toma de decisiones lo más rápido posible.


### 1. Filtro de publicaciones de salud del conjunto de datos de centros de salud nacionales

Antes de verificar qué instalaciones son accesibles, Aina necesita aislar los **puestos de salud** del conjunto de datos más amplio de todos los centros de salud.

1. **Cargue el conjunto de datos de centros de salud**
   - Archivo: `hotosm_mdg_health_facilities_points.gpkg` (o el GeoPackage respectivo que esté utilizando)
   - Cárguelo arrastrando y soltando o a través de `Layer` → `Add Vector Layer`.
2. **Abra la tabla de atributos** y compruebe la columna llamada `amenity`.
3. **Filtre por expresión** para mantener solo las publicaciones de salud:
   - Haga clic con el botón derecho en la capa → `Filter…`
   - Utilice la siguiente expresión:
     ```qgis
     "amenity" = 'health_post'
     ```
4. **Exporte la capa filtrada**
   - Haga clic con el botón derecho en la capa filtrada en el panel Capas → `Export` → `Save Features As…`
   - Formato: `GeoPackage`
   - Guarde en su `project` carpeta como:
     ```
     health_posts_only.gpkg
     ```
   - Haga clic en `OK` para confirmar la exportación.
5. **Quite el filtro** o capa original del proyecto para evitar confusiones.
 💡 **Sugerencia**: El filtrado directo en QGIS le permite trabajar con un subconjunto específico de características sin modificar el conjunto de datos original.

### 2. Carga de capas isócronas para los tres CRM

Aina sabe que únicamente**tres almacenes** guardan los suministros médicos necesarios: 
**Antananarivo**, **Maroantsetra**y **Tolanaro**. Ahora cargará las capas isócronas de cada uno de estos almacenes para comenzar a analizar las áreas de servicio.

1. **Carga de las capas isócronas individuales** para cada almacén:
   - `CRM_warehouse_Isochrones_Antananarivo.gpkg`
   - `CRM_warehouse_Isochrones_Maroantsetra.gpkg`
   - `CRM_warehouse_Isochrones_Tolanaro.gpkg`

  Puede arrastrar y soltar cada archivo en QGIS o ir a `Layer` → `Add Layer` → `Add Vector Layer`.

2. **Inspeccione la tabla de atributos** de cada capa isócrona 
   Confirme que cada registro tiene un campo `traveltime_h` que muestra el tiempo de viaje estimado en **horas**.

3. **Elimine todas las características en las que el tiempo de viaje sea superior a 10 horas**:
   - Haga clic con el botón derecho en cada capa → `Filter…`
   - Aplique la expresión:
     ```qgis
     "traveltime_h" <= 10
     ```

4. **Exporte cada capa filtrada** a la carpeta `temp`:
    En este punto, Aina también se asegura de que todas las capas exportadas se guarden en el mismo CRS que el conjunto de datos de la publicación de salud, `EPSG:4326`, para evitar problemas en la unión espacial.
   - Guarde cada uno como:
     ```
     CRM_isochrones_Antananarivo_upto10h.gpkg
     CRM_isochrones_Maroantsetra_upto10h.gpkg
     CRM_isochrones_Tolanaro_upto10h.gpkg
     ```

5. **Estilice las isócronas para mayor claridad**
   Aina puede aplicar un archivo de estilo predefinido para colorear la capa en función de `traveltime_h` para visualizar diferentes franjas horarias (4h, 6h, 8h, 10h) más adelante en el Paso 5.
   - Haga clic con el botón derecho en cada capa filtrada → `Properties` → `Symbology`
   - Haga clic en `Style` en la parte inferior → `Load Style…`
   - Seleccione el archivo: 
     `CRM_warehouse_isochrones_style.qml`
   - Haga clic en `Open`, luego en `Apply` y `OK`

### 3. Visualización de la accesibilidad de los puestos de salud desde los almacenes de CRM
Aina necesita identificar a qué puestos de salud se puede llegar por carretera desde tres almacenes clave de CRM (Antananarivo, Maroantsetra y Tolanaro) **dentro de las 10 horas de tiempo de viaje**. Lo hará manualmente combinando las isócronas de 10 horas de estos almacenes y comparándolas con el conjunto de datos del puesto nacional de salud.
1. **Fusión de las capas isócronas de los tres almacenes**
   - En **Caja de herramientas de procesamiento**busque `Merge Vector Layers`.
   - **Capas de entrada**:
     - `CRM_isochrones_Antananarivo_upto10h.gpkg`
     - `CRM_isochrones_Maroantsetra_upto10h.gpkg`
     - `CRM_isochrones_Tolanaro_upto10h.gpkg`
   - **CRS**: `EPSG:4326`
   - **Guardar en archivo**:
     ```
     merged_isochrones_10h.gpkg
     ```
   - Haga clic en **Ejecutar**.
2. **Seleccione puestos de salud accesibles en 10 horas**
   - En **Caja de herramientas de procesamiento**busque `Select by Location`.
   - Configure los siguientes parámetros:
     - **Capa de entrada**: `health_posts_only.gpkg`
     - **Predicado**: `intersects`
     - **Capa de intersección**: `merged_isochrones_10h.gpkg`
   - Haga clic en **Ejecutar**.
   💡 Los puntos seleccionados son aquellos que se encuentran dentro de las áreas de servicio de 10 horas de los almacenes.
3. **Cree un campo de accesibilidad para publicaciones de salud seleccionadas**
   - Abra la **Calculadora de campo** ![](/fig/mActionCalculateField.png) en la capa `health_posts_only`.
   - Confirme ✅ `Only update selected features`
   - **Nombre del campo de salida**: `Reachability_time`
   - **Tipo de campo de salida**: `Text (string)`
   - **Expresión**:
     ```qgis
     'reachable in 10 hours'
     ``` 
   - Haga clic en ``Ok`` para crear y completar el nuevo campo para las características seleccionadas.
4. **Marque las publicaciones de salud restantes como no accesibles**
   - Invierta la selección: 
        Vaya a `Edit` → `Invert Feature Selection` ![](/fig/mActionInvertSelection.png) 
        o haga clic con el botón derecho en la capa y seleccione `Invert Selection`.
   - Abra la **Calculadora de campo** otra vez.
   - Confirme ✅ `Only update selected features`
   - Utilice el mismo campo: `Reachability_time`
   - **Expresión**:
     ```qgis
     'not reachable in 10 hours'
     ``` 
   - Haga clic en `Ok` para aplicar la actualización.

✅ Ahora todos los puestos de salud están etiquetados como **accesibles** o **no accesibles** en `Reachability_time` columna.





