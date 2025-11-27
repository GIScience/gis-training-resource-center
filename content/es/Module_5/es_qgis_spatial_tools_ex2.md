::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/es/content/es_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 1: Parte 1: Calcular el índice de vulnerabilidad

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}

### Objetivo del ejercicio
Queremos crear una visión general de diferentes indicadores de vulnerabilidad. Usando un conjunto de datos de indicadores de riesgo de Covid-19, tomamos `% permanent wall type`, `% permanent roof type` y `poverty incidence`. Usando estadísticas de población de Uganda, calculamos el `% of under fives` y el `% of elderly`. Combinando los datos, ahora podemos visualizar las áreas en Uganda que son más vulnerables.

#### Tipo de ejercicio de capacitación:

- Este ejercicio puede utilizarse en formaciones en línea o presenciales. 
- Puede hacerse como un ejercicio guiado o de forma individual como autoestudio.

:::

:::{grid-item-card}

#### Grupo destinatario (Nivel de conocimiento en SIG)


#### Estas habilidades son relevantes para 


:::
::::

::::{grid} 2
:::{grid-item-card}

#### Tiempo estimado necesario para el ejercicio.

 

:::

:::{grid-item-card}

## Artículos relevantes del Wiki

* [Importación de Geodatos en QGIS](/content/es/Wiki/en_qgis_import_geodata_wiki.md)
* [Proyecciones](/content/es/Wiki/en_qgis_projections_wiki.md)
* [Geoprocesamiento](/content/es/Wiki/en_qgis_geoprocessing_wiki.md)
* [Uniones espaciales](/content/es/Wiki/en_qgis_spatial_joins_wiki.md)

:::

::::

## Instrucciones para los formadores

:::{dropdown} __Rincón de formadores__ 

### Preparar la formación

- Tómese tiempo para familiarizarse con el ejercicio y el material proporcionado.  
- Prepare una pizarra. Puede ser una pizarra física, un rotafolio o una pizarra digital (por ejemplo, un tablero Miro) donde los participantes puedan añadir sus hallazgos y preguntas.  
- Antes de empezar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.  
- Consulte [¿Cómo realizar formaciones?](/content/es/Trainers_corner/es_how_to_training.md) para consejos generales sobre la conducción de formaciones.

### Impartir la formación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.  
- Proporcione el enlace de descarga y asegúrese de que todos hayan descomprimido la carpeta antes de comenzar las tareas.

__Ejercicio guiado:__

- Muestre y explique cada paso usted mismo al menos dos veces, y lo suficientemente despacio para que todos puedan ver lo que hace y seguirlo en su propio proyecto QGIS.  
- Asegúrese de que todos sigan el ritmo y realicen los pasos por sí mismos preguntando periódicamente si alguien necesita ayuda o si todos siguen.  
- Sea abierto y paciente con cualquier pregunta o problema que pueda surgir. Los participantes están esencialmente haciendo multitarea: prestando atención a sus instrucciones y orientándose en su propio proyecto QGIS.

__Cierre:__

- Deje tiempo al final para resolver dudas o problemas relacionados con las tareas.  
- Deje también tiempo para preguntas abiertas. 

:::


