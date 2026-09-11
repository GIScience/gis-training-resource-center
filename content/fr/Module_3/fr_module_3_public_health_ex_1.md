# Exercice 1 : Créer une carte d’ensemble du système de santé et de la couverture vaccinale <a id="exercise-1-creating-an-overview-map-of-the-health-system-and-vaccination-coverage"></a>

% MISSING:  - MAKE ENRICHED DATASET PERMANENT
%           - BASEMAP
%           - SMALL SELECTION EXPORT/QUERIES?
%           - PROJECTIONS
%           - ADD SMALLER EASIER EXERCISES EARLIER (INCLUDING IMPORTING DATA SO HERE WE CAN INTRODUCE THE PROJECT  HOME)
%           - ADD MORE PICTURES
%           - REMOVE STEPS TO CLEAN HEALTHSITES AS HEALTHSITES WITHOUT INFORMATION COULD STILL BE GOOD; E.G., TO REACH OUT
%           - ADD STEP FOR COUNT POINTS IN POLYGONS FOR HEALTHSITES
%           - ADD STEP FOR JOIN BY LOCATION
%           - MAKE THEM PLAN MEASLES VACCINATION CAMPAIGN
%               - WHERE TO PUT VACCINATION CENTERS WITH HOW MUCH POP TO SERVE
%               - WHERE TO DEPLOY MOBILE VACCINATION CENTERS -> DIGITISATION
%           - IM COORDINATION INSRTUCTED TO GET DATA ON HEALTHSITE CAPACITIES
%           - MAKE THEM DOWNLOAD HDX
%           - ADD SMALL STEPS UNDER DROPDOWN, AS NOTES, ETC. 

## Contexte <a id="background"></a>

Au cours du mois dernier, les autorités sanitaires au Tchad ont signalé une hausse des cas de rougeole, en particulier dans les régions du Mandoul, du Mayo-Kebbi Est et du Logone Oriental. L’unité de surveillance a fourni des données de line-listing ainsi que des données existantes sur les structures de santé. Votre première tâche consiste à créer une carte de base montrant la répartition des structures de santé et à les classifier selon leur capacité de service afin de comprendre les infrastructures de réponse disponibles.

## Données disponibles <a id="available-data"></a>

