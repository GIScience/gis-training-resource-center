::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# El diseño de impresión

El diseño de impresión en QGIS es donde se diseña y finaliza el mapa con el fin de imprimirlo o exportarlo como PDF (o formato de archivo de su elección). Aquí puede añadir elementos importantes como la leyenda, el título, el texto explicativo y todo lo que necesite para crear un mapa completo. Al añadir elementos de diseño (leyenda, título, barra de escala, fuentes, etc.) a un mapa, proporciona a su público la información necesaria para contextualizar y evaluar la información mostrada en el mapa.

1. Vaya a __Project > New Print Layout > ingrese un nombre para el nuevo diseño de impresión > haga clic en OK__
2. Aparecerá una nueva ventana con un diseño de impresión en blanco.

:::{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Crear una nueva composición de impresión
:::

## Composición del mapa

Un buen mapa guía al lector en la comprensión de la información disponible en el mapa, facilita el acceso a la información y no está sobrecargado de información.

En general, hay que tener en cuenta algunas cosas a la hora de crear un mapa:

- El mapa principal debe ocupar la mayor parte de la página y debe estar centrado.
- Un mapa completo debe tener leyenda, fuentes, título, escala y demás información necesaria para contextualizar la información presentada en el mapa.
- La información adicional, como el título, la fuente, la barra de escala, la leyenda, la orientación, etc., debe escalarse en consecuencia.
    - Los títulos deben ser grandes para que el lector pueda identificarlos como el tema principal del mapa.
    - La información adicional debe ser más pequeña y estar fuera del foco principal de la página (por ejemplo, en la parte inferior, a los lados o en las esquinas).
- Un diseño de página bien estructurado ayuda al lector a discernir los distintos datos del mapa y facilita saber dónde buscar determinada información. Los marcos y los cuadros pueden estructurar el diseño de la página. Por ejemplo, se puede poner una leyenda en la parte inferior o a la derecha del mapa.

Para elaborar buenos mapas, hay que seguir algunas __reglas básicas__ y evitar __errores semiológicos__. El siguiente subcapítulo repasará los elementos clave de un mapa, así como los errores de diseño más comunes.

### Elementos clave de un mapa

Para que el público y los lectores dispongan de información suficiente que les permita contextualizar el mapa, es importante añadir estos elementos clave:

- __Título__
- __Leyenda__
- __Escala__
- __Orientación__
- __Fuente__
- __Mapa general__
- __Autor__

:::{figure} ../../fig/en_good_map_composition_example.png
---
name: en_good_map_composition_example
width: 750px
---
Elementos para una buena composición cartográfica
:::

---

__El título__ resume en pocas palabras la información representada en el mapa, lo que proporciona al lector información contextual útil. Los títulos deben incluir la siguiente información:

- __El lugar__, con varios grados de precisión según la escala (país, región, municipio, etc.).
- __El tema__ debe ser inteligible para todos (asegúrese de que todo acrónimo utilizado se especifique en otra parte del mapa).
- __La fecha__ de los datos representados.

_Ejemplos:_

- _“Acceso a la atención sanitaria en Maputo, Mozambique en 2022”_
- _“Riesgo de inundaciones en Ghardaïa, Argelia”_

__La leyenda__ es clave para interpretar la información representada en el mapa. Sin la leyenda, es imposible entender el significado de los distintos símbolos y colores utilizados en el mapa. Con el fin de orientar al lector, la leyenda debe ser:

- __Completa__: Todos los datos del mapa deben aparecer en la leyenda.
- __Representativa__: Las cifras del mapa y de la leyenda deben coincidir (mismo tamaño, mismo color, etc.).
- __Organizada__: Los datos de la leyenda pueden agruparse por categorías temáticas (salud, medio ambiente, mapa de fondo, etc.) o por tipo de figura (punto, línea, superficie) para facilitar la lectura.

:::{figure} ../../fig/en_legend_good_practice.png
---
width: 750px
name: en_legend_good_practice
---
Ejemplo de leyenda bien organizada
:::

__La barra de escala__ es esencial para un mapa, ya que da la correspondencia entre una distancia medida en el mapa y la distancia en el mundo real. Existen dos tipos de escalas:

- __La escala numérica__ se expresa como una fracción (1/25000 o 1:25000) que indica la relación entre 1 centímetro en el mapa y la distancia real. Se trata de una escala que puede calcularse con software SIG y que suele encontrarse en los mapas topográficos. Una escala de 1:25000 significa que 1 cm representa 25 000 cm (o 250 metros) sobre el terreno.

- __La escala gráfica__ se expresa mediante una línea en el mapa, con un valor de distancia asociado. Esta escala es muy útil para comprender las distancias sobre el terreno. La escala gráfica siempre tendrá el tamaño correcto, aunque se utilice un formato de impresión diferente, ya que sufrirá la misma transformación que el resto del mapa

:::{figure} ../../fig/example_scale_bar.png
---
name: example_scale_bar
---
Ejemplos de barras de escala
:::

### Orientación

Aunque la mayoría de los mapas están orientados hacia el norte, sigue siendo necesario especificar la orientación de su mapa. Esto suele indicarse con una flecha que apunta al norte, ya que a veces se utiliza una orientación distinta a la del norte para representar la zona de estudio.

### Fuentes

Todo dato representado en un mapa debe indicar sus fuentes. Esto proporciona un registro de los datos utilizados, pero también da crédito al autor de los datos. El lector podrá entonces buscar más información sobre las fuentes si lo desea. Los datos geográficos de libre acceso, como OpenStreetMap, están cada vez más abundantes y también deben citarse en los mapas.

Es posible indicar la fuente de cada dato bajo la leyenda o hacerlo en un espacio específico del mapa. El nivel de precisión de las fuentes varía según el autor o la precisión de los datos.

---

:::{admonition} ¡Es su turno!
:class: tip

Observe los mapas que aparecen a continuación y preste mucha atención a cómo los cartógrafos dispusieron los diferentes elementos. También puede echar un vistazo a los mapas que ha encontrado en su trabajo o en su vida cotidiana.

:::

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


Ahora que hemos visto qué debemos tener en cuenta a la hora de diseñar mapas, veamos cómo crear mapas con el compositor de diseños de impresión de QGIS.

## Preguntas de autoevaluación

::::{admonition} Compruebe lo que aprendió
:class: note

1. __¿Qué es el gestor de diseños de impresión y por qué se utiliza para crear mapas en QGIS en lugar de la ventana principal de QGIS?__

:::{dropdown} Respuesta
El gestor de diseño de impresión (a través de `Proyecto` → `Nueva composición de impresión` en QGIS) es una interfaz/ventana independiente en la que se ensambla el mapa para su salida (impresión o exportación) en lugar de trabajar únicamente en el lienzo principal del mapa.

El __compositor de diseños de impresión__:

- Permite colocar elementos cartográficos (marcos, leyendas, barras de escala, títulos, mapas insertados, anotaciones) en un diseño fijo (tamaño de página, orientación, márgenes) adecuado para su exportación o impresión.
- El lienzo principal del mapa QGIS está diseñado para la edición interactiva, la exploración y la simbología dinámica, no para diseñar una composición final con todos los elementos adicionales del mapa y las especificaciones de impresión (tamaño del papel, resolución, formato de exportación).
- En el compositor de diseños para impresión, puede controlar con precisión la colocación, el tamaño, la estratificación y la ubicación de los elementos del mapa.
- Le permite crear un producto cartográfico pulido.

:::

2. __¿Cuáles son los elementos clave del mapa (componentes del mapa) que debe incluir en el diseño final (por ejemplo, título, leyenda, flecha que indica el norte, barra de escala, inserción, coordenadas norte, atribución)?__

:::{dropdown} Respuesta

Un buen mapa debe ofrecer información adicional que permita contextualizar el mapa y la información mostrada, así como la atribución.

Los elementos básicos de un diseño cartográfico completo deben incluir:

- __Título:__ Una descripción breve y concisa de lo que muestra el mapa (incluidos el lugar, el tema y la fecha, si corresponde).
- __Leyenda:__ Explica los símbolos, colores y capas utilizados en el mapa para que el lector pueda interpretar la simbología del mapa.
- __Escala:__ Indica la relación espacial entre las unidades del mapa y las distancias del mundo real.
- __Orientación:__ Normalmente una flecha que indica el norte.
- __Fuente/Atribución de datos:__ Declaración de las fuentes de datos, autor, fecha de los datos.
- Información adicional para ayudar a contextualizar el mapa (por ejemplo, descripción, mapa general, tabla de atributos, gráfico, etc.).
:::

::::

## Recursos adicionales

- [Lista de comprobación de la accesibilidad de la visualización de los datos](https://learn-sims.org/style-guidance/data-visualization-accessibility-checklist/)