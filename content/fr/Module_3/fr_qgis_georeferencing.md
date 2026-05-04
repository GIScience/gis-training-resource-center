::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/fr_intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Géoréférencement <a id="georeferencing"></a>

Le géoréférencement dans QGIS est le processus qui consiste à aligner une image raster, telle qu’une carte scannée ou une photographie aérienne, sur un système de coordonnées connu afin qu’elle puisse être utilisée dans une analyse spatiale. Cela implique d’attribuer des coordonnées du monde réel à l’image en identifiant des points de contrôle sur le raster qui correspondent à des emplacements connus sur la Terre, souvent à l’aide de couches vectorielles existantes ou de grilles de coordonnées comme référence.

Dans de nombreux cas, les institutions gouvernementales publient des cartes uniquement au format PDF, sans accès public aux données sous-jacentes. Dans ces cas, savoir géoréférencer correctement une carte vous permet d’accéder à l’information et de l’utiliser dans vos analyses SIG. Dans le cas présenté dans ce chapitre, la carte de dégradation des sols de la Somalie n’est disponible que dans un rapport PDF. Afin d’utiliser cette information dans une analyse SIG, nous pouvons utiliser le géoréférenceur pour attribuer des coordonnées géographiques aux pixels de l’image. Après le géoréférencement de l’image, le résultat est un fichier raster (`.tiff`). Ce jeu de données peut être vectorisé (converti en données vectorielles) ou combiné avec d’autres données raster afin d’obtenir des informations supplémentaires.

