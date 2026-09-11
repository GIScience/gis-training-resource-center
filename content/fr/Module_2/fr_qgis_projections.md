::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Projections <a id="projections"></a>

## Introduction <a id="introduction"></a>

<iframe width="800" height="500" src="https://www.youtube.com/embed/kIID5FDi2JQ?si=C0tYz7nteMF_xqvr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Un enjeu important lors de la création d’une carte d’une région est qu’il est impossible de représenter une sphère sur un plan 2D sans déformer la carte. La transformation d’un objet 3D sur une surface plane peut être réalisée à l’aide d’une __projection__. Au fil des siècles, les cartographes et les mathématiciens ont développé une multitude de méthodes différentes pour projeter la Terre sur une surface plane ({numref}`en_examples_projections_IBIS`). Cependant, il n’est jamais possible de représenter correctement le monde sur une surface plane (voir la vidéo ci-dessus). Toute projection déforme soit la distance entre deux points, soit les angles entre deux lignes (directions), soit la superficie d’une zone. Une projection ne peut représenter correctement qu’une seule de ces trois dimensions. Cela signifie que, selon la méthode de projection utilisée, votre carte du monde ne représentera pas correctement les tailles, les angles ou les distances.

:::{figure} /fig/en_examples_projections_IBIS.png
---
width: 700px
align: center
name: en_examples_projections_IBIS
---
Exemples de projections (Source : inconnue. Cette figure est incluse à des fins d’illustration uniquement et n’est pas soumise à la licence Creative Commons de cette plateforme).
:::

Chaque projection a son cas d’usage. Par exemple, la projection de Mercator représente correctement les angles entre deux points. Elle a été largement utilisée à l’époque de la navigation maritime sans satellites, car les navires pouvaient rejoindre leur destination en suivant une ligne droite sur la carte. Ainsi, la projection de Mercator représente correctement les intersections routières : une route qui en croise une autre à angle droit apparaîtra bien comme telle dans une projection de Mercator. C’est particulièrement utile pour la navigation. La forme d’une surface reste correcte, puisque les angles entre les lignes sont conservés. En revanche, lorsque l’on augmente l’échelle de la carte, les tailles et les distances deviennent fortement déformées (voir la figure ci-dessous). De plus, plus on s’éloigne de l’équateur, plus la déformation augmente.

