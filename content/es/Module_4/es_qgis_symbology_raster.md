::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Simbología para los datos ráster

Como ya hemos aprendido, los datos ráster son básicamente una cuadrícula de píxeles con diferentes valores (numéricos). Como tal, no se puede aplicar estilo a la forma, ni relleno ni contorno a los datos ráster. Los datos ráster se visualizan con la asignación de una rampa de color al valor del píxel. QGIS ofrece varias opciones para visualizar los datos ráster. Por ejemplo, puede crear un relieve sombreado con un modelo digital de elevación (DEM). Este breve capítulo solo cubre los aspectos básicos de la visualización de datos ráster. Si desea obtener más información sobre datos ráster y cómo trabajar con capas ráster, consulte el [módulo 8](/content/es/Module_8/es_module_8_overview.md).

## Asignar un gradiente de color a datos ráster

Para asignar un gradiente de color a los datos ráster:

1. Abra las `Propriedades` de la capa ráster.
2. Navegue a la pesteña `Simbología`.
3. Por defecto, el esquema de color se configura en Singleband Gray (si solo tiene una banda de color en el conjunto de datos). Haga clic en `Gris monobanda` y cambie a `Pseudocolor monobanda`.
4. Haga clic en __la flecha situada a la derecha de la rampa de color__. Aquí puede elegir una rampa de color predefinida.
5. Puede modificarla __con un clic en la rampa de color__.

:::{figure} ../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: es_30.30.2_raster_data_colour_gradient
width: 600px
---
Selector de rampa de color en QGIS 3.36.
:::

En el selector de rampa de color, puede ajustar paso a paso el color. En la parte inferior, puede ver un gráfico para el tono, la __saturación__, la __luminosidad__ y la __opacidad__. Los tres últimos son especialmente útiles para entender cómo aparecerá su rampa de color. Los degradados de claro a oscuro son más fáciles de leer: Compruebe si el gráfico de __luminosidad__ tiene un trazo más o menos lineal.

## Invertir la rampa de color

En algunos casos, la rampa de color deberá invertirse para facilitar la lectura del mapa:

1. Haga clic en la __flecha junto a la rampa de color__ para abrir el menú desplegable.
2. Haga clic en `Invertir rampa de color`.

## Uso de mejores paletas de colores

:::{note}

Las rampas de color disponibles, por defecto, en QGIS son limitadas y no se ajustan, a muchos propósitos de la cartografía. Sin embargo, QGIS incluye el catálogo `cpt-city` de paletas de colores con numerosas rampas y paletas de colores, cuidadosamente elaboradas. Entre otras, puede encontrar rampas de color creadas específicamente para modelos de terreno o de elevación.

:::

:::{figure} /fig/en_3.36_cpt-city_cat_1.png
---
name: es_3.36_cpt-city_cat_1
width: 350 px
---
Acceso al catálogo de colores.
:::

Para acceder al catálogo `cpt-city`,

1. abra la pestaña de simbología de capas ráster y seleccione `monobanda pseudocolor` como método de simbolización.
2. Navegue hasta la flecha desplegable, situada junto a la rampa de color, esto abrirá un menú desplegable con diferentes rampas de color.
3. Haga clic en `Crear nueva rampa de color`. Se abrirá un pequeño cuadro de diálogo.
    :::{figure} /fig/en_3.36_cpt-city_cat_2.png
    ---
    name: es_3.36_cpt-city_cat_2
    width: 200 px
    ---
    Selección del catálogo de rampas de colores
    :::
4. Se abrirá una nueva ventana. Aquí encontrará una multitud de paletas de colores. Por ejemplo, para un modelo digital de elevación, puede seleccionar una rampa de color para topografía o en concreto, para modelos digitales de elevación.

:::{figure} /fig/en_3.36_cpt-city_cat_3.png
---
name: es_3.36_cpt-city_cat_3
width: 600 px
---
El catálogo de rampas de colores cpt-city en QGIS 3.36
:::


## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Por qué no se puede aplicar estilo a una capa ráster mediante el cambio en el "relleno" o en el "contorno", como se hace con los datos vectoriales?__

:::{dropdown} Respuesta
- Los datos ráster están formados por __píxeles (celdas)__, cada uno con un valor (p. ej.: elevación, reflectancia), no por geometrías discretas. Por lo tanto, no hay un "contorno" que trazar, ni un "relleno" único para todo el polígono.
- El estilo de los rásters consiste en cartografiar los valores de los píxeles a los colores, en lugar de aplicar estilos de límites o de relleno a las entidades.
- El estilo vectorial funciona sobre entidades geométricas (puntos, líneas, polígonos) y puede controlar rellenos, trazos, formas, etc.; pero el estilo ráster, funciona mediante algoritmos de simbología/renderización (rampa de color, estiramiento, clasificación) sobre la cuadrícula continua de valores.
:::

