::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: ../intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# La mise en page d'impression <a id="the-print-layout"></a>

La mise en page de QGIS est l’espace dans lequel vous concevez et finalisez votre carte afin de l’imprimer ou de l’exporter au format PDF (ou dans le format de fichier de votre choix). Vous pouvez y ajouter des éléments importants tels que la légende, le titre, un texte explicatif et tout autre élément nécessaire à la création d’une carte complète. En ajoutant des éléments de mise en page (légende, titre, barre d’échelle, sources, etc.) à une carte, vous fournissez à votre public les informations nécessaires pour contextualiser et évaluer les informations présentées sur la carte.

1. Dans la barre supérieure, accédez à __`Project` → `New Print Layout` → saisissez un nom pour la nouvelle mise en page → cliquez sur `OK`__.
2. Une nouvelle fenêtre contenant une mise en page vierge s’affichera.

:::{figure} ../../../fig/en_30.30.2_create_print_layout.png
---
width: 700px
name: Create Print Layout
---
Créer une nouvelle mise en page d'impression
:::

## Composition de carte <a id="map-composition"></a>

Une bonne carte guide le lecteur dans la compréhension des informations qu’elle présente, les rend facilement accessibles et évite toute surcharge d’informations.

En général, il convient de garder quelques éléments à l’esprit lors de la création d’une carte :

- La carte principale doit occuper la majeure partie de la page et être centrée.
- Une carte complète doit comporter une légende, les sources, un titre, une échelle ainsi que toute autre information nécessaire pour contextualiser les données présentées sur la carte.
- Les informations complémentaires, telles que le titre, les sources, la barre d’échelle, la légende, l’orientation, etc., doivent être dimensionnées de manière appropriée.
    - Les titres doivent être suffisamment grands pour que le lecteur puisse les identifier comme le sujet principal de la carte.
    - Les informations complémentaires doivent être plus petites et placées en dehors de la zone principale de la page (par exemple, en bas, sur les côtés ou dans les coins).
- Une mise en page bien structurée aide le lecteur à distinguer les différentes informations figurant sur la carte et lui permet de repérer plus facilement où trouver certains éléments. Des cadres et des encadrés peuvent servir à structurer la mise en page. Par exemple, la légende peut être placée sous la carte ou à sa droite.

Afin de produire de bonnes cartes, il convient de respecter certaines __règles de base__ et d’éviter certaines __erreurs sémiologiques__. Le sous-chapitre suivant présente les principaux éléments d’une carte ainsi que les erreurs de conception courantes.

### Éléments clés d'une carte <a id="key-elements-of-a-map"></a>

Afin de fournir à votre public et à vos lecteurs suffisamment d’informations pour contextualiser la carte, il est important d’ajouter les éléments cartographiques essentiels suivants :

- __Titre__
- __Légende__
- __Échelle__
- __Orientation__
- __Source__
- __Carte de localisation__
- __Auteur__

:::{figure} ../../../fig/en_good_map_composition_example.png
---
name: en_good_map_composition_example
width: 750px
---
Éléments de bonne composition de la carte
:::

---

__Le titre__ résume en quelques mots les informations représentées sur la carte et fournit au lecteur des éléments de contexte utiles. Il doit inclure les informations suivantes :


- __Le lieu__, avec un degré de précision adapté à l’échelle (pays, région, commune, etc.)

- __Le sujet__, compréhensible par tous (veillez à expliciter ailleurs sur la carte tous les acronymes utilisés)
- __La date__ des données représentées

_Exemples :_

- _« Accès aux soins de santé à Maputo, au Mozambique, en 2022 »_
- _« Risque d’inondation à Ghardaïa, en Algérie »_

__La légende__ est essentielle à l’interprétation des informations représentées sur la carte. Sans elle, il est impossible de comprendre la signification des différents symboles et couleurs utilisés. Afin de guider le lecteur, la légende doit être :

- __Exhaustive__ : toutes les données figurant sur la carte doivent être présentées dans la légende.
- __Représentative__ : les figurés sur la carte et dans la légende doivent correspondre (même taille, même couleur, etc.).
- __Organisée__ : les données de la légende peuvent être regroupées par catégories thématiques (santé, environnement, fond de carte, etc.) ou par type de figuré (point, ligne, surface) afin de faciliter la lecture.

:::{figure} ../../../fig/en_legend_good_practice.png
---
width: 750px
name: en_legend_good_practice
---
Exemple de légende bien organisée
:::

__La barre d’échelle__ est essentielle sur une carte, car elle indique la correspondance entre une distance mesurée sur la carte et la distance réelle sur le terrain. Il existe deux types d’échelles :

- __L’échelle numérique__ est exprimée sous la forme d’une fraction (1/25 000 ou 1:25 000) qui indique le rapport entre 1 centimètre sur la carte et la distance réelle. Cette échelle peut être calculée à l’aide d’un logiciel SIG et se retrouve souvent sur les cartes topographiques. Une échelle de 1:25 000 signifie que 1 cm représente 25 000 cm (soit 250 mètres) sur le terrain.

- __L’échelle graphique__ est représentée par une ligne sur la carte, accompagnée d’une valeur de distance. Elle est très utile pour comprendre les distances sur le terrain. L’échelle graphique conserve toujours les bonnes proportions, même si un format d’impression différent est utilisé, puisqu’elle subit la même transformation que le reste de la carte

:::{figure} ../../../fig/example_scale_bar.png
---
name: example_scale_bar
---
Exemples de barres d’échelle :::


### Orientation <a id="orientation"></a>

