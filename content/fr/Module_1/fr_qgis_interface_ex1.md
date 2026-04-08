::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 1 : Comprendre l’interface de QGIS

## Objectif de l’exercice

QGIS est un logiciel complexe offrant de nombreuses fonctionnalités, et son interface peut sembler déroutante, en particulier pour les débutant·e·s. Cet exercice vous permettra de vous familiariser avec les principales barres d’outils, fenêtres et panneaux dans QGIS. Vous allez créer un nouveau projet QGIS, l’enregistrer, puis explorer les différents panneaux et barres d’outils.

L’exercice couvre : 

- L’enregistrement et l’ouverture d’un projet QGIS
- L’identification et l’utilisation des différentes barres d’outils
- L’identification et l’utilisation des différents panneaux 
- Le déplacement des panneaux
- L’activation de nouveaux panneaux


## Articles wiki associés

- [Interface QGIS](/content/fr/Wiki/fr_qgis_interface_wiki.md)
- [Projets et arborescence de dossiers](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_projects_folder_structure_wiki.html)


## Préparation des données

Dans cet exercice, nous n’utiliserons pas de données géographiques. Nous allons plutôt apprendre à naviguer dans les différentes interfaces et à enregistrer et ouvrir un projet QGIS. Vous pouvez télécharger la structure de dossiers modèle compressée [ici](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_1/Modul_1_Exercise_1_Understanding_the_interface/Modul_1_Exercise_1_Understanding_the_interface.zip).

:::{figure} /fig/standard_folder_structure_new_2025.drawio.png
---
width: 800px
align: center
name: Standard folder structure
---
Arborescence de dossiers standard. Source : HeiGIT.
:::
---

## Tâches

1. Créez un nouveau projet. Lorsque vous ouvrez QGIS, l’écran de démarrage apparaît et affiche l’interface sans projet chargé. À gauche, vous trouverez un panneau affichant les projets récents (probablement vide si vous débutez). À droite, un panneau d’actualités présente des publications du blog QGIS, et en dessous se trouve le panneau `Project Templates`.

:::{figure} /fig/en_project_template_BRC.png
---
height: 400
name: en_project_template_BRC
---
:::

- Dans le panneau `Project Templates`, __double-cliquez sur l’option `New Empty Project`__ (il devrait s’agir du seul modèle visible). Une zone de travail vide apparaît dans l’interface principale, car aucune donnée n’est encore chargée.

2. Familiarisez-vous avec l’interface QGIS : au-dessus de la zone de travail, vous trouverez les __barres d’outils__ contenant de nombreuses fonctions. À gauche et à droite de la zone de travail se trouvent les panneaux. Dans QGIS, vous accédez généralement aux outils via les __barres d’outils__ ou les __panneaux__.

- Les barres d’outils se situent par défaut en haut de l’écran. Elles regroupent les commandes permettant d’interagir avec l’interface.
- Les panneaux se trouvent par défaut sur les côtés de l’écran. Ils incluent notamment le navigateur de fichiers et le panneau des couches à gauche. D’autres panneaux peuvent être activés pour rechercher et utiliser des outils de traitement. Dans le panneau des couches, vous verrez apparaître les données que nous ajouterons ultérieurement.
À droite de l’écran, vous trouverez très probablement le panneau __Boîte à outils de traitements__. S’il n’apparaît pas, consultez cette [page wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_common_errors_and_Issues.html#missing-toolbox).

:::{figure} /fig/en_QGIS_GUI.png
---
width: 800px
align: center
name: QGIS User Interface
---
Interface utilisateur de QGIS.
:::

3. Vous pouvez détacher un panneau de son emplacement en cliquant sur son titre et en le faisant glisser. Vous pouvez soit l’ancrer à un autre panneau (il apparaîtra alors sous forme d’onglet), soit le transformer en fenêtre indépendante. Vous pouvez également redimensionner les panneaux. Essayez par exemple de déplacer le panneau des couches vers la droite ([Vidéo Wiki](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_interface_wiki.html#move-and-arrange-toolbars)). 

:::{tip}

Dans QGIS, l’interface peut apparaître légèrement différente selon la résolution de votre écran. Il arrive que certains éléments soient masqués en raison des paramètres d’affichage par défaut. Si cela se produit, essayez de redimensionner les panneaux et d’explorer les différentes options et fonctionnalités disponibles. Cela vous permettra d’accéder facilement à tous les outils essentiels pendant votre travail.

:::

4. QGIS propose d’autres panneaux qui ne sont pas affichés par défaut. Voyons comment les localiser et les activer.
- Dans le menu `Vue`, recherchez les options `Panneaux` et `Barres d’outils`. En passant la souris sur chacune d’elles, une liste des panneaux et barres d’outils disponibles apparaît, ainsi que leur état (activé ou non). Prenez un moment pour parcourir les différentes options. Il existe de nombreuses possibilités, mais ne vous inquiétez pas : vous n’en utiliserez qu’une partie dans cette formation. Les panneaux que nous utiliserons le plus souvent sont : 
- Navigateur
- Couches
- Style de couche
- Boîte à outils de traitements

5. Observons maintenant les barres d’outils. Celles que nous utiliserons le plus souvent sont :  
- Barre d’outils Attributs
- Barre d’outils Numérisation
- Barre d’outils Navigation cartographique
- Barre d’outils Projet
- Barre d’outils Sélection
 

Prenez le temps de vous familiariser avec les différentes façons d’organiser l’interface QGIS. Savoir où trouver les différentes fonctionnalités vous fera gagner beaucoup de temps et vous évitera des frustrations à l’avenir.

6. Enregistrons maintenant le projet. Cliquez sur l’icône d’enregistrement dans la barre d’outils ou ouvrez le menu `Projet` puis choisissez `Enregistrer sous...`
    1. Choisissez un emplacement pour le fichier projet. L’endroit idéal est le sous-dossier du projet dans la structure de dossiers modèle. Accédez au dossier nommé `Module_1_Exercise_1`. Donnez un nom à votre projet QGIS (par exemple : `QGIS_Training_Exercise_1`). Le projet sera enregistré sous forme de fichier `.qgz`.
    2. Cliquez sur `Enregistrer`. 
    3. Fermez l’application QGIS puis rouvrez-la.
7. Lorsque QGIS redémarre, le projet que vous venez d’enregistrer apparaît dans le panneau `Projets récents`. Vous pouvez double-cliquer dessus pour l’ouvrir. Vous pouvez également accéder au fichier `.qgz` via votre explorateur de fichiers et double-cliquer dessus.  
Cela lancera également QGIS et chargera le projet.

:::{Tip}

Maintenir une arborescence de dossiers organisée contribue grandement à travailler efficacement et sereinement.

:::

:::{Warning}

__Rappel__ : Les fichiers projet dans QGIS sont enregistrés séparément des données utilisées dans le projet. Il est donc recommandé de conserver tous les fichiers liés à un projet dans un même dossier.

:::