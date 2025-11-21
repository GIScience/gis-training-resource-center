::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 4: Visualización de los resultados del impacto del ciclón: Aina diseña sus capas

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse en la formación en línea y en la presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Programa de ejercicios:__

Este ejercicio forma parte del [programa de ejercicios de análisis de ciclones de acción anticipatoria de Madagascar.](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_mdg_aa_cyclones.html)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
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
^^^
Aina, experta en SIG de la Cruz Roja Malgache (CRM), se prepara para la próxima temporada de ciclones. Quiere mejorar la capacidad de su equipo para actuar con rapidez una vez que se pronostica una tormenta, mediante la automatización de análisis clave en QGIS. Esto incluye la estimación de las poblaciones expuestas, la identificación de los servicios afectados como la sanidad y la educación, y la evaluación de si se puede llegar a los puestos sanitarios desde los almacenes clave en un plazo crítico de 10 horas.
El objetivo es preparar un flujo de trabajo de análisis y visualización de principio a fin de que pueda respaldar una acción anticipatoria rápida y basada en datos antes de que un ciclón toque tierra.


:::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html#how-to-do-trainings) para obtener consejos generales sobre cómo impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes han descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y replicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su proyecto de QGIS.

__Cierre de la sesión:__

- Deje tiempo para cualquier problema o pregunta relacionada con las tareas al final del ejercicio.
- Deje tiempo para preguntas abiertas.

:::

## Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_4_Exercise_6_AA_MDG_task_4-20250825T143508Z-1-001.zip

__Descargue todos los conjuntos de datos aquí, guarde la carpeta en su computadora y descomprima el archivo.__
:::

## Contexto

Aina dispone ahora de todos los resultados de análisis que necesita, pero los números y las tablas por sí solos no convencerán a sus colegas ni a los responsables de la toma de decisiones. Lo que necesitan son mapas claros y fáciles de leer que puedan utilizarse directamente en reuniones e informes.

Con el fin de ahorrar tiempo, Aina no quiere ajustar manualmente los colores ni las leyendas cada vez que llega un nuevo ciclón. En su lugar, utilizará archivos (.qml) de estilo ya creados que confieren instantáneamente a las capas un aspecto profesional y coherente. Cuando aún no exista un estilo, ella misma creará uno, para que la próxima vez el mapa pueda actualizarse con unos pocos clics.

En esta tarea, ayudarás a Aina a hacer que sus mapas de impacto de ciclones sean informativos y visualmente atractivos, aplicando y creando archivos de estilo QGIS.

## Tareas

### 1. **Cargue las capas necesarias (si aún no están cargadas)**

Asegúrese de que las siguientes capas ya están cargadas en su proyecto de QGIS. Estos son los resultados de la **tarea 3**:

- `example_Harald_2025_Track`
- `trayectoria_harald_buffer`
- `población_expuesta_suma_harald`
- `adm2_educación_expuesta`
- `adm2_centros_salud_expuestos`

Si falta alguno:
- Cárguelos mediante la función de **arrastrar y soltar** desde su carpeta `results`; o bien
- utilice `Capa` → `Añadir Capa` → `Añadir capa vectorial` o `Añadir capa ráster`

---

### 2. **Aplicar archivos de estilo predefinidos**
Aplique los siguientes archivos de estilo `.qml` a las capas correspondientes:

| **Capa** | **Archivo de estilos** |
|----------------------------------------|-------------------------------------------|
| `example_Harald_2025_Track` | `storm_track_cyclone_style.qml` |
| `trayectoria_harald_buffer` | `exposed_cyclone_area_style.qml` |
| `población_expuesta_suma_harald` | `exposed_population_style.qml` |
| `adm2_centros_salud_expuestos` | `exposed_healthsites_style.qml` |
| `adm2_educación_expuesta` | `exposed_education_facilities_style.qml` |

:::{note}
⚠️ Para las **instalaciones sanitarias** y **educativas**, los archivos de estilo proporcionados están vinculados a la columna que contiene la **suma de las instalaciones expuestas**. 
**No** se basan en la columna de porcentaje. 
:::

**Pasos:**
- Haga clic derecho sobre la capa en el **Layers Panel**
- Seleccione **Properties**
- En la ventana que se abre, vaya a la pestaña **Symbology**
- En la parte inferior izquierda, haga clic en **Style** → **Load Style…**
- Haga clic en los tres puntos ![](/fig/Three_points.png).
- Navegue hasta el archivo `.qml` correspondiente en la carpeta `layer_style` y selecciónelo.
- Haga clic en **Open**, luego **Apply** y **OK** para confirmar.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_output_style.mp4"></video>

