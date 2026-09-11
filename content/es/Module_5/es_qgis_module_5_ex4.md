::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 4: Seguridad en Peshawar

:::{card}
__Objetivo del ejercicio:__
^^^
En este ejercicio, crearemos un mapa de seguridad para un equipo humanitario. En respuesta a un reciente brote de cólera en Khyber Pakhtunkhwa (KP), la Media Luna Roja de Pakistán (MLRP) y otras Sociedades Nacionales Asociadas (SNP, por sus siglas en inglés) han movilizado un equipo a esta región. El objetivo principal del equipo es llevar a cabo una evaluación exhaustiva sobre el terreno y facilitar la coordinación para cualquier respuesta futura que sea necesaria.

Para garantizar la seguridad de nuestro equipo, crearemos un mapa con información relacionada con la seguridad, como amenazas de bomba. Además, echaremos un vistazo a los datos sobre conflictos armados y crearemos un mapa general que muestre los conflictos por thesil (subdistrito/ADM3).

Para ello, utilizaremos herramientas de geoprocesamiento más avanzadas, como los buffers y las herramientas de intersección, y uniremos dos conjuntos de datos mediante uniones de tablas de atributos.

El ejercicio se divide en __tres tareas__:
- En la primera tarea, digitalizaremos la información relacionada con la seguridad como datos de punto y crearemos zonas buffer para indicar las zonas de alto riesgo.
- En la segunda tarea, cargaremos un archivo csv con datos sobre conflictos ocurridos en Pakistán. Utilizaremos este conjunto de datos para averiguar el número de incidentes conflictivos por thesil (subdistrito).
- En la tercera tarea, cargaremos otro archivo csv con datos sobre el índice de pobreza múltiple (IPM) por distrito (ADM2). El Índice de Pobreza Multidimensional (IPM) mide la pobreza considerando otros aspectos, no únicamente los ingresos. Incluye aspectos como la educación, la sanidad y el nivel de vida para comprender por qué las personas son pobres. El archivo csv no contiene información espacial explícita. Añadiremos información espacial uniéndola a una capa de polígonos que contenga los límites del distrito.

:::

::::{grid} 2
:::{grid-item-card}
__Serie de ejercicios de respuesta a las inundaciones en Larkana:__
^^^

Este ejercicio forma parte de la [Serie de ejercicios de respuesta a las inundaciones en Larkana](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Exercise_tracks/es_larkana_flood_response.html).

Sin embargo, el ejercicio __puede__ realizarse sin haber completado los ejercicios anteriores.
:::

:::{grid-item-card}
__Estas habilidades son relevantes para__
^^^

- Fundamentos de QGIS
- Trabajar con varias capas
- Realizar consultas espaciales
- Creación de datos geoespaciales

:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura unas 3 horas, dependiendo del número de participantes y de su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki:__
^^^

* [Importación de datos geoespaciales en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html)
* [Concepto de capa](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_layer_concept_wiki.html)
* [Clasificación de datos geoespaciales por categorías](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_categorized_wiki.html)
* [Digitalización - Datos de punto](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_digitisation_wiki.html#add-geometries-to-a-layer)
:::
::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese su tiempo para familiarizarse con el ejercicio y el material proporcionado.
- Prepare una pizarra. Puede ser una pizarra blanca física, un rotafolio o una pizarra digital (por ejemplo, una pizarra Miro) donde los participantes puedan añadir sus conclusiones y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos hayan instalado QGIS y hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Trainers_corner/es_how_to_training.html#how-to-do-trainings) para obtener algunos consejos generales para impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes hayan descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre cada paso y explíquelo al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y aplicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio, para asegurarse de que todos comprenden y realizan los pasos por sí mismos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Los participantes están haciendo varias tareas a la vez: prestan atención a sus instrucciones y las aplican en su propio proyecto de QGIS.

__Cierre de la sesión:__

- Dedique tiempo al final del ejercicio a cualquier problema o pregunta relacionada con las tareas que pueda surgir.
- Reserve algo de tiempo para preguntas abiertas.

:::
### Datos disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Exercise_4_Security_Peshawar/Modul_5_Exercise_4_Security_Peshawar.zip
__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_5/Exercise_4_Security_Peshawar/Modul_5_Exercise_4_Security_Peshawar.zip), guarde la carpeta en su ordenador y descomprima el archivo.__
:::

