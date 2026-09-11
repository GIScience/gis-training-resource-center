::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 3 : Sources de données <a id="exercise-3-data-sources"></a>

<!--This exercise is quite minimal with the explanation of steps (most should be looked up) so it is not suited for a follow along session -->

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

:::{card}
:class-card: sd-text-justify
__Objectif de l’exercice :__
^^^

L’objectif de cet exercice est d’explorer différentes sources de données, de comprendre où et comment accéder à des données pertinentes, et d’identifier les problèmes potentiels. Il est important d’**utiliser des sources de données fiables, à jour et adaptées** à l’objectif de l’analyse afin de garantir des résultats pertinents et exploitables. Gardez toujours à l’esprit les objectifs et les exigences de votre analyse lorsque vous recherchez des données.

:::

::::{grid} 2
:::{grid-item-card}
__Parcours d’exercices sur la réponse aux inondations à Larkana__
^^^

Cet exercice fait partie du [parcours d’exercices sur la réponse aux inondations à Larkana](https://giscience.github.io/gis-training-resource-center/content/fr/Exercise_tracks/fr_larkana_flood_response.html).

:::

:::{grid-item-card}
__Compétences couvertes par cet exercice__
^^^ 

- Fondamentaux QGIS
- Rechercher et télécharger des jeux de données pertinents et les préparer pour une analyse ultérieure
- Littératie des données

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice :__
^^^

- L’exercice prend environ 1 heure, selon le nombre de participant·e·s et leur familiarité avec les outils informatiques.

:::

:::{grid-item-card}
__Articles wiki et chapitres de module pertinents__
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Types de données géographiques](/content/fr/Wiki/fr_qgis_geodata_types_wiki.md)
* [Import de données géographiques dans QGIS](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md)
* [Concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)
* [Classification des données géographiques - Graduée](/content/fr/Wiki/fr_qgis_graduated_wiki.md)
* [Sources de données](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_data_sources.html)

:::

::::

## Instructions pour les formateur·rice·s <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Espace formateur·rice__ 
## Préparer la formation : <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. un tableau Miro) sur lequel les participant·e·s peuvent ajouter leurs remarques et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment animer des formations ?](/content/fr/Trainers_corner/fr_how_to_training.md) pour quelques conseils généraux sur la conduite d’une formation.

## Animer la formation <a id="conduct-the-training"></a>

__Introduction :__

- Présentez l’idée et l’objectif de l’exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a décompressé le dossier avant de commencer les tâches.

__Suivi pas à pas :__

- Montrez et expliquez chaque étape vous-même au moins deux fois, et suffisamment lentement pour que tout le monde puisse voir ce que vous faites et suivre dans son propre projet QGIS. 
- Assurez-vous que tout le monde suit bien et effectue les étapes en demandant régulièrement si quelqu’un a besoin d’aide ou si tout le monde suit toujours.  
- Soyez disponible et patient·e face à chaque question ou difficulté qui pourrait se présenter. Vos participant·e·s sont en situation de multitâche : ils doivent à la fois prêter attention à vos consignes et se repérer dans leur propre projet QGIS.

__Conclusion :__

- Gardez du temps à la fin de l’exercice pour traiter les éventuels problèmes ou questions liés aux tâches.
- Prévoyez également un moment pour les questions ouvertes.

:::

## Exercice <a id="exercise"></a>

### Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Backup/Module_2_Exercise_3_Data_Sources.zip

Téléchargez les données et le fichier projet pour cet exercice [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Backup/Module_2_Exercise_3_Data_Sources.zip) puis décompressez le dossier.

:::


::::{dropdown} Arborescence de dossiers standard
:::{figure} /fig/standard_folder_structure_new_2025.drawio.png
name: standard_folder_struc
width: 500 px
---
Arborescence de dossiers standard. Source : HeiGIT
:::
::::

### Tâche 1 : Télécharger les limites administratives et les sites de santé pour le Pakistan <a id="task-1-download-the-administrative-boundaries-and-healthsites-for-pakistan"></a>

Pour notre carte de réponse aux inondations, nous aurons besoin de quelques jeux de données provenant du web. Dans cet exercice, nous allons rechercher les __limites administratives__ du Pakistan, les __sites de santé__, ainsi que l’__étendue des inondations__ au Pakistan en 2024.  
Commençons par créer un nouveau projet QGIS et mettre en place l’arborescence de dossiers standard :

::::{margin}
:::{tip}
Consultez l’arborescence de dossiers standard et enregistrez le fichier projet QGIS au bon endroit.
:::
::::

1. Téléchargez l’arborescence de dossiers puis décompressez-la.
2. Créez une copie de cette arborescence et nommez le dossier `module_2_exercise_3_data_sources`.
3. Ouvrez un nouveau projet QGIS et enregistrez-le dans ce dossier.

Maintenant que le projet QGIS est créé, nous pouvons commencer à rechercher les jeux de données.

