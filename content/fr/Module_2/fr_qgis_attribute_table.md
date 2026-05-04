::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Table attributaire <a id="attribute-table"></a>

Chaque couche vectorielle est composée d’entités géométriques (points, lignes ou polygones) et d’une __table attributaire__ ({numref}`en_vector_data_overview`). La table attributaire contient des informations sur chaque entité de la couche. Ces informations sont organisées en lignes et en colonnes. Chaque __ligne__ représente une __entité__, tandis que les __colonnes__ stockent les __attributs__ de cette entité. Vous pouvez utiliser la table attributaire pour rechercher, trier, filtrer, modifier et sélectionner des données. 


:::{figure} /fig/en_vector_data_overview.png
---
width: 600px
align: center
name: en_vector_data_overview
---
Vue d’ensemble des données vectorielles (Source : HeiGIT).
:::

:::{admonition} À vous de jouer !
:class: note

Vous pouvez compléter ce chapitre en réalisant les étapes avec une couche vectorielle de votre choix. Lors du travail avec des données géographiques, vous devez toujours comprendre les informations stockées dans les jeux de données, à la fois les géométries et les données attributaires.

:::

## Ouvrir la table attributaire <a id="opening-the-attribute-table"></a>

Consulter la table attributaire est essentiel pour comprendre et avoir une vue d’ensemble des données avec lesquelles vous travaillez. Après avoir téléchargé et importé un jeu de données dans QGIS, vous ouvrirez très probablement la table attributaire pour comprendre les données et voir quelles informations sont disponibles. Comprendre quelles informations sont présentes est indispensable lorsque l’on travaille avec un logiciel SIG.

Vous pouvez ouvrir la table attributaire de deux manières :

::::{margin}
:::{tip}

Vous pouvez également utiliser le raccourci <kbd>F6</kbd> (dans certains cas <kbd>Fn</kbd> + <kbd>F6</kbd>) pour ouvrir la table attributaire.

:::
::::

1. Faites un clic droit sur une couche dans le panneau des couches et sélectionnez `Open Attribute Table` ({numref}`en_attributetable_right_click`). 

:::{figure} /fig/en_attributetable_right_click.png
---
height: 500px
align: center
name: en_attributetable_right_click
---
Ouverture de la table attributaire via clic droit dans QGIS 3.36
:::

2. Sélectionnez une couche dans le panneau des couches et cliquez sur l’icône de la table attributaire dans la barre d’outils ({numref}`en_attributetable_top_right`). 

:::{note} 

Si vous avez plusieurs couches, seule la table attributaire de la couche actuellement sélectionnée dans le panneau des couches s’ouvrira.

:::

:::{figure} /fig/en_attributetable_top_right.png
---
height: 500px 
align: center
name: en_attributetable_top_right
---
Ouverture de la table attributaire dans QGIS 3.36
:::

:::{dropdown} Boutons de la table attributaire
:open:

| Icon                                        | Description                         | Purpose                                      | Shortcut                                          |
|---------------------------------------------|-------------------------------------|----------------------------------------------|---------------------------------------------------|
| ![](/fig/mActionToggleEditing.png)          | __Activer/désactiver le mode édition__ | Activer les fonctions d’édition             | <kbd>Ctrl</kbd> + <kbd>E</kbd>                    |
| ![](/fig/mActionMultiEdit.png)              | Activer le mode multi-édition       | Mettre à jour plusieurs champs simultanément |                                                   |
| ![](/fig/mActionSaveEdits.png)              | __Enregistrer les modifications__   | Enregistrer les modifications en cours       |                                                   |
| ![](/fig/mActionRefresh.png)                | Recharger la table                  |                                              |                                                   |
| ![](/fig/mActionNewTableRow.png)            | Ajouter une entité                  | Ajouter une nouvelle entité sans géométrie   |                                                   |
| ![](/fig/mActionDeleteSelectedFeatures.png) | Supprimer les entités sélectionnées | Supprimer les entités sélectionnées          |                                                   |
| ![](/fig/mActionEditCut.png)                | Couper les entités sélectionnées    |                                              | <kbd>Ctrl</kbd> + <kbd>X</kbd>                    |
| ![](/fig/mActionCopySelected.png)           | Copier les entités sélectionnées    |                                              | <kbd>Ctrl</kbd> + <kbd>C</kbd>                    |
| ![](/fig/mActionEditPaste.png)              | Coller des entités                  | Insérer de nouvelles entités copiées         | <kbd>Ctrl</kbd> + <kbd>V</kbd>                    |
| ![](/fig/mIconExpressionSelect.png)         | Sélection via une expression        |                                              |                                                   |
| ![](/fig/mActionSelectAll.png)              | Tout sélectionner                   | Sélectionner toutes les entités              | <kbd>Ctrl</kbd> + <kbd>A</kbd>                    |
| ![](/fig/mActionInvertSelection.png)        | Inverser la sélection               | Inverser la sélection actuelle               | <kbd>Ctrl</kbd> + <kbd>R</kbd>                    |
| ![](/fig/mActionDeselectActiveLayer.png)    | Tout désélectionner                 | Désélectionner toutes les entités            | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>A</kbd> |
| ![](/fig/mActionFilterMap.png)              | Filtrer/sélectionner via formulaire |                                              | <kbd>Ctrl</kbd> + <kbd>F</kbd>                    |
| ![](/fig/mActionSelectedToTop.png)          | Déplacer la sélection en haut       | Mettre les lignes sélectionnées en haut      |                                                   |
| ![](/fig/mActionPanToSelected.png)          | Centrer la carte sur la sélection   |                                              | <kbd>Ctrl</kbd> + <kbd>P</kbd>                    |
| ![](/fig/mActionZoomToSelected.png)         | Zoom sur la sélection               |                                              | <kbd>Ctrl</kbd> + <kbd>J</kbd>                    |
| ![](/fig/mActionNewAttribute.png)           | Nouveau champ                       | Ajouter un champ à la source de données      | <kbd>Ctrl</kbd> + <kbd>W</kbd>                    |
| ![](/fig/mActionDeleteAttribute.png)        | Supprimer un champ                  | Supprimer un champ                           |                                                   |
| ![](/fig/mActionEditTable.png)              | Organiser les colonnes              | Afficher/masquer les champs                  |                                                   |
| ![](/fig/mActionCalculateField.png)         | __Ouvrir le calculateur de champs__ | Mettre à jour un champ pour plusieurs entités | <kbd>Ctrl</kbd> + <kbd>I</kbd>                    |
| ![](/fig/mActionConditionalFormatting.png)  | Formatage conditionnel              | Appliquer une mise en forme                  |                                                   |
| ![](/fig/dock.png)                          | Ancrer la table attributaire        | Ancrer/désancrer la table                    |                                                   |
| ![](/fig/mAction.png)                       | Actions                             | Liste des actions liées à la couche          |                                                   |

:::

<!-- ADD: What will be the most important of these. Needs more explanation.-->

## Trier la table attributaire <a id="sort-the-attribute-table"></a>

Vous pouvez trier les données de la table attributaire en cliquant sur l’en-tête d’une colonne. Les données textuelles seront triées par ordre alphabétique et les données numériques par valeur. Pour inverser l’ordre de tri, cliquez à nouveau sur l’en-tête. Une petite flèche dans l’en-tête indique si le tri est croissant ou décroissant.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_show_attribute_table.mp4"></video>

:::::{grid} 2
::::{grid-item-card} 

:::{figure} /fig/en_ascending.png
---
width: 300px
name: en_ascending
---
Table attributaire triée par ordre croissant.
:::

::::

::::{grid-item-card}

:::{figure} /fig/en_descending.png
---
width: 300px
name: en_descending
---
Table attributaire triée par ordre décroissant.
:::

::::
:::::

## Zoomer sur une entité via la table attributaire <a id="zoom-in-on-a-specific-feature-via-attribute-table"></a>

Vous pouvez zoomer sur une entité spécifique pour la localiser géographiquement ou l’examiner plus en détail :

1. __Zoom :__ clic droit sur une entité → `Zoom To Feature`.
2. Fermez la table attributaire. La carte affichera alors l’entité sélectionnée.

:::{dropdown} Vidéo : zoom sur une entité

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom_to_feature.mp4"></video>

:::

## Sélection manuelle d’entités dans la table attributaire <a id="manually-select-features-in-the-attribute-table"></a>

Pour interagir avec des entités dans une couche, vous devez les sélectionner. Une manière de le faire est via la table attributaire.

* __Sélection :__ cliquez sur les lignes correspondant aux entités.
* __Sélection multiple :__ maintenez `Ctrl` enfoncé et sélectionnez plusieurs entités.
* __Afficher uniquement les entités sélectionnées :__ en bas à gauche de la table attributaire, ouvrez le menu déroulant et sélectionnez `Show selected features`. Pour afficher à nouveau toutes les entités, cliquez sur `Show all features`.
* __Afficher uniquement les entités non sélectionnées :__ sélectionnez des entités puis cliquez sur ![](/fig/mActionInvertSelection.png)

:::{dropdown} Vidéo : sélection manuelle d’entités

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_attribute_table_select.mp4"></video>

:::

