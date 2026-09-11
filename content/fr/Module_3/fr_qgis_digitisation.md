::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Numérisation <a id="digitisation"></a>

La numérisation est le processus de conversion de données géographiques provenant de cartes ou d’images en une forme numérique, généralement représentée sous forme de données vectorielles. La maîtrise de la numérisation constitue une compétence fondamentale pour les spécialistes SIG. Elle leur permet de convertir des informations spatiales en format numérique, facilitant ainsi la manipulation des données de manière plus efficace que les méthodes traditionnelles d’interprétation d’images ou de cartes papier. 

:::{admonition} Numérisation dans le travail humanitaire
:class: tip

Si vous souhaitez comprendre comment la cartographie communautaire et la numérisation peuvent renforcer la résilience des communautés et faciliter le travail humanitaire, consultez l’article de blog de Paul Knight [« This is the first time this community is on a map… » — Digital Community Mapping in Nigeria](https://medium.com/digital-and-innovation-at-british-red-cross/first-time-this-community-has-been-on-a-map-nigeria-f592906b7be1).

:::

:::{figure} /fig/en_digitisation_concept.png
---
width: 900px
align: center
name: en_digitisation_concept
---
Le concept de la numérisation dans les SIG (Source : HeiGIT).
:::

## Numérisation dans QGIS <a id="digitising-in-qgis"></a>

Dans QGIS, la numérisation consiste à tracer des entités telles que des points, des lignes ou des polygones directement sur le canevas cartographique afin de représenter des éléments géographiques comme des bâtiments, des routes ou des parcelles. De plus, vous pouvez attribuer des attributs à chaque entité lors de la numérisation, ce qui permet une analyse plus approfondie et une intégration avec d’autres données géospatiales. Ces données numérisées deviennent alors une ressource précieuse pour l’analyse spatiale et la cartographie.

:::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Scénario réel 1/3__
^^^
Une inondation s’est produite dans un village à la suite de fortes pluies. Afin d’évaluer les besoins des ménages et l’impact sur les infrastructures, vous êtes chargé de réaliser une carte d’ensemble de la région et d’indiquer les bâtiments et les routes touchés par l’inondation. Cependant, aucun jeu de données contenant les bâtiments ou les routes n’est disponible. Pour créer la carte, vous devrez donc créer deux nouvelles couches : une pour le réseau routier et une pour les bâtiments. Heureusement, des images satellites récentes sont disponibles. À l’aide de ces images, vous pouvez créer des couches vectorielles représentant les infrastructures clés, telles que les bâtiments et les routes. Une fois ces couches créées, vous pouvez produire une première carte d’ensemble du village. Cette carte sera ensuite distribuée aux membres de la communauté et aux volontaires sur le terrain afin de cartographier les infrastructures endommagées. Dans une étape suivante, les informations collectées sur le terrain pourront être utilisées pour enrichir les données et réaliser une évaluation de l’impact des inondations. Pour créer cette carte, vous devrez créer de nouvelles couches vectorielles. 
:::


### Barres d’outils de numérisation <a id="digitisation-toolbars"></a>

:::{figure} /fig/Activate_digitizing_toolbox.png
---
width: 300px
align: left
name: Activate digitising Toolbar 
---
La barre d’outils de numérisation dans QGIS 3.36.
:::

La numérisation se fait à l’aide de la `Digitizing Toolbar` et sur le canevas cartographique.  
Tout d’abord, vous devez vérifier si la `Digitizing Toolbar` est activée. Pour cela :
* Cliquez sur l’onglet `View` dans la barre de menu puis sur `Toolbars`. Vérifiez que les barres `Digitizing` et `Advanced Digitizing` sont activées.

Tout d’abord, vous devez vérifier si la `Digitizing Toolbox` est activée. Pour cela  
1. Cliquez sur l’onglet `View` dans la barre de menu puis sur `Toolbars`. Vérifiez que les barres `Digitizing` et `Advanced Digitizing` sont activées.

2. Une boîte à outils comme celle-ci devrait apparaître en haut de l’interface QGIS

<br>

<br>  

<br>  

La barre d’outils de numérisation offre les outils de base pour créer, enregistrer et modifier des entités. Cependant, pour toute opération allant au-delà de la simple création ou suppression d’entités, la barre d’outils de numérisation avancée est nécessaire (voir {numref}`digitising_toolbar`). La barre d’outils de numérisation avancée permet de déplacer des entités, de supprimer des parties d’entités et bien plus encore. Toutes les fonctions sont listées dans les deux tableaux ci-dessous.

:::{figure} /fig/Toolbox.png
---
width: 700 px
name: digitising_toolbar
align: center
---
Barre d’outils de numérisation dans QGIS 3.36.
:::

:::{dropdown} Barre d’outils de numérisation
| Outil | Fonction | Outil | Fonction |
|---|---|-----|---|
| ![](/fig/mActionAllEdits.png) | Accès à l’enregistrement, à l’annulation ou au rétablissement des modifications dans toutes ou certaines couches simultanément | ![](/fig/mActionToggleEditing.png) | Activer ou désactiver le mode édition des couches sélectionnées |
| ![](/fig/mActionSaveEdits.png) | Enregistrer les modifications | |
| ![](/fig/mActionDigitizeWithSegment.png) | Numériser avec des segments droits | ![](/fig/mActionDigitizeWithCurve.png) | Numériser avec des courbes |
| ![](/fig/mActionStreamingDigitize.png) | Activer la numérisation à main levée | ![](/fig/mActionDigitizeShape.png) | Numériser un polygone de forme régulière |
| ![](/fig/mActionNewTableRow.png)  | Ajouter un nouvel enregistrement | ![](/fig/mActionCapturePoint.png) | Ajouter une entité : point |
| ![](/fig/mActionCaptureLine.png) | Ajouter une entité : ligne | ![](/fig/mActionCapturePolygon.png) | Ajouter une entité : polygone |
| ![](/fig/mActionVertexTool.png) | Outil de sommets (toutes les couches) | ![](/fig/mActionVertexToolActiveLayer.png) | Outil de sommets (couche active) |
| ![](/fig/checkbox.png) | Définir si le panneau d’édition des sommets doit s’ouvrir automatiquement | ![](/fig/mActionMultiEdit.png) | Modifier les attributs de toutes les entités sélectionnées simultanément |
| ![](/fig/mActionDeleteSelectedFeatures.png) | Supprimer les entités sélectionnées de la couche active | ![](/fig/mActionEditCut.png) | Couper les entités de la couche active |
| ![](/fig/mActionCopySelected.png) | Copier les entités sélectionnées de la couche active | ![](/fig/mActionEditPaste.png) | Coller les entités dans la couche active |
| ![](/fig/mActionUndo.png) | Annuler les modifications dans la couche active | ![](/fig/mActionRedo.png) | Rétablir les modifications dans la couche active |

:::

Pour des procédures de numérisation plus complexes, vous utiliserez la barre d’outils de numérisation avancée. Cependant, dans ce chapitre, nous nous concentrerons sur la barre d’outils de numérisation standard. 

:::{dropdown} Barre d’outils de numérisation avancée

| Outil                                                                                                        | Fonction                               | Outil                                                                                                                              | Fonction                  |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| ![](/fig/cad.png)                                                                                           | Activer les outils de numérisation avancée      |                                                                                                                                   |                          |
| ![](/fig/mActionMoveFeature-1.png)![](/fig/mActionMoveFeatureLine.png)![](/fig/mActionMoveFeaturePoint.png) | Déplacer des entités                       | ![Alt text](/fig/mActionMoveFeatureCopy.png) ![](/fig/mActionMoveFeatureCopyLine.png) ![](/fig/mActionMoveFeatureCopyPoint-2.png) | Copier et déplacer des entités |
| ![Alt text](/fig/mActionRotateFeature.png)                                                                  | Faire pivoter des entités                     | ![Alt text](/fig/mActionSimplify.png)                                                                                             | Simplifier une entité         |
| ![Alt text](/fig/mActionScaleFeature.png)                                                                   | Mettre à l’échelle une entité                         |                                                                                                                                   |
| ![Alt text](/fig/mActionAddRing.png)                                                                        | Ajouter un anneau                              | ![Alt text](/fig/mActionAddPart.png)                                                                                              | Ajouter une partie                 |
| ![Alt text](/fig/mActionFillRing.png)                                                                       | Remplir un anneau                             | ![Alt text](/fig/mActionReverseLine.png)                                                                                          | Inverser la direction           |
| ![Alt text](/fig/mActionDeleteRing.png)                                                                     | Supprimer un anneau                           | ![Alt text](/fig/mActionDeletePart.png)                                                                                           | Supprimer une partie              |
| ![Alt text](/fig/mActionOffsetCurve.png)                                                                    | Décaler une courbe                          | ![Alt text](/fig/mActionReshape.png)                                                                                              | Remodeler des entités         |
| ![Alt text](/fig/mActionSplitParts.png)                                                                     | Scinder des parties                           | ![Alt text](/fig/mActionSplitFeatures.png)                                                                                        | Scinder des entités           |
| ![Alt text](/fig/mActionMergeFeatureAttributes.png)                                                         | Fusionner les attributs des entités sélectionnées | ![Alt text](/fig/mActionMergeFeatures.png)                                                                                        | Fusionner les entités sélectionnées  |
| ![Alt text](/fig/mActionRotatePointSymbols.png)                                                             | Faire pivoter des symboles de points                  | ![Alt text](/fig/mActionOffsetPointSymbols.png)                                                                                   | Décaler des symboles de points     |
| ![Alt text](/fig/mActionTrimExtend.png)                                                                     | Rogner ou prolonger une entité                |                                                                                                                                   |                          |
:::


## Création de nouveaux jeux de données <a id="creating-new-datasets"></a>

Pour numériser de nouvelles données, vous devez toujours commencer par créer le jeu de données avant de le remplir avec des données numérisées. Gardez à l’esprit qu’une couche ne peut contenir qu’un seul type de géométrie : soit des points, des lignes ou des polygones. Lors de la création d’un jeu de données, vous devrez choisir le type de géométrie. De plus, vous pouvez ajouter des colonnes supplémentaires avec des attributs afin d’enrichir la table de données. 

:::{admonition} À vous de jouer !
:class: note

Pensez à un jeu de données spatial dont vous pourriez avoir besoin dans vos opérations humanitaires. Quel type d’informations supplémentaires serait utile ? Comment les collecteriez-vous ? Cela peut aller du type de route, des cultures, du type de végétation ou d’indicateurs sociaux. Vous pouvez en discuter en groupe et l’écrire sur papier ou l’ajouter à un tableau blanc numérique. 

:::


:::{dropdown} Vidéo : Comment créer un nouveau jeu de données

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_create_layer.mp4"></video>

:::

1. `Layer` → `Create Layer` → `New GeoPackage Layer` ou `New Shapefile Layer`.
2. Cliquez sur ![](/fig/Three_points.png) à côté du champ `file name` et naviguez vers le dossier où vous souhaitez enregistrer le jeu de données.
3. `File encoding` : assurez-vous qu’il est défini sur UTF-8.
4. `Geometry type` : sélectionnez le type d’entité que vous souhaitez numériser, par exemple des points ou des lignes.
5. Sous `Additional dimension`, assurez-vous toujours de sélectionner `None`, sauf si vous avez la possibilité de collecter également des valeurs Z (élévation), ce qui est rarement le cas.
6. Menu déroulant CRS : sélectionnez le EPSG/CRS que vous souhaitez définir pour la nouvelle couche. Par défaut, QGIS sélectionne le CRS du projet. Pour le modifier, cliquez sur ![](/fig/mIconProjectionEnabled.png).
7. Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Vous pouvez y définir le type de données que vous souhaitez collecter dans ce jeu de données.
    * `Type` : sélectionnez le type de données de la colonne, par exemple `Text`, `Whole number`, `Decimal Number`, `Date`.
    * Cliquez sur ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
8. Cliquez sur `OK` pour créer les données.


:::{figure} /fig/New_GeoPackage_Layer.png
---
width: 500px
name: New_GeoPackage_Layer
align: center
---
La fenêtre de création de couche dans QGIS 3.36.
:::


:::{attention} 
Un concept important à comprendre avant de commencer à ajouter des données aux jeux de données est que, chaque fois que vous effectuez des modifications sur un jeu de données autres que le style, vous devez activer le mode édition. Cela se fait en sélectionnant la couche et en cliquant sur ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Les boutons de nombreuses fonctions de la barre d’outils de numérisation deviennent alors actifs. Une fois les modifications terminées, cliquez sur ![](/fig/mActionSaveEdits.png) `Save Layer Edits` pour enregistrer vos modifications. 
:::

Une fois la nouvelle couche configurée, vous pouvez commencer à ajouter des entités géométriques. Le processus est globalement le même pour les trois types de géométrie : 

### Création de nouvelles entités <a id="creating-new-data-entries"></a>

1. Sélectionnez la couche à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Assurez-vous que la couche est en mode édition. Sinon, cliquez sur l’icône ![](/fig/mActionToggleEditing.png) dans la barre d’outils de numérisation. 

### Création de données ponctuelles <a id="creating-point-data"></a>

1. Sélectionnez la couche de points à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png) `Toggle Editing`. Assurez-vous que la couche est en mode édition. Sinon, cliquez sur l’icône ![](/fig/mActionToggleEditing.png). 
3. Cliquez sur ![](/fig/mActionCapturePoint.png). 
4. Cliquez avec le bouton gauche sur l’entité que vous souhaitez numériser.
5. Une fenêtre `[Nom de votre couche] - Feature Attribute` apparaîtra. Vous pouvez y ajouter les informations relatives à cette entité dans les différentes colonnes, en fonction de la table attributaire de la couche.
5. Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
6. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

