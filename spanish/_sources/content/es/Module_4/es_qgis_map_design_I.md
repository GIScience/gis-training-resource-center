::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Simbología y colores

La representación de datos geográficos en mapas es esencial para proporcionar información útil basada en la ubicación. Este subcapítulo
abarcará los fundamentos básicos del buen diseño cartográfico, cómo crear un diseño cartográfico en QGIS y los errores comunes al diseñar o
interpretar mapas.

En este capítulo repasaremos los conceptos básicos de simbología, colores y cómo ajustar capas individuales en QGIS para crear
mapas exhaustivos.

::::{admonition} Recapitulación: Tipos de mapas
:class: seealso

En general, existen dos tipos principales de mapas: __mapas topográficos__ y __mapas temáticos__.

Los __mapas topográficos__ pretenden ser exhaustivos e incluir elementos fundamentales para la localización (localidades, redes
viales, terreno, hidrografía). Muestran la ubicación física de los objetos en el mundo real. La representación de
los elementos en los mapas topográficos se realiza mediante signos convencionales (por ejemplo, azul para el agua, verde para los bosques, amarillo para
las tierras agrícolas).

:::{figure} ../../fig/en_30.30.2_topographic_map_examples.png
---
width: 600px
name: en_30.30.2_topographic_map_examples
---
Ejemplos de mapas topográficos
:::

Los __mapas temáticos__ muestran la distribución de datos específicos o información procesada estadísticamente, como el tamaño de
la población, la incidencia de enfermedades, el riesgo de inundaciones, etc. La representación de los elementos en los mapas temáticos se decide según
las reglas de la semiología gráfica.


:::{figure} ../../fig/en_30.30.2_thematic_maps_examples.png
---
width: 600px
name: en_30.30.2_thematic_maps_examples
---
Ejemplos de mapas temáticos
:::

Estos dos mapas utilizan los elementos de diseño de forma diferente. Los mapas topográficos utilizarán símbolos y colores por convención y
legibilidad, mientras que en el diseño de mapas temáticos, los símbolos y colores que se utilizan dependen del contexto y la
información que se desea transmitir.

::::

## Variables visuales

:::{figure} ../../fig/en_30.30.2_graphic_semiology_signs.png
---
width: 500px
name: en_30.30.2_graphic_semiology_signs
---
Puede utilizar distintos signos gráficos en función del tipo de información que se desee mostrar (fuente: Desconocida. Esta figura se incluye únicamente con fines ilustrativos y no está sujeta a la licencia Creative Commons de esta plataforma).
:::

Las variables visuales son los __medios gráficos para transcribir visualmente la información__. Las variables visuales son __la forma,
el tamaño, el tono, el valor, la textura y la orientación__. Estas variables pueden ajustarse para representar adecuadamente los datos
a su disposición. Permiten expresar la __relación de diferencia, orden, asociación o cantidad__
entre cada elemento, lo que ayuda a mostrar información diferente.

:::{figure} ../../fig/en_visual_variables.png
---
name: en_visual_variables
width: 500px
---
Variables visuales según Bertin (1967).
:::

:::{Caution}
La percepción visual varía de una persona a otra en función de diversas capacidades:
- Fisiológicas (por ejemplo, daltonismo)
- Transculturales (verde = naturaleza, azul = agua)
:::

## Uso de variables visuales en cartografía

A partir de estas variables visuales, los cartógrafos son capaces de interpretar y comunicar
información crucial para las operaciones humanitarias. Según el caso práctico y los destinatarios, se utilizarán diferentes estilos para comunicar diferentes datos.
OpenStreetMap ofrece varios productos cartográficos: OSM Standard, Tracestack Topo, CyclOSM o el mapa de transporte público, por ejemplo. Los datos que sustentan los mapas
son los mismos, pero el estilo es diferente. En cada caso, los cartógrafos tenían diferentes objetivos en mente (por ejemplo, para
el mapa ciclista, mostrar las rutas ciclistas más seguras, las estaciones de reparación de bicicletas y los lugares de descanso) y eligieron el estilo en consecuencia.

