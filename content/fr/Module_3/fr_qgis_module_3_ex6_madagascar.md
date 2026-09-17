::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Exercice 6 : Réponse aux inondations à Sava <a id="exercise-6-sava-flood-response"></a>

::::{grid} 2
:::{grid-item-card}
__Objectif de l’exercice :__
^^^

Les participants travailleront avec plusieurs couches et effectueront des requêtes spatiales. De plus, ils apprendront à créer leurs propres géodonnées.

__Type d’exercice de formation :__

- Cet exercice peut être utilisé dans des formations en ligne et en présentiel. 

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour__
^^^ 

- Les bases de QGIS
- Travailler avec plusieurs couches
- Effectuer des requêtes spatiales
- Création de géodonnées

:::
::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé nécessaire pour l’exercice :__
^^^

- L’exercice prend environ 3 heures à réaliser, en fonction du nombre de participants et de leur familiarité avec les systèmes informatiques.

:::

:::{grid-item-card}
__Articles wiki pertinents :__
^^^

* [Importation de géodonnées dans QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html)
* [Concept de couche](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_layer_concept_wiki.html)
* [Classification des géodonnées - Catégorisée](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)
* [Classification des géodonnées - Graduée](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_graduated_wiki.html)
* [Requêtes spatiales](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html)
* [Fonction de table - Ajouter un champ](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_table_functions_wiki.html#add-field)
* [Numérisation - Données ponctuelles](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#add-geometries-to-a-layer)

:::
::::

::::{grid} 1
:::{grid-item-card}
__Contexte :__
^^^

« The Government declared a national emergency situation, on 3 April, following the passage of the Tropical Cyclone (TS) Gamane, that hit the north and northeast of Madagascar on 27 March » [Madagascar: Tropical Cyclone Gamane Flash Update No. 2, 4 April 2024 (reliefweb)](https://reliefweb.int/report/madagascar/madagascar-tropical-cyclone-gamane-flash-update-no-2-4-april-2024). L’analyse suivante utilisera des données réelles issues de cette catastrophe naturelle. L’objectif est d’identifier précisément les centres médicaux et établissements de santé qui ont été affectés par les inondations. De plus, nous évaluerons la viabilité de l’accès routier vers les lieux habités.

:::
::::

## Instructions pour les formateurs <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Coin des formateurs__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. un tableau Miro) où les participants peuvent ajouter leurs observations et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment organiser des formations ?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/fr_how_to_training.html#how-to-do-trainings) pour quelques conseils généraux sur l’animation des formations. 

### Conduire la formation <a id="conduct-the-training"></a>

__Introduction :__

- Présentez l’idée et l’objectif de l’exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a décompressé le dossier avant de commencer les tâches.

__Suivi guidé :__

- Montrez et expliquez chaque étape vous-même au moins deux fois et suffisamment lentement pour que tout le monde puisse voir ce que vous faites, et suivre dans son propre projet QGIS. 
- Assurez-vous que tout le monde suit et effectue les étapes lui-même en demandant régulièrement si quelqu’un a besoin d’aide ou si tout le monde suit toujours.  
- Soyez ouvert et patient face à chaque question ou problème qui pourrait survenir. Vos participants effectuent essentiellement du multitâche en prêtant attention à vos instructions et en s’orientant dans leur propre projet QGIS.

__Conclusion :__

- Laissez du temps pour toute question ou problème concernant les tâches à la fin de l’exercice.
- Laissez du temps pour les questions ouvertes. 

:::

### Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module3/Exercise_6/Modul_3_Exercise_6_Sava_flood.zip), enregistrez le dossier sur votre ordinateur et décompressez le fichier.__

:::

<!--:::{hint}
Reprojected and fixed Flood extend layer can be downloaded __[here](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/______________.zip)__
:::-->

| Nom du jeu de données| Titre original|Éditeur|Téléchargé depuis| 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| mdg_admin1.shp | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-mdg) | UN OCHA| HDX |
| mdg_admin2.shp | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-mdg) | UN OCHA| HDX |
| hotosm_mdg_health_facilities.gpkg |  [Madagascar Health Facilities (OpenStreetMap Export)]([https://data.humdata.org/dataset/hotosm_pak_health_facilities](https://data.humdata.org/dataset/madagascar-healthsites)) | Humanitarian OpenStreetMap Team (HOT) | HDX |
| TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp | [Satellite detected water extent over Sambava and Vohemar Districts, Sava Region, Madagascar as of 01 April 2024]([[https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024](https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024))) | UNOSAT | HDX |
|roads_sava.gpkg | Roads Sava | Humanitarian OpenStreetMap Team | HOT Export Tool |


<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint} Structure des dossiers

Pour garder vos données organisées et facilement accessibles, il est important de mettre en place une structure de dossiers claire sur votre ordinateur pour vos projets QGIS et vos géodonnées. Assurez-vous que les données de l’exercice sont enregistrées dans un emplacement permettant une récupération facile et une association avec le projet QGIS correspondant.

:::


## Tâche 1 : Obtenir une vue d’ensemble de la situation autour de Sambava et Vehomar <a id="task-1-gain-an-overview-of-the-situation-around-sambava-and-vehomar"></a>

::::{card}

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
name: 
align: right
name: IFRC Surge Icon
---
:::

__Contexte :__

Vous avez été déployé en tant que gestionnaire de l’information dans les régions de Madagascar touchées par les inondations. À votre arrivée, vous avez reçu des rapports de l’équipe opérationnelle indiquant que les distrcits [Sambava and Vohemar](https://www.openstreetmap.org/search?query=Sava%2C%20Madagascar#map=8/-14.374/49.795) de la région de Sava sont affectés par les inondations. L’équipe a besoin d’une vue d’ensemble générale des lieux affectés.

::::
 
1. Ouvrez QGIS et créez un [nouveau projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`.
2. Une fois le projet créé, [enregistrez le projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#save) dans le dossier "project" de l’exercice “Module_3_Exercise_2_Flood_Larkana”. Pour cela, cliquez sur `Project` → `Save as` et naviguez jusqu’au dossier. Nommez le projet "MDG_Sava_flood_2024".
3. Tout d’abord, nous voulons ajouter OpenStreetMap comme fond de carte pour l’orientation. Pour ajouter OSM comme fond de carte, cliquez sur `Layer` → `Add Layer` → `Add XYZ Layer…`. Choisissez `OpenStreetMap` et cliquez sur `Add`. 

:::{Tip}
Vous ne pouvez pas interagir avec un fond de carte !
:::

4. Ensuite, chargez le GeoPackage __"mdg_admin2.gpkg"__ dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à __"mdg_admin2.gpkg"__. Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


:::{Attention}
Les fichiers GeoPackage peuvent contenir plusieurs fichiers et même des projets QGIS entiers. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers que vous souhaitez charger dans votre projet QGIS.
:::

5. Tout d’abord, nous voulons exporter le district __Sambava__ et le district voisin __Vohemar__ depuis __mdg_admin2__ afin de l’avoir comme couche vectorielle autonome. Pour cela : 
    * Ouvrez la table attributaire de __mdg_admin2__ en faisant un clic droit sur la couche → `Open Attribute Table` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html)).
    * Trouvez la ligne de Sambava dans la colonne __ADM2_EN__ et sélectionnez-la en cliquant sur le numéro tout à fait à gauche de la table attributaire. La ligne apparaîtra en bleu et la zone de Sambava deviendra jaune dans le canevas cartographique. Vous pouvez faire un clic droit sur la ligne puis cliquer sur `Zoom to Feature` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    Pour sélectionner le district de Vohemar, cliquez sur l’icône `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) dans la barre d’outils de QGIS, maintenez la touche `Shift` de votre clavier, puis cliquez sur les districts soit sur la carte soit dans la table attributaire ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html#manual-selection)).
    * Une fois la sélection des districts terminée, cliquez sur l’icône ![](/fig/qgis_move_symbol.png) pour quitter le mode de sélection d’entités.
    * Faites ensuite un clic droit sur la couche dans le panneau des couches puis cliquez sur `Export` → `Save Selected Features as`. Nous voulons enregistrer les districts sélectionnés comme GeoPackage, donc choisissez l’option `Format` en conséquence. Cliquez sur les trois points et naviguez jusqu’à votre dossier `temp`. Ici, vous pouvez donner à la couche le nom __“Flood_2024_AOI”__ puis cliquer sur `Save`. Vous devriez maintenant voir le même nom dans le champ `Layer name`. Cliquez sur `OK` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file)).
    * Cliquez sur l’icône ![](/fig/selection_toolbar_feature_deselection.png) dans la barre d’outils pour terminer la sélection d’entités.

:::{card}
__Résultat :__
^^^

Vous avez maintenant une vue d’ensemble de l’emplacement des districts de Sambava et Vohemar à Sava. L’équipe opérationnelle peut utiliser cette information. 

:::

:::{Tip}
N’oubliez pas d’enregistrer votre projet de temps en temps !
:::

## Tâche 2 : Estimation de l’impact des inondations sur le secteur de la santé à Sambava et Vohemar <a id="task-2-estimation-of-flood-impact-on-the-health-sector-in-sambava-and-vohemar"></a>

::::{card}

:::{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
:::

__Contexte :__

Des publications sur les réseaux sociaux ont indiqué un impact significatif sur le système de santé à Madgascar. Vous avez été chargé d’en apprendre autant que possible sur la situation à Sava et, si possible, d’estimer l’impact sur le système de santé.

::::

1. La première chose à faire est d’identifier où se trouvent les établissements de santé dans la zone. Pour cela, vous effectuez une recherche rapide sur HDX. Vous trouvez le jeu de données Madagascar Health Facilities (OpenStreetMap Export). Cela fera l’affaire pour l’instant.

    * Chargez le GeoPackage __"hotosm_mdg_health_facilities.gpkg"__ dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à __"mdg_admin2.gpkg"__. Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    * Tout d’abord, nous devons extraire les établissements de santé situés dans notre zone d’intérêt. Pour cela, nous utiliserons l’outil __"Extract by Location"__.
    * Ouvrez la `Processing Toolbox` ([voici comment](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil.
        * Comme `Input Layer`, nous utiliserons "hotosm_mdg_health_facilities".
        * Pour `By comparing to the features from`, nous utilisons la couche “Flood_2024_AOI”.
        * Comme `Geometric predicate`, nous utilisons `intersect`. 
        * Pour enregistrer le résultat, cliquez sur les trois points dans `Extract (location)` → `Save to GeoPackage` et naviguez jusqu’à votre dossier `temp`. Enregistrez la nouvelle couche sous le nom __“Health_Facilities_Flood_2024_AOI”__. Donnez à la nouvelle couche le même `Layer name` puis cliquez sur `Run`.
    * Ouvrez la table attributaire de la nouvelle couche et examinez-la.

:::{figure} /fig/m3_ex6_qgis_task2_1.png
---
width: 400px
name: m3_ex6_qgis_task2_1
align: center
---
Extract by location. 
:::

Très bien, nous avons maintenant une bonne vue d’ensemble de l’emplacement des établissements de santé. Nous avons besoin d’informations bien meilleures sur la zone inondée pour identifier les établissements de santé touchés par l’inondation. Heureusement, l’ONU vient de partager un jeu de données sur l’étendue des inondations. Satellite detected water extent over Sambava and Vohemar Districts, Sava Region, Madagascar as of 01 April 2024.

2. Chargez le jeu de données __"TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp"__ dans votre QGIS.
   * Ajustez l’opacité de la couche d’inondation en faisant un clic droit sur la couche __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology`. Ajustez l’opacité à environ 60 % en déplaçant le curseur.
3. Une fois que vous avez chargé les couches dans QGIS, vous pouvez voir qu’elles s’affichent correctement. Cependant, en vérifiant les informations de la couche, vous pouvez voir que les nouvelles couches ont un système de coordonnées de référence (CRS) différent. Elles ont le code EPSG 9707 alors que notre projet a 4326 ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * Faites un clic droit sur la couche de données, puis cliquez sur “Properties”.
    * La fenêtre “Layer Properties” de la couche de données s’ouvrira. Cliquez sur “Information”.
    * Sous l’intitulé “Coordinate Reference System (CRS)”, vous trouverez toutes les informations sur le CRS. Les plus importantes sont :
    - __Name:__     Ici, vous trouvez le code EPSG.
    - __Unites:__    Ici, vous pouvez voir s’il est possible d’utiliser des mètres avec cette couche de données, des degrés ou la latitude et la longitude. 
4. Cela deviendra un problème dès que nous ferons autre chose que simplement afficher les couches. Puisque nous voulons manipuler les couches à l’étape suivante, nous devons d’abord les reprojeter ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)). 
    * Cliquez sur l’onglet `Vector` -> `Data Management Tools` -> `Reproject Layer` ou recherchez l’outil dans la `Processing Toolbox`.
    * Comme `Input layer`, sélectionnez __"TDX_20240401_FloodExtent_SambavaDistrict_MDG.shp"__
    * Sélectionnez comme CRS cible / code EPSG __4326__.
    * Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png) à côté de `Reprojected`, indiquez le nom du fichier comme __"2024_MinFloodExtend_reprojected"__.
    * Cliquez sur `Run`
    * Supprimez l’ancienne couche du panneau des couches en faisant un clic droit sur la couche -> `Remove layer`.
    * Ajustez l’opacité de la couche d’inondation en faisant un clic droit sur la couche __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__ dans le Layer Panel puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology`. Ajustez l’opacité à environ 60 % en déplaçant le curseur.

Nous avons observé que certains établissements de santé sont situés dans la zone inondée. Afin de visualiser cette information sur la carte, nous prévoyons d’inclure un nouvel attribut appelé __"affected"__ dans la table attributaire de __"Health_Facilities_Flood_2024_AOI"__.
Pour ce faire, la première étape consistera à sélectionner tous les établissements de santé affectés. Une nouvelle colonne contenant cette information est ensuite ajoutée à la table attributaire de __"Health_Facilities_Flood_2024_AOI"__.

5. Ouvrez la `Processing Toolbox` ([voici comment](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil __"Select by Location"__.
    * `Select features from` = __"Health_Facilities_Flood_2024_AOI"__.
    * Comme `Geometric predicate`, nous utilisons `intersect`.
    * Pour `By comparing to the features from`, nous utilisons la couche __"TDX_20240401_FloodExtent_SambavaDistrict_MDG"__.
    * `Modify current selection by` = `creating new selection`.
    * Cliquez sur `Run`.

:::{card}
Veuillez noter : d’après les données originales, aucun établissement de santé réel n’a été affecté par l’inondation, mais dans le cadre de l’apprentissage de QGIS, nous avons placé trois établissements de santé fictifs dans les zones inondées.
:::


:::{figure} /fig/m3_ex6_qgis_task2_5.png
---
width: 400px
name: m3_ex6_qgis_task2_5
align: center
---
Selecting the flood affected health facilities.
:::

::::{warning}

Dans le cas où vous rencontreriez l’erreur suivante :

```
Feature (1) from “TDX_20240401_FloodExtent_SambavaDistrict_MDG” has invalid geometry. Please fix the geometry or change the Processing setting to the “Ignore invalid input features” option. Execution failed after 0.07 seconds
```

Vous devez d’abord utiliser l’outil __"Fix Geometry"__ avant de répéter l’étape 5 précédemment échouée avec l’outil __"Select by Location"__.

* Pour ce faire, ouvrez la `Processing Toolbox` ([voici comment](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil __"Fix Geometries"__.
* `Input layer` = `TDX_20240401_FloodExtent_SambavaDistrict_MDG`
* Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png), indiquez le nom du fichier comme __"TDX_20240401_FloodExtent_SambavaDistrict_MDG_fix"__.
* Cliquez sur `Run`.

:::{figure} /fig/ m3_ex6_qgis_fix.png
---
width: 400px
name: m3_ex6_qgis_fix
align: center
---
Correction de la géométrie
:::

::::

6. Ouvrez la table attributaire de __"Health_Facilities_Flood_2024_AOI"__ en faisant un clic droit sur la couche → `Open Attribute Table`([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html)) puis activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Vous pouvez maintenant modifier directement les données dans la table.
7. Tout d’abord, nous ajoutons une nouvelle colonne avec le nom __“Flood_affected”__. Pour cela, cliquez sur ![](/fig/mActionNewAttribute.png). Dans la fenêtre `Add field`, vous devez ajouter le nom et définir le `Type` sur `Text(string)`. Cliquez sur `OK` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#add-new-column)).


:::{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column
align: center
---
Ajouter une nouvelle colonne
:::

8. Recherchez maintenant l’option `Show all Features` dans le coin inférieur gauche et cliquez dessus. Ensuite, sélectionnez l’option `Show selected features` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). Cela filtrera la table pour n’afficher que les lignes représentant les établissements de santé directement touchés par l’inondation.
Heureusement, aucun établissement de santé n’est directement affecté par l’inondation.
9. Si certains étaient affectés : écrivez `Yes` dans la colonne __"Flood_affected"__.
 * Une fois terminé, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications et désactivez le mode édition en cliquant de nouveau sur ![](/fig/mActionToggleEditing.png)([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
 * Cliquez sur l’icône ![](/fig/selection_toolbar_feature_deselection.png) dans la barre d’outils pour terminer la sélection des entités.

* Pour visualiser le jeu de données enrichi, nous utilisons la fonction "Categorized Classification". Cela signifie que nous sélectionnons une colonne de la table attributaire et utilisons son contenu comme catégories pour trier et afficher les données ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)).
    * Faites un clic droit sur la couche __"Health_Facilities_Flood_2024_AOI"__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology`.
    * En haut, vous trouverez un menu déroulant. Ouvrez-le puis choisissez `Categorized`. Sous `Value`, sélectionnez “Flood_affected”.
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir toutes les valeurs ou attributs uniques de la colonne sélectionnée “Flood_affected”. Vous pouvez ajuster les couleurs en double-cliquant sur chaque couleur dans le champ central. Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.

:::{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Classification des établissements de santé affectés par les inondations
:::

:::{card} 
__Résultat :__
Nous avons identifié que 3 établissements de santé ont été inondés par les inondations. 
:::

## Tâche 3 : Accès logistique <a id="task-3-logistical-access"></a>

::::{card}

:::{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
align: right
name: IFRC Logistics Icon
---
:::

Contexte : 

L’équipe opérationnelle prépare des plans pour acheminer des fournitures indispensables vers les régions touchées de Sambava et Vohemar. À l’heure actuelle, il existe une incertitude quant à la manière dont ces fournitures peuvent y être transportées. L’équipe opérationnelle a demandé davantage d’informations à ce sujet.
Elle a besoin de réponses aux deux questions suivantes :

* Quelles routes menant aux régions affectées sont bloquées, et à quels emplacements précis sont-elles bloquées ?
<!--* Are there any bridges that can be crossed from the eastern side of the Indus to the western side, and where are these bridges located?-->
* Si le transport de fournitures par route vers la région n’est pas réalisable, quelle autre méthode pourrait être utilisée pour acheminer les fournitures ?


Afin d’obtenir une image plus claire, nous devons importer les données du réseau routier de la région dans QGIS. Recherchez le fichier dans le dossier input. Le réseau routier est initialement affiché sans montrer les types de routes ni d’autres détails pertinents. Nous devrions appliquer une technique de classification catégorisée afin d’afficher uniquement les routes spécifiques qui nous intéressent.
::::

1. Chargez le jeu de données __"roads_sava.gpkg"__ depuis votre dossier input dans votre QGIS.
2. Pour la classification catégorisée, faites un clic droit sur la couche __"roads_sava"__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)).
    * En haut, vous trouverez un menu déroulant. Ouvrez-le puis choisissez `Categorized`. Sous `Value`, sélectionnez “highway”.
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir toutes les valeurs ou attributs uniques de la colonne sélectionnée “Flood_affacted”. Vous pouvez ajuster les couleurs en double-cliquant sur les couleurs de chaque ligne dans le champ central.
    * Supprimez la coche de toutes les catégories sauf : `motorway`, `primary`, `secondary`, `trunk`.
    :::{figure} /fig/m3_ex6_qgis_task3_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2
    align: center
    ---
    Classification des routes
    :::
    * Vous avez la possibilité de personnaliser l’épaisseur des lignes des routes principales afin d’améliorer la visualisation. Ouvrez la fenêtre de symbologie, puis sélectionnez `Symbol`. Dans la nouvelle fenêtre, vous pouvez ajuster l’épaisseur des lignes selon vos préférences.
    :::{figure} /fig/m3_ex6_qgis_task3_2_2.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_2_2
    align: center
    ---
    Classification des routes
    :::
    * Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.
3. Pour simplifier le processus, nous allons rechercher visuellement les routes bloquées et les marquer avec des points. Pour cela, nous créerons un tout nouveau jeu de données ponctuelles représentant les routes bloquées.
    * Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer`([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#create-a-new-layer)). 
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) puis naviguez jusqu’au dossier `temp`. Donnez au nouveau jeu de données le nom __“MDG_flood_2024_blocked_road”__. Cliquez sur `Save`.
    - `Geometry type`: sélectionnez `Point`
    - Sous `Additional dimension`, vous devez toujours vous assurer qu’aucune d’entre elles n’est cochée. 
    - Sélectionnez le système de coordonnées de référence (CRS) "EPSG:4326-WGS 84". Par défaut, QGIS sélectionne le CRS du projet. 
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: sélectionnez `Text (string)`
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Créez un autre champ avec le `name` __"Blocked_bridge"__ et le `Type`: sélectionnez `Text (string)`.
        * Cliquez sur `OK`.
    * Votre nouvelle couche apparaîtra dans le `Layer Panel`.
    :::{figure} /fig/m3_ex6_qgis_Task3_3.png
    ---
    width: 400px
    name: m3_ex6_qgis_Task3_3
    align: center
    ---
    Nouvelle couche avec les routes bloquées.
    :::
4. Vous pouvez maintenant créer un point pour chaque endroit où la couche d’inondation recouvre les routes principales traversant l’AOI [wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#creation-of-point-data). Actuellement, la nouvelle couche __“MDG_flood_2024_blocked_road”__ est vide. Pour ajouter des entités, nous pouvons utiliser la `Digitizing Toolbar`. Si vous ne voyez pas la barre d’outils, cliquez sur l’onglet `View` → `Toolbars` et cochez `Digitizing Toolbar` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md#creation-of-point-data)). ![](/fig/Digitizing_Toolbar.png) 
    * Activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png). Activez ensuite l’option d’ajout de nouveaux points en cliquant sur ![](/fig/mActionCapturePoint.png).
    * Recherchez les endroits où la couche d’inondation recouvre les routes principales ou les ponts. Une fois que vous en avez trouvé un, faites un clic gauche sur l’emplacement que vous souhaitez numériser.
    * Une fois que vous cliquez sur un endroit, une fenêtre apparaîtra. Indiquez que la route est bloquée en écrivant `Yes` dans le champ `Blocked_road`.
    * Répétez cette étape pour tous les emplacements que vous pouvez trouver. 
    :::{figure} /fig/m3_ex6_qgis_task3_4.png
    ---
    width: 200px
    name: m3_ex6_qgis_task3_4
    align: center
    ---
    Numérisation des routes bloquées.
    :::
    * Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    * Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.
5. Nous avons maintenant cartographié toutes les routes de notre AOI qui sont bloquées par l’inondation. Nous pouvons utiliser des icônes au lieu de simples points pour afficher la couche __“MDG_flood_2024_blocked_road”__ afin de mieux visualiser ce fait [wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_single_symbol_wiki.html).

    * Faites un clic droit sur la couche __“MDG_flood_2024_blocked_road”__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology`.
    * Conservez l’option `Single Symbol`. Sélectionnez n’importe quel symbole de la liste qui convient pour marquer les routes bloquées (assurez-vous que le filtre est défini sur `Favourites` ou `All Symbols`).
    * Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.
    * Une fois terminé, cliquez sur l’icône ![](/fig/qgis_move_symbol.png) pour quitter le mode de sélection d’entités.
    :::{figure} /fig/m3_ex6_qgis_task3_5.png
    ---
    width: 600px
    name: m3_ex6_qgis_task3_5
    align: center
    ---
    Visualisation des routes bloquées avec des icônes.
    :::

:::{card}

L’équipe opérationnelle dispose maintenant de toutes les informations dont elle a besoin pour planifier sa logistique. Bon travail !

:::
