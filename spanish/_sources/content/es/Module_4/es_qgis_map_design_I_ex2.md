::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 2: Creación de un mapa de situación de las inundaciones de Larkana, Pakistán

::::{grid} 2
:::{grid-item-card}
__Programa de ejercicios de respuesta a las inundaciones de Larkana:__
^^^

Este ejercicio es la cuarta parte del [programa de ejercicios de respuesta a las inundaciones de Larkana](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_larkana_flood_response.html).

Puede consultar el ejercicio anterior [aquí](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_module_3_ex5.html)

:::
:::{grid-item-card}
__Competencias abordadas en este ejercicio:__
^^^

- Trabajar con múltiples capas
- Importar bibliotecas SVG
- Usar marcadores SVG
- Clasificar datos geoespaciales
- Crear un diseño de impresión
- Configurar mapas generales

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura alrededor de 3 horas, dependiendo del número de participantes y su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Visualización de los datos vectoriales](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_visualisation_wiki.html)
* [Creación de mapas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_map_making_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_layer_concept_wiki.html)
* [Clasificación de datos geoespaciales: categorizados](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_categorized_wiki.html)
* [Clasificación de datos geoespaciales: graduado](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_graduated_wiki.html)

:::
::::

::::{topic} Contexto

En 2024, las provincias de Punyab, Sind y Baluchistán, en Pakistán, sufrieron inundaciones devastadoras debido a las intensas y prolongadas lluvias. Como consecuencia, la infraestructura crítica, como los centros de salud, se vieron afectadas y el acceso por carretera a la ciudad de Larkana quedó gravemente limitado. Usted ya ha realizado un análisis utilizando datos reales de este desastre natural en el [ejercicio anterior](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_module_3_ex5.html). Ahora queremos visualizar nuestros hallazgos en un mapa atractivo, que se pueda imprimir o compartir con las diferentes partes interesadas. El mapa mostrará los centros de salud y los centros hospitalarios específicos, que fueron impactados por las inundaciones. Además, visualizaremos el acceso por carretera a la ciudad de Larkana el 12 de agosto de 2024. Esta información es crucial para evaluar el acceso logístico a la ciudad.

El ejercicio se divide en dos partes. En la primera parte, ajustará la Simbolización de las capas para el mapa final. En la segunda parte, usará el compositor de diseño de impresión para crear un mapa terminado, que se pueda imprimir y distribuir.

::::

:::{figure} ../../fig/Larkana_Map_Overview.png
---
width: 700px
name: Map Larkama
---
El mapa que realizaremos en este ejercicio (fuente: HeiGIT).
:::

### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/Exercise_2/Module_4_Exercise_2_Larkana_flood_map.zip

