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

- Show and explain each step yourself at least twice and slow enough so everybody can see what you are doing, and follow along in their own QGIS-project. 
- Make sure that everybody is following along and doing the steps themselves by periodically asking if anybody needs help or if everybody is still following.  
- Be open and patient to every question or problem that might come up. Your participants are essentially multitasking by paying attention to your instructions and orienting themselves in their own QGIS-project.

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
    - CRS cible : EPSG:29738 ou un autre SCR projeté en mètres adapté à Madagascar.
    - Enregistrez le résultat dans le dossier temp sous le nom: `Harald_Track_Reprojected`

```{figure} /fig/fr_MDG_AA_reproject_cyclon_track.PNG
---
width: 600px
align: center
---
Reprojeter la trajectoire du cyclone
```

```{Attention}
Les distances de tampon doivent être calculées en mètres. De nombreux jeux de données (comme les trajectoires de cyclone en GeoJSON) utilisent des systèmes de coordonnées géographiques (CRS) comme EPSG:4326, qui mesurent en degrés — et non en mètres. Pour calculer correctement un tampon de 200 km, il faut d’abord reprojeter la trajectoire dans un CRS projeté utilisant les mètres.
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

6. **Reprojeter la zone tampon en EPDG:4326 (pour correpondre au CRS de la couche raster)**


    - Dans la Boîte à outils de traitement, cherchez `Reprojeter une couche`
    - Couche source: `Harald_Buffer_200km_29738`
    - CRS (système de coordonnées de référence): `EPSG:4326 - WGS 84`.
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


- In the **Layers panel**, right-click on the layer `Harald_Exposed_Population` and choose `Properties`.
- Go to the **Symbology** tab on the left.
- At the top of the window, change the style from `Single Symbol` to `Graduated`.
- In the **Value** drop-down menu, select the field that contains the population sum. It typically starts with the prefix you defined earlier, e.g. `exposed_population_sum`.
- Set the **color ramp** to one that suits your map (e.g. `Reds`).
- Choose a **classification mode** (e.g. `)`, `Natural Breaks`, or `Equal Interval`) and select the number of classes (e.g. 5).
- Click `Classify` to generate the classification.
- Click `Apply` and then `OK` to display the classified map.

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
name: the_world_result
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
        - **Groupe**: `Outils de analysis cyclones`
        - Laissez la description vide ou ècrivez: *Modèle automatisé pour estimer la population exposée a partir d'un tampon autour du cyclone*.


3. **Enregistrer le modèle:**
   - Pour enregistrer le modèle:
     - Cliquez sur l'icône __Enregistrer__ (💾) ou naviguez à `Modèle` -> `Enregistrer`. 
     - Naviguez jusqu'au dossier `/models/` de votre structure de dossier pour la formation
     - Enregistrer le modèle sous: `Esimation_Population_Exposée`.


4. **Ajouter les entrées du modèle**:  
   - Dans le panneau gauche, ouvrez la section __Entrées__.
   - Ajouter les couches d'entrées  On the **left panel**, expand the **Inputs** section.
   - Add the following input layers with type constraints:
     - `+ Vector Layer`  
       - **Label**: `Cyclone Track`  
       - In the **Advanced panel**, set **geometry type** to `Line`
     - `+ Raster Layer`  
       - **Label**: `Population Raster`
     - `+ Vector Layer`  
       - **Label**: `Admin Boundaries`  
       - In the **Advanced panel**, set **geometry type** to `Polygon`
   - These will appear at the top of your model canvas and serve as the input data when the model is run.

     ```{tip}
     All inputs should be set as **mandatory**, so the model always receives the necessary data to run correctly.
     ```

::::{tab-set}

:::{tab-item} Input Cyclon Track
```{figure} /fig/fr_MDG_AA_model_input_cyclon_track.PNG
---
width: 600px
align: center
---
Definition of the model input: Cyclon Track
```
:::

:::{tab-item} Input Admin Boundaries 
```{figure} /fig/fr_MDG_AA_model_input_admin_bounderies.PNG
---
width: 600px
align: center
---
Definition of the model input: Admin Bounderies
:::

