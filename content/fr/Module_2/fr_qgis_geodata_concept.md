::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Introduction aux données géographiques et aux couches <a id="introduction-to-geodata-and-layers"></a>

**Compétences :**

Dans ce chapitre, vous apprendrez ce que sont les __données géographiques__ et vous comprendrez la différence entre les __données vectorielles et raster__. En outre, ce chapitre explique le __concept de couche__ dans les logiciels SIG, qui est fondamental pour chaque carte que vous créerez.

## Qu’est-ce qu’une donnée géographique ? <a id="what-is-geodata"></a>

Les données géographiques, ou données géospatiales, sont des données comportant une information géographique. Cela signifie que les données se rapportent à une localisation définie par des coordonnées. Elles sont similaires à d’autres formes de données pouvant être représentées dans des tableaux (comme des feuilles de calcul Excel ou des fichiers CSV), mais chaque élément du jeu de données contient également une information de coordonnées (voir {numref}`en_vector_raster`). Les logiciels SIG nous aident à visualiser et manipuler les données géographiques dans un espace 2D (voire 3D). Il existe deux grands types de données géographiques : **les données vectorielles et les données raster**. Ces deux types représentent des objets tangibles ou non tangibles du monde réel. Toutefois, leur manière de stocker l’information est très différente. Par conséquent, leur manipulation et leur représentation diffèrent fortement. Comprendre la différence entre ces deux types de données, savoir travailler avec chacun séparément, ainsi que les combiner, constitue l’une des compétences principales que vous développerez en apprenant les SIG.

