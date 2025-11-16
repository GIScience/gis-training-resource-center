::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Diseño de mapas ejercicio 1: Crear un mapa de Ghana

## Características del ejercicio

:::{card}
__Objetivo del ejercicio__
^^^
El objetivo de este ejercicio es crear un mapa general de Ghana con sus subdistritos, carreteras principales, asentamientos y
hospitales. Esta información puede ser útil en la labor humanitaria. La primera parte del ejercicio abarcará la
simbolización de las capas de datos. La segunda parte se centrará en crear el diseño de impresión.

:::

::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse en la formación en línea y en la presencial.
- Puede realizarse como ejercicio guiado o de forma individual como autoaprendizaje.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para:__
^^^

- Visualizar de datos geográficos
- Comprender cómo QGIS visualiza los datos geoespaciales
- Crear mapas generales, elaborar informes de situación

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio__
^^^

- El ejercicio tiene una duración de 3 horas aproximadamente, según el número de participantes y capacitadores.

:::

:::{grid-item-card}
__Artículos relevantes__
^^^

- [Visualización](/content/es/Wiki/es_qgis_visualisation_wiki.md)
- [Módulo 4: Visualización de datos geoespaciales](/content/es/Module_4/es_qgis_map_design_I.md)
- [Módulo 4: Diseño de mapas: El diseño de impresión](/content/es/Module_4/es_qgis_map_design_2.md)
:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo hacer capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md#how-to-do-trainings) para obtener consejos generales sobre cómo impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes han descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y replicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su proyecto de QGIS.

__Cierre de la sesión:__

- Deje tiempo para cualquier problema o pregunta relacionada con las tareas al final del ejercicio.
- Deje tiempo para preguntas abiertas.

:::

## Datos disponibles

__Descargue los datos del ejercicio [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_4/Modul_4_Exercise_1_creating_a_map_of_ghana/Modul_4_Exercise_1.zip).__ 
Siempre es importante familiarizarse con los datos que se tienen a disposición.
Para este ejercicio, utilizaremos las siguientes capas:

- Ghana: Límites administrativos subnacionales (https://data.humdata.org/dataset/cod-ab-gha)
- Centros sanitarios de Ghana (OSM Export; https://data.humdata.org/dataset/hotosm_gha_health_facilities). Estos datos fueron depurados para que solo contengan información sobre hospitales.
- Carreteras de Ghana (OSM Export; https://data.humdata.org/dataset/hotosm_gha_roads)
- Asentamientos de Ghana (https://data.humdata.org/dataset/ghana-settlements). Estos datos ya modificados. Solo están disponibles las capitales regionales, distritales y nacionales.

Todos los datos se descargaron del Intercambio de Datos Humanitarios. Descargue los datos desde Nexus, __descomprima la carpeta__ y cargue los datos en un nuevo proyecto QGIS.




## Tareas

### Preparación de los datos

1. Cargue los archivos `.shp` en un nuevo proyecto de QGIS.
2. Examine la tabla de atributos de las diferentes capas y observe qué información hay disponible y cómo se denominan los atributos.
3. Queremos crear un mapa comprensible, piense en qué datos necesitamos y qué datos podemos omitir.
    - Por ejemplo, la capa `hotosm_gha_roads_lines` contiene demasiadas carreteras para un mapa a escala nacional. Abramos la tabla de atributos y veamos cómo se clasifican las carreteras. Los datos utilizan la clasificación convencional de OpenStreetMap: El tipo de carretera se describe en el atributo `highway`. En nuestro caso, podría ser útil mostrar solo las carreteras primarias y secundarias, por lo tanto, todas las entidades en las que `highway=primary` O `highway=secondary`.

### Primera parte: Simbolización

Ahora que ya conocemos los datos de que disponemos, vamos a elegir la simbología de las distintas capas. ¿Qué información debe aparecer en el mapa?

Empecemos por los límites administrativos. Queremos mostrar los nombres y contornos de la capa `adm_1`, así como los contornos de la capa `adm_2`.

1. Coloque las capas de los límites administrativos en orden ascendente con `adm_0` en la parte inferior, seguida de `adm_1` y `adm_2`.
2. Abra la pestaña __Symbology__ para la capa `adm_2`. Configure el __relleno de color__ en transparente, el __ancho de trazo__ en 0,16 milímetros y el __estilo de trazo__ en línea discontinua.
3. Abra la pestaña __Symbology__ para la capa `adm_1` y establezca el color en transparente. Deje el ancho de trazo en 0,26 milímetros y el estilo de trazo en línea continua.
4. Abra la pestaña __Symbology__ para la capa `adm_0` y configúrela con un color neutro (por ejemplo, gris claro).
5. Queremos mostrar los nombres de las regiones (`adm_1`). Abra la pestaña __Label__ para la capa `adm_1`. Seleccione “Single Labels” y elija el atributo `ADM1_EN` para los valores que se van a mostrar.

---

Pasemos ahora a los asentamientos.

La capa de los asentamientos se limpió y solo están disponibles las ciudades, las capitales regionales, las capitales del distrito y las capitales de país.

1. Abra la pestaña __Symbology__ para la capa `gha_ppl_1m_NGA` y seleccione una simbología categorizada.
2. En “Value”, seleccione `popPlace1`
3. Haga clic en “Classify”.
4. Aparecerá una lista de todos los valores únicos. Asigne a cada uno un marcador de puntos gris oscuro.
5. Queremos poder diferenciar entre capital de país, de región o de distrito. La capital más importante es la del país, seguida de las capitales regionales y, por último, las capitales de distrito. Asigne a cada marcador un tamaño diferente que corresponda a su importancia.
6. Añadimos a continuación una etiqueta para la capital del país y las capitales regionales.
7. Vaya a la pestaña “__Label__” y seleccione __“Rule-based Labelling”__.
8. Añada una nueva regla e introduzca la siguiente expresión en el filtro: `(  "popPlace1"  =   'Country capital'  ) OR ( "popPlace1" = 'Regional capital' )`.
9. Configure el “Value” en `Name`.
10. Establezca la fuente en cursiva y dibuje un buffer de texto para diferenciar las etiquetas de los asentamientos de las etiquetas de las regiones.

---

Pasemos a la red vial.

1. La capa de la red vial debe situarse sobre los límites administrativos para que el trazado y las conexiones de las carreteras sean siempre visibles.
2. Abra la pestaña __Symbology__ para `hotosm_gha_roads_lines`. Seleccione “__Rule-based__” y añada un nuevo filtro haciendo doble clic en `(no filter)`.
3. Abra el constructor de expresiones haciendo clic en el icono situado a la derecha de la opción de filtro.
4. En primer lugar, abra un paréntesis haciendo doble clic en `(`.
5. En la pestaña central del generador de expresiones, despliegue la lista __“Fields and Values”__. Haga doble clic en `highway` para añadirlo a la expresión de la izquierda. A continuación, a la derecha, haga clic en `All Unique` para listar todos los valores posibles de ese atributo.
6. En la ventana de la izquierda, haga clic en el signo `=` para añadirlo a su expresión.
7. En la lista con todos los valores únicos. Seleccione `primary` y añádalo a su expresión.
8. Cierre el paréntesis haciendo clic en `)` debajo del campo de expresión de la izquierda.
9. Añada el Operador `OR` y repita la misma expresión con el paréntesis, pero seleccionando el valor único `secondary`.
10. La expresión terminada debe ser `(  "highway"  =  'primary' )  OR  ( "highway"  =  'secondary'  )`.
11. Seleccione un color y un grosor para la línea, de modo que se distinga de los límites administrativos (por ejemplo, amarillo; tenga en cuenta que algunos colores tienen asociaciones convencionales; azul para el agua, por ejemplo).

---

Ahora, como toque final, seleccionemos un símbolo para las instalaciones sanitarias:

1. Vaya a la capa `hospital_GHA`.
2. Abra la pestaña __Symbology__ y seleccione la opción `Simple Marker`.
3. En “Symbol Layer type”, seleccione SVG-Symbol.
4. Desplácese hacia abajo hasta que vea el navegador SVG-Symbol.
5. En la barra de búsqueda, ingrese “hospital”.
6. Seleccione uno de los símbolos SVG a su disposición.
7. Ajuste el color a rojo.
8. Haga clic en Apply y OK.

Hemos asignado un símbolo para cada capa a nuestra disposición. Observe el mapa que ha creado y decida si quiere ajustar alguna simbología para que el mapa sea más fácil de leer. ¿Necesita cambiar algunos colores? ¿Están las capas ordenadas de forma que la información sea visible? ¿El tamaño de letra es adecuado o tapa demasiada información?

__Paso adicional__: [Añadir un mapa base](/content/es/Wiki/es_qgis_basemaps_wiki.md) puede ayudar a los lectores potenciales a orientarse.

Ahora el mapa debería estar listo para un diseño de impresión.

### Segunda parte: Creación del diseño de impresión

Una vez que esté satisfecho con la simbología y los colores de sus datos, el siguiente paso es crear un diseño de impresión. Al añadir información adicional como el título, las fuentes de datos, la proyección cartográfica, la descripción, etc., proporciona a su público los medios para contextualizar y evaluar el mapa y su contenido por sí mismos.

1. Abra una nueva composición de impresión y asígnele un nombre (por ejemplo, Mapa de Ghana con hospitales). Se abrirá una nueva ventana con un lienzo en blanco y un conjunto diferente de herramientas. Este es el maquetador de impresión.
    - A la izquierda, encontrará una barra de herramientas para añadir y mover elementos en el lienzo de diseño de impresión.
    - A la derecha encontrará una lista de los elementos que agregó al diseño de impresión (aún está vacía). Debajo encontrará una pestaña llamada __“item properties”__. Aquí se modifican los elementos del diseño de impresión (por ejemplo, se puede introducir el texto de un cuadro de texto o cambiar el tipo de letra).
2. Agregue un nuevo mapa haciendo clic en el ![icono New Map](/fig/30.30.2_print_layout_insert_map_icon.png) (`Add Map`) de la barra de herramientas de la izquierda y dibuje un rectángulo en el lienzo de impresión. [Video](/content/es/Module_4/es_qgis_map_design_2.md#adding-a-new-map)
3. Mueva el mapa y colóquelo de manera que todo el país sea visible a una escala razonable.
4. Añadamos un título:
    - Haga clic en el ![icono Add text](/fig/30.30.2_print_layout_add_text.png) (`Add text`)
    - Arrastre un rectángulo sobre el lienzo.
    - En la ventana de propiedades del elemento, a la derecha, encontrará un cuadro de texto con el texto “Lorem ipsum”. Aquí puede introducir el título del mapa (por ejemplo, Mapa de Ghana con carreteras y hospitales).
    - Ajuste el tamaño de fuente: Haga clic en el menú desplegable __Font__ y ajuste el tamaño de la fuente para un título (25 pts. o más). Ajuste el cuadro de texto si es necesario.
5. Añadamos una leyenda:
    - Haga clic en el ![icono Add legend](/fig/30.30.2_print_layout_add_legend.png) (`Add legend`).
    - Vaya al panel __Item Properties__ situado a la derecha.
    - Desplácese un poco hacia abajo y desactive la casilla de verificación `Auto Update`. Ahora puede editar libremente cada elemento de la leyenda.
    - Ajuste la leyenda eliminando las capas innecesarias (que no se ven en el mapa) y cambie el nombre de la capa en la leyenda haciendo clic en el ![icono Edit](/fig/30.30.2_print_layout_legend_edit.png) (`Edit selected item properties`) debajo de las entradas de la leyenda.
6. Ahora, añadamos una barra de escala:
    - Haga clic en el ![icono Add Scale bar](/fig/30.30.2_print_layout_add_scale_bar.png) (`Add Scale bar`)
    - Dibuje un rectángulo en el mapa y coloque la barra de escala en el borde del mapa. Puede ajustar las unidades de la barra de escala (metros, kilómetros, etc.), el ancho fijo del segmento (50 km, 75 km, 100 km, etc.) y el número de segmentos (a la derecha).
7. Añadamos una flecha que indique el norte:
    - Haga clic en el ![icono Add North Arrow](/fig/30.30.2_print_layout_add_orientation.png) (`Add North Arrow`).
    - Arrastre un rectángulo sobre el diseño de impresión. Ajuste el tamaño y la ubicación de la flecha norte. También puede cambiar el icono en las propiedades del elemento.
8. Añadamos un logotipo (por ejemplo, el de la IFRC o el de su sociedad nacional):
    - Haga clic en ![Add Picture](/fig/30.30.2_print_layout_add_image.png) (`Add picture`)
    - Arrastre un rectángulo en el lugar donde desea añadir el logotipo.
    - Vaya al panel `Item properties` de la derecha y cambie a `Raster image`.
    - Haga clic en los tres puntos `...` y seleccione el archivo con su logotipo.
    - Si es necesario, cambie el tamaño o mueva la imagen en el diseño de impresión.

:::{figure} ../../fig/30.30.2_print_layout_add_picture_options.png
---
name: add picture item properties
width: 600 px
---
El panel de propiedades de las imágenes. Es necesario especificar la ubicación de guardado de una imagen para poder verla en el diseño de impresión.
:::

9. Añada un cuadro de texto con información adicional, las fuentes, el autor (usted) y la fecha de creación.
10. Cuando esté satisfecho con el diseño de impresión. Puede exportarlo como PDF. Puede guardarlo en la carpeta del proyecto, en “resultados”.
11. Una vez exportado el mapa. Mire el PDF y asegúrese de que tiene el aspecto que pretendía. Algunas cosas pueden parecer diferentes en el PDF. Si no es correcto, es posible que tenga que realizar algunos ajustes en la simbología.

El mapa terminado podría tener un aspecto similar al siguiente:

:::{figure} ../../fig/en_map_design_exercise_1_results.png
---
name: Main road network and hospitals in Ghana, Africa
width: 600px
---
Se dejó espacio en la esquina inferior derecha para un mapa general.
:::

¿Qué se puede aprender de este mapa? Se pueden identificar claramente las zonas de más difícil acceso y donde el tiempo de desplazamiento hasta un hospital es mucho mayor que en las regiones pobladas del sur de Ghana.

### Ejercicio adicional.

Si terminó con el mapa principal, haga clic en el mapa y vaya a las propiedades del elemento. En la sección de capas, marque las casillas `Lock Layers` y `Lock styles for layers`. Esto significa que si cambia el mapa en la ventana principal de QGIS, el mapa que añadió en Ahora puede empezar a trabajar en un mapa general. Utilizaremos un shapefile con los países de África.

1. Vuelva a la ventana principal de QGIS y cargue las capas de la carpeta `Bonus Exercise`.
2. En el panel __Layer__, oculte las capas del mapa principal haciendo clic en el icono ![Ojo](/fig/30.30.2_layer_visibility_icon.png) situado junto al nombre de la capa.
3. Diseñe un estilo a los países con un color neutro y discreto. Por ejemplo, puede utilizar el “__relleno gris 3__” de las plantillas de estilo.
4. Una vez que esté satisfecho con el estilo de su mapa general, vuelva a la ventana __Print Layout__.
5. Añada un segundo mapa y colóquelo en una esquina.
6. En el panel __Item properties__ del segundo mapa (“__Mapa 2__”), desplácese hacia abajo y abra las opciones `Overview`.
7. Haga clic en el botón `+` para añadir una nueva vista general.
8. En la opción “__Map Frame__”, seleccione “__Mapa 1__”. Esto mostrará el marco del mapa principal en su mapa general.

¡Felicidades! Finalizó su primer mapa.
