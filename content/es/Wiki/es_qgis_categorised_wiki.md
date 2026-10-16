## Clasificación por categorías


__🔙[Volver a la página de inicio](../es_intro.md)__

La clasificación por categorías en QGIS agrupa los datos espaciales en categorías distintas con base en atributos específicos. Esta clasificación mejora la organización e interpretación de la información geoespacial para obtener conclusiones más claras.

La clasificación por categorías suele utilizarse para los datos con escala __nominal__ y __ordinal__.

| Escala de datos | Definición | Ejemplo | Formato de datos típico |
|---|---|---|---|
| Escala nominal | Categorías sin orden ni clasificación inherentes | Tipos de cobertura terrestre, distritos, zonas de subsistencia | Texto (“Desierto”) o número entero (5) |
| Escala ordinal | Categorías con un orden o clasificación significativos | Rangos (p. ej., bajo, medio) | Texto (“alto”) o número entero (5) |

:::{dropdown} Video: Clasificación de datos
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>
:::

__Para clasificar los datos en categorías…__
- Haga clic derecho en su capa.
- Haga clic en `Simbología`.
- Haga clic en `Categorizado`.
- En el menú desplegable `Valor`, seleccione la columna con la que desee categorizar sus datos.
- Más abajo, haga clic en `Clasificar`. Ahora debería ver todos los valores o atributos únicos de la columna seleccionada en `Valor`. Para añadir o borrar valores individuales, utilice los botones `-` y `+`.
- *Opcional*: en el menú desplegable `Símbolo`, puede seleccionar los colores y símbolos que desea utilizar.
- *Opcional*: en el menú desplegable `Rampa de color`, puede especificar la gama de colores que desea utilizar.
- *Opcional*: Puede abrir el panel `Representación de la capa` en el botón de la ventana. Aquí puede ajustar la opacidad/transparencia de la capa.
- Haga clic en `Aplicar` para aplicar el ajuste.
- Haga clic en `Aceptar` para cerrar la ventana.

:::{figure} ../../../fig/Categorized_district_map_SierraLeone.png
---
name: es_Categorized_district_map_SierraLeone
align: center
---
:::