:::{dropdown} Vidéo : Comment créer des données ponctuelles
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_point_feature.mp4"></video>
:::

:::{figure} /fig/point_creation.png 
---
width: 750 px
name: point_creation
align: center
---
Création de points.
:::

<!--REPLACE IMAGE showing a point creation window with more attributes and not just ID and type to show the 
information you can add at this stage-->



::::{admonition} Obtenir des coordonnées depuis Google Maps
:class: tip

Parfois, le moyen le plus simple d’obtenir les coordonnées d’un lieu, comme le bureau d’une branche nationale de la Croix-Rouge ou du Croissant-Rouge ou simplement une maison, est d’utiliser Google Maps. Dans Google Maps, vous pouvez faire un clic droit sur n’importe quel emplacement pour obtenir les coordonnées (en degrés). 

:::{figure} /fig/en_google_maps_rightclick_coords.png
---
width: 250 px
align: right
name: en_google_maps_rightclick_coords
---
:::

1. Dans Google Maps, localisez le point que vous souhaitez ajouter à votre projet QGIS.
2. Faites un clic droit sur le point et sélectionnez les coordonnées. Elles seront automatiquement copiées dans votre presse-papiers.
3. Revenez à votre projet QGIS et collez les coordonnées dans la barre de recherche en bas à gauche de la fenêtre QGIS.
4. Sélectionnez `Go to [Your coordinates] (EPSG 4326: WGS 84)`. 
5. Le point de coordonnées apparaîtra en rouge sur le canevas cartographique. 
::::




