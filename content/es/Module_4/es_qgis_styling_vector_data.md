::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Estilos de datos vectoriales

En el capítulo anterior se repasaron los fundamentos de la simbolización gráfica y las variables visuales. En este capítulo, queremos aplicar nuestra comprensión de la representación visual y aprender a utilizar el panel de estilos en QGIS para personalizar cómo se visualizan las capas en su proyecto QGIS.

## Panel de estilo

:::{figure} ../../fig/en_30.30.2_styling_panel.png
---
height: 400px
name: en_30.30.2_styling_panel
align: left
---
Panel de estilo en QGIS 3.30.2.
:::

Para cada capa de QGIS existe un panel de estilos, en el que se puede cambiar la simbología, el color y la etiqueta de las entidades de esa capa. Hay dos maneras de abrir las opciones de estilo de capa en QGIS:

1. Haga clic con el botón derecho en la capa a la que desee aplicar el estilo y seleccione `Propriedades`. Se abrirá una nueva ventana con una sección de pestañas vertical a la izquierda. Vaya a la pestaña `Simbología`.
2. Abra el panel de estilo de capas activándolo en `Ver` → `Paneles` → `Panel Estilo de Capas `. Normalmente, el panel aparecerá en la parte derecha del lienzo del mapa.

A la izquierda del panel de estilo puede elegir las distintas pestañas para acceder a las diferentes opciones de estilo.

En el panel de estilos, puede cambiar el estilo de todas las entidades de una capa y establecer categorías para los distintos símbolos,
crear etiquetas y crear rampas de color para diferenciar las entidades con valores variables.

:::{dropdown} Video: Abrir el panel de estilo
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_the_styling_panel.mp4"></video>

:::

## Simbología para datos vectoriales

Puede utilizar variables gráficas para aplicar estilos a los datos vectoriales. Como ya hemos aprendido, los datos vectoriales pueden ser puntos,
líneas o polígonos. Existen diferentes opciones para simbolizar estos diferentes tipos de datos vectoriales.

:::{figure} ../../fig/en_symbolization_vector_data.png
---
name: es_symbolization_vector_data
width: 750px
---
Simbolización de datos vectoriales; fuente: White, T. (2017). Symbolization and the Visual Variables. *The Geographic Information Science & Technology Body of Knowledge (edición segundo trimestre de 2017), John P. Wilson (ed.). DOI: 10.2222/gistbok/2017.2.3.
:::

:::{note}
Recuerde que __la simbología de la capa se guarda en su archivo de proyecto, ¡No en su shapefile!__ Si comparte un shapefile con un colega, tendrá un estilo diferente cuando lo añadan a su propio proyecto.
:::

QGIS le permite visualizar datos con el uso de marcadores simples, archivos SVG o archivos ráster. Lo más habitual es trabajar con marcadores simples. Generalmente, se utilizan para crear los símbolos de la mayoría de los elementos de un mapa. Por ejemplo, se utilizan marcadores simples para visualizar calles, siluetas de edificios, masas de agua, límites administrativos u otros polígonos.
La mayoría de los marcadores simples constan de un __relleno__ y un __contorno__. Según el tipo de geometría de la capa, deberá utilizar diferentes opciones de simbología.


- El relleno determina el color de relleno del símbolo. Puede cambiar el color y la transparencia. También puede hacer rellenos más complejos, como un relleno de patrón de línea o un relleno de símbolo SVG.
- El contorno determina el color, el tipo y el grosor del contorno. Junto al color y la transparencia, el contorno es el elemento más critico para diferenciar entre los distintos elementos. Por ejemplo, las líneas más gruesas para las carreteras suelen significar vías de un orden superior (como autopistas), mientras que las líneas discontinuas finas, podrían significar senderos, inaccesibles para los vehículos de carretera.
- Puede aplicar estilos a un único símbolo para cada capa o utilizar estilos diferentes basados en un [método de categorización](/content/es/Module_3/es_qgis_data_classification.md).

En la pestaña Simbología, puede seleccionar entre varios métodos de simbolización (consulte la {numref}`es_3.36_m4_symbolisation_methods`). Los más importantes son __Single Symbol__, __Categorized__, __Graduated__, y __Rule base__.

:::{figure} /fig/en_3.36_m4_symbolisation_methods.png
---
name: es_3.36_m4_symbolisation_methods
width: 500 px
---

:::

::::{tab-set}

