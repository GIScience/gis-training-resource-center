::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 2 : Traitement de base des données géographiques <a id="exercise-2-basic-geodata-processing"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

:::{card}
__Objectif de cet exercice :__
^^^

L’objectif de cet exercice est de se familiariser avec les données géographiques et de commencer à les manipuler. Comprendre la table attributaire, la trier, effectuer des sélections manuelles et exporter ces sélections, ainsi qu’ajouter un fond de carte.

:::

::::{grid} 2
:::{grid-item-card}
__Type d’exercice de formation :__
^^^

- Cet exercice peut être utilisé en formation en ligne ou en présentiel. 
- Il peut être réalisé en mode pas-à-pas ou individuellement en autoformation.

:::

:::{grid-item-card}
__Compétences visées__
^^^ 

- Bases de QGIS
- Navigation dans l’interface de QGIS 
- Tri et manipulation de jeux de données via la table attributaire
- Sélection du système de coordonnées approprié
- Réalisation d’analyses spatiales de base et avancées

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice :__
^^^

- Environ 1 heure, selon le nombre de participants et leur familiarité avec les outils informatiques.

:::

:::{grid-item-card}
__Articles wiki associés :__
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Import de données dans QGIS](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md)
* [Concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)
* [Table attributaire dans QGIS](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)
* [Projections](/content/fr/Wiki/fr_qgis_projections_wiki.md)

:::

::::

## Instructions pour les formateurs <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Espace formateur__ 
__Préparation de la formation :__

- Prenez le temps de vous familiariser avec l’exercice et les ressources fournies.
- Préparez un tableau (physique ou numérique, par exemple Miro) permettant aux participants de noter leurs observations et questions. 
- Avant de commencer, assurez-vous que tous les participants ont installé QGIS et ont téléchargé __et décompressé__ les données.
- Consultez [Comment organiser une formation ?](/content/fr/Trainers_corner/fr_how_to_training.md) pour des conseils généraux.

__Conduite de la formation :__

__Introduction :__

- Présentez l’objectif de l’exercice.
- Fournissez le lien de téléchargement et vérifiez que les fichiers sont bien décompressés.

__Suivi pas-à-pas :__

- Montrez et expliquez chaque étape au moins deux fois, lentement, afin que les participants puissent suivre dans leur propre projet QGIS. 
- Vérifiez régulièrement que tout le monde suit et proposez de l’aide si nécessaire.  
- Soyez patient et disponible face aux questions ou difficultés.

__Conclusion :__

- Prévoyez du temps pour répondre aux questions liées à l’exercice.
- Laissez également un moment pour des questions ouvertes.

:::

## Exercice <a id="exercise"></a>

### Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_2/Module_2_Exercise_2_Basic_Geodata_Processing.zip 

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_2/Module_2_Exercise_2_Basic_geodata_processing.zip), enregistrez le dossier sur votre ordinateur et décompressez-le.__ 

:::

Le dossier zip contient :

| Nom du jeu de données | Titre original | Producteur | Source de téléchargement | 
| :-------------- | :----------------- |:----------------- |:----------------- |
| `nigeria_populated_places.shp` | Nigeria Populated Places (export OpenStreetMap) | Humanitarian OpenStreetMap Team (HOT) | [HDX](https://data.humdata.org/dataset/hotosm_nga_populated_places) | 
| `nigeria_boundaries.geojson` |   |   |   |

Le shapefile des localités contient des __données vectorielles de type point__ représentant les établissements humains au Nigeria (villes, villages, etc.). Le fichier GeoJSON des limites administratives contient des informations aux niveaux 2 et 4 (niveau 2 = pays, niveau 4 = États).

:::{note}

Le format GeoJSON ne supporte pas plusieurs couches : les limites du pays et des États sont donc regroupées dans une seule couche __avec des polygones qui se chevauchent__.

:::

### Tâches <a id="tasks"></a>

1. Chargez les deux fichiers dans QGIS.

2. Ajoutez le fond de carte OpenStreetMap via le panneau `Browser` → `XYZ Tiles`. 

3. Explorez les données en ouvrant la table attributaire. Identifiez le type d’informations disponibles, les colonnes et celles pertinentes pour votre analyse.

4. Dans la couche `nigeria_populated_places`, ouvrez la table attributaire, sélectionnez l’entité correspondant à **Zuyel**, puis zoomez sur ce point.

:::{hint}
Le nom commence par *Z*, vous pouvez trier la colonne `name` par ordre décroissant.
:::

5. Exportez **Zuyel** en tant que GeoPackage. Vérifiez la projection et choisissez un SCR approprié. Nommez le fichier `zuyel.gpkg`.

:::{note}
Aucun calcul n’étant nécessaire (surface, distance), le système WGS84 (EPSG:4326) est adapté.
:::

6. Répétez les étapes pour la couche `nigeria_boundaries.geojson` et exportez uniquement le district où se trouve **Zuyel**. Nommez le fichier de manière appropriée.  
Utilisez l’outil ![](/fig/qgis_identify_features.png) `Identify Features` pour identifier le district, puis sélectionnez-le dans la table attributaire.

7. Supprimez toutes les couches initiales, puis ouvrez la table attributaire de vos nouvelles couches pour vérifier qu’elles contiennent chacune une seule entité.

8. Enregistrez votre projet.

### Résultat <a id="result"></a>

:::{figure} /fig/en_result_geodata_processing_exercise.png
---
width: 80%
name: en_result_geodata_processing_exercise
---
Voici un exemple du résultat attendu.
:::