(content:references:wiki:plugins)=
# Complementos

__🔙[Volver a la página de inicio](/content/es/es_intro.md)__

Existen muchas extensiones para QGIS, también llamadas complementos, que proporcionan funcionalidades adicionales. Si hay que llevar a cabo una tarea específica y QGIS no tiene la funcionalidad adecuada, busque un complemento. Puede buscarlo en Google o en la ventana del complemento.

Los complementos en QGIS son herramientas adicionales útiles que se pueden utilizar para facilitar algunas tareas. Los complementos son creados por desarrolladores de QGIS y otros usuarios independientes que desean ampliar las funciones básicas del software. Estos complementos están disponibles de forma gratuita en QGIS para todos los usuarios. Una vez instalados, los complementos permanecerán disponibles en QGIS.

:::{note}
No es necesario reinstalar los complementos para cada nuevo proyecto.
:::

## Instalación de complementos

Para instalar un complemento vaya a `Plugins` -> `Manage and Install Plugins…` -> `All` -> Buscar el complemento -> `Install Plugin`


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

:::{tip}
Si no encuentra una extensión específica, compruebe el uso de las mayúsculas y la correcta utilización de los espacios. Si sigue sin encontrar una extensión, es posible que tenga que habilitar las extensiones experimentales en las opciones (consulte más abajo).
:::

## Gestionar complementos

Si actualmente no utiliza complementos instalados, podría ser útil desactivarlos para evitar la saturación de las barras de herramientas y reducir loa cantidad de paneles abiertos.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Manage_plugins.mp4"></video>

## Permitir extensiones experimentales

Las extensiones experimentales son extensiones que están en desarrollo o son obsoletas, y ya no se optimizan ni se adaptan a las versiones más recientes de QGIS. No obstante, el uso de extensiones experimentales puede ser útil en los siguientes casos:

* Cuando las funciones específicas no sean compatibles con ninguna otra extensión.
* Cuando haya problemas con alguna otra extensión.
* Un tutorial utiliza una extensión específica.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Experimentel_plugins.mp4"></video>

:::{tip}
Debido a que a menudo no están optimizadas para la versión de QGIS utilizada, las extensiones experimentales pueden generar más mensajes de error u otros problemas, e incluso provocar que QGIS se bloquee. Por lo tanto, las extensiones experimentales solo deben activarse para su uso y luego permanecer desactivadas. Además, asegúrese de guardar el progreso del trabajo para evitar la pérdida de datos cuando QGIS se bloquee.
:::

### Descargar el complemento Quick OSM

Para descargar datos e importarlos a QGIS, el complemento **QuickOSM** es una buena opción. Primero es necesario instalarlo. Puede encontrarlo en la pestaña `Manage and Install Plugins`.

::::{dropdown} Cómo descargar el complemento

:::{figure} /fig/managa_install_plugins.png
---
width: 400px
align: center
name: managa_install_plugins_wiki
---
Gestionar e instalar complementos
:::

:::{figure} /fig/install_quickosm.png
---
width: 800px
name: install_quickosm_wiki
align: center
---
Instalar QuickOSM
:::
::::

Para iniciar el complemento recién instalado, haga clic en ![](fig/quickosmplugin.png) o en `vector` -> `QuickOSM`.

Siga los pasos para obtener los datos:

1. Seleccione una clave y un valor en la lista desplegable. Si no está seguro, consulte aquí: [taginfo.openstreetmap.org](https://taginfo.openstreetmap.org).

:::{figure} /fig/key_value_quickosm.png
---
width: 800px
align: center
name: key_value_quickosm_wiki
---
Elegir la clave y el valor en QuickOSM
:::

2. Limite el área escribiendo el nombre de su área de interés.

3. Despliegue la pestaña `Advanced`. Solo seleccione los tipos de datos que espera para minimizar la cantidad de errores.

:::{figure} /fig/quickosm_usage.png
---
width: 800px
align: center
name: quickosm_usage_wiki
---
Ejecutar el complemento QuickOSM
:::

4. Haga clic en `Run query`.

:::{dropdown} Cómo obtener datos para varias consultas

Si desea obtener más datos en la misma área, puede agregar una consulta haciendo clic en el icono ![](fig/plus_quickosm.png). Tenga cuidado al elegir el operador lógico correcto `And` o `Or`. Si no está seguro, consulte la [Wiki](/content/es/Wiki/es_qgis_non_spatial_queries_wiki).

:::