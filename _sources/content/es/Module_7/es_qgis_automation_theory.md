::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# El diseñador de modelos en QGIS

## Introducción al diseñador de modelos de QGIS

El ![](/fig/processingModel.png) `Graphical Modeler`, también conocido como Model Builder, permite a los usuarios crear modelos complejos mediante una interfaz visual. La mayoría de las tareas de análisis en un SIG no están aisladas, sino que forman parte de una cadena de operaciones que dan lugar a una serie de entradas y salidas (por ejemplo, recortar el área de interés, realizar una unión espacial y aplicar algunas funciones de tabla). Con el Modelador Gráfico, esta cadena de operaciones puede combinarse en un único proceso, que luego puede reproducirse fácilmente con un conjunto diferente de entradas. Independientemente de cuántos pasos y algoritmos distintos intervengan en el análisis, un modelo se ejecuta como un único algoritmo, lo que ahorra tiempo y esfuerzo.

### Interfaz gráfica de usuario

Se puede acceder al Modelador gráfico desde el menú Procesamiento `Processing -> Graphical Modeler` como se muestra en {numref}`open_graphical_modeler`.

:::{figure} /fig/en_open_graphical_modeler.png
---
height: 150px
name: open_graphical_modeler
---
Cómo abrir el Modelador gráfico en QGIS
:::

Se abrirá la siguiente ventana, que contiene todo lo que necesitamos para construir un modelo.

:::{figure} /fig/en_gui_graphical_modeler.PNG
---
height: 500px
name: gui_graphical_modeler
---
Captura de pantalla de la ventana Modelador gráfico para QGIS versión 3.28.4
:::

En la ventana del Modelador gráfico se pueden ver varios iconos y menús. En primer lugar, nos centraremos en la ventana izquierda de la sección `Inputs` y `Algorithms`. Las entradas son todas las variables o capas de entrada de un modelo, como una capa vectorial, una capa rasterizada, una cadena, una booleana, una expresión y muchas otras. Los algoritmos son todas las herramientas que se utilizan para procesar las variables de entrada. En la cadena de procesamiento, un algoritmo/herramienta devolverá una salida que será utilizada por otra/herramienta siguiente hasta crear la salida final.

### Creación de un modelo

La creación de un modelo implica dos pasos básicos:
 1. Defina los aportes necesarias. Estas entradas se añaden a la ventana de parámetros para que el usuario pueda establecer sus valores al ejecutar el modelo.
 2. Definición de las etapas de tratamiento. Los pasos de procesamiento se definen añadiendo algoritmos y seleccionando cómo utilizan las entradas definidas o las salidas generadas por otros algoritmos del modelo.

#### Construir un modelo para amortiguar las infraestructuras viarias

Construiremos nuestro primer modelo simple mediante la creación de zonas de amortiguación entre segmentos de carretera. Este proceso se basa en una capa vectorial que contiene los datos de la carretera y el algoritmo de amortiguación.

#### Selección de insumos

Para añadir nuevas entradas:

1. Seleccione la `Inputs` pestaña en la ventana de la izquierda.
2. A continuación, seleccione la página `Vector Layer` haciendo doble clic o arrastrándola y soltándola en el lienzo del modelo ({numref}`vector_layer_modeler`). Se abrirá la ventana de definición de parámetros de entrada ({numref}`input_vector_modeler`).
3. En esta ventana podemos personalizar algunos parámetros de entrada vectorial como `Description`, `Geometry type` (Punto, Línea, Polígono) y también podemos definir nuestra entrada como obligatoria para su modelo marcando la casilla `Mandatory`.

<!---It is also possible to select the `Advanced` checkbox to set the input to be within the Advanced section. This is particularly useful when the model has many parameters and some of them are not trivial, but you still want to be able to select them.-->

:::{figure} /fig/en_vector_layer_modeler.PNG
---
height: 300px
name: vector_layer_modeler
---
Capa vectorial como entrada
:::

:::{figure} /fig/en_input_vector_modeler.PNG
---
height: 300px
name: input_vector_modeler
---
Definición de los parámetros de la capa vectorial
:::

#### Selección de algoritmos

El creador de modelos utiliza los mismos algoritmos que están disponibles en la caja de herramientas de procesamiento de la ventana principal de QGIS.
Para añadir algoritmos:

1. Seleccione la `Algorithms` pestaña de la izquierda.
2. Utilizando la barra de búsqueda, busque la herramienta `Buffer` algoritmo como se muestra en {numref}`model_buffer`.
3. Añádelo al lienzo del modelo arrastrándolo sobre el lienzo o haciendo doble clic sobre él.

