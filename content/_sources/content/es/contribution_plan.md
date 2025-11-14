# Plan de Contribución para la Plataforma de capacitación en SIG de la IFRC

## Introducción

Gracias por su interés en contribuir al Centro de Recursos SIG de la IFRC.
Esta página <!--Document-->resume el proceso de contribución y las directrices para colaborar con el Centro de Recursos SIG. Ofrece información detallada para las contribuciones y las mejores prácticas correspondientes. Tanto si tiene la intención de añadir nuevos contenidos, como contribuir al material existente o colaborar en la mejora general de la plataforma de capacitación como socio, esta guía le ayudará a comprender los pasos necesarios.

## Colaboraciones

### Contenido

Se anima a los colaboradores a proponer nuevos temas o contenido relevantes para el Centro de Recursos SIG. Estos temas deberán alinearse con los objetivos de capacitación para la acción anticipatoria (AA), la gestión de la información y enfocarse en las operaciones básicas del SIG. Si tiene un tema en mente, envíe una breve introducción y los puntos clave a `gis-training-platform@heigit.org` para iniciar la colaboración.

Para ayudarnos a comprender y evaluar su propuesta, tenga en cuenta las siguientes tres preguntas orientativas:

1. __¿Qué nivel de experiencia en el SIG se requiere para el contenido propuesto?__
2. __¿Cuál es el objetivo principal de aprendizaje o valor agregado del contenido propuesto?__
3. __¿Usted mismo añadirá el contenido a la plataforma de capacitación (en Markdown) o necesitará ayuda?__

Revisaremos y evaluaremos cada idea en cada caso particular.

### ¿Está interesado en convertirse en socio o colaborador de la Plataforma de Recursos de Capacitación?

El Grupo de Trabajo de Capacitación en SIG, responsable del Centro de Recursos SIG de la IFRC, fue creado por las Sociedades Nacionales de la Cruz Roja en Gran Bretaña, Alemania y Países Bajos, con el apoyo técnico del Heidelberg Institute for Geoinformation Technology (HeiGIT).

Además de las contribuciones de contenido, este consorcio le da la bienvenida a los nuevos socios del Movimiento Internacional de la Cruz Roja y de la Media Luna Roja. También alentamos las contribuciones, en forma de ayuda financiera o en especie para desarrollar e impulsar, aun más, la mejora continua de la plataforma de capacitación.

## Directrices para la contribución de contenidos

### Su contribución

- __Markdown MyST y Jupyter Book:__ Además de CommonMark Markdown, Jupyter Book también admite una versión más completa de Markdown denominada __MyST Markdown__. Se trata de un superset de CommonMark, que incluye piezas sintácticas útiles, para publicar narrativas computacionales. Para obtener más información sobre MyST Markdown, consulte el [resumen de MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html).
- __Cambios en la Dev-Branch:__
    - Todos los cambios deben subirse con un push a la `dev` rama. Estos cambios serán revisados por el HeiGIT y/o la Cruz Roja (RC) antes de fusionar una solicitud de extracción.
    - Actualmente, solo HeiGIT o la Cruz Roja (RC) están autorizados a crear solicitudes de extracción y los colaboradores pueden solicitar revisiones a HeiGIT y/o a la Cruz Roja a través de GitHub.
- __Contenido nuevo:__
    - Si tiene ideas para nuevos contenidos (como nuevas secciones en módulos existentes o nuevos módulos independientes), envíenos un correo electrónico o presente una issue en GitHub, mediante el uso de las etiquetas adecuadas. Una propuesta también podría incluir una página de Markdown o una estructura sugerida.
    - Las propuestas de nuevos contenidos se someterán a revisión y se anima a los colaboradores, para que interactúen activamente con los revisores, a través de los issues de GitHub. Si desea profundizar en temas sobre contenidos o colaboraciones, HeiGIT y/o la Cruz Roja (RC) con gusto pueden agendar videollamadas.
- __Envío de datos externos:__
    - Si necesita enviar datos u otros materiales, puede enviarlos por correo electrónico a `gis-training-platform@heigit.org` para cargarlos en el repositorio de datos Nexus.

### Licencias

- __Derechos de autor y fuentes de datos:__ Proporcione siempre citas claras para cualquier material externo, incluidos los artículos, los libros y el contenido web. Para los artículos y los libros, incluya la cita completa con DOI. Para las páginas web, incluya la URL de origen (deben mantenerse los enlaces externos)
- Todo el contenido de la plataforma se publicará bajo la licencia __[CC 4.0 BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)__

### Estructura ideal para el contenido nuevo

De ser posible, la estructura de los nuevos módulos/capítulos deberá incluir:

