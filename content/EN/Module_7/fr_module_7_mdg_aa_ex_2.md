::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice : Automatisation de l'estimation de la population exposée - Le Modèle d'Aina


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

Cet exercice est le deuxième exercice de la piste d'exercice ["Analyse d’Action Anticipative pour les Cyclones à Madagascar"](/content/Exercise_tracks/fr_mdg_aa_cyclones.md)

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

Après avoir estimé manuellement les populations exposées lors des saisons cycloniques précédentes, Aina a décidé de créer un __modèle automatisé__ à l’aide du __Modeleur Graphique de QGIS__.
Cela lui permettra d’agir plus rapidement et d’éviter de répéter les mêmes étapes à chaque fois qu’un cyclone est annoncé.

Dans cette tâche, vous allez aider Aina à construire une version simple de ce modèle, en réutilisant les outils de la Tâche 1. Le modèle doit effectuer les étapes suivantes:

- Reprojeter la trajectoire du cyclone en EPSG:29738
- Créer une zone tampon autour de cette trajectoire  
- Reprojeter la zone tampon en EPSG:4326
- Découper le raster de population  
- Appliquer les statistiques zonales pour obtenir la population exposée par district

---

## Téléchargement des données pour cet exercice

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_7_Exercise_2_AA_MDG_task_2-20250825T143513Z-1-001.zip

__Téléchargez les données pour cet exercice ici et dezipé le fichier.__
:::

## Tâches 

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



