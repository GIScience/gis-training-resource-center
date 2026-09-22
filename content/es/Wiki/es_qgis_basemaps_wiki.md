# Mapas base


__🔙[Volver a la página de inicio](../es_intro.md)__

Los mapas base son mapas de fondo. Suelen ser muy prácticos, ya que son fáciles de usar, permiten una fácil orientación en el lienzo del mapa y son diversos.

```{Note}
No es posible interactuar con los mapas base. ¡Solo son “imágenes” de fondo!
```

## Mapas base estándar de QGIS

Siempre puede añadir el mapa OpenStreetMap estándar como mapa base a su lienzo del mapa.

Hay dos formas de agregar el OpenStreetMap como mapa base.

__Opción 1:__ Busque `Teselas XYZ` en el panel `Navegador`. Abra el menú desplegable haciendo clic en él y seleccione OpenStreetMap u otro mapa base.

__Opción 2:__ `Capa` → `Añadir capa` → `Añadir capa XYZ...` → Seleccione el mapa de OpenStreetMap u otro mapa base.

__Añadir un mapa de OpenStreetMap estándar como mapa base__
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>

### Añadir mapas base de Google y Bing

Para añadir mapas base adicionales sin utilizar complementos, se deben configurar las `Teselas XYZ`.
En panel `Navegador`, haga clic con el botón derecho en `XYZ Tiles` → `Conexión nueva...`.

`Nombre` = El nombre del nuevo mapa base.

`URL` = Puede utilizar cualquiera de las URL de la tabla siguiente.

| Nombre | Información | URL |
| ----- | --- | --- |
| [OpenTopoMap](https://wiki.openstreetmap.org/wiki/OpenTopoMap) | Mapa topográfico de código abierto basado en OSM y SRTM |https://tile.opentopomap.org/{z}/{x}/{y}.png |
| Google Terrain||https://mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z} |
| Google Hybrid||https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z} |
| Google Satellite||https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z} |
| Google Road||https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z} |
| Solo Google Roads ||https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z} |
| Mapa de rutas alternativa de Google||https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z} |
| Bing Aerial||http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1 |

Las ventajas de usar mapas base de XYZ Tiles son:
* Cargan más rápido
* Admiten reproyección
* Permiten la impresión
* Compatibles con aplicaciones en línea como [QField](https://qfield.org/)

## Mapas base del complemento [QuickMapServices](https://nextgis.com/blog/quickmapservices/)

El complemento QuickMapServices permite acceder a una amplia gama de mapas base.

:::{Note}
¡Pueden surgir problemas al imprimir algunos mapas base desde QuickMapServices!
:::

`Web` → `QuickMapServices` → seleccionar el proveedor, p. ej., NASA → seleccionar mapa base

__Funcionalidad del complemento QuickMapServices__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>

### Configuración de QuickMapServices
Después de instalar el complemento (complementos en Wiki), necesita configurarlo para acceder a todos los mapas base.

`Web` → `QuickMapServices` → `Settings` → Use las flechas horizontales para navegar a `More Services` → `Get Contributed Pack`

## Navegación en mapa base con el complemento OSM Place Search

Con el complemento OSM Place Search, puede encontrar lugares en todo el mundo basados en OpenStreetMap. Esto significa que la búsqueda de lugares es independiente de cualquier mapa base que esté utilizando, siempre se basa en OpenStreetMap.

:::{Tip}
Si el complemento está instalado y activado, pero el panel no es visible, revise [Mover y organizar barras de herramientas y paneles](es_qgis_interface_wiki.md) en Wiki.
:::

__Funcionalidad del complemento de OSM Place Search__
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/OSM_Place_Search.mp4"></video>