# Cómo enseñar GIS

__🔙[Volver a la página principal](/content/intro.md)__

Aprender GIS puede ser un desafío, especialmente para personas que son nuevas en el tema o tienen experiencia limitada con tecnología más allá de sistemas de oficina estándar. El concepto de geodatos y todo lo que implica está bastante alejado de las actividades diarias de muchas personas en el sector humanitario. Sin embargo, comprender estos conceptos es esencial para trabajar eficazmente con GIS y resolver problemas. Dicho esto, a menudo no hay suficiente tiempo para profundizar en temas como proyecciones o algoritmos. Y aprendemos más a través de la capacitación práctica que de conferencias teóricas sobre GIS.

Por ello, debemos ser conscientes de equilibrar la práctica y la teoría al enseñar GIS.  
En este artículo, presentaremos buenas prácticas para enseñar GIS según nuestra experiencia. Comenzaremos discutiendo la diferencia entre enseñar teoría y enseñar mediante ejercicios prácticos, y la importancia de conectar GIS con su profesión o requerimientos laborales. Posteriormente, el artículo aborda consideraciones prácticas al enseñar GIS y métodos para evitar y resolver problemas.

## Teoría vs. práctica

En general, queremos enseñar GIS de manera que las personas comprendan cómo realizar tareas específicas necesarias en su trabajo de la forma más sencilla posible. Esto significa que nos enfocamos en ejercicios prácticos con conexión al mundo real, para que sea fácil ver cómo pueden usar GIS en su trabajo. Sin embargo, a veces necesitamos enseñar cosas teóricamente. Por lo general, porque son tan esenciales que las personas deben comprender el concepto antes de realizar cualquier acción en GIS (por ejemplo, el concepto de capa) o porque no conocer el concepto genera errores y problemas al trabajar con GIS y geodatos (por ejemplo, proyecciones).

Equilibrar teoría y práctica es esencial en la capacitación en GIS. A continuación, presentamos algunas buenas prácticas para incorporar ambos aspectos de manera efectiva:

* Hacer que las personas comprendan por qué es importante entender el concepto (por ejemplo, evitar errores o resultados incorrectos, o poder trabajar más rápido). Por ejemplo, si trabajan con geodatos proyectados en diferentes sistemas de referencia de coordenadas.  
* Usar gráficos, videos y otros medios para explicar el concepto. Por ejemplo, para enseñar el tema de proyecciones en el módulo 1, usamos videos y gráficos. Incluso puedes llevar un modelo en papel y [demostrar](https://education.nationalgeographic.org/resource/the-cartographers-dilemma/) el concepto con un ejemplo.

```{dropdown} Demostración de proyección: El dilema del cartógrafo
%%html
<iframe src="https://res.cloudinary.com/dtpgi0zck/video/upload/q_auto/vc_vp9/v1/videos/The%20Cartographer's%20Dilemma.webm?_s=vp-1.10.1" width="750" height="500"></iframe>
```

* Hacer la conexión entre la teoría y el uso práctico de GIS. Por ejemplo, mostrar qué tipo de errores puede generar usar una proyección incorrecta y por qué es importante usar proyecciones como UTM, o la diferencia entre sistemas de coordenadas métricas y geográficas (por ejemplo, al usar metros o kilómetros al crear buffers).  

(handson)=
## Ejercicios prácticos

Los ejercicios prácticos son altamente efectivos al enseñar GIS en todos los niveles de habilidad. Desde explorar la interfaz hasta ejecutar un análisis espacial completo, realizar estas tareas permite comprender mejor cómo trabajar con GIS. Siempre se recomienda priorizar ejercicios prácticos sobre presentaciones teóricas.

Existen dos tipos muy comunes de capacitación práctica: ejercicios paso a paso y ejercicios en grupo.

::::{grid} 2
:::{card} Ejercicios paso a paso
Los ejercicios paso a paso son una excelente herramienta para introducir nuevas funciones y herramientas, porque el facilitador está presente para responder preguntas y resolver problemas.

```{list-table}
:header-rows: 1

*   - Ventajas
    - Desventajas
*   - `+` Bueno para introducir nuevos temas
    - `-` Intercambio limitado entre participantes
*   - `+` Las preguntas se pueden responder de inmediato
    - `-` Los participantes tienen poca iniciativa propia
*   - `+` Buenas posibilidades de resolución de problemas por parte del facilitador
    - 
```

:::

:::{card} Ejercicios en grupo
Los ejercicios en grupo dependen más del trabajo independiente de las personas participantes. Esto es excelente para fomentar discusiones e intercambio entre ellos.

```{list-table}
:header-rows: 1

*   - Ventajas
    - Desventajas
*   - `+` Gran intercambio entre participantes
    - `-` No hay soporte inmediato por parte del facilitador(es)
*   - `+` Se fomenta la iniciativa y la resolución colaborativa de problemas
    - 
*   - `+` Ideal para capacitación en lugar de introducir nuevos conceptos
    - 
```

:::
::::

### Inicio de un ejercicio

Independientemente del tipo de ejercicio, se deben repasar brevemente los siguientes puntos con las personas participantes al comienzo del ejercicio:

1. __Objetivo del ejercicio:__ Generalmente, un ejercicio práctico debe comenzar explicando el objetivo del mismo. Por ejemplo: _“Este ejercicio tiene como objetivo enseñar el proceso de procesamiento básico de datos espaciales utilizando las herramientas Clip, Merge y Dissolve”_. Es una buena oportunidad para destacar la utilidad práctica de las herramientas que aprenderán, aumentando la motivación.
2. __Contexto:__ Idealmente, el ejercicio está basado en un ejemplo real o un escenario ficticio dentro del trabajo humanitario. Debes explicar rápidamente el contexto y la historia. Un ejemplo es el ejercicio del módulo 3 ([Ejercicio 4: Inundaciones en Nigeria](https://giscience.github.io/gis-training-resource-center/content/Module_3/es_qgis_module_3_ex4.html)).
3. __Datos del ejercicio:__ La mayoría de los ejercicios prácticos usan datos reales (por ejemplo, de [HDX](https://data.humdata.org)). Cada conjunto de datos debe explicarse brevemente. Esta información está disponible en cada ejercicio en la plataforma. Asegúrate de que todos hayan descargado los datos antes de comenzar. Algunos participantes no están familiarizados con archivos `zip`. Asegúrate de que descompriman las carpetas antes de importarlas en QGIS y dedica tiempo a resolver otros problemas relacionados con los datos del ejercicio.

### Durante el ejercicio: Paso a paso
Si realizas un ejercicio paso a paso, puedes seguir estos principios básicos. Explica el propósito de cada paso, por ejemplo: _“En este paso cargamos los datos en QGIS”_ o _“En este paso, recortamos todos los puntos excepto los del área de interés”_. Muestra cada paso tres veces, ya sea en pantalla grande o compartiendo tu pantalla (remoto). Esto requerirá paciencia. Las personas participantes necesitarán alternar entre observarte y orientarse en la interfaz de QGIS en su propio equipo para ejecutar los pasos. Esto llevará tiempo y no tiene sentido apresurarse. El objetivo es que nadie se quede atrás. Sé deliberado y muestra todo paso a paso, incluso lo más pequeño. Pregunta varias veces si hay problemas.

```{tip} ¡No uses botones de icono! 
Usa las pestañas o la caja de herramientas de geoprocesamiento en lugar de hacer clic en los íconos. Ver iconos puede ser difícil para las personas participantes, pero buscar herramientas en la caja de procesamiento es mucho más fácil.
```

1. Durante la primera demostración, anima a los participantes a solo observar lo que haces. Hazlo despacio y de manera deliberada.  
2. En la segunda demostración, deja que los participantes sigan los pasos en sus computadoras.  
3. La tercera demostración puede usarse para abordar problemas encontrados en la segunda demostración. A veces vale la pena dejar que exploren distintas opciones, por ejemplo, al estilizar capas o mapas.

Una vez que todos hayan logrado los resultados deseados, se puede continuar.

### Durante el ejercicio: Trabajo en grupo
Si realizas trabajo en grupo, hay otros aspectos a considerar:

1. Distribuye a las personas participantes en grupos después de la introducción al ejercicio. Explica si y cómo deben presentar los resultados.  
2. Dales tiempo para organizarse y revisar las instrucciones.  
3. Revisa los grupos periódicamente para resolver preguntas o malentendidos.  
4. Si es necesario, visita los grupos nuevamente y ajusta el tiempo según lo requerido.  
5. Al finalizar el trabajo en grupo, reúne a los participantes y verifica si hay problemas o dudas.  
6. Permite que los grupos presenten sus resultados.

### Final de un ejercicio
Después de un ejercicio, toma tiempo para preguntar si lo encontraron relevante y si están cómodos con el nivel de complejidad. Reflexiona con ellos sobre posibles aplicaciones de lo aprendido. Fomenta la discusión entre los participantes y planifica tiempo para que intercambien experiencias.

## Discusión y trabajo en grupo

La discusión y el trabajo en grupo son fundamentales en la capacitación en GIS, fomentando colaboración, pensamiento crítico e intercambio de conocimientos. Al participar en actividades colaborativas, los participantes pueden profundizar en los conceptos y metodologías de GIS, obteniendo valiosos aprendizajes de sus pares. Razones clave para incluir discusión y trabajo en grupo:

* __Intercambio de ideas y perspectivas:__ Permite compartir experiencias y enfoques, enriqueciendo el aprendizaje.  
* __Reflexión crítica:__ Fomenta evaluar críticamente métodos, fuentes de datos y técnicas analíticas, mejorando la toma de decisiones en proyectos GIS reales.  
* __Aprender de los pares:__ Ejercicios colaborativos permiten aprender de las fortalezas y conocimientos de otros.  
* __Mayor participación:__ Promueve el aprendizaje activo mediante ejercicios prácticos, estudios de caso y tareas basadas en proyectos.  
* __Desarrollo de habilidades:__ Facilita el desarrollo de comunicación, trabajo en equipo y resolución de problemas, habilidades transferibles a diversos contextos profesionales.

Incorporar discusión y trabajo en grupo crea entornos dinámicos donde los participantes colaboran, aprenden y aplican conceptos y habilidades de GIS de manera práctica.

## GIS para resolver problemas reales

En el mundo acelerado de la ayuda humanitaria, el tiempo es un recurso valioso y asistir a quienes lo necesitan es prioritario. La motivación de los participantes depende de ver el valor que GIS aporta a su trabajo diario. Por ello, siempre se deben usar ejemplos, datos y ejercicios de la vida real. Los ejercicios abstractos son menos efectivos porque los participantes no comprenden la relevancia de los métodos y flujos de trabajo.

La plataforma refleja esto. La sección principal sobre este tema es "[Módulo 1: Ejemplos de GIS utilizados por organizaciones humanitarias](https://giscience.github.io/gis-training-resource-center/content/Module_1/es_qgis_theory.html#examples-of-gis-used-by-humanitarian-organisations)".

Casi todos los ejercicios se orientan a métodos, flujos de trabajo o productos estándar en el sector humanitario, como mapas generales o mapas de regiones afectadas.

Consejos prácticos para hacer los ejercicios relevantes para el trabajo humanitario:

* __Audiencia:__ Reflexiona sobre tu audiencia y qué productos necesitarían más.  
* __Productos comunes:__ Comienza con mapas sencillos para informes y presentaciones. Esto interesa a todos, ya que todos deben presentar o reportar su trabajo.  
* __Escenarios:__ Personaliza los ejercicios para simular situaciones comunes, como crear mapas de situación para equipos de respuesta o analizar datos espaciales para identificar áreas de riesgo.  
* __Datos reales:__ Incentiva a usar datos reales y desarrollar soluciones GIS para desafíos humanitarios reales, fomentando aprendizaje práctico y resolución de problemas.  
* __Historias de éxito:__ Usa estudios de caso o historias de éxito de organizaciones como [Reliefweb](https://reliefweb.int) para ilustrar el impacto tangible de GIS.  
* __Cumplimiento de la misión:__ Presenta ejemplos donde GIS fue crucial para cumplir una misión.  
* __Proceso de planificación:__ Permite que los participantes identifiquen mapas y productos más relevantes para su trabajo.

## Practicar resolución de problemas: ¿Qué hacer si estás atascado?

Trabajar con GIS implica que en algún momento no sabrás cómo proceder. Por ejemplo, mostrar solo ciertas partes de la tabla de atributos en tu mapa impreso.

Dominar cada función de QGIS es impráctico. En cambio, desarrollar métodos de resolución de problemas es fundamental. La capacidad de enfrentar desafíos y saber dónde y cómo buscar soluciones es esencial en GIS. Toda capacitación debe priorizar esta habilidad. Estrategias para empoderar a los participantes:

* __Uso de la Wiki de la Plataforma de Capacitación en GIS de la IFRC:__ ¡Anima a los participantes a usar los recursos disponibles!  
* __Uso efectivo de motores de búsqueda como Google:__ Enseña a formular búsquedas precisas con palabras clave relevantes, incluyendo nombres de software, mensajes de error y descripciones de tareas.  
* __Uso de la documentación de QGIS:__ Aprende a navegar eficazmente [la documentación de QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/), incluyendo manuales, tutoriales y FAQs.  
* __Participación en la comunidad de usuarios de QGIS:__ Presenta [foros, grupos de Telegram y comunidades](https://www.qgis.org/en/site/forusers/support.html), como QGIS Community Forum y [subreddit QGIS](https://www.reddit.com/r/QGIS/).  
* __Explorar videos tutoriales de QGIS:__ Recomienda videos específicos de QGIS en YouTube para ver demostraciones visuales y resolución de problemas comunes.  
* __Uso de chatbots y asistentes de IA:__ Introduce asistentes IA como ChatGPT, entrenados para responder consultas sobre QGIS y guiar en resolución de problemas. Enseña a interactuar eficazmente con estos asistentes.  
* __Participar en grupos de usuarios de QGIS:__ Anima a [unirse a grupos de usuarios locales o en línea](https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups) y al grupo SIMS Geo en Slack para networking, intercambio de conocimientos y mentoría.

## Errores, problemas y obstáculos comunes

Las personas nuevas en GIS suelen tropezar con los mismos obstáculos. Cada aplicación GIS tiene desafíos y errores típicos, como manejar mal shapefiles, no ver datos en el lienzo por el orden de capas o usar la herramienta incorrecta por nombres similares (`Join by location` y `Join by location (summary)`).

Como usuario experimentado de GIS, puedes evitar estos errores automáticamente, pero los principiantes carecen de esa experiencia.

Para abordar estos problemas:

* __Wiki:__ Indica la [lista de problemas y soluciones comunes](/content/Wiki/es_qgis_common_errors_and_Issues.md) disponible en la plataforma.  
* __Google y ChatGPT:__ Anima a usar recursos en línea como Google y ChatGPT para fortalecer la autonomía.  
* __Proactividad:__ Señala posibles problemas durante los ejercicios y ofrece orientación paso a paso.  
* __Aprendizaje colaborativo:__ Fomenta un entorno donde los participantes compartan experiencias y soluciones.  
* __Salas de trabajo separadas:__ Úsalas para resolución individual sin interrumpir al grupo principal. Asegúrate de que puedan ponerse al día.  
* __Buenas prácticas:__ Destaca la importancia de seguir buenas prácticas en gestión de datos para evitar problemas comunes y mejorar eficiencia y precisión en los flujos de trabajo GIS.

Al abordar proactivamente errores y desafíos, se empodera a los participantes para manejar eficazmente las complejidades de GIS, promoviendo una experiencia de aprendizaje más productiva y satisfactoria.