:::{figure} /fig/en_model_buffer.PNG
---
height: 300px
name: model_buffer
---
Selección del algoritmo de amortiguación
:::

4. Se abrirá la ventana de parámetros del algoritmo. Aquí tenemos que especificar la descripción (título), la entrada, el tamaño del amortiguador y la salida.

:::{note}
La ventana del algoritmo tiene un aspecto un poco diferente que cuando se utiliza el algoritmo fuera del model builder. La principal diferencia es que tiene que especificar que la entrada del algoritmo sea una de las entradas del modelo ____ que haya definido o una salida __de otro algoritmo__. Al seleccionar la salida de otro algoritmo, puede encadenar varios pasos de análisis para crear un flujo de trabajo complejo.
:::

5. En el campo `Description`, ingrese un nombre o una descripción de la etapa de tratamiento (por ejemplo, Red de carretera de amortiguación)
6. Como `Input layer`, seleccione una capa de entrada para el modelo (por ejemplo, infraestructura vial).
7. A continuación, queremos especificar el tamaño del amortiguador. Las unidades de medida serán las mismas que para el proyecto CRS. Ingrese 200.000. Esto indicará al algoritmo que cree un amortiguador de 200 metros (o unidades de medida).
8. Añada un nombre en el campo de salida ![](/fig/qgis_3.40_model_outputs.png) para especificar la salida del algoritmo como salida del modelo.

:::{figure} /fig/en_qgis_3.40_model_adding_algorithm_buffer.png
---
name: en_qgis_3.40_model_adding_algorithm_buffer
width: 500 px
---
Añada el algoritmo de amortiguación al modelo
:::

#### Algoritmos de encadenamiento

La potencia del diseñador de modelos reside en su capacidad para encadenar varios pasos de procesamiento, creando un complejo flujo de trabajo automatizado.

Para encadenar etapas de tratamiento:

1. Añada otro algoritmo al lienzo del modelo (por ejemplo, Recortar)
2. Como `Input layer`, en lugar de ![](/fig/qgis_3.40_input_model_input.png) `Model input`, seleccione ![](fig/qgis_3.40_input_model_algo_output.png). `Algorithm output`.
3. A continuación, seleccione la entrada específica de un paso de procesamiento anterior.


### Trucos y consejos para trabajar con el diseñador de modelos

:::{admonition} Trabajar con múltiples pasos de procesamiento
:class: tip

Cuando se trabaja con múltiples pasos de procesamiento, puede resultar confuso rápidamente elegir las entradas al conectar los pasos de procesamiento.
__Asegúrese de dar a cada paso un nombre claro para que pueda identificarlo fácilmente cuando elija los insumos para otros pasos de procesamiento.__

:::

:::{admonition} Añada comentarios al modelo
:class: tip

El diseñador gráfico de modelos puede resultar difícil de entender cuando se observa un modelo de tamaño medio o grande, ya que no se pueden ver los parámetros de los algoritmos ni los atributos de las capas.

Para facilitar la comprensión, puede añadir cuadros de comentarios a los pasos de procesamiento o a las entradas.

- <kbd>Haga doble clic</kbd> en un algoritmo para abrir el parámetro del algoritmo.
- En la parte superior de la ventana del algoritmo, vaya a la pestaña `Comments`. Aquí puede introducir un comentario que describa lo que hace el paso de procesamiento y lo que debe tenerse en cuenta. También puede especificar un color para el cuadro de comentarios.
- Haga clic en `Ok`. Aparecerá un nuevo cuadro conectado al algoritmo en el lienzo del modelo.

:::

:::{admonition} Unir atributos
:class: tip
Cuando se unen capas en el diseñador de modelos, por defecto, se copian todos los atributos a la nueva capa.
Esto puede dar lugar rápidamente a tablas de atributos grandes y confusas.
Para copiar varios atributos, pero no todos, debe introducir los nombres de las columnas con la siguiente sintaxis:

```
Value_1;Value_2;Value_3
```

:::

:::{admonition} Añada cuadros de grupo
:class: tip

Cuando organice su modelo, puede añadir cuadros de grupo para agrupar algoritmos en el lienzo del modelo y ordenar visualmente los diferentes pasos.

- En la barra superior, vaya a `Edit` -> `Add Group Box`. Aparecerá un cuadro gris en el fondo del lienzo del modelo
- <kbd>Haga doble clic</kbd> en el cuadro de grupo para introducir un nombre y personalizar el color.

:::

:::{admonition} Pruebe el modelo

Cuando se construye un modelo, es útil añadir salidas temporales para los pasos individuales para verificar que los pasos de procesamiento o los cálculos son correctos en los pasos intermedios.

:::