:::{admonition} À vous de jouer !
 
Essayez de numériser les branches RCRC de votre pays en suivant les étapes ci-dessous.

:::

1. Créez un nouveau jeu de données de points.
2. Ajoutez un [basemap](/content/fr/Module_2/fr_qgis_basemap.md) (OSM ou Bing Aerial, par exemple).
3. Recherchez les branches RCRC de votre pays sur Google Maps.
4. Une fois les branches localisées, faites un clic droit sur une branche dans Google Maps et cliquez sur les coordonnées. Elles seront copiées dans votre presse-papiers.
5. Collez les coordonnées dans la barre de recherche en bas à gauche de la fenêtre QGIS. Sélectionnez l’option pour naviguer vers les coordonnées. L’emplacement sera marqué par un point rouge.

6. Activez le mode édition ![](/fig/mActionToggleEditing.png) dans votre nouvelle couche.
7. Cliquez sur ![](/fig/mActionCapturePoint.png).
8. Ajoutez l’entité ponctuelle à l’emplacement indiqué.
9. Ajoutez le nom de la branche RCRC.
10. Cliquez sur `Ok`. 
11. Cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
12. Cliquez sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition. 



### Création de couches linéaires et polygonales <a id="creating-line-and-polygon-layers"></a>

Le processus de création de couches linéaires ou polygonales est essentiellement le même que celui des données ponctuelles. La principale différence est que, au lieu d’ajouter un seul point, les géométries de type ligne et polygone nécessitent plusieurs points (sommets). Chaque point ajouté est un sommet entre deux segments. Dans QGIS, vous créez des lignes et des polygones en ajoutant un point, puis un autre point relié au précédent. Pour terminer la création de l’entité, utilisez le <kbd>bouton droit de la souris</kbd>. 

