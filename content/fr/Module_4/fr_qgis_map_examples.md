::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Bon design de carte & Erreurs sémiologiques <a id="good-map-design-and-semiological-errors"></a>

Dans ce chapitre, nous aborderons les principes d’une conception cartographique réussie et présenterons des exemples permettant de reproduire certains éléments graphiques dans QGIS. Une deuxième partie sera consacrée aux erreurs sémiologiques courantes. Pour consulter d’autres exemples de bonnes pratiques en matière de conception cartographique, vous pouvez visiter les sites web et dépôts suivants :

- [impact-initiatives.org/resource-centre maps](https://www.impact-initiatives.org/resource-centre/?category%5B%5D=information_products&category%5B%5D=data_methods&type%5B%5D=281&order=latest&limit=10)
- [geo.msf.org maps](https://geo.msf.org/catalogue/DOCID-1877329211-4979?from=0&sort=_score&desc=true)
- [reliefweb.int maps](https://reliefweb.int/updates?list=Maps%20/%20Infographics&view=maps)

## Exemples de cartes <a id="map-examples"></a>

### Exemple de carte 1 : Zones et routes affectées par les inondations dans la région somalienne, Ethiopie <a id="map-example-1-flood-affected-areas-and-roads-in-the-somali-region-ethiopia"></a>

:::{figure} ../../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: Flood affected Areas in Somali
width: 800 px
---
Zones et routes touchées par les inondations dans la région Somali, en Éthiopie (source : OCHA)
:::

:::{dropdown} Contexte : Situation en Éthiopie

La Grande Corne de l’Afrique reçoit entre 20 et 70 % de ses précipitations annuelles totales entre octobre et décembre. La FICR signale une probabilité prévisionnelle exceptionnellement élevée, supérieure à 80 %, de précipitations au-dessus de la normale. En outre, les conditions El Niño se sont installées entre juillet et août, augmentant davantage la probabilité de fortes précipitations en Éthiopie.

Depuis octobre, les inondations ont touché au moins 763 000 personnes dans la région, causé 33 décès dans la seule région Somali et entraîné la mort de 4 806 têtes de bétail. Elles ont également provoqué d’importants dégâts aux infrastructures, aux transports et aux établissements scolaires. Les moyens de subsistance et la santé de la population ont été gravement affectés.  
L’impact des inondations devrait s’intensifier au cours des prochaines années, ce qui entraînera une augmentation des crues soudaines et des crues fluviales.

Les cartes d’accessibilité, comme celle présentée ci-dessus, jouent un rôle essentiel en aidant les gestionnaires de l’information et le personnel sur le terrain à déterminer quelles zones sont accessibles. Cela est particulièrement important lors des inondations, car le déploiement rapide des opérations de secours ou d’aide est essentiel.

(Source: [IFRC](https://go.ifrc.org/emergencies/6773/details))
:::

La carte ci-dessus montre les zones touchées par les inondations ainsi que les principaux réseaux routiers de la région Somali, en Éthiopie, en novembre 2023. De telles cartes sont essentielles pour les acteurs de l’aide humanitaire lorsqu’ils planifient des opérations de secours ou d’assistance et doivent être tenues à jour. Elles indiquent les principales localités et, surtout, l’accessibilité des routes et des pistes d’atterrissage.

Il s’agit d’une carte thématique ayant un objectif clair et ne présentant que les éléments essentiels à cet objectif.

- Un remplissage hachuré a été appliqué au fichier Shapefile des zones touchées par les inondations. Cette symbologie est disponible dans QGIS.
- Une couche représentant le réseau routier a été placée au-dessus de celle des zones touchées par les inondations. La symbologie des routes a été __catégorisée__ en trois catégories : routes accessibles (vert), routes partiellement accessibles (gris) et routes difficiles d’accès (rouge).
- La couche supérieure est une couche de points contenant des informations sur les routes ou les ponts impraticables, ainsi que sur l’emplacement des pistes d’atterrissage et leur accessibilité. Les points ont été représentés à l’aide de symboles SVG.
- (Les frontières administratives de l’Éthiopie sont séparées des pays voisins en faisant du polygone un blanc clair et des pays voisins dans une nuance de gris. Cela peut être réalisé en copiant le polygone de l’Éthiopie dans une nouvelle couche et en modifiant la symbologie.

:::{note}
La gamme de couleurs utilisée pour les routes permet une lecture intuitive de la carte, car le rouge est généralement associé à des caractéristiques négatives et le vert à des caractéristiques positives. Il convient toutefois de noter que les personnes daltoniennes peuvent avoir des difficultés à lire la carte.
:::

---

### Exemple de carte 2: Risque d'inondation dans la région d'Ouham, République centrafricaine <a id="map-example-2-flooding-risk-in-the-ouham-region-central-african-republic"></a>

:::{figure} ../../../fig/REACH_CAF_Susceptibilite_inondations_CF32_Juillet2023_A3_FR.png
---
name: REACH Flooding Risk Ouhman Region, Central African Republic
width: 720 px
---
Risque d'inondation dans la région de Ouham, République centrafricaine (Source : REACH).
:::

:::{dropdown} Contexte : Situation en République centrafricaine

La République centrafricaine a été frappée par des inondations destructrices à la fin de 2019, qui ont déplacé plus de 100 000 personnes et causé des dommages considérables aux infrastructures. Les inondations ont détruit des abris, entravé les voies de transport et ont entraîné des épidémies comme le choléra et le paludisme. En raison du changement climatique, ces inondations deviendront plus fréquentes, ce qui entraînera une vulnérabilité accrue pour les villes et les villages. Comme les dangers naturels sont difficiles à prédire, l’évolution du climat réduit la résilience des communautés.

Source: [REACH Initiative](https://reliefweb.int/report/central-african-republic/central-african-republic-flood-susceptibility-risk)
:::

Cette carte représente le risque d’inondation à l’aide d’une image raster. Les données raster ont été calculées à partir de plusieurs facteurs, notamment l’intensité des précipitations, leur durée maximale, la hauteur par rapport au réseau de drainage le plus proche, la direction de l’écoulement et le réseau hydrographique, l’humidité topographique, un modèle numérique d’élévation et la couverture du sol.

- Les données raster sont affichées à l’aide d’un dégradé de couleurs divergent. (Vous pouvez voir ici comment attribuer un dégradé de couleurs.).
- Les districts administratifs environnants ont été recouverts d'un gris transparent.
- Le réseau fluvial a été ajouté en bleu.
- Les routes principales ont également été ajoutées en noir.
- Les colonies sont affichées sous forme de points noirs, ce qui permet d'identifier les zones présentant une densité de population plus élevée dans les zones les plus à risque.

---


## Erreurs communes dans la sémiologie <a id="common-missteps-in-semiology"></a>


### Le problème des unités spatiales modifiables <a id="the-modifiable-areal-unit-problem"></a>

:::{caution}
Soyez prudent lorsque vous représentez des données par régions administratives.
:::

Le problème des unités spatiales modifiables (MAUP) est un biais statistique qui apparaît lorsque des données spatiales sont agrégées par régions. Il montre que les résultats d’une analyse spatiale peuvent varier selon la manière dont les données sont regroupées en unités surfaciques (zones spatiales).

Le problème des unités spatiales modifiables comporte deux composantes principales :

__Effet d'échelle :__

L'échelle de l'agrégation (petites ou grandes zones) affecte les résultats.

- Lorsque des unités plus petites, telles que des îlots de recensement, sont utilisées, l’analyse peut faire ressortir des variations locales détaillées.
- Lorsque des unités plus grandes, telles que des comtés ou des États, sont utilisées, les variations locales sont atténuées et les résultats peuvent faire apparaître des tendances plus générales. Par exemple, le revenu moyen peut varier considérablement à l’échelle des quartiers, mais paraître plus uniforme à l’échelle du comté.

__Effet de zonage :__

La forme et la disposition des zones utilisées pour l’agrégation peuvent également influencer les résultats.

- La modification des limites des zones, par exemple en divisant une ville selon un axe est-ouest plutôt que nord-sud, peut conduire à des résultats différents, même si la population totale ou les données restent identiques. Cela s’explique par le fait que les limites influencent la manière dont les valeurs sont moyennées ou additionnées.

__Pourquoi est-ce important dans les SIG ?__

- Décisions politiques : si l’analyse repose sur des limites arbitraires, les décisions, par exemple l’allocation des ressources, risquent de se fonder sur des résultats trompeurs.
- Statistiques spatiales : les corrélations, les régressions et d’autres analyses portant sur des données spatiales peuvent être biaisées en raison du MAUP.

:::{figure} ../../../fig/en_modifiable_areal_unit_problem_diagram.png
---
name: en_modifiable_areal_unit_problem_diagram
width: 500 px
---
Visualisation du problème des unités spatiales modifiables : le même indicateur représenté à trois échelles différentes (Source : Kitchin, Rob & Lauriault, Tracey & McArdle, Gavin. (2015). Knowing and governing cities through urban indicators, city benchmarking and real-time dashboards. Regional Studies, Regional Science. 2. 6-28. 10.1080/21681376.2014.983149.).
:::

### Cercles proportionnels vs. Couleurs solides <a id="proportional-circles-vs-solid-colours"></a>

:::{caution}
Soyez prudent lorsque vous représentez des données __quantitatives__ avec une couleur __solide__.
:::

Bien qu'il soit graphiquement attrayant, la représentation de données quantitatives avec des couleurs solides peut entraîner des problèmes et distraire du message de la carte :

- Vous perdez la relation d'ordre __entre les données__ (un cercle peut être deux fois plus grand qu'un autre, une couleur ne peut pas être "deux fois plus sombre").
- Les pays ayant une grande surface se distinguent visuellement (par exemple la Russie dans l'exemple ci-dessous).
- Nous essayons de représenter des données __qui n'ont rien à voir avec la zone d'un pays__.


<!---Add example-->

### Gradient de couleur vs. Palette de couleurs distincte <a id="colour-gradient-vs-distinct-colour-palette"></a>

:::{caution}
NE PAS utiliser une palette de couleurs __séparée__ pour représenter __entités ordonnées__.
:::

Une représentation qui « se sent bien » parce qu'il semble logique qu'un taux « faible » soit représenté différemment d'un taux « élevé ».

C'est une erreur parce que:

- En utilisant une variable de couleur différenciante, __vous perdez la relation ordinale entre les entités__. Au lieu de cela, un dégradé __de la même couleur__ qui devrait être utilisé.
- Différentes couleurs sont utilisées pour différencier les entités distinctes.

### Dégradé en une seule couleur vs. dégradé entre deux couleurs <a id="gradient-in-a-single-colour-vs-gradient-between-two-colours"></a>

:::{Caution}
Soyez prudent lorsque vous utilisez un dégradé __sur deux couleurs différentes__ pour des données __toujours positives__ (ou négatives).
:::

C'est difficile parce que nos cerveaux sont utilisés pour donner la priorité à certaines couleurs, en particulier du vert au rouge, ou du bleu au rouge. Nous devons nous rappeler que __si nos valeurs n'ont pas de point zéro__, Il serait peut-être préférable de rester dans la même couleur et d'utiliser des nuances différentes de cette couleur pour indiquer des valeurs différentes. Alternativement, un dégradé de couleur qui ne diverge pas peut être utilisé.


Un gradient divergeant entre deux couleurs peut être utilisé quand il est nécessaire de montrer une gradation qui peut aller du négatif au positif. Quant aux températures, il est logique de distinguer les valeurs négatives (en nuances de bleu par exemple) et les valeurs positives (en nuances de rouge).

C'est une erreur parce que:

- En choisissant différentes couleurs pour des valeurs qui sont liées entre elles, nos yeux perçoivent une différence entre les éléments, et non pas un ordre.
- Les couleurs plus foncées se distinguent plus que des couleurs plus légères, et peuvent être perçues comme plus importantes.
- La carte enverra un message de divergence, d'opposition entre certaines valeurs, alors que nous essayons simplement de représenter une hiérarchie entre les valeurs.
- De cette façon, la couleur elle-même indique directement des informations sur la tendance (positif/négatif ou croissant/diminution).

### Symboles géométriques limités par rapport aux icônes et symboles complexes <a id="limited-geometric-symbols-vs-complex-icons-and-symbols"></a>

:::{Caution}
NE PAS utiliser __trop de symboles__ sur une carte thématique.
:::

Intégrer une multitude de symboles (et de données) afin de créer une carte informative est une aspiration courante. Cependant, un trop grand nombre de symboles peut __surcharger la carte__ et __réduire sa lisibilité__. L’utilisation excessive de symboles, en particulier de formes géométriques, peut rendre la carte difficile à lire et à comprendre.  
__L’œil peut facilement distinguer entre quatre et cinq symboles différents.__ Au-delà, il devient difficile de différencier les éléments. Il s’agit toutefois d’une erreur moins grave, car elle ne transmet pas de fausses informations sur la carte.

C'est une erreur parce que:

- Il complique la carte et limite son impact.
- Parfois, vous êtes forcé de représenter plusieurs symboles, donc vous devez faire attention au chevauchement des points et à la surcharge de la carte.


---

## Questions d'auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

1. __Qu’est-ce qui rend une carte « bonne » ou efficace ? Avec vos propres mots, énumérez au moins trois qualités ou principes illustrés par les exemples de cartes.__

:::{dropdown} Réponse
1. __Clarté/lisibilité en un coup d'œil__
    - Une bonne carte permet au spectateur de comprendre immédiatement le message clé ou la distribution sans avoir à déchiffrer une symbologie trop complexe. Par exemple, les cartes d'exemple utilisent des schémas de couleurs propres (ou des distractions minimales) de sorte que le motif spatial se démarque.
2. __Arborescence visuelle appropriée et concentrez__
    - Cela signifie mettre l'accent sur le thème principal ou les données de la carte, tout en déplaçant les couches de fond ou de contexte de façon à ce qu'elles ne soient pas en compétition. Par exemple, les caractéristiques de contexte (routes, limites, basemap) sont souvent légères, subtiles ou grisées, tandis que les couches thématiques sont audacieuses. Un des exemples de cartes montre comment les couches subsidiaires sont soumises, de sorte que les données principales apparaissent dans les pages principales.
3. __Adaptation à l’objectif et au public, ainsi que choix de conception efficaces__
    - Une bonne carte aligne son design (couleurs, symboles, étiquetage, orientation) sur le public visé et le but (communication opérationnelle, humanitaire, scientifique). Par exemple, en utilisant des couleurs intuitives (p. ex. rouge pour risque élevé, vert pour sécurité) ou icônes simplifiées pour les publics non techniques. Le module montre implicitement différents types d'exemples de cartes adaptés à l'utilisation humanitaire, à la prise de décision opérationnelle, etc.
:::

2. __Prenez en compte le public cible et l’usage prévu de l’un des exemples de cartes (p. ex. action humanitaire, opérations ou communication destinée au grand public). Comment les choix de conception reflètent-ils ce public (p. ex. simplicité, clarté, choix des symboles) ?__

:::{dropdown} Réponse
Les choix de conception devraient refléter ceci:
- __Simplicité et clarté__: La carte évite les caractéristiques trop détaillées ou décoratives ; il se concentre sur l'essentiel : la zone touchée, les zones / routes sûres, les centres de secours dans le contexte d'une carte de réponse aux inondations.
- __Utilisation d'icônes intuitives__: Par exemple, une icône de refuge, ou un triangle pour le danger, les flèches pour le mouvement — facilement compréhensible sans avoir besoin d'un regard de légende profonde.
- __Haut contraste et couleurs de meaningule__: Par exemple, rouge/orange pour les zones dangereuses, vert pour les zones sûres ou défrichées, éventuellement un gris neutre pour le contexte. Cela aide les utilisateurs non techniques à interpréter rapidement ce qui est urgent.
- __Distractions minimales__: L'arrière-plan peut être soumis, routes/frontières muets, pour faire ressortir la couche opérationnelle. Aussi de grandes polices lisibles pour les titres/étiquettes parce que peut-être vu dans le champ.
- __Éléments cartographiques clairs et mise en page adaptée à une consultation rapide__ : grand titre (p. ex. « Zones de dégâts dus aux inondations – 24 oct. 2025 »), légende bien visible, barre d’échelle, flèche du nord et, éventuellement, carte de localisation pour faciliter l’orientation.
Ainsi, les choix de conception reflètent le public cible en privilégiant la lisibilité, l’immédiateté et une interprétation intuitive plutôt que l’élégance cartographique ou un niveau de détail approfondi.
:::


::::