| Dataset name | Original title | Publisher | Downloaded from | 
| :-------------- | :----------------- |:----------------- |:----------------- |
| `tcd_admbnda_adm0_20250212_AB.shp` (Polygons) | Chad Subnational Administrative Boundaries (level 0: country) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm1_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 1: regions) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd) |
| `tcd_admbnda_adm2_20250212_AB.shp` (Polygons) | Chad Administrative Boundaries (level 2: province) | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/cod-ab-tcd)
| `hotosm_tcd_health_facilities_points_gpkg.gpkg` (Points) | Chad Health Facilities (OpenStreetMap Export) | Humanitarian OpenStreetMap Team | [HOTOSM](https://data.humdata.org/dataset/hotosm_tcd_health_facilities) | 
| `tcd_roads_ocha.shp` (Lines) | Chad - Road Network | United Nations Office for the Coordination of Humanitarian Affairs (OCHA) | [HDX](https://data.humdata.org/dataset/chad-roads-osm-ministry-of-transport) |
| `tcd_healthsite_capacities.csv` | Healthsite Capacities | HeiGIT | This is a fictional dataset generated for the purpose of this exercise. | 
| `vaccination_coverage_adm2.csv` | Measles vaccination coverage | HeiGIT | This is a fictional dataset generated for the purpose of this exercise. | 

:::{note}

Dans cet exercice, nous téléchargerons de vrais jeux de données depuis le [Humanitarian Data Exchange (HDX)](humdata.org) afin d’identifier et d’analyser des informations pertinentes. Toutefois, les jeux de données sur les capacités des structures de santé et la couverture vaccinale utilisés ici sont fictifs et ont été créés uniquement à des fins de formation. Ils ne représentent pas des données du monde réel.

:::



:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/public_health/GIS_Training_Public_Health.zip

__Téléchargez ici tous les jeux de données fournis par HeiGIT [here](https://nexus.heigit.org/repository/gis-training-resource-center/public_health/GIS_Training_Public_Health.zip), enregistrez le dossier sur votre ordinateur et décompressez le fichier.__

:::


---

## Tâches <a id="tasks"></a>

### Tâche 1 : Mettre en place l’arborescence de dossiers et créer un nouveau projet QGIS <a id="task-1-setting-up-the-folder-structure-and-creating-a-new-qgis-project"></a>

:::{admonition} Arborescence de dossiers standard
:class: tip

La pratique la plus importante en matière de gestion des données géographiques consiste à utiliser une arborescence de dossiers standardisée qui contient tous les éléments du projet QGIS. Nous enregistrerons toutes les données que nous utilisons ou créons dans notre projet QGIS à l’intérieur de cette arborescence.
Les chemins entre un projet QGIS et les données géographiques sont, par défaut, relatifs. Cela signifie que lorsque les données et le projet sont organisés dans une structure de dossiers fixe, vous pouvez déplacer l’ensemble de cette structure sans affecter le projet QGIS ni les chemins vers les données.

Une arborescence de dossiers standard présente deux avantages principaux :
1. Si nous partageons l’ensemble du dossier du projet, nous pouvons nous attendre à ce que le projet fonctionne sans problème sur un autre ordinateur.
2. L’arborescence de dossiers favorise une bonne organisation des données du projet et contribue à garantir le bon fonctionnement du projet QGIS.
:::

1. Créez sur votre ordinateur un nouveau dossier nommé "GIS_Training_Public_Health_Day_1-2". Dans ce dossier, créez l’arborescence suivante :

```
GIS_Training_Public_Health
├── project
├── results
├── styles
└── data
    ├── input
    ├── interim
    └── output
```

1. Ouvrez QGIS et créez un nouveau projet.
2. Enregistrez le projet via `Project` → `Save As...`. Accédez au dossier de cette formation et enregistrez-le dans le sous-dossier `/project`. Donnez-lui un nom (par ex. `GIS_Training_Public_Health_Part_1`) puis cliquez sur `Save`. 
3. Nous devons maintenant définir le SCR du projet.
    - Dans le coin inférieur droit de la fenêtre QGIS, cliquez sur l’icône de projection ![](/fig/3.40_projection_icon.png). Choisissons un SCR métrique qui représente le Tchad sans trop de déformation. Pour cet exercice, nous utiliserons __"Albers Equal Area Conic" (EPSG: 102022)__.
Dans la barre `Filter`, saisissez le nom ou le numéro EPSG. Le SCR devrait apparaître dans la boîte "Predefined Coordinate Reference Systems". Sélectionnez-le puis cliquez sur `Apply` et `OK`. 
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_project_crs.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_project_crs.png
    width: 450 px
    ---
    Définir le SCR du projet dans QGIS
    :::

::::{admonition} Comment choisir le bon SCR
:class: dropdown, note

Choisir un système de coordonnées de référence adapté à votre projet SIG est essentiel. En règle générale, vous devez utiliser un SCR qui représente au mieux votre zone d’intérêt. Deuxièmement, vous devez réfléchir au type de calculs que vous prévoyez d’effectuer dans votre projet. Les SCR existent en deux catégories : les systèmes de coordonnées de référence géographiques et les systèmes de coordonnées de référence métriques. Les SCR géographiques utilisent la longitude et la latitude (degrés) comme coordonnées et unités de mesure. Il s’agit de mesures angulaires qui ne représentent pas les distances de manière linéaire. Les SCR métriques utilisent des coordonnées exprimées en __unités linéaires__ (comme les mètres), ce qui signifie qu’ils représentent les distances réelles à la surface de la Terre. Les SCR métriques, comme l’UTM, sont conçus pour la cartographie locale et régionale et peuvent introduire des déformations s’ils sont appliqués à de très grandes zones. Pour des régions très étendues, on utilise souvent des projections comme Albers Equal Area ou Mercator afin de réduire les déformations.

Si vous souhaitez effectuer des calculs de distance, vous devez utiliser un SCR métrique. 

Pour en savoir plus sur les projections et les systèmes de coordonnées de référence, consultez ce __[chapitre du module](/content/fr/Module_2/fr_qgis_projections.md)__.

::::


:::{attention}

Le SCR du projet détermine le système de coordonnées de référence utilisé pour afficher les données géographiques dans le canevas cartographique QGIS. En revanche, il ne modifie pas le SCR des couches. Chaque couche, ou jeu de données, est encodé avec un SCR. QGIS reprojette ces couches "à la volée" pour afficher sur le canevas des couches ayant des SCR différents. Cela ne modifie ni les unités de mesure ni les déformations des couches elles-mêmes. Pour effectuer des calculs de distance, vous devrez [reprojeter la couche](/content/fr/wiki/fr_qgis_projections_wiki.md) dans un système de coordonnées de référence métrique. 

Définir le SCR du projet sur celui que vous souhaitez utiliser peut vous aider à choisir plus rapidement le bon SCR lors de l’exécution d’algorithmes. 
:::
% SET UP PROJECT HOME IN NEXT EXERCISE


### Tâche 2 : Télécharger les données pertinentes <a id="task-2-downloading-the-relevant-data"></a>

1. Dans votre navigateur, rendez-vous sur __humdata.org__ 
2. Recherchez les jeux de données suivants :
    - Chad Administrative Boundaries (OCHA): ADM0, ADM1, ADM2 
    - Chad Health Facilities (OpenStreetMap Export)
    - Chad Roads (OCHA)
:::{figure} /fig/en_m3_ex_8_public_health_part_1_hdx_search.png
---
width: 600 px
name: en_m3_ex_8_public_health_part_1_hdx_search
---
:::
3. Téléchargez les couches.
    - Sur la page de téléchargement, vous pouvez généralement choisir différents formats de données. Les formats sont indiqués par leur extension de fichier (par ex. `.shp`, `.gpkg`, `.gdb`).
    - Parfois, les données sont encore compressées, de sorte que l’extension du fichier n’est pas visible.
    - Choisissez les formats suivants : 
        - Chad Administrative Boundaries (OCHA): __Shapefile__
        - Chad Health Facilities (OpenStreetMap Export): __GeoPackage__ pour les __Points__, nous n’avons pas besoin des polygones pour cet exemple
        - Chad Roads (OCHA): __Shapefile__ 
        :::{figure} /fig/en_m3_ex_8_public_health_part_1_hdx_data_formats.png
        ---
        name: en_m3_ex_8_public_health_part_1_hdx_data_formats
        width: 600 px
        ---
        :::
4. Décompressez les dossiers et veillez à les enregistrer dans le dossier `data/input/` de l’arborescence standard. 


% ADD IMAGE AND EXPAND THIS SECTION: DONE


### Tâche 3 : Importer les jeux de données <a id="task-3-importing-the-datasets"></a>

1. Dans votre projet QGIS, [importez les jeux de données suivants](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#open-vector-data-via-drag-and-drop) par glisser-déposer :
    - `tcd_admbnda_adm0_20250212_AB.shp`
    - `tcd_admbnda_adm1_20250212_AB.shp`
    - `tcd_admbnda_adm2_20250212_AB.shp`
    - `hotosm_tcd_health_facilities_points_gpkg.gpkg`
    - `tcd_trs_roads_OCHA.shp`
::::{margin}
:::{tip}
Un shapefile est composé de plusieurs fichiers interdépendants. L’information géométrique est stockée dans le fichier `.shp`. Pour faciliter l’import, vous pouvez trier le dossier par "File type" et ne faire glisser que le fichier approprié.  
:::
::::

:::{dropdown} Vidéo : importer des shapefiles dans un projet QGIS par glisser-déposer
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_import_vector_d_d.mp4"></video>
:::

% THIS STEP NEEDS REVISING: THEY ARE DOWNLOADING THE DATASET THEMSELVES AS GEOPACKAGE

% THE FOLLOWING SECTION IS NOT NEEDED THEN?

<!--
4. The file `hotosm_tcd_health_facilities_points.csv` contains point data, but it is in a delimited text format. QGIS won't automatically recognise the geographic information and display the dataset as points. We need to import it as a [delimited text layer](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_import_geodata_wiki.html#text-data-import):
    - In the top bar, click on `Layer` → `Add Layer` → `Add Delimited Text Layer...`. A new window will open. Here we need to specify the file, the file format and define the geometry information
    - To the right of the `File name`-field, click on the ![](/fig/Three_points.png) three points to open the file browser. 
    - Navigate to the data input folder and select the file `hotosm_tcd_health_facilities_points.csv`. Click `Open`.
    - Make sure that QGIS uses the correct delimiter (e.g., comma, tab, semicolon, etc.). If it is the correct delimiter, a preview of the datatable should appear in the Sample Data field. 
    - Specify the `X-` and `Y-field` by selecting the respective column. 
    - Click `Add`. The healthsites should now appear as points on your map canvas. 

:::{dropdown} Video: Importing CSV files via the Data Source Manager
<video width="90%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_textfile.mp4"></video>
:::
-->

:::{attention}

Les fichiers importés __ne sont pas enregistrés dans__ le projet QGIS. Si vous déplacez ou supprimez le fichier d’origine, QGIS ne retrouvera plus le jeu de données correspondant. 

:::

### Tâche 4 : Le panneau des couches et le concept de couche <a id="task-4-the-layers-panel-and-the-layer-concept"></a>

1. Une fois toutes les couches pertinentes importées, commençons par les organiser logiquement afin de travailler plus facilement. Sur la gauche se trouve le panneau `Layers`. Vous pouvez y voir tous les jeux de données que nous avons importés jusqu’à présent. 
    - QGIS affiche les données géographiques sous forme de couches, chaque jeu de données étant représenté dans une couche. Les couches sont empilées les unes sur les autres. 
    - Organisons les couches pour travailler plus facilement :
        - La couche ADM0 doit être en bas, suivie de ADM1, puis de ADM2.
        - Ensuite, nous pouvons ajouter le réseau routier.
        - Les structures de santé doivent se trouver au-dessus. 
2. Ajoutons un fond de carte :
    - Dans le navigateur de fichiers, faites défiler vers le bas jusqu’à voir `XYZ-Tiles`
    - Dépliez-le puis <kbd>double-cliquez</kbd> sur `OpenStreetMap`. Une nouvelle couche sera ajoutée à votre panneau des couches, généralement en bas. Veillez à ce que cette couche reste tout en bas du panneau afin que toutes les autres couches restent visibles.

> Votre fenêtre QGIS devrait ressembler à ceci (avec des couleurs de couches différentes).

:::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_ordering_layers.png
---
name: en_3.40_m3_ex_8_pub_health_1_ordering_layers
width: 750 px
---
:::

3. Examinons maintenant les couches que nous avons ajoutées jusqu’ici. Chaque couche vectorielle possède une table attributaire, dans laquelle chaque ligne représente une entité géométrique sur le canevas cartographique.
    - Ouvrez la table attributaire en faisant un <kbd>clic droit</kbd> sur la couche ADM2 dans le panneau des couches à gauche → `Open Attribute Table`.
    - Une nouvelle fenêtre s’ouvre. Il s’agit de la table attributaire. Elle affiche la couche vectorielle sous forme tabulaire, ce qui vous permet de consulter les valeurs attributaires, de trier la table et de modifier les valeurs à l’aide des outils de la barre supérieure. 
    - Regardez les différentes colonnes de la table attributaire. Que représentent-elles ?
    - Essayez de trier la table attributaire en cliquant sur ![](/fig/sort.png)
    - Ouvrez les tables attributaires des couches `hotosm_tcd_health_facilities_points_gpkg` et `tcd_admbnda_adm2_20250212_AB.shp` et familiarisez-vous avec les données. 
    - <kbd>Faites un clic droit</kbd> sur chaque couche et sélectionnez 

<!--- ADD SOME ADDITIONAL INFO HERE?
:::{dropdown} Familiarisez-vous avec l’interface QGIS

Familiarisez-vous avec le canevas cartographique en zoomant et dézoomant (<kbd>Molette de souris</kbd> ou <kbd>Ctrl</kbd> + <kbd>+</kbd> et <kbd>Ctrl</kbd> + <kbd>-</kbd>). 
Maintenir <kbd>Space</kbd> active automatiquement l’outil ![](/fig/qgis_pan_map.png) `Pan Map`. 

:::
-->


### Tâche 5 : Joindre les données de couverture vaccinale aux limites administratives <a id="task-5-joining-vaccination-coverage-data-with-administrative-boundaries"></a>

% ADD A DISCLAIMER MAKING TRAINEES THINK WHERE THE DATA CAME FROM

Dans notre dossier `data/input/`, nous trouvons un fichier csv nommé `vaccination_coverage_adm2`. Ce fichier contient la couverture vaccinale pour les vaccins mcv1 et mcv2. Heureusement, le jeu de données inclut le nom du district (`amd2_name`) ainsi que le pcode adm2. Grâce à ces informations, nous pouvons effectuer une [jointure non spatiale](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_non_spatial_joins_wiki.html) afin d’ajouter les données de couverture vaccinale à notre couche des limites de district (adm2). 

:::{attention}
Les Pcodes administratifs sont bien adaptés aux jointures non spatiales dans QGIS, car ils fournissent des identifiants uniques et normalisés qui évitent les divergences de noms et garantissent une liaison de données fiable et précise.
:::

% ADD ADM2 PCODE TO DATASET AND HAVE THE ADM2 NAMES IN ENGLISH SO THEY CAN'T JOIN WITH ADM2 NAMES BUT USE PCODES: DONE

1. Importez `vaccination_coverage_adm2` dans votre projet QGIS :
    - Dans la barre supérieure, allez à `Layer` → `Add Layer` → `Add Delimited Text Layer...`
    - À droite du champ `File name`, cliquez sur les ![](/fig/Three_points.png) trois points et accédez au fichier `data/input/vaccination_coverage_adm2.csv`, puis cliquez sur `Open`.
    - Dans la fenêtre d’import, vous verrez un aperçu des données dans le champ des données d’exemple. Examinez les colonnes et les données disponibles. Quel type d’information est présent dans chaque colonne ? 
    - Malheureusement, cette table de données ne contient pas de colonnes avec les coordonnées des structures de santé individuelles. Sous `Geometry Definition`, sélectionnez `No geometry (attribute only table)`.
    - Cliquez sur `Add`. La couche apparaîtra dans l’onglet des couches comme une table de données, mais ne s’affichera pas dans le canevas cartographique.
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_add_vacc_coverage_csv.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_add_vacc_coverage_csv
    width: 700 px
    ---
    :::
2. Examinez plus en détail cette nouvelle table de couverture vaccinale :
    - <kbd>Faites un clic droit</kbd> sur la nouvelle couche et ouvrez la table attributaire. Quelles informations sont disponibles ? Comment la table est-elle structurée ? Nous pouvons voir que nous pouvons utiliser la colonne `ADM2_PCODE` pour effectuer une [jointure non spatiale].
3. Dans la [boîte à outils de traitements](/content/fr/Module_1/fr_qgis_start.md#toolbox--toolbars) à droite, recherchez l’outil __"Join attributes by key value"__ et <kbd>double-cliquez</kbd> dessus. 
    - Une nouvelle fenêtre s’ouvre. Nous pouvons y définir les paramètres de l’outil `Join attributes by field value`.
    - Comme "Input layer", sélectionnez la couche `tcd_admbnda_adm2_20250212_AB`.
    - Sous "Table field", sélectionnez `ADM2_PCODE`.
    - Comme "Input layer 2", sélectionnez `vaccination_coverage_adm2`.
    - Sous "Table field 2", sélectionnez `adm2_pcode`.
    - Sous "Layer 2 fields to copy", nous pouvons choisir les colonnes à copier. Cliquez sur les ![](/fig/Three_points.png) trois points à droite du champ et sélectionnez `vaccination_rate_mcv1` et `vaccination_rate_mcv2`. Puis cliquez sur `OK`.
    - Enfin, pour exécuter l’algorithme, cliquez sur `Run`. 
    
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_join_attr_vaccine_coverage.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_join_attr_vaccine_coverage
    width: 650 px
    ---
    :::

Une nouvelle couche appelée "Joined Layer" apparaîtra dans le panneau des couches. À sa droite, vous verrez un symbole ![](/fig/qgis_3.40_temp_layer.png). Ce symbole indique qu’il s’agit d’une couche temporaire de travail. Cela signifie qu’elle sera supprimée lorsque vous fermerez votre projet QGIS, même si vous enregistrez le projet. 

4. __Nous pouvons enregistrer la couche temporaire__ en faisant un <kbd>clic droit</kbd> dessus puis en sélectionnant `Make permament...`.
    - Une nouvelle fenêtre s’ouvrira. Nous devons y préciser l’emplacement du fichier et le nom de la couche. 
    - Laissez le `Format` sur "GeoPackage".
    - Cliquez sur les ![](/fig/Three_points.png) trois points, accédez au dossier `data/interim/` et saisissez un nom de fichier tel que `tcd_adm2_vacc_coverage`. Cliquez sur `Save`. 
    - Saisissez le même nom dans le champ `Layer name` (ce sera le nom de la couche dans le panneau des couches).
    - Laissez le reste inchangé puis cliquez sur `Ok`.

> Très bien ! Nous avons ajouté les informations de couverture vaccinale à notre couche adm2. Nous pouvons maintenant visualiser ces informations en appliquant une symbologie graduée à la couche.

### Tâche 6 : Visualiser la couverture vaccinale <a id="task-6-visualising-the-vaccination-coverage"></a>

:::{Admonition} Enregistrer votre progression
:class: tip

Pensez à enregistrer votre projet régulièrement pour conserver votre progression en cliquant sur ![](/fig/qgis_save_project.png). QGIS est en constante évolution grâce à la communauté open source et il lui arrive de planter de temps en temps. 

:::

Maintenant que les informations de couverture vaccinale figurent dans notre couche adm2, nous pouvons les visualiser afin de comprendre leur répartition spatiale. 
::::{margin}
:::{tip}
QGIS propose différentes façons de [visualiser les données vectorielles](/content/fr/Module_4/fr_qgis_styling_vector_data.md). Si vous souhaitez en savoir plus sur ces différentes méthodes, consultez le [module 4](/content/fr/Module_4/fr_module_4_overview.md).
:::
::::

::::{margin}
:::{tip}
Vous pouvez déplacer la fenêtre des propriétés sur le côté afin de voir les changements de symbologie directement dans le canevas cartographique.
:::
::::
1. Ouvrez l’onglet de symbologie via la fenêtre des propriétés de la couche : 
    - <kbd>Faites un clic droit</kbd> sur la couche `tcd_adm2_vacc_coverage` → `Properties`. 
    - Accédez à "Symbology" dans les onglets à gauche.
    - Ici, nous pouvons changer la méthode de symbologie de `Single Symbol` à `Graduated`.
    - Ensuite, nous devons sélectionner la valeur qui sera utilisée pour la classification. Sous `Value`, sélectionnez la colonne `vaccination_rate_mcv1` puis cliquez sur classify. Nous voulons utiliser le mode `Equal Interval` avec 5 classes pour une première évaluation de la couverture vaccinale.

:::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_vacc_coverage_map.png
---
name: en_3.40_m3_ex_8_pub_health_1_vacc_coverage_map
width: 700 px
---
Capture d’écran de la variable vaccination_rate_mcv1 classée
:::

% ADD CLASSIFICATION STEPS AND RESULT IMAGE: DONE

### Tâche 7 : Enrichir le jeu de données des structures de santé <a id="task-7-enriching-the-healthsites-dataset"></a>

% HERE MAYBE HAVE SOME ENTRIES IN THE ADM2 COLUMN USE FRENCH NAMES OR HAVE SOME TYPOS (MAX 2 or 3). BUT SHOW HOW YOU HAVE TO CLEAN DATA TO MAKE THINGS WORK. CHECK THE LOG AND THEN RERUN 

Dans cette étape, nous voulons enrichir la couche contenant les structures de santé avec des données supplémentaires sur leur capacité. La couche `tcd_healthsite_capacities.csv` contient des informations sur la capacité en lits de l’unité de soins pédiatriques ainsi que sur la capacité de chaîne du froid. Ces informations sont utiles pour identifier la capacité du secteur de la santé à traiter les cas aigus de rougeole et à coordonner une campagne de vaccination. 

:::{admonition} Recueillir les informations sur les capacités
Dans un scénario réaliste, ces données pourraient avoir été collectées lors d’une évaluation rapide des structures de santé menée par le ministère de la Santé et des volontaires de la Croix-Rouge.
Comme la collecte de données a été décentralisée et partiellement réalisée sur support papier, certains noms de structures diffèrent légèrement d’un jeu de données à l’autre (par ex. variantes orthographiques, abréviations).
Lors des jointures, soyez attentif·ve à ce type d’incohérences.
:::

1. Importons `tcd_healthsite_capacities.csv` dans votre projet QGIS :
    - Dans la barre supérieure, allez à `Layer` → `Add Layer` → `Add Delimited Text Layer...`
    - À droite du champ `File name`, cliquez sur les ![](/fig/Three_points.png) trois points et accédez au fichier `data/input/tcd_healthsite_capacities.csv`, puis cliquez sur `Open`.
    - Dans la fenêtre d’import, vous verrez un aperçu des données dans le champ des données d’exemple. Examinez les colonnes et les données disponibles. Quel type d’information est présent dans chaque colonne ? 
    - Malheureusement, cette table de données ne contient pas de coordonnées pour les structures de santé individuelles. Sous `Geometry Definition`, sélectionnez `No geometry (attribute only table)`.
    - Cliquez sur `Add`. La couche apparaîtra dans votre onglet des couches sous forme de table de données, mais ne sera pas affichée dans le canevas cartographique.
2. Examinons plus en détail la table des capacités. 
    - <kbd>Faites un clic droit</kbd> sur la couche et ouvrez la table attributaire. 
    - Dans la barre supérieure, vous pouvez voir combien d’entrées contient le jeu de données (*148 features*)
    - La table de données contient une colonne appelée `name`, qui contient le nom des structures de santé. Ces noms sont les mêmes que ceux stockés dans la couche ponctuelle des structures de santé importée précédemment.
    - Cela signifie que nous pouvons joindre les deux tables à l’aide des valeurs attributaires de la colonne `name`.
3. Dans la [boîte à outils de traitements](https://giscience.github.io/gis-training-resource-center/content/fr/Module_1/fr_qgis_start.html#toolbox-toolbars), recherchez l’outil `Join attributes by field value` et ouvrez-le par <kbd>double-clic</kbd>. 
    - Une nouvelle fenêtre s’ouvrira. Nous pouvons y définir les paramètres de l’outil `Join attributes by field value`.
    - Comme "Input layer", sélectionnez la couche `hotosm_tcd_health_facilities_points_gpkg`.
    - Sous "Table field", sélectionnez `name`.
    - Comme "Input layer 2", sélectionnez `tcd_healthsite_capacities`.
    - Sous "Table field 2", sélectionnez `name`.
    - Sous "Layer 2 fields to copy", nous pouvons choisir les colonnes à copier. Cliquez sur les ![](/fig/Three_points.png) trois points à droite du champ et sélectionnez `cold_chain`, `measles_vaccination`, `measles_treatment`, `beds_total`, `pediatric_beds`, `staff_total`, et `remarks`. Puis cliquez sur `OK`.
    - Enfin, pour exécuter l’algorithme, cliquez sur `Run`. 
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value.png
    ---
    width: 550 px
    name: en_3.40_m3_ex_8_pub_health_1_join_attr_by_field_value
    ---
    :::

    :::{note}
    Après avoir exécuté l’algorithme, la fenêtre basculera vers l’onglet `Log`. Vous pourrez y voir si l’algorithme a rencontré un problème. Dans notre cas, nous pouvons voir que 149 entités ont été jointes avec succès tandis que 183 n’ont pas pu être jointes. Cela se produit lorsque la valeur d’identification (table field) est absente de la colonne correspondante de la couche 2. Cela peut arriver soit parce que la donnée n’est pas disponible, soit à cause d’incohérences dans la valeur d’identification, comme des fautes de frappe ou des orthographes différentes.
    :::
    - Après avoir consulté le `Log`, nous pouvons fermer la fenêtre de l’outil. Une nouvelle couche appelée `Joined layer` devrait apparaître dans votre panneau des couches. Renommez-la en `healthsites_points_capacities` et déplacez-la tout en haut. 

> Nous disposons maintenant d’une nouvelle couche ponctuelle contenant les capacités des structures de santé pertinentes. Grâce à ces informations, nous pouvons créer une carte montrant les capacités du secteur de la santé. 

### Tâche 8 : Nettoyer les données des structures de santé <a id="task-8-cleaning-the-healthsite-data"></a>

% This step is not necessary

1. Examinons la nouvelle couche que nous venons de créer, qui inclut les capacités des structures de santé, en ouvrant la table attributaire. 
    - <kbd>Faites un clic droit</kdd> sur la couche puis ouvrez la table attributaire.
    - Dans la table attributaire, si vous faites défiler vers la droite, vous verrez les nouvelles colonnes contenant les informations ajoutées via l’outil "join attributes by field value".
    - Triez la table attributaire selon les nouvelles colonnes. Comme vous pouvez le constater, toutes les entités ne disposent pas d’informations sur la capacité. 
    - Nous pouvons retirer les structures de santé sans informations supplémentaires, puisqu’elles sont déjà disponibles dans le jeu de données d’origine.
    - Triez la colonne `beds_total` par ordre croissant, de manière à faire apparaître les entités ayant une valeur "NULL" en haut. 
    - Cliquez sur le numéro de ligne à gauche et sélectionnez la première entité. Lorsqu’elle est sélectionnée, l’entité apparaît en bleu.
    - Faites ensuite défiler jusqu’à voir la première entité dont la valeur de la colonne `beds_total` est différente de "NULL".
    - Maintenez <kbd>Shift</kbd> et cliquez sur le numéro de la dernière ligne ayant la valeur NULL. 
    - Dans la barre d’outils de la table attributaire, cliquez sur le bouton ![](/fig/mActionToggleEditing.png) `Toggle Editing Mode` pour passer en mode édition. 
    - Ensuite, cliquez sur ![](/fig/attribute_table_delete_feature.png) `Delete selected features` pour supprimer les points sans information de capacité. 
    - Cliquez sur ![](/fig/mActionToggleEditing.png) pour enregistrer et quitter le mode édition.
    - Enregistrez la couche nettoyée des capacités des structures de santé en faisant un <kbd>clic droit</kbd> dessus puis en sélectionnant `Make permament...`. Choisissez "Geopackage" comme format de sortie, enregistrez la couche dans le dossier `data/interim/` et saisissez un nom de fichier comme `tcd_healthsites_points_capacities`. Cliquez sur `Save`.


% Adjust the cleaning instructions to decide on cold capacity = NULL: WILL BE DONE IN ONE OF THE FOLLOWING EXERCISES

> Notre nouvelle couche ponctuelle des structures de santé n’inclut désormais que les structures pour lesquelles nous avons reçu des données supplémentaires.

### Tâche 9 : Classifier les structures de santé <a id="task-9-classifying-the-healthsites"></a>

1. Nous pouvons maintenant classifier les points représentant les structures de santé afin d’indiquer quelles structures disposent d’une chaîne du froid pour stocker les vaccins contre la rougeole.
    - <kbd>Faites un clic droit</kbd> sur `tcd_healthsites_points_capacities` puis sélectionnez `Properties`. Une nouvelle fenêtre s’ouvrira.
    - À gauche, accédez à l’onglet Symbology.
    :::{figure} /fig/en_3.40_m3_ex_8_pub_health_1_classifying_healthpoint_capacity.png
    ---
    name: en_3.40_m3_ex_8_pub_health_1_classifying_healthpoint_capacity
    width: 600 px
    ---
    :::

    - Au lieu de `Single Symbol`, nous allons maintenant sélectionner `Categorised` comme méthode de visualisation.
    - Comme "Value", sélectionnez `cold_chain`
    - Ensuite, cliquez sur `Classify`. 
    - Si vous le souhaitez, vous pouvez ajuster la symbologie des classes en double-cliquant sur l’une d’elles. 
    - Comme nous ne nous intéressons pas aux valeurs de `cold_chain` égales à NULL, nous pouvons supprimer cette entrée de classification en la sélectionnant puis en cliquant sur le signe moins rouge juste à côté du bouton `Classify`.
    - Cliquez sur `Apply`, puis fermez la fenêtre des propriétés. 
    - Analysez la répartition des structures de santé ayant une valeur `cold_chain` vraie.

% Also remove the NULL values from the categorisation: DONE

% Optionally, add DEM here and style the raster layer. This will be used for a overview map. -> WHAT WAS THE IDEA HERE?

<!---
### Task 7: Add Digital elevation model <a id="task-7-add-digital-elevation-model"></a>
-->