1. __Teoría:__ introducción a los conceptos clave.
2. __Ejemplos prácticos:__ Demostración de cómo aplicar conceptos de acción anticipatoria, gestión de la información y QGIS.
3. __Ejercicios:__ Práctica activa con ejercicios guiados.
4. __Síntesis:__ Un ejercicio o un ejemplo más complejo que sintetice el contenido del módulo
5. __Preguntas de autoevaluación:__ Para evaluar la comprensión de los conceptos principales del módulo

### Tipos de contenidos

- __Teoría:__ Explicación de los conceptos.
- __Ejemplos del mundo real:__ Incluya ejemplos prácticos, que sean relevantes para el campo del SIG (preferiblemente relacionados con la gestión de la información, la acción anticipatoria o el trabajo humanitario, en general).
- __Ejercicios:__ Ejercicios guiados o autoguiados para reforzar el aprendizaje.
- __Preguntas para el debate:__ Fomente la interacción y la conexión con escenarios del mundo real.
- __Wiki:__ Artículos breves que ofrezcan explicaciones o instrucciones relacionadas con la plataforma de capacitación.
- __Estadísticas:__ Imágenes o estadísticas para ilustrar los conceptos teóricos, ejemplos del mundo real o la muestra de capturas de pantallas
- __Videos:__ La plataforma de capacitación utiliza videos cortos sin comentarios para mostrar cómo realizar determinados pasos (por ej.: editar la tabla de atributos, importar capas o establecer la simbología de una capa)

:::{note}
Tenga en cuenta que existen muchos recursos detallados sobre el SIG, así como también documentación oficial. Explique la teoría necesaria para que los participantes realicen las actividades. Además puede consultar recursos externos.
:::

### Directrices para los ejercicios

- __Instrucciones:__ Proporcione instrucciones paso a paso.
- __Notas para el facilitador:__ Incluya notas para los facilitadores sobre cómo guiar el ejercicio.
- __Datos:__ Proporcione siempre un enlace al conjunto o conjuntos de datos utilizados en el ejercicio. Asegúrese de que el conjunto de datos, no contenga datos personales y errores, a menos que la limpieza de datos, forme parte del ejercicio.

:::{note}
Se invita a los colaboradores a subir videos con guías paso a paso, cuando sea útil.
:::

## Directrices para la nomenclatura y el formato a los archivos

Siga estas directrices para nombrar los archivos y estructurar los directorios:

