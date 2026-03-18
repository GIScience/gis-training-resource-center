# Compositor de diseños de impresión

## Añadir elementos al diseño de impresión

### Añadir un nuevo mapa

- Para añadir un nuevo mapa, haga clic en el botón __Añadir mapa__ de la barra de herramientas __de la izquierda__ y __arrastre un rectángulo en el lienzo del mapa.
- Para desplazar el mapa en el lienzo, basta con __seleccionar el mapa__ y __arrastrarlo__ con el mouse.
- Para desplazarse dentro de un mapa seleccione el botón __Mover contenido del elemento__ en el
- Para acercar el zoom en el mapa, mientras utiliza el botón __Mover contenido del elemento__, puede __mantener presionado CTRL mientras desplaza la rueda del mouse__ (suavemente) o introducir la escala manualmente en las propiedades del elemento.

:::{figure} ../../fig/en_30.30.2_adding_a_map.png
---
width: 750px
name: es_Add a new map
---
Añadir un nuevo mapa al diseño de impresión.
:::

:::: {tab-set}
::: {tab-item} Añadir un nuevo mapa
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_new_map
.mp4"></video>
:::

::: {tab-item} Mover y escalar el mapa
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_moving_the_map
.mp4"></video>
:::
::::

### Añadir un título o un cuadro de texto

El título deberá describir el fenómeno representado en el mapa.

- Para añadir texto (título, explicaciones), utilice la herramienta __Añadir etiqueta__ y dibuje un rectángulo del tamaño deseado.
- En el panel __Propiedades del elemento__ (a la derecha de su pantalla) puede __introducir su texto__ y __cambiar la fuente, el estilo, el color, etc.__ (Recuerde utilizar la barra de desplazamiento de la ventana para ver todas las opciones).

:::{figure} ../../fig/en_30.30.2_print_layout_add_text.png
---
width: 750px
name: es_ Add text to the print layout
---
Añadir texto al diseño de impresión.
:::

:::{dropdown} Video: Añadir un cuadro de texto
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_a_title
.mp4"></video>
:::

### Añadir una imagen o un logotipo

Si trabaja para una organización, lo más probable es que añada el logotipo de esa organización en los mapas que elabore.

1. Haga clic en `Añadir imagen` en la barra de herramientas de la izquierda.
2. Arrastre un rectángulo sobre el lienzo.
3. En la pestaña `Propriedades del elemento`, tendrá la opción de elegir una imagen SVG de su biblioteca SVG en QGIS o elegir una imagen __Ráster__. La mayoría de los archivos de imagen son imágenes ráster.
4. Seleccione `Imagen ráster` y haga clic en `...` para elegir la ubicación de la imagen.
5. Su imagen aparecerá en el diseño de impresión. Para asegurarse de que la imagen no se distorsione, deje el `Modo de redimensionado` en “Zoom”.

:::{dropdown}
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_raster_image.mp4"></video>
:::

### Añadir una leyenda

Antes de añadir una leyenda, asegúrese de que:

- Todas sus capas tengan un nombre explícito (“ríos”, “carreteras primarias”, etc.).
- Utilice la versión final de su mapa (asegúrese de que no haya más capas que añadir, mover, renombrar o modificar). Puede modificarlos más tarde, pero tendrá que rehacer la leyenda.

Para añadir una leyenda, puede utilizar el botón __Añadir leyenda__ de la __barra de herramientas de la izquierda__.

:::{figure} ../../fig/en_30.30.2_print_layout_add_legend.png
---
width: 750px
name: es_Add a legend to the print layout
---
Añadir una leyenda al diseño de impresión.
:::

En el panel de __Propiedades de elementos__, si mantiene la opción __Actualización automática__ marcada, las nuevas capas añadidas a su proyecto se añadirán automáticamente a la leyenda, pero no podrá controlarlas individualmente (renombrarlas si es necesario, reordenarlas o eliminar elementos). 
Una vez desmarcada la opción, podrá actualizar el nombre de las capas, agruparlas, eliminarlas o reorganizarlas, etc.

Si tiene demasiados elementos en su leyenda y no caben horizontalmente en el mapa, también puede dividir la leyenda en varias columnas si navega por el panel `Propriedades del elemento`, amplía la sección `Columnas` y aumenta el __recuento__.

:::: {tab-set}
::: {tab-item} Añadir una leyenda

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_legend
.mp4"></video>

:::

:::{tab-item} Editar la leyenda

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_editing_the_legend
.mp4"></video>

