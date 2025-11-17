# Errores y problemas comunes en QGIS <!-- omit from toc -->

Aquí recopilamos errores y problemas comunes en QGIS como apoyo general a la capacitación en QGIS.

# Contenido <!-- omit from toc -->

- [Diferentes versiones de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#different-qgis-versions)
- [QGIS no abre en Mac](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#qgis-on-mac-doesnt-open)
- [Una capa no se muestra en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#a-layer-is-not-displayed-in-qgis)
- [Desapareció una ventana de capas en QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#a-layer-window-has-disappeared-in-qgis)
- [Las capas que deberían estar en la misma posición no están unas sobre otras](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#layers-that-should-actually-be-in-the-same-position-are-not-on-top-of-each-other)
- [El archivo de capa ha desaparecido de la ventana de capas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#layer-file-disappeared-from-the-layer-window)
- [Faltan herramientas de procesamiento en la herramienta de paneles y la pestaña de vectores está incompleta](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#missing-processing-tools-in-the-panels-tool-and-incomplete-vector-tab)
- [Falta la caja de herramientas](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#missing-toolbox)
- [La flecha norte no se sincroniza con el mapa correspondiente](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#the-north-arrow-is-not-syncing-with-the-corresponding-map)
- [Geometría inválida](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#invalid-geometry)
- [Sistemas de coordenadas: ¿Qué significan todos estos términos?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#coordinate-systems-what-do-all-these-terms-mean)
- [Sistemas de coordenadas: ¿Cómo puedo redefinir el sistema de coordenadas de un conjunto de datos?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#coordinate-systems-how-do-i-redefine-a-datasets-coordinate-system)
- [Sistemas de coordenadas: ¿Por qué se utiliza Mercator si está tan distorsionado?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#coordinate-systems-why-is-mercator-ever-used-if-its-so-distorted)
- [Sistemas de coordenadas: ¡Mi conjunto de datos no se encuentra donde debería!](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#coordinate-systems-my-dataset-is-not-located-where-it-should-be)
- [Sistemas de coordenadas: ¿En qué sistema de coordenadas debe estar mi conjunto de datos?](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#coordinate-systems-what-coordinate-system-should-my-dataset-be-in)
- [¡Mi conjunto de datos está ligeramente desplazado de donde debería estar!](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#my-dataset-is-slightly-offset-from-where-it-should-be)
- [Resultados erróneos o falta de datos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#wrong-data-results-or-missing-data)
- [Problemas de gestión de archivos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#file-management-issues)
- [Problemas específicos de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#specific-qgis-problems)
  - [Configuración básica \> Desactivar la selección automática de proyección](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#basic-settings--deactivating-the-automatic-projection-selection)
  - [Guardar regularmente](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#saving-regularly)
  - [Aplicaciones GRASS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#grass-applications)
  - [SAGA con Linux](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#saga-with-linux)
  - [Diéresis, caracteres especiales y espacios en las rutas de los archivos](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#umlauts-special-characters-spaces-in-file-paths)
- [Enlaces de acceso a la Ayuda de QGIS](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#qgis-help-access-links)
    - [Tutoriales y consejos sobre QGIS:](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#qgis-tutorials-and-tips)
    - [Comunidad/foros de QGIS:](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#qgis-communityforums)
    - [Canales de YouTube sobre QGIS:](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#qgis-youtube-channels)
    - [ChatGPT](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Wiki/es_qgis_common_errors_and_Issues.html#chatgpt)



## Diferentes versiones de QGIS
La Wiki y, en particular, los videos que contiene son solo una fotografía en el tiempo. QGIS en sí, así como las extensiones instalables, se desarrollan y mejoran constantemente. Por lo tanto, puede haber diferencias entre las distintas versiones en el aspecto de la interfaz de usuario o, en raras ocasiones, incluso en el funcionamiento. En consecuencia, puede haber diferencias entre la Wiki y el QGIS instalado en su PC. No obstante, este capítulo se centra en errores y problemas comunes, con la esperanza de que sean útiles para muchas versiones (futuras).

## QGIS no abre en Mac
Al abrir QGIS por primera vez en Mac puede aparecer este mensaje de error:

:::{figure} /fig/qgis_on_mac.png
---
width: 55%
name: qgis_on_mac.png
align: center
name: Error when opening QGIS on Mac for the first time
---
Error al abrir QGIS en Mac por primera vez.
:::

Para solucionarlo, presione el botón control del teclado y haga clic derecho del mouse en abrir.

Si este problema persiste, puede cambiar la configuración de su dispositivo. Vaya a `Settings` > `Security & Privacy` y desplácese hacia abajo, haga clic en `Open Anyway`

:::{figure} /fig/opening_qgis_mac.png
---
width: 55%
name: opening_qgis_mac.png
align: center
name: Change settings to open QGIS on Mac
---
Cambiar la configuración para abrir QGIS en Mac.
:::


## Una capa no se muestra en QGIS

__Solución:__
  1. Haga clic derecho en la capa correspondiente.
  2. Active la función `Zoom to Layer` en la ventana emergente.

:::{figure} /fig/en_layer_display.png
---
width: 55%
name: en_layer_display.png
align: center
name: Zoom to layer if layer is not displayed
---
Hacer zoom a la capa si no se muestra la capa.
:::


## Desapareció una ventana de capas en QGIS

__Solución:__
 1. Abrir en la pestaña principal `View`.
 2. En la ventana emergente, seleccione `Panels`.
 3. En la subventana, marque la casilla `Layers`.

:::{figure} /fig/en_closed_layer_view.png
---
width: 75%
name: en_closed_layer_view.png
align: center
name: Layer window disappeared
---
Desapareció la ventana de capas.
:::

## Las capas que deberían estar en la misma posición no están unas sobre otras.

__Solución:__

Este tipo de problemas suele deberse a a) *una falta de coincidencia entre el SRC de las capas y el del proyecto* o b) una *reproyección incorrecta*.

 a)
 1. Compruebe las propiedades de la capa (haga clic con el botón derecho en la capa correspondiente).
 2. En la ventana emergente, seleccione `Properties`.
 3. En la siguiente ventana emergente, seleccione `Information` y revise qué proyección está definida en la entrada `Coordinate Reference System (CRS)`.
 4. Además, compruebe si en la barra de estado, en la parte inferior derecha, está configurada la misma proyección.
 5. Corrija cualquier discrepancia reproyectando las capas o cambiando la configuración del SRC del proyecto.

b)

**Reproyección:** 
Si hay dos capas con diferentes SRC, seleccione una de las capas como capa de entrada que tenga, por ejemplo, el SRC EPSG:32632 - WGS 84, y defina como SRC de destino EPSG:4326 - WGS 84. Al ejecutar el algoritmo obtendrá una nueva capa, idéntica a la capa de entrada, pero con un SRC diferente.

Se mostrará en el espacio de trabajo en el mismo lugar que las demás capas, ya que QGIS la reproyecta en tiempo de ejecución. Sin embargo, sus coordenadas reales son diferentes.


:::{figure} /fig/en_qgis_layer_with_different_KBS.png
---
width: 75%
name: en_qgis_layer_with_different_KBS.png
align: center
name: Layer with different crs
---
Capa con diferentes SRC.
:::

Puede comprobarlo utilizando el algoritmo `Add Geometry Attributes` < `Geometry Tools`. Las coordenadas son distintas a las coordenadas de las otras dos tablas de atributos de las otras capas.

En su lugar, haga lo siguiente:

1. Seleccione la pestaña `Vector`.

2. En el menú emergente active `Data Management Tools`.

3. Y en el siguiente menú emergente `Reproject Layer`.


:::{figure} /fig/en_qgis_reproject_vector_layer01.png
---
width: 75%
name: en_qgis_reproject_vector_layer01.png
align: center
name: Reproject Layer in QGIS
---
Reproyectar capa en QGIS.
:::


:::{figure} /fig/en_qgis_reprojected_layer.png
---
width: 75%
name: en_qgis_reprojected_layer.png
align: center
name: Tool to reproject layer in QGIS
---
Herramienta para reproyectar capas en QGIS.
:::

Guarde siempre las capas reproyectadas mediante las funciones `Export` y `Save as`, ya que solo se guardan temporalmente y desaparecerán tras cerrar el proyecto.

:::{figure} /fig/en_qgis_reprojection_export.png
---
width: 75%
name: en_qgis_reprojection_export.png
align: center
name: Export reprojected layer
---
Exportar capa reproyectada.
:::

Procedimiento similar para capas ráster...

1. Seleccione la pestaña `Raster`.

2. En el menú emergente active `Projections`.

3. Y en el siguiente menú emergente `Warp (Reproject)`.


:::{figure} /fig/en_qgis_reproject_raster_layers01.png
---
width: 75%
name: en_qgis_reproject_raster_layers01.png
align: center
name: Reproject raster layer in QGIS
---
Reproyectar capa ráster en QGIS.
:::
:::{attention}
 A menudo se producen errores si se establece el SRC y no se ha utilizado ninguna herramienta de reproyección. Si sospecha de que su reproyección ha salido mal, borre todas las capas afectadas de QGIS, vuelva a cargar los datos y, a continuación, reproyéctelos y expórtelos.
:::

## El archivo de capa ha desaparecido de la ventana de capas

Si un archivo de capa ya no se muestra o no está activo en la ventana de capas después de reabrir un proyecto de QGIS, se trata solo de una capa temporal. Las capas temporales tienen un símbolo a la derecha de su nombre:
 ![](/fig/en_qgis_temporary_Layer.png)

__Solución:__

La próxima vez, guárdelo:
1. Haga clic en la pestaña `Layer` y en `Save as` en la ventana emergente.

:::{figure} /fig/en_qgis_save_layer01.png
---
width: 65%
name: en_qgis_save_layer01.png
align: center
name: Save layer
---
Guardar capa.
:::


2. Ponga un _nombre de archivo_ y haga clic en `three points` ![](/fig/Three_points.png) para guardar el archivo en el lugar del directorio elegido.
3. Seleccione el SRC correspondiente.
4. Haga clic en `ok`.

:::{figure} /fig/en_qgis_save_layer02.png
---
width: 85%
name: en_qgis_save_layer02
align: center
---
Guarde la capa en su directorio.
:::



## Faltan herramientas de procesamiento en la herramienta de paneles y la pestaña de vectores está incompleta

__Solución:__

  1. Active `Processing Tools` en `Plugins` >
  `Manage and install Plugins`.
  2. Seleccione `All`.
  3. Vuelva a marcar la función `Processing` en la lista correspondiente.

:::{figure} /fig/en_missing_processing_tools.png
---
width: 85%
name: en_missing_processing_tools
align: center
---
Vuelva a instalar la herramienta de procesamiento.
:::

Véase también: Sistemas de información geográfica
https://gis.stackexchange.com/questions/202111/missing-processing-tools-in-vector-menu-of-qgis


## Falta la caja de herramientas
__Solución:__

  1. Para reactivar la `Toolbox` ![](/fig/mAction.png) haga clic en `View Tab`.
  2. En la ventana emergente, seleccione `Panels`.
  3. En la siguiente ventana emergente marque la casilla de `Processing Toolbox`.

:::{figure} /fig/en_missing_toolbox.png
---
width: 75%
name: en_missing_toolbox
align: center
---
Reactivar caja de herramientas.
:::

## La flecha norte no se sincroniza con el mapa correspondiente
__Solución:__

Hay dos lugares en los que tiene que definir con qué mapa debe sincronizarse la flecha norte.

 En la pestaña `Layout Tab` (del diseño de impresión) para la imagen del mapa en `General Settings` asegúrese de que el mapa de referencia tiene seleccionado el mapa correcto.


:::{figure} /fig/en_qgis_correct_referenciation_to_map.png
---
width: 85%
name: en_qgis_correct_referenciation_to_map.png
align: center
---
Referencia correcta al mapa.
:::

Véase también: Sistemas de información geográfica
https://gis.stackexchange.com/questions/265095/north-arrow-not-syncing-with-map-qgis-2-18#:~:text=1%20Answer&text=2-,There%20are%20TWO%20places%20where%20you%20have%20to%20tell%20it,and%20tell%20it%20which%20map

## Geometría inválida

Si aparece el mensaje de error `Invalid Geometries`, es posible que los archivos vectoriales se hayan “desplazado” durante el procesamiento o la descarga (p. ej., las líneas de los polígonos ya no encajan exactamente).

__Solución:__

Estos errores en las geometrías pueden corregirse ejecutando `Fix Geometries`. Búsquela en la caja de herramientas de procesos.

## Sistemas de coordenadas: ¿Qué significan todos estos términos?

Los conjuntos de datos geoespaciales constan de tres datos básicos:

+ Atributos: los significados o etiquetas de un punto de datos.

+ Coordenadas: números que describen la posición del punto de datos en el espacio.

+ Sistema (de referencia) de coordenadas: metadatos que describen el espacio en sí; origen, ejes, unidades, etc.

Por ejemplo:

+ Atributos: “La Casa Blanca” o “1600 Pennsylvania Avenue”

+ Coordenadas: (-77.0367, 38.8976)

+ Sistema (de referencia) de coordenadas: WGS84 longitud, latitud



:::{Tip}
Para obtener información más detallada sobre los sistemas de coordenadas, véase también: https://ihatecoordinatesystems.com/#correct-crs
:::

## Sistemas de coordenadas: ¿Cómo puedo redefinir el sistema de coordenadas de un conjunto de datos?

Redefinir significa que se modifican los metadatos sobre el sistema de coordenadas, pero no las coordenadas. Esto contrasta con las reproyecciones y transformaciones, que modifican tanto el sistema de coordenadas como las coordenadas.

__Soluciones:__

+ En QGIS, para los conjuntos de datos vectoriales, utilice la herramienta `Assign Projection` del conjunto de herramientas `Vector General`, no la herramienta `Reproject Layer`. Véase también: https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/gdal/rasterprojections.html#assign-projection


+ En QGIS, para los conjuntos de datos ráster, utilice la herramienta `Assign Projection` del conjunto de herramientas `GDAL`, no la herramienta `Warp (Reproject)`. Véase también: https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/gdal/rasterprojections.html#assign-projection


+ Desde la línea de comandos, para conjuntos de datos vectoriales, utilice `ogr2ogr` con el parámetro `-a_srs`, no con el parámetro `-t_srs`. Véase también:
https://gdal.org/programs/ogr2ogr.html#cmdoption-ogr2ogr-a_srs


+ Desde la línea de comandos, para los conjuntos de datos ráster, utilice `gdal_edit` con el parámetro `-a_srs`. Véase también: https://gdal.org/programs/gdal_edit.html#cmdoption-a_srs.py

## Sistemas de coordenadas: ¿Por qué se utiliza Mercator si está tan distorsionado?

Mercator es la única proyección cartográfica cilíndrica conforme. Las proyecciones cartográficas cilíndricas significan que toda la Tierra se ajusta dentro de un rectángulo, lo que resulta muy conveniente para los algoritmos de procesamiento de datos que están diseñados para trabajar con imágenes rectangulares. Conforme significa que los ángulos y las formas siempre se preservan: el norte siempre está arriba, los cuadrados siguen siendo cuadrados, etc. Utilizar una proyección que no sea conforme haría que las formas se vieran estiradas, aplastadas y/o rotadas al hacer zoom.


:::{figure} /fig/qgis_mercator.jpg
---
width: 75%
name: qgis_mercator.jpg
align: center
---
Proyección Mercator.
:::

Mercator agranda las zonas más alejadas del ecuador, pero al menos esta distorsión es la misma horizontal y verticalmente. Y es trivial calcular un factor de escala para corregir las medidas (véase también: https://en.wikipedia.org/wiki/Mercator_projection#Scale_factor). 
La distorsión solo resulta problemática al visualizar un mapa a escala global, donde existe un rango amplio de factores de escala diferentes; pero la mayoría de los mapas no son de escala global y, para estos casos, existen muchas proyecciones más adecuadas para este caso.

## Sistemas de coordenadas: ¡Mi conjunto de datos no se encuentra donde debería!
Es probable que su conjunto de datos tenga un sistema de coordenadas incorrecto. Este es el caso más general del problema anterior. Esto puede ocurrir si el sistema de coordenadas falta por completo, en cuyo caso el software de SIG suele asumir que se trata del mismo sistema de coordenadas que el de un conjunto de datos cargado previamente, o del sistema de coordenadas establecido en el “proyecto” o “documento del mapa”.

__Solución:__

 Redefinir el sistema de coordenadas, redefinir, es decir, cambiar el sistema de coordenadas pero no las coordenadas, al sistema de coordenadas correcto.

1. Abra su `Project`: abra el proyecto de QGIS en el que desea redefinir el sistema de coordenadas.

2. Acceda a `Project Properties`: vaya a `Project menu` en la parte superior de la ventana de QGIS y seleccione `Properties`. También puede presionar `Ctrl + Shift + P` como un atajo.

3. Pestaña Sistema de coordenadas: en la ventana `Project Properties`, seleccione la pestaña Sistema de coordenadas.

4. Cambie el sistema de coordenadas: aquí puede seleccionar un nuevo sistema de coordenadas para su proyecto. Puede buscar un sistema de coordenadas específico utilizando la barra de búsqueda, o puede navegar por la lista de los sistemas de coordenadas disponibles.

Aplicar cambios: Una vez seleccionado el sistema de coordenadas deseado, haga clic en `OK` para aplicar los cambios. QGIS reproyectará las capas de su proyecto para que coincidan con el nuevo sistema de coordenadas.

:::{figure} /fig/en_qgis_redefining_CRS01.png
---
width: 80%
name: en_qgis_redefining_CRS01
align: center
---
Redefinir los SRC.
:::

5. Compruebe y ajuste las capas: después de redefinir el sistema de coordenadas, es esencial comprobar las capas para asegurarse de que se alinean correctamente. Algunas capas pueden requerir ajustes manuales o una reproyección si no se alinean como se esperaba.
Vuelva a revisar la parte inferior derecha de la ventana de QGIS, donde se indica el SRC real.

:::{figure} /fig/en_qgis_redefining_CRS02.png
---
width: 80%
name: en_qgis_redefining_CRS02
align: center
---
Comprobar la redefinición del SRC.
:::

## Sistemas de coordenadas: ¿En qué sistema de coordenadas debe estar mi conjunto de datos?

Los atributos de un punto de datos dan contexto sobre dónde se encuentra en la Tierra. La mayoría de los programas de SIG muestran las coordenadas mínimas y máximas en las propiedades de la capa como “extensión” o “cuadro delimitador”.

__Soluciones:__

Si los atributos indican la longitud y la latitud aproximadas en las que deben encontrarse las coordenadas, intente realizar una búsqueda inversa. Esto se repite en todos los sistemas de coordenadas bien definidos, elimina la proyección de las coordenadas X, Y a WGS84 y mide el error respecto a la longitud y la latitud conocidas. Los errores menores a unos cientos de metros indican una proyección razonable, aunque no es lo bastante preciso para determinar el SCG.
Puede ejecutar este código de ejemplo usted o utilizar este formulario:


<form>
    <table style="padding: 0.5em;width:100%;font-size:90%;">
        <colgroup>
            <col span="1" style="width: 18%;">
            <col span="1" style="width: 20%;">
            <col span="1" style="width: 18%;">
            <col span="1" style="width: 20%;">
            <col span="1" style="width: 20%;">
        </colgroup>
        <tbody>
            <tr>
                <td style="text-align:right;"><label for="lookup_lng">Longitud:</label></td>
                <td><input style="width:90%;" type="number" step="any" id="lookup_lng"
                        name="lookup_lng"></td>
                <td style="text-align:right;"><label for="lookup_lat">Latitud:</label></td>
                <td><input style="width:90%;" type="number" step="any" id="lookup_lat"
                        name="lookup_lat"><br></td>
                <td></td>
            </tr>
            <tr>
                <td style="text-align:right;"><label for="lookup_x">Coordenada X:</label></td>
                <td><input style="width:90%;" type="number" step="any" id="lookup_x" name="lookup_x">
                </td>
                <td style="text-align:right;"><label for="lookup_y">Coordenada Y:</label></td>
                <td><input style="width:90%;" type="number" step="any" id="lookup_y" name="lookup_y">
                </td>
                <td><input style="width:70%;" id="projectionLookupButton" type="submit" value="Submit">
                </td>
            </tr>
        </tbody>
    </table>
</form>
<p id="projectionLoookupLoading" style="display:none;text-align:center;">
    <span id="projectionLoookupLoadingText" class="bold italic"></span>
</p>
<table id="projectionLookupResults" style="display:none;padding:0.5em;font-size:80%;">
    <tr>
        <td><span class="bold">Código</span></td>
        <td><span class="bold">Nombre</span></td>
        <td style="text-align:right;"><span class="bold">Error (metros)</span></td>
    </tr>
</table>

<br>



+ Si las coordenadas tienen valores X entre -180 y 180, y valores Y entre -90 y 90, entonces probablemente quiera redefinir un sistema de coordenadas geográficas, o SCG, (con longitud y latitud) como WGS84.

+ Si las coordenadas tienen valores absolutos grandes, intente redefinirlas a un sistema de coordenadas local como UTM, Gauss-Krüger, State Plane o una cuadrícula nacional. También considere la posibilidad de probar con zonas vecinas, p. ej., si la zona UTM 19N es incorrecta, pruebe con la zona UTM 18N.

+ Si los atributos sugieren que el conjunto de datos está en EE. UU., podría haber un problema de conversión a/desde el sistema imperial. Pruebe a multiplicar/dividir las coordenadas de un punto de datos por 3,28084 para convertir pies a metros/metros a pies y compruebe si eso lo coloca en la ubicación correcta.

+ Si las coordenadas mínimas X/Y son cero y las máximas X/Y son positivas, es posible que el conjunto de datos se haya exportado desde un software no geoespacial, como Photoshop, Illustrator o Inkscape. Esto es especialmente probable si el conjunto de datos aparece invertido verticalmente, ya que esos editores suelen tener el eje Y aumentado hacia abajo. Tendrá que georreferenciar manualmente el conjunto de datos para utilizarlo, lo que cambia tanto las coordenadas como el sistema de coordenadas.

Véase también la siguiente [__Página_Wiki__](../Wiki/es_qgis_projections_wiki.md) sobre `Projections`.


## ¡Mi conjunto de datos está ligeramente desplazado de donde debería estar!

Es probable que su conjunto de datos tenga un sistema de coordenadas geográficas (SCG) con la longitud/latitud incorrecta. Los distintos SCG definen tamaños/formas ligeramente distintos de la Tierra (sus elipsoides) y diferentes posicionamientos sobre ella (sus datums). Como resultado, las mismas coordenadas de longitud/latitud en dos SCG diferentes pueden aparecer desplazadas, aunque normalmente con una diferencia de decenas de metros. Esto puede ocurrir incluso si está utilizando un sistema de coordenadas proyectadas (SCP) cuyas unidades no son grados de longitud/latitud, ya que los SCP tienen un SCG incrustado en ellos.

:::{figure} /fig/qgis_wrong-gcs.png
---
width: 75%
name: qgis_wrong-gcs.png
align: center
name: Offset because of wrong GCS
---
Desplazamiento por SCG erróneo. Fuente: Dan Mahr. Todos los derechos reservados. Este contenido está excluido de nuestra licencia Creative Commons.
:::

__Solución__:

 Redefina el sistema de coordenadas, es decir, cambie el sistema de coordenadas pero no las coordenadas, por uno de los siguientes:

* Intente redefinirlo al SCG WGS84.
* Si su conjunto de datos se recopiló con GPS, intente redefinirlo a WGS84.
* Si su conjunto de datos se recopiló con GLONASS, intente redefinirlo a PZ-90.
* Si su conjunto de datos se recopiló con Galileo, intente redefinirlo a ITRF.
* Si su conjunto de datos se encuentra en EE.UU., intente redefinirlo a NAD27, NAD83 o WGS84.
* Si su conjunto de datos se encuentra en Europa, intente redefinirlo a ED50, ETRS89 o WGS84.
* Si su conjunto de datos se encuentra en Australia, intente redefinirlo a GDA94 o GDA2020.
* Si su conjunto de datos se encuentra en China y/o se ha recopilado con BeiDou, buena suerte. :weary:

## Resultados erróneos o falta de datos

Si obtiene resultados erróneos o le faltan datos, compruebe los nombres de los archivos. No debe utilizar nombres de archivo con mayúsculas, caracteres especiales o espacios vacíos. Utilice siempre guiones bajos entre las palabras del nombre del archivo.

## Problemas de gestión de archivos

Puede haber diferentes razones, p. ej., al reabrir su proyecto en QGIS, no todos los archivos se mostrarán correctamente porque algunos se perdieron o se almacenaron en diferentes lugares. En cualquier caso, hay una solución: una estructura de carpetas clara.

__Solución:__

Estructura de carpetas estándar recomendada:

:::{figure} /fig/Standard_project_folder_structure.drawio.svg
---
width: 75%
name: Standard_project_folder_structure.drawio.svg
align: center
---
Estructura de carpetas estándar. Fuente: HeiGIT
:::

Cómo podría verse en su PC:

:::{figure} /fig/en_qgis_folder_structure_pc.png
---
width: 75%
name: en_qgis_folder_structure_pc.png
align: center
name: Standard folder structure on your PC
---
Estructura de carpetas estándar en su PC.
:::

La estructura de carpetas estándar tiene dos ventajas principales:
1. Al compartir toda la carpeta del proyecto, podemos garantizar que el proyecto se ejecutará sin problemas en una computadora diferente.
2. La estructura de carpetas permite la correcta organización de los datos geoespaciales y favorece el funcionamiento estable de un proyecto en QGIS.

La plantilla de estructura de carpetas puede descargarse [__aquí__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).


:::{Tip}
Los datos de capa utilizados en el proyecto no se guardan en el archivo de proyecto. En cambio, el archivo de proyecto solo contiene las rutas de los archivos donde se encontraban los datos de las capas en el momento en que el proyecto se guardó por última vez en la computadora. Si posteriormente se cambia la ubicación de estos datos de la capa, aparecerá el mensaje de error “handle unavailable layers” (gestionar capas no disponibles) cuando se vuelva a abrir el proyecto.
Una buena organización de los datos con una estructura de carpetas fija y bien elaborada evita tales problemas.
:::

Véase también la siguiente [__Página_Wiki__](https://github.com/GIScience/gis-training-resource-center/blob/main/spanish/content/es/Wiki/es_qgis_projects_folder_structure_wiki.md) para `How to create a new QGIS project` y `How to open an existing QGIS project`.

## Problemas específicos de QGIS
### Configuración básica > Desactivar la selección automática de la proyección
Después de instalar QGIS, deben modificarse algunos ajustes básicos para evitar posibles fuentes de error.
Si un archivo de capas no tiene una proyección, deberá definirse una proyección para este cuando se importe a QGIS. Al desactivar la selección automática de la proyección, esta puede definirse manualmente. Esto evita que las capas se encuentren en la proyección equivocada accidentalmente.

1. Seleccione la pestaña `Settings`.
2. A continuación, en el menú de navegación active `Options`.
3. En la ventana emergente, seleccione `CRS Handling`.
4. En `CRS for projects` active `Use CRS from first layer added`.
5. Y en `CRS for layers` active `Prompt for CRS`.

:::{figure} /fig/en_qgis_CRS_settings.png
---
width: 95%
name: en_qgis_CRS_settings.png
align: center
---
Cambiar la configuración del SRC en QGIS.
:::

### Guardar regularmente
Lamentablemente, los programas de SIG son conocidos por congelarse o fallar por completo. Aunque existe una tendencia a reducir las complicaciones con un mejor hardware, incluso una “computadora para videojuegos” que cuesta varios miles de dólares no es completamente segura.
Las tareas más complejas, con tiempos de cálculo más largos, pueden seguir causando problemas. Por ello, se recomienda guardar con regularidad.

Véase también la siguiente [__Página_Wiki__](https://github.com/GIScience/gis-training-resource-center/content/es/Wiki/es_qgis_interface_wiki.html#save-open-qgis-projects) `Save and open QGIS Projects.`

### Aplicaciones GRASS

QGIS también permite utilizar herramientas de software de SIG externo, como el SIG GRASS. GRASS no tiene que descargarse por separado, sino que se instala automáticamente al instalar QGIS. Las herramientas de GRASS se identifican por su icono.

:::{attention}
Tenga en cuenta que el software GRASS no se inicia cuando se inicia la aplicación estándar de QGIS. En consecuencia, puede aparecer un mensaje de error al utilizar las herramientas de GRASS. Esto puede remediarse abriendo QGIS con la aplicación GRASS (que se encuentra mediante la función de búsqueda de la computadora) en lugar de la aplicación estándar.
:::

### SAGA con Linux

SAGA es otro programa externo de SIG. Las herramientas SAGA se identifican por su icono. Cuando se utiliza Windows o MacOS como sistema operativo, SAGA se implementa automáticamente al instalar QGIS. Con Linux, sin embargo, SAGA no se instala automáticamente y debe instalarse manualmente. La experiencia ha demostrado que esta instalación no siempre es fácil y puede causar problemas. Como alternativa, puede utilizar una máquina virtual de Windows o MacOS, o abstenerse de utilizar las herramientas SAGA (entonces tendrá que buscar herramientas alternativas por su cuenta).

### Diéresis, caracteres especiales y espacios en las rutas de los archivos

Si la ruta del archivo contiene diéresis (ä,ö,ü), caracteres especiales (!,?, ., etc.) o espacios, pueden ocurrir problemas al procesar estos archivos con QGIS. Por ello, se recomienda evitar estos caracteres en las rutas de los archivos (sustituya las diéresis y reemplace los espacios por _).

:::{attention}
Los archivos temporales son específicos de cada usuario (si varias personas utilizan una misma PC, cada una tiene sus propios archivos temporales). Por lo tanto, la ruta del archivo contiene su nombre de usuario. Si contiene caracteres problemáticos, entonces es recomendable cambiarlo.
:::

## Enlaces de acceso a la Ayuda de QGIS

Aquí encontrará más enlaces de acceso a la ayuda o enlaces a la comunidad/foro de QGIS para tratar cuestiones específicas:

#### Tutoriales y consejos sobre QGIS:
+ Colección de tutoriales y consejos sobre QGIS: https://www.qgistutorials.com/en/

+ Manual de capacitación en QGIS: https://docs.qgis.org/3.28/en/docs/training_manual/index.html

+ Guía del usuario de QGIS: https://docs.qgis.org/3.28/en/docs/user_manual/index.html

+ Guía/manual del servidor de QGIS: https://docs.qgis.org/3.28/en/docs/server_manual/index.html

+ Manual del usuario de complementos de QGIS: https://docs.qgis.org/3.28/en/docs/user_manual/plugins/plugins.html

+ Taller y tutoriales en video de QGIS (Universidad de Harvard): https://gis.harvard.edu/qgis-workshop-and-video-tutorials-0

+ Tutorial de QGIS (CartONG): https://cartong.pages.gitlab.cartong.org/learning-corner/en/6_tutorials/6_3_gis/6_3_1_qgis

#### Comunidad/foros de QGIS:
+ Sistemas de Información Geográfica: https://gis.stackexchange.com/?tags=qgis

+ Grupos de usuarios de QGIS: https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups

#### Canales de YouTube sobre QGIS:
+ Los mejores canales de YouTube sobre QGIS y herramientas SIG de código abierto: https://hatarilabs.com/ih-en/the-best-youtube-channels-in-qgis-and-open-source-gis-tools-in-any-language
+ Guía para principiantes absolutos en QGIS: https://www.youtube.com/watch?v=NHolzMgaqwE
+ Tutorial completo de QGIS para principiantes: https://www.youtube.com/watch?v=d15Xl4OphDk
+ QGIS para principiantes: https://www.youtube.com/watch?v=Eg4_duqH5Q4
+ Introducción a QGIS: https://www.youtube.com/watch?v=kxJI5FAGjzQ

#### ChatGPT
+ Y no olvide ChatGPT https://chat.openai.com/
¡Es rápido!