💡 *Si el estilo no se carga correctamente, revise los nombres de columna y asegúrese de que el nombre de columna utilizado en el archivo `.qml` coincida con el de su capa. Para ello, abra la página **Tabla de atributos** de la capa y compare los nombres de los campos.*

---


:::::{tab-set}

::::{tab-item} Resultado intermedio: Población expuesta

:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_pop_style.PNG
---
width: 600px
align: center
---
Mapa que muestra el número de personas expuestas por distrito después de aplicar el estilo .qml.
:::
::::
::::{tab-item} Resultado intermedio: Instalaciones sanitarias expuestas
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_HS_sum_style.PNG
---
width: 600px
align: center
---
Mapa que indica el número total de establecimientos de salud expuestos por distrito, representados con el estilo predefinido.
:::
::::
::::{tab-item} Resultado intermedio: Instalaciones educativas expuestas
:::{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_ES_sum_style.PNG
---
width: 600px
align: center
---
Mapa que muestra el número total de establecimientos educativos expuestos por distrito, tras la aplicación del archivo de estilo .qml.
:::
::::
:::::



### 3. **Estilizar capas porcentuales manualmente**

Aina también quiere visualizar el porcentaje de instalaciones sanitarias y educativas expuestas. Sin embargo, como no hay ningún estilo preparado disponible, debe completar el proceso manualmente.

**Pasos:**
- **Haga clic derecho** en la capa `adm2_centros_salud_expuestos` → seleccione **Duplicar capa**.
- **Cambie el nombre** de la capa duplicada a:
  ```
  adm2_pct_expuesto_centros_salud
  ```
- Haga clic derecho sobre la capa en el **Panel de capas**
- Seleccione **Propriedades**
- En la ventana que se abre, vaya a la pestaña **Simbología**
- Configure la simbología a `Graduado`
- Elija el **campo** correcto:
  - `pct_expuesto_centros_salud`
- Abra la pestaña **Histograma** para ver la distribución de valores haciendo clic en `Cargar valores`
- A continuación, vuelva a `Clases` y establezca la siguiente configuración:
  - **Modo**: `Intervalo igual`
  - **Clases**: `4`
- Haga clic en `Aceptar`. Se crearán cuatro clases (`0–25%`, `25–50%`, `50–75%`, `75–100%`).
- Elija una rampa de color (por ejemplo, amarillo claro → rojo oscuro).
- Opcionalmente, personalice las etiquetas de las clases para mayor claridad
- Haga clic en `Apliquar`.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_affacted_HS_pct.mp4"></video>

- Repita el mismo proceso para la capa `adm2_educación_expuesta`.
Después de duplicar la capa, cambie el nombre de la nueva a:
```
adm2_pct_educación_expuesta
```


🧠 *¿Por qué 4 clases iguales?* 
Esto ayuda a visualizar la gravedad en todos los distritos mediante categorías de riesgo sencillas e interpretables. Sin embargo, puede experimentar con **cortes naturales** si los datos están distribuidos de forma desigual.

---

### 4. **Guarde sus nuevos estilos para volver a utilizarlos.**

Guarde los estilos creados manualmente como archivos `.qml` para reutilizarlos en el futuro.

**Pasos:**
- Haga clic derecho sobre la capa en el **panel de capas**
- Seleccione **Propriedades**
- En la ventana que se abre, vaya a la pestaña **Simbologia **
- Haga clic en `Estilo` → `Guardar estilo`.
- Guarde el archivo en la carpeta `layer_sytle`.
- Utilice estos nombres de archivo:
  ```
  adm2_pct_expuesto_centros_salud
  ```
  ```
  adm2_pct_educación_expuesta
  ```


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_save_new_style.mp4"></video>


### 5. *(Opcional)* Importar estilos a su biblioteca QGIS

Para reutilizar sus estilos en cualquier proyecto futuro:

- Vaya a `Configuración` → `Administrador de estilos`.
- Haga clic en `Importar / Exportar` → `Importar elementos`.
- Busque los archivos `.qml` guardados y selecciónelos.

Los estilos aparecerán ahora como ajustes preestablecidos en **Panel de estilos de capa**.

---
