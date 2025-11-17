::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Procesamiento de datos espaciales

## Introducción

El procesamiento espacial utiliza la información espacial para extraer un nuevo significado de los datos de SIG. Para ello, utiliza la __relación espacial__ de diferentes capas o entidades. Las relaciones espaciales describen cómo se sitúan las cosas entre sí. En el ámbito humanitario, esto ayuda a responder a preguntas críticas como "¿Qué comunidades están cerca de una fuente de agua?" o "¿Qué zonas están aisladas de los servicios de salud?". O puede que queramos identificar los mejores lugares para distribuir la ayuda, evaluar las zonas de riesgo de inundaciones o planificar las rutas de evacuación.

Ya hemos encontrado relaciones espaciales en el módulo 3 en el subcapítulo sobre __[operadores geométricos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_data_queries.html#geometric-operators)__, también denominados predicados geométricos en QGIS.
En el cuadro siguiente se describen las relaciones espaciales y se dan ejemplos de cuándo estas relaciones espaciales son relevantes en la ayuda humanitaria.

## Relaciones espaciales

| __Relación espacial__ | __Descripción__ | __*Ejemplo en el ámbito humanitario*__ |
| ------------------------ | --------------- | -------------------------- |
| __Proximidad__ | Lo cerca que está una cosa de otra | *Encontrar los refugios más cercanos a una comunidad desplazada* |
| __Contención__ | Si algo está dentro de otra área/polígono | *Determinar qué escuelas se encuentran dentro de una zona específica afectada por un conflicto* |
| __Intersección__ | Identificar las entidades geométricas superpuestas | *Buscar zonas en las que la infraestructura dañada se superponga con poblaciones vulnerables* |
| __Adyacencia__ | Entidades geométricas que comparten un punto o un límite | *Identificar las regiones limítrofes con una zona de conflicto que puedan correr riesgo de desplazamiento* |
| __Conectividad__ | Cómo se conectan las cosas a través de redes como carreteras, ríos o incluso rutas comerciales | *Trazar el camino más corto entre pueblos y hospitales para planificar evacuaciones de emergencia* |
| __Dirección__ | Posición relativa, como norte, sur, este, oeste, o posición relativa respecto a la corriente de un río, por ejemplo | *Localizar los pueblos al norte de un río que están aislados debido a las inundaciones y a la inaccesibilidad de los puentes de conexión* |

QGIS ofrece una variedad de herramientas de procesamiento espacial que podemos utilizar para analizar y crear nuevas perspectivas utilizando estas relaciones espaciales. Por ejemplo:
- __Uniones espaciales__ nos permite unir valores de atributos de una capa a otra basándonos en su relación espacial. Esto nos permite enriquecer los conjuntos de datos e
incorporar información adicional procedente de capas, que puede ayudarnos a comprender una situación.
- La operación de superposición __Recorte__ puede emplearse para extraer áreas de interés específicas de múltiples capas, lo que nos permite centrar nuestra atención donde más se necesita.
- La operación __Disolución__ nos permite simplificar geometrías uniendo geometrías de dos capas distintas.
- Mediante __zona de influencia__, podemos crear zonas alrededor de entidades para ayudar a identificar áreas vulnerables y planificar rutas de evacuación en caso de inundación.
- __Centroides__ crea puntos en el centro geométrico de las geometrías de una capa. Esto resulta especialmente útil para crear mapas con símbolos graduados


:::{figure} /fig/en_module5_spatial_geodataprocessing.PNG
---
width: 750 px
name: en_module5_spatial_geodataprocessing
---
Distintas herramientas de geoprocesamiento espacial. Fuente: Adaptado de [Saylor Academy](https://saylordotorg.github.io/text_essentials-of-geographic-information-systems/s11-geospatial-analysis-i-vector-o.html)
:::

En este capítulo, exploraremos en primer lugar las __uniones espaciales__. Las uniones espaciales, por ejemplo, nos permiten importar atributos de una capa a otra en función de su ubicación en relación con las entidades geográficas de otra capa. Estas relaciones espaciales también pueden utilizarse para seleccionar entidades de una capa. Además, repasaremos las herramientas de procesamiento espacial __zona de influencia__, __recorte__ y __disolución__. Estas operaciones permiten combinar geometrías de dos capas de varias maneras (véase {numref}`en_module5_spatial_geodataprocessing`).


## Uniones espaciales

Las uniones son formas de combinar dos capas de datos diferentes. En general, existen dos tipos de uniones: __uniones no espaciales__ y __uniones espaciales__.

- Las uniones no espaciales se basan en valores de atributos específicos, que se utilizan como campos ID, para combinar dos capas. Se tratan en el capítulo "[Herramientas de procesamiento no espacial](/content/es/Module_5/es_qgis_non_spatial_tools.md)" de este módulo.
- A veces queremos combinar información de diferentes capas que no comparten un valor común. En estos casos, podemos utilizar las uniones espaciales, que nos permiten unir datos basándonos en reglas de localización.
- Las uniones espaciales en QGIS mejoran los atributos de la capa de entrada añadiendo información adicional de la capa de unión, apoyándose en su __relación espacial__. Este proceso enriquece sus datos incorporando detalles relevantes de una capa a otra en función de sus asociaciones geográficas.
- En QGIS, una unión espacial crea una nueva capa comparando las entidades de una capa con las de otra, en función de
su relación espacial.
- La capa unida resultante __recibe atributos__ de ambas capas en función de los parámetros elegidos.

Por ejemplo:

- Cualquier punto __dentro de__ un polígono debe heredar atributos del polígono.

::::{card}
__Ejemplo en el ámbito humanitario:__
^^^
*Se dispone de un modelo de profundidad de inundación y el objetivo es determinar qué edificios se inundan en este escenario. Esto puede lograrse realizando una unión espacial para añadir la profundidad de la inundación a la capa de polígonos que contiene las casas.*

*El mapa resultante podría tener este aspecto:*

:::{figure} /fig/en_flood_damage_assessement_libya.png
---
name: en_flood_damage_assessement_libya
width: 450 px
---
Una capa de área en construcción combinada con una capa de extensión de la inundación. Al unirlas, podemos evaluar qué casas corren riesgo de sufrir daños por inundaciones (fuente: IFRC).
:::

::::

## Operadores geométricos

Las uniones espaciales se basan en los operadores geométricos. En las pestañas siguientes, puede encontrar los diferentes operadores geométricos disponibles en QGIS y cómo afectan al procesamiento de datos.

::::{tab-set}

:::{tab-item} Intersección
Compruebe si la geometría de las dos capas se intersecan entre sí. El algoritmo devuelve el valor "Verdadero" (1), si las geometrías se intersecan espacialmente. Esto significa que comparten cualquier porción de espacio, se superponen o se tocan. Si no se superponen, los algoritmos devuelven el valor "Falso" (0). En la imagen siguiente, el algoritmo devuelve los círculos __1, 2 y 3__.
:::


:::{tab-item} No interseca
Las entidades no intersecas no comparten ninguna porción de espacio. Esto significa que no se tocan ni se superponen. En la imagen más abajo, el algoritmo produciría una capa con solo el círculo 4.
:::

:::{tab-item} Igual
El algoritmo devuelve una capa con geometrías exactamente iguales (todos los puntos y líneas son iguales). En la imagen siguiente, no se devuelve ningún círculo (añadido a la capa de salida). 
:::

:::{tab-item} Toca
Comprueba si una geometría toca a otra. El algoritmo genera una nueva capa con las geometrías que tienen al menos un punto en común, pero cuyos interiores no se intersecan. En la imagen siguiente, solo se devuelve el círculo 3.
:::

:::{tab-item} Superposición
Compruebe si las geometrías se superponen. Devuelve geometrías si comparten espacio, son de la misma dimensión, pero no están completamente contenidas entre sí. En la imagen siguiente, solo se devuelve el círculo 2.
:::

:::{tab-item} Dentro de
Comprueba si una geometría está dentro de otra. Devuelve las geometrías a si están completamente dentro de la geometría b. Solo se devuelve el círculo 1.
:::

:::{tab-item} Contiene
Devuelve geometrías si y solo si ningún punto de b está en el exterior de a, y al menos un punto del interior de b está en el interior de a. En la imagen, no se devuelve ningún círculo, pero el rectángulo si se buscara, el resultado sería en sentido inverso, ya que contiene completamente al círculo 1. Es lo contrario de "dentro de".
:::

:::{tab-item} Cruza
Devuelve geometrías que tienen algunos puntos interiores en común, pero no todos, y el cruce real es de una dimensión inferior a la geometría suministrada más alta. Por ejemplo, una línea que cruza un polígono se cruzará como una línea (verdadero). Dos líneas que se cruzan se cruzarán como un punto (verdadero). Dos polígonos se cruzan como un polígono (falso). En la imagen de abajo, no se devolverá ningún círculo.
:::

::::

:::{figure} /fig/en_select_by_location.png
---
width: 600 px
name: en_select_by_location
---
Buscando relaciones espaciales entre capas <br /> (fuente: [QGIS Documentation](https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html?highlight=join%20attributes%20location), Version 3.28)
:::

### Ejercicio: Realizar una unión espacial


:::{admonition} ¡Ahora es su turno!
:class: tip

El ejercicio práctico es crucial para comprender cómo funcionan los SIG y QGIS. Puede seguirlo paso a paso descargando los datos necesarios.

:::

En el ejemplo anterior ({numref}`en_spatial_join_example`), tenemos un conjunto de datos que contiene el conjunto de datos de centros de salud por healthsite.ioand con los límites administrativos (adm2) de Nigeria. Queremos saber en qué estado se encuentra cada centro de salud. Para ello, debemos utilizar la herramienta "Unir atributos por ubicación".

:::{figure} /fig/en_spatial_join_example.png
---
name: en_spatial_join_example
width: 400 px
---
Un ejemplo de una situación en la que utilizará una unión espacial (fuente: BRC)
:::

::::{margin}

:::{tip}
Puede encontrar y activar el panel de la caja de herramientas de Procesos navegando a `View` > `Panels` > `Processing Toolbox`. Debería aparecer en la parte derecha de la pantalla.
:::

::::

::::{dropdown} __Herramienta:__ Unir atributos por ubicación

Esta herramienta toma dos capas de entrada y crea una nueva capa vectorial que tiene los atributos de ambas capas en su tabla de atributos.
- La primera capa de entrada (véase "Unir a entidades en" en {numref}`en_spatial_join_1`) dicta qué entidades geométricas se copiarán en la nueva capa.
- La segunda capa de entrada (véase "Comparando con" en {numref}`en_spatial_join_1`) dicta los atributos que se añadirán a la nueva capa sobre los atributos de la primera capa de entrada. Puede seleccionar cuáles de estos atributos deben transferirse a la nueva capa.


:::{figure} /fig/en_spatial_join_1.PNG
---
width: 450 px
name: en_spatial_join_1
---
La herramienta "Unir atributos por ubicación" de QGIS 3.36.
:::

::::

1. Descargue los conjuntos de datos necesarios de HDX
    - [nigeria-healthsites-shp](https://data.humdata.org/dataset/nigeria-healthsites)
    - [nga_adm_osgof_20190417.zip](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_5/es_qgis_spatial_tools.html)
2. Descomprima los archivos, cree un nuevo proyecto QGIS y cargue los archivos en el proyecto QGIS.
3. Busque la herramienta __"Unir atributos por ubicación"__ en la caja de herramientas de Procesos y <kbd>haga doble clic</kbd> sobre ella. Se abrirá una nueva ventana
(véase {numref}`join_by_location_ex1`).
4. Utilice la capa de centros de salud como objetivo ("Unir a entidades en") y la capa adm2 como capa de comparación ("Comparando con").
5. Utilice `are within` como predicado geométrico.
6. Seleccione los campos que desea añadir: `ADM2_EN`, `ADM2_PCODE`
7. Seleccione `Discard records that could not be joined`
8. Haga clic en `Run` para continuar; el registro debería confirmar que se ha realizado correctamente.
9. Aparecerá una nueva capa (temporal) denominada "Entidades unidas" en el panel de capas
10. <kbd>Haga clic con el botón derecho</kbd> en la capa y seleccione "Exportar" o "Establecer" para guardar la nueva capa.



Enhorabuena, ¡ya hemos añadido la información sobre la región administrativa a la capa de centros de salud! Podemos simbolizar la capa unida con la simbología categorizada para comprobar si ha funcionado (véase {numref}`spatial_join_ex1_results_categorised`). Obsérvese que los puntos del conjunto de datos original que estaban fuera de la frontera de Nigeria se han descartado, ya que no se han podido unir.

:::{figure} /fig/spatial_join_ex1_results_categorised.png
---
name: spatial_join_ex1_results_categorised
width: 500 px
---
Los diferentes colores de los puntos indican que están situados en un estado diferente (adm2).
:::


### Más herramientas de unión espacial en QGIS

Por defecto, QGIS proporciona tres herramientas diferentes para realizar uniones espaciales.

- La primera, y la más común, es la herramienta __"Unir atributos por ubicación"__ que hemos utilizado en el ejercicio anterior.
- También existen las herramientas __"Unir atributos por ubicación (resumen)"__ y __"Unir atributos por el más cercano"__.

:::::{tab-set}

::::{tab-item} Unir atributos por ubicación (resumen)

Esta herramienta es similar a la herramienta "Unir atributos por ubicación". Sin embargo, además de añadir los atributos de una capa a otra, este algoritmo también calcula resúmenes estadísticos de los valores de las entidades coincidentes en la segunda capa. Estos resúmenes incluyen una amplia gama de opciones, como __valores mínimos y máximos__, __valores medios__, así como __recuentos__, __sumas__, __desviación estándar__, y mucho más.

:::{figure} /fig/en_spatial_join_3.PNG
---
width: 450 px
name: en_spatial_join_3
---
Captura de pantalla de la herramienta Unir atributos por ubicación (resumen) en QGIS 3.36
:::

::::

::::{tab-item} Unir atributos por el más cercano

Este tipo de unión espacial es similar a las otras dos uniones, pero la unión de entidades se produce __identificando las entidades más cercanas__ de cada una de estas capas. Además, si se especifica una distancia máxima, solo se considerarán coincidencias adecuadas para el proceso de unión las entidades que se encuentren dentro de esta distancia designada.


:::{figure} /fig/en_spatial_join_2.PNG
---
width: 450 px
name: en_spatial_join_2
---
Captura de pantalla de la herramienta Unir atributos por el más cercano en QGIS 3.36
:::

::::

:::::

:::{note}
Encontrará una descripción detallada de las funciones y configuración de estas herramientas en la documentación de [QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location)

:::


### Ejercicio: Calcular la suma de la población afectada y la superficie inundada para el área de interés


Tras las inundaciones, es fundamental disponer de datos sobre la población afectada y el alcance de las inundaciones. Esta información puede refinarse a partir de un conjunto de datos de ámbito nacional para obtener cifras específicas de distritos o estados concretos. Esto puede ayudar a identificar las zonas más afectadas, lo que permitirá llevar a cabo operaciones de ayuda humanitaria más eficaces. En el próximo ejercicio, calcularemos la extensión total de las inundaciones en kilómetros cuadrados y la población afectada en el estado de Unity, Sudán del Sur. Para ello, utilizaremos la herramienta __Unir atributos por ubicación (resumen)__.

1. Cargue los datos necesarios para este ejercicio en su QGIS. Ambos conjuntos de datos se descargaron de HDX:
    - [Sudán del Sur, Límites administrativos subnacionales](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/Spatial_Join/State_Unity_South_Sudan.zip):<br /> __State_Unity_South_Sudan.shp__
    - [Extensiones de agua detectadas por satélite entre el 11 y el 15 de agosto de 2023 sobre Sudán del Sur](https://data.humdata.org/dataset/satellite-detected-water-extents-between-11-and-15-august-2023-over-south-sudan): Descargue la carpeta __FL20220424SSD_SHP.zip__, descomprímala y busque el archivo __VIIRS_20230811_20230815_MaximumFloodWaterExtent_SouthSudan.shp__.
2. Localice la herramienta denominada __Unir atributos por ubicación (resumen)__.
    - Elija __límites estatales__ como capa de destino para unir entidades.
    - Establezca __interseca__ como relación espacial.
    - Seleccione __capa de extensión de inundación__ como capa de comparación.
    - Especifique los campos a resumir como __Area_km2__ y __Pop__.
    - Seleccione __sum__ como tipo de resúmenes a calcular.
    - Haga clic en `Run` para iniciar el proceso.
3. Una vez completado, tendrá acceso a la información sobre la __población total afectada__ y __zonas inundadas__ para todo el estado de Unity.


:::{dropdown} Solución: Calcular la suma de la población afectada y la superficie inundada para el área de interés
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_spatial_join.mp4"></video>
:::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Qué diferencia a una herramienta de procesamiento espacial de otra no espacial?__

:::{dropdown} Respuesta
Una herramienta de __procesamiento espacial__ opera sobre la geometría (ubicación, forma, relación espacial) de entidades (puntos, líneas, polígonos o celdas ráster) y utiliza esa información espacial (p. ej., distancia, adyacencia, superposición) en su operación. Una herramienta de__ procesamiento no espacial__ opera únicamente sobre datos de atributos o tabulares sin tener en cuenta la geometría (por ejemplo, ordenar una tabla, calcular un campo, unir tablas por clave).
:::

2. __Nombre y describa brevemente al menos tres herramientas u operaciones espaciales comunes cubiertas (p. ej., zona de influencia, recorte, disolución, intersección, unión).__

:::{dropdown} Respuesta
- __Zona de influencia:__ Crea una zona a una distancia especificada alrededor de las entidades de entrada (puntos, líneas o polígonos). Por ejemplo, alrededor de la línea de una carretera se crea un polígono de zona de influencia de 100 m que representa toda el área en un radio de 100 m de la carretera.
- __Recorte:__ Utiliza una capa (la capa de "recorte") para recortar o cortar otra capa de modo que solo quede la parte de la capa de entrada que cae dentro (o quizá fuera) de la capa de recorte. Extrae eficazmente un subconjunto de geometría.
- __Disolución:__ Fusiona las entidades adyacentes o superpuestas en una capa basándose en un atributo compartido (o simplemente elimina los límites internos) para que las entidades se conviertan en formas agregadas más grandes. Por ejemplo, combinar muchas unidades administrativas pequeñas en una más grande basada en un código de región.
:::

3. __Si tiene una capa de carreteras y aplica una zona de influencia de 100 m alrededor de cada carretera, ¿cuál es la geometría resultante y cuál es un posible caso de uso?__

:::{dropdown} Respuesta
- El resultado serán entidades de polígonos (zonas) que representan todas las áreas en un radio de 100 m de cada carretera. Así, si las carreteras de entrada son entidades lineales, después de la zona de influencia tendrá polígono(s) que "envuelven" cada línea de carretera, extendiéndose a ambos lados 100 m (suponiendo una zona de influencia plana simple).
- Se podría utilizar una zona de influencia para amortiguar una trayectoria del ciclón y aproximarse a la región afectada por el ciclón (véase [Flujo de trabajo de activación de QGIS para Madagascar](https://giscience.github.io/gis-training-resource-center/spanish/content/es/GIS_AA/es_qgis_cyclone_trigger_madagascar.html)).

:::

4. __¿Por qué es importante comprobar si las capas de entrada tienen proyecciones cartográficas/SRC compatibles antes de ejecutar las herramientas espaciales?__

:::{dropdown} Respuesta
- Si las capas tienen diferentes SRC (o datos) y se aplica una herramienta espacial sin realizar una reproyección adecuada, los cálculos de geometría (distancias, áreas, zona de influencia, superposición) pueden ser incorrectos o engañosos. Por ejemplo, una zona de influencia de "100 m" puede ser en realidad 100 unidades de un sistema de coordenadas diferente (grados o pies), por lo que la distancia en el mundo real es incorrecta.
- Las operaciones espaciales dependen de relaciones geométricas precisas; si una capa está en, por ejemplo, grados geográficos WGS84 y otra está en un SRC basado en metros proyectados, el desajuste puede causar desalineación, estiramiento, distorsión o errores en los resultados.
- Garantizar la compatibilidad de las proyecciones ayuda a mantener la precisión espacial, la exactitud del área/distancia y las relaciones topológicas válidas (p. ej., superposiciones, intersecciones), que son fundamentales para obtener resultados significativos.

::::