| Nombre del conjunto de datos | Título original | Editorial | Descargar desde |
| :-------------------- | :----------------- |:----------------- |:----------------- |
| 2024-01-01-2024-09-23-Pakistan.xlsx | Datos sobre conflictos en Pakistán 01/2024-09/2024 | ACLED | HDX |
| PAK_KP_admin_3.gpkg | Límites administrativos de nivel 3 del PK | UN OCHA | HDX |
| Pak_adm2_Khyber Pakhtunkhwa.gpkg | Límites administrativos de nivel 1 del PK | UN OCHA | HDX |
| 20240605_PAK_MPI.xlsx | Pakistán Índice de Pobreza Múltiple (IPM) | Oficina de Estadísticas de Pakistán | Oficina de Estadísticas de Pakistán |
| AOI_Peshawar.gpkg | Área de interés (AOI, por sus siglas en inglés) en los alrededores de Peshawar | | |

## Preparación

- Cree un nuevo proyecto QGIS y guárdelo en la carpeta de ejercicios.

## Tarea 1: Geolocalizar la información relacionada con la seguridad de los últimos días

:::{card} Contexto:
En respuesta a un reciente brote de cólera en Khyber Pakhtunkhwa (KP), la Media Luna Roja de Pakistán (MLRP) y otras Sociedades Nacionales Asociadas (SNP, por sus siglas en inglés) han movilizado un equipo a esta región. El objetivo principal del equipo es llevar a cabo una evaluación exhaustiva sobre el terreno y facilitar la coordinación para cualquier respuesta futura que sea necesaria.
El equipo se alojará en el "Roomy Crossroad Hotel Peshawar" durante su misión en la zona afectada.
Hemos recibido información relacionada con la seguridad de diversas fuentes. Nuestra tarea consiste en digitalizar esta información en datos espaciales que puedan representarse en un mapa.
:::

