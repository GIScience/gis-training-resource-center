::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Clasificación de datos geoespaciales

La clasificación de datos geoespaciales en los SIG consiste en categorizar la información geográfica en distintos grupos o clases en función de características o atributos compartidos. A cada clase se le puede asignar un símbolo o color distinto. Este proceso mejora la organización e interpretación de los datos espaciales.

Los atributos de los datos geoespaciales se almacenan en una columna específica dentro de la tabla de atributos. Esencialmente, elegimos una columna que contenga las características específicas de interés, lo que permite a QGIS agrupar los datos según estos atributos seleccionados ({numref}`es_classification_basic`).

:::{figure} /fig/classification_basic.drawio.png
---
width: 900px
name: es_classification_basic
align: center
---
Clasificación básica (fuente: HeiGIT).
:::

## Escalas nominal, ordinal y métrica

En la clasificación de datos geoespaciales, se utilizan las escalas __nominal__, __ordinal__ y __métrica__ para categorizar y medir las entidades espaciales según distintos niveles de precisión y jerarquía:

::::{margin}
:::{attention}

“Escalas” en este contexto no se refiere al nivel de zoom ni a la relación de medidas entre el mundo real y la representación cartográfica. Se refiere a las relaciones entre los distintos valores de los datos.

:::
::::

- La __escala nominal__ (datos categóricos) es la forma más sencilla de medición en la que las entidades se agrupan en categorías distintas basadas en atributos cualitativos. Estas categorías no tienen ningún orden ni clasificación inherentes. No tienen ningún significado numérico: los valores o etiquetas son solo nombres o identificadores (en algunos casos, las clases de cubierta terrestre pueden identificarse con números).
    - Ejemplos: Clases de cubiertas terrestres, tipos de vegetación, tipos de suelo, tipo de equipamiento (hospital, iglesia, escuela, etc.).

    :::{figure} /fig/nominal_scale_examples.png
    ---
    name: es_nominal_scale_example
    width: 600 px
    ---
    Ejemplos de datos nominales y su representación (fuente: Dickmann [2018] Kartographie, Westermann).
    :::

- La __escala ordinal__ (datos clasificados) implica categorizar los datos, pero, en este caso, las categorías tienen un orden o rango significativo. Sin embargo, los intervalos entre los rangos no son necesariamente iguales ni conocidos. El orden de clasificación es importante: las entidades pueden clasificarse u ordenarse de menor a mayor, pero la diferencia real entre las clasificaciones no se mide. Es posible comparar y clasificar los datos (es decir, qué entidad está clasificada en un nivel superior o inferior).
    - Ejemplos: Adecuación del terreno, red vial jerárquica, clases de tamaño de la población, clases de vulnerabilidad (p. ej., para unidades administrativas).

    :::{figure} /fig/ordinal_scale_example.png
    ---
    name: es_ordinal_scale_example
    width: 600 px
    ---
    Ejemplos de datos ordinales y su representación (fuente: Dickmann [2018] Kartographie, Westermann)
    :::

- La __escala métrica__ (datos cuantitativos) se ocupa de datos que tienen tanto orden como diferencias exactas entre los valores. Estos datos se representan con valores numéricos precisos y las diferencias entre los valores son constantes en toda la escala. Los datos métricos pueden dividirse a su vez en:
    - Escala de intervalos. Datos numéricos en los que la diferencia entre valores es significativa, pero no existe un verdadero punto cero (p. ej., la temperatura en grados Celsius).
    - Escala de proporciones. Datos numéricos en los que tanto las diferencias como los coeficientes son significativos y existe un verdadero punto cero (p. ej., distancia, área).
    - Ejemplos: Datos de elevación, distancia, área y población.

    :::{figure} /fig/interval_ratio_scale_example.png
    ---
    name: es_interval_scale_example
    width: 600 px
    ---
    Ejemplos de datos métricos y su representación (fuente: Dickmann [2018] Kartographie, Westermann).
    :::

Según el tipo de escala, utilizará distintos métodos de clasificación. A continuación, repasaremos los distintos tipos de clasificación disponibles en QGIS y cuándo utilizarlos para cada dato. También repasaremos algunos escenarios con los que se puede encontrar en su trabajo con los SIG.


## Clasificación por símbolo único

Por defecto, QGIS genera una visualización de todas las capas en la configuración `Símbolo Único`. Esto significa que todas las entidades de una capa se visualizan igual. En esta configuración, puede cambiar muchos parámetros como el color o la opacidad, __pero no puede clasificar los datos en varios grupos.__

