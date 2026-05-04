::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Exercice 4 : Inondations au Nigeria <a id="exercise-4-flooding-in-nigeria"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

::::{grid} 2
:::{grid-item-card}
__Objectif de l’exercice__
^^^

Dans cet exercice, vous apprendrez à numériser la position des établissements en créant de nouveaux jeux de données. De plus, vous apprendrez à enrichir un jeu de géodonnées simple avec des informations supplémentaires.

__Type d’exercice de formation :__

- Cet exercice peut être utilisé dans des formations en ligne et en présentiel. 
- Il peut être réalisé comme exercice guidé ou individuellement en auto-apprentissage.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour__ 
^^^

- Les compétences testées dans cet exercice sont nécessaires pour tous les utilisateurs SIG.

:::
::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé nécessaire pour l’exercice__
^^^

- L’exercice prend environ 1 heure à réaliser, en fonction du nombre de participants et des formateurs. 

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
- Consultez [Comment organiser des formations ?](/content/fr/Trainers_corner/fr_how_to_training.md#how-to-do-trainings) pour quelques conseils généraux sur l’animation des formations.

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
- Laissez du temps pour les questions ouvertes. 

:::

## Sources de données <a id="data-sources"></a>

Téléchargez le dossier de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_1/Module_3_Exercise_1_Flood_Nigeria.zip) et enregistrez-le sur votre PC. Décompressez le fichier .zip.
Le dossier s’appelle “Module_3_Exercise_1_Flood_Nigeria" et contient toute la [structure de dossiers standard](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md#standard-folder-structure) avec toutes les données dans le dossier input et la documentation supplémentaire dans le dossier documentation.