Même si la majorité des cartes sont orientées vers le nord, il est nécessaire de préciser l’orientation de votre carte. Celle-ci est souvent indiquée par une flèche pointant vers le nord, car une orientation différente peut parfois être utilisée pour représenter la zone d’étude.

### Sources <a id="sources"></a>

Toutes les données représentées sur une carte doivent être accompagnées de leurs sources. Cela permet de conserver une trace des données utilisées, mais aussi d’en créditer les auteurs. Le lecteur pourra ainsi consulter les sources s’il souhaite obtenir davantage d’informations. Les données géographiques en libre accès, telles que celles d’OpenStreetMap, sont de plus en plus utilisées et doivent également être citées sur les cartes.

Il est possible d’indiquer la source de chaque donnée sous la légende ou de regrouper les sources dans un espace dédié de la carte. Le niveau de précision des sources varie selon l’auteur et le degré de précision des données.

---

:::{admonition} À vous de jouer !
:class: tip

Examinez les cartes ci-dessous et observez attentivement la manière dont les cartographes ont disposé les différents éléments. Vous pouvez également vous inspirer de cartes rencontrées dans le cadre de votre travail ou dans votre vie quotidienne.

:::

::::{dropdown} __Exemple de carte 1__

:::{figure} ../../../fig/ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4.png
---
name: ET_Somali_Humanitarian_Access_Flooded_Areas_11152023_A4
width: 750 px
---
Zones et routes touchées par les inondations dans la région Somali, en Éthiopie (source : OCHA)
:::

::::

::::{dropdown} __Exemple de carte 2__

:::{figure} ../../../fig/proportional_circles_example.png
---
name: proportional_circles_example
width: 500 px
---
Personnes déplacées à l’intérieur de leur propre pays (PDI), 30 septembre 2024 (source : [HCR](https://reliefweb.int/map/sudan/regional-bureau-east-horn-africa-and-great-lakes-region-internally-displaced-persons-idps-30-september-2024)).
:::

::::

::::{dropdown} __Exemple de carte 3__

:::{figure} ../../../fig/choropleth_hum_example.png
---
name: choropleth_hum_example
width: 700 px
---
Soudan du Sud : suivi de la situation humanitaire, avril-mai 2024 – abris endommagés (source : [REACH](https://repository.impact-initiatives.org/document/impact/897badb8/REACH_SSD_Map_HSM_AprilMay2024_DamagedShelters_June2024-1.pdf))
:::

::::


::::{dropdown} __Exemple de carte 4__

:::{figure} ../../../fig/en_m4_operational_overview_example.png
---
name: en_m4_operational_overview_example
width: 650 px
---
Vue d’ensemble opérationnelle ou carte des activités d’intervention (source : [Shelter Cluster Vanuatu](https://reliefweb.int/map/vanuatu/vanuatu-tropical-cyclone-lola-distribution-and-gap-map-malampa-13022024))
:::

::::


Maintenant que nous avons abordé les éléments à prendre en compte lors de la conception d’une carte, voyons comment créer des cartes à l’aide du composeur de mise en page de QGIS.

## Questions d'auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note

1. __Qu’est-ce que le gestionnaire de mises en page et pourquoi l’utilise-t-on pour créer des cartes dans QGIS plutôt que la fenêtre principale de QGIS ?__

:::{dropdown} Réponse
Le gestionnaire de mises en page (accessible via `Project` → `New Print Layout` dans QGIS) est une interface ou une fenêtre distincte dans laquelle vous assemblez votre carte en vue de son impression ou de son exportation, plutôt que de travailler uniquement dans le canevas cartographique principal.

Le __composeur de mise en page__ :

- Permet de placer les éléments cartographiques (cadres de carte, légendes, barres d’échelle, titres, cartes de localisation et annotations) dans une mise en page fixe (format de page, orientation et marges) adaptée à l’exportation ou à l’impression.
- Le canevas cartographique principal de QGIS est conçu pour la modification interactive, l’exploration des données et la gestion dynamique de la symbologie, et non pour élaborer une composition finale comprenant tous les éléments cartographiques supplémentaires et les paramètres d’impression (format du papier, résolution et format d’exportation).
- Dans le composeur de mise en page, vous pouvez contrôler avec précision la position, la taille, la superposition et l’agencement des éléments cartographiques.
- Il permet de créer un produit cartographique soigné et prêt à être diffusé.

:::

2. __Quels sont les principaux éléments cartographiques à inclure dans une mise en page finale (par exemple, le titre, la légende, la flèche du nord, la barre d’échelle, la carte de localisation, l’orientation et les sources) ?__

:::{dropdown} Réponse

Une bonne carte doit fournir des informations supplémentaires permettant de contextualiser la carte et les données représentées, ainsi que d’en indiquer les sources.

Les éléments de base d’une mise en page cartographique complète doivent comprendre :

- __Titre :__ une formulation courte et concise indiquant ce que représente la carte (notamment le lieu, le sujet et la date, le cas échéant).
- __Légende :__ explique les symboles, les couleurs et les couches utilisés sur la carte afin que le lecteur puisse en interpréter la symbologie.
- __Échelle :__ indique le rapport spatial entre les unités de la carte et les distances réelles sur le terrain.
- __Orientation :__ généralement indiquée par une flèche pointant vers le nord.
- __Sources et attribution des données :__ une mention indiquant les sources des données, leur auteur et leur date.
- Informations supplémentaires permettant de contextualiser la carte (par exemple, une description, une carte de localisation, une table attributaire, un graphique, etc.).
:::

::::

## Ressources supplémentaires <a id="further-resources"></a>

- [Liste de contrôle pour l’accessibilité des visualisations de données](https://learn-sims.org/style-guidance/data-visualization-accessibility-checklist/)
