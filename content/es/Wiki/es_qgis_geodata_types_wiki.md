# Tipos de datos geográficos


__🔙[Volver a la página de inicio](/content/es/intro.md)__

* Datos vectoriales
* Datos ráster
* Datos no espaciales transformados en datos geográficos

# Datos vectoriales

Los datos vectoriales pueden tener los siguientes formatos de datos:

| Extensión de nombre de archivo | Nombre | Descripción |
|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `.shp` | Shapefile | Formato de datos geográficos obsoleto, pero aún ampliamente utilizado. Solo puede contener un conjunto de datos. Un archivo shapefile **debe incluir** estos archivos: `.shp`, `.shx`, y `.dbf`. También puede contener más archivos, como por ejemplo: `.prj`, `.sbn`, `.sbx`, `.cpg`, `.qix` |
| `.gpkg` | GeoPackage | Formato de datos geográficos muy versátil y el nuevo estándar para datos geográficos. Puede contener múltiples archivos de datos (vectoriales, ráster y datos no espaciales como tablas) |
| `.kml` | Lenguaje de marcado Keyhole | Formato de datos geográficos para su uso con [Google Earth](https://earth.google.com/web/) |
| `.gpx` | Formato de intercambio GPS | Formato de datos geográficos para el intercambio de coordenadas. Por ejemplo, para los puntos de referencia de las rutas. |
| `.geojson` | GeoJSON | Similar a los archivos shapefile, pero almacena toda la información en un solo archivo. |

# Datos ráster

Los datos ráster pueden tener los siguientes formatos de datos:
| Extensión del archivo  | Nombre         | Descripción                |
|---------------------|-----------------------|---------------------------------------------|
| `.tif`/`.tiff`/`.geotiff` | Formato de archivo de imagen etiquetada | Formato común de datos ráster y de imagen. No necesariamente contiene información georreferenciada. Si un archivo .tif contiene información georreferenciada, se denomina GeoTIFF. |
| `.nc`  | netCDF    | Formato de datos estándar para datos científicos como la velocidad o la temperatura. Puede ser un archivo ráster. Puede contener varios conjuntos de datos    |
| `.asc`   | Archivos de cuadrícula ASCII de Esri | Formato de archivo ráster simple antiguo, siempre con información georreferenciada     |

## Datos de texto

| Extensión de nombre de archivo | Nombre | Descripción |
|--------------------|------------------------|-----------------------------|
| `.xls` | EXCEL | Formato de datos utilizado para EXCEL. EXCEL es un programa de hojas de cálculo muy utilizado. |
| `.csv` | valores separados por comas | Formato de datos muy común que separa los datos con comas u otros delimitadores. |

## Buenas prácticas

El siguiente video ofrece una buena visión general de los formatos de datos geográficos y proporciona consejos sobre cómo nombrar archivos y otras buenas prácticas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kggwFZHXCl4?si=i2lLEo0u0wGdB759" title="Reproductor de video de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>