:::{tab-item} Population Raster
```{figure} /fig/fr_MDG_AA_model_input_population_raster.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
```
:::
::::
**Intermediate Result**

```{figure} /fig/fr_MDG_AA_intermediate_result_model_input.PNG
---
width: 600px
name: the_world_result
align: center
---
Résultat intermédiaire de la définition des données d'entrée du modèle
```

5. **Reproject the cyclone track to EPSG:29738**  
   - From the **Algorithms** panel, search for **Reproject Layer** .
   - In the configuration window:
     - Add a description: `Reprojecter la couche de trajectoire du cyclone a EPSG : 29738`
     - Set **Input layer** to `Cyclone Track` (from **Model Input**).
     - Set **Target CRS** to `EPSG:29738 – Madagascar / Laborde Grid`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_reporject_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter la couche de trajectoire du cyclone vers un système de référence de coordonnées métrique (CRS) EPSG : 29738
```
6. **Buffer the reprojected cyclone track**  
   - From the **Algorithms** panel, search for **Buffer**.
   - In the configuration window:
    - Add a description:  `Mettre en mémoire tampon la couche Cyclone reprojetée`
     - Add a description: 
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Distance** to `200000` (200 km).
     - Leave **Segments** at the default value (`5`).
     - Set **Dissolve result** to `Yes`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_buffer_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Mettre en mémoire tampon la couche Cyclone reprojetée
```
7. **Reproject the buffer back to EPSG:4326**  
   - From the **Algorithms** panel, search for **Reproject Layer**.
   - In the configuration window:
    - Add a description:  `Reprojecter le tampon vers EPSG:4326`
   - In the configuration window:
     - Set **Input layer** to the output from the previous step (from **Algorithm Output**).
     - Set **Target CRS** to `EPSG:4326 – WGS 84`.
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_reporject_bufferd_cyclon_track.PNG
---
width: 600px
name: the_world_result
align: center
---
Reprojecter le tampon vers EPSG:4326
```
8. **Clip the population raster using the buffered area**  
   - From the **Algorithms** panel, search for **Clip Raster by Mask Layer** .
   - In the configuration window:
     - Add a description: `Découper la couche raster de population pour l'étendre au tampon Cyclon`
   - In the configuration window:
     - Set **Input layer** to `Population Raster` (from **Model Input**).
     - Set **Mask layer** to the output from the previous step (from **Algorithm Output**).
     - Set the output to **Model Output** (leave the output name **empty**).
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_clip_pop_raster.PNG
---
width: 600px
name: the_world_result
align: center
---
Découper la couche raster de population pour l'étendre au tampon Cyclon
```
9. **Calculate zonal statistics to estimate exposed population**  
   - From the **Algorithms** panel, search for **Zonal Statistics** .
   - In the configuration window: Calcul de la population exposée aux cyclones par district
     - Add a description: `Calcul de la population exposée aux cyclones par district`
     - Set **Input layer** to `Admin Boundaries` (from **Model Input**).
     - Set **Raster layer** to the output of the previous step (from **Algorithm Output**).
     - Set **Output column prefix** to `exposed_population_`.
     - Under **Statistics to calculate**, select `Sum`.
     - Set the output to **Model Output** and name it: 
      ```
      exposed_population_sum
      ```
   - Click **OK** to add the step to the model.
```{figure} /fig/fr_MDG_AA_model_zonal_statistic_pop_admin2.PNG
---
width: 600px
name: the_world_result
align: center
---
Calcul de la population exposée aux cyclones par district
```

**Your results should look something like this:** 

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms.PNG
---
width: 600px
name: the_world_result
align: center
---
Votre modèle devrait ressembler à ceci. Tous les algorithmes sont correctement connectés et la sortie du modèle est définie.
```

