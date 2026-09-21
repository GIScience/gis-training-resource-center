::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../es_intro.md
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

Este ejercicio forma parte del [programa de ejercicios de análisis de ciclones de acción anticipatoria de Madagascar.](../Exercise_tracks/es_mdg_aa_cyclones.md)

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

* [Estadísticas zonales](../Wiki/es_qgis_raster_basic_wiki.md)
* [Intersección](../../en/Wiki/en_qgis_spatial_joins_wiki.md#join-attributes-by-location-summary)
* [Proyecciones cartográficas](../Wiki/es_qgis_projections_wiki.md)
* [Buffer](../Wiki/es_qgis_projections_wiki.md)
* [Recorte](../Wiki/es_qgis_projections_wiki.md)
* [Automatización](../Wiki/es_qgis_automation_wiki.md)

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
- Consulte [¿Cómo realizar capacitaciones?](../Trainers_corner/es_how_to_training.md) para obtener algunos consejos generales para impartirlas.

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

__Contexto:__

Cuando se pronostica que un ciclón tocará tierra, Aina trabaja con los equipos de logística y salud para decidir **a dónde enviar los kits médicos preposicionados**. Sin embargo, no todos los almacenes de la CRM tienen los artículos necesarios — solo tres los almacenan.

Para tomar decisiones rápidas y basadas en datos, Aina necesita saber **qué puestos de salud son alcanzables** desde esos almacenes **en un máximo de 10 horas**. Este análisis ayuda a garantizar que los kits se envíen a instalaciones **que realmente pueden ser alcanzadas a tiempo**.

Su objetivo es crear un mapa visual claro que muestre los puestos de salud alcanzables y no alcanzables — y compartirlo con los responsables de la toma de decisiones lo más rápido posible.

# Tareas

## 1. Filtrar los puestos de salud del conjunto nacional de establecimientos sanitarios

Antes de comprobar qué instalaciones son alcanzables, Aina necesita aislar los **puestos de salud** del conjunto más amplio de todos los establecimientos sanitarios.

1. **Cargar el conjunto de datos de establecimientos sanitarios**  
   - Archivo: `hotosm_mdg_health_facilities_points.gpkg` (o el GeoPackage correspondiente que esté utilizando)  
   - Cárguelo arrastrando y soltando o a través de `Capa` → `Añadir capa vectorial`.
2. **Abra la tabla de atributos** y revise la columna `amenity`.
3. **Filtrar por expresión** para conservar únicamente los puestos de salud:  
   - Clic derecho en la capa → `Filtro…`  
   - Utilice la siguiente expresión:
     ```qgis
     "amenity" = 'health_post'
     ```
4. **Exportar la capa filtrada**  
   - Clic derecho en la capa filtrada en el panel de capas → `Exportar` → `Guardar elementos como…`  
   - Formato: `GeoPackage`  
   - Guardar en su carpeta `project` como:
     ```
     health_posts_only.gpkg
     ```
   - Hacer clic en `OK` para confirmar la exportación.
5. **Eliminar el filtro** o la capa original del proyecto para evitar confusiones.

> 💡 **Consejo**: Filtrar directamente en QGIS le permite trabajar con un subconjunto específico sin modificar el conjunto de datos original.

## 2. Cargar las capas de isocronas de los tres almacenes de la CRM

Aina sabe que solo **tres almacenes** tienen los suministros médicos necesarios:  
**Antananarivo**, **Maroantsetra** y **Tolanaro**. Ahora cargará las capas de isocronas para cada uno de estos almacenes para comenzar a analizar las áreas de servicio.

1. **Cargar las capas individuales de isocronas** de cada almacén:
   - `CRM_warehouse_Isochrones_Antananarivo.gpkg`
   - `CRM_warehouse_Isochrones_Maroantsetra.gpkg`
   - `CRM_warehouse_Isochrones_Tolanaro.gpkg`

   Puede arrastrar y soltar cada archivo en QGIS o ir a `Capa` → `Añadir capa` → `Añadir capa vectorial`.

2. **Inspeccionar la tabla de atributos** de cada capa de isocronas  
   Confirme que cada registro tenga un campo `traveltime_h` que indique el tiempo de viaje estimado en **horas**.

3. **Eliminar todos los elementos cuyo tiempo supere las 10 horas**:  
   - Clic derecho en cada capa → `Filtro…`
   - Aplicar la expresión:
     ```qgis
     "traveltime_h" <= 10
     ```

4. **Exportar cada capa filtrada** a la carpeta `temp` :  
   En este punto, Aina también se asegura de que todas las capas exportadas se guarden en el mismo CRS que el conjunto de datos de los puestos de salud — `EPSG:4326` — para evitar problemas en la unión espacial.
   - Guardar cada una como:
     ```
     CRM_isochrones_Antananarivo_upto10h.gpkg
     CRM_isochrones_Maroantsetra_upto10h.gpkg
     CRM_isochrones_Tolanaro_upto10h.gpkg
     ```

5. **Aplicar estilo a las isocronas para mayor claridad**  
   Aina puede aplicar un archivo de estilo predefinido para colorear la capa según `traveltime_h` y visualizar diferentes bandas de tiempo (4h, 6h, 8h, 10h) más adelante en el Paso 5.
   - Clic derecho en cada capa filtrada → `Propiedades` → `Simbología`
   - Clic en `Estilo` (parte inferior) → `Cargar estilo…`
   - Seleccionar:
     `CRM_warehouse_isochrones_style.qml`
   - Clic en `Abrir`, luego `Aplicar` y `Aceptar`

## 3. Visualizar la alcanzabilidad de los puestos de salud desde los almacenes de la CRM

Aina necesita identificar qué puestos de salud pueden ser alcanzados por carretera desde los tres almacenes clave de la CRM (Antananarivo, Maroantsetra y Tolanaro) **en un máximo de 10 horas de viaje**. Lo hará manualmente combinando las isocronas de 10 horas de estos almacenes y comparándolas con el conjunto nacional de puestos de salud.
1. **Combinar las capas de isocronas de los tres almacenes**  
   - En la **Caja de herramientas de procesos**, busque `Unir capas vectoriales (Merge Vector Layers)`.  
   - **Capas de entrada**:  
     - `CRM_isochrones_Antananarivo_upto10h.gpkg`  
     - `CRM_isochrones_Maroantsetra_upto10h.gpkg`  
     - `CRM_isochrones_Tolanaro_upto10h.gpkg`  
   - **CRS**: `EPSG:4326`  
   - **Guardar en archivo**:  
     ```
     merged_isochrones_10h.gpkg
     ```  
   - Clic en **Ejecutar**.
2. **Seleccionar los puestos de salud alcanzables en 10 horas**  
   - En la **Caja de herramientas de procesos**, busque `Seleccionar por ubicación (Select by Location)`.  
   - Configure los parámetros:  
     - **Capa de entrada**: centros de salud  
     - **Predicado**: `intersects`  
     - **Capa de intersección**: `merged_isochrones_10h.gpkg`  
   - Clic en **Ejecutar**.
   > 💡 Los puntos seleccionados son aquellos dentro de las áreas de servicio de 10 horas de los almacenes.
3. **Crear un campo de alcanzabilidad para los puestos de salud seleccionados**  
   - Abra la **Calculadora de campos** ![](../../../fig/mActionCalculateField.png) en la capa `health_posts_only`.  
   - Marque ✅ `Actualizar solo las entidades seleccionadas`  
   - **Nombre del campo de salida**: `Reachability_time`  
   - **Tipo de campo de salida**: `Texto (string)`  
   - **Expresión**:
     ```qgis
     'reachable in 10 hours'
     ```  
   - Clic en **OK** para crear y rellenar el campo.
4. **Marcar los puestos de salud restantes como no alcanzables**  
   - Invertir la selección:  
     `Editar` → `Invertir selección` ![](../../../fig/mActionInvertSelection.png)  
     o clic derecho en la capa → `Invertir selección`.  
   - Abra nuevamente la **Calculadora de campos**.  
   - Marque ✅ `Actualizar solo las entidades seleccionadas`  
   - Use el mismo campo: `Reachability_time`  
   - **Expresión**:
     ```qgis
     'not reachable in 10 hours'
     ```  
   - Clic en **OK** para aplicar la actualización.

> ✅ Ahora todos los puestos de salud están etiquetados como **alcanzables** o **no alcanzables** en la columna `Reachability_time`.

