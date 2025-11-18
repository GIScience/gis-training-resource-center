::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Digitalización

La digitalización es el proceso de convertir los datos geográficos de mapas o imágenes en una forma digital comúnmente representada como datos vectoriales. El dominio de la digitalización es clave para los especialistas en SIG. Les permite convertir la información espacial a un formato digital, lo que facilita una manipulación más eficaz de los datos en comparación con los métodos tradicionales de interpretación de imágenes o mapas en papel.

:::{admonition} La digitalización en la labor humanitaria
:class: tip

Si quiere saber cómo el mapeo comunitario y la digitalización pueden ayudar a mejorar la resiliencia de las comunidades y facilitar la labor humanitaria, consulte la publicación de Paul Knight [“This is the first time this community is on a map…”, Digital Community Mapping en Nigeria](https://medium.com/digital-and-innovation-at-british-red-cross/first-time-this-community-has-been-on-a-map-nigeria-f592906b7be1).

:::

:::{figure} /fig/en_digitisation_concept.png
---
width: 900px
align: center
name: en_digitisation_concept
---
El concepto de digitalización en los SIG (fuente: HeiGIT).
:::

## Digitalización en QGIS

En QGIS, la digitalización consiste en trazar entidades como puntos, líneas o polígonos directamente sobre el lienzo del mapa para representar elementos geográficos como edificios, carreteras o parcelas. Además, se pueden asignar atributos a cada entidad durante la digitalización, lo que permite su posterior análisis e integración con otros datos geoespaciales. Estos datos digitalizados se convierten en un valioso activo para el análisis espacial y el mapeo.

:::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Escenario real 1/3__
^^^
Se ha producido una inundación en un pueblo como consecuencia de las fuertes lluvias. Para evaluar las necesidades de las familias y el impacto en la infraestructura, se le pide que haga un mapa general de la región y marque los edificios y carreteras afectados por las inundaciones. Sin embargo, no se dispone de conjuntos de datos con los edificios o las carreteras. Para el mapa, tendrá que crear dos capas nuevas con la red vial y los edificios. Sin embargo, se dispone de imágenes satelitales recientes. Con estas imágenes, puede crear capas vectoriales que representen las infraestructuras esenciales, como edificios y carreteras. Una vez creadas las capas, puede crear un mapa general preliminar del pueblo. Este mapa se entregará a los miembros de la comunidad y a los voluntarios sobre el terreno para mapear la infraestructura dañada. En un siguiente paso, la información recopilada por el equipo sobre el terreno puede utilizarse para enriquecer los datos y crear una evaluación del impacto de la inundación. Para crear el mapa, tendrá que crear capas vectoriales nuevas.
:::


### Barras de herramientas de digitalización

:::{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
align: left
name: Activate digitising Toolbar
---
La barra de herramientas de digitalización en QGIS 3.36.
:::

La digitalización se realiza con la `Digitizing Toolbar` y en el lienzo del mapa.
En primer lugar, debe comprobar si `Digitizing Toolbar` está activado. Para ello,
* haga clic en la pestaña `View` de la barra de menús y luego en `Toolbars`. Compruebe si las barras de herramientas `Digitizing` y `Advanced Digitizing` están activadas.

En primer lugar, debe comprobar si `Digitizing Toolbox` está activado. Para ello,
1. Haga clic en la pestaña `View` de la barra de menús y luego en `Toolbars`. Compruebe si las cajas de herramientas `Digitizing` y `Advanced Digitizing` están activadas.

2. En la parte superior de la interfaz de QGIS debería aparecer un recuadro de herramientas como el siguiente.

<br>

<br>

<br>

La barra de herramientas de digitalización ofrece las herramientas básicas para crear, guardar y editar entidades. Sin embargo, para todo lo que va más allá de la simple creación de nuevas entidades y la eliminación de entidades, se necesita la barra de herramientas Advanced Digitization (véase {numref}`digitising_toolbar`). Esta última sirve para mover entidades, eliminar partes de entidades y mucho más. Todas las funciones se enumeran en las dos tablas que figuran abajo.

:::{figure} /fig/Toolbox.png
---
width: 700 px
name: digitising_toolbar
align: center
---
Barra de herramientas de digitalización en QGIS 3.36.
:::

:::{dropdown} Barra de herramientas de digitalización
| Herramienta                                 | Finalidad                                                                                                      | Herramienta                                | Finalidad                                                                    |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------------------------------------|
| ![](/fig/mActionAllEdits.png)               | Permite guardar, retroceder o cancelar cambios simultáneamente en todas las capas o en las capas seleccionadas | ![](/fig/mActionToggleEditing.png)         | Activar o desactivar el modo de edición en las capas seleccionadas.          |
| ![](/fig/mActionSaveEdits.png)              | Guardar cambios                                                                                                |                                            |
| ![](/fig/mActionDigitizeWithSegment.png)    | Digitalizar usando segmentos rectos                                                                            | ![](/fig/mActionDigitizeWithCurve.png)     | Digitalizar usando líneas curvas                                             |
| ![](/fig/mActionStreamingDigitize.png)      | Activar digitalización a mano alzada                                                                           | ![](/fig/mActionDigitizeShape.png)         | Digitalizar polígono de forma regular                                        |
| ![](/fig/mActionNewTableRow.png)            | Añadir nuevo registro                                                                                          | ![](/fig/mActionCapturePoint.png)          | Añadir objeto espacial: Capturar punto                                       |
| ![](/fig/mActionCaptureLine.png)            | Añadir objeto espacial: Capturar línea                                                                         | ![](/fig/mActionCapturePolygon.png)        | Añadir objeto espacial: Capturar polígono                                    |
| ![](/fig/mActionVertexTool.png)             | Herramienta Vértice (todas las capas)                                                                          | ![](/fig/mActionVertexToolActiveLayer.png) | Herramienta Vértice (capa actual)                                            |
| ![](/fig/checkbox.png)                      | Establecer si el panel del editor de vértices debe abrirse automáticamente                                     | ![](/fig/mActionMultiEdit.png)             | Modificar los atributos de todas las entidades seleccionadas simultáneamente |
| ![](/fig/mActionDeleteSelectedFeatures.png) | Borrar objetos seleccionados de la capa activa                                                                 | ![](/fig/mActionEditCut.png)               | Cortar entidades de la capa activa                                           |
| ![](/fig/mActionCopySelected.png)           | Copiar las entidades seleccionadas de la capa activa                                                           | ![](/fig/mActionEditPaste.png)             | Pegar las entidades en la capa activa                                        |
| ![](/fig/mActionUndo.png)                   | Deshacer cambios en la capa activa                                                                             | ![](/fig/mActionRedo.png)                  | Rehacer cambios en la capa activa                                            |

:::

Para procedimientos de digitalización más complejos, utilizará la barra de herramientas de digitalización avanzada. Sin embargo, en este capítulo, nos centraremos en la barra de herramientas de digitalización normal.

:::{dropdown} Barra de herramientas de digitalización avanzada

| Herramienta                                                                                                 | Propósito                                        | Herramienta                                                                                                                                | Propósito                     |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| ![](/fig/cad.png)                                                                                           | Activar herramientas avanzadas de digitalización |
| ![](/fig/mActionMoveFeature-1.png)![](/fig/mActionMoveFeatureLine.png)![](/fig/mActionMoveFeaturePoint.png) | Mover entidades                                  | ![Texto alternativo](/fig/mActionMoveFeatureCopy.png) ![](/fig/mActionMoveFeatureCopyLine.png) ![](/fig/mActionMoveFeatureCopyPoint-2.png) | Copiar y mover entidades      |
| ![Texto alternativo](/fig/mActionRotateFeature.png)                                                         | Girar entidades                                  | ![Texto alternativo](/fig/mActionSimplify.png)                                                                                             | Simplificar entidad           |
| ![Texto alternativo](/fig/mActionScaleFeature.png)                                                          | Escalar entidad                                  |
| ![Texto alternativo](/fig/mActionAddRing.png)                                                               | Añadir anillo                                    | ![Texto alternativo](/fig/mActionAddPart.png)                                                                                              | Añadir parte                  |
| ![Texto alternativo](/fig/mActionFillRing.png)                                                              | Rellenar anillo                                  | ![Texto alternativo](/fig/mActionReverseLine.png)                                                                                          | Intercambiar dirección        |
| ![Texto alternativo](/fig/mActionDeleteRing.png)                                                            | Eliminar anillo                                  | ![Texto alternativo](/fig/mActionDeletePart.png)                                                                                           | Eliminar parte                |
| ![Texto alternativo](/fig/mActionOffsetCurve.png)                                                           | Desplazar curva                                  | ![Texto alternativo](/fig/mActionReshape.png)                                                                                              | Cambiar la forma de entidades |
| ![Texto alternativo](/fig/mActionSplitParts.png)                                                            | Separar partes                                   | ![Texto alternativo](/fig/mActionSplitFeatures.png)                                                                                        | Separar entidades             |
| ![Texto alternativo](/fig/mActionMergeFeatureAttributes.png)                                                | Unir atributos de entidades seleccionadas        | ![Texto alternativo](/fig/mActionMergeFeatures.png)                                                                                        | Unir entidades seleccionadas  |
| ![Texto alternativo](/fig/mActionRotatePointSymbols.png)                                                    | Rotar símbolos de punto                          | ![Texto alternativo](/fig/mActionOffsetPointSymbols.png)                                                                                   | Desplazar símbolos de punto   |
| ![Texto alternativo](/fig/mActionTrimExtend.png)                                                            | Recortar o ampliar entidades                     |
:::


## Crear conjuntos de datos nuevos

Para digitalizar datos nuevos, siempre hay que empezar por crear el conjunto de datos antes de cargarlo con datos digitalizados. Tenga en cuenta que una capa solo puede contener un tipo de geometría: puntos, líneas o polígonos. Cuando cree un conjunto de datos, tendrá que elegir el tipo de geometría. Además, puede añadir más columnas con atributos para añadir más datos a la tabla de datos.

:::{admonition} ¡Ahora es su turno!
:class: note

Piense en un conjunto de datos espaciales que podría necesitar en sus operaciones humanitarias. ¿Qué tipo de información adicional es útil? ¿Cómo la recopilaría? Puede tratarse del tipo de carretera, cultivos sembrados, tipo de vegetación o indicadores sociales. Puede debatir en grupos y escribir las respuestas en papel o en la pizarra digital.

:::


:::{dropdown} Video: Cómo crear un conjunto de datos nuevo

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_create_layer.mp4"></video>

:::

1. `Layer` --> `Create Layer` -> `New GeoPackage Layer` o `New Shapefile Layer`
2. Haga clic en ![](/fig/Three_points.png) junto al campo de entrada `file name` y vaya a la carpeta en la que desea guardar el conjunto de datos.
3. `File encoding`: Asegúrese de que está configurado como UTF-8.
4. `Geometry type`: Seleccione el tipo de entidad que desea digitalizar, p. ej., puntos o líneas.
5. En `Additional dimension` debe asegurarse siempre de que `None` está marcada. Excepto si existe la posibilidad de recoger también los valores Z (elevación). Pero en la mayoría de los casos no es así.
6. Lista desplegable del SRC: Seleccione el EPSG/SRC que desea establecer para la nueva capa. Por defecto, QGIS selecciona el SRC del proyecto. Si desea cambiarlo, haga clic en ![](/fig/mIconProjectionEnabled.png).
7. En `New Field` puede añadir columnas a la nueva capa. Aquí puede configurar qué otro tipo de datos desea recopilar en este conjunto de datos.
    * `Type`: Seleccione el tipo de datos que tendrá la columna, p. ej. `Text`, `Whole number`, `Decimal Number`, `Date`.
    * Haga clic en ![](/fig/mActionNewAttribute.png) para añadir la nueva columna a `Fields List`.
8. Haga clic en `OK` para crear los nuevos datos.


:::{figure} /fig/New_GeoPackage_Layer.png
---
width: 500px
name: new_gpgk_layer
align: center
---
La ventana de creación de capas en QGIS 3.36.
:::


:::{attention}
Un concepto importante que hay que entender antes de empezar a añadir datos a los conjuntos de datos es que, siempre que se realicen cambios en un conjunto de datos que no sean de estilo, hay que activar el modo de edición. Para ello, seleccione la capa y haga clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Ahora es posible hacer clic en los botones de muchas funciones de la barra de herramientas de digitalización. Cuando haya terminado de manipular la capa, haga clic en ![](/fig/mActionSaveEdits.png) `Save Layer Edits` para guardar los cambios.
:::

Una vez configurada la nueva capa, puede empezar a añadir entidades geométricas. El proceso para los tres tipos geométricos es básicamente el mismo:

### Crear nuevas entradas de datos.

1. Seleccione la capa a la que se desea añadir datos en el panel Layer.
2. Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Asegúrese de que la capa está en modo de edición. Si no es así, haga clic en el icono ![](/fig/mActionToggleEditing.png) de la
barra de herramientas de digitalización.

### Crear datos de punto

1.	Seleccione la capa de puntos a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Asegúrese de que la capa está en modo de edición. Si no es así, haga clic en el icono ![](/fig/mActionToggleEditing.png) de la barra de herramientas de digitalización.
3.	Haga clic en ![](/fig/mActionCapturePoint.png).
4.	Haga clic izquierdo en la entidad que desea digitalizar.
5.	Al hacer clic, aparecerá una ventana `[Your Layer Name]- Feature Attribute`. Aquí puede añadir la información sobre esta entidad a las diferentes columnas, sobre la base de la tabla de atributos de la capa.
5.	Una vez que haya terminado la digitalización, ![](/fig/mActionSaveEdits.png) para guardar los cambios.
6.	Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

:::{dropdown} Video: Cómo crear datos de punto
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>
:::

:::{figure} /fig/point_creation.png
---
width: 750 px
name: point_creation
align: center
---
Creación de puntos.
:::

<!--REPLACE IMAGE showing a point creation window with more attributes and not just ID and type to show the 
information you can add at this stage-->



::::{admonition} Obtener coordenadas de Google Maps
:class: tip

A veces la forma más fácil de obtener las coordenadas de un lugar, como la oficina de una sociedad nacional de la Cruz Roja o de la Media Luna Roja o simplemente de una casa, es utilizar Google Maps. En Google Maps, puede hacer clic derecho en cualquier lugar para obtener las coordenadas (en grados).

:::{figure} /fig/en_google_maps_rightclick_coords.png
---
width: 250 px
align: right
name: en_google_maps_rightclick_coords
---
:::

1. En Google Maps, localice el punto que desea añadir a su proyecto de QGIS.
2. Haga clic derecho en el punto y seleccione las coordenadas. Se copiarán automáticamente en el portapapeles.
3. Vaya a su proyecto de QGIS y pegue las coordenadas en la barra de búsqueda de la esquina inferior izquierda de la ventana de QGIS.
4. Seleccione `Go to [Your coordinates] (EPSG 4326: WGS 84)`.
5. El punto de coordenadas parpadeará en rojo en el lienzo del mapa.
::::




:::{admonition} ¡Ahora es su turno!

Intente digitalizar las oficinas de la Cruz Roja y la Media Luna Roja de su país siguiendo los pasos que se indican a continuación.

:::

1. Cree un nuevo conjunto de datos de puntos.
2. Añada un [mapa base](/content/es/Module_2/es_qgis_basemap.md) (OSM o Bing Aerial, por ejemplo).
3. Busque las oficinas de la Cruz Roja y la Media Luna Roja de su país en Google Maps.
4. Una vez localizadas, haga clic derecho en una de ellas en Google Maps y haga clic en las coordenadas. Las coordenadas se copiarán en el portapapeles
5. Pegue las coordenadas en la barra de búsqueda ubicada en la parte inferior izquierda de la ventana de QGIS. Seleccione ir a las coordenadas. La ubicación se marcará con un punto rojo.

6. Active el modo de edición ![](/fig/mActionToggleEditing.png) en su nueva capa.
7. Haga clic en ![](/fig/mActionCapturePoint.png).
8. Añada la entidad de punto en la ubicación indicada.
9. Añada el nombre de la oficina.
10. Haga clic en `Ok`.
11. Haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
12. Haga clic en ![](/fig/mActionToggleEditing.png) para salir del modo de edición.



### Crear capas de líneas y polígonos

El proceso de creación de capas de líneas o polígonos es esencialmente el mismo que el de datos de puntos. La diferencia principal es que, en lugar de añadir solo un punto, las geometrías de líneas y polígonos requieren varios puntos (vértices). Cada punto que añade es un vértice entre dos líneas. En QGIS las líneas y los polígonos se crean estableciendo un punto y, a continuación, otro punto conectado al punto añadido anteriormente. Para terminar de añadir la entidad haga <kbd>clic derecho</kbd>.

:::{attention}
Recuerde cambiar el tipo de geometría a líneas si desea crear una nueva capa de línea.
:::

::::{tab-set}

:::{tab-item} Crear datos de línea

La creación de datos de líneas funciona de la misma manera que la creación de datos de puntos (véase más arriba). En primer lugar, debe crear una nueva capa de líneas o utilizar una ya existente.

1.	Seleccione la capa de línea a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png). Ahora, la capa está en modo de edición.
3.	Haga clic en ![](/fig/mActionCaptureLine.png).
4.	Para digitalizar entidades de línea, haga clic a lo largo de la línea. Cuando haya terminado, haga clic derecho en el último punto de la línea para finalizar la entidad.
5.	Aparecerá una ventana `[Your Layer Name]- Feature Attribute`. Aquí puede añadir la información sobre esta entidad a las diferentes columnas, sobre la base de la tabla de atributos de la capa.
6.	Una vez que haya terminado la digitalización, haga clic en ![](/fig/mActionSaveEdits.png) `Save Layer Edits` para guardar los cambios.
7.	Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing` para salir del modo de edición.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>

:::

:::{tab-item} Crear datos de polígonos

La creación de capas de polígonos funciona del mismo modo que para los datos de puntos y líneas.

1.	Seleccione la capa de polígonos a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png). Ahora, la capa está en modo de edición.
3.	Haga clic en ![](/fig/mActionCapturePolygon.png).
4.	Para digitalizar entidades poligonales, haga clic izquierdo alrededor del área que desea digitalizar. Cuando haya terminado, haga clic derecho en el último punto del área para finalizar la entidad.
5.	Aparecerá una ventana `[Your Layer Name]- Feature Attribute`. Aquí puede añadir la información sobre esta entidad a las diferentes columnas, sobre la base de la tabla de atributos de la capa.
6.	Una vez que haya terminado la digitalización, ![](/fig/mActionSaveEdits.png) para guardar los cambios.
7.	Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing` para salir del modo de edición.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_feature.mp4"></video>

:::

::::

:::{card}
:class-card: sd-text-justify sd-rounded-3 sd-border-2
__Escenario real 2/3__
^^^

Lo primero que hay que hacer es localizar el pueblo utilizando las coordenadas GPS que se introducen en la esquina inferior derecha de la ventana de QGIS. Por suerte, el proceso de digitalización es relativamente fácil, ya que se dispone de una imagen por satélite reciente proporcionada por Microsoft Bing. Puede cargar la imagen satelital utilizando el __QuickMapServices__ y buscando y añadiendo el mapa base `Bing Aerial`. Puede ver los edificios y las carreteras en la imagen de satélite. El siguiente paso será crear capas nuevas: una para las carreteras y otra para los edificios.

:::

## Editar los datos

En algunos casos, es posible que desee modificar o corregir datos vectoriales debido a imprecisiones o cambios. La edición de estos datos se realiza con la barra de herramientas de digitalización. En QGIS puede editar tanto las geometrías como los valores de la tabla de atributos.

### Editar geometrías

Para todos los casos:

1. Seleccione la capa que desea editar.
2. Haga clic en ![](/fig/mActionToggleEditing.png) para activar el modo de edición.
3. Haga los cambios.
4. Guarde los cambios haciendo clic en ![](/fig/mActionSaveEdits.png).
5. Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

:::{Tip}
Puede utilizar los botones ![](/fig/mActionUndo.png) y ![](/fig/mActionRedo.png) para deshacer los cambios fácilmente.

Tenga en cuenta que esto solo es posible __antes__ de guardar los cambios.
:::

:::::{tab-set}

::::{tab-item} Eliminar entidades

1.	Seleccione la capa que desea modificar.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png) `Toggle Editing`.
3.	Haga clic en ![](/fig/mActionSelectRectangle.png) y seleccione la entidad que desea eliminar (consulte la [wiki](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_spatial_queries_wiki.html#manual-selection)).
4.	Una vez seleccionadas las entidades, haga clic en ![](/fig/mActionDeleteSelectedFeatures.png) para eliminarlas.
5.	Una vez que haya terminado de editar, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
6.	Haga clic de nuevo en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

:::{note}
Tenga en cuenta que una vez que guarde los cambios ![](/fig/mActionSaveEdits.png), ya no podrá deshacer o recuperar las entidades eliminadas. Los cambios modifican permanentemente el archivo de datos de su carpeta.
:::
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/delet_feature_geometry.mp4"></video>

::::

::::{tab-item} Mover entidades

Existen múltiples métodos para mover entidades. Aquí mostraremos el método que funciona de la misma manera para entidades de punto, línea y polígono. Para esto se necesita la caja de herramientas de digitalización avanzada.

1.	Seleccione la capa de línea a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png).
3.	Haga clic en ![](/fig/mActionMoveFeaturePoint.png) y en la entidad que desea mover. A continuación, haga clic en la ubicación a la que desea desplazar la entidad.
4.	Una vez que haya terminado de editar, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
5.	Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/move_feature_geometry.mp4"></video>

::::

::::{tab-item} Modificar geometrías

1.	Seleccione la capa de línea a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png).
3.	Haga clic en ![](/fig/mActionVertexToolActiveLayer.png).
4.	Ahora puede mover cada vértice (esquina) de una entidad. Haga clic en el vértice/esquina que desea mover y, a continuación, haga clic en la ubicación a la que desea mover el vértice.
5.	Una vez que haya terminado de editar, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
6.	Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_move_vertices.mp4"></video>

