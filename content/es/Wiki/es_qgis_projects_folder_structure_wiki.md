# Proyectos y estructura de carpetas

__🔙[Volver a la página de inicio](../es_intro.md)__

Este artículo de la Wiki trata sobre las mejores prácticas para la creación y gestión de datos geoespaciales y proyectos QGIS.


## Paso a paso: Creación de un nuevo proyecto QGIS desde cero

:::{Tip}
Una de las prácticas recomendadas consiste en utilizar una __estructura de carpetas estándar__ para los proyectos QGIS en la que se almacenen el proyecto, todos los datos geoespaciales utilizados, los archivos de estilo y la documentación.
:::

1. Copie la estructura de carpetas estándar para proyectos QGIS en el lugar donde desee almacenar todo el proyecto. Puede descargar la estructura de carpetas estándar [aqui](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).

2. Abra QGIS y cree un nuevo proyecto. Haga clic en `Proyecto` → `Nuevo proyecto`.

### Cree un nuevo proyecto en QGIS.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>

3. Guarde el nuevo proyecto en la carpeta `Proyecto` en la estructura de carpetas estándar y ejecute un git push.
4. Nombre su proyecto y haga clic en
:::{Tip}
No utilice espacios ` ` en el nombre; utilice siempre guiones bajos `_`.
:::
#### Guarde el proyecto.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_as.mp4"></video>



4. Compruebe el código del sistema de referencia de coordenadas (SRC)/EPSG del proyecto con el SRC/EPSG que desea utilizar. Para más información, consulte el artículo de la Wiki sobre [Proyección cartográfica](es_qgis_projections_wiki.md).

### Verifique y cambie el SRC/EPSG.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

:::{Tip}
Los datos de capa utilizados en el proyecto no se guardan en el archivo de proyecto. En cambio, el archivo de proyecto solo contiene las rutas de los archivos donde se encontraban los datos de las capas en el momento en que el proyecto se guardó por última vez en la computadora. Si posteriormente se cambia la ubicación de estos datos de la capa, aparecerá el mensaje de error “handle unavailable layers” (gestionar capas no disponibles) cuando se vuelva a abrir el proyecto.
Una buena organización de los datos con una estructura de carpetas fija y bien elaborada evita tales problemas.
:::

## Abrir proyectos QGIS existentes

Abra QGIS → `Proyecto` → `Abrir` → Seleccione su proyecto.

__Abrir proyecto QGIS__

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4"></video>

## Estructura de carpetas estándar

La estructura de carpetas estándar tiene dos ventajas principales:
1. Al compartir toda la carpeta del proyecto, podemos garantizar que el proyecto se ejecutará sin problemas en una computadora diferente.
2. La estructura de carpetas permite la correcta organización de los datos geoespaciales y favorece el funcionamiento estable de un proyecto en QGIS.

La plantilla de estructura de carpetas puede descargarse [__aquí__](https://github.com/GIScience/gis-training-resource-center/blob/main/fig/GIS_Project_folder_template.zip).


:::{figure} ../../../fig/Standard_project_folder_structure.drawio.svg
---
width: 800px
align: center
name: es_Standard_project_folder_structure_wikki
---
Estructura de carpetas estándar. Fuente: HeiGIT
:::

