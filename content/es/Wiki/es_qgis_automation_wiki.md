# Automatización en QGIS (el diseñador de modelos)


__🔙[Volver a la página de inicio](../es_intro.md)__

## ¿Por qué es necesaria la automatización?

La automatización agiliza las tareas al reducir el esfuerzo del usuario y minimizar errores mediante una menor repetición manual. Permite la modularización, mejora la reutilización y disminuye la redundancia al emplear de manera repetida un conjunto definido de herramientas necesarias. En QGIS, esto se puede lograr utilizando el “diseñador de modelos”.

## El diseñador de modelos de QGIS

El diseñador de modelos es una herramienta visual que permite a los usuarios crear y editar un flujo de trabajo con todas las herramientas disponibles en QGIS, que pueden utilizarse repetidamente de una manera sencilla y eficiente. Proporciona una interfaz gráfica para construir flujos de trabajo conectando algoritmos y herramientas de geoprocesamiento. El usuario puede definir las entradas, las salidas y el flujo de datos entre las distintas etapas de procesamiento.

### Uso del diseñador de modelos/Modelador gráfico

- Abra la herramienta en `Procesos` → `Diseñador de modelos`
    <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_3.40_opening_model_designer.mp4"></video>

- Guarde el archivo del modelo en una carpeta de su elección haciendo clic en el botón ![](../../../fig/qgis_save_project_as.png) `Guardar modelo como` de la barra superior.

- Abra un modelo existente a través de `Modelo` → `Abrir modelo` y navegue hasta el archivo del modelo.
    <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_3.40_open_model_file.mp4"></video>


### Componentes del modelo

Hay dos tipos de componentes del modelo que puede utilizar para crear flujos de trabajo:

**Entradas**: el modelo comienza con los datos de entrada. Pueden ser capas vectoriales, capas ráster, archivos CSV o incluso valores o expresiones. La mayoría de las veces, utilizará capas como entradas.

**Algoritmos**: los pasos del procesamiento están conformados por algoritmos o herramientas disponibles en QGIS, como el recorte, la reproyección, la unión por valores de atributos, etc.

### Diseñar un modelo

**Añadir entradas**

- Puede añadir entradas al modelo a través de la pestaña `Entrada` situada a la izquierda de la ventana del diseñador de modelos, ya sea haciendo <kbd>doble clic</kbd> en ella o arrastrándola al lienzo del diseñador de modelos.
- Una vez añadida, se abrirá una nueva ventana en la que podrá especificar la descripción de la entrada, que aparecerá como título, así como el tipo de geometría para los datos vectoriales y seleccionar si se trata de una entrada obligatoria u opcional para el flujo de trabajo.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_3.40_model_adding_inputs.mp4"></video>


**Añadir pasos de procesamiento:**

- En el panel `Algoritmos`, a la izquierda de la ventana del diseñador de modelos, puede elegir pasos de procesamiento o algoritmos de la caja de herramientas de procesos de QGIS. Por ejemplo, la herramienta “buffer” para crear una zona de influencia en una red vial con radio de 500.
- Para añadir un algoritmo, basta con <kbd>hacer doble clic en</kbd> él o arrastrarlo al lienzo del diseñado de modelos.
- Una vez añadido, se abrirá la ventana de parámetros del algoritmo. Tendrá un aspecto similar al de la ventana normal de parámetros de ese algoritmo, con algunas excepciones:
    1. Puede añadir una descripción.
    2. Debe definir `Capa de entrada` como entrada del modelo o como salida de otro algoritmo del modelo.
    3. La salida del algoritmo puede definirse como salida del modelo introduciendo un nombre.
    - Pueden aparecer otras diferencias en función del algoritmo.

:::{figure} ../../../fig/en_qgis_3.40_model_adding_algorithms.png
---
width: 500 px
name: es_qgis_3.40_model_adding_algorithms
---
Página de parámetros del algoritmo “buffer” en el diseñador de modelos
:::

- Una vez configurados los parámetros, haga clic en `Aceptar`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_3.40_model_adding_algorithms.mp4"></video>


**Añadir más pasos de procesamiento**

- Puede encadenar varios algoritmos seleccionando `Salida del algoritmo` para la `Capa de entrada` y seleccionando una salida de un algoritmo anterior.

:::{figure} ../../../fig/en_qgis_3.40_model_adding_more_steps.png
---
width: 500 px
name: es_qgis_3.40_model_adding_more_steps
---
Seleccionar la salida del algoritmo “Algorithm Output” como capa de entrada para encadenar varios pasos de procesamiento.
:::


**Ejecutar el modelo**

Para ejecutar el modelo, haga clic en la flecha verde de la barra superior; se abrirá una nueva ventana en la que deberá ingresar/especificar las entradas y, a continuación, haga clic en “Run” para ejecutar. Las capas de salida se añaden automáticamente a la interfaz de su proyecto en QGIS.

Una vez que haya terminado de crear su flujo de trabajo, o si desea probar el resultado de su modelo, puede ejecutar el modelo. Esto realizará automáticamente todos los pasos de procesamiento ingresados en el modelador gráfico y creará capas en su proyecto de QGIS para las salidas definidas.

- En la barra superior de la ventana del diseñador de modelos, haga clic en el botón ![](../../../fig/qgis_3.40_run_model.png) `Ejecutar modelo`.
- Se abrirá una nueva ventana; aquí es donde usted define qué capas de su proyecto de QGIS funcionarán como capas de entrada de su modelo.
- Haga clic en `Ejecutar`. Una vez finalizado, las capas calculadas o procesadas aparecerán en su lienzo principal de QGIS.

:::{figure} ../../../fig/en_3.40_model_run_inputs.png
---
width: 500 px
name: es_3.40_model_run_inputs
---
Selección de las entradas antes de ejecutar el modelo.
:::


<!---
**Export the Model**
Models can be exported as an image (e.g. in png format), PDF, SVG and as a Python Script. Exporting the model can be beneficial for documenting your work steps or to integrate it in a Python based workflow.

Export the model via Model > Export > Export as Image/PDF/SVG Python Script

**VIDEO**
-->