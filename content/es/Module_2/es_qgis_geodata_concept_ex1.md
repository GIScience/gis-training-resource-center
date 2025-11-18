::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 1: Comprensión de los datos geográficos

## Características del ejercicio

:::{card}
__Objetivo de este ejercicio:__
^^^

El objetivo de este ejercicio es dar los primeros pasos en QGIS. Comprender la interfaz de usuario y familiarizarse con el concepto de capa. Aprenderá a importar y visualizar datos vectoriales en QGIS y a abrir la tabla de atributos. Además, aprenderemos a reproyectar o cambiar la proyección cartográfica de los conjuntos de datos vectoriales.
:::


::::{grid} 2
:::{grid-item-card}
__Tipo de ejercicio de capacitación:__
^^^

- Este ejercicio puede utilizarse en la capacitación en línea y presencial.
- Puede realizarse como ejercicio guiado o individualmente.

:::

:::{grid-item-card}
__Estas habilidades son relevantes para:__
^^^

- Fundamentos QGIS
- Comprensión de los componentes espaciales de los conjuntos de datos
- Navegación por la interfaz de QGIS
- Gestión y manipulación de datos geográficos
- Realización de análisis espaciales básicos y avanzados


:::
::::

::::{grid} 2
:::{grid-item-card}
__Duración estimada del ejercicio:__
^^^

- El ejercicio dura entre 30 y 60 minutos, dependiendo del número de participantes y de su familiaridad con los sistemas informáticos.

:::

:::{grid-item-card}
__Artículos relevantes en Wiki__
^^^

