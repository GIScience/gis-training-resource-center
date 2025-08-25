::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 4 : Visualisation des résultats d'impact du cyclone - Aina applique des styles á ses couches


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

Cet exercice est le quatrième exercice de la piste d'exercice ["Analyse d’Action Anticipative pour les Cyclones à Madagascar"](/content/Exercise_tracks/fr_mdg_aa_cyclones.md)

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

# Tâches

Après avoir terminé son modèle, Aina souhaite **communiquer clairement les résultats** — à la fois à ses collègues de la Croix-Rouge et à des partenaires externes.

Elle en a **assez de devoir restyler manuellement chaque couche** à chaque fois que de nouvelles données cycloniques arrivent. À la place, elle veut :
- ✅ **Des visuels clairs et cohérents**
- 🔁 **Des modèles réutilisables**
- 📂 **Des fichiers .qml standardisés** partagés entre projets

Dans cette tâche, vous allez aider Aina à appliquer des styles `.qml` existants et à en créer de nouveaux pour les couches qui n’ont pas encore de style défini.

---


### 1. **Charger les couches nécessaires (si ce n’est pas déjà fait)**

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

### 2. **Appliquer des fichiers de style prédéfinis**
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

### 3. **Styliser manuellement les couches de pourcentage**

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

### 4. **Enregistrez vos nouveaux styles pour les réutiliser**

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


### 5. *(Optionnel)* Importer les styles dans votre bibliothèque QGIS

Pour réutiliser vos styles dans de futurs projets:

- Allez dans `Préférences` → `Gestionnaire de styles`
- Cliquez sur `Importer/Exporter` → `Importer des éléments`
- Parcourez et sélectionnez vos fichiers `.qml` enregistrés

Les styles apparaîtront désormais comme préréglages dans le **Panneau de style de couche**.

---
