::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

## Operaciones de superposición (recorte, disolución, zona de influencia)

- Las operaciones de superposición nos permiten combinar las geometrías de dos capas de diferentes maneras (véase {numref}`es_overlay_operations`).
- La diferencia con las uniones espaciales es que las __geometrías se transforman en el proceso__, y no principalmente los atributos.

:::{figure} /fig/overlay_operations.png
---
name: es_overlay_operations
width: 500 px
---
Representación visual de diferentes operaciones de superposición.
:::

Las operaciones de superposición incluyen __recorte, zona de influencia y disolución__. En los próximos subcapítulos, analizaremos cada una de estas operaciones de superposición y proporcionaremos algunos ejemplos en el ámbito humanitario.

### Recorte

- La herramienta ![](/fig/mAlgorithmClip.png) `Cortar` se utiliza para cortar una capa vectorial utilizando los límites de otra capa de polígonos. En otras palabras, extrae una parte de un conjunto de datos en función de los límites de otro.
- Mantiene solo las partes de las entidades de la capa de entrada que están dentro de los polígonos de la capa de superposición, lo que produce un conjunto de datos refinado.
- Aunque los atributos principales de las entidades siguen siendo los mismos, algunas propiedades, como el área o la longitud, pueden cambiar después de la operación de recorte. Si ha almacenado estas propiedades como atributos, es posible que deba actualizarlas manualmente.

:::{card}
__Ejemplo en el ámbito humanitario:__
^^^
*Los datos sobre la extensión de las inundaciones en Pakistán están disponibles, pero la atención se centra en el mapeo de los daños causados por las inundaciones en una región administrativa específica. En este caso, la capa de inundación se puede recortar a los límites administrativos del área de interés.*

:::


La herramienta tiene dos diferentes opciones de entrada:
* __Capa de entrada__: Capa de la que se recorta la selección
* __Capa de superposición__: Área de interés a la que se recortará la capa de entrada

:::{figure} /fig/en_clip_sudan.PNG
---
width: 550 px
name: es_clip_sudan
---
Captura de pantalla de la herramienta Recortar con los datos de entrada.
:::

### Ejercicio: Recortar una capa de carreteras a límites administrativos

La información sobre la infraestructura vial para las operaciones de ayuda humanitaria es de suma importancia y se puede recuperar fácilmente de fuentes de datos de código abierto como OpenStreetMap. Sin embargo, esta información a menudo se incluye en conjuntos de datos extensos que contienen una cantidad significativa de detalles irrelevantes para operaciones específicas o cubre mucha más área de la necesaria para la operación. Para que el trabajo con estos datos sea más eficiente, es una práctica común recortar los datos al área de interés. Además del recorte, los datos a menudo se pueden filtrar para eliminar los datos que no nos interesan.

1. Cargue los datos de carreteras de OSM desde la herramienta de exportación HOT (parte del equipo humanitario de OpenStreetMap) [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Spatial_geodataprocessing/hotosm_sdn_roads_lines_shp.zip).
como una nueva capa: __Road_infrastructure_Sudan.geojson__.

2. Filtre la capa por medio de __generador de consultas__ para mostrar solo __carreteras primarias y residenciales__ ("carretera" = 'primary' OR "carretera" = 'residential').
3. Cargue la capa admin1 para Sudán que contiene el distrito Nilo Blanco, __ne_10m_admin_1_Sudan_White_Nile.geojson__. Se descarga de los [datos de Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
4. Seleccione la capa de carreteras y abra el diálogo de __Cortar__ desde `Vectorial` > `Geoprocessing Tools`.
    - Configure las carreteras como __capa de entrada__ y los límites del distrito de Nilo Blanco como __capa de superposición__.
    - Haga clic en __Ejecutar__ para generar una capa temporal llamada `Recortado`.
7. Ahora tiene una capa de carreteras ordenadas que contiene la información necesaria.

:::{dropdown} Solución: Recortar una capa de carreteras a límites administrativos
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_clip_roads.mp4"></video>
:::


### Disolución

La herramienta ![](/fig/mAlgorithmDissolve.png) `Disolver` crea una nueva capa y fusiona entidades superpuestas de una o dos capas vectoriales. Puede elegir uno o varios atributos para agrupar entidades que compartan el mismo valor para esos atributos. Alternativamente, puede combinar todas las entidades en una. Si está trabajando con polígonos, eliminará los límites compartidos entre ellos.

Si activa la opción "Mantener objetos disjuntos separados" al ejecutar la herramienta, se asegurará de que las entidades o partes que no se superponen ni se tocan entre sí se guarden como entidades independientes en lugar de formar parte de una entidad grande. Esto le permite crear varias capas vectoriales.

:::{card}
__Ejemplo en el ámbito humanitario:__
^^^
*Dos conjuntos de datos muestran la extensión de la inundación de dos eventos de inundación diferentes en el último año. Ambas capas se superponen pero muestran diferencias. Disolver puede crear polígonos que muestren el área inundada en el último año.*
:::

:::{figure} /fig/en_buffer_dissolve.png
---
width: 550 px
name: es_buffer_dissolve
---
Zonas de influencia con límites disueltos (izquierda) y con límites intactos (derecha) que muestran áreas superpuestas <br /> (fuente: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), Version 3.28)
:::

