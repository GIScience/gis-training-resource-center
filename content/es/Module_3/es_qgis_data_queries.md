::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/es/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Selección y consulta de datos geoespaciales

La selección y consulta de datos geoespaciales en QGIS permite seleccionar partes específicas de conjuntos de datos espaciales. Puede utilizarse para filtrar y analizar la información geoespacial, que son tareas esenciales cuando se trabaja con datos espaciales.
\
\
Existen tres tipos generales de selección o consulta en QGIS que cubrirán la mayoría de sus necesidades:\
**1. Selección manual.** Consiste en la selección manual de entidades con una de las diversas herramientas de selección que ofrece QGIS.

**2. Selección basada en atributos.** Esta selección se basa en los valores de los atributos almacenados en la tabla de atributos.

**3. Selección espacial basada en capas.** Selección de entidades de una capa en función de relaciones geométricas especificadas con entidades de otra capa.


::::{admonition} ¡Ahora es su turno!

La consulta de datos es esencial para comprender y manipular sus conjuntos de datos. Puede seguir los pasos que se indican más abajo descargando [este conjunto de datos](https://datacatalog.worldbank.org/search/dataset/0038272/World-Bank-Official-Boundaries).

:::{card}
:class-card: sd-text-justify sd-rounded-3 sd-border-2
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Module_3_world_bank_official_boundaries.zip

__Descargar Official Boundaries del Banco Mundial__

:::

::::

## Selección manual

La selección manual se realiza principalmente mediante una de las herramientas de selección basadas en clics disponibles en la barra de herramientas del proyecto (alternativa: `Edit` > `Select`). Entre ellas figuran `Select Feature(s)`, `Select Feature by Polygon`, `Select Feature by Freehand` y `Select Feature by Radius`.
\
\
Ejemplo: `Select Feature(s)`

1.	Haga clic en `Select Feature(s)` en el menú desplegable de ![](/fig/mActionSelectRectangle.png).
2.	Seleccione las entidades haciendo clic en ellas o dibujando un rectángulo que se superponga a ellas.
3.	Utilice la herramienta fuera de las entidades seleccionables para finalizar la selección.

:::{Tip}
Si mantiene presionada la tecla “Shift” durante la selección por clic, podrá seleccionar varias entidades.
:::

:::{dropdown} Ejemplo: Selección manual de polígonos de países haciendo clic
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_features_by_click_wiki.mp4"></video>

:::

Las otras opciones de ![](/fig/mActionSelectRectangle.png) funcionan de forma similar, seleccionando todas las entidades que se superponen con la geometría respectiva generada por las herramientas.

1. Haga clic en `Select Feature(s) by Polygon` en el menú desplegable de ![](/fig/mActionSelectRectangle.png).
2. Seleccione las entidades haciendo clic izquierdo alrededor de las entidades que desea seleccionar.
3. Haga clic derecho cuando haya terminado de dibujar el polígono.

:::{dropdown} Ejemplo: Selección manual de países mediante un polígono
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_select_features_by_polygon.mp4"></video>

:::

:::{Note}
Las entidades seleccionadas se resaltan en amarillo brillante en la vista geoespacial y en azul en la tabla de atributos.
:::

## Selección por atributos

Se puede realizar una consulta basada en atributos específicos utilizando la herramienta `Select Features by Expression` disponible en ![](/fig/mActionSelectbyExpression.png) en la barra de herramientas del proyecto y la tabla de atributos (alternativa: `Edit` > `Select` > `Select` Entidades por expresión).

1.	En la interfaz de herramientas, amplíe `Fields and Values` en el panel derecho.
2.	Elija el campo en el que desea basar su selección haciendo doble clic sobre él (ahora debería aparecer en el panel de expresión de la izquierda).
3.	Utilice una expresión con operadores particulares para especificar su selección en el panel izquierdo (p. ej., “'continent' LIKE 'Asia'” para seleccionar todas las entidades con el valor “Asia” en el campo “continente” ).


:::{Tip}
Haga clic en `Show Values` en la esquina superior derecha cuando se selecciona un campo para obtener una visión general sobre los diferentes valores del campo respectivo haciendo clic en `All Unique`/`10 Samples`. Haga doble clic en los valores para utilizarlos en el panel de expresiones de la izquierda.
:::

::::{tab-set}

:::{tab-item} Operadores de comparación
| Operador | Función            |
|----------|--------------------------|
| __=__    | igual a                   |
| __!=__   | no igual                |
| __<__    | menor que                |
| __>__    | mayor que             |
| __<=__   | menor o igual a    |
| __>=__   | mayor o igual a |
:::

:::{tab-item} Operadores lógicos
Se pueden utilizar operadores como AND u OR para combinar diferentes consultas o criterios.
| Operador | Función          |
|----------|------------------------|
| __AND__  | lógico Y            |
| __OR__   | lógico O             |
| __NOT__  | lógico NO            |
:::

:::{tab-item} Operadores especiales
| Operador      | Función                                  |
|---------------|------------------------------------------------|
| __LIKE__      | concordancia de patrones                               |
| __IN__        | comprueba si un valor está en una lista de valores       |
| __IS NULL__   | comprueba si hay valores NULL                         |
| __BETWEEN__   | comprueba si un valor está dentro del rango especificado  |
| __CASE WHEN__ | expresiones condicionales                        |
:::

::::

:::{dropdown} Ejemplo: Seleccione todos los polígonos de países que compartan el valor “Asia” en el campo “continente”.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_like_wiki.mp4"></video>
:::

## Selección espacial por capas
La selección espacial de entidades permite seleccionar partes de una capa según su relación con entidades de otra capa geoespacial (p. ej., la selección de todas las entidades de punto de la capa A que se encuentren dentro de una entidad de polígono de la capa B). Para ello, utilice la herramienta “Select by Location” disponible en ![](/fig/mActionSelectbyLocation.png) en la barra de herramientas del proyecto (alternativa: `Vector` > `Research Tools` > `Select by Location`).

1.	En la interfaz de la herramienta, elija la capa vectorial de la que desea seleccionar entidades mediante “Select features from” y la capa en la que desea basar la selección mediante “By comparing to the features from”.
2.	Elija el operador geométrico que utilizará para seleccionar las entidades (véase el párrafo inferior).
3.	En la ventana inferior, elija cómo desea proceder con las nuevas entidades seleccionadas. Las opciones incluyen:
    1.	Crear una nueva selección.
    2.	Añadir a la selección actual.
    3.	Seleccionar dentro de la selección actual.
    4.	Eliminar de la selección actual.

Las entidades seleccionadas se resaltan de nuevo en amarillo brillante en su interfaz geoespacial.

:::{dropdown} Ejemplo: Seleccionar las ciudades (entidades de punto) que se intersecan con el polígono “China”.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_intersect_wiki.mp4"></video>
:::

:::{dropdown} Ejemplo 2: Seleccionar todos los polígonos de países que tocan el polígono “China”.
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_touch_wiki.mp4"></video>
:::

### Operadores geométricos
 Los operadores geométricos definen las condiciones de la relación entre la capa de origen y la de destino en las que se basará la selección. Hay ocho opciones en total:


 | Operación | Descripción | Ejemplo |
 |-------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
 | Interseca | Las entidades de la capa de destino se seleccionan si se intersecan con entidades de la capa de origen. | Seleccionar todas las carreteras que cruzan un polígono que representa un parque nacional. |
 | Contiene | Las entidades de la capa de destino se seleccionan si contienen completamente entidades de la capa de origen. | Seleccionar un polígono de país que contenga completamente polígonos más pequeños de ciudades. |
 | No interseca | Las entidades no intersecas son aquellas que no comparten ningún punto o área común. | Seleccionar distritos administrativos que no tienen límites ni zonas comunes. |
 | Igual | Las entidades son iguales si sus geometrías son idénticas. | Seleccionar dos segmentos de línea con exactamente el mismo conjunto de coordenadas. |
 | Toca | Las entidades de la capa de destino se seleccionan si tocan entidades de la capa de origen. | Seleccionar los parques que tocan una carretera específica. |
 | Superpuesta | Las entidades de la capa de destino se seleccionan si comparten algún espacio común con las entidades de la capa de origen. | Seleccionar parcelas que se superpongan con una zona de construcción propuesta. |
 | Dentro de | Las entidades de la capa de destino se seleccionan si están completamente dentro de las entidades de la capa de origen. | Seleccionar polígonos de edificios que se encuentran en su totalidad dentro de un polígono de un límite urbano. |
 | Cruza | Las entidades de la capa de destino se seleccionan si se cruzan con entidades de la capa de origen. | Seleccionar ríos que cruzan una carretera. |

 <!--ADD examples relevant to IM? -->

 ## Preguntas de autoevaluación

::::{admonition} Evalúe lo que aprendió
:class: note

1. __¿Cuáles son los tres tipos generales de selección o consulta en QGIS? Describa brevemente cada uno de ellos.__

:::{dropdown} Respuesta
- __Selección manual__:
    Las entidades se seleccionan con el mouse utilizando la herramienta `Select Features` en el lienzo del mapa o haciendo clic en la columna en la tabla de atributos (los números a la izquierda de la tabla de atributos). En el lienzo del mapa, las entidades seleccionadas se resaltarán en amarillo brillante, en la tabla de atributos se resaltan en azul.
- __Consultas basadas en atributos__ (Selección por atributo o por expresión):
    Se genera una consulta seleccionando atributos con valores específicos (p. ej., `"population" > 10000 AND "type" = 'urban'`).
- __Consultas espaciales__ (Selección por ubicación): 
    Las entidades se seleccionan en función de su relación espacial con las entidades de otra capa (p. ej., las que se cruzan, se tocan o no se intersecan).
:::

2. __Nombre al menos cuatro operadores geométricos en consultas espaciales (p. ej., “interseca”, “dentro de”) y explique su función.__



:::{dropdown} Respuesta

| Operador | Significado/Comportamiento |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| **Interseca** | Selecciona las entidades de la capa A que se intersecan (comparten cualquier parte) con las entidades de la capa B (se superponen de cualquier forma). |
| **Dentro de** | Selecciona las entidades de A que se encuentran completamente dentro de las entidades de B. |
| **Contiene** | Selecciona las entidades de A que contienen en su totalidad entidades de B. |
| **Toca** | Selecciona las entidades de A que se tocan (comparten un límite o punto) con las entidades de B, pero no se superponen internamente. |
| **Cruza** | Selecciona las entidades de A que pasan por las entidades de B (se cruzan). |
| **Superpuesta** | Selecciona entidades de A y B que se superponen, pero ninguna está completamente dentro de la otra. |

Ejemplos:
- Si desea todas las carreteras que cruzan los límites de un parque, utilice “Interseca” o “Cruza”.
- Si desea seleccionar todas las áreas en construcción que están completamente dentro de una zona inundable, utilice “Dentro de”.

::::

[def]: /fig/mActionSelectRectangle.png
