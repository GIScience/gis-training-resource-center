::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 1 (Numérisation) : Accès aux institutions financières <a id="exercise-1-digitisation-access-to-financial-institutions"></a>

## Caractéristiques de l’exercice <a id="characteristics-of-the-exercise"></a>

::::{grid} 2
:::{grid-item-card}
__Objectif de l’exercice :__
^^^

Dans cet exercice, vous apprendrez à numériser des points, des lignes et des polygones représentant des entités dans des zones urbanisées en créant de nouveaux jeux de données. 

__Type d’exercice de formation :__

- Cet exercice peut être utilisé en formation en ligne et en présentiel. 
- Il peut être réalisé en mode pas à pas ou individuellement en autoformation.

:::

:::{grid-item-card}
__Ces compétences sont pertinentes pour :__
^^^ 

- La collecte de données et la numérisation
- La correction d’informations spatiales

:::
::::

::::{grid} 2
:::{grid-item-card}
__Durée estimée de l’exercice :__
^^^

- L’exercice prend environ 2 heures à réaliser, selon le nombre de participant·e·s et leur familiarité avec les outils informatiques.

:::

:::{grid-item-card}
__Articles wiki pertinents :__
^^^

* [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
* [Types de données géographiques](/content/fr/Wiki/fr_qgis_geodata_types_wiki.md)
* [Numérisation](/content/fr/Wiki/fr_qgis_digitisation_wiki.md)
* [Fonds de carte](/content/fr/Wiki/fr_qgis_basemaps_wiki.md)

:::

::::

## Instructions pour les formateur·rice·s <a id="instructions-for-the-trainers"></a>

:::{admonition} Remarque sur les plugins
:class: attention

Cet exercice utilise un plugin qui n’est pas installé par défaut : `OSM Place Search`. Assurez-vous de prendre cela en compte. Par ailleurs, au lieu d’utiliser les XYZ Tiles pour le fond de carte, vous pouvez choisir d’utiliser le plugin __"QuickMapServices"__. 

:::

:::{dropdown} __Espace formateur·rice__ 

### Préparer la formation <a id="prepare-the-training"></a>

- Prenez le temps de vous familiariser avec l’exercice et le matériel fourni.
- Préparez un tableau blanc. Il peut s’agir d’un tableau blanc physique, d’un paperboard ou d’un tableau blanc numérique (par ex. Miro) sur lequel les participant·e·s peuvent ajouter leurs constats et leurs questions. 
- Avant de commencer l’exercice, assurez-vous que tout le monde a installé QGIS et a téléchargé __et décompressé__ le dossier de données.
- Consultez [Comment animer des formations ?](/content/fr/Trainers_corner/fr_how_to_training.mdhow-to-do-trainings) pour quelques conseils généraux sur la conduite d’une formation.

### Conduire la formation <a id="conduct-the-training"></a>

__Introduction :__

- Présentez l’idée et l’objectif de l’exercice.
- Fournissez le lien de téléchargement et assurez-vous que tout le monde a décompressé le dossier avant de commencer les tâches.

__Suivi pas à pas :__

- Montrez et expliquez chaque étape vous-même au moins deux fois et suffisamment lentement pour que tout le monde puisse voir ce que vous faites et suivre dans son propre projet QGIS. 
- Assurez-vous que tout le monde suit et réalise bien les étapes en demandant régulièrement si quelqu’un a besoin d’aide ou si tout le monde suit toujours.  
- Soyez ouvert·e et patient·e face à chaque question ou problème qui pourrait survenir. Vos participant·e·s effectuent essentiellement plusieurs tâches à la fois : suivre vos consignes et se repérer dans leur propre projet QGIS.

__Conclusion :__

- Gardez du temps à la fin de l’exercice pour traiter les éventuels problèmes ou questions liés aux tâches.
- Prévoyez également un temps pour les questions ouvertes. 

:::


:::{Attention}
Essayez d’utiliser systématiquement l’arborescence de dossiers standard. Vous pouvez trouver un modèle __[ici](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.mf#standard-folder-structure)__.
:::

## Contexte : pénurie de liquidités à Abuja <a id="background-cash-crunch-in-abuja"></a>

En 2022, le Nigeria a connu une pénurie de liquidités. Les petites entreprises dépendent fortement des transactions en espèces et des services fondés sur les paiements en liquide. Cela a provoqué une pénurie de cash à Abuja, la capitale du Nigeria. [Article sur la pénurie d’espèces à Abuja](https://businessday.ng/news/article/business-groan-as-cash-crunch-hits-banks-in-abuja/). 

## Tâche : cartographier les banques <a id="task-map-the-banks"></a>

Notre objectif est de créer une couche de points représentant trois banques proches les unes des autres dans le quartier central des affaires (CBD) d’Abuja, au Nigeria. Cela permettra aux personnes d’identifier facilement les banques situées dans le CBD d’Abuja pour leurs opérations. 

Pour cela, nous allons représenter la numérisation de First Bank, du bâtiment Bank of Industry et de Zenith Bank Abuja. 

### Ajouter un fond de carte <a id="add-a-basemap"></a>

1.  Ajoutez OSM comme fond de carte. Pour ajouter OSM comme fond de carte, cliquez sur `Layer` → `Add Layer` → `Add XYZ Layer…`. Choisissez `OpenStreetMap` puis cliquez sur `Add`. 
Organisez vos couches dans le `Layer Panel` de façon à ce que l’OSM soit tout en bas ([Vidéo wiki](/content/fr/Wiki/fr_qgis_basemaps_wiki.md)).

:::{Tip}
Vous ne pouvez pas interagir directement avec un fond de carte !
:::

2. Pour ajouter le plugin `OSM Place Search`, cliquez sur `Plugins` → `Manage and Install Plugins…` → `All` puis recherchez `OSM Place Search`. Une fois le plugin trouvé, cliquez dessus puis sur `Install Plugin`. Vous pouvez ouvrir le `OSM Place Search Panel` comme n’importe quel autre panneau en cliquant sur `View` → `Panels` puis en cochant `OSM Place Search Panel` ([Vidéo wiki](/content/fr/Wiki/fr_qgis_plugins_wiki.md)).
3. Dans le panneau `OSM place search`, recherchez "Abuja Central Business District" puis choisissez Abuja Municipality Area Council, City. Zoomez sur le Central Business District. Nous voulons numériser l’emplacement de banques dans cette zone. 
Pour cela, nous devons créer une nouvelle couche de points : 
    1. Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Vidéo wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md)).
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) puis accédez au dossier `temp` de votre dossier de projet. Donnez au nouveau jeu de données le nom “Abuja_bank_point”. Cliquez sur `Save`.
    - Sous `Geometry type`, sélectionnez `Point`.
    - Sélectionnez le système de coordonnées de référence (SCR) "EPSG:4326-WGS 84". Par défaut, QGIS sélectionne le SCR du projet. 
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne "Name".
        * `Name` = "Name"
        * `Type`: sélectionnez `Text (string)`.
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Cliquez sur `OK`.
    * Votre nouvelle couche apparaîtra dans le `Layer Panel`.


