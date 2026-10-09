# Visualización


__🔙[Volver a la página de inicio](../es_intro.md)__

## Visualización de datos vectoriales

### Simbología

QGIS ofrece varias formas de visualizar datos vectoriales. En la pestaña Symbology, puede seleccionar entre varios métodos de simbolización

::::{tab-set}

:::{tab-item} Símbolo único
- Asigna un símbolo a cada entidad del conjunto de datos, sin importar si los atributos son diferentes.

__Por ejemplo__, asigne un símbolo de hospital a una capa que solo contenga puntos que muestren la ubicación de hospitales.
:::

:::{tab-item} Categorizado

- Clasifica las entidades en categorías utilizando un atributo (`Valor`).
- Se crea una categoría para cada valor único de este atributo.
- Se puede signar a un símbolo diferente a cada categoría.
- Puede utilizarse tanto para datos nominales como ordinales.

__Por ejemplo__, asigne un símbolo diferente para cada tipo de edificio (industrial, comercial, público, residencial,...)

:::

:::{tab-item} Graduado

- Crea clases para datos numéricos.
- Se puede seleccionar un gradiente de color para representar la distribución de los datos

__Por ejemplo__, cree seis clases de tamaños de población y asigne un gradiente de color de blanco a rojo para indicar el tamaño de la población en un distrito.

:::

:::{tab-item} Basado en reglas

- Cree reglas utilizando una expresión y asigne un símbolo a las entidades en las que se aplica la regla.
- Puede especificar con mayor precisión las entidades que desea simbolizar.
- Puede utilizar valores de distintos atributos (por ejemplo, tipo de edificio y distrito urbano).
- El constructor de expresiones le ayuda a crear reglas mostrando los valores, campos, operadores, etc. disponibles.

__Por ejemplo__, seleccione un símbolo para cada centro de salud que sea un hospital y que haya superado su capacidad.

:::

::::

::::{dropdown} Mostrar sólo los contornos de los polígonos

En este ejemplo, queremos cambiar la simbología de una sola capa para que __solo sean visibles los contornos de los polígonos__.

Para cambiar la simbología de una sola capa:
1. Abra la página `Estilo de capas` y vaya a la pestaña symbology. Por defecto, la simbología se establecerá en `Símbolo único`. Esto significa que se aplicarán los mismos colores y contornos a todos las entidades de esa capa.
2. Haga clic en `Relleno simple`.
3. Haga clic en la flecha situada a la derecha de `Color de relleno`.
4. Marque la opción `Relleno transparente`.

:::{figure} ../../../fig/en_30.30.2_vector_layer_styling_transparent.png
---
name: es_30.30.2_vector_layer_styling_transparent_wiki
width: 500 px
---
:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_make_only_outlines_visible.mp4"></video>

::::

::::{dropdown} Cambiar el estilo de varias capas superpuestas

En este ejercicio, aplicaremos el mismo estilo a todas las entidades de una capa, pero cambiaremos varias capas y las superpondremos para que cada una sea visible con un estilo diferente. Tenemos los polígonos para tres niveles administrativos.

:::{figure} ../../../fig/en_30.30.2_changing_layer_style_1.png
---
name: es_30.30.2_changing_layer_style_1_wiki
height: 400 px
---
Ordene las capas y vaya al panel de estilo de la capa superior.
:::

1. Añada los `Adm0`, `Adm1` y `Adm2` shapefiles a su proyecto de la Sesión 2.
2. Ordene las capas para que todas sean visibles: Ponga la capa `Adm2` en la parte inferior, luego la `Adm1` y después `Adm0`. Al principio, esto puede parecer raro porque `Adm0` lo cubrirá todo.
3. Cambie la simbología de la capa Adm0 abriendo el panel de estilos y yendo hasta la pestaña Symbology.


:::{figure} ../../../fig/en_30.30.2_changing_layer_style_2.png
---
name: es_30.30.2_changing_layer_style_2_wiki
width: 350 px
align: left
---
Cambiar el tipo de relleno.
:::

