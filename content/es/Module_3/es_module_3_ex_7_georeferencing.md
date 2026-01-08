::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Ejercicio 7: Georreferenciación de un mapa de Somalia

:::{card}
__Objetivo del ejercicio:__
^^^

El objetivo de este ejercicio es que aprenda a georreferenciar un mapa. En muchos casos, las instituciones (gubernamentales) solo
publican datos o mapas en formato PDF. Sin embargo, al georreferenciar el mapa, es posible importarlo como un conjunto de datos ráster en el proyecto de QGIS. Luego, se puede usar para digitalizar entidades vectoriales o se pueden usar los valores de ráster en un análisis de datos ráster.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación__
^^^

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Digitalizar mapas
- Preparar datos para el análisis espacial

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
^^^
~ 90 minutos

:::

:::{grid-item-card}
__Artículos relevantes__
^^^

* [Georreferenciación](/content/es/Module_3/es_qgis_georeferencing.md)
:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser una pizarra física, un rotafolio o una pizarra digital (p. ej., una pizarra en Miro) en la que los participantes puedan agregar sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener consejos generales sobre cómo impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos hayan descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y aplicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su propio proyecto de QGIS.

__Cierre de la sesión:__

- Dedique tiempo al final del ejercicio a cualquier problema o pregunta relacionada con las tareas que pueda surgir.
- Reserve tiempo para preguntas abiertas.

:::

## Instrucciones paso a paso

:::{card}
:class-card: sd-text-justify sd-rounded-2 sd-border-1
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_7/Module_3_Exercise_7_Georeferencing.zip


__Haga clic [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_7/Module_3_Exercise_7_Georeferencing.zip) para descargar los conjuntos de datos para este ejercicio.__

:::

:::{card}
__Datos disponibles:__
^^^

