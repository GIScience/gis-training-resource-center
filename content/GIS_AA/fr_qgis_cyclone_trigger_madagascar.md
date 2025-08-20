# Workflow de déclenchement en QGIS pour Madagascar

<!-- Maybe have a final look over introduction and all the official stuff which should be included in the documentation -->

Le workflow QGIS présenté dans cet article a été développé dans le cadre du projet "Anticipatory-Action" (AA) (action anticipative) de la Croix-Rouge malgache (CRM), de la Croix-Rouge allemande (GRC) et de l'institut de Heidelberg pour les technologies de géoinformation (HeiGIT).

Le workflow est presque entièrement automatisé grâce à un modèle QGIS et ne nécessite aucune intervention manuelle. Le chapitre --Automated Trigger Workflow--- décrit le processus et l'application pratique. <!-- what chapter?? Where is it?--> 
Chaque étape inclut dans le modèle est expliquée en détail afin de permettre une compréhension complète du workflow et de la manière dont l'analyse a été réalisée.

## Contexte

La définition de déclencheurs est l'un des piliers du système de financement basé sur les prévisions (anglais: Forecast-based financing (FbF)). Pour qu'une Société Nationale puisse bénéficier d'un financement automatique pour ses actions précoces, son protocole d'action précoce doit définir clairement où et quand les fonds seront alloués et l'aide fournie. Dans le cadre de l'AA, cela est décidé en fonction de valeurs seuils spécifiques, appelées « déclencheurs », basées sur les prévisions météorologiques et climatiques, qui sont définies pour chaque région (voir [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/06-develop-a-trigger-system/)).

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

```{dropdown} Video: Input and output Model
<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/model_input_output.mp4"></video>
```

:::{card}
Résultats
^^^
Nous avons toutes les couches nécessaires pour créer les cartes individuelles. La section suivante explique comment utiliser les couches prédéfinies et calculées pour créer les cartes à l'aide des modèles de carte et des fichiers de style de couche.
:::

# Creating the map reports using the map templates

## Visualization and Styling of the Model Outputs and creating the Print Map

<!-- Is a video necessary for this chapter? -->

:::{admonition} Output maps
:class: note

We will generate three different types of output maps to support the analysis:
- Map 1 will provide an cyclone impact overview of the **affected districts, the extent of the cyclone event, and the locations of relevant warehouses**.
- Map 2 will focus on the impact to infrastructure and population. We will create 5 different impact maps displaying the following information:
    - **exposed population**
    - **exposed buildings**
    - **exposed health sites**
    - **exposed education facilities**
    - **exposed agricultural landcover**

Additionally, a map showing the **warehouse isochrones** for all 13 warehouses will be provided. The map and the map template can be found in the **warehouse_isochrone_matrix** folder.
:::