:::{tab-item} Símbolo único
- Asigna un símbolo a cada entidad del conjunto de datos, sin importar, si los atributos son diferentes.

__Por ejemplo__, asigne un símbolo de hospital a una capa que solo contenga puntos, que muestren la ubicación de hospitales.
:::

:::{tab-item} Categorizado

- Clasifica las entidades en categorías con el uso de un atributo (`Valor`).
- Se crea una categoría para cada valor único de este atributo.
- Cada categoría puede asignarse a un símbolo diferente.
- Puede utilizarse tanto para datos nominales como ordinales.

__Por ejemplo__, asigne un símbolo diferente para cada tipo de edificio (industrial, comercial, público, residencial, etc.)

:::

:::{tab-item} Graduado

- Crea clases para los datos numéricos.
- Se puede seleccionar un gradiente de color para representar la distribución de los datos.

__Por ejemplo__, cree seis clases de tamaños de población y asigne un gradiente de color de blanco a rojo para indicar el tamaño de la población en un distrito (consulte el [Módulo 3: Clasificación de datos geoespaciales](/es/Module_3/es_qgis_data_classification.md)).

:::

:::{tab-item} Basado en reglas

- Cree reglas mediante el uso de una expresión y asigne un símbolo a las entidades, en las que se aplica la regla.
- Puede especificar con mayor precisión las entidades que desea simbolizar.
- Puede utilizar valores de distintos atributos (p. ej.:,tipo de edificio y distrito urbano).
- El constructor de expresiones le ayuda a crear reglas ya que le muestra los valores, campos, operadores, etc. disponibles.

__Por ejemplo__, seleccione un símbolo para cada centro de salud, que sea un hospital y haya excedido su capacidad.

:::

::::

A continuación, repasaremos algunos métodos de aplicación de estilos habituales en cartografía.

### Estilos de límites administrativos (polígonos)

Al crear informes de situación, utilizará, con frecuencia, límites administrativos. En el siguiente ejemplo, queremos crear un mapa general mediante el uso de los límites administrativos de Nigeria. Para visualizar los tres límites administrativos al mismo tiempo, tenemos que configurar la simbología de cada capa, de modo que las capas inferiores sean visibles y se pueda distinguir la jerarquía de los niveles administrativos.

:::{admonition} *Opcional*: ¡Es su turno!

