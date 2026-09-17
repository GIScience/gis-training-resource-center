# Gestión de datos geoespaciales con SharePoint


Las organizaciones pequeñas suelen tener dificultades para mantener la consistencia y el acceso a los datos geoespaciales. 
Un centro de datos geoespaciales simple y bien estructurado ayuda a **estandarizar el trabajo en SIG**, **preparar las respuestas** e **incorporar nuevo personal** de forma eficiente. 
Esta guía describe un enfoque práctico utilizando **SharePoint**, que muchas organizaciones ya utilizan para la gestión de documentos.

## Propósito y audiencia
- **Quién**: organizaciones pequeñas que inician o formalizan el trabajo en SIG.
- **Por qué**: establecer una estructura ligera y estandarizada para **datos, proyectos y plantillas**.
- **Resultado**: incorporación más rápida, menos enlaces rotos, mapas y análisis consistentes.

### La función del administrador de datos

Un **administrador de datos** es una persona designada (o un equipo pequeño) responsable de:
- Aprobar y cargar nuevos conjuntos de datos en `10_Data` y `20_Raster_Data/`.
- Administrar permisos (p. ej., quién puede editar frente a quién solo puede ver).
- Apoyar a colegas con preguntas sobre la calidad o los estándares del conjunto de datos.

Contar con una función clara de administrador evita sobrescrituras accidentales y garantiza que todo el personal trabaje con **datos confiables y consistentes**.


:::{tip}
Si su organización supera esta configuración (muchos editores, ediciones intensivas, rásteres muy grandes), mantenga SharePoint para la distribución y la documentación y añada una base de datos espacial (p. ej., PostGIS) para la edición multiusuario.
:::

## Ejemplo de estructuras de carpetas

A continuación se presentan tres posibles estructuras, de la más simple a la más avanzada. 
Elija la que coincida con el tamaño y la capacidad de su organización.

### 1. Configuración minimalista (equipos muy pequeños)
```
GIS_Hub/
│
├── Data/ # Todos los datos geoespaciales en un solo lugar
│ ├── Boundaries/ # Límites administrativos
│ ├── Roads/ # Redes viales
│ ├── Hydro/ # Ríos, lagos
│ ├── Exposure/ # Centros de salud, escuelas
│ └── Hazards/ # Ciclones, inundaciones, sequías
│
├── Projects/ # Trabajo y resultados de proyectos
│ ├── Project_A/
│ ├── Project_B/
│ └── Project_C/
│
└── Templates/ # Estilos, diseños, símbolos de QGIS
```


💡 **Usar cuando:** el equipo es muy pequeño, los datos son limitados y hay poca superposición entre usuarios. Esta estructura se configura rápidamente y es fácil para colegas sin perfil técnico.

⚠️ **Limitación:** Todo se mezcla en una sola carpeta `Data/`: no es evidente qué conjuntos de datos son definitivos y cuáles son borradores, y su posterior ampliación puede resultar confusa.

**Convenciones de nombres para la configuración minimalista**
- Mantener los nombres de archivo simples y descriptivos, por ejemplo:
  - `Boundaries_ADM2_MDG_2024.gpkg`
  - `HealthFacilities_SOM_2025.csv`
- Para proyectos, anteponer el nombre del proyecto a los entregables, por ejemplo:
  - `ProjectA_Map_202501.pdf`
  - `ProjectB_QGISProject.qgz`
- Las fechas pueden ser opcionales aquí, ya que el volumen del conjunto de datos es bajo.

---
### 2. Configuración equilibrada (organizaciones pequeñas en general)