### Datos
Descargue todos los conjuntos de datos, guarde la carpeta en su ordenador y descomprima el archivo. La carpeta zip incluye:
- `uga_admbnda_adm2_ubos_20200824.shp`: [Límites distritales de Uganda (nivel administrativo 2)](https://data.humdata.org/dataset/cod-ab-uga)
- `COVID19_RISK_INDEX.shp`: [Indicadores de riesgo de Covid-19](https://data.humdata.org/dataset/covid19_risk_index)


```{Hint}
Todos los archivos mantienen sus nombres originales. Sin embargo, si es necesario, puede modificarlos para identificarlos más fácilmente.
```

### Tarea
Esta primera parte del ejercicio preparará los datos para posteriores procesos no espaciales, como trabajar con la tabla de atributos. Para calcular el índice de vulnerabilidad, uniremos todos los datos relevantes mediante geoprocesamiento espacial en una sola capa vectorial.

1. Cargue en QGIS los límites distritales de Uganda (nivel administrativo 2) (`uga_admbnda_adm2_ubos_20200824.shp`), así como las estadísticas de población (`uga_admpop_adm2_2020proj_1y.csv`) y los indicadores de riesgo de Covid-19 (`COVID19_RISK_INDEX.shp`).

2. Asegúrese de reproyectar el conjunto de datos de los __límites distritales__ y los __indicadores de riesgo de Covid-19__ a UTM zona 36N. Utilice la herramienta `Reproyectar capa` para este proceso. Consulte la entrada del Wiki sobre [proyecciones](/content/es/Wiki/es_qgis_projections_wiki.md) para obtener más información.

```{Attention}
Antes de comenzar cualquier operación GIS, __siempre explore los datos__. Compruebe siempre si las proyecciones de las distintas capas coinciden.
```

```{Hint}
El sistema de coordenadas proyectadas para Uganda es `EPSG:32636 WGS 84 / UTM zone 36N`. Si necesita un sistema de coordenadas proyectadas para cualquier región del mundo, puede encontrar buenos ejemplos en [epsg.io](https://epsg.io).
```

3. Podemos ver que los polígonos difieren en forma y cantidad. Probablemente los datos de riesgo utilizan una versión más antigua de los límites administrativos. ¡Es un problema que debemos resolver para trabajar adecuadamente con los datos!

```{figure} /fig/en_ex3_1_attribute_table_size.png
---
width: 100%
name: attribute_table_size
---
Captura de pantalla de diferentes tamaños de las tablas de atributos
```

4. Usaremos la siguiente solución para este problema:
    - Tomaremos el __centroide del distrito más cercano__ (del conjunto con más registros al conjunto con menos). Esta es la solución que utilizaremos en el ejercicio, ya que la diferencia entre los conjuntos no es drástica.

5. Calcule los ![](/fig/mAlgorithmCentroids.png) `Centroides` para el conjunto que contiene más elementos, es decir, los límites distritales. La herramienta está en `Vectorial` --> `Geometry Tools` --> `Centroides`. Consulte la entrada del Wiki sobre [Geoprocesamiento](/content/Wiki/en_qgis_geoprocessing_wiki.md) para más información.

6. Edite los puntos para que queden dentro de los polígonos correctos. Esto es necesario porque el __centroide de un polígono puede quedar fuera__ cuando tiene una __forma inusual__. Para mover un centroide fuera de sus límites hacia el distrito correcto, active primero `Conmutar edicion`, haciendo clic en ![](/fig/mActionToggleEditing.png) con la capa de centroides activa. Luego seleccione ![](/fig/mActionMoveFeaturePoint.png) `Mover Objeto` (desde la barra de herramientas `Digitalizaciòn avanzada). Localice el centroide fuera de su polígono y muévalo al distrito adecuado. Guarde los cambios y salga del modo de edición.

```{figure} /fig/en_centroids_screenshot_red.png
---
width: 80%
name: en_qgis_centroids
---
Los puntos negros representan los centroides de las entidades de la capa de entrada. El círculo rojo indica el centroide que requiere edición.
```

7. Hay un problema que aparece al unir los conjuntos de datos, pero puede resolverse usando la herramienta `Corregir geometrías` en el conjunto de riesgo de Covid-19.

```{figure} /fig/en_ex3_1_fix_geometries.PNG
---
width: 60%
name: fix_geometries
---
Captura de pantalla de cómo corregir las geometrías.
```

8. Use la herramienta `Unir objetos por localizaciòn` para unir los polígonos de riesgo de Covid-19 a los centroides. Como relación espacial seleccione `están dentro` y seleccione las columnas `%permrooft`, `%permwallt` y `Povertyinc` como campos a añadir. Consulte el Wiki sobre [uniones espaciales](/content/es/Wiki/es_qgis_spatial_joins_wiki.md) para más información.

```{figure} /fig/en_ex3_1_join_attribute_location_1.PNG
---
width: 60%
name: join_attribute_by_location
---
Captura de pantalla de la operación Unir objetos por localizaciòn.
```

9. Utilice nuevamente `Unir objetos por localizaciònn` para unir los puntos enriquecidos a los límites distritales de Uganda. Ahora seleccione “contienen” como relación espacial y seleccione de nuevo las mismas tres columnas.

```{figure} /fig/en_ex3_1_join_attribute_location_2.PNG
---
width: 60%
name: join_attribute_by_location_2
---
Captura de pantalla de la segunda operación Unir objetos por localizaciòn.
```

% Los siguientes pasos del cálculo del índice de vulnerabilidad se completarán en la segunda parte de este ejercicio, dentro de la sección de Geoprocesamiento No Espacial. Consulte el [enlace proporcionado](/content/es/Module_6/en_qgis_non_spatial_tools_ex2.md) para este ejercicio.