:::{admonition} Ajouter davantage d’informations
:class: tip

Vous pouvez numériser encore plus d’informations en ajoutant davantage de colonnes. Par exemple, vous pouvez ajouter une colonne `amenity` pour indiquer le type d’équipement (banque). Réfléchissez au type de données que vous pourriez ajouter. 

:::

:::{figure} /fig/new_layer_abuja.png
---
height: 400px
name: New point layer Abuja
align: center
---
Création d’une nouvelle couche de points.
:::

4. Vous pouvez maintenant créer un point pour chacune des trois banques de la zone [wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md#add-geometries-to-a-layer). Pour l’instant, la nouvelle couche “Abuja_bank_point” est vide. Pour ajouter des entités, nous pouvons utiliser la `Digitizing Toolbar`. Si vous ne voyez pas cette barre d’outils, allez dans `View` → `Toolbars` puis cochez `Digitizing Toolbar` ([Vidéo wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md#creation-of-point-data)).  ![](/fig/Digitizing_Toolbar.png) 
    1. Sélectionnez la couche de points “Abuja_bank_point” dans le panneau des couches. Accédez à la barre d’outils de numérisation puis cliquez sur ![](/fig/mActionToggleEditing.png). La couche passe alors en mode édition.
    2. Recherchez des banques sur la carte ou utilisez le panneau OSM Place Search. Une fois que vous en avez trouvé une, cliquez sur ![](/fig/mActionCapturePoint.png). Faites un clic gauche sur l’entité que vous souhaitez numériser.
    3. Une fois le clic effectué, une fenêtre "Abuja_bank_point" apparaîtra. Vous pourrez y saisir le nom de la banque.
    4. Répétez le même processus pour autant de banques que vous pouvez en trouver.
    5. Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    6. Cliquez de nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

Voici à quoi votre résultat devrait ressembler.

:::{figure} /fig/Abuja_Banks_Point_Layers.png
---
height: 200px
name: Abuja_Banks_Point_Layers
align: center
---
Les entités numérisées pourraient ressembler à ceci. 
:::

## Cartographier les barrages routiers <a id="mapping-road-blocks"></a>

Nous disposons d’informations fiables indiquant qu’un barrage routier dû à des travaux se trouve au carrefour de "Independent Avenue" et "Tafawa Balewa Way". Pour le visualiser sur notre carte, nous voulons créer un polygone représentant ce barrage routier. Le polygone doit couvrir tout le carrefour.

1. Pour cela, nous avons de nouveau besoin d’une nouvelle couche. Dans ce cas, une couche polygonale. Sa création est en grande partie identique à celle de la couche de points.
    1. Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md)). 
    2. Sous `Database`, cliquez sur ![](/fig/Three_points.png) puis accédez au dossier `temp`. Donnez au nouveau jeu de données le nom “Abuja_roadbloc_polygon”. Cliquez sur `Save`.
    3. `Geometry type`: sélectionnez `Polygon`.
    4. Sélectionnez le système de coordonnées de référence (SCR) "EPSG:4326-WGS 84".
    5. Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne "Roadblock_type".
        * `Name` = "Roadblock_type"
        * `Type`: sélectionnez `Text (string)`.
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Cliquez sur `OK`.

    6. Votre nouvelle couche apparaîtra dans le `Layer Panel`.