```
GIS_Hub/
│
├── 00_Admin/                 # POE, directrices, notas
├── 10_Data/                  # Todos los conjuntos de datos compartidos (autorizados + temáticos, de solo lectura; gestionados por administradores)
│   ├── Boundaries/           # Límites administrativos, límites de asentamientos
│   ├── Roads/                # Redes viales, senderos
│   ├── Hydro/                # Ríos, lagos, cuencas
│   ├── Settlements/          # Aldeas, pueblos, ciudades
│   ├── Health/               # Centros de salud, clínicas
│   ├── Logistics/            # Almacenes, pistas de aterrizaje
│   └── Hazards/              # Trayectorias de ciclones, zonas de inundación, indicadores de sequía
├── 20_Raster_Data/           # WorldPop, DEM, cubierta terrestre, imágenes satelitales, rásteres de amenazas
├── 30_Styles_Templates/      # Estilos y diseños de QGIS compartidos
│   └── Generic_Styles/       # Simbología estándar y plantillas de diseño
├── 40_Working_Data/          # Borradores y ediciones temporales (acceso restringido)
└── 50_Projects/              # Ordenados por tema
    ├── Disaster_Preparedness/
    ├── Health/
    └── Climate_Risk/
```
**💡 Usar cuando:**
La organización quiere mantener todos los datos seleccionados juntos en `10_Data/`, mientras separa los datos ráster (`20_Raster_Data/`), los estilos compartidos (`30_Styles_Templates/`), los borradores (`40_Working_Data/`) y los resultados del proyecto (`50_Projects/`). Esta configuración funciona bien para la mayoría de las ONG pequeñas.

**⚠️ Limitación:**
El personal debe entender que `10_Data/` y `20_Raster_Data/` son de solo lectura. Si las ediciones se guardan allí, los conjuntos de datos pueden sobrescribirse o corromperse.
:::{note}
Los archivos ráster grandes (p. ej., DEM, imágenes satelitales, rásteres de viento o lluvia) pueden ralentizar la sincronización de OneDrive y llenar las unidades locales rápidamente.

Para reducir los problemas:
- Mantenga solo las capas ráster más importantes en `20_Raster_Data/`.
- Archive versiones antiguas de ráster en una biblioteca independiente si es necesario. 
:::
**Convenciones de nombres para la configuración equilibrada (uso general)**

Para sea fácil encontrar los archivos y evitar duplicados, utilice un patrón de nombres consistente:

- **Datos (todos los compartidos):** 
  Patrón: `[Theme]_[Location/ADMlevel]_[Source]_[YYYYMM].[ext]` 
  *Ejemplo:* `Boundaries_ADM2_MDG_GADM_202407.gpkg`

- **Datos ráster:** 
  Patrón: `[Theme]_[Location]_[Source]_[YYYYMM].[ext]` 
  *Ejemplo:* `Rainfall_MDG_CHIRPS_202502.tif`

- **Proyectos:** 
  Patrón: `[ProjectName]_[OutputType]_[Region]_[YYYYMM]_vX.[ext]` 
  *Ejemplo:* `HealthAssessment_Report_SOM_202503_v1.pdf`


### 3. Configuración extendida (con flujos de trabajo de PAT)
```
GIS_Hub/
│
├── 00_Admin/                 # POE, directrices, notas
├── 10_Data/                  # Todos los conjuntos de datos compartidos (autorizados + temáticos, de solo lectura; gestionados por administradores)
│   ├── Boundaries/
│   ├── Roads/
│   ├── Hydro/
│   ├── Settlements/
│   ├── Health/
│   ├── Logistics/
│   └── Hazards/
├── 20_Raster_Data/           # DEM, cobertura terrestre, datos satelitales, rásteres de amenazas (solo lectura)
├── 30_Styles_Templates/      # Estilos y diseños de QGIS compartidos
│   ├── Generic_Styles/       
│   └── Cyclone_EAP_Styles/   # Plantillas para resultados específicos para ciclones
├── 40_Working_Data/          # Borradores y ediciones (restringido)
├── 50_Cyclone_EAP/           # Flujos de trabajo de acción anticipatoria (ciclón)
│   ├── Fixed_Data/           # Capas de exposición de referencia
│   ├── Models/               # Modelos para desencadenantes, seguimiento de zonas de influencia, archivos de pronósticos
│   └── Activations/          # Una subcarpeta por activación de ciclón
│       ├── Cyclone_Freddy_2023/
│       ├── Cyclone_Batsirai_2022/
│       └── Cyclone_X_YYYY/
└── 60_Projects/              # Clasificados por tema
    ├── Disaster_Preparedness/
    ├── Health/
    └── Climate_Risk/

```


💡 **Usar cuando:** 
La organización quiere mantener todos los datos seleccionados juntos en `10_Data/`, mientras separa los **datos ráster pesados** (`20_Raster_Data/`), los **estilos compartidos** (`30_Styles_Templates/`) y los **flujos de trabajo específicos del proyecto o del PAT**.

⚠️ **Limitación:** 
El personal debe entender que `10_Data/` y `20_Raster_Data/` son de **solo lectura**. Si los usuarios guardan las ediciones allí, los conjuntos de datos pueden sobrescribirse o corromperse.

