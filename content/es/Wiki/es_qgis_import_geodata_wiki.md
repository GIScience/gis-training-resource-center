# Importación de datos geográficos en QGIS


__🔙[Volver a la página de inicio](/content/es/intro.md)__

## Importación de datos vectoriales

:::{Tip}
Al importar un archivo shapefile mediante la función arrastrar y soltar, debe utilizar el archivo con la terminación .shp.
:::

### Abrir capa vectorial

#### Abrir datos vectoriales mediante la pestaña Layer

1. Haga clic en `Layer`-> `Add Layer`-> `Add Vector Layer`.
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo ráster.
3. Seleccione el archivo y haga clic en `Open`
4. Nuevamente en QGIS, haga clic en `Add`


<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>


#### Abra los datos vectoriales mediante la función arrastrar y soltar

1. En el explorador de archivos, abra la carpeta con los datos vectoriales que desea importar.
2. Arrástrelo y suéltelo en el lienzo del mapa de QGIS.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>

## Importación de datos ráster

### Abrir datos ráster mediante la pestaña Layer

1. Haga clic en `Layer`-> `Add Layer`-> `Add Raster Layer`.
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo ráster.
3. Seleccione el archivo y haga clic en `Open`
4. Nuevamente en QGIS, haga clic en `Add`

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>


### Abra los datos ráster mediante arrastrar y soltar

1. En el explorador de archivos, abra la carpeta con los datos ráster que desea importar.
2. Arrástrelo y suéltelo en el lienzo del mapa de QGIS.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

### Abrir archivos ráster NetCDF

1. `Layer` -> `Add Layer` -> `Add Raster Layer` -> Seleccione su archivo -> haga clic en `add`
2. Se abrirá una ventana en la que deberá seleccionar el conjunto de datos exacto que desea utilizar. -> Haga clic en `add Layers`
3. Haga clic en ? en la ventana Layers. Se abrirá la ventana `Coordination Reference System Select`. -> Seleccione el sistema de referencia correcto-> Haga clic en `OK`

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_NetCDF_raster.mp4"></video>


## Importación de datos de texto

:::{tip}
Para cargar directamente datos .csv o EXCEL en QGIS, los conjuntos de datos deben tener columnas que contengan geometría en forma de latitud (campo Y) y longitud (campo X).
:::

### Abrir datos .csv en QGIS

:::{mote}
Al cargar datos vectoriales en formato de texto como .csv o .txt en QGIS, estos datos tienen que tener columnas de latitud y longitud.
* `X field` = “LONGITUD”
* `Y field` = “LATITUD”
:::

1. `Layer` -> `Add Layer` ->`Open Delimited Text Layer`.
2. Haga clic en `File name` haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo CSV y haga clic en `Open`.
3. En la ventana “Data Source manager | Delimited Text” de QGIS encontrará varios menús desplegables
    * `File Format`: Aquí puede especificar qué delimitador se utiliza en el archivo que desea importar. En un archivo estándar `.csv` se utilizan comas `,`. Si no es el caso, seleccione `Custom delimiters`. Aquí puede elegir el delimitador exacto utilizado en su archivo.
    :::{tip}
    Para averiguar qué delimitador se utiliza, puede abrir el archivo .csv en el Bloc de notas o en Excel. Allí puede comprobar qué delimitador se utiliza para separar la información.
    :::
    * `Record and Fields Options`: En este menú desplegable, puede indicar a QGIS que detecte el tipo de datos de las distintas columnas del campo y que detecte las cabeceras de las columnas. Por lo general, aquí no se debe realizar ningún ajuste.
    * `Geometry definition`: En esta sección se especifica qué columnas del archivo contienen la información espacial para georreferenciar los datos en el mapa. Si el archivo tiene una columna con datos de __latitud__ y otra con datos de __longitud__, puede utilizarlas para georreferenciar los datos. Verifique `Point Coordinates`. Seleccione para `X field` "LONGITUD" y para `Y field` "LATITUD".
        Debajo, seleccione `Geometry CRS`el sistema de referencia de coordenadas (SRC). De manera predeterminada, QGIS seleccionará el SRC del proyecto.
        Si el archivo no contiene información espacial, elija la opción `No geometry (attribute only table)`.
4. Haga clic en `Add`

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

### Abrir archivos .xlsx en QGIS

1. Arrastre y suelte el archivo .xlsx en QGIS.
2. Si el fichero contiene varias tablas, seleccione la tabla con la que desea trabajar. Haga clic en `add Layers`
3. haga clic en la pestaña `Processing` -> `Toolbox` -> busque la herramienta `Create points layer from table`
4. Seleccione su tabla como `Input Layer`
5. Seleccione la columna de longitud para `X field` y la columna de latitud para `Y field`
6. Haga clic en `Run`

:::{tip}
Otra opción es siempre transformar el archivo .xlsx en .csv, que es más fácil de abrir en QGIS.
:::

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_xlsx.mp4"></video>