10. **Validate your model (recommended)**
   - Before saving or running, click the ✔️ **Validate Model** button in the top toolbar.
   - Fix any warnings or errors shown in the log panel.
   - This helps ensure your model is complete and won't break during execution.

11. **Run the model**  
   - Run the model by clicking on `Model` -> `Run Model`
   - Set **Admin Bounderies** to `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Set **Cyclone Track** to `example_Harald_2025_Track`
   - Set **Population Raster** to `MDG_WorldPop_2020_constrained.tif`
   - Set the model output **exposed_population_sum** to `Harald_Exposed_Population`and save it in the `data` -> `output`


You can now run this model any time a new cyclone track becomes available.

```{figure} /fig/fr_MDG_AA_model_run_model_M7_e1_task2.PNG
---
width: 600px
name: the_world_result
align: center
---
Pour exécuter le modèle, spécifiez l'entrée comme indiqué dans l'image et définissez le nom de la couche de sortie.
```

**Your results should look something like this:**
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_basics.PNG
---
width: 600px
name: the_world_result
align: center
---

``` 
12. **Add the cyclone buffer as an additional model output**  
   - Double-click on the algorithm from step 7 (**Reproject the buffer back to EPSG:4326**) to open its configuration.  
   - In the **Output layer** field, check the box for **Model Output**.  
   - Give the output a clear name, for example:
     ```
     cyclone_harald_buffer
     ```  
   - Click **OK** to save the change.  
   - This will allow the model to produce both the exposed population results and the buffered cyclone impact zone when it is run.

```{figure} /fig/fr_MDG_AA_model_output_buffer.PNG
---
width: 600px
name: the_world_result
align: center
---
```

13. **Run the model again**  
   - Run the model by clicking on `Model` -> `Run Model`
   - Set **Admin Bounderies** to `mdg_admbnda_adm2_BNGRC_OCHA_20181031.gpkg`
   - Set **Cyclone Track** to `example_Harald_2025_Track`
   - Set **Population Raster** to `MDG_WorldPop_2020_constrained.tif`
   - Set the model output **cyclone_harald_buffer** to `cyclone_harald_buffer`and save it in the `data` -> `output`
   - Set the model output **exposed_population_sum** to `Harald_Exposed_Population`and save it in the `data` -> `output`


::::{tab-set}


:::{tab-item} Graphic Modler Output Buffer 

```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_graphic.PNG
---
width: 600px
name: the_world_result
align: center
---
```
Definition of the model input: Admin Bounderies
:::

:::{tab-item} Run Model with Buffer Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_task1_buffer_output_model_model_exicution.PNG
---
width: 600px
align: center
---
Definition of the model input: Population Raster
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



## Task 3: Identifying Affected Health Facilities and Schools – Aina Adds More Layers

After building her model to estimate exposed population, Aina wants to expand its usefulness. She decides to also **identify critical services** affected by cyclones — especially **health facilities** and **schools**. 

Not only does she want to know *which* facilities are affected, but also *how many in total exist* per district. That way, she can calculate the **percentage of services affected** in each area.

To achieve this, she will use two point datasets from OpenStreetMap:

