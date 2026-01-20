# Importación de datos geográficos en QGIS


__🔙[Volver a la página de inicio](/content/es/es_intro.md)__

## Importación de datos vectoriales

:::{Tip}
Al importar un archivo shapefile mediante la función arrastrar y soltar, debe utilizar el archivo con la terminación .shp.
:::

### Abrir capa vectorial

#### Abrir datos vectoriales mediante la pestaña Layer

1. Haga clic en `Capa` → `Añadir capa` → `Añadir capa vectorial`.
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo vectorial.
3. Seleccione el archivo y haga clic en `Abrir`.
4. Nuevamente en QGIS, haga clic en `Añadir`.


<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>


#### Abra los datos vectoriales mediante la función arrastrar y soltar

1. En el explorador de archivos, abra la carpeta con los datos vectoriales que desea importar.
2. Arrástrelo y suéltelo en el lienzo del mapa de QGIS.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>

## Importación de datos ráster

### Abrir datos ráster mediante la pestaña Layer

1. Haga clic en `Capa` → `Añadir capa` → `Añadir capa ráster`.
2. Haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo ráster.
3. Seleccione el archivo y haga clic en `Abrir`.
4. Nuevamente en QGIS, haga clic en `Añadir`.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>


### Abra los datos ráster mediante arrastrar y soltar

1. En el explorador de archivos, abra la carpeta con los datos ráster que desea importar.
2. Arrástrelo y suéltelo en el lienzo del mapa de QGIS.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

### Abrir archivos ráster NetCDF

1. `Capa` → `Añadir capa` → `Añadir capa ráster` → Seleccione su archivo → haga clic en `Añadir`.
2. Se abrirá una ventana en la que deberá seleccionar el conjunto de datos exacto que desea utilizar → Haga clic en `Añadir capa`.
3. Haga clic en ? en la ventana Layers. Se abrirá la ventana `Seleccionar sistema de referencia de coordenadas` → Seleccione el sistema de referencia correcto → Haga clic en `Aceptar`.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_NetCDF_raster.mp4"></video>


## Importación de datos de texto

:::{tip}
Para cargar directamente datos .csv o EXCEL en QGIS, los conjuntos de datos deben tener columnas que contengan geometría en forma de latitud (campo Y) y longitud (campo X).
:::

### Abrir datos .csv en QGIS

:::{mote}
Al cargar datos vectoriales en formato de texto como .csv o .txt en QGIS, estos datos tienen que tener columnas de latitud y longitud.
* `Campo X` = “LONGITUD”
* `Campo Y` = “LATITUD”
:::

1. `Capa` → `Añadir capa` → `Añadir capa de texto delimitado`.
2. Haga clic en `Nombre de archivo` haga clic en los tres puntos ![](/fig/Three_points.png) y navegue hasta su archivo CSV y haga clic en `Abrir`.
3. En la ventana “Data Source manager | Delimited Text” de QGIS encontrará varios menús desplegables
    * `Formato de archivo`: Aquí puede especificar qué delimitador se utiliza en el archivo que desea importar. En un archivo estándar `.csv` se utilizan comas `,`. Si no es el caso, seleccione `Delimitadores personalizados`. Aquí puede elegir el delimitador exacto utilizado en su archivo.
    :::{tip}
    Para averiguar qué delimitador se utiliza, puede abrir el archivo .csv en el Bloc de notas o en Excel. Allí puede comprobar qué delimitador se utiliza para separar la información.
    :::
    * `Opciones de registros y campos`: En este menú desplegable, puede indicar a QGIS que detecte el tipo de datos de las distintas columnas del campo y que detecte las cabeceras de las columnas. Por lo general, aquí no se debe realizar ningún ajuste.
    * `Definición de geometría`: En esta sección se especifica qué columnas del archivo contienen la información espacial para georreferenciar los datos en el mapa. Si el archivo tiene una columna con datos de __latitud__ y otra con datos de __longitud__, puede utilizarlas para georreferenciar los datos. Verifique `Coordenadas del punto`. Seleccione para `Campo X` "LONGITUD" y para `Campo Y` "LATITUD".
        Debajo `SRC de la geometría` seleccione el sistema de referencia de coordenadas (SRC). De manera predeterminada, QGIS seleccionará el SRC del proyecto.
        Si el archivo no contiene información espacial, elija la opción `Ninguna geometría (tabla solo de atributos)`.
4. Haga clic en `Añadir`.

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

### Abrir archivos .xlsx en QGIS

1. Arrastre y suelte el archivo .xlsx en QGIS.
2. Si el fichero contiene varias tablas, seleccione la tabla con la que desea trabajar. Haga clic en `Añadir capa(s)`.
3. haga clic en la pestaña `Procesos` → `Caja de herramientas de Procesos` → busque la herramienta `Crear capa de puntos a partir de tabla`.
4. Seleccione su tabla como `Capa de entrada`.
5. Seleccione la columna de longitud para `Campo X` y la columna de latitud para `Campo Y`.
6. Haga clic en `Ejecutar`. 

:::{tip}
Otra opción es siempre transformar el archivo .xlsx en .csv, que es más fácil de abrir en QGIS.
:::

<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_xlsx.mp4"></video>





