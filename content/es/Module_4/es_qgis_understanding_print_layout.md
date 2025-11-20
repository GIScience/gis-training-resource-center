::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Comprensión del compositor de diseño de impresión

:::{figure} ../../fig/en_30.30.2_understanding_the_print_layout_composer.png
---
name: en_30.30.2_understanding_the_print_layout_composer
---
La interfaz del compositor de diseño de impresión.
:::

1. __Configuración del diseño__ (Añadir páginas, Exportar mapa, Gestionar paneles)
2. __Herramientas de marcación__ (Guardar, Nuevo, Duplicar, Añadir elementos desde plantilla, Guardar plantilla)
3. __Barra de navegación__ (Aumentar, Actualizar, Bloquear/Desbloquear elementos)
4. __Barra de herramientas__ (Aumentar, Seleccionar, Mover en mapa, Añadir nuevo mapa/imagen/texto/leyenda/escala/forma/...)
5. __Panel de entidades__: Muestra los elementos añadidos al diseño de impresión
6. __Opciones avanzadas__: Personaliza cada elemento de la capa

El gestor de diseños de impresión también funciona con una barra de herramientas (en la parte izquierda de la pantalla), donde se pueden seleccionar distintas herramientas (p. ej.: para añadir imágenes) y paneles (en la parte derecha de la pantalla), donde se puede cambiar la configuración de las herramientas o de los elementos, que se han añadido al mapa.

En primer lugar, siempre deberá configurar el tamaño de su mapa:

- Haga clic con el botón derecho en el mapa en blanco > `Page Properties`.
- Elija __el tamaño de su documento__ (A4, A3, A2). A4 y A3 son los tamaños más utilizados para los mapas.
- Elija la orientación (Horizontal o Vertical).

## Añadir elementos al diseño de impresión

### Añadir un nuevo mapa

- Añada un nuevo mapa haciendo clic en el botón ![](/fig/30.30.2_print_layout_insert_map_icon.png) `Add map` de la __barra de herramientas a la izquierda__ y arrastre un rectángulo sobre el lienzo del mapa.
- Para desplazar el mapa en el lienzo, basta con __seleccionar el mapa__ y __arrastrarlo__ con el mouse.
- Para desplazarse dentro de un mapa, seleccione el botón ![](/fig/30.30.2_print_layout_move_content_icon.png) `Move item content` de la barra de herramientas de la izquierda.
- Para acercar zoom sobre el mapa, mientras utiliza la herramienta ![](/fig/30.30.2_print_layout_move_content_icon.png) `Move item content`, puede __presionar CTRL + desplazar la rueda del mouse__ (suavemente) o introducir la escala de manera manual en las propiedades del elemento.

:::{figure} ../../fig/en_30.30.2_adding_a_map.png
---
width: 750px
name: en_30.30.2_adding_a_map
---
Añadir un nuevo mapa al diseño de impresión (fuente: CartONG).
:::

::::{tab-set}
:::{tab-item} Añadir un nuevo mapa

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_new_map.mp4"></video>

:::

:::{tab-item} Mover y escalar el mapa

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_moving_the_map.mp4"></video>

:::
::::

### Añadir un título o un cuadro de texto

El título deberá describir el fenómeno representado en el mapa.

- Para añadir texto (título, explicaciones), utilice la herramienta ![](../../fig/30.30.2_print_layout_add_text.png) `Add Label` y dibuje un rectángulo del tamaño deseado.
- En el panel __Propiedades del elemento__ (a la derecha de su pantalla) puede __introducir su texto__ y __cambiar la fuente, el estilo, el color, etc.__ (Recuerde utilizar la barra de desplazamiento de la ventana para ver todas las opciones).

:::{figure} ../../fig/en_30.30.2_print_layout_add_text.png
---
width: 750px
name: en_30.30.2_print_layout_add_tex
---
Añadir texto al diseño de impresión (fuente: CartONG).
:::

:::{dropdown} Video: Añadir un cuadro de texto

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_a_title.mp4"></video>

