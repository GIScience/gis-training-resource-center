::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Tabla de atributos

Cada capa vectorial consta de entidades geométricas (puntos, líneas o polígonos) y de una __tabla de atributos__ ({numref}`es_vector_data_overview`). La tabla de atributos contiene información sobre cada entidad en la capa. La información se almacena en filas y columnas en la tabla de atributos. Cada __fila__ de la tabla representa una __entidad__, mientras que las __columnas__ almacenan __atributos__ de esa entidad. Puede utilizar la tabla de atributos para buscar, ordenar, filtrar, editar y seleccionar datos.


:::{figure} /fig/en_vector_data_overview.png
---
width: 600px
align: center
name: es_vector_data_overview
---
Visión general de los datos vectoriales (fuente: HeiGIT).
:::

:::{admonition} ¡Ahora es su turno!
:class: note

Puede complementar este capítulo realizando los pasos con una capa vectorial de su elección. Al trabajar con datos geoespaciales, siempre tendrá que comprender la información almacenada en los conjuntos de datos, tanto las geometrías como los datos de atributos.

:::

## Abrir la tabla de atributos

Echar un vistazo a la tabla de atributos es esencial para comprender y tener una visión general de los datos con los que se está trabajando. Después de descargar e importar un conjunto de datos en QGIS, lo más probable es que abra la tabla de atributos para comprender los datos y ver qué información está disponible. Entender qué tipo de información está disponible es indispensable cuando se trabaja con software de SIG.

Puede abrir la tabla de atributos de dos maneras:

::::{margin}
:::{tip}

También puede utilizar el atajo <kbd>F6</kbd> (en algunos casos <kbd>Fn</kbd> + <kbd>F6</kbd>) para abrir el atributo.

:::
::::

1. Haga clic con el botón derecho en una capa del panel de capas Layers y seleccione `Abrir tabla de atributos` ({numref}`es_attributetable_right_click`).

:::{figure} /fig/en_attributetable_right_click.png
---
height: 500px
align: center
name: es_attributetable_right_click
---
Abrir la tabla de atributos haciendo clic derecho en QGIS 3.36.
:::

2. Seleccione una capa en el panel de capas Layers y haga clic en el símbolo de la tabla de atributos en la barra de herramientas ({numref}`es_attributetable_top_right`).

:::{note}

Si tiene varias capas, solo se abrirá la tabla de atributos de la capa actualmente seleccionada en el panel de capas.

:::

:::{figure} /fig/en_attributetable_top_right.png
---
height: 500px
align: center
name: es_attributetable_top_right
---
Abrir la tabla de atributos en QGIS 3.36.
:::

:::{dropdown} Botones de la tabla de atributos
:open:

| Icono | Descripción | Propósito | Atajo |
|---|---|-----|---|
| ![](/fig/mActionToggleEditing.png) | __Conmutar el modo de edición__ | Habilitar las funciones de edición |          |
| ![](/fig/mActionMultiEdit.png) | Conmutar el modo de edición múltiple | Actualizar múltiples campos de muchas entidades |  |
| ![](/fig/mActionSaveEdits.png) | __Guardar ediciones__ | Guardar las modificaciones actuales | |
| ![](/fig/mActionRefresh.png) | Volver a cargar la tabla | | |
| ![](/fig/mActionNewTableRow.png) | Añadir objeto espacial | Añadir una nueva entidad sin geometría |  |
| ![](/fig/mActionDeleteSelectedFeatures.png) | Borrar objetos seleccionados | Eliminar las entidades seleccionadas de la capa |  |
| ![](/fig/mActionEditCut.png) | Cortar las entidades seleccionadas al portapapeles |  | <kbd>Ctrl</kbd> + <kbd>X</kbd> |
| ![](/fig/mActionCopySelected.png) | Copiar las entidades seleccionadas al portapapeles |   | <kbd>Ctrl</kbd> + <kbd>C</kbd> |
| ![](/fig/mActionEditPaste.png) | Pegar entidades desde el portapapeles | Insertar nuevas entidades a partir de las copiadas | <kbd>Ctrl</kbd> + <kbd>V</kbd> |
| ![](/fig/mIconExpressionSelect.png) | Seleccionar entidades mediante una expresión | |
| ![](/fig/mActionSelectAll.png) | Seleccionar todo | Seleccionar todas las entidades en la capa |       |
| ![](/fig/mActionInvertSelection.png) | Invertir selección | Invertir la selección actual en la capa | <kbd>Ctrl</kbd> + <kbd>I</kbd> |
| ![](/fig/mActionDeselectActiveLayer.png) | Deseleccionar todo | Deseleccionar todas las entidades en la capa actual | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>A</kbd> |
| ![](/fig/mActionFilterMap.png) | Filtrar/seleccionar entidades mediante formulario | | <kbd>Ctrl</kbd> + <kbd>F</kbd> |
| ![](/fig/mActionSelectedToTop.png) | Mover la selección hacia arriba | Mover las filas seleccionadas a la parte superior de la tabla |  |
| ![](/fig/mActionPanToSelected.png) | Desplazar el mapa a las filas seleccionadas |  | <kbd>Ctrl</kbd> + <kbd>P</kbd> |
| ![](/fig/mActionZoomToSelected.png) | Hacer zoom a las filas seleccionadas | | <kbd>Ctrl</kbd> + <kbd>J</kbd> |
| ![](/fig/mActionNewAttribute.png) | Campo nuevo | Añadir un campo nuevo a la fuente de datos | <Kbd>Ctrl</kbd> + <kbd>W</kbd> |
| ![](/fig/mActionDeleteAttribute.png) | Borrar campo | Eliminar un campo de la fuente de datos | |
| ![](/fig/mActionEditTable.png) | Organizar columnas | Mostrar/ocultar campos de la tabla de atributos |
| ![](/fig/mActionCalculateField.png) | __Abrir calculadora de campos__ | Actualizar el campo para muchas entidades en una fila | <kbd>Ctrl</kbd> + <kbd>M</kbd> |
| ![](/fig/mActionConditionalFormatting.png) | Formato condicional | Habilitar dar formato a la tabla | |
| ![](/fig/dock.png) | Acoplar la tabla de atributos | Permite acoplar o desacoplar la tabla de atributos |
| ![](/fig/mAction.png) | Acciones | Lista las acciones relacionadas con la capa | |