En la siguiente sección sobre __zona de influencia (buffer)__ usaremos la __herramienta de disolución__.

### Buffer

La creación de zonas buffer crea zonas de distancias predeterminadas alrededor de las entidades geométricas como una nueva capa de polígono. Estas zonas de influencia rodean las entidades vectoriales de entrada. Esta zona de influencia suele ser uniforme y se extiende hacia afuera desde las entidades de entrada originales, lo que la hace útil para diversos análisis espaciales y aplicaciones cartográficas. Se pueden crear estas zonas alrededor de puntos, líneas y polígonos, como se muestra en {numref}`es_buffering_options`.

Algunos ejemplos de análisis que utilizan zona de influencia podrían ser:
- Crear zonas de influencia para proteger el medio ambiente
- Análisis de las áreas verdes alrededor de la zona residencial
- Crear áreas de riesgo para desastres naturales.

:::{card}
__Ejemplo en el ámbito humanitario:__
^^^
Para analizar el acceso a fuentes de agua limpia, un escenario considera qué tan lejos puede caminar la población para llegar a ellas. Se crea una zona de influencia de 2 km alrededor de un conjunto de datos de pozos para visualizar qué áreas se encuentran dentro de esta distancia. Este método ayuda a evaluar la cobertura e identificar las deficiencias en el acceso al agua potable.

:::

:::{figure} /fig/en_buffer_point_line_polygon.png
---
width: 550 px
name: es_buffering_options
---
Diferentes tipos de zonas de influencia <br /> (adaptado según [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html?highlight=dissolve), versión 3.28)
:::

Existen diferentes variantes de zona de influencia. La __distancia de zona de influencia__ o __el tamaño de esta puede variar__ según los valores numéricos proporcionados. Los valores numéricos deben definirse en unidades de mapa de acuerdo con el Sistema de Referencia de Coordenadas (SRC) utilizado con los datos.

::::{Attention}

:::{figure} /fig/en_dist_in_degrees_error_msg.png
---
width: 450 px
name: es_dist_degree_error_message
---
El mensaje de error que muestra QGIS al realizar cálculos basados en la distancia en un sistema de coordenadas geográficas.
:::
Si...
- Aparece un mensaje de advertencia de proyección cartográfica
- Sus capas no aparecen
- Las capas se ven extrañas, p. ej., aplastadas
- Se muestra el mensaje de error "uso de grados" al utilizar distancias (como se muestra en {numref}`es_dist_degree_error_message`)
… podría ser un problema de [proyección](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_projections.html).

Para resolverlo, intente...

- Cambiar el SRC de la capa
- Reproyectar la capa

Por ejemplo, si está intentando crear una zona de influencia en una capa con un sistema de coordenadas geográficas, QGIS le advertirá y le sugerirá que vuelva a proyectar la capa a un __sistema de coordenadas métricas__. Esto se debe a que cuando se utiliza un sistema de coordenadas métricas, el algoritmo utilizará grados para calcular la distancia del tamaño de la zona de influencia. Sin embargo, la distancia entre grados no es uniforme y depende de la latitud (véase {numref}`es_distance_longitudes`)