:::

### Añadir una imagen o un logotipo

Si trabaja para una organización, lo más probable es que añada el logotipo de esa organización en los mapas que elabore.

1. Haga clic en la herramienta ![](../../fig/30.30.2_print_layout_add_image.png) `Add image` de la barra de herramientas de la izquierda.
2. Arrastre un rectángulo sobre el lienzo.
3. En la pestaña __“Item Properties”__, tendrá la opción de elegir una imagen SVG de su biblioteca SVG en QGIS o elegir una __imagen ráster__. La mayoría de los archivos de imagen son imágenes ráster.
4. Seleccione `Raster image` y haga clic en `...` para elegir la ubicación de la imagen.
5. Su imagen aparecerá en el diseño de impresión. Para asegurarse de que la imagen no se distorsione, deje el `Resize Mode` en "Zoom".

:::{figure} /fig/3.36_print_layout_add_image.png
---
name: 3.36_print_layout_add_image
width: 650 px
---
Añadir una imagen o logotipo al diseño de impresión.
:::

:::{dropdown} Video: Añadir una imagen al diseño de impresión
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_raster_image.mp4"></video>
:::

### Añadir una leyenda

Antes de añadir una leyenda, asegúrese de que:

- Todas sus capas tengan un nombre explícito ("ríos", "carreteras primarias", etc.).
- Utilice la versión final de su mapa (asegúrese de que no haya más capas que añadir, mover, renombrar o modificar). Puede modificarlos más tarde, pero tendrá que rehacer la leyenda.

Para añadir una leyenda, puede utilizar el botón ![](../../fig/30.30.2_print_layout_add_legend.png) `Add legend` de la __barra de herramientas de la izquierda__.

:::{figure} ../../fig/en_30.30.2_print_layout_add_legend.png
---
width: 750px
name: en_30.30.2_print_layout_add_legend
---
Añadir una leyenda al diseño de impresión.
:::

En el panel de __Propiedades de elementos__, si mantiene la opción __`Auto update`__ marcada, las nuevas capas añadidas a su proyecto se añadirán automáticamente a la leyenda, pero no podrá controlarlas individualmente (renombrarlas si es necesario, reordenarlas o eliminar elementos). 
Una vez, desmarcada la opción, podrá actualizar el nombre de las capas, agruparlas, eliminarlas o reorganizarlas, etc.

Si tiene demasiados elementos en su leyenda y no caben en su mapa horizontalmente, también puede dividir la leyenda en varias columnas, con la navegación por el panel Item Properties, expandir la sección `Columns` y aumentar la `Count`.

::::{tab-set}
:::{tab-item} Añadir una leyenda

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_a_legend
.mp4"></video>

:::

:::{tab-item} Editar la leyenda

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_editing_the_legend
.mp4"></video>

:::

:::{tab-item} Añadir una leyenda de dos columnas

A veces, el espacio de su mapa no es el adecuado para una sola leyenda vertical. En este caso, es útil añadir varias columnas. Asegúrese de agrupar los elementos de la leyenda de forma lógica para que la leyenda vertical sea más fácil de leer.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_multiple_columns_legend
.mp4"></video>

:::

::::

### Añadir una barra de escala

Antes de añadir una barra de escala, seleccione su mapa principal y compruebe en el panel __Item Properties__ que el campo `Scale` tiene un __número redondo__.

:::{figure} ../../fig/en_30.30.2_print_layout_scale.png
---
width: 750px
name: en_30.30.2_print_layout_scale
---
Asegúrese de que la escala sea un número redondo.
:::

Para añadir una barra de escala, puede utilizar el botón ![](../../fig/30.30.2_print_layout_scale_bar.png)`Add scale bar` de la __barra de herramientas de la izquierda__. En el panel __Propiedades del elemento__, personalice las siguientes funciones:

- Qué mapa __está relacionado con la escala__.
- __Sistema de unidades de la barra__ (metros, millas, grados).
- __Segmentos a la izquierda__: segmentos mostrados antes de 0 m (siempre ajustados a 0).
- __Ancho fijo__: defina el ancho de cada segmento (p. ej.: 1 km, 10 km, 50 km, etc.).
- __Altura__: altura (grosor) de la barra de escala.

Hay muchas otras opciones para personalizar la barra de escala (cambiar la fuente, los colores, etc.).

:::{figure} ../../fig/en_30.30.2_print_layout_add_scale_bar.png
---
width: 750px
name: en_30.30.2_print_layout_add_scale_bar
---
Añadir y personalizar la barra de escala.
:::

:::{dropdown}
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_print_layout_adding_scalebar.mp4"></video>
:::

### Añadir un mapa general

Añadir un mapa general en la esquina de su mapa le ayudará a localizar la zona, que está viendo en el mapa principal.

Para crear un mapa general, debe seguir estos pasos:

1. Asegúrese de __bloquear las capas y el estilo de capa__ en su mapa principal.
    - Navegue al panel __Item Properties__ > `Lock layers` y `Lock styles for layers`.
2. Prepare una __capa con las fronteras nacionales o subnacionales o los puntos de referencia importantes__ en su proyecto (p. ej.: límites administrativos, capitales). Estas no deberán ser las mismas capas que las del mapa principal. Si es necesario, puede duplicar las capas, que desee utilizar en el mapa general (como los límites administrativos). No cambie las capas de su mapa principal, si tiene intención de cambiar la simbología, más adelante.
3. __Inserte el mapa general__ en su diseño de impresión, con el uso de la herramienta ![](../../fig/30.30.2_print_layout_insert_map_icon.png)`Add Map` (en la esquina inferior derecha, por ejemplo).
4. __Bloquee el nuevo mapa__ en el panel de propiedades del elemento.
5. Añada un rectángulo para mostrar la extensión de su mapa principal.
    1. Vaya a las __propiedades__ de su mapa principal > desplácese hacia abajo hasta que vea __Overviews__.
    2. Añada una visión general haciendo clic el botón `+`.
    3. __Vincule el mapa principal__ seleccionándolo en la opción `Map frame`.

:::{figure} ../../fig/en_30.30.2_print_layout_overview_map_preparations.png
---
width: 500px
name: en_30.30.2_print_layout_overview_map_preparations
---
Un mapa general deberá mostrar los puntos de referencia y las fronteras importantes para que el lector pueda localizar la región mostrada en el mapa, sin tener conocimientos específicos de la región.
:::

:::{figure} ../../fig/en_30.30.2_print_layout_add_overview_map.png
---
width: 750px
name: en_30.30.2_print_layout_add_overview_map
---
Añadir un mapa general y __bloquear la capa__.
:::

:::{dropdown} Video: Configurar un mapa general
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_adding_overview_maps
.mp4"></video>
:::

:::{Caution}
Este método requiere que esté seguro de que no va a modificar el mapa general, ya que una vez bloqueadas las capas, éstas mantendrán el estilo y cualquier actualización no afectará al mapa general.
:::

----

## Exportar el diseño de impresión

Una vez que haya terminado con la composición del mapa, es el momento de exportar el diseño de impresión como archivo PDF o SVG.

1. En la barra de herramientas encima del lienzo, haga clic en el botón ![](../../fig/30.30.2_print_layout_export_pdf.png) `Export as PDF`.
2. Asigne un nombre nuevo al archivo y seleccione la ubicación en la que quiere guardarlo.
3. Haga clic en `Save`.
4. Se abrirá una nueva ventana "PDF Export Options". Aquí puede ajustar el algoritmo de compresión. Para obtener los mejores resultados, seleccione la compresión de imagen sin pérdida.
5. Haga clic en `Save` de nuevo.
6. Aparecerá una nueva barra verde, debajo de las barras de herramientas. Haga clic en el enlace del archivo para __revisar el mapa exportado__.

:::{note}
Asegúrese de comprobar el mapa, después de exportar el PDF, ya que algunos elementos de diseño pueden haber cambiado en el proceso de exportación.
:::

