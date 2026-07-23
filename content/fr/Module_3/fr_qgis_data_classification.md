::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Classification des données géographiques <a id="geodata-classification"></a>

La classification des données spatiales dans un SIG consiste à catégoriser l’information géographique en groupes ou classes distincts sur la base de caractéristiques ou d’attributs communs. Chaque classe peut se voir attribuer un symbole ou une couleur distincte. Ce processus améliore l’organisation et l’interprétation des données spatiales.

Les attributs des données géographiques sont stockés dans une colonne spécifique de la table attributaire. En pratique, nous choisissons une colonne contenant les caractéristiques qui nous intéressent, ce qui permet à QGIS de regrouper les données à partir de ces attributs sélectionnés ({numref}`classification_basic`). 

:::{figure} /fig/classification_basic.drawio.png
---
width: 900px
name: classification_basic
align: center
---
Classification de base (Source : HeiGIT).
:::

## Échelles nominale, ordinale et métrique <a id="nominal-ordinal-and-metric-scales"></a>

Dans la classification des données géographiques, les échelles __nominale__, __ordinale__ et __métrique__ sont utilisées pour catégoriser et mesurer les entités spatiales selon différents niveaux de précision et de hiérarchie :

::::{margin}
:::{attention}

Le terme « échelles » utilisé ici ne fait pas référence au niveau de zoom ni au rapport entre les mesures dans le monde réel et leur représentation cartographique. Il renvoie aux relations entre les différentes valeurs des données. 

:::
::::

- L’__échelle nominale__ (données catégorielles) est la forme de mesure la plus simple, dans laquelle les entités sont regroupées en catégories distinctes sur la base d’attributs qualitatifs. Ces catégories n’ont pas d’ordre ni de hiérarchie intrinsèques. Elles n’ont pas de signification numérique : les valeurs ou les libellés sont simplement des noms ou des identifiants (dans certains cas, les classes d’occupation du sol peuvent être identifiées par des nombres).
    - Exemples : classes d’occupation du sol, types de végétation, types de sols, type d’équipement (hôpital, église, école, etc.)

    :::{figure} /fig/nominal_scale_examples.png
    ---
    name: nominal_scale_example
    width: 600 px
    ---
    Exemples de données nominales et de leur représentation (Source : Dickmann (2018) Kartographie, Westermann).
    :::

- L’__échelle ordinale__ (données classées) consiste également à catégoriser les données, mais ici les catégories possèdent un ordre ou un rang significatif. En revanche, les intervalles entre les rangs ne sont pas nécessairement égaux ni connus. L’ordre de classement est important : les entités peuvent être classées du plus faible au plus élevé, mais l’écart réel entre les rangs n’est pas mesuré. Il est possible de comparer et de classer les données (par exemple, déterminer quelle entité est classée plus haut ou plus bas).
    - Exemples : aptitude des terres, hiérarchie du réseau routier, classes de taille de population, classes de vulnérabilité (par ex. pour des unités administratives)

    :::{figure} /fig/ordinal_scale_example.png
    ---
    name: ordinal_scale_example
    width: 600 px
    ---
    Exemples de données ordinales et de leur représentation (Source : Dickmann (2018) Kartographie, Westermann)
    :::

- L’__échelle métrique__ (données quantitatives) concerne des données qui possèdent à la fois un ordre et des écarts exacts entre les valeurs. Les données sont représentées par des valeurs numériques précises et les différences entre ces valeurs sont constantes sur toute l’échelle. Les données métriques peuvent être subdivisées en :
    - Échelle d’intervalle : données numériques où la différence entre les valeurs est significative, mais sans véritable zéro absolu (par ex. la température en degrés Celsius).
    - Échelle de rapport : données numériques pour lesquelles les différences et les rapports sont significatifs, avec un véritable zéro absolu (par ex. distance, surface).
    - Exemples : données d’altitude, distance, surface, données de population.

    :::{figure} /fig/interval_ratio_scale_example.png
    ---
    name: interval_scale_example
    width: 600 px
    ---
    Exemples de données métriques et de leur représentation (Source : Dickmann (2018) Kartographie, Westermann).
    :::

