::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Sélection et requêtes de données géographiques <a id="geodata-selection-and-queries"></a>

La sélection et les requêtes de données géographiques dans QGIS permettent de cibler des parties spécifiques de jeux de données géospatiaux. Cela peut être utilisé pour filtrer et analyser des informations géographiques, ce qui constitue une tâche essentielle lors du travail avec des données spatiales.
\
\
Trois types généraux de sélection/requêtes dans QGIS couvrent la majorité des besoins :\
**1. Sélection manuelle :** sélection des entités en les choisissant manuellement à l’aide des différents outils de sélection proposés par QGIS. 

**2. Sélection basée sur les attributs :** sélection basée sur les valeurs d’attributs stockées dans la table attributaire.

**3. Sélection spatiale basée sur une couche :** sélection d’entités dans une couche en fonction de relations géométriques spécifiques avec des entités d’une autre couche.


::::{admonition} À vous de jouer !

L’interrogation des données est essentielle pour comprendre et manipuler vos jeux de données. Vous pouvez suivre les étapes ci-dessous en téléchargeant [ce jeu de données](https://datacatalog.worldbank.org/search/dataset/0038272/World-Bank-Official-Boundaries).

:::{card}
:class-card: sd-text-justify sd-rounded-3 sd-border-2
:link: https://nexus.heigit.org/repository/gis-training-resource-center/Module_3/Module_3_world_bank_official_boundaries.zip

__Télécharger les limites officielles de la Banque mondiale__

:::

::::

## Sélection manuelle <a id="manual-selection"></a>

La sélection manuelle se fait principalement à l’aide des outils de sélection basés sur le clic disponibles dans la barre d’outils du projet (alternative : `Edit` → `Select`). Ceux-ci incluent `Select Feature(s)`, `Select Feature by Polygon`, `Select Feature by Freehand` et `Select Feature by Radius`.
\
\
Exemple : `Select Feature(s)`

1.	Cliquez sur `Select Feature(s)` dans le menu déroulant de ![](/fig/mActionSelectRectangle.png).
2.	Sélectionnez les entités en cliquant dessus ou en dessinant un rectangle qui les recouvre.
3.	Utilisez l’outil en dehors des entités sélectionnables pour terminer la sélection.

:::{Tip}
Maintenir la touche "Shift" enfoncée lors de la sélection permet de sélectionner plusieurs entités.
:::

:::{dropdown} Exemple : sélectionner manuellement des polygones de pays par clic
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_features_by_click_wiki.mp4"></video>

:::

Les autres options de ![](/fig/mActionSelectRectangle.png) fonctionnent de manière similaire, en sélectionnant toutes les entités qui intersectent la géométrie dessinée avec l’outil.

1. Cliquez sur `Select Feature(s) by Polygon` dans le menu déroulant de ![](/fig/mActionSelectRectangle.png).
2. Sélectionnez les entités en cliquant avec le bouton gauche autour des entités que vous souhaitez sélectionner.
3. Faites un clic droit lorsque vous avez terminé de dessiner le polygone. 

:::{dropdown} Exemple : sélectionner manuellement des pays en dessinant un polygone
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_select_features_by_polygon.mp4"></video>

:::

:::{Note}
Les entités sélectionnées sont surlignées en jaune vif dans la vue cartographique et en bleu dans la table attributaire.
:::

## Sélection basée sur les attributs <a id="attribute-based-selection"></a>

Une requête basée sur des attributs spécifiques peut être réalisée à l’aide de l’outil `Select Features by Expression`, disponible via ![](/fig/mActionSelectbyExpression.png) dans la barre d’outils du projet ainsi que dans la table attributaire (alternative : `Edit` → `Select` → `Select Features by Expression`).

1.	Dans l’interface de l’outil, développez `Fields and Values` dans le panneau de droite.
2.	Choisissez le champ sur lequel baser votre sélection en double-cliquant dessus (il apparaît alors dans le panneau d’expression à gauche).
3.	Utilisez une expression avec des opérateurs spécifiques pour définir votre sélection dans le panneau de gauche (par ex. `"continent"  LIKE  'Asia'` pour sélectionner toutes les entités ayant la valeur “Asia” dans le champ "continent").


:::{Tip}
Cliquez sur `Show Values` en haut à droite lorsqu’un champ est sélectionné pour obtenir un aperçu des différentes valeurs du champ via `All Unique` / `10 Samples`. Double-cliquez sur les valeurs pour les utiliser dans le panneau d’expression.
:::

::::{tab-set}

:::{tab-item} Opérateurs de comparaison
| opérateur | fonctionnalité            |
|----------|--------------------------|
| __=__    | égal à                   |
| __!=__   | différent de             |
| __<__    | inférieur à              |
| __>__    | supérieur à              |
| __<=__   | inférieur ou égal à      |
| __>=__   | supérieur ou égal à      |
:::

:::{tab-item} Opérateurs logiques
Des opérateurs tels que AND, OR peuvent être utilisés pour combiner différentes requêtes ou critères.
| opérateur | fonctionnalité          |
|----------|------------------------|
| __AND__  | ET logique             |
| __OR__   | OU logique             |
| __NOT__  | NON logique            |
:::

:::{tab-item} Opérateurs spéciaux
| opérateur      | fonctionnalité                                  |
|---------------|------------------------------------------------|
| __LIKE__      | correspondance de motif                        |
| __IN__        | vérifie si une valeur est dans une liste       |
| __IS NULL__   | vérifie les valeurs nulles                     |
| __BETWEEN__   | vérifie si une valeur est dans un intervalle   |
| __CASE WHEN__ | expressions conditionnelles                    |
:::

::::

:::{dropdown} Exemple : sélectionner tous les polygones de pays ayant la valeur `Asia` dans le champ "continent"
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_expression_like_wiki.mp4"></video>
:::

## Sélection spatiale basée sur une couche <a id="layer-based-spatial-selection"></a>

La sélection spatiale permet de sélectionner des entités d’une couche en fonction de leur relation avec des entités d’une autre couche géospatiale (par ex. sélectionner tous les points d’une couche A situés à l’intérieur d’un polygone d’une couche B). Elle peut être réalisée à l’aide de l’outil “Select by Location” disponible via ![](/fig/mActionSelectbyLocation.png) dans la barre d’outils du projet (alternative : `Vector` → `Research Tools` → `Select by Location`).

1.	Dans l’interface de l’outil, choisissez la couche à partir de laquelle vous souhaitez sélectionner des entités via `Select features from` et la couche de référence via `By comparing to the features from`.
2.	Choisissez l’opérateur géométrique qui sera utilisé pour la sélection (voir paragraphe ci-dessous).
3.	Dans la section inférieure, choisissez comment traiter la nouvelle sélection :
    1.	Créer une nouvelle sélection.
    2.	Ajouter à la sélection actuelle.
    3.	Sélectionner à l’intérieur de la sélection actuelle.
    4.	Supprimer de la sélection actuelle.

Les entités sélectionnées sont à nouveau surlignées en jaune vif dans l’interface cartographique.

:::{dropdown} Exemple : sélectionner les villes (points) qui intersectent le polygone "China"
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_intersect_wiki.mp4"></video>
:::

:::{dropdown} Exemple 2 : sélectionner tous les polygones de pays qui touchent le polygone "China"
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_select_by_location_touch_wiki.mp4"></video>
:::

### Opérateurs géométriques <a id="geometric-operators"></a>

Les opérateurs géométriques définissent les conditions de relation entre la couche source et la couche cible sur lesquelles la sélection est basée. Il existe huit options principales :

| Opération   | Description                                                                                       | Exemple                                                                         |
|-------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Intersect   | Les entités de la couche cible sont sélectionnées si elles intersectent des entités de la couche source. | Sélectionner toutes les routes qui traversent un polygone représentant un parc national. |
| Contain     | Les entités de la couche cible sont sélectionnées si elles contiennent entièrement des entités de la couche source. | Sélectionner un pays qui contient entièrement des polygones de villes. |
| Disjoint    | Les entités sont disjointes si elles ne partagent aucun point ou surface commun.                 | Sélectionner des districts administratifs sans frontière commune.       |
| Equal       | Les entités sont égales si leurs géométries sont identiques.                                     | Sélectionner deux segments de ligne avec les mêmes coordonnées.             |
| Touch       | Les entités de la couche cible sont sélectionnées si elles touchent celles de la couche source.  | Sélectionner des parcs qui touchent une route spécifique.                                    |
| Overlap     | Les entités de la couche cible sont sélectionnées si elles partagent une surface commune avec la couche source. | Sélectionner des parcelles qui chevauchent une zone de construction.        |
| Are within  | Les entités de la couche cible sont sélectionnées si elles sont entièrement à l’intérieur de celles de la couche source. | Sélectionner des bâtiments situés entièrement dans une ville. |
| Cross       | Les entités de la couche cible sont sélectionnées si elles croisent celles de la couche source. | Sélectionner des rivières qui traversent une route.                                           |

<!--ADD examples relevant to IM? -->

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

1. __Quels sont les trois types généraux de sélection ou de requêtes dans QGIS ? Donnez une brève description de chacun.__

:::{dropdown} Réponse
- __Sélection manuelle__ :  
    Vous sélectionnez des entités à l’aide de la souris avec l’outil `Select Features` dans la carte ou en cliquant sur les lignes dans la table attributaire. Dans la carte, les entités sélectionnées apparaissent en jaune, dans la table attributaire en bleu.  
- __Requêtes basées sur les attributs__ (Select by Attribute ou Select by Expression) :  
    Vous construisez une requête pour sélectionner des entités selon des valeurs spécifiques (par ex. `"population" > 10000 AND "type" = 'urban'`).  
- __Requêtes spatiales__ (Select by Location) :  
    Vous sélectionnez des entités en fonction de leur relation spatiale avec celles d’une autre couche (intersection, contact, disjonction, etc.).
:::

2. __Citez au moins quatre opérateurs géométriques utilisés dans les requêtes spatiales et expliquez leur fonctionnement.__

:::{dropdown} Réponse

| Opérateur     | Signification / comportement                                                                 |
|---------------|----------------------------------------------------------------------------------------------|
| **Intersect** | Sélectionne les entités qui partagent une partie commune avec une autre couche               |
| **Within**    | Sélectionne les entités entièrement à l’intérieur d’une autre                                |
| **Contains**  | Sélectionne les entités qui contiennent entièrement d’autres entités                         |
| **Touches**   | Sélectionne les entités qui partagent une frontière ou un point sans chevauchement interne   |
| **Crosses**   | Sélectionne les entités qui se croisent                                                      |
| **Overlaps**  | Sélectionne les entités qui se chevauchent partiellement                                     |

Exemples : 
- Pour sélectionner les routes traversant un parc, utilisez Intersect ou Crosses  
- Pour sélectionner les bâtiments entièrement dans une zone inondable, utilisez Within  

::::

[def]: /fig/mActionSelectRectangle.png
