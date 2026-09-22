# Operaciones básicas de ráster


__🔙[Volver a la página de inicio](../es_intro.md)__

## Estadísticas zonales

El `Estadísticas zonales` permite la combinación de datos vectoriales y ráster.

Calcule las estadísticas de cada entidad vectorial sobre la base de la capa de ráster (véase el cuadro siguiente).



| Estadística | Descripción |
|------------------------|-------------------------------------------------|
| Cuenta | Número de celdas con valores válidos en cada zona. |
| Suma | Suma total de valores dentro de cada zona. |
| Media | Valor promedio dentro de cada zona. |
| Mediana | Valor promedio en la distribución dentro de las zonas. |
| Desviación estándar | Medida de la cantidad de variación o dispersión. |
| Mínimo | Valor más bajo dentro de cada zona. |
| Máximo | Valor máximo dentro de cada zona. |
| Rango | Diferencia entre los valores máximos y mínimos. |
| Minoría | Valor menos frecuente dentro de las zonas. |
| Mayoría | Valor más frecuente dentro de las zonas. |
| Variedad | Número de valores únicos dentro de cada zona. |
| Varianza | Medida de la dispersión de valores dentro de cada zona. |





1.	Haga clic en `Processing` -> `Toolbox` -> Buscar `Zonal Statistics`
2.	`Input Layer`: Seleccione su capa vectorial
3.	`Raster Layer`: Seleccione su capa ráster
4.	`Statistics to calculate`: Aquí puede seleccionar la estadística que desea calcular. Por ejemplo, la temperatura media del SPI.
5.	`Zonal Statistics`: Especifique dónde quiere guardar los resultados y dele un buen nombre.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zonal_stats.mp4"></video>




