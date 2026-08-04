::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 5 : Le monde <a id="exercise-5-the-world"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Objectif de l’exercice :__
^^^

Cet exercice vous aidera à mieux vous familiariser avec l’interface de QGIS. En outre, vous chargerez vos premières données dans QGIS, vous acquerrez une première expérience pratique du concept de couche et vous apprendrez à reprojeter des couches.

:::

::::{grid} 2
:::{grid-item-card}
__Type d’exercice de formation :__
^^^

- Cet exercice peut être utilisé en formation en ligne ou en présentiel. 
- Il peut être réalisé en mode pas-à-pas ou individuellement en autoformation.

:::

:::{grid-item-card}
__Compétences couvertes par cet exercice :__
^^^
- Créer et enregistrer un nouveau projet QGIS
- Importer des données vectorielles (`.shp` et `.gpkg`) ainsi que des données tabulaires (`.txt`)
- Comprendre le concept de couche
- Naviguer dans l’interface de QGIS et dans le canevas cartographique

:::

::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice__
^^^
- L’exercice prend environ 30 minutes, selon le nombre de participant·e·s et de formateur·rice·s. 

:::

:::{grid-item-card}
__Articles wiki pertinents__
^^^

* [Interface QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html)
* [Types de données géographiques](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_geodata_types_wiki.html)
* [Import de données géographiques dans QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html)
* [Concept de couche](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_layer_concept_wiki.html)

:::

::::

## Instructions pour les formateur·rice·s <a id="instructions-for-the-trainers"></a>

:::{dropdown} __Espace formateur·rice__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. un tableau Miro) sur lequel les participant·e·s peuvent ajouter leurs remarques et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment animer des formations ?](https://giscience.github.io/gis-training-resource-center/content/fr/Trainers_corner/fr_how_to_training.html#how-to-do-trainings) pour quelques conseils généraux sur la conduite d’une formation.

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
:class-card: sd-text-center 
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Module_2_Exercise_5_The_World.zip

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Module_2_Exercise_5_The_World.zip), enregistrez le dossier sur votre ordinateur et décompressez-le.__ 

:::