* [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
* [Importación de datos geoespaciales en QGIS](/content/es/Wiki/es_qgis_import_geodata_wiki.md)
* [Concepto de capa](/content/es/Wiki/es_qgis_layer_concept_wiki.md)
* [Tabla de atributos en QGIS](/content/es/Wiki/es_qgis_attribute_table_wiki.md)
* [Proyecciones cartográficas](/content/es/Wiki/es_qgis_projections_wiki.md)

<!-- FIXME: to be updated -->

:::

::::

## Instrucciones para capacitadores

:::{dropdown} __Rincón del instructor__

### Preparar la capacitación

- Tómese el tiempo necesario para familiarizarse con el ejercicio y el material proporcionado.
- Prepare un pizarrón. Puede ser un pizarrón físico, un rotafolio o un pizarrón digital (p. ej., un pizarrón en Miro) donde los participantes puedan añadir sus resultados y preguntas.
- Antes de comenzar el ejercicio, asegúrese de que todos los participantes hayan instalado QGIS y que hayan descargado __y descomprimido__ la carpeta de datos.
- Consulte [¿Cómo realizar capacitaciones?](/content/es/Trainers_corner/es_how_to_training.md) para obtener algunos consejos generales para impartirlas.

### Impartir la capacitación

__Introducción:__

- Presente la idea y el objetivo del ejercicio.
- Proporcione el enlace de descarga y asegúrese de que todos los participantes han descomprimido la carpeta antes de comenzar las tareas.

__Guía paso a paso:__

- Muestre y explique cada paso al menos dos veces y de manera pausada para que todos puedan ver lo que está haciendo y replicarlo en su propio proyecto de QGIS.
- Pregunte con regularidad si alguien necesita ayuda o si todos están siguiendo el ejercicio para asegurarse de que todos comprenden y realizan los pasos.
- Mantenga una actitud abierta y paciente ante cualquier pregunta o problema que pueda surgir. Esencialmente, los participantes están realizando varias tareas a la vez, prestando atención a sus instrucciones y orientándose en su propio proyecto QGIS.

__Cierre de la sesión:__

- Reserve tiempo para cualquier cuestión o pregunta relacionada con las tareas al final del ejercicio.
- Reserve tiempo para preguntas abiertas.

:::

## Ejercicio
### Datos disponibles

:::{card}
:class-card: sd-text-center
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_1/Module_2_Exercise_1_Understanding_Geodata.zip

__Descargue todos los conjuntos de datos [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_1/Module_2_Exercise_1_Understanding_Geodata.zip) y descomprima la carpeta.__

:::

La carpeta comprimida incluye:

| Nombre del conjunto de datos | Título original | Publicado por | Descargado de |
| :-------------- | :----------------- |:----------------- |:----------------- |
| `sle_admbnda_adm0_adm1_gov_ocha.gpkg` (Polígonos) | Sierra Leona: Límites administrativos subnacionales | Oficina de Coordinación de Asuntos Humanitarios de las Naciones Unidas (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-sle) |
| `sierra_leone_health_HOT.shp` (Puntos) | Instalaciones sanitarias de Sierra Leona (Exportación OpenStreetMap) | Equipo Humanitario de OpenStreetMap (HOT) | [HDX](https://data.humdata.org/dataset/hotosm_sle_health_facilities) |
| `sl-airports.csv` (CSV) | Aeropuertos en Sierra Leona | Nuestros aeropuertos | [HDX](https://data.humdata.org/dataset/ourairports-sle) |


El GeoPackage `Sierra_leone_administrative_boundaries.gpkg` contiene información administrativa de Sierra Leona tanto a nivel nacional como provincial. Además, shapefile `sierra_leone_health_HOT.shp` proporciona información sobre diversas instalaciones sanitarias dentro del país, mientras que el archivo CSV `sl-airports.csv` ofrece información sobre aeropuertos.

:::{admonition} Estructura de las carpetas
:type: hint

Mantenga la gestión de sus datos organizada creando una [estructura de carpetas estándar]() en su ordenador para sus proyectos QGIS y datos geográficos.
Los datos del ejercicio deben guardarse en un lugar donde pueda encontrarlos fácilmente, así como el proyecto QGIS correspondiente

:::

### Tareas

1. Abra los archivos que ha descargado en QGIS.
   - __Descomprima la carpeta__ con los datos del ejercicio.
   - El GeoPackage (`.gpkg`) y el shapefile (`.shp`) pueden arrastrarse y soltarse sobre el lienzo del mapa en QGIS.
   - El archivo .csv debe importarse a través del menú de capas.
      - Navegue hasta `Layer`> `Add Layer` > `Add delimited text layer`. Se abrirá una nueva ventana. Aquí puede seleccionar el archivo que desea importar haciendo clic en `...` a la derecha del campo __Nombre de archivo__ situado en la parte superior.
      - Navegue hasta la carpeta con los archivos de ejercicios y seleccione `sl-airports.csv`.
      - Haga clic en abrir. La ventana de importación CSV se actualizará y le mostrará una vista previa de la tabla CSV.
      - La tabla contiene información geográfica. Tendremos que especificar esto en __"Definición de geometría"__.
         - Haga clic en `Point Coordinates` y seleccione `longitude_deg` como su __"campo X"__ y `latitude_deg` como su __"campo Y"__.
      - Haz clic en Agregar. Debería aparecer una nueva capa de puntos con los aeropuertos en el lienzo del mapa.


:::{figure} /fig/en_3.36_add_csv.png
---
width: 500 px
name: navigation to add csv layer
---
Abrir la ventana de importación de CSV.
:::


:::{figure} /fig/en_delimited_text_screenshot.PNG
---
width: 80%
name: delimited_text
---
Captura de pantalla del Administrador de fuentes de datos - Texto delimitado para cargar un archivo CSV
:::

2. Interactúe con el mapa y explore los conjuntos de datos. Utilice la herramienta de zoom y desplácese
   por el mapa. Concéntrese en la ventana de escala y observe cómo varía al acercar y alejar la imagen.

3. Familiarícese con el panel de capas (lista de capas). Muestre y oculte
   diferentes capas y mueva las capas alrededor de la estructura. Asigne un nombre significativo a la capa de datos.

:::{Note}
Cambiar el nombre de la capa no afecta a la fuente de datos, como los nombres de archivo o la
ubicación de almacenamiento.
:::

4. Compruebe los datos de los atributos de las capas examinando la tabla de atributos.

5. Cambie la proyección cartográfica en la vista del mapa a `WGS 84 / Pseudo-Mercator EPSG:3857`. Puede hacerlo en la esquina inferior derecha de la ventana de QGIS.

:::{Note}
Esto no cambia la proyección cartográfica (coordenadas) de los archivos, sólo la proyección
de la vista del mapa. Compruébelo con una consulta sobre las propiedades de la capa de puntos
. ¿Qué proyección cartográfica se muestra allí?
:::

:::{Hint}
Para obtener información sobre una capa y sus proyecciones cartográficas, haga doble clic sobre la capa y busque la sección `Information`. Esta sección contiene detalles generales como el nombre y la ruta del archivo, así como información sobre el Sistema de Referencia de Coordenadas (SRC) en la sección correspondiente.
:::


6. Guarde la capa del centro de salud en la proyección cartográfica `WGS 84 / Pseudo-Mercator EPSG:3857`. Esto cambiará la proyección cartográfica del archivo. Para ello, haga clic con el botón derecho en la capa --> `Export` --> `Save Features As..`. En la ventana emergente, seleccione **GeoPackage como formato de archivo de salida** y **especifique la ubicación del archivo y el nombre** haciendo clic en los tres puntos pequeños. También se le puede dar al archivo un nombre de capa, que se mostrará cuando se cargue en QGIS. Antes de ejecutar este proceso, **se puede cambiar la proyección** seleccionando el SRC deseado en la sección designada. Verifique la proyección modificada observando las propiedades de la capa recién creada.

:::{figure} /fig/en_ex1_export_layer.PNG
---
width: 40%
name: export_layer
---
Captura de pantalla de la ventana Exportar
:::

7. Guarde su proyecto.

8. Opcional: Puede añadir el mapa base de OpenStreetMap a través de la ventana del navegador,
   en `XYZ Tiles`.

:::{Note}

La combinación de capas en diferentes proyecciones cartográficas con mapas base en línea (que suelen tener sus propias proyecciones) puede dar lugar a problemas de visualización debido a los [conflictos del SRC](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_2/es_qgis_projections.html#how-to-choose-an-appropriate-projected-coordinate-system). Cuando las capas tienen un SRC distinto, podrían no alinearse correctamente o aparecer distorsionadas al superponerlas con un mapa base en línea. Para mitigar estos problemas, es aconsejable reproyectar las capas para que coincidan con SRC del mapa base (lo que a menudo no es aplicable) o eliminar temporalmente el mapa base antes de guardar el proyecto. Esto garantiza que el mapa se muestre con precisión y evita posibles discrepancias visuales causadas por incoherencias del SRC.

:::


:::{figure} /fig/en_result_geodata_concept_exercise.png
---
width: 80%
name: en_result_geodata_concept_exercise
---
Este es el aspecto que podría tener el resultado final.
:::