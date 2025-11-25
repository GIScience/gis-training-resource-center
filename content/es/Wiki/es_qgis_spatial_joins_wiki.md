# Uniones espaciales


__🔙[Volver a la página de inicio](/content/es/es_intro.md)__


## Une atributos por ubicación

- Añada atributos adicionales de la capa de unión a la capa de entrada en función de la __relación espacial__.
- `Input Layer`: conjunto de datos que desea enriquecer
- `Join layer`: conjunto de datos con información/atributos adicionales
- Puede especificar qué campos de la capa de unión se deben agregar

:::{dropdown} Ejemplo: Añada la zona horaria (capa de unión) a las ciudades (capa de entrada)
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_spatial_join_wiki.mp4"></video>
:::

## Une atributos por ubicación (resumen)
- Añada atributos adicionales de la capa de unión a la capa de entrada en función de la __relación espacial__.
- `Input Layer`: conjunto de datos que desea enriquecer
- `Join layer`: conjunto de datos con información/atributos adicionales
- Además, calcule los resúmenes estadísticos de los valores de las entidades coincidentes en la segunda capa
    - Opciones: min, max, mean, count, sum

:::{dropdown} Solución: Calcule la suma de la población afectada y el área inundada para el área de interés
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_exercise_spatial_join.mp4"></video>
:::

## Unión de relaciones espaciales

::::{tab-set}

:::{tab-item} Interseca
Compruebe si la geometría de las dos capas se intersecan entre sí. Devuelva 1 (verdadero) si las geometrías se interseca espacialmente (comparten cualquier porción del espacio, podrían superponerse o tocarse) y 0 si no lo hacen. En la imagen de arriba, esto devolverá los círculos 1, 2 y 3.
:::

:::{tab-item} Contiene
Devuelva 1 (verdadero) si y solo si no hay puntos de b en el exterior de a, y al menos un punto del interior de b se encuentra en el interior de a. En la imagen, no se devuelve ningún círculo, pero el rectángulo si se buscara, el resultado sería en sentido inverso, ya que contiene completamente al círculo 1. Esto es lo opuesto a estar dentro.
:::

:::{tab-item} No interseca
Devuelva 1 (verdadero) si las geometrías no comparten ninguna porción de espacio (sin superposición ni tocase). Solo se devuelve el círculo 4.
:::

:::{tab-item} Igual
Devuelva 1 (verdadero) si las geometrías son exactamente las mismas. No se devolverán círculos.
:::

:::{tab-item} Toque
Compruebe si una geometría toca a otra. Devuelva 1 (verdadero) si las geometrías tienen al menos un punto en común, pero sus interiores no se intersecan. Solo se devuelve el círculo 3.
:::

:::{tab-item} Superpuesta
Compruebe si las geometrías se superponen. Devuelva 1 (verdadero) si las geometrías comparten espacio, son de la misma dimensión, pero no están completamente contenidas entre sí. Solo se devuelve el círculo 2.
:::

:::{tab-item} Dentro de
Compruebe si una geometría está dentro de otra. Devuelva 1 (verdadero) si la geometría a está completamente dentro de la geometría b. Solo se devuelve el círculo 1.
:::

:::{tab-item} Cruza
Devuelva 1 (verdadero) si las geometrías suministradas tienen algunos puntos interiores en común, pero no todos, y el cruce real es de una dimensión menor que la geometría suministrada más alta. Por ejemplo, una línea que cruza un polígono se cruzará como una línea (verdadero). Dos líneas que cruzan se cruzarán como un punto (verdadero). Dos polígonos se cruzan como un polígono (falso). En la imagen, no se devolverán círculos.
:::

::::