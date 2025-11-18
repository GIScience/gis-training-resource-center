::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/es_intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Centroides

Este proceso crea una nueva capa de puntos, con puntos que representan los centroides de las geometrías de la capa de entrada.

El centroide es un punto único que muestra el centro de todas las partes de una entidad geográfica. Puede estar fuera de la entidad geográfica o en cada una
de sus partes.

Los atributos de los puntos de la capa de salida son los mismos que los de las entidades originales.

Los centroides son especialmente útiles a la hora de crear [mapas con símbolos graduados](https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_qgis_styling_vector_data.html#creating-a-graduated-symbols-map), ya que el tamaño de los símbolos de puntos puede ajustarse según el método de clasificación graduada.

:::{figure} /fig/en_centroids_screenshot.png
---
width: 650 px
name: en_qgis_centroids
---
Los puntos negros representan los centroides de las entidades de la capa de entrada.
:::