Le dossier s’appelle “Module_2_Exercise_5_The_World” et contient l’ensemble de l’[arborescence de dossiers standard](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md#standard-folder-structure), avec toutes les données dans le dossier input et la documentation complémentaire dans le dossier documentation.

- [World Countries (Generalized)](https://hub.arcgis.com/datasets/2b93b06dc0dc4e809d3c8db5cb96ba69_0/explore) (Polygones / Shapefile)
- [Significant Earthquake Dataset](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ngdc.mgg.hazards:G012153) (CSV)
- [Global Power Plant Dataset](https://datasets.wri.org/dataset/globalpowerplantdatabase) (Points / GeoPackage)

## Tâches <a id="tasks"></a>

::::{margin}
:::{tip}
Veillez à __décompresser__ le dossier de l’exercice avant de commencer les tâches. Sinon, vous ne pourrez pas importer les jeux de données dans QGIS.
:::
::::

1. Ouvrez QGIS et créez un [nouveau projet](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Project` → `New`

2. Une fois le projet créé, enregistrez-le dans le sous-dossier `/Project` de `/Module_2_Exercise_5_The_World`/. Dans la barre supérieure, cliquez sur `Project` → `Save as` et accédez au dossier. Nommez le projet “Module_2_Ex_5_The_World”.

3. Chargez le shapefile `World_countries_generalized.shp` dans votre projet par glisser-déposer ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md#open-vector-data-via-drag-and-drop)). Ou cliquez sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et accédez à "World_countries__generalized". Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md#open-vector-data-via-layer-tab)).

    :::{Attention}
    Avec les deux méthodes, vous devez sélectionner le fichier portant l’extension `.shp` ! Un [shapefile est composé de plusieurs fichiers](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_qgis_geodata_concept.html#shapefile-structure) qui se référencent entre eux. Le fichier qui contient les informations géométriques est celui qui se termine par `.shp`.
    :::

4. Chargez le fichier GeoPackage `global_power_plant_database_nuclear.gpkg` dans le projet QGIS. Vous pouvez utiliser l’une des méthodes de l’étape précédente : soit glisser-déposer ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop)) le fichier, soit cliquer sur `Layer` → `Add Layer` → `Add Vector Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et accédez à `/data/input/`. Sélectionnez le fichier puis cliquez sur `Open`. De retour dans QGIS, cliquez sur `Add` ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-layer-tab)).

    :::{Note}
    Les fichiers GeoPackage peuvent contenir plusieurs fichiers, voire des projets QGIS complets. Lorsque vous chargez un tel fichier dans QGIS, une fenêtre apparaît dans laquelle vous devez sélectionner les fichiers à charger dans votre projet QGIS.
    :::

5. Nous voulons ensuite charger le fichier `Significant_earthquake_data.txt` dans QGIS. Comme il s’agit de données vectorielles au format texte, nous devons suivre des étapes spécifiques ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-csv-data-in-qgis)).
    * Cliquez sur `Layer` → `Add Layer` → `Add Delimited text Layer`. Cliquez sur les trois points ![](/fig/Three_points.png) et accédez à `Significant_earthquake_data.txt` dans le sous-dossier `data/input/`. Sélectionnez le fichier puis cliquez sur `Open`.
    * Dans la fenêtre "Data Source manager| Delimited Text" de QGIS, ouvrez le menu déroulant `File Format` et cochez `Custom delimiter` puis `Tab`.
    * Ouvrez le menu déroulant `Geometry definition`. Assurez-vous que l’option `Point coordinates` est cochée. Sélectionnez ensuite “LONGITUDE” pour le `X field` et “LATITUDE” pour le `Y field`.
    * Sélectionnez le système de coordonnées de référence (SCR) "EPSG:4326-WGS 84".
    * Cliquez sur `Add`.
    :::{Note}
    Lors du chargement de données vectorielles au format texte comme `.csv` ou `.txt` dans QGIS, ces données doivent comporter des colonnes de latitude et de longitude. 
    * `X field` = “LONGITUDE” 
    * `Y field` = “LATITUDE”.
    :::

    :::{figure} /fig/en_ex_The_world_add_text_layer_import.png
    ---
    width: 600px
    name: ex5_import_text_layer
    align: center
    ---
    :::

6. Dans le panneau des couches à gauche, organisez les trois couches dans un ordre logique. Rappelez-vous le [concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md). La couche des pays doit se trouver en dessous des couches des séismes et des centrales électriques.

:::{figure} /fig/Module_2/en_m2_ex_5_interface_explanation.png
---
name: en_m2_ex_5_interface_explanation
width: 750 px
---
:::

::::{margin}
:::{tip}
Vous pouvez également déplacer la carte en cliquant dans le canevas cartographique tout en maintenant <kbd>Space</kbd>. Cela active automatiquement l’outil main pendant que vous appuyez sur la barre d’espace. Faire défiler avec votre souris ou votre pavé tactile vous permet aussi de zoomer et dézoomer dans le canevas cartographique. Maintenir <kbd>Ctrl</kbd> sous Windows, ou <kbd>Cmd</kbd> sur MacOS, permet de zoomer par plus petits incréments.
:::
::::

7. Interagissez avec la carte et explorez les jeux de données. Utilisez l’outil de zoom et déplacez la carte. Où observe-t-on beaucoup de séismes et où se trouvent la plupart des centrales électriques ?

::::{margin}
:::{Tip}
Si vous voyez un `*` devant le nom de votre projet dans le coin supérieur gauche de QGIS, cela signifie qu’il existe des modifications non enregistrées dans votre projet. Enregistrez votre progression !
:::
::::

8. Enregistrez votre projet en cliquant sur ![](/fig/mActionFileSave.png) ou en utilisant le raccourci clavier <kbd>Ctrl</kbd> + <kbd>S</kbd>.

9. Votre résultat devrait ressembler à ceci :

:::{figure} /fig/en_ex_The_world_result.png
---
width: 600px
name: the_world_result
align: center
---
:::
