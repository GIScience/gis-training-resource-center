::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
:::{grid-item-card}
:link: https://giscience.github.io/gis-training-resource-center/content/fr/Module_3/fr_qgis_module_3_exercises.html
__Cliquez ici pour revenir à la page d’aperçu des exercices du module 3__ 
:::
::::

# Exercice 5 : Réponse aux inondations à Larkana <a id="exercise-5-larkana-flood-response"></a>

:::{topic} Objectif de l’exercice

En 2024, les provinces du Pendjab, du Sindh et du Baloutchistan au Pakistan ont connu des inondations dévastatrices en raison de pluies intenses et prolongées. L’analyse suivante utilisera des données réelles issues de cette catastrophe naturelle. L’objectif est d’identifier précisément les centres médicaux et les établissements de santé qui ont été affectés par les inondations. De plus, nous évaluerons la praticabilité de l’accès routier à la ville de Larkana pendant toute la période des inondations.

Les participants travailleront avec plusieurs couches et effectueront des requêtes spatiales. En outre, ils apprendront à créer leurs propres géodonnées. L’exercice est divisé en trois tâches. Dans la première partie, nous exporterons les limites administratives dans notre zone d’intérêt (AOI). Dans la deuxième tâche, les établissements de santé situés dans notre AOI seront extraits et nous identifierons quels établissements de santé se trouvent à l’intérieur de la couche d’étendue des inondations. Dans la troisième tâche, l’accès routier sera déterminé en identifiant quelles routes sont potentiellement inondées. 
:::

::::{grid} 1

:::{grid-item-card}
__Compétences couvertes dans cet exercice__
^^^ 

- Sélectionner des entités et les exporter vers un nouveau fichier
- Extraire par localisation
- Reprojeter une couche
- Modifier la table attributaire
- Classification
- Numériser une couche de points

:::
::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé nécessaire pour l’exercice__
^^^

- L’exercice prend environ 3 heures à réaliser, selon le nombre de participants et leur familiarité avec les systèmes informatiques.

:::

:::{grid-item-card}
__Articles wiki et chapitres de module pertinents__
^^^

* [Importation de géodonnées dans QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html)
* [Concept de couche](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_layer_concept_wiki.html)
* [Classification des géodonnées - Catégorisée](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)
* [Classification des géodonnées - Graduée](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_graduated_wiki.html)
* [Requêtes spatiales](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html)
* [Fonction de table - Ajouter un champ](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_table_functions_wiki.html#add-field)
* [Numérisation - Données ponctuelles](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitalization_wiki.html#add-geometries-to-a-layer)
:::
::::



## Instructions pour les formateurs <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Espace formateurs__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par exemple un tableau Miro) où les participants peuvent ajouter leurs observations et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment organiser des formations ?](https://giscience.github.io/gis-training-resource-center/content/fr/Trainers_corner/fr_how_to_training.html#how-to-do-trainings) pour quelques conseils généraux sur la conduite de formations

### Conduire la formation <a id="conduct-the-training"></a>

__Introduction :__

- Présentez l’idée et l’objectif de l’exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a décompressé le dossier avant de commencer les tâches.

__Suivi pas à pas :__

- Montrez et expliquez chaque étape vous-même au moins deux fois et suffisamment lentement pour que tout le monde puisse voir ce que vous faites et suivre dans son propre projet QGIS. 
- Assurez-vous que tout le monde suit et effectue les étapes lui-même en demandant régulièrement si quelqu’un a besoin d’aide ou si tout le monde suit toujours.  
- Soyez ouvert et patient face à chaque question ou problème qui pourrait survenir. Vos participants font essentiellement du multitâche en prêtant attention à vos instructions tout en s’orientant dans leur propre projet QGIS.

__Clôture :__

- Prévoyez du temps à la fin de l’exercice pour traiter les éventuels problèmes ou questions concernant les tâches.
- Réservez également un moment pour les questions ouvertes. 

:::

## Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Modul_3_Exercise_4_Larkana_flood.zip

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Modul_3_Exercise_4_Larkana_flood.zip), enregistrez le dossier sur votre ordinateur et décompressez le fichier.__

:::


| Jeu de données | Titre original | Éditeur | Téléchargé depuis | 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_Sindh_adm1.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sindh_adm2.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) |UN OCHA | HDX |
| PAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) |UNO SAT | HDX |
| Roads_Larkana.gpkg | [Roads Larkana](https://export.hotosm.org/v3/exports/7f1e78c7-f671-41e3-9ec3-6fc6ac31c929) |Humanitarian OpenStreetMap Team | HOT Export Tool (Export créé en septembre 2024) |

<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint}

