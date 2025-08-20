::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Exercice 1: Automatisation

🚧Cette partie de la plateforme de formation est en construction et ne peut pas être partagée ou publée! 🚧

## Caractéristiques de l'exercise



::::{grid} 2
:::{grid-item-card}
__Type d'exercice:__
^^^

- Cet exercice peut être utilisé dans le cadre de formations en ligne ou en présentiel.
- Il peut être réalisé en tant qu'exercice guidé ou individuellement en auto-apprentissage.

:::

:::{grid-item-card}


:::

::::

::::{grid} 2
:::{grid-item-card}
__Temps estimé pour l'exercice__
^^^


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
Aina, l'experte GIS (SIG) de la Croix-Rouge malgache (CRM), se prépare pour la prochaine saison des cyclones. Elle souhaite eméliorer la capacité de réaction de son équipe une fois un tempête annoncée, en automatisant des analyses clés dans la application QGIS. 
Celles-ci incluent l'estimation des populations exposées, l'identification des services impactés comme la santé et l'education, et l'évaluation de l'accessibilité des postes de santé à partir des entrepôts de la croix rouge dans une fenêtre critique de 10 heures. 
L'objectif est de préparer un workflow d'analyse et de visualisation pour soutenir une action anticipée (eng.: Anticipatory Action) et fondée sur les données, avant que le cyclone ne touche terre. 


:::

## Instruction pour les formateurs



:::{dropdown} __Trainers Corner__ 

### Préparer la formation

- Prenez du temps pour vous familiariser avec l'exercice et le matériel founi. 
- Préparez und tableau blanc. Cela peut être un tableau physique, un paperboard (tableau blanc virtuel, e.g., Miro Board) où les participant·es peuvent ajouter leurs observations et questions. 
- Avant de commencer l'exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et dézippé__ le dossier de données.
- Consultez [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) pour des conseils généraux sur la conduite de formations (ce matériel est en anglais).


### Animer la formation

__Introduction:__

- Présentez l'idée et l'objectif de l'exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a bien dézippé le dossier avant de commencer les tâches.

__Exercice guidée:__

- Montrez et expliquez chaque étape cous-même au moins deux fois, et suffisamment lentement por que chacun·e puisse voir ce que vous faites et reproduire les étapes dans sons prope projet QGIS.
- Assurez-vous que tout le monde suit en demandant régulièrement si quelqu'un a besoid d'aide ou si tout le monde suit toujours.
- Soyez ouvert·e et patient·e face aux questions ou problèmes éventuels. Vos participant·es sont en train de faire plusieures choses à la fois: écouter vos instructions tout en s'orientant dasn leur propre projet QGIS.

### Fin de la formation

- Prévoyez du temps à la fin pour répondre aux questions ou aborder les éventuels problèmes rencontrés lors de tâches.
- Laissez un moment pour des questions ouvertes.

:::

## Données

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip

__Téléchargez toutes les données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip), enregistrez le dossier sur votre ordinateur et dézippez le fichier.__ 

:::

Le dossier s'appelle __"__ et contient toute la [structure de dossier standard](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_management.html#standard-folder-structure) avec toutes les données dans le sous-dossier `/data/input/` et la documentation supplémentaire dans le dossier `/documentation/`. 


 with all data in the input folder and the additional documentation in the documentation folder.

