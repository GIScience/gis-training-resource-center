::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 6 : Exporter les résultats du modèle pour l’équipe des opérations

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

## Données disponibles

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/GIS_AA/MDG/Module_7_Exercise_4_AA_MDG_task_6-20250825T143514Z-1-001.zip

__Téléchargez les données pour cet exercice ici et dezipé le fichier.__
:::






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