Para este ejercicio, utilizaremos el complemento __"QuickMapService"__ para localizar lugares con precisión. Los complementos QuickMapServices le permiten añadir fácilmente mapas base u otros servicios de mapas como una capa a su proyecto QGIS. Para [instale el complemento](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_plugins_wiki.html#installation-of-plugins):

1. En la barra de menús, haga clic en `Complementos` → `Administrar e instalar complementos...`. Se abrirá una nueva ventana.
2. En `Todos`, busque "QuickMapServices". Haga clic y seleccione `Instalar complementos` en la esquina inferior derecha.

Después de instalar el complemento, podremos añadir mapas base:

3. En la barra de menús, vaya a `Web` → `QuickMapServices` → `ESRI` → `ESRI Satellite`. Esto añadirá el mapa base de la imagen de satélite en su __panel de capas__.
4. Agregaremos también una capa de carreteras para facilitar la orientación: `Web` → `QuickMapServices` → `Google` → `Google Road`.
5. En el [panel de capas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_layer_concept_wiki.html), asegúrese de que la capa `Google Road` esté por encima de las imágenes satélites.
6. Para facilitar la navegación, haga transparentes las imágenes satélites. Para ello, vaya a la [pestaña de simbología](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#styling-panel) y ajuste la opacidad global.


7. Necesitaremos el complemento __"Lat Lon Tools"__ para localizar las coordenadas que recibimos del campo. Para [instale el complemento](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_plugins_wiki.html#installation-of-plugins), siga las mismas instrucciones que para el complemento QuickMapServices pero busque "Lat Lon Tools" en su lugar.

Genial, ahora hemos configurado nuestro proyecto QGIS y podemos empezar a digitalizar los incidentes conocidos y las áreas de interés relacionadas (como polígonos).
A continuación encontrará una tabla con la información y las ubicaciones. Lea la tabla una vez y piense qué tipo de geometría puede representar la información.

| Número | Descripción |
| :-------------------- | :----------------- |
| 1 | Las emisoras de radio locales han informado de una __amenaza de bomba__ que incluye artefactos explosivos improvisados (IED) en la carretera N45, justo entre __Seri-Bahlol__ y Tableeghi Markaz Mardina, cerca de Jandy. Por favor, marque la zona entre las comunidades a lo largo de la carretera como zonas prohibidas. |
| 2 | En una conversación con un conductor de la MLRP, una maestra local contó que las inmediaciones de la escuela__Government Girls Primary School en Takkar__ tienen fama de ser un campo minado. Concretamente, se sabe que los campos situados entre la escuela y el hospital __Noormuhmmad__ están muy minados. Debido a este peligro, los agricultores locales son muy reacios a trabajar en este terreno en concreto. |
| 3 | A raíz de los acontecimientos recientes, se ha decidido que los alrededores del estadio de criquet __Arbab Niaz Cricket Stadium Peshawar__ se designen como zona prohibida para todos los miembros del personal. Esta zona abarca la región delimitada por la carretera __N5__ al sur, la carretera __Afghan Colony__ al norte y al este, y la carretera __Charsadda__ al oeste. |
| 4 | Coordenadas GPS: __(33.99519949518549, 71.66217873936723)__. Un trabajador humanitario transportaba suministros médicos por la región cuando se les acercó un agricultor local. El agricultor mencionó que un pozo abandonado cercano, ubicado en estas coordenadas, se ha convertido en un punto de __concentración de municiones sin explotar__. Debido a su proximidad a una zona residencial, este lugar se considera de alto riesgo y requiere la atención inmediata de los equipos de desminado. |
| 5 | Coordenadas GPS: __(34.02878398623702, 71.43081737211224)__. Recientemente se ha desalojado aquí una unidad sanitaria tras una amenaza de bomba. La policía y los artificieros registraron el local, pero no encontraron explosivos. Sin embargo, los propietarios de negocios locales reportaron actividad inusual alrededor del edificio en las semanas previas a la amenaza. Este lugar está ahora bajo vigilancia. La zona situada entre la unidad sanitaria y el río, así como los parques y el área de juegos que hay detrás, deben señalarse como zona prohibida temporalmente. |
| 6 | __Qissa Khwani Bazaar, Peshawar__: En esta dirección se ha instalado un popular mercado histórico que se ha convertido en punto de encuentro de la comunidad local, pero recientes informes de inteligencia sugieren que el lugar podría estar en peligro por las protestas políticas que se han tornado violentas en el pasado. Las autoridades están estudiando la posibilidad de establecer barreras temporales para gestionar el flujo de personas, y es crucial que este lugar esté marcado como zona de alto riesgo para posibles medidas de control de multitudes. |

Para digitalizar la información, necesitaremos dos nuevas capas: Una capa de puntos y una capa de polígonos.
En caso de que la información indique un área exacta, crea una nueva capa de polígonos y mapee el área con precisión.

8. [Cree un nuevo punto y una nueva capa de polígonos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_digitissation.html#creating-new-datasets) para digitalizar la información de puntos y polígonos.

:::{tip}
Al crear la capa de puntos y polígonos utilice el SRC UTM 42 N __EPSG: 32642__. Este sistema de referencia de coordenadas es ideal para Pakistán y las unidades de medida de __están en metros__.
:::

9. Busque las ubicaciones en la tabla y cree nuevas entidades utilizando la [barra de herramientas de digitalización ](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_3/es_qgis_digitisation.html#digitisation-toolbars). Capture la información de la tabla y utilice Google, u otro buscador en su navegador, el mapa base y el complemento Lat Lon Tools para localizar la posición exacta.

10. Una vez que haya terminado, asegúrese de guardar las modificaciones en las capas haciendo clic en el botón ![](/fig/3.44_digitisation_save_edits.png) `Guardar cambios de la capa`.

Genial, hemos digitalizado con éxito la información de seguridad importante. Sin embargo, para que la información sea útil, necesitamos procesar los datos geoespaciales.

El procedimiento operativo estándar (SOP, por sus siglas en inglés) actual indica que se debe evitar un radio de 1 km alrededor de los lados involucrados en incidentes violentos recientes. Para reflejarlo en el mapa, utilizaremos la herramienta ![](/fig/mAlgorithmBuffer.png) buffer.

::::{margin}
{admonition} Recordatorio
:class: seealso

Si ve un símbolo ![](/fig/3.44_caution_symbol.png) junto al parámetro `Distancia`, significa que la capa en la que desea hacer el buffer está en un sistema de referencia de coordenadas geográficas. Esto significa que las unidades de medida están en __grados, y no en metros__. En ese caso, deberá [reproyectar su capa](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer) en un sistema de referencia de coordenadas métricas.

Consejo: EPSG:32642 es un SRC ideal para Pakistán.

::::

6. [Crear un buffer alrededor de los puntos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_geoprocessing_wiki.html) de incidentes violentos con una distancia de __2000 metros__.

7. Ahora tenemos dos capas de polígonos (los puntos de buffers y las zonas digitalizadas). Para visualizar el Área No-Go en Peshwar, podemos fusionar los polígonos de ambas capas en una sola capa con la herramienta `Unir capas vectoriales` y seleccionar las capas que queremos fusionar como entradas.

8. Cargue la capa `AOI_Peshawar.gpkg` en su proyecto.

::::{margin}
:::{tip}

Existen varios algoritmos de recorte en la caja de herramientas. Asegúrese de elegir la herramienta de recorte ![](3.44_clip_vector.png) agrupada en "Vector overlay".
:::
::::

9. Queremos crear un polígono que indique la zona segura por la que puede circular el equipo. Para ello, tenemos que "invertir" el polígono. Para ello podemos utilizar la herramienta `Diferencia simétrica`:
	- En la caja de herramientas de procesos, busque la herramienta "Symmetrical difference" y ábrala.
	- En `Capa de entrada`, seleccione la capa que contenga la información de seguridad.
	- Como `Capa de superposición`, seleccione la capa `AOI_Peshawar.gpkg`.
	- En `Diferencia simétrica`, haga clic en `...` y vaya hasta la carpeta `data/results/`, para este ejercicio, y guarde la capa.
	- Haga clic en `Ejecutar`.


10. Hagamos una simbolización rápida de la capa resultante para que podamos entender la información más fácilmente:
	- Abra el [styling panel](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#styling-panel) para la zona segura.
	- [Ajuste la simbología](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#only-display-the-outlines-of-polygons) para la capa de modo que los polígonos sean __semitransparentes y verdes__.

¡Felicidades! Ahora tenemos un mapa para ayudar al equipo sobre el terreno a mantenerse a salvo.


<!--ADD: Images of the different steps and results.-->

## Tarea 2: Cargar en QGIS un archivo Excel con datos sobre conflictos

:::{card}
__Contexto:__
^^^

En este paso, queremos obtener una visión más amplia de los acontecimientos conflictivos en Pakistán. El proyecto [Armed Conflict Location and Event Data (ACLED)](https://acleddata.com/) distribuye conjuntos de datos sobre acontecimientos conflictivos por país en forma de hojas de cálculo Excel. Los conjuntos de datos incluyen fechas, actores, __ubicación__, víctimas mortales y tipos de acontecimientos conflictivos notificados.

El conjunto de datos también incluye las coordenadas geográficas de cada hecho notificado. En QGIS, podemos transformar la tabla de datos en un conjunto de datos espaciales, como un GeoPackage.
Una vez que tengamos los sucesos conflictivos como datos de punto, podemos agregar los datos a nivel de subdistrito y crear un mapa que muestre los subdistritos (ADM3) más afectados por los conflictos.

:::

1. Arrastre y suelte la tabla Excel del conflicto ACLED `2024-01-01-2024-09-23-Pakistan.xlsx` en su proyecto QGIS.
2. En la caja de herramientas de procesos, busque la herramienta `Crear capa de puntos a partir de tabla` y ábrala.
    - Como `Campo X` seleccione la columna "longitud", y como `Campo Y` seleccione "latitud".
    - En `Puntos a partir de tabla`, haga clic en los tres puntos, seleccione "Guardar en GeoPackage" y vaya a su carpeta temporal. Guarde la capa con el nombre "Pak_Puntos_de_conflicto_2024".
	- Haga clic en `Ejecutar`.


:::{figure} ../../fig/Create_ponts_from_table.PNG
---
width: 700px
name: create_points_from_table
---
Cree puntos a partir de la tabla.
:::

¡Estupendo! Ahora tenemos una capa de puntos que muestra los acontecimientos del conflicto en Pakistán. Ahora, podríamos investigar más a fondo este conjunto de datos echando un vistazo a la [tabla de atributos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_attribute_table.html) y ver qué tipo de información hay. Sin embargo, queremos saber el número de incidentes conflictivos por thesil (subdistrito/ADM3). Para calcularlo:

3. Importe la capa `PAK_KP_admin_3.gpkg` de su carpeta `data/input` a su proyecto QGIS.
4. Queremos contar el número de eventos conflictivos por thesil (subdistrito/ADM3). Para ello:
	- En la caja de herramientas de procesos, busque la herramienta `Contar puntos en un polígono` y ábrala.
	- Como `Polígonos`, seleccione la capa `PAK_KP_admin_3`.
	- Como `Puntos`, seleccione el `PAK_Conflict_points_2024`.
	- En `Numéro`, haga clic en `...` y guarde la capa en su carpeta `data/results/` como "PAK_num_events_adm3".


:::{figure} ../../fig/count_point_polygon.PNG
---
width: 700px
name: es_count_point_polygon
---
Cuente los puntos en el polígono
:::

5. Abra el atributo de su capa "Pak_num_events_adm3" y desplácese hacia la derecha. Encontrará una columna con el nombre "NUMPOINTS". Aquí encontrará el número de eventos por thesil.
    - Haga clic con el botón derecho en la capa y vaya a `Propriedades` → `Simbología`. En la parte superior cambie Símbolo Único por "Graduado".
    	- En el campo `Valor` elija "NUMPOINTS".
	- A continuación, haga clic en `Classify`.
	- Si lo desea, puede ajustar el modo y el número de clases. También puede elegir la rampa de color. Puede probar diferentes opciones de colores.
	- Cuando esté satisfecho con el aspecto, haga clic en `Aplicar` y luego en `Aceptar`.

El resultado podría verse parecido a esto:

:::{figure} ../../fig/Number_events_graduated.PNG
---
width: 700px
name: es_Number_events_graduated
---
Número de eventos conflictivos por thesil (distrito).
:::


## Tarea 3: Datos IPM

:::{card}
__Contexto:__
^^^
En este paso, queremos visualizar el índice de pobreza múltiple a nivel de distrito (ADM2).

Esto puede ayudarnos a comprender geográficamente la vulnerabilidad económica y social. Los datos con el índice IPM están disponibles en una hoja de cálculo Excel. Sin embargo, no contiene columnas con los datos geográficos específicos (como las coordenadas). Tenemos que encontrar la manera de unir la tabla de datos con un conjunto de datos espaciales.

:::


1. En primer lugar, abramos la hoja de cálculo con Microsoft Excel o un programa similar (como LibreOffice Calc):
	- Aquí ya puede investigar la información que se almacena en las distintas columnas. ¿Puede identificar las columnas que contienen información espacial?
	- Por ahora, vamos a exportar el archivo como CSV UTF-8.
		* Haga clic en `Archivo` → `Guardar como...`
		* Elija una carpeta de salida donde guardarlo (se recomienda la carpeta `data` > `temp` ) y asigne al archivo un nombre significativo, por ejemplo __20240605_PAK_MPI__.
		* Elija la opción __CSV UTF-8 (delimitado por comas) (*.csv)__ y `Guardar`.

	:::{figure} /fig/PAK_Excel_to_CSV.png
	---
	width: 400px
	name: es_PAK_Excel_to_CSV
	align: center
	---
	Convierta el Excel a CSV.
	:::

2. Abra QGIS y cree un nuevo proyecto. Guarde el proyecto en su carpeta de proyectos.
3. [Importe las capas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_import_geodata_wiki.html) `__20240605_PAK_MPI.csv__` y `Pak_adm2_Khyber Pakhtunkhwa.gpkg` a QGIS:
	* Arrastre y suelte la capa ADM2 en su ventana QGIS.
	* Para importar el archivo CSV, haga clic en la pestaña `Capa` → `Añadir capa` → `Añadir capa de texto delimitado`.
	* Busque su archivo __20240605_PAK_MPI.csv__.
	* Elija la correcta `Formato de archivo`: `Delimitadores personalizados` → `Punto y coma`.
	* Vaya a	la pestaña `Definición de geometría` y elija `Ninguna geometría (tabla solo de atributos)`. No tenemos una columna con coordenadas o información geométrica, solo tenemos el nombre admin2 y P-Code.
	* Añada la capa y cierre la ventana.

	:::{figure} /fig/PAK_Load_CSVfile.PNG
	---
	width: 400px
	name: es_PAK_Load_CSVfile
	align: center
	---
	Cargue el archivo CSV en QGIS.
	:::

Ahora, tenemos que unir los datos a los límites de distrito existentes (ADM2). Este proceso se denomina [unión no espacial](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_5/es_qgis_spatial_tools.html#spatial-joins) y permite enriquecer los conjuntos de datos mediante datos de atributos. En nuestro caso, el conjunto de datos IPM contiene una columna con los nombres de los distritos (admin2) y los códigos P. Los códigos P son códigos internacionales de límites administrativos y suelen ser la mejor forma de identificar una unidad administrativa, ya que los nombres pueden tener varias grafías. Nuestra capa de polígonos también tiene columnas con los códigos p.

Por lo tanto, tenemos que realizar una unión no espacial utilizando las columnas de códigos P como identificadores. Para ello:

4. Abra la tabla de atributos de la tabla de atributos y detecte la columna que contiene la información que desea utilizar para unir los datos con la ubicación. Por ejemplo: Nombre de la ciudad, del distrito o, mejor, el código P. En nuestro caso es `ADM2_PCODE`.
	* __Una pista__: Cada nivel administrativo y zona contiene un número de código único en el mundo. Esto ayuda a determinar el límite administrativo exacto sin escribir mal el nombre de la zona.
5. Ahora necesitamos la capa de polígonos con los límites administrativos.
	* Abra la tabla de atributos de la capa __Pak_adm2_Khyber Pakhtunkhwa.gpkg__ y localice la columna que contiene el P-Code. ¿Cómo se llama?
6. Para unir las dos capas, abra la caja de herramientas y busque la herramienta __Unir atributos por valor de campo__. Ábralo.
	* `Capa de entrada`: __Pak_adm2_Khyber Pakhtunkhwa.gpkg__
	* `Campo de la tabla`: __admin2Pcode__
	* `Capa de entrada 2`: __20240605_PAK_MPI.csv__
	* `Campo de tabla 2`: __ADM2_PCOCDE__
	* Elija una ubicación para guardar el archivo como GeoPackage y dele un nombre significativo, por ejemplo __MPI_Admin2_joined.gpkg__
	* `Ejecutar` y cierre.

	:::{figure} /fig/PAK_joined_MPI_csv_admin2.PNG
	---
	width: 400px
	name: es_PAK_joined_MPI_csv_admin2
	align: center
	---
	Unir los distritos con los datos del IPM.
	:::
	
	__Info__: Puede notar que no todas las zonas son visibles. Dado que no contamos con datos para todos los distritos, solo se vincularon los distritos que aparecen en el CSV con los datos del IPM.
	
	:::{figure} /fig/PAK_joined_MPI_csv_admin2_info.PNG
	---
	width: 400px
	name: es_PAK_joined_MPI_csv_admin2_info
	align: center
	---
	Información de datos no unidos y enlazados.
	:::

5. Visualice __MPI_Admin2_joined.gpkg__ file: Tenemos un nuevo archivo que muestra los límites de los distritos, pero que contiene la información del IPM en la tabla de atributos. El valor IPM por distrito que ahora queremos visualizar.
	* Abra la ventana `Simbología` del archivo __MPI_Admin2_joined.gpkg__.
	* Decida qué columna quiere visualizar. Por ejemplo, los valores del año 2014 en la columna __A_2014_15__.
	* Seleccione `Graduado` visualización.
	* Seleccione `Valor` __A_2014_15__.
	* Haga clic en `Clasificar`.
	* Seleccione el __modo__ `Pretty Breaks`.
	* Haga clic en `Aceptar` y cierre la ventana.
6. Visualice__Pak_adm2_Khyber Pakhtunkhwa.gpkg__ capa para los distritos de los que no tenemos datos IPM.
	* Abra la ventana `Simbología` del archivo __Pak_adm2_Khyber Pakhtunkhwa.gpkg__.
	* Cambie el color, tal vez a gris oscuro, para que podamos diferenciar los distritos de los que disponemos datos del IPM de los que no.
7. Añada OpenStreetMap como capa base para orientarse mejor.


:::{figure} /fig/PAK_visualized_MPI.PNG
---
width: 400px
name: es_PAK_visualized_MPI
align: center
---
Visualice de los datos del IPM a nivel de distrito.
:::