4. Trouvez une source de données permettant de télécharger les **limites administratives** et les **sites de santé** du Pakistan. Les instructions suivantes sont conçues pour l’exemple du Pakistan. Si vous souhaitez réaliser la même analyse pour un autre pays, certaines instructions pourront différer, mais le flux de travail général restera le même.

:::{dropdown} Sources de données possibles

Il existe de nombreux dépôts de données sur le web où vous pouvez trouver des données appropriées. Vous trouverez une liste de sources de données possibles [ici](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_data_sources.html).

Pour la plupart des données humanitaires, vous pouvez effectuer vos recherches sur le __[Humanitarian Data Exchange/HDX](https://data.humdata.org/)__.
Le Humanitarian Data Exchange (HDX) est une plateforme de référence pour accéder à des données géospatiales utiles dans les contextes de crise humanitaire. C’est un dépôt centralisé offrant un large éventail de jeux de données issus de différentes sources, ce qui en fait une ressource précieuse pour les organisations d’aide et les chercheur·euse·s.

:::

:::{admonition} Quel format de données choisir

La plupart des jeux de données disponibles sur HDX existent dans différents formats, par exemple xlsx, csv, shapefile ou GeoJSON. Nous recherchons ici des données spatiales utilisables dans QGIS ; il nous faut donc un format spatial tel que `.shp` (Shapefile), `.gpkg` (GeoPackage), `.geojson` (GeoJSON) ou `.gdb` (GeoDatabase).

:::

<!-- SUGGESTION: some of the instructions below assume that these are the datasets
   that are being used, instead of just examples. Can we just ask people to use these
   datasets, so that the rest of the instructions make sense? -->

5. Téléchargez les données et enregistrez les **limites administratives** et les **sites de santé** dans le dossier `data\input`.

:::{Note}
Veillez à n’utiliser que les données de type point issues du jeu de données des sites de santé. Les autres géométries, comme les lignes ou les polygones, peuvent être ignorées dans cet exemple. Selon la source, l’information peut être fournie sous forme de points, mais aussi sous forme de lignes ou de polygones.
:::

::::{margin}
:::{tip}
La plupart du temps, les jeux de données téléchargés depuis le web sont compressés sous forme de fichiers `.zip`. Avant de pouvoir les utiliser dans QGIS, __vous devez les décompresser__.
:::
::::

6. [Chargez les deux fichiers vectoriels dans QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_qgis_geodata_concept.html#data-import).

7. Ajoutez ensuite le fond de carte OpenStreetMap via la fenêtre du navigateur → `XYZ Tiles`. L’ajout d’un fond de carte peut vous aider à vous repérer, à mieux comprendre la zone d’intérêt et à produire des cartes plus informatives.

8. Familiarisez-vous avec les données en ouvrant la table attributaire et identifiez les différents types de structures de santé présents dans le jeu de données. Faites le point sur les informations stockées dans chaque colonne. Par exemple, certaines colonnes peuvent indiquer le type de site de santé.

9. Si votre jeu de données contient des informations sur le type de site de santé (par ex. clinique, hôpital, médecin, etc.), nous pouvons extraire ces entités et les enregistrer dans une nouvelle couche. Pour cela, sélectionnez les hôpitaux puis copiez-les dans une nouvelle couche.

:::{Hint}

Pour savoir comment filtrer facilement vos données en sélectionnant manuellement des entités dans la table attributaire après avoir trié une colonne, consultez la page __[table attributaire](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)__ du wiki.

:::

### Tâche 2 : Télécharger l’étendue des inondations au Pakistan pour août 2024 <a id="task-2-download-the-flood-extent-for-pakistan-for-august-2024"></a>

Téléchargeons maintenant l’étendue des inondations au Pakistan du 8 au 12 août 2024.

1. Retournez sur le Humanitarian Data Exchange et recherchez __"Pakistan Flood"__. Vous trouverez une liste de jeux de données contenant des étendues d’eau détectées par satellite pour différentes périodes.
2. Choisissez le jeu de données intitulé __"Satellite detected water extents from 08 to 12 August 2024 over Pakistan"__ et téléchargez le dossier zip.
3. Décompressez le dossier et examinez son contenu. Il contient plusieurs shapefiles. Nous recherchons l’__étendue minimale des inondations__. Repérez les fichiers nommés `VIIRS_20240721_20240803_MinimumFloodExtent_PAK` et copiez-les dans le dossier `data\input`.

:::{admonition} Travailler avec des shapefiles
:class: attention
Les shapefiles sont composés de plusieurs fichiers (`.shp`, `.shx`, `.sbx`, `.sbn`, `.prj`, `cpg`). Pour copier correctement l’ensemble du shapefile vers un nouvel emplacement, __assurez-vous de copier tous les fichiers portant exactement le même nom dans le nouveau dossier__.

:::