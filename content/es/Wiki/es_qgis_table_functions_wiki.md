# Manipulación de la tabla de atributos

__🔙[Volver a la página de inicio](/content/es/intro.md)__

## Agregar campo

- Agrega un campo a la tabla de atributos.

:::{Attention}
Dependiendo de la información que se vaya a introducir en el campo de atributo, se debe seleccionar el tipo de dato correcto.
:::

:::{dropdown} Ejemplo: Agregue un campo para la densidad de población, tipo de dato: Float, Double o Real (números de punto flotante)
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_add_field_wiki.mp4"></video>
:::

## Borrar campo

- Borra un campo de la tabla de atributos.

:::{dropdown} Ejemplo: Borre todos los campos no utilizados/innecesarios de la capa.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_delete_field_wiki.mp4"></video>
:::

## Calcular campo

- Calcula los valores de los atributos de un campo, por ejemplo, basándose en los valores de otros campos.
- En QGIS se puede crear un campo nuevo o actualizar uno existente.

:::{Attention}
Compruebe que el tipo de datos del campo y su cálculo coincidan. Por ejemplo, si está calculando una relación (por ejemplo, densidad), el campo no debe ser de tipo entero.
:::

:::{dropdown} Ejemplo: Calcula la densidad de población utilizando los campos ya existentes Población y Área.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_calculate_field_wiki.mp4"></video>
:::

## Estadísticas básicas para campos

- Genera una estadística para un campo específico en la tabla de atributos.

:::{dropdown} Ejemplo: Estadísticas sobre la densidad de población en todos los países: ¿Cuál es el valor máximo, el promedio, etc.?
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_field_stats_wiki.mp4"></video>
:::

## Estadísticas por categorías

- Crea estadísticas agregadas para las categorías.
- ¿Para qué campos de la tabla de atributos se deben calcular las estadísticas?
- ¿Qué campo de la tabla de atributos contiene la categoría?

:::{dropdown} Ejemplo: ¿Cuántas ciudades con más de 300 000 habitantes hay por país? Para cada país: ¿Cuántas personas viven en la mayor aglomeración urbana?
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_stats_by_category_wiki.mp4"></video>
:::