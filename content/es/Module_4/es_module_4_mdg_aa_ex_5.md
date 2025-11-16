::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::


# Ejercicio 5: Creación rápida de mapas: Aina utiliza plantillas de mapas

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
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_4_Exercise_7_AA_MDG_task_5-20250825T143511Z-1-001.zip

__Descargue todos los conjuntos de datos aquí, guarde la carpeta en su computadora y descomprima el archivo.__
:::


## Contexto

Después del arduo trabajo de analizar datos y capas de estilo, Aina está lista para **compartir sus resultados**. Aunque crear un mapa de aspecto profesional desde cero cada vez sería lento y repetitivo.

Para ahorrar tiempo, utiliza las plantillas de mapas **(archivos .qpt)** preparadas por su equipo. Estas plantillas ya contienen los elementos esenciales: marcos de mapa, leyendas, logotipos, títulos y barras de escala. Con ellas, Aina puede convertir su análisis en un **mapa limpio y coherente** en unos pocos clics.

✅ **Objetivo** 
Utilice una plantilla de mapas de QGIS ya preparada para crear y exportar rápidamente mapas que muestren los impactos de los ciclones en la población, los centros sanitarios y las escuelas.


## Tareas:



1. Cargar el diseño de diseño de impresión prediseñada

- Localice la plantilla `cyclone_impact_population_map_template.qpt` en la carpeta de su proyecto: 
`Map_Templates/`

- Puede cargar la plantilla mediante la función de **arrastrar y soltar**:
  - Abra su proyecto QGIS.
  - Arrastre el archivo `.qpt` directamente a QGIS: se creará automáticamente un nuevo diseño.

- Alternativamente:
  - Vaya a `Project` → `New Print Layout`.
  - Introduzca un nombre (por ejemplo, `Harald_2025_population`).
  - Haga clic en `OK`.
  - En el diseño, vaya a `Layout` → `Import from Template…`.
  - Seleccione el archivo `cyclone_impact_overview_map_template.qpt` y haga clic en `Open`.
 2. Comprobar y ajustar el tamaño de página
- Haga clic derecho en cualquier parte del lienzo blanco y elija `Page Properties`.
- En el panel de la derecha, asegúrese de lo siguiente:
  - **Tamaño de página**: A3
  - **Orientación**: Horizontal

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_load_mpa_template.mp4"></video>

3. Actualizar la tabla de atributos de los distritos expuestos
- En el **diseño de impresión**, haga clic en la tabla de atributos (parte derecha del diseño).
- En el panel **Item Properties**:
  - Asegúrese de que está seleccionada la capa correcta `Harald_Exposed_population`.
  - Haga clic en `Refresh Table Data`.
  - Haga clic en `Attributes…` → en la parte superior en **Campos** haga clic en `Clear`.
    - A continuación, añada la siguiente capa haciendo clic en ➕ :
    - **Atributo**: `ADM1_EN`; `ADM2_EN`; `ADM2_PCODE`; `exposed_population_sum`
    - Para ordenar el contenido de la pestaña, en **Ordenar** haga clic en ➕ y añada la columna `AMD1_EN`.
    - **Orden de clasificación**: Ascendente
  - Haga clic en `OK`.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_makingadjust_AT.mp4"></video>


:::{admonition} ⚠️ Advertencia: Tablas largas
Si la tabla de atributos que desea incluir es **más larga que el marco del mapa**, parte de ella quedará cortada en el mapa exportado. 
Para solucionarlo, abra las propiedades de la tabla en el diseño y **reduzca el tamaño de la fuente** hasta que quepa toda la tabla. 
:::


5. Ajustar la leyenda
- En el diseño, haga clic en el elemento **Legend**.
- En el panel **Item Properties**:
  - Desmarque **Auto update**.
  - Desplácese hasta **Legend items** y elimine todas las entradas (🗑️).
  - Añada las siguientes capas relevantes:
    - `example_Harald_2025_Track`
    - `cyclone_harald_buffer`
    - `Harald_Exposed_Population`
  - Al seleccionar capas, marque **Only visible layers**.
  - Renombrar las entradas de la leyenda para que coincidan con la nomenclatura del diseño.
    - `example_Harald_2025_Track` ->
     ```
     Seguimiento del ciclón Harald
     ```
    - `cyclone_harald_buffer`->
     ```
     Zona de influencia de 200 km frente al ciclón Harald
     ```
    - `Harald_Exposed_Population`->
     ```
     Número de personas expuestas
     ```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_adjust_map_making_Legend.mp4"></video>

6. **Actualizar logotipos e iconos**
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
- Ajuste el tamaño de letra o la alineación si es necesario

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_mak_making_adjust_title.mp4"></video>

### ✅ Lista de control final

| Tarea | Hecho |
|------------------------------------------------|------|
| Página ajustada a A3 Horizontal | ☐ |
| Solo el grupo de capas relevante está activo | ☐ |
| Actualización de la tabla de atributos de los distritos expuestos | ☐ |
| Leyenda limpia y renombrada | ☐ |
| Todos los elementos de texto actualizados | ☐ |

---



::::{dropdown} El resultado final debería ser el siguiente después de aplicar el estilo a la capa.
El mapa muestra ahora claramente la población expuesta dentro de los distritos afectados. Se resalta la línea original de la trayectoria de la tormenta, utilizada como datos de entrada, y la zona buffer de impacto, que sirve como indicador para identificar los distritos expuestos.

En la parte derecha del mapa, una lista muestra todos los distritos expuestos, con datos sobre la población total y la población expuesta. Los distritos (Admin 2) están organizados bajo sus correspondientes regiones (Admin 1).

:::{figure} /fig/MAD_Trigger_Impact_Population_Map_example.png
---
width: 1000px
name:
align: center
---
:::
::::