:::

<!-- ADD: What will be the most important of these. Needs more explanation.-->

## Ordenar la tabla de atributos

Puede ordenar los datos de la tabla de atributos haciendo clic en el encabezado de una columna. Los datos de texto se ordenarán alfabéticamente y los datos numéricos se ordenarán por valor. Para invertir el orden de clasificación, vuelva a hacer clic en el encabezado. Una pequeña flecha en el encabezado de la columna indica si está ordenada de forma ascendente o descendente.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_show_attribute_table.mp4"></video>

:::::{grid} 2
::::{grid-item-card}

:::{figure} /fig/en_ascending.png
---
width: 300px
name: es_ascending
---
Tabla de atributos ordenada de forma ascendente.
:::

::::

::::{grid-item-card}

:::{figure} /fig/en_descending.png
---
width: 300px
name: es_descending
---
Tabla de atributos ordenada de forma descendente.  
:::

::::
:::::

## Acercar el zoom a una entidad específica mediante la tabla de atributos

Puede acercar el zoom a una entidad específica si necesita ubicarla geográficamente o si quiere verla más de cerca:

1. __Zoom:__ Haga clic con el botón derecho en una entidad → `Zoom a objeto`
2. Cierre su tabla de atributos. El lienzo del mapa ahora mostrará la entidad seleccionada.

:::{dropdown} Video: Acercar el zoom a una entidad

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom_to_feature.mp4"></video>

:::

## Seleccionar manualmente entidades en la tabla de atributos

Para interactuar con las entidades de una capa, debe seleccionarlas. Una forma de seleccionar entidades es a través de la tabla de atributos.

* __Selección:__ haga clic en las líneas de las entidades.
* __Selección múltiple:__ para seleccionar varias entidades, presione <kbd>Ctrl</kbd> y seleccione objetos en la tabla.
* __Mostrar solo las entidades seleccionadas:__ en la parte inferior izquierda de la tabla de atributos, abra
  el menú desplegable (`Mostrar todos los objetos espaciales`) y seleccione `Mostrar objetos espaciales seleccionados`. Para volver a mostrar todas
  las entidades, haga clic en `Show all features`.
* __Mostrar solo las entidades no seleccionadas:__ seleccione las entidades y haga clic en ![](/fig/mActionInvertSelection.png).

:::{dropdown} Video: Seleccionar manualmente entidades en la tabla de atributos

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>

:::

## Hacer zoom al área seleccionada

Ahora que ya sabe cómo seleccionar las entidades, puede hacer zoom a su área de
interés. Para ello, puede hacer clic en el símbolo de la barra de herramientas o hacer clic derecho
en la capa y seleccionar `Zoom a la Selección` ({numref}`es_zoom_to_selection_1`).

:::{figure} /fig/en_zoom_to_selection_1.png
---
width: 800px
align: center
name: es_zoom_to_selection_1
---
Captura de pantalla que muestra cómo hacer zoom a la selección en la parte superior.
:::

