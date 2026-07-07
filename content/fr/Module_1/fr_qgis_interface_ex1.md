::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../content/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Exercice 1 : Comprendre l'interface QGIS <a id="exercise-1-understanding-the-qgis-interface"></a>

## Objectif de l'exercice <a id="aim-of-the-exercise"></a>

QGIS est un logiciel complexe offrant de nombreuses fonctionnalit?s, et son interface peut sembler d?routante, en particulier pour les d?butant?e?s. Cet exercice vous permettra de vous familiariser avec les principales barres d?outils, fen?tres et panneaux dans QGIS. Vous allez cr?er un nouveau projet QGIS, l?enregistrer, puis explorer les diff?rents panneaux et barres d?outils.

L'exercice couvre :

- L?enregistrement et l?ouverture d?un projet QGIS
- L?identification et l?utilisation des diff?rentes barres d?outils
- L?identification et l?utilisation des diff?rents panneaux
- Le d?placement des panneaux
- L?activation de nouveaux panneaux


## Articles wiki associ?s<a id="related-wiki-articles"></a>

- [Interface QGIS](/content/Wiki/en_qgis_interface_wiki)
- [Projets et structure de dossier](/content/Wiki/en_qgis_projects_folder_structure_wiki)


## Pr?paration des donn?es <a id="data-preparation"></a>

Dans cet exercice, nous n?utiliserons pas de donn?es g?ographiques. Nous allons plut?t apprendre ? naviguer dans les diff?rentes interfaces et ? enregistrer et ouvrir un projet QGIS. Vous pouvez t?l?charger la structure de dossiers mod?le compress?e[ici](https://nexus.heigit.org/repository/gis-training-resource-center/Modul_1/Modul_1_Exercise_1_Understanding_the_interface/Modul_1_Exercise_1_Understanding_the_interface.zip).

```{figure} /fig/standard_folder_structure_new_2025.drawio.png
---
width: 800px
align: center
name: Standard folder structure
---
Standard folder structure. Source: HeiGIT.
```
---

## T?ches <a id="tasks"></a>

1. Cr?ez un nouveau projet. Lorsque vous ouvrez QGIS, l??cran de d?marrage appara?t et affiche l?interface sans projet charg?. ? gauche, vous trouverez un panneau affichant les projets r?cents (probablement vide si vous d?butez). ? droite, un panneau d?actualit?s pr?sente des publications du blog QGIS, et en dessous se trouve le panneau `Project Templates`.

```{figure} /fig/en_project_template_BRC.png
---
height: 400
name: en_project_template_BRC
---
```

- Dans le panneau `Project Templates` , __double-cliquez sur l'option `New Empty Project`__ (ce devrait ?tre le seul mod?le visible). Vous verrez une toile vierge dans l'interface principale car il n'y a pas encore de donn?es.

2. D?couvrez l'interface QGIS : Au-dessus de la toile, vous trouverez la barre d'outils ____ avec de nombreuses fonctions diff?rentes. ? gauche et ? droite de la toile, vous trouverez les panneaux. Dans QGIS, vous acc?derez principalement aux outils en les trouvant dans les barres d'outils ____ ou __panneaux__.

- Les barres d?outils se situent par d?faut en haut de l??cran. Elles regroupent les commandes permettant d?interagir avec l?interface.
- Les panneaux se trouvent par d?faut sur les c?t?s de l??cran. Ils incluent notamment le navigateur de fichiers et le panneau des couches ? gauche. D?autres panneaux peuvent ?tre activ?s pour rechercher et utiliser des outils de traitement. Dans le panneau des couches, vous verrez appara?tre les donn?es que nous ajouterons ult?rieurement.
? droite de l??cran, vous trouverez tr?s probablement le panneau __Bo?te ? outils de traitements__. S?il n?appara?t pas, consultez cette [page wiki](../content/Wiki/en_qgis_common_errors_and_Issues#missing-toolbox).

```{figure} /fig/en_QGIS_GUI.png
---
width: 800px
align: center
name: QGIS User Interface
---
QGIS User Interface.
```

3. Vous pouvez d?tacher un panneau de son emplacement en cliquant sur son titre et en le faisant glisser. Vous pouvez soit l?ancrer ? un autre panneau (il appara?tra alors sous forme d?onglet), soit le transformer en fen?tre ind?pendante. Vous pouvez ?galement redimensionner les panneaux. Essayez par exemple de d?placer le panneau des couches vers la droite ([Vid?o Wiki](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_interface_wiki.html#move-and-arrange-toolbars)).

:::{tip}

Dans QGIS, l?interface peut appara?tre l?g?rement diff?rente selon la r?solution de votre ?cran. Il arrive que certains ?l?ments soient masqu?s en raison des param?tres d?affichage par d?faut. Si cela se produit, essayez de redimensionner les panneaux et d?explorer les diff?rentes options et fonctionnalit?s disponibles. Cela vous permettra d?acc?der facilement ? tous les outils essentiels pendant votre travail.

:::

4. QGIS propose d?autres panneaux qui ne sont pas affich?s par d?faut. Voyons comment les localiser et les activer.
- Dans le menu `View`, recherchez les options `Panels` et `Toolbars`. En passant la souris sur chacune d?elles, une liste des panneaux et barres d?outils disponibles appara?t, ainsi que leur ?tat (activ? ou non). Prenez un moment pour parcourir les diff?rentes options. Il existe de nombreuses possibilit?s, mais ne vous inqui?tez pas : vous n?en utiliserez qu?une partie dans cette formation. Les panneaux que nous utiliserons le plus souvent sont :
- Navigateur
- Couches
- Style de couche
- Bo?te ? outils de traitement

5. Observons maintenant les barres d?outils. Celles que nous utiliserons le plus souvent sont :
- Barre d'outils d'attributs
- Barre d'outils de num?risation
- Barre d?outils Navigation cartographique
- Barre d'outils du projet
- Barre d'outils de s?lection


Prenez le temps de vous familiariser avec les diff?rentes fa?ons d?organiser l?interface QGIS. Savoir o? trouver les diff?rentes fonctionnalit?s vous fera gagner beaucoup de temps et vous ?vitera des frustrations ? l?avenir.

6. Enregistrons maintenant le projet. Cliquez sur l?ic?ne d?enregistrement dans la barre d?outils ou ouvrez le menu `Project`puis choisissez`Save As...`.
    1. Choisissez un emplacement pour le fichier projet. L?endroit id?al est le sous-dossier du projet dans la structure de dossiers mod?le. Acc?dez au dossier nomm?`Module_1_Exercise_1`. Donnez un nom ? votre projet QGIS (par exemple : `QGIS_Training_Exercise_1`). Le projet sera enregistr? sous forme de fichier `.qqz`.
    2. Cliquez sur `Save`
    3. Fermez l'application QGIS et rouvrez-la.
7.  Lorsque QGIS red?marre, le projet que vous venez d?enregistrer appara?t dans le panneau `Recent Projects`. Vous pouvez double-cliquer dessus pour l?ouvrir. Vous pouvez ?galement acc?der au fichier `.qgz` via votre explorateur de fichiers et double-cliquer dessus.
Cela lancera ?galement QGIS et chargera le projet.

:::{Tip}

Maintenir une arborescence de dossiers organis?e contribue grandement ? travailler efficacement et sereinement.

:::

:::{Warning}

__Rappel__: Les fichiers projet dans QGIS sont enregistr?s s?par?ment des donn?es utilis?es dans le projet. Il est donc recommand? de conserver tous les fichiers li?s ? un projet dans un m?me dossier.

:::