Selon le type d’échelle, vous utiliserez différentes méthodes de classification. Ci-dessous, nous allons passer en revue les différents types de classification disponibles dans QGIS, ainsi que les cas dans lesquels les utiliser. Nous aborderons également plusieurs situations que vous pourriez rencontrer dans votre pratique des SIG. 


## Classification à symbole unique <a id="single-symbol-classification"></a>

Par défaut, QGIS visualise toutes les couches avec le paramètre `Single symbol`. Cela signifie que toutes les entités d’une couche sont visualisées de la même manière. Dans ce mode, vous pouvez modifier de nombreux paramètres comme la couleur ou l’opacité, __mais vous ne pouvez pas classer les données en plusieurs groupes !__

La classification à symbole unique est utile lorsque vous disposez d’un jeu de données simple. Par exemple, vous chargez une couche polygonale contenant les limites administratives d’une région, ainsi qu’une couche ponctuelle contenant les principales villes. Dans ce cas, vous pouvez choisir une classification à symbole unique et ajuster le symbole pour chaque couche.

::::{dropdown} Comment faire : classification à symbole unique
:open: 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Single_symbol_video.mp4"></video>

__Pour ajuster le style d’une couche...__
1. Faites un clic droit sur votre couche.
2. Cliquez sur `Symbology`.
3. Vérifiez que le paramétrage de la couche est sur `Single Symbol`.
4. Sélectionnez la couleur de votre choix dans le menu déroulant. Pour davantage d’options de couleur, choisissez `Choose Color` dans le menu déroulant.
5. *Optionnel* : vous pouvez ajuster l’opacité/la transparence de la couche. Cela peut être très utile lorsque vous souhaitez afficher plusieurs couches qui se chevauchent.
6. *Optionnel* : vous pouvez ici définir le type d’unité. Cela est utile si vous souhaitez visualiser des points avec une certaine taille, par exemple.
7. *Optionnel* : vous trouverez ici rapidement des styles standard et des styles précédemment utilisés.
8. Cliquez sur `Apply` pour appliquer vos modifications.
9. Cliquez sur `OK` pour fermer la fenêtre.


:::{figure} /fig/Single_symbol_classify.png
---
width: 900px
name: Single_symbol_classify
align: center
---
Ajustement du style d’une couche.
:::
::::


## Classification catégorisée <a id="categorised-classification"></a>

La classification catégorisée dans QGIS regroupe les données spatiales en catégories distinctes sur la base d’attributs spécifiques. 

Cette classification organise les entités en catégories à partir de valeurs spécifiques de la table attributaire.
En attribuant un symbole à chaque catégorie, vous facilitez l’interprétation de l’information géospatiale sur votre carte et obtenez ainsi une lecture plus claire.

