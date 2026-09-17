::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Exercice 7 : Géoréférencer une carte de la Somalie <a id="exercise-7-georeferencing-a-map-of-somalia"></a>

:::{card}
__Objectif de l’exercice :__
^^^

L’objectif de cet exercice est d’apprendre à géoréférencer une carte. Dans de nombreux cas, des institutions (gouvernementales) publient des données ou des cartes uniquement au format PDF. En géoréférençant la carte, nous pouvons toutefois l’importer comme jeu de données raster dans notre projet QGIS. Nous pourrons ensuite soit l’utiliser pour numériser des entités vectorielles, soit exploiter les valeurs raster dans une analyse raster.

:::

::::{grid} 2
:::{grid-item-card}
__Type d’exercice de formation :__
^^^

- Cet exercice peut être utilisé en formation en ligne ou en présentiel. 
- Il peut être réalisé en mode pas-à-pas ou individuellement en autoformation.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour__ 
^^^

- La numérisation de cartes
- La préparation des données pour l’analyse spatiale

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice__
^^^
~ 90 minutes

:::

:::{grid-item-card}
__Articles pertinents__
^^^

* [Géoréférencement](/content/fr/Module_3/fr_qgis_georeferencing.md)
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

## Instructions pas à pas <a id="step-by-step-instructions"></a>

:::{card} 
:class-card: sd-text-justify sd-rounded-2 sd-border-1
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_7/Module_3_Exercise_7_Georeferencing.zip 

__Cliquez [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Exercise_7/Module_3_Exercise_7_Georeferencing.zip) pour télécharger les jeux de données de cet exercice.__

:::

:::{card}
__Données disponibles :__
^^^

