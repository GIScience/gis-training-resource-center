::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 2 : Création rapide de cartes – Aina utilise des modèles de carte

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

## Tâches:

Après tout le travail d’analyse et de stylisation, Aina est prête à **partager ses résultats**. Mais créer une 
carte professionnelle à partir de zéro à chaque fois serait long et répétitif.  

Pour gagner du temps, elle utilise des **modèles de carte (.qpt)** préparés par son équipe. Ces modèles 
contiennent déjà les éléments essentiels — cadres cartographiques, légendes, logos, titres et barres d’échelle. 
Grâce à eux, Aina peut transformer son analyse en une **carte claire et cohérente** en seulement quelques clics.  


✅ **Objectif**  
Appliquer un modèle de carte QGIS prêt à l’emploi pour créer et exporter rapidement des cartes montrant les impacts du cyclone sur la population, les établissements de santé et les écoles.  

---

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

### ✅ Liste de vérification finale

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