:::

:::{tab-item} Leyenda de 2 columnas

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_multiple_columns_legend
.mp4"></video>

:::

::::

### Añadir una barra de escala

Antes de añadir una barra de escala, seleccione su mapa principal y compruebe en el panel __Propiedades del elemento__ que el campo __Escala__ tenga un __número redondo__.

:::{figure} ../../fig/en_30.30.2_print_layout_scale.png
---
width: 750px
name: es_30.30.2_print_layout_scale_2
---
Asegúrese de que la escala sea un número redondo.
:::

Para añadir una barra de escala, puede utilizar el botón __Añadir barra de escala__ que se encuentra en la __barra de herramientas de la izquierda__. En el panel __Propiedades del elemento__, personalice las siguientes funciones:

- Qué mapa __está relacionado con la escala__.
- __Sistema de unidades de la barra__ (metros, millas, grados).
- __Segmentos a la izquierda__: segmentos mostrados antes de 0 m (siempre ajustados a 0).
- __Ancho fijo__: defina el ancho de cada segmento (por ejemplo: 1 km, 10 km, 50 km, etc.).
- __Altura__: altura (grosor) de la barra de escala.

_Hay muchas otras opciones para personalizar la barra de escala (cambiar la fuente, los colores, etc.)._

:::{figure} ../../fig/en_30.30.2_print_layout_add_scale_bar.png
---
width: 750px
name: es_30.30.2_print_layout_add_scale_bar_2
---
Añadir y personalizar la barra de escala.
:::

:::{dropdown}
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_scalebar
.mp4"></video>
:::

### Añada un mapa general

Añadir un mapa general en la esquina de su mapa le ayudará a localizar la zona, que está viendo en el mapa principal.

Para crear un mapa general, debe seguir estos pasos:

1. Prepare una __capa con las fronteras nacionales o subnacionales, o con los puntos de referencia importantes__ en su proyecto (por ejemplo: límites administrativos, capitales).
2. __Inserte el mapa general__ en su diseño de impresión (en la esquina inferior derecha, por ejemplo).
3. __Bloquee el nuevo mapa__ en el panel de propiedades del elemento.
4. Añada un rectángulo para mostrar la extensión de su mapa principal.
    1. Vaya a las __propiedades__ de su mapa principal → desplácese hacia abajo hasta que vea __Overviews__.
    2. Haga clic en __“+” el icono__ y añada una visión general.
    3. __Vincule el mapa principal__ seleccionándolo en la opción __“Marco del mapa”__.


:::{figure} ../../fig/en_30.30.2_print_layout_overview_map_preparations.png
---
width: 500px
name: es_30.30.2_print_layout_overview_map_preparations_2
---
Un mapa general debe mostrar los puntos de referencia y las fronteras importantes.
:::

:::{figure} ../../fig/en_30.30.2_print_layout_add_overview_map.png
---
width: 750px
name: es_30.30.2_print_layout_add_overview_map_2
---
Añadir un mapa general y __bloquear las capas__.
:::


:::{figure} ../../fig/en_30.30.2_print_layout_add_map_extent_overview_map.png
---
width: 750px
name: es_30.30.2_print_layout_add_map_extent_overview_map_2
---
Añadir la extensión del mapa principal al mapa general (el rectángulo rojo de la vista general).
:::

:::{dropdown} Video: Configurar un mapa general
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_overview_maps
.mp4"></video>
:::

:::{caution}
Este método requiere la certeza de que no se modificará el mapa general, ya que una vez bloqueadas las capas, éstas mantendrán el estilo y las actualizaciones no afectarán al mapa general.
:::


## Exportar el diseño de impresión

Una vez que haya terminado con la composición del mapa, es el momento de exportar el diseño de impresión como archivo PDF o SVG.

1. En la barra de herramientas, haga clic en el botón `Exportar como PDF`.
2. Asigne un nombre nuevo al archivo y seleccione la ubicación en la que quiere guardarlo.
3. Haga clic en `Guardar`.
4. Se abrirá una nueva ventana "Opciones de exportación de PDF”. Aquí puede ajustar el algoritmo de compresión. Para obtener los mejores resultados, seleccione la compresión de imagen sin pérdida.
5. Haga clic en `Guardar` de nuevo.
6. Aparecerá una nueva barra verde, debajo de las barras de herramientas. Haga clic en el enlace del archivo para __revisar el mapa exportado__.