## Plantillas de mapas

Las plantillas de mapas pueden simplificar y acelerar la creación de un diseño de impresión mediante el guardado de la disposición de los elementos. Sin embargo, no guardan las capas e imágenes del proyecto, que deberán reconfigurarse todas las veces.
Si trabaja para una organización, que publica mapas a menudo, o tiene que crear varios mapas sobre los mismos temas, pero en distintas regiones o épocas, puede utilizar plantillas de mapas para omitir la disposición de los elementos.

:::{note}
Las capas, los mapas y las imágenes individuales no se guardan en la plantilla. De todos modos, si tiene las mismas capas en el proyecto en el que carga la plantilla, la leyenda se actualizará, como corresponde.
:::

::::{tab-set}
:::{tab-item} Guardar una plantilla

1. Cuando esté satisfecho con el diseño de su mapa, haga clic en el botón ![](../../fig/en_30.30.2_save_as_template.png) `Save as template` de la barra de herramientas encima del lienzo para guardarlo como una nueva plantilla.
2. Elija la ubicación en la que desea guardarla. Lo ideal, es elegir el directorio de plantillas.
3. Haga clic en `Save`.
4. Puede abrir la plantilla arrastrándola a un proyecto QGIS.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_saving_layout_template
.mp4"></video>
:::

:::{tab-item} Abrir una plantilla

Puede arrastrar y soltar archivos de plantillas (`.qpt`, QGIS template file) en QGIS o utilizar el __gestor de diseños__.

1. Abra el gestor de diseño en `Layout` > `Layout Manager`.
2. Vaya a la sección __New from Template__.
3. Elija `Specific` y seleccione la ubicación donde guardó su plantilla.
4. Haga clic en “Open”.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_opening_template
.mp4"></video>

:::

:::{tab-item} Directorio de plantillas