:::{figure} /fig/fr_simple_classification_example_map.png
---
name: fr_simple_classification_example_map
width: 750px
---
Niger – Carte des régions de Tillabéri et Tahoua montrant les établissements scolaires fermés ou endommagés entre 2019 et 2022 (Source : [REACH](https://repository.impact-initiatives.org/document/impact/e6174a66/REACH_NER_Map_Ecoles_fermees_mai2022_tillaberi_tahoua.pdf)).
:::

Sur la carte ci-dessus, les routes principales ont reçu un symbole unique. Les écoles ont été classées en deux catégories : école primaire et école secondaire. 


La classification catégorisée est généralement utilisée pour des données d’échelle __nominale__ et __ordinale__.

| Data Scale    | Definition                                    | Example                                       | Typical Data Format            |
|---------------|-----------------------------------------------|-----------------------------------------------|--------------------------------|
| Échelle nominale | Catégories sans ordre ni hiérarchie intrinsèques | Types d’occupation du sol, districts, zones de moyens d’existence | Texte ("Désert") ou entier (5) |
| Échelle ordinale | Catégories avec un ordre ou un rang significatif | Rang (par ex. faible, moyen)                  | Texte ("élevé") ou entier (5)   |

:::{figure} /fig/Categorized_district_map_SierraLeone.png
---
width: 750 px
name: Categorized_district_map_SierraLeone
align: center
---
Exemple de carte utilisant une classification catégorisée.
:::

:::{dropdown} Comment faire : classification catégorisée
:open:

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Classify_by_categorized.mp4"></video>

__Pour classer les données par catégories...__
1. Faites un clic droit sur votre couche.
2. Cliquez sur `Symbology`.
3. Cliquez sur `Categorized`.
4. Dans le menu déroulant `Value`, sélectionnez la colonne à partir de laquelle vous souhaitez catégoriser vos données.
5. Plus bas dans la fenêtre, cliquez sur `Classify`. Vous devriez maintenant voir toutes les valeurs ou tous les attributs uniques de la colonne sélectionnée dans `Value`. Pour ajouter ou supprimer des valeurs individuelles, utilisez les boutons `-` et `+`. 
6. *Optionnel* : dans le menu déroulant `Symbol`, vous pouvez choisir les couleurs et symboles à utiliser.
7. *Optionnel* : dans le menu déroulant `Color ramp`, vous pouvez définir la gamme de couleurs à utiliser.
8. *Optionnel* : vous pouvez ouvrir le panneau `Layer Rendering` en bas de la fenêtre. Vous pourrez y ajuster l’opacité/la transparence de la couche.
9. Cliquez sur `Apply` pour appliquer vos modifications.
10. Cliquez sur `OK` pour fermer la fenêtre.

:::

## Classification graduée <a id="graduated-classification"></a>

La classification graduée dans un SIG consiste à répartir les données spatiales en classes ou intervalles sur la base d’une progression de valeurs. Cette méthode est particulièrement utile pour visualiser des données quantitatives, car elle permet de différencier des niveaux d’intensité, de densité ou de magnitude sur un continuum, ce qui favorise une représentation nuancée des phénomènes géographiques. 

::::{card}

:::{figure} /fig/example_classification_hexagons.png
---
name: example_classification_hexagons
width: 750 px
---
REACH, Ukraine, carte de suivi des sites collectifs pour les personnes déplacées internes, sites actifs, juillet 2024 (Source : [Reach](https://repository.impact-initiatives.org/document/impact/192097a8/REACH_UKR_Map_CSM_SituationOverview_ActiveSites_JULY2024_ENG_A4-1.pdf)).
:::

Dans {numref}`example_classification_hexagons`, chaque cellule hexagonale contient une valeur correspondant au "nombre de sites par 150 km²", allant de 1 à 91. Les cellules ont été regroupées en 5 catégories, ce qui permet de distinguer facilement les différentes valeurs de chaque cellule. En limitant le nombre de classes, le lecteur peut lire et comprendre la carte plus rapidement. 

::::

La classification graduée est généralement utilisée pour des données quantitatives d’échelle __d’intervalle__ ou __de rapport__.

| Data Scale     | Definition                                         | Example                             | Typical Data Format                          |
|----------------|----------------------------------------------------|-------------------------------------|----------------------------------------------|
| Échelle d’intervalle | Intervalles égaux entre les valeurs, sans véritable zéro | Température (Celsius)               | Float (44.5 Degree)                          |
| Échelle de rapport   | Intervalles égaux avec un véritable zéro                | Population, longueur, nombre d’arbres | Integer (5 Trees) ou Float (12.5 km of Road) |

Pour classer des données quantitatives, il existe de nombreuses méthodes de définition des classes. Il n’existe pas une seule meilleure façon de choisir une méthode ni de décider du nombre de classes à utiliser. Tout dépend de ce que vous souhaitez montrer.

:::{tip} 
Un bon intervalle pour le nombre de classes est de __3 à 7__. N’utilisez pas plus de __9__ classes, car il devient alors difficile de distinguer les classes entre elles, ce qui rend la carte plus difficile à comprendre. 
:::

Prenons l’exemple ci-dessous. Vous voyez un histogramme de la population des districts. Cela signifie que nous disposons d’un jeu de données comportant des districts et le nombre d’habitants dans chacun d’eux. Rien qu’à partir de l’histogramme, nous pouvons formuler quelques constats généraux.

1. Il n’existe aucun district sans population ou avec une population nulle.
2. Il n’y a que quelques districts avec une très faible population.
3. Il semble qu’il existe trois grands groupes de districts.

:::{figure} /fig/Histogramm_example.drawio.svg
---
width: 900px 
align: center
name: Histogram_example.drawio
---
Histogramme des données de population. Source : [Axis Maps](https://www.axismaps.com/guide/data-classification).
:::

Cependant, si nous voulons montrer sur une carte quels districts ont une population plus élevée que d’autres, nous devons classer les districts.

Il existe __sept__ façons dans QGIS de répartir des données quantitatives en classes. Les quatre plus importantes sont : __Intervalles égaux__, __Quantiles__, __Seuils naturels__, __Manuel__. Regardons à quoi ressembleraient les classes de population des districts si nous répartissions les données en trois classes en utilisant ces méthodes.


:::{figure} /fig/classification_method_map.drawio.svg
---
width: 900px
align: center
name: classification_method_map
---
Différentes classifications. Source : HeiGIT (adapté de [Axis Maps](https://www.axismaps.com/guide/data-classification)).
:::



::::{tab-set}

:::{tab-item} Intervalles égaux
La classification par intervalles égaux divise les données en classes de taille uniforme, par exemple 0–10, 10–20, 20–30, etc. Elle est efficace pour des données réparties de manière homogène sur toute l’étendue des valeurs. Toutefois, il faut être prudent lorsque les données sont asymétriques ou présentent des valeurs extrêmes importantes, car cela peut conduire à des classes vides. Les données de population utilisées ici, qui ne présentent pas de grandes valeurs extrêmes, conviennent bien à cette méthode.
:::

:::{tab-item} Effectif égal (quantile)
La classification par quantiles garantit un nombre égal d’observations dans chaque classe, ce qui produit des cartes visuellement équilibrées. Toutefois, elle peut entraîner des classes dont les intervalles numériques sont très différents ; dans certains cas, des valeurs similaires peuvent être séparées tandis que des valeurs différentes sont regroupées ensemble. Il est conseillé d’utiliser un histogramme pour évaluer les éventuels problèmes. Dans l’exemple de population par district, la classification par quantiles a produit une rupture discutable, en intégrant une partie du troisième groupe dans la classe 2 alors que ces observations étaient numériquement plus proches de celles de la classe 3.
:::

:::{tab-item} Seuils naturels
La méthode des seuils naturels est une méthode de classification optimale qui vise à minimiser la variance à l’intérieur des classes et à maximiser les différences entre les classes pour un nombre donné de classes. Toutefois, elle produit une solution de classification propre à chaque jeu de données, ce qui peut être un inconvénient lorsqu’on souhaite comparer plusieurs cartes, par exemple dans une série ou un atlas. Dans ce type de cas, un schéma de classification cohérent appliqué à toutes les cartes peut être préférable.
:::

:::{tab-item} Manuel
La classification manuelle permet à l’utilisateur de définir un ou plusieurs seuils de classe en fonction de besoins spécifiques. Cette approche est utile lorsqu’il est nécessaire de fixer à l’avance certains seuils, par exemple pour les aligner sur la moyenne ou pour maintenir la cohérence dans une série de cartes. La classification manuelle est recommandée lorsque d’autres méthodes fournissent une bonne solution mais pourraient bénéficier de légers ajustements pour mieux répondre à des besoins particuliers ou à certaines méthodes de visualisation.
:::

:::{tab-item} Échelle logarithmique
La classification en échelle logarithmique est utilisée lorsque les données couvrent plusieurs ordres de grandeur et qu’une échelle linéaire ne représente pas efficacement les variations. Cette échelle applique une transformation logarithmique aux données, en compressant les grandes valeurs tout en étendant les petites. Elle est utile pour visualiser des données présentant une croissance ou une décroissance exponentielle. Toutefois, l’interprétation des valeurs sur une échelle logarithmique peut nécessiter une compréhension plus fine. Envisagez cette méthode lorsqu’il existe une très large plage de valeurs et qu’une échelle linéaire masquerait des structures ou tendances importantes.
:::

:::{tab-item} Seuils arrondis
La méthode des seuils arrondis est conçue pour produire des cartes visuellement agréables et faciles à interpréter. Elle cherche à générer des seuils de classes correspondant à des nombres « ronds », ce qui rend la carte plus intuitive pour le lecteur. Cette méthode est particulièrement utile lorsqu’on communique des données spatiales complexes à un large public, car elle améliore la clarté et la lisibilité de la carte. Gardez à l’esprit que le choix de seuils « esthétiques » peut dépendre du contexte spécifique et des préférences du public visé.
:::

:::{tab-item} Écart-type
La classification par écart-type est une méthode qui détermine les seuils de classes à partir de l’écart-type des valeurs des données. Cette approche organise les données en classes en tenant compte de la distribution des valeurs autour de la moyenne. Chaque classe représente un certain nombre d’écarts-types par rapport à la moyenne, fournissant ainsi une base statistique pour catégoriser les données. Cette méthode est efficace lorsqu’on souhaite mettre en évidence la variabilité à l’intérieur du jeu de données. Toutefois, il est important de prendre en compte la nature de la distribution des données et de vérifier si cette méthode correspond bien aux objectifs analytiques de la carte.
:::

::::


::::{dropdown} Comment faire : classification graduée dans QGIS
:open:

La mise en place d’une classification graduée dans QGIS est similaire à celle d’une classification catégorisée. Toutefois, contrairement à la classification catégorisée, vous devez ici décider du nombre de classes et de la méthode de graduation à utiliser. 

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/graduated_classification.mp4"></video>

__Pour classer les données en classes...__
1. Faites un clic droit sur votre couche.
2. Cliquez sur `Symbology`.
3. Cliquez sur `Graduated`.
4. Dans le menu déroulant `Value`, sélectionnez la colonne selon laquelle vous souhaitez classer vos données.
5. En bas à droite, sélectionnez le nombre de classes que vous souhaitez utiliser.
6. Sous `Mode`, sélectionnez la méthode de classification que vous souhaitez utiliser, par exemple Equal count (Quantile).
7. Cliquez sur `Classify`. Vous devriez maintenant voir toutes les classes et la distribution des valeurs. Pour ajouter ou supprimer des classes, utilisez les boutons `-` et `+`. 
8. *Optionnel* : cliquez sur `Histogram` → `Load Values`. Vous pouvez alors visualiser la distribution exacte des valeurs dans les différentes classes. Cela est très pratique pour choisir une méthode de classification. Vous pouvez également consulter la moyenne et l’écart-type.

:::{figure} /fig/Graduated_histogram.png
---
width: 900px
name: Graduated_histogram
align: center
---
Classification graduée. Source : [Axis Maps](https://www.axismaps.com/guide/data-classification).
:::

9. *Optionnel* : dans le menu déroulant `Symbol`, vous pouvez choisir les couleurs et les symboles à utiliser.
10. *Optionnel* : dans le menu déroulant `Color ramp`, vous pouvez définir la gamme de couleurs à utiliser. Pour voir toutes les rampes de couleurs, cliquez sur la flèche du `Color ramp` → `All Color Ramps`.
11. *Optionnel* : sous `Legend Format`, vous pouvez ajuster le niveau de précision avec lequel les intervalles de classes seront affichés dans la légende. En général, il est préférable d’éviter d’utiliser des nombres trop complexes dans la légende.
12. *Optionnel* : vous pouvez ouvrir le panneau `Layer Rendering` en bas de la fenêtre. Vous pourrez y ajuster l’opacité/la transparence de la couche.
13. Cliquez sur `Apply` pour appliquer vos modifications.
14. Cliquez sur `OK` pour fermer la fenêtre.

:::{figure} /fig/classification_graduated_basic.png
---
width: 900px
name: classification_graduated_basic
align: center
---
Classification graduée dans QGIS 3.36.
:::
::::

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Vérifiez vos connaissances
:class: note

1. __Qu’est-ce que la classification des données géographiques, et pourquoi est-elle utile dans un SIG ?__

:::{dropdown} Réponse
- La classification des données géographiques est le processus qui consiste à regrouper ou catégoriser des entités géographiques selon des valeurs attributaires communes (ou des intervalles de valeurs), puis à attribuer à chaque classe son propre symbole ou sa propre couleur.
- Elle permet de visualiser des structures, de rendre les cartes plus lisibles, de distinguer les différences dans les données et de communiquer plus clairement les variations spatiales, en particulier pour des attributs quantitatifs ou catégoriels.
:::

2. __Quelles sont les trois méthodes de classification les plus courantes dans QGIS ? Expliquez leurs différences.__

:::{dropdown} Réponse
QGIS prend en charge les trois modes de classification courants suivants :

| Method            | Use case / data type                                               | How it works / difference                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Single symbol** | Pour des jeux de données simples ou lorsque vous souhaitez que toutes les entités aient le même aspect | Toutes les entités reçoivent le même symbole (couleur, taille). Aucune différenciation par attribut.                                                                                                                                                                |
| **Categorised**   | Pour des données **nominales** ou **ordinales** (catégorielles)                  | Les entités sont regroupées selon les valeurs attributaires uniques (catégories). Chaque catégorie reçoit son propre symbole.                                                                                                                                                     |
| **Graduated**     | Pour des données **quantitatives / métriques**                                 | Les valeurs numériques sont réparties en classes numériques (intervalles). Chaque classe reçoit une symbologie différente, souvent par rampe de couleur. Vous choisissez le nombre de classes et la méthode de classification (par ex. intervalles égaux, quantiles, seuils naturels). |



:::

3. __Citez trois méthodes différentes pour répartir des données quantitatives en classes. Quelles sont leurs différences ?__

:::{dropdown} Réponse
| Method                     | Description / how breaks are determined                                                                                    | Strengths & drawbacks                                                                                                                 |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Equal Interval**         | Divise l’étendue complète des données en intervalles de taille égale (par ex. en divisant [min, max] en n intervalles de même largeur)              | Méthode simple et intuitive, mais elle peut produire de nombreuses classes vides ou très peu remplies si les données sont asymétriques ou comportent des valeurs extrêmes.          |
| **Quantile (Equal Count)** | Chaque classe contient approximativement le même nombre d’entités                                        | Offre un bon équilibre visuel, mais les intervalles numériques des classes peuvent être très différents, et des valeurs proches peuvent être séparées entre différentes classes.             |
| **Natural Breaks (Jenks)** | Utilise un algorithme pour minimiser la variance à l’intérieur des classes et maximiser les différences entre classes (c’est-à-dire trouver des regroupements « naturels ») | Produit souvent des seuils visuellement pertinents et bien adaptés à la distribution des données. En revanche, les seuils dépendent du jeu de données, ce qui complique les comparaisons entre cartes. |


:::

4. __Quels sont les compromis ou les difficultés liés au choix du nombre de classes dans une classification graduée ?__

:::{dropdown} Réponse
- Plus il y a de classes, plus le niveau de détail est élevé, mais trop de classes rendent la carte confuse, car il devient difficile de distinguer les couleurs ou les nuances subtiles. Le module recommande de rester entre 3 et 7 classes, et de ne pas dépasser 9.
- Si le nombre de classes est trop faible, vous risquez de trop simplifier les données et de masquer des variations importantes ou des valeurs extrêmes.
- Si le nombre de classes est trop élevé, la carte devient chargée, les couleurs trop proches les unes des autres, et l’interprétation devient plus difficile.
- La distribution des données est également importante : des données très asymétriques ou avec des valeurs extrêmes peuvent fausser les intervalles de classes, de sorte que la majorité des entités se retrouve concentrée dans quelques classes, tandis que d’autres restent presque vides.
- Pour des cartes comparatives (par ex. une série de cartes), utiliser des seuils différents pour chaque carte parce que les données diffèrent peut réduire la comparabilité ; des seuils fixes améliorent la cohérence mais ne sont pas toujours adaptés à la distribution spécifique de chaque jeu de données.
:::

::::