- __Nomenclatura:__ Elija nombres descriptivos. Asegúrese de que los ejercicios estén numerados correctamente (p. ej.: `module_#_ex#_title`). El número del ejercicio deberá ser el siguiente número disponible
- __Estructura de la carpeta:__ Asegúrese de que los datos del ejercicio sigan la [estructura correcta de las carpetas](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_projects_folder_structure_wiki.html#standard-folder-structure) y estén comprimidos correctamente (evite anidar las carpetas excesivamente, ya que esto puede provocar problemas al descomprimirlas)
- __Idioma y versión de QGIS:__ incluya siempre la versión de QGIS y el idioma en los nombres de los archivos.
- __Imágenes:__ todas las imágenes y estadísticas deben guardarse en la carpeta `/fig/`.
    - Las imágenes comunes y generales solo deben tener un título breve e informativo.
        - Ejemplo de nombre de imagen: HeiGIT_logo_compact.svg
    - En el caso de una captura de pantalla de QGIS u otro programa, se aplican reglas adicionales.  En primer lugar, debe incluirse la abreviatura del idioma utilizado (p. ej.: es). En segundo lugar, la versión de QGIS (p. ej.: 3.28).
        - Ejemplo de nombre de captura de pantalla: en_3.29_clip_tool.png
    - Cuando se trate de imágenes de OpenStreetMap (OSM) o de imágenes satelitales, se debe incluir el año y el lugar.
        - Ejemplo de imágenes de mapas o imágenes satelitales: OSM_Heidelberg_2023.png

Siga estas directrices al crear y dar formato a los contenidos:

- __Ortografía:__ Utilice la ortografía del español.
- __Encabezados:__
    - `# Title` Para los títulos principales de las páginas Markdown
    - `## Title` Para las secciones
    - `### Title` Para las subdivisiones
    - Evite encabezados más allá del nivel H3 (`### Title`). Utilice negritas, el subrayado o colóquelos en tarjetas para conseguir un efecto similar.
- __Enlaces:__
    - En Markdown, puede incrustar enlaces en el texto con `[text/name](link)`
- __Figuras e imágenes:__
    - Las imágenes y los videos se guardan en la carpeta `/fig/`.
    - Utilice la directiva figure para las imágenes:
        ```
        :::{figure} /fig/example.png
        ---
        name: example_figure
        width: 750 px
        align: center/left/right
        ---
        Leyenda descriptiva que incluya la fuente de la imagen
        :::
        ```
    - `name` debe indicar un nombre descriptivo único. Puede hacer referencia a la figura en el texto con:
        ```
        {numref}`name`
        ```
        - Esto no funciona en las páginas que no están incluidas en el archivo `TOC.yml`.
    - `width` especifique la anchura del píxel. La cantidad máxima de píxeles para la anchura es de 750 px. También puede utilizar `height`. Tenga cuidado al establecer valores altos, ya que esto distorsionará la imagen, una vez que alcance el tope de anchura de 750 px.
    - Alinear, especifica dónde debe mostrarse la imagen en la página de Markdown. Por ej.: `align: left` puede utilizarse para alinear la imagen a la parte izquierda de la página y dejar espacio para el texto a la derecha.
    - La leyenda de la imagen debe describir lo que se ve en la figura, en el contexto de la sección. Las fuentes de la imagen deben especificarse con la mayor precisión posible.
    - Es posible incrustar iconos en el texto con el uso de `![](/fig/FILENAME)`. Asegúrese de que la altura del icono no supere los 30 píxeles.
- __Admonitions:__
    - Utilice admonitions como note, caution, tip, tldr para las notas adicionales como
    ```
    :::{admonition} TÍTULO
    :class: tip, caution, note, tldr, note
    CONTENIDO
    :::
    ```
- __Menús desplegables:__ Para los contenidos opcionales (p. ej.: videos o información complementaria), utilice menús desplegables:
    ```
    :::{dropdowns} TÍTULO
    CONTENIDO
    :::
    ```
- __Cards:__ Utilice las directivas card para resaltar el contenido de una “tarjeta”:
    ```
    :::{card}
    ENCABEZADO
    ^^^
    CONTENIDO
    :::
    ```
- __Grids:__ Para crear varias columnas, que muestren contenidos o imágenes una al lado de la otra, puede crear cuadrículas:
    ```
    ::::{grid} 2
    :::{card}
    :::
    :::{card}
    :::
    ::::
    ```

- __Márgenes:__ A veces, puede ser útil colocar pistas o información adicional en el margen derecho. Esto puede lograrse con la siguiente directiva:
    ```
    ::::{margin}
    CONTENIDO (puede incluir otras directivas)
    ::::
    ```

:::::{admonition} Anidamiento de directivas
:class: tip
Es posible anidar directivas como figuras dentro de cards o admonitions. Simplemente utilice más signos de dos puntos alrededor de las directivas que contienen otras como:

```
::::{card}
ENCABEZADO
^^^
CONTENIDO
:::{figure} /fig/figure.png
---
name:
width:
align:
---
LEYENDA DE LA IMAGEN
:::
::::
```

:::::


- __Incrustación de videos:__ Los videos deben incrustarse mediante el uso del código HTML:
    ```md
    <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>
    ```
    - Copie el código e ingrese el nombre del archivo de video que desea incrustar.

- __Normas para el formato de texto:__
    - Cuando describa un proceso, utilice números. Por ejemplo:
        ```
        1. Haga clic con el botón derecho en la capa “ML1_IPC_Index” -> `Attribute Table`-> haga clic en [`Field Calculator`](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_table_functions_wiki.html#calculate-field) ![](/fig/mActionCalculateField.png) para abrir la calculadora de campo
        2. Marque la opción `Create new field`
        3. `Output field name`: Nombre la nueva columna “Trigger_activation”
        4. `Result field type`: Texto (cadena)
        ```
    - __Toda la superficie en la que se pueda hacer clic debe escribirse como fragmento de código, p. ej.: `Attribute Table`__
    - Si se utiliza un icono especial en QGIS, colóquelo junto a los fragmentos de código, p. ej.: `Field Calculator` ![](/fig/icon_scratch_layer.png).
    - Si es necesario seleccionar una opción, escriba el nombre de la superficie de clic, en el fragmento de código y la opción, como texto normal, por ej.:`Result field type`: Texto (cadena)
    - Si el nombre de un archivo debe escribirse de una forma determinada, utilice comillas, p. ej.:`Output field name`: Nombre la nueva columna “Trigger_activation”
    - Cuando los participantes deban utilizar una herramienta o una funcionalidad, que no esté descrita detalladamente en su guía paso a paso actual, añada tanto el enlace al nombre de la herramienta, por ej.: [arrastrar y soltar](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop) o el use algo como el [mapa base de la Wiki](https://giscience.github.io/gis-training-resource-center/content/es/Wiki/es_qgis_basemaps_wiki.html) y donde sea lógico, añada el enlace al video de la Wiki correspondiente.