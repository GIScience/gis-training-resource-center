::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Preparación

En este capítulo, prepararemos la configuración para la capacitación. Esto incluye la instalación de QGIS, la configuración de una estructura de carpetas para todos los datos de la capacitación y cómo administrar el material descargado. El primer paso será instalar QGIS. Después de eso, configuraremos una estructura de carpetas para la capacitación, así como repasaremos algunos pasos para mantener limpia su administración de datos.

## Guía rápida QGIS 3.34.12: instalación y configuración básica

<iframe width="800" height="515" src="https://youtube.com/embed/ck4PjoOIwMQ?si=8HHR03VzpyuhXOmr" title="Reproductor de video de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Descarga e instalación de QGIS

QGIS es de código abierto y por lo tanto, está disponible de forma gratuita para todas las personas. Puede instalar QGIS para computadoras Windows, Mac y Linux. La instalación de QGIS es muy sencilla. Dependiendo de su sistema operativo (Windows, Mac o Linux), hay algunos aspectos que debe tener en cuenta. A continuación, encontrará recomendaciones sobre cómo instalar QGIS en distintos sistemas operativos.

:::{Warning}

Hay varias versiones de QGIS disponibles para descargar. Se recomienda utilizar la versión __Long Term Release__ porque es la más estable y contiene la menor cantidad de errores.
La versión actual de __Long Term Release__ es __[QGIS 3.40.4. 'Bratislava'](https://qgis.org/download/)__

:::

### Descargar QGIS

1. Vaya a la [__página de descarga de QGIS__](https://www.qgis.org/en/site/forusers/download.html).
2. Seleccione `Download for Windows`, `Download for macOS` o `Download for Linux`, en función de su sistema operativo.
3. Haga clic en `Looking for the most stable version? Get QGIS 3.34 LTR`

:::{figure} /fig/QGIS_download_LTR_version.png
---
width: 600 px
name: QGIS_download_LTR_version
align: center
---
La página de descarga de QGIS 3.34.
:::

4. Se iniciará la descarga.
5. Localice el archivo descargado (generalmente en su carpeta Descargas) y ejecútelo para iniciar el instalador
6. ¡Siga las instrucciones del instalador para instalar QGIS!

## Consideraciones específicas del sistema operativo

:::::{tab-set}

::::{tab-item} Instalación en Windows

__¿32 bits o 64 bits?__
Para __sistemas operativos Windows__, siempre hay una versión de 32 bits y una versión de 64 bits de cada versión de QGIS disponible para descargar. La versión que se instale depende del equipo y del sistema operativo. Si no está claro cuántos bits tiene su sistema operativo, puede averiguarlo fácilmente: Haga clic con el botón izquierdo en el __icono de Windows__ en la parte inferior izquierda de la pantalla (alternativamente, abra la función de búsqueda de Windows). Escriba __“Sistema”__ en el teclado, haga clic en la entrada __“Sistema”__ en los resultados de la búsqueda. En el apartado __“Tipo de sistema”__ puede ver el número de bits.

:::{Note}

Desde QGIS 3.20, solo hay ejecutables de Windows de 64 bits.

:::

::::

::::{tab-item} Instalación en Linux

Para la instalación en sistemas Linux con `apt` puede instalar QGIS:

```
sudo apt install qgis qgis-plugin-grass
```


En las fuentes convencionales de paquetes APT, probablemente se instalará una versión anterior de QGIS. Si está utilizando el paquete [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), tenga en cuenta las siguientes [notas](https://qgis.org/en/site/forusers/alldownloads.html#repositories) de instalación.

Si instala una versión 3.30 o superior de QGIS, debe instalar el plugin
_Processing Saga NextGen Provider_.

::::

:::::

## Configuración de una estructura de carpetas para la capacitación

Mantener organizados sus datos y archivos de proyecto es la clave para trabajar con éxito en el software de los SIG. Estos ejercicios en esta plataforma requieren que descargue datos geoespaciales y los procese por su cuenta. Para mantener todo organizado, le recomendamos que cree una estructura de carpetas para todos los datos y el material descargado en el curso de esta capacitación.

- Cree una carpeta en la ubicación que elija con el nombre `GIS_Training`
- Al descargar los datos de los ejercicios, cree subcarpetas para cada módulo y ejercicio de la capacitación (p. ej. `/GIS_Training/Module_1/Exercise_1`)
- Guarde todos los proyectos QGIS, así como el material descargado para los ejercicios en estas carpetas.

En el [módulo 2](/content/es/Module_2/es_qgis_geodata_concept.md) se profundizará en la gestión de datos geoespaciales y se introducirá una estructura de carpetas estándar para proyectos QGIS.

:::{note}

Antes de comenzar los ejercicios, asegúrese de descomprimir los archivos.

:::

## Preguntas de autoevaluación

:::{admonition} Compruebe lo aprendido
:class: note
Tómese un momento para sintetizar lo que ha aprendido en este módulo, asegurándose de tener las siguientes competencias:

1. __Saber cómo descargar la versión más reciente de QGIS.__
2. __Saber cómo configurar su propia estructura de carpetas estándar.__

:::
