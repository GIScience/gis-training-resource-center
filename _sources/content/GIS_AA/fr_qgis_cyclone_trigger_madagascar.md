# Workflow de déclenchement en QGIS pour Madagascar

<!-- Maybe have a final look over introduction and all the official stuff which should be included in the documentation -->

Le workflow QGIS présenté dans cet article a été développé dans le cadre du projet "Anticipatory-Action" (AA) (action anticipative) de la Croix-Rouge malgache (CRM), de la Croix-Rouge allemande (GRC) et de l'institut de Heidelberg pour les technologies de géoinformation (HeiGIT).

Le workflow est presque entièrement automatisé grâce à un modèle QGIS et ne nécessite aucune intervention manuelle. Le chapitre --Automated Trigger Workflow--- décrit le processus et l'application pratique. <!-- what chapter?? Where is it?--> 
Chaque étape inclut dans le modèle est expliquée en détail afin de permettre une compréhension complète du workflow et de la manière dont l'analyse a été réalisée.

## Contexte

La définition de déclencheurs est l'un des piliers du système de financement basé sur les prévisions (anglais: Forecast-based financing (FbF)). Pour qu'une Société Nationale puisse bénéficier d'un financement automatique pour ses actions précoces, son protocole d'action précoce doit définir clairement où et quand les fonds seront alloués et l'aide fournie. Dans le cadre de l'AA, cela est décidé en fonction de valeurs seuils spécifiques, appelées "déclencheurs", basées sur les prévisions météorologiques et climatiques, qui sont définies pour chaque région (voir [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/06-develop-a-trigger-system/)).

## Déclaration de déclenchement

**Déclencheur préalable à l'activation:** au moins une des prévisions météorologiques de Météo Madagascar, du RMSC La Réunion ou de l'ECMWF prévoit une probabilité supérieure à 50% qu'un cyclone tropical de force tempête tropicale ou plus atteigne les côtes dans les 7 prochains jours.

**ADéclencheur d'activation:** si les prévisions de Météo Madagascar (DGM) indiquent l'arrivée d'un cyclone tropical avec des vents dépassant 118 km/h dans les 48 à 72 heures à venir.

# Téléchargement du rapport

<!-- This section will include information on how to download the final report as soon as its published -->

# Fonctionnalité du flux de travail

Le concept de processus déclencheur est illustré dans la figure ci-dessous.

```{figure} /fig/MAD_Trigger_concept.png
---
width: 1000px
name: fig-trigger-concept
align: center
---
```
<!--do we need french alternative text describing the figure?-->

Le projet QGIS présenté contient les couches nécessaires et un fichier modèle QGIS permettant d'évaluer l'impact potentiel du cyclone prévu. Le processus d'analyse sera exécuté dans le modèle QGIS, qui automatise les étapes d'évaluation de l'impact d'un cyclone tropical.  Il intègre les données relatives à la trajectoire du cyclone avec les frontières administratives, les données démographiques, les infrastructures et les positions des services afin d'identifier et de quantifier les zones et les ressources exposées. 
Sur la base des prévisions cycloniques de Météo Madagascar, le modèle calcule la zone susceptible d'être exposée au cyclone, la population potentiellement exposée, le nombre de bâtiments exposés, les terres agricoles exposées et les établissements de santé et d'enseignement potentiellement exposés.

De plus, le fichier QGIS contient des couches représentant les entrepôts CRM et les zones qu'ils peuvent couvrir, ce qui permet d'évaluer rapidement leur accessibilité. Le dossier fourni contient également des modèles de carte et des fichiers de style permettant de générer des rapports cartographiques basés sur les calculs du modèle. 

La documentation est divisée en deux parties. La première partie traite de l'analyse spatiale à l'aide du modèle QGIS automatisé. La deuxième partie explique comment créer des rapports cartographiques à l'aide des modèles de carte et des fichiers de style.

<!--Insert image of report?-->

:::{attention}

Le projet et le modèle ont été créés à l'aide de la version 3.40.9 (LTR) Bratislava de QGIS. Afin de garantir le bon fonctionnement du modèle, n'utilisez pas de versions antérieures de QGIS.

:::

## Données disponibles

Pour que le mécanisme de déclenchement fonctionne correctement, nous utilisons actuellement différents ensembles de données: des données que nous supposons statiques à court terme et des données variables qui décrivent les ensembles de données qui seront vérifiés régulièrement pour déclencher le mécanisme en fonction de la survenue d'événements cycloniques anticipés.

### Données fixes

Par données fixes, nous entendons les ensembles de données nécessaires à la création des rapports cartographiques, qui ne sont pas susceptibles de changer à court terme. À long terme, ces ensembles de données peuvent être facilement adaptés.

