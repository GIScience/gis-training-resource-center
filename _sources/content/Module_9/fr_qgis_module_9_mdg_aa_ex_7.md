::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 7 : Accessibilité des postes de santé depuis les entrepôts CRM

## Caractéristiques


::::{grid} 2
:::{grid-item-card}
__Type d'exercice:__
^^^

- Cet exercice peut être utilisé dans le cadre de formations en ligne ou en présentiel.
- Il peut être réalisé en tant qu'exercice guidé ou individuellement en auto-apprentissage.

:::

:::{grid-item-card}
__Piste d'Exercice:__
^^^

Cet exercice est le cinquième exercice de la piste d'exercice ["Analyse d’Action Anticipative pour les Cyclones à Madagascar"](/content/Exercise_tracks/fr_mdg_aa_cyclones.md)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé pour l'exercice__
^^^

1 à 2 heures

:::

:::{grid-item-card}
__Articles Wiki pertinents__
^^^

* [Zonal Statistics](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_raster_basic_wiki.html)
* [Intersection](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_spatial_joins_wiki.html#join-attributes-by-location-summary)
* [Projections](/content/Wiki/en_qgis_projections_wiki.md)
* [Buffer](/content/Wiki/en_qgis_projections_wiki.md)
* [Clip](/content/Wiki/en_qgis_projections_wiki.md)
* [Automatisation](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html)

:::

::::

:::{card}
:class-card: sd-border-1 sd-shadow-none
__Objectif de l'exercice:__
^^^
Aina, l'experte GIS (SIG) de la Croix-Rouge malgache (CRM), se prépare pour la prochaine saison des cyclones. Elle souhaite eméliorer la capacité de réaction de son équipe une fois une tempête annoncée, en automatisant des analyses clés dans la application QGIS. 
Celles-ci incluent l'estimation des populations exposées, l'identification des services impactés comme la santé et l'education, et l'évaluation de l'accessibilité des postes de santé à partir des entrepôts de la croix rouge dans une fenêtre critique de 10 heures. 
L'objectif est de préparer un workflow d'analyse et de visualisation pour soutenir une action anticipée (eng.: Anticipatory Action) et fondée sur les données, avant que le cyclone ne touche terre. 


:::

## Instruction pour les formateurs


:::{dropdown} __Espace Formateurs (Trainers Corner)__ 

### Préparer la formation

- Prenez du temps pour vous familiariser avec l'exercice et le matériel founi. 
- Préparez un tableau blanc. Cela peut être un tableau physique, un paperboard (tableau blanc virtuel, e.g., Miro Board) où les participant·es peuvent ajouter leurs observations et questions. 
- Avant de commencer l'exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et dézippé__ le dossier de données.
- Consultez [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) pour des conseils généraux sur la conduite de formations (ce matériel est en anglais).


### Animer la formation

__Introduction:__

- Présentez l'idée et l'objectif de l'exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a bien dézippé le dossier avant de commencer les tâches.

__Exercice guidée:__

- Montrez et expliquez chaque étape cous-même au moins deux fois, et suffisamment lentement por que chacun·e puisse voir ce que vous faites et reproduire les étapes dans sons prope projet QGIS.
- Assurez-vous que tout le monde suit en demandant régulièrement si quelqu'un a besoid d'aide ou si tout le monde suit toujours.
- Soyez ouvert·e et patient·e face aux questions ou problèmes éventuels. Vos participant·es sont en train de faire plusieures choses à la fois: écouter vos instructions tout en s'orientant dans leur propre projet QGIS.

### Fin de la formation

- Prévoyez du temps à la fin pour répondre aux questions ou aborder les éventuels problèmes rencontrés lors de tâches.
- Laissez un moment pour des questions ouvertes.

:::

---

## Tâches

Lorsque qu’un cyclone est prévu pour un atterrissage, Aina collabore avec les équipes logistique et santé pour 
décider **où envoyer les kits médicaux prépositionnés**. Cependant, tous les entrepôts CRM ne stockent pas les 
articles nécessaires — seulement trois le font.

Pour prendre des décisions rapides et basées sur les données, Aina souhaite savoir **quels postes de santé sont accessibles** à partir de ces entrepôts **en moins de 10 heures**. Cette analyse permet de s’assurer que les kits 
sont envoyés vers des établissements **réellement accessibles à temps**.

Son objectif est de créer une carte visuelle claire montrant les postes de santé accessibles vs. non accessibles — 
et de la partager avec les décideurs le plus rapidement possible.


### 1. Filtrer les postes de santé depuis le jeu de données national des établissements de santé

Avant de vérifier quels établissements sont accessibles, Aina doit isoler les **postes de santé** à partir du jeu de données plus large de tous les établissements de santé.

1. **Charger le jeu de données des établissements de santé**  
   - Fichier : `hotosm_mdg_health_facilities_points.gpkg` (ou le GeoPackage utilisé)  
   - Chargez-le par glisser-déposer ou via `Couche` → `Ajouter une couche vecteur`.

2. **Ouvrir la table attributaire** et vérifier la colonne nommée `amenity`.

3. **Filtrer par expression** pour ne garder que les postes de santé :  
   - Clic droit sur la couche → `Filtrer…`  
   - Utiliser l’expression suivante :
     ```qgis
     "amenity" = 'health_post'
     ```

4. **Exporter la couche filtrée**  
   - Clic droit sur la couche filtrée dans le panneau des couches → `Exporter` → `Enregistrer les entités sous…`  
   - Format : `GeoPackage`  
   - Enregistrez dans votre dossier `project` sous :
     ```
     health_posts_only.gpkg
     ```
   - Cliquez sur `OK` pour confirmer l’exportation.

5. **Retirer le filtre** ou la couche originale de votre projet pour éviter toute confusion.

> 💡 **Astuce**: Filtrer directement dans QGIS vous permet de travailler avec un sous-ensemble spécifique sans modifier le jeu de données original.


### 2. Charger les couches isochrones pour les trois entrepôts CRM

Aina sait que seulement **trois entrepôts** disposent des fournitures médicales nécessaires:  
**Antananarivo**, **Maroantsetra**, et **Tolanaro**. Elle va maintenant charger les couches isochrones pour chacun de ces entrepôts afin de commencer l’analyse des zones desservies.

1. **Charger les couches isochrones individuelles** pour chaque entrepôt:
   - `CRM_warehouse_Isochrones_Antananarivo.gpkg`
   - `CRM_warehouse_Isochrones_Maroantsetra.gpkg`
   - `CRM_warehouse_Isochrones_Tolanaro.gpkg`

   Vous pouvez glisser-deposer chaque fichier dans QGIS ou aller dans `Couche` → `Ajouter une couche` → `Ajouter une couche vecteur`.


2. **Inspecter la table attributaire** de chaque couche isochrone  
   Vérifiez que chaque enregistrement possède un champ `traveltime_h` indiquant le temps de trajet estimé en **heures**.

3. **Retirer toutes les entités où le temps de trajet dépasse 10 heures**:  
   - Clic droit sur chaque couche → `Filtrer…`  
   - Appliquer l’expression:
     ```qgis
     "traveltime_h" <= 10
     ```

4. **Exporter chaque couche filtrée** vers le dossier `temp`:  
   À ce stade, Aina s’assure également que toutes les couches exportées utilisent le même SCR que la couche des postes de santé — `EPSG:4326` — pour éviter tout problème lors de la jointure spatiale.  
   - Enregistrez chaque fichier sous:
     ```
     CRM_isochrones_Antananarivo_upto10h.gpkg
     CRM_isochrones_Maroantsetra_upto10h.gpkg
     CRM_isochrones_Tolanaro_upto10h.gpkg
     ```

5. **Appliquer un style aux isochrones pour plus de clarté**  
   Aina peut appliquer un style prédéfini pour colorer la couche selon `traveltime_h` et visualiser différentes plages horaires (4h, 6h, 8h, 10h) à l’étape 5.
   - Clic droit sur chaque couche filtrée → `Propriétés` → `Symbologie`
   - Cliquez sur `Style` en bas → `Charger le style…`
   - Sélectionnez le fichier:  
     `CRM_warehouse_isochrones_style.qml`
   - Cliquez sur `Ouvrir`, puis `Appliquer` et `OK`

### 3. Visualiser l’accessibilité des postes de santé depuis les entrepôts CRM

Aina doit identifier quels postes de santé sont accessibles par la route à partir des trois entrepôts clés (Antananarivo, Maroantsetra et Tolanaro) **en moins de 10 heures de trajet**. Elle va le faire manuellement en combinant les isochrones 10h de ces entrepôts et en les comparant au jeu de données national des postes de santé.

1. **Fusionner les couches isochrones des trois entrepôts**  
   - Dans la **Boîte à outils de traitement**, rechercher `Fusionner des couches vecteur`.  
   - **Couches en entrée**:  
     - `CRM_isochrones_Antananarivo_upto10h.gpkg`  
     - `CRM_isochrones_Maroantsetra_upto10h.gpkg`  
     - `CRM_isochrones_Tolanaro_upto10h.gpkg`  
   - **SCR**: `EPSG:4326`  
   - **Enregistrer sous**:
     ```
     merged_isochrones_10h.gpkg
     ```
   - Cliquez sur **Exécuter**.

2. **Sélectionner les postes de santé accessibles en moins de 10 heures**  
   - Dans la **Boîte à outils de traitement**, rechercher `Sélection par localisation`.  
   - Définir les paramètres suivants:  
     - **Couche source**: `health_posts_only.gpkg`  
     - **Prédicat**: `intersects`  
     - **Couche d’intersection**: `merged_isochrones_10h.gpkg`  
   - Cliquez sur **Exécuter**.
   > 💡 Les points sélectionnés sont ceux situés dans les zones de desserte des entrepôts à moins de 10 heures.

3. **Créer un champ d’accessibilité pour les postes sélectionnés**  
   - Ouvrir la **calculatrice de champs** ![](/fig/mActionCalculateField.png) sur la couche `health_posts_only`.  
   - Cochez ✅ `Mettre à jour uniquement les entités sélectionnées`  
   - **Nom du champ de sortie**: `Reachability_time`  
   - **Type du champ de sortie**: `Texte (chaîne)`  
   - **Expression**:
     ```qgis
     'reachable in 10 hours'
     ```  
   - Cliquez sur **OK** pour créer et renseigner le champ pour les entités sélectionnées.

4. **Marquer les autres postes de santé comme non accessibles**  
   - Inverser la sélection:  
     Allez dans `Édition` → `Inverser la sélection` ![](/fig/mActionInvertSelection.png)  
     ou clic droit sur la couche → `Inverser la sélection`.
   - Ouvrez à nouveau la **calculatrice de champs**.  
   - Cochez ✅ `Mettre à jour uniquement les entités sélectionnées`  
   - Utiliser le même champ: `Reachability_time`  
   - **Expression**:
     ```qgis
     'not reachable in 10 hours'
     ```  
   - Cliquez sur **OK** pour appliquer la mise à jour.


> ✅ Tous les postes de santé sont maintenant étiquetés comme **accessibles** ou **non accessibles** dans la colonne `Reachability_time`.
