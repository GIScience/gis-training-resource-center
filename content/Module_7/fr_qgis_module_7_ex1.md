::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::

::::

# Piste d'Exercice : Analyse d’Action Anticipative pour les Cyclones à Madagascar <a id="piste-dexercice-analyse-daction-anticipative-pour-les-cyclones-a-madagascar"></a>


## Caractéristiques <a id="caracteristiques"></a>


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
Aina, l'experte GIS (SIG) de la Croix-Rouge malgache (CRM), se prépare pour la prochaine saison des cyclones. Elle souhaite eméliorer la capacité de réaction de son équipe une fois une tempête annoncée, en automatisant des analyses clés dans la application QGIS. 
Celles-ci incluent l'estimation des populations exposées, l'identification des services impactés comme la santé et l'education, et l'évaluation de l'accessibilité des postes de santé à partir des entrepôts de la croix rouge dans une fenêtre critique de 10 heures. 
L'objectif est de préparer un workflow d'analyse et de visualisation pour soutenir une action anticipée (eng.: Anticipatory Action) et fondée sur les données, avant que le cyclone ne touche terre. 


:::

## Instruction pour les formateurs <a id="instruction-pour-les-formateurs"></a>



:::{dropdown} __Espace Formateurs (Trainers Corner)__ 

### Préparer la formation <a id="preparer-la-formation"></a>

