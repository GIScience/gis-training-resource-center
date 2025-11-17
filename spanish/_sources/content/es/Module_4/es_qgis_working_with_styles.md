::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exportar e importar estilos

Las capas en QGIS se guardan, por separado, de la configuración y los estilos de un Proyecto QGIS. Esto significa que si carga las mismas capas en un proyecto QGIS distinto, la simbología y el estilo de los datos serán diferentes. QGIS permite guardar la simbología y el estilo de una capa como un archivo independiente (archivos `.qml`). Trabajar con `.qml`archivos le ahorra mucho trabajo y le garantiza la consistencia entre los mapas.

Un `.qml`archivo guarda la información de una capa determinada. Esto incluye los colores, los contornos, las formas, el etiquetado, así como la configuración de la capa, la configuración de la tabla de atributos y otras opciones ,que haya establecido para una capa en su proyecto QGIS, que no estén relacionadas con los propios archivos de datos. Puede elegir si desea guardar solo la simbología en color o cualquier información adicional.

Puede exportar un estilo a la misma carpeta que los datos para que sus colegas puedan aplicar el mismo estilo al cargar los datos en QGIS.
Algunas organizaciones también podrían utilizar símbolos o colores normalizados en sus mapas.

Por ejemplo, si desea enviar una capa a un colega con el mismo estilo que usted, lo mejor es que marque las categorías "__Propiedades de la capa__", "__Simbología__" y "__Etiquetas__" (y cualquier otra opción de estilo adicional, que haya configurado). Si solo desea guardar un determinado color, grosor de línea o estilo de etiquetado, solo tiene que marcar las casillas correspondientes.

### Guardar o exportar la configuración de estilo

1. Abra el panel de estilo y haga clic en `Styles`. Se abrirá un menú desplegable con la opción de exportar el estilo de la capa.
2. Dado que en este caso el estilo es precisamente para ese conjunto de datos, puede dejar todas las casillas marcadas.
3. Seleccione una ubicación y un nombre para el estilo. El estilo se guardará en un archivo `.qml`. __Asegúrese de guardarlo en la misma carpeta que el conjunto de datos y asígnele el mismo nombre que al conjunto de datos correspondiente. De este modo, al cargar los datos en QGIS, el estilo se aplicará automáticamente.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>

:::{figure} ../../fig/en_30.30.2_save_layer_style_window.png
---
width: 350px
name: en_30.30.2_save_layer_style_window
---
Ventana Guardar estilo de capa en QGIS 30.30.2.
:::

Cuando se trabaja con datos similares (por ej.: tipos de edificios o riesgo de inundación), es útil disponer de plantillas de estilos, que puedan cargarse rápidamente en el proyecto QGIS o guardarse en la biblioteca de plantillas de estilos.

:::{Tip}
¡Cuando un estilo se guarda en la misma ubicación que los datos y tiene el mismo nombre que el conjunto de datos correspondiente, el estilo se aplicará automáticamente a la capa, al cargar los datos en QGIS!
:::

### Cargar un estilo en un proyecto QGIS

1. Abra el administrador de estilos: `Settings` > `Style manager`.
2. Haga clic en `import/export` y seleccione `import items`.
3. Navegue hasta la carpeta donde está guardado el estilo y haga clic en importar.
4. El estilo ahora debería estar disponible como preestablecido en el panel de estilos.

:::{note}
También puede importar estilos directamente en el panel de estilos de una capa. Pero no se añadirá a su biblioteca de estilos, a menos que lo guarde en ella.
:::


:::{tip}
Puede copiar estilos de una capa a otra:
1. Haga clic con el botón derecho en la capa con el estilo aplicado → `Styles` → `Copy Style` → `All Style Categories`.
2. Haga clic con el botón derecho en la segunda capa → `Styles` → `Paste Style` → `All Style Categories`.

:::


## Preguntas de autoevaluación


::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Cuáles son las ventajas de crear y utilizar estilos?__

:::{dropdown} Respuesta
- __Consistencia:__ garantiza una simbología uniforme en todos los mapas y proyectos.
- __Reutilización:__ permite aplicar el mismo estilo a distintas capas o a distintos proyectos, sin tener que volver a empezar desde cero.
- __Eficiencia:__ ahorra tiempo al aplicar estilos a muchas capas (con solo cargar el archivo de estilos).
- __Facilidad para compartir:__ puede compartir sus diseños visuales (símbolos, rampas de colores, configuración de etiquetas) con sus colegas.
:::

2. __¿Cómo se importa o exporta un estilo?__

:::{dropdown} Respuesta
1. En QGIS, hacer clic con el botón derecho en la capa → `Properties` → `Symbology`
2. En la esquina inferior izquierda, hay un menú desplegable llamado `Style` con opciones para importar o exportar estilos.
:::

3. __¿Cómo compartiría los estilos con sus colegas o entre diferentes equipos? ¿Qué hay que tener en cuenta (por ej.: rutas de archivos, dependencias de recursos, etc.)?__

:::{dropdown} Respuesta
1. Abrir la`Symbology` pestaña en la`Properties` ventana .
2. En la esquina inferior izquierda, hacer clic en `Style` → `Save Style`.
3. Especificar el nombre y la ubicación donde desea guardarlo.
4. En el explorador de archivos, buscar el archivo `.qml` y compartirlo con su colega.

__Aspectos a tener en cuenta:__
- __Rutas/referencias de los archivos:__ Si el estilo hace referencia a archivos externos (SVG, imágenes) con rutas absolutas, esas rutas pueden dejar de funcionar en otro equipo.
- __Recursos faltantes:__ Si un recurso externo (símbolo, imagen) no está presente o se ha movido, el estilo puede fallar o volver a los símbolos predeterminados.
- __Compatibilidad de versiones__: Los estilos creados en una versión de QGIS podrían no funcionar completamente o verse degradados en otra versión.
- __Compatibilidad de datos:__ Si ha establecido reglas o una clasificación basada en los atributos de una capa, los nombres de las columnas y los atributos deben estar presentes en el conjunto de datos de la segunda computadora.
:::


::::