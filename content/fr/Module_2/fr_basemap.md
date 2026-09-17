::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Fonds de carte <a id="basemaps"></a>

Les fonds de carte dans QGIS constituent des couches de référence qui fournissent un contexte géographique essentiel aux autres couches de données spatiales. Ils incluent généralement des éléments tels que les routes, les rivières, les limites administratives, des informations topographiques et, dans certains cas, des images satellites. Leur objectif principal est d’offrir une référence visuelle pour l’analyse spatiale, la visualisation des données et la création de cartes dans les projets QGIS.

Les avantages de l’utilisation des fonds de carte dans QGIS, y compris les images satellites, incluent :

* Référence contextuelle : les fonds de carte fournissent un arrière-plan sur lequel superposer d’autres couches de données spatiales, offrant un contexte précieux pour les analyses et visualisations.
* Visualisation améliorée : l’intégration d’images satellites apporte un niveau de détail et de réalisme supplémentaire. Ces images offrent une vue à haute résolution de la surface terrestre, permettant de visualiser précisément des éléments tels que l’occupation du sol, la végétation ou les zones urbaines.
* Mise en place rapide des projets : l’utilisation de fonds de carte existants permet de démarrer rapidement un projet sans avoir à numériser ou créer des couches de base.

Les limites des fonds de carte, y compris les images satellites, peuvent inclure :

* Niveau de détail limité : bien que les images satellites soient détaillées, elles peuvent ne pas représenter certains éléments visibles dans d’autres types de cartes, comme les cartes topographiques ou thématiques.
* Précision des données : selon la source, la précision, la complétude ou l’actualité des données peuvent varier, ce qui peut affecter la fiabilité des analyses ou des visualisations.
* Dépendance à la connexion Internet : certains fonds de carte, notamment ceux provenant de services en ligne, nécessitent une connexion Internet active et ne sont pas disponibles hors ligne.

Globalement, les fonds de carte jouent un rôle essentiel dans les projets SIG en fournissant un contexte géographique et une référence visuelle. Il est important de tirer parti de leurs avantages tout en tenant compte de leurs limites et en utilisant des sources de données complémentaires pour des analyses complètes.

La section suivante présente comment accéder aux fonds de carte et les ajouter à votre projet QGIS.

## Fonds de carte standards de QGIS <a id="standard-qgis-basemaps"></a>

Vous pouvez toujours ajouter OpenStreetMap comme fond de carte dans votre canevas.

:::{tip}

L’[article wiki sur les fonds de carte](/content/fr/Wiki/fr_qgis_basemaps_wiki.md) propose un tutoriel pour ajouter d’autres types de fonds de carte (par exemple depuis Google Maps) aux options standards de QGIS.

:::

Il existe deux méthodes pour ajouter OpenStreetMap comme fond de carte :

1. Dans le panneau `Browser`, recherchez `XYZ Tiles`. Ouvrez le menu déroulant en cliquant sur la flèche et sélectionnez OpenStreetMap.
2. Dans le menu `Layer` → `Add Layer` → `Add XYZ layer...` → sélectionnez OpenStreetMap.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Add_basemap_OSM.mp4"></video>

## QuickMapServices <a id="quickmapservices"></a>