:::{note}
Asegúrese de comprobar el mapa, después de exportar el PDF, ya que algunos elementos de diseño pueden haber cambiado en el proceso de exportación.
:::


## Plantillas de mapas

::::{tab-set}
:::{tab-item} Guardar una plantilla

1. Cuando esté satisfecho con el diseño de su mapa, haga clic en el símbolo ![](../../fig/en_30.30.2_save_as_template.png) para guardarlo como nueva plantilla.
2. Elija la ubicación en la que desea guardarla. Lo ideal es elegir el directorio de plantillas (consulte el consejo).
3. Haga clic en `Guardar`.
4. Puede abrir la plantilla arrastrándola a un proyecto QGIS.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_saving_layout_template
.mp4"></video>

:::

:::{tab-item} Abrir una plantilla

Puede arrastrar y soltar archivos de plantillas (`.qpt`, archivo de plantilla QGIS) en QGIS o utilizar el __gestor de diseños__.

1. Abra el gestor de diseño en `Diseño` → `Layout Manager`.
2. Vaya a la sección "__Nuevo usando plantilla__”.
3. Elija `Especifico` y seleccione la ubicación donde guardó su plantilla.
4. Haga clic en Abrir.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_template
.mp4"></video>

:::

:::{tab-item} Directorio de plantillas

El directorio de plantillas es donde QGIS busca las plantillas de diseño. Si tiene plantillas guardadas aquí, puede cargarlas directamente a través del gestor de diseño, sin seleccionar el archivo. 
En Windows, la ruta del archivo es `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.
En Mac, la ruta del archivo suele ser `~/Library/Application Support/QGIS/QGIS3/profiles/default/layouts/`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_template_directory
.mp4"></video>

:::

::::

:::{tip}
El gestor de diseño de QGIS ya dispone de una ubicación dedicada a las plantillas de mapas. En Windows, la ruta del archivo es `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.
En Mac,
Si guarda las plantillas aquí, podrá cargarlas directamente a través del gestor de diseño, sin necesidad de buscar el archivo.
También puede añadir rutas de archivos en la configuración de la plantilla de QGIS.
:::

## Generar un atlas

Un atlas generará una nueva página, con el mismo diseño de mapa para cada entidad de una capa. Para la mayoría de los propósitos, es útil crear primero un diseño de mapa con los elementos como leyenda, fuentes y mapa general y, luego, insertar el elemento de mapa, que será controlado por el atlas. Para generar un atlas:

1. Haga clic en el icono Configuración del atlas de la barra de herramientas del Atlas
2. En la nueva ventana, active la opción __Generar un atlas__.
3. Seleccione la página __Capa de cobertura__. Esto determinará las entidades o polígonos, que se mostrarán en una página. En nuestro ejemplo, utilizaremos los distritos administrativos subnacionales de Nigeria (`Adm1`).
4. Seleccione la página __Nombre de la página__. Debe ser el nombre del distrito o localidad subnacional que aparece en esa página. Para mostrar el nombre del distrito, elegiremos `ADM1_REF`.
5. Ahora vamos a añadir un mapa al diseño de impresión vacío.
6. Haga clic en el mapa y navegue hasta la ventana __Propiedades de la capa__ a la derecha.
7. Desplácese hacia abajo hasta que vea la opción `Controlado por Atlas` y actívela.
8. Ahora, active la vista previa del atlas en la __barra de herramientas del atlas__. De lo contrario, el diseño de impresión no se actualizará para mostrarle la página del atlas. Puede hacer clic en cada página para ver su aspecto. Dependiendo de la cantidad de entidades de su mapa, podrían tardar un poco en reproducirse.
9. Ahora puede ajustar las __opciones de margen__ para adaptar mejor la legibilidad del mapa. Por defecto, está configurado al 10 %, lo que debería bastar para la mayoría de los propósitos.
10. Antes de imprimir o exportar el atlas, asegúrese de verificar en cada página, que los otros elementos del mapa, no cubran la región representada.

:::{note}
Por ahora, el único elemento del diseño de impresión controlado por el atlas es el mapa que añadimos. Los demás elementos del mapa son los mismos en todas las páginas.
:::

:::{dropdown} Video: Configurar un atlas
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_an_atlas
.mp4"></video>
:::


### Configurar mapas de visión general con un atlas

La configuración de mapas de visión general con un atlas funciona de la misma manera que la configuración para un mapa normal. Siempre que seleccione el mapa controlado por el atlas como `Marco`, se actualizará automáticamente.


