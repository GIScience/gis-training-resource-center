::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 1 : Estimation de la population exposée – Approche manuelle d’Aina

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

Cet exercice est le premier exercice de la piste d'exercice ["Analyse d’Action Anticipative pour les Cyclones à Madagascar"](/content/Exercise_tracks/fr_mdg_aa_cyclones.md)

:::

::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé pour l'exercice__
^^^

3 à 4 heures

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

## Téléchargement des données pour cet exercice

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_5_Exercise_8_AA_MDG_task_1-20250825T143512Z-1-001.zip

__Téléchargez les données pour cet exercice ici et dezipé le fichier.__
:::

Le dossier s'appelle __"__ et contient toute la [structure de dossier standard](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_management.html#standard-folder-structure) avec toutes les données dans le sous-dossier `/data/input/` et la documentation supplémentaire dans le dossier `/documentation/`. 

| Ensemble de données | Source | Descriptions |
| ----- | --- | --- |
| Frontières administrative | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Les limites administratives aux niveaux 0 à 4 pour Madagascar sont accessibles via HDX fourni par OCHA. Pour cette analyse, nous fournissons les limites administratives des niveaux 1 (régional) et 2 (district) au format shapefile. |
| Trajectoires des cyclones | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive)  | Le projet IBTrACS est la collection mondiale des cyclones tropicaux la plus complète  disponible. Il fusionne des données récentes et historiques provenant de plusieurs agences pour créer un jeu de données unifié, public  améliorant les comparaisons inter-agences.  |
| Établissements éducatifs et sites de santé| [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | Les données des lieux d'intérêts (établissements éducatifs et sites de santé) sont téléchargées via l'util "HOT Export Tool" basé sur les données du projet OpenStreetMap. |
| Population | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | L'ensemble de données WorldPop au format raster fournit le nombre estimé de personnes par cellule raster pour l’année 2020. Nous travaillerons avec l'ensemble de données des pays individuels contraints 2020 à une résolution de 100 m. | 



## Tâches

Avant de développer le modèle automatisé, Aina estimait manuellement la population exposée à chaque fois qu’un cyclone approchait de Madagascar.
Dans cette tâche, vous allez suivre les étapes qu’elle utilisait auparavant, en travaillant avec la trajectoire historique du Cyclone Harald, les données raster de WorldPop et les frontières administratives.

Vous allez tamponner manuellement la trajectoire du cyclone, découper le raster de population, puis calculer la population exposée à l’aide des statistiques zonales.


1. __Ouvrez QGIS__ et créez un [nouveau projet](/content/Wiki/en_qgis_projects_folder_structure_wiki.md#step-by-step-setting-up-a-new-qgis-project-from-scratch) en cliquant sur `Projet`-> `Nouveau Projet`.

2. __Enregistrez le projet__ dans le dossier `/project`: Cliquez sur `Projet` -> `Enregistrer sous...` et naviguez jusqu’au dossier. Nommez le projet "Cyclon_Harald_Exposure".

3. __Importer le fichier__ GeoJSON "example_Harald_2025_Track.geojson" dans votre projet en le glissant-déposant (Vidéo Wiki). Le fichier se trouve dans le dossier `/data/input`

4. __Reprojetez la trajectoire du cyclone__ pour utiliser des mètres au lieu de degrés (ceci est important pour un tampon précis):
    - Dans la __[Boîte à outils de traitement](https://giscience.github.io/gis-training-resource-center/content/Module_1/en_qgis_start.html?highlight=processing+toolbox#toolbox-toolbars)__, cherchez `Reprojeter une couche`.
    - Couche source: example_Harald_2025_Track
    - SCR cible : EPSG:29738 ou un autre SCR projeté en mètres adapté à Madagascar.
    - Enregistrez le résultat dans le dossier temp sous le nom: `Harald_Track_Reprojected`

```{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reprojeter la trajectoire du cyclone
```

```{Attention}
Les distances de tampon doivent être calculées en mètres. De nombreux jeux de données (comme les trajectoires de cyclone en GeoJSON) utilisent des systèmes de coordonnées géographiques (CRS/SCR) comme EPSG:4326, qui mesurent en degrés — et non en mètres. Pour calculer correctement un tampon de 200 km, il faut d’abord reprojeter la trajectoire dans un CRS projeté utilisant les mètres.
```
5. **Créer une zone tampon autour de la trajectoire du cyclone**:
   - Dans la __Boîte à outils de traitement__, cherchez `Tampon`.
   - Couche source: `Harald_Track_Reprojected`
   - Distance du tampon: `200000` (en mêtres)
   - Segments: Laisser par défaut (5)
   - Regrouper le résultat: `Oui`
   - Enregistrez la sortie dans le dossier `/data/temp/` sous le nom: `Harald_Buffer_200km`


:::{figure} /fig/fr_MDG_AA_cyclon_track_buffer.PNG
---
width: 600px
align: center
---
Tamponner la trajectoire du cyclone
:::


::::{dropdown} Résultat intermédiaire: Zone tampon
:::{figure} /fig/fr_MDG_AA_intermediate_result_cyclon_track_buffer.PNG  
---
width: 600px
align: center
---
Les résultats intermédiaires doivent montrer la trajectoire du cyclone et la zone tampon de 200 kilomètres autour de celui-ci. La zone tampon doit être une seule entité.
:::
::::

6. **Reprojeter la zone tampon en EPDG:4326 (pour correpondre au CRS/SCR de la couche raster)**


    - Dans la Boîte à outils de traitement, cherchez `Reprojeter une couche`
    - Couche source: `Harald_Buffer_200km_29738`
    - CRS/SCR cible (système de coordonnées de référence): `EPSG:4326 - WGS 84`.
    - Entregistrez le résultat dans le dossier `temp` sous le nom: `Harald_Buffer_200km_4326` 


```{figure} /fig/fr_MDG_AA_reproject_cyclon_buffer.PNG
---
width: 600px
align: center
---
Reprojetter la tamponner trajectoire du cyclone
```
   
7. **Importer les frontières administratives**:
    - Fichier: `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
    - Ajoutez le par glisser-déposer ou via `Couche` -> `Ajouter une couche` -> `Ajouter une couche vecteur...`.
8. **Importer la couche raster de population**:
    - Fichier: `MDG_WorldPop_2020_constrained.tif`
    - Ajouter la couche via `Couche` -> `Ajouter une couche` -> `Ajouter une couche raster...`.
9. **Couper le raster de population** à l'aide de la zone tampon:
    - Dans la __Boîte à outils de traitements__, cherchez `Découper un raster selon une couche de masque` (`Clip Raster by Mask Layer`).
    - Couche source: `MDG_WorldPop_2020_constrained`
    - Couche de masquage: `Harald_Buffer_200km_4326`
    - Découpé (masque): Enregistrez le résultat dans le dossier `/data/temp` sous le nom: `Harald_Pop_Clip`. 


```{figure} /fig/fr_MDG_AA_clip_pop_raster.PNG
---
width: 600px
align: center
---
Découpez la population ratser selon la zone affectée par le cyclone (trajectoire tampon du cyclone)
```
:::{dropdown} Résultat intermédiaire: Raster population découpé

```{figure} /fig/fr_MDG_AA_intermediate_result_clip_pop_raster.PNG
---
width: 600px
align: center
---
Résultat intermédiaire du découpage de la couche raster de population à l'étendue de la trajectoire tamponnée du cyclone.
```
:::

10. **Calculer la population exposée totale**:
    - Dans la __boîte à outils de traitements__, cherchez `Statistiques de zone` (eng.: `Zonal Statistics`)
    - Couche source (input layer): `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
    - Couche raster (raster layer): `Harald_Pop_Clip`
    - Préfixe de la colonne en sortie (Field prefix): par ex. `exposed_population_`
    - Statistiques à calculer: `Somme` (eng.: `Sum`)
    - Enregistrez la couche vecteur mise à jour dans le dossier `/data/results` sous le nom `Harald_Exposed_Population`. 
    - Le résultat sera une nouvelle couche avec les colonnes de la couche `mdg_admbnda_adm2_BNGRC_OCHA_20181031` et une nouvelle colonne tout à la droite affichant la population totale se trouvant dans la zone tampon du cyclone pour chaque district. 

```{figure} /fig/fr_MDG_AA_pop_zonal_statistic.PNG
---
width: 600px
align: center
---
Calcul de la population exposée aux cyclones par district sur la base du raster de population.
```
   
11. **Visualiser la population affectée en classifiant les résultats**: 
Maintenant qu'Aina a estimé la population exposée dans chaque district, elle souhaite mettre en évidence clairement les différences entre les régions sur la carte.  
Pour cela, nous allons appliquer une __[classification graduée]()__ à la couche `Harald_Exposed_Population` en utilisant la nouvelle colonne crée par l'outil de Statistiques de zone. 

- Dans le panneau **Panneau couche** en bas à gauche, faites un clic droit sur la couche `Harald_Exposed_Population` puis choisissez `Propriétés`. Une nouvelle fenêtre s'ouvrira.
- À gauche, naviguez à l'onglet __Symbologie__.
- En haut de la fenêtre, changez le style style de `Symbole Unique` à `Gradué`
- Pour la option `Valeur`, choisissez le champ contenant la somme de population. Il commence par le préfixe que vous avez défini auparavant, par exemple `exposed_population_sum`. 
- Choisissez une palette de couleur adaptée à votre carte (par exemple, `Reds`).
- Sélectionnez un __mode de classification__ (par exemple, `Nombres égal (Quantile)`, `Intervalles égaux` ou `Ruptures naturelles (Jenks)`) et indiquez le nombre de classes (par exemple 5). 
- Cliquez sur `Classer` pour générer la classification.
- En suite, cliquez sur `Appliquer` puis `OK` pour afficher la carte classifiée.


```{tip}
Vous pouvez ajuster les bornes des classes ou les étiquettes en double-cliquant sur chaque entrée de classe.
```

```{figure} /fig/fr_MDG_AA_pop_graduadt_classification_exposed_population.PNG
---
width: 600px
align: center
---
Configuration de la visualisation de la population exposée en cinq classes. 
```

Vos résultats devraient ressembler à ceci:

```{figure} /fig/fr_MDG_AA_intermediate_result_visualisation_exposed_population.PNG
---
width: 600px
name: mdg_visualiser_pop_exposee
align: center
---
Visualisation de la population exposée en cinq classes.
```
