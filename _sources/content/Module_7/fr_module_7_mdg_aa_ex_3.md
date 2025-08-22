::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 2 : Identification des établissements de santé et d'éducation impactés – Aina ajoute des couches supplémentaires


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

Cet exercice est le troisième exercice de la piste d'exercice ["Analyse d’Action Anticipative pour les Cyclones à Madagascar"](/content/Exercise_tracks/fr_mdg_aa_cyclones.md)

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


Après avoir construit son modèle pour estimer la population exposée, Aina souhaite améliorer son utilité. Elle décide d'identifier également les services essentiels affectés par les cclones — en particulier les établissments de santé et les écoles. 

Elle veut non seulement savoir quels établissements sont affectés, mais aussi combien il en existe au total par district. Cela lui permettera de calculer le __pourcentage de service affectés__ dans chaque zone. 

Pour cela, elle utilisera deux jeux de données contenant des points issus d'OpenStreetMap:

- [Établissement de santé](https://data.humdata.org/dataset/hotosm_mdg_health_facilities)
- [Établissement d'éducation](https://data.humdata.org/dataset/hotosm_mdg_education_facilities)

# Tâches

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