:::{figure} /fig/en_zoom_to_selection_2.png
---
width: 450px
align: center
name: es_zoom_to_selection_2
---
Captura de pantalla que muestra cómo hacer zoom a la selección al dar clic derecho.
:::

## Guardar solo las entidades seleccionadas como un nuevo archivo

Una vez que haya seleccionado sus datos, es posible que desee continuar solo con la
selección. Puede guardar su selección como una nueva capa. Para ello, haga clic con el botón derecho en la
capa - `Exportar` → `Guardar objetos seleccionados como...`.

:::{figure} /fig/en_save_selection.png
---
height: 500px
align: center
name: en_save_selection
---
Captura de pantalla que muestra cómo guardar solo las entidades seleccionadas.
:::

Ahora, puede elegir el formato, el nombre de la capa y el SRC.

<!--ADD IMAGE-->

:::{tip}

Recomendamos utilizar GeoPackage (.gpkg) en lugar de shapefile (.shp) en la mayoría de los casos.
Si no tiene la certeza de cuál es el formato más adecuado, consulte la página sobre [tipos de datos geoespaciales](/content/es/Wiki/es_qgis_geodata_types_wiki.md) en la wiki.

:::


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_export_wiki.mp4"></video>


## Preguntas de autoevaluación

::::{admonition} Ponga a prueba sus conocimientos
:class: note

Compruebe si conoce los conceptos clave de este capítulo respondiendo a las preguntas siguientes.

1. __¿Qué es la tabla de atributos en una capa vectorial y cómo está estructurada?__

:::{dropdown} Respuesta
La tabla de atributos es una representación tabular de los datos no espaciales (o descriptivos) de una capa vectorial. Cada fila corresponde a una entidad (punto, línea, polígono) de la capa. Cada columna (también llamada campo o atributo) almacena un atributo/propiedad (p. ej., nombre, población, tipo) para cada entidad.
:::

2. __¿Cómo se abre la tabla de atributos en QGIS?__

:::{dropdown} Respuesta
- En QGIS hacer clic derecho sobre la capa en el panel de capas Layers y seleccionar abrir tabla de atributos.
- También puede utilizar el botón Tabla de atributos ![](/fig/qgis_open_attribute_table.png) de la barra de herramientas.
:::

3. __¿Cómo hacer zoom a una entidad específica utilizando la tabla de atributos?__

:::{dropdown} Respuesta
- Dentro de la tabla de atributos, se puede hacer clic derecho en la fila de una entidad (o en una celda) y elegir “Zoom to Feature”. Esto cambia la vista del mapa para centrarse en esa entidad.
:::

4. __Describa cómo seleccionar manualmente las entidades a través de la tabla de atributos y cómo mostrar solo las entidades seleccionadas o no seleccionadas.__

:::{dropdown} Respuesta
__Seleccionar entidades manualmente:__
- Al hacer clic en el encabezado de la fila de una entidad individual en la tabla de atributos, se selecciona la entidad. Se resaltará en color azul.
- Para seleccionar varias entidades, se mantiene presionado <kbd>Ctrl</kbd> o <kbd>Cmd</kbd> en MacOS y se hace clic en los encabezados de las filas adicionales para añadir más entidades a la selección.
- Mantener presionada la tecla <kbd>Shift</kbd> permite seleccionar una serie de entidades.
__Mostrar solo las entidades seleccionadas o no seleccionadas:__
- En la parte inferior izquierda del cuadro de diálogo de la tabla de atributos, hay un menú desplegable (filtro) que permite cambiar entre:
  - __Mostrar todas las entidades__
  - __Mostrar las entidades seleccionadas__
  - __Mostrar las entidades no seleccionadas__
  - Otros filtros: mostrar entidades visibles en el mapa, mostrar entidades editadas y nuevas, etc.
- También se puede utilizar el botón ![](/fig/qgis_3.40_move_selection_to_top.png) `Mover la selección arriba del todo` de la barra de herramientas de la tabla de atributos.
:::

5. __Una vez seleccionado un subconjunto de entidades, ¿cómo se guardan solo esas entidades en una nueva capa (o archivo)?__

:::{dropdown} Respuesta
1. <kbd>Clic derecho</kbd> en la capa donde están seleccionadas las entidades.
2. Seleccionar `Exportar` → `Guardar objetos seleccionados como...`. Se abrirá una nueva ventana.
3. Elegir el formato de los datos, especificar la ubicación de almacenamiento y el nombre del archivo haciendo clic en ![](/fig/Three_points.png).
4. Hacer clic en `Aceptar`.
::::

