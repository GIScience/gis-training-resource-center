# Instalación de QGIS

__🔙[Volver a la página de inicio](../es_intro.md)__

QGIS es de código abierto y por lo tanto, está disponible de forma gratuita para todas las personas. Puede instalar QGIS en computadoras Windows, Mac y Linux.

Generalmente, recomendamos usar la última versión a largo plazo, porque es la más estable y contiene el menor número de errores.

Puede descargar la última versión aquí:

1. Vaya a la [__página de descarga de QGIS__](https://www.qgis.org/en/site/forusers/download.html).
2. Seleccione `Download for Windows`, `Download for macOS` o `Download for Linux`, dependiendo de su sistema.
3. Haga clic en `Looking for the most stable version? Get QGIS 3.28 LTR`.


## Consideraciones específicas de Windows

### ¿32 bits o 64 bits?
Para __sistemas operativos Windows__, siempre hay una versión de 32 bits y una versión de 64 bits de cada versión de QGIS disponible para descargar. La versión que se instale depende del equipo y del sistema operativo. Si desconoce cuántos bits tiene su sistema operativo, puede averiguarlo fácilmente: Haga clic con el botón izquierdo en el __icono de Windows__ en la parte inferior izquierda de la pantalla (alternativamente, abra la función de búsqueda de Windows). Escriba __"Sistema"__ en el teclado, haga clic en la entrada __"Sistema"__ en los resultados de la búsqueda. En el apartado __"Tipo de sistema"__ puede ver el número de bits.

:::{Note}
Desde QGIS 3.20, solo hay ejecutables de Windows de 64 bits.
:::

## Consideraciones específicas de Mac


:::{Note}
A partir de la versión 3.30 SAGA debe integrarse a través del [instalador del complemento](es_qgis_plugins_wiki.md).
:::

## Consideraciones específicas de Linux

Puede instalar QGIS en el sistema Linux a través de `apt`:

```
sudo apt install qgis qgis-plugin-grass
```

:::{Note}
A partir de la versión 3.30 SAGA debe integrarse a través del [instalador del complemento](es_qgis_plugins_wiki.md).
:::



