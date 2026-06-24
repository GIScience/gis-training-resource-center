````markdown
::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice : exporter des données OpenStreetMap <a id="exercise-openstreetmap-data-export"></a>

:::{card}
__Objectif de l’exercice :__
^^^

Cet exercice vise à montrer deux façons d’intégrer des données OpenStreetMap (OSM) sous forme de fichiers vectoriels dans QGIS. Nous passerons en revue le flux de travail avec Geofabrik, le HOT (Humanitarian OpenStreetMap Team) Export Tool et l’extension QGIS QuickOSM.

:::

::::{grid} 2
:::{grid-item-card}
__Type d’exercice de formation :__
^^^

- Cet exercice peut être utilisé aussi bien en formation en ligne qu’en présentiel.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour__
^^^ 

- Fondamentaux QGIS
- Rechercher et télécharger des jeux de données pertinents et les préparer pour une analyse ultérieure

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice__
^^^

- L’exercice prend environ 2 heures, selon le nombre de participant·e·s et leur familiarité avec les outils informatiques.

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
- Consultez [Comment animer des formations ?](/content/fr/Trainers_corner/fr_how_to_training.md) pour quelques conseils généraux sur la conduite de formations.

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

Puisque cet exercice porte sur la recherche de données, il n’y a pas de données à télécharger directement.
À la place, téléchargez la __structure de dossiers standard__ [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_3/Module_2_Exercise_3_Data_sources.zip) et ajoutez-y vos données au fur et à mesure de leur téléchargement.

:::

## Tâches <a id="tasks"></a>

OpenStreetMap (OSM) est un projet collaboratif et open source qui produit des cartes libres et modifiables du monde, construites par une communauté mondiale de contributeur·rice·s. Il existe plusieurs façons de télécharger ou d’exporter des données depuis OpenStreetMap (OSM), chacune avec ses propres avantages. Dans cet exercice, nous allons passer en revue quelques-unes de ces méthodes et discuter de leurs avantages respectifs.

<!-- FIXME: This task needs more information. what is the user trying to achieve 
   and why?
   
   ADD: Maybe a discussion step for each extraction method? in which scenarios would you choose which extraction method? -->

### Tâche 1 : Geofabrik <a id="task-1-geofabrik"></a>

Le site Geofabrik propose des téléchargements de données OSM par région.

1. Rendez-vous sur __https://download.geofabrik.de/__ et accédez au jeu de données de Maurice en cliquant sur `Africa` → ` Mauritius`
2. Dans __Commonly Used Formats__, sélectionnez l’option `mauritius-latest-free.shp.zip`
   et téléchargez le fichier. Enregistrez-le à un endroit de votre ordinateur où vous pourrez le retrouver facilement, puis décompressez-le.
