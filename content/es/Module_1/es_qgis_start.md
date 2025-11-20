::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Primeros pasos con QGIS

## Presentación de QGIS

:::{figure} /fig/en_qgis_banner_website.png
---
name: en_qgis_banner_website
width: 300 px
align: right
---
[qgis.org](https://qgis.org/)
:::

:::{div} sd-text-justify
- QGIS es un __software de código abierto del sistema de información geográfica__. Eso significa que el código fuente está disponible para todas las personas,
lo que hace que QGIS sea una aplicación gratuita. El código fuente completo puede consultarse y descargarse en https://github.com/qgis/QGIS.
- QGIS es un __software de escritorio__: eso significa que usted obtiene un programa, que se abre en su computadora, como una ventana con botones
en los que puede hacer clic, formularios que puede llenar para realizar tareas y en general, una experiencia interactiva visual.
- Puede __ver, editar, capturar y analizar datos geoespaciales o crear mapas imprimibles__ con ellos. QGIS fue creado en 2002
y es un proyecto impulsado por voluntarios. Y está en __constante cambio__.
- QGIS está respaldado por una __gran comunidad de usuarios__, por lo que es fácil encontrar soluciones a problemas técnicos mediante el uso de los foros, los blogs o sub-reddits de QGIS. La comunidad oficial de QGIS se encuentra [aquí](https://qgis.org/en/site/forusers/support.html#support). Además, puede encontrar una lista de sitios web útiles en la [Wiki aquí](/content/es/Wiki/es_qgis_common_errors_and_Issues.md).
:::


:::{note}

Tenga en cuenta que a medida que QGIS sigue desarrollándose, la interfaz y las funciones del programa estarán sujetos a cambios. El material escrito para esta plataforma de capacitación se refiere a la versión 3.36 de QGIS. Si el material de capacitación ya no está actualizado, eche un vistazo a la [Documentación de QGIS](https://docs.qgis.org/3.34/en/docs/index.html).

:::

:::{attention}

QGIS evoluciona constantemente y se añaden nuevas entidades. Por ello, las versiones más recientes pueden presentar cambios o incluso errores (como fallos). Sin embargo, siempre hay una versión estable disponible, que recibe soporte durante más tiempo. Esta versión se denomina __Long-term release (LTR)__.

:::


## Trabajar con QGIS


En QGIS, puede crear proyectos donde puede visualizar y manipular datos geoespaciales. Existen tres flujos de trabajo principales: __recopilación y creación de datos, procesamiento de datos y visualización de datos__. Los datos geoespaciales se cargan en proyectos QGIS, que se representarán como capas en un lienzo del mapa.

:::{hint}

En los SIG intervienen muchos algoritmos complejos, pero QGIS se encarga de ellos por sí solo y no es necesario tener un profundo conocimiento de las matemáticas y los algoritmos para utilizar QGIS. __Siempre que sepa utilizar Excel y Powerpoint, no debería tener problemas para aprender a utilizar QGIS__.

:::

::::{tab-set}

:::{tab-item} Recopilación y creación de datos

QGIS ofrece herramientas para crear sus propios datos geoespaciales. Por ejemplo, con las herramientas de digitalización se pueden crear puntos, polígonos y líneas con información, que puede representar información espacial. Además, la georreferenciación permite añadir información geográfica a diversos tipos de datos, como imágenes satelitales o mapas dibujados a mano. Aprenderá a crear datos geoespaciales y a georreferenciar datos en el __[módulo 2](/content/es/Module_2/es_module_2_overview.md)__.

A veces, trabajar con SIG requiere salir al campo para recopilar los datos. En este caso, puede utilizar [aplicaciones web y móviles](/content/es/Wiki/es_web_and_mobile_apps_wiki.md).

:::

:::{tab-item} Procesamiento de datos

QGIS ofrece una amplia gama de algoritmos para procesar datos geoespaciales. En los siguientes módulos, conocerá una serie de algoritmos especialmente útiles para los SIG en el trabajo humanitario. Aprenderá más sobre procesamiento y manipulación de datos a partir del [módulo 2](https://giscience.github.io/gis-training-resource-center/content/es/Module_2/es_module_2_overview.html).


:::

:::{tab-item} Visualización

QGIS permite visualizar datos geoespaciales y crear mapas para comunicar información. Para ello, asigna símbolos y colores a los distintos elementos de sus datos geoespaciales. Asignar una simbología a los datos geoespaciales es una de las principales habilidades que desarrollará como usuario del SIG y una buena visualización de los datos, es inmensamente útil a la hora de comunicar ideas. Aprenderá a asignar símbolos en el [Módulo 4: Visualización de datos geoespaciales y elaboración de mapas](/content/es/Module_4/es_qgis_map_design_I.md)


:::
::::




:::{card}
__Nota sobre los complementos__
^^^

Además de los algoritmos incluidos en la instalación estándar, QGIS ofrece complementos que añaden funciones adicionales a la aplicación QGIS. Estos complementos son desarrollados por organizaciones independientes o por la comunidad QGIS. Por ejemplo, los complementos le permiten conectarse a servicios en línea como OpenStreetMap o añadir más algoritmos para procesar sus datos. Pueden ser muy útiles para determinados casos de uso. También hay complementos diseñados específicamente para el trabajo humanitario. Aprenderá más sobre los complementos en los siguientes módulos. Si quiere saber cómo instalarlos, consulte la [Wiki](/content/es/Wiki/es_qgis_plugins_wiki.md).

:::

## Abrir un nuevo proyecto en QGIS

Abra QGIS como cualquier otro programa en su computadora. La pantalla de inicio de QGIS suele mostrarle los proyectos, en los que ha trabajado recientemente y la opción de crear un nuevo proyecto.

Existen __dos__ opciones para crear un nuevo proyecto:

::::{margin}
:::{tip}

Un archivo de proyecto de QGIS tiene un formato con la extensión `.qgz`.

:::

::::
1. En la pantalla de inicio, haga clic en `Project Template`

:::{figure} /fig/en_project_template_BRC.png
---
height: 400
name: en_project_template_BRC
align: center
---
:::

2. En la esquina superior izquierda, haga clic en `Project` -> ` New Project `

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>



## Visión general de la interfaz de QGIS

A primera vista, la interfaz de QGIS es bastante compleja. Sin embargo, una vez que conozca todos los componentes podrá orientarse rápidamente. Aquí encontrará una descripción de todos los componentes de la interfaz.

::::{margin}
:::{tip}

Cuando pase el puntero sobre los iconos, aparecerá un texto que explica la función del botón.

:::
::::

:::{figure} /fig/en_QGIS_GUI.png
---
width: 800px
align: center
name: en_QGIS_GUI
---
Interfaz de usuario de QGIS. Fuente: Cruz Roja Británica (BRC)
:::

1. __Panel de capas:__ La __lista de capas__ muestra __todas las capas/archivos__ que están __cargados en el proyecto__. Puede mostrar/ocultar capas y establecer otras propiedades.

2. __Barras de herramientas:__  Las __barras de herramientas__ son atajos para ejecutar comandos de uso frecuente. Por ejemplo, hay barras de herramientas especiales para __archivos vectoriales y archivos ráster__, pero también, otras generales para guardar el proyecto, etc. La barra de herramientas contiene, entre otras cosas, una lista de todos los comandos, que puedes utilizar. La barra de herramientas también contiene la __caja de herramientas de procesos__, que se utiliza, más adelante, en muchos de los videos de la Wiki.

:::{figure} /fig/en_Interface_02.png
---
height: 75 px
name: en_Interface_02
align: center
---
:::

3. __Lienzo del mapa:__ El __lienzo del mapa__ es el __componente central__ de todo programa del sistema de información geográfica (SIG). Aquí se muestran los __datos geoespaciales__. La vista del mapa tiene una proyección cartográfica, que no siempre tiene por qué coincidir con la proyección cartográfica de las capas.

4.  __Coordenadas y escala:__ Aquí puede encontrar información sobre la escala del lienzo del mapa, así como también, leer las coordenadas del puntero.

5. __Panel del navegador:__ El panel del navegador le permite explorar los archivos de su computadora y cargar conjuntos de datos en su proyecto de QGIS.

6. __Barra de búsqueda:__ Aquí puede __buscar herramientas y capas__ en QGIS. Si no sabe dónde encontrar una herramienta, puede intentarlo aquí. También puede escribir las coordenadas para encontrarlas en el lienzo del mapa.

:::{dropdown} Ejercicio: Crear un nuevo proyecto en QGIS

1. En su carpeta “Capacitación_SIG”, cree una __subcarpeta__ llamada “Mi_Primer_Proyecto”.
2. Abrir __QGIS__
3. Haga clic en `Project` -> ` New Project `
4. En la esquina superior izquierda, haga clic en `Project` -> `Save as`, vaya a la carpeta de sus proyectos y guarde el proyecto como “Sesión 1”
5. Haga clic en __guardar como__, vaya a la carpeta Proyectos y guarde el proyecto como “Mi_primer_proyecto”
6. Abra su carpeta y compruebe el __archivo .qgz__ que acaba de crear.

:::

:::{attention}

Si ve un `*` en la barra de título, a la izquierda del nombre de su proyecto, significa que el proyecto tiene cambios __sin guardar__. Dado que QGIS puede bloquearse, de vez en cuando, asegúrese de guardar su proyecto periódicamente, para evitar perder el progreso.

:::

## Botones y atajos

En QGIS el __control del mouse__ le permite a los usuarios interactuar con el lienzo del mapa y habilita funciones como el desplazamiento, el zoom y la selección de entidades geográficas.

__Atajos de teclado__ en la interfaz de QGIS ofrecen accesos rápidos a diversos comandos, lo que mejora la eficiencia y acelera el flujo de trabajo. A continuación, encontrará todos los atajos de teclado.

:::{dropdown} Navegación en la vista del mapa

| Nombre | Opción del menú | Atajo | Descripción |
|---------------------------|--------------------------------|---------------------------------|---------------------------------------------|
| Desplazar el mapa | ![](/fig/qgis_pan_map.png) | <kbd>Barra espaciadora</kbd>, <kbd>Re Pág</kbd>, <kbd>Av Pág</kbd> o las <kbd>teclas de flecha</kbd> | Mover el mapa |
| Desplazar mapa a la selección | ![](/fig/qgis_pan_map_selection.png) |                                  | Desplazar el mapa hacia el elemento seleccionado |
| Acercar zoom | ![](/fig/qgis_zoom_in.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>+</kbd> o <kbd>rueda del mouse</kbd> | Acercar el mapa |
| Alejar zoom | ![](/fig/qgis_zoom_out.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>-</kbd> o <kbd>rueda del mouse</kbd> | Aleja zoom del mapa |
| Zoom completo | ![](/fig/qgis_zoom_full.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd> | Zoom al elemento seleccionado |
| Zoom a la selección | ![](/fig/qgis_zoom_to_selection.png) | <kbd>Ctrl</kbd> + <kbd>L</kbd> | Zoom al elemento seleccionado |
| Zoom a la capa | ![](/fig/qgis_zoom_to_layer.png) |                                  | Zoom a la capa seleccionada |
| Zoom a la resolución nativa | ![](/fig/qgis_zoom_native_resolution.png) |                             | Zoom a la resolución nativa (100%) |
| Zoom último | ![](/fig/qgis_zoom_last.png) |                                 | Zoom al último zoom |
| Zoom siguiente | ![](/fig/qgis_zoom_next.png) |                                 | Zoom al siguiente Zoom |

:::

:::{dropdown} Gestión de proyectos

| Nombre | Opción del menú | Atajo | Descripción |
|-----------------|------------------------------------|------------------|-----------------------------------------|
| Nuevo proyecto | ![](/fig/qgis_new.png) | <kbd>Ctrl</kbd> + <kbd>N</kbd> | Crear un nuevo proyecto |
| Abrir Proyecto | ![](/fig/qgis_open_project.png) | <kbd>Ctrl</kbd> + <kbd>A</kbd> | Abrir un proyecto existente |
| Guardar | ![](/fig/qgis_save_project.png) | <kbd>Ctrl</kbd> + <kbd>G</kbd> | Guardar proyecto |
| Guardar como… | ![](/fig/qgis_save_project_as.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> | Guardar proyecto como… |
| Propiedades |                                    | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> | Abrir las propiedades del proyecto |
| Nueva composición de impresión | ![](/fig/qgis_new_print_layerout.png) | <kbd>Ctrl</kbd> + <kbd>P</kbd> | Abrir el diálogo para crear una nueva composición de impresión |
| Buscar |                                    | <kbd>Ctrl</kbd> + <kbd>K</kbd> | Abrir la barra de búsqueda |

:::

:::{dropdown} Gestión de capas

| Nombre | Opción del menú | Atajo | Descripción |
|-----------------------------|----------------------------------------------|----------------------|-----------------------------------|
| Administrador de fuentes de datos | ![](/fig/qgis_data_source_manager.png) |                      | Añadir una nueva capa |
| Nueva capa GeoPackage | ![](/fig/qgis_new_geopackage_layer.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> | Añadir una nueva capa GeoPackage |
| Añadir capa vectorial | ![](/fig/qgis_add_vector_layer.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Añadir una nueva capa vectorial |
| Añadir capa ráster | ![](/fig/qgis_add_raster_layer.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> | Añadir una nueva capa ráster |
| Eliminar la capa seleccionada | ![](/fig/qgis_remove_selected_layer.png) | <kbd>Ctrl</kbd> + <kbd>E</kbd> | Eliminar la capa seleccionada |
| Alternar la vista de las capas |                                              | <kbd>Ctrl</kbd> + <kbd>1</kbd> | Alternar la vista de las capas |
| Alternar la vista del navegador |                                              | <kbd>Ctrl</kbd> + <kbd>2</kbd> | Alternar la vista del navegador |

:::

:::{dropdown} Herramientas de análisis

| Nombre | Opción del menú | Atajo | Descripción |
|------------------------------------------|---------------------------------------------|-----------------------------|--------------------------------------------------------|
| Identificar entidades geográficas | ![](/fig/qgis_identify_features.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> | Identificar entidades geográficas en la vista de mapa, mediante un clic sobre ellas |
| Seleccionar la entidad geográfica | ![](/fig/qgis_select_features.png) |  | Seleccionar una entidad geográfica por área o con un solo clic |
| Seleccionar entidad geográfica por valor | ![](/fig/qgis_select_features_by_value.png) | <kbd>F3</kbd> | Seleccionar entidades geográficas por valor |
| Abrir tabla de atributos | ![](/fig/qgis_open_attribute_table.png) | <kbd>F6</kbd> | Abrir la tabla de atributos |
| Abrir tabla de atributos (objetos seleccionados) | ![](/fig/qgis_open_attribute_table.png) | <kbd>Shift</kbd> + `F6` | Abrir tabla de atributos (objetos seleccionados) |
| Abrir tabla de atributos (objetos visibles) | ![](/fig/qgis_open_attribute_table.png) | <kbd>Ctrl</kbd> + `F6` | Abrir la tabla de atributos solo con las entidades geográficas visibles |

:::

:::{dropdown} Herramientas avanzadas

| Nombre | Opción del menú | Atajo | Descripción |
|-------------------------|----------------------------------------|--------------------|------------------------------|
| Caja de herramientas de procesos | ![](/fig/qgis_processing_toolbox.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> | Abrir la caja de herramientas de procesos |
| Consola de Python | ![](/fig/qgis_python_console.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>P</kbd> | Abrir la Consola de Python |

:::

## Navegar en el lienzo del mapa

::::{admonition} *Opcional*: ¡Ahora, es su turno!

Puede seguir los siguientes pasos en su propio proyecto de QGIS. Descargue [este conjunto de datos](https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg) y arrastre y suelte el archivo `wb_countries_admin0_10m.gpkg` en el lienzo del mapa. El conjunto de datos corresponde a las limites administrativos oficiales de cada país [Banco Mundial](https://datacatalog.worldbank.org/search/dataset/0038272/World-Bank-Official-Boundaries).

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg

Descargar los límites administrativos oficiales del Banco Mundial

:::

::::

### Mover la vista del mapa

::::{margin}

:::{tip}

Si mantiene presionada la <kbd>barra espaciadora</kbd> en su teclado, se activa la herramienta ![](/fig/qgis_pan_map.png) `Pan Map`, cuando se sitúa el puntero sobre el lienzo del mapa. Solo tiene que mover el puntero mientras mantiene presionada la <kbd>barra espaciadora</kbd> y podrá mover la vista del mapa.

:::

::::

Para moverse por el lienzo del mapa con el puntero, tiene que activar el botón de la mano.

:::{image} /fig/qgis_move_symbol.png
---
name: qgis_move_symbol
height: 40 px
---
:::

Siempre puede moverse por el lienzo del mapa con las flechas del teclado.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

### Hacer zoom en la vista del mapa

::::{margin}

:::{tip}
Al mantener presionada la tecla <kbd>Ctrl</kbd> mientras usa la rueda del mouse, podrá desplazarse en incrementos más pequeños (más lento). Pruebe ajustar el lienzo del mapa de acuerdo a sus necesidades con este método.
:::

::::

La forma más sencilla de hacer zoom en el lienzo del mapa es __desplazándose__.

O con los atajos de teclado <kbd>Ctrl</kbd> + <kbd>+</kbd> y <kbd>Ctrl</kbd> + <kbd>-</kbd>

![](/fig/qgis_zoom_symbol.png)

Otra forma es utilizar los botones de zoom del panel de la caja de herramientas.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

## Caja de herramientas y barras de herramientas

Básicamente, todas las funciones, herramientas y aplicaciones de QGIS están organizadas en la caja de herramientas. Algunas herramientas tienen sus propias barras de herramientas que puede añadir a su interfaz de QGIS.

### Abrir la caja de herramientas

::::{margin}
:::{tip}

Mantener presionado <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> abre y cierra la caja de herramientas.

:::
::::

Para abrir la caja de herramientas en QGIS, haga clic en la rueda de desplazamiento. O haga clic en `Processing` -> `Toolbox`

![](/fig/Geschlossene_Toolbox_01.png)

Puede utilizar la barra de búsqueda para encontrar herramientas específicas.

:::{tip}

Hay casos en los que quiere hacer algo en QGIS, pero no conoce la herramienta exacta. A veces, vale la pena simplemente buscar lo que crea que pudiera ser el nombre de la herramienta.

:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

### Mostrar y ocultar pantallas y barras de herramientas

Hay barras de herramientas y paneles para muchas tareas diferentes. Para evitar una interfaz abarrotada, lo más inteligente, es activar las barras de herramientas o los paneles específicos, solo cuando realmente los necesite.

Para añadir o eliminar barras de herramientas de su interfaz, haga clic en `View` -> `Toolbars` -> Marque o desmarque las cajas de herramientas, que desee añadir o eliminar.

Para añadir o eliminar paneles de su interfaz, haga clic en `View` -> `Panels` -> Marque o desmarque los paneles, que desee añadir o eliminar.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video>

### Mover y organizar las barras de herramientas

En cada barra de herramientas, hay un campo de dos líneas punteadas. Si mueve el puntero del mouse sobre ella, hasta que aparezca cruz de flechas y mantiene presionado el botón izquierdo del mouse, puede mover la barra de herramientas. Esto permite una disposición individualizada de sus propias herramientas. Al comprimir todas las barras de herramientas en unas pocas líneas, también se puede ampliar la ventana de la vista del mapa.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

___

## Guardar y abrir proyectos de QGIS

Guardar el progreso o abrir un proyecto existente en QGIS es muy similar a programas como MS Word. Sin embargo, hay una __GRAN__ diferencia.
En QGIS, los datos geoespaciales con los que trabaja __no__ se guardan en el archivo de su proyecto de QGIS. En su lugar, el archivo del proyecto solo contiene las rutas de los archivos, donde se encontraban los datos geoespaciales, en el momento, en que se guardó el proyecto, por última vez, en la computadora. Si posteriormente, se cambia la ubicación de estos datos geoespaciales, aparecerá el mensaje de error “controlar capas no disponibles” al abrir nuevamente el proyecto.

Una buena organización de los datos con una estructura de carpetas fija y bien elaborada, evita tales problemas.

:::{Warning}
¡Siempre organice sus datos! Consulte el artículo de la Wiki sobre la [estructura de carpetas estándar](/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md) para obtener más información.
:::


### Proyectos abiertos

::::{margin}

:::{tip}
Mantener presionado <kbd>Ctrl</kbd> + <kbd>A</kbd> también abre el`Open Project` cuadro de diálogo.

:::

::::

Para abrir un proyecto de QGIS existente, haga clic en `Project` -> `Open…` -> Navegue hasta su proyecto y ábralo.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

### Guardar proyectos

::::{margin}

:::{tip}
Al presionar <kbd>Ctrl</kbd> + <kbd>G</kbd> se guarda el proyecto, mientras que al presionar <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd>, le permite especificar una ubicación de guardado en su computadora.

:::

::::

* __Guardar por primera vez__: Para guardar el proyecto de QGIS en el que está trabajando, haga clic en `Project` -> `Save as…`-> Navegue hasta la carpeta, donde quiere guardar el proyecto -> Nombre el proyecto -> `Save`
* __Cuándo guardar su progreso__: Para guardar el progreso en un proyecto, que ya estaba guardado en algún lugar de computadora:
    * Haga clic en `Project` -> `Save`.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>


## Iconos de advertencia

Puede ocurrir que, mientras trabaja con QGIS, se encuentre con iconos de advertencia de color naranja. Esto indica que debe prestar atención. Para entender lo que significa el icono de advertencia, __coloque el puntero sobre el icono__ y aparecerá un texto explicativo. Por ejemplo, en la {numref}`warning_icon_example`, el icono de advertencia indica que las unidades de medida son grados, que no son constantes (la distancia entre 1⁰ de longitud es mucho mayor en el ecuador que en los polos).

:::{figure} /fig/en_3.36_warning_icon_example.png
---
name: warning_icon_example
width: 700 px
---
Ejemplo de icono de advertencia al ajustar los parámetros de una herramienta de procesamiento.
:::

## Dónde encontrar ayuda

:::{admonition} ¡Conéctese con nosotros!
:class: tip
Si tiene más preguntas antes o después de la capacitación o necesita ayuda, no dude en ponerse en contacto con nosotros con un correo electrónico a `gis-training-platform@heigit.org`.
:::

:::{admonition} Errores y problemas comunes
:class: tip
Hemos recopilado una lista de __[Errores y problemas comunes](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_common_errors_and_Issues.html)__. Si alguna vez, no sabe qué hacer (¡Lo que puede ocurrir a menudo al trabajar con QGIS!), intente buscar la solución a su problema aquí.
:::


También hay una gran comunidad dinámica de QGIS en línea. Si tiene problemas con una función específica o tiene preguntas sobre cómo realizar operaciones en el SIG que no están cubiertas en esta plataforma de capacitación, puede encontrar ayuda en los foros dedicados a QGIS:

- Documentación sobre QGIS: https://docs.qgis.org/3.34/en/docs/index.html
- Foro de usuarios de QGIS en stackexchange: https://gis.stackexchange.com/?tags=qgis
- Grupos de usuarios de QGIS: https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups
- Canal de Telegram de QGIS: https://t.me/joinchat/Aq2V5RPoxYYhXqUPoxRWPQ


Además, existe una gran cantidad de tutoriales en YouTube, guías en línea y material didáctico sobre
operaciones especificas del SIG, por lo que siempre es una buena idea hacer una búsqueda rápida en Google. Entre otros, la [documentación de QGIS](https://docs.qgis.org/3.34/en/docs/index.html) también ofrece ejercicios y material de capacitación, así como una [Introducción fácil a QGIS](https://docs.qgis.org/3.34/en/docs/gentle_gis_introduction/index.html).


## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

Tómese un momento para resumir lo que ha aprendido en este capítulo, con las respuestas a las preguntas, a continuación:

1. __¿Qué es QGIS y qué significa que sea de “código abierto”?__

:::{dropdown} Respuesta
QGIS es un software de SIG que permite a los usuarios ver, editar, analizar y producir mapas a partir de datos espaciales (geográficos) y de atributos.
El ser de código abierto significa que su código fuente está disponible libremente: cualquiera puede inspeccionarlo, modificarlo y distribuirlo (bajo licencia). También implica que existe una comunidad de usuarios y desarrolladores, que contribuyen a él y que el software está generalmente disponible, sin costo alguno.
:::

2. __Nombre tres cosas que puede hacer al trabajar con QGIS.__

:::{dropdown} Respuesta

- Cargar datos geoespaciales (vectoriales o ráster), visualizarlos en un mapa
- Editar o digitalizar entidades geográficas (p. ej.: añadir puntos, líneas, polígonos)
- Realizar análisis espaciales (p. ej.: buffer, superposición, unión) o producir resultados cartográficos (exportar a PDF/imagen)
:::

3. __¿Cómo saber si un proyecto de QGIS se ha guardado o no?__

:::{dropdown} Respuesta
Normalmente, si hay cambios sin guardar, QGIS mostrará un asterisco (*) junto al nombre del proyecto o en el título de la ventana/pestaña. Si no aparece ningún asterisco (o si “Guardar” aparece atenuado), eso sugiere que el proyecto ya está guardado (es decir, actualizado).
:::

4. __¿Cómo se abre un proyecto de QGIS?__

:::{dropdown} Respuesta
Puede abrir un proyecto de QGIS a través del `File` menú → `Open Project` (o el botón “Abrir proyecto” de la barra de herramientas) y a continuación, buscar un archivo `.qgs` o `.qgz`. Alternativamente, al hacer doble clic en el archivo del proyecto (si está asociado en su sistema) también podría abrirse en QGIS.
:::

5. __¿Cómo mostrar y ocultar paneles o barras de herramientas?__

:::{dropdown} Respuesta
En la barra superior, utilice el `View` menú → `Panels` o los submenús `Toolbars` para alternar (marcar/desmarcar) entre paneles o barras de herramientas específicos.
:::

6. __¿Dónde puede encontrar ayuda si tiene problemas con QGIS?__

:::{dropdown} Respuesta

- En nuestra página [Errores y problemas comunes](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_common_errors_and_Issues.html)
- Consultando la [documentación de QGIS](https://docs.qgis.org/3.34/en/docs/index.html)
- En el [foro de usuarios de QGIS en stackexchange](https://gis.stackexchange.com/?tags=qgis)
- En [grupos de usuarios de QGIS](https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups)
- Buscando tutoriales en YouTube

:::

::::

