::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Ejercicio 1: Distribución de los centros de salud en la región de San Luis

## Características del ejercicio

::::{grid} 2
:::{grid-item-card}
__Objetivo del ejercicio:__
^^^

Familiarizarse con distintos tipos de herramientas de geoprocesamiento y análisis espacial. Comprender el proceso de descubrimiento de relaciones y conexiones entre entidades en datos espaciales.

__Tipo de ejercicio de capacitación:__

- Este ejercicio puede utilizarse tanto en la capacitación en línea como en la presencial.
- Puede realizarse como ejercicio guiado o individualmente a modo de autoestudio.

:::

:::{grid-item-card}
__Grupo focal (Nivel de conocimientos SIG):__
^^^

__Estas habilidades son relevantes para:__


:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

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
- Consulte [¿Cómo realizar capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener algunos consejos generales para impartirlas.

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

### Datos

Descargue los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Exercise_1/Module_5_Exercise_1_Healthsite_distribution_Saint_Louis_region.zip) y descomprima los archivos.

<!---Download all datasets and save the folder on your computer and unzip the file. The zip folder includes:
- `sen_healthsites.shp`: [Senegal health site data](https://data.humdata.org/dataset/senegal-healthsites)
- `sen_admbnda_adm1_1m_gov_ocha_20190426.shp`: [Senegal boundary data (Admin level 1)](https://data.humdata.org/dataset/senegal-administrative-boundaries)
- `EO4SD_SAINT_LOUIS_FLOOD_2018.shp`: [Saint Louis flood extend data](https://wbwaterdata.org/dataset/saint-louis-senegal-flood-risk-map-esa-eo4sd-urban)-->

:::{Hint}
Todos los archivos conservan sus nombres originales. No obstante, no dude en modificar sus nombres si fuera necesario para identificarlos más fácilmente.
:::

### Tarea

El objetivo de este ejercicio será evaluar la distribución de los centros de salud en la región de Saint Louis, en Senegal, y determinar qué centros de salud son propensos a las inundaciones.

:::{Hint}
El sistema de coordenadas previsto para Senegal es `EPSG:32628 WGS 84 / UTM zone 28N`
:::

1. Cargue la capa de centros de salud (`sen_healthsites.shp`) y los datos de límites administrativos (`sen_admbnda_adm1_1m_gov_ocha_20190426.shp`) en su proyecto QGIS. Añada OpenStreetMap como capa de fondo (sugerencia: XYZ a través de la ventana del navegador o del complemento QuickMapServices).

:::{attention}
Asegúrese siempre de que sus conjuntos de datos se ponen en la proyección correcta. Si no es el caso, es necesario reproyectar los datos en el sistema de referencia de coordenadas deseado. Para obtener más información, consulte la entrada de Wiki sobre [proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md).
:::

2. Seleccione todos los centros de salud situados en la región de San Luis:
    - Seleccione la región `Saint Louis` en la capa límite. Puede seleccionar manualmente las filas específicas. Para obtener más información, consulte la entrada de Wiki sobre [consultas espaciales](/content/es/Wiki/es_qgis_spatial_queries_wiki.md).
    - Guarde la selección con el nuevo nombre `Saint_Louis_region` en una capa adicional. Para ello, haga clic con el botón derecho en la capa límite → `Exportar` → `Guardar objetos seleccionados como...`

:::{figure} /fig/en_ex2_export_selected.PNG
---
width: 40%
name: es_export_selected_features
---
Captura de pantalla de cómo exportar las entidades seleccionadas.
:::

3. Utilice la herramienta ![](/fig/mAlgorithmSelectLocation.png) `Seleccionar por ubicación` o ![](/fig/mAlgorithmClip.png) `Cortar` para seleccionar todos los centros de salud dentro de la capa `Saint_Louis_region`.
    - Guarde la nueva selección con el nuevo nombre `healthsites_Saint_Louis` en una capa adicional (sugerencia: haga clic con el botón derecho sobre la capa, Exportar, etc.).

:::{figure} /fig/en_ex2_select_by_location.PNG
---
width: 70%
name: es_select_by_location
---
Captura de pantalla de la herramienta de selección por ubicación.
:::

4. Investigue el riesgo de inundación en San Luis. Tras la selección satisfactoria de todos los centros de salud de la región de San Luis en el paso anterior, proceda a cargar la capa de extensión de la inundación de San Luis en QGIS:
    - Añada la capa de extensión de la inundación (`EO4SD_SAINT_LOUIS_FLOOD_2018.shp`)
    - Aunque la capa no cubre la totalidad de la región de San Luis, se extiende más allá de San Luis en el norte. Utilice la herramienta ![](/fig/mAlgorithmClip.png) `Cortar` para recortar la capa de extensión de la inundación a la región de San Luis (sugerencia: como entrada utilice la extensión de la inundación de San Luis, utilice Saint_louis_region como superposición) para un enfoque más concentrado en el centro de San Luis. Para obtener más información, consulte la entrada de Wiki sobre [geoprocesamiento](/content/es/Wiki/es_qgis_geoprocessing_wiki.md).
    - Guarde la selección como `Saint_Louis_flood_clipped`.

5. Al consultar la tabla de atributos de la capa `Saint_Louis_flood_clipped` (columna Watertype), verá que la capa incluye zonas inundadas, no inundadas y masas de agua.

:::{figure} /fig/en_ex1_attribute_table_floods.PNG
---
width: 40%
name: es_attribute_table_floods
---
Captura de pantalla de la capa Saint_Louis_flood_clipped
:::

6. Visualice solo las zonas inundadas y las masas de agua del conjunto de datos:
    - Vaya a `Simbología` y cambie la primera selección de `Símbolos Únicos` a `Categorizado`.
    - `Valor`: Seleccione la columna `Watertype` y haga clic en `Clasificar`.
    - Elija colores diferentes para las masas de agua y las zonas inundadas. Deje las zonas no inundadas sin marcar o hágalas transparentes (opacidad = 0%).
    - Exploración visual: ¿Qué zonas son más y menos propensas a las inundaciones?

:::{figure} /fig/en_ex2_screenshot_flood.PNG
---
width: 40%
name: es_screenshot_flood
---
Captura de pantalla de las masas de agua y las zonas inundadas. 
:::

7. Evalúe qué centros de salud están expuestos al riesgo de inundación.
    - Utilice la herramienta `Seleccionar por expresión` para seleccionar todas las zonas inundadas en la capa `Saint_Louis_flood_clipped`. Puede acceder a esta herramienta a través de la tabla de atributos haciendo clic en este símbolo ![](/fig/mIconExpressionSelect_new.png)

:::{figure} /fig/en_ex2_select_by_expression.PNG
---
width: 70%
name: es_select_by_expression
---
Captura de pantalla de la herramienta Seleccionar por expresión.
:::

8. Guarde la selección en una capa separada. Nómbrelo `Saint_Louis_flooded_areas`.

9. Ahora puede eliminar la capa `Saint_Louis_flood_clipped` para evitar confusiones.
    - Utilice la herramienta ![](/fig/mAlgorithmSelectLocation.png) `Seleccionar por ubicación` para evaluar qué centros de salud son propensos a las inundaciones por estar situados dentro de las zonas inundadas de San Luis (sugerencia: Seleccione las entidades de: `healthsites_Saint_Louis`; comparando con: `Saint_Louis_flooded_areas`).

:::{figure} /fig/en_ex2_select_by_location_health.PNG
---
width: 70%
name: es_select_by_location
---
Captura de pantalla de la herramienta Seleccionar por ubicación.
:::

10. Compruebe la tabla de atributos de la capa `healthsites` para las entidades seleccionadas: una farmacia y un hospital.

:::{figure} /fig/en_ex1_selected_healthsites_senegal.PNG
---
width: 60%
name: es_selected_healthsites_senegal
---
Captura de pantalla de los centros de salud seleccionados en las zonas inundadas.
:::

11. ¿Qué centros de salud están situados cerca de zonas inundadas?
    - Cree una zona de influencia![](/fig/mAlgorithmBuffer.png) alrededor de los centros de salud de San Luis con una distancia de `20 meters`. Para obtener más información, consulte la entrada de Wiki sobre [geoprocesamiento](/content/es/Wiki/es_qgis_geoprocessing_wiki.md).

:::{figure} /fig/en_ex2_buffer.PNG
---
width: 60%
name: es_ex2_buffer
---
Captura de pantalla del proceso de zona de influencia.
:::

:::{Hint}
A más tardar en esta fase, recibirá un recordatorio de que debe reproyectar las capas. Las zona de influencia significativas solo pueden calcularse en sistemas de coordenadas proyectadas. El sistema de coordenadas previsto para Senegal es `EPSG:32628 WGS 84 / UTM zone 28N`
:::

12. Ahora vuelva a utilizar la herramienta ![](/fig/mAlgorithmSelectLocation.png) `Seleccionar por ubicación` para evaluar qué zonas de influencia se intersecan con las zonas inundadas.

:::{figure} /fig/en_ex1_select_healthsites_buffer.PNG
---
width: 60%
name: es_ex1_select_healthsites_buffer
---
Captura de pantalla de la herramienta Seleccionar por ubicación para las zonas de influencia.
:::

13. ¿Cuántos centros de salud se seleccionaron? Compruebe la tabla de atributos. La selección debe incluir cinco farmacias y un hospital.
    - No dude en experimentar con distancias de zona de influencia adicionales.

:::{figure} /fig/en_ex1_selected_flooded_healthsites.PNG
---
width: 60%
name: es_ex1_selected_flooded_healthsites
---
Captura de pantalla de los centros de salud seleccionados en las zonas inundadas.
:::

El resultado final puede representarse del siguiente modo: mostrará las zonas inundadas, los centros de salud de la zona de influencia y las intersecciones entre ellos. Aunque estas entidades no sean fácilmente visibles en QGIS, puede comprobar que todo ha funcionado correctamente consultando la tabla de atributos.

:::{figure} /fig/en_ex1_final_result.PNG
---
width: 60%
name: es_ex1_final_result
---
Captura de pantalla del resultado final.
:::