- `SOM_soil_deg.png` - Una imagen de un mapa de degradación del suelo de Somalia tomada de un informe en PDF (fuente: [FAO SWALIM](https://www.faoswalim.org/resources/site_files/L-14%20Land%20Degradation%20and%20a%20Monitoring%20Framework%20in%20Somalia_0.pdf))
- `som_admbnda_adm1_ocha_20230308.gkpg` - Una capa vectorial con los límites administrativos de las regiones (adm1) de Somalia (fuente: OCHA)

:::

### Preparación de los datos

1. Descomprima la carpeta y mire el mapa de degradación del suelo para familiarizarse con los datos. El mapa está en la carpeta `Module_3_Exercise_7_Georeferencing/data/input/`.
2. Cree un nuevo proyecto en QGIS.

:::{figure} /fig/SOM_Soil_deg.png
---
name: es_SOM_soil_deg
width: 500 px
---
Degradación del suelo en Somalia
:::

### Paso 1: Agregar un mapa base y cargar la capa vectorial

La georreferenciación se realiza conectando los puntos del mapa que se georreferenciará a las coordenadas del lienzo del mapa en QGIS. Agregar un mapa base o una capa de referencia a su proyecto de QGIS le ayudará a identificar las coordenadas correspondientes.

1. Agregue un mapa base usando XYZ Tiles o el [complemento QuickMapServices](/content/es/Wiki/es_qgis_basemaps_wiki.md).
2. Importe la capa `som_admbnda_adm1_ocha_20230308` al proyecto de QGIS.

### Paso 2: Georreferenciar el mapa

Ahora que hemos preparado nuestro proyecto de QGIS, empecemos a georreferenciar el mapa.

3. Abra el Georreferenciador en la barra superior > `Capa` > `Georreferenciador` <!---(see {numref}`open_georeferencer`)-->

:::{figure} /fig/en_3.36_open_georefencer.png
---
name: es_open_georeferencer
width: 500 px
---
Abrir el Georreferenciador en QGIS 3.36.
:::

4. Se abrirá una nueva ventana. Este es el __georreferenciador__. Para agregar una imagen a la georreferencia, haga clic en ![](/fig/3.36_add_raster_georef.png) `Abrir ráster`.
5. Seleccione la imagen del mapa que desea georreferenciar. Haga clic en `Open` (`Module_3_Exercise_7_Georeferencing/data/input`).
6. La imagen aparecerá en el centro de la ventana del georreferenciador. Haga clic en ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. Se abrirá una nueva ventana. Aquí puede establecer el tipo de transformación y el sistema de referencia de coordenadas (SRC) objetivo. Para nuestro propósito, utilizaremos el tipo de transformación lineal. Como SRC objetivo, queremos utilizar el mismo que en nuestros otros datos. En nuestro caso, podemos usar EPSG:4326. A continuación, puede establecer el nombre y la ubicación de guardado del archivo. Asegúrese de que `Load in project when done` esté marcado.

::::{margin}

:::{note}
En la mayoría de los casos, puede dejar el tipo de transformación en `lineal`. Los mapas regionales suelen estar en una proyección cartográfica conforme (es decir, se conservan los ángulos). Las imágenes satelitales también. Si se da cuenta de que los ángulos no son correctos o que el mapa está deformado o distorsionado, es posible que tenga que elegir `polinomial` como tipo de transformación. Las transformaciones polinómicas necesitan más puntos de control terrestre y los puntos deben distribuirse uniformemente en el mapa.

Para obtener más información sobre los diferentes tipos de transformación en QGIS, consulte la [documentación de QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_raster/georeferencer.html#available-transformation-algorithms).
:::
::::

8. Haga clic en `Aceptar`.
9. Una vez que haya establecido el tipo de transformación, puede comenzar a agregar puntos de control terrestre (PCT) haciendo clic en ![](/fig/3.36_georef_add_point.png) `Add GCP Point`. Los puntos de control terrestre son puntos a los que asigna coordenadas geográficas específicas.
10. Haga clic en un punto de la imagen del mapa. Esta será la ubicación precisa que puede identificar tanto en el mapa base como en el mapa que desea georreferenciar.
11. Después de que haga clic en una posición, aparecerá una ventana nueva. Aquí, agregue las coordenadas al punto que seleccionó. Hay dos opciones para hacerlo:
    - Introducir las coordenadas manualmente. Necesitará conocer la coordenada exacta. A veces, en los mapas hay una cuadrícula de coordenadas.
    - Seleccionar los puntos ![](/fig/en_3.36_georef_select_from_canvas.png). Este modo minimizará el georreferenciador y abrirá el lienzo del mapa de QGIS. Amplíe la misma ubicación que seleccionó en el mapa no georreferenciado y haga clic una vez.
    - Una vez introducidas las coordenadas, haga clic en `Aceptar`
12. La ventana del georreferenciador se abrirá de nuevo. Esta vez, debajo de la imagen del mapa, podrá ver un punto en la tabla. Estos son los PCT. Continúe añadiendo más PCT. Repártalos por todo el mapa. Asegúrese de que el `Error medio` en la esquina inferior derecha de la ventana del georreferenciador sea lo más bajo posible (lo ideal es que sea menor a 5).

:::{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: es_georeferencer_dialogue
---
Diálogo de georreferenciación en QGIS 3.36
:::

13. Una vez que haya añadido suficientes puntos, haga clic en ![](/fig/3.36_start_georef.png) `Comenzar georreferenciado`. QGIS usará los puntos que haya añadido para transformar la imagen en una imagen georreferenciada, en la que cada píxel tiene asignadas coordenadas GPS.
14. Puede cerrar la ventana del georreferenciador. Decida si quiere guardar los PCT en un archivo. Si no está seguro de si su georreferenciación fue lo suficientemente precisa, guarde los PCT para no tener que hacer todo el trabajo de nuevo.
15. Felicitaciones, el mapa georreferenciado ahora aparecerá como una capa ráster en su proyecto de QGIS


:::{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: es_Som_georef_map
---
Mapa georreferenciado de Somalia en el lienzo del mapa de QGIS
:::

### Paso 3 *opcional*: Ajustar la transparencia del mapa georreferenciado

Ahora que tenemos el mapa georreferenciado, podemos __establecer la transparencia__ para que podamos ver otras capas o el mapa base debajo:

16. Haga <kbd>clic derecho</kbd> sobre la capa del mapa georreferenciado.
17. Seleccione `Propriedades`.
18. Vaya a la __pestaña Transparency__.
19. Establezca la transparencia en 50 %.
20. Haga clic en `Aplicar`.

Ahora podemos ver las capas subyacentes. También podemos comprobar la precisión de la georreferenciación comparando las líneas de los límites administrativos de ambas capas.

### Paso 4 *opcional*: Digitalizar entidades vectoriales con el mapa georreferenciado

Ahora que tenemos el mapa georreferenciado, podemos usarlo como capa de fondo para digitalizar entidades vectoriales, como un polígono que indique una región donde la degradación del suelo es grave.

21. Cree una nueva capa shapefile (consulte [digitalización](https://giscience.github.io/gis-training-resource-center/content/es/Module_3/es_qgis_digitisation.html#creating-new-datasets)). Haga clic en `Capa` > `Crear capa` > `Nueva capa de archivo Shape...` (también puede optar por crear una nueva capa GeoPackage).
22. Se abrirá una nueva ventana de diálogo. Primero, necesitamos especificar la ubicación de guardado del nuevo conjunto de datos.
    1. Haga clic en ![](/fig/3.36_three_dots.png) a la derecha del campo de `Nombre de archivo`.
    2. Vaya a la carpeta de exportación de datos (`Module_3_Exercise_7_Georeferencing/data/output`).
    3. Introduzca un nombre para el conjunto de datos.
    4. Haga clic en `Guardar`.
23. Establezca el `Tipo de geometría` en `Polígono`.
24. Agreguemos un campo (columna en la tabla de atributos) para poder añadir información sobre el tipo de degradación del suelo:
    1. En `Nuevo campo`, agregue un nombre, p. ej., `soil_deg`. Queremos que otras personas puedan identificar el tipo de información almacenada en esa columna.
    2. Deje el tipo en String (texto).
    3. Haga clic en `Añadir a la lista de campos`.
25. Termine de crear el conjunto de datos haciendo clic en `Aceptar`. La capa se agregará a su panel de capas.
26. Ahora, vamos a crear una nueva entidad de polígono:
    1. Seleccione la nueva capa en el panel de capas.
    2. Active el modo de edición haciendo clic en ![](/fig/en_editing_mode.png).
    3. Haga clic en ![](/fig/mActionCapturePolygon.png) en la barra de herramientas de digitalización para crear un nuevo polígono.
    4. Comience a trazar el contorno de un campo donde la degradación del suelo es grave (en rojo) estableciendo varios puntos (<kbd>clic izquierdo</kbd>).
    5. Una vez trazado el contorno, termine de crear la entidad haciendo <kbd>clic derecho</kbd>.
    6. Aparecerá una nueva ventana de diálogo. Aquí puede introducir los atributos de la entidad poligonal recién creada. En `soil_deg`, escriba “grave”.
    7. Haga clic en `Aceptar`.

¡Felicitaciones, hemos digitalizado un mapa y entidades vectoriales que podemos usar para análisis adicionales!