2. Pour numériser cette zone, cliquez sur votre nouvelle couche „Abuja_roadbloc_polygon“ ([Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md)). 
    - Cliquez sur ![](/fig/mActionToggleEditing.png) pour démarrer le `edit mode`, puis ajoutez une entité avec `Capture Polygon` ![](/fig/mActionCapturePolygon.png)|. 
    - Dessinez les géométries et saisissez les `feature attributes`, "Roadblock_type" = "Construction_site".
    - Enregistrez les modifications ![](/fig/mActionSaveEdits.png), puis quittez le `Edit mode`. 

    
## Cartographier les itinéraires de liaison <a id="map-the-connection-routes"></a>

Un homme d’affaires a parcouru toute la partie nord de Herbert Macauley Way dans le quartier central des affaires d’Abuja pour effectuer une opération à la Bank of Industry un lundi matin. Malheureusement, il a constaté que le serveur réseau de la banque était en panne et a dû se rendre à Zenith Bank, la seule banque encore opérationnelle. Il a ensuite découvert qu’une route était bloquée au carrefour de Independence Avenue et Tafawa Balewa Way en raison de travaux.

Créez une couche linéaire représentant l’itinéraire routier qui lui permettra d’atteindre facilement Zenith Bank.

1. Pour cela, nous avons de nouveau besoin d’une nouvelle couche. Dans ce cas, une couche linéaire. Sa création est presque identique à celle de la couche de points.
    - Cliquez sur `Layer` → `Create Layer` → `New GeoPackage Layer` ([Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md)). 
    - Sous `Database`, cliquez sur ![](/fig/Three_points.png) puis accédez au dossier `temp`. Donnez au nouveau jeu de données le nom “Abuja_bank_road_connection_line”. Cliquez sur `Save`.
    - `Geometry type`: sélectionnez `Line`.
    - Sélectionnez le système de coordonnées de référence (SCR) "EPSG:4326-WGS 84".
    - Sous `New Field`, vous pouvez ajouter des colonnes à la nouvelle couche. Ajoutez la colonne “Road_type”.
        * `Name` = "Road_type"
        * Cliquez sur `Add to Fields List` ![](/fig/mActionNewAttribute.png) pour ajouter la nouvelle colonne à la `Fields List`.
        * Cliquez sur `OK`.
            :::{admonition} Ajouter davantage d’informations
            :class: tip

            Là encore, en ajoutant davantage de champs, vous pouvez ajouter davantage d’informations. Par exemple, vous pouvez ajouter le type de route (par ex. revêtue, non revêtue, autoroute, résidentielle), la limitation de vitesse ou le nombre de voies. Réfléchissez aux informations que vous pourriez ajouter, ainsi qu’au `Type` que vous utiliseriez. Gardez à l’esprit qu’il n’est pas possible d’effectuer des calculs avec des données de type chaîne de caractères.

            :::
    * Votre nouvelle couche apparaîtra dans le `Layer Panel`.
2. Sélectionnez la couche linéaire “Abuja_bank_road_connection_line” dans laquelle ajouter les données dans le panneau des couches [Wiki](/content/fr/Wiki/fr_qgis_digitisation_wiki.md). 
    1. Allez dans la barre d’outils de numérisation puis cliquez sur ![](/fig/mActionToggleEditing.png). La couche passe alors en mode édition.
    2.	Cliquez sur ![](/fig/mActionCaptureLine.png). 
    3.	Pour numériser une entité linéaire, cliquez le long de la ligne. Une fois terminé, faites un clic droit sur le dernier point de la ligne pour terminer l’entité.
    4.	Une fois le clic effectué, une fenêtre "Abuja_bank_road_connection_line- Feature Attribute" apparaîtra. Ajoutez le type de route, qui est "Secondary_road".
    5.	Une fois la numérisation terminée, cliquez sur ![](/fig/mActionSaveEdits.png) pour enregistrer vos modifications.
    6.	Cliquez de nouveau sur ![](/fig/mActionToggleEditing.png) pour quitter le mode édition.

:::{figure} /fig/Abuja_Banks_final.png
---
height: 400px
name: Abuja_Banks_final
align: center
---
Votre résultat pourrait ressembler à ceci. 
:::