* [Nigeria: Administrative Division with Aggregated Population ("kontur_boundaries_NG_20230628.gpkg")](https://data.humdata.org/dataset/kontur-boundaries-nigeria)-Kontor
* [Nigeria : Données d’inondation (“Nigeria_flood_2022_affacted_population”)](https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas)- UN OCHA. Ce jeu de données a été manipulé à des fins de formation.
* [Étendues d’eau détectées par satellite entre le 1er et le 25 octobre 2022 au Nigeria (VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp)](https://data.humdata.org/dataset/satellite-detected-water-extents-between-1-and-25-october-2022-over-nigeria?force_layout=desktop) UNOSAT


## Tâches <a id="tasks"></a>

Notre objectif est de produire un aperçu de l’impact de l’inondation de 2022 dans l’État de Burco au Nigeria. Pour ce faire, nous visualiserons l’État et les districts affectés, et nous numériserons les communautés qui seraient affectées.

1. Ouvrez QGIS et créez un [nouveau projet](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`.

2. Une fois le projet créé, [enregistrez le projet](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md#save) dans le dossier “project” de l’exercice “Module_3_Exercise_1_Flood_Nigeria”. Pour cela, cliquez sur `Project` → `Save as` et naviguez jusqu’au dossier. Nommez le projet “Nigeria_Borno_flood_2022”.

3. Chargez le GeoPackage "kontur_boundaries_NG_20230628.gpkg" dans votre projet par glisser-déposer ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à "kontur_boundaries_NG_20230628.gpkg". Sélectionnez le fichier et cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md#open-vector-data-via-layer-tab)).
Ce jeu de données contient toutes les zones de division administrative (admin 0 à 5) avec la population correspondante de ces zones. 

:::{Attention}
Les fichiers GeoPackage peuvent contenir plusieurs fichiers et même des projets QGIS entiers. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers que vous souhaitez charger dans votre projet QGIS.
:::

4. Tout d’abord, nous voulons exporter l’État de Borno depuis kontur_boundaries_NG_20230628 afin de l’avoir comme couche vectorielle autonome. Pour ce faire : 
    * Ouvrez la table attributaire de "kontur_boundaries_NG_20230628" en faisant un clic droit sur la couche → `Open Attribute Table` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)).
    * Trouvez la ligne correspondant à l’État de Borno et sélectionnez-la en cliquant sur le numéro tout à fait à gauche de la table attributaire. La ligne apparaîtra en bleu et la zone de l’État de Borno deviendra jaune dans le canevas cartographique. Vous pouvez faire un clic droit sur la ligne puis cliquer sur `Zoom to Feature` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md#zoom-in-on-a-specific-feature)).
    * Faites ensuite un clic droit sur la couche dans le panneau des couches puis cliquez sur `Export` → `Save Selected Features as`. Nous voulons enregistrer Borno comme GeoPackage, donc ajustez le `Format` en conséquence. Cliquez sur les trois points et naviguez jusqu’à votre dossier `temp`. Ici, vous pouvez donner à la couche le nom “AOI_Borno_admin1” puis cliquer sur `Save`. Vous devriez maintenant voir le même nom dans le champ `Layer name`. Cliquez sur `OK` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_non_spatial_queries_wiki.md#save-selected-features-as-a-new-file))

5. Dans les étapes suivantes, nous voulons créer dans notre projet une couche vectorielle avec les zones admin 2, ou au Nigeria appelées Local Government Areas (LGA), avec la population. 
Comme nous voulons uniquement les LGA, nous devons les exporter depuis le jeu de données d’origine. 
    * Ouvrez la table attributaire de la couche "kontur_boundaries_NG_20230628" en faisant un clic droit sur la couche → `Attribute Table` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)). Examinez la table attributaire. Vous voyez deux colonnes de niveaux administratifs, "admin levels" et "[osm_admin_levels](https://wiki.openstreetmap.org/wiki/Key:admin_level)". Les deux ont des valeurs différentes. Dans les [métadonnées](https://data.humdata.org/dataset/kontur-boundaries-nigeria) du jeu de données sur HDX, nous pouvons voir que la colonne "osm_admin_levels" fait référence aux niveaux administratifs utilisés dans OpenStreetMaps (OSM). Il existe une [liste](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#10_admin_level_values_for_specific_countries) indiquant quels niveaux administratifs officiels correspondent à quels niveaux administratifs OSM. Les LGA correspondent au niveau administratif OSM __6__. Cela signifie que nous voulons exporter toutes les entités avec `osm_admin_level` = `6`.
    * Pour exporter exactement ces entités, nous utiliserons l’outil `Extract by attribute`. Ouvrez la `Processing Toolbox` ([voici comment](/content/fr/Wiki/fr_qgis_interface_wiki.md#toolbox-toolbars)) et recherchez l’outil.
    Ouvrez l’outil et choisissez comme `Input Layer` la couche “kontur_boundaries_NG_20230628.gpkg“. Sous `Selection attribute`, choisissez la colonne `osm_admin_level`. L’`Operator` doit être `=` et comme `value`, nous utilisons `6` puisque les LGA ont le niveau `osm_admin_level` 6. 
    * Sous `Extracted (attribute)`, cliquez sur les trois points → `Save to GeoPackage`, naviguez jusqu’à votre dossier `temp` et nommez la nouvelle couche “Nigeria_admin2_pop”. Cliquez sur `Save`. Donnez à la couche le même nom (“Nigeria_admin2_pop”). Cliquez sur `OK` puis cliquez sur `Run`.

6. Maintenant, nous devons extraire toutes les LGA de Borno. Pour cela, nous utiliserons l’outil `Extract by Location` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_non_spatial_queries_wiki.md#select-by-expression)). Recherchez l’outil dans la `Processing Toolbox` et ouvrez-le.
    * Comme `Input Layer`, nous utiliserons “Nigeria_admin2_pop”.
    * Pour `By comparing to the features from`, nous utilisons la couche “AOI_Borno_admin1”.
    * Comme `Geometric predicate`, nous utilisons `are within`. 
    * Pour enregistrer le résultat, cliquez sur les trois points dans `Extract (location)` → `Save to GeoPackage`, puis naviguez jusqu’à votre dossier `temp`. Enregistrez la nouvelle couche sous le nom "Borno_admin2_pop". Donnez à la nouvelle couche le même `Layer name` puis cliquez sur `Run`.
    * Ouvrez la table attributaire de la nouvelle couche. Vous devriez avoir 27 entités.

:::{figure} /fig/en_qgis_extract_by_location_nigeria_flood.png
---
width: 400px
name: m3ex4_extract_by_location
align: center
---
:::

7. Nous avons maintenant nos zones administratives en place et pouvons commencer à enrichir ces couches avec des données supplémentaires concernant l’inondation de 2022.
Ouvrez le fichier Excel ou pdf "Nigeria_flood_2022_affacted_population" et ouvrez l’onglet Borno. Vous y trouverez un tableau avec les LGA et les communautés qui ont été affectées par l’inondation. Nous voulons maintenant ajouter une partie de ces informations à notre couche “Borno_admin2_pop”. Pour cela, il existe deux méthodes. L’une simple, mais plus chronophage, et l’autre plus compliquée, mais beaucoup plus rapide. Nous montrerons la méthode facile, mais dans le menu déroulant ci-dessous, vous pouvez aussi trouver le tutoriel pour la méthode avancée.
    * Ouvrez la table attributaire de “Borno_admin2_pop” et activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md#attribute-table-data-editing)). Vous pouvez maintenant modifier directement les données dans la table.
    * Tout d’abord, nous ajoutons une nouvelle colonne avec le nom “Flood_affacted”. Pour ce faire, cliquez sur ![](/fig/mActionNewAttribute.png). Dans la fenêtre `Add field`, vous devez ajouter le nom et définir le `Type` sur `Text(string)`. Cliquez sur `OK` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md#add-new-column)).
    * À l’étape suivante, vérifiez dans le tableau Excel/PDF quelles LGA ont été affectées et inscrivez “Yes” dans la table attributaire pour ces LGA.
    * Une fois terminé, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications et désactivez le mode édition en cliquant de nouveau sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md#attribute-table-data-editing)).

8. Pour visualiser le jeu de données enrichi, nous utilisons la fonction "Categorized Classification". Cela signifie que nous sélectionnons une colonne de la table attributaire et utilisons son contenu comme catégories pour trier et afficher les données ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_categorized_wiki.md)).
    * Faites un clic droit sur la couche "Borno_admin2_pop" dans le `Layer Panel` → `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Accédez à l’onglet `Symbology`.
    * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Categorized`. Sous `Value`, sélectionnez "Flood_affected".
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir toutes les valeurs ou attributs uniques de la colonne sélectionnée “Flood_affected”. Vous pouvez ajuster les couleurs en double-cliquant sur une ligne dans le champ central. Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.

:::{figure} /fig/en_qgis_categorized_classification_nigeria_flood_exercise.png
---
width: 600px
name: m3ex4_classification
align: center
---
:::

9. Ensuite, nous voulons visualiser les communautés affectées qui sont listées dans le tableau Nigeria_flood_2022_affected_population. Pour trouver ces communautés dans QGIS, nous avons besoin de deux choses. Un fond de carte OpenStreetMap et le plugin `OSM Place Search`. 
    * Pour ajouter OSM comme fond de carte, cliquez sur `Layer` → `Add Layer` → `Add XYZ Layer…`. Choisissez `OpenStreetMap` puis cliquez sur `Add`. 
    Organisez votre couche dans le `Layer Panel` de manière à ce que l’OSM soit en bas ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_basemaps_wiki.md)). 
    :::{Tip}
    Vous ne pouvez pas interagir avec un fond de carte !
    :::
    * Pour ajouter le plugin `OSM Place Search`, cliquez sur `Plugins` → `Manage and Install Plugins…` → `All` puis recherchez `OSM Place Search`. Une fois que vous l’avez trouvé, cliquez dessus puis cliquez sur `Install Plugin`. Vous pouvez ouvrir le `OSM Place Search Panel` comme n’importe quel autre panneau en cliquant sur `View` → `Panels` puis en cochant `OSM Place Search Panel` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_plugins_wiki.md#installation-of-plugins)).
    * Dans le panneau, vous pouvez rechercher des lieux dans OpenStreetMap en saisissant le nom du lieu dans la barre de recherche. Il est souvent utile d’ajouter des informations supplémentaires comme le nom du pays. Par exemple, essayez "Laujeri Bulama, Nigeria".

10. Maintenant, nous avons tous nos outils en place. À l’étape suivante, nous créons une nouvelle couche vectorielle de points à partir de zéro pour numériser l’emplacement des communautés affectées. 
    * Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md#create-a-new-layer)) 
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) et naviguez jusqu’au dossier `temp`. Donnez au nouveau jeu de données le nom "Borno_affected_communities_point". Cliquez sur `Save`.
    * `Geometry type` : sélectionnez `Point`.
    - Sous `Additional dimension`, vous devez toujours vous assurer que `None` est coché. 
    - Sélectionnez le système de coordonnées de référence (CRS) "EPSG:4326-WGS 84". Par défaut, QGIS sélectionne le CRS du projet. 
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne "Name".
        * `Name` = "Name"
        * `Type` : sélectionnez `Text Data`
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Cliquez sur `OK`.
    * Votre nouvelle couche apparaîtra dans le `Layer Panel`.

:::{figure} /fig/en_qgis_create_point_layer_nigeria_flood_exercise.png
---
width: 400px
name: m3ex4_create_point_layer 
align: center
---
:::

11. Actuellement, la nouvelle couche “Borno_affected_communities_point” est vide. Pour ajouter des entités, nous pouvons utiliser la `Digitizing Toolbar`. Si vous ne voyez pas la barre d’outils, utilisez `View` → `Toolbars` et cochez `Digitizing Toolbar` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md#creation-of-point-data)). ![](/fig/Digitizing_Toolbar.png) 
    * Sélectionnez la couche de points “Borno_affected_communities_point” dans le panneau des couches. Allez dans la barre d’outils de numérisation puis cliquez sur ![](/fig/mActionToggleEditing.png). La couche est maintenant en mode édition.
    * Recherchez une communauté affectée à partir du tableau “Nigeria_flood_2022_affacted_population”. Une fois que vous en avez trouvé une, cliquez sur ![](/fig/mActionCapturePoint.png). Faites un clic gauche sur l’entité que vous souhaitez numériser.
    * Une fois que vous avez cliqué, une fenêtre apparaîtra ` Borno_affected_communities_point Feature Attribute`. Ici, vous pouvez ajouter le nom de l’emplacement.
    * Répétez le même processus pour autant de communautés que vous le souhaitez.
    * Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    * Cliquez de nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

12. Dans cette étape, nous voulons ajouter des informations sur la population à la carte. Cela nous aidera à visualiser où le plus grand nombre de personnes sont potentiellement affectées.
Comme la couche "Borno_admin2_pop" contient cette information, nous pouvons dupliquer cette couche. 
    * Pour cela, faites un clic droit sur la couche → `Duplicate Layer`. Le nom de la nouvelle couche sera "Borno_admin2_pop_copy".

13. Comme les nombres absolus de population sont des nombres naturels, nous ne pouvons pas utiliser la classification catégorisée. À la place, nous utilisons l’option `Graduated` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_graduated_wiki.md)).
    * Faites un clic droit sur la couche “Borno_admin2_pop_copy” dans le `Layer Panel` → `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Accédez à l’onglet `Symbology`.
    * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Graduated`.
    * Sous `Value`, sélectionnez "Population".
    * `Color ramp` : sélectionnez une rampe de couleurs allant du blanc au vert. Comme nous voulons visualiser la population, il est important d’utiliser des couleurs neutres. 
    * `Mode` : Equal Count (Quantile)
    * `Classes` : 5
    * Cliquez sur `Classify`.
    * Cliquez sur `Apply`.

:::{figure} /fig/en_qgis_graduated_classification_nigeria_flood_exercise.png
---
width: 600px
name: m3ex4_graduated_classif
align: center
---
:::

14. QGIS a maintenant créé cinq classes couvrant l’ensemble de la plage des nombres de population dans l’État de Borno. Cliquez sur l’onglet `Histogram` → `Load Values`. Ici, vous voyez la distribution des valeurs dans le jeu de données et les limites des classes. Nous voyons que la plupart des LGA ont une population inférieure à 300 personnes. Essayez aussi certains autres modes de classification, tels que les ruptures naturelles ou les intervalles égaux.

:::{figure} /fig/en_qgis_graduated_classification_Histogram_nigeria_flood_exercise.png
---
width: 400px
name: m3ex4_histogram
align: center
---
:::

15. Pour visualiser ensemble “Borno_admin2_pop” (montrant les LGA affectées) et “Borno_admin2_pop_copy” (montrant les données de population), nous devons modifier la symbologie de "Borno_admin2_pop". 
Tout d’abord, faites un clic droit sur la couche “Borno_admin2_pop” dans le `Layer Panel` → `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Accédez à l’onglet `Symbology`.
Actuellement, nous utilisons la classification `Categorized`. Nous voulons la conserver. Cependant, nous voulons uniquement afficher les LGA affectées. Nous décochons donc la ligne correspondant aux LGA sans `Affected` = `Yes`.
    * Faites un clic droit sur la couche "Borno_admin2_pop" dans le `Layer Panel` → `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Accédez à l’onglet `Symbology`.
    * Ensuite, double-cliquez sur la ligne `Yes`. Ici, nous avons deux options. Nous pouvons utiliser une grille ou seulement les bordures.
    * Pour utiliser une grille, faites défiler vers le bas et sélectionnez celle qui vous convient. Cliquez ensuite sur `OK`.

:::{figure} /fig/en_qgis_grid_flood_exercise.png
---
width: 600px
align: center
---
:::

* Pour n’utiliser que les bordures, cliquez sur `simple fill` → `Fill style` puis sélectionnez `No Brusch`. Ajustez le `Stroke Color` en rouge ou dans une autre couleur vive. Augmentez le `Stroke width` pour rendre les bordures plus épaisses. Cliquez ensuite sur `OK`.

:::{figure} /fig/en_qgis_now_brush_nigeria_flood_exercise.png
---
width: 400px
align: center
---
:::

16. Pour avoir une idée plus détaillée de l’étendue de l’inondation, nous pouvons charger la couche "VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp" qui montre l’étendue maximale des eaux de surface entre le 9 et le 30 octobre 2022. Si vous le souhaitez, vous pouvez aussi charger "VIIRS_20220901_20220930_PermanentWater_Nigeria.shp". Cette couche montre les lacs et autres entités permanentes d’eaux de surface.
Une fois les couches chargées dans QGIS, vous pouvez voir qu’elles s’affichent correctement. Cependant, en vérifiant les informations de couche, vous pouvez voir que les nouvelles couches ont un système de coordonnées de référence (CRS) différent. Elles ont le code EPSG 9707 alors que notre projet a 4326 ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_projections_wiki.md#how-to-check-epsg-code-crs-of-layer-data)).
    * Faites un clic droit sur la couche de données, puis cliquez sur `Properties`.
    * La fenêtre "Layer Properties" de la couche de données s’ouvrira. Cliquez sur `Information`.
    * Sous l’intitulé "Coordinate Reference System (CRS)", vous trouverez toutes les informations sur le CRS. Les plus importantes sont :
    - __Name:__ Ici, vous trouvez le code EPSG.
    - __Unites:__ Ici, vous pouvez voir s’il est possible d’utiliser des mètres avec cette couche de données ou la latitude et la longitude.

17. Cela deviendra un problème dès que nous ferons autre chose que simplement afficher les couches. Puisque nous voulons manipuler les couches à l’étape suivante, nous devons d’abord les reprojeter ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_projections_wiki.md#changing-the-projection-of-a-vector-layer)). 
    * Cliquez sur l’onglet `Vector` → `Data Management Tools` → `Reproject Layer` ou recherchez l’outil dans la `Processing Toolbox`.
    * Comme `Input layer`, sélectionnez "VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp".
    * Sélectionnez comme CRS cible / code EPSG __4326__.
    * Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png) à côté de `Reprojected`, indiquez le nom du fichier comme "Flood_extand_Nigeria_october_2022_reprojected.
    * Cliquez sur `Run`.
    * Supprimez l’ancienne couche du panneau des couches en faisant un clic droit sur la couche → `Remove layer`.
    
18. La couche d’étendue de l’inondation couvre l’ensemble du Nigeria. Nous pouvons utiliser l’outil `Clip` pour la découper selon la forme de l’État de Borno ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_geoprocessing_wiki.md#clip)).
    * Ouvrez la `Processing Toolbox` ([voici comment](/content/fr/Wiki/fr_qgis_interface_wiki.md#toolbox-toolbars)) et recherchez l’outil `Clip`.
    :::{Note}
    Il existe __deux__ versions de l’outil `Clip`. Comme nous travaillons avec des données vectorielles, assurez-vous d’utiliser celle sous "Vector overlay".
    :::
    * `Input layer`: "VIIRS_20220901_20220930_MaximumFloodWaterExtent_Nigeria.shp”
    * `Overlay layer`: “AOI_Borno_admin1”
    * Pour enregistrer le résultat, cliquez sur les trois points dans `Clipped` → `Save to GeoPackage` puis naviguez jusqu’à votre dossier `temp`. Enregistrez la nouvelle couche sous le nom "Flood_extend_october_2022_reprojected_Borno". Donnez à la nouvelle couche le même `Layer name` puis cliquez sur `Run`.

:::{figure} /fig/en_qgis_clip_flood_exercise.png
---
width: 400px
align: center
---
:::

Super, nous avons réalisé notre visualisation. BRAVO !
Vos résultats devraient ressembler à l’image ci-dessous.

:::{figure} /fig/en_qgis_result_flood_exercise.png
---
width: 600px
align: center
---
:::
