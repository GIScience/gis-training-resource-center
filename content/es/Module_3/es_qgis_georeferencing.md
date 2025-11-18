::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Georreferenciación

La georreferenciación en QGIS es el proceso de alinear una imagen ráster, como un mapa escaneado o una fotografía aérea, con un sistema de coordenadas conocido para poder utilizarla en un análisis espacial. Esto implica asignar coordenadas reales a la imagen identificando puntos de control en el ráster que correspondan a ubicaciones conocidas en la Tierra, a menudo utilizando como referencia capas vectoriales o cuadrículas de coordenadas existentes.

En muchos casos, las instituciones gubernamentales publican los mapas únicamente en formato PDF, sin acceso público a los datos subyacentes. En estos casos, saber georreferenciar correctamente un mapa le permitirá acceder a la información y utilizarla en sus análisis de SIG. En el caso analizado en este capítulo, el mapa de degradación del suelo de Somalia solo está disponible en un informe en PDF. Para utilizar la información en un análisis de SIG, podemos utilizar el georreferenciador para asignar coordenadas geográficas a los píxeles de la imagen. Tras georreferenciar la imagen, el resultado es un archivo ráster (`.tiff`). Este conjunto de datos puede vectorizarse (convertirse en datos vectoriales) o unirse a otros datos ráster, para obtener información adicional.