La clasificación por símbolo único es útil cuando se dispone de un conjunto de datos sencillo. Cuando se carga, por ejemplo, una capa de polígonos con los límites administrativos de una región y una capa de puntos con las principales ciudades. En este caso, puede elegir una clasificación por símbolo único y ajustar el símbolo para cada capa.

::::{dropdown} Cómo: Establecer la clasificación por símbolo único
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>

__Para ajustar el estilo de una capa…__
1. Haga clic derecho en la capa.
2. Haga clic en `Simbología`.
3. Confirme que el ajuste de capa está en `Símbolo Único`.
4. Seleccione el color que desee en el menú desplegable. Para ver más opciones de color, seleccione en el menú desplegable `Seleccionar Color`.
5. *Opcional*: Puede ajustar la opacidad/transparencia de la capa. Esto puede ser muy útil cuando se desea mostrar varias capas superpuestas.
6. *Opcional*: Aquí puede establecer el tipo de unidad. Esto es útil si desea visualizar puntos en un tamaño determinado, por ejemplo.
7. *Opcional:* Aquí puede encontrar rápidamente estilos estándar y usados anteriormente.
8. Haga clic en `Aplicar` para aplicar el ajuste.
9. Haga clic en `Aceptar` para cerrar la ventana.


:::{figure} /fig/Single_symbol_classify.png
---
width: 900px
name: es_Single_symbol_classify
align: center
---
Ajustar el estilo de una capa.
:::
::::


## Clasificación por categorías

La clasificación por categorías en QGIS agrupa los datos espaciales en categorías distintas basadas en atributos específicos.

Esta clasificación organiza las entidades en categorías basadas en valores específicos de la tabla de atributos.
Al asignar un símbolo a cada categoría, puede facilitar la interpretación de la información geoespacial en el mapa para obtener una visión más clara.

:::{figure} /fig/fr_simple_classification_example_map.png
---
name: es_simple_classification_example_map
width: 750px
---
Niger - Régions de Tillabéri et de Tahoua Éducation: infrastructures scolaires fermées ou endommagées pour cause d'insécurité entre 2019 et 2022 (fuente: [REACH](https://repository.impact-initiatives.org/document/impact/e6174a66/REACH_NER_Map_Ecoles_fermees_mai2022_tillaberi_tahoua.pdf)).
:::

En el mapa anterior, a las carreteras principales se les asignó un símbolo único. Las escuelas se clasificaron en dos categorías: escuela primaria (*école primaire* en francés) y escuela secundaria (*école secondaire* en francés).


La clasificación por categorías suele utilizarse para los datos de escala __nominal__ y __ordinal__.

| Escala de datos | Definición | Ejemplo | Formato de datos típico |
|---|---|---|---|
| Escala nominal | Categorías sin orden ni clasificación inherentes | Tipos de cubiertas terrestres, distritos, zonas de subsistencia | Texto (“Desierto”) o número entero (5) |
| Escala ordinal | Categorías con un orden o clasificación significativos | Rangos (p. ej., bajo, medio) | Texto (“alto”) o número entero (5) |

:::{figure} /fig/Categorized_district_map_SierraLeone.png
---
width: 750 px
name: es_Categorized_district_map_SierraLeone
align: center
---
Ejemplo de mapa con una clasificación por categorías.
:::

:::{dropdown} Cómo: Establecer la clasificación por categorías
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

__Para clasificar los datos en categorías…__
1. Haga clic derecho en la capa.
2. Haga clic en `Simbología`.
3. Haga clic en `Categorizado`.
4. En el menú desplegable `Valor`, seleccione la columna en función de la cual desea clasificar los datos.
5. Más abajo, haga clic en `Clasificar`. Ahora debería ver todos los valores únicos o atributos de la columna seleccionada en `Valor`. Para añadir o eliminar valores individuales, utilice los botones `-` y `+`.
6. *Opcional*: En el menú desplegable `Símbolo`, puede seleccionar los colores y símbolos que desea utilizar.
7. *Opcional*: En el menú desplegable `Rampa de color`, puede especificar la gama de colores que desea utilizar.
8. *Opcional*: Puede abrir el panel `Representación de capa` en el botón de la ventana. Aquí puede ajustar la opacidad/transparencia de la capa.
9. Haga clic en `Aplicar` para aplicar el ajuste.
10. Haga clic en `Aceptar` para cerrar la ventana.

:::

## Clasificación graduada

La clasificación graduada en los SIG consiste en categorizar los datos espaciales en clases o rangos basados en una progresión de valores. Este método es especialmente útil para visualizar datos cuantitativos, ya que permite diferenciar la intensidad, la densidad o la magnitud a lo largo de un espectro, lo que facilita una representación matizada de los fenómenos geográficos.

