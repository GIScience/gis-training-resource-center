# Clasificación graduada


__🔙[Volver a la página de inicio](/content/es/es_intro.md)__

- La clasificación graduada en SIG consiste en categorizar los datos espaciales en **clases o rangos** basados en una progresión de valores.
- Este método es especialmente útil para visualizar datos cuantitativos, ya que permite diferenciar la intensidad, la densidad o la magnitud a lo largo de un espectro, lo que facilita una representación matizada de los fenómenos geográficos.

- La clasificación graduada se utiliza para datos cuantitativos, normalmente __intervalo__ o __relación__ escalada.

| Escala de datos | Definición | Ejemplo | Formato de datos típico |
|----------------|----------------------------------------------------|-------------------------------------|----------------------------------------------|
| Escala de intervalos | Intervalos equitativos entre valores, sin punto cero verdadero | Temperatura (Celsius) | Flotante (44,5 grados) |
| Escala de proporciones | Intervalos equitativos con un punto cero verdadero | Población, longitud, número de árboles | Entero (5 árboles) o flotante (12,5 km de carretera) |



:::{dropdown} Video: Aplicar una clasificación graduada a una capa
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/graduated_classification.mp4"></video>
:::


__Clasificar los datos en clases…__
- Haga clic derecho en su capa
- Haga clic en `Symbology`
- Haga clic en `Graduated`
- En el menú desplegable `Value` seleccione la columna en función de la cual desea clasificar sus datos.
- Seleccione el número de clases que desea utilizar.
- En `Mode` seleccione el método de clasificación que desea utilizar, por ejemplo, recuento equitativo (cuantil).
- Haga clic en `Classify`. Ahora debería ver todas las clases y la distribución de los valores. Para añadir o eliminar clases individuales utilice los botones `-` y `+`.
- *Opcional*: Haga clic en `Histogram` -> `Load Values`. Ahora puede ver la distribución exacta de los valores entre las clases. Esto resulta muy práctico para decidir un método de clasificación. También puede comprobar el valor medio y la desviación estándar.
:::{figure} /fig/Graduated_histogram.png
---
width: 900px
name: raduated classification
align: center
---
:::
- *Opcional*: En el menú desplegable `Symbol` puede seleccionar los colores y símbolos que desea utilizar.
- *Opcional*: En el menú desplegable `Color ramp` puede especificar la gama de colores que desea utilizar. Para ver todas las rampas de color, haga clic en la flecha hacia abajo de la `Color ramp` -> `All Color Ramps`.
- *Opcional*: En `Legend Format` puede ajustar la precisión con la que se mostrará el rango de las clases en la leyenda. Normalmente, es práctico no utilizar números demasiado complicados en la leyenda.
- *Opcional*: Puede abrir el panel `Layer Rendering` en el botón de la ventana. Aquí puede ajustar la opacidad/transparencia de la capa.
- Haga clic en `Apply` para aplicar el ajuste.
- Haga clic en `OK` para cerrar la ventana.

## El número de clases

- Decidir el número de clases y dónde se sitúan los rangos de las distintas clases tiene un profundo impacto en el mapa resultante.
- En QGIS existen siete formas de dividir los datos cuantitativos en clases.
- Los cuatro más importantes son: Intervalo equitativo, cuantil, cortes naturales, manual.
- En general, debe limitar el número de clases entre 3 y 9.

:::{figure} /fig/classification_method_map.drawio.svg
---
width: 750 px
name: classification_method_map_wiki
---
Impacto de las diferentes rupturas de clase en los mapas (fuente: HeiGIT, adaptado de [Axis Maps](https://www.axismaps.com/guide/data-classification)).
:::