:::{note}
Los archivos ráster grandes (p. ej., DEM, cuadrículas viento ciclónico o de profundidad de la inundación) pueden ralentizar la sincronización de OneDrive y llenar los discos locales. 
Para reducir los problemas:
- Mantenga solo las capas ráster más importantes en `20_Raster_Data/`.
- Archive los rásteres más antiguos en `30_Snapshots/` si necesita conservar versiones históricas.
:::

**Convenciones de nombres para la configuración equilibrada (con PAT)**

Para sea fácil encontrar los archivos y evitar duplicados, utilice un patrón de nombres consistente. 
A continuación se sugieren convenciones con ejemplos:

- **Datos (todos los compartidos):** 
  Patrón: `[Theme]_[Location/ADMlevel]_[Source]_[YYYYMM].[ext]` 
  Ejemplo: `Boundaries_ADM2_MDG_GADM_202407.gpkg`

- **Datos ráster:** 
  Patrón: `[Theme]_[Location]_[Source]_[YYYYMM].[ext]` 
  Ejemplo: `Rainfall_MDG_CHIRPS_202502.tif`

- **Modelos de PAT:** 
  Patrón: `Model_[Hazard]_[Version]_[YYYYMM].[ext]` 
  Ejemplo: `Model_CycloneTrigger_v3_202502.model3`

- **Activaciones:** 
  Patrón: `Cyclone_[Name]_[Year]_[OutputType]_[Region].[ext]` 
  Ejemplo: `Cyclone_Freddy_2023_ImpactMap_ADM2_MDG.pdf`

- **Proyectos:** 
  Patrón: `[ProjectName]_[OutputType]_[Region]_[YYYYMM]_vX.[ext]` 
  Ejemplo: `ClimateRiskAssessment_Map_MDG_202502_v1.pdf`



## Ventajas, limitaciones y permisos

Cuando se configura un centro de datos geoespaciales en SharePoint, existen beneficios claros, pero también algunos límites importantes que se deben tener en cuenta.  
A continuación, se muestra una breve descripción de las **ventajas**, las **limitaciones** y cómo gestionar los **permisos** de manera eficaz.

---

### Ventajas

El uso de SharePoint para la gestión de datos geoespaciales ofrece las organizaciones pequeñas un punto de partida sólido:

- **Estandarización**: todo el personal trabaja con los mismos conjuntos de datos, archivos de estilo y plantillas de mapas, lo que reduce la confusión y garantiza resultados consistentes.
- **Incorporación sencilla**: los nuevos colegas no pierden el tiempo buscando archivos; la estructura de carpetas deja claro dónde encontrarlos.
- **Control de versiones integrado**: SharePoint almacena automáticamente el historial de archivos, lo que facilita recuperar versiones anteriores si se producen errores.
- **Permisos flexibles**: puede decidir quién solo puede ver, quién puede editar y quién tiene el control total.
- **Integración con QGIS**: a través de la sincronización con OneDrive, se puede acceder a los conjuntos de datos de forma local y confiable dentro de los proyectos de QGIS.

---

### Limitaciones

Sin embargo, SharePoint no es una base de datos de SIG, lo que presenta algunas restricciones:

- **Problemas de concurrencia**: los formatos de datos geoespaciales basados en archivos (como GeoPackage) pueden corromperse si varias personas intentan editarlos simultáneamente.
- **Cuellos de botella en el rendimiento**: los rásteres muy grandes o las ediciones de alta frecuencia se ralentizarán con rapidez; en estos casos, es mejor utilizar una base de datos espacial como PostGIS.
- **Se requiere disciplina**: el sistema depende de que los usuarios sigan las estructuras de carpetas y las convenciones de nombres de manera consistente; de lo contrario, el centro pierde su valor.

:::{important}
Piense en SharePoint como un **centro de distribución y coordinación**. 
Para la **edición multiusuario** o el **almacenamiento a gran escala**, necesitará una infraestructura de base de datos.
:::

### Permisos

Es esencial gestionar bien el acceso para proteger los datos autorizados y, al mismo tiempo, permitir la colaboración. 
Una buena práctica es diferenciar entre los **datos autorizados**, los **datos de trabajo** y los **resultados del proyecto**:

- **Datos autorizados**: de solo lectura para la mayoría del personal; únicamente los administradores de datos designados pueden cargar o editar.
- **Datos de trabajo**: restringidos a los editores; habilite proteger/desproteger para evitar sobrescrituras accidentales.
- **Proyectos**: editables por los equipos del proyecto, pero pueden ser de solo lectura para otros, a fin de evitar ediciones no deseadas.
- **Conjuntos de datos sensibles**: si es necesario controlar la distribución, utilice enlaces de *solo lectura* combinados con la opción *Bloquear descarga*.

---

**Mantenga los permisos simples.** 
En lugar de asignar derechos a cada persona, cree grupos en SharePoint como:
- *Propietarios* (Control total)
- *Editores* (Editar)
- *Lectores* (Solo lectura)

Esto hace que la gestión sea mucho más sencilla cuando el personal se incorpora o deja la organización.


## Metadatos y catalogación

Incluso si sus archivos están bien organizados en carpetas, puede resultar difícil para el personal nuevo saber **cuál conjunto de datos es el más reciente** o **para qué se utiliza cada archivo**. 
Aquí es donde entran los *metadatos*. En SharePoint, puede agregar campos de información adicionales (columnas) a las bibliotecas. Estos campos facilitan filtrar, ordenar y buscar en todos los datos, sin depender únicamente de los nombres de los archivos.

### ¿Por qué usar metadatos?
- **Claridad**: el personal puede ver rápidamente qué conjunto de datos está autorizado, es un borrador o está desactualizado.
- **Consistencia**: todos usan los mismos campos estándar.
- **Búsqueda y filtrado**: en lugar de navegar por docenas de carpetas, los usuarios pueden filtrar por país, amenaza o fecha de actualización.
- **Documentación**: el contexto clave (como el origen y el ciclo de actualización) se almacena con el archivo en sí, no solo en la memoria de alguien.

### Campos de metadatos sugeridos
Al crear o editar una biblioteca en SharePoint, puede agregar columnas simples como:
- **Tema** (p. ej., límites, salud, logística, amenazas)
- **Ubicación/Código ISO3** (p. ej., MDG, SOM, nombre de la región)
- **Fuente** (p. ej., PMA, OCHA, OSM)
- **Fecha de actualización** (DDMMAAAA)
- **Contacto/Propietario** (persona o equipo responsable)
- **URL** (enlace a la fuente de datos o a la documentación original)

:::{tip}
No es necesario etiquetar *todo*. Comience con tres o cuatro campos principales que ayuden a su equipo a encontrar los datos rápidamente. 
Por ejemplo: *Tema*, *Ubicación*, *Fuente*y *Fecha de actualización*. Se pueden añadir más campos posteriormente si es necesario.
:::

<iframe width="560" height="315" src="https://www.youtube.com/embed/qB2acPUSF_o?si=JyjVHEqcTNHqTKUK" title="Reproductor de video de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Guía de implementación (inicio rápido)

Configurar un centro de datos geoespaciales en SharePoint es sencillo. 
Siga estos pasos para comenzar:

1. **Crear una nueva biblioteca de documentos en SharePoint**
   - Asígnele un nombre claro, p. ej., `GIS_Hub`.
   - Esta será el espacio raíz para todas sus carpetas de datos geoespaciales.

2. **Configurar la estructura de las carpetas**
   - Reproduzca la estructura acordada (minimalista, equilibrada o extendida) dentro de la biblioteca.
   - Ejemplo de configuración equilibrada:
     - `00_Admin/`
     - `10_Data/`
     - `20_Raster_Data/`
     - `30_Styles_Templates/`
     - `40_Working_Data/`
     - `50_Projects/`

3. **Configurar permisos**
   - Use los grupos de SharePoint: *Propietarios* (control total), *Editores* (editar), *Lectores* (solo lectura).
   - Configure `10_Data/` y `20_Raster_Data/` como de solo lectura para la mayoría de los usuarios.
   - Restrinja `40_Working_Data/` solo para editores.

4. **Agregar contenido inicial**
   - Cargue conjuntos de datos autorizados en `10_Data/` (límites, caminos, capas de exposición).
   - Cargue algunos DEM o rásteres de cobertura terrestre en `20_Raster_Data/`.
   - Agregue estilos (`.qml`) y diseños (`.qpt`) de QGIS compartidos en `30_Styles_Templates/`.