- Prenez du temps pour vous familiariser avec l'exercice et le matériel founi. 
- Préparez un tableau blanc. Cela peut être un tableau physique, un paperboard (tableau blanc virtuel, e.g., Miro Board) où les participant·es peuvent ajouter leurs observations et questions. 
- Avant de commencer l'exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et dézippé__ le dossier de données.
- Consultez [How to do trainings?](https://giscience.github.io/gis-training-resource-center/content/Trainers_corner/en_how_to_training.html#how-to-do-trainings) pour des conseils généraux sur la conduite de formations (ce matériel est en anglais).


### Animer la formation <a id="animer-la-formation"></a>

__Introduction:__

- Présentez l'idée et l'objectif de l'exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a bien dézippé le dossier avant de commencer les tâches.

__Exercice guidée:__

- Montrez et expliquez chaque étape cous-même au moins deux fois, et suffisamment lentement por que chacun·e puisse voir ce que vous faites et reproduire les étapes dans sons prope projet QGIS.
- Assurez-vous que tout le monde suit en demandant régulièrement si quelqu'un a besoid d'aide ou si tout le monde suit toujours.
- Soyez ouvert·e et patient·e face aux questions ou problèmes éventuels. Vos participant·es sont en train de faire plusieures choses à la fois: écouter vos instructions tout en s'orientant dans leur propre projet QGIS.

### Fin de la formation <a id="fin-de-la-formation"></a>

- Prévoyez du temps à la fin pour répondre aux questions ou aborder les éventuels problèmes rencontrés lors de tâches.
- Laissez un moment pour des questions ouvertes.

:::

## Données <a id="donnees"></a>

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip

__Téléchargez toutes les données [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Module_7/Exercise_1.zip), enregistrez le dossier sur votre ordinateur et dézippez le fichier.__ 

:::

Le dossier s'appelle __"__ et contient toute la [structure de dossier standard](https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_geodata_management.html#standard-folder-structure) avec toutes les données dans le sous-dossier `/data/input/` et la documentation supplémentaire dans le dossier `/documentation/`. 

| Ensemble de données | Source | Descriptions |
| ----- | --- | --- |
| Frontières administrative | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Les limites administratives aux niveaux 0 à 4 pour Madagascar sont accessibles via HDX fourni par OCHA. Pour cette analyse, nous fournissons les limites administratives des niveaux 1 (régional) et 2 (district) au format shapefile. |
| Trajectoires des cyclones | [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive)  | Le projet IBTrACS est la collection mondiale des cyclones tropicaux la plus complète  disponible. Il fusionne des données récentes et historiques provenant de plusieurs agences pour créer un jeu de données unifié, public  améliorant les comparaisons inter-agences.  |
| Établissements éducatifs et sites de santé| [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | Les données des lieux d'intérêts (établissements éducatifs et sites de santé) sont téléchargées via l'util "HOT Export Tool" basé sur les données du projet OpenStreetMap. |
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

## Tâche 1 : Estimation de la population exposée – Approche manuelle d’Aina <a id="tache-1-estimation-de-la-population-exposee-approche-manuelle-daina"></a>

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


## Tâche 2: Automatisation de l’estimation de la population exposée – Le modèle d’Aina <a id="tache-2-automatisation-de-lestimation-de-la-population-exposee-le-modele-daina"></a>

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
        - Laissez la description vide ou écrivez: *Modèle automatisé pour estimer la population exposée a partir d'un tampon autour du cyclone*.


3. **Enregistrer le modèle:**
   - Pour enregistrer le modèle:
     - Cliquez sur l'icône __Enregistrer__ (💾) ou naviguez à `Modèle` -> `Enregistrer`. 
     - Naviguez jusqu'au dossier `/models/` de votre structure de dossier pour la formation
     - Enregistrer le modèle sous: `Esimation_Population_Exposée`.


4. **Ajouter les entrées du modèle**:  
  - Dans le panneau gauche, ouvrez la section __Entrées__.
  - Ajouter les couches d'entrées en cliquant sur `+ Couche Vecteur` (`+ Vector Layer`) et `+ Couche Raster` (`+ Raster Layer`) Dans le **panneau gauche**, élargissez la section **Entrées**.
  - Ajoutez les couches d'entrée suivantes avec des contraintes de type:
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

1. **Reprojetter la trajectoire du cyclone vers EPSG:29738** 
  - Dans le panneau de **Algorithmes** à gauche, cherchez **Reprojeter une couche** et faites un double-clic dessus.
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
Reprojeter la couche du trajectoire du cyclone vers un système de référence de coordonnées métrique (SCR) EPSG: 29738
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
Ajouter l'étape pour tamponner la couche Cyclone reprojetée.
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
Reprojeter le tampon vers EPSG:4326.
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
Découper la couche raster de population pour l'étendre au tampon cyclon.
```

9. **Calul de la population exposée aux cyclone par district**
  - Dans le panneau **Algorithme**, cherchez pour l'outil `Statistiques de zone` (eng.: `Zonal Statistics`) et ouvrez le. 
  - Dans la fenêtre de configuration:
    - Ajoutez une description: `Calcul de la population exposée aux cyclone par district` 
    - Comme __"Couche source"__, choisissez la couche `Frontières administratives`.
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
  - Corrigez les éventuels avertissements ou erreurs affichés dans le panneau de journal. 
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


Vous pouvez maintenant exécuter ce modèle chaque fois qu’une nouvelle trajectoire de cyclone est disponible.

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

:::{tab-item} Résultat du modèle
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_extended_buffer.PNG
---
width: 600px
align: center
---
Définition de l'entrée du modèle: Raster de population
```
:::

::::



## Tâche 3: Identification des établissements de santé et d'éducation impactés – Aina ajoute des couches supplémentaires <a id="tache-3-identification-des-etablissements-de-sante-et-deducation-impactes-aina-ajoute-des-couches-supplementaires"></a>

Après avoir construit son modèle pour estimer la population exposée, Aina souhaite améliorer son utilité. Elle décide d'identifier également les services essentiels affectés par les cclones — en particulier les établissments de santé et les écoles. 

Elle veut non seulement savoir quels établissements sont affectés, mais aussi combien il en existe au total par district. Cela lui permettera de calculer le __pourcentage de service affectés__ dans chaque zone. 

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
2. **Enregistrez votre modèle sous un nouveau nom**
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
Définir une nouvelle entrée de modèle: couche vectorielle de points représentant les établissements de santé
```
:::
:::{tab-item} Entrée: établissements d’enseignement
```{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle: couche vectorielle de points représentant les établissements d'enseignement
```
:::
::::

4. **Compter tous les établissements de santé par district (ADM2)**
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
5. **Compter tous les établissements d’enseignement par Niveau 2**  
   - Ajouter une autre étape **Compter les points dans un polygone**.
   - Configuration:
     - Ajouter une description: `Comptez le nombre d'établissements d’enseignement dans chaque district`
     - **Polygones**: `Limites administratives` (entrée du modèle)
     - **Points**: `Établissements d’enseignement` (entrée du modèle)
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
Configuration de l'opération: compter le nombre d'établissements scolaires dans chaque district.
```
6. **Intersection des établissements de santé avec la zone tampon du cyclone**  
   - Depuis le panneau **Algorithmes**, recherchez **Intersection**.
   - Dans la fenêtre de configuration:
   - Ajouter une description: 
      ```
      Établissements de santé dans la zone d'impact du cyclone
      ```  
     - **Couche source**: `Établissements de santé` (entrée du modèle)
     - **Couche de superposition**: zone tampon du cyclone (utiliser “Reprojected to EPSG:4326” depuis la **Sortie d’algorithme**)
     - Laissez la sortie vide. 
   - Cliquez sur **OK** pour ajouter l'étape au modèle.
```{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de santé avec la zone d'impact du cyclone.
```
7. **Intersection des établissements d’éducation avec la zone tampon du cyclone**  
   - Ajouter un autre algorithme **Intersection**.
   - Configuration:
     - Ajouter une description:
       ```
       Établissements d’éducation dans la zone d'impact du cyclone.
       ```  
     - **Couche source**: `Établissements d’éducation` (entrée du modèle)
     - **Couche de superposition**: zone tampon du cyclone (utiliser “Reprojecter vers EPSG:4326” depuis la **Sortie d’algorithme**)
     - Laisser la sortie vide. 
   - Cliquer sur **OK** pour ajouter l'étape au modèle. 
```{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération: intersecter les établissements de education avec la zone d'impact du cyclone.
```
8. **Compter les établissements de santé affectés par Niveau 2**  
   - Ajouter **Compter les points dans un polygone**
   - Configuration:
     - Ajouter une description: 
       ```
       Compter les établissements de santé touchés par district
       ```  
     - **Polygones**: sortie du décompte total des établissements de santé
     - **Points**: sortie des établissements de santé intersectés
     - **Nom du champ de dénombrement**: 
       ```
       sum_exposed_healthsites_POI
       ```  
     - Cliquez sur **OK** pour ajouter l'étape au modèle.

```{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération: compter les établissements de santé touchés par district.
```
9. **Compter les établissements d’enseignement affectés par Niveau 2**  
   - Ajouter **Compter les points dans un polygone**
   - Configuration:
     - Ajouter une description: 
       ```
       Compter les établissements d’enseignement touchés par district
       ```   
     - **Polygones**: sortie du décompte total des établissements d’enseignement
     - **Points**: sortie des établissements d’éducation intersectés
     - **Nom du champ de dénombrement**: 
       ```
       sum_exposed_education_POI
       ```  
     - Cliquez sur **OK** pour ajouter l'étape au modèle.
```{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération: compter les établissements de santé touchés par district.
```
10. **Calculer le pourcentage d’établissements de santé affectés**
Pour calculer le pourcentage d’établissements de santé affectés par zone administrative, utilisez la **Calculatrice de champ**:
- Ajouter la **Calculatrice de champ**:
   - Configuration:
     - Ajouter une description:
       ```
       Calculer le pourcentage d’établissements de santé touchés par district
       ```  
    - **Couche en entrée**: sortie du comptage des établissements de santé affectés
    - **Nom du champ de sortie**:  
       ```
       pct_health_affected
       ``` 
    - **Type de champ**: Décimal (réel)
    - **Expression**:
    ```qgis
    CASE WHEN "count_health_total" > 0
    THEN "sum_exposed_healthsites_POI" / "count_health_total" * 100
    ELSE
    ```
    - Définir la sortie comme **Sortie du modèle**
    - Nommer:
   ```
   admin2_health_affected_pct
   ```

```{figure} /fig/fr_MDG_AA_model_field_calc_pct_health_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération: calculer le pourcentage d’établissements de santé touchés par district.
```


11. **Calculer le pourcentage d’établissements d’enseignement affectés**  

Pour calculer le pourcentage d’établissements d’enseignement affectés par zone administrative, utilisez la **Calculatrice de champ**:  
- Ajouter la **Calculatrice de champ**:  
   - Configuration:  
     - Ajouter une description:  
       ```
       Calculer le pourcentage d’établissements d’éducation touchés par district
       ```  
     - **Couche en entrée**: sortie du comptage des établissements d’éducation affectés  
     - **Nom du champ de sortie**:  
       ```
       pct_education_affected
       ```  
     - **Type de champ**: Décimal (réel)  
     - **Expression**:  
       ```qgis
       CASE WHEN "count_education_total" > 0
       THEN "sum_exposed_education_POI" / "count_education_total" * 100
       ELSE 0
       END
       ```  
   - Définir la sortie comme **Sortie du modèle**  
   - Nommer:  
     ```
     admin2_education_affected_pct
     ```


```{figure} /fig/fr_MDG_AA_model_field_calc_pct_education_exposed.PNG
---
width: 600px
align: center
---
Configuration de l’opération: calculer le pourcentage d’établissements d’éducation touchés par district.
```

12.  **Valider et enregistrer votre modèle étendu**  
   - Cliquez sur le bouton ✔️ **Valider le modèle** (sous `Modèle` dans le menu en haut) pour vérifier les erreurs.
   - Enregistrez à nouveau sous:  
     **`Estimate_Exposed_Population_Health_Education.model3`**

13.  **Exécuter le modèle**
   - Cliquez sur le bouton ▶️ **Exécuter** en haut de la fenêtre du Modélisateur Graphique.
   - Dans la boîte de dialogue:
     - Sélectionnez les couches d’entrée nécessaires:
       - `Trajectoire du cyclone` → sélectionnez le fichier GeoJSON du cyclone (ex. `Harald_2025_Track.geojson`)
       - `Raster de population` → sélectionnez le raster WorldPop
       - `Limites administratives` → sélectionnez la couche de Niveau 2 (ex. `MDG_adm2.gpkg`)
       - `Établissements de santé` → sélectionnez la couche ponctuelle des établissements de santé
       - `Établissements d’enseignement` → sélectionnez la couche ponctuelle des écoles
     - Choisissez un emplacement pour enregistrer les couches finales (vous pouvez laisser les couches intermédiaires en mémoire temporaire)
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


## Tâche 4: Visualiser les résultats de l’impact du cyclone – Aina applique des styles à ses cartes <a id="tache-4-visualiser-les-resultats-de-limpact-du-cyclone-aina-applique-des-styles-a-ses-cartes"></a>

Après avoir terminé son modèle, Aina souhaite **communiquer clairement les résultats** — à la fois à ses collègues de la Croix-Rouge et à des partenaires externes.

Elle en a **assez de devoir restyler manuellement chaque couche** à chaque fois que de nouvelles données cycloniques arrivent. À la place, elle veut :
- ✅ **Des visuels clairs et cohérents**
- 🔁 **Des modèles réutilisables**
- 📂 **Des fichiers .qml standardisés** partagés entre projets

Dans cette tâche, vous allez aider Aina à appliquer des styles `.qml` existants et à en créer de nouveaux pour les couches qui n’ont pas encore de style défini.

---


### 1. **Charger les couches nécessaires (si ce n’est pas déjà fait)** <a id="1-charger-les-couches-necessaires-si-ce-nest-pas-deja-fait"></a>

Assurez-vous que les couches suivantes sont déjà chargées dans votre projet QGIS. Ce sont les sorties de la **Tâche 3**:

- `Harald_2025_Track`
- `Harald_Buffer_200km`
- `Harald_Exposed_Population`
- `sum_exposed_healthsites_POI`
- `sum_exposed_education_POI`
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

Si l’une d’elles manque:
- Chargez-la par **glisser-déposer** depuis votre dossier `results`, ou
- Utilisez `Couche` → `Ajouter une couche` → `Ajouter une couche vectorielle` ou `Ajouter une couche raster`

---

### 2. **Appliquer des fichiers de style prédéfinis** <a id="2-appliquer-des-fichiers-de-style-predefinis"></a>
Appliquez les fichiers de style `.qml` suivants aux couches correspondantes:

| **Couche**                             | **Fichier de style**                           |
|----------------------------------------|------------------------------------------------|
| `Harald_2025_Track`                    | `storm_track_cyclone_style.qml`               |
| `Harald_Buffer_200km`                  | `exposed_cyclone_area_style.qml`              |
| `Harald_Exposed_Population`            | `exposed_population_style.qml`                |
| `sum_exposed_healthsites_POI`          | `exposed_healthsites_style.qml`               |
| `sum_exposed_education_POI`            | `exposed_education_facilities_style.qml`      |




```{note}
⚠️ Pour les **établissements de santé** et **établissements d’enseignement**, les fichiers de style fournis sont liés à la colonne contenant le **nombre total d’établissements exposés**.  
Ils ne sont **pas** basés sur la colonne de pourcentage.  
```


**Étapes:**
- Faites un clic droit sur la couche dans le **Panneau des couches**  
- Sélectionnez **Propriétés**  
- Dans la fenêtre qui s’ouvre, allez dans l’onglet **Symbologie**  
- En bas à gauche, cliquez sur **Style** → **Charger le style…**
- Cliquez sur les trois points ![](/fig/Three_points.png)  
- Naviguez jusqu’au fichier `.qml` correspondant dans le dossier `layer_style` et sélectionnez-le  
- Cliquez sur **Ouvrir**, puis **Appliquer** et **OK** pour confirmer  

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_output_style.mp4"></video>

> 💡 *Si le style ne se charge pas correctement, vérifiez les noms de colonnes et assurez-vous qu’ils 
correspondent à ceux utilisés dans le fichier `.qml`. Pour cela, ouvrez la **table attributaire** de la couche et 
comparez les noms des champs.*

---


::::{tab-set}

:::{tab-item} Résultat intermédiaire: Population exposée

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_pop_style.PNG
---
width: 600px
align: center
---
Carte montrant le nombre de personnes exposées par district après l’application du style .qml.
```
:::
:::{tab-item} Résultat intermédiaire: Établissements de santé exposés
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_HS_sum_style.PNG
---
width: 600px
align: center
---
Carte indiquant le nombre total d’établissements de santé exposés par district, représentés avec le style prédéfini.
```
:::
:::{tab-item} Résultat intermédiaire: Établissements scolaires exposés
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task4_exposed_ES_sum_style.PNG
---
width: 600px
align: center
---
Carte affichant le nombre total d’établissements scolaires exposés par district, après application du fichier de style .qml.
```
:::
::::

### 3. **Styliser manuellement les couches de pourcentage** <a id="3-styliser-manuellement-les-couches-de-pourcentage"></a>

Aina souhaite également visualiser le pourcentage d’établissements de santé et d’éducation exposés. Toutefois, puisqu’aucun style n’est encore disponible, elle doit effectuer la procédure manuellement.

**Étapes:**
- **Cliquez droit** sur la couche `admin2_health_affected` → sélectionnez **Dupliquer la couche**  
- **Renommez** la couche dupliquée:
  ```
  admin2_health_affected_percentage
  ```
- Faites un clic droit sur la couche dans le **Panneau des couches**  
- Sélectionnez **Propriétés**  
- Dans la fenêtre qui s’ouvre, allez à l’onglet **Symbologie**  
- Définissez la **Symbologie** sur `Graduée`
- Choisissez le **champ** approprié:
  - `pct_health_affected`
- Ouvrez l’onglet **Histogramme** pour visualiser la distribution des valeurs en cliquant sur `calculer l’histogramme`
- Ensuite, retournez à l’onglet `Classes` et configurez:
  - **Mode**: `Intervalle égal`
  - **Classes**: `4`
- Cliquez sur `OK`. Cela créera quatre classes (`0–25%`, `25–50%`, `50–75%`, `75–100%`)
- Choisissez un dégradé de couleur (ex.: jaune clair → rouge foncé)
- Facultativement, personnalisez les étiquettes de classes pour plus de clarté
- Cliquez sur **Appliquer**

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_affacted_HS_pct.mp4"></video>

- Répétez la même procédure pour la couche `admin2_education_affected`.  
Après duplication, renommez la nouvelle couche :
 ```
 admin2_health_affected_percentage
```


> 🧠 *Pourquoi 4 classes égales ?*  
> Cela permet de visualiser la gravité par district en utilisant des catégories de risque simples et interprétables. Cependant, vous pouvez aussi expérimenter les **ruptures naturelles** si les données sont inégalement réparties.

---

### 4. **Enregistrez vos nouveaux styles pour les réutiliser** <a id="4-enregistrez-vos-nouveaux-styles-pour-les-reutiliser"></a>

Enregistrez vos styles manuels au format `.qml` pour pouvoir les réutiliser plus tard.

**Étapes:**
- Faites un clic droit sur la couche dans le **Panneau des couches**  
- Sélectionnez **Propriétés**  
- Dans la fenêtre qui s’ouvre, allez à l’onglet **Symbologie**  
- Cliquez sur `Style` → `Enregistrer le style…`
- Enregistrez le fichier dans le dossier `layer_sytle`
- Utilisez les noms de fichiers suivants:
   ```
   health_pct_affected_style
   ```
   ```
   education_pct_affected_style
   ```


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_model_style_save_new_style.mp4"></video>


### 5. *(Optionnel)* Importer les styles dans votre bibliothèque QGIS <a id="5-optionnel-importer-les-styles-dans-votre-bibliotheque-qgis"></a>

Pour réutiliser vos styles dans de futurs projets:

- Allez dans `Préférences` → `Gestionnaire de styles`
- Cliquez sur `Importer/Exporter` → `Importer des éléments`
- Parcourez et sélectionnez vos fichiers `.qml` enregistrés

Les styles apparaîtront désormais comme préréglages dans le **Panneau de style de couche**.

---

## Tâche 5: Création rapide de cartes – Aina utilise des modèles de carte <a id="tache-5-creation-rapide-de-cartes-aina-utilise-des-modeles-de-carte"></a>

Après tout le travail d’analyse et de stylisation, Aina est prête à **partager ses résultats**. Mais créer une 
carte professionnelle à partir de zéro à chaque fois serait long et répétitif.  

Pour gagner du temps, elle utilise des **modèles de carte (.qpt)** préparés par son équipe. Ces modèles 
contiennent déjà les éléments essentiels — cadres cartographiques, légendes, logos, titres et barres d’échelle. 
Grâce à eux, Aina peut transformer son analyse en une **carte claire et cohérente** en seulement quelques clics.  


✅ **Objectif**  
Appliquer un modèle de carte QGIS prêt à l’emploi pour créer et exporter rapidement des cartes montrant les impacts du cyclone sur la population, les établissements de santé et les écoles.  


1. Charger le modèle d’impression préconçu

- Localisez le modèle `cyclone_impact_population_map_template.qpt` dans votre dossier projet sous:  
  `Map_Templates/`

- Vous pouvez charger le modèle **par glisser-déposer**:
  - Ouvrez votre projet QGIS.
  - Glissez directement le fichier `.qpt` dans QGIS — une nouvelle mise en page sera automatiquement créée.

- Ou bien :
  - Allez dans `Projet` → `Nouvelle mise en page`
  - Entrez un nom (par ex. `Harald_2025_population`)
  - Cliquez sur `OK`
  - Dans la mise en page, allez dans `Mise en page` → `Importer depuis un modèle…`
  - Sélectionnez le fichier `cyclone_impact_overview_map_template.qpt` et cliquez sur `Ouvrir`

2. Vérifiez et définissez le format de la page
- Cliquez droit n’importe où sur le canevas blanc et choisissez `Propriétés de la page`.
- Dans le panneau de droite, assurez-vous de:
  - **Taille de la page**: A3
  - **Orientation**: Paysage


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_load_mpa_template.mp4"></video>

3. Mettre à jour le tableau attributaire des districts exposés
- Dans la **Mise en page**, cliquez sur le tableau attributaire (à droite dans la mise en page).
- Dans le panneau **Propriétés de l’élément**:
  - Assurez-vous que la bonne couche est sélectionnée: `Harald_Exposed_population`
  - Cliquez sur `Actualiser les données du tableau`
  - Cliquez sur `Attributs…` → dans la partie supérieure sous **Champs**, cliquez sur `Effacer`
    - Puis ajoutez les champs suivants avec ➕:
    - **Champs**: `ADM1_EN`; `ADM2_EN`; `ADM2_PCODE`; `exposed_population_sum`
    - Pour trier le contenu du tableau, sous l’onglet **Trier**, cliquez sur ➕ et ajoutez la colonne `AMD1_EN`
    - **Ordre de tri**: Ascendant
  - Cliquez sur `OK`

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_makingadjust_AT.mp4"></video>

  

```{admonition} ⚠️ Avertissement – Tableaux longs
Si le tableau attributaire que vous souhaitez inclure est **plus long que le cadre cartographique**, une partie sera coupée dans la carte exportée.  
Pour corriger cela, ouvrez les propriétés du tableau dans la mise en page et **réduisez la taille de la police** jusqu’à ce que le tableau entier tienne.
```


5. Ajuster la légende
- Dans la mise en page, cliquez sur l’élément **Légende**.
- Dans le panneau **Propriétés de l’élément**:
  - Décochez **Mise à jour automatique**
  - Faites défiler jusqu’à **Éléments de la légende** et supprimez toutes les entrées (🗑️)
  - Ajoutez les couches pertinentes suivantes:
    - `example_Harald_2025_Track`
    - `cyclone_harald_buffer`
    - `Harald_Exposed_Population`
  - Lors de la sélection des couches, cochez **Uniquement les couches visibles**
  - Renommez les entrées de légende pour correspondre aux noms sur la carte:
    - `example_Harald_2025_Track` →
     ```
     Trace du cyclone Harald
     ```
    - `cyclone_harald_buffer` →
     ```
     Zone tampon de 200 km – Cyclone Harald
     ```
    - `Harald_Exposed_Population` →
     ```
     Nombre de personnes exposées
     ```

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_adjust_map_making_Legend.mp4"></video>

6. **Mettre à jour les logos et icônes**  
- Les logos à insérer sont représentés par des **X rouges**.  
- Cliquez sur l’image dans la **Liste des éléments**.  
- Cliquez sur les trois points ![](/fig/Three_points.png) à côté du chemin de fichier.  
- Parcourez le dossier `logos_pictures` et sélectionnez le bon logo.  

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_map_making_update_logos.mp4"></video>


7. Revoir et mettre à jour les textes de la mise en page
   - Vérifiez que tous les textes sont à jour, en particulier:
     - **Titre de la carte**
     - **Nom et date du cyclone**
     - **Auteur/Organisation** (facultatif)
   - Ajustez la taille de la police ou l’alignement si nécessaire


<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/fr_MDG_mak_making_adjust_title.mp4"></video>

### ✅ Liste de vérification finale <a id="liste-de-verification-finale"></a>

| Tâche                                           | Fait |
|------------------------------------------------|------|
| Page définie en format A3 Paysage              | ☐    |
| Seul le groupe de couches pertinent est actif  | ☐    |
| Tableau attributaire des districts exposés mis à jour | ☐ |
| Légende nettoyée et renommée                   | ☐    |
| Tous les éléments de texte mis à jour          | ☐    |

---



```{dropdown} Le rendu final devrait ressembler à ceci après le stylage
La carte montre désormais clairement la population exposée dans les districts affectés. La ligne de trajectoire du cyclone — utilisée comme donnée d’entrée — est mise en évidence, ainsi que la zone tampon, qui sert de proxy pour identifier les districts exposés.

Sur le côté droit de la carte, un tableau présente tous les districts exposés, avec les données sur la population totale et la population exposée. Les districts (Niveau 2) sont regroupés sous leurs régions correspondantes (Niveau 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map_example.png
---
width: 1000px
name: 
align: center
---
```


## Tâche 6: Exporter les résultats du modèle pour l’équipe des opérations <a id="tache-6-exporter-les-resultats-du-modele-pour-lequipe-des-operations"></a>

**Contexte – Aina soutient les décideurs**

Après avoir produit des cartes et des visualisations, Aina reçoit souvent des demandes de l’équipe des opérations:  
> _« Peux-tu nous envoyer les données au format tableau ? »_

Plutôt que d’exporter manuellement ces tableaux à chaque fois, Aina souhaite automatiser cette étape dans son modèle — afin que chaque exécution produise des fichiers de données clairs et prêts à l’emploi.

Dans cette tâche, vous aiderez Aina à étendre son modèle existant pour exporter certaines couches.

Nous allons joindre les couches suivantes étape par étape:

- `admin2_health_affected_pct`:  
  Contient le **nombre total d’établissements de santé**, le **nombre d’établissements affectés** et le **pourcentage d’établissements affectés**.

- `admin2_education_affected_pct`:  
  Contient le **nombre total d’établissements scolaires**, le **nombre d’établissements scolaires affectés** et le **pourcentage d’établissements scolaires affectés**.

- `exposed_population`:  
  Contient la **population totale par district** ainsi que la **population exposée**, issue de l’étape des statistiques zonales.

---


1. Ouvrez votre modèle
- Ouvrir `Estimate_Exposed_Population_Health_Education`
- Enregistrer une nouvelle version sous :  
  ```
  Estimate_Exposed_Population_Health_Education_Spreadsheet_Export
  ```
2. Joindre les données de santé et d’éducation dans une seule couche
- Dans les **Algorithmes**, cherchez `Joindre les attributs par valeur de champ` (eng.: `Join Attributes by Field Value`).
- Ajoutez une description: `Joindre santé et éducation dans une seule couche par ADM2`
- Configurez l’algorithme comme suit:
- **Couche source**: `admin2_health_affected` (sélectionner depuis **Sortie de l’algorithme**)
- **Champ de la table**:
   ```
   ADM2_PCODE
   ```
- **Couche en entrée 2**: `admin2_education_affected` (sélectionner depuis **Sortie de l’algorithme**)
  - **Champ de la table 2**: 
   ```
   ADM2_PCODE
   ```
  - **Couche 2 champs à copier**: Laisser vide (tous les champs seront copiés)
  - **Type de jointure**: Prendre uniquement les attributs de la première entité correspondante (un-à-un)
  - Laisser la sortie comme **Sortie du modèle** (sans entrer un nom)

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération: joindre les données de santé et d’éducation par le champ `ADM2_PCODE` afin de combiner les résultats dans une seule couche.
``` 

1. Joindre le résultat aux données de population  
Maintenant, joindre le résultat de l’étape précédente (santé + éducation) aux données de **population exposée**.

- Ajouter un deuxième algorithme `Joindre les attributs par valeur de champ` (eng.: `Join Attributes by Field Value`) au modèle.
- Ajouter une description: `Joindre les données de population avec les indicateurs santé et éducation`
- Configurer l’algorithme comme suit:
  - **Couche source**: `exposed_population` (sélectionner depuis la **Sortie de l’algorithme** des statistiques zonales)
  - **Couche d’entrée 2**: Sortie de l’étape précedente (santé + éducation)
  - **Champ de la table**: 
    ```
    ADM2_PCODE
    ```
  - **Champ de la table 2**: 
    ```
    ADM2_PCODE
    ```
  - **Champs à copier de la couche 2**: *(Entrer les noms de champs exactement comme ci-dessous — séparés par des points-virgules, sans espaces)*
    ```
    count_health_total;sum_exposed_health;pct_exposed_health;count_education_total;sum_exposed_education;pct_exposed_education
    ```
  - **Type de jointure** : Prendre uniquement les attributs de la première entité correspondante (un-à-un)
  - Laisser la sortie comme **Sortie du modèle** sans nom. 

```{figure} /fig/fr_MDG_AA_model_join_affacted_pop_HS_ES.PNG
---
width: 600px
name: the_world_result
align: center
---
Configuration de l’opération: joindre les données de population avec les indicateurs de santé et d’éducation.
``` 

::::{tip} Où trouver les noms des colonnes?  
Ouvrez les **tables attributaires** des couches `health_total_per_admin2`, `sum_exposed_healthsites_POI` et `admin2_health_affected_pct` dans QGIS.  
Consultez les **en-têtes de colonnes** pour trouver les noms exacts des champs à copier.
::::
::::{warning} Les espaces invisibles feront échouer la jointure!  
Si un nom de colonne comme `count_health_total` contient un espace invisible à la fin, la jointure échouera silencieusement.  
Copiez toujours les noms de champs **directement depuis la table attributaire** pour éviter les erreurs.
::::

1. Exporter les résultats vers un tableur
- Dans la **Boîte à outils de traitement**, recherchez `Exporter vers un tableur`(eng.: `Export to spreadsheet`) et double-cliquez pour ouvrir.
- Ajouter une description: `Exporter les données de population, d'éducation et de santé dans un seul tableau`
- Configurer l’outil comme suit:
  - **Couche d’entrée**: Sélectionner la sortie de l’étape précedente (3) depuis la **Sortie de l’algorithme**
  - **Tableur de destination**:
    ```
    exposure_indicators_spreadsheet
    ```
  - Cliquer sur **OK** pour l’ajouter au modèle.  


Une fois que vous exécutez le modèle, cette étape génèrera automatiquement un fichier tableur contenant tous les indicateurs nécessaires pour l’équipe des opérations!


```{figure} /fig/fr_MDG_AA_model_export_as_table.PNG
---
width: 600px
name: the_world_result
align: center
---
Exporter tous les indicateurs (population, santé, éducation) vers un tableau unique au format tableur.
``` 



5. **Valider et enregistrer votre modèle étendu**  
   - Cliquez sur le bouton ✔️ **Valider le modèle** (sous `Modèle` dans le menu du haut) pour vérifier les erreurs.
   - Enregistrez à nouveau sous:  
     **`Estimate_Exposed_Population_Health_Education.model3`**

6. **Exécuter le modèle**
   - Cliquez sur le bouton ▶️ **Exécuter** en haut à droite de la fenêtre du Modeleur graphique.
   - **Entrées:**
     - Cliquez sur les trois points pour chaque jeu de données et sélectionnez les entrées appropriées:
       - `Cyclone Track` → sélectionnez le fichier GeoJSON de la trajectoire de la tempête (ex. `Harald_2025_Track.geojson`)
       - `Population Raster` → sélectionnez le fichier raster WorldPop
       - `Admin Boundaries` → sélectionnez la couche de Niveau 2 (ex. `MDG_adm2.gpkg`)
       - `Health Facilities` → sélectionnez le jeu de données ponctuel des centres de santé
       - `Education Facilities` → sélectionnez le jeu de données ponctuel des écoles
   - **Sorties:**
     - Enregistrez toutes les couches de sortie dans le dossier de sortie en utilisant les noms ci-dessous:
       - `admin2_health_affacted` → 
         ```
         admin2_health_affected
         ```
       - `admin2_education_affected` →
         ```
         admin2_education_affected
         ```
       - `cyclone_harald_buffer` →  
         ```
         cyclone_harald_buffer
         ```
       - `exposed_population_sum` →
         ```
         admin2_harald_Exposed_Population
         ```
       - `exposure_indicators_spreadsheet` →
         ```
         exposure_indicators_harald
         ```
   - Cliquez sur **Exécuter** pour lancer le modèle complet.


::::{tab-set}

:::{tab-item} Modeleur

```{figure} /fig/
---
width: 600px
align: center
---

```
:::
:::{tab-item} Configuration d’exécution du modèle
```{figure} /fig/
---
width: 600px
align: center
---

```
:::
:::{tab-item} Résultat du modèle
```{figure} /fig/
---
width: 600px
align: center
---

```
:::
::::

---





## Tâche 7: Accessibilité des postes de santé depuis les entrepôts CRM <a id="tache-7-accessibilite-des-postes-de-sante-depuis-les-entrepots-crm"></a>

Lorsque qu’un cyclone est prévu pour un atterrissage, Aina collabore avec les équipes logistique et santé pour 
décider **où envoyer les kits médicaux prépositionnés**. Cependant, tous les entrepôts CRM ne stockent pas les 
articles nécessaires — seulement trois le font.

Pour prendre des décisions rapides et basées sur les données, Aina souhaite savoir **quels postes de santé sont accessibles** à partir de ces entrepôts **en moins de 10 heures**. Cette analyse permet de s’assurer que les kits 
sont envoyés vers des établissements **réellement accessibles à temps**.

Son objectif est de créer une carte visuelle claire montrant les postes de santé accessibles vs. non accessibles — 
et de la partager avec les décideurs le plus rapidement possible.


### 1. Filtrer les postes de santé depuis le jeu de données national des établissements de santé <a id="1-filtrer-les-postes-de-sante-depuis-le-jeu-de-donnees-national-des-etablissements-de-sante"></a>

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


### 2. Charger les couches isochrones pour les trois entrepôts CRM <a id="2-charger-les-couches-isochrones-pour-les-trois-entrepots-crm"></a>

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

### 3. Visualiser l’accessibilité des postes de santé depuis les entrepôts CRM <a id="3-visualiser-laccessibilite-des-postes-de-sante-depuis-les-entrepots-crm"></a>

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