## Zoomer sur la zone sélectionnée <a id="zoom-to-selected-area"></a>

Maintenant que vous savez sélectionner des entités, vous pouvez zoomer sur votre zone d’intérêt. Pour cela, cliquez sur l’icône correspondante dans la barre d’outils ou faites un clic droit sur la couche et sélectionnez `Zoom to Selection` ({numref}`en_zoom_to_selection_1`).

:::{figure} /fig/en_zoom_to_selection_1.png
---
width: 800px
align: center
name: en_zoom_to_selection_1
---
Exemple de zoom sur la sélection via la barre d’outils.
:::

:::{figure} /fig/en_zoom_to_selection_2.png
---
width: 450px
align: center
name: en_zoom_to_selection_2
---
Exemple de zoom sur la sélection via clic droit.
:::

## Enregistrer uniquement les entités sélectionnées dans un nouveau fichier <a id="save-only-selected-features-as-a-new-file"></a>

Après avoir sélectionné vos données, vous pouvez souhaiter ne travailler qu’avec cette sélection. Il est possible d’enregistrer cette sélection dans une nouvelle couche. Pour cela, faites un clic droit sur la couche → `Export` → `Save only selected features`.

:::{figure} /fig/en_save_selection.png
---
height: 500px
align: center
name: en_save_selection
---
Exemple d’enregistrement des entités sélectionnées.
:::

Vous pouvez ensuite choisir le format, le nom de la couche et le SCR.

<!--ADD IMAGE-->

:::{tip}

Nous recommandons d’utiliser le format GeoPackage (.gpkg) plutôt que le shapefile (.shp) dans la plupart des cas.
Si vous hésitez sur le format le plus adapté, consultez la page [types de données géographiques](/content/fr/Wiki/fr_qgis_geodata_types_wiki.md) du wiki.

:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_export_wiki.mp4"></video>


## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

Vérifiez si vous maîtrisez les concepts clés de ce chapitre en répondant aux questions ci-dessous.

1. __Qu’est-ce que la table attributaire d’une couche vectorielle et comment est-elle structurée ?__

:::{dropdown} Réponse
La table attributaire est une représentation tabulaire des données non spatiales (ou descriptives) d’une couche vectorielle. Chaque ligne correspond à une entité (point, ligne ou polygone). Chaque colonne (appelée champ ou attribut) contient une information (par ex. nom, population, type) pour chaque entité.
:::

2. __Comment ouvrir la table attributaire dans QGIS ?__

:::{dropdown} Réponse
- Dans QGIS, faites un clic droit sur la couche dans le panneau des couches et choisissez Open Attribute Table.
- Vous pouvez également utiliser le bouton de la table attributaire ![](/fig/qgis_open_attribute_table.png) dans la barre d’outils.
:::

3. __Comment zoomer sur une entité spécifique à partir de la table attributaire ?__

:::{dropdown} Réponse
- Dans la table attributaire, faites un clic droit sur la ligne correspondant à l’entité (ou dans une cellule) puis choisissez "Zoom to Feature". La carte se centrera alors sur cette entité.
:::

4. __Décrivez comment sélectionner manuellement des entités via la table attributaire et comment afficher uniquement les entités sélectionnées ou non sélectionnées.__

:::{dropdown} Réponse
__Sélection manuelle :__
- Cliquer sur l’en-tête d’une ligne sélectionne une entité (mise en surbrillance en bleu).
- Pour sélectionner plusieurs entités, maintenez <kbd>Ctrl</kbd> (ou <kbd>Cmd</kbd> sur MacOS) et cliquez sur d’autres lignes.
- Maintenir <kbd>Shift</kbd> permet de sélectionner une plage d’entités.
__Afficher uniquement certaines entités :__
- En bas à gauche de la table attributaire, un menu déroulant permet de choisir :
  - __Show All Features__
  - __Show Selected Features__
  - __Show Unselected Features__
  - Autres filtres : entités visibles, entités modifiées, etc.
- Vous pouvez également utiliser le bouton ![](/fig/qgis_3.40_move_selection_to_top.png) pour déplacer les entités sélectionnées en haut.
:::

5. __Une fois un sous-ensemble d’entités sélectionné, comment enregistrer uniquement ces entités dans une nouvelle couche (ou fichier) ?__

:::{dropdown} Réponse
1. Faites un <kbd>clic droit</kbd> sur la couche contenant la sélection.
2. Sélectionnez `Export` → `Save Selected Features as...`. Une nouvelle fenêtre s’ouvre.
3. Choisissez le format, l’emplacement et le nom du fichier en cliquant sur ![](/fig/Three_points.png)
4. Cliquez sur `Ok`.
::::