5. **Habilitar la sincronización con OneDrive para acceder sin conexión**
   - El personal puede sincronizar la biblioteca `GIS_Hub` en sus computadoras portátiles.
   - Esto permite a QGIS utilizar rutas de archivos locales (más estables que los enlaces en línea).

6. **Documentar los POE en **`00_Admin/`**
   - Añada un simple archivo `ReadMe.md` o `SOPs.pdf` explicando lo siguiente:
     - Qué carpetas son de solo lectura.
     - Cómo nombrar los archivos.
     - Dónde guardar borradores y dónde los resultados finales.

7. **Incorporar personal**
   - Indique al nuevo personal dónde encontrar datos, proyectos y estilos.
   - Enfatice que solo los administradores de datos actualizan las carpetas `10_Data/` y `20_Raster_Data/`.

:::{tip}
Empiece de a poco. No cargue todo a la vez. Comience con los conjuntos de datos que se utilizan con más frecuencia en sus proyectos (p. ej., límites administrativos, centros de salud, WorldPop). 
Puede ampliar la biblioteca más adelante, a medida que el equipo se familiarice con el sistema.
:::

## Procedimientos operativos estándar (POE)

Una estructura de carpetas clara solo es útil si todos la aplican de manera consistente. 
Para evitar confusiones y pérdida de datos, las organizaciones deben acordar algunas reglas simples. 
Estos **procedimientos operativos estándar (POE)** pueden servir como punto de partida:

1. **Carga de datos** 
   Solo los administradores de datos pueden agregar o actualizar archivos en `10_Data/` y `20_Raster_Data/`. 
   Otros miembros del personal pueden descargar estos conjuntos de datos, pero no modificarlos.

2. **Nombrar archivos** 
   Siga siempre la convención de nombres acordada (véase la sección sobre nombres). 
   Esto garantiza que sea fácil encontrar los conjuntos de datos y evita la duplicación.

3. **Datos de trabajo**
   - Use `40_Working_Data/` solo para borradores, procesamiento intermedio o ediciones temporales.
   - Para evitar problemas de sincronización (especialmente con archivos grandes), el personal también puede guardar los archivos de trabajo **localmente en su propia computadora**.
   - Antes de los fines de semana, o cuando sea necesario compartir los resultados con el equipo (para copias de seguridad y contingencias), cargue los archivos relevantes en `40_Working_Data/`.

4. **Carpetas de proyectos** 
   Cada proyecto debe tener su propia subcarpeta en `50_Projects/` (p. ej., `FloodResponse_2025/`). 
   Allí guarde:
   - Proyectos de QGIS (`.qgz`).
   - Resultados finales del análisis (mapas, informes, tablas).
   - Una copia de los **conjuntos de datos que realmente se utilizan en el proyecto** (para que el trabajo pueda reproducirse posteriormente).

5. **Plantillas** 
   Aplique siempre los estilos y diseños de QGIS compartidos desde `30_Styles_Templates/` al producir mapas o análisis. 
   Esto mantiene la consistencia de los resultados en toda la organización.

6. **Flujos de trabajo de PAT (si corresponde)** 
   Para una acción anticipatoria, almacene los datos de referencia en `50_Cyclone_EAP/Fixed_Data/`, los modelos en `50_Cyclone_EAP/Models/`, 
   y cree una nueva carpeta para cada activación en `50_Cyclone_EAP/Activations/`.

7. **Registro de cambios** 
   Mantenga un registro simple `00_Admin/` (p. ej., `Change_Log.xlsx`) donde los administradores registren actualizaciones a los datos o plantillas.

8. **Permisos** 
   Administre el acceso a través de los grupos de SharePoint, no para cada persona:
   - *Propietarios* → control total
   - *Editores* → editar (p. ej., para `40_Working_Data/` y las carpetas de proyectos)
   - *Lectores* → solo lectura (para la mayoría de las carpetas de datos)

:::{tip}
Los POE breves son más eficaces si caben en **una página**. 
Manténgalos simples y revíselos una vez al año para asegurarse de que sigan siendo relevantes. 
Enfatice que **los archivos de trabajo diarios pueden permanecer en las computadoras portátiles individuales**. 
Cargue archivos a `40_Working_Data/` únicamente antes de los fines de semana, los cambios de turno o cuando sea necesario compartir los resultados para uso del equipo y en contingencias.
:::



