::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Etiquetas para datos vectoriales

Las etiquetas son textos que muestran información o valores de los datos. En QGIS, puede seleccionar __Etiquetas simples__ o
__Etiquetado basado en reglas__. Para cada opción, se mostrará un atributo (`value`) en el mapa. Por ejemplo, el
nombre de una ciudad o región. Además, puede __cambiar la fuente, el tamaño, el color y otras opciones de estilo__
para el texto de la etiqueta. Al crear un mapa, puede añadir etiquetas para ayudar al lector a comprenderlo rápidamente. Sin embargo,
tenga en cuenta que un exceso de texto puede sobrecargar el mapa con demasiada información para que el lector la procese.

### Etiquetas simples y etiquetado basado en reglas

QGIS ofrece dos métodos para mostrar etiquetas: __Etiquetas simples__ y __Etiquetado basado en reglas__

#### Etiquetas simples

Crea un único estilo de etiqueta para cada entidad de la capa. Puede seleccionar un atributo (valor) que se
mostrará. Por ejemplo, el nombre de un asentamiento. Necesita saber qué atributo muestra la información que desea
mostrar. Consultar la tabla de atributos del conjunto de datos para averiguarlo.

:::{figure} /fig/labels_single_labels_example_nga_adm1.png
---
width: 600 px
name: labels_single_labels_example_nga_adm1
---
Etiquetas simples para cada región administrativa (adm1) de Nigeria. El lector puede asignar cada etiqueta a la entidad administrativa correspondiente.
:::

:::{figure} /fig/en_30.30.2_assigning_value_to_labels.png
---
width: 600 px
name: en_30.30.2_assigning_value_to_labels
---
Asignar el valor de atributo correcto en las opciones de etiquetado. QGIS necesita saber qué atributo (columna) de la tabla de atributos debe mostrarse como etiqueta. En este caso, queremos que aparezca el nombre de la región administrativa (`ADM1_EN`).
:::

#### Añadir etiquetas simples a una capa

1. En el panel de estilo, haga clic en la pestaña `Labels` situada debajo de la pestaña Symbology.
2. Seleccione ![](../../fig/en_30.30.2_icon_single_labels) `Single labels`.
3. `Value` es donde se elige el atributo que se mostrará como etiqueta. Por ejemplo, `*ADM1_EN*` mostrará los nombres en inglés de los estados nigerianos para cada entidad del conjunto de datos.
4. __Cambiemos la fuente__: Abra el menú desplegable de fuentes y seleccione Arial. Cree el texto `Bold` en el menú desplegable Style. Cambie el color haciendo clic en `Colour`, y cambie el `Size` a 8 pts.
5. __Añadamos un buffer blanco__ alrededor de la etiqueta. En la pestaña `Labels`, encontrará una lista con diferentes opciones para diseñar las etiquetas. Ahora, estamos en el menú `Text`. Seleccione `Buffer` y marque la opción `Draw text buffer`. Esto hará que las etiquetas se destaquen más en mapas oscuros o con mucha información.
7. Haga clic en `Apply` y `OK`.

:::{figure} ../../fig/en_30.30.2_setting_up_labels.png
---
width: 600px
name: en_30.30.2_setting_up_labels
---
Configurar etiquetas en QGIS 30.30.2
:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_labels.mp4"></video>

::::{attention}

Las etiquetas simples no siempre son útiles. Por ejemplo, si el conjunto de datos es demasiado grande, o si solo desea mostrar determinadas entidades del conjunto de datos. En el ejemplo siguiente, hay demasiados asentamientos para mostrar etiquetas para cada asentamiento. En cambio, podría ser útil mostrar solo las capitales regionales y nacionales. Para este tipo de casos, el etiquetado basado en reglas es ideal.

:::{figure} /fig/single_labels_bad_example.png
---
name: single_labels_bad_example
width: 400 px
---
Se seleccionaron etiquetas simples para mostrar los nombres de los asentamientos (puntos rojos). Un mapa con tanta información textual es ilegible y apenas se entiende la información.
:::

::::

#### Etiquetado basado en reglas

Cree reglas mediante expresiones para seleccionar con precisión las entidades que deben etiquetarse. Cada regla puede tener un
formato de texto diferente. Utilícelo si desea tener más control sobre la información que se mostrará como etiquetas. Por
ejemplo, puede filtrar los datos para que solo se muestren los nombres de las capitales regionales.

:::{figure} /fig/rule-based_labeling_example_settlements_nga.png
---
name: rule-based_labeling_example_settlements_nga
width: 500 px
---
El etiquetado basado en reglas permite filtrar conjuntos de datos. De este modo, puede mostrar las etiquetas solo para las entidades seleccionadas sin alterar el conjunto de datos.
:::