Puede seguir la guía paso a paso con la descarga de los [límites administrativos de Nigeria](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/nga_adm_osgof_20190417.zip) en [OCHA Nigeria](https://data.humdata.org/dataset/cod-ab-nga).

:::

#### Mostrar solo los contornos de los polígonos

Ahora, queremos cambiar la simbología de una capa para que __solo sean visibles los contornos de los polígonos__. Esto es necesario para hacer visibles las capas inferiores a ésta.

Para cambiar la simbología de una sola capa:
1. Abra `Panel de Estilo` y vaya a la pestaña Symbology. Por defecto, la simbología se configurará en `Símbolo Único`. Esto significa que se aplicarán los mismos colores y contornos a todas las entidades de esa capa.
2. Haga clic en `Relleno simple`.
3. Haga clic en la flecha situada a la derecha de `Color de relleno`.
4. Marque la opción `Relleno transparente`.

:::{figure} ../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: es_30.30.2_vector_layer_styling_transparent
width: 500 px
---
:::

:::{dropdown} Video: Transparentar el color de relleno

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

:::

#### Ajuste de los estilos de varias capas superpuestas

__Paso 1: Ordenar las capas__

1. Importe los límites administrativos a su proyecto QGIS.
2. Tenemos que ordenar las capas en el panel de capas de modo que la `adm0` capa se sitúe en la parte superior, seguida de `adm1` y `adm2`. Al principio, esto puede parecer raro porque `Adm0` lo cubrirá todo.

:::{figure} ../../fig/en_30.30.2_changing_layer_style_1.png
---
name: es_30.30.2_changing_layer_style_1
height: 400px
---
Ordene las capas y vaya al panel de estilo de la capa superior
:::

3. Cambie la simbología de la capa Adm0 abriendo el panel de estilos y navegando hasta la pestaña de “Symbology”.
4. Haga clic en `Relleno simple` para abrir las opciones de estilo.
5. Despliegue el menú `Color de relleno` y marque la opción `Relleno transparente`. Esto hará visibles solo los límites, por lo que __podremos ver la capa debajo de esta__.
6. Elija un `Color der marca` y haga el `Anchura de marca` de 0,66 milímetros.
7. Haga clic en `Aplicar`.
8. __Repita el mismo proceso__ para la capa Adm1, utilizando el mismo color que para Adm0 (estará en "colores recientes") y deje el ancho del trazo en 0,26.
9. Ahora podemos ver los límites del país y sus estados y detrás de ellos los distritos (Adm2).
10. Hagamos que el estilo de la capa de distritos sea consistente con los demás.
11. Elija un `Color de relleno`.
12. Utilice el mismo `Color de marca` que para Adm0 y Adm1, pero haga que el ancho sea de 0,1 milímetros y el estilo de marca __Dash Line__.
13. Haga clic en "Aplicar" y mire su mapa: ¡Esperamos que empiece a verse más bonito!

:::{figure} ../../fig/en_30.30.2_changing_layer_style_3.png
---
width: 500 px
name: en_30.30.2_changing_layer_style_3
---
El estilo de datos vectoriales consiste en el color y el contorno.
:::

:::{dropdown} Video: Ajuste del estilo para múltiples capas
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_change_style_for_multiple_layers
.mp4"></video>
:::


#### Creación de un mapa coroplético (“Gradudated Styling”)


Si una capa contiene valores numéricos, que son continuos, pueden organizarse en intervalos. Estos intervalos pueden visualizarse con colores graduados. En este ejercicio, asignamos colores a los polígonos de Adm1 en función de la población total de cada estado.


1. Descargue el [shapefile NGA_Adm1_Pop](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/NGA_adm1_pop.zip) y guárdelo en su carpeta shapefile.
2. En QGIS, desactive las capas Adm1 y Adm2, y solo deje la Adm0.
3. Arrastre el shapefile NGA_Adm1_Pop a su mapa.
4. Abra sus opciones de `Simbología` y elija `Graduado`.
5. __Seleccione el valor, que desea utilizar para asignar colores__, en este caso, será `total_pop`.

:::{figure} ../../fig/en_30.30.2_symbology_variable_ranges.png
---
name: es_30.30.2_symbology_variable_ranges
width: 550px
---
Con rangos variables, seleccione simbología __graduada__ y elija el atributo con valores continuos
:::

6. Haga clic en `Clasificar` para __enumerar todos los valores divididos en clases__.
7. Elija __en cuántas clases__ desea dividir los datos: digamos 4.
8. Por defecto, la rampa de color será roja. Sin embargo, el rojo no es el color adecuado para el recuento de la población, ya que suele utilizarse para comunicar elementos negativos, como la inseguridad alimentaria o los casos de cólera.
9. Haga clic en __la flecha situada junto a la rampa de color__ para elegir otra combinación de colores: digamos una rampa de color del blanco al azul.
10. Haga clic en `Aplicar` para obtener una vista previa del aspecto de su capa, luego haga clic en `Aceptar`.

:::{figure} ../../fig/en_30.30.2_symbology_variable_ranges_2.png
---
name: es_30.30.2_symbology_variable_ranges_2
width: 500px
---
Puede clasificar los valores continuos en clases y asignarles una rampa de color.
:::

El siguiente mapa muestra los estados más poblados de Nigeria mediante una categorización graduada por colores. Este tipo de mapas se denominan __mapas coropléticos__.

:::{figure} ../../fig/en_map_design_example_variable_ranges.png
---
name: es_map_design_example_variable_ranges
width: 500px
---
Mapa que muestra la población de los estados nigerianos.
:::

:::{dropdown} Video: Cómo crear un mapa coroplético
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_graduated_styling
.mp4"></video>
:::

#### Crear un mapa con símbolos graduados

Los símbolos graduados son útiles cuando se tiene más información en el mapa y no es posible, crear un mapa coroplético,
o en situaciones, en las que desee comunicar dos variables, en un mismo mapa. Por ejemplo, es fácil combinar
mapas coropléticos con símbolos graduados.
La creación de mapas con símbolos graduados se realiza de forma similar a la creación de mapas coropléticos, pero implica un paso adicional:
Crear centroides de los límites administrativos. Los centroides son puntos, que se sitúan en el centro calculado de
polígonos (consulte el [módulo 5](/content/es/Module_5/es_qgis_non_spatial_tools.md)). 
Utilizaremos la misma capa que para el mapa coroplético (consulte la {numref}`es_map_design_example_variable_ranges`):
`NGA_Adm1_Pop`.

1. En la [caja de herramientas de procesos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_1/es_qgis_start.html?highlight=processing+toolbox#toolbox-toolbars), busque la herramienta `centroides`. <kbd>Haga doble clic</kbd> en ella. Se abrirá una nueva ventana (consulte la {numref}`es_3.36_m4_centroids`)

:::{figure} /fig/en_3.36_m4_centroids.png
---
name: es_3.36_m4_centroids
width: 500 px
---
Creación de centroides en QGIS 3.36.
:::

2. En `Capa de entrada`, seleccione la capa `NGA_Adm1_Pop`. Haga clic en `Ejecutar`.
3. Aparecerá una nueva capa de puntos denominada `Centroides` en su panel de capas. Abra su panel de Layer Styling y navegue hasta la pestaña Symbology.
4. Configure el método de simbolización a `Graduado`.
5. En __Valor__, seleccione `total_pop`.
6. Cambie __Método__ de `Color` a `Tamaño`.
7. Haga clic en `Clasificar`.
8. *Opcional*: Cambiar el color y la transparencia de los círculos.

:::{figure} /fig/en_m4_graduated_symbols_example.png
---
name: es_m4_graduated_symbols_example
width: 550 px
---
Mapa de Nigeria que muestra los mismos datos. Una vez con el uso de colores graduados (coropléticos) y símbolos graduados (círculos proporcionales).
:::

:::{dropdown} Video: Cómo crear un mapa de círculos proporcionales

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_3.36_graduated_symbols.mp4"></video>

:::


### Utilizar diferentes estilos en una sola capa

Al categorizar o clasificar los datos en una sola capa, podemos asignar diferentes estilos a cada clasificación.
Podemos utilizar la simbología para __mostrar la diferencia entre las entidades__ en la misma capa. Por ejemplo, podría tratarse de distintos tipos de edificios, cantidades de casos de Covid por distrito o tipos de carreteras. Podemos elegir un atributo específico de un conjunto de datos para asignar diferentes colores, contornos o tamaños a las entidades:

#### Configuración de los diferentes símbolos de puntos para distintas entidades

1. Descargue el [GeoPackage de incidentes de seguridad de ACLED](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/follow_along/NGA_ACLED_security_incidents.zip) y cárguelo en su proyecto de QGIS. Se trata de una capa de puntos en la que cada punto, indica un incidente de seguridad distinto.
2. Abra la pestaña `Simbología` para esa capa y elija `Categorizado` en lugar de `Símbolo Único`.

:::{note}
La simbología categorizada se utiliza cuando se dispone de variables ***distintas***.
:::

:::{figure} ../../fig/en_30.30.2_categorized_layer_symbology_1.png
---
name: en_30.30.2_categorized_layer_symbology_1
width: 500px
---
Cambie el tipo de simbología a `Categorized` y elija el valor (variable) que desea visualizar.
:::

3. Ahora tenemos que __elegir qué atributos queremos mostrar a través de la simbología__. En este caso, podría ser el número de víctimas o el actor que perpetró el acto. Categoricemos las entidades por `event_type`.
4. Haga clic en `Clasificar` para __enumerar todos los valores únicos contenidos__ en el campo `event_type` (es decir, todos los posibles tipos de incidentes de seguridad registrados en nuestra tabla).
5. Ahora podemos __cambiar el estilo de cada valor individual__.
6. Haga doble clic en el valor `Explosions`.
7. En la parte inferior de la ventana del __selector de símbolos__, elija un símbolo para resaltar los puntos de explosión.
8. Haga clic en `Aceptar`, luego en `Aplicar` para obtener una vista previa del aspecto que tendrá la capa.
9. Haga clic en `Aceptar` de nuevo.

:::{figure} ../../fig/en_30.30.2_categorized_layer_symbology_2.png
---
name: es_30.30.2_categorized_layer_symbology_2
width: 500px
---
Al hacer doble clic en los __valores únicos__ de la lista clasificada, puede cambiar el símbolo de cada valor.
:::

Ahora, tenemos un mapa de Nigeria, en el que puede localizar las zonas, que fueron afectadas, más que otras, por las explosiones. En el mapa que figura , a continuación, también hemos añadido etiquetas de texto, que se explicarán más adelante.

:::{figure} ../../fig/en_exercise_map_design_example_Nigeria.png
---
name: en_exercise_map_design_example_Nigeria
width: 500px
---
Regiones afectadas por las explosiones en Nigeria.
:::

:::{dropdown} Video: Configurar diferentes símbolos en una sola capa

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_styling
.mp4"></video>

:::



:::{card}
:class-card: sd-text-justify sd-text-black sd-border-0
__Marcadores simples, símbolos SVG e imágenes ráster__
^^^
Además de los marcadores simples, QGIS también le permite utilizar símbolos SVG e imágenes ráster, como símbolos para los datos vectoriales.

- __Los marcadores simples__ son formas simples como rectángulos, círculos o cruces, que pueden ajustarse en la capa de simbolización (color, tamaño, contorno, etc.). La mayor parte de su estilo en QGIS se hará con estos marcadores.
- __Los símbolos SVG__ son *símbolos gráficos vectoriales escalables*. Como archivos vectoriales, pueden expandirse a cualquier tamaño, mientras, que mantiene la misma resolución. En la mayoría de los casos, si desea utilizar un símbolo más complejo (p. ej.: hospital, escuela, estación de tren), los símbolos SVG son la mejor opción, ya que le permiten ajustar el símbolo (colores, contorno, tamaño, etc.).
- Si selecciona las __imágenes ráster__, la resolución del símbolo estará limitada por la cantidad de píxeles de la imagen. No es aconsejable utilizar imágenes de alta resolución como símbolos en su mapa porque esto podría sobrecargar su computadora.

:::

#### __Uso de símbolos SVG y IFRC__

### Uso de símbolos SVG

En algunos casos, es posible que desee utilizar símbolos más complejos en su mapa. Por ejemplo, una cruz para un hospital, un libro para una biblioteca o un avión para un aeropuerto. En estos casos, puede utilizar los símbolos SVG. Tenga en cuenta que, normalmente, los símbolos SVG solo funcionan para datos de punto.
Para utilizar los símbolos SVG:

1. Abra el panel de estilo y las opciones de `single marker`.
2. En `Tipo de capa del símbolo`, seleccione __“Marcador SVG”__.
3. Desplácese hacia abajo hasta el navegador SVG. Aquí encontrará todas las carpetas de sus bibliotecas instaladas SVG.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

Ya existe, por defecto, una biblioteca de símbolos SVG. Si busca un símbolo concreto, inténtelo en la barra de búsqueda.

#### Añadir una biblioteca externa SVG

QGIS también le ofrece la opción de añadir sus propias bibliotecas SVG, por ejemplo, si su organización utiliza un conjunto específico de iconos.
Si tiene una biblioteca de símbolos SVG en una carpeta, puede añadirlos a su administrador de estilos.

1. Abra el administrador de estilos: `Configuración` → `Administrador de estilos...`.
2. Haga clic en `Importar / Exportar` y seleccione `Importar elemento(s)`.
3. Navegue hasta la ubicación donde haya guardado la biblioteca o el estilo y seleccione el archivo (en la mayoría de los casos `.qml`, pero el tipo de archivo también puede ser `.xml`).
4. Ahora puede seleccionar los símbolos, que desea importar. En la mayoría de los casos, puede seleccionar todos los símbolos.
5. Haga clic en `Importar`.

Los nuevos símbolos SVG están en su biblioteca SVG.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

#### Uso de símbolos de IFRC

:::{admonition} Repositorios de símbolos de IFRC y de la ONU
:class: tip

La Federación Internacional de Sociedades de la Cruz Roja y de la Media Luna Roja (IFRC) proporciona iconos y símbolos, que pueden utilizarse en sus mapas. Puede encontrarlos en [este enlace](https://go-user-library.ifrc.org/brand-design/iconography).

También existe una biblioteca con iconos humanitarios de la [Oficina de la ONU para la Coordinación de Asuntos Humanitarios (OCHA)](https://www.unocha.org) que puede consultarse [aquí](https://github.com/mapaction/ocha-humanitarian-icons-for-gis?tab=readme-ov-file). Los archivos están disponibles en diferentes formatos, que Ud. puede utilizar en QGIS.

:::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __Nombre y describa los cuatro métodos principales de simbolización utilizados para las capas vectoriales.__

:::{dropdown} Respuesta
1. __Símbolo único__
    - Todas las entidades utilizan el mismo símbolo (mismo color, tamaño, trazo) independientemente de sus atributos.
2. __Categorizados (Valores únicos/Categorizados)__
    - Las entidades se estilizan por categorías distintas (valores de atributo). Cada valor único (o clase) recibe su propio símbolo (tono, forma, etc.).
3. __Símbolos graduados__
    - Los atributos numéricos (continuos) se dividen en clases (rangos de valores) y cada clase recibe un símbolo (a menudo, con una rampa de colores). Se utiliza para mostrar la variación en los datos cuantitativos.
4. __Basado en reglas__
    - Los usuarios definen una o varias reglas mediante el generador de expresiones, que determina el símbolo que recibe cada entidad. Las reglas pueden combinar atributos y lógica espacial, lo que permite un estilo condicional complejo.

:::

2. __¿Dónde se guarda la simbología de una capa?__

:::{dropdown} Respuesta
- La simbología de una capa no se guarda en el conjunto de datos. Si solo comparte el conjunto de datos con un colega, la capa no aparecerá como en su computadora.
- La simbología se almacena en el __archivo de proyecto QGIS__ (`.qgz` o `.qgs`).
- También es posible __exportar__ o __guardar__ el estilo externamente (como un archivo `.qml` ) para poder reutilizarlo o compartirlo.
:::
3. __Al estilizar las capas de polígonos (p. ej.: los límites administrativos), ¿Para qué sirve utilizar relleno transparente y contornos visibles?__

:::{dropdown} Respuesta
- __Contexto:__ El relleno transparente permite que las capas subyacentes (p. ej.: mapa base, imágenes, etiquetas) se muestren a través del contexto espacial.
- __Importancia de los límites:__ Los contornos visibles (trazos) indican claramente los bordes del polígono, aunque el relleno sea sutil.
- __Jerarquía y legibilidad:__ Si se muestran muchos polígonos superpuestos o regiones adyacentes, los rellenos transparentes evitan que las áreas se bloqueen entre sí, mientras que los contornos mantienen los límites diferenciados.
:::


4. __Explique cómo se crea un mapa coroplético en QGIS con el uso de colores graduados. ¿Qué debe elegir (p. ej.: atributo, número de clases, rampa de color)?__

:::{dropdown} Respuesta
1. Hacer clic con el <kbd>botón derecho</kbd> en la capa, seleccionar `Propriedades` y vaya hasta la pestaña `Simbología`.
2. Cambiar el método de simbolización de `Símbolo Único` a `Graduado`.
3. Junto a `Valor`, elegir el atributo numérico, que se desee visualizar en el mapa coroplético (p. ej.: densidad de población, porcentaje, precipitación, casos de enfermedad normalizados, etc.). El valor de este atributo determinará el color.
4. Elegir un método de clasificación y configurar el número de clases (p. ej.: intervalo equitativo, cuantil, cortes naturales, etc.).
5. Elegir una rampa de color adecuada para la información, que se quiere visualizar (claro → oscuro).
6. Haga clic en `Clasificar` y `Aplicar`.
7. Observar el lienzo del mapa y realizar los ajustes necesarios (p. ej.: eliminar los contornos de los polígonos).
:::

5. __¿Qué son los símbolos SVG y qué ventajas ofrecen sobre las imágenes ráster para la simbología de puntos?__

:::{dropdown} Respuesta
- Los símbolos __SVG (Gráficos Vectoriales Escalables)__ son iconos o gráficos basados en vectores, que pueden utilizarse para simbolizar puntos en QGIS.
- __Ventajas:__
    - __Escalabilidad sin pérdidas:__ Los Gráficos Vectoriales Escalables (SVG) se escalan suavemente (acercar o alejar zoom) sin pixelado ni borrosidad, mientras que las imágenes ráster, se degradan al cambiar de tamaño.
    - __Editable/estilizable:__ Se puede cambiar el color, el trazo, el relleno y el tamaño de forma dinámica, ya que el símbolo está basado en vectores.
    - __Nitidez en la impresión:__ Mantienen los bordes nítidos a cualquier resolución, por lo que son mejores para la producción cartográfica.
    :::


::::

## Recursos adicionales

- [Cartography Guide](https://www.axismaps.com/guide) de [Axis Maps](axismaps.com)
- Tutorial sobre [cómo importar la paleta de colores SIMS a QGIS](https://learn-sims.org/geospatial/importing-sims-color-palette-to-qgis/)
- Tutorial sobre [cómo crear un mapa de relieve sombreado en QGIS](https://learn-sims.org/geospatial/creating-a-shaded-relief-map-in-qgis/)
- [Creating a 3W (Who, What, Where) Infographic](https://learn-sims.org/information-design/creating-a-3w-who-what-where-infographic/)
- [Paleta oficial de colores de la IFRC](https://learn-sims.org/style-guidance/color-palettes/)