:::{note} La taille réelle de
La projection de Mercator est célèbre pour la déformation qu’elle introduit dans la taille relative des pays. Vous pouvez comparer la taille réelle de différents pays selon leur position sur la carte sur le site [TheTrueSize.com](https://www.thetruesize.com). Un exemple classique est celui du Groenland comparé à l’Afrique, qui semblent avoir une taille similaire sur la carte, alors qu’en réalité l’Afrique est beaucoup plus vaste.
:::

:::{figure} /fig/en_greenland_africa.png
---
width: 600px
align: center
name: en_greenland_africa
---
Comparaison Groenland - Afrique (Source : [The True Size of](https://www.thetruesize.com/#?borders=1~!MTYwODM1MTk.MzkyNDUyNg*MjY5NjM4Mzg(MTA1MjgyOTE~!CONTIGUOUS_US*MTAwMjQwNzU.MjUwMjM1MTc(MTc1)MQ~!IN*NTI2NDA1MQ.Nzg2MzQyMQ)MA~!CN*OTkyMTY5Nw.NzMxNDcwNQ(MjI1)Mg)).
:::

## Comment choisir un système de coordonnées projeté approprié <a id="how-to-choose-an-appropriate-projected-coordinate-system"></a>

En SIG, nous projetons la Terre sur un système de coordonnées plan (d’où le nom de système de coordonnées de référence, ou SCR). Il est essentiel d’avoir à l’esprit que vos données peuvent être dans un SCR et votre projet QGIS dans un autre.

Le SCR du projet est affiché en bas à droite de l’[interface QGIS](https://giscience.github.io/gis-training-resource-center/content/fr/Module_1/fr_qgis_start.html#overview-of-qgis-interface). Vous y voyez le code EPSG. EPSG signifie European Petroleum Survey Group et fait référence à un système normalisé de codes pour les systèmes de coordonnées de référence (SCR) et les projections. Chaque code EPSG (par ex. EPSG:4326 pour WGS84) identifie de manière unique un SCR spécifique, ce qui garantit la cohérence et l’interopérabilité des données géospatiales sur différentes plateformes et applications.

- __Codes EPSG :__ il s’agit d’identifiants numériques attribués par la base de données EPSG à des systèmes de coordonnées de référence spécifiques, ce qui les rend concis et sans ambiguïté (par ex. EPSG:4326 pour WGS84). Ils offrent une manière normalisée de référencer les SCR dans les différentes applications SIG.
- __Noms de SCR :__ il s’agit généralement de noms descriptifs de systèmes de coordonnées de référence (par ex. "WGS 84" ou "NAD83"). Bien qu’ils donnent des indications sur le système utilisé, ils ne sont pas toujours uniques ni universellement reconnus, ce qui peut entraîner des confusions en l’absence du code EPSG correspondant.

Pour modifier le SCR de vos données et de votre projet, suivez les étapes expliquées ci-dessous. Le SCR/code EPSG par défaut de tout projet QGIS est le World Geodetic System 84
(EPSG:4326). Ce SCR est optimisé pour les cartes mondiales et n’est donc pas idéal pour la plupart des applications humanitaires, car nous avons besoin de projections spécifiques à une région, qui minimisent les déformations à l’échelle que nous souhaitons représenter.

:::{Tip}
Choisissez la projection en fonction de votre zone d’intérêt. Il existe des SCR spécifiques créés pour réduire la déformation et les imprécisions des projections dans différentes régions du monde. Vous pouvez trouver toutes les projections et leurs codes SCR sur [epsg.io](http://epsg.io).
:::

Observez les images suivantes et prêtez attention à la manière dont les différents systèmes de coordonnées de référence modifient et déforment la carte du monde.

:::{figure} /fig/world_mercator_tissots.png
---
width: 500 px
name: world_mercator_tissot
---
La projection de Mercator (EPSG:54004) (Source : HeiGIT).
:::

Remarquez que la forme du cercle reste identique. On peut donc en conclure que les angles restent inchangés. En revanche, les cercles deviennent plus grands à mesure qu’ils s’éloignent de l’équateur, et la distance entre eux change également lorsqu’ils s’en éloignent. Nous pouvons donc conclure que les distances et les surfaces sont déformées avec la projection de Mercator. La force de cette projection est qu’elle conserve les angles entre deux lignes. Nous le voyons au fait que les cercles restent parfaitement circulaires, même loin de l’équateur.

:::{figure} /fig/WGS_84_tissots.png
---
name: WGS_84_tissots
width: 500 px
---
Le World Geodetic System 1984 (EPSG:4326) (Source : HeiGIT).
:::

Le WGS 84 est un SCR constitué d’un ellipsoïde qui ressemble étroitement à la forme de la Terre. Au lieu d’utiliser des unités métriques, il utilise des degrés angulaires (latitude et longitude). La forme des cercles de Tissot n’est pas déformée près de l’équateur, mais elle s’allonge selon l’axe est-ouest à mesure que l’on s’éloigne de l’équateur. Contrairement à la projection de Mercator, il n’y a pas de déformation dans la direction nord-sud. Comme les cercles se déforment, nous pouvons en déduire que ce SCR déforme les angles.

:::{figure} /fig/World_equidistant_cylindrical_tissots.png
---
name: World_equidistant_cylindrical_tissots
width: 500 px
---
La projection cylindrique équidistante mondiale (EPSG:54002) (Source : HeiGIT).
:::

Le SCR cylindrique équidistant mondial conserve les distances (sans déformation de longueur) le long de n’importe quel méridien (lignes de longitude, du nord au sud), ainsi que le long des deux parallèles standards. La forme, l’échelle et la surface se déforment à mesure que l’on s’éloigne des parallèles standards.

Ce tableau donne un aperçu des projections à utiliser selon la propriété recherchée :

| Characteristic | Mercator (cylindrical) | Lambert cylindrical | Albers conic |
| :------------- | :--------------------: | :-----------------: | :----------: |
| Shape          |           ✅           |         ❌          |      ✅      |
| Rotation       |           ✅           |         ✅          |      ❌      |
| Area           |           ❌           |         ✅          |      ✅      |

Un autre point très important dans le choix du système de coordonnées de référence est que, selon l’ellipsoïde et la méthode de projection utilisée, un même point peut se trouver à des emplacements différents (voir {numref}`wrong_CRS`). Dans la figure ci-dessous, le même point est encodé dans 3 systèmes de référence différents.

:::{figure} /fig/wrong_CRS.png
---
name: wrong_CRS
width: 750 px
---
Le même point dans trois systèmes de référence différents (Source : HeiGIT).
:::

### Systèmes de coordonnées de référence métriques et géographiques <a id="metric-and-geographic-coordinate-reference-systems"></a>

Il existe deux types de systèmes de coordonnées de référence : les SCR __géographiques__ et les SCR __métriques__.

- Un SCR géographique repose sur un modèle tridimensionnel ellipsoïdal de la Terre. Il utilise des mesures angulaires (__latitude et longitude__) pour définir des positions à la surface terrestre. Les coordonnées sont généralement exprimées en degrés (par ex. 45°N, 120°W).
   - __Avantages :__ comme il repose sur la courbure terrestre, il permet de représenter des localisations n’importe où sur le globe. La plupart des jeux de données mondiaux, des systèmes GPS et des systèmes de cartographie utilisent un SCR géographique, ce qui le rend très compatible avec de nombreuses sources de données. Les localisations peuvent être exprimées avec précision à l’aide de mesures angulaires.
   - __Inconvénient :__ comme il utilise des mesures angulaires, les distances, les surfaces et les formes peuvent être fortement __déformées__. La distance entre les parallèles et les méridiens variant, la conversion des angles en mètres n’est pas constante.
- Un SCR métrique est une représentation en 2D de la surface terrestre. Même s’il est difficile de représenter de vastes portions du globe sur une surface plane sans déformation, il est possible de créer une projection 2D d’une région limitée avec une déformation minimale. Les unités cartographiques sont généralement les mètres ou les pieds. Ce type de SCR est obtenu en projetant la Terre sur un plan.
   - __Avantages :__ comme il repose sur un plan, il permet de calculer avec précision les distances, les surfaces et les angles.
   - __Inconvénients :__ un SCR projeté donné est généralement optimisé pour une région précise. Son utilisation en dehors de cette zone entraîne souvent des déformations importantes en distance, en surface et en forme.

:::{figure} /fig/Problem_distance_geographic_coords.png
---
name: problem_distance_geographic_coords
width: 600 px
---
Représentation géographique du globe. La distance entre les méridiens converge vers les pôles nord et sud (Source : HeiGIT).
:::

:::{caution}

Lors du traitement des données géographiques, QGIS utilise toujours les unités de mesure de la couche en cours de traitement. Cela signifie que si vous souhaitez calculer, par exemple, une distance en kilomètres, la couche doit être dans un SCR métrique. Vous pouvez vérifier les unités de mesure d’une couche donnée en faisant un <kbd>clic droit</kbd> sur la couche dans le panneau des couches → `Properties` → `Information` → `Coordinate Reference System (CRS)`.

:::

### SCR locaux et globaux <a id="local-and-global-crs"></a>

:::{figure} /fig/en_local_crs.png
---
width: 800px
name: en_local_crs
align: center
---
Systèmes de coordonnées de référence (SCR) locaux et globaux (Source : British Red Cross).
:::

Comme vous pouvez le constater, les petites régions apparaissent déformées dans un SCR global. Pour des zones de petite taille, il convient d’utiliser des projections locales, car elles offrent un affichage plus précis. En revanche, les projections locales déforment fortement la carte à l’échelle mondiale.

### Comment vérifier et modifier le système de coordonnées de référence du projet <a id="how-to-check-and-change-the-project-coordinate-reference-system"></a>

:::{admonition} À vous de jouer !
:class: note

Comprendre les projections et les systèmes de coordonnées de référence n’est pas simple. Les étapes suivantes peuvent être suivies avec n’importe quelle couche de données géographiques dans votre projet QGIS.

:::

:::{Note}
L’une des premières choses à faire lors de la création d’un nouveau projet QGIS est de vérifier et d’ajuster le SCR/code EPSG en fonction de la région ou de la zone sur laquelle vous travaillez. Si vous réalisez une carte montrant l’ensemble du globe, une projection globale telle que la projection de Mercator doit être utilisée. Si vous travaillez sur une zone plus restreinte, comme un continent, un pays ou une région encore plus petite, __vous devez toujours utiliser un SCR local afin d’éviter les imprécisions__. Si vous ne savez pas quel SCR utiliser, vous pouvez rechercher un système approprié sur EPSG.IO. Saisissez simplement le nom de votre région et consultez les options proposées. Assurez-vous que le SCR choisi utilise la bonne unité de mesure (mètres, pieds ou degrés).
:::

1. Ouvrez un projet QGIS.
2. Tout en bas à droite de QGIS, vous trouvez le bouton `EPSG`. Le numéro affiché à côté correspond au code EPSG actuellement utilisé dans le projet. Pour afficher davantage d’informations ou modifier le SCR, cliquez sur le bouton `Current CRS` ![](/fig/EPSG_Code.png).
3. La fenêtre `Project Properties` s’ouvre. Vous pouvez y consulter tous les SCR/codes EPSG disponibles ainsi que leurs propriétés.
4. Pour modifier le SCR/code EPSG, sélectionnez celui que vous souhaitez utiliser puis cliquez sur `Apply`.

:::{dropdown} Vidéo : comment vérifier et modifier le SCR dans votre projet QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_change_project_CRS.mp4"></video>

:::

### SCR du projet et SCR des couches <a id="project-crs-and-layer-crs"></a>

Le système de coordonnées de référence de votre projet QGIS détermine la manière dont QGIS affiche les informations. Toutefois, les couches et les jeux de données possèdent leur propre SCR. Celui-ci peut être consulté dans les métadonnées ou dans les propriétés de la couche. Le SCR de la couche correspond au système de coordonnées des entités ou objets contenus dans le jeu de données. Les mêmes coordonnées dans deux systèmes de coordonnées de référence différents ne renvoient pas au même emplacement sur Terre, en raison des déformations de distance et de surface.

:::{note}
La première chose à faire lorsque vous chargez une nouvelle couche ou un nouveau jeu de données dans votre projet QGIS est de vérifier le système de coordonnées de référence du jeu de données et de le reprojeter si nécessaire vers le SCR du projet. Vous garantissez ainsi la cohérence de votre projet et le bon positionnement des objets géographiques dans la couche. Dans le cas contraire, vous produirez des résultats erronés.
:::

#### Modifier la projection d’une couche vectorielle <a id="changing-the-projection-of-a-vector-layer"></a>

1. Onglet `Vector` → `Data Management Tools` → `Reproject Layer`.
2. Sélectionnez le SCR/code EPSG cible.
3. Enregistrez le nouveau fichier en cliquant sur les trois points à côté de `Reprojected`, puis précisez le nom du fichier et l’emplacement où vous souhaitez l’enregistrer.
5. Cliquez sur `Run`.

:::{dropdown} Vidéo : comment modifier le SCR d’une couche vectorielle
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_vector.mp4"></video>
:::

#### Modifier la projection d’une couche raster <a id="changing-the-projection-of-a-raster-layer"></a>

1. Onglet `Raster` → `Projections` → `Warp (Reproject)`.
2. Sélectionnez le SCR/code EPSG cible.
3. Sélectionnez la méthode de rééchantillonnage.
4. Enregistrez le nouveau fichier en cliquant sur les trois points à côté de `Reprojected`, puis précisez le nom du fichier et l’emplacement où vous souhaitez l’enregistrer.
5. Cliquez sur `Run`.

:::{dropdown} Vidéo : comment modifier le SCR d’une couche raster
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_reproject_raster.mp4"></video>
:::

<!-- Move this part? At this point trainees have not worked with rasterdata--->

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

Prenez un moment pour vérifier ce que vous avez appris dans ce chapitre en répondant aux questions ci-dessous :

1. __Pourquoi une projection cartographique est-elle nécessaire lorsqu’on visualise la Terre en 2D ? Quelles déformations sont inévitables lorsqu’on projette une surface sphérique sur un plan ?__

:::{dropdown} Réponse
- Parce que la Terre (ou plus précisément l’ellipsoïde de référence) est une surface courbe tridimensionnelle, il est impossible de la représenter parfaitement sur une carte plane (2D) sans déformation. La projection consiste justement à transformer cette surface courbe en plan.
- Toute projection déforme nécessairement au moins l’un des éléments suivants : les angles (directions), les surfaces (tailles relatives) ou les distances (échelles). On peut préserver correctement une ou parfois deux propriétés, mais jamais toutes en même temps.
- Par exemple, la projection de Mercator conserve les angles (les formes sont donc localement correctes), ce qui est utile pour la navigation, mais elle déforme fortement les surfaces, surtout vers les pôles.
- Autre exemple : les projections équidistantes conservent les distances le long de certaines lignes (méridiens ou parallèles standards), mais déforment les formes ou les surfaces ailleurs.
:::

2. __Expliquez la différence entre un SCR géographique et un SCR projeté (ou métrique). Quels sont leurs avantages et leurs inconvénients ?__
:::{dropdown} Réponse
- Un SCR géographique (système de coordonnées de référence) repose sur un modèle ellipsoïdal (ou sphérique) de la Terre et exprime les positions en coordonnées angulaires (latitude, longitude), généralement en degrés.
   - Avantages : il reflète naturellement la courbure terrestre et fonctionne à l’échelle mondiale. De nombreux jeux de données mondiaux, systèmes GPS et cartes sont nativement en coordonnées géographiques, ce qui le rend très compatible.
   - Inconvénients : comme latitude et longitude sont des mesures angulaires, leur conversion en mesures linéaires (mètres, kilomètres) n’est pas uniforme. Les distances, surfaces et formes peuvent être déformées, surtout loin de l’équateur. On ne peut pas mesurer de manière fiable des distances euclidiennes ou des surfaces sans reprojeter d’abord les données.
- Un SCR projeté (ou métrique) transforme la surface terrestre (ou une partie de celle-ci) en un plan bidimensionnel, avec des unités linéaires (mètres, pieds, etc.). La projection "aplatit" la surface.
   - Avantages : comme les données sont dans un espace métrique plan, on peut calculer plus directement et avec moins de déformation les distances, surfaces et angles (dans l’emprise prévue par la projection). Il est donc mieux adapté à la plupart des analyses spatiales sur des zones limitées.
   - Inconvénients : chaque SCR projeté est généralement optimisé pour une région ou une zone donnée. En dehors de cette zone, les déformations augmentent (forme, échelle ou surface). Une seule projection ne peut pas convenir uniformément à l’ensemble du globe. Même à l’intérieur de son domaine, certaines projections introduisent des déformations de direction ou de surface.

:::

3. __Pourquoi est-il important de choisir un SCR adapté à votre zone d’intérêt (local vs global) ? Quels problèmes peuvent survenir si vous appliquez un SCR local à des données mondiales (ou inversement) ?__

:::{dropdown} Réponse
- Parce que chaque projection est conçue pour réduire certaines déformations (surface, distance, forme) sur une emprise spatiale précise. Pour une zone locale, un SCR local ou régional limite les déformations et permet des mesures plus fiables.
- Si vous appliquez un SCR local (prévu pour une petite zone) à des données mondiales, les déformations deviennent très importantes en dehors de la région cible. Les entités peuvent être inclinées, étirées ou mal positionnées, et les calculs de distance ou de surface seront très inexacts loin de la zone optimale.
- Inversement, utiliser une projection globale (par ex. un Mercator mondial) pour une petite zone n’exploite pas la possibilité de réduire les déformations localement et peut donner une précision locale inférieure à celle d’une projection spécialisée. De plus, les projections globales déforment souvent fortement les grandes surfaces, ce qui nuit à la précision locale.
- En résumé : utiliser un SCR inadapté entraîne des incohérences, des décalages entre couches, des erreurs de mesure et des relations spatiales trompeuses.

:::

4. __Qu’est-ce qu’un code EPSG et en quoi est-il utile pour sélectionner ou désigner un SCR ?__

:::{dropdown} Réponse
- EPSG signifie European Petroleum Survey Group, organisme à l’origine d’un registre (base de données) de systèmes de coordonnées de référence et de projections.
- Un code EPSG est un identifiant numérique (par ex. EPSG:4326) attribué à un SCR donné.
- Il est utile car il fournit une manière standardisée et non ambiguë de désigner un SCR dans les logiciels SIG et les jeux de données. Plutôt que de s’appuyer uniquement sur des noms parfois ambigus, le code EPSG permet d’identifier précisément le SCR (ellipsoïde, paramètres de projection, unités).
- Dans QGIS et d’autres outils SIG, on recherche souvent un SCR par son code EPSG ou par région. Le site EPSG.io est une ressource utile pour trouver des codes SCR adaptés à une région donnée.

:::

5. __Comment reprojeter (modifier le SCR) d’une couche vectorielle dans QGIS ?__

:::{dropdown} Réponse

1. Dans la barre supérieure, allez dans le menu `Vector` → `Data Management Tools` → `Reproject Layer`.
2. Dans la fenêtre des paramètres, sélectionnez le SCR cible (en recherchant le code EPSG ou le nom).
3. Cliquez sur `Run`. Une nouvelle couche appelée `Reprojected` sera ajoutée au canevas cartographique.

:::

::::

## Ressources complémentaires <a id="further-resources"></a>

Le site [__I Hate Coordinate Systems!__](https://ihatecoordinatesystems.com/) 
propose « un guide basé sur les problèmes les plus fréquents liés aux SCR, à leurs causes et à leurs solutions ». Consultez-le si vous rencontrez des difficultés avec les systèmes de coordonnées de référence.