Las reglas, o filtros, se basan en una expresión. Puede utilizar el ![](../../fig/expression_string_builder_icon.png) `Expression string builder` situado a la derecha de la opción __Filter__ del panel de etiquetas.

#### Añadir etiquetas basadas en reglas a una capa

1. En el panel de estilo, haga clic en la pestaña `Labels` situada debajo de la pestaña Simbología.
2. Seleccione ![](/../fig/30.30.2_Icon_rule_based_labeling.png) `Rule-based Labeling`.
3. Añada una regla haciendo clic en el botón `+`, en la esquina izquierda del panel de estilo. Se abrirá una nueva ventana en el panel de estilo. En esta ventana, ingresará la regla (`Filter`) y personalizará la fuente, el tamaño y la ubicación de la etiqueta. Además, puede introducir una descripción.
4. Introduzca un filtro (cuadro rojo en la figura inferior). La forma más sencilla es utilizar la `Expression string builder` situada a la derecha de la opción Filter. Haga clic en el símbolo ![](/../fig/expression_string_builder_icon.png). Se abrirá un nuevo panel.
5. En el generador de cadenas de expresión, ingrese una regla. En el ejemplo del video que aparece a continuación, queremos mostrar únicamente los asentamientos que son capitales nacionales o regionales. Corresponde a la cadena `("CLASS" = 1 ) OR ("CLASS" = 2)`. Lo sabemos porque conocemos nuestros datos y hemos consultado previamente la tabla de atributos.
6. Haga clic en `OK`.
7. Establezca la fuente y el tamaño de la fuente.
8. Haga clic en `Apply`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_rule-based_labels.mp4"></video>

:::{note}
Para añadir reglas a sus etiquetas, necesitas conocer bien sus datos. Observe los metadatos (en las propiedades o en la fuente) y consulte la tabla de atributos. Piense en el significado de las distintas columnas e identifique los atributos. Esto no siempre es fácil, ya que pueden tener nombres abreviados, pero a medida que trabaje más con datos, le resultará más sencillo.
:::

A continuación se exponen otras consideraciones que se deben tener en cuenta al utilizar etiquetas:

- Mostrar únicamente la información que cumpla la función del mapa o que sea útil para el lector. La información útil puede ser el nombre de un asentamiento o un lugar, de modo que el lector pueda asignar un determinado símbolo en el mapa a este lugar concreto.

- Si desea mostrar distintos tipos de información como etiquetas, el tipo de letra debe ser diferente para que el lector pueda diferenciar entre los distintos tipos de información que se muestran. Una buena práctica es mostrar las etiquetas en un color similar al de los objetos a los que se refieren. Por ejemplo, texto azul oscuro para las etiquetas de masas de agua azul claro o texto marrón para las etiquetas de casas marrón claro.