:::{figure} /fig/example_georefencing_hague.png
---
width: 750 px
name: example_georeferencing_hague
---
Mapa antiguo digitalizado de La Haya (fuente: [Kokoalberti](https://kokoalberti.com/articles/georeferencing-and-digitizing-old-maps-with-gdal/)).
:::

<!--ADD: Pictures of maps available in pdf reports-->

## Georreferenciación en QGIS

En QGIS se utiliza la herramienta Georreferenciador para este proceso. Los usuarios colocan manualmente puntos de control en la imagen ráster y les asignan una coordenada geográfica, ya sea introduciendo las coordenadas manualmente o seleccionando el punto correspondiente en el lienzo del mapa de QGIS. Estos puntos sirven de referencia para que el algoritmo de georreferenciación añada coordenadas geográficas a cada píxel del ráster. A continuación, el algoritmo transforma la imagen, ajustando su escala, rotación y posición para superponerla con precisión a otras capas geoespaciales. Las imágenes georreferenciadas resultan valiosas para digitalizar entidades y realizar análisis espaciales dentro de un SIG.

Existen varios algoritmos de transformación disponibles en QGIS para referenciar un mapa. Si el mapa está en el mismo SRC y solo hay que rotarlo, basta con una transformación lineal. Sin embargo, si la imagen o el mapa están en un SRC diferente o están visiblemente sesgados, se necesita una transformación polinómica. Cuanto más complejo sea el algoritmo de transformación, más puntos de control terrestre necesitará.

:::{figure} /fig/en_georef_transformations.png
---
width: 600 px
name: en_georef_transformations
---
Diferentes tipos de transformación: lineal (izquierda), polinómica de 2.º grado (centro), polinómica de 3.º grado (derecha) (fuente: [ESRI](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/overview-of-georeferencing.htm)).
:::

En la mayoría de los casos, utilizará transformaciones lineales o polinómicas (de segundo o tercer grado). Hay muchos más tipos de transformación que se pueden utilizar en QGIS. Cada una funciona mejor para un uso específico. Para obtener una explicación de cada tipo de transformación, consulte la [documentación de QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_raster/georeferencer.html).


### Cómo georreferenciar en QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_3.36_georeferencing_howto.mp4"></video>

Para georreferenciar un mapa en PDF, debe seguir los siguientes pasos:

1. Prepare el mapa que desea georreferenciar exportando la página correspondiente del PDF o haciendo una captura de pantalla.
2. En su ventana de QGIS, añada un mapa base utilizando XYZ Tiles:
    1. `Layer` > `Add Layer` > `Add XYZ Tiles`.
    2. Se abrirá una nueva ventana. En `XYZ Connection`, en la parte superior de la ventana, seleccione “OpenStreetMap”.
    3. Haga clic en `Add`.
    Lo ideal es utilizar un mapa base en el que pueda identificar ubicaciones exactas tanto en el mapa base como en el mapa que desea georreferenciar.
3. Para abrir el georreferenciador vaya a la barra superior > `Layer` > `Georeferencer` (véase {numref}`open_georeferencer`).

:::{figure} /fig/en_3.36_open_georefencer.png
---
name: en_3.36_open_georefencer
width: 500 px
---
Abrir el Georreferenciador en QGIS 3.36.
:::

4. Se abrirá una nueva ventana. Este es el __georreferenciador__. Para agregar una imagen que georreferenciar, haga clic en ![](/fig/3.36_add_raster_georef.png)`Open Raster`.
5. Seleccione la imagen del mapa que desea georreferenciar. Puede cargar archivos de imagen, así como `Open` PDFClick.
6. La imagen aparecerá en el centro de la ventana del georreferenciador. Haga clic en ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. Se abrirá una nueva ventana. Aquí puede establecer el tipo de transformación y el sistema de referencia de coordenadas (SRC) objetivo. A continuación, puede establecer el nombre y la ubicación de guardado del archivo. Asegúrese de que `Load in the project when done` esté marcado.

:::{note} Establecer el sistema de referencia de coordenadas adecuado.
:class: tip
Lo ideal es que el SRC del mapa georreferenciado sea el mismo que el del proyecto o las otras capas del proyecto. Para saber cómo elegir un SRC adecuado, consulte el capítulo [sobre proyecciones cartográficas](/content/es/Module_2/es_qgis_projections.md) en el módulo 1.
:::

::::{margin}

:::{note}
En la mayoría de los casos, puede dejar el tipo de transformación en lineal. Los mapas regionales suelen estar en una proyección cartográfica conforme (es decir, se conservan los ángulos). Las imágenes satelitales también. Si se da cuenta de que los ángulos no son verdaderos o que el mapa está deformado o distorsionado, quizás tenga que elegir un polinomio como tipo de transformación. Las transformaciones polinómicas necesitan más puntos de control terrestre y los puntos deben distribuirse uniformemente en el mapa.
:::

::::

8. Haga clic en `Ok`.
9. Una vez que haya establecido el tipo de transformación, puede comenzar a agregar puntos de control terrestre (PCT) haciendo clic en ![](/fig/3.36_georef_add_point.png) `Add Point`. Los puntos de control terrestre son puntos a los que se asignan coordenadas geográficas específicas.
10. Haga clic en un punto de la imagen del mapa. Esta será la ubicación precisa que puede identificar tanto en el mapa base como en el mapa que desea georreferenciar.
11. Cuando haga clic en una posición, aparecerá una ventana nueva. Aquí, agregue las coordenadas al punto que seleccionó. Hay dos opciones para hacerlo:
    - Introducir las coordenadas manualmente. Necesitará conocer la coordenada exacta. A veces, en los mapas hay una cuadrícula de coordenadas.
    - Seleccionar los puntos ![](/fig/en_3.36_georef_select_from_canvas.png). Este modo minimizará el georreferenciador y abrirá el lienzo del mapa de QGIS. Amplíe la misma ubicación que seleccionó en el mapa no georreferenciado y haga clic una vez.
    - Una vez introducidas las coordenadas, haga clic en `Ok`
12. La ventana del georreferenciador se abrirá de nuevo. Esta vez, debajo de la imagen del mapa, podrá ver un punto en la tabla. Estos son los PCT. Continúe añadiendo más PCT. Repártalos por todo el mapa. Asegúrese de que el `Mean error` en la esquina inferior derecha de la ventana del georreferenciador sea lo más bajo posible (lo ideal es que sea menor a 5).

:::{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: en_3.36_georef_dialogue_GCP
---
Diálogo de georreferenciación en QGIS 3.36
:::

13. Una vez que haya añadido suficientes puntos, haga clic en ![](/fig/3.36_start_georef.png) `Start Georeferencing`. QGIS usará los puntos que haya añadido para transformar la imagen en una imagen georreferenciada, en la que cada píxel tiene asignadas coordenadas GPS.
14. Puede cerrar la ventana del georreferenciador. Decida si desea guardar los PCT en un archivo. Si no está seguro de si su georreferenciación fue lo suficientemente precisa, guarde los PCT para no tener que hacer todo el trabajo de nuevo.
15. Felicitaciones, el mapa georreferenciado ahora aparecerá como una capa ráster en su proyecto de QGIS


:::{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: en_3.36_finished_georef
---
Mapa georreferenciado de Somalia en el lienzo del mapa de QGIS
:::

## Configuración de la capa georreferenciada

Es posible determinar la transparencia del mapa georreferenciado para poder ver las capas subyacentes:

1. Para abrir las propiedades de la capa, <kbd>haga clic derecho</kbd> en la capa y seleccione __Propiedades__.
2. Vaya a la pestaña __Transparencia__.
3. Configure la opacidad global al 50 %.

También es posible eliminar el fondo blanco. Esto se hace asignando los píxeles blancos al valor Alfa en la pestaña de transparencia en “Opciones de transparencia personalizadas”.

1. Para abrir las propiedades de la capa, <kbd>haga clic derecho</kbd> en la capa y seleccione __Propiedades__.
2. Vaya a la pestaña __Transparencia__.
3. En el cuadro __Custom Transparency Options__, en Transparency Band, seleccione Band 4 (Alpha).
4. A la derecha, haga clic en ![](/fig/en_3.36_add_value_from_display) `Add value from display`
5. Haga clic en el color blanco del mapa georreferenciado en el lienzo del mapa.
6. Haga clic en `Apply`.

## Preguntas de autoevaluación

::::{admonition} Evalúe lo que aprendió
:class: note

1. __¿Qué es la georreferenciación y por qué es importante?__

:::{dropdown} Respuesta
- La georreferenciación es el proceso de asignar coordenadas espaciales del mundo real (en un sistema de referencia de coordenadas conocido) a una imagen (p. ej., una fotografía aérea o un mapa escaneado) para que se ajuste correctamente a los datos geográficos (vectoriales o ráster).
- Esto permite superponer, comparar, medir y analizar esa imagen junto con otros datos de los SIG. Sin georreferenciación, la imagen “flota” sin contexto espacial.
- Garantiza la precisión espacial, la integración y la coherencia entre conjuntos de datos y permite realizar análisis espaciales relevantes y elaborar mapas.
:::

2. __¿Qué son los puntos de control terrestre (PCT)? ¿Por qué es importante distribuirlos uniformemente por la imagen?__

:::{dropdown} Respuesta
- Los PCT son puntos específicos de la imagen cuyas coordenadas reales se conocen (es decir, se puede identificar el mismo punto tanto en el ráster como en un mapa de referencia o en una capa vectorial).
- En la georreferenciación, se recopilan pares de coordenadas de la imagen y coordenadas del terreno en estos puntos de control, y a partir de ellos se deriva la transformación que mapea toda la imagen en el sistema de coordenadas.

__¿Por qué deben distribuirse uniformemente?__
- Si todos los PCT se agrupan en un área, la transformación puede ser más precisa localmente, pero muy distorsionada en otros lugares.
- La distribución uniforme (en esquinas, bordes y centro) ayuda a limitar las distorsiones en toda la extensión de la imagen y produce una deformación más estable y equilibrada.
- Reduce los errores de extrapolación y garantiza el control de todas las partes de la imagen.
:::


::::