| Ensemble de données | Source | Descriptions |
| ----- | --- | --- |
| Limites administratives | [HDX](https://data.humdata.org/dataset/cod-ab-mdg) | Les limites administratives de niveau 0 à 4 pour Madagascar sont accessibles via HDX fourni par OCHA. Pour ce mécanisme de déclenchement, nous fournissons les limites administratives de niveau 1 (niveau régional) et 2 (niveau district) sous forme de fichier shapefile. |
| Nombre de Point d'intérêt (POI) | [HOT Export Tool](https://export.hotosm.org/vi/v3/exports/new/describe) | Les données POI (établissements scolaires et sites de santé) sont téléchargées à l'aide de l'outil HOT Export Tool basé sur les données OpenStreetMap. |
| Entrepôts CRM | Croix-Rouge Malagasy | Cette couche contient des points représentant les emplacements des entrepôts CRM. |
| Isochrones des entrepôts CRM | HeiGIT | À l'aide de la [surface de friction globale](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_friction_surface_2019#bands), nous avons calculé la zone pouvant être atteinte en un temps donné en voiture à partir d'un entrepôt donné. | 
| Chiffres de population | [WorldPop](https://hub.worldpop.org/geodata/summary?id=49646) | L'ensemble de données WorldPop au format raster fournit une estimation du nombre total d'habitants par cellule de grille pour l'année 2020. Nous travaillerons avec l'ensemble de données `Constrained Individual countries 2020` à une résolution de 100 m. |
| Nombre de bâtiments | [Global ML Building Footprints](https://gee-community-catalog.org/projects/msbuildings/) | L'ensemble de données sur le nombre de bâtiments au format raster compte le nombre de bâtiments par cellule de grille de 100 m. Le processus de création de cet ensemble de données est disponible sur [GitLab](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar). |
| Couverture terrestre | [ Copernicus Land Cover](https://land.copernicus.eu/en/products/global-dynamic-land-cover/copernicus-global-land-service-land-cover-100m-collection-3-epoch-2019-globe) | L'ensemble de données sur la couverture terrestre au format raster fournit une vue d'ensemble du type de couverture terrestre dominant avec une résolution de 100 m. Le processus de téléchargement de cet ensemble de données est disponible sur [GitLab](https://gitlab.heigit.org/giscience/disaster-tools/fbf/aa_madagascar). |

:::{admonition} Raster Principal
:class: note

Les trois ensembles de données raster sont combinés en un **raster principal**, une couche raster multibande avec une résolution spatiale de 100 mètres. Cette couche composite comprend les informations suivantes sur trois canaux :
1. Nombre d'habitants par cellule de grille d'après Worldpop constrained (2020)
2. Nombre de bâtiments par cellule de grille d'après ML Building Footprints (2021)
3. Type de couverture terrestre par cellule de grille d'après Copernicus Land Cover (2019)

:::

### Données de monitoring

```{admonition} Attention
:class: attention

Les informations prévisionnelles proviendront du DGM (Météo Madagascar), qui fournira les données de trajectoire des cyclones tropicaux pour le workflow de déclenchement.
```

Pour analyser les événements passés, il est possible d'utiliser les données fournies par la NOAA (National Centers for Environmental Information). Les trajectoires des cyclones sont fournies dans le cadre du projet [International Best Track Archive for Climate Stewardship (IBTrACS)](https://www.ncei.noaa.gov/products/international-best-track-archive). Il s'agit de la collection mondiale la plus complète sur les cyclones tropicaux disponible à ce jour. Elle regroupe les données récentes et historiques sur les cyclones tropicaux provenant de plusieurs agences afin de créer un ensemble de données unifié, accessible au public et représentant les meilleures trajectoires. L'IBTrACS a été développé en collaboration avec tous les centres météorologiques régionaux spécialisés de l'Organisation météorologique mondiale (World Meteorological Organization (WMO)), ainsi qu'avec d'autres organisations et individus du monde entier.

:::{admonition} Trajectoires des cyclones
:class: hint

Les données relatives aux trajectoires des cyclones tropicaux sont disponibles sous forme de différents sous-ensembles, en fonction de l'échelle temporelle qui vous intéresse. Des sous-ensembles régionaux peuvent également être générés, les données relatives à l'**océan Indien sud** étant particulièrement importantes pour ce mécanisme de déclenchement.

:::

# Estimation de l'impact du cyclone à l'aide du modèle QGIS

Comme expliqué au début de ce chapitre, le workflow déclencheur développé est exécuté automatiquement par un modèle QGIS. Dans ce chapitre, nous expliquerons son fonctionnement et, dans une étape ultérieure, nous expliquerons comment exécuter le modèle automatisé.

## Fonctionnement du modèle

<!-- Have a final look over this section to see if all the important information is covered -->

Les étapes clés suivantes sont exécutées dans le modèle :

1. Mise en mémoire tampon du cyclone et extraction de la zone d'impact 
   * La trajectoire du cyclone est mise en mémoire tampon afin de créer une zone d'impact estimée. La mémoire tampon est dissoute pour générer un polygone unique représentant la zone exposée au cyclone. Cette couche sert de base pour les calculs d'exposition ultérieurs.

2. Unités administratives exposées  
   * La zone tampon du cyclone est recoupée avec les limites des districts (Admin 2) afin d'extraire les districts exposés. Ceux-ci sont ensuite reliés aux régions (Admin 1) à l'aide de la région (Admin 1) afin de créer des zones de risque.

3. Effet sur la population
    * Le modèle utilise le raster de population pour calculer les statistiques zonales sur les districts exposés. Cela permet de déterminer la population totale par district et la population exposée, qui sont ensuite exportées vers un tableau.

4. Effet sur les infrastructures
    * La zone tampon du cyclone est croisée avec:
        * Les bâtiments pour extraire les bâtiments exposés.
        * Les couches des sites de santé et des établissements d'enseignement pour extraire et résumer les points d'intérêt exposés.
    Ces ensembles de données sont combinés dans un tableau qui résume les infrastructures exposées.

<!---5. Warehouse Accessibility
    * Warehouses are filtered based on proximity to exposed regions. The model uses road data and spatial filters to determine accessible warehouses relevant to the response.
5. Accessibilité des entrepôts
   * Les entrepôts sont filtrés en fonction de leur proximité avec les régions exposées. Le modèle utilise des données routières et des filtres spatiaux pour déterminer les entrepôts accessibles pertinents pour l'intervention.
-->

## Comment exécuter le modèle

Le [QGIS Model Designer](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_automatisation_wiki.html#the-qgis-model-designer) est un outil visuel qui permet aux utilisateurs de créer et de modifier un flux de travail avec tous les outils disponibles dans QGIS qui peuvent être utilisés de manière répétée, simple et rapide, tout en garantissant la reproductibilité. Il fournit une interface graphique pour créer des flux de travail en connectant des outils et des algorithmes de géomatique. L'utilisateur peut définir les entrées, les sorties et le flux de données entre les différentes étapes de traitement.


## Étape 1 : Explication de la structure des fichiers

```{figure} /fig/MAD_Trigger_workflow_Step1.png
---
width: 1000px
name: 
align: center
---
```
__Objectif :__ Cette étape décrit la structure de dossiers recommandée pour simplifier l'analyse et garantir des résultats cohérents et reproductibles.

__Outil :__ Aucun outil ou programme particulier n'est nécessaire.

``````{list-table}
:header-rows: 1
:widths: 10 25

* - Instructions
  - Structure du répertoire
* - 1. Ouvrez le dossier “AA_Cyclone_Monitoring_Trigger_MAD".
    2. Les données d'entrée se trouvent dans le dossier "fixed_input_data".
    3. Le modèle QGIS se trouve dans le dossier "trigger_model" folder.
    4. Les ressources pour la mise en forme et la création de cartes se trouvent dans:
        - layer_styles – symbologie prédéfinie des couches
        - logos_pictures – logos et éléments visuels
        - map_templates – modèles pour la mise en page finale des cartes
        - example_map_results – exemples de résultats pour s'orienter
        - Sauvegardez vos propres résultats dans le dossier "map_outputs".
    5. Pour lancer le processus, ouvrez le fichier de projet QGIS "AA_Cyclone_Monitoring_Trigger_MAD.qgz" en double-cliquant dessus. Cela lancera le processus d'analyse complet.

  -
    ```{figure} /fig/MAD_trigger_Folder_Structure_MAD_Trigger.png
    ---
    width: 450px
    name: 
    align: center
    ---
    ```
``````


## Étappe 2: Ouvrez le projet dans QGIS et chargez le modèle dans le concepteur de modèles QGIS

```{figure} /fig/MAD_Trigger_workflow_Step2.png
---
width: 1000px
name: 
align: center
---
```

Dans cette étape, nous allons ouvrir notre projet de déclenchement dans QGIS et charger le modèle QGIS qui exécutera automatiquement l'analyse pour nous.

1. Ouvrez le fichier `AA_Cyclone_Monitoring_Trigger_MAD.qgz` en double-cliquant dessus.
2. Le projet QGIS s'ouvrira avec de nombreuses données préchargées. Ces données sont nécessaires pour exécuter le modèle QGIS et créer certaines cartes de résultats.

Les données seront structurées en cinq groupes:

```{figure} /fig/MAD_trigger_QGIS_project_structure.PNG
---
width: 500px
name: 
align: center
---
```

**Groupe 1: Données d'entrée fixes (Fixed_Input_data)**

Ce groupe contient toutes les **données d'entrée fixes** nécessaires au bon fonctionnement du modèle. Ces ensembles de données restent constants et ne changent pas d'un événement à l'autre. La seule donnée supplémentaire nécessaire est la **trajectoire de la tempête** pour l'événement étudié, qui doit être ajoutée **avant** ce groupe de données dans le panneau des couches.

:::{attention}

Assurez-vous toujours d'utiliser la **trajectoire de tempête la plus récente** pour l'événement analysé. Pour ajouter la couche, il suffit de la glisser-déposer dans le panneau Couches, en la plaçant directement au-dessus du groupe **Fixed_Input_data** pour plus de clarté.

Pour une meilleure gestion des données, donnez à la trajectoire de la tempête un nom descriptif, tel que `trajectoire_tempete_nom-événement_année` (par exemple, trajectoire_tempete_freddy_2023). Cette convention de nommage vous aide à organiser votre espace de travail et garantit que les données correctes sont utilisées pendant l'analyse.

:::

**Groupe 2: Résultats du modèle (Model_outputs)**

Ce groupe sert à organiser toutes les **couches de sortie générées par le modèle** après son exécution. Vous pouvez examiner les sorties ici et identifier les couches nécessaires pour des cartes spécifiques. Une fois identifiées, déplacez-les vers le groupe de cartes approprié pour la visualisation et la mise en page.

**Groupe 3: Carte Aperçu de l'impact du cyclone (Map_Cyclone_Impact_Overview)**

Ce groupe comprend toutes les couches nécessaires à la création de la **carte générale de l'impact du cyclone** (illustrée ci-dessous). La trajectoire de la tempête et les limites de la région (Admin1) (`Admin1_Impact_Overview_Map`) sont préchargées pour vous aider à démarrer rapidement.
Assurez-vous que vous travaillez avec la **trajectoire correcte et mise à jour** de la tempête pour l'événement étudié.

```{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
Cette carte sera créée à l'aide des couches du groupe 3.
```

**Groupe 4: Carte d'évaluation de l'impact du cyclone (Map_Cyclone_Impact_Assessment)**

Ce groupe contient toutes les couches nécessaires pour générer des **cartes détaillées d'évaluation d'impact**. Comme pour la carte générale, la trajectoire de la tempête et les limites de la région (Admin1) sont préchargées.
Assurez-vous d'utiliser les données d'événement correctes afin de garantir la cohérence et la précision de l'évaluation. Dans cette section, nous pouvons créer 5 cartes différentes pour différents impacts:
- population exposée
- bâtiments exposés
- établissements scolaires exposés
- établissements de santé exposés
- terres agricoles exposées

Les résultats finaux de la carte ressembleront à ce qui suit.

```{figure} /fig/MAD_Trigger_Impact_Population_Map.png
---
width: 1000px
name: 
align: center
---
Cette carte sera créée à l'aide des couches du groupe 4.
```

<!--EDIT: ADD THE CORRECT PICTURE FOR THIS MAP-->

**Groupe 5: Isochrones de l'entrepôt CRM (CRM_Warehouse_Isochrones)**

Ce groupe comprend les isochrones pour tous les entrepôts, calculées pour des intervalles de temps allant jusqu'à 24 heures. Ces couches sont utiles pour évaluer l'accessibilité des sites dans le cadre de la planification des interventions d'urgence. Ce groupe est utilisé pour créer la carte matrice d'accessibilité des entrepôts CRM. Il est également possible d'ajouter une isochrone spécifique à l'un des entrepôts précédents. Nous y reviendrons plus bas.


----

### Ouvrir le modèle dans QGIS  

Nous allons ouvrir le modèle QGIS :
1. Dans la barre du haut de votre fenêtre QGIS, naviguez vers `Traîtement` -> `Modeleur`. Une nouvelle fenêtre s'ouvrira. Il s'agit du concepteur de modèles.
2. Dans le panneau du haut, cliquez sur `Modèle` -> `Ouvrir le Modèle` et naviguez jusqu'à votre dossier "AA_Cyclone_Monitoring_Trigger_MAD/trigger_model".
3. Sélectionnez "Cyclones_EAP_MAD_Trigger.model3" et cliquez sur `Ouvrir`. Le modèle s'ouvrira et vous verrez des boîtes jaunes, blanches, vertes et grises.

<!--ADD PICTURE
-->

:::{figure} /fig/AA/fr_qgis_3.44_opening_model_builder.png
---
width: 600 px
name: fr_qgis_ouvrir_modeleur
---
Ouvrir le modélisateur graphique dans QGIS 3.44
:::

| Boîte | Signification | Description |
| ----- | --- | --- |
|Jaune| Entrée du modèle | Définition des données d'entrée pour le modèle sur lequel le modèle va fonctionner. |
|Blanc| Algorithmes | Les algorithmes ou outils sont des étapes de géotraitement spécifiques qui effectuent des tâches spécifiques, telles que le découpage, la reprojection ou la création de zones tampons. |
|Vert| Sortie du modèle| Les résultats créés par le modèle (couches de sortie) sont automatiquement ajoutés à votre panneau de couches dans l'interface de votre projet QGIS. |
|Gris| Commentaires| Les boîtes sont utilisées pour expliquer plus en détail les processus spécifiques. |

<!-- Do we need a video here? -->

## Étappe 3: Exécutez le modèle

```{figure} /fig/MAD_Trigger_workflow_Step3.png
---
width: 1000px
name: 
align: center
---
```

__Entrées et sorties du modèle__


1. Un modèle QGIS peut être exécuté en naviguant vers la barre du haut > `Modèle` > `Exécuter le modèle` ou en cliquant sur l'icône ![](/fig/Module_7/qgis_3.44_run_model.png). 


2. Une nouvelle fenêtre s'ouvrira. Vous devrez y définir les entrées et les sorties du modèle. Pour chacune de ces entrées obligatoires, cliquez sur la flèche déroulante et sélectionnez le fichier correspondant.

:::{figure} /fig/AA/fr_qgis_3.44_executer_modele.png
---
width: 600 px
name: fr_qgis_executer_modele
---
Sélectionner les entrées et définir les sorties avant d'exécuter le modèle.
:::

::::{margin}
:::{note}  
Dans la liste déroulante, seules les couches actuellement chargées dans votre projet QGIS seront affichées.
:::
::::

3. Pour exécuter le modèle, sélectionnez les 5 couches d'entrée suivantes:
    1. ADM1 = `mdg_admbnda_adm1_BNGRC_OCHA_20181031`
    2. ADM2 & Risk = `mdg_adm2_risk - mad_adm2_risk`
    3. Cyclone_monitoring_data = `cyclone track of the current event` 
    4. Madagascar_Health_and_Education_Facilities = `Madagascar_Health_and_Education_Facilities`
    5. Master Raster = `MAD_pop_constrained_buildings_landcover`


<!-- Names should be the final ones. They are given after the last model from Elias -->

::::{margin}
:::{attention}
Si vous ne spécifiez pas l'emplacement où sauvegarder les fichiers de sortie, les sorties seront chargées en tant que __couches temporaires__ après l'exécution du modèle et __disparaîtront même après la sauvegarde du fichier de projet__.
:::
::::

4. Plus bas, vous devez spécifier où sauvegarder les sorties. Pour chaque sortie, cliquez sur les trois points ![](/fig/Three_points.png) > `Enregistrer dans un Geopackage...`. Une fenêtre de l'explorateur de fichiers s'ouvrira. Naviguez jusqu'au dossier `.../AA_Cyclone_Monitoring_Trigger_MDG/model_outputs/` et donnez-lui __le nom de la couche de sortie et la date__ (AAAAMMJJ). 
    1. `Exposed_Cyclone_Area_AAAAMMJJ`, par exemple, `Exposed_Cyclone_Area_20250805`
    2. Une des sorties s'appelle `Spreadsheet_Exposed_District` pour laquelle le modèle produira un fichier `.csv`. Pour cette couche, choisissez `Enregistrer vers un fichier...`, naviguez jusqu'au dossier `.../AA_Cyclone_Monitoring_Trigger_MDG/model_outputs/` et donnez-lui le nom `Spreadsheet_Exposed_Districts_AAAAMMJJ`
    3. `Exposed_Education_Facilities_points_AAAAMMJJ`
    4. `Exposed_Health_Facilities_points_AAAAMMJJ`
    5. `Exposed_Regions_YAAAAMMJJ`
    6. `Exposed_Districts_AAAAMMJJ`
    7. `Exposed_Population_AAAAMMJJ`
    8. `Exposed_Buildings_AAAAMMJJ`
    9. `Exposed_Agricultural_Landcover_AAAAMMJJ`
    10. `Exposed_Education_Facilities_AAAAMMJJ`
    11. `Exposed_Health_Facilities_AAAAMMJJ`


5. Une fois que vous avez défini les noms et les emplacements de sauvegarde des couches de sortie, cliquez sur `Exécuter` to execute the model. pour exécuter le modèle. Les couches de résultats de sortie seront automatiquement ajoutées à la fenêtre principale de QGIS une fois le processus terminé. Quand le processus a terminé, vous pouvez fermer la fenêtre `Modeleur`.



6. Vous verrez de nouveaux couches ajoutés à la zone de travail de la carte et au panneau des calques (en bas à gauche). Déplacez les nouveaux calques vers le groupe "Model_Outputs".

:::{figure} /fig/AA/mdg_aa_model_outputs_canvas.png
---
name: mdg_model_output_canvas
width: 700 px
---
:::


<!-- Do we need a video here to show how to run the model? -->

```{dropdown} Vidéo: Modèle d'entrée et de sortie
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/model_input_output.mp4"></video>
```

:::{card}
Résultats
^^^
Nous avons toutes les couches nécessaires pour créer les cartes individuelles. La section suivante explique comment utiliser les couches prédéfinies et calculées pour créer les cartes à l'aide des modèles de carte et des fichiers de style de couche.
:::

# Création des cartes à l'aide des modèles de carte

## Visualisation et mise en forme des résultats du modèle et création de la carte imprimée

<!-- Is a video necessary for this chapter? -->

:::{admonition} Cartes de résultats
:class: note

Nous générerons trois types de cartes différents pour faciliter l'analyse : 
- La carte 1 donnera un aperçu de l'impact du cyclone sur les **districts touchés, la gravité du cyclone et l'emplacement des entrepôts concernés**.
- La carte 2 se concentrera sur l'impact sur les infrastructures et la population. Nous créerons 5 cartes d'impact différentes affichant les informations suivantes:
    - **population exposée**
    - **bâtiments exposés**
    - **sites de santé exposés**
    - **établissements scolaires exposés**
    - **couverture agricole exposée**

De plus, une carte indiquant les **isochrones des entrepôts** pour les 13 entrepôts sera fournie. La carte et le modèle de carte se trouvent dans le dossier **warehouse_isochrone_matrix**.
:::

Nous allons créer les cartes en deux étapes:
Tout d'abord, nous allons utiliser le __[layer styling panel (panneau de style des couches)](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#styling-panel)__ et le __layer style files (fichiers de style des couches) (.qml)__ pour ajuster la visualisation des couches sur le canevas de la carte.

La deuxième étape consiste à utiliser le __[print layout composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)__ pour créer des cartes imprimables avec des tableaux de données supplémentaires.

<!---

```{figure} /fig/MAD_Trigger_workflow_Step4a.png
---
width: 1000px
name: 
align: center
---
```

__Tool:__ [Symbology tab](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_I.html#symbology-for-vector-data)

```{figure} /fig/MAD_Trigger_workflow_Step4b.png
---
width: 1000px
name: 
align: center
---
```


__Tool:__  [Print Layout](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

### Carte 1: Aperçu de l'impact du cyclone: Districts touchés, gravité de l'événement et emplacement des entrepôts

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::

Couches nécessaires pour cette carte:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Admin1_Impact_Overview_Map` déjà chargée et stylisée dans QGIS
- `Exposed_Districts`

__Faites un clic droit sur chacun des couches et sélectionnez `Dupliquer la couche`. Déplacez la copie vers le groupe "Map_Cyclone_Impact_Overview".__ 

Les couches devraient être disposées comme indiqué dans la figure ci-dessous.

```{figure} /fig/MAD_Trigger_layer_order_overview_map.PNG
---
width: 300px
name: 
align: center
---
```

#### Stylisation des couches

1. Faites un clic droit sur la couche exposed_districts -> `Propriétés` -> `Symbologie`
2. Dans le coin inférieur gauche, cliquez sur `Style` -> `Charger le style`
3. Dans la nouvelle fenêtre, cliquez sur les trois points ![](/fig/Three_points.png). Naviguez jusqu'au dossier "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” et sélectionnez le fichier __“exposed_districts_style.qml”__.
4. Cliquez sur `Ouvrir`. Cliquez ensuite sur `Charger le style`
5. De retour dans la fenêtre “Propriétés de la couche” cliquez sur `Appliquer` et `OK`

Répétez ce processus pour les couches de sortie suivantes, ainsi que pour leurs feuilles de style correspondantes:

| Nom de la couche | Style | Remarques
| ----- | --- | --- |
|`Admin1_Impact_Overview_Map`| `adm1_style.qml` | préchargé |
|`CRM_warehouses` | `relevant_warehouses_style.qml` | résultat du modèle |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| résultat du modèle |
|`cyclone_track`| `storm_track_cyclone_style.qml`| préchargé |

6. Le style de la couche `CRM_warehouses` n'est pas encore défini. Cliquez avec le bouton droit sur la couche `CRM_warehouses` > `Propriétés` et naviguez à la section `Symbologie`.
  :::{figure} /fig/AA/fr_mdg_aa_fix_warehouse_icon.png
  ---
  name: fix_warehouse_icon
  width: 550px
  ---
  :::
  * Sélectionnez `Remplissage image raster` puis cliquez sur les trois points ![](/fig/Three_points.png).
  * Dans le dossier du projet, naviguez jusqu'au sous-dossier appelé `logo_pictures`. Vous y trouverez un fichier png appelé "ngo-office". Sélectionnez-le et cliquez sur `Ouvrir`.


<!--EDIT: Add that the picture location for the CRM warehouse icon needs to specified again. It is located in the logos_pictures folder.-->

:::{attention}

Assurez-vous que toutes les couches de sortie sont correctement ajoutées au projet QGIS. Si certaines couches manquent, essayez de relancer le modèle ou vérifiez dans le dossier Model Outputs si les fichiers ont bien été créés.

Pour conserver un espace de travail clair et organisé, regroupez les couches de sortie dans le panneau Couches sous le groupe approprié (par exemple, Map_Cyclone_Impact_Overview). Cela permet de structurer votre projet et facilite la navigation pendant le processus de création de la carte.

:::

#### Création de la mise en page

Pour faciliter la visualisation, nous avons créé ces [modèles de carte](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) afin de présenter les résultats de l'analyse des déclencheurs. Ces modèles servent de base à vos propres visualisations et sont disponibles dans le répertoire suivant: `AA_Cyclone_Monitoring_Trigger_MAD/map_templates`. Vous pouvez personnaliser les modèles en fonction de vos besoins et préférences. Vous trouverez de l'aide [ici](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).


1. Désactivez tous les groupes de couches à l'exception du groupe `Map_Cyclone_Impact_Overview` et de la carte de base `OpenStreetMap`.
2. Ouvrez une nouvelle mise en page en cliquant sur `Projet` -> `Gestionnaire de mise en page`. Une petite fenêtre apparaîtra. Vous pouvez y sélectionner une mise en page existante ou créer une nouvelle mise en page à partir d'un modèle.
3. Nous voulons créer une nouvelle mise en page à partir d'un modèle. Cliquez sur le menu déroulant `Mise en page vide` et sélectionnez `Spécifique`. 
4. Ci-dessous, cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu'au dossier `../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` et sélectionnez le fichier nommé `cyclone_impact_overview_map_template`. Cliquez sur `Ouvrir`, enpuis sur `Créer`. 
5. QGIS vous demandera de nommer la nouvelle mise en page. Donnez-lui un nom tel que "Cyclone_Overview_Map_Freddy_2023". Cliquez sur `OK`. Une nouvelle fenêtre s'ouvrira. Il s'agit du compositeur de mise en page. Il devrait ressembler à la figure ci-dessous.

:::{figure} /fig/AA/overview_map_template.png
---
name: overview_map_template
width: 700 px
---
Le compositeur de mise en page après l'ouverture du fichier modèle.
:::

La mise en page chargera automatiquement le canevas de la carte. Cependant, pour finaliser le rapport, nous devons ajuster et mettre à jour certains éléments de la mise en page d'impression. Par exemple, sur le côté droit de la carte, le tableau des attributs ne s'affiche pas correctement, la légende semble incorrecte et les logos du CRM et de HeiGIT s'affichent sous forme de croix rouges.

6. **Mettre à jour le titre de la carte** 
   - Cliquez sur l'élément de texte du titre en haut de la carte.
   - Dans le panneau `Propriétés de l'objet` modifiez le texte **Étiquette principale** pour qu'il corresponde à votre événement, par exemple `Cyclone Harald – 2025`.
   - Ajustez la taille de la font ou l'alignement si nécessaire.



7. **Mettre à jour le tableau des attributs situé à droite de la carte**
:::{figure} /fig/AA/mdg_aa_map_1_update_attribute_table.png
---
name: mdg_aa_map_1_update_attribute_table
width: 600 px
---
:::
   - Sur le côté droit, il y a un tableau d'attributs qui ne s'est pas entièrement chargé. Nous voulons mettre à jour le tableau d'attributs pour afficher les districts exposés.
   - Dans le panneau `Propriétés de l'élément`, sélectionne la couche `Exposed_Districts` et cliquez sur **Actualiser les données du tableau**
   - Cliquez sur on `Attributs...`
   - Dans la section **Colonnes**:
     - Cliquez sur `Effacer`
     - ➕ Ajoutez les colonnes: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE`
   - Dans la section **Trier**:
     - ➕ Ajoutez `ADM1_EN` et définissez l'ordre de tri sur `Ascendant`
   - Cliquez sur **OK** pour appliquer


```{note}
💡 Si trop de districts sont concernés, le tableau des attributs risque de ne pas être adapté à la page. Réduisez la taille de la fonte dans les propriétés des éléments du tableau afin que tout soit visible, mais sachez que cela peut réduire la lisibilité.
```

8. **Ajuster la légende**
    * Sélectionnez l'élément de légende, naviguez jusqu'à la section `Propriétés de l'élément` et faites défiler vers le bas jusqu'à ce que vous voyiez `Éléments de la légende`. Si ce n'est pas le cas, vérifiez si vous devez ouvrir le menu déroulant. Assurez-vous que la case `Mise à jout auto` n'est **pas cochée**.
    * Supprimez tous les éléments de la légende en cliquant sur chaque élément, puis sur l'icône rouge moins
        * Dans la fenêtre contextuelle, cochez **Ne montrer que les entités à l'intérieur de la carte liée** pour vous aider à trouver les corrects.
        * Pour renommer un élément de la légende, **double-cliquez** sur le nom de la couche dans la liste des éléments de la légende et entrez le nouveau nom
    * ➕ Ajoutez les couches suivantes en cliquant sur le signe plus vert:
        * `Admin1_Impact_Overview_Map`
        * `exposed_districts`
        * `Cyclone Track`
        * `Exposed_Cyclone_Area`
        * `CRM_warehouses`  
        * `OpenStreetMap`
      * Maintenant, nous allons renommer les couches dans la légende. Dans les __propriétés de l'élément__, sous la liste des couches de la légende, se trouve un bouton ![](/fig/AA/mdg_aa_edit_legend.png) `Editer les propriétés de l'élément sélectionné`. En cliquant dessus, vous pouvez modifier le nom de l'icône dans la légende. Renommez les couches comme suit:
        * `Admin1_Impact_Overview_Map` → renommer en  
        ```md
        Régions
        ```
        * `exposed_districts` → renommer en  
        ```md
        Districts exposés
        ```
        * `Cyclone Track` → renommer en
        ```md
        Trajectoire prévue du cyclone
        ```
        * `Exposed_Cyclone_Area` → renommer en
        ```md
        Zone exposée aux cyclones
        ```
        * `relevant_warehouses` → renommer en
        ```md
        Entrepôts concernés
        ```
        * `Background Map: OpenStreetMap` → renommer en
        ```md
        Carte de fond:
        OpenStreetMap
        ```

9. Ajustez les icônes en cliquant sur le bouton <Image> dans la liste des éléments ou sur la croix rouge dans le modèle de carte.
  * Dans les propriétés de l'élément, corrigez le chemin d'accès au logo CRM en cliquant sur les trois points ![](/fig/Three_points.png) et naviguez jusqu'à  `\aa_madagascar\AA_Cyclone_Monitoring_Trigger_MAD\logos_pictures` puis sélectionnez le fichier du logo CRM.
  *  Répétez le processus pour la deuxième image manquante. Cette fois-ci, sélectionnez le logo HeiGIT.


10. Sous les logos, modifiez les informations dans la zone de texte en sélectionnant celle-ci et en naviguant vers les propriétés de l'élément.

11. Enfin, verrouillons les calques et les styles de calque afin que les modifications apportées dans la fenêtre principale de QGIS n'affectent pas notre mise en page d'impression:
  * Dans la liste des éléments, sélectionnez __Carte 1__.
  * Dans les propriétés de l'élément, cochez les cases __verrouiller les couches__ et __verrouiller le style des couches__. Cela empêchera la carte de se mettre automatiquement à jour lorsque nous apporterons des modifications à la zone de travail de la carte.

```{figure} /fig/AA/mdg_aa_lock_layers.png
---
name: mdg_aa_lock_layers
width: 600 px
---
```

<!-- Maybe add a video on how the Print Layout is created 

```{dropdown} Video: Making print map
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_Trigger_print_map.mp4"></video>
```

-->

```{Attention}
Liste de contrôle pour la version finale de la carte:
- Informations cartographiques: vérifiez et mettez à jour tous les éléments textuels si nécessaire.
- Légende: supprimez les éléments inutiles et renommez les couches avec des descriptions claires et significatives.
- Districts exposés: n'incluez que les districts réellement touchés dans votre "Liste des districts exposés". Mettez-les à jour en fonction de l'événement.
```

::::{dropdown} Une fois la couche est stylisé, votre résultat final devrait ressembler à ceci.
Vous pouvez voir maintenant les districts exposés et l'emplacement des entrepôts concernés clairement indiqués sur la carte. De plus, la trajectoire originale de la tempête, utilisée comme données d'entrée, est mise en évidence, ainsi que la zone d'impact tamponnée, qui sert de référence pour identifier les districts exposés.

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::
::::


#### Exporter la carte 

<!--Exporting the map should be done after each layout. If the maps are not locked, it will break the layouts and the work will have to be repeated-->


<!---
```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order to print it as a pdf or format of your choice.


__Tool:__ [Print Layout Composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

Une fois la conception de votre carte terminée, vous pouvez l'exporter au format PDF ou image dans différents formats.

__Exporter en tant qu'image__  

1. Dans la mise en page, cliquez sur `Mise en page` -> `Exporter en tant qu'image`.
2. Choisissez le dossier __map_outputs__. Donnez au fichier le nom de l'événement, par exemple **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.  
3. Cliquez sur `Sauvegarder`.  
4. La fenêtre `Options d'exportation d'image` apparaîtra.  
5. Cliquez sur `Sauvegarder`.
L'image se trouve maintenant dans le dossier de résultats.


__Exporter au format PDF__

1. Dans la mise en page d'impression, cliquez sur `Mise en page` -> `Exporter au format PDF`
2. Sélectionnez le dossier __map_outputs__. Donnez au fichier le nom de l'événement, par exemple **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.  
3. Cliquez sur `Sauvegarder`.
4. La fenêtre `Options d'exportation PDF` s'affiche. Pour obtenir les meilleurs résultats, sélectionnez la compression d'image `sans perte`.
5. Cliquez sur `Sauvegarder`.
L'image se trouve maintenant dans le dossier de résultats.

### Carte 2: Évaluation de l'impact: population exposée et infrastructures critiques

Couches nécessaires pour cette carte:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Exposed_Population`
- `Admin1_Impact_Assessment_Map` déjà chargé et stylisé dans QGIS

Cliquez avec le bouton droit sur chaque couche > `Dupliquer la couche` et déplacez les copies vers le groupe "Map_Cyclone_Impact_Assessment"

```{figure} /fig/MAD_Trigger_layer_order_impact_map.PNG
---
width: 300px
name: 
align: center
---
```

<!--Remove the comment as duplicating and loading the style ensures that previous map layouts are not broken. also add that you can fix layer styles and layers in the map items-->


#### Carte 2: Stylisation des couches

1. Désactivez toutes les couches sauf le groupe "Map_Cyclone_Impact_Assessment" et la carte de base OpenStreetMap.
2. Cliquez avec le bouton droit sur la couche "exposed_population - copy" (population_exposée copie) -> `Propriétés` -> `Symbologie`
3. Dans le coin inférieur gauche, cliquez sur `Style` -> `Charger le Style`
4. Dans la nouvelle fenêtre, cliquez sur les trois points ![](/fig/Three_points.png). Naviguez jusqu'au dossier "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” et sélectionnez le fichier __“exposed_population_style.qml”__.
5. Cliquez sur `Ouvrir`. Cliquez ensuite sur `Charger le style`
6. De retour dans la fenêtre “Propriétés de la couche” cliquez sur `Appliquer` et `OK`

Répétez ce processus pour les couches de sortie suivantes, ainsi que pour leurs feuilles de style correspondantes:

| Nom de la couche | Style | Remarques
| ----- | --- | --- |
|`Admin1_Impact_Assessment_Map`| `adm1_style.qml` | préchargé |
|`CRM_warehouses` | `relevant_warehouses_style.qml` | résultat du modèle |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| résultat du modèle |
|`cyclone_track`| `storm_track_cyclone_style.qml`| chargé par l'utilisateur |

:::{attention}

Assurez-vous que toutes les couches de résultats sont correctement ajoutées au projet QGIS. Si certaines couches manquent, essayez de relancer le modèle ou vérifiez dans le dossier Model Outputs si les fichiers ont bien été créés.

Pour conserver un espace de travail clair et organisé, regroupez les couches de sortie dans le panneau Couches sous le groupe approprié (par exemple, Map_Cyclone_Impact_Overview). Cela permet de structurer votre projet et facilite la navigation pendant le processus de création de la carte.

:::

::::{admonition} Autres cartes d'évaluation d'impact
:class: hint

La documentation couvre la carte d'évaluation de l'impact sur la population exposée. Cependant, le modèle estime également les bâtiments exposés, la couverture terrestre et les établissements de santé et d'enseignement. Ces variables peuvent également être affichées sur la carte à l'aide des fichiers de style suivants. Pour que la carte reste facilement compréhensible, n'utilisez qu'une seule des variables.


| Nom de la couche | Style | Remarques
| ----- | --- | --- |
|`exposed_population`|`exposed_population_style.qml`|résultat du modèle|
|`exposed_building`|`exposed_building_style.qml`|résultat du modèle|
|`exposed_health_facilities`| `exposed_health_facilities_style.qml` | résultat du modèle |
|`exposed_education_facilities`| `exposed_education_facilities_style.qml` | résultat du modèle |
|`exposed_agricultural_landcover`| `exposed_agriculture_landcover_style.qml` | résultat du modèle |
|`exposed_health_facilities_points`| `points_exposed_health_facilities_style.qml` | résultat du modèle |
|`exposed_education_facilities_points`| `points_exposed_education_facilities_style.qml` | résultat du modèle |
|`relevant_warehouses` | `relevant_warehouses_style.qml` | résultat du modèle |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| résultat du modèle |
|`cyclone_track`| `storm_track_cyclone_style.qml`| chargé par l'utilisateur |
<!--Move this somewhere else where it is easier to understand OR add pictures to illustrate the different maps?-->
::::

#### Carte 2: Création de la mise en page

```{tip}
Le même processus s'applique aux cinq variables d'impact: population, bâtiments, établissements scolaires, sites de santé et couverture agricole. L'exemple suivant illustre le processus de création de la carte d'impact sur la population. Les autres cartes peuvent être générées en suivant les mêmes étapes.
```

1. Ouvrez une nouvelle mise en page en cliquant sur `Projet` -> `Gestionnaire de mise en page`. Une petite fenêtre apparaîtra. Vous pouvez y sélectionner une mise en page existante ou créer une nouvelle mise en page à partir d'un modèle.
2. Nous voulons créer une nouvelle mise en page à partir d'un modèle. Cliquez sur le menu déroulant `Mise en page vide` et sélectionnez `Spécifique`. 
3. Ci-dessous, cliquez sur les trois points ![](/fig/Three_points.png) et naviguez jusqu'au dossier`../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` et sélectionnez le fichier nommé `cyclone_impact_population_map_template`. Cliquez sur `Ouvrir`, enpuis sur `Créer`. 
4.  QGIS vous demandera de nommer la nouvelle mise en page. Donnez-lui un nom tel que "Cyclone_Overview_Map_Freddy_2023". Cliquez sur `OK`. Une nouvelle fenêtre s'ouvrira. Il s'agit du compositeur de mise en page. Il devrait ressembler à la figure ci-dessous.

:::{figure} /fig/AA/mdg_aa_pop_impact_template.png
---
name: mdg_aa_pop_impact_template
width: 600 px
---
:::

1. **Mettre à jour le titre de la carte** 
   - Cliquez sur l'élément de texte du titre en haut de la carte.
   - Dans le panneau `Propriétés de l'objet` modifiez le texte **Étiquette principale** pour qu'il corresponde à votre événement, par exemple `Cyclone Harald – 2025`.
   - Ajustez la taille de la police ou l'alignement si nécessaire.
2. **Mettre à jour le tableau des attributs situé à droite de la carte**
   Pour mettre à jour le tableau des attributs affichant les districts exposés:
   - Dans le panneau `Propriétés de l'élément`, sélectionne la couche `exposed_population`**Ou toute autre couche avec laquelle vous travaillez**, puis cliquez sur **Actualiser les données du tableau**.
   - Cliquez sur on `Attributs...`
   - Dans la section **Colonnes**:
     - Cliquez sur `Effacer`
     - ➕ Ajoutez les colonnes: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE` et `exposed_population` **Ou toute autre couche avec laquelle vous travaillez**
   - Dans la section **Trier**:
     - ➕ Ajoutez `ADM1_EN` et définissez l'ordre de tri sur `Ascendant`
   - Cliquez sur **OK** pour appliquer

```{note}
💡 Si trop de districts sont concernés, le tableau des attributs risque de ne pas être adapté à la page. Réduisez la taille de la fonte dans les propriétés des éléments du tableau afin que tout soit visible, mais sachez que cela peut réduire la lisibilité.
```

8. Ajustez la légende en cliquant dessus dans la mise en page de la carte, puis consultez la section « Propriétés de l'élément » et faites défiler vers le bas jusqu'à ce que vous voyiez le champ « Éléments de la légende ». S'il n'apparaît pas, vérifiez si vous devez ouvrir le menu déroulant. Assurez-vous que l'option `Mise à jout auto` n'est **pas cochée**.
    * Supprimez tous les éléments de la légende en cliquant sur chaque élément, puis sur l'icône rouge moins
        * Dans la fenêtre contextuelle, cochez **Ne montrer que les entités à l'intérieur de la carte liée** pour vous aider à trouver les corrects.
        * 💡 Pour renommer un élément de la légende, **double-cliquez** sur le nom de la couche dans la liste des éléments de la légende et entrez le nouveau nom
    * ➕ Ajoutez les couches suivantes en cliquant sur le signe plus vert:
   - Veillez à ce que toutes les entrées de légende utilisent des **étiquettes claires et significatives**.
::::{tab-set}

:::{tab-item} Population exposée
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_population` → renommer en  
```md
Population exposée
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue du cyclone
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone exposée aux cyclones
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

:::{tab-item} Bâtiments exposés
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_building` → renommer en  
```md
Bâtiments exposés
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue du cyclone
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone exposée aux cyclones
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

:::{tab-item} Établissements de santé exposés
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_health_facilities` → renommer en  
```md
Établissements de santé exposés
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue du cyclone
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone exposée aux cyclones
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

:::{tab-item} Établissements scolaires exposés
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_education_facilities` → renommer en  
```md
Établissements scolaires exposés
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue du cyclone
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone exposée aux cyclones
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

:::{tab-item} Agriculture exposée en hectares
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_agricultural_landcover` → renommer en  
```md
Agriculture exposée en hectares
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue des cyclones
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone cyclonique exposée
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

:::{tab-item} Points des établissements de santé exposés
* `Admin1_Impact_Overview_Map` → renommer en  
```md
Régions
```
* `exposed_health_facilities_points` → renommer en  
```md
Points des établissements de santé exposés
```
* `Cyclone Track` → renommer en  
```md
Trajectoire prévue du cyclone
```
* `Exposed_Cyclone_Area` → renommer en  
```md
Zone exposée aux cyclones
```
* `relevant_warehouses` → renommer en  
```md
Entrepôts concernés
```
* `Carte de fond : OpenStreetMap` → renommer en  
```md
Carte de fond :
OpenStreetMap
```
:::

::::




```{dropdown} Votre résultat final devrait ressembler à ceci après avoir stylisé la couche.
La carte affiche maintenant clairement la population exposée dans les districts touchés, ainsi que l'emplacement des entrepôts concernés. La trajectoire originale de la tempête, utilisée comme donnée d'entrée, est mise en évidence, tout comme la zone d'impact tamponnée, qui sert de proxy pour identifier les districts exposés.

Sur le côté droit de la carte, une liste affiche tous les districts exposés, y compris des données sur la population totale et la population exposée. Les districts (Admin 2) sont organisés sous leurs régions correspondantes (Admin 1).

```{figure} /fig/MAD_Trigger_Impact_Population_Map.png
---
width: 1000px
name: 
align: center
---
```

#### Exporter la carte

<!--Exporting the map should be done after each layout. If the maps are not locked, it will break the layouts and the work will have to be repeated

```{figure} /fig/MAD_Trigger_workflow_Step5.png
---
width: 1000px
name: 
align: center
---
```

__Purpose:__ Export the designed and finalized map layout in order to print it as a pdf or format of your choice.


__Tool:__ [Print Layout Composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)

-->

Une fois la conception de votre carte terminée, vous pouvez l'exporter au format PDF ou image dans différents formats.

__Exporter en tant qu'image__  

1. Dans la mise en page, cliquez sur `Mise en page` -> `Exporter en tant qu'image`.
2. Choisissez le dossier __map_outputs__. Donnez au fichier le nom de l'événement, par exemple **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.  
3. Cliquez sur `Sauvegarder`.  
4. La fenêtre `Options d'exportation d'image` apparaîtra.  
5. Cliquez sur `Sauvegarder`.
L'image se trouve maintenant dans le dossier de résultats.


__Exporter au format PDF__

1. Dans la mise en page d'impression, cliquez sur `Mise en page` -> `Exporter au format PDF`
2. Sélectionnez le dossier __map_outputs__. Donnez au fichier le nom de l'événement, par exemple **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.  
3. Cliquez sur `Sauvegarder`.
4. La fenêtre `Options d'exportation PDF` s'affiche. Pour obtenir les meilleurs résultats, sélectionnez la compression d'image `sans perte`.
5. Cliquez sur `Sauvegarder`.
L'image se trouve maintenant dans le dossier de résultats.

<!-- Maybe add a video. Might not be necessary

```{dropdown} Video: Export image and PDF
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/SRCS_trigger_export_image_pdf.mp4"></video>
```
-->

```{figure} /fig/MAD_Trigger_Impact_Buildings_Map.png
---
width: 1000px
name: Impact of Cyclone Event Freddy 2023
align: center
---
```

## Utilisation des isochrones d'entrepôt

Le projet comprend des isochrones pour chaque entrepôt. Les isochrones d'entrepôt correspondent à un entrepôt et sont identifiables par le nom de leur emplacement. Si vous souhaitez ajouter une isochrone à l'une des cartes Il est possible d'ajouter des isochrones individuelles aux modèles de carte en dupliquant simplement la couche d'isochrones et en la déplaçant vers le groupe de cartes souhaité.

<!--INSERT EXAMPLE PICTURE-->

# Analyse historique des impacts des cyclones

Pour exécuter le processus de déclenchement complet à l'aide des données historiques sur la trajectoire des cyclones, vous pouvez évaluer les impacts des événements passés et obtenir des informations sur ce qui s'est produit dans des scénarios similaires. Les données sur la trajectoire des tempêtes sont disponibles auprès de l'**International Best Track Archive for Climate Stewardship (IBTrACS)**. Les instructions pour accéder à ces données sont fournies dans la section suivante.

## Téléchargement des données historiques sur les trajectoires des tempêtes

Les données **International Best Track Archive for Climate Stewardship (IBTrACS)** v04r01 sont mises à jour trois fois par semaine (généralement le dimanche, le mardi et le jeudi) et peuvent être mises à jour plus fréquemment pour répondre à des besoins et des cas d'utilisation spécifiques. Les dernières mises à jour dans le format de fichier approprié sont disponibles sur leur [site web](https://www.ncei.noaa.gov/products/international-best-track-archive):

1. Recherchez la section `Access Methods` et cliquez sur `Shapefiles`. Le site web suivant s'ouvre alors: [site web](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/shapefile/), que vous pouvez également voir dans l'image ci-dessous.
2. Comme nous n'avons pas besoin des données sur les trajectoires des tempêtes pour le monde entier ni de l'archive complète, nous ne téléchargerons qu'un sous-ensemble significatif. Recherchez le fichier nommé `IBTrACS.ACTIVE.list.v04r01.lines.zip` et cliquez dessus. Le téléchargement devrait démarrer automatiquement.
3. Décompressez le fichier et ouvrez-le dans QGIS.
4. Ouvrez la table d'attributs et supprimez toutes les trajectoires de tempêtes qui ne sont pas pertinentes pour cette analyse. Enregistrez le fichier de trajectoires de tempêtes mis à jour.

:::{note}

Le sous-ensemble de trajectoires de tempêtes `IBTrACS.ACTIVE.list.v04r01.lines.zip` contient toutes les **tempêtes actives au cours des 7 derniers jours**. Si vous avez besoin de données plus complètes, il est conseillé de télécharger un sous-ensemble par bassin. Pour Madagascar, la région la plus pertinente est **SI – South Indian**, , qui comprend notre zone d'intérêt. Cet ensemble de données peut être téléchargé à partir du même site web sous le nom `IBTrACS.SI.list.v04r01.lines.zip`. 

:::


```{figure} /fig/MAD_Trigger_stromtrack_download.PNG
---
width: 1000px
name: MAD_Trigger_stromtrack_download
align: center
---
```