Ha creado los datos para Larkana en el [módulo 3, ejercicio 5](https://giscience.github.io/gis-training-resource-center/content/es/Module_3/es_qgis_module_3_ex2.html). Para realizar este ejercicio, cree una carpeta en su computadora y copie toda la estructura de carpetas del Ejercicio 4. __En caso de que no haya hecho el ejercicio 4 del módulo 3, puede descargar los datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_4/Exercise_2/Module_4_Exercise_2_Larkana_flood_map.zip)__. Guarde la carpeta en su computadora y descomprima el archivo.
:::


| Nombre del conjunto de datos | Título original | Publicado por | Descargado de |
| :-------------------- | :----------------- |:----------------- |:----------------- |
| Health_Facilities_Flood_2024_AOI.gpkg | [Centros de salud de Pakistán (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) | Equipo humanitario de OpenStreetMap (HOT) | HDX |
| PAK_2024_Minimum_Flood_Extend_reprojected.gpkg | [El satélite detectó extensiones de agua del 08 al 12 de agosto de 2024 sobre Pakistán)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) | UNO SAT | HDX |
| PAK_flood_2024_blocked_road.gpkg | PAK_flood_2024_blocked_road | Usted mismo | Este conjunto de datos fue creado en el [ejercicio anterior](https://giscience.github.io/gis-training-resource-center/content/es/Module_3/es_qgis_module_3_ex2.html) |


<!--FIX: add all datasets used in this exercise to the table-->


:::{hint} Estructura de las carpetas
Mantenga su gestión de datos ordenada, mediante la creación de una estructura de carpetas estándar en su computadora para sus proyectos QGIS y sus datos geoespaciales.
:::

## Tarea 1: Preparación de los datos


1. Cree un nuevo proyecto QGIS y guárdelo en su carpeta de ejercicios. Dele un nombre claro, p. ej.: “Larkana_inundacion_respuesta_map”.

2. En el __panel Navegador__, abra la carpeta `Project Home` y vaya a la subcarpeta de datos.
3. Importe las capas a la carpeta y luego, importe las capas a su proyecto de QGIS:
    - Centros de salud: `Health_Facilities_Flood_2024_AOI.gpkg`
    - Carreteras: `Roads_Larkana.gpkg`
    - Puntos de las carreteras bloqueados: `PAK_flood_2024_blocked_road.gpkg`
    - Extensión de las inundaciones 2024, reproyectada: `PAK_2024_Minimum_Flood_Extend_reprojected.gpkg`

4. Tómese un momento para familiarizarse con los datos disponibles. Examine la tabla de atributos de las diferentes capas y observe qué información hay disponible y cómo se denominan los atributos.

5. [Añadir un mapa base](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_basemaps_wiki.html#standard-qgis-basemaps):
    - Navegar a la barra de menús -> `Layer` -> `Add Layer` -> `Add XYZ-Layer...` y añadir un mapa base OpenStreetMap.


## Tarea 2: Simbolización

Crear un buen mapa implica seleccionar los iconos y colores adecuados para transmitir la información en sus datos.
El primer paso para crear un mapa comprensible es ordenar las capas de forma lógica para poder ver la información:

En el panel de capas:
- Coloque la capa de límites administrativos en la parte inferior,
- coloque las capas de carreteras y extensión de inundaciones en el medio
- y coloque las capas de puntos (centros de salud y carreteras bloqueadas) en la parte superior.

Cada capa tiene su propio [panel de simbología](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#styling-panel) donde puede ajustar la simbología, los colores y las etiquetas de las entidades geográficas de esa capa. ¿Necesita cambiar algunos colores? ¿Están las capas ordenadas de forma que la información sea visible? Piense en qué datos necesitamos y qué datos podemos omitir.
Por ejemplo, la capa `Roads_Larkana` contiene demasiadas carreteras para un mapa a escala nacional. Abramos la tabla de atributos y veamos cómo se clasifican las carreteras. Los datos utilizan la clasificación convencional de OpenStreetMap: El tipo de carretera se describe en el atributo `highway`. En nuestro caso, podría ser útil mostrar solo las carreteras primarias y secundarias, por lo tanto, todas las entidades en las que `highway=primary` OR `highway=secondary`.

Recorramos las capas una por una y visualicémoslas, de manera significativa.

### __Centros de salud:__

En el __panel de capas__, haga clic con el botón derecho en la capa `Health_Facilities_Flood_2024_AOI` > `Properties`. Se abrirá una nueva ventana con una sección de pestañas vertical a la izquierda. Vaya a la pestaña `Symbology`.
Vamos a crear nuestro propio símbolo personalizado para los centros de salud:
1. En `Symbol layer type`, seleccione __`SVG Marker`__.
2. Desplácese hacia abajo hasta el navegador SVG. Aquí encontrará todas las carpetas de sus bibliotecas instaladas SVG.

:::{dropwodn} Video: Uso de los símbolos SVG
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_30.30.2_using_svg_symbols.mp4"></video>
:::

- Desplácese por la carpeta hasta encontrar un símbolo adecuado (p. ej.:![](/fig/en_m4_ex_2_cross_symbol.png)).

:::{figure} ../../fig/crescent_moon.PNG
---
width: 450px
name: SVG Marker
---
Cree un marcador SVG personalizado.
:::

Podemos personalizar el icono aún más:

- En la esquina superior derecha de la pestaña de simbología, haga clic en el `+` para agregar otro "Simple Marker".
- Por defecto, será un círculo. Asegúrese de que el círculo esté debajo del ![](/fig/en_m4_ex_2_cross_symbol.png) símbolo de haciendo clic en ![](/fig/m4_ex2_down_symbol.png).
- Cambie el color del círculo a blanco.
- Haga clic en `Apply`, luego en `OK`.

:::{figure} /fig/en_3.36_m4_ex2_complex_symbol.png
---
name: m4ex2_complex_symbol
width: 450 px
---
Puede usar varias capas de símbolos para crear un símbolo complejo en QGIS 3.36.
:::

### __Carreteras:__

El conjunto de datos de carreteras contiene mucha información, que no necesariamente, queremos mostrar en nuestro mapa final. Podemos clasificar los datos y ocultar la información no deseada. Ya identificamos las carreteras importantes en el ejercicio anterior: las carreteras donde __autopista__ es igual a `motorway`, `primary`, `secondary`, `trunk`. Estos caminos son las __carreteras principales__.



Podemos clasificar las carreteras y luego seleccionar aquellas pertinentes, que se mostrarán. Para categorizar las carreteras, haga doble clic en la capa `Roads_Larkana`. La ventana de propiedades se abrirá con una barra de pestañas vertical a la izquierda. Vaya a la __`Symbology tab`__.
- En la parte superior, se encuentra un menú desplegable. Despliéguelo y elija `Categorized`.
- En `Value`, seleccione “autopista”.
- Más abajo en la ventana, haga clic en `Classify`. Ahora debería ver todos los valores o atributos únicos de la columna seleccionada “Inundación_afectados”. Puede ajustar los colores, con un doble clic en una fila del campo central.
- Elimine la marca de todas las categorías excepto: `motorway`, `primary`, `secondary`, `trunk`

    :::{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Clasificación de las carreteras: Puede ocultar la información innecesaria al desmarcar las casillas.
    :::

* Tiene la opción de personalizar el ancho de las líneas de las carreteras principales para mejorar la visualización. Abra la ventana de simbología y seleccione “Symbol”. En la nueva ventana, puede ajustar el ancho de las líneas, según su preferencia.

    :::{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Clasificación de las carreteras: Puede ajustar el ancho de una sola categoría.
    :::

* Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.

### __Puntos de carreteras bloqueadas:__

* Haga clic con el botón derecho en la capa __“PAK_inundación_2024_bloqueada_carretera”__ en el `Layer Panel` -> `Properties`. Se abrirá una nueva ventana con una sección de pestañas vertical a la izquierda. Vaya a la `Symbology` pestaña.
* Mantenga la opción de símbolo único. Seleccione cualquier símbolo de la lista, que sea adecuado para marcar carreteras bloqueadas.
* Una vez que haya terminado, haga clic en `Apply` y `OK` para cerrar la ventana de simbología.

    :::{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visulsing blocked roads with icons
    align: center
    ---
    Visualización de carreteras bloqueadas con iconos
    :::


### __Aeropuertos:__

En el [ejercicio anterior](/content/es/Module_3/es_qgis_module_3_ex2.md) descubrió que el aeropuerto de Mohenjo Daro, en el suroeste de Larkana City, todavía es accesible a través de la red vial. Los suministros esenciales podrían transportarse desde el aeropuerto hasta la ciudad, sin toparse con ninguna barricada. Queremos señalar esta posibilidad. ¡Marquemos el aeropuerto como un punto y visualicémoslo!

Para ello, crearemos un conjunto de datos de puntos, completamente nuevo, que represente a los aeropuertos.
* Haga clic en `Layer` --> `Create Layer` -> `New GeoPackage Layer`([Video Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#create-a-new-layer))
* En `Database`, haga clic en ![](/fig/Three_points.png) y navegue a la carpeta `temp`. Asigne un nombre para el nuevo conjunto de datos __“PAK_airports”__. Haga clic en `Save`.
* `Geometry type`: Seleccione `Point`
* En `Additional dimension`, siempre deberá asegurarse de marcar `None`.
* Seleccione el sistema de referencia de coordenadas (SRC) "EPSG:4326-WGS 84". De forma predeterminada, el QGIS selecciona el proyecto SRC.
* En `New Field`, puede agregar columnas a la nueva capa. Agregue la columna __“Airport”__.
* `Type`: Seleccione `Text(string)`
* Haga clic en `Add to Fields List` ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
* Haga clic en `OK`.
* Su nueva capa aparecerá en el `Layer Panel`.

    :::{figure} /fig/Create_Geopackagelayer_airport.PNG
    ---
    width: 400px
    name: Digitising airports
    align: center
    ---
    Creación de una nueva capa de puntos para los aeropuertos.
    :::

::::{margin}
:::{tip}
Si no puede ver la barra de herramientas, `View` -> `Toolbars` consulte el `Digitizing Toolbar` ([Video Wiki](/content/es/Wiki/es_qgis_digitisation_wiki.md#creation-of-point-data)). ![](/fig/Digitizing_Toolbar.png)
:::
::::

* Ahora puede crear un punto para el aeropuerto y si desea aeropuertos adicionales también ([Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#add-geometries-to-a-layer)). Actualmente la nueva capa __“PAK_airports”__ está vacía. Para añadir entidades, podemos usar `Digitising Toolbar`.

*  Busque el Aeropuerto de Mohenjo Daro en Google. Una vez que haya encontrado el aeropuerto, haga clic en ![](/fig/mActionCapturePoint.png). Haga clic con el botón izquierdo en la entidad que desea digitalizar.

    :::{figure} /fig/Feature_Att_Airport.PNG
    ---
    width: 400px
    name: Digitising airports
    align: center
    ---
    Digitalización de nuevas entidades geográficas de punto.
    :::

* Una vez que haya terminado con la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
* Haga clic, de nuevo, en ![](/fig/mActionToggleEditing.png) para finalizar el modo de edición.

Simbolicemos el aeropuerto con un icono de avión, para que podamos identificarlo con rapidez.

* Haga clic con el botón derecho en la capa __"PAK_airports"__ en el `Layer Panel` -> `Properties`. Se abrirá una nueva ventana, con una sección de pestañas vertical, a la izquierda. Navegue a la pestaña [ `Symbology`](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#styling-panel).
* Haga clic en `Simple Marker`.
* En `Symbol layer type`, seleccione __`SVG-Marker`__.
* Desplácese un poco hacia abajo y encontrará un cuadro con todos los símbolos SVG disponibles.
* En la barra de búsqueda debajo del cuadro, busque "Plane".
* Seleccione un símbolo de avión.
* Haga clic en `Apply`, luego en `Ok`.


### __Extensión de las inundaciones:__

Abra la pestaña __`Symbology`__ para la capa `PAK_2024_Minimum_Flood_Extend_reprojected`. Elija la opción de color azul claro y ajuste la opacidad a aproximadamente el 30 %.

:::{figure} /fig/Module_4/m4_ex2_symbology_flood.png
---
name: m4_ex2_symbology_flood.png
width: 550 px
---
Ajustes de la simbología para indicar la zona inundada.
:::

## Tarea 3: Creación del diseño de impresión

Una vez que esté satisfecho con la simbolización y los colores de sus datos, el siguiente paso es crear un __diseño de impresión__. El diseño de impresión es donde coloca todos los elementos de su mapa, junto con la información adicional, para crear un mapa completo. Al añadir información adicional como el título, las fuentes de datos, la proyección cartográfica, la descripción, etc., proporciona a su público los medios para contextualizar y evaluar el mapa y su contenido por sí mismos.

1. Abra una nueva composición de impresión y asígnele un nombre (p. ej.: Larkana_inundaciones).
    - Vaya a `Project` > `New Print Layout` > introduzca un nombre para la nueva composición de impresión > haga clic en `OK`.

:::{figure} ../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Creación de una nueva composición de impresión
:::

- Aparecerá una nueva ventana con un diseño de impresión en blanco. Este es el compositor de diseño de impresión.
    - A la izquierda, encontrará una barra de herramientas para añadir y mover elementos en el lienzo de diseño de impresión.
    - A la derecha encontrará una lista de los elementos que agregó al diseño de impresión (aún está vacía). Debajo encontrará una pestaña llamada __`item properties`__. Aquí se modifican los elementos del diseño de impresión (por ejemplo, se puede introducir el texto de un cuadro de texto o cambiar el tipo de letra).

2. Agregue un nuevo mapa haciendo clic en el ![icono New Map](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) de la barra de herramientas de la izquierda y dibuje un rectángulo en el lienzo de impresión. [Video Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_map_design_2.md#adding-a-new-map)

3. Mueva y posicione el mapa para que el área de interés sea visible a una escala razonable. Para mover el contenido del mapa, utilice la herramienta ![](30.30.2_print_layout_move_content_icon) `Move item content`.


:::{figure} /fig/Module_4/m4_ex2_print_layout_add_map.png
---
name: m4_ex2_print_layout_add_map
width: 650 px
---
Incorporación del mapa al diseño de impresión.
:::

4. Añadamos una etiqueta para la ciudad de Larkana. Esto ayudará a la audiencia a orientarse por si misma, ya que podría no estar familiarizada con la región.
    - Haga clic en el ![icono de añadir texto](/fig/30.30.2_print_layout_add_text.png) (`Add text`).
    - Dibuje un pequeño rectángulo junto a la ciudad de Larkana.
    - En la ventana de propiedades del elemento, a la derecha, encontrará un cuadro de texto con el texto “Lorem ipsum”. Introduzca "Larkana" en su lugar.
    - Haga clic en el menú desplegable __`Font`__ y ajuste el tamaño de la fuente, para que se pueda leer fácilmente.

:::{figure} /fig/Module_4/m4_ex2_print_layout_label_city
---
name: m4_ex2_print_layout_label_city
width: 600 px
---
Incorporación de una etiqueta para la ciudad de Larkana.
:::

4. Añadamos un título:
    - Haga clic en ![icono de añadir texto](/fig/30.30.2_print_layout_add_text.png) (`Add text`).
    - Arrastre un rectángulo sobre el lienzo.
    - En la ventana de propiedades del elemento, a la derecha, encontrará un cuadro de texto con el texto “Lorem ipsum”. Aquí puede introducir el título de su mapa (p. ej.: “Larkana, centros de salud y carreteras afectadas por inundaciones”).
    - Ajuste el tamaño de fuente: Haga clic en el menú desplegable __`Font`__ y ajuste el tamaño de la fuente para un título (25 pts. o más). Ajuste el cuadro de texto si es necesario.
    - Debajo del menú desplegable de fuentes, agregue un pequeño margen horizontal y vertical.

:::{figure} /fig/Module_4/m4_ex2_print_layout_add_title.png
---
name: m4_ex2_print_layout_add_title
width: 600 px
---
Incorporación de un título al diseño de impresión.
:::


5. Añadamos una leyenda:
    - Haga clic en el ![icono Add legend](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`).
    - Arrastre un rectángulo sobre el lienzo.
    - Vaya al panel __`Item Properties`__ situado a la derecha.
    - Desplácese un poco hacia abajo y desactive la casilla de verificación `Auto Update`. Ahora puede editar libremente cada elemento de la leyenda.
    - Ajuste la leyenda eliminando las capas innecesarias (que no se ven en el mapa) y cambie el nombre de la capa en la leyenda haciendo clic en el ![icono Edit](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) debajo de las entradas de la leyenda. Utilice el![](/fig/Module_4/m4_ex2_print_layout_add_to_legend.png) icono de para agregar o eliminar capas de la leyenda.
    - En `Main Properties` superior, inserte "Leyenda" como título.

:::{figure} ../../fig/Larkana_Legend.PNG
---
width: 700px
name: Create Print Layout
---
Ajustes de la leyenda.
:::

6. Ahora, añadamos una barra de escala:
    - Haga clic en el ![icono Add Scale bar](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Dibuje un rectángulo en el mapa y coloque la barra de escala en el borde del mapa. Puede ajustar las unidades de la barra de escala (metros, kilómetros, ...), el ancho de segmento fijo (p. ej.: 10 km, 20 km, 50 km, ...) y el número de segmentos (a la derecha).

7. Añadamos una flecha que indique el norte:
    - Haga clic en el ![icono Add North Arrow](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`).
    - Arrastre un rectángulo sobre el diseño de impresión. Ajuste el tamaño y la ubicación de la flecha norte. También puede cambiar el icono en las propiedades del elemento.

8. Añadamos un logotipo (por ejemplo: su sociedad nacional):
    - Haga clic en ![Add Picture](/fig/30.30.2_print_layout_add_image.png) (`Add picture`)
    - Arrastre un rectángulo en el lugar donde desea añadir el logotipo.
    - Vaya al panel `Item properties` de la derecha y cambie a `Raster image`.
    - Haga clic en los tres puntos `...` y seleccione el archivo con su logotipo (para este ejercicio, el logotipo de la Sociedad de la Media Luna Roja de Pakistán está guardado aquí: `/Module_4_Exercise_2_Larkana_flood_map/img/`).
    - Si es necesario, cambie el tamaño o mueva la imagen en el diseño de impresión.

9. Agregue información adicional en un cuadro de texto.
    - Haga clic en el ![icono Add text](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Arrastre un rectángulo sobre el lienzo
    - En la ventana de propiedades del elemento, a la derecha, encontrará un cuadro de texto con el texto “Lorem ipsum”. Aquí puede introducir alguna información adicional del mapa, p. ej.: el sistema de coordenadas, la información del mapa base o la fecha.

Cuando haya terminado con el diseño de su mapa, puede exportar el mapa imprimible como imagen o en formato pdf en `Layout`--> `Export as Image` o `Export as PDF`.

Ahora podría tener como resultado un mapa similar a este. Aquí se ha dejado algo de espacio para implementar un mapa general. ¡Si aún dispone de tiempo, haga el ejercicio adicional y añada un mapa general!

:::{figure} ../../fig/Larkana_Map_withoutOverview.png
---
width: 700px
name: Map Larkama
---
Su mapa final podría verse algo así.
:::

### Ejercicio adicional

Si terminó con el mapa principal, haga clic en el mapa y vaya a las propiedades del elemento. En la sección de capas, marque las casillas `Lock Layers` y `Lock styles for layers`. Esto significa, que si cambia el mapa en la ventana principal de QGIS, el primer mapa, que haya agregado al diseño de impresión, no se verá afectado por estos cambios. Ahora puede comenzar a trabajar en un mapa general. Utilizaremos un shapefile con los límites administrativos de Pakistán.

1. Vuelva a la ventana principal de QGIS. Vaya a la carpeta `Module_4_Exerise_2_Larkana_flood_map/data/Bonus_exercise/` y cargue la capa `PAK_admbnda_adm0_wfp_20220909` en su proyecto QGIS.
2. En el panel __`Layer`__, oculte las capas del mapa principal haciendo clic en el icono ![Ojo](/fig/30.30.2_layer_visibility_icon.png) situado junto al nombre de la capa.
3. Aplique el estilo del límite del país (adm0) en un color neutro y discreto. Por ejemplo, puede utilizar el “__relleno gris 3__” de las plantillas de estilo.
4. Una vez que esté satisfecho con el estilo de su mapa general, vuelva a la ventana __`Print Layout`__.
5. Añada un segundo mapa y colóquelo en una esquina.
6. En el panel __`Item properties`__ del segundo mapa (“__Mapa 2__”), desplácese hacia abajo y abra las opciones `Overview`.
7. Haga clic en el botón `+` para añadir una nueva vista general.
8. En la opción __`Map Frame`__, seleccione “__Mapa 1__”. Esto mostrará el marco del mapa principal en su mapa general.
9. También, puede agregar una barra de escala y una flecha hacia el norte a su mapa general.

:::{figure} ../../fig/Larkana_Map_Overview.png
---
width: 700px
name: Map Larkama
---
El mapa terminado podría verse algo así (fuente: HeiGIT).
:::

¡Felicidades! Ha creado un mapa terminado, que está listo para imprimir y distribuir.