La couche d’étendue des inondations reprojetée et corrigée peut être téléchargée __[ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_4/Module_3_Exercise_4_Larkana_flood_Day2.zip)__

:::

```{hint} Structure des dossiers
Pour garder vos données organisées et facilement accessibles, il est important d’établir une structure de dossiers claire sur votre ordinateur pour vos projets QGIS et vos géodonnées. Assurez-vous que les données de l’exercice sont enregistrées dans un emplacement permettant une récupération facile et leur association avec le projet QGIS correspondant.
```

:::{figure} /fig/M3_Ex5_workflow_chart.drawio.png
---
name: M5_Ex5_Workflow_chart
width: 450 px
---
:::

## Tâche 1 : Obtenir une vue d’ensemble de la situation autour de Larkana <a id="task-1-gain-an-overview-of-the-situation-around-larkana"></a>

:::::{card} 
__Contexte__
^^^
```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

Vous avez été déployé en tant que gestionnaire de l’information dans les régions du Pakistan touchées par les inondations. À votre arrivée, vous avez reçu des rapports de l’équipe des opérations indiquant que la ville de [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) et ses environs ont été sévèrement touchés par les inondations. L’équipe a besoin d’une vue d’ensemble de la localisation de la ville.

:::::


::::{margin}
```{admonition} Astuce
:class: note
Vous ne pouvez pas interagir avec un fond de carte !
```
::::

1. Ouvrez QGIS et créez un [nouveau projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`.
2. Une fois le projet créé, [enregistrez le projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#save) dans le dossier “project” de l’exercice “Module_3_Exercise_2_Flood_Larkana”. Pour cela, cliquez sur `Project` → `Save as` et naviguez jusqu’au dossier. Nommez le projet “PAK_Larkana_flood_2024”.
3. Tout d’abord, nous voulons ajouter OpenStreetMap comme fond de carte pour l’orientation. Pour ajouter OSM comme fond de carte, cliquez sur `Layer` → `Add Layer` → `Add XYZ Layer…`. Choisissez `OpenStreetMap` puis cliquez sur `Add`. 
4. Ensuite, chargez le GeoPackage __"PAK_Sindh_adm2.gpkg"__ dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à __"PAK_Sindh_adm2.gpkg"__. Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


```{Attention}
Les fichiers GeoPackage peuvent contenir plusieurs fichiers et même des projets QGIS entiers. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers que vous souhaitez charger dans votre projet QGIS.
```

5. Tout d’abord, nous voulons exporter __le district de Larkana__ et les districts voisins __Kambar Shahdad Kot__, __Shikarpur__ et __Sukkur__ depuis __PAK_adm2_Sindh__ afin de les avoir comme couche vectorielle autonome. Pour cela : 
    * Ouvrez la table attributaire de __PAK_adm2_Sindh__ en faisant un clic droit sur la couche → `Open Attribute Table` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html)).
    * Trouvez la ligne de Larkana et sélectionnez-la en cliquant sur le numéro tout à gauche de la table attributaire. La ligne apparaîtra en bleu et la zone de Larkana deviendra jaune sur le canevas cartographique. Vous pouvez faire un clic droit sur la ligne puis cliquer sur `Zoom to Feature` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#zoom-in-on-a-specific-feature)).
    Pour sélectionner les districts environnants, cliquez sur l’icône `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png) dans la barre d’outils QGIS, maintenez la touche `Shift` de votre clavier et cliquez sur les districts soit sur la carte, soit dans la table attributaire ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html#manual-selection)).
    * Une fois la sélection des districts terminée, cliquez sur l’icône ![](/fig/qgis_move_symbol.png) pour quitter le mode de sélection d’entités.
    * Faites ensuite un clic droit sur la couche dans le panneau des couches puis cliquez sur `Export` → `Save Selected Features as`. Nous voulons enregistrer les districts sélectionnés sous forme de GeoPackage, choisissez donc l’option `Format` correspondante. Cliquez sur les trois points et naviguez jusqu’à votre dossier `temp`. Vous pouvez donner à la couche le nom __“Flood_2024_AOI”__ puis cliquer sur `Save`. Vous devriez maintenant voir le même nom dans le champ `Layer name`. Cliquez sur `Ok` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_non_spatial_queries_wiki.html#save-selected-features-as-a-new-file))
    * Cliquez sur l’icône ![](/fig/selection_toolbar_feature_deselection.png) dans la barre d’outils pour terminer la sélection des entités.

:::{topic} Résultat obtenu

Vous avez maintenant une vue d’ensemble de l’emplacement du district de Larkana dans le Sindh. L’équipe des opérations peut utiliser cette information. 

:::

::::{margin}
```{Tip}
N’oubliez pas d’enregistrer votre projet de temps en temps !
```
::::

## Tâche 2 : Estimation de l’impact des inondations sur le secteur de la santé à Larkana <a id="task-2-estimation-of-flood-impact-on-the-health-sector-in-larkana"></a>

::::{topic} Contexte

```{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
```

Des publications sur les réseaux sociaux ont indiqué un impact important sur le système de santé dans la région. Vous avez pour mission d’en apprendre le plus possible sur la situation et, si possible, d’estimer l’impact sur le système de santé.

::::

1. La première chose à faire est de déterminer où se situent les établissements de santé dans la zone. Pour cela, vous effectuez une recherche rapide sur HDX. Vous trouvez le jeu de données Pakistan Health Facilities (OpenStreetMap Export). Cela conviendra pour le moment.

    * Chargez le GeoPackage __"PAK_Health_Facilities_complete.gpkg"__ dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à __"PAK_Sindh_adm2.gpkg"__. Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).
    * Nous devons d’abord extraire les établissements de santé situés dans notre zone d’intérêt. Pour cela, nous utiliserons l’outil __"Extract by Location"__.
    * Ouvrez la `Processing Toolbox` ([voici comment faire](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil.
        * Comme `Input Layer`, nous utiliserons "PAK_Health_Facilities_complete".
        * Pour `By comparing to the features from`, nous utiliserons la couche “Flood_2024_AOI”.
        * Comme `Geometric predicate`, nous utiliserons `intersect`. 
        * Pour enregistrer le résultat, cliquez sur les trois points à `Extract (location)` → `Save to GeoPackage` et naviguez jusqu’à votre dossier `temp`. Enregistrez la nouvelle couche sous le nom __“Health_Facilities_Flood_2024_AOI”__. Donnez à la nouvelle couche le même `Layer name` puis cliquez sur `Run`.
    * Ouvrez la table attributaire de la nouvelle couche et examinez-la.

    * Nous devons d’abord extraire les établissements de santé situés dans notre zone d’intérêt. Pour cela, nous utiliserons l’outil __"Extract by Location"__.
    * Ouvrez la `Processing Toolbox` ([voici comment faire](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil.
        * Comme `Input Layer`, nous utiliserons "PAK_Health_Facilities_complete".
        * Pour `By comparing to the features from`, nous utiliserons la couche "Flood_2024_AOI".
        * Comme `Geometric predicate`, nous utiliserons `intersect`. 
        * Pour enregistrer le résultat, cliquez sur les trois points à `Extract (location)` → `Save to GeoPackage` et naviguez jusqu’à votre dossier `temp`. Enregistrez la nouvelle couche sous le nom __“Health_Facilities_Flood_2024_AOI”__. Donnez à la nouvelle couche le même `Layer name` puis cliquez sur `Run`.
    * Ouvrez la table attributaire de la nouvelle couche et examinez-la.

```{figure} /fig/PAK_extract_locatio_HS.png
---
width: 400px
name: Extract by location Pakistan
align: center
---
Extraction par localisation au Pakistan
```

Très bien, nous avons maintenant une bonne vue d’ensemble de l’emplacement des établissements de santé. Nous avons besoin d’informations beaucoup plus précises sur la zone inondée afin d’identifier les établissements de santé touchés par l’inondation. Heureusement, l’ONU vient de partager un jeu de données sur l’étendue des inondations : Satellite detected water extents from 08 to 12 August 2024 over Pakistan.

2. Chargez le jeu de données __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ dans QGIS.
3. Une fois les couches chargées dans QGIS, vous pouvez voir qu’elles s’affichent correctement. Cependant, en vérifiant les informations de la couche, vous pouvez constater que les nouvelles couches ont un système de coordonnées de référence (CRS) différent. Elles ont le code EPSG 9707 alors que notre projet est en 4326 ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * Faites un clic droit sur la couche de données, puis cliquez sur `Properties`.
    * La fenêtre "Layer Properties" de la couche de données s’ouvrira. Cliquez sur l’onglet `Information`.
    * Sous l’intitulé “Coordinate Reference System (CRS)”, vous trouverez toutes les informations concernant le CRS. Les plus importantes sont :
    - __Name :__ vous y trouvez le code EPSG.
    - __Units :__ vous pouvez y vérifier s’il est possible d’utiliser des mètres avec cette couche de données, des degrés, ou des coordonnées latitude/longitude. <!--ADD: Why is it a problem? Add explanation-->
4. Cela posera problème dès que nous ferons autre chose qu’afficher les couches. Puisque nous voulons manipuler les couches à l’étape suivante, nous devons d’abord les reprojeter ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)). 
    * Cliquez sur l’onglet `Vector` → `Data Management Tools` → `Reproject Layer` ou recherchez l’outil dans la `Processing Toolbox`.
    * Comme `Input layer`, sélectionnez __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__.
    * Sélectionnez comme CRS cible / code EPSG __4326__.
    * Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png) à côté de `Reprojected`, et indiquez le nom de fichier __"2024_MinFloodExtend_reprojected"__.
    * Cliquez sur `Run`.
    * Supprimez l’ancienne couche du panneau des couches par clic droit sur la couche → `Remove layer`.
    * Ajustez l’opacité de la couche d’inondation en faisant un clic droit sur la couche __"2024_MinFloodExtend_reprojected"__ dans le panneau des couches puis sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section d’onglets verticale à gauche. Accédez à l’onglet `Symbology`. Ajustez l’opacité à environ 60 % à l’aide du curseur.

Nous avons observé que certains établissements de santé ont été touchés par l’inondation. Afin de visualiser cette information sur la carte, nous prévoyons d’inclure un nouvel attribut appelé __"affected"__ dans la table attributaire de __"Health_Facilities_Flood_2024_AOI"__.
Pour y parvenir, notre première étape consistera à sélectionner tous les établissements de santé affectés. Une nouvelle colonne contenant cette information sera ensuite ajoutée à la table attributaire de __"Health_Facilities_Flood_2024_AOI"__.

5. Ouvrez la `Processing Toolbox` ([voici comment faire](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil __"Select by Location"__.
    * `Select features from` = __"Health_Facilities_Flood_2024_AOI"__.
    * Comme `Geometric predicate`, nous utilisons `intersect`.
    * Pour `By comparing to the features from`, nous utilisons la couche __"2024_MinFloodExtent_reprojected"__.
    * `Modify current selection by` = `creating new selection`.
    * Cliquez sur `Run`.

```{figure} /fig/PAK_flood_select_by_location.PNG
---
width: 400px
name: Select flood affected health facilities
align: center
---
Sélection des établissements de santé affectés par les inondations
```

::::{admonition} Message d’erreur possible
:class: warning, dropdown
Si vous rencontrez l’erreur suivante :

> Feature (1) from “2024_MinFloodExtend_reprojected” has invalid geometry. Please fix the geometry or change the Processing setting to the “Ignore invalid input features” option.
Execution failed after 0.07 seconds

Vous devez d’abord utiliser l’outil __"Fix Geometry"__ avant de répéter l’étape 5 précédente utilisant l’outil __"Select by Location"__.

* Pour cela, ouvrez la [`Processing Toolbox`](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox) et recherchez l’outil __"Fix Geometries"__.
* `Input layer` = `2024_MinFloodExtend_reprojected`
* Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png), puis indiquez le nom de fichier __"2024_MinFloodExtend_reprojected_fix"__.
* Cliquez sur `Run`.

```{figure} /fig/ PAK_flood_ngeomertrie_error.PNG
---
width: 400px
name: Fix Geometry
align: center
---
Le message d’erreur indiquant des géométries invalides.
```

::::

6. Ouvrez la table attributaire de __"Health_Facilities_Flood_2024_AOI"__ en faisant un clic droit sur la couche → `Open Attribute Table` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html)) et activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Vous pouvez maintenant modifier les données directement dans la table.

7. Ajoutez d’abord une nouvelle colonne nommée __“Flood_affected”__. Pour cela, cliquez sur ![](/fig/mActionNewAttribute.png). Dans la fenêtre `Add field`, vous devez saisir le nom et définir le `Type` sur `Text(string)`. Cliquez sur `Ok` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#add-new-column))

```{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column Pakistan
align: center
---
Ajout d’une nouvelle colonne à la table attributaire. 
```

8. Recherchez maintenant l’option `Show all Features` en bas à gauche et cliquez dessus. Sélectionnez ensuite l’option `Show selected features` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). Cela filtrera la table pour n’afficher que les lignes représentant les établissements de santé directement touchés par l’inondation.
Vous pouvez maintenant écrire `Yes` dans la colonne __"Flood_affected"__.
 * Une fois terminé, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications, puis désactivez le mode édition en cliquant à nouveau sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
 * Cliquez sur l’icône ![](/fig/selection_toolbar_feature_deselection.png) dans la barre d’outils pour terminer la sélection des entités.

9. Pour visualiser le jeu de données enrichi, nous utilisons la fonction "Categorized Classification". Cela signifie que nous sélectionnons une colonne de la table attributaire et utilisons son contenu comme catégories pour trier et afficher les données ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)).
    * Faites un clic droit sur la couche __"Health_Facilities_Flood_2024_AOI"__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section d’onglets verticale à gauche. Accédez à l’onglet `Symbology`.
    * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Categorized`. Sous `Value`, sélectionnez "Flood_affacted".
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez alors voir toutes les valeurs ou tous les attributs uniques de la colonne sélectionnée "Flood_affacted". Vous pouvez ajuster les couleurs en double-cliquant sur chaque couleur dans le champ central. Une fois terminé, cliquez sur `Apply` puis sur `Ok` pour fermer la fenêtre de symbologie.

```{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Les établissements de santé classifiés selon qu’ils sont ou non affectés par les inondations. 
```

:::{card} 
__Résultat obtenu :__
^^^

Nous avons identifié précisément les établissements de santé qui ont été inondés. Nos résultats indiquent qu’un total de quatre établissements ont été complètement inondés et sont actuellement non opérationnels. Étant donné que nous avons évalué l’impact minimal des inondations, il est très probable que davantage d’établissements de santé soient également touchés. Ces données sont cruciales pour notre équipe opérationnelle, car elles lui permettront de planifier et d’exécuter une réponse efficace.

:::

## Tâche 3 : Accès logistique à la ville de Larkana <a id="task-3-logistical-access-to-larkana-city"></a>

::::{topic} Contexte

```{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
name: 
align: right

name: IFRC Logistics Icon
---
```

L’équipe des opérations prévoit d’acheminer des fournitures indispensables vers la région affectée autour de Larkana. Actuellement, il existe une incertitude sur la manière dont ces fournitures peuvent y être transportées. L’équipe des opérations a demandé davantage d’informations à ce sujet.

Elle a besoin de réponses aux trois questions suivantes :
* Quelles routes menant à Larkana sont bloquées, et à quels endroits précis sont-elles bloquées ?
* Existe-t-il des ponts permettant de traverser depuis le côté est de l’Indus vers le côté ouest, et où ces ponts se trouvent-ils ?
* Si le transport des fournitures par route vers la région n’est pas possible, quelle autre méthode pourrait être utilisée pour acheminer les fournitures ?

Afin d’avoir une vue plus claire, nous devons importer dans QGIS les données du réseau routier de la région. Recherchez le fichier dans le dossier input. Le réseau routier s’affiche initialement sans montrer les types de routes ni d’autres détails pertinents. Nous devrions appliquer une technique de classification catégorisée afin de n’afficher que les routes spécifiques qui nous intéressent.
::::

1. Chargez le jeu de données __"Roads_Larkana.gpkg"__ depuis votre dossier input dans QGIS.
2. Pour la classification catégorisée, faites un clic droit sur la couche __"Roads_Larkana"__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section d’onglets verticale à gauche. Accédez à l’onglet `Symbology` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)).
    * En haut, vous trouverez un menu déroulant. Ouvrez-le et choisissez `Categorized`. Sous `Value`, sélectionnez "highway".
    * Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir toutes les valeurs ou attributs uniques de la colonne sélectionnée "highway". Vous pouvez ajuster les couleurs en double-cliquant sur les couleurs dans chaque ligne du champ central.
    * Décochez toutes les catégories sauf : `motorway`, `primary`, `secondary`, `trunk`.
    ```{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    La fenêtre de symbolisation pour la couche Roads_Larkana.gpkg.
    ```
    * Vous avez la possibilité de personnaliser la largeur des lignes des routes principales afin d’améliorer la visualisation. Ouvrez la fenêtre Symbology, puis sélectionnez `Symbol`. Dans la nouvelle fenêtre, vous pouvez ajuster la largeur des lignes selon vos préférences.
    
    ```{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Ajustement de la symbolisation des différents types de routes.
    ```

    * Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.