4. Haga clic en `Relleno simple` para abrir las opciones de estilo.
5. Despliegue el menú `Color de relleno` y marque la opción `Relleno transparente`. Esto hará visibles solo los límites, por lo que __podremos ver la capa bajo ésta__.
6. Elija un `Color de marca`, y haga que el `Anchura de marca` sea de 0,66 milímetros.
7. Haga clic en `Aceptar`.
8. __Repita el mismo proceso__ para la capa Adm1, utilizando el mismo color que para Adm0 (estará en "Colores recientes") y deje el ancho del trazo en 0,26.
9. Ahora podemos ver los límites del país y sus estados, y detrás los distritos (Adm2).
10. Hagamos que el estilo de la capa del distrito sea coherente con los demás.

<br/><br/>

11. Elija una `Color de Relleno`
12. Utilice el mismo color de trazo` que para Adm0 y Adm1, pero haga que el ancho sea de 0,1 milímetros y el estilo de trazo __Línea de guiones__
13. Haga clic en `Aceptar` y mire el mapa: ¡Parecería tener un mejor aspecto!

:::{figure} ../../../fig/en_30.30.2_changing_layer_style_3.png
---
name: es_30.30.2_changing_layer_style_3_wiki
---
El estilo de un dato vectorial consiste en el color y el contorno.
:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_change_style_for_multiple_layers
.mp4"></video>


::::

::::{dropdown} Utilizar diferentes estilos en una misma capa

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_styling
.mp4"></video>

Podemos utilizar la simbología para __mostrar la diferencia entre las entidades__ en la misma capa. Por ejemplo, podría tratarse de distintos tipos de edificios, cantidades de casos Covid por distrito o tipos de carreteras. Podemos elegir un atributo específico de un conjunto de datos para asignar diferentes colores, contornos o tamaños a las entidades:

1. Desde su carpeta shapefile, __arrastre el shapefile de incidentes de seguridad ACLED a su mapa__
2. Abra el panel `Simbología` para esa capa y elija `Categorizado` en lugar de Single Symbol. 
:::{note}
La simbología categorizada se utiliza cuando se dispone de ***variables*** discretas.
:::

:::{figure} ../../../fig/en_30.30.2_categorized_layer_symbology_1.png
---
name: es_30.30.2_categorized_layer_symbology_1_wiki
width: 500 px
---
Cambie el tipo de simbología a “categorizada” y elija el valor (variable) que desea visualizar.
:::
3. Ahora tenemos que __elegir qué atributos queremos mostrar a través de la simbología__. En este caso, podría ser el número de víctimas o el actor que perpetró el acto. Clasifiquemos las entidades por `event_type`.
4. Haga clic en `Clasificar` para __listar todos los valores únicos contenidos__ en el campo `event_type` (es decir, todos los posibles tipos de incidentes de seguridad registrados en nuestra tabla).
5. Ahora podemos __cambiar el estilo de cada valor individual__.
6. Haga doble clic en el valor `Explosions`.
7. En la parte inferior de la ventana __Symbol selector__, elija un símbolo para resaltar los puntos de explosión.
8. Haga clic en `Aceptar`, luego en `Aplicar` para previsualizar el aspecto que tendrá la capa.
9. Haga clic en `Aceptar` de nuevo.

:::{figure} ../../../fig/en_30.30.2_categorized_layer_symbology_2.png
---
name: es_30.30.2_categorized_layer_symbology_2_wiki
width: 500 px
---
Haciendo doble clic en los __unique values__ de la lista clasificada, puede cambiar el símbolo de cada valor.
:::

Ahora tenemos un mapa de Nigeria en el que se pueden localizar las zonas más afectadas por las explosiones. En el mapa de abajo, también hemos añadido etiquetas de texto, que se explicarán más adelante.

:::{figure} ../../../fig/en_exercise_map_design_example_Nigeria.png
---
name: es_exercise_map_design_example_Nigeria_wiki
width: 500px
---
Regiones afectadas por las explosiones en Nigeria.
:::
::::

::::{dropdown} Datos de estilo basados en rangos variables (estilo "__Graduado__")

Si una capa contiene valores numéricos que son continuos, pueden organizarse en intervalos. Estos intervalos pueden visualizarse en colores graduados. En este ejercicio, asignamos colores a los polígonos de Adm1 en función de la población total de cada Estado.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_graduated_styling
.mp4"></video>

% IMPORTANT ADD LINK TO DOWNLOAD THE FILE!!

1. Descargue el archivo shapefile NGA_Adm1_Pop y guárdelo en su carpeta shapefile.
2. En QGIS, desactive las capas Adm1 y Adm2, dejando solo Adm0.
3. Arrastre el shapefile NGA_Adm1_Pop a su mapa.
4. Abra sus opciones de `Simbología` y elija `Graduado`.
5. __Seleccione el valor que desea utilizar para asignar colores__, en este caso, será `Population`.

:::{figure} ../../../fig/en_30.30.2_symbology_variable_ranges.png
---
name: es_30.30.2_symbology_variable_ranges_wiki
width: 550px
---
Con rangos variables, seleccione __Graduated__ symbology elija el atributo con valores continuos.
:::

6. Haga clic en `Clasificar` para __listar todos los valores divididos en clases__.
7. Elija __en cuántas clases__ desea dividir los datos - digamos 4.
8. Por defecto, la rampa de color será roja. Sin embargo, el rojo no es el color adecuado para el recuento de población, ya que suele utilizarse para comunicar elementos negativos, como la inseguridad alimentaria o los casos de cólera.
9. Haga clic en __la flecha junto a la rampa de color__ para elegir otra combinación de colores - digamos una rampa de color de blanco a azul.
10. Haga clic en `Aplicar` para previsualizar el aspecto de su capa y, a continuación `Aceptar`.

:::{figure} ../../../fig/en_30.30.2_symbology_variable_ranges_2.png
---
name: es_30.30.2_symbology_variable_ranges_2_wiki
width: 500 px
---
Puede clasificar los valores continuos en clases y asignarles una rampa de color.
:::

El siguiente mapa muestra los estados más poblados de Nigeria mediante una categorización graduada por colores. Este tipo de mapas se denominan __mapas coropléticos__.

:::{figure} ../../../fig/en_map_design_example_variable_ranges.png
---
name: es_map_design_example_variable_ranges_wiki
width: 500px
---
Mapa de la población de los estados nigerianos.
:::
::::


----

### Etiquetas

Las etiquetas son textos que muestran información o valores de los datos. En QGIS, puede seleccionar __Etiquetas individuales__ o __Etiquetado basado en reglas__. Para cada opción, se mostrará un atributo (`valor`) en el mapa. Además, puede __cambiar la fuente, el tamaño, el color y otras opciones de estilo__.

::::{tab-set}

:::{tab-item} Etiquetas simples

- Crea un único estilo de etiqueta para cada entidad de la capa. Puede seleccionar un atributo (valor) que se mostrará. Por ejemplo, el nombre de un asentamiento. Necesita saber qué atributo muestra la información que desea. Consulte la tabla de atributos del conjunto de datos para averiguarlo.

:::

:::{tab-item} Etiquetado basado en reglas

- Cree reglas mediante expresiones para seleccionar con precisión las entidades que deben etiquetarse.
- Cada regla puede tener un formato de texto diferente

:::

::::

:::{note} Etiquetado

A veces las etiquetas pueden ocultar otros símbolos. En ese caso, puede ajustar la ubicación de las etiquetas en la pestaña __etuiqueta__ o utilizar la herramienta `Mover una etiqueta, diagrama o leyenda` de la barra de herramientas __etiqueta__

Por defecto, QGIS genera las etiquetas de manera que no se superpongan con otras etiquetas. Esto significa que no todas las etiquetas serán visibles si los datos son densos o se muestran muy cerca unos de otros. Puede optimizar la renderización en la opción de renderizado.

:::

::::{dropdown} Añadir etiquetas a una capa

1. En el panel de estilo, haga clic en la pestaña `Etiquetas` situada debajo de la pestaña Symbology.
2. Seleccione `Etiquetas sencillas`.
3. `Valor` es donde se elige el atributo que se mostrará como etiqueta. Por ejemplo, `*ADM1_EN*` mostrará los nombres en inglés de los estados nigerianos para cada entidad del conjunto de datos.
4. __Cambiemos la fuente__: Abra el menú desplegable de fuentes y seleccione Arial. Cree el texto `Bold` en el menú desplegable Style. Cambie el color haciendo clic en `Color` y cambie el `Tamaño` a 8 pts.
5. __Añadamos un buffer blanco__ alrededor de la etiqueta. En la pestaña `Etiquetas`, encontrará una lista con diferentes opciones para diseñar las etiquetas. Ahora, estamos en el menú `Texto (cadena)`. Seleccione `Buffer` y marque `Dibujar buffer de texto` la opción. Esto hará que las etiquetas se destaquen más en mapas oscuros o con mucha información.
7. Haga clic en `Aplicar` y `Aceptar`.

:::{figure} ../../../fig/en_30.30.2_setting_up_labels.png
---
width: 500 px
name: es_30.30.2_setting_up_labels_wiki
---
Configurar etiquetas en QGIS 30.30.2.
:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_labels
.mp4"></video>

::::

::::{dropdown} Añadir diferentes estilos de etiqueta a la misma capa

A veces necesitará crear dos estilos de etiqueta diferentes para distintas entidades de una misma capa. En este ejemplo, crearemos un estilo de etiqueta para la *Capital de país*, y otro para las *Capitales de Estado*

1. Abra el panel de estilo de la capa `"NGA_settlements_nga"` y haga clic en la pestaña `Etiquetas`.
2. Seleccione `Etiquetas basado en reglas`.
3. Haga clic en el botón __Añadir regla__ de la parte inferior (el signo "+") y __cree la primera regla__
4. Para __Value__, seleccione `"NAME"` (para que las etiquetas muestren el nombre de cada ciudad) y, a continuación, haga clic en `"ε"-button` junto a la barra __Filtro__.

:::{figure} ../../../fig/en_30.30.2_adding_rule-based_labels.png
---
width: 500 px
name: es_30.30.2_adding_rule-based_labels_wiki
---
Para añadir etiquetas basadas en reglas, debe introducir una expresión.
:::

5. En la columna central, expanda `Campos y Valores` para mostrar una lista de todos los campos de su capa y haga doble clic en `"CLASS"` para __añadirlo al marco de expresión__ de la izquierda.
6. En la columna de la derecha, haga clic en `All unique` para listar todos los valores únicos contenidos en el campo Clase. En este conjunto de datos, `"CLASS"=1` designa la capital, mientras que `"CLASS"=2` designa otras ciudades importantes. Familiarícese con el conjunto de datos que tiene a su disposición para saber qué representan los distintos atributos.
7. Haga clic en el operador `"="` y, a continuación, haga doble clic en `value 1` (que en este caso representa la capital del país). Haga clic en `Aceptar`.
8. Desplácese hacia abajo para __cambiar el estilo de la etiqueta__. Elija Arial, negrita, color negro, 12pt y añada un buffer blanco.
9. __Repita los pasos 4 a 9__, pero seleccione `Value 2` (Capitales del Estado) y elija una etiqueta negra, negrita, 10pt, sin buffer.
10. Haga clic en `Aplicar`, el `Aceptar`.

:::{figure} ../../../fig/en_30.30.2_adding_rule-based_labels_expression_builder.png
---
width: 500 px
name: es_30.30.2_adding_rule-based_labels_expression_builder_wiki
---
El constructor de expresiones: Expresión (izquierda); módulos, operadores, campos y valores (centro); valores únicos (derecha).
:::
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_rule_based_labelling
.mp4"></video>

::::

:::{dropdown} Añadir etiquetas subrayadas

1. Configure las etiquetas siguiendo los mismos pasos que antes.
2. Para subrayar las etiquetas, haga clic en el botón de subrayado

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_underlign_labels
.mp4"></video>

::::

::::{dropdown} Mover las etiquetas de forma independiente
A veces, la colocación de las etiquetas no es la ideal y puede obstaculizar la legibilidad del mapa. En este caso, puede mover las etiquetas de forma independiente.

1. En la barra de herramientas `Etiqueta`, hay una opción para __mover las etiquetas de forma independiente__. Haga clic en él para activar la herramienta. (Nota: En algunos casos, es posible que la barra de herramientas de etiquetas no esté visible. En este caso, actívela accediendo a `Ver` → `Barras de herramientas` → activate the Label toolbar).
2. Haga clic en la etiqueta __que desee mover__.
3. Se le pedirá que seleccione la clave primaria para la unión con el almacenamiento interno de datos. __No es necesario cambiarlo__ (puede seleccionar el campo ID del conjunto de datos) y hacer clic en `Aceptar`.
4. Vuelve a hacer clic en la etiqueta, ahora podrás moverla libremente.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_move_labels_independently
.mp4"></video>

::::

::::{dropdown} Añadir etiquetas a las carreteras
Al trabajar con entidades lineales, las etiquetas se alinearán paralelas a la línea que representa el elemento.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_add_road_labels
.mp4"></video>

::::


---

## Visualización de datos ráster

### Asignación de un gradiente de color a datos ráster

Para asignar un gradiente de color a los datos ráster, es necesario:

1. Abra el panel `Estilo de capas` para la capa ráster.
2. Navegue hasta la pesteña `Simbología`.
3. Por defecto, el esquema de color se establece en gris banda única (si solo tiene una banda de color en el conjunto de datos). Haga clic en `Gris monobanda` y cambie a `Pseudocolor monobanda`.
4. Haga clic en __la flecha situada a la derecha de la rampa de color__. Aquí puedes elegir una rampa de color preestablecida
5. Puede modificar la rampa de color presionando __en la rampa de color__.

:::{figure} ../../../fig/en_30.30.2_raster_data_colour_gradient.png
---
name: es_raster data colour gradient
width: 600px
---
Selector de rampa de color.
:::

En el selector de rampa de color, se puede ajustar cada paso de color. En la parte inferior, puede ver un gráfico para el Tono, __Saturación__, __Luminosidad__ y __Opacidad__. Los tres últimos son especialmente útiles para ver cómo se traducirá la rampa de color. Los degradados de claro a oscuro son más fáciles de leer: Compruebe si el gráfico de la __luminosidad__ tiene un trazado más o menos lineal.

::::{dropdown} Estilizar un modelo digital de elevación

Los conjuntos de datos de elevación se utilizan con frecuencia para comunicar el terreno en un mapa. Por defecto, un modelo de elevación se mostrará con una rampa de color gris. Sin embargo, si no necesita conocer la elevación en determinados puntos, puede optar por mostrar la __sombra de la colina__ del terreno. El sombreado simulará la sombra del terreno como si estuviera expuesto a una fuente de luz. En este ejemplo, utilizaremos los datos ráster de elevación (.tiff) de Argelia de la plataforma Humanitarian Data Exchange (humdata.org) Para conseguirlo,

 1. Abra la pestaña `Simbología`.
 2. Haga clic en `Gris monobanda` y seleccione `Mapa de sombras (Hillshade)`. Tendrá la opción de seleccionar la dirección de la luz. Por convención, la fuente de luz se sitúa en el Noroeste, por lo que podemos mantener la configuración por defecto. En algunos casos con terreno accidentado, puede ser útil hacer la sombra de la colina __Multidireccional__.
 3. La sombra de la colina será muy oscura y cubrirá la mayor parte del mapa. Tenemos que hacerla más clara...

<!--ADD: Video-->

::::

### Invertir la rampa de colores

En algunos casos, la rampa de colores debe invertirse para facilitar la lectura del mapa:
1. Haga clic en la flecha __situada junto a la rampa de color__ para abrir el menú desplegable.
2. Haga clic en `Invertir rampa de color`.

## Exportación e importación de estilos

:::::{tab-set}
::::{tab-item} Guardar o exportar los ajustes de estilo

1. Haga <kbd>clic derecho</kbd> en la capa con el estilo → `Propriedades` → `Simbología`y haga clic en `Estilos` en la esquina inferior izquierda. Se abrirá un menú desplegable con la opción de exportar el estilo de la capa.
2. Como en este caso, el estilo es exactamente para ese conjunto de datos, puede dejar todas las casillas marcadas.
3. Selecciona una ubicación y un nombre para el estilismo. El estilo se guardará en un archivo `.qml`. __Asegúrese de que se guarde en la misma carpeta que el conjunto de datos y asígnele el mismo nombre que al conjunto de datos correspondiente. De este modo, al cargar los datos en QGIS, el estilo se aplicará automáticamente.__

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_exporting_style_to_send_to_colleague
.mp4"></video>
::::

::::{tab-item} Carga de un estilo en el proyecto de QGIS

1. Abra el gestor de estilos: `Configuración` → `Administrador de estilos`.
2. Haga clic en `Importar / Exportar` y seleccione `Importar elementos`.
3. Navegue hasta la carpeta donde está guardado el estilo y haga clic en importar.
4. El estilo debería estar ahora disponible como preajuste en el panel de estilos.

:::{note}
También puede importar estilos directamente en el panel de estilos de una capa. Pero no se añadirá a su biblioteca de estilos a menos que lo guarde en ella.
:::
::::

::::{tab-item} Uso de los símbolos de la IFRC

Con el complemento __"Plugin Resource Sharing"__, puede instalar las bibliotecas de símbolos e iconos utilizadas por la Cruz Roja y la ONU, así como otros símbolos útiles.

1. Instale el __"Plugin Resource Sharing"__ abriendo la ventana de instalación del complemento y buscándolo.
2. Una vez instalado, abra la interfaz del complemento haciendo clic en `Complementos` → `Plugin Resource Sharing`
3. Búsqueda de paquetes por la Cruz Roja y la ONU
4. Instale los paquetes.

Ahora los símbolos deberían estar disponibles en el gestor de estilos en la carpeta SVG.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_resource_sharing_plugin.mp4"></video>


:::{tip}
No deje de consultar los demás recursos disponibles en el complemento para compartir recursos y compruebe si le resultan útiles.
:::
::::

::::{tab-item} Uso de símbolos SVG

1. Abra el panel de estilo y las opciones de `Marcador simple`.
2. En `Tipo de capa del símbolo`, seleccione __"Marcador SVG"__.
3. Desplácese hasta el navegador SVG. Aquí encontrará todas las carpetas de sus bibliotecas SVG instaladas.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

::::

::::{tab-item} Añadir una biblioteca SVG externa u otras bibliotecas de estilo

Si tiene una biblioteca de símbolos SVG en una carpeta, puede añadirlos a su gestor de estilos.

1. Abra el gestor de estilos: `Configuración` → `Administrador de estilos`.
2. Haga clic en `Importar / Exportar` y seleccione `Importar elementos`.
3. Navegue hasta la ubicación donde haya guardado la biblioteca o el estilo y seleccione el archivo (en la mayoría de los casos `.qml` pero el tipo de archivo también puede ser .xml)
4. Ahora puede seleccionar los símbolos que desea importar. En la mayoría de los casos, puede seleccionar todos los símbolos.
4. Haga clic en `Importar`
Los nuevos símbolos SVG están en su biblioteca SVG.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>

::::
:::::