3. Examinez le contenu du dossier. Il contient de nombreux shapefiles,
   chacun correspondant à un type de données OSM. La liste complète des couches et de leur contenu est disponible [ici](https://download.geofabrik.de/osm-data-in-gis-formats-free.pdf).

4. Ouvrez un nouveau projet QGIS et enregistrez-le dans le dossier `/Project` de votre dossier d’exercice.
5. Chargez le fichier `gis_osm_places_a_free_1.shp`. Cette couche polygonale
   contient les limites de différents objets. Prenez le temps d’explorer
   les données à l’aide de la table attributaire.
6. (Optionnel) Vous pouvez sélectionner toutes les entités de la couche pour lesquelles
   “fclass” = “island” et les exporter dans une nouvelle couche. Cela vous permettra de
   commencer à créer une carte des îles Maurice.
7. Chargez le fichier `gis_osm_buildings_a_free_1.shp`. Cette couche polygonale
   contient tous les bâtiments de l’île Maurice cartographiés dans OSM. Prenez le temps
   d’explorer cette couche.
8. Ajoutez un fond de carte satellite à l’aide de l’[extension QuickMapServices](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_basemaps_wiki.html#basemaps-from-quickmapservices-plugin)
   afin de vérifier s’il existe des bâtiments non cartographiés.
8. Chargez le fichier `gis_osm_landuse_a_free_1.shp`. Examinez ce
    jeu de données et utilisez la fonction de classification pour obtenir une meilleure vue d’ensemble.
    * Faites un clic droit sur la couche `gis_osm_landuse_a_free_1` dans le `Panneau des couches`
      → `Propriétés`. Une nouvelle fenêtre s’ouvre avec une section d’onglets verticale sur
      la gauche. Accédez à l’onglet `Symbologie`.
    * En haut de la fenêtre, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Catégorisé`.
      Dans `Valeur`, sélectionnez “fclass” (abréviation de _featureclass_).
    * Plus bas dans la fenêtre, cliquez sur `Classer`. Vous verrez apparaître toutes les
      valeurs uniques de la colonne “fclass”. Vous pouvez ajuster les
      couleurs en double-cliquant sur une ligne dans la zone centrale. Une fois terminé,
      cliquez sur `Appliquer` puis sur `OK` pour fermer la fenêtre de symbologie.

Comme vous pouvez le constater, Geofabrik est très utile si vous souhaitez obtenir des jeux de données OSM complets pour des pays entiers ou de grandes régions.

| Advantages                                                                  | Disadvantages                                                                                   |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| + Accès rapide à des jeux de données OSM complets                           | - Peu adapté si l’on recherche uniquement des objets précis ou des zones plus petites qu’un pays |
| + Exports OSM très à jour                                                   | - Taille de fichier importante                                                                  |
| + Documentation claire des objets OSM contenus dans chaque shapefile        | - Disponible uniquement au format shapefile                                                     |


### Tâche 2 : HOT Export Tool <a id="task-2-hot-export-tool"></a>

Le [HOT Export Tool](https://export.hotosm.org/v3/)
est un outil d’accès aux données OSM proposé par le Humanitarian OpenStreetMap Team (HOT).
HOT met à disposition un outil accessible depuis un navigateur permettant de télécharger des données OSM avec de bonnes possibilités pour préciser
la zone, la période, le type d’objet et le format des données.

1. Rendez-vous sur le HOT Export Tool. Pour utiliser l’outil, vous devez disposer d’un compte OSM. Si vous
   n’en avez pas, vous devez en créer un. Cliquez sur `Log in`. Dans la nouvelle fenêtre,
   choisissez l’option permettant de créer un nouveau compte.
2. Si vous avez déjà un compte OSM, vous pouvez vous connecter directement au HOT Export Tool en
   cliquant sur `Log in`.
3. Dans cet exemple, nous voulons télécharger tous les objets liés aux services bancaires et financiers présents dans OSM
   pour l’île Maurice.
    1. Sélection de la zone ou du lieu : zoomez sur l’île Maurice sur la carte ou utilisez la barre de recherche.
       Pour délimiter l’île principale, trois options existent. Vous pouvez dessiner un rectangle,
       dessiner un polygone ou téléverser un fichier GeoJSON contenant vos limites. Dans ce cas,
       utilisez l’une des deux premières options pour délimiter l’île Maurice.
    2. Nom et description : donnez à votre export le nom “Mauritius financial
       institutions” et ajoutez une courte description de l’export.
    3. Onglet Format : le HOT Export Tool propose de nombreux formats d’export.
       Sélectionnez GeoPackage (`.gpkg`) et laissez les autres
       options décochées.
    4. Onglet Data : la façon la plus simple de choisir les données à télécharger est d’utiliser l’arborescence des tags.
       Puisque nous voulons télécharger des institutions financières, trouvez la catégorie “Financial”
       et sélectionnez toutes les options (ATM, Bank, Bureau de Change).
    5. Onglet Summary : cliquez sur `Create Export`. Vous serez redirigé·e vers une page
       d’attente pendant que l’export est généré. Une fois le traitement terminé,
       la page affichera un lien de téléchargement pour votre fichier.

```{figure} /fig/en_Hot_Export.png
---
width: 800px
align: center
name: Hot Export tool download of Mauritius financial institutions
---
Téléchargement des institutions financières de l’île Maurice avec le HOT Export Tool. Capture d’écran adaptée du [HOT Export Tool](https://export.hotosm.org/v3/exports/new/describe)
````

4. Chargez le nouveau fichier dans QGIS.
5. Réorganisez les couches sur la carte de façon à pouvoir voir la nouvelle couche.
6. (Optionnel) Utilisez la fonction de classification pour obtenir une meilleure vue d’ensemble :

   * Faites un clic droit sur la couche `Mauritius_finical_institution` dans le `Panneau des couches`
     → `Propriétés`. Une nouvelle fenêtre s’ouvre avec une section d’onglets verticale sur
     la gauche. Accédez à l’onglet `Symbologie`.
   * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Catégorisé`.
     Dans `Valeur`, sélectionnez "amenity".
   * Plus bas dans la fenêtre, cliquez sur `Classer`. Vous devriez maintenant voir toutes les valeurs uniques
     ou attributs de la colonne “fclass” sélectionnée. Vous pouvez ajuster les
     couleurs en double-cliquant sur une ligne dans la zone centrale. Une fois terminé,
     cliquez sur `Appliquer` puis `OK` pour fermer la fenêtre de symbologie.

     <!-- SUGGESTION: I don't think the symbology instructions need to be repeated 
        if they are already provided above -->

Comme vous pouvez le constater, le HOT Export Tool offre un bon compromis entre flexibilité et accès rapide aux données OSM. Toutefois, plusieurs étapes sont nécessaires avant que les données soient utilisables dans QGIS.

<!-- note: is it quick or are there lots of steps? doesn't make sense if
   both are true! -->

| Advantages                                | Disadvantages                               |
| ----------------------------------------- | ------------------------------------------- |
| + Bonnes options de sélection des données | - De nombreuses étapes sont nécessaires     |
| + Nombreux formats de données disponibles | - Options de sélection des données limitées |
| + Facile à utiliser                       |                                             |
| + Requête facilement réutilisable         |                                             |

### Tâche 3 : QuickOSM <a id="task-3-quickosm"></a>

L’extension QuickOSM vous permet de charger directement des données OSM dans QGIS.
Toutefois, par rapport aux deux options précédentes, cette extension nécessite la compréhension la plus approfondie du modèle de données OSM.
Pour adapter votre requête en fonction de la clé et de la valeur exactes dont vous avez besoin, deux ressources sont particulièrement utiles :

1. [OSM Wiki](https://wiki.openstreetmap.org/wiki/Main_Page), et en particulier l’article
   [Map features](https://wiki.openstreetmap.org/wiki/Map_features).
2. [Taginfo](https://taginfo.openstreetmap.org/)

Prenez le temps de consulter les deux.

<!-- NOTE: this feels like info that is best dealt with outside of an exercise -->

1. Installez l’extension QuickOSM en cliquant sur l’onglet `Plugin`, → `Manage and Install Plugins…` → `All` → recherchez "QuickOSM" → `Install Plugin`.

2. Nous voulons maintenant trouver toutes les structures de santé sur l’île Maurice.

   1. Positionnez l’île Maurice de manière à ce qu’elle soit entièrement visible
      dans votre zone de carte.
   2. Ouvrez l’extension QuickOSM en cliquant sur le menu `Vector` → `QuickOSM` →
      `QuickOSM`.
   3. Cliquez sur `Quick query`.
   4. Dans le tableau, ajoutez "amenity" comme clé et "hospital" comme valeur. Cette
      requête retournera les données des hôpitaux.
   5. Cliquez sur l’icône plus verte pour ajouter une ligne supplémentaire au tableau. Dans cette
      nouvelle ligne, choisissez “OR” dans le petit menu déroulant situé à gauche.
   6. Ajoutez "healthcare" comme nouvelle clé avec "hospital" comme valeur.
   7. Sous le tableau, réglez le petit menu déroulant sur “Canvas Extent”
   8. Cliquez sur `Run query`.

   ```{figure} /fig/en_quick_OSM_hospital_key.png
   ---
   width: 800px
   align: center
   name: QuickOSM hospital query
   ---
   Requête QuickOSM pour les hôpitaux
   ```

3. Examinez les nouvelles couches dans le panneau des couches. Ouvrez la table attributaire de la
   couche de points. Regardez les colonnes “healthcare” et “amenity”. Quelles données seraient
   absentes si vous n’aviez utilisé qu’une seule des deux clés ?

4. Faites la même requête pour La Réunion, située au sud-ouest de Maurice.
   Déplacez l’île au centre de votre zone de carte puis cliquez sur `Run query`. La
   table attributaire de cette nouvelle couche de points est-elle différente ?

5. Et si nous voulons uniquement les hôpitaux disposant d’un service d’urgence ? Dans ce cas, nous
   devons construire une requête en combinant les opérateurs "OR" et "AND".
   Regardez l’image ci-dessous.

   ```{figure} /fig/en_quick_OSM_hospital_emgerency_key.png
   ---
   width: 800px
   align: center
   name: QuickOSM hospital with emergency  query
   ---
   Requête QuickOSM pour les hôpitaux disposant d’un service d’urgence
   ```

<!-- SUGGESTION: This exercise is already long - suggest leaving out the hotels query 
6.	Now try to create a query that shows all accommodations like hotels on 
   the island. To do that, use this [wiki page](https://wiki.openstreetmap.org/wiki/DE:Key:tourism). 
   The solution can be found in the dropdown menu below.


::::{dropdown}  Solution accommodation query

```{figure} /fig/en_quick_OSM_accomedation_key.png
---
width: 800px
align: center
name: QuickOSM accommodation query
---
QuickOSM accommodation query
```
::::
-->

| Advantages                                               | Disadvantages                                         |
|----------------------------------------------------------|-------------------------------------------------------|
| + Requête paramétrable pour des données très spécifiques | - Nécessite une connaissance du modèle de données OSM |
| + Les données se chargent directement dans QGIS          | - Les requêtes peuvent rapidement devenir complexes   |
| + Requête facilement réutilisable                        |                                                       |

