::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 3: Identificación de centros de salud y escuelas afectados: Aina añade más capas

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

Este ejercicio forma parte del [programa de ejercicios de análisis de ciclones de acción anticipatoria de Madagascar.](https://giscience.github.io/gis-training-resource-center/content/es/Exercise_tracks/es_mdg_aa_cyclones.html)

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

* [Estadísticas zonales](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_raster_basic_wiki.html)
* [Intersección](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Buffer](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Recorte](/content/es/Wiki/es_qgis_projections_wiki.md)
* [Automatización](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_automation_wiki.html)

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
- Consulte [¿Cómo realizar capacitaciones?](https://giscience.github.io/gis-training-resource-center/content/es/Trainers_corner/es_how_to_training.html#how-to-do-trainings) para obtener algunos consejos generales para impartirlas.

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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_7_Exercise_3_AA_MDG_task_3-20250825T143514Z-1-001.zip

__Descargue todos los conjuntos de datos aquí, guarde la carpeta en su ordenador y descomprima el archivo.__
:::

## Contexto

Tras construir su modelo para estimar la población expuesta, Aina quiere ampliar su utilidad. Asimismo, decide **identificar los servicios críticos** afectados por los ciclones, especialmente los **centros de salud** y las **escuelas**.

No solo quiere saber *qué instalaciones* están afectadas, sino también *cuántas hay en total* en cada distrito. De ese modo, puede calcular el porcentaje **de servicios afectados** en cada zona.

Para ello, utilizará dos conjuntos de datos de puntos de OpenStreetMap:

- [Centros de salud](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)
- [Establecimientos educativos](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

## Tareas:

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
        Health Facilities
        ```
       - Configure **Tipo de geometría** en `Point`
     - `Vector Layer`
       - **Descripción**:
        ```
        Education Facilities
        ```
       - Configure **Tipo de geometría** en `Point`
:::::{tab-set}

::::{tab-item} Entrada del modelo: Centros de salud
:::{figure} /fig/fr_MDG_AA_model_input_health_facilities.PNG
---
width: 300px
name: the_world_result
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements de santé
:::
::::
::::{tab-item} Entrada del modelo: Establecimientos educativos
:::{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements d'éducation
:::
::::
:::::
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
:::{figure} /fig/fr_MDG_AA_model_count_points_HF_admin2.PNG
---
width: 600px
align: center
---
Configuración de la operación: calcular el número de centros de salud de cada distrito.
:::    
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
:::{figure} /fig/fr_MDG_AA_model_count_points_EF_admin2.PNG
---
width: 600px
align: center
---
Configuración de la operación: calcular el número de centros escolares de cada distrito.
:::
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
:::{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuración de la operación: interconectar los centros de salud con la zona de impacto del ciclón.
:::
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
:::{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuración de la operación: interconectar los centros educativos con la zona de impacto del ciclón.
:::
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
:::{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuración de la operación: cómputo de los centros sanitarios afectados por distrito.
:::
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
:::{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuración de la operación: cómputo de los centros sanitarios afectados por distrito.
:::
9. **Calcule el porcentaje de centros sanitarios afectados**
Para calcular el porcentaje de centros de salud afectados por área administrativa, utilizaremos la **Calculadora de Campo** :
- Añada la **Calculadora de Campo**:
   - Añada una descripción: `Calculer le pourcentage d’établissements de santé touchés par district`
   - Configuración:
     - Añada una descripción:
       ```
       Calculer le pourcentage d’établissements de santé touchés par district
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
:::{figure} /fig/fr_MDG_AA_model_field_calc_pct_health_exposed.PNG
---
width: 600px
align: center
---
Configuración de la operación: calcular el porcentaje de centros de salud afectados por distrito.
:::
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
:::{figure} /fig/fr_MDG_AA_model_field_calc_pct_education_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements d’éducation touchés par district.
:::
11. **Valide su modelo ampliado y guárdelo.**
   - Haga clic en el botón ✔️ **Validate Model** para verificar si hay errores.
   - Guarde de nuevo en:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
12. **Ejecute el modelo**
   - Haga clic en el botón ▶️ **Run** en la esquina superior derecha de la ventana del modelador gráfico.
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

:::::{tab-set}

::::{tab-item} Modelador gráfico

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model.PNG
---
width: 600px
align: center
---
Vista de conjunto del Modelo Gráfico de la Tarea 3 mostrando todos los algoritmos conectados y las salidas definidas.
:::
::::
::::{tab-item} Configuración del modelo de ejecución
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_run_configurations.PNG
---
width: 600px
align: center
---
Configuration des paramètres pour exécuter le modèle de la tâche 3 avec toutes les couches d’entrée requises.
:::
::::
::::{tab-item} Salida del modelo
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model_results_AT.PNG
---
width: 600px
align: center
---
Résultats du modèle de la tâche 3 affichés dans QGIS, y compris les pourcentages d’établissements de santé et d’éducation touchés par district.
:::
::::
:::::

---