::::

::::{tab-item} Añadir anillos a entidades poligonales

Un anillo en QGIS es una parte dentro de un polígono que no forma parte del polígono. Imagine un polígono que representa un lago. El anillo es una isla en el lago. Para comprenderlo mejor, vea el video más abajo.

1.	Seleccione la capa de línea a la que desea añadir datos en el panel Layer.
2.	Vaya a la barra de herramientas de digitalización y haga clic en ![](/fig/mActionToggleEditing.png).
3.	Haga clic en ![añadir icono de anillo](/fig/mActionAddRing.png).
4.	Cree un anillo haciendo clic en el área que desea excluir. Haga clic derecho para cerrar el anillo.
5.	Una vez que haya terminado de editar, haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
6.	Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) para cerrar el modo de edición.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_ring.mp4"></video>

::::

:::::

### Editar los valores de los atributos

A veces tendrá que editar los valores de las columnas de la tabla de atributos. Por ejemplo, el nombre de un distrito administrativo que esté escrito de forma incorrecta o diferente o si un valor no se ha introducido correctamente. Para ello, tendrá que:

::::{margin}

:::{tip}
Puede abrir la tabla de atributos de la capa seleccionada pulsando <kbd>F6</kbd>.
:::
::::

1. Abra la tabla de [atributos](/content/es/Module_2/es_qgis_attribute_table.md)
2. Haga clic en ![](/fig/mActionToggleEditing.png) para activar el modo de edición.
3. Seleccione el campo que desea editar.
4. Introduzca el valor corregido.
5. Haga clic en ![](/fig/mActionSaveEdits.png) para guardar los cambios.
6. Vuelva a hacer clic en ![](/fig/mActionToggleEditing.png) para salir del modo de edición.