:::{attention} 
N’oubliez pas de changer le type de géométrie en lignes si vous souhaitez créer une nouvelle couche linéaire.
:::

::::{tab-set}

:::{tab-item} Création de données linéaires

La création de données linéaires fonctionne de la même manière que la création de données ponctuelles (voir ci-dessus). Vous devez d’abord créer une nouvelle couche linéaire ou en utiliser une existante. 

1. Sélectionnez la couche linéaire à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png). La couche est alors en mode édition.
3. Cliquez sur ![](/fig/mActionCaptureLine.png). 
4. Pour numériser des lignes, cliquez le long de la ligne. Lorsque vous avez terminé, faites un clic droit sur le dernier point pour finaliser l’entité.
5. Une fenêtre `[Nom de votre couche] - Feature Attribute` apparaîtra. Vous pouvez y ajouter les informations relatives à cette entité dans les différentes colonnes, en fonction de la table attributaire de la couche.
6. Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) `Save Layer Edits` pour enregistrer vos modifications.
7. Cliquez sur ![](/fig/mActionToggleEditing.png) `Toggle Editing` pour quitter le mode édition.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Creat_line_feature.mp4"></video>

:::

:::{tab-item} Création de données polygonales

La création de couches polygonales fonctionne de la même manière que pour les données ponctuelles et linéaires.