:::{figure} /fig/en_vector_raster.png
---
width: 500px
align: center
name: en_vector_raster
---
Concept raster / vecteur (Source : adapté de [WikiMedia](https://commons.wikimedia.org/wiki/File:Raster_vector_tikz.png)).
:::

Les types d’informations pouvant être stockés dans des données géographiques sont presque illimités. Elles peuvent contenir des informations sur le monde physique, par exemple :

* des données d’altitude
* des données environnementales (sols, climat, température, précipitations, informations sur des événements météorologiques ou des phénomènes naturels, comme l’étendue d’une inondation)
* des données sur les infrastructures, les bâtiments, les transports, etc.
* des données socioculturelles ou économiques, telles que des données démographiques, des limites administratives, des événements sociaux, des données sur la criminalité, etc.

Les données géographiques représentent généralement les enregistrements de données sous forme de __géométries__ sur un canevas 2D. Ces géométries peuvent être des points, des lignes, des polygones, voire des pixels, et représenter différents objets du monde physique — comme des routes, des lacs ou des arbres — ou des objets immatériels — comme des limites administratives, des effectifs de population, des indicateurs de santé, des événements historiques, etc.

### Données vectorielles <a id="vector-data"></a>

Les données vectorielles sont des objets numériques capables de stocker des informations géographiques/spatiales ainsi que d’autres attributs. Elles sont donc idéales pour visualiser des informations sur une carte. Chaque entité peut être représentée sur une carte à l’aide de l’une des trois géométries suivantes : __points, lignes ou polygones__ (voir {numref}`en_vector_data_overview`). Une couche ne peut contenir que des entités ayant le même type de géométrie.

:::{figure} /fig/en_vector_data_overview.png
---
width: 650px
align: center
name: en_vector_data_overview
---
Vue d’ensemble des données vectorielles (Source : HeiGIT).
:::

- Les données ponctuelles ne comportent généralement qu’un seul ensemble de coordonnées par enregistrement (longitude, latitude et parfois altitude, souvent notées x, y et z).
- Les lignes sont construites en reliant plusieurs points, enregistrés comme une seule entité.
- Les polygones sont également construits en reliant plusieurs points, mais ils forment une géométrie fermée. Chaque géométrie est alors représentée par une seule entité.

Chaque entité stocke sa localisation (sous forme d’adresse ou de coordonnées) ainsi que d’autres attributs, par exemple un nom, un identifiant ou toute autre information ({numref}`en_geodata_example_2`). Le type de géométrie utilisé dépend du type de donnée représentée. Par exemple, une route pourra être représentée par une ligne, l’emprise d’un bâtiment par un polygone et un arbre par un point.

:::{figure} /fig/en_geodata_example_2.png
---
name: en_geodata_example_2
width: 700px
---
L’information géographique peut être une adresse et/ou des coordonnées GPS (Source : British Red Cross).
:::

- Les entités sont représentées sur la carte par des géométries, mais elles sont constituées d’informations organisées dans des tables (voir {numref}`Geodata_attribute_table_example`).
- Chaque ligne du tableau correspond à une entité sur la carte, tandis que chaque colonne contient une information attributaire (champ).
- Plusieurs attributs peuvent être associés à chaque entité.

:::{figure} /fig/Geodata_attribute_table_example.png
---
name: Geodata_attribute_table_example
width: 750px
---
Table de données dans Microsoft Excel contenant des informations géographiques. (Source : British Red Cross).
:::

{numref}`example_geometric_vs_attribute_view` montre le même jeu de données affiché à la fois sous sa représentation géométrique et sous forme de table attributaire.

:::{figure} /fig/example_geometric_and_attribute_view.png
---
name: example_geometric_vs_attribute_view
width: 700 px
---
Chaque polygone à gauche représente une ligne (entité) à droite. (Source : British Red Cross).
:::

#### Formats de fichiers vectoriels <a id="vector-file-formats"></a>

Il existe plusieurs formats de fichiers pour les données vectorielles. Ils diffèrent par la façon dont les géométries et les attributs sont stockés. Toutefois, ils ne contiennent toujours que des points, des lignes ou des polygones. Certains formats présentent des avantages par rapport à d’autres, tandis que certains sont encore utilisés par habitude, bien qu’ils soient dépassés.
Le tableau suivant donne une courte description des formats de fichiers vectoriels les plus courants.

| Filename extension| Name | Description |
| ----------- | ---------------------- | --------------------------------------------------------- |
|`.shp`       | Shapefile              | Un shapefile est un format de fichier de données vectorielles couramment utilisé en analyse géospatiale. Il stocke la localisation, la géométrie et les attributs des entités ponctuelles, linéaires et polygonales. C’est un format courant utilisé par la plupart des logiciels SIG et des plateformes de cartographie en ligne. Le format est ancien, mais reste très largement utilisé. Un shapefile ne peut contenir qu’un seul jeu de données. Un shapefile complet doit comprendre au minimum trois fichiers distincts (.shp, .shx, .dbf).| 
|`.gpkg`      | GeoPackage             | Le nouveau standard pour les données géographiques. Les fichiers GPKG sont un format ouvert, portable et basé sur SQLite pour stocker des données géospatiales vectorielles et raster, compatibles avec différentes plateformes SIG sur poste de travail, web et mobile. Ils peuvent contenir plusieurs jeux de données (vecteur, raster et données non spatiales comme des tables). |
|`.kml`/`.kmz.`       |Keyhole Markup Language | Format de données géographiques destiné à être utilisé avec [Google Earth]( https://earth.google.com/web/). Les fichiers KMZ sont des versions compressées des fichiers KML (Keyhole Markup Language) utilisées pour stocker des données géographiques, telles que des points, des tracés et des polygones, ainsi que des ressources associées comme des images et des icônes. Couramment utilisés avec Google Earth et d’autres logiciels cartographiques, les fichiers KMZ regroupent les données spatiales et les ressources dans un seul fichier compact, ce qui facilite le partage de cartes interactives et de visualisations.|
| `.gpx`      | GPS Exchange Format    | Format de données géographiques destiné à l’échange de coordonnées, par exemple pour des points de passage ou des traces. |
| `.geojson`  | GeoJSON                | Format de données ouvert utilisant la notation JSON (Javascript Object Notation) pour stocker des données géographiques. Il peut contenir plusieurs types de géométrie dans un seul fichier et est largement compatible avec les applications web et mobiles. | 
| `.gdb`      | Geodatabase            | Conçu pour une gestion efficace des données, l’analyse spatiale et des flux de travail géospatiaux complexes. Les geodatabases sont un format propriétaire d’Esri destiné au stockage et à la gestion de grands volumes de données spatiales, y compris des classes d’entités, des tables et des relations dans une base de données structurée. |

:::{note}

Les différents formats de fichiers répondent à des usages distincts et présentent des avantages ou des limites.

- Par exemple, les fichiers __GeoJSON__ ne peuvent pas stocker les informations de projection et sont par convention limités à l’ellipsoïde WGS84. Cela les rend difficiles à utiliser dans des projets fondés sur des projections régionales spécifiques ou sur des projections reposant sur d’autres ellipsoïdes.

- Contrairement aux autres formats, __Geodatabase__ et __GeoPackage__ sont des bases de données. En SIG, les bases de données stockent les données spatiales dans des systèmes structurés et évolutifs permettant l’accès multi-utilisateur, les requêtes complexes et la gestion de grands volumes de données, ce qui les rend adaptées à l’analyse et à la gestion de données à l’échelle d’une organisation. Les fichiers, quant à eux, stockent les données dans des formats individuels et portables comme Shapefile, GeoJSON ou GeoPackage, plus faciles à partager et à utiliser hors ligne, mais moins performants pour les requêtes avancées et moins évolutifs.

:::

#### Structure d’un shapefile <a id="shapefile-structure"></a>

Un shapefile est un ensemble de fichiers distincts, généralement regroupés dans un même dossier/répertoire. Certains fichiers sont obligatoires, d’autres sont optionnels (voir {numref}`en_shapefile_structure`). Pour disposer d’un shapefile fonctionnel, il faut que tous les fichiers obligatoires se trouvent dans le même dossier.

:::{figure} /fig/en_shapefile_structure.png
---
name: en_shapefile_structure
width: 400 px
---
__SHP, SHX__ et __DBF__ sont les fichiers __obligatoires__ qu’un shapefile doit contenir pour fonctionner correctement. Le fichier SHP est le fichier principal et contient la géométrie.
:::

### Données raster <a id="raster-data"></a>

Un autre type de données géospatiales est constitué par les données raster. Les données raster sont composées de cellules organisées en une grille de lignes et de colonnes, formant ainsi un raster. Chaque cellule, ou pixel, contient une valeur qui porte une information (par exemple la température ou la densité de population). Comme les données raster sont constituées de pixels, les photographies aériennes ou les images satellites peuvent également être utilisées comme données raster, à condition qu’elles possèdent des coordonnées géographiques (voir [module 3 : Géoréférencement](/content/fr/Module_3/fr_qgis_georeferencing.md)).

Les usages typiques des données raster sont :

* les données d’altitude (souvent appelées modèle numérique d’élévation ou MNE)
* les données de précipitations
* les données de température interpolées
* la densité de population

La valeur de chaque cellule est généralement visualisée en associant une couleur à une valeur. Pour les données d’altitude, par exemple, on utilise souvent une rampe colorée. Pour les données catégorielles, comme l’occupation du sol, on utilise des catégories de couleurs (par exemple vert = forêt ; jaune = terres agricoles ; rouge = zones résidentielles).

:::::{grid} 2
::::{grid-item-card}

:::{figure} /fig/raster_data_example_corine_LC.png
---
name: raster_data_example_corine_LC
width: 350 px
align: left
---
Le jeu de données CORINE Land Cover de Copernicus (Source : [EEA/Copernicus](https://land.copernicus.eu/en/map-viewer?product=130299ac96e54c30a12edd575eff80f7)).
:::

::::

::::{grid-item-card}

:::{figure} /fig/NASADEM_Alps_example.png
---
name: NASADEM_Alps_example
width: 300 px
---
Le MNE de la NASA montrant les Alpes (Source : [NASA/USGS/JPL-CALTECH](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)).
:::

::::
:::::

Les valeurs raster n’ont généralement qu’une seule valeur par cellule, mais elles peuvent aussi comporter plusieurs bandes (de couleur). Les images satellites proposent souvent plusieurs bandes représentant des données collectées dans différentes parties du spectre lumineux, que nous pouvons utiliser pour analyser différents phénomènes, comme l’humidité de la végétation. Plusieurs bandes signifient donc plusieurs valeurs par cellule.

Les principales caractéristiques spatiales sont l’emprise — la surface représentée dans le monde réel (10 km², 100 km²) — et la résolution raster — la taille de chaque pixel. Dans {numref}`en_quality_raster`, vous pouvez voir deux jeux de données raster ayant des résolutions différentes.

:::{figure} /fig/en_quality_raster.png
---
width: 800px
align: center
name: en_quality_raster
---
Deux jeux de données raster de résolutions différentes couvrant la même région. (Source : [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_3_vector_raster_data)).
:::

Dans {numref}`Vector` et {numref}`Raster`, vous pouvez voir le même lieu : à gauche sous forme de données vectorielles représentant les rues et les zones urbaines, et à droite sous forme de données raster (image satellite) montrant l’occupation du sol.

:::::{grid} 2
::::{card} Vector

:::{figure} /fig/en_same_location_vector.png
---
width: 400px
name: Vector
align: center
---
Entités représentées sous forme de données vectorielles. (Source : British Red Cross).
:::

::::

::::{card} Raster

:::{figure} /fig/en_same_location_raster.png
---
width: 400px
name: Raster
align: center
---
Le même lieu représenté sous forme d’image raster. (Source : British Red Cross).
:::

::::
:::::

#### Formats de données raster <a id="raster-data-formats"></a>

Les données raster peuvent se présenter dans les formats suivants :

| Filename extension| Name | Description |
| ----- | --- | --- |
|`.tif`/`.tiff`/`.geotiff`|Tag Image File Format|Format courant pour les données raster et image. Il ne contient pas nécessairement des données géoréférencées. Si un fichier `.tif` est géoréférencé, on parle de GeoTIFF.|
|`.nc`|netCDF|Format standard pour les données scientifiques telles que la vitesse ou la température. Peut être un fichier raster. Peut contenir plusieurs jeux de données.|
|`.asc`|Esri ASCII Grid files|Ancien format raster simple, toujours géoréférencé.|

:::{admonition} L’avantage des géodatabases

Les bases de données telles que la Geodatabase (`.gdb`) ou le GeoPackage (`gkpg`) peuvent également contenir des couches raster.

:::

----

## Le concept de couche <a id="the-layer-concept"></a>

Les logiciels SIG nous aident à visualiser les données géographiques. Pour cela, ils affichent les géométries ou les cellules raster sur un canevas 2D. Cependant, lorsque nous créons une carte, nous utilisons plusieurs jeux de données simultanément. Chaque type de donnée géographique, qu’il s’agisse de données raster, de polygones, de points ou de lignes, est généralement stocké dans une __couche__. Chaque couche est composée d’objets géographiques du même type (ligne, polygone, raster, etc.). Les logiciels SIG affichent ces couches les unes au-dessus des autres et permettent d’en réorganiser l’ordre afin de produire des cartes pertinentes (voir {numref}`en_layer`).

En ajoutant différentes couches, vous construisez votre carte et pouvez combiner des informations provenant de différentes sources. Vous pouvez ensuite réaliser des analyses ou adapter la représentation en utilisant des symboles et des couleurs.

:::{figure} /fig/en_layer.png
---
width: 800px 
align: center
name: en_layer
---
Les couches dans un SIG (Source : [CartONG](https://cartong.pages.gitlab.cartong.org/learning-corner/en/3_key_gis_concepts/3_3_key_concepts/3_3_1_layers)).
:::

::::{admonition} À vous de jouer !
:class: note

La pratique est essentielle pour maîtriser les SIG. C’est le bon moment pour appliquer ce que nous avons vu dans le premier exercice du module 2.

:::{card}
:class-card: sd-text-center sd-rounded-2 sd-border-1
:link: https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_qgis_geodata_concept_ex1.html

__Module 2 Exercice 1 : Comprendre les données géographiques__

:::
::::

## Import de données <a id="data-import"></a>

Avant de pouvoir commencer à créer des cartes dans QGIS, vous devez charger vos données dans le logiciel. Selon le format de fichier à importer, le processus varie légèrement.

### Import de données vectorielles <a id="vector-data-import"></a>

Les formats vectoriels les plus courants sont le Shapefile (`.shp`) et le GeoPackage (`.gpkg`). Le processus d’importation est identique pour ces deux formats.

QGIS propose plusieurs façons de charger des données vectorielles. La plus directe est le glisser-déposer, qui consiste à faire glisser les fichiers depuis votre explorateur de fichiers vers la fenêtre de QGIS. Une autre méthode consiste à utiliser le "__Gestionnaire des sources de données__" (`Layer` → `Data Source Manager`). Vous pouvez également ouvrir le gestionnaire via le raccourci clavier <kbd>CTRL</kbd> + <kbd>L</kbd>.

:::{Note}
Les fichiers GeoPackage peuvent contenir plusieurs jeux de données et même des projets QGIS complets. Lorsque vous chargez un GeoPackage dans QGIS, une fenêtre s’ouvre pour vous permettre de sélectionner les jeux de données à charger.
:::

#### Ouvrir des données vectorielles via le Gestionnaire des sources de données <a id="open-vector-data-via-the-data-source-manager"></a>

1. Cliquez sur `Layer` → `Add Layer` → `Add Vector Layer...`. Cela ouvrira le Gestionnaire des sources de données.
2. Cliquez sur les trois points ![](/fig/Three_points.png) et accédez à votre fichier vectoriel.
3. Sélectionnez le fichier puis cliquez sur `Open`. D’autres options apparaîtront. Dans la plupart des cas, vous pouvez les laisser telles quelles.
4. De retour dans la fenêtre QGIS, cliquez sur `Add`.

:::{Attention}
QGIS vous permet d’importer uniquement des shapefiles __décompressés__. Veillez à décompresser vos fichiers avant de les importer dans QGIS.
:::

:::{dropdown} Vidéo : importer des données vectorielles via le Gestionnaire des sources de données

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_vector.mp4"></video>

:::

#### Ouvrir des données vectorielles par glisser-déposer <a id="open-vector-data-via-drag-and-drop"></a>

QGIS vous permet d’ouvrir des données dans votre projet simplement en faisant glisser les fichiers depuis votre explorateur vers la fenêtre de QGIS. Les shapefiles ne contiennent qu’une seule couche par fichier, qui sera automatiquement ajoutée dans le panneau des couches. Les fichiers GeoPackage (`.gpkg`) peuvent contenir plusieurs couches dans un même fichier. Si vous ajoutez un fichier GeoPackage, une nouvelle fenêtre s’ouvrira pour vous demander de sélectionner les couches à ajouter à votre projet.

:::{dropdown} Vidéo : importer des données vectorielles par glisser-déposer
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

### Import de texte délimité (.csv, .txt) <a id="delimited-text-import-csv-txt"></a>

Au cours de votre pratique des SIG, vous rencontrerez souvent des données géographiques sous forme de fichiers texte délimités, comme les fichiers `.csv` (Comma Separated Values). Ces fichiers contiennent des données tabulaires, qui peuvent être ouvertes avec des logiciels comme Microsoft Excel. Ils contiennent des informations géographiques ou de position sous forme de coordonnées ponctuelles dans des colonnes distinctes (par exemple latitude et longitude, ou coordonnées x et y), ou sous forme de "Well Known Text" (WKT), qui permet de représenter des géométries plus complexes, comme des polygones ou des lignes.

#### Ouvrir une couche de texte délimité <a id="open-delimited-text-layer"></a>

:::{Tip}
Pour charger des données issues de feuilles de calcul comme des fichiers CSV (`.csv`) ou Excel (`.xlsx`), les jeux de données doivent contenir des colonnes de géométrie — le plus souvent sous la forme de latitude (champ Y) et longitude (champ X), mais cela peut aussi être d’autres formats comme le WKT. Dans ce cas, votre fichier texte délimité peut également contenir des géométries complexes.
:::

:::{figure} /fig/en_import_delimeted_text.png
---
width: 600px 
align: center
name: en_import_delimeted_text
---
Importer un texte délimité dans QGIS 3.36.
:::

1. `Layer` → `Add Layer` → `Open Delimited Text Layer`.
2. Cliquez sur `File name`, puis sur les trois points ![](/fig/Three_points.png), accédez à votre fichier CSV et cliquez sur `Open`.
3. `File Format` : ici, vous pouvez préciser quel délimiteur est utilisé dans le fichier à importer. Dans un fichier CSV standard, il s’agit de la virgule `,`. Si ce n’est pas le cas, sélectionnez `Custom delimiters`. Vous pourrez alors choisir le délimiteur exact utilisé dans le fichier.

:::{Tip}
Pour savoir quel délimiteur est utilisé, vous pouvez ouvrir le fichier `.csv` dans le Bloc-notes ou dans Excel. Vous pourrez ainsi vérifier quel caractère sépare les informations.
:::

:::{figure} /fig/en_delimited_text_fileformat.png
---
width: 600px
align: center
name: en_delimited_text_fileformat
---
Réglage des paramètres de format lors de l’import d’une couche de texte délimité dans QGIS.
:::

4. `Geometry definition` : dans cette section, vous indiquez quelles colonnes du fichier contiennent les informations spatiales permettant de géoréférencer les données sur la carte. Si le fichier comporte une colonne de __latitude__ et une autre de __longitude__, vous pouvez les utiliser pour géoréférencer les données. Cochez `Point Coordinates` si le fichier `.csv` contient des données ponctuelles. Sélectionnez “LONGITUDE” pour le `X field` et “LATITUDE” pour le `Y field`.
5. Sous `Geometry CRS`, sélectionnez le système de coordonnées de référence (SCR). Par défaut, QGIS choisira le SCR du projet. Si le fichier ne contient pas d’informations spatiales, choisissez l’option `No geometry (attribute only table)`.
6. Cliquez sur `Add`.

:::{dropdown} Vidéo : ouvrir des fichiers texte délimités dans QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>

:::

### Import de données raster <a id="raster-data-import"></a>

L’import de données raster fonctionne de la même manière que pour les données vectorielles. Vous pouvez soit glisser-déposer les fichiers raster dans la fenêtre de QGIS, soit les ouvrir via le "Gestionnaire des sources de données".

:::{dropdown} Vidéo : ouvrir des données raster via le Gestionnaire des sources de données

1. Cliquez sur `Layer` → `Add Layer` → `Add Raster Layer`.
2. Cliquez sur les trois points ![](/fig/Three_points.png) et accédez à votre fichier raster.
3. Sélectionnez le fichier puis cliquez sur `Open`.
4. De retour dans QGIS, cliquez sur `Add`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_raster.mp4"></video>

:::

:::{dropdown} Vidéo : ouvrir des données raster par glisser-déposer

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_raster_d_d.mp4"></video>

:::

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

Vérifiez si vous maîtrisez les concepts clés de ce chapitre en répondant aux questions ci-dessous.

1. __Définissez les données géographiques. Qu’est-ce qui les distingue de données tabulaires classiques ?__

:::{dropdown} Réponse
Les données géographiques, ou données spatiales, désignent des informations associées à une localisation précise à la surface de la Terre. Elles incluent à la fois la géométrie (la composante spatiale) et les attributs (les données descriptives). Contrairement aux données tabulaires classiques, qui se limitent à des lignes et des colonnes sans référence spatiale, les données géographiques comportent une composante géographique permettant leur cartographie et leur analyse dans un contexte spatial.
:::

2. __Quels sont les deux principaux types de données géographiques et comment stockent-ils l’information ?__

:::{dropdown} Réponse
Les deux principaux types de données géographiques sont :
- Les __données vectorielles__ : elles représentent des entités géographiques sous forme de points, lignes et polygones. Chaque entité possède des attributs stockés dans une table. Les formats courants incluent Shapefile (`.shp`), GeoPackage (`.gpkg`) et GeoJSON (`.geojson`).
- Les __données raster__ : elles représentent l’information géographique sous la forme d’une matrice de cellules (pixels), chaque cellule portant une valeur, par exemple une température ou une altitude. Les formats courants incluent GeoTIFF (`.tif` ou `.tiff`), JPEG2000 (`.jp2`) et Esri ASCII Grid (`.asc`).

:::

3. __Donnez des exemples de phénomènes ou d’objets du monde réel mieux représentés sous forme de données vectorielles ou raster.__

:::{dropdown} Réponse
__Données vectorielles :__ adaptées à la représentation d’entités discrètes aux limites bien définies, par exemple :
   - Limites administratives (pays, districts)
   - Routes et rivières
   - Parcelles
   - Bâtiments et infrastructures
__Données raster :__ adaptées à des phénomènes continus variant dans l’espace, par exemple :
   - Images satellites
   - Modèles d’élévation (par ex. modèles numériques d’élévation ou de terrain)
   - Cartes de température ou de précipitations
   - Occupation du sol
:::

4. __Décrivez la structure d’un shapefile. Quels fichiers obligatoires doivent l’accompagner ?__

:::{dropdown} Réponse

Un Shapefile est un format vectoriel très répandu composé d’au moins trois fichiers obligatoires :
- `.shp` : contient la géométrie (points, lignes ou polygones).
- `.shx` : contient l’index de la géométrie, permettant des requêtes spatiales rapides.
- `.dbf` : contient les données attributaires sous forme tabulaire, associées à chaque géométrie.

Il peut aussi contenir des fichiers supplémentaires, comme `.prj`. Ensemble, ces fichiers partageant le même nom constituent le shapefile.
:::

5. __Expliquez le concept de “couche” en SIG. Pourquoi les systèmes SIG utilisent-ils des couches pour construire des cartes ?__

:::{dropdown}
En SIG, une couche est un ensemble de données géographiques représentant un type d’information spécifique, comme des routes, des rivières ou l’occupation du sol. Les couches sont empilées les unes sur les autres pour créer une carte complète. L’utilisation de couches permet :
- une __gestion organisée des données__ : chaque couche peut être modifiée ou analysée indépendamment ;
- une __visualisation claire__ : différents types de données peuvent être stylisés et affichés séparément ;
- une __analyse efficace__ : les couches peuvent être activées ou désactivées pour se concentrer sur certains aspects des données.
:::

6. __Savez-vous comment importer des données vectorielles dans un projet QGIS ?__

:::{dropdown} Réponse
Les données vectorielles peuvent être importées dans un projet QGIS de deux façons :
- via le menu `Layer` → `Add vector layer` dans la barre supérieure ;
- en glissant-déposant directement le fichier vectoriel dans le canevas cartographique de QGIS.
:::

7. __Où les couches importées dans un projet QGIS sont-elles enregistrées ?__

:::{dropdown} Réponse
Les couches ne sont pas stockées à l’intérieur du projet QGIS. Lorsqu’elles sont importées, elles ne sont ni déplacées ni copiées. À la place, QGIS enregistre dans le fichier projet (`.qgz`) le chemin vers la source de données. Si la source est déplacée ou supprimée, QGIS ne pourra plus la localiser tant que le chemin n’aura pas été mis à jour.  
Par ailleurs, la modification d’une couche affecte le jeu de données d’origine.
:::

8. __Si vous disposez d’un fichier `.csv` ou d’un autre fichier texte délimité, quelles informations doit-il contenir pour pouvoir être importé dans QGIS comme couche de points ?__

:::{dropdown} Réponse
Pour importer un fichier `.csv` ou un fichier texte délimité comme couche de points dans QGIS, il doit :
- contenir une ligne d’en-tête avec les noms des champs ;
- comporter au moins deux colonnes représentant les coordonnées X (longitude) et Y (latitude) ;
- contenir des valeurs de coordonnées numériques et correctement formatées.

QGIS utilise ces colonnes de coordonnées pour positionner les points dans le canevas cartographique.
:::

::::
