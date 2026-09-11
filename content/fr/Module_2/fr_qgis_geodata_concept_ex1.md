::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 1 : Comprendre les données géographiques <a id="exercise-1-understanding-geodata"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

:::{card}
__Objectif de cet exercice :__
^^^

L’objectif de cet exercice est de faire vos premiers pas dans QGIS. Comprendre l’interface utilisateur et se familiariser avec le concept de couche. Vous apprendrez à importer et afficher des données vectorielles dans QGIS et à ouvrir la table attributaire. En outre, nous apprendrons à reprojeter ou à modifier la projection des jeux de données vectoriels.
:::


::::{grid} 2
:::{grid-item-card}
__Type d’exercice de formation :__
^^^

- Cet exercice peut être utilisé en formation en ligne ou en présentiel. 
- Il peut être réalisé en mode pas-à-pas ou individuellement.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour :__ 
^^^

- Fondamentaux QGIS
- Comprendre les composantes spatiales des jeux de données
- Naviguer dans l’interface de QGIS
- Gérer et manipuler des données géographiques
- Réaliser des analyses spatiales de base et avancées


:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice :__
^^^

- L’exercice prend environ 30 à 60 minutes, selon le nombre de participant·e·s et leur familiarité avec les outils informatiques.

:::

:::{grid-item-card}
__Articles wiki pertinents__
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Import de données géographiques dans QGIS](/content/fr/Wiki/fr_qgis_import_geodata_wiki.md)
* [Concept de couche](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)
* [Table attributaire dans QGIS](/content/fr/Wiki/fr_qgis_attribute_table_wiki.md)
* [Projections](/content/fr/Wiki/fr_qgis_projections_wiki.md)

<!-- FIXME: to be updated -->

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

## Exercice <a id="exercise"></a>
### Données disponibles <a id="available-data"></a>

:::{card}
:class-card: sd-text-center
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_1/Module_2_Exercise_1_Understanding_Geodata.zip

__Téléchargez tous les jeux de données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_2/Exercise_1/Module_2_Exercise_1_Understanding_Geodata.zip) et décompressez le dossier.__

:::

Le dossier zip contient :