2. __¿Cuál es el estilo de representación, por defecto, para un ráster de banda única en QGIS, y qué estilo se suele cambiar para obtener una mejor visualización?__

:::{dropdown} Respuesta
- La representación, por defecto, para un ráster de una sola banda es __gris monobanda (escala de grises)__: los valores bajos son más oscuros y los valores altos, más claros.
- Para conseguir una mejor visualización, es habitual cambiarlo a __pseudocolor monobanda__ (es decir, asignar una rampa de color) para que las variaciones en los valores sean más distintivos visualmente.
:::

3. __¿Qué es una “rampa de color” (o gradiente) en el contexto de la simbología ráster y cómo ayuda a interpretar los datos?__

:::{dropdown} Respuesta
- Una rampa de color (o gradiente) es una gama continua de colores, que se asignan a la gama de valores ráster (del mínimo al máximo).
- Al asignar valores crecientes (o decrecientes) a una progresión de colores, el lector puede interpretar visualmente la magnitud, los gradientes y los patrones espaciales de los datos numéricos subyacentes.
- El uso de color (en lugar del gris) puede ayudar a destacar los umbrales significativos, los valores críticos (p. ej.: muy alto o bajo) y mejorar la legibilidad y el atractivo visual.
- Una rampa de color bien diseñada puede resaltar diferencias (p. ej.: valores más altos vs.valores más bajos), revelar la estructura espacial (p. ej.: cumbres, valles, agrupaciones) y hacer que el ráster sea significativo, en lugar de una simple mancha gris.


:::

4. __Brinde un ejemplo de un conjunto de datos ráster (p. ej.: modelo digital de elevación, Índice de Vegetación de Diferencia Normalizada (NDVI) , precipitación) y proponga una rampa o paleta de colores adecuada, que podría utilizar en QGIS__

:::{dropdown} Respuesta
__Ejemplo:__ Un modelo digital de elevación (DEM) que represente la elevación del terreno (en metros)
__Propuesta de rampa / paleta de colores adecuada:
- Elevaciones inferiores: verde oscuro (tierras bajas)
- Elevaciones medias: verde claro → amarillo (pendientes suaves)
- Elevaciones más altas: naranja → marrón (pendientes pronunciadas/terreno alto)
- Elevaciones/cumbres más altas: blanco (nieve/hielo)

En QGIS puede elegir una rampa como “Terrain (elevation)” o una rampa personalizada del catálogo cpt-city (el módulo menciona que QGIS, incluye el catálogo de paletas de colores cpt-city con muchas rampas de colores cuidadosamente elaboradas, algunas incluidas para los modelos de elevación).

:::

5. __Al diseñar una rampa de color para datos ráster (p. ej.: elevación, temperatura), ¿Qué hay que tener en cuenta en términos de luminosidad, tono o uniformidad perceptiva?__

:::{dropdown} Respuesta

- __Progresión claridad/oscuridad:__ Una progresión de colores más claros a más oscuros facilita la lectura. QGIS dispone de un gráfico de luminosidad en el editor de la rampa de colores. Si la luminosidad sube y baja de forma irregular, algunos segmentos pueden parecer visualmente más prominentes que otros. Además, las rampas de colores con luminosidad irregular, no se traducen en impresiones en blanco y negro. En general, las rampas de colores irregulares son menos intuitivas para la lectura.
- __Cambios de tono:__ Los cambios bruscos de tono pueden llamar indebidamente la atención y podrían implicar diferencias categóricas, en lugar de continuas. Si los tonos cambian drásticamente mientras que la luminosidad permanece constante, puede inducir al lector a pensar erróneamente que existen clases discretas.
- __Evitación de asociaciones engañosas:__ Los colores tienen significados culturales o intuitivos (por e.: rojo = calor/peligro, azul = frío, verde = vegetación). Si la rampa utiliza un color poco habitual, el significado podría ser confuso.
- __Contraste y legibilidad:__ Los segmentos muy oscuros podrían ocultar detalles; los segmentos muy claros podrían desvanecerse. También hay que considerar cómo aparecerá la rampa al imprimirla, en escala de grises, o para lectores daltónicos.
- __Interpretación de los extremos y de los rangos medios:__ Si la rampa tiene saltos pronunciados en los extremos o una gama media muy plana, podría perder matices en segmentos importantes. Hay que evitar también las rampas, que sitúan los extremos en colores, visualmente "chillones" y que ensombrecen los valores moderados.

::::