:::{figure} /fig/en_dist_longitudes.png
---
name: es_distance_longitudes
width: 450 px
---
Esta imagen ilustra esto: 10 grados de longitud en el ecuador son 1113 km, pero 10 grados de
longitud a 70 grados de latitud son solo 381 km. (Fuente: [Ricky Angueria](https://x.com/RickyAngueira/status/1594030866132410368)).
:::

Es por ello que deberá convertir a un sistema de coordenadas local/proyectado para poder especificar distancias en km/millas (p. ej., cuando use la herramienta de zona de influencia).

::::

### Ejercicio: Crear una zona de influencia de 10 km alrededor de los centros de salud

Otro ejemplo relevante para la labor humanitaria puede ser la creación de un mapa que proporcione información sobre la cobertura de los centros de salud en la distancia de 10 km.
Para lograr esto, se crea una zona de influencia de 10 km alrededor de los puntos que representan los centros de salud. En algunos casos, esto creará zonas de influencia que se superponen. Para crear un área homogénea, podemos disolver zonas de influencia superpuestas.

1. Descargue los datos de los __centros de salud de Sudán__ de [HDX](https://data.humdata.org/dataset/sudan-healthsites) como shapefile.
2. Cargue sus datos nuevos en QGIS. Agregue también los límites del distrito de Jartum, __ne_10m_admin_1_Sudan_Khartoum.geojson__.
También se descargan y se adaptan de los [datos de Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
3. Recorte sus centros de salud a los límites del distrito de Jartum.
4. __Reproyecte__ la capa de centros de salud a un sistema de coordenadas local para habilitar la configuración de distancias en kilómetros.
    - Menú `vectorial` → `Geoprocessing tools` → `Reproyectar capa`.
    - Seleccione la capa de __centros de salud__ como capa de entrada.
    - Establezca el objetivo __SRC a WGS 84 / UTM zona 36N__ (haga clic en el icono de proyecciones para buscar en la lista completa de opciones).
    - Haga clic `Ejecutar` para reproyectar.
5. Abra la herramienta __zona de influencia__ accediendo a `Vectorial` → `Geoprocessing Tools` → `Buffer`.
    - Seleccione la __capa reproyectada__ como capa de entrada.
    - Establezca la distancia a __10 km__.
    - Marque la opción para __disolver__ el resultado.
    - Deje las otras opciones como predeterminadas y haga clic en `Ejecutar`.
6. Ahora tiene una visión general aproximada de la cobertura con centros de salud para el distrito de Jartum.

:::{dropdown} Solución: Crear una zona de influencia de 10 km alrededor de los centros de salud
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_buffer_health.mp4"></video>
:::

### Operaciones de recorte más avanzadas


Además de la operación estándar __Recorte__ de QGIS, hay otras dos herramientas más avanzadas para realizar procesos de recorte. Estas herramientas son operaciones GDAL, que permiten la definición de la extensión de recorte. Esta extensión puede ser un área específica o una capa de máscara. La segunda opción es bastante similar al proceso de recorte estándar proporcionado por QGIS.

:::{figure} /fig/en_gdal_clipping_tools.PNG
---
width: 250 px
name: es_gdal_clipping_tools
---
Las herramientas GDAL Recorte de vector por extensión y Recorte de vector por capa de máscara.
:::

:::::{tab-set}

::::{tab-item} Recorte de vector por extensión

Esta operación recorta cualquier archivo vectorial en una extensión determinada. Esta extensión de recorte se definirá mediante un cuadro delimitador que se debe utilizar para el archivo de salida vectorial. También debe definirse en las coordenadas SRC objetivo. Existen diferentes métodos para definir el cuadro delimitador, que constituyen la gran diferencia entre esta herramienta y el proceso de recorte estándar:
* Calcular a partir de una capa: utiliza la extensión de una capa cargada en el proyecto actual.
* Calcular a partir del mapa de diseño: utiliza la extensión de un elemento de mapa de diseño en el proyecto activo.
* Calcular a partir de marcador: utiliza la extensión de un marcador guardado.
* Utilizar la extensión del lienzo del mapa.
* Dibujar en el lienzo: hacer clic y arrastrar un rectángulo que delimite el área a tener en cuenta.
* Introducir las coordenadas como xmin, xmax, ymin ymax.

:::{figure} /fig/en_clip_vector_by_extent.PNG
---
width: 450 px
name: es_clip_vector_by_extent
---
Captura de pantalla de la herramienta Recorte de vector por extensión
:::

::::

::::{tab-item} Recorte de vector por capa de máscara
Esta operación utiliza una capa de polígonos de máscara para recortar cualquier capa vectorial. Esta operación solo toma dos entradas:
1. La capa de entrada
2. La capa de máscara que se utiliza como extensión de recorte para la capa vectorial de entrada

:::{figure} /fig/en_clip_vector_by_mask_layer.PNG
---
width: 450 px
name: es_clip_vector_by_mask_layer
---
Captura de pantalla de la herramienta Recorte de vector por capa de máscara.
:::

::::

:::::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Qué es una operación de superposición en SIG y cuándo es útil?__

:::{dropdown} Respuesta
- Una operación de superposición es un tipo de herramienta de geoprocesamiento vectorial en SIG que combina o manipula las geometrías de dos (o más) capas en función de sus relaciones espaciales (como intersección, unión, recorte, etc.). 
Es útil:
- Cuando se desea extraer un subconjunto de entidades de un conjunto de datos más grande (p. ej., recorte de carreteras a un límite administrativo)
- Cuando se desea fusionar o agregar áreas espaciales (p. ej., disolver extensiones de inundación superpuestas en un área combinada).
- En flujos de trabajo humanitarios u operacionales: p. ej., determinar el área de cobertura de los centros de salud, la extensión de las zonas de peligro dentro de una región o recortar grandes conjuntos de datos a un área de interés para mejorar la eficiencia.

:::

2. __Al realizar operaciones de superposición en QGIS, ¿cómo se combinan las tablas de atributos de las capas de entrada en la capa de salida? ¿Qué sucede con los atributos de cada entrada?__

:::{dropdown} Respuesta
- En la mayoría de los casos, QGIS le permite especificar qué atributos se copiarán de qué entrada a la salida del algoritmo. Si no se especifica nada, QGIS generalmente copiará todos los atributos de ambas capas a la capa resultante.
- Aunque los atributos principales de las entidades siguen siendo los mismos, algunas propiedades, como el área o la longitud, pueden cambiar después de la operación de recorte. Si ha almacenado estas propiedades como atributos, es posible que tenga que actualizarlas en la capa resultante.

:::

::::

