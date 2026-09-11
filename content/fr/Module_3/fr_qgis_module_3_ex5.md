::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 5 : Réponse aux inondations à Larkana <a id="exercise-5-larkana-flood-response"></a>

::::{grid} 2
:::{grid-item-card}
__Parcours d’exercices sur la réponse aux inondations à Larkana :__
^^^

Cet exercice est le troisième exercice du [parcours d’exercices sur la réponse aux inondations à Larkana](https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/fr_larkana_flood_response.html).

- [Exercice précédent](https://giscience.github.io/gis-training-resource-center/content/Module_2/fr_qgis_data_sources_ex4.html)
- [Exercice suivant](https://giscience.github.io/gis-training-resource-center/content/Module_4/fr_qgis_map_design_I_ex4.html)
:::

:::{grid-item-card}
__Compétences couvertes dans cet exercice__
^^^ 

- Sélectionner des entités et exporter vers un nouveau fichier
- Extract by Location
- Reproject Layer
- Modifier la table attributaire
- Classification
- Numériser une couche de points

:::
::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé nécessaire pour l’exercice__
^^^

- L’exercice prend environ 3 heures à réaliser, en fonction du nombre de participants et de leur familiarité avec les systèmes informatiques.

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
* [Numérisation - Données ponctuelles](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#add-geometries-to-a-layer)
:::
::::

:::{topic} Objectif de l’exercice

En 2024, les provinces du Pendjab, du Sindh et du Baloutchistan au Pakistan ont subi des inondations dévastatrices dues à des précipitations intenses et prolongées. En conséquence, des infrastructures critiques, telles que les établissements de santé, ont été affectées et l’accès routier à la ville de Larkana a été sévèrement limité. Les exercices suivants utiliseront des données réelles issues de cette catastrophe naturelle. L’objectif est d’identifier précisément les centres médicaux et les établissements de santé qui ont été affectés par les inondations. De plus, nous évaluerons la viabilité de l’accès routier à la ville de Larkana au 12 août 2024.

Les participants travailleront avec plusieurs couches et effectueront des requêtes spatiales. De plus, ils apprendront à créer leurs propres géodonnées. L’exercice est divisé en trois tâches. Dans la première partie, nous exporterons les limites administratives dans notre zone d’intérêt (AOI). Dans la deuxième tâche, les établissements de santé situés dans notre AOI seront extraits et nous identifierons quels établissements de santé sont situés à l’intérieur de la couche d’étendue des inondations. Dans la troisième tâche, l’accès routier sera déterminé en identifiant quelles routes sont potentiellement inondées. 
:::

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

## Données disponibles <a id="available-data"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood.zip

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood.zip), enregistrez le dossier sur votre ordinateur et décompressez le fichier.__

:::


| Jeu de données | Titre original | Éditeur | Téléchargé depuis | 
| :-------------------- | :----------------- |:----------------- |:----------------- |
| PAK_Sindh_adm1.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) | UN OCHA | HDX |
| PAK_Sindh_adm2.gpkg | [Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-pak) | UN OCHA | HDX |
| PAK_Sind_Health_Facilities.gpkg |  [Pakistan Health Facilities (OpenStreetMap Export)](https://data.humdata.org/dataset/hotosm_pak_health_facilities) |Humanitarian OpenStreetMap Team (HOT) | HDX |
| VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp | [Satellite detected water extents from 08 to 12 August 2024 over Pakistan)](https://data.humdata.org/dataset/satellite-detected-water-extents-from-08-to-12-august-2024-over-pakistan) | UNO SAT | HDX |
| Roads_Larkana.gpkg | [Roads Larkana](https://export.hotosm.org/v3/exports/7f1e78c7-f671-41e3-9ec3-6fc6ac31c929) |Humanitarian OpenStreetMap Team | HOT Export Tool (export créé en septembre 2024) |

<!--ADD: Add an explanation how to create the healthsite dataset by combining points and polygons -->

:::{hint}

La couche d’étendue des inondations reprojetée et corrigée peut être téléchargée __[ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_5/Module_3_Exercise_5_Larkana_Flood_Day2.zip)__

:::

:::{hint} Structure des dossiers
Pour garder vos données organisées et facilement accessibles, il est important de mettre en place une structure de dossiers claire sur votre ordinateur pour vos projets QGIS et vos géodonnées. Assurez-vous que les données de l’exercice sont enregistrées dans un emplacement permettant une récupération facile et une association avec le projet QGIS correspondant.
:::


<!---
:::{figure} /fig/M3_Ex5_workflow_chart.drawio.png
---
name: M5_Ex5_Workflow_chart
width: 450 px
---
:::
-->

## Tâche 1 : Obtenir une vue d’ensemble de la situation autour de Larkana <a id="task-1-gain-an-overview-of-the-situation-around-larkana"></a>

::::{card} 
__Contexte__
^^^

:::{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
:::

Vous avez été déployé en tant que gestionnaire de l’information dans les régions du Pakistan touchées par les inondations. À votre arrivée, vous avez reçu des rapports de l’équipe opérationnelle indiquant que la ville de [Larkana](https://www.openstreetmap.org/#map=12/27.5565/68.1672) et ses environs ont été gravement affectés par les inondations. L’équipe a besoin d’une vue d’ensemble générale de l’emplacement de la ville.

::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_1.png
---
name: Task_1_workflow
width: 750 px
---

:::

::::{margin}
:::{admonition} Astuce
:class: note
Vous ne pouvez pas interagir avec un fond de carte !
:::
::::

1. Ouvrez QGIS et créez un [nouveau projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`.
2. Une fois le projet créé, [enregistrez le projet](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#save) dans le dossier de l’exercice "Module_3_Exercise_2_Flood_Larkana". Pour cela, cliquez sur `Project` → `Save as` et naviguez jusqu’au dossier. Nommez le projet "PAK_Larkana_flood_2024".
3. Tout d’abord, nous voulons ajouter OpenStreetMap comme fond de carte pour l’orientation. Pour ajouter OSM comme fond de carte, cliquez sur `Layer` → `Add Layer` → `Add XYZ Layer…`. Choisissez `OpenStreetMap` et cliquez sur `Add`. 
4. Ensuite, chargez le GeoPackage __"PAK_Sindh_adm2.gpkg"__ dans votre projet par glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu’à __"PAK_Sindh_adm2.gpkg"__. Sélectionnez le fichier et cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).


:::{Attention}
Les fichiers GeoPackage peuvent contenir plusieurs fichiers et même des projets QGIS entiers. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers que vous souhaitez charger dans votre projet QGIS.
:::

5. Pour obtenir une vue d’ensemble de la situation, nous voulons exporter les limites administratives de notre zone d’intérêt (AOI). Pour ce faire, nous voulons exporter le district __Larkana__, ainsi que les districts voisins depuis la couche `PAK_adm2_Sindh`. 
    - <kbd>Clic droit</kbd> sur la couche `PAK_adm2_Sindh` et sélectionnez [Open Attribute table](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html).
    - Trouvez la colonne `ADM2_EN` puis trouvez la ligne correspondant au district de Larkana.
    - <kbd>Cliquez</kbd> sur les numéros tout à gauche de la fenêtre de la table attributaire pour sélectionner l’entité Larkana. La ligne apparaîtra en bleu et la zone de Larkana deviendra jaune dans le canevas cartographique. 
    - <kbd>Cliquez</kbd> sur `Zoom Map to selected rows` dans la barre supérieure de la fenêtre de la table attributaire. ![](/fig/qgis_3.36_zoom_to_selected_rows_at.png).
    - Fermez la table attributaire. 
    ::::{margin}
    :::{tip}
    Maintenir <kbd>Ctrl</kbd> pendant la sélection d’entités vous permet d’ajouter d’autres entités à votre sélection actuelle. Sinon, vous désélectionnerez le polygone précédent. 
    Gardez à l’esprit que vous ne pouvez sélectionner des entités que dans la couche actuellement sélectionnée dans le panneau des couches. 
    ::::
    - Dans la barre d’outils en haut de la fenêtre QGIS, sélectionnez l’outil `Select Feature(s)` ![](/fig/selection_toolbar_feature_selection.png). Maintenez <kbd>Ctrl</kbd> et <kbd>Cliquez</kbd> sur les districts entourant le district de Larkana ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html#manual-selection)). Les six districts sélectionnés devraient apparaître en jaune sur votre canevas cartographique. 
    <!--FIX: The districts named are not the only ones surrounding the -->
    - Désactivez l’outil `Select Feature(s)` en cliquant sur l’icône ![](/fig/qgis_move_symbol.png) dans la barre d’outils en haut de votre fenêtre QGIS. 
    - Nous pouvons maintenant exporter les entités sélectionnées et les enregistrer dans un nouveau fichier. Faites un clic droit sur la couche `PAK_adm2_Sindh` puis sélectionnez `Export` → `Save Selected Features as`. 
    - Une nouvelle fenêtre s’ouvrira. Ici, vous pouvez choisir comment et où les entités sélectionnées sont enregistrées. 
    :::{figure} /fig/en_qgis_3.36_m3_ex5_export_features.png
    ---
    name: m3_ex5_export_selection
    width: 450 px
    ---
    Assurez-vous d’enregistrer le geopackage au bon emplacement en cliquant sur les trois points à droite du champ `File name`.
    :::
    - Sous `Format`, sélectionnez geopackage.
    - À droite du champ `File name`, cliquez sur les trois points. Naviguez jusqu’au dossier contenant les données de l’exercice et enregistrez-le dans le dossier `data/temp/`. 
    - Saisissez un nom de couche. Par exemple, "__Flood_2024_AOI__". 
    - Cliquez sur `OK`. La couche exportée devrait apparaître dans votre panneau des couches. 
     
::::{margin}
:::{Tip}
N’oubliez pas d’enregistrer votre projet de temps en temps !
:::
::::

:::{topic} Résultat

Vous disposez maintenant d’une vue d’ensemble de l’emplacement du district de Larkana dans le Sindh. L’équipe opérationnelle peut utiliser cette information. 

:::



## Tâche 2 : Estimation de l’impact des inondations sur le secteur de la santé à Larkana <a id="task-2-estimation-of-flood-impact-on-the-health-sector-in-larkana"></a>

::::{card} 
__Contexte__
^^^

:::{figure} /fig/IFRC-icons-colour_Health.svg
---
width: 100px
align: right
name: IFRC HEalth Icon
---
:::

Des publications sur les réseaux sociaux ont indiqué un impact significatif sur le système de santé dans la région. Vous avez été chargé d’en apprendre autant que possible sur la situation et, si possible, d’estimer l’impact sur le système de santé.

::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_2.png
---
name: task_2_workflow
width: 750 px
---

:::

1. Tout d’abord, nous devons identifier où se trouvent les établissements de santé dans la zone. Nous pouvons trouver des jeux de données en effectuant une recherche rapide sur le [Humanitarian Data Exchange (HDX)](https://data.humdata.org). Vous pouvez y trouver le jeu de données "Pakistan Health Facilities (OpenStreetMap Export)". Nous utiliserons ce jeu de données. Il est déjà disponible dans le dossier de téléchargement de cet exercice. 
    - Importez le GeoPackage `PAK_Health_Facilities_complete.gpgk` dans votre projet. Vous pouvez soit le glisser sur le canevas cartographique, soit ouvrir la fenêtre d’importation en cliquant sur `Layer` → `Add Layer` → `Add Vector Layer` dans la barre supérieure de QGIS ([voir la page wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html)). Une nouvelle couche de données ponctuelles apparaîtra sur votre canevas cartographique. 
    - Une fois les établissements de santé importés, nous pouvons extraire ceux qui sont situés à l’intérieur de notre zone d’intérêt. Nous pouvons y parvenir avec l’outil `Extract by Location`. 
    - Dans la __Processing Toolbox__ ([ouvrir la toolbox](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)), recherchez l’outil "Extract by Location". <kbd>Double-cliquez</kbd> dessus. Une nouvelle fenêtre s’ouvrira.
    :::{figure} /fig/PAK_extract_locatio_HS.png
    ---
    width: 400px
    name: Extract by location Pakistan
    align: center
    ---
    Extraction des établissements de santé dans notre zone d’intérêt à l’aide de l’outil "Extract by Location". 
    :::
    - Comme `Input Layer`, sélectionnez la couche `PAK_Health_Facilities_complete`. 
    - Le `Geometric predicate` doit être défini sur `Intersect`.
    - Sous `By comparing to the features from`, sélectionnez la couche de zone d’intérêt "__Flood_2024_AOI__".
    - Sous `Extracted (location)`, cliquez sur les trois points puis sélectionnez `Save to Geopackage`. 
    - Naviguez jusqu’au dossier `/Module_3_Exercise_5_Larkana_Flood/data/temp/`.
    - Donnez au fichier le nom __“Health_Facilities_Flood_2024_AOI”__ puis cliquez sur `Save`.
    - Il vous sera demandé de saisir un nom de couche. Donnez-lui le même nom que le fichier puis cliquez sur `OK`. 
    - Cliquez sur `Run`. La nouvelle couche apparaîtra dans votre panneau des couches.


Nous avons maintenant une vue d’ensemble de l’emplacement des établissements de santé. Cependant, nous voulons savoir quels établissements de santé sont affectés par les inondations. Heureusement, l’ONU vient de partager un jeu de données sur l’étendue des inondations du 8 au 12 août, que nous pouvons superposer à notre couche contenant les établissements de santé afin d’identifier ceux qui se trouvent dans la zone inondée.

2. Importez le jeu de données __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__ dans votre projet QGIS.
3. Une fois les couches chargées dans QGIS, vous pouvez voir qu’elles s’affichent correctement. Cependant, en vérifiant les informations de la couche, vous pouvez voir que les nouvelles couches ont un système de coordonnées de référence (CRS) différent. Elles ont le code EPSG 9707 alors que notre projet a 4326 ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#how-to-check-epsg-code-crs-of-your-qgis-project-and-change-it)).
    * <kbd>Clic droit</kbd> sur la couche puis sélectionnez `Properties`. La fenêtre des propriétés s’ouvrira.
    - Dans la barre d’onglets verticale à gauche, naviguez jusqu’à `Information`. Vous y trouverez des informations supplémentaires sur le jeu de données sélectionné. 
    * Sous l’intitulé "Coordinate Reference System (CRS)", vous pouvez trouver toutes les informations concernant le CRS. Les plus importantes sont :
    - __Name:__     Ici, vous trouvez le code EPSG.
    - __Units:__    Ici, vous trouvez des informations sur les unités de mesure utilisées dans le jeu de données, par exemple des mètres ou des degrés. <!--ADD: Why is it a problem? Add explanation-->
4. Cela deviendra un problème dès que nous ferons autre chose que simplement afficher les couches. Puisque nous voulons manipuler les couches à l’étape suivante, nous devons d’abord les reprojeter ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projections_wiki.html#changing-the-projection-of-a-vector-layer)). 
    * En haut de votre fenêtre QGIS, </kbd>cliquez</kbd> sur l’onglet `Vector` → `Data Management Tools` → `Reproject Layer`, ou recherchez l’outil dans la `Processing Toolbox`.
    * Comme `Input layer`, sélectionnez __"VIIRS_20240721_20240803_MinimumFloodExtent_PAK.shp"__.
    * Sélectionnez comme CRS cible / code EPSG __4326__.
    * Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png) à côté de `Reprojected`, indiquez le nom du fichier comme __"2024_MinFloodExtend_reprojected"__.
    * Cliquez sur `Run`.
    * Supprimez l’ancienne couche du panneau des couches en faisant un clic droit sur la couche → `Remove layer`.
    * Ajustez l’opacité de la couche d’inondation en faisant un clic droit sur la couche __"2024_MinFloodExtend_reprojected"__ dans le panneau des couches puis en sélectionnant `Properties`. La fenêtre des propriétés s’ouvrira avec une section verticale d’onglets sur la gauche. 
    - Naviguez jusqu’à l’onglet `Symbology`.
    - Ajustez l’opacité à environ 60 % en déplaçant le curseur.

<!--Symbology tab has not been covered in the modules yet.-->

Nous avons observé que certains établissements de santé ont été touchés par les inondations. Afin de visualiser cette information sur la carte, nous prévoyons d’inclure un nouvel attribut appelé __"Flood_affected"__ dans la table attributaire de __"Health_Facilities_Flood_2024_AOI"__. Pour ce faire, nous allons sélectionner tous les établissements de santé qui se trouvent à l’intérieur de l’étendue des inondations en utilisant l’outil "Select by Location". Dans une étape suivante, nous ajouterons une nouvelle colonne à la table attributaire et ajouterons des informations à nos établissements de santé sélectionnés. 

5. Ouvrez la `Processing Toolbox` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox)) et recherchez l’outil __"Select by Location"__.
    * `Select features from` = __"Health_Facilities_Flood_2024_AOI"__.
    * Comme `Geometric predicate`, nous utilisons `intersect`.
    * Pour `By comparing to the features from`, nous utilisons la couche __"2024_MinFloodExtent_reprojected"__.
    * `Modify current selection by` = `creating new selection`.
    * Cliquez sur `Run`.

:::{figure} /fig/PAK_flood_select_by_location.PNG
---
width: 400px
name: Select flood affected health facilities
align: center
---
Sélection des établissements de santé affectés par les inondations à l’aide de l’outil "Select by Location".
:::

::::{admonition} Message d’erreur possible
:class: warning, dropdown
Dans le cas où vous rencontreriez l’erreur suivante :

```
Feature (1) from “2024_MinFloodExtend_reprojected” has invalid geometry. 
Please fix the geometry or change the Processing setting to the “Ignore 
invalid input features” option.
Execution failed after 0.07 seconds
```

Vous devez d’abord utiliser l’outil __"Fix Geometry"__ avant de répéter l’étape 5 précédemment échouée avec l’outil __"Select by Location"__.

* Pour ce faire, ouvrez la [`Processing Toolbox`](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#open-toolbox) et recherchez l’outil __"Fix Geometries"__.
* `Input layer` = `2024_MinFloodExtend_reprojected`
* Enregistrez le nouveau fichier dans votre dossier `temp` en cliquant sur les trois points ![](/fig/Three_points.png), indiquez le nom du fichier comme __"2024_MinFloodExtend_reprojected_fix"__.
* Cliquez sur `Run`.

:::{figure} /fig/ PAK_flood_ngeomertrie_error.PNG
---
width: 400px
name: Fix Geometry
align: center
---
Le message d’erreur indiquant des géométries invalides.
:::

::::

6. Nous pouvons modifier la table attributaire pour les entités que nous avons sélectionnées :
    - Ouvrez la table attributaire de __"Health_Facilities_Flood_2024_AOI"__ en faisant un clic droit sur la couche → `Open Attribute Table` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html)).
    - Activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)). Vous pouvez maintenant modifier directement les données dans la table.
    - Nous voulons ajouter une nouvelle colonne portant le nom __"Flood_affected"__ pour identifier quels établissements de santé sont situés à l’intérieur de l’étendue des inondations. Cliquez sur ![](/fig/mActionNewAttribute.png). Une nouvelle fenêtre s’ouvrira.
    - Dans la fenêtre `Add field`, ajoutez le nom de la colonne et définissez le `Type` sur `Text (string)` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#add-new-column)). 
    - Cliquez sur `OK`. 


:::{figure} /fig/ PAK_flood_new_column.PNG
---
width: 300px
name: New column Pakistan
align: center
---
Ajout d’une nouvelle colonne à la table attributaire pour la couche des établissements de santé.
:::

7. Ensuite, nous voulons modifier les lignes de la table attributaire correspondant aux entités que nous avons sélectionnées. 
    - Recherchez l’option `Show all Features` dans le coin inférieur gauche et cliquez dessus.
    - Sélectionnez l’option `Show selected features` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#manually-select-features-in-the-attribute-table)). Cela filtrera la table pour n’afficher que les lignes représentant les établissements de santé directement touchés par les inondations.
    - Écrivez `Yes` dans la colonne __"Flood_affected"__ pour chaque ligne sélectionnée. 
    - Une fois terminé, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications et désactivez le mode édition en cliquant de nouveau sur ![](/fig/mActionToggleEditing.png) ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_attribute_table_wiki.html#change-data-in-the-attribute-table)).
    - Cliquez sur l’icône ![](/fig/selection_toolbar_feature_deselection.png) dans la barre d’outils pour terminer la sélection des entités.

8. Nous pouvons afficher le jeu de données enrichi en le visualisant avec la méthode de symbolisation par classification catégorisée. Cela signifie que nous sélectionnons une colonne de la table attributaire et utilisons les valeurs / contenus comme catégories pour trier et afficher les données ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)) :
    - Dans le panneau des couches, faites un clic droit sur la couche __"Health_Facilities_Flood_2024_AOI"__ puis sélectionnez `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche.
    - Naviguez jusqu’à l’onglet `Symbology`.
    - En haut de la fenêtre, il y a un menu déroulant. Ouvrez-le puis choisissez `Categorized`.
    - Sous `Value`, sélectionnez la colonne que nous avons ajoutée, "Flood_affected".
    - Plus bas dans la fenêtre, cliquez sur `Classify`. Les valeurs uniques de la colonne "Flood_affected" devraient apparaître.
    - Vous pouvez ajuster la symbolisation et la couleur de chaque valeur en double-cliquant sur chaque couleur dans le tableau. 
    - Une fois les couleurs ajustées, cliquez sur `Apply`, puis sur `OK` pour fermer la fenêtre de symbolisation.  

:::{figure} /fig/en_qgis_categorized_classification_Pakistan_flood_exercise.png
---
width: 600px
name: Flood affected health facilities classification
align: center
---
Classification des établissements de santé affectés par les inondations.
:::

:::{card} 
__Résultat :__
^^^

Nous avons identifié précisément les établissements de santé qui ont été inondés par les crues. Nos résultats indiquent qu’un total de quatre établissements ont été complètement inondés et sont actuellement non opérationnels. Étant donné que nous avons évalué l’impact minimal des inondations, il est très probable que davantage d’établissements de santé soient également affectés. Ces données sont cruciales pour notre équipe opérationnelle car elles lui permettront de planifier et d’exécuter une réponse efficace.

:::

## Tâche 3 : Accès logistique à la ville de Larkana <a id="task-3-logistical-access-to-larkana-city"></a>

::::{card}
__Contexte__
^^^

:::{figure} /fig/IFRC-icons-colour_Logistics.svg
---
width: 100px
align: right
name: IFRC Logistics Icon
---
:::

L’équipe opérationnelle prépare des plans pour acheminer des fournitures indispensables vers la région touchée autour de Larkana. À l’heure actuelle, il existe une incertitude quant à la manière dont ces fournitures peuvent y être transportées. L’équipe opérationnelle a demandé davantage d’informations à ce sujet.

Elle a besoin de réponses aux trois questions suivantes :
* Quelles routes menant à Larkana sont bloquées, et à quels emplacements précis sont-elles bloquées ?
* Existe-t-il des ponts permettant de traverser depuis le côté est de l’Indus vers le côté ouest, et où ces ponts sont-ils situés ?
* Si le transport de fournitures par route vers la région n’est pas réalisable, quelle autre méthode pourrait être utilisée pour acheminer les fournitures ?

Afin d’obtenir une image plus claire, nous devons importer les données du réseau routier de la région dans QGIS. Recherchez le fichier dans le dossier input. Le réseau routier est initialement affiché sans montrer les types de routes ni d’autres détails pertinents. Nous devrions appliquer une technique de classification catégorisée afin d’afficher uniquement les routes spécifiques qui nous intéressent.
::::

:::{figure} /fig/Module_3/en_m3_ex5_Task_3.png
---
name: Task_3_workflow
width: 750 px
---

:::


1. Chargez le jeu de données __"Roads_Larkana.gpkg"__ depuis votre dossier input dans votre projet QGIS.
2. Mettons en place la classification catégorisée. Les données OpenStreetMap distinguent différents types de routes à l’aide de la colonne "highway". 
    - Faites un clic droit sur la couche __"Roads_Larkana"__ puis sélectionnez `Properties`. La fenêtre des propriétés s’ouvrira. 
    - Naviguez jusqu’à l’onglet `Symbology`.
    - En haut, sélectionnez `Categorized` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_categorized_wiki.html)).
    - Sous `Value`, sélectionnez "highway".
    - Cliquez sur `Classify`. Vous devriez voir toutes les valeurs uniques de la colonne "highway". 
    - Supprimez les coches pour toutes les catégories sauf `motorway`, `primary`, `secondary` et `trunk`.
    - Vous pouvez ajuster les couleurs en double-cliquant sur les catégories. 
    :::{figure} /fig/PAK_road_classification.PNG
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    La fenêtre de symbolisation pour la couche Roads_Larkana.gpkg.
    :::
    - Vous avez la possibilité de personnaliser l’épaisseur des lignes des routes principales afin d’améliorer la visualisation. Ouvrez la fenêtre de symbologie, puis sélectionnez `Symbol`. Dans la nouvelle fenêtre, vous pouvez ajuster l’épaisseur des lignes selon vos préférences.
    :::{figure} /fig/PAK_road_symbol_weight.png
    ---
    width: 600px
    name: Pakistan road classification
    align: center
    ---
    Ajustement de la symbolisation des différents types de routes.
    :::
    - Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.

::::{margin}
:::{tip}
Il existe des méthodes pour automatiser le processus de numérisation, qui seront abordées dans le [module 5 : Opérations SIG intermédiaires](https://giscience.github.io/gis-training-resource-center/content/Module_5/fr_module_5_overview.html).
:::
::::

3. Enfin, nous voulons visualiser les routes qui sont inondées. Pour simplifier le processus, nous allons rechercher manuellement les routes qui intersectent la couche d’étendue des inondations et les marquer avec des points. Pour cela, nous créerons un nouveau jeu de données ponctuelles représentant les routes bloquées. 
    * Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#create-a-new-layer)) 
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) puis naviguez jusqu’au dossier `temp`. Donnez au nouveau jeu de données le nom __“PAK_flood_2024_blocked_road”__. Cliquez sur `Save`.
    - `Geometry type`: sélectionnez `Point`
    - Sous `Additional dimension`, vous devez toujours vous assurer que `None` est coché. 
    - Sélectionnez le système de coordonnées de référence (CRS) "EPSG:4326-WGS 84". Par défaut, QGIS sélectionne le CRS du projet. 
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne __“Blocked_road”__.
        * `Name` = __“Blocked_road”__
        * `Type`: sélectionnez `Text(string)`.
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Créez un autre champ avec le `name` __"Blocked_bridge"__ et le `Type`: sélectionnez `Text(string)`.
        * Cliquez sur `OK`.
    * Votre nouvelle couche apparaîtra dans le panneau des couches.
    :::{figure} /fig/PAK_blocked_road_new_layer.png
    ---
    width: 400px
    name: Pakistan road classification
    align: center
    ---
    Création d’une nouvelle couche de points. Assurez-vous de spécifier un emplacement en utilisant les trois points en haut.
    :::

::::{margin}
:::{tip}
Si vous ne voyez pas la barre d’outils, cliquez sur l’onglet `View` → `Toolbars` et cochez `Digitizing Toolbar` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#creation-of-point-data)).
:::
::::

4. Vous pouvez maintenant créer un point pour chaque endroit où la couche d’inondation recouvre les routes principales quittant Larkana ([Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_digitisation_wiki.html#creation-of-point-data)). 
    * Actuellement, la nouvelle couche __“PAK_flood_2024_blocked_road”__ est vide. Pour ajouter des entités, nous pouvons utiliser la `Digitizing Toolbar`. ![](/fig/Digitizing_Toolbar.png) 
    * Activez le mode édition en cliquant sur ![](/fig/mActionToggleEditing.png). Ensuite, activez l’option d’ajout de nouveaux points en cliquant sur ![](/fig/mActionCapturePoint.png) `Add Point Feature`.
    * Recherchez les endroits où la couche d’inondation recouvre les routes principales ou les ponts quittant Larkana. Une fois que vous en avez trouvé un, faites un clic gauche sur l’emplacement que vous souhaitez numériser.
    * Une fois que vous cliquez sur un endroit, une fenêtre apparaîtra. Indiquez que la route est bloquée en écrivant `Yes` dans le champ `Blocked_road`.
    * Répétez cette étape pour tous les emplacements que vous pouvez trouver. 

    :::{figure} /fig/PAK_blocked_road_digitalise.png
    ---
    width: 400px
    name: Digitising blocked roads
    align: center
    ---
    Cette fenêtre contextuelle s’ouvrira une fois que vous aurez sélectionné un emplacement pour ajouter un point. Assurez-vous de saisir les informations pertinentes dans les colonnes. 
    :::

    * Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    * Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

5. Nous avons maintenant cartographié toutes les principales routes d’accès bloquées vers Larkana. Nous pouvons utiliser des icônes au lieu de simples points pour afficher la couche __“PAK_flood_2024_blocked_road”__ afin de mieux visualiser ce fait ([Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_single_symbol_wiki.html)).

    * Faites un clic droit sur la couche __“PAK_flood_2024_blocked_road”__ dans le panneau des couches puis cliquez sur `Properties`. Une nouvelle fenêtre s’ouvrira avec une section verticale d’onglets sur la gauche. Naviguez jusqu’à l’onglet `Symbology`.
    * Conservez l’option `Single Symbol`. Sélectionnez n’importe quel symbole de la liste qui convient pour marquer les routes bloquées. 
    * Une fois terminé, cliquez sur `Apply` puis sur `OK` pour fermer la fenêtre de symbologie.
    * Une fois terminé, cliquez sur l’icône ![](/fig/qgis_move_symbol.png) pour terminer le mode de sélection d’entités.

    :::{figure} /fig/PAK_blocked_road_symbol.png
    ---
    width: 600px
    name: Visualising blocked roads with icons
    align: center
    ---
    Ajustement de la symbolisation pour la nouvelle couche de points. Assurez-vous de choisir un marqueur facilement identifiable. 
    :::

Une partie de votre mission consistait à indiquer des alternatives possibles au transport routier. Pouvez-vous en identifier une ?

::::{dropdown} __Réponse__

Dans le sud-ouest de la ville de Larkan, vous pouvez trouver [l’aéroport de Mohenjodaro](https://www.google.com/search?q=Larkana&rlz=1C1GCEA_enDE1048DE1048&oq=Larkana&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORjjAhiABDIHCAEQLhiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIGCAYQRRg9MgYIBxBFGD2oAgiwAgE&sourceid=chrome&ie=UTF-8#vhid=0x0:0xf59fc8243b2b9d0e&vssid=lclsmap&eim=CAEQDhoRMjcuMzI4NDM3NTc5NDIyNjIiETY4LjE0MjA5NTk3MDUzNTQ4KhQxNzY5OTA4NTExODUyNjQzMDQ3OA). Actuellement, la route reliant la ville de Larkana à l’aéroport semble être ouverte et accessible. Cela signifie que des fournitures essentielles pourraient potentiellement être transportées depuis l’aéroport vers la ville sans rencontrer de blocages routiers. 

:::{figure} /fig/PAK_road_access_airport.png
---
width: 600px
name: Road access to Mohenjodaro Airport
align: center
---
Accès routier à l’aéroport de Mohenjodaro
:::
::::

:::{card} 

L’équipe opérationnelle dispose maintenant de toutes les informations dont elle a besoin pour planifier sa logistique. Bon travail ! 

:::


::::{admonition} Continue along this exercise track
:class: note

:::{figure} /fig/IFRC-icons-colour_Map.png
---
width: 100px
align: right
name: IFRC map icon
---
:::

Cet exercice fait partie du __parcours d’exercices sur la réponse aux inondations à Larkana__ et se poursuit avec un exercice du module 4.

Cliquez [ici](https://giscience.github.io/gis-training-resource-center/content/Module_4/fr_qgis_map_design_I_ex2.html) si vous souhaitez passer à l’exercice suivant de ce parcours d’exercices.

::::
