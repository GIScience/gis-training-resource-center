::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Procesamiento no espacial

#### Introducción

El procesamiento de datos no espaciales en QGIS se refiere a la manipulación de datos de atributos sin implicar directamente componentes o información espacial, como las relaciones espaciales o las geometrías.
- Modifica los atributos no geométricos de los conjuntos de datos (es decir, la tabla de atributos).
- El procesamiento no espacial puede utilizarse para realizar cálculos, generar estadísticas y obtener información sobre los aspectos no espaciales de los conjuntos de datos geoespaciales.
- QGIS ofrece diversas herramientas de procesamiento no espacial para ayudar a los usuarios a gestionar y analizar eficazmente los datos de atributos.
- Esto puede incluir la limpieza, transformación, enriquecimiento y análisis de datos basados en la información de atributos asociada, como estadísticas de población, clasificaciones de uso del suelo o indicadores económicos.

:::{figure} /fig/en_attribute_table_large.PNG
---
height: 500px
name: es_attribute_table_large
---
Captura de pantalla de una tabla de atributos para la versión 3.28.4 de QGIS.
:::

## Uniones no espaciales (unir atributos por valor de campo)

- Se pueden hacer muchos análisis con una sola capa. Pero, a veces, la información necesaria para nuestro análisis está __dividida entre__ diferentes conjuntos de datos/capas de datos.
- Con QGIS, estas capas pueden __combinarse__ para realizar el análisis que deseemos. La forma más sencilla de combinar capas es mediante una __unión de atributos__. Esta operación busca información de una segunda fuente de datos basándose en un __valor de atributo compartido__. Este valor funciona como identificador único común, también conocido como ID, UID o clave (véase {numref}`es_simple_attr_join_example`).

:::{figure} /fig/simple_attr_join_example.png
---
name: es_simple_attr_join_example
width: 500 px
---
Las entradas de las dos tablas de datos pueden unirse a través del campo ID común.
:::

::::{card}
__Ejemplo en el ámbito humanitario:__
^^^
*Un flujo de trabajo SIG habitual en el ámbito humanitario que implica uniones no espaciales consiste en unir datos sobre límites administrativos utilizando códigos P como identificador común/atributo compartido.

Los códigos P son códigos de identificación de unidades administrativas (por ejemplo, país (adm0), región (adm1), distrito (adm2)), que se introdujeron para simplificar la unión de datos tabulares sobre regiones administrativas. Estos códigos identifican claramente las unidades administrativas facilitando las uniones no espaciales.

Por ejemplo: Tenemos un conjunto de datos espaciales que contiene los límites administrativos de los distritos (adm2) de Nigeria y una tabla de datos que contiene la población por distrito, pero sin los polígonos. Utilizando los códigos P como atributos de identificación, podemos unir fácilmente los datos de población con el conjunto de datos vectoriales.*

:::{figure} /fig/en_attribute_join_pcode_example.png
---
name: es_attribute_join_pcode_example
width: 550 px
---
El código P asociado al distrito Edo Sur es NG01201.
:::

::::


:::{Attention}
- Una unión de atributos en QGIS solo funciona correctamente cuando los atributos **coinciden exactamente**.
- Por ejemplo: **"S. Sudán"** no coincidirá con **"South Sudan"**.
- Siempre que sea posible, lo mejor es **utilizar atributos que hayan sido diseñados para la unión**, como los **códigos P** o los **identificadores** que no puedan lugar a errores ortográficos.
:::

### Ejercicio: Realizar una unión no espacial

En este breve ejercicio guiado, añadiremos los datos de población a la capa de límites administrativos (adm1).

1. Descargue las capas necesarias [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_5/non_spatial_join/non_spatial_join.zip), descomprímalas y añádalas a su proyecto QGIS.

