# Serie de ejercicios: Análisis de acción anticipatoria para ciclones en Madagascar


Este ejercicio se centra en la evaluación preliminar de un evento ciclónico en Madagascar. El objetivo es crear un flujo de trabajo analítico como modelo QGIS que estime la población, la infraestructura y las tierras agrícolas expuestas. Además, se puede evaluar la accesibilidad de las regiones expuestas utilizando isócronas precalculadas.
En esta serie de ejercicios, usted creará un flujo de trabajo analítico como un modelo de QGIS y visualizará los resultados utilizando plantillas de mapa y archivos de estilo.


::::{card}
Contexto
^^^

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
:::

Madagascar se ve expuesta con frecuencia a intensos ciclones tropicales, que pueden provocar daños generalizados, desplazamientos de población y pérdida de vidas. El análisis anticipatorio es esencial para reducir el impacto de estos fenómenos meteorológicos extremos. Al utilizar datos de pronóstico y herramientas geoespaciales para predecir las áreas que probablemente se verán afectadas, los actores humanitarios y las autoridades locales pueden tomar medidas tempranas, como preposicionar suministros y emitir alertas, para proteger vidas y medios de subsistencia antes de que ocurra un desastre. Este enfoque proactivo fortalece la capacidad de preparación y respuesta, y ahorra tiempo, recursos y vidas.

Aina, experta en SIG de la Cruz Roja Malgache (CRM), se prepara para la próxima temporada de ciclones. Quiere mejorar la capacidad de su equipo para actuar con rapidez una vez pronosticada una tormenta automatizando los análisis clave en QGIS. Esto incluye la estimación de las poblaciones expuestas, la identificación de los servicios afectados como la sanidad y la educación, y la evaluación de si se puede llegar a los puestos sanitarios desde los almacenes clave en un plazo crítico de 10 horas.
El objetivo es preparar un flujo de trabajo de análisis y visualización de principio a fin que pueda respaldar una acción anticipatoria rápida y basada en datos antes de que un ciclón toque tierra.

::::

---


:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_5/es_qgis_module_5_mdg_aa_ex_1.html
__Ejercicio 1: Estimación de la población expuesta: el método manual de Aina (módulo 5)__
^^^


- Importación de conjuntos de datos a QGIS
- capas de reproyección
- capas vectoriales de almacenamiento en buffer
- capas ráster de recorte
- cálculo de estadísticas zonales
- aplicación de la clasificación graduada a los resultados


:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_7/es_module_7_mdg_aa_ex_2.html
__Ejercicio 2: Automatización de la estimación de la población expuesta: el modelo de Aina (módulo 7)__
^^^

- Utilice el constructor de modelos
- capas de reproyección
- capas vectoriales de almacenamiento en buffer
- capas ráster de recorte
- cálculo de estadísticas zonales
- aplicación de la clasificación graduada a los resultados

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_7/es_module_7_mdg_aa_ex_3.html
__Ejercicio 3: Identificación de centros sanitarios y escuelas afectadas: Aina agrega más capas (módulo 7)__
^^^

- amplíe el modelo
- cuente puntos en un polígono
- use la calculadora de campo

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_module_4_mdg_aa_ex_4.html
__Ejercicio 4: Visualización de los resultados del impacto del ciclón: Aina diseña sus capas (módulo 4)__
^^^

- Utilice el panel de estilo
- Aplique archivos de estilo a las capas
- Guarde archivos de estilo

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_4/es_module_4_mdg_aa_ex_5.html
__Ejercicio 5: Creación rápida de mapas: Aina utiliza plantillas de mapas (módulo 4)__
^^^

- utilice el compositor de diseño de impresión para crear un mapa
- utilice plantillas de mapas
- utilice tablas de atributos en el compositor de diseño de impresión

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_7/es_module_7_mdg_aa_ex_6.html
__Ejercicio 6: Exportación de resultados del modelo para el equipo de operaciones (módulo 7)__
^^^

- amplíe el modelo
- una los resultados del modelo
- exporte el resultado del modelo en formato de hoja de cálculo (.csv)

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/spanish/content/es/Module_7/es_qgis_module_9_mdg_aa_ex_7.html
__Ejercicio 7: Accesibilidad de las publicaciones de salud desde los almacenes de CRM__
^^^

- filtre conjuntos de datos
- realice un análisis de accesibilidad
- actualice conjuntos de datos con nueva información
- visualice la accesibilidad de los centros de salud

:::