1. Sélectionnez la couche polygonale à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png). La couche est alors en mode édition.
3. Cliquez sur ![](/fig/mActionCapturePolygon.png). 
4. Pour numériser des polygones, cliquez avec le bouton gauche autour de la zone que vous souhaitez numériser. Lorsque vous avez terminé, faites un clic droit sur le dernier point pour finaliser l’entité.
5. Une fenêtre `[Nom de votre couche] - Feature Attribute` apparaîtra. Vous pouvez y ajouter les informations relatives à cette entité dans les différentes colonnes, en fonction de la table attributaire de la couche.
6. Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
7. Cliquez sur ![](/fig/mActionToggleEditing.png) `Toggle Editing` pour quitter le mode édition.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_feature.mp4"></video>

:::

::::

:::{card} 
:class-card: sd-text-justify sd-rounded-3 sd-border-2
__Scénario réel 2/3__
^^^
La première étape consiste à localiser le village à l’aide des coordonnées GPS que vous saisissez en bas à droite de la fenêtre QGIS. Heureusement, le processus de numérisation est relativement simple grâce à une image satellite récente fournie par Microsoft Bing. Vous pouvez charger cette image en utilisant __QuickMapServices__ et en recherchant puis en ajoutant le fond de carte `Bing Aerial`. Les bâtiments et les routes sont visibles sur l’image satellite. L’étape suivante consiste à créer de nouvelles couches : une pour les routes et une pour les bâtiments.

:::

## Modification des données <a id="editing-the-data"></a>

Dans certains cas, vous pouvez vouloir modifier ou corriger des données vectorielles en raison d’inexactitudes ou de changements. La modification des données vectorielles se fait à l’aide de la barre d’outils de numérisation. Dans QGIS, vous pouvez modifier à la fois les géométries et les valeurs de la table attributaire. 

### Modification des géométries <a id="editing-geometries"></a>

Dans tous les cas :

1. Sélectionnez la couche que vous souhaitez modifier.
2. Cliquez sur ![](/fig/mActionToggleEditing.png) pour activer le mode édition.
3. Effectuez vos modifications.
4. Enregistrez vos modifications en cliquant sur ![](/fig/mActionSaveEdits.png).
5. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

:::{Tip} 
Vous pouvez utiliser les boutons ![](/fig/mActionUndo.png) et ![](/fig/mActionRedo.png) pour annuler ou rétablir facilement des modifications.

Notez que cela n’est possible __avant__ d’enregistrer les modifications.
:::

:::::{tab-set}

::::{tab-item} Suppression d’entités

