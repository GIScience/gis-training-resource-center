::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Gestion des données géographiques <a id="geodata-management"></a>

Dans ce chapitre, nous allons examiner plus en détail comment stocker les données géographiques sur votre ordinateur afin de travailler dans QGIS ou dans d’autres applications SIG. Comme les données vectorielles constituent le principal type de données géographiques avec lequel vous travaillerez au début de votre parcours en SIG, nous nous concentrerons sur les données vectorielles. Nous verrons comment mettre en place une arborescence de dossiers cohérente pour vos données et vos projets SIG, ainsi que comment nommer correctement les fichiers de données géographiques.

## Principes fondamentaux de la gestion des données géographiques <a id="fundamentals-of-geodata-management"></a>

Travailler avec des données géographiques n’est pas la même chose que travailler avec des données dans des logiciels comme Microsoft Excel ou Word. Par exemple, lorsque vous insérez une image dans un document Word, le fichier contient cette image. Si vous supprimez l’image sur votre ordinateur, le document Word conservera malgré tout une copie de l’image.

Ce n’est pas le cas dans QGIS. Lorsque vous chargez des données géographiques dans QGIS, le logiciel établit uniquement un lien vers l’emplacement où les données sont stockées sur votre ordinateur. Cela signifie que votre projet QGIS __ne contient pas__ les données géographiques : il ne fait qu’y faire référence. Si vous chargez des données dans votre projet QGIS puis que vous modifiez leur emplacement ou que vous les supprimez, ces données ne seront plus disponibles dans le projet et vous obtiendrez une erreur lors de son ouverture.

Comme vous travaillez directement avec les données source, et non avec une copie, toute modification apportée aux données dans QGIS remplace les données source et ne peut pas être annulée. Si vous prévoyez de modifier vos données, il est donc recommandé d’en faire d’abord une copie, afin de toujours disposer d’une version « propre » à laquelle revenir.

### Arborescence de dossiers standard <a id="standard-folder-structure"></a>

La pratique la plus importante en matière de gestion des données géographiques consiste à utiliser une arborescence de dossiers standardisée qui regroupe tous les éléments du projet QGIS.

