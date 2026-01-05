::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Ejercicio 1: Comprensión de la interfaz de QGIS

## El objetivo del ejercicio

QGIS es un programa complejo con muchas funciones y la interfaz puede resultar confusa, sobre todo para los principiantes. Este ejercicio le permitirá familiarizarse con las principales barras de herramientas, ventanas y paneles de QGIS. Creará un nuevo proyecto de QGIS y lo guardará y navegará por los diferentes paneles y barras de herramientas.

El ejercicio abarca:

- Guardar y cargar un proyecto de QGIS.
- Encontrar y utilizar las distintas barras de herramientas.
- Encontrar y utilizar diferentes paneles.
- Desplazamiento de paneles.
- Activación de nuevos paneles.


## Artículos relacionados de Wiki.

- [Interfaz de QGIS](/content/es/Wiki/es_qgis_interface_wiki.md)
- [Proyectos y estructura de carpetas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html)


## Preparación de datos

En este ejercicio no utilizaremos datos geoespaciales. En su lugar, aprenderemos a navegar por las diferentes interfaces y a guardar y cargar un proyecto de QGIS. Puede descargar la estructura de carpetas modelo en un formato comprimido [aquí](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_1/Modul_1_Exercise_1_Understanding_the_interface/Modul_1_Exercise_1_Understanding_the_interface.zip).

:::{figure} /fig/standard_folder_structure_new_2025.drawio.png
---
width: 800px
align: center
name: Standard folder structure
---
Estructura de carpetas estándar. Fuente: HeiGIT
:::
---

## Tareas

1. Crear un nuevo proyecto. Al abrir QGIS, aparecerá la capa de inicio, que muestra la interfaz de QGIS sin ningún proyecto cargado. A la izquierda habrá un panel con los proyectos recientes (probablemente estará vacío). A la derecha habrá un panel de noticias, con publicaciones del blog de QGIS y debajo de este se encuentra un panel `Project Templates`.

:::{figure} /fig/en_project_template_BRC.png
---
height: 400
name: Project Template
align: Left
---
:::

- En el panel `Plantillas de proyectos`, __haga doble clic en la opción `Proyecto nuevo vacío`__ (debe ser la única plantilla visible). Verá un lienzo en blanco en la interfaz principal, ya que aún no hay datos cargados.

2. Conozca la interfaz de QGIS: Sobre el lienzo encontrará la __barra de herramientas__ con muchas funciones diferentes. A izquierda y a la derecha del lienzo, se encuentran los paneles. En QGIS, por lo general, accederá a la herramientas en las __barras de herramientas__ o en los __paneles__.

- Por defecto, las barras de herramientas están en la parte superior de la pantalla. Incluyen los controles, que le permiten cambiar entre distintas formas de interactuar con la interfaz.
- Por defecto, los paneles están a los lados de la pantalla. Incluyen el explorador de archivos y los paneles de navegación, por capas, situados a la izquierda de la pantalla. Se pueden activar otros paneles para buscar y utilizar herramientas de procesamiento. En el panel de capas, verá los datos, que añadiremos más adelante.
A la derecha de la pantalla, lo más probable es que tenga el panel __Caja de herramientas de procesos__. Si no lo encuentra, consulte la [página Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#missing-toolbox).

:::{figure} /fig/en_QGIS_GUI.png
---
width: 800px
align: center
name: es_QGIS_GUI
---
Interfaz de usuario de QGIS.
:::

3. Puede desacoplar los paneles de su ubicación, haciendo clic y arrastrando el título del panel. Puede anclarlo a otro panel (aparecerá como otra pestaña) o convertirlo en una ventana independiente. También puede cambiar el tamaño de los paneles. Inténtelo moviendo el panel de las capas hacia la derecha ([video del Wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_interface_wiki.html#move-and-arrange-toolbars)).

:::{tip}

En QGIS, la interfaz podría aparecer ligeramente diferente dependiendo de la resolución de su pantalla. Ocasionalmente, algunos elementos pueden quedar ocultos debido a la configuración de renderizado por defecto. Si se encuentra con esta situación, pruebe cambiar el tamaño de los paneles y explorar las distintas opciones y funciones que ofrecen. Esto puede ayudar a garantizar que todas las herramientas y las entidades geográficas estén fácilmente accesibles durante el flujo de trabajo.

:::

4. QGIS tiene otros paneles que puede utilizar y que no se muestran por defecto. Veamos cómo podemos encontrar y activar los demás paneles y barras de herramientas.
- En el menú `Ver`, busque las opciones `Paneles` y `Barras de herramientas`. Al pasar el puntero sobre cada elemento, verá una lista de los paneles y barras de herramientas disponibles, así como cuáles están activados. Tómese un minuto para explorar las distintas barras de herramientas y paneles. Hay muchas opciones, pero no se preocupe, no utilizará la mayoría de ellas, en esta capacitación. Los paneles que más utilizaremos son:
- Navegador
- Capas
- Estilo de capa
- Caja de herramientas de procesos

5. Ahora, veamos las barras de herramientas. Las barras de herramientas que más utilizaremos son:
- Barra de herramientas de atributos
- Barra de herramientas de digitalización
- Barra de herramientas de navegación del mapa
- Barra de herramientas del proyecto
- Barra de herramientas de selección


Tómese un momento para familiarizarse con las distintas formas de organizar la interfaz de QGIS. ¡Saber dónde encontrar las distintas funciones puede ahorrarle mucho tiempo y frustraciones en el futuro!

6. Ahora guardemos el proyecto. Haga clic en el icono de guardar de la barra de herramientas o abra el menú `Proyecto` y elija `Guardar como...`
    1. Elija una ubicación para el archivo del proyecto. Un lugar ideal sería en la subcarpeta del proyecto en la estructura de carpetas modelo. Vaya a la carpeta llamada `Modulo_1_Ejercicio_1`. Asigne un nombre al proyecto de QGIS (por ejemplo: `QGIS_Training_Exercise_1`). El proyecto se guardará como un archivo `.qqz`.
    2. Haga clic en `Save`
    3. Cierre la aplicación QGIS y vuelva a abrirla.
7.  Cierre la aplicación QGIS y vuelva a abrirla. Cuando QGIS se reinicie, el proyecto que acabamos de guardar aparecerá en el panel `Proyectos recientes`. Puede hacer doble clic para abrirlo. También puede navegar hasta el archivo `.qgz` en su explorador de archivos y hacer doble clic sobre él.
Esto también iniciará QGIS y cargará el proyecto.

:::{Tip}

Mantener organizada su estructura de carpetas, le ayudará mucho a trabajar de forma eficaz y sin frustraciones.

:::

:::{Warning}

__Recuerde__: Los archivos de proyecto en QGIS se guardan por separado de los datos,que está utilizando en el proyecto, por lo que es aconsejable mantener todos los
archivos relacionados con un proyecto en una carpeta.

:::


