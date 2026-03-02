::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Premiers pas avec QGIS

## Présentation de QGIS

:::{figure} /fig/en_qgis_banner_website.png
---
name: en_qgis_banner_website
width: 300 px
align: right
---
[qgis.org](https://qgis.org/)
:::

:::{div} sd-text-justify
- QGIS est un __logiciel SIG open source__. Cela signifie que son code source est accessible à tous, ce qui fait de QGIS une application gratuite. L’intégralité du code source peut être consultée et téléchargée sur https://github.com/qgis/QGIS.
- QGIS est un __logiciel de bureau__ : cela signifie qu’il s’agit d’un programme qui s’ouvre sur votre ordinateur sous forme de fenêtre, avec des boutons sur lesquels cliquer, des formulaires à remplir pour réaliser des tâches, et une utilisation globalement visuelle et interactive.
- Il permet de __visualiser, modifier, saisir et analyser des données spatiales, ainsi que de produire des cartes imprimables__. QGIS a été créé en 2002 et est développé par une communauté de bénévoles. Il est __en constante évolution__.
- QGIS s’appuie sur une __large communauté d’utilisateurs__, ce qui facilite la recherche de solutions à des problèmes techniques via des forums, des blogs ou des subreddits. La communauté officielle QGIS est accessible [ici](https://qgis.org/en/site/forusers/support.html#support). Par ailleurs, une liste de sites utiles est disponible dans le [wiki ici](/content/fr/Wiki/fr_qgis_common_errors_and_Issues.md).
:::


:::{note}

Gardez à l’esprit qu’à mesure que QGIS continue d’évoluer, son interface et ses fonctionnalités peuvent changer. Les contenus de cette plateforme se réfèrent à la version 3.36 de QGIS. Si le matériel de formation n’est plus à jour, consultez la [documentation QGIS](https://docs.qgis.org/3.34/en/docs/index.html).

:::

:::{attention}

QGIS évolue en permanence, avec l’ajout régulier de nouvelles fonctionnalités. Pour cette raison, les versions les plus récentes peuvent comporter des changements, voire des bugs (par exemple des plantages). Cependant, une version stable est toujours disponible et bénéficie d’un support plus long. Cette version est appelée __Long-term release (LTR)__.

:::


## Travailler avec QGIS


Dans QGIS, vous créez des projets dans lesquels vous visualisez et manipulez des données géographiques. Trois grands flux de travail reviennent le plus souvent : __la collecte et la création de données, le traitement des données, et la visualisation__. Les données géographiques sont chargées dans des projets QGIS et apparaissent sous forme de couches dans la zone de carte.

:::{hint}

Les SIG peuvent impliquer des mathématiques complexes, mais QGIS s’en charge et vous n’avez pas besoin d’une compréhension approfondie des maths et des algorithmes pour utiliser QGIS. __Si vous savez utiliser Excel et PowerPoint, vous ne devriez pas avoir de difficulté à apprendre QGIS__.

:::

::::{tab-set}

:::{tab-item} Collecte et création de données

QGIS propose des outils pour créer vos propres données géographiques. Par exemple, avec les outils de numérisation, vous pouvez créer des points, des polygones et des lignes avec des informations attributaires représentant des phénomènes géographiques. Par ailleurs, le géoréférencement permet d’ajouter une information géographique à différents types de données, comme des images satellites ou des cartes dessinées à la main. Vous apprendrez à créer des données géographiques et à géoréférencer des données dans le __[module 2](/content/fr/Module_2/fr_module_2_overview.md)__.

Il arrive aussi que le travail en SIG nécessite de collecter des données sur le terrain. Dans ce cas, vous pouvez utiliser des [applications web et mobiles](/content/fr/Wiki/fr_web_and_mobile_apps_wiki.md).

:::

:::{tab-item} Traitement des données

QGIS offre un large éventail d’algorithmes pour traiter les données géographiques. Dans les modules suivants, vous découvrirez plusieurs algorithmes particulièrement utiles pour l’usage des SIG dans l’action humanitaire. Vous en apprendrez davantage sur le traitement et la manipulation des données à partir du [module 2](https://giscience.github.io/gis-training-resource-center/content/fr/Modulew_2/fr_module_2_overview.html).

:::

:::{tab-item} Visualisation

QGIS permet de visualiser des données géographiques et de produire des cartes pour communiquer des informations. Cela se fait en attribuant des symboles et des couleurs aux différents éléments de vos données. La mise en place d’une symbologie est l’une des compétences clés que vous développerez en tant qu’utilisateur·rice SIG, et une bonne visualisation est extrêmement utile pour communiquer des résultats. Vous apprendrez à attribuer des symboles dans le [Module 4 : Visualisation des données géographiques et cartographie](/content/fr/Module_4/fr_qgis_map_design_I.md)

:::
::::




:::{card}
__À propos des extensions__
^^^

En plus des algorithmes inclus dans l’installation standard, QGIS propose des extensions qui ajoutent des fonctionnalités supplémentaires à l’application. Ces extensions sont développées par des organisations indépendantes ou par la communauté QGIS. Par exemple, elles permettent de se connecter à des services en ligne comme OpenStreetMap, ou d’ajouter de nouveaux algorithmes pour traiter vos données. Elles peuvent être très utiles selon les besoins. Il existe également des extensions conçues spécifiquement pour l’action humanitaire. Vous en apprendrez davantage sur les extensions dans les modules suivants. Si vous souhaitez savoir comment les installer, consultez le [wiki](/content/fr/Wiki/fr_qgis_plugins_wiki.md).

:::

## Ouvrir un nouveau projet dans QGIS

Ouvrez QGIS comme n’importe quel autre programme sur votre ordinateur. L’écran de démarrage de QGIS affiche généralement les projets récents et propose l’option de créer un nouveau projet.

Il existe __deux__ façons de créer un nouveau projet :

::::{margin}
:::{tip}

Un fichier de projet QGIS possède l’extension `.qgz`.

:::

::::

1. Sur l’écran de démarrage, cliquez sur `Project Template`.

:::{figure} /fig/en_project_template_BRC.png
---
height: 400
name: en_project_template_BRC
align: center
---
:::

2. Dans l’angle supérieur gauche, cliquez sur `Project` → `New Project`.

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_new_project.mp4"></video>



## Aperçu de l’interface de QGIS

L’interface de QGIS peut sembler complexe au premier abord. Cependant, une fois que vous connaissez ses composants, vous pourrez vous y repérer rapidement. Vous trouverez ici une description des principaux éléments de l’interface.

::::{margin}
:::{tip}

Lorsque vous survolez une icône avec le curseur de la souris, un texte s’affiche pour expliquer la fonction du bouton.

:::
::::

:::{figure} /fig/en_QGIS_GUI.png
---
width: 800px 
align: center
name: en_QGIS_GUI
---
Interface utilisateur de QGIS. Source : BRC
:::

1. __Panneau des couches :__ La __liste des couches__ affiche __toutes les couches/fichiers__ qui sont __chargés dans le projet__. Vous pouvez afficher/masquer des couches et modifier d’autres propriétés.

2. __Barres d’outils :__ Les __barres d’outils__ sont des raccourcis permettant d’exécuter des commandes fréquemment utilisées. Par exemple, il existe des barres d’outils spécifiques pour les __données vectorielles et raster__, ainsi que des barres plus générales pour enregistrer le projet, etc. Les barres d’outils contiennent notamment un accès à la __boîte à outils de traitements__, utilisée plus tard dans de nombreuses vidéos du wiki.

:::{figure} /fig/en_Interface_02.png
---
height: 75 px
name: en_Interface_02
align: center
---
:::

3. __Zone de carte :__ La __zone de carte__ est le __composant central__ de tout logiciel SIG. C’est ici que les __données géographiques__ sont affichées. L’affichage cartographique utilise un système de projection qui ne correspond pas forcément à celui des couches.

4. __Coordonnées et échelle :__ Vous trouverez ici des informations sur l’échelle de la zone de carte, ainsi que les coordonnées de la position du curseur.

5. __Panneau Navigateur :__ Le panneau Navigateur vous permet de parcourir les fichiers sur votre ordinateur et de charger des jeux de données dans votre projet QGIS.

6. __Barre de recherche :__ Elle permet de __rechercher des outils et des couches__ dans QGIS. Si vous ne savez pas où se trouve un outil, vous pouvez essayer ici. Vous pouvez également saisir des coordonnées pour vous y rendre dans la zone de carte.

:::{dropdown} Exercice : Créer un nouveau projet QGIS

1. Dans votre dossier “GIS_Training”, créez un __sous-dossier__ nommé "My_First_Project".
2. Ouvrez __QGIS__.
3. Cliquez sur `Project` → `New Project`.
4. Dans le coin supérieur gauche, cliquez sur `Project` → `Save as`, accédez à votre dossier Projects et enregistrez le projet sous le nom "Session_1".
5. Cliquez sur `Save as`, accédez à votre dossier Projects et enregistrez le projet sous le nom "My_First_Project".
6. Ouvrez votre dossier et vérifiez le __fichier `.qgz`__ que vous venez de créer.

:::

:::{attention}

Si vous voyez un `*` dans la barre de titre, à gauche du nom de votre projet, cela signifie que des modifications n’ont pas été __enregistrées__. Comme QGIS peut parfois se fermer inopinément, pensez à enregistrer régulièrement votre projet afin d’éviter de perdre votre travail.

:::

## Boutons et raccourcis

Dans QGIS, la __navigation à la souris__ permet d’interagir avec la zone de carte : déplacement, zoom et sélection d’entités.

Les __raccourcis clavier__ (hotkeys) offrent des accès rapides à différentes commandes, améliorant l’efficacité et accélérant le flux de travail. Vous trouverez ci-dessous les principaux raccourcis.

:::{dropdown} Navigation dans la vue cartographique

| Name                      | Menu option                    | Shortcut                        | Description                                 |
|---------------------------|--------------------------------|---------------------------------|---------------------------------------------|
| Map pan                   | ![](/fig/qgis_pan_map.png)     | <kbd>Space</kbd>, <kbd>Page Up</kbd>,  <kbd>Page Down</kbd> or the <kbd>Arrow Keys</kbd> | Move the map                                 |
| Pan map to selection      | ![](/fig/qgis_pan_map_selection.png) |                                  | Pans the map to the selected element        |
| Zoom in                   | ![](/fig/qgis_zoom_in.png)     | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>+</kbd> or <kbd>mouse wheel</kbd>   | Zoom into the map                            |
| Zoom out                  | ![](/fig/qgis_zoom_out.png)    | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>-</kbd> or <kbd>mouse wheel</kbd>   | Zoom out of the map                          |
| Zoom full                 | ![](/fig/qgis_zoom_full.png)   | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>                  | Zoom to the selected element                |
| Zoom to selection         | ![](/fig/qgis_zoom_to_selection.png) | <kbd>Ctrl</kbd> + <kbd>J</kbd>     | Zoom to the selected element                |
| Zoom to layer             | ![](/fig/qgis_zoom_to_layer.png) |                                  | Zoom to the selected layer                   |
| Zoom to native resolution | ![](/fig/qgis_zoom_native_resolution.png) |                             | Zoom to the native resolution (100%)         |
| Zoom last                 | ![](/fig/qgis_zoom_last.png)   |                                 | Zoom to the last zoom                        |
| Zoom next                 | ![](/fig/qgis_zoom_next.png)   |                                 | Zoom to the next zoom                        |

:::

:::{dropdown} Gestion de projet

| Name            | Menu option                        | Shortcut         | Description                             |
|-----------------|------------------------------------|------------------|-----------------------------------------|
| New Project     | ![](/fig/qgis_new.png)             | <kbd>Ctrl</kbd> + <kbd>N</kbd>   | Create a new project                    |
| Open Project    | ![](/fig/qgis_open_project.png)   | <kbd>Ctrl</kbd> + <kbd>O</kbd>     | Open an existing project                |
| Save            | ![](/fig/qgis_save_project.png)   | <kbd>Ctrl</kbd> + <kbd>S</kbd>     | Save the project                        |
| Save as…        | ![](/fig/qgis_save_project_as.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd>  | Save the project as…           |
| Properties      |                                    | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>   | Open the project properties      |
| New print layout| ![](/fig/qgis_new_print_layerout.png) | <kbd>Ctrl</kbd> + <kbd>P</kbd>  | Opens the Dialog to create a new print layout |
| Search          |                                    | <kbd>Ctrl</kbd> + <kbd>K</kbd>        | Opens the search bar                    |

:::

:::{dropdown} Gestion des couches

| Name                        | Menu option                                  | Shortcut            | Description                       |
|-----------------------------|----------------------------------------------|----------------------|-----------------------------------|
| Data source manager         | ![](/fig/qgis_data_source_manager.png)       | <kbd>Ctrl</kbd> + <kbd>L</kbd>        | Add a new layer                   |
| New GeoPackage layer        | ![](/fig/qgis_new_geopackage_layer.png)     | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> | Add a new GeoPackage Layer       |
| Add vector layer            | ![](/fig/qgis_add_vector_layer.png)         | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Add a new vector layer           |
| Add raster layer            | ![](/fig/qgis_add_raster_layer.png)         | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> | Add a new raster layer           |
| Remove selected layer       | ![](/fig/qgis_remove_selected_layer.png)    | <kbd>Ctrl</kbd> + <kbd>D</kbd>        | Remove the selected layer        |
| Toggle layers view          |                                              | <kbd>Ctrl</kbd> + <kbd>1</kbd>        | Toggle the layers view           |
| Toggle browser view         |                                              | <kbd>Ctrl</kbd> + <kbd>2</kbd>       | Toggle the browser view          |

:::

:::{dropdown} Outils d’analyse

| Name                                     | Menu option                                 | Shortcut                   | Description                                            |
|------------------------------------------|---------------------------------------------|-----------------------------|--------------------------------------------------------|
| Identify Features | ![](/fig/qgis_identify_features.png) | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>  | Identify features on the map view by clicking on them |
| Select feature   | ![](/fig/qgis_select_features.png) |  | Select a feature by area or single click  |
| Select feature by value | ![](/fig/qgis_select_features_by_value.png) | <kbd>F3</kbd> | Select features by value  |
| Open Attribute table    | ![](/fig/qgis_open_attribute_table.png)     | <kbd>F6</kbd>  | Open the Attribute table                              |
| Open Attribute table with selected features only | ![](/fig/qgis_open_attribute_table.png) | <kbd>Shift</kbd> + `F6`             | Open the Attribute table with selected features only  |
| Open Attribute table with visible features only | ![](/fig/qgis_open_attribute_table.png)  | <kbd>Ctrl</kbd> + `F6`               | Open the Attribute table with visible features only   |

:::

:::{dropdown} Outils avancés

| Name                    | Menu option                            | Shortcut          | Description                  |
|-------------------------|----------------------------------------|--------------------|------------------------------|
| Processing Toolbox      | ![](/fig/qgis_processing_toolbox.png) | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> | Opens the Processing Toolbox |
| Python Console          | ![](/fig/qgis_python_console.png)     | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>P</kbd> | Opens the Python Console     |

:::

## Naviguer dans la zone de carte

::::{admonition} *Optionnel* : à vous de jouer !

Vous pouvez suivre les étapes ci-dessous dans votre propre projet QGIS. Téléchargez [ce jeu de données](https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg) puis faites glisser-déposer le fichier `wb_countries_admin0_10m.gpkg` dans la zone de carte. Ce jeu de données correspond aux limites officielles des pays publiées par la [Banque mondiale](https://datacatalog.worldbank.org/search/dataset/0038272/World-Bank-Official-Boundaries).

:::{card}
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_1/wb_boundaries/wb_countries_admin0_10m.gpkg

Télécharger les limites officielles (Banque mondiale).

:::

::::

### Déplacer la vue cartographique

::::{margin}

:::{tip}

Maintenir la touche <kbd>Space</kbd> enfoncée active l’outil ![](/fig/qgis_pan_map.png) `Pan Map` lorsque le curseur se trouve dans la zone de carte. Déplacez simplement la souris tout en maintenant <kbd>Space</kbd> pour déplacer la vue.

:::

::::

Pour déplacer la vue dans la zone de carte avec la souris, vous devez activer l’outil “main”.

:::{image} /fig/qgis_move_symbol.png
---
name: qgis_move_symbol
height: 40 px
---
:::

Vous pouvez aussi déplacer la vue avec les touches fléchées de votre clavier.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_move.mp4"></video>

### Zoomer dans la vue cartographique

::::{margin}

:::{tip}
Maintenir <kbd>Ctrl</kbd> tout en faisant défiler la molette permet de zoomer par incréments plus petits (plus lentement). Essayez d’ajuster la zone de carte à vos besoins avec cette méthode.
:::

::::

La manière la plus simple de zoomer dans la zone de carte est d’__utiliser la molette__.

Ou avec les raccourcis <kbd>Ctrl</kbd> + <kbd>+</kbd> et <kbd>Ctrl</kbd> + <kbd>-</kbd>.

![](/fig/qgis_zoom_symbol.png)

Une autre méthode consiste à utiliser les boutons de zoom du panneau de navigation.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_zoom.mp4"></video>
___

## Boîte à outils et barres d’outils

De manière générale, l’ensemble des fonctionnalités, outils et applications de QGIS sont organisés dans la Boîte à outils. Certains outils disposent également de barres d’outils dédiées que vous pouvez ajouter à l’interface de QGIS.

### Ouvrir la boîte à outils

::::{margin}
:::{tip}

Le raccourci <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> permet d’ouvrir et de fermer la boîte à outils.

:::
::::

Pour ouvrir la Boîte à outils dans QGIS, cliquez sur le bouton en forme d’engrenage, ou cliquez sur `Processing` → `Toolbox`.

![](/fig/Geschlossene_Toolbox_01.png)

Vous pouvez utiliser la barre de recherche pour trouver un outil spécifique.

:::{tip} 

Il arrive que vous souhaitiez faire quelque chose dans QGIS sans connaître le nom exact de l’outil. Dans ce cas, il peut être utile de chercher un mot-clé correspondant à ce que vous pensez être le nom de l’outil.

:::

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_toolbars.mp4"></video>

### Afficher/masquer les panneaux et barres d’outils

Il existe des barres d’outils et des panneaux pour de nombreuses tâches. Pour éviter d’encombrer l’interface, il est préférable d’activer uniquement ceux dont vous avez réellement besoin.

- Pour ajouter ou retirer des barres d’outils, cliquez sur `View` → `Toolbars` → cochez/décochez les barres souhaitées.

- Pour ajouter ou retirer des panneaux, cliquez sur `View` → `Panels` → cochez/décochez les panneaux souhaités.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Anzeigen_einblenden_ausblenden.mp4"></video> 

### Déplacer et organiser les barres d’outils

Sur chaque barre d’outils, un repère composé de deux lignes pointillées est présent. En plaçant le curseur dessus jusqu’à voir apparaître une croix de déplacement, puis en maintenant le bouton gauche de la souris, vous pouvez déplacer la barre d’outils. Cela permet de personnaliser l’organisation de votre interface. En regroupant les barres d’outils sur quelques lignes, vous pouvez également agrandir la zone de carte.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_arrange_toolbars.mp4"></video>

___

## Enregistrer et ouvrir des projets QGIS

Enregistrer votre travail ou ouvrir un projet existant dans QGIS ressemble beaucoup à ce que vous connaissez dans des logiciels comme MS Word. Il existe toutefois une __GRANDE__ différence.  
Dans QGIS, les données géographiques avec lesquelles vous travaillez ne sont __pas__ intégrées au fichier projet. Le fichier projet contient uniquement les chemins d’accès vers les fichiers de données, tels qu’ils existaient au moment du dernier enregistrement. Si l’emplacement de ces données est modifié par la suite, un message d’erreur du type « handle unavailable layers » apparaît lors de la réouverture du projet.

Une bonne organisation des données, fondée sur une arborescence de dossiers stable et bien pensée, permet d’éviter ce type de problème.

:::{Warning} 
Organisez toujours vos données ! Consultez l’article wiki sur l’[Arborescence de dossiers standard](/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.md) pour en savoir plus. 
:::


### Ouvrir des projets

::::{margin}

:::{tip}

Le raccourci <kbd>Ctrl</kbd> + <kbd>O</kbd> ouvre également la boîte de dialogue `Open Project`.

:::

::::

Pour ouvrir un projet QGIS existant, cliquez sur `Project` → `Open…` → accédez à votre projet et ouvrez-le.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_open_project.mp4">
</video>

### Enregistrer des projets

::::{margin}

:::{tip}
<kbd>Ctrl</kbd> + <kbd>S</kbd> enregistre le projet, tandis que <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> permet de définir un emplacement d’enregistrement sur votre ordinateur.
:::

::::

* __Lors du premier enregistrement__ : pour enregistrer le projet QGIS en cours, cliquez sur `Project` → `Save as…` → accédez au dossier où vous souhaitez enregistrer le projet → donnez un nom au projet → `Save`.
* __Pour enregistrer votre progression__ : pour enregistrer l’avancement dans un projet déjà enregistré :
    * Cliquez sur `Project` → `Save`. 


<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_save_project.mp4"></video>


## Icônes d’avertissement

Il peut arriver qu’en travaillant avec QGIS, vous voyiez des icônes d’avertissement orange. Cela indique qu’il faut être vigilant. Pour comprendre la signification d’une icône d’avertissement, __survolez-la avec la souris__ : un texte explicatif apparaîtra. Par exemple, dans {numref}`warning_icon_example`, l’icône indique que les unités de mesure sont en degrés, qui ne sont pas constantes (la distance correspondant à 1° de longitude est beaucoup plus grande à l’équateur qu’aux pôles).

:::{figure} /fig/en_3.36_warning_icon_example.png
---
name: warning_icon_example
width: 700 px
---
Exemple d’icône d’avertissement lors du paramétrage d’un outil de traitement.
:::

## Où trouver de l’aide

:::{admonition} Contactez-nous !
:class: tip
Si vous avez des questions avant ou après la formation, ou si vous avez besoin d’aide, n’hésitez pas à nous contacter en envoyant un e-mail à `gis-training-platform@heigit.org`.
:::

:::{admonition} Erreurs fréquentes et problèmes courants
:class: tip
Nous avons rassemblé une liste des __[Erreurs fréquentes et problèmes courants](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_common_errors_and_Issues.html)__. Si vous êtes bloqué·e (ce qui arrive souvent lorsqu’on travaille avec QGIS !), essayez d’y trouver la solution.
:::


Il existe également une grande et dynamique communauté QGIS en ligne. Si vous rencontrez des difficultés avec une fonctionnalité spécifique, ou si vous avez des questions sur des opérations SIG qui ne sont pas couvertes sur cette plateforme, vous pouvez obtenir de l’aide sur des forums dédiés :

- Documentation QGIS : https://docs.qgis.org/3.34/en/docs/index.html 
- Forum utilisateurs QGIS sur StackExchange : https://gis.stackexchange.com/?tags=qgis
- Groupes d’utilisateurs QGIS : https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups
- Canal Telegram QGIS : https://t.me/joinchat/Aq2V5RPoxYYhXqUPoxRWPQ


Par ailleurs, il existe un grand nombre de tutoriels YouTube, de guides en ligne et de ressources pédagogiques portant sur des opérations SIG spécifiques : il est donc souvent pertinent de faire une recherche rapide sur Google. Entre autres, la [documentation QGIS](https://docs.qgis.org/3.34/en/docs/index.html) propose également des exercices et du matériel de formation, ainsi qu’une [Gentle Introduction to QGIS](https://docs.qgis.org/3.34/en/docs/gentle_gis_introduction/index.html).


## Questions d’auto-évaluation

::::{admonition} Testez vos connaissances
:class: note

Prenez un moment pour récapituler ce que vous avez appris dans ce chapitre en répondant aux questions ci-dessous :

1. __Qu’est-ce que QGIS et que signifie le fait qu’il soit « open source » ?__

:::{dropdown} Réponse
QGIS est un logiciel de Système d’Information Géographique (SIG) qui permet de visualiser, modifier, analyser et produire des cartes à partir de données spatiales (géographiques) et de données attributaires.
Le terme « open source » signifie que le code source est librement accessible : chacun peut l’inspecter, le modifier et le redistribuer (selon la licence). Cela implique également l’existence d’une communauté d’utilisateurs et de développeurs qui contribuent au projet, et que le logiciel est généralement disponible gratuitement.
:::

2. __Citez trois choses que vous pouvez faire avec QGIS.__  

:::{dropdown} Réponse

- Charger des données spatiales (vectorielles ou raster) et les visualiser sur une carte
- Modifier ou numériser des entités (par exemple ajouter des points, des lignes, des polygones)
- Réaliser des analyses spatiales (par exemple tampon, superposition, jointure) ou produire des sorties cartographiques (export PDF/image)
:::

3. __Comment savoir si un projet QGIS est enregistré ou non ?__

:::{dropdown} Réponse
En général, QGIS affiche un astérisque (*) à côté du nom du projet (dans le titre de la fenêtre ou de l’onglet) lorsqu’il existe des modifications non enregistrées. S’il n’y a pas d’astérisque (ou si l’option « Enregistrer » est grisée), cela indique que le projet est à jour.
:::

4. __Comment ouvrir un projet QGIS ?__

:::{dropdown} Réponse
Vous pouvez ouvrir un projet QGIS via le menu `File` → `Open Project` (ou le bouton « Open Project » dans la barre d’outils), puis rechercher un fichier `.qgs` ou `.qgz`. Vous pouvez aussi double-cliquer sur le fichier projet (s’il est associé à QGIS sur votre système) pour l’ouvrir directement dans QGIS.
:::

5. __Comment afficher et masquer des panneaux ou des barres d’outils ?__

:::{dropdown} Réponse
Dans la barre de menu, utilisez `View` → `Panels` ou `Toolbars` pour activer/désactiver (cocher/décocher) les panneaux ou barres d’outils souhaités.
:::

6. __Où trouver de l’aide lorsque vous rencontrez des problèmes avec QGIS ?__

:::{dropdown} Réponse

- Sur notre page [Erreurs fréquentes et problèmes courants](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_common_errors_and_Issues.html)
- En consultant la [documentation QGIS](https://docs.qgis.org/3.34/en/docs/index.html)
- Sur le [forum utilisateurs QGIS sur StackExchange](https://gis.stackexchange.com/?tags=qgis)
- Via les [groupes d’utilisateurs QGIS](https://www.qgis.org/en/site/forusers/usergroups.html#qgis-usergroups)
- En recherchant des tutoriels sur YouTube

:::

::::