::::{card}

:::{figure} /fig/example_classification_hexagons.png
---
name: es_example_classification_hexagons
width: 750 px
---
REACH, Ucrania, Mapa de seguimiento de los emplazamientos colectivos de desplazados internos, Actives, julio de 2024 (fuente: [Reach](https://repository.impact-initiatives.org/document/impact/192097a8/REACH_UKR_Map_CSM_SituationOverview_ActiveSites_JULY2024_ENG_A4-1.pdf)).
:::

En {numref}`es_example_classification_hexagons`, cada celda hexagonal contiene un valor de “número de emplazamientos por cada 150 km²” que oscila entre 1 y 91. Las celdas están organizadas en 5 categorías, lo que facilita la distinción entre los distintos valores de cada celda. Al reducir al mínimo la cantidad de clases, el lector puede leer y comprender el mapa más rápido.

::::

La clasificación graduada se suele utilizar para datos cuantitativos medidos con una escala de __intervalo__ o __proporción__.

| Escala de datos | Definición | Ejemplo | Formato de datos típico |
|----------------|----------------------------------------------------|-------------------------------------|----------------------------------------------|
| Escala de intervalos | Intervalos equitativos entre valores, sin punto cero verdadero | Temperatura (Celsius) | Flotante (44,5 grados) |
| Escala de proporciones | Intervalos equitativos con un punto cero verdadero | Población, longitud, número de árboles | Entero (5 árboles) o flotante (12,5 km de carretera) |

Para clasificar los datos cuantitativos existen muchos métodos sobre cómo establecer las clases. No existe una única forma de seleccionar un método o de decidir cuántas clases utilizar. Todo depende de lo que quiera mostrar.

:::{tip}
Un buen intervalo para el número de clases es de __3 a 7__. No utilice más de __9__ clases, ya que se hace difícil distinguirlas y ello dificulta la comprensión del mapa.
:::

En el ejemplo que figura más abajo se ve un histograma de la población de distrito. Eso significa que tenemos un conjunto de datos con distritos y con la cantidad de personas que viven en cada uno de ellos. Solo basándonos en el histograma podemos hacer algunas afirmaciones generales.

1. No hay distritos con población nula o cero.
2. Solo hay unos pocos distritos con muy poca población.
3. Parece que hay tres grupos generales de distritos.

:::{figure} /fig/Histogramm_example.drawio.svg
---
width: 900px
align: center
name: es_Histogram_example.drawio
---
Histograma de datos de población. Fuente: [Axis Maps](https://www.axismaps.com/guide/data-classification).
:::

Sin embargo, si queremos mostrar en un mapa qué distritos tienen más población que otros, tenemos que clasificar los distritos.

Existen __siete__ maneras en QGIS de dividir datos cuantitativos en clases. Las cuatro más importantes son: __intervalos equitativo__, __cuantil__, __cortes naturales__ y __manual__. Veamos cómo quedarían las clases de la población de distrito si dividiéramos los datos en tres clases utilizando estos métodos.


:::{figure} /fig/classification_method_map.drawio.svg
---
width: 900px
align: center
name: classification_method_map
---
Diferentes clasificaciones. Fuente: HeiGIT (adaptado de [Axis Maps](https://www.axismaps.com/guide/data-classification))
:::



::::{tab-set}

:::{tab-item} Intervalo equitativo
La clasificación por intervalos equitativos divide los datos en clases de tamaño uniforme, como 0-10, 10-20, 20-30, etc. Es eficaz para datos distribuidos uniformemente en toda la serie. Sin embargo, se recomienda tener precaución cuando los datos están sesgados o tienen valores atípicos significativos, ya que esto puede dar lugar a clases vacías. Los datos de población utilizados aquí, al carecer de grandes valores atípicos, son adecuados para la clasificación por intervalos equitativos.
:::

:::{tab-item} Recuento equitativo (cuantil)
La clasificación por cuantiles garantiza un número igual de observaciones en cada clase, lo que crea mapas visualmente atractivos. Sin embargo, puede dar lugar a clases con rangos numéricos significativamente diferentes y, en algunos casos, se separan tasas similares y se agrupan tasas diferentes. Es aconsejable utilizar un histograma para evaluar posibles problemas. En el ejemplo de la población de distrito, la clasificación por cuantil produjo un corte cuestionable, al combinar una parte del tercer grupo con la clase 2 a pesar de su mayor proximidad numérica a otras observaciones de la clase 3.
:::

:::{tab-item} Cortes naturales
Los cortes naturales constituyen un método de clasificación óptimo cuyo objetivo es minimizar la diferencia dentro de una clase y maximizar las diferencias entre clases para un número determinado de clases. Sin embargo, produce una solución de clasificación única para cada conjunto de datos, lo que puede ser un inconveniente a la hora de hacer comparaciones entre mapas, como en una serie o atlas. En tales casos, sería preferible aplicar el mismo sistema de clasificación en todos los mapas.
:::

:::{tab-item} Manual
La clasificación manual permite a los usuarios establecer uno o todos los cortes de clase según necesidades específicas. Este enfoque resulta útil cuando es necesario predeterminar ciertos puntos de corte, como la alineación con la media o el mantenimiento de la uniformidad en una serie de mapas. La clasificación manual se recomienda cuando otros métodos proporcionan una buena solución, pero pueden beneficiarse de ligeros ajustes para adaptarse mejor a necesidades o a métodos de visualización específicos.
:::

:::{tab-item} Escala logarítmica
La clasificación en escala logarítmica se emplea cuando los datos abarcan varios órdenes de magnitud y una escala lineal no representa eficazmente las variaciones. Esta escala aplica una transformación logarítmica a los datos, al comprimir los valores más grandes y expandir los más pequeños. Es útil para visualizar datos con crecimiento o decrecimiento exponencial. Sin embargo, la interpretación de los valores en una escala logarítmica puede requerir una comprensión profunda. Considere la posibilidad de utilizar una escala logarítmica cuando exista una serie amplia de valores y una escala lineal pueda ocultar patrones o tendencias importantes.
:::

:::{tab-item} Cortes redondeados
Cortes redondeados es un método de clasificación diseñado para crear mapas visualmente atractivos y fáciles de interpretar. Este enfoque busca generar cortes de clase que se alineen con números “redondos”, lo que hace el mapa más intuitivo para los lectores. Cortes redondeados es especialmente útil cuando se comunican datos espaciales complejos a un público amplio, ya que mejora la claridad y comprensibilidad del mapa. Tenga en cuenta que la elección de cortes redondeados puede depender del contexto específico y de las preferencias del público destinatario.
:::

:::{tab-item} Desviación estándar
La clasificación por desviación estándar es un método que determina los cortes de clase según la desviación estándar de los valores de los datos. Este enfoque organiza los datos en clases teniendo en cuenta la distribución de los valores en torno a la media. Cada clase representa un determinado número de desviaciones estándar de la media, lo que proporciona una base estadística para categorizar los datos. Esta clasificación es eficaz cuando se desea resaltar la variabilidad dentro del conjunto de datos. Sin embargo, es importante considerar la naturaleza de la distribución de los datos y si este método se ajusta a los objetivos analíticos del mapa.
:::

::::


::::{dropdown} Cómo: Establecer la clasificación graduada en QGIS
:open:

La configuración de una clasificación graduada en QGIS es similar a la configuración de una clasificación por categorías. Sin embargo, a diferencia de esta última, aquí tiene que decidir cuántas clases y qué método de graduación desea utilizar.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/graduated_classification.mp4"></video>

__Clasificar los datos en clases…__
1. Haga clic derecho en la capa.
2. Haga clic en `Simbología`.
3. Haga clic en `Graduado`.
4. En el menú desplegable `Valor` seleccione la columna según la cual desea clasificar sus datos.
5. Seleccione el número de clases que desea utilizar.
6. En `Modo` seleccione el método de clasificación que desea utilizar, p. ej., recuento equitativo (cuantil).
7. Haga clic en `Clasificar`. Ahora debería ver todas las clases y la distribución de los valores. Para añadir o eliminar clases utilice los botones `-` y `+`.
8. *Opcional*: Haga clic en `Histograma` → `Cargar valores`. Ahora puede ver la distribución exacta de los valores entre las clases. Esto resulta muy práctico para elegir un método de clasificación. También puede comprobar el valor medio y la desviación estándar.

:::{figure} /fig/Graduated_histogram.png
---
width: 900px
name: es_Graduated_histogram
align: center
---
Clasificación graduada. Fuente: [Axis Maps](https://www.axismaps.com/guide/data-classification).
:::

9. *Opcional*: En el menú desplegable `Símbolo` puede seleccionar los colores y símbolos que desea utilizar.
10. *Opcional*: En el menú desplegable `Rama de color` puede especificar la gama de colores que desea utilizar. Para ver todas las rampas de color, haga clic en la flecha hacia abajo de la `Rampa de color` → `Todas las rampas de color`.
11. *Opcional*: En `Tamaño de leyenda definido por datos` puede ajustar la precisión con la que se mostrará el rango de las clases en la leyenda. Normalmente, es práctico no utilizar números demasiado complicados.
12. *Opcional*: Puede abrir el panel `Representación de capas` en el botón de la ventana. Aquí puede ajustar la opacidad/transparencia de la capa.
13. Haga clic en `Aplicar` para aplicar el ajuste.
14. Haga clic en `Aceptar` para cerrar la ventana.

:::{figure} /fig/classification_graduated_basic.png
---
width: 900px
name: classification_graduated_basic
align: center
---
Clasificación graduada en QGIS 3.36.
:::
::::

## Preguntas de autoevaluación

::::{admonition} Compruebe lo que aprendió
:class: note

1. __¿Qué es la clasificación de datos geoespaciales y por qué es útil en los SIG?__

:::{dropdown} Respuesta
- La clasificación de datos geoespaciales es el proceso de agrupar o categorizar las entidades de los datos geográficos por valores de atributos compartidos (o rangos) y, a continuación, asignar a cada clase su propio símbolo o color.
- Esto ayuda a visualizar patrones, hacer que los mapas sean más fáciles de interpretar, distinguir diferencias en los datos y comunicar la variación espacial con mayor claridad (especialmente en el caso de atributos cuantitativos o categóricos).
:::

2. __¿Cuáles son los tres métodos de clasificación más comunes disponibles en QGIS? Explique sus diferencias.__

:::{dropdown} Respuesta
QGIS admite estos tres modos de clasificación habituales:

| Método | Caso de uso y tipo de datos | Funcionamiento y diferencias |
|-------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Símbolo único** | Para conjuntos de datos sencillos o cuando se desea que todas las entidades tengan el mismo aspecto. | Todas las entidades reciben el mismo símbolo (color, tamaño). No hay diferenciación por atributos. |
| **Categorizado** | Para datos **nominales** u **ordinales** (categóricos). | Las entidades se agrupan por valores de atributo únicos (categorías). Cada categoría tiene su propio símbolo. |
| **Graduado** | Para **datos cuantitativos/métricos**. | Los valores numéricos se dividen en clases numéricas (rangos). Cada clase se simboliza de forma diferente (a menudo mediante una rampa). Puede elegir varias clases y métodos de clasificación (p. ej., intervalo equitativo, cuantil o cortes naturales). |



:::

3. __Nombre tres métodos diferentes para dividir los datos cuantitativos en clases. ¿Cuáles son sus diferencias?__

:::{dropdown} Respuesta
| Método                     | Descripción/Forma de determinar cortes                                                                                    | Fortalezas e inconvenientes                                                                                                                 |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Intervalo equitativo**         | Divide la serie completa de datos en intervalos de igual tamaño (p. ej., dividiendo [min., máx.] en n intervalos de igual anchura)              | Sencillo e intuitivo, pero puede dar lugar a muchas clases vacías o poco pobladas si los datos están sesgados o tienen valores atípicos.           |
| **Cuantil (recuento equitativo)** | Cada clase recibe (aproximadamente) el mismo número de entidades (es decir, recuentos iguales por clase)                                        | Buen equilibrio visual, pero los intervalos numéricos de las clases pueden variar mucho, y valores similares pueden dividirse entre clases.             |
| **Cortes naturales (Jenks)** | Utiliza un algoritmo para minimizar la diferencia dentro de la clase y maximizar las diferencias entre clases (es decir, encuentra agrupaciones “naturales”) | A menudo proporciona cortes visualmente significativos adaptados a la distribución de los datos. Pero los cortes dependen del conjunto de datos (menos comparables entre mapas). |


:::

4. __¿Cuáles son las ventajas y desventajas de elegir el número de clases de una clasificación graduada?__

:::{dropdown} Respuesta
- Más clases = más detalle, pero, si son demasiadas, el mapa resulta confuso (se hace difícil distinguir colores o diferencias sutiles). El módulo sugiere mantener las clases entre 3 y 7, y no más de 9.
- Si las clases son demasiado pocas, se puede simplificar en exceso y ocultar variaciones o extremos importantes.
- Si hay demasiadas clases, el mapa queda desordenado, los colores se parecen demasiado y resulta más difícil interpretarlo o compararlo.
- La distribución de los datos es importante: los datos muy sesgados o los valores atípicos pueden distorsionar los rangos de clase, lo que hace que la mayoría de las entidades se agrupen en unas pocas clases y dejen otras casi vacías.
- En el caso de los mapas comparativos (p. ej., series de mapas), el uso de cortes diferentes en cada mapa (porque los datos difieren) puede reducir la comparabilidad; los cortes fijos pueden ayudar a la uniformidad, pero es posible que no se adecuen por igual a la distribución de cada conjunto de datos.
:::

::::