| Dataset name                                     | Original title                                        | Publisher                                                                 | Downloaded from                                                      |
|:-------------------------------------------------|:------------------------------------------------------|:--------------------------------------------------------------------------|:---------------------------------------------------------------------|
| `sle_admbnda_adm0_adm1_gov_ocha.gpkg` (Polygons) | Sierra Leone - Subnational Administrative Boundaries  | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-sle)                   |
| `sierra_leone_health_HOT.shp` (Points)           | Sierra Leone Health Facilities (OpenStreetMap Export) | Humanitarian OpenStreetMap Team (HOT)                                     | [HDX](https://data.humdata.org/dataset/hotosm_sle_health_facilities) |
| `sl-airports.csv` (CSV)                          | Airports in Sierra Leone                              | Our Airports                                                              | [HDX](https://data.humdata.org/dataset/ourairports-sle)              |


Le GeoPackage `Sierra_leone_administrative_boundaries.gpkg` contient des informations administratives sur la Sierra Leone aux niveaux national et provincial. De plus, le shapefile `sierra_leone_health_HOT.shp` fournit des informations sur différentes structures de santé dans le pays, tandis que le fichier CSV `sl-airports.csv` contient des informations sur les aéroports.

:::{admonition} Arborescence de dossiers
:type: hint

Gardez une gestion des données rigoureuse en créant sur votre ordinateur une [arborescence de dossiers standard](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html#standard-folder-structure) pour vos projets QGIS et vos données géographiques.  
Les données de l’exercice doivent être enregistrées à un emplacement où vous pourrez facilement les retrouver, ainsi que le projet QGIS correspondant.

:::

### Tâches <a id="tasks"></a>

1. Ouvrez dans QGIS les fichiers que vous avez téléchargés. 
   - __Décompressez le dossier__ contenant les données de l’exercice. 
   - Le GeoPackage (`.gpkg`) et le shapefile (`.shp`) peuvent être glissés-déposés directement dans le canevas cartographique de QGIS. 
   - Le fichier `.csv` doit être importé via le menu des couches.
      - Allez dans `Layer` → `Add Layer` → `Add delimited text layer`. Une nouvelle fenêtre s’ouvrira. Vous pouvez y sélectionner le fichier à importer en cliquant sur `...` à droite du champ __File name__ en haut.
      - Accédez au dossier contenant les fichiers de l’exercice et sélectionnez `sl-airports.csv`. 
      - Cliquez sur ouvrir. La fenêtre d’import CSV se mettra à jour et affichera un aperçu du tableau CSV. 
      - Le tableau contient des informations géographiques. Nous devons les préciser dans __"Geometry Definition"__. 
         - Cliquez sur `Point Coordinates` et sélectionnez `longitude_deg` comme __"X field"__ et `latitude_deg` comme __"Y field"__.
      - Cliquez sur ajouter. Une nouvelle couche ponctuelle contenant les aéroports devrait apparaître dans votre canevas cartographique.


:::{figure} /fig/en_3.36_add_csv.png
---
width: 500 px
name: navigation to add csv layer
---
Ouverture de la fenêtre d’import CSV.
:::


:::{figure} /fig/en_delimited_text_screenshot.PNG
---
width: 80%
name: delimited_text
---
Capture d’écran du gestionnaire de sources de données - texte délimité pour charger un fichier CSV.
:::

2. Interagissez avec la carte et explorez les jeux de données. Utilisez l’outil de zoom et déplacez la carte. Concentrez-vous sur la fenêtre d’échelle et observez comment elle varie lorsque vous zoomez et dézoomez. 

3. Familiarisez-vous avec le panneau des couches (liste des couches). Affichez et masquez différentes couches et déplacez-les dans la hiérarchie. Donnez aux couches de données un nom explicite. 

:::{Note}
Renommer une couche n’a aucun effet sur la source de données, comme le nom des fichiers ou leur emplacement de stockage.
:::

4. Examinez les données attributaires des couches en consultant la table attributaire.

5. Modifiez la projection de l’affichage cartographique en `WGS 84 / Pseudo-Mercator EPSG:3857`. Vous pouvez le faire dans le coin inférieur droit de votre fenêtre QGIS. 

:::{Note}
Cela ne modifie pas la projection (les coordonnées) des fichiers, seulement celle de l’affichage cartographique. Vérifiez-le en consultant les propriétés de la couche de points. Quelle projection y est indiquée ?
:::

:::{Hint}
Pour obtenir des informations sur une couche et sa projection, double-cliquez sur la couche et recherchez la section `Information`. Cette section contient des informations générales telles que le nom du fichier et son chemin d’accès, ainsi que des informations sur le système de coordonnées de référence (SCR) dans la section correspondante.
:::


6. Enregistrez la couche des structures de santé dans la projection `WGS 84 / Pseudo-Mercator EPSG:3857`. Cela modifiera la projection du fichier. Vous pouvez le faire en effectuant un clic droit sur la couche → `Export` → `Save Features As..`. Dans la fenêtre contextuelle, sélectionnez **GeoPackage comme format de sortie** et **précisez l’emplacement et le nom du fichier** en cliquant sur les trois petits points. Il est également possible de donner un nom de couche, qui sera affiché lors de son chargement dans QGIS. Avant d’exécuter cette opération, la **projection peut être modifiée** en sélectionnant le SCR souhaité dans la section prévue à cet effet. Vérifiez la projection modifiée en consultant les propriétés de la nouvelle couche créée.

:::{figure} /fig/en_ex1_export_layer.PNG
---
width: 40%
name: export_layer
---
Capture d’écran de la fenêtre d’export.
:::

7. Enregistrez votre projet.

8. Optionnel : vous pouvez ajouter le fond de carte OpenStreetMap via la fenêtre du navigateur, sous `XYZ Tiles`. 

:::{Note}

La combinaison de couches ayant des projections différentes avec des fonds de carte en ligne (qui ont généralement leurs propres projections) peut entraîner des problèmes d’affichage dus à des [conflits de SCR](https://giscience.github.io/gis-training-resource-center/content/fr/Module_2/fr_qgis_projections.html#how-to-choose-an-appropriate-projected-coordinate-system). Lorsque les couches utilisent des SCR distincts, elles peuvent ne pas s’aligner correctement ou apparaître déformées lorsqu’elles sont superposées à un fond de carte en ligne. Pour limiter ces problèmes, il est conseillé soit de reprojeter les couches pour qu’elles correspondent au SCR du fond de carte (ce qui n’est pas toujours applicable), soit de retirer temporairement le fond de carte avant d’enregistrer le projet. Cela garantit un affichage correct de la carte et évite les incohérences visuelles liées aux différences de SCR.

:::


:::{figure} /fig/en_result_geodata_concept_exercise.png
---
width: 80%
name: en_result_geodata_concept_exercise
---
Voici à quoi votre résultat final pourrait ressembler.
:::