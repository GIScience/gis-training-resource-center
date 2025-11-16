# Proyecciones cartográficas

__🔙[Volver a la página de inicio](/content/es/intro.md)__

## Cómo verificar el código EPSG

:::{Note}
Verifique siempre que el código del Sistema de referencia de coordenadas (SRC)/del EPSG de sus datos sea el mismo que el código SRC/EPSG de su proyecto.
:::

El código SRC/EPSG predeterminado de cada proyecto de QGIS es el World Geodetic System 84 (EPSG: 4326). Este SRC está optimizado para mapas mundiales. Por lo tanto, no es el mejor para la mayoría de las aplicaciones, ya que solemos usar mapas para áreas pequeñas.

### Cómo hacer para verificar y modificar el código EPSG/SRC de su proyecto de QGIS
:::{Note}
Verificar y modificar el código SRC o el código EPSG es lo primero que se debería hacer al iniciar un nuevo proyecto de QGIS.
:::

1. Abrir un proyecto QGIS
2. En la esquina inferior derecha de QGIS encontrará el botón `EPSG`. El número que aparece junto a él es el código EPSG utilizado actualmente en el proyecto. Para obtener más información, haga clic en el botón.
![](/fig/EPSG_Code.png)
3. Se abrirá la ventana `Project Properties`. Aquí puede ver todos los códigos SRC/EPSG disponibles y sus propiedades.
4. Para cambiar el código SRC/EPSG, seleccione el que desee utilizar y haga clic en `Apply`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

### Cómo verificar el código EPSG/SRC de una capa/datos
:::{Note}
Después de cargar cualquier dato espacial en QGIS, verifique el código SRC/EPSG de los datos para asegurarse de que sea el mismo que el código SRC/EPSG del proyecto.
:::
1. Haga clic derecho en la capa de datos y luego haga clic en “Propiedades”.
2. Se abrirá la ventana “Propiedades de capa” de la capa de datos. Haga clic en “Información”.
3. En el título “Sistema de referencia de coordenadas (SRC)” encontrará toda la información sobre el SRC. Los datos más importantes son los siguientes:
    - __Nombre:__   Aquí encontrará el código EPSG
    - __Unidades:__  Aquí puede averiguar si es posible utilizar metros con esta capa de datos o latitud y longitud.


## Modificación de la proyección cartográfica de una capa vectorial

1. `Vector` Tabulador -> `Data Management Tools` -> `Reproject Layer`
2. Seleccione el código SRC/EPSG de destino.
3. Guarde el nuevo archivo haciendo clic en los tres puntos situados junto a `Reprojected`, especifique en el nombre del archivo y la ubicación donde desea guardarlo.
5. Haga clic en `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>


## Modificación de la proyección cartográfica de una capa ráster

1. `Raster` Tabulador -> `Projections` -> `Warp (Reproject)`
2. Seleccione el código SRC/EPSG de destino.
3. Seleccione el método de remuestreo.
4. Guarde el nuevo archivo haciendo clic en los tres puntos situados junto a `Reprojected`, especifique en el nombre del archivo y la ubicación donde desea guardarlo.
5. Haga clic en `Run`

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>

## Errores comunes con los sistemas de referencia de coordenadas

El sitio web [__I Hate Coordinate Systems!__](https://ihatecoordinatesystems.com/) (¡Detesto los sistema de referencia de coordenadas!) ofrece una “guía de problemas basada en los problemas comunes de SRC, sus causas raíz y soluciones”.
