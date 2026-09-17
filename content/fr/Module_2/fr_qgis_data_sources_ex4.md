::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice : export de données OpenStreetMap <a id="exercise-openstreetmap-data-export"></a>

:::{card}
__Objectif de l’exercice :__
^^^

Cet exercice vise à montrer deux façons d’intégrer [OpenStreetMap (OSM)](https://www.openstreetmap.org) sous forme de données vectorielles dans QGIS. Nous utiliserons le [HOT Export Tool](https://export.hotosm.org/v3/) pour télécharger des données spécifiques depuis OpenStreetMap.

:::

::::{grid} 2
:::{grid-item-card}
__Parcours d’exercices sur la réponse aux inondations à Larkana__

Cet exercice fait partie du [parcours d’exercices sur la réponse aux inondations à Larkana](https://giscience.github.io/gis-training-resource-center/content/fr/Exercise_tracks/fr_larkana_flood_response.html)

:::

:::{grid-item-card}
__Compétences couvertes par cet exercice__
^^^ 
- Exporter des données OSM à l’aide du HOT Export Tool.
- Importer des fichiers dans un projet QGIS.
- Ajuster la symbologie d’une couche.

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice__
^^^

- L’exercice prend environ 45 minutes, y compris la discussion, selon le nombre de participant·e·s et leur familiarité avec les outils informatiques.

:::

:::{grid-item-card}
__Articles wiki pertinents__
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Types de données géographiques](/content/fr/Wiki/fr_qgis_geodata_types_wiki.md)
* [Import de données géographiques dans QGIS](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md)
* [Concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)
* [Classification des données géographiques - Graduée](/content/fr/Wiki/fr_qgis_graduated_wiki.md)

:::

::::

## Instructions pour les formateur·rice·s <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Espace formateur·rice__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. un tableau Miro) sur lequel les participant·e·s peuvent ajouter leurs remarques et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment animer des formations ?](/content/fr/Trainers_corner/fr_how_to_training.md) pour quelques conseils généraux sur la conduite d’une formation.

### Animer la formation <a id="conduct-the-training"></a>

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


## Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip

Comme cet exercice porte sur la recherche de données, il n’y a pas de jeu de données à télécharger directement.  
Téléchargez plutôt la __structure de dossiers standard__ [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) et enregistrez vos données dans le dossier `data/input` au fur et à mesure de leur téléchargement.

:::

## Tâches <a id="tasks"></a>

OpenStreetMap (OSM) est un projet collaboratif et open source qui produit des cartes libres et modifiables du monde, construites par une communauté mondiale de contributeur·rice·s. Il existe plusieurs façons de télécharger ou d’exporter des données depuis OpenStreetMap (OSM), chacune ayant ses propres avantages. Dans cet exercice, nous allons nous concentrer sur le [HOT Export Tool](https://export.hotosm.org/v3/). [En bas de cet exercice](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_qgis_data_sources_ex4.html#alternative-tools), vous trouverez une liste d’outils alternatifs.

### Utiliser le HOT Export Tool <a id="using-the-hot-export-tool"></a>

Le [HOT Export Tool](https://export.hotosm.org/v3/) 
est un outil d’accès aux données OSM proposé par le Humanitarian OpenStreetMap Team (HOT).
HOT met à disposition un outil accessible depuis un navigateur permettant de télécharger des données OSM avec de bonnes possibilités pour préciser 
la zone, la période, le type d’objet et le format des données. 
Pour l’analyse suivante, nous voulons exporter le réseau routier du district de Larkana au Pakistan. 


1. Rendez-vous sur le HOT Export Tool. Pour utiliser l’outil, vous devez disposer d’un compte OSM. Si vous
   n’avez pas encore de compte, vous devrez en créer un. Cliquez sur `Log in`. Dans la nouvelle fenêtre,
   choisissez l’option permettant de créer un nouveau compte. 
2. Si vous avez déjà un compte OSM, vous pouvez vous connecter directement au HOT Export Tool en
   cliquant sur `Log in`.
3. Nous pouvons maintenant commencer à créer un export OSM. Pour cela, cliquez sur `Start Exporting`. Vous serez redirigé·e vers l’outil d’export.

:::{figure} /fig/en_m2_ex4_HOT_Export_Tool1.png
---
name: HOT_Export_Tool_1
width: 750 pc
---

:::

Dans l’outil d’export, vous disposez d’un canevas cartographique à droite et d’une zone de saisie à gauche. Sur le canevas cartographique, vous définissez la localisation géographique des données à exporter. À gauche, vous définissez les métadonnées de l’export, le format du fichier et les données à télécharger (par ex. bâtiments, routes, hôpitaux, établissements humains, etc.).

4. À gauche, donnez un nom à votre export, par exemple `Larkana Roads export 20250314`, et ajoutez une courte description de ce que vous souhaitez télécharger. Dans notre cas, nous voulons télécharger le réseau routier de Larkana au Pakistan. Vous pouvez également renseigner un projet si vous le souhaitez (par ex. GIS Training). 

::::{margin}
:::{tip}
Il existe deux entrées pour Larkana dans OpenStreetMap. L’une correspond à la ville et l’autre au district. Notre zone d’intérêt est le __district__. Nous pouvons choisir l’entrée qui possède la boîte la plus grande.  
Sinon, une fois la zone affichée, vous pouvez dessiner un rectangle ou un polygone pour sélectionner la zone. 
:::
::::

5. Sur le canevas cartographique, recherchez Larkana dans la barre de recherche et sélectionnez le district. La carte zoomera sur le district. Cela sélectionnera également le district comme zone d’intérêt. Vous pouvez le voir grâce au polygone bleu. Notre export ne téléchargera que les données situées à l’intérieur de cette zone.

:::{figure} /fig/Module_2/en_m2_ex_4_HOT_Export_Tool3.png
---
name: HOT_Export_3
width: 500 px
---


6. Cliquez sur `Next`.

7. Sélectionnez le format que vous souhaitez télécharger. Nous recommandons d’utiliser GeoPackage `.gpkg`, mais GeoJSON et Shapefile conviennent également. Cliquez sur `Next`.

8. Dans l’onglet des données, nous pouvons sélectionner les couples clé-valeur qui nous intéressent. Nous voulons télécharger le réseau routier ; il faut donc ouvrir le menu déroulant sous `Transportation` et cocher la case `Roads`.

:::{figure} /fig/Module_2/en_m2_ex4_HOT_export_tool4.png
---
name: Hot Export Tool 5
width: 500 px
---
:::

9. Nous avons terminé la configuration de l’export. Cliquez sur `Next`. Une page récapitulative s’ouvrira. Cliquez sur `Create Export`. Votre nouvel export commencera.

:::{figure} /fig/en_Hot_Export.png
---
width: 800px
align: center
name: Hot Export tool download
---
:::

::::{dropdown} Exercice bonus !

Dans l’exercice suivant du parcours de réponse aux inondations à Larkana, nous souhaitons identifier les structures de santé situées à Larkana. Pouvez-vous imaginer une façon d’exporter ces structures de santé à l’aide du HOT Export Tool ?

::::

4. [Importez le nouveau fichier dans votre projet QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#vector-data-import).
5. Organisez les couches sur la carte de manière à pouvoir voir la nouvelle couche.
6. (Optionnel) Utilisez la fonction de classification pour obtenir une meilleure vue d’ensemble :
    * Faites un clic droit sur la couche `Larkana_Roads` dans le `Panneau des couches` → `Propriétés`. Une nouvelle fenêtre s’ouvre avec une section d’onglets verticale sur la gauche. Accédez à l’onglet `Symbologie`.
    * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Catégorisé`. Dans `Valeur`, sélectionnez "highway".
    * Plus bas dans la fenêtre, cliquez sur `Classer`. Vous devriez maintenant voir toutes les valeurs uniques
      ou attributs de la colonne sélectionnée. Vous pouvez ajuster les
      couleurs en double-cliquant sur une ligne dans la zone centrale. Une fois terminé,
      cliquez sur `Appliquer` puis `OK` pour fermer la fenêtre de symbologie.

Comme vous pouvez le constater, le HOT Export Tool offre un bon compromis entre flexibilité et accès rapide aux données OSM.

| Advantages                              | Disadvantages                          |
|-----------------------------------------|----------------------------------------|
| + Bonnes options de sélection des données | - De nombreuses étapes sont nécessaires |
| + Nombreux formats de données disponibles | - Options de sélection des données limitées |
| + Facile à utiliser                      |                                        |
| + Requête facilement réutilisable        |                                        |


## Outils alternatifs <a id="alternative-tools"></a>

:::::{tip}

Le HOT Export Tool constitue une bonne solution pour exporter des données OSM ciblées pour votre usage personnel. Toutefois, dans certains cas, vous préférerez peut-être utiliser un autre outil, comme Geofabrik, QuickOSM ou simplement le site du Humanitarian Data Exchange. Vous trouverez ci-dessous une brève présentation de ces outils et de leurs avantages. Vous pouvez découvrir comment utiliser ces différents outils pas à pas sur [cette page wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_OpenStreetMap_wiki.html).

::::{dropdown} Geofabrik, QuickOSM, HDX

:::{card}
__Geofabrik__
^^^
Le [site Geofabrik](https://download.geofabrik.de/) permet de télécharger des données OSM par région. Vous pouvez sélectionner une zone d’intérêt et télécharger l’ensemble des données OSM contenues dans cette zone. Il s’agit de la méthode la plus complète. Nous la recommandons si vous souhaitez explorer les données OSM ou si vous avez besoin d’un grand volume de données OSM. En revanche, si vous ne recherchez que des données spécifiques, comme les routes, les points d’établissement humain ou les bâtiments, il peut être préférable d’utiliser le HOT Export Tool ou QuickOSM.

| Advantages                                                                  | Disadvantages                                                                                   |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| + Accès rapide à des jeux de données OSM complets                           | - Peu adapté si l’on recherche uniquement des objets précis ou des zones plus petites qu’un pays |
| + Exports OSM très à jour                                                   | - Taille de fichier importante                                                                  |
| + Documentation claire des objets OSM contenus dans chaque shapefile        | - Disponible uniquement au format shapefile                                                     |

:::


:::{card}
__QuickOSM__
^^^
L’extension QuickOSM permet de charger des données OSM directement depuis QGIS. C’est une méthode rapide et pratique, mais elle nécessite la compréhension la plus poussée du modèle de données OSM par rapport aux autres options.  
Vous devrez formuler une requête pour trouver les données recherchées. Pour adapter votre requête à la clé et à la valeur exactes dont vous avez besoin, deux ressources sont particulièrement utiles : 

1. [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page), et en particulier l’article
   [Map features](https://wiki.openstreetmap.org/wiki/Map_features). 
2. [Taginfo](https://taginfo.openstreetmap.org/)

Cette méthode présente l’avantage de permettre le téléchargement très ciblé des données dont vous avez besoin, mais elle suppose de savoir formuler des requêtes. Pour utiliser QuickOSM, vous devez [installer l’extension QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_plugins_wiki.html). 

| Advantages                                     | Disadvantages                                 |
|------------------------------------------------|-----------------------------------------------|
| + Requête paramétrable pour des données très spécifiques | - Nécessite une connaissance du modèle de données OSM |
| + Les données se chargent directement dans QGIS | - Les requêtes peuvent rapidement devenir complexes |
| + Requête facilement réutilisable              |                                               |

:::

:::{card}
__Humanitarian Data Exchange (exports HOT)__
^^^
Une façon rapide et simple d’obtenir des données OSM spécifiques, comme le réseau routier ou la localisation des structures de santé, consiste à rechercher ces données sur le [Humanitarian Data Exchange (HDX)](https://data.humdata.org/).

Le Humanitarian OpenStreetMap Team y publie des exports OSM par pays. L’inconvénient de cette méthode est que, puisque les exports sont fournis à l’échelle nationale, les jeux de données sont généralement assez volumineux et parfois difficiles à manipuler dans QGIS.

:::

::::
:::::