Les chemins entre un projet QGIS et les données géographiques sont, par défaut, relatifs. Cela signifie que lorsque les données et le projet sont organisés selon une structure de dossiers fixe, vous pouvez déplacer l’ensemble de cette structure sans affecter le projet QGIS ni les chemins vers les données. La version de l’arborescence de dossiers standardisée utilisée dans tous les exercices de cette formation est expliquée ci-dessous. Un modèle de cette structure peut être téléchargé [__ici__](https://nexus.heigit.org/repository/gis-training-resource-center/Templates/GIS_project_folder_template.zip).

Une arborescence de dossiers standard présente deux avantages principaux :

1. Si nous partageons l’ensemble du dossier de projet, nous pouvons nous attendre à ce que le projet fonctionne sans problème sur un autre ordinateur.
2. Cette structure favorise une bonne organisation des données du projet et contribue à garantir le bon fonctionnement du projet QGIS.

:::{figure} /fig/standard_folder_structure_new_2025.drawio.png
---
width: 600px
align: center
name: standard_folder_structure_new_2025
---
Arborescence de dossiers standard. Source : HeiGIT
:::

### Nommer les données géographiques <a id="naming-geodata"></a>

Nommer correctement vos données permet d’identifier facilement les couches et d’éviter les problèmes liés au traitement des fichiers sur votre ordinateur. Les noms de fichiers doivent être explicites, de sorte que vous ou d’autres personnes puissiez identifier ce que représentent les données, leur provenance et la période à laquelle elles se rapportent. Dans QGIS, vous devez nommer vos couches de manière à pouvoir identifier à la fois leur contenu et les traitements effectués. Par exemple, si vous avez découpé une couche de rues de New York, ne nommez pas la couche "clipped", mais plutôt quelque chose comme "streets_NYC_clipped".

Voici quelques principes de base pour nommer les données géographiques que vous produisez ou manipulez :

* N’utilisez pas de caractères spéciaux comme `!`, `?`, `/` ou `-`.
* N’utilisez pas d’espaces ; utilisez des underscores `_`.
* Donnez aux couches des noms explicites afin de pouvoir comprendre ce qu’elles représentent, même lorsqu’il s’agit d’étapes intermédiaires ou temporaires dans une chaîne de traitement.

Ci-dessous, vous voyez un exemple de chaîne de traitement appliquée à un jeu de données de limites administratives (`adm0`). L’objectif des étapes intermédiaires n’est pas clair, car les noms de couches ne sont pas explicites.

`adm0 >> adm0_temp >> adm0_temp2 >> adm0_temp3 >> facilities_final`

Un bon système de nommage des couches est illustré ci-dessous. Dans cet exemple, il est clair quel traitement a été réalisé à chaque étape (reprojection, découpage, jointure avec une autre couche, résultat final).  
De cette manière, d’autres personnes peuvent comprendre le rôle des différentes couches et savoir si elles sont nécessaires dans le projet final.

`adm0 >> adm0_projUTM >> adm0_projUTM_clipUrban >> adm0_projUTM_clipUrban_intersectFacilities >> facilities_processed`

### Documentation <a id="documentation"></a>

La documentation est une étape importante lorsque l’on travaille avec des données géographiques ou que l’on réalise des analyses. Elle garantit la clarté, la reproductibilité et facilite la collaboration. L’analyse de données spatiales implique souvent des processus complexes, du nettoyage de données, des transformations et l’utilisation de sources spécifiques. Sans documentation appropriée, il devient difficile, pour vous comme pour d’autres, de comprendre, reproduire ou prolonger votre travail. La documentation permet d’organiser l’objectif, les méthodes ou outils utilisés, les données d’entrée et de sortie, ainsi que les hypothèses et les limites. De manière générale, une bonne documentation permet aux praticien·ne·s SIG de reproduire les étapes d’analyse et d’obtenir exactement le même résultat. Dans un travail collaboratif, elle sert de feuille de route et est essentielle dans les projets SIG. Dans le secteur humanitaire et dans les processus de prise de décision, une bonne documentation est indispensable car elle permet d’éclairer les décisions et d’aider les équipes humanitaires à allouer les ressources.

Vous pouvez documenter vos projets à l’aide d’éditeurs Markdown ou simplement en créant un document Word. Veillez à l’enregistrer dans le sous-dossier de documentation de votre dossier de projet. Il n’existe pas de règles fixes pour rédiger une documentation, mais suivre une structure logique facilite à la fois l’écriture et la lecture. Il est également conseillé de rédiger la documentation au fur et à mesure de l’analyse. QGIS offre de nombreuses options et paramètres pendant les traitements, et il est facile d’oublier ceux qui ont été utilisés à une étape donnée.

1. __Vue d’ensemble du projet :__
   - Indiquez le titre et l’objectif du projet.
   - Ajoutez un bref résumé de l’analyse.
2. __Sources de données :__
   - Liste de tous les jeux de données d’entrée (avec des liens si possible)
   - Système de coordonnées utilisé
   - Notes sur la qualité des données ou leurs limites
3. __Logiciels et outils :__
   - Version de QGIS
   - Extensions utilisées
4. __Flux de travail et méthodologie :__
   - Processus étape par étape, avec des captures d’écran ou des schémas si nécessaire
   - Décrivez chaque étape de traitement (éventuellement sous forme de liste à puces)
   - Mentionnez les paramètres clés ou les décisions prises

Veillez à ce que vous-même et d’autres personnes puissiez comprendre et reproduire les étapes de l’analyse. Une bonne documentation transforme votre projet QGIS d’une boîte noire en un travail transparent, partageable et professionnel.


## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

Prenez un moment pour vérifier ce que vous avez appris dans ce chapitre en répondant aux questions ci-dessous :

1. __Où sont enregistrées les couches chargées dans un projet QGIS ? Quelles en sont les implications lorsqu’on déplace ou renomme des fichiers ?__

:::{dropdown} Réponse
- Les couches chargées dans un projet QGIS ne sont pas intégrées dans le fichier projet `.qgz` : elles y sont liées via des chemins vers les fichiers de données source.
- Cela signifie que si vous déplacez, renommez ou supprimez un fichier source après l’avoir ajouté au projet, QGIS ne pourra plus le retrouver, et la couche apparaîtra comme manquante ou cassée.
- Pour éviter cela, il faut maintenir une arborescence de dossiers cohérente et éviter de modifier l’emplacement des fichiers une fois le projet mis en place, ou mettre à jour les chemins si nécessaire.
:::

2. __Lorsqu’on modifie des données géographiques dans QGIS, pourquoi est-il recommandé d’en faire une copie au préalable ?__

:::{dropdown} Réponse
- Parce que QGIS modifie directement le fichier de données d’origine et qu’il n’existe pas de sauvegarde automatique intégrée une fois les changements enregistrés.
- Si vous faites une erreur pendant l’édition, il n’est pas facile de revenir en arrière.
- Créer une copie du jeu de données avant modification permet de conserver les données d’origine et d’avoir une solution de repli en cas de problème.
:::

3. __Quels sont les deux principaux avantages d’une arborescence de dossiers standardisée pour les projets SIG et les données ?__

:::{dropdown} Réponse
1. __Portabilité :__ si l’ensemble du dossier du projet (y compris les sous-dossiers de données) est déplacé vers un autre ordinateur ou un autre disque, le projet QGIS pourra toujours retrouver ses données tant que des chemins relatifs sont utilisés.
2. __Organisation et cohérence :__ une structure claire et homogène permet d’éviter les fichiers égarés, rend le projet plus facile à parcourir et permet à d’autres personnes de comprendre et d’utiliser plus facilement votre projet.
:::

4. __Décrivez au moins trois bonnes pratiques pour nommer des données géographiques / des couches.__

:::{dropdown} Réponse
1. Éviter les caractères spéciaux et les espaces dans les noms de fichiers ; utiliser des underscores `_` à la place (par ex. `land_cover_2020.shp`).
2. Utiliser des noms explicites qui indiquent le contenu de la couche (par ex. `population_density_europe` plutôt que simplement `data1`).
3. Indiquer dans le nom les traitements effectués si la couche a été modifiée (par ex. `rivers_clipped`, `buildings_buffered_500m`) afin de rendre le flux de travail transparent et reproductible.
:::

5. __Si vous déplacez l’ensemble du dossier de projet (avec ses sous-dossiers et ses données) vers un autre ordinateur, dans quelles conditions le projet QGIS continuera-t-il à fonctionner sans chemins cassés ?__

:::{dropdown} Réponse
- Le projet continuera à fonctionner si :
   - tous les fichiers utilisés dans le projet __se trouvent à l’intérieur du dossier de projet__ ;
   - vous n’utilisez pas d’extensions ou de ressources indisponibles sur l’autre ordinateur.
- Si certains fichiers ont été chargés via des chemins absolus (par ex. depuis un emplacement extérieur au dossier de projet), ces chemins risquent de ne plus fonctionner après le déplacement vers une autre machine.
:::

::::