:::::{grid} 2
::::{grid-item}

:::{figure} /fig/m4_OSM_Overviewmap_example.png
---
name: m4_OSM_Overviewmap_example
width: 375 px
---
Norma de [OSM](https://www.openstreetmap.org)
:::

::::

::::{grid-item}

:::{figure} /fig/m4_OSM_bikemap.png
---
name: m4_OSM_bikemap
width: 375 px
---
Mapa ciclista de OSM
:::

::::
:::::

En los siguientes menús desplegables,
encontrará diferentes ejemplos de mapas utilizados en la labor humanitaria.

:::{admonition} ¡Es su turno!
:class: tip

¿Qué tipo de variables visuales o métodos de simbolización puede identificar en estos mapas? ¿Qué tipo de información se comunicó y de qué manera (por ejemplo, información sobre infraestructuras, paisajes naturales, etc.)?
¿Qué otros métodos para comunicar la información imagina o conoce? También puede mostrar un mapa que haya encontrado en su trabajo o en su vida personal.

También puede utilizar mapas que haya encontrado en su trabajo o en su vida cotidiana.

::::

::::{dropdown} __Ejemplo de mapa 1__

:::{figure} /fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4
width: 750 px
---
Zonas y carreteras afectadas por las inundaciones en la región de somalí de Etiopía (fuente: OCHA)
:::

::::

::::{dropdown} __Ejemplo de mapa 2__

:::{figure} /fig/proportional_circles_example.png
---
name: proportional_circles_example
width: 500 px
---
Desplazados internos, 30 de septiembre de 2024 (fuente: [ACNUR](https://reliefweb.int/map/sudan/regional-bureau-east-horn-africa-and-great-lakes-region-internally-displaced-persons-idps-30-september-2024)).
:::

::::

::::{dropdown} __Ejemplo de mapa 3__

:::{figure} /fig/choropleth_hum_example.png
---
name: choropleth_hum_example
width: 700 px
---
Sudán del Sur: Seguimiento de la situación humanitaria, abril-mayo de 2024. Refugios dañados (fuente: [REACH](https://repository.impact-initiatives.org/document/impact/897badb8/REACH_SSD_Map_HSM_AprilMay2024_DamagedShelters_June2024-1.pdf)).
:::

::::


::::{dropdown} __Ejemplo de mapa 4__

:::{figure} /fig/en_m4_operational_overview_example.png
---
name: en_m4_operational_overview_example
width: 650 px
---
Panorama de las operaciones o mapa de actividades de respuesta (fuente: [Grupo temático de refugios de emergencia de Vanuata](https://reliefweb.int/map/vanuatu/vanuatu-tropical-cyclone-lola-distribution-and-gap-map-malampa-13022024)).
:::

::::

### Mapas con símbolos graduados y coropléticos

Los mapas con símbolos graduados y coropléticos son dos tipos de mapas temáticos muy utilizados en el ámbito
humanitario.

En esencia:

- Los datos se dividen en áreas en el mapa.
- Los __mapas coropléticos__ son mapas que muestran datos utilizando colores o sombreado dentro de áreas geográficas específicas, como
países, estados o condados. Ayuda a visualizar patrones o distribuciones de datos en distintas regiones. Por ejemplo, un
mapa coroplético podría mostrar la densidad de población, donde los tonos más oscuros indican densidades más altas y los más claros,
densidades más bajas.
- Los __mapas con símbolos graduados__ utilizan círculos u otros símbolos de distintos tamaños para representar los valores de los datos en
distintas ubicaciones. Cuanto más grande es el círculo, mayor es el valor de los datos que representa. Esto hace que sea útil para mostrar cantidades o comparar valores en diferentes
puntos de un mapa.
- En los mapas coropléticos, los colores o tonos representan valores diferentes para cada zona. Normalmente, el color más oscuro o intenso significa valores más altos. La eficacia de un mapa coroplético depende del __esquema de colores__.
- Los mapas coropléticos suelen crearse [clasificando](/content/es/Module_3/es_qgis_data_classification.md) los datos geográficos en
grupos distintos, ya sea mediante una clasificación categorizada o graduada.
- Los mapas con símbolos graduados se crean cambiando el tamaño de un símbolo en relación con un valor de la tabla de atributos.

Los mapas coropléticos y los mapas con símbolos graduados son ideales para mostrar patrones en áreas extensas, pero deben utilizarse con cuidado, ya que no muestran con exactitud valores
exactos dentro de cada región, si no solo un gradiente general o nivel de intensidad, y se utilizan en casi todas las aplicaciones
de cartografía y SIG.

:::{figure} /fig/choropleth_intro_example.png
---
name: choropleth_intro_example
width: 600 px
---
Ejemplo de mapa coroplético (fuente: [Axis Maps](https://www.axismaps.com/guide/choropleth)).
:::

#### Casos prácticos

:::{dropdown} __Labor humanitaria__

En la labor humanitaria, se utilizan mapas coropléticos o mapas con símbolos graduados para lo siguiente:

- Identificación de las regiones vulnerables: Los mapas pueden mostrar zonas con altos índices de pobreza, conflicto o afectadas por desastres, lo que ayuda a los equipos de respuesta a priorizar las regiones que más necesitan ayuda.
- Seguimiento de brotes de enfermedades: Por ejemplo, durante una epidemia, puede mostrar las zonas con altas tasas de infección, lo que ayuda a dirigir los recursos médicos y evitar una mayor propagación.
- Supervisión de la inseguridad alimentaria y los riesgos de hambruna: Los mapas que ilustran la escasez de alimentos ayudan a las organizaciones humanitarias a centrarse en las regiones donde la ayuda alimentaria es más necesaria.

:::

:::{dropdown} __Ciencia del medio ambiente__

- Visualización de los niveles de contaminación: Representa la calidad del aire o el agua en todas las regiones, lo que ayuda a identificar las zonas contaminadas.
- Seguimiento de la deforestación: Los mapas que destacan los cambios en la cobertura forestal facilitan la detección de las tendencias de deforestación.
- Impacto climático: Las regiones propensas al aumento de la temperatura o a condiciones meteorológicas extremas pueden destacarse para contribuir a los esfuerzos de adaptación al clima.

:::

:::{dropdown} __Salud pública__

- Visualización de las disparidades sanitarias: Muestra las regiones con altos índices de enfermedad, acceso deficiente a la atención sanitaria o tasas de vacunación variables.
- Asignación de recursos: Las autoridades sanitarias utilizan estos mapas para asignar recursos médicos en función de las zonas con mayores necesidades sanitarias.

:::

:::{dropdown} __Planificación urbana e infraestructura__

- Visualización de la densidad de población: Los mapas muestran dónde se concentra la población, lo que ayuda en la planificación urbana y el desarrollo de infraestructuras.
- Identificación de patrones socioeconómicos: Los urbanistas utilizan estos mapas para ver los niveles de ingresos, empleo y educación en los distintos barrios.

:::

---

## Simbología y estilo

Según el caso práctico y el tipo de datos geográficos a disposición, existen múltiples formas de visualizar datos geográficos en un
formato completo. Por ejemplo:

- Se puede cambiar el “estilo” y el color de los datos.
- Cambiar el grosor, el color de las líneas o asignar un patrón de guiones.
- Cambiar el color y los contornos de los polígonos.
- Se puede asignar símbolos o imágenes a los datos geográficos.
- Cambiar el tamaño, el color y la orientación de los símbolos.
- Se puede añadir etiquetas de texto.
- Se puede cambiar el tipo de letra, el color y la orientación de la etiqueta de texto.
- Para los datos ráster, se puede asignar un gradiente de color a los diferentes valores.

El estilo de una capa es la forma en que se comunica la información al público. Cada capa de datos de su proyecto de QGIS
tiene sus propias reglas de estilo. Pueden variar desde las más simples (por ejemplo, mostrar los datos de las líneas como líneas negras, asignar un color a
los polígonos) hasta las más complejas (por ejemplo, diferenciar entre distintos tipos de carreteras, añadir patrones de relleno complejos a los polígonos
o añadir símbolos SVG de distintos tamaños).


## Simbología

- La simbología se utiliza para cambiar el aspecto de las entidades de un mapa.
- Hace que los mapas sean más atractivos visualmente y más fáciles de leer.
- Los colores y estilos representan una información específica.
- La simbología se aplica a las capas, pero dentro de la misma capa podemos asignar diversos estilos a las entidades.
- La simbología de una capa puede modificarse en __función de uno de los atributos de la capa__.

<!--ADD: EXAMPLES OF DIFFERENT STYLING METHODS FOR SIMPLE GEODATA (e.g. houses in different colours, roads in different thickness or colous, points as point symbols or hospital symbols)-->

<!---- To Do: add different visualisation for different types of data (discrete vs. continuous values, insert image). For example the amount of rainfall/temperature is a continuous value.-->

## Colores

Los colores son sin duda las variables visuales más llamativas, ya que se distinguen fácilmente. Sin embargo, según el
tipo de datos y la información que desea transmitir, hay algunos aspectos que debe tener en cuenta a la hora de elegir una combinación de colores
para su mapa. Las variables más importantes para los colores son el __tono__, el __valor__ (saturación) y la
__transparencia__.

Los esquemas de colores pueden ser __categóricos, secuenciales o divergentes__. Si desea mostrar diferentes tipos de edificios o
carreteras, los esquemas de color deben ser categóricos. Los gradientes de color, ya sean secuenciales o divergentes, se utilizan para
datos numéricos o datos que pueden ordenarse. Por ejemplo, para el tamaño de población de los distritos, lo mejor es utilizar un esquema
de colores secuencial para mostrar la diferencia relativa entre los valores. Sin embargo, si los datos tienen valores positivo __y__ negativo
debe utilizarse un gradiente de color divergente.

:::{figure} ../../fig/en_colour_gradients_qualities.png
---
name: en_colour_gradients_qualities
width: 750px
---
Diferentes tipos de esquemas de colores.
:::

A la hora de elegir gradientes de color, lo más adecuado suele ser un degradado de más claro a más oscuro, ya que
la gradación se distingue fácilmente y se traduce bien en blanco y negro. En la figura siguiente, los ejemplos A y B no son
buenas combinaciones de colores, ya que es difícil distinguir la gradación y no se traducen bien al negro y al
blanco. Puede conseguir una secuencia clara graduando la __saturación__ del gradiente de color.

:::{figure} ../../fig/de_colour_gradients_saturation.png
---
name: de_colour_gradients_saturation
width: 750px
---
Ejemplos de diferentes gradientes de color traducidos a blanco y negro. Preste atención al degradado de saturación debajo
de cada ejemplo. (Fuente: Stauffer, Reto y Mayr, Georg y Dabernig, Markus y Zeileis, Achim. (2014). Somewhere Over the
Rainbow: How to Make Effective Use of Colours in Meteorological Visualizations. Bulletin of the American Meteorological
Society. 96. 140710055335002. 10.1175/BAMS-D-13-00155.1.)
:::

Los gradientes de color también pueden abarcar múltiples tonos:

:::{figure} ../../fig/colour_gradients_hues.png
---
name: colour_gradients_hues
width: 750px
---
Degradado de un solo tono a la izquierda; degradado de varios tonos a la derecha. 
:::

:::{tip}
El [sitio web Colourbrewer](colorbrewer2.org) es una herramienta rápida y útil para seleccionar y
generar paletas de colores para su caso práctico.
:::

### Daltonismo

Al elegir los colores, hay que tener en cuenta que los gradientes de color (especialmente los degradados divergentes de rojo a verde) pueden ser difíciles o imposibles de distinguir para las personas daltónicas.

:::{figure} ../../fig/Colour_Blindness.png
---
name: Colour_Blindness
width: 750px
---
Diferentes esquemas de colores para las personas con problemas de visión cromática (fuente: Jenny, Bernhard, y Nathaniel Vaughn Kelso. (2007). Color Design for the Color Vision Impaired. *Cartographic Perspectives*, núm. 58 (1 de septiembre de 2007): 61-67. https://doi.org/10.14714/CP58.270).
:::

## Mapas complejos

Los distintos métodos de simbolización analizados en este capítulo pueden combinarse de distintas formas para crear informes y mapas sofisticados. Combinando varios métodos, puede comunicar al lector distintos fenómenos de forma intuitiva. Un ejemplo clásico es la combinación de un mapa de coroplético (colores graduados) con un mapa de círculos proporcionales (consultar {numref}`en_complex_map_lebanon`).

__Mapa complejo 1:__

:::{figure} /fig/en_complex_map_lebanon.png
---
name: en_complex_map_lebanon
width: 550 px
---
Mapa complejo con colores graduados y círculos proporcionales (fuente: [REACH](https://reliefweb.int/map/lebanon/lebanon-conflict-and-displacement-overview-30-september-2024)).
:::

__Mapa complejo 2:__

:::{figure} /fig/en_complex_bivariate_map.png
---
name: en_complex_bivariate_map
width: 550 px
---
Un mapa complejo que combina el estilo de las capas y distintas variables visuales para comunicar una situación compleja (fuente: [SIMS](https://rcrcsims.org/portfolio/view/18)).
:::

__Mapa complejo 3:__

:::{figure} /fig/en_complex_map_example_yemen.png
---
name: en_complex_map_example_yemen
width: 550 px
---
Un mapa complejo que utiliza colores graduados para indicar la profundidad de las inundaciones, así como el riesgo de inundación para los sitios de los desplazados internos (fuente: [REACH](https://reliefweb.int/map/yemen/flood-hazard-idp-sites-marib-governorate-flood-depth-model-january-2024-production-date-07-may-2024)).
:::

:::{admonition} ¡Es su turno!
:class: tip
{numref}`en_complex_map_lebanon`{numref}`en_complex_bivariate_map` y {numref}`en_complex_map_example_yemen` utilizan colores graduados y símbolos graduados. ¿Qué otros principios de simbolización puede detectar en estos mapas?
:::


Ahora que hemos aprendido las diferentes variables visuales, y sabemos cómo utilizarlas para crear mapas complejos, el siguiente capítulo [Simbología para datos vectoriales](/content/es/Module_4/es_qgis_styling_vector_data.md) explicará cómo configurar diferentes métodos de simbolización y estilo en QGIS.

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Qué son las “variables visuales” (variables gráficas) y cómo ayudan en el diseño de mapas?__

:::{dropdown} Respuesta
- Las variables visuales son propiedades gráficas de los símbolos cartográficos (puntos, líneas, polígonos) que pueden variarse para codificar información (por ejemplo, tono, valor, tamaño, forma, orientación, textura).
- Ayudan a diseñar la representación visual de los datos geográficos para comunicar la información:
    - utilizar el tamaño para mostrar la magnitud;
    - utilizar diferentes colores para distinguir las clases, y
    - utilizar la intensidad de un color (valor) para mostrar la progresión o el aumento de intensidad de un fenómeno.
- Bien elegido
:::

2. __¿Por qué es importante tener en cuenta los esquemas de color (tono, valor, saturación) al diseñar mapas?__

:::{dropdown} Respuesta
- El __tono__ es la “familia de colores” (rojo, azul, verde, etc.); sirve para __distinguir categorías__.
- El __valor__ (o claridad/oscuridad) da una sensación de orden: más oscuro → más, más claro → menos. Útil para datos cuantitativos.
- La __saturación__ (intensidad del color) influye en lo vivo o apagado que parece un color; una saturación alta llama la atención, una saturación baja pasa desapercibida.

El uso de combinaciones inadecuadas (por ejemplo, tonos adyacentes muy saturados o pequeñas diferencias de valor) puede reducir el contraste, hacer que las entidades no se distingan o provocar “vibraciones” de color o ilusiones ópticas.
El esquema debe ser perceptivamente eficaz, accesible (por ejemplo, para lectores daltónicos), coherente y adecuado al tipo de datos (nominales versus ordinales versus de intervalo) y al propósito del mapa.
:::

3. __¿Cuál es la diferencia entre esquemas de colores categóricos (cualitativos), secuenciales y divergentes? ¿Cuándo es apropiado cada uno?__

:::{dropdown}

- __Categórico (cualitativo)__
    Se utiliza para datos nominales (sin orden inherente). Cada categoría recibe un tono (o forma) distinto sin que ello implique magnitud. Ejemplo: tipos de uso del suelo (forestal, urbano, agua).
- __Secuencial__
    Se utiliza para datos que progresan en una dirección (bajo → alto). Suele ser un único tono cuyo valor o saturación cambia gradualmente (por ejemplo, de claro a oscuro). Adecuado, por ejemplo, a la densidad de población, los ingresos o la temperatura.
- __Divergente__
    Se utiliza para datos que se desvían en torno a un punto medio significativo (por ejemplo, cero, media). Dos tonos contrastantes se apartan de un color neutro central. Ejemplo: mapas de cambio (crecimiento positivo frente a descenso negativo), anomalías por encima/por debajo de la media.
:::

4. __¿Cuáles son algunas formas más comunes de estilizar datos vectoriales (líneas, puntos, polígonos)? Proporcione ejemplos (p. ej., cambiar el trazo, el relleno, usar símbolos).__

:::{dropdown} Respuesta
- __Puntos:__
    - Cambiar la forma del símbolo (círculo, cuadrado, estrella).
    - Tamaño variable en función del atributo (símbolo proporcional).
    - Usar el color o el relleno para la clasificación.
    - Añadir contorno (trazo) o halo para contrastar.
- __Líneas:__
    - Ajustar el trazo (ancho) para indicar la magnitud (p. ej., hacer las carreteras principales más gruesas).
    - Usar diferentes estilos de línea (continua, discontinua, punteada) para las categorías.
    - Cambiar el color de las líneas para distinguir tipos (p. ej., ríos, carreteras, límites administrativos).
- __Polígonos:__
    - Usar el color de relleno (tono + valor) para indicar la categoría o la intensidad.
    - Usar la transparencia (opacidad) para que se vean las entidades del fondo.
    - Usar trazos (bordes) de ancho o color variable (tipos de énfasis o límites).
    - Añadir sombreados, texturas o rellenos de patrones para obtener detalles categóricos.
    :::

5. __¿Qué es un mapa coroplético? ¿En qué se diferencia de un mapa con símbolos graduados?__

:::{dropdown} Respuesta
- Un mapa coroplético es un mapa temático en el que las áreas (polígonos) están sombreadas o coloreadas según el valor de una variable (con frecuencia normalizada, p. ej., per cápita). Se rellena todo el polígono con el color (tono/valor) que representa la magnitud de esa variable.
- Un mapa con símbolos graduados (o símbolos proporcionales/graduados) utiliza símbolos (normalmente puntos situados dentro de regiones o centroides) cuyo tamaño (o posiblemente color) varía para representar la magnitud de los datos. Los polígonos subyacentes podrían permanecer sin sombrear o ligeramente estilizados.
:::

::::