Este proceso se denomina __“Limpieza de datos”__ y es importante cuando se realizan análisis de datos o se manipulan datos de cualquier forma. Al recopilar o digitalizar datos, es fácil cometer pequeños errores, como un valor erróneo, un tipo de valor equivocado o una falta de ortografía. Por lo tanto, al realizar los análisis, es importante revisar la tabla de atributos en busca de incoherencias o errores. Si estos errores no se limpian, los resultados serán incorrectos y se podrían sacar conclusiones erróneas.

::::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Escenario real 3/3__
^^^

Con las nuevas capas, ya tiene todo listo para trazar los edificios y las carreteras en las nuevas capas. Ya tiene algunos conocimientos sobre el estado de las carreteras (p. ej., la superficie de la carretera, la calidad y si está inundada) y el estado de las casas (p. ej., si fueron afectadas por la inundación, si tienen varios pisos, etc.). Se trata de información útil que puede almacenarse en los atributos adicionales de la tabla de datos.

:::{figure} /fig/Building_damage_assessement_bangladesh.png
---
name: Building_damage_assessement
width: 750 px
---
Evaluación de daños en edificios de Paikgachha Upazila, distrito de Khulna, división de Khulna, Bangladesh, al 4 de junio de 2024 (fuente: [Int'l Charter, UNOSAT](https://reliefweb.int/map/bangladesh/building-damage-assessment-paikgachha-upazila-khulna-district-khulna-division-bangladesh-4-june-2024-imagery-analysis-4-june-2024-published-7-june-2024-v1))
:::

::::

## Errores de digitalización espacial en QGIS

La precisión de los datos geoespaciales es crucial para el análisis espacial. Los errores de posición son inevitables cuando los datos se digitalizan manualmente. Los ejemplos más comunes son el subajuste y el sobreajuste. Cuando las coordenadas no se conectan como deberían, y sobreajuste, cuando las líneas se pasan de donde deberían. A menudo, estos errores no son visibles a menos que se acerque el zoom sobre esas coordenadas. Establecer una tolerancia difusa (tolerancia de ajuste) sirve para reducir los subajustes y los sobreajustes. La tolerancia de ajuste es la distancia mínima tolerada entre nodos, líneas y vértices.

:::{figure} /fig/Digitization_Errors.PNG
---
width: 500px
align: center
name: Digitization_Errors
---
Errores de digitalización (fuente: SpatialPost).
:::

## Preguntas de autoevaluación

::::{admonition} Recapitule sus conocimientos
:class: note

1. __¿Qué es la digitalización en los SIG? ¿Por qué es útil convertir entidades de mapas o imágenes en forma vectorial?__

:::{dropdown} Respuesta
La digitalización en SIG es el proceso de trazar o capturar entidades geográficas (puntos, líneas y polígonos) de mapas, imágenes (como imágenes satelitales, aéreas o de mapas escaneados) __o informes__ y convertirlos en datos vectoriales. 
Es útil porque nos permite realizar análisis espaciales y obtener información sobre el fenómeno captado en el espacio. Además, podemos combinarlos con otros datos espaciales y mostrarlos en mapas informativos.
:::

2. __¿Cómo se crea un nuevo conjunto de datos vectoriales?__

:::{dropdown} Respuesta
1. En la barra superior, vaya al menú `Layer` → `Create Layer` → `New GeoPackage Layer` o `New Shapefile Layer`.
2. Especifique las propiedades de la capa.
    - Especifique la ruta y el nombre del archivo.
    - **Codificación**: UTF-8 (permite caracteres especiales).
    - **Tipo de geometría**: punto, línea o polígono (una capa solo admite un tipo de geometría).
    - **Sistema de referencia de coordenadas (SRC)**
    - Defina los __campos de atributo__ (columnas) que desea en la tabla de atributos de la capa.
3. Haga clic en `Ok` para crear la capa.
:::


3. __Imagine que está digitalizando edificios afectados por una inundación a partir de una imagen aérea. ¿Qué campos de atributos podría incluir y qué nivel de detalle o precisión intentaría mantener?__

:::{dropdown} Respuesta
Los atributos que desee digitalizar dependerán siempre del objetivo de su labor de mapeo (p. ej., respuesta a emergencias, evaluación de daños o planificación) y de si trabaja sobre el terreno o se basa en imágenes satelitales.
- __Posibles campos de atributo__
    - __Tipo de edificio/uso__: p. ej., residencial, comercial, industrial, público
    - __Número de pisos__
    - __Material del techo__
    - __Material de las paredes__
    - __Condición del edificio__: p. ej., “sin daños”, “daños menores”, “daños graves”, “colapsado”
    - __Profundidad de la inundación o exposición al agua__
    - __Fecha de la evaluación__
    - __Confianza/calidad__
    - __Dirección__
    - ...
:::

::::