| Ensemble de données | Source | Descriptions |
| ----- | --- | --- |
| Frontières administrative | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Les limites administratives aux niveaux 0 à 4 pour Madagascar sont accessibles via HDX fourni par OCHA. Pour cette analyse, nous fournissons les limites administratives des niveaux 1 (régional) et 2 (district) au format shapefile. |
| Trajectoires des cyclones | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive)  | Le projet IBTrACS est la collection mondiale des cyclones tropicaux la plus complète  disponible. Il fusionne des données récentes et historiques provenant de plusieurs agences pour créer un jeu de données unifié, public  améliorant les comparaisons inter-agences.  |
| Établissements éducatifs et sites de santé| [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | Les données des lieux d'intérêts (établissements éducatifs et sites de santé) sond téléchargées via l'util "HOT Export Tool" basé sur les données du projet OpenStreetMap. |
| Population | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | L'ensemble de données WorldPop au format raster fournit le nombre estimé de personnes par cellule raster pour l’année 2020. Nous travaillerons avec l'ensemble de données des pays individuels contraints 2020 à une résolution de 100 m. | 




:::{card} 
__Contexte__
^^^

```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

__Aina__ est l’experte GIS (SIG) à la __Croix-Rouge Malagasy (CRM)__. Avec l’arrivée de la saison cyclonique, elle sait que chaque minute compte dès qu’une tempête est annoncée. Chaque heure est précieuse pour protéger les communautés à risque.

Cette année, Aina veut prendre une longueur d’avance. Plutôt que d’analyser manuellement les données cycloniques sous pression, elle décide de préparer un modèle QGIS automatisé qui l’aidera à réagir rapidement et efficacement.

**Son objectif**  
> Construire un workflow qui estime automatiquement les populations exposées et les infrastructures à risque.

:::

```{figure} /fig/Module_7/en_ex_m7_cylone_automatisation.drawio.png
---
name: Task_1_workflow
width: 750 px
---

```

## Tâche 1 : Estimation de la population exposée – Approche manuelle d’Aina

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
    - Ajoutez_le par glisser-déposer ou via `Couche` -> `Ajouter une couche` -> `Ajouter une couche vecteur...`.
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


## Tâche 2: Automatisation de l’estimation de la population exposée – Le modèle d’Aina

Après avoir estimé manuellement les populations exposées lors des saisons cycloniques précédentes, Aina a décidé de créer un __modèle automatisé__ à l’aide du __Modeleur Graphique de QGIS__.
Cela lui permettra d’agir plus rapidement et d’éviter de répéter les mêmes étapes à chaque fois qu’un cyclone est annoncé.

Dans cette tâche, vous allez aider Aina à construire une version simple de ce modèle, en réutilisant les outils de la Tâche 1. Le modèle doit effectuer les étapes suivantes:

- Reprojeter la trajectoire du cyclone en EPSG:29738
- Créer une zone tampon autour de cette trajectoire  
- Reprojeter la zone tampon en EPSG:4326
- Découper le raster de population  
- Appliquer les statistiques zonales pour obtenir la population exposée par district

---

1. **Ouvrir le modeleur**:
   - Ouvrez le modeleur depuis le menu du haut: `Traitement` (`Processing`) -> `Modeleur` (`Graphic Modeler`)   
     `Processing` → `Graphical Modeler…`

2. **Nommer le modèle**:   
    - Une nouvelle fenêtre s'ouvrira. À gauch, vous trouvez le panneau `Propriétes du modèle`. Ici, vous pouvez definir les informations du modèle: 
        - **Nom du modèle**: `Estimation_Population_Exposée`
        - **Groupe**: `Outils d'analyse cyclones`
        - Laissez la description vide ou ècrivez: *Modèle automatisé pour estimer la population exposée a partir d'un tampon autour du cyclone*.


3. **Enregistrer le modèle:**
   - Pour enregistrer le modèle:
     - Cliquez sur l'icône __Enregistrer__ (💾) ou naviguez à `Modèle` -> `Enregistrer`. 
     - Naviguez jusqu'au dossier `/models/` de votre structure de dossier pour la formation
     - Enregistrer le modèle sous: `Esimation_Population_Exposée`.


4. **Ajouter les entrées du modèle**:  
  - Dans le panneau gauche, ouvrez la section __Entrées__.
  - Ajouter les couches d'entrées en cliquant sur `+ Couche Vecteur` (`+ Vector Layer`) et `+ Couche Raster` (`+ Raster Layer`) On the **left panel**, expand the **Inputs** section.
  - Add the following input layers with type constraints:
    - `+ Couche Vecteur`  
      - **Description**: `Trajectoire du cyclone`  
      - Type de géometrie: `Ligne`
    - `+ Couche Raster`
      - **Description**: `Raster Population`
    - `+ Couche Vecteur`  
      - **Description**: `Frontières adminitratives`
      - Type de géometrie: `Polygone`
  - Ces couches apparaîtront en haut du canevas du modèle et serviront de données d'entrée lorsque le modèle sera exécuté.

     ```{tip}
     Toutes les entrées doivent être définies comme **obligatoires**, afin que le modèle dispose toujours des données nécessaires pour s’exécuter correctement.
     ```

::::{tab-set}

:::{tab-item} Entrée: trajectoire du cylcone
```{figure} /fig/fr_MDG_AA_model_input_cyclon_track.PNG
---
width: 600px
align: center
---
Ajouter la entrée couche vecteur pour la trajectoire du cyclone
```
:::

:::{tab-item} Entrée: Frontières administratives
```{figure} /fig/fr_MDG_AA_model_input_admin_bounderies.PNG
---
width: 600px
align: center
---
Ajouter la entrée couche vecteur pour les frontières administratives
:::

:::{tab-item} Entrée: Raster Population
```{figure} /fig/fr_MDG_AA_model_input_population_raster.PNG
---
width: 600px
align: center
---
Ajouter la couche raster pour les données de population
```
:::
::::
**Résultat intermédiaire:**

```{figure} /fig/fr_MDG_AA_intermediate_result_model_input.PNG
---
width: 600px
name: mdg_modele_resultat_intermed
align: center
---
Résultat intermédiaire de la définition des données d'entrée du modèle
```

5. **Reprojetter la trajectoire du cyclone vers EPSG:29738** 
  - Dans le panneau de **Algorithmes** a gauche, cherchez **Reprojeter une couche** et faites un double-clic dessus.
  - Dans la fenêtre de configuration: 
    - Ajouter une description: `Reprojeter la couche de trajectoire du cyclone à EPSG:29738`
    - Définissez la **Couche source** sur `Trajectoir du cyclone` (depuis Entrée du modèle).
    - Définissez la SCR cible sur `EPSG:29738 - Tananarive / UTM zone 38 S`
    - Cliquez sur `OK` pour ajouter l'étape au model. 

```{figure} /fig/fr_MDG_AA_model_reporject_cyclon_track.PNG
---
width: 600px
name: mdg_reproj_cyclone_track
align: center
---
Reprojeter la couche du trajectoire du cyclone vers un système de référence de coordonnées métrique (SCR) EPSG : 29738
```

6. **Tamponner la trajectoire du cyclone reprojetée**  
   - Dans le panneau **Algorithmes**, cherchez `Tampon` (eng.: `Buffer`)
   - Dans la fenêtre de configuration:
    - Ajoutez une description: `Tamponner la trajectoire du cyclone reprojetée`
    - Choisissez, comme couche source, le résultat de l'étape précedente (sous l'option `Sortie d'un algorithme` -> `"Reprojeté" créé par l'algorithme "Reprojeter la couche de trajectoire du cyclone à EPSG:29738"`).
    - Définissez la distance du tampon à `200000` (200 km). 
    - Laissez les __segments__ à la valeur par défaut (`5`).
    - Regrouper le résultat: `Oui`.
    - Cliquez sur `OK`. L'algorithme sera ajouter au modèle. 

```{figure} /fig/fr_MDG_AA_model_buffer_cyclon_track.PNG
---
width: 600px
name: fr_mdg_tamponner_cyclone
align: center
---
Ajouter l'étape pour tamponner la couche Cyclone reprojetée
```

7. **Reprojeter le tampon vers le SCR du projet (EPSG:4326)**
  - Dans le panneau **Algorithmes**, cherchez `Reprojeter une couche` (eng.: `Reproject vector layer`).
  - Dans la fenêtre de configuration:
    - Ajoutez une description: `Reprojeter le tampon ver EPSG:4326`.
    - Choisissez, comme couche source, le résultat de l'étape prècedente (sous l'option `Sortie d'un algorithme` -> `"Mis en tampon" créé par l'algorithme "Tamponner la trajectoire du cyclone reprojetée"`)
    - SCR cible: `EPSG: 4326 - WGS 84`
    - Cliquez sur `OK` pour ajouter l'étape au modèle. 

```{figure} /fig/fr_MDG_AA_model_reporject_bufferd_cyclon_track.PNG
---
width: 600px
name: mdg_reprojeter_tampon_cyclone
align: center
---
Reprojeter le tampon vers EPSG:4326
```


8. **Découper la couche raster de population avec le tampon du cyclone**  
   - Dans le panneau **Algorithmes**, cherchez `Découper un raster selon une couche de masque` (eng.: `Clip Raster by Mask Layer`)
   - Dans la fenêtre de configuration:
    - Ajoutez une description: `Decouper la couche raster de population avec le tampon du cyclone`.
    - Comme __"Couche source"__, choisissez la Entrée `Raster Population`
    - Comme __"Couche de Masquage"__, choisissez le tampon du cyclone (sous `Sortie d'un algorithme` -> `"Mis en tampon" créé par l'algorithme "Tamponner la trajectoire du cyclone reprojetée"`)
    - Laissez la sortie de l'algorithme (`reprojeté`) vide.
    - Cliquez sur `OK` pour ajouter l'étape au modèle.

```{figure} /fig/fr_MDG_AA_model_clip_pop_raster.PNG
---
width: 600px
name: mdg_model_clip_pop_raster
align: center
---
Découper la couche raster de population pour l'étendre au tampon Cyclon
```

9. **Calul de la population exposée aux cyclone par district**
  - Dans le panneau **Algorithme**, cherchez pour l'outil `Statistiques de zone` (eng.: `Zonal Statistics`) et ouvrez le. 
  - Dans la fenêtre de configuration:
    - Ajoutez une description: `Calcul de la population exposée aux cyclone par district` 
    - Comme __"Couche source"__, choisissez la couche "Frontières administratives`.
    - Comme __"Couche raster"__, choisissez le raster découpé (sous `Sortie d'un algorithme` -> `"Découpé (masque)" créé par l'algorithme "Decouper la couche raster de population avec le tampon du cyclone"`)
    - Définissez le __préfixe de la colonne en sortie__ comme `exposed_population_`
    - Sous __statistiques à calculer__, choisissez `Somme` (eng.: `Sum`).
    - Sous __statistiques de zones__, ajoutez un nombre pour la sortie de l'algorithme:
      ```
      exposed_population_sum
      ```
    - Cliquez sur `OK` pour ajouter l'étape au modèle.

```{figure} /fig/fr_MDG_AA_model_zonal_statistic_pop_admin2.PNG
---
width: 600px
name: mdg_statistiques_de_zone
align: center
---
Calcul de la population exposée aux cyclones par district utilisant l'algorithme "Statistiques de zone".
```

**Vos résultats devraient ressembler à ceci:** 

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms.PNG
---
width: 600px
name: fr_resultat_modele
align: center
---
Votre modèle devrait ressembler à ceci. Tous les algorithmes sont correctement connectés et la sortie du modèle est définie.
```

10. **Valider le modèle (recommandé)**
  - Avant d'enregistrer ou exécuter le modèle. Dans le menu en haut de la fenêtre, cliquez sur `Modèle` -> ✔️  `Valider le modèle`.  
  - Corrigez les èventuels avertissements ou erreurs affichés dans le panneau de journal. 
  - Cela permet de s'assurer que le modèle est complet et qu'il s'exécutera sans erreur.

11. **Exécuter le modèle**
  - Exécutez le modèle: Dans le menu en haut de la fenêtre, cliquez sur `Modèle` -> `Exècuter le modèle...`
    - Maintenant, vous devez définir les __Couches Source__ pour le modèle. Vous pouvez choisir les couches que vous avez importées dans votre projet QGIS.
    - Sous __Frontières Administratives__, choisissez: 
      `mdg_admbnda_adm2_BNGRC_OCHA_20281031.gpkg`
    - Sous __Raster Population__, choisissez:
      `MDG_WorldPop_2020_constrained.tif`
    - Sous __Trajectoire Cyclone__, choisissez:
      `example_Harald_2025_Track`
    - Definissez la sortie du modèle __"exposed_population_sum"__ comme: `Harald_Exposed_Population` et engeristrez-le dans le dossier `/data/output/` en cliquant sur les trois points ![](/fig/3.36_three_dots.png).
    - Cliquez sur `Éxecuter`.


Vous pouvez désormais exécuter ce modèle chaque fois qu’une nouvelle trajectoire de cyclone est disponible.

```{figure} /fig/fr_MDG_AA_model_run_model_M7_e1_task2.PNG
---
width: 600px
align: center
---
Pour exécuter le modèle, spécifiez l'entrée comme indiqué dans l'image et définissez le nom de la couche de sortie.
```

**Vos résultats devraient ressembler à ceci:**
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_basics.PNG
---
width: 600px
name: mdgtask_model_result
align: center
---

``` 
12. **Ajouter le tampon du cyclone comme sortie supplémentaire du modèle**  
  - Faites un double-clic sur l'algorithme __"Reprojeter le tampon vers EPSG:4326"__ pour ouvrir sa configuration.
  - Dans le champ `Reprojecté`, entrez un nom pour la sortie du modèle, comme: `cyclone_harald_buffer`
  - Cliquez sur `OK` pour enregistrer la modification. 
  - Maintenant, le modèle va produire à la fois les résultats de population exposée __et__ la zone tampon du cyclone lors de son exécution. 

```{figure} /fig/fr_MDG_AA_model_output_buffer.PNG
---
width: 600px
name: mdg_model_add_buffer_output
align: center
---
```

13. **Exécuter à nouveau le modèle**  
  - Exécutez le modèle en cliquant sur `Modèle` -> `Exécuter le modèle...`.
    - Sous __Frontières Administratives__, choisissez: 
      `mdg_admbnda_adm2_BNGRC_OCHA_20281031.gpkg`
    - Sous __Raster Population__, choisissez:
      `MDG_WorldPop_2020_constrained.tif`
    - Sous __Trajectoire Cyclone__, choisissez:
      `example_Harald_2025_Track`
    - Definissez la sortie du modèle __"exposed_population_sum"__ comme: `Harald_Exposed_Population` et engeristrez-le dans le dossier `/data/output/` en cliquant sur les trois points ![](/fig/3.36_three_dots.png).
    - Sous __cyclone_harald_buffer__, cliquez sur les trois points et naviguez au dossier `/data/output/` et nommez la sortie comme `cyclone_harald_buffer`. 
    - Cliquez sur `Éxecuter`.


::::{tab-set}


:::{tab-item} Le modèle modifié

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_graphic.PNG
---
width: 600px
name: the_world_result
align: center
---
Le modèle modifié devrait resembler à ceci. 
```

:::

:::{tab-item} Exécuter le modèle avec la nouvelle sortie
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_model_exicution.PNG
---
width: 600px
align: center
---
```
:::

:::{tab-item} Model Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_extended_buffer.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
```
:::

::::



## Tâche 3: Identification des établissements de santé et d'éducation impactés – Aina ajoute des couches supplémentaires

Après avoir construit son modèle pour estimer la population exposée, Aina souhaite améliorer son utilité. Elle décide d'identifier également les services essentiels affectés par les cclones — en particulier les établissments de santé et les écoles. 

Elle veut non seulement savoir quels établissements sont affectés, mais aussi combien il en existe au total par district. Cela lui permettera de calculer le __pourcentage de service affectés dans chaque zone. 

Pour cela, elle utilisera deux jeux de données contenant des points issus d'OpenStreetMap:

- [Établissement de santé](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)
- [Établissement d'éducation](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

1. **Importer les données des établissements de santé et d'éducation**
  Tout d'abord, examinons les données avec lesquelles nous allons travailler:
    - Accédez à votre dossier `Data/input/`
    - Glissez-déposez les couches suivantes dans votre projet QGIS:
      - `hotosm_mdg_health_facilities`  
      - `hotosm_mdg_education_facilities` 
    - Vérifiez que les deux couches sont visibles dans __le panneau Couches__. 
2. **Save your model under a new name**  
  - Ouvrez votre modèle existant `Estimate_Exposed_Population.model3.`
  - Immédiatement, enregistrez-le sous un nouveau nom:
  - Cliquez sur `Modèle` → `Enregistrer le modèle sous…`
  - Enregistrez-le dans le dossier `/project` sous le nom: 
  ```
  estimate_exposed_population_health_education 
  ```

3. **Ajouter de nouvelles entrées dans le modèle**  
  - Dans la section __Entrées__ a gauche, ajoutez:
    - `Couche vecteur`:
      - __Description:__
      ```
      Établissements de santé
      ```
      - __Type de géometrie__: `Point`
    - `Couche vecteur`:
      - __Description__:
      ```
      Établissements d'éducation  
      ```
      - __Type de géometrie__: `Point`

::::{tab-set}

:::{tab-item} Entrée: établissements de santé
```{figure} /fig/fr_MDG_AA_model_input_health_facilities.PNG
---
width: 300px
name: the_world_result
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements de santé
```
:::
:::{tab-item} Entrée : établissements d’enseignement
```{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements d'enseignement
```
:::
::::

3. **Compter tous les établissements de santé par district (ADM2)**
  - Dans le panneau **Algorithmes**, cherchez `Compter les points dans les polygones`
  - Configuration: 
    - Description: `Comptez le nombre d’établissements de santé dans chaque district`
    - __Polygones__: `Frontières administratives` (sous entrées du modèle)
    - __Points__: `Établissements de santé` (sous entrées du modèle)
    - **Nom du champ de dénombrement**: 
    `count_health_total`
    - Laisser la sortie vide.
```{figure} /fig/fr_MDG_AA_model_count_points_HF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements de santé dans chaque district.
```    
4. **Compter tous les établissements d’enseignement par Admin 2**  
   - Ajouter une autre étape **Compter les points dans un polygone**.
   - Configuration :
     - Ajouter une description : `Comptez le nombre d'établissements d’enseignement dans chaque district`
     - **Polygones** : `Limites administratives` (entrée du modèle)
     - **Points** : `Établissements d’enseignement` (entrée du modèle)
     - **Nom du champ de dénombrement**: 
      ```
      count_education_total
      ```
     - Laissez la sortie vide

```{figure} /fig/fr_MDG_AA_model_count_points_EF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements scolaires dans chaque district.
```
5. **Intersection des établissements de santé avec la zone tampon du cyclone**  
   - Depuis le panneau **Algorithmes**, recherchez **Intersection**.
   - Dans la fenêtre de configuration :
   - Ajouter une description : 
      ```
      Établissements de santé dans la zone d'impact du cyclone
      ```  
     - **Couche source** : `Établissements de santé` (entrée du modèle)
     - **Couche de superposition** : zone tampon du cyclone (utiliser “Reprojected to EPSG:4326” depuis la **Sortie d’algorithme**)
     - Laissez la sortie vide. 
   - Cliquez sur **OK** pour ajouter l'étape au modèle.
```{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de santé avec la zone d'impact du cyclone.
```
6. **Intersection des établissements d’éducation avec la zone tampon du cyclone**  
   - Ajouter un autre algorithme **Intersection**.
   - Configuration :
     - Ajouter une description :
       ```
       Établissements d’éducation dans la zone d'impact du cyclone.
       ```  
     - **Couche source** : `Établissements d’éducation` (entrée du modèle)
     - **Couche de superposition** : zone tampon du cyclone (utiliser “Reprojected to EPSG:4326” depuis la **Sortie d’algorithme**)
     - Laisser la sortie vide. 
   - Cliquer sur **OK** pour ajouter l'étape au modèle. 
```{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de education avec la zone d'impact du cyclone.
```
7. **Compter les établissements de santé affectés par Admin 2**  
   - Ajouter **Compter les points dans un polygone**
   - Configuration :
     - Ajouter une description : 
       ```
       Compter les établissements de santé touchés par district
       ```  
     - **Polygones** : sortie du décompte total des établissements de santé
     - **Points** : sortie des établissements de santé intersectés
     - **Nom du champ de dénombrement** : 
       ```
       sum_exposed_healthsites_POI
       ```  
     - Cliquez sur **OK** pour ajouter l'étape au modèle.

```{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
8. **Compter les établissements d’enseignement affectés par Admin 2**  
   - Ajouter **Compter les points dans un polygone**
   - Configuration :
     - Ajouter une description : 
       ```
       Compter les établissements d’enseignement touchés par district
       ```   
     - **Polygones** : sortie du décompte total des établissements d’enseignement
     - **Points** : sortie des établissements d’éducation intersectés
     - **Nom du champ de dénombrement** : 
       ```
       sum_exposed_education_POI
       ```  
     - Cliquez sur **OK** pour ajouter l'étape au modèle.
```{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
9. **Calculer le pourcentage d’établissements de santé affectés**
Pour calculer le pourcentage d’établissements de santé affectés par zone administrative, utilisez la **Calculatrice de champ** :
- Ajouter la **Calculatrice de champ** :
   - Configuration :
     - Ajouter une description :
       ```
       Calculer le pourcentage d’établissements de santé touchés par district
       ```  
    - **Couche en entrée** : sortie du comptage des établissements de santé affectés
    - **Nom du champ de sortie** :  
       ```
       pct_health_affected
       ``` 
    - **Type de champ** : Décimal (réel)
    - **Expression** :
    ```qgis
    CASE WHEN "count_health_total" > 0
    THEN "sum_exposed_healthsites_POI" / "count_health_total" * 100
    ELSE
    ```
    - Définir la sortie comme **Sortie du modèle**
    - Nommer :
   ```
   admin2_health_affected_pct
   ```

```{figure} /fig/fr_MDG_AA_model_field_calc_pct_health_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements de santé touchés par district.
```


10. **Calculer le pourcentage d’établissements d’enseignement affectés**
Pour calculer le pourcentage d’établissements d’enseignement affectés par zone administrative, utilisez la **Calculatrice de champ** :  
- Ajouter la **Calculatrice de champ** :  
   - Configuration :  
     - Ajouter une description :  
       ```
       Calculer le pourcentage d’établissements d’éducation touchés par district
       ```  
     - **Couche en entrée** : sortie du comptage des établissements d’éducation affectés  
     - **Nom du champ de sortie** :  
       ```
       pct_education_affected
       ```  
     - **Type de champ** : Décimal (réel)  
     - **Expression** :  
       ```qgis
       CASE WHEN "count_education_total" > 0
       THEN "sum_exposed_education_POI" / "count_education_total" * 100
       ELSE 0
       END
       ```  
   - Définir la sortie comme **Sortie du modèle**  
   - Nommer :  
     ```
     admin2_education_affected_pct
     ```


```{figure} /fig/fr_MDG_AA_model_field_calc_pct_education_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération : calculer le pourcentage d’établissements d’éducation touchés par district.
```

11. **Valider et enregistrer votre modèle étendu**  
   - Cliquez sur le bouton ✔️ **Valider le modèle** (sous `Modèle` dans le menu en haut) pour vérifier les erreurs.
   - Enregistrez à nouveau sous :  
     **`Estimate_Exposed_Population_Health_Education.model3`**

11. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**

12. **Exécuter le modèle**
   - Cliquez sur le bouton ▶️ **Exécuter** en haut de la fenêtre du Modélisateur Graphique.
   - Dans la boîte de dialogue :
     - Sélectionnez les couches d’entrée nécessaires :
       - `Trajectoire du cyclone` → sélectionnez le fichier GeoJSON du cyclone (ex. `Harald_2025_Track.geojson`)
       - `Raster de population` → sélectionnez le raster WorldPop
       - `Limites administratives` → sélectionnez la couche Admin 2 (ex. `MDG_adm2.gpkg`)
       - `Établissements de santé` → sélectionnez la couche ponctuelle des établissements de santé
       - `Établissements d’enseignement` → sélectionnez la couche ponctuelle des écoles
     - Choisissez un emplacement pour enregistrer les couches finales (vous pouvez laisser les couches intermédiaires en mémoire temporaire):
     - **Sorties:**
     -  Enregistrez les couches de sorties dans le dossier `/data/output` comm ceci: 
        - __"exposed_population_sum"__ comme `Harald_Exposed_Population`
        - __"example_Harald_2025_Track"__ comme `cyclone_harald_buffer`. 
        - __"admin2_health_affected_pct"__ comme `admin2_health_affected`
        - __"admin2_education_affected_pct"__ comme `admin2_education_affected`

   - Cliquez sur **Exécuter** pour lancer le modèle complet.
   - Une fois terminé, toutes les couches finales seront affichées dans votre espace de travail QGIS.
::::{tab-set}

:::{tab-item} Modeleur

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model.PNG
---
width: 600px
align: center
---
Vue d’ensemble du Modèle Graphique de la tâche 3 montrant tous les algorithmes connectés et les sorties définies.
```
:::
:::{tab-item}  Configuration de l’exécution du modèle
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_run_configurations.PNG
---
width: 600px
align: center
---
Configuration des paramètres pour exécuter le modèle de la tâche 3 avec toutes les couches d’entrée requises.
```
:::
:::{tab-item} Sortie du modèle
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model_results_AT.PNG
---
width: 600px
align: center
---
Résultats du modèle de la tâche 3 affichés dans QGIS, y compris les pourcentages d’établissements de santé et d’éducation touchés par district.
```
:::
::::


## Tâche 4 : Visualiser les résultats de l’impact du cyclone – Aina applique des styles à ses cartes

Après avoir terminé son modèle, Aina souhaite **communiquer clairement les résultats** — à la fois à ses collègues de la Croix-Rouge et à des partenaires externes.

Elle en a **assez de devoir restyler manuellement chaque couche** à chaque fois que de nouvelles données cycloniques arrivent. À la place, elle veut :
- ✅ **Des visuels clairs et cohérents**
- 🔁 **Des modèles réutilisables**
- 📂 **Des fichiers .qml standardisés** partagés entre projets

Dans cette tâche, vous allez aider Aina à appliquer des styles `.qml` existants et à en créer de nouveaux pour les couches qui n’ont pas encore de style défini.

---


### 1. **Charger les couches nécessaires (si ce n’est pas déjà fait)**

Assurez-vous que les couches suivantes sont déjà chargées dans votre projet QGIS. Ce sont les sorties de la **Tâche 3** :

- `Harald_2025_Track`
- `Harald_Buffer_200km`
- `Harald_Exposed_Population`
- `sum_exposed_healthsites_POI`
- `sum_exposed_education_POI`
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

Si l’une d’elles manque :
- Chargez-la par **glisser-déposer** depuis votre dossier `results`, ou
- Utilisez `Couche` → `Ajouter une couche` → `Ajouter une couche vectorielle` ou `Ajouter une couche raster`

---

### 2. **Appliquer des fichiers de style prédéfinis**
Appliquez les fichiers de style `.qml` suivants aux couches correspondantes :

| **Couche**                             | **Fichier de style**                           |
|----------------------------------------|------------------------------------------------|
| `Harald_2025_Track`                    | `storm_track_cyclone_style.qml`               |
| `Harald_Buffer_200km`                  | `exposed_cyclone_area_style.qml`              |
| `Harald_Exposed_Population`            | `exposed_population_style.qml`                |
| `sum_exposed_healthsites_POI`          | `exposed_healthsites_style.qml`               |
| `sum_exposed_education_POI`            | `exposed_education_facilities_style.qml`      |



## Task 4: Visualizing Cyclone Impact Results – Aina Styles Her Layers

Aina now has all the analysis results she needs — but numbers and tables alone won’t convince her colleagues or decision-makers. What they need are clear and easy-to-read maps that can be used directly in meetings and reports.

To save time, Aina doesn’t want to adjust colors and legends manually each time a new cyclone comes in. Instead, she will use ready-made style files (.qml) that instantly give layers a professional and consistent look. Where no style exists yet, she will create one herself, so that next time the map can be updated with just a few clicks.

In this task, you will help Aina make her cyclone impact maps both informative and visually compelling by applying and creating QGIS style files.

### 1. **Load Required Layers (if not already loaded)**

Make sure the following layers are already loaded into your QGIS project. These are outputs from **Task 3**:

- `example_Harald_2025_Track`
- `cyclone_harald_buffer`
- `Harald_Exposed_Population`
- `admin2_health_affected`
- `admin2_education_affected`

If any are missing:
- Load them using **drag & drop** from your `results` folder, or
- Use `Layer` → `Add Layer` → `Add Vector Layer` or `Add Raster Layer`

---

### 2. **Apply Predefined Style Files**
Apply the following`.qml` style files to the respective layers:

| **Layer**                              | **Style File**                            |
|----------------------------------------|-------------------------------------------|
| `example_Harald_2025_Track`                    | `storm_track_cyclone_style.qml`           |
| `cyclone_harald_buffer`                  | `exposed_cyclone_area_style.qml`          |
| `Harald_Exposed_Population`            | `exposed_population_style.qml`            |
| `admin2_health_affected`          | `exposed_healthsites_style.qml`           |
| `admin2_education_affected`            | `exposed_education_facilities_style.qml`  |

```{note}
⚠️ For the **health** and **education facilities**, the provided style files are linked to the column containing the **sum of exposed facilities**.  
They are **not** based on the percentage column.  
```


**Steps:**
- Right-click on the layer in the **Layers Panel**  
- Select **Properties**  
- In the window that opens, go to the **Symbology** tab  
- At the bottom left, click **Style** → **Load Style…**
- Click on the three points ![](/fig/Three_points.png)  
- Navigate to the corresponding `.qml` file in the folder `layer_sytle`and select it  
- Click **Open**, then **Apply** and **OK** to confirm  

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_output_style.mp4"></video>

> 💡 *If the style doesn’t load correctly, double-check the column names and make sure the column name used in the `.qml` file matches the one in your layer. To do this, open the **Attribute Table** of the layer and compare field names.*

---


::::{tab-set}

:::{tab-item} Intermediate result: Exposed Population

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_pop_style.PNG
---
width: 600px
align: center
---
Carte montrant le nombre de personnes exposées par district après l’application du style .qml.
```
:::
:::{tab-item} Intermediate result: Exposed Health Facilities
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_HS_sum_style.PNG
---
width: 600px
align: center
---
Carte indiquant le nombre total d’établissements de santé exposés par district, représentés avec le style prédéfini.
```
:::
:::{tab-item} Intermediate result: Exposed Education Facilities
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_ES_sum_style.PNG
---
width: 600px
align: center
---
Carte affichant le nombre total d’établissements scolaires exposés par district, après application du fichier de style .qml.
```
:::
::::



### 3. **Style Percentage Layers Manually**

Aina also wants to visualise the percentage of exposed health and education facilities. However, since there is no prepared style available, she must complete the process manually.

**Steps:**
- **Right-click** on the layer `admin2_health_affected` → select **Duplicate Layer**  
- **Rename** the duplicated layer to:
  ```
  admin2_health_affected_percentage
  ```
- Right-click on the layer in the **Layers Panel**  
- Select **Properties**  
- In the window that opens, go to the **Symbology** tab  
- Set **Symbology** to `Graduated`
- Choose the correct **field**:
  - `pct_health_affected`
- Open the **Histogram** tab to view the value distribution by clicking on `calculate histogram`
- Next go back to `Classes` and set the following configuration:
  - **Mode**: `Equal Interval`
  - **Classes**: `4`
- Click `OK`.This will create four classes (`0–25%`, `25–50%`, `50–75%`, `75–100%`)
- Choose a color ramp (e.g., light yellow → dark red)
- Optionally customize class labels for clarity
- Click `Apply`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_affacted_HS_pct.mp4"></video>

- Repeat the same process for the layer `admin2_education_affected`.
After duplicating the layer, rename the new one to:
 ```
 admin2_health_affected_percentage
``` 


> 🧠 *Why 4 equal classes?*  
> This helps visualize severity across districts using simple and interpretable risk categories. However, you can experiment with **Natural Breaks** if data is unevenly distributed.

---

### 4. **Save Your New Styles for Reuse**

Save your manually created styles as `.qml` files for future reuse.

**Steps:**
- Right-click on the layer in the **Layers Panel**  
- Select **Properties**  
- In the window that opens, go to the **Symbology** tab  
- Click on `Style` → `Save Style…`
- Save the file in the folder `layer_sytle`
- Use these filenames:
   ```
   health_pct_affected_style
  ```
  ```
  education_pct_affected_style
  ```


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_save_new_style.mp4"></video>


### 5. *(Optional)* Import Styles into Your QGIS Library

To reuse your styles in any future project:

- Go to `Settings` → `Style Manager`
- Click `Import/Export` → `Import Items`
- Browse to and select your saved `.qml` files

The styles will now appear as presets in the **Layer Styling Panel**.

---

## Task 5: Quick Map Creation – Aina Uses Map Templates

After all the hard work of analyzing data and styling layers, Aina is ready to **share her results**. But creating a professional-looking map from scratch every time would be slow and repetitive.  

To save time, she uses **map templates (.qpt files)** prepared by her team. These templates already contain the essential elements — map frames, legends, logos, titles, and scale bars. With them, Aina can turn her analysis into a **clean, consistent map** in just a few clicks.  

✅ **Goal**  
Apply a ready-made QGIS map template to quickly create and export maps that show cyclone impacts on population, health facilities, and schools.  


1. Load the pre-made print layout template

- Locate the template `cyclone_impact_population_map_template.qpt` in your project folder under:  
  `Map_Templates/`

- You can load the template **by drag-and-drop**:
  - Open your QGIS project.
  - Drag the `.qpt` file directly into QGIS — a new layout will be created automatically.

- Alternatively:
  - Go to `Project` → `New Print Layout`
  - Enter a name (e.g. `Harald_2025_population`)
  - Click `OK`
  - In the layout, go to `Layout` → `Import from Template…`
  - Select the file `cyclone_impact_overview_map_template.qpt` and click `Open`
 2. Check and set page size
- Right-click anywhere on the white canvas and choose `Page Properties`.
- On the right-side panel, ensure the following:
  - **Page Size**: A3
  - **Orientation**: Landscape

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_load_mpa_template.mp4"></video>

3. Update the attribute table of exposed districts
- In the **Print Layout**, click on the attribute table (right-hand side of the layout).
- In the **Item Properties** panel:
  - Ensure the correct layer is selected `Harald_Exposed_population`
  - Click `Refresh Table Data`
  - Click `Attributes…` → in the upper part under **Fields** click on `Clear`
    - Then add the following layer by clicking on ➕ :
    - **Attribute**: `ADM1_EN`; `ADM2_EN`; `ADM2_PCODE`; `exposed_population_sum`
    - To sort the tabel content, under the **Sorting**  clicking on ➕ and add the column `AMD1_EN`
    - **Sort Order**: Ascending
  - Click `OK`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_makingadjust_AT.mp4"></video>

  
```{admonition} ⚠️ Warning – Long Tables
If the attribute table you want to include is **longer than the map frame**, part of it will be cut off in the exported map.  
To fix this, open the table properties in the layout and **reduce the font size** until the full table fits.  
```


5. Adjust the legend
- In the layout, click on the **Legend** item.
- In the **Item Properties** panel:
  - Uncheck **Auto update**
  - Scroll to **Legend items** and remove all entries (🗑️)
  - Add the following relevant layers:
    - `example_Harald_2025_Track`
    - `cyclone_harald_buffer`
    - `Harald_Exposed_Population`
  - When selecting layers, check **Only visible layers**
  - Rename legend entries to match layout naming
    - `example_Harald_2025_Track` ->
     ```
     Cyclone Harald Track
     ```
    - `cyclone_harald_buffer`->
     ```
     Cyclone Harald 200 km Buffer
     ```
    - `Harald_Exposed_Population`->
     ```
     Number of exposed peopel
     ```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_adjust_map_making_Legend.mp4"></video>

6. **Update Logos and Icons**  
- The logos that need to be added to the map are represented by the red **X**.  
- Click on the image in the **Item List**.  
- Click on the three dots ![](/fig/Three_points.png) next to the file path.  
- Browse to the folder `logos_pictures` and select the correct logo file.  

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_making_update_logos.mp4"></video>


7. Review and update layout text elements
- Make sure all text elements are up to date, especially:
  - **Map title**
  - **Cyclone name and date**
  - **Author/Organization** (optional)
- Adjust font size or alignment if necessary

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_mak_making_adjust_title.mp4"></video>

### ✅ Final Checklist

| Task                                           | Done |
|------------------------------------------------|------|
| Page set to A3 Landscape                       | ☐    |
| Only relevant layer group active               | ☐    |
| Exposed districts attribute table updated      | ☐    |
| Legend cleaned and renamed                     | ☐    |
| All text elements updated                      | ☐    |

---



```{dropdown} Your final output should look like this after styling the layer
The map now clearly displays the exposed population within the affected districts The original storm track line — used as input data — is highlighted, as well as the buffered impact area, which serves as a proxy for identifying exposed districts.

On the right-hand side of the map, a list shows all exposed districts, including data on total population and exposed population. The districts (Admin 2) are organized under their corresponding regions (Admin 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map_example.png
---
width: 1000px
name: 
align: center
---
```

## Task 6: Exporting Model Results for the Operations Team

**Background – Aina Supports Decision Makers**

After producing maps and visuals, Aina often gets requests from the operations team:  
> _“Can you send us the data in table format?”_

Instead of exporting these tables manually each time, Aina wants to automate this step within her model — ensuring that every run of the model produces clear, ready-to-use data files.

In this task, you’ll help Aina extend her existing model to export selected layers.

We will join the following layers step by step:

- `admin2_health_affected_pct`:  
  Contains the **total number of health facilities**, the **number of affected health facilities**, and the **percentage of affected health facilities**.

- `admin2_education_affected_pct`:  
  Contains the **total number of education facilities**, the **number of affected education facilities**, and the **percentage of affected education facilities**.

- `exposed_population`:  
  Contains the **total population per district** and the **exposed population** from the zonal statistics step.

---

1. Open your model
- Open `Estimate_Exposed_Population_Health_Education`
- Save a new version as:  
  ```
  Estimate_Exposed_Population_Health_Education_Spreadsheet_Export
  ```
2. Join Health and Education data into one layer
- In the **Algorithms**, search for `Join Attributes by Field Value`.
- Add a description: `Joindre santé et éducation dans une seule couche par ADM2`
- Configure the algorithm as follows:
  - **Input Layer**: `admin2_health_affected` (select from **Algorithm Output**)
  - **Input Layer 2**: `admin2_education_affected` (select from **Algorithm Output**)
  - **Table field**: 
   ```
   ADM2_PCODE
   ```
  - **Table field 2**: 
   ```
   ADM2_PCODE
   ```
  - **Layer 2 fields to copy**: Leave empty (all fields will be copied)
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de santé et d’éducation par le champ `ADM2_PCODE` afin de combiner les résultats dans une seule couche.
``` 
3. Join the result with the population data
Now join the result of the previous step (health + education) to the **exposed population** data.
- Add a second `Join Attributes by Field Value` algorithm to the model
- Add a description: `Joindre les données de population avec les indicateurs santé et éducation`
- Configure the algorithm as follows:
  - **Input Layer**: `exposed_population` (select from **Algorithm Output** of the Zonal Statistics step)
  - **Input Layer 2**: Output from Step 2 (health + education)
  - **Table field**: 
   ```
   ADM2_PCODE
   ```
  - **Table field 2**: 
   ```
   ADM2_PCODE
   ```
  - **Layer 2 fields to copy**: *(Enter the following field names exactly as shown — comma-separated, no spaces)*
    ```
    count_health_total;sum_exposed_health;pct_exposed_health;count_education_total;sum_exposed_education;pct_exposed_education
    ```
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop_HS_ES.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération : joindre les données de population avec les indicateurs de santé et d’éducation.
``` 

::::{tip} Where to find the column names  
Open the **attribute tables** of the outputs `health_total_per_admin2`, `sum_exposed_healthsites_POI`, and `admin2_health_affected_pct` in QGIS.  
Look at the **column headers** to find the exact names of the fields you want to copy.
::::
::::{warning} Invisible spaces will break the join  
If a column name like `count_health_total` has an invisible trailing space, the join will silently fail.  
Always copy field names **directly from the attribute table** to avoid errors.
::::


4. Export results to a spreadsheet
- In the **Processing Toolbox**, search for `Export to spreadsheet` and double-click to open.
- Add a description: `Exporter les données de population, d'éducation et de santé dans un seul tableau`
- Configure the tool as follows:
  - **Input Layer**: Select the output of Step 3 from **Algorithm Output**
  - **Destination spreadsheet**:
    ```
    exposure_indicators_spreadsheet
    ```

  - Click **OK** to add it to the model.
Once you run the model, this step will automatically generate a spreadsheet with all relevant indicators ready for the operations team!

```{figure} /fig/fr_MDG_AA_model_export_as_table.PNG
---
width: 600px
name: the_world_result
align: center
---
Exporter tous les indicateurs (population, santé, éducation) vers un tableau unique au format tableur.
``` 



5. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
6. **Run the model**
   - Click the ▶️ **Run** button in the top-right corner of the Graphical Modeler window.
   - **Input:**
     - Click on the three dots for each input dataset and select the correct input:
       - `Cyclone Track` → select the GeoJSON of the storm path (e.g. `Harald_2025_Track.geojson`)
       - `Population Raster` → select the WorldPop raster file
       - `Admin Boundaries` → select the Admin 2 layer (e.g. `MDG_adm2.gpkg`)
       - `Health Facilities` → select the point dataset for health sites
       - `Education Facilities` → select the point dataset for schools
   - **Output:**
     - Save all output layers in the output folder and use the names below.
       - `admin2_health_affacted` -> 
        ```
        admin2_health_affected
        ```
       - `admin2_education_affected` ->
        ```
        admin2_education_affected
        ```
       - `cyclone_harald_buffer` ->  
        ```
        cyclone_harald_buffer
        ```
       - `exposed_population_sum` ->
        ```
        admin2_harald_Exposed_Population
        ```
       - `exposure_indicators_spreadsheet` ->
        ```
        exposure_indicators_harald
        ```
   - Click **Run** to execute the full model.

::::{tab-set}

:::{tab-item} Graphic Modler

```{figure} /fig/
---
width: 600px
align: center
---

```
:::
:::{tab-item} Run Model Configuration
```{figure} /fig/
---
width: 600px
align: center
---

```
:::
:::{tab-item} Model Output
```{figure} /fig/
---
width: 600px
align: center
---

```
:::
::::

---





## Task 7: Reachability of health Posts from CRM Warehouses
When a cyclone is forecast to make landfall, Aina works with the logistics and health teams to decide **where to send prepositioned medical kits**. However, not all CRM warehouses stock the needed items — only three do.

To make fast, data-driven decisions, Aina wants to know **which health posts are reachable** from those warehouses **within 10 hours**. This analysis helps ensure that kits are sent to facilities **that can actually be reached in time**.

Her goal is to create a clear visual map showing reachable vs. non-reachable health posts — and share this with decision-makers as quickly as possible.


### 1. Filter Health Posts from the National Health Facility Dataset

Before checking which facilities are reachable, Aina needs to isolate **health posts** from the broader dataset of all health facilities.

1. **Load the health facilities dataset**  
   - File: `hotosm_mdg_health_facilities_points.gpkg` (or the respective GeoPackage you are using)  
   - Load it via drag and drop or through `Layer` → `Add Vector Layer`.
2. **Open the attribute table** and check the column named `amenity`.
3. **Filter by expression** to keep only health posts:  
   - Right-click the layer → `Filter…`  
   - Use the following expression:
     ```qgis
     "amenity" = 'health_post'
     ```
4. **Export the filtered layer**  
   - Right-click the filtered layer in the Layers Panel → `Export` → `Save Features As…`  
   - Format: `GeoPackage`  
   - Save to your `project` folder as:
     ```
     health_posts_only.gpkg
     ```
   - Click `OK` to confirm export.
5. **Remove the filter** or original layer from your project to avoid confusion.
> 💡 **Tip**: Filtering directly in QGIS lets you work with a specific subset of features without modifying the original dataset.

### 2. Load Isochrone Layers for the Three CRM Warehouses

Aina knows that only **three warehouses** stock the necessary medical supplies:  
**Antananarivo**, **Maroantsetra**, and **Tolanaro**. She will now load the isochrone layers for each of these warehouses to begin analyzing service areas.

1. **Load the individual isochrone layers** for each warehouse:
   - `CRM_warehouse_Isochrones_Antananarivo.gpkg`
   - `CRM_warehouse_Isochrones_Maroantsetra.gpkg`
   - `CRM_warehouse_Isochrones_Tolanaro.gpkg`

   You can drag and drop each file into QGIS or go to `Layer` → `Add Layer` → `Add Vector Layer`.

2. **Inspect the attribute table** of each isochrone layer  
   Confirm that each record has a `traveltime_h` field showing the estimated travel time in **hours**.

3. **Remove all features where travel time is above 10 hours**:  
   - Right-click each layer → `Filter…`
   - Apply the expression:
     ```qgis
     "traveltime_h" <= 10
     ```

4. **Export each filtered layer** to the `temp` folder :
   At this point, Aina also ensures all exported layers are saved in the same CRS as the health post dataset — `EPSG:4326` — to avoid problems in the spatial join.
   - Save each as:
     ```
     CRM_isochrones_Antananarivo_upto10h.gpkg
     CRM_isochrones_Maroantsetra_upto10h.gpkg
     CRM_isochrones_Tolanaro_upto10h.gpkg
     ```

5. **Style the isochrones for clarity** 
   Aina can apply predefined style file to color the layer based on `traveltime_h` to visualize different time bands (4h, 6h, 8h, 10h) later in Step 5.
   - Right-click each filtered layer → `Properties` → `Symbology`
   - Click `Style` at the bottom → `Load Style…`
   - Select the file:  
     `CRM_warehouse_isochrones_style.qml`
   - Click `Open`, then `Apply` and `OK`

### 3. Visualizing Health Post Reachability from CRM Warehouses
Aina needs to identify which health posts can be reached by road from three key CRM warehouses (Antananarivo, Maroantsetra, and Tolanaro) **within 10 hours of travel time**. She will do this manually by combining the 10-hour isochrones from these warehouses and comparing them to the national health post dataset.
1. **Merge the Isochrone Layers from the Three Warehouses**  
   - In the **Processing Toolbox**, search for `Merge Vector Layers`.  
   - **Input layers**:  
     - `CRM_isochrones_Antananarivo_upto10h.gpkg`  
     - `CRM_isochrones_Maroantsetra_upto10h.gpkg`  
     - `CRM_isochrones_Tolanaro_upto10h.gpkg`  
   - **CRS**: `EPSG:4326`  
   - **Save to file**:  
     ```
     merged_isochrones_10h.gpkg
     ```  
   - Click **Run**.
2. **Select Health Posts Reachable Within 10 Hours**  
   - In the **Processing Toolbox**, search for `Select by Location`.  
   - Set the following parameters:  
     - **Input layer**: `health_posts_only.gpkg`  
     - **Predicate**: `intersects`  
     - **Intersect layer**: `merged_isochrones_10h.gpkg`  
   - Click **Run**.
   > 💡 The selected points are those within the 10-hour service areas of the warehouses.
3. **Create a Reachability Field for Selected Health Posts**  
   - Open the **Field Calculator** ![](/fig/mActionCalculateField.png) on the `health_posts_only` layer.  
   - Check ✅ `Only update selected features`  
   - **Output field name**: `Reachability_time`  
   - **Output field type**: `Text (string)`  
   - **Expression**:
     ```qgis
     'reachable in 10 hours'
     ```  
   - Click **OK** to create and populate the new field for selected features.
4. **Mark the Remaining Health Posts as Not Reachable**  
   - Invert the selection:  
     Go to `Edit` → `Invert Feature Selection` ![](/fig/mActionInvertSelection.png)  
     or right-click the layer and select `Invert Selection`.  
   - Open the **Field Calculator** again.  
   - Check ✅ `Only update selected features`  
   - Use the same field: `Reachability_time`  
   - **Expression**:
     ```qgis
     'not reachable in 10 hours'
     ```  
   - Click **OK** to apply the update.

> ✅ Now all health posts are labeled as either **reachable** or **not reachable** in the `Reachability_time` column.





