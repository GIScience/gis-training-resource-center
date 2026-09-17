::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Exercice 2 (Classification des géodonnées) : Carte de l’insécurité alimentaire en Sierra Leone <a id="exercise-2-geodata-classification-map-of-food-insecurity-in-sierra-leone"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

:::{card}
__Objectif de l’exercice :__
^^^

Cet exercice vise à créer une carte d’ensemble de la répartition de l’insécurité alimentaire en Sierra Leone au niveau du district. Pour ce faire, nous visualiserons à la fois la répartition de l’insécurité alimentaire et des éléments d’infrastructure clés tels que les hôpitaux, les aéroports et les routes. 

:::

::::{grid} 2
:::{grid-item-card}
__Type d’exercice :__
^^^

- Cet exercice peut être utilisé dans des formations en ligne et en présentiel. 
- Il peut être réalisé comme exercice guidé ou individuellement en auto-apprentissage.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour__ 
^^^

- Les bases de QGIS
- Les compétences testées dans cet exercice sont nécessaires pour tous les utilisateurs SIG.
- La classification des données géographiques

:::
::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé nécessaire pour l’exercice :__
^^^

- L’exercice prend environ 1 heure à réaliser, en fonction du nombre de participants et de formateurs. 

:::

:::{grid-item-card}
__Articles Wiki pertinents__:
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Types de géodonnées](/content/fr/Wiki/fr_qgis_geodata_types_wiki.md)
* [Importation de géodonnées dans QGIS](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md)
* [Concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)
* [Table attributaire](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)
* [Fonction de table - Ajouter un champ](/content/fr/Wiki/fr_qgis_table_functions_wiki.md)
* [Classification des géodonnées - Catégorisée](/content/fr/Wiki/fr_qgis_categorized_wiki.md)
* [Classification des géodonnées - Graduée](/content/fr/Wiki/fr_qgis_graduated_wiki.md)
* [Numérisation - Données ponctuelles](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#add-geometries-to-a-layer)

:::

::::

## Instructions pour les formateurs <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Coin des formateurs__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. un tableau Miro) où les participants peuvent ajouter leurs observations et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment organiser des formations ?](/content/fr/Trainers_corner/fr_how_to_training.md) pour quelques conseils généraux sur la conduite des formations.

### Conduire la formation <a id="conduct-the-training"></a>

__Introduction :__

- Présentez l’idée et l’objectif de l’exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a décompressé le dossier avant de commencer les tâches.

__Suivi guidé :__

- Montrez et expliquez chaque étape vous-même au moins deux fois et suffisamment lentement pour que tout le monde puisse voir ce que vous faites, et suivre dans son propre projet QGIS. 
- Assurez-vous que tout le monde suit et effectue les étapes lui-même en demandant régulièrement si quelqu’un a besoin d’aide ou si tout le monde suit toujours.  
- Soyez ouvert et patient face à chaque question ou problème qui pourrait survenir. Vos participants font essentiellement du multitâche en prêtant attention à vos instructions et en s’orientant dans leur propre projet QGIS.

__Conclusion :__

- Laissez du temps à la fin de l’exercice pour traiter tout problème ou toute question concernant les tâches.
- Laissez du temps pour des questions ouvertes. 

:::


### Données disponibles <a id="available-data"></a>

Téléchargez tous les jeux de données __[ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_2/Module_3_Exercise_2_Sierra_Leone_Food_Insecurity.zip)__ et enregistrez le dossier sur votre ordinateur. Décompressez le fichier .zip. Le dossier décompressé est structuré selon la structure de dossiers recommandée pour les projets QGIS. Sous "data > input", vous trouverez les fichiers suivants :

- `Sierra_leone_foodinsecurity_2015.shp` (Polygon) Shapefile
- `Sierra_leone_borders.gpkg` (MultiLineString) GeoPackage
    - Sierra_Leone_national_borders (Lines)
    - Sierra_Leone_provinces (Lines)
- `Sierra_leone_roads.gpd` (Lines) GeoPackage
- `Sierra_leone_healthsites.gpkg` (Points) Geopackage
- `sl_airports.gpkg` (Points) GeoPackage

### Tâches <a id="tasks"></a>

Notre objectif est de produire un aperçu de la situation de l’insécurité alimentaire en Sierra Leone en 2015 avec l’affichage des principaux éléments d’infrastructure. Pour y parvenir, nous visualiserons les classifications de l’insécurité alimentaire totale ainsi que les aéroports, les hôpitaux et les routes principales sur une carte.

1. Ouvrez QGIS et créez un [nouveau projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`.

2. Une fois le projet créé, enregistrez le projet dans le dossier “project” de “Ex_Sierra_Leone_foodinsecurity”. Pour cela, cliquez sur `Project` → `Save as` et naviguez jusqu’au dossier. Nommez le projet “Sierra_Leone_foodinsecurity”.

3. Importez les GeoPackages `Sierra_leone_borders.gpkg`, `Sierra_leone_airports`, `Sierra_leone_healthsites` et `Sierra_leone_roads.gpkg` ainsi que le shapefile `Sierra_leone_foodinsecurity_2015.shp` dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-raster-data-via-drag-and-drop)). 
Ou en cliquant sur `Layer` → `Add Layer` → `Add Vector Layer` : cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à "Sierra_leone_borders.gpkg" dans votre navigateur de fichiers. Sélectionnez le fichier et cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-raster-data-via-layer-tab)).

:::{Attention}
Les GeoPackages peuvent contenir plusieurs fichiers et même des projets QGIS entiers. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers que vous souhaitez charger dans votre projet QGIS.
:::

4. Tout d’abord, ajoutons un fond de carte à votre canevas cartographique en utilisant le plugin `QuickMapServices` en cliquant sur le symbole ![](/fig/QMS_search_icon.png) dans la barre d’outils de votre projet. Recherchez "Bing Maps Satellite Imagery" dans le panneau QMS et ajoutez la couche de fond de carte par double-clic. Pour une vue optimisée, [ajustez l’opacité](https://www.youtube.com/watch?v=WguUkN1YRzY&ab_channel=GISBigfootAnswers) de vos couches afin d’optimiser l’utilisation du fond de carte. 

5. En utilisant la table attributaire de la couche des aéroports, zoomez sur l’aéroport de Tongo en faisant un clic droit sur la ligne dans la table attributaire puis en sélectionnant `Zoom to Feature`([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)). Vérifiez le fond de carte. Pensez-vous que la piste d’atterrissage soit encore opérationnelle ? La réponse est non, selon Wikipédia. Supprimez Tongo Airport dans la [table attributaire](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md). Supprimez aussi l’aéroport de Kabala, puisqu’il n’est lui non plus plus opérationnel.

6. Nous voulons maintenant examiner les aéroports des villes de Bo et Kenema. Ces pistes d’atterrissage sont-elles en meilleur état ? Si oui, ajoutez-les à la couche des aéroports. Pour trouver ces villes sur votre interface cartographique, utilisez le plugin QGIS `OSM Place Search`. 
Pour ajouter le plugin `OSM Place Search`, cliquez sur `Plugins` → `Manage and Install Plugins…` → `All` puis recherchez "OSM Place Search". Une fois que vous l’avez trouvé, cliquez dessus puis sélectionnez `Install Plugin`. Vous pouvez ouvrir le `OSM Place Search Panel` comme n’importe quel autre panneau en cliquant sur `View` → `Panels` puis en cochant `OSM Place Search Panel`([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_plugins_wiki.html)).
    * Dans le panneau, vous pouvez rechercher des lieux dans OpenStreetMap en saisissant le nom dans la barre de recherche. Il est souvent utile d’ajouter des informations supplémentaires comme le nom du pays. Essayez par exemple “Bo, Sierra Leone”.

:::{figure} /fig/mod3_classification_ex_OSMsearch.png
---
width: 400px
align: center
---
Recherche de lieux OSM.
:::

Ajoutez les aéroports de Bo et Kenema sous forme de points à la couche `Sierra_Leone_airports`. Vous trouverez de l’aide sur l’ajout d’entités à une couche de points [ici](/content/fr/Wiki/fr_qgis_digitisation_wiki.md). 
 

8. *Optionnel :* Dans la table attributaire, créez une nouvelle colonne `Runway_length` et ajoutez la longueur des pistes de Bo et Kenema en les mesurant approximativement avec l’outil de mesure ![](/fig/measuring_tool_icon.png).

9. Nous voulons maintenant créer une visualisation intuitive des différences d’insécurité alimentaire. Pour y parvenir, nous utilisons l’option de visualisation "[Classification graduée](/content/fr/Wiki/fr_qgis_graduated_wiki.md)" pour la couche `Sierra_leone_foodinsecurity_2015` en affichant les polygones selon des classes créées sur la base de la colonne "Total_FI" dans la table attributaire.
    * Faites un clic droit sur la couche `Sierra_leone_foodinsecurity_2015.shp` dans le `Layer Panel` → `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Accédez à l’onglet `Symbology`.
    * Dans le menu déroulant tout en haut, choisissez `Graduated`. Sous `Value`, sélectionnez “Total_FI”.
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir plusieurs classes basées sur la plage de valeurs de la colonne "TotalFI", représentées avec différentes couleurs. Vous pouvez ajuster les couleurs en choisissant différentes palettes de couleurs dans le menu déroulant `Color ramp`. Vous pouvez également modifier la distribution des valeurs des classes en sélectionnant différents modes de classification ([Wiki](/content/fr/Wiki/fr_qgis_graduated_wiki.md)) dans le menu déroulant `Mode`. 
    * Testez ces options afin d’obtenir un schéma de couleurs adapté aux données. Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.

:::{figure} /fig/mod3_classification_ex_Graduatedclassification.png
---
width: 900px
name: basic classification
align: center
---
Classification de l’insécurité alimentaire en Sierra Leone.
:::

1.  Pour donner aux hôpitaux et aux aéroports une visualisation plus distinctive, ouvrez de nouveau l’onglet `Symbology` pour les couches respectives et choisissez "Topology" dans le menu déroulant au-dessus du panneau inférieur supérieur. Recherchez le symbole d’aéroport / hôpital et sélectionnez-le en cliquant dessus. Appliquez à nouveau vos modifications en cliquant sur `Apply` puis sur `OK`.

:::{figure} /fig/mod3_classification_ex_Topology.png
---
width: 900px
name: basic classification
align: center
---
Symbole pour hôpital.
:::

11. Comme dernière étape de visualisation, ouvrez l’onglet `Symbology` de `Sierra_Leone_roads (Lines)` et, comme à l’étape 9, ouvrez le menu déroulant supérieur. Maintenant, au lieu de `Graduated`, choisissez [Classification catégorisée](/content/fr/Wiki/fr_qgis_categorized_wiki.md) puis sélectionnez "highway" dans le menu `Value`. Cliquez sur `Classify` pour obtenir une classification avec des couleurs individuelles pour toutes les valeurs uniques de la colonne "highway". Dans les carrés à côté des classes, désélectionnez toutes les classes sauf "primary". Vous pouvez changer la couleur des classes en cliquant manuellement dessus puis en ajustant la couleur dans le menu déroulant `Symbol` près du haut de la fenêtre.

:::{figure} /fig/mod3_classification_ex_Categorizedclassification.png
---
width: 900px
name: basic classification
align: center
---
Routes catégorisées en Sierra Leone.
:::

12. Rendez visibles toutes les couches que vous avez chargées dans votre projet et organisez-les dans un ordre adapté à une bonne visualisation de l’insécurité alimentaire ainsi que des éléments d’infrastructure. Choisissez un fond de carte que vous jugez approprié. Votre résultat final pourrait ressembler à ceci :

:::{figure} /fig/mod3_classification_ex_Result.png
---
width: 900px
name: basic classification
align: center
---
Exemple du résultat de cet exercice.
:::

L’ordre des couches ici de haut en bas est :
- `Sierra_Leone_health` 
- `Sierra_Leone_airports`
- `Sierra_Leone_roads` 
- `Sierra_Leone_national_borders` 
- `Sierra_leone_foodinsecurity_2015`
- Fond de carte : `OpenStreetMap`

:::{figure} /fig/mod3_classification_ex_LayerOrder.png
---
width: 600px
name: basic classification
align: center
---
Ordre des couches.
:::