Il existe de nombreux plugins pour QGIS qui fournissent des outils supplémentaires non disponibles dans l’installation standard. L’[article sur les plugins](/content/fr/Wiki/fr_qgis_plugins_wiki.md) du wiki donne des informations détaillées. Un plugin particulièrement utile est [QuickMapServices](https://nextgis.com/blog/quickmapservices/). Ce plugin permet d’accéder à une large gamme de fonds de carte non disponibles par défaut dans QGIS, comme les images satellites Bing ou Sentinel-2.

::::{dropdown} Installation des plugins

Pour [installer un plugin](https://giscience.github.io/gis-training-resource-center/content/fr/Wiki/fr_qgis_plugins_wiki.html), dans la barre supérieure, allez dans `Plugins` → `Manage and Install Plugins…` → `All` → recherchez le plugin → `Install Plugin`.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_plugins.mp4"></video>

:::{tip}

Si vous ne trouvez pas une extension spécifique, vérifiez que vous n’avez pas ajouté d’espaces incorrects dans le nom du plugin (par exemple, “Quick Map” ne donnera pas de résultat, mais “quickmap” oui). Vous pouvez utiliser un astérisque (`*`) comme joker (par exemple "quick*map").

:::

Si vous ne trouvez toujours pas l’extension, vous devrez peut-être activer les extensions expérimentales dans les options (voir ci-dessous).

:::{figure} /fig/en_30.30.2_plugin_installation_experimental_checkbox.png
---
name: en_30.30.2_plugin_installation_experimental_checkbox
width 400 px
---
Paramètres du gestionnaire de plugins pour afficher les extensions expérimentales.
:::

::::

Pour ajouter un fond de carte via le plugin QuickMapServices :

1. Dans le menu principal, allez dans `Web` → `QuickMapServices`. 
2. Cliquez sur `Search QMS`. Un nouveau panneau s’ouvrira, généralement en bas à droite.
3. Vous pouvez alors rechercher un fond de carte, par exemple Bing Aerial, différentes versions d’OpenStreetMap ou des images Sentinel-2.

:::{tip}

Une liste de fonds de carte et de requêtes utiles pour le plugin QMS est disponible sur [ce site](https://qms.nextgis.com). Ce lien est également accessible dans la section "About" du plugin.

:::

:::{dropdown} Vidéo : fonctionnement du plugin QuickMapServices

<video width="100%" controls muted src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/add_basemap_quickmapservice.mp4"></video>

:::

:::{note}

Lorsque vous utilisez QuickMapServices, gardez à l’esprit que certains fonds de carte sont soumis à des droits d’auteur qui limitent leur reproduction. Vérifiez toujours les licences associées aux fonds de carte utilisés. En général, les images satellites ne sont pas libres d’utilisation, ce qui signifie que vous ne pouvez pas publier librement des cartes utilisant ces fonds de carte.

:::

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Vérifiez vos compétences
:class: note

Vérifiez si vous maîtrisez les concepts clés de ce chapitre en répondant aux questions ci-dessous.

1. __Qu’est-ce qu’un fond de carte et pourquoi est-il utile dans un projet SIG ?__

:::{dropdown} Réponse
Un fond de carte est une couche de base qui fournit un contexte géographique (routes, rivières, relief, images satellites, limites administratives) sur laquelle on superpose des données thématiques ou analytiques. Il est utile car il permet de se repérer, fournit un contexte spatial et facilite la création et la compréhension des cartes.
:::

2. __Comment ajouter un fond de carte dans QGIS ? Décrivez au moins une méthode (plugin, XYZ tiles, etc.).__

:::{dropdown} Réponse
- Dans le panneau `Browser`, développez le groupe "*XYZ Tiles*" et sélectionnez un service comme OpenStreetMap.
- Alternativement, installez le plugin QuickMapServices et utilisez-le pour ajouter un fond de carte.
:::

3. __Quelles sont les exigences d’attribution et comment les gérer lors de l’utilisation de fonds de carte de fournisseurs tiers ?__

:::{dropdown} Réponse
- Les exigences d’attribution correspondent aux obligations imposées par le fournisseur de données concernant la manière de citer ou créditer leur travail.
- De nombreux fonds de carte ou images satellites sont soumis à des licences restrictives.
- Pour respecter ces obligations :
   - Vérifiez les conditions d’utilisation du fournisseur.
   - Ajoutez la mention requise sur votre carte.
Par exemple, pour OpenStreetMap, il faut indiquer "© OpenStreetMap contributors". Une fois cela fait, vous pouvez diffuser votre carte.
:::

::::