:::{tip}
La capa de población debe [añadirse como una capa de texto delimitada](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_geodata_concept.html#delimited-text-import-csv-txt) (`Capa` → `Añadir capa` → `Añadir capa de texto delimitado`) sin geometría.
:::

2. Abra la herramienta `Unir atributos por valor de campo` de la caja de herramientas de Procesos.
3. Como capa de entrada 1, seleccione la capa `nga_admbnda_adm1_osgof_20190417`, configure "campo de tabla" a `ADM1_PCODE`
4. Como capa de entrada 2, seleccione la capa `nga_adm1pop_2022`, configure "campo de tabla 2" a `ADM1_PCODE`. Además, en `campos de la tabla 2 a copiar`, seleccione `F_TL`, `M_TL` y `T_TL`.
5. Haga clic en `Ejecutar`. Aparecerá una nueva capa en su panel de capas denominada "Capa unida".

:::{figure} /fig/en_3.36_pcode_join.png
---
name: es_3.36_pcode_join
width: 450 px
---
Configurar los parámetros de la unión en Pcode
:::

6. Abra la tabla de atributos de la nueva capa y desplácese hacia la derecha. Aquí encontrará los atributos unidos.

¡Estupendo! Hemos añadido correctamente los datos de población a nuestra capa de límites administrativos. Ahora, podemos visualizar la distribución de la población o seguir analizando nuestros datos.


:::{figure} /fig/nga_pop_join.png
---
name: es_nga_pop_join
width: 600 px
---
Los datos unidos se clasifican utilizando la simbología graduada para el valor de población.
:::


## Funciones de la tabla

Las funciones de la tabla suelen implicar solo una única capa de datos y manipulan la tabla de atributos. Puede añadir nuevos campos, eliminar campos no deseados o incluso calcular nuevos campos utilizando la __calculadora de campos__.

Para obtener una descripción general detallada de la funcionalidad de la tabla de atributos y su propósito, le invitamos a explorar el artículo de [Wiki](/content/es/Wiki/es_qgis_attribute_table_wiki.md) sobre el tema.

### Añadir campo
Se puede acceder a la información contenida en una capa vectorial a través de su __tabla de atributos__, y se puede mejorar __introduciendo nuevos campos__ en esta tabla. Estos campos adicionales pueden derivarse de cálculos, como se ejemplifica en el siguiente caso, en el que la densidad de población se calcula para proporcionar una visión más profunda de las distribuciones espaciales de la población.

:::{Attention}
La selección del tipo de datos adecuado debe coincidir con la información que se añade al nuevo campo de atributo. Téngalo en cuenta cuando vea el video de ejemplo.
:::
__Posibles tipos de datos:__

Los más comunes son:
- __Número entero: Entero (32 y 64 bits)__
- __Número decimal (real)__
- __Texto (cadena)__

Opciones adicionales:
- Fecha y hora
- Booleano

:::{dropdown} Ejemplo: Añadir un campo para la densidad de población
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_add_field.mp4"></video>
:::

### Borrar campo
También es posible __borrar campos__ de la tabla de atributos. Una práctica comúnmente utilizada es __eliminar todos los campos no utilizados o innecesarios__ de una capa antes de empezar a trabajar en ella. Esto __hace que el conjunto de datos esté mucho más organizado__.

:::{dropdown} Ejemplo: Eliminar todos los campos no utilizados o innecesarios de una capa vectorial
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_delete_field.mp4"></video>
:::

### Calcular campos

Una práctica importante es calcular los valores de los atributos de un campo, por ejemplo, a partir de los valores de otros campos. En QGIS, puede __crear un campo nuevo o actualizar un campo existente__.

:::{Note}

Es necesario __comprobar si el tipo de datos del campo__ (nuevo o actualizado) __y su cálculo coinciden__. Por ejemplo, si está calculando una proporción (por ejemplo, la densidad), el campo no debe ser de tipo entero, sino de tipo número decimal.
:::

Un ejemplo podría ser calcular la densidad de población a partir de los campos ya existentes de Población y Área.

Una herramienta muy importante para estos cálculos es la __calculadora de campo__. Le permite __realizar cálculos basados en valores de atributos existentes o funciones definidas__, por ejemplo, para calcular la longitud o el área de una entidad geométrica o, en el ejemplo dado, podría utilizarse para calcular la densidad de población basándose en los campos ya existentes Población y Área. Los resultados de estos cálculos pueden escribirse en un campo nuevo o actualizar un campo existente.

:::{figure} /fig/en_field_calculator_red_boxes.png
---
width: 100%
name: es_field_calculator_red_boxes
---
Captura de pantalla de la calculadora de campo.
:::

A continuación se enumeran los grupos más importantes y sus respectivas funciones que se proporcionan con la calculadora de campo:
- __Campos y valores__
    - Contiene una lista de campos de la capa
- __Geometría__
    - Calcula el área de una entidad de polígono: `$area`
    - Calcula la longitud de una entidad de línea: `$length`
    - Calcula el centroide de una entidad de polígono: `centroid($geometry)`
    - Calcula el cuadro delimitador de una entidad: `bounds($geometry)`
    - Calcula la distancia entre dos puntos: `distance(point_a, point_b)`
- __Matemáticas__
    - Calcula la raíz cuadrada de un campo: `sqrt("field")`
    - Calcula el `min` y `max`

:::{dropdown} Ejemplo: Calcular la densidad de población
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_calculate_field.mp4"></video>
:::


### Estadísticas básicas de los campos

La herramienta __Basic statistics for fields__ genera estadísticas para un campo específico de la tabla de atributos de una capa vectorial. Los resultados se generan como un archivo HTML y se puede acceder a ellos utilizando el enlace __ruta del archivo__ en el __Visor de resultados__. Esta operación es muy valiosa para conocer a fondo los datos con los que se pretende trabajar. Permite determinar el intervalo de valores, precisar los valores mínimos y máximos. En el ejemplo proporcionado, esta operación se aplica para calcular la densidad de población global, lo que permite identificar con facilidad la región más densamente poblada del mundo.

:::{dropdown} Ejemplo: Calcular estadísticas de densidad de población por campo para países de todo el mundo.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_field_stats.mp4"></video>
:::

### Estadísticas por categorías
Para calcular las estadísticas de un campo en función de una clase principal puede utilizar la herramienta __Statistics by categories__. La clase principal es una combinación de valores de otros campos.

__Cuestiones que deben tenerse en cuenta al realizar estos cálculos:__
* ¿Para qué campos deben calcularse las estadísticas en la tabla de atributos?
* ¿Qué campo de la tabla de atributos contiene qué información?

Para conseguir una mayor precisión en estos cálculos, la opción “statistics by categories” ofrece una visión más completa que las mencionadas anteriormente. En este caso, resulta sencillo determinar el número de ciudades por país con más de 300 000 habitantes y, para cada país, la población que vive en la mayor aglomeración urbana.

:::{dropdown} Ejemplo: Ciudades de más de 300 000 habitantes y cantidad de población en las mayores aglomeraciones.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_stats_by_category.mp4"></video>
:::

## Consultas no espaciales
En SIG, puede __consultar__ (filtrar) datos basados en información de atributos específicos. Una vez que el filtrado se ha realizado correctamente, solo se muestran las entidades deseadas que __corresponden__ al atributo elegido. El filtrado de datos es una técnica valiosa para crear __subconjuntos__ de entidades que pueden exportarse como una nueva capa.

### Selección manual
Es posible seleccionar manualmente filas concretas haciendo clic en el número que aparece a su izquierda. Esto resulta muy útil para seleccionar un número reducido de filas. Si se seleccionan correctamente, aparecerán en __amarillo__.

:::{dropdown} Ejemplo: Selección manual de filas.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_attribute_table.mp4"></video>
:::

### Selección por expresión
En este cuadro de diálogo, puede construir sus expresiones para consultar los datos. Hay varios operadores que se pueden utilizar para filtrar su capa vectorial.

::::{tab-set}

:::{tab-item} Operadores aritméticos
| operador | función          |
|----------|------------------------|
| __+__    | suma               |
| __-__    | resta           |
| __*__    | multiplicación         |
| __/__    | división               |
| __%__    | resto de la división  |
:::

:::{tab-item} Operadores de comparación
| operador | función            |
|----------|--------------------------|
| __=__    | igual a                   |
| __!=__   | no igual                |
| __<__    | menor que                |
| __>__    | mayor que             |
| __<=__   | menor que o igual a    |
| __>=__   | mayor que o igual a |
:::

:::{tab-item} Operadores lógicos
Se pueden utilizar operadores como AND, OR para combinar diferentes consultas o criterios.
| operador | función          |
|----------|------------------------|
| __AND__  | lógico Y            |
| __OR__   | lógico O             |
| __NOT__  | lógico NO            |
:::

:::{tab-item} Operadores especiales
| operador      | función                                  |
|---------------|------------------------------------------------|
| __LIKE__      | concordancia de patrones                               |
| __IN__        | comprueba si un valor está en una lista de valores       |
| __IS NULL__   | comprueba si hay valores null                         |
| __BETWEEN__   | comprueba si un valor está dentro de un rango específico |
| __CASE WHEN__ | expresiones condicionales                        |
:::

::::

La consulta de sus datos para responder a preguntas más complejas es de gran importancia. Para ello, utilice la herramienta "Selección por expresión". En el ejemplo proporcionado, aspiramos responder a la pregunta: ¿Qué ciudades, excluidas las que tenían una población de un millón de habitantes en 1950, habían superado los diez millones de habitantes en 2015?

:::{dropdown} Ejemplo: Ciudades, excluidas las que tenían una población de un millón de habitantes en 1950, que han superado los diez millones de habitantes en 2015.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_and.mp4"></video>
:::

##### SQL

Otra posibilidad para crear sus expresiones es utilizar SQL.

::::{tab-set}

:::{tab-item} Introducción a SQL
SQL (Structured Query Language) es un lenguaje de programación estandarizado que se utiliza para gestionar bases de datos y realizar diversas operaciones con los datos que contienen. En el Constructor de consultas de QGIS, puede utilizar expresiones SQL para utilizar una o más condiciones para filtrar una capa.
:::

:::{tab-item} Hoja de referencia rápida de SQL
Puede acceder fácilmente a los comandos esenciales de SQL consultando esta práctica [hoja de referencia rápida](https://www.sqltutorial.org/sql-cheat-sheet/). Ofrece un resumen conciso de las funciones básicas.
:::

::::

### Generador de consultas

El Generador de consultas proporciona una interfaz que permite definir un __subconjunto de las entidades__ en la capa utilizando comandos de tipo SQL y mostrar los resultados en la ventana principal. Mientras la consulta esté activa, solo estarán disponibles en el proyecto las entidades __correspondientes__ a su resultado. Puede utilizar uno o varios atributos de capa para definir el filtro en el generador de consultas. El generador de consultas está estructurado de la siguiente manera:

:::{figure} /fig/en_query_builder_comment.png
---
width: 100%
name: es_query_builder_comment
---
Captura de pantalla del generador de consultas.
:::

1. La __lista de campos y valores__ contiene todos los campos de la capa. Para añadir una columna de atributos a la ventana de expresión, haga doble clic en su nombre o escríbalo en la casilla.
2. El cuadro __Valores__ enumera los valores del campo actualmente seleccionado.
    - Para enumerar __todos los valores únicos__ de un campo, haga clic en el botón `Todos`.
    - Para enumerar los __primeros 25__ valores únicos de la columna, haga clic en el botón `Muestra`.
    - Para añadir un valor a la ventana de expresión, haga doble clic sobre él en la lista valores. Puede utilizar el __cuadro de búsqueda__ situado en la parte superior del panel "Values" para buscar fácilmente valores de atributos en la lista.
3. La sección __Operadores__ contiene todos los operadores utilizables. Para añadir un operador, haga clic en el botón correspondiente.
4. El botón __Probar__ ayuda a comprobar su consulta y __muestra un cuadro de mensaje con el número de entidades__ que satisfacen la consulta actual.
5. Utilice el botón __Limpiar__ para revertir la capa a su estado original.

:::{Note}
Cuando se aplica un filtro con el generador de consultas, QGIS trata el subconjunto resultante como si fuera la __capa completa__.
:::

En este breve video, descubrirá la ubicación del generador de consultas y aprenderá a crear una consulta sencilla para aislar un estado concreto de un conjunto de datos que abarca todo el país. El ejemplo se centra en un conjunto de datos relacionados con Sudán del Sur y sirve como ilustración básica.

:::{dropdown} Ejemplo: Uso sencillo del generador de consultas.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_query_builder.mp4"></video>
:::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Qué significa "procesamiento no espacial" en el contexto de SIG/QGIS? ¿En qué se diferencia de las operaciones espaciales?__

:::{dropdown} Respuesta
- El procesamiento no espacial se refiere a las operaciones que actúan únicamente sobre el lado de los atributos (la tabla o las columnas de datos) de una capa, sin utilizar ni modificar la geometría (ubicación, forma) de las entidades. Se manipulan datos sobre entidades, no sus relaciones espaciales.
- Algunos ejemplos son la adición, eliminación o actualización de campos; el filtrado de registros basado en consultas de atributos; la realización de uniones de tablas basadas en campos clave coincidentes; el cálculo de nuevos valores a partir de atributos existentes.
- Por el contrario, las operaciones espaciales implican geometría: utilizan relaciones espaciales (proximidad, intersección, contención) y a menudo producen cambios en la forma, el tamaño o la disposición de las entidades (por ejemplo, buffer, intersección, recorte, unión). Las herramientas espaciales calculan nuevas geometrías o reestructuran las existentes.
:::

2. __¿Qué es una "unión no espacial" (unir atributos por valor de campo)? Describa cómo y cuándo la utilizaría.__

:::{dropdown} Respuesta
- Una unión no espacial (en QGIS a menudo denominada Unir atributos por valor de campo) vincula datos de atributos de una tabla (o datos no espaciales) a otra capa de entidades basándose en un valor clave común (campo), no basándose en la geometría. También se denomina unión tabular o unión por atributos.
- Se utilizaría cuando se tienen dos conjuntos de datos que comparten un atributo común (por ejemplo, un código de región, un ID, un nombre) y se desea enriquecer una capa con atributos adicionales de la otra. Por ejemplo: usted tiene una capa de polígonos administrativos y una tabla separada de estadísticas de población codificadas por el mismo código administrativo; usted quiere traer esas cifras de población a la capa de polígonos para poder mapearlas o analizarlas.
- La unión no espacial añade campos de una capa o conjunto de datos a la tabla de atributos de la capa de destino cuando la clave coincide.
-
:::

3. __¿Qué condiciones deben cumplirse para que una unión no espacial funcione correctamente? (Por ejemplo, campos clave, valores coincidentes, tipos de datos)__

:::{dropdown} Respuesta

1. __Campo clave común presente en ambas tablas__
    - Tanto la capa de destino (la que recibe la unión) como la tabla de unión deben tener un campo (columna) que es la "join key", que contiene identificadores coincidentes en las filas correspondientes.
2. __Valores coincidentes en esos campos clave__
    - Los valores del campo clave deben superponerse: para cada entidad de la capa de destino de la que desee obtener datos unidos, debe haber un valor coincidente en el campo clave de la tabla de unión. Si no coinciden, el valor unido será normalmente NULL o en blanco.
3. __Tipos de datos compatibles__
    - Los campos clave deben ser del mismo tipo de datos o compatibles (por ejemplo, ambos enteros, o ambos de texto) para que QGIS pueda hacerlos coincidir. Si uno es un campo de texto y el otro es numérico, la coincidencia no funcionará de forma fiable.
4. __Unicidad de valores__
    - Lo ideal es que la tabla de unión tenga valores únicos en la clave de unión (unión uno a uno). Si hay múltiples filas coincidentes (uno a muchos), entonces es posible que se produzcan duplicados o coincidencias ambiguas; QGIS puede tomar la primera coincidencia o agregar, dependiendo del método de unión.
    - La capa de destino normalmente no cambia su número de entidades: la unión solo añade campos, no duplica la geometría (a menos que se convierta a un archivo unido permanente de manera diferente).

4. __¿Qué tipo de operaciones puede realizar con las funciones de tabla (añadir campo, borrar campo, calcular campo)?__

:::{dropdown} Respuesta
- __Añadir campo__: Crear una nueva columna de atributos (de un tipo elegido, por ejemplo, entero, decimal, texto) para contener valores calculados o importados.
- __Borrar campo__: Eliminar campos/columnas no deseados o redundantes de la tabla de atributos de una capa.
- __Calcular campo (calculadora de campo)__: Calcular nuevos valores (para campos existentes o nuevos) utilizando expresiones (aritmética, lógica condicional, funciones) basadas en otros atributos, constantes o funciones. Por ejemplo: calcular la densidad de población = población / superficie; o clasificar valores utilizando la lógica CASE WHEN.
- __Actualizar/Editar campo existente__: También se pueden actualizar o sobrescribir valores en un campo existente, siempre que la capa esté en modo de edición.
:::

5. __¿Qué es una consulta no espacial? ¿Cómo utilizaría "Select by expression" para filtrar sus datos?__

:::{dropdown} Respuesta
- Una consulta no espacial es una consulta aplicada a la tabla de atributos (campos) en lugar de basarse en la geometría. Filtra o selecciona filas (entidades) a partir de condiciones de atributo, no de condiciones espaciales.
- En QGIS, `Selccionar por expresión` es una herramienta que permite escribir expresiones lógicas (por ejemplo, `"population" > 10000 AND "region" = 'East'`) para seleccionar el subconjunto de entidades cuyos atributos satisfacen los criterios.
- Tras la selección, puede utilizar el subconjunto seleccionado para otras operaciones (por ejemplo, exportar las entidades seleccionadas, aplicarles un estilo diferente, analizarlas solo a ellas, etc.).

:::

::::