- [Health facilities](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)  
- [Education facilities](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

1. **Load the health and education facilities datasets**
First, let's have a look at the data we want to work with.
- Navigate to your `input` data folder.  
- Drag and drop the following layers into your QGIS project:  
  - `hotosm_mdg_health_facilities`  
  - `hotosm_mdg_education_facilities`  
- Confirm that both layers are visible in the **Layers Panel** 
2. **Save your model under a new name**  
   - Open your existing model `Estimate_Exposed_Population.model3`.
   - Immediately save it under a new name:
     - Click `Model` → `Save As…`
     - Save it to the `project` folder as:
```  
Estimate_Exposed_Population_Health_Education
```
3. **Add new model inputs**  
   - In the **Inputs** section, add:
     - `Vector Layer`  
       - **Description**:
        ```
        Health Facilities
        ```
       - Set **Geometry Type** to `Point`
     - `Vector Layer`  
       - **Description**:
        ```
        Education Facilities
        ``` 
       - Set **Geometry Type** to `Point`
::::{tab-set}

:::{tab-item} Model Input: Health Facilities
```{figure} /fig/fr_MDG_AA_model_input_health_facilities.PNG
---
width: 300px
name: the_world_result
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements de santé
```
:::
:::{tab-item} Model Input: Education Facilities
```{figure} /fig/fr_MDG_AA_model_input_education_facilities.PNG
---
width: 300px
align: center
---
Définir une nouvelle entrée de modèle : couche vectorielle de points représentant les établissements d'enseignement
```
:::
::::
3. **Count All Health Facilities per Admin 2**  
   - From the **Algorithms** panel, search for **Count Points in Polygon**.
   - Configuration:
     - Add a description: `Comptez le nombre d'établissements de santé dans chaque district.`
     - **Polygon layer**: `Admin Boundaries` (Model Input)
     - **Points layer**: `Health Facilities` (Model Input)
     - **Count field name**: 
      ```
      Count_health_total
      ```
     - Leave output as **Model Output**
```{figure} /fig/fr_MDG_AA_model_count_points_HF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements de santé dans chaque district.
```    
4. **Count All Education Facilities per Admin 2**  
   - Add another **Count Points in Polygon** step.
   - Configuration:
     - Add a description: `Comptez le nombre d'établissements de education dans chaque district`
     - **Polygon layer**: `Admin Boundaries` (Model Input)
     - **Points layer**: `Education Facilities` (Model Input)
     - **Count field name**: 
      ```
      count_education_total
      ```
     - Leave output as **Model Output**
```{figure} /fig/fr_MDG_AA_model_count_points_EF_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter le nombre d'établissements scolaires dans chaque district.
```
5. **Intersect Health Facilities with Cyclone Buffer**  
   - From the **Algorithms** panel, search for **Intersection**.
   - In the configuration window:
   - Add a description: 
      ```
      Établissements de santé dans la zone d'impact du cyclone
      ```  
     - **Input layer**: `Health Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output** 
   - Click **OK**
```{figure} /fig/fr_MDG_AA_model_clip_intersect_HF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de santé avec la zone d'impact du cyclone.
```
6. **Intersect Education Facilities with Cyclone Buffer**  
   - Add another **Intersection** algorithm.
   - Configuration:
     - Add a description:
       ```
       Établissements de education dans la zone d'impact du cyclone.
       ```  
     - **Input layer**: `Education Facilities` (Model Input)
     - **Overlay layer**: buffered cyclone zone (use “Reprojected to EPSG:4326” from **Algorithm Output**)
     - Leave output as **Model Output**
   - Click **OK**
```{figure} /fig/fr_MDG_AA_model_clip_intersect_EF_cyclone_buffer.PNG
---
width: 600px
align: center
---
Configuration de l'opération : intersecter les établissements de education avec la zone d'impact du cyclone.
```
7. **Count Affected Health Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Configuration:
     - Add a description: 
       ```
       Compter les établissements de santé touchés par district
       ```  
     - **Polygon layer**: Count total health facilities output
     - **Points layer**: intersected health facilities output
     - **Count field name**: 
       ```
       sum_exposed_healthsites_POI
       ```  
```{figure} /fig/fr_MDG_AA_model_count_points_HF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
8. **Count Affected Education Facilities per Admin 2**  
   - Add **Count Points in Polygon**
   - Configuration:
     - Add a description: 
       ```
       Compter les établissements education touchés par district
       ```   
     - **Polygon layer**: Count total education facilities output
     - **Points layer**: intersected education facilities output
     - **Count field name**: 
       ```
       sum_exposed_education_POI
       ```  
```{figure} /fig/fr_MDG_AA_model_count_points_EF_affected_admin2.PNG
---
width: 600px
align: center
---
Configuration de l'opération : compter les établissements de santé touchés par district.
```
9. **Calculate percentage of affected Health Facilities**
To compute the percentage of affected health sites per administrative area, we will use the **Field Calculator**:
- Add the  **Field Calculator**:
   - Configuration:
     - Add a description:
       ```
       Calculer le pourcentage d’établissements de santé touchés par district
       ```  
    - **Input layer**: the output of Count Affected Health Facilities per Admin 2
    - **Output field name**:  
       ```
       pct_health_affected
       ``` 
    - **Field type**: Decimal (real)
    - **Expression**:
    ```qgis
    CASE WHEN "count_health_total" > 0
    THEN "sum_exposed_healthsites_POI" / "count_health_total" * 100
    ELSE 0
    END
    ```
  - Set the output as **Model Output**
  - Name it:
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
10. **Calculate percentage of affected Education Facilities**
To compute the percentage of affected education sites per administrative area, we will use the **Field Calculator**:  
- Add the **Field Calculator**:  
   - Configuration:  
     - Add a description:  
       ```
       Calculer le pourcentage d’établissements d’éducation touchés par district
       ```  
     - **Input layer**: the output of Count Affected Education Facilities per Admin 2  
     - **Output field name**:  
       ```
       pct_education_affected
       ```  
     - **Field type**: Decimal (real)  
     - **Expression**:  
       ```qgis
       CASE WHEN "count_education_total" > 0
       THEN "sum_exposed_education_POI" / "count_education_total" * 100
       ELSE 0
       END
       ```  
   - Set the output as **Model Output**  
   - Name it:  
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
11. **Validate and Save Your Extended Model**  
   - Click the ✔️ **Validate Model** button to check for errors.
   - Save again to:  
     **`Estimate_Exposed_Population_Health_Education.model3`**
12. **Run the model**
   - Click the ▶️ **Run** button in the top-right corner of the Graphical Modeler window.
   - In the popup dialog:
     - Browse to select the required input layers:
       - `Cyclone Track` → select the GeoJSON of the storm path (e.g. `Harald_2025_Track.geojson`)
       - `Population Raster` → select the WorldPop raster file
       - `Admin Boundaries` → select the Admin 2 layer (e.g. `MDG_adm2.gpkg`)
       - `Health Facilities` → select the point dataset for health sites
       - `Education Facilities` → select the point dataset for schools
     - Choose a location to save the output for the final layers (you can leave intermediate layers in temporary memory).
   - Click **Run** to execute the full model.
   - When finished, you should see all final output layers loaded into your QGIS workspace.

::::{tab-set}

:::{tab-item} Graphic Modler

```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model.PNG
---
width: 600px
align: center
---
Vue d’ensemble du Modèle Graphique de la tâche 3 montrant tous les algorithmes connectés et les sorties définies.
```
:::
:::{tab-item} Run Model Configuration
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_run_configurations.PNG
---
width: 600px
align: center
---
Configuration des paramètres pour exécuter le modèle de la tâche 3 avec toutes les couches d’entrée requises.
```
:::
:::{tab-item} Model Output
```{figure} /fig/fr_MDG_AA_intermediate_result_model_algorythms_task3_exposed_HF_EF_model_results_AT.PNG
---
width: 600px
align: center
---
Résultats du modèle de la tâche 3 affichés dans QGIS, y compris les pourcentages d’établissements de santé et d’éducation touchés par district.
```
:::
::::


## Task 4: Visualizing Cyclone Impact Results – Aina Styles Her Maps

After completing her model, Aina wants to **communicate the results clearly** — both to her Red Cross colleagues and external partners.

She’s **tired of manually restyling every layer** every time new cyclone data comes in. Instead, she wants:
- ✅ **Clear and consistent visuals**
- 🔁 **Reusable templates**
- 📂 **Standardized .qml files** shared across projects

In this task, you will help Aina apply existing `.qml` styles and create new ones for layers that currently have no preset style.

---

### 1. **Load Required Layers (if not already loaded)**

Make sure the following layers are already loaded into your QGIS project. These are outputs from **Task 3**:

- `Harald_2025_Track`
- `Harald_Buffer_200km`
- `Harald_Exposed_Population`
- `sum_exposed_healthsites_POI`
- `sum_exposed_education_POI`
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

If any are missing:
- Load them using **drag & drop** from your `results` folder, or
- Use `Layer` → `Add Layer` → `Add Vector Layer` or `Add Raster Layer`

---

### 2. **Apply Predefined Style Files**
Apply the following `.qml` style files to the respective layers:

| **Layer**                              | **Style File**                            |
|----------------------------------------|-------------------------------------------|
| `Harald_2025_Track`                    | `storm_track_cyclone_style.qml`           |
| `Harald_Buffer_200km`                  | `exposed_cyclone_area_style.qml`          |
| `Harald_Exposed_Population`            | `exposed_population_style.qml`            |
| `sum_exposed_healthsites_POI`          | `exposed_healthsites_style.qml`           |
| `sum_exposed_education_POI`            | `exposed_education_facilities_style.qml`  |

**Steps:**
- Open the **Layer Styling Panel**
- Click the `Style` button → `Load Style…`
- Navigate to the corresponding `.qml` file
- Click **OK** to apply the style

> 💡 *If the style doesn’t load correctly, double-check the column names and make sure the column name used in the `.qml` file matches the one in your layer. To do this, open the **Attribute Table** of the layer and compare field names.*

---

### 3. **Style Percentage Layers Manually**

Now let’s style the two **percentage layers** that don’t yet have `.qml` files:
- `admin2_health_affected_pct`
- `admin2_education_affected_pct`

**Steps:**
- Select the layer and open the **Layer Styling Panel**
- Set **Symbology** to `Graduated`
- Choose the correct **field**:
  - `pct_health_affected` or `pct_education_affected`
- Open the **Histogram** tab to view the value distribution
- Set:
  - **Mode**: `Equal Interval`
  - **Classes**: `4`
  - **Breaks**: `0–25%`, `25–50%`, `50–75%`, `75–100%`
- Choose a color ramp (e.g., light yellow → dark red)
- Optionally customize class labels for clarity

> 🧠 *Why 4 equal classes?*  
> This helps visualize severity across districts using simple and interpretable risk categories. However, you can experiment with **Natural Breaks** if data is unevenly distributed.

---

### 4. **Save Your New Styles for Reuse**

Save your manually created styles as `.qml` files for future reuse.

**Steps:**
- In the **Styling Panel**, click `Style` → `Save Style…`
- Save the file in the same folder as the corresponding dataset
- Use these filenames:
  - `health_pct_affected_style.qml`
  - `education_pct_affected_style.qml`
---

### 5. *(Optional)* Import Styles into Your QGIS Library

To reuse your styles in any future project:

- Go to `Settings` → `Style Manager`
- Click `Import/Export` → `Import Items`
- Browse to and select your saved `.qml` files

The styles will now appear as presets in the **Layer Styling Panel**.

---

## Task 5: Quick Map Creation – Aina Uses Map Templates
Background: Aina Gets Map-Ready in Minutes
After preparing all the analysis and styling, Aina wants to present her results quickly and professionally. She doesn’t want to recreate map layouts every time — she needs a quick way to generate clean, consistent maps.

That’s why she’s using map templates (.qpt files) already prepared by her team. These templates include map frames, legends, logos, titles, scale bars, and more — everything Aina needs to finish her product in just a few clicks.

✅ Goal
Use a provided QGIS map template to visualize and export maps showing cyclone exposure results, including population, health, and education impacts.

1. Load the pre-made print layout template

- Locate the template `cyclone_impact_overview_map_template.qpt` in your project folder under:  
  `Map_Templates/`

- You can load the template **by drag-and-drop**:
  - Open your QGIS project.
  - Navigate to the Print Layout area in the browser panel.
  - Drag the `.qpt` file directly into QGIS — a new layout will be created automatically.

- Alternatively:
  - Go to `Project` → `New Print Layout`
  - Enter a name (e.g. `Harald_2025_Overview`)
  - Click `OK`
  - In the layout, go to `Layout` → `Import from Template…`
  - Select the file `cyclone_impact_overview_map_template.qpt` and click `Open`
 2. Check and set page size
- Right-click anywhere on the white canvas and choose `Page Properties`.
- On the right-side panel, ensure the following:
  - **Page Size**: A3
  - **Orientation**: Landscape
3. Update the attribute table of exposed districts
- In the **Print Layout**, click on the attribute table (right-hand side of the layout).
- In the **Item Properties** panel:
  - Ensure the correct layer is selected (e.g. `Exposed_Districts`)
  - Click `Refresh Table Data`
  - Click `Attributes…` → ➕ Add:
    - **Attribute**: `ADM1_EN`
    - **Sort Order**: Ascending
  - Click `OK`
5. Adjust the legend
- In the layout, click on the **Legend** item.
- In the **Item Properties** panel:
  - Uncheck **Auto update**
  - Scroll to **Legend items** and remove all entries (🗑️)
  - Add the following relevant layers:
    - `Relevant_Warehouses`
    - `Exposed_Cyclone_Area`
    - `Exposed_Districts`
    - `Admin1_Impact_Overview_Map`
  - When selecting layers, check **Only visible layers**
  - Rename legend entries to match layout naming
6. Review and update layout text elements
- Make sure all text elements are up to date, especially:
  - **Map title**
  - **Cyclone name and date**
  - **Author/Organization** (optional)
- Adjust font size or alignment if necessary


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
The map now clearly displays the exposed population within the affected districts, along with the locations of relevant warehouses. The original storm track line — used as input data — is highlighted, as well as the buffered impact area, which serves as a proxy for identifying exposed districts.

On the right-hand side of the map, a list shows all exposed districts, including data on total population and exposed population. The districts (Admin 2) are organized under their corresponding regions (Admin 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map.png
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
- Open `Estimate_Exposed_Population_Health_Education.model3`
- Save a backup as:  
  `Estimate_Exposed_Population_Health_Education_Export.model3`
2. Join Health and Education data into one layer
- In the **Algorithms**, search for `Join Attributes by Field Value`.
- Configure the algorithm as follows:
  - **Input Layer**: `admin2_health_affected_pct` (select from **Algorithm Output**)
  - **Input Layer 2**: `admin2_education_affected_pct` (select from **Algorithm Output**)
  - **Table field**: `ADM2_PCODE`
  - **Table field 2**: `ADM2_PCODE`
  - **Layer 2 fields to copy**: Leave empty (all fields will be copied)
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**
3. Join the result with the population data
Now join the result of the previous step (health + education) to the **exposed population** data.
- Add a second `Join Attributes by Field Value` algorithm to the model
- Configure the algorithm as follows:
  - **Input Layer**: `exposed_population` (select from **Algorithm Output** of the Zonal Statistics step)
  - **Input Layer 2**: Output from Step 2 (health + education)
  - **Table field**: `ADM2_PCODE`
  - **Table field 2**: `ADM2_PCODE`
  - **Layer 2 fields to copy**: *(Enter the following field names exactly as shown — comma-separated, no spaces)*
    ```
    count_health_total,sum_exposed_healthsites_POI,health_affected_precentage,count_education_total,sum_exposed_education_POI,pct_education_affected
    ```
  - **Join type**: Take attributes of the first matching feature only (one-to-one)
  - Leave output as **Model Output**
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
- Configure the tool as follows:
  - **Input Layer**: Select the output of Step 3 from **Algorithm Output**
  - **Destination spreadsheet**:
    ```
    exposed_indicators_spreadsheet.xlsx
    ```

  - Click **OK** to add it to the model.
Once you run the model, this step will automatically generate a spreadsheet with all relevant indicators ready for the operations team!

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