1. Sélectionnez la couche que vous souhaitez modifier.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png) `Toggle Editing`. 
3. Cliquez sur ![](/fig/mActionSelectRectangle.png) et sélectionnez l’entité que vous souhaitez supprimer (voir le [wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_spatial_queries_wiki.html#manual-selection)).
4. Une fois les entités sélectionnées, cliquez sur ![](/fig/mActionDeleteSelectedFeatures.png) pour les supprimer.
5. Une fois les modifications terminées, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
6. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

:::{note}
Gardez à l’esprit qu’une fois les modifications enregistrées ![](/fig/mActionSaveEdits.png), vous ne pouvez plus annuler ou récupérer les entités supprimées. Les modifications affectent définitivement le fichier de données dans votre dossier. 
:::
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/delet_feature_geometry.mp4"></video>

::::

::::{tab-item} Déplacement d’entités

Il existe plusieurs méthodes pour déplacer des entités. Nous présentons ici une méthode qui fonctionne de la même manière pour les points, les lignes et les polygones. Pour cela, vous devez utiliser la barre d’outils de numérisation avancée.

1. Sélectionnez la couche linéaire à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png). 
3. Cliquez sur ![](/fig/mActionMoveFeaturePoint.png), puis sur l’entité que vous souhaitez déplacer. Cliquez ensuite sur l’emplacement où vous souhaitez la déplacer.
4. Une fois les modifications terminées, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
5. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/move_feature_geometry.mp4"></video>

::::

::::{tab-item} Modification des géométries

1. Sélectionnez la couche linéaire à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png). 
3. Cliquez sur ![](/fig/mActionVertexToolActiveLayer.png).
4. Vous pouvez maintenant déplacer chaque sommet d’une entité. Cliquez sur le sommet que vous souhaitez déplacer, puis sur le nouvel emplacement.
5. Une fois les modifications terminées, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
6. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_move_vertices.mp4"></video>

::::

::::{tab-item} Ajouter des anneaux aux polygones

Un anneau dans QGIS correspond à une zone à l’intérieur d’un polygone qui n’en fait pas partie. Imaginez un polygone représentant un lac : l’anneau correspond alors à une île dans ce lac. Pour mieux comprendre, regardez la vidéo ci-dessous.

1. Sélectionnez la couche linéaire à laquelle vous souhaitez ajouter des données dans le panneau des couches.
2. Accédez à la barre d’outils de numérisation et cliquez sur ![](/fig/mActionToggleEditing.png). 
3. Cliquez sur ![add ring icon](/fig/mActionAddRing.png).
4. Créez un anneau en cliquant sur la zone que vous souhaitez exclure. Faites un clic droit pour fermer l’anneau.
5. Une fois les modifications terminées, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
6. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_digitize_add_ring.mp4"></video>

::::

:::::

### Modification des valeurs attributaires <a id="editing-the-attribute-values"></a>

Parfois, vous devrez modifier les valeurs dans les colonnes de la table attributaire. Par exemple, le nom d’un district administratif peut être mal orthographié ou incohérent, ou une valeur peut être incorrecte. Pour cela, vous devez :

::::{margin}

:::{tip}
Vous pouvez ouvrir la table attributaire de la couche sélectionnée en appuyant sur <kbd>F6</kbd>. 
:::
::::

1. Ouvrir la [table attributaire](/content/fr/Module_2/fr_qgis_attribute_table.md).
2. Cliquez sur ![](/fig/mActionToggleEditing.png) pour activer le mode édition.
3. Choisissez le champ que vous souhaitez modifier. 
4. Saisissez la valeur corrigée.
5. Cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
6. Cliquez à nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition. 

Ce processus est appelé __« nettoyage des données »__ et est essentiel lors de l’analyse ou de la manipulation de données. Lors de la collecte ou de la numérisation, il est facile de commettre de petites erreurs, comme une valeur incorrecte, un mauvais type de valeur ou une faute d’orthographe. Il est donc important de vérifier la table attributaire pour détecter les incohérences ou erreurs. Si ces erreurs ne sont pas corrigées, les résultats seront erronés et vous pourriez tirer de mauvaises conclusions.

::::{card}
:class-card: sd-text-justify sd-text-black sd-rounded-3 sd-border-2
__Scénario réel 3/3__
^^^
Avec les nouvelles couches, vous êtes prêt à tracer les bâtiments et les routes. Vous disposez déjà d’informations sur l’état des routes (par exemple, le type de surface, la qualité ou si elles sont inondées) et sur l’état des bâtiments (par exemple, s’ils sont affectés par une inondation, s’ils comportent plusieurs étages, etc.). Ces informations sont utiles et peuvent être stockées dans les attributs supplémentaires de la table de données. 