:::{figure} /fig/example_georefencing_hague.png
---
width: 750 px
name: example_georeferencing_hague
---
Une ancienne carte numérisée de La Haye (Source : [Kokoalberti](https://kokoalberti.com/articles/georeferencing-and-digitizing-old-maps-with-gdal/)).
:::

<!--ADD: Pictures of maps available in pdf reports-->

## Géoréférencement dans QGIS <a id="georeferencing-in-qgis"></a>

Dans QGIS, l’outil Georeferencer est utilisé pour ce processus. Les utilisateurs placent manuellement des points de contrôle sur l’image raster et leur attribuent une coordonnée géographique, soit en saisissant les coordonnées manuellement, soit en sélectionnant le point correspondant dans le canevas cartographique de QGIS. Ces points servent de points de référence pour l’algorithme de géoréférencement afin d’ajouter des coordonnées géographiques à chaque pixel du raster. L’algorithme transforme ensuite l’image en ajustant son échelle, sa rotation et sa position pour la superposer correctement aux autres couches géospatiales. Les images géoréférencées deviennent alors précieuses pour numériser des entités et mener des analyses spatiales dans un SIG.  

Il existe plusieurs algorithmes de transformation disponibles dans QGIS pour géoréférencer une carte. Si la carte est dans le même CRS et doit seulement être pivotée, une transformation linéaire est suffisante. En revanche, si l’image ou la carte est dans un CRS différent ou est visiblement déformée, une transformation polynomiale est nécessaire. Plus l’algorithme de transformation est complexe, plus vous aurez besoin de points de contrôle au sol.

:::{figure} /fig/en_georef_transformations.png
---
width: 600 px
name: en_georef_transformations
---
Différents types de transformation : linéaire (à gauche), polynomiale de degré 2 (au centre), polynomiale de degré 3 (à droite) (Source : [ESRI](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/overview-of-georeferencing.htm)).
:::

Dans la plupart des cas, vous utiliserez soit des transformations linéaires, soit des transformations polynomiales (de degré 2 ou 3). Il existe de nombreux autres types de transformation pouvant être utilisés dans QGIS. Chacun fonctionne mieux pour un cas d’usage spécifique. Pour une explication de chaque type de transformation, consultez la [documentation QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_raster/georeferencer.html).


### Comment géoréférencer dans QGIS <a id="how-to-georeference-in-qgis"></a>

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_3.36_georeferencing_howto.mp4"></video>

Afin de géoréférencer une carte PDF, vous devez suivre les étapes suivantes :

1. Préparez la carte que vous souhaitez géoréférencer, soit en exportant la page pertinente du PDF, soit en faisant une capture d’écran.
2. Dans votre fenêtre QGIS, ajoutez un fond de carte à l’aide des XYZ-tiles :
    1. `Layer` → `Add Layer` → `Add XYZ Tiles`. 
    2. Une nouvelle fenêtre s’ouvrira. Sous `XYZ Connection` en haut de la fenêtre, sélectionnez "OpenStreetMap".
    3. Cliquez sur `Add`.
Idéalement, utilisez un fond de carte sur lequel vous pouvez identifier des emplacements précis à la fois sur le fond de carte et sur la carte que vous souhaitez géoréférencer.
3. Ouvrez le Georeferencer en allant dans la barre supérieure → `Layer` → `Georeferencer` (voir {numref}`open_georeferencer`).

:::{figure} /fig/en_3.36_open_georefencer.png
---
name: en_3.36_open_georefencer
width: 500 px
---
Ouverture du géoréférenceur dans QGIS 3.36.
:::

4. Une nouvelle fenêtre s’ouvrira. Il s’agit du __géoréférenceur__. Pour ajouter une image à géoréférencer, cliquez sur ![](/fig/3.36_add_raster_georef.png) `Open Raster`.
5. Sélectionnez l’image de la carte que vous souhaitez géoréférencer. Vous pouvez charger des fichiers image ainsi que des PDF. Cliquez sur `Open`.
6. L’image apparaîtra au centre de la fenêtre du géoréférenceur. Cliquez sur ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. Une nouvelle fenêtre s’ouvrira. Vous pourrez y définir le type de transformation et le CRS cible. En dessous, vous pouvez définir le nom et l’emplacement d’enregistrement du fichier. Assurez-vous que l’option `Load in the project when done` est cochée. 

:::{note} Définir le système de coordonnées de référence approprié 
:class: tip
Idéalement, vous devez définir le CRS de la carte géoréférencée identique à celui de votre projet / des autres couches de votre projet. Pour apprendre à choisir un CRS approprié, consultez le [chapitre sur les projections](/content/fr/Module_2/fr_qgis_projections.md) dans le module 2.
:::

::::{margin}

:::{note}
Dans la plupart des cas, vous pouvez laisser le type de transformation sur linéaire. Les cartes régionales sont généralement dans une projection conforme (c’est-à-dire que les angles sont conservés). Les images satellites également. Si vous constatez que les angles ne sont pas corrects, ou que la carte est déformée, vous devrez peut-être choisir une transformation polynomiale. Les transformations polynomiales nécessitent davantage de points de contrôle au sol et ces points doivent être répartis uniformément sur la carte.
:::

::::

8. Cliquez sur `Ok`. 
9. Une fois le type de transformation défini, vous pouvez commencer à ajouter des Ground Control Points (GCP) en cliquant sur ![](/fig/3.36_georef_add_point.png) `Add Point`. Les Ground Control Points sont des points auxquels vous attribuez des coordonnées géographiques spécifiques. 
10. Cliquez sur un point de l’image de la carte. Il doit s’agir d’un emplacement précis que vous pouvez identifier à la fois sur le fond de carte et sur la carte que vous souhaitez géoréférencer. 
11. Une fois que vous avez cliqué sur une position, une nouvelle fenêtre apparaîtra. Vous y ajoutez les coordonnées du point sélectionné. Il existe deux options pour cela :  
    - Saisir les coordonnées manuellement. Vous devez connaître la coordonnée exacte. Parfois, une grille de coordonnées figure sur les cartes, ce qui peut vous aider. 
    - Sélectionner les points ![](/fig/en_3.36_georef_select_from_canvas.png). Ce mode réduira le géoréférenceur et ouvrira le canevas cartographique de QGIS. Zoomez sur le même emplacement que celui sélectionné sur la carte non géoréférencée et cliquez une fois.
    - Une fois les coordonnées saisies, cliquez sur `Ok`.
12. La fenêtre du géoréférenceur s’ouvrira à nouveau. Cette fois, sous l’image de la carte, vous verrez un point dans le tableau. Ce sont les Ground Control Points. Continuez à ajouter d’autres GCP. Répartissez-les sur l’ensemble de la carte. Assurez-vous que la `Mean error` en bas à droite de la fenêtre du géoréférenceur soit aussi faible que possible (idéalement inférieure à 5). 

:::{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: en_3.36_georef_dialogue_GCP
---
Boîte de dialogue du géoréférenceur dans QGIS 3.36.
:::

13. Une fois que vous avez ajouté suffisamment de points, cliquez sur ![](/fig/3.36_start_georef.png) `Start Georeferencing`. QGIS utilisera les points que vous avez ajoutés pour transformer l’image en une image géoréférencée, dans laquelle chaque pixel possède des coordonnées GPS qui lui sont attribuées. 
14. Vous pouvez fermer la fenêtre du géoréférenceur. Décidez si vous souhaitez enregistrer les points GPC dans un fichier. Si vous n’êtes pas sûr que la précision de votre géoréférencement soit suffisante, enregistrez les points GPC afin de ne pas avoir à refaire tout le travail. 
15. Félicitations, la carte géoréférencée apparaîtra maintenant comme une couche raster dans votre projet QGIS


:::{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: en_3.36_finished_georef
---
Une carte géoréférencée de la Somalie dans le canevas cartographique QGIS
:::

## Ajuster la couche géoréférencée <a id="adjusting-the-georeferenced-layer"></a>

Il est possible d’ajuster la transparence de la carte géoréférencée afin de voir les couches sous-jacentes :

1. Ouvrez les propriétés de la couche en <kbd>faisant un clic droit</kbd> sur la couche, puis en sélectionnant __Properties__.
2. Allez dans l’__onglet Transparency__.
3. Réglez l’opacité globale sur 50 %.

Il est également possible de supprimer l’arrière-plan blanc. Cela se fait en attribuant les pixels blancs à la valeur Alpha dans l’onglet de transparence, sous "Custom Transparency Options".

1. Ouvrez les propriétés de la couche en <kbd>faisant un clic droit</kbd> sur la couche, puis en sélectionnant __Properties__.
2. Allez dans l’__onglet Transparency__.
3. Dans la zone __Custom Transparency Options__, sous Transparency Band, sélectionnez Band 4 (Alpha).
4. À droite, cliquez sur ![](/fig/en_3.36_add_value_from_display) `Add value from display`.
5. Cliquez sur la couleur blanche de la carte géoréférencée dans le canevas cartographique.
6. Cliquez sur `Apply`.

## Questions d’auto-évaluation <a id="self-assessment-questions"></a>

::::{admonition} Testez vos connaissances
:class: note 

1. __Qu’est-ce que le géoréférencement, et pourquoi est-ce important ?__

:::{dropdown} Réponse
- Le géoréférencement est le processus qui consiste à attribuer à une image des coordonnées spatiales du monde réel (dans un système de coordonnées de référence connu), par exemple à une photographie aérienne ou à une carte scannée, afin qu’elle s’aligne correctement avec des données géographiques (vectorielles ou raster).
- Cela vous permet de superposer, comparer, mesurer et analyser cette image avec d’autres données SIG. Sans géoréférencement, l’image « flotte » sans contexte spatial.
- Il garantit l’exactitude spatiale, l’intégration et la cohérence entre les jeux de données, et permet des analyses spatiales et une production cartographique pertinentes.
:::

2. __Que sont les Ground Control Points (GCPs) ? Pourquoi est-il important de les répartir uniformément sur l’image ?__

:::{dropdown} Réponse
- Les Ground Control Points (GCPs) sont des points spécifiques de l’image pour lesquels les coordonnées du monde réel sont connues (c’est-à-dire que vous pouvez identifier le même point à la fois dans le raster et dans une carte de référence ou une couche vectorielle).
- Lors du géoréférencement, vous collectez des paires de coordonnées image et de coordonnées terrain à ces points de contrôle, puis vous en déduisez la transformation qui permet de projeter l’ensemble de l’image dans le système de coordonnées.

__Pourquoi les répartir uniformément ?__
- Si tous les GCPs sont concentrés dans une seule zone, la transformation peut être plus précise localement dans cette zone, mais très déformée ailleurs.
- Une répartition uniforme (dans les coins, sur les bords et au centre) permet de mieux contraindre les déformations sur l’ensemble de l’étendue de l’image et produit une transformation plus stable et plus équilibrée.
- Cela réduit les erreurs d’extrapolation et garantit que toutes les parties de l’image sont contrôlées.
:::


::::