:::{figure} ../../fig/good_labels_example.png
---
width: 400 px
name: good_labels_example
---
Un buen ejemplo de colocación de etiquetas y tipo de letra. Preste atención a los colores y a la orientación del texto. Cada etiqueta puede atribuirse fácilmente a la entidad cartográfica correcta. (Fuente: [Axis Maps](https://www.axismaps.com/guide/labeling))
:::

::::::{Attention}

- En la mayoría de los casos, mostrar valores numéricos como etiquetas confunde al lector y hace que el mapa resulte demasiado complejo. En la mayoría de los casos, para los datos numéricos, puede elegir una visualización diferente, como los colores o el tamaño del símbolo.


:::::{grid} 2
::::{card}

:::{figure} ../../fig/labels_numerical_values_bad_example.png
---
name: labels_numerical_values_bad_example
---
Etiquetas numéricas
:::

::::

::::{card}

:::{figure} /fig/labels_graduated_symbology_example.png
---
name: labels_graduated_symbology_example
---
[Simbología graduada](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_data_classification.html#graduated-classification)
:::

::::

:::::

::::::

- QGIS coloca las etiquetas automáticamente. A veces, si utiliza muchos contornos negros o colores oscuros, el texto negro es difícil de leer en el mapa. En ese caso, puede añadir un buffer blanco alrededor del texto para hacerlo visible.

:::{figure} ../../fig/label_text_buffer_example.png
---
width: 500 px
name: label_text_buffer_example
---
Una etiqueta sin buffer de texto (izquierda) y una etiqueta con buffer de texto blanco (derecha).
:::

:::{note}
QGIS genera las etiquetas automáticamente.
A veces las etiquetas pueden ocultar otros símbolos. En ese caso, puede ajustar la ubicación de las etiquetas en la pestaña __Etiqueta__ o utilizar la herramienta ![](../../fig/30.30.2_move_a_label_diagram_callout_icon.png) `Move a Label, Diagram, or Callout` de la barra de herramientas __Etiqueta__.

Por defecto, QGIS genera las etiquetas de manera que no se superpongan con otras etiquetas. Esto significa que no todas las etiquetas serán visibles si los datos son densos o se muestran muy cerca unos de otros. Puede optimizar la generación en la opción de renderizado.

:::

:::{Attention}

Consulte el [artículo en Wiki](/content/es/Wiki/es_qgis_representation_wiki.md) para obtener tutoriales detallados, paso a paso, sobre cómo utilizar las distintas funciones del panel de estilo.

También puede leer más en el artículo “[Etiquetado y jerarquía de textos en la cartografía](https://www.axismaps.com/guide/labeling)” de Axis Maps.


:::


## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __Cuando se utilizan etiquetas simples, ¿qué debe seleccionar para que se muestren las etiquetas (es decir, qué significa “Valor”)?__

:::{dropdown} Respuesta
- En el modo Etiquetas simples, debe seleccionar un __campo de atributo__ (columna) de la capa cuyos valores se mostrarán como etiquetas. Esto se denomina campo Valor. Por ejemplo, puede elegir la columna que almacena el nombre de una calle para mostrar los nombres de las calles en el mapa.
- También puede utilizar una expresión en lugar de un campo simple, por ejemplo, concatenar varios campos o incluir funciones, para construir lo que muestra la etiqueta.

2. __¿Qué es una “regla” en el etiquetado basado en reglas y cómo se crea una (por ejemplo, utilizando expresiones)?__

:::{dropdown} Respuesta
- Una __regla__ en el etiquetado basado en reglas es una condición (filtro) que determina qué entidades se etiquetan según esa regla y, opcionalmente, con un estilo particular. Cada regla puede tener su propio estilo de etiqueta (fuente, tamaño, etc.).
- Para crear una regla: en las propiedades de Etiqueta de la capa, seleccione Etiquetado basado en reglas. A continuación, añada una nueva regla, asígnele una descripción y establezca una expresión de filtro (utilizando el generador de expresiones) que compruebe algunos atributos (y, opcionalmente, la escala, la visibilidad, etc.). Solo las entidades que satisfacen la expresión se etiquetan bajo esa regla.
:::

3. __¿Por qué se prefiere el etiquetado basado en reglas en lugar de etiquetar cada entidad (con etiquetas simples)? Proporcione un ejemplo hipotético.__

:::{dropdown} Respuesta
- El __etiquetado basado en reglas__ le permite etiquetar de forma selectiva (solo algunas entidades, por ejemplo, solo las carreteras principales, solo las capitales o las características de un tamaño superior a cierto límite), lo que evita el desorden.
- También permite variar el estilo de las etiquetas por regla (diferente tamaño de letra, color, estilo) en función del atributo o la escala de la entidad.
- __Ejemplo hipotético__: Supongamos que tiene un mapa de ciudades y desea etiquetar solo las grandes ciudades (población > 100 000) con sus nombres en negrita grande, las ciudades medianas en letra más pequeña y omitir las ciudades muy pequeñas para reducir la aglomeración. Puedes hacer reglas como “población” > 100 000, 10 000 < “población” <= 100 000, etc. Cada regla etiqueta únicamente esas entidades, con el estilo adecuado. Así se evita etiquetar cada pequeño pueblo, lo que podría superponerse y generar confusión.
:::

4. __¿Por qué se desaconseja en general etiquetar valores numéricos (continuos) directamente como etiquetas de texto?__

:::{dropdown} Respuesta
- Los valores numéricos continuos (por ejemplo, recuentos precisos, mediciones) tienden a producir __demasiadas etiquetas únicas__, que pueden desordenar el mapa o superponerse, lo que dificulta su lectura.
- Suelen cambiar continuamente, por lo que los pequeños cambios (precisión menor) pueden no ser útiles y saturar el etiquetado.
- Además, los valores continuos se representan mejor mediante __variables visuales graduadas__ (por ejemplo, color, tamaño o coroplética degradados) que mediante texto, de modo que los espectadores perciben la magnitud relativa de forma más natural.
:::


::::

## Recursos adicionales

- [Fuentes compatibles con la marca IFRC](https://learn-sims.org/style-guidance/standard-fonts/)