:::{figure} /fig/Building_damage_assessement_bangladesh.png
---
name: Building_damage_assessement
width: 750 px 
---
Évaluation des dommages aux bâtiments à Paikgachha Upazila, district de Khulna, division de Khulna, Bangladesh au 4 juin 2024 (Source : [Int'l Charter, UNOSAT](https://reliefweb.int/map/bangladesh/building-damage-assessment-paikgachha-upazila-khulna-district-khulna-division-bangladesh-4-june-2024-imagery-analysis-4-june-2024-published-7-june-2024-v1))
:::

::::

## Erreurs de numérisation spatiale dans QGIS <a id="spatial-digitisation-errors-in-qgis"></a>

La précision des géodonnées est essentielle pour l’analyse spatiale. Les erreurs de position sont inévitables lorsque les données sont numérisées manuellement. Les exemples les plus courants incluent les sous-extensions (undershooting) et les dépassements (overshooting). Les sous-extensions se produisent lorsque les entités ne se connectent pas correctement, et les dépassements lorsque les lignes dépassent leur point de connexion. Souvent, ces erreurs ne sont visibles qu’en zoomant fortement sur les coordonnées. La définition d’une tolérance d’accrochage (snapping tolerance) permet de réduire ces erreurs. La tolérance d’accrochage correspond à la distance minimale tolérée entre les nœuds, les lignes et/ou les sommets.

:::{figure} /fig/Digitization_Errors.PNG
---
width: 500px
align: center
name: Digitization_Errors
---
Erreurs de numérisation (Source : SpatialPost).
:::

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Récapitulez vos connaissances
:class: note 

1. __Qu’est-ce que la numérisation dans les SIG ? Pourquoi est-il utile de convertir des entités issues de cartes ou d’images en format vectoriel ?__

:::{dropdown} Réponse
La numérisation dans les SIG est le processus de tracé ou de capture d’entités géographiques (points, lignes, polygones) à partir de cartes, d’images (telles que des images satellites ou aériennes, ou des cartes scannées) __ou de rapports__, puis leur conversion en données vectorielles.  
Elle est utile car elle permet d’effectuer des analyses spatiales et de mieux comprendre les phénomènes étudiés. De plus, ces données peuvent être combinées avec d’autres données spatiales et visualisées sous forme de cartes informatives.
:::

2. __Comment créer un nouveau jeu de données vectorielles ?__

:::{dropdown} Réponse
1. Dans la barre supérieure, accédez au menu `Layer` → `Create Layer` → `New GeoPackage Layer` ou `New Shapefile Layer`
2. Définissez les propriétés de la couche :
    - Spécifiez le chemin et le nom du fichier
    - **Encoding** : UTF-8 (permet les caractères spéciaux)
    - **Geometry type** : point, ligne, polygone (une couche ne supporte qu’un seul type de géométrie)
    - **Coordinate Reference System (CRS)**
    - Définissez les __champs attributaires__ (colonnes) de la table attributaire.
3. Cliquez sur `Ok` pour créer la couche. 
:::


3. __Imaginez que vous numérisez des bâtiments affectés par une inondation à partir d’une image aérienne. Quels champs attributaires pourriez-vous inclure et quel niveau de détail ou de précision chercheriez-vous à atteindre ?__ 

:::{dropdown} Réponse 
Les attributs à numériser dépendent toujours de l’objectif de votre cartographie (par exemple : réponse d’urgence, évaluation des dommages, planification) et du fait que vous soyez sur le terrain ou que vous utilisiez des images satellites.   
- __Champs attributaires potentiels__ :  
    - __Type/usage du bâtiment__ : résidentiel, commercial, industriel, public  
    - __Nombre d’étages__
    - __Matériau du toit__
    - __Matériau des murs__
    - __État des dommages__ : « aucun dommage », « dommages mineurs », « dommages importants », « effondré »
    - __Profondeur de l’inondation ou exposition à l’eau__
    - __Date de l’évaluation__
    - __Niveau de confiance/qualité__
    - __Adresse__
    - ...
:::

::::