- `SOM_soil_deg.png` - Une image d’une carte de dégradation des sols en Somalie extraite d’un rapport PDF (Source : [FAO SWALIM](https://www.faoswalim.org/resources/site_files/L-14%20Land%20Degradation%20and%20a%20Monitoring%20Framework%20in%20Somalia_0.pdf))
- `som_admbnda_adm1_ocha_20230308.gkpg` - Une couche vectorielle contenant les limites administratives des régions (adm1) de la Somalie (Source : OCHA)

:::

### Préparer les données <a id="preparing-the-data"></a>

1. Décompressez le dossier et familiarisez-vous avec les données en examinant la carte de dégradation des sols. La carte se trouve dans le dossier `Module_3_Exercise_7_Georeferencing/data/input/`.
2. Créez un nouveau projet QGIS.

:::{figure} /fig/SOM_Soil_deg.png
---
name: SOM_soil_deg
width: 500 px
---
Dégradation des sols en Somalie.
:::

### Étape 1 : Ajouter un fond de carte et charger la couche vectorielle <a id="step-1-adding-a-basemap-and-loading-the-vector-layer"></a>

Le géoréférencement consiste à relier des points de la carte à géoréférencer à des coordonnées dans votre canevas cartographique QGIS. Ajouter un fond de carte ou une couche de référence à votre projet QGIS vous aidera à identifier les coordonnées correspondantes.

1. Ajoutez un fond de carte en utilisant soit les XYZ Tiles, soit le [plugin QuickMapServices](/content/fr/Wiki/fr_qgis_basemaps_wiki.md). 
2. Importez la couche `som_admbnda_adm1_ocha_20230308` dans le projet QGIS. 

### Étape 2 : Géoréférencer la carte <a id="step-2-georeferencing-the-map"></a>

Maintenant que nous avons préparé notre projet QGIS, commençons le géoréférencement de la carte.

3. Ouvrez le Géoréférenceur en allant dans la barre supérieure → `Layer` → `Georeferencer` ({numref}`open_georeferencer`)

:::{figure} /fig/en_3.36_open_georefencer.png
---
name: open_georeferencer
width: 500 px
---
Ouvrir le Géoréférenceur dans QGIS 3.36.
:::

4. Une nouvelle fenêtre s’ouvre. Il s’agit du __géoréférenceur__. Pour ajouter une image à géoréférencer, cliquez sur ![](/fig/3.36_add_raster_georef.png) `Open Raster`.
5. Sélectionnez l’image de la carte que vous souhaitez géoréférencer. Cliquez sur `Open` (`Module_3_Exercise_7_Georeferencing/data/input`). 
6. L’image apparaît au centre de la fenêtre du géoréférenceur. Cliquez sur ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. Une nouvelle fenêtre s’ouvre. Vous pouvez y définir le type de transformation et le SCR cible. Pour notre besoin, nous utiliserons le type de transformation linéaire. Comme SCR cible (système de coordonnées de référence), nous voulons utiliser le même que pour nos autres données. Dans notre cas, nous pouvons utiliser EPSG:4326. En dessous, vous pouvez définir le nom du fichier et son emplacement d’enregistrement. Assurez-vous que l’option `Load in project when done` est cochée.

::::{margin}

:::{note}
Dans la plupart des cas, vous pouvez laisser le type de transformation sur `linear`. Les cartes régionales utilisent généralement une projection conforme (c’est-à-dire que les angles sont conservés), tout comme l’imagerie satellite. Si vous constatez que les angles ne sont pas corrects ou que la carte est déformée, vous devrez peut-être choisir `polynomial` comme type de transformation. Les transformations polynomiales nécessitent davantage de points de contrôle au sol et ces points doivent être répartis de manière homogène sur l’ensemble de la carte.

Pour en savoir plus sur les différents types de transformation dans QGIS, consultez la [documentation officielle de QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_raster/georeferencer.html#available-transformation-algorithms).
:::
::::

8. Cliquez sur `Ok`. 
9. Une fois le type de transformation défini, vous pouvez commencer à ajouter des points de contrôle au sol (GCP) en cliquant sur ![](/fig/3.36_georef_add_point.png) `Add Point`. Les points de contrôle au sol sont des points auxquels vous attribuez des coordonnées géographiques précises. 
10. Cliquez sur un point de l’image de la carte. Il s’agira d’un emplacement précis que vous pouvez identifier à la fois sur le fond de carte et sur la carte que vous souhaitez géoréférencer. 
11. Une fois la position cliquée, une nouvelle fenêtre apparaît. Vous y ajoutez les coordonnées du point sélectionné. Il existe deux façons de le faire :  
    - Saisir les coordonnées manuellement. Vous devez alors connaître les coordonnées exactes. Il arrive que certaines cartes comportent une grille de coordonnées où vous pouvez les lire.  
    - Sélectionner les points ![](/fig/en_3.36_georef_select_from_canvas.png). Ce mode minimise le géoréférenceur et ouvre le canevas cartographique QGIS. Zoomez sur le même emplacement que celui sélectionné sur la carte non géoréférencée et cliquez une fois.
    - Une fois les coordonnées saisies, cliquez sur `Ok`.
12. La fenêtre du géoréférenceur s’ouvre de nouveau. Cette fois, vous pouvez voir un point dans le tableau situé sous l’image de la carte. Il s’agit des points de contrôle au sol. Continuez à ajouter d’autres GCP. Répartissez-les sur l’ensemble de la carte. Assurez-vous que le `Mean error` en bas à droite de la fenêtre du géoréférenceur soit aussi faible que possible (idéalement inférieur à 5). 

:::{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: georeferencer_dialogue
---
Fenêtre du Géoréférenceur dans QGIS 3.36.
:::

13. Une fois que vous avez ajouté suffisamment de points, cliquez sur ![](/fig/3.36_start_georef.png) `Start Georeferencing`. QGIS utilisera les points ajoutés pour transformer l’image en image géoréférencée, dans laquelle chaque pixel possède des coordonnées GPS.
14. Vous pouvez fermer la fenêtre du géoréférenceur. Décidez si vous souhaitez enregistrer les points GCP dans un fichier. Si vous n’êtes pas certain·e que la précision du géoréférencement soit suffisante, enregistrez les points GCP afin de ne pas avoir à tout recommencer. 
15. Félicitations, la carte géoréférencée apparaît maintenant comme couche raster dans votre projet QGIS.

:::{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: Som_georef_map
---
Une carte géoréférencée de la Somalie dans le canevas cartographique QGIS.
:::

### *Étape 3 optionnelle* : Ajuster la transparence de la carte géoréférencée <a id="optional-step-3-adjusting-the-transparency-of-the-georeferenced-map"></a>

Maintenant que nous avons la carte géoréférencée, nous pouvons __régler la transparence__ afin de voir les autres couches ou le fond de carte en dessous : 

16. Faites un <kbd>clic droit</kbd> sur la couche de la carte géoréférencée. 
17. Sélectionnez `Properties`.
18. Accédez à l’__onglet Transparency__.
19. Réglez la transparence à 50 %.
20. Cliquez sur `Apply`.

Nous pouvons désormais voir les couches sous-jacentes. Nous pouvons aussi vérifier la précision de notre géoréférencement en comparant les limites administratives des deux couches.

### *Étape 4 optionnelle* : Numériser des entités vectorielles à l’aide de la carte géoréférencée <a id="optional-step-4-digitising-vector-features-using-the-georeferenced-map"></a>

Maintenant que la carte est géoréférencée, nous pouvons l’utiliser comme couche de fond pour numériser des entités vectorielles, par exemple un polygone indiquant une zone où la dégradation des sols est sévère.

21. Créez une nouvelle couche shapefile (voir [numérisation](https://giscience.github.io/gis-training-resource-center/content/fr/Module_3/fr_qgis_digitisation.html#creating-new-datasets)). Cliquez sur `Layer` → `Create Layer` → `Create new Shapefile Layer` (vous pouvez aussi choisir de créer une nouvelle couche GeoPackage).
22. Une nouvelle fenêtre de dialogue s’ouvre. Nous devons d’abord préciser l’emplacement d’enregistrement du nouveau jeu de données. 
    1. Cliquez sur ![](/fig/3.36_three_dots.png) à droite du champ `File Name`. 
    2. Accédez au dossier de sortie des données (`Module_3_Exercise_7_Georeferencing/data/output`).
    3. Saisissez un nom pour le jeu de données. 
    4. Cliquez sur `Save`.
23. Réglez le `Geometry Type` sur `Polygon`.
24. Ajoutons un champ (colonne dans la table attributaire) afin de renseigner le type de dégradation des sols : 
    1. Sous `New field`, ajoutez un nom, par exemple `soil_deg`. Nous voulons que d’autres personnes puissent identifier le type d’information stocké dans cette colonne. 
    2. Laissez le type sur String (texte).
    3. Cliquez sur `Add to field list`. 
25. Terminez la création du jeu de données en cliquant sur `Ok`. La couche sera ajoutée à votre panneau des couches.
26. Créons maintenant une nouvelle entité polygonale : 
    1. Sélectionnez la nouvelle couche dans le panneau des couches.
    2. Activez le mode édition en cliquant sur ![](/fig/en_editing_mode.png).
    3. Cliquez sur ![](/fig/mActionCapturePolygon.png) dans la barre d’outils de numérisation pour créer un nouveau polygone.
    4. Commencez à tracer le contour d’une zone où la dégradation des sols est sévère (en rouge) en plaçant plusieurs points (<kbd>Left-Click</kbd>)
    5. Une fois le contour terminé, achevez la création de l’entité par un <kbd>clic droit</kbd>.
    6. Une nouvelle fenêtre de dialogue apparaîtra. Vous pourrez y saisir les attributs de la nouvelle entité polygonale. Sous `soil_deg`, saisissez "severe". 
    7. Cliquez sur `Ok`.

Félicitations, nous avons maintenant géoréférencé une carte et numérisé des entités vectorielles que nous pouvons utiliser pour des analyses ultérieures !