El directorio de plantillas es donde QGIS almacena las plantillas de diseño. Si tiene plantillas guardadas aquí, puede cargarlas directamente a través del gestor de diseño, sin seleccionar el archivo.
En computadoras con Windows, la ruta del archivo es `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_template_directory.mp4"></video>

:::

::::

:::{tip}
El gestor de diseño de QGIS ya dispone de una ubicación dedicada a las plantillas de mapas. En computadoras con Windows, la ruta del archivo es `\Users\AppData\Roaming\QGIS\QGIS3\profiles\default\composer_templates`.
Si guarda las plantillas aquí, podrá cargarlas directamente a través del gestor de diseño, sin necesidad de buscar el archivo.
También puede añadir rutas de archivos en la configuración de la plantilla QGIS.
:::

## La función Atlas (generación automática de mapas)

En algunos casos, puede ser necesario crear varios mapas para distintas ubicaciones con las mismas capas. Por ejemplo, si dispone de un conjunto de datos detallados sobre las zonas afectadas por las inundaciones en Nigeria, puede crear un mapa, más detallado, para cada distrito subnacional. En QGIS, esto puede hacerse automáticamente con la __función Atlas__.

La función Atlas se encuentra en el __Compositor de diseños de impresión__ en la barra de herramientas.

:::{figure} ../../fig/en_atlas_toolbar.png
---
name: en_atlas_toolbar
width: 500 px
---
La barra de herramientas de Atlas.
:::

:::{note}
Si no puede ver las herramientas del Atlas, primero debe activar la barra de herramientas del Atlas en `View` > `Toolbars` > `Atlas Toolbar`.
:::

### Generar un Atlas

Un atlas generará una nueva página, con el mismo diseño de mapa para cada entidad de una capa. Para la mayoría de los propósitos, es útil crear primero, un diseño de mapa con los elementos como leyenda, fuentes y mapa general y luego insertar el elemento de mapa, que será controlado por el Atlas. Para generar un atlas:

1. Haga clic en el botón ![](../../fig/30.30.2_print_layout_atlas_settings.png) `Atlas Settings` de la barra de herramientas del Atlas.
2. En la nueva ventana, active la `Generate an Atlas`opción .
3. Seleccione `Coverage Layer`. Esto determinará las entidades o polígonos, que se mostrarán en una página. En nuestro ejemplo, utilizaremos las regiones administrativas subnacionales de Nigeria (`ADM1`).
4. Seleccione `Page Name`. Deberá ser el nombre de la región o localidad subnacional, que aparece en esa página. Para mostrar el nombre de la región, elegiremos la columna `ADM1_REF`, que contiene los nombres de las regiones en inglés.
5. Ahora vamos a añadir un mapa al diseño de impresión vacío.
6. Haga clic en el mapa y navegue hasta la ventana __Propiedades de la capa__ a la derecha.
7. Desplácese hacia abajo hasta que vea la opción `Controlled by Atlas` y actívela.
8. Active ahora la vista previa del Atlas en la __barra de herramientas del Atlas__. De lo contrario, el diseño de impresión no se actualizará para mostrarle la página del atlas. Puede hacer clic en cada página para ver su aspecto. Dependiendo de la cantidad de entidades de su mapa, podrían tardar un poco en reproducirse.
9. Ahora puede ajustar las __opciones de margen__ para adaptar mejor la legibilidad del mapa. Por defecto, está configurado al 10 %, lo que debería bastar para la mayoría de los propósitos.
10. Antes de imprimir o exportar el atlas, asegúrese de verificar en cada página, que los otros elementos del mapa, no cubran la región representada.

:::{Note}
El único elemento del diseño de impresión, que es controlado por el atlas, es el mapa que hemos añadido (a menos que especifique lo contrario, en las propiedades del elemento). Los demás elementos del mapa serán los mismos en todas las páginas.
:::

:::{dropdown} Video: Configurar un Atlas
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_setting_up_an_atlas
.mp4"></video>
:::

## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

1. __¿Cómo se crea o se abre un diseño en QGIS?__

:::{dropdown} Respuesta
- En QGIS, ir a `Project` → `New Print Layout` para crear un nuevo diseño.
- Se abrirá el compositor de diseños de impresión, una nueva ventana en la que podrá empezar a componer el diseño del mapa.
- Si ya se tienen diseños guardados __en este proyecto__, puede abrirlos a través del __gestor de diseño__ (`Project` → `Layout Manager`), donde habrá una lista de los diseños existentes.
- Además, puede crear un diseño, a partir de un archivo de plantilla a través del gestor de diseños (__nuevo desde plantilla__) si se ha guardado un archivo `.qpt`.
:::


2. __¿Cuál es la diferencia entre el “elemento de mapa” (marco de mapa) dentro de un diseño y el lienzo del mapa principal de QGIS?__

:::{dropdown} Respuesta
- El elemento de mapa en el compositor de diseño de impresión es una del lienzo del mapa en la ventana principal de QGIS y muestra las capas tal y como aparecen en la ventana principal.
- En el lienzo del mapa principal, puede interactuar con los datos, mientras, que en el compositor de diseños de impresión, solo se pueden ver los datos.
- El elemento de mapa muestra el mapa tal y como está en el lienzo del mapa (podría tener que actualizar el elemento de mapa para mostrar la simbología modificada), a menos que bloquee las capas y los estilos de capas para el elemento de mapa específico.
:::

3. __¿Cómo se bloquea la capa de un mapa que se ha añadido al diseño de impresión?__

:::{dropdown} Respuesta
El bloqueo es esencial, si quiere que el elemento de mapa del diseño, conserve exactamente lo que se ha establecido, incluso si más tarde, se cambian cosas en el proyecto.
- Seleccionar el elemento de mapa en el compositor de diseños de impresión
- En el__panel de propiedades de elemento__, hay una opción para __bloquear capas y estilos__ para ese mapa.
- Una vez bloqueado, puede cambiar el orden de las capas o la simbología de las capas en la ventana principal de QGIS, sin cambiar el mapa en el diseño de impresión.

:::


::::