::::{margin}
:::{tip}

Il existe des méthodes pour automatiser le processus de numérisation, qui seront abordées dans le [module 5 : Opérations SIG intermédiaires](https://giscience.github.io/gis-training-resource-center/content/fr/Module_5/fr_module_5_overview.html).
:::
::::

3. Pour simplifier le processus, nous allons rechercher visuellement les routes bloquées et les marquer avec des points. À cette fin, nous créerons un tout nouveau jeu de données ponctuelles représentant les routes bloquées.
    * Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitalization_wiki.html#create-a-new-layer)). 
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) et naviguez jusqu’au dossier `temp`. Donnez au nouveau jeu de données le nom __“PAK_flood_2024_blocked_road”__. Cliquez sur `Save`.
    - `Geometry type` : sélectionnez `Point`
    - Sous `Additional dimension`, assurez-vous toujours que l’option `None` est cochée. 
    - Sélectionnez le système de coordonnées de référence (CRS) "EPSG:4326-WGS 84". Par défaut, QGIS sélectionne le CRS du projet. 
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type` : sélectionnez `Text Data`
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Créez un autre champ avec le `name` __"Blocked_bridge"__ et le `Type` : sélectionnez `Text Data`.
        * Cliquez sur `OK`.
    * Votre nouvelle couche apparaîtra dans le `Layer Panel`.

    ```{figure} /fig/PAK_blocked_road_new_layer.png
    ---
    width: 400px
    name: Pakistan road classification
    align: center
    ---
    Création d’une nouvelle couche de points. Assurez-vous de spécifier un emplacement à l’aide des trois points en haut.
    ```

::::{margin}
:::{tip}
Si vous ne voyez pas la barre d’outils, cliquez sur l’onglet `View` → `Toolbars` et cochez `Digitizing Toolbar` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_digitalization_wiki.md#creation-of-point-data)).
:::
::::

4. Vous pouvez maintenant créer un point pour chaque endroit où la couche des inondations recouvre les routes principales menant hors de Larkana [wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitalization_wiki.html#creation-of-point-data). 
    * Actuellement, la nouvelle couche __“PAK_flood_2024_blocked_road”__ est vide. Pour ajouter des entités, nous pouvons utiliser la `Digitizing Toolbar`. ![](/fig/Digitizing_Toolbar.png) 
    * Activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png). Ensuite, activez l’option d’ajout de nouveaux points en cliquant sur ![](/fig/mActionCapturePoint.png) `Add Point Feature`.
    * Repérez les endroits où la couche d’inondation recouvre les routes principales ou les ponts menant hors de Larkana. Une fois que vous en avez trouvé un, faites un clic gauche sur l’emplacement que vous souhaitez numériser.
    * Une fois que vous cliquez sur un endroit, une fenêtre apparaîtra. Indiquez que la route est bloquée en écrivant `Yes` dans le champ `Blocked_road`.
    * Répétez cette étape pour tous les emplacements que vous pouvez trouver. 

    ```{figure} /fig/PAK_blocked_road_digitalise.png
    ---
    width: 400px
    name: Digitalising blocked roads
    align: center
    ---
    Cette fenêtre contextuelle s’ouvrira une fois que vous aurez sélectionné un emplacement pour ajouter un point. Assurez-vous de saisir les informations pertinentes dans les colonnes. 
    ```

    * Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    * Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

5. Nous avons maintenant cartographié toutes les principales routes d’accès bloquées vers Larkana. Nous pouvons utiliser des icônes au lieu de simples points pour afficher la couche __“PAK_flood_2024_blocked_road”__ afin de mieux visualiser cette information [wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_single_symbol_wiki.html).

    * Faites un clic droit sur la couche __“PAK_flood_2024_blocked_road”__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section d’onglets verticale à gauche. Accédez à l’onglet `Symbology`.
    * Conservez l’option `Single Symbol`. Sélectionnez n’importe quel symbole de la liste qui convient pour marquer les routes bloquées. 
    * Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.
    * Une fois terminé, cliquez sur l’icône ![](/fig/qgis_move_symbol.png) pour quitter le mode de sélection d’entités.

    ```{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visulsing blocked roads with icons
    align: center
    ---
    Ajustement de la symbolisation pour la nouvelle couche de points. Assurez-vous de choisir un marqueur facilement identifiable. 
    ```

Une partie de votre mission consistait à identifier des alternatives possibles au transport routier. Pouvez-vous en repérer une ?

:::{dropdown} __Réponse__

Au sud-ouest de la ville de Larkana, vous pouvez trouver [l’aéroport de Mohenjodaro](https://www.google.com/search?q=Larkana&rlz=1C1GCEA_enDE1048DE1048&oq=Larkana&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORjjAhiABDIHCAEQLhiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIGCAYQRRg9MgYIBxBFGD2oAgiwAgE&sourceid=chrome&ie=UTF-8#vhid=0x0:0xf59fc8243b2b9d0e&vssid=lclsmap&eim=CAEQDhoRMjcuMzI4NDM3NTc5NDIyNjIiETY4LjE0MjA5NTk3MDUzNTQ4KhQxNzY5OTA4NTExODUyNjQzMDQ3OA). Actuellement, la route reliant la ville de Larkana à l’aéroport semble ouverte et praticable. Cela signifie que des fournitures essentielles pourraient potentiellement être acheminées depuis l’aéroport vers la ville sans rencontrer de blocages routiers. 

```{figure} /fig/PAK_road_access_airport.png
---
width: 600px
name: Road access to Mohenjodaro Airport
align: center
---
Accès routier à l’aéroport de Mohenjodaro.
```
:::

:::{card} 

L’équipe des opérations dispose maintenant de toutes les informations nécessaires pour planifier sa logistique. Bon travail !

:::


:::{admonition} Poursuivez cet exercice
:class: note

```{figure} /fig/IFRC-icons-colour_Map.png
---
width: 100px
align: right
name: IFRC map icon
---
```

Cet exercice fait partie du __parcours d’exercices sur la réponse aux inondations à Larkana__ et se poursuit avec un exercice du module 4.

Cliquez [ici](https://giscience.github.io/gis-training-resource-center/content/fr/Module_4/fr_qgis_map_design_I_ex4.html) si vous souhaitez passer à l’exercice suivant de ce parcours.

:::