We will create the maps in two steps:
First, we will use the __[layer styling panel](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_styling_vector_data.html#styling-panel)__ and the __layer style files (.qml)__ to adjust the visualisation of the layers on the map canvas.

In a second step, we will use the __[print layout composer](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html?highlight=print+layout#print-layout)__ to create printable maps with additional datatables. 

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

### Map 1: Cyclone Impact Overview: Affected Districts, Event Extent, and Warehouse Locations

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::

Layers needed for this map:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Admin1_Impact_Overview_Map` already loaded and styled in QGIS 
- `Exposed_Districts`

__Right-click on each of the layers and select `Duplicate this layer`. Move the copy to the group "Map_Cyclone_Impact_Overview".__ 

The layers should be arranged as shown in the figure below.

```{figure} /fig/MAD_Trigger_layer_order_overview_map.PNG
---
width: 300px
name: 
align: center
---
```

#### Styling of the layers

1. Right click on the exposed_districts layer -> `Properties` -> `Symbology`
2. In the down left corner click on `Style` -> `Load Style`
3. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” folder and select the file __“exposed_districts_style.qml”__.
4. Click `Open`. Then click on `Load Style`
5. Back in the “Layer Properties” window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | Comment
| ----- | --- | --- |
|`Admin1_Impact_Overview_Map`| `adm1_style.qml` | pre-loaded |
|`CRM_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| pre-loaded |

6. The styling for the layer `CRM_warehouses` is not fixed yet. Right-click on the layer `CRM_warehouses` > `Properties` and navigate to the symbology tab.
  :::{figure} /fig/AA/mdg_aa_fix_warehouse_icon.png
  ---
  name: fix_warehouse_icon
  width: 550px
  ---
  :::
  * Select `Raster Image Marker` and then click on the three points ![](/fig/Three_points.png).
  * In the project folder, navigate to the subfolder called `logo_pictures`. Here you will find a png-file called "ngo-office". Select it and click `Open`.


<!--EDIT: Add that the picture location for the CRM warehouse icon needs to specified again. It is located in the logos_pictures folder.-->

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

#### Making the Print Layout

For easier visualization, we have created these [map templates](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#map-templates) for presenting the results of the trigger analysis. These templates serve as a base for your own visualizations and are available in the following directory: `AA_Cyclone_Monitoring_Trigger_MAD/map_templates`. You can customize the templates to suit your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Module_4/en_qgis_map_design_2.html#print-layout).


1. Deactivate all Layer Groups except the group `Map_Cyclone_Impact_Overview` and the `OpenStreetMap` basemap.
2. Open a new print layout by clicking on `Project` -> `Layout Manager`. A small new window will appear. Here you can select an existing layout or create a new layout from a template. 
3. We want to create a new layout from a template. Click on the `Empty Layout` dropdown menu and select `Specific`. 
4. Below, click on the three dots ![](/fig/Three_points.png) and navigate to the folder `../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` and select the file with the name `cyclone_impact_overview_map_template`. Click `Open`, then `Create`. 
5. QGIS will ask you to name the new layout. Give it a name such as "Cyclone_Overview_Map_Freddy_2023". Click `OK`. A new window will open. This is the print layout composer. It should look similar to the figure below.

:::{figure} /fig/AA/overview_map_template.png
---
name: overview_map_template
width: 700 px
---
The print layout composer after opening the template file.
:::

The print layout will automatically load the map canvas. However, to finish the report, we need to adjust and update some of the elements on the print layout. For example, on the right side of the map, the attribute table is not displayed correctly, the legend seems to be wrong, and the logos of the CRM and HeiGIT are displayed as red crosses.

6. **Update the Map Title**  
   - Click on the title text element at the top of the map.
   - In the `Item Properties` panel, edit the **Main Label** text to match your event, e.g. `Cyclone Harald – 2025`.
   - Adjust font size or alignment as needed.



7. **Update the Attribute Table on the Right-Hand Side of the Map**  
:::{figure} /fig/AA/mdg_aa_map_1_update_attribute_table.png
---
name: mdg_aa_map_1_update_attribute_table
width: 600 px
---
:::
   - On the right side, there is a attribute table that did not fully load. We want to update the attribute table to display the exposed districts.
   - In the `Item Properties` panel, select the `Exposed_Districts` layer and click **Refresh Table Data**
   - Click on `Attributes...`
   - In the **Columns** section:
     - Click `Clear`
     - ➕ Add the columns: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE`
   - In the **Sorting** section:
     - ➕ Add `ADM1_EN` and set the sort order to `Ascending`
   - Click **OK** to apply


```{note}
💡 If too many districts are affected, the attribute table might not fit the page. Reduce the font size in the table’s item properties to make everything visible — but be aware that this may reduce readability.
```

8. **Adjust the Legend**
    * Select the legend item, navigate to the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend by clicking on each item and then the red minus icon
        * In the pop-up, check **Only show visible layers** to help you find the correct ones
        * To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name  
    * ➕ Add the following layers by clicking the green plus:
        * `Admin1_Impact_Overview_Map`
        * `exposed_districts`
        * `Cyclone Track`
        * `Exposed_Cyclone_Area`
        * `CRM_warehouses`  
        * `OpenStreetMap`
      * Now, let's rename the layers in the legend. In the __Item properties__, below the list of the legend layers, there is a ![](/fig/AA/mdg_aa_edit_legend.png) `Edit selected item properties`-button. By clicking on it, you can edit the label of the icon in the legend. Rename the layers as follows:
        * `Admin1_Impact_Overview_Map` → rename to  
        ```md
        Regions
        ```
        * `exposed_districts` → rename to  
        ```md
        Exposed Districts
        ```
        * `Cyclone Track` → rename to  
        ```md
        Projected Cyclone Track
        ```
        * `Exposed_Cyclone_Area` → rename to  
        ```md
        Exposed Cyclone Area
        ```
        * `relevant_warehouses` → rename to  
        ```md
        Relevant Warehouses
        ```
        * `Background Map: OpenStreetMap` → rename to  
        ```md
        Background Map:
        OpenStreetMap
        ```

9. Adjust the icons by clicking on the <Picture> field in the items list or on the red cross in the map template. 
  * In the Item Properties, correct the path to the CRM logo by clicking on the three dots ![](/fig/Three_points.png) and navigate to `\aa_madagascar\AA_Cyclone_Monitoring_Trigger_MAD\logos_pictures` and selecting the CRM logo file.
  * Repeat the process for the second missing image. This time, select the HeiGIT Logo


10. Below the logos, adjust the information in the text box by selecting the text box and navigating to the Item properties.

11. Finally, let's lock the layers and layer styles so that changes in the main QGIS window do not affect our print layout:
  * In the item list, select __Map 1__.
  * In the item properties, check the boxes for __lock layers__ and __lock styles for layers__. This will prevent the map to automatically when we make changes to the map canvas

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
Checklist for final map output:
- Map Information: Review and update all text elements as needed.
- Legend: Remove unnecessary items and rename layers with clear, meaningful descriptions.
- Exposed Districts: Include only districts that are actually impacted in your "List of Exposed Districts". Update them according to the event.
```

::::{dropdown} Your final output should look like this after styling the layer
You will now see the exposed districts and the locations of relevant warehouses clearly displayed on the map. Additionally, the original storm track line — used as input data — is highlighted, along with the buffered impact area, which serves as a proxy for identifying exposed districts.

:::{figure} /fig/MAD_Trigger_Impact_Overview_Map.png
---
width: 1000px
name: 
align: center
---
:::
::::


#### Exporting the Map 

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

When you have finished the design of your map, you can export it as pdf or image file in different data formats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. 
3. Click on `Save`
4. The window `Image Export Options` will appear. Click `Save`.
Now the image can be found in the result folder.


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**.
3. Click on `Save`.
4. The window `PDF Export Options` will appear. For the best results, select the `lossless` image compression.
5. Click `Save`.
Now the image can be found in the result folder.

### Map 2: Impact Assessment: Exposed Population and Critical Infrastructure

Layers needed for this map:
- `CRM_Warehouses`
- `cyclone_track`
- `Exposed_Cyclone_Area`
- `Exposed_Population`
- `Admin1_Impact_Assessment_Map` already loaded and style in QGIS

Right click on each layer > `Duplicate this layer` and move the copies to the group "Map_Cyclone_Impact_Assessment"

```{figure} /fig/MAD_Trigger_layer_order_impact_map.PNG
---
width: 300px
name: 
align: center
---
```

<!--Remove the comment as duplicating and loading the style ensures that previous map layouts are not broken. also add that you can fix layer styles and layers in the map items-->


#### Map 2: Styling of the layers

1. Deactivate all the layers except gor the group "Map_Cyclone_Impact_Assessment" and the OpenStreetMap Basemap.
2. Right click on the "exposed_population - copy" layer -> `Properties` -> `Symbology`
3. In the down left corner click on `Style` -> `Load Style`
4. In the new window click on the three points ![](/fig/Three_points.png). Navigate to the "AA_Cyclone_Monitoring_Trigger_MAD/layer_styles” folder and select the file __“exposed_population_style.qml”__ style layer.
5. Click `Open`. Then click on `Load Style`
6. Back in the “Layer Properties” window click `Apply` and `OK`

Repeat this process for the following output layers, along with their corresponding style sheets:

| Layer name | Style | Comment
| ----- | --- | --- |
|`Admin1_Impact_Assessment_Map`| `adm1_style.qml` | pre-loaded |
|`CRM_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| loaded by user |

:::{attention}

Ensure that all relevant output layers are properly added to the QGIS project. If any layers are missing, try re-running the model or check your Model Outputs folder to see if the files were created successfully.

To maintain a clear and organized workspace, group the output layers in the Layers panel under the appropriate group (e.g., Map_Cyclone_Impact_Overview). This helps keep your project structured and makes navigation easier during the map creation process.

:::

::::{admonition} Other Impact Assessment Maps
:class: hint

The documentation covers the exposed population impact assessment map. However, the model also estimates the exposed buildings, landcover, and health and education facilities. These variables can also be displayed on the map using the following style files. To keep the map easily understandable, use only one of the 


| Layer name | Style | Comment
| ----- | --- | --- |
|`exposed_population`|`exposed_population_style.qml`|model output|
|`exposed_building`|`exposed_building_style.qml`|model output|
|`exposed_health_facilities`| `exposed_health_facilities_style.qml` | model output |
|`exposed_education_facilities`| `exposed_education_facilities_style.qml` | model output |
|`exposed_agricultural_landcover`| `exposed_agriculture_landcover_style.qml` | model output |
|`exposed_health_facilities_points`| `points_exposed_health_facilities_style.qml` | model output |
|`exposed_education_facilities_points`| `points_exposed_education_facilities_style.qml` | model output |
|`relevant_warehouses` | `relevant_warehouses_style.qml` | model output |
|`exposed_cyclone_area`|`exposed_cyclone_area_style.qml`| model output |
|`cyclone_track`| `storm_track_cyclone_style.qml`| loaded by user |
<!--Move this somewhere else where it is easier to understand OR add pictures to illustrate the different maps?-->
::::

#### Map 2: Making the Print Layout

```{tip}
The same workflow applies to all five impact variables: population, buildings, education facilities, health sites, and agricultural landcover. The following example demonstrates the process for creating the population impact map. The remaining maps can be generated by following the same steps.
```


1. Open a new print layout by clicking on `Project` -> `Layout Manager`. A small new window will appear. Here you can select an existing layout or create a new layout from a template. 
2. We want to create a new layout from a template. Click on the `Empty Layout` dropdown menu and select `Specific`. 
3. Below, click on the three dots ![](/fig/Three_points.png) and navigate to the folder `../AA_Cyclone_Monitoring_Trigger_MAD/map_templates/` and select the file with the name `cyclone_impact_population_map_template`. Click `Open`, then `Create`. 
4.  QGIS will ask you to name the new layout. Give it a name such as "Cyclone_Overview_Map_Freddy_2023". Click `OK`. A new window will open. This is the print layout composer. It should look similar to the figure below.

:::{figure} /fig/AA/mdg_aa_pop_impact_template.png
---
name: mdg_aa_pop_impact_template
width: 600 px
---
:::

5. **Update the Map Title**  
   - Click on the title text element at the top of the map.
   - In the `Item Properties` panel, edit the **Main Label** text to match your event, e.g. `Cyclone Harald – 2025`.
   - Adjust font size or alignment as needed.
6. **Update the Attribute Table on the Right-Hand Side of the Map**  
   To update the attribute table displaying the exposed districts:
   - In the `Item Properties` panel, select the `exposed_population`**Or any other layer you are working with** layer and click **Refresh Table Data**
   - Click on `Attributes...`
   - In the **Columns** section:
     - Click `Clear`
     - ➕ Add the columns: `ADM1_EN`, `ADM2_EN`, `ADM2_PCODE` and `exposed_population` **or any other layer you are working with**
   - In the **Sorting** section:
     - ➕ Add `ADM1_EN` and set the sort order to `Ascending`
   - Click **OK** to apply

```{note}
If too many districts are affected, the attribute table might not fit the page. Reduce the font size in the table’s item properties to make everything visible — but be aware that this may reduce readability.
```

7. Adjust the Legend by clicking on it in the map layout and have a look at the `Item Properties` tab and scroll down until you see the `Legend items` field. If it is not there, check if you have to open the dropdown. Make sure `Auto update` is **not checked**.
    * Remove all items in the legend by clicking on each item and then the red minus icon
        * In the pop-up, check **Only show visible layers** to help you find the correct ones
        * To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name  
    * ➕ Add the following layers by clicking the green plus:
   - In the pop-up, check **Only show visible layers** to help you find the correct ones
   - 💡 To rename a legend item, **double-click** on the layer name in the legend item list and enter the new name
   - Ensure all legend entries use **clear and meaningful labels**
::::{tab-set}

:::{tab-item} Exposed Population
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_population` → rename to  
```md
Exposed Population
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Buildings 
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_building` → rename to  
```md
Exposed Buildings
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Facilities
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_health_facilities` → rename to  
```md
Exposed Health Facilities
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Education Facilities
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_education_facilities` → rename to  
```md
Exposed Education Facilities
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Agriculture in Hectare
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_agricultural_landcover` → rename to  
```md
Exposed Agriculture in Hectare
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Facilities Points
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_health_facilities_points` → rename to  
```md
Exposed Health Facilities Points
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

:::{tab-item} Exposed Health Education Points
* `Admin1_Impact_Overview_Map` → rename to  
```md
Regions
```
* `exposed_education_facilities_points` → rename to  
```md
Exposed Health Education Points
```
* `Cyclone Track` → rename to  
```md
Projected Cyclone Track
```
* `Exposed_Cyclone_Area` → rename to  
```md
Exposed Cyclone Area
```
* `relevant_warehouses` → rename to  
```md
Relevant Warehouses
```
* `Background Map: OpenStreetMap` → rename to  
```md
Background Map:
OpenStreetMap
```
:::

::::




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

#### Exporting the Map 

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

When you have finished the design of you map you can export it as pdf or image file in different data formats.

__Export as Image__

1. In the print layout click on `Layer` -> `Export as Image`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. For the specific impact assessment change the name to something like **MDG_Trigger_Impact_Population_Map_Freddy_2023**.
3. Click on `Save`
4. The window `Image Export Options` will appear. Click `Save`.
Now the image can be found in the result folder.


__Export as PDF__

1. In the print layout click on `Layer` -> `Export as PDF`
2. Choose the __map_outputs__ folder. Give the file the name of the event e.g **MDG_Trigger_Impact_Overview_Map_Freddy_2023**. For the specific impact assessment change the name to something like **MDG_Trigger_Impact_Population_Map_Freddy_2023**.
3. Click on `Save`.
4. The window `PDF Export Options` will appear. For the best results, select the `lossless` image compression.
5. Click `Save`.
Now the image can be found in the result folder.

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

## Working with the warehouse isochrones

The project includes isochrones for each warehouse. The warehouse isochrones correspond to one warehouse and are identifiable by their location name. If you want to add an isochrone to one of the  It is possible to add individual isochrones to the map templates by simply duplicating the isochrone layer and moving it to the desired map group.

<!--INSERT EXAMPLE PICTURE-->

# Historical Analysis of Cyclone Impacts

To run the full trigger process using historical cyclone track data, you can assess the impacts of past events and gain insights into what occurred in similar scenarios. The storm track data is available from the **International Best Track Archive for Climate Stewardship (IBTrACS)**. Instructions on how to access this data are provided in the following section.

## Download of historical storm track data

The **International Best Track Archive for Climate Stewardship (IBTrACS)** v04r01 data is updated three times a week (usually on Sunday, Tuesday, and Thursday), and could be updated more frequently to address specific needs and use cases. The latest updates in the correct file format can be found on their [website](https://www.ncei.noaa.gov/products/international-best-track-archive):

1. Look for the `Access Methods` section and click on `Shapefiles`. The link leads to the following [website](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/shapefile/) which can also be seen in the figure below.
2. Since we don’t need storm track data for the entire world or the full archive, we will download only a relevant subset. Locate for the file named `IBTrACS.ACTIVE.list.v04r01.lines.zip` and click on it - the download should begin automatically.
3. Unzip the file and open it in QGIS.
4. Open the attribute table and delete all the storm tracks that are not relevant for this analysis. Safe the updated storm track file.

:::{note}

The storm track subset `IBTrACS.ACTIVE.list.v04r01.lines.zip` contains all **storms active in the last 7 days**. If more comprehensive data is needed, it is advisable to download a subset by basin. For Madagascar, the most relevant region is **SI – South Indian**, which includes our Area of Interest. This dataset can be downloaded from the same website under the name `IBTrACS.SI.list.v04r01.lines.zip`. 

:::


```{figure} /fig/MAD_Trigger_stromtrack_download.PNG
---
width: 1000px
name: MAD_Trigger_stromtrack_download
align: center
---
```

