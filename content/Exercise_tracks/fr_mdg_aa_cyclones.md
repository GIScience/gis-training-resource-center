# Piste d'Exercice : Analyse d’Action Anticipative pour les Cyclones à Madagascar


Cette piste d’exercice se concentre sur l’évaluation préliminaire d’un événement cyclonique à Madagascar. L’objectif est de créer un flux de travail analytique sous forme de modèle QGIS permettant d’estimer la population exposée, les infrastructures exposées et les terres agricoles exposées. De plus, l’accessibilité des régions exposées peut être évaluée à l’aide d’isochrones pré-calculées.
Dans cette piste, vous construirez un flux de travail analytique sous forme de modèle QGIS et visualiserez les résultats à l’aide de modèles de cartes et de fichiers de style.


::::{admonition} French version - Version française
:class:

The french version of this exercise track can be found [here]()

La version française de cet article se trouve [ici]()

:::{card}
:link:
Version française
:::

::::

::::{card} 
Contexte
^^^

```{figure} /fig/IFRC-icons-colour_SURGE.png
---
width: 100px
align: right
name: IFRC Surge Icon
---
```

Madagascar is frequently exposed to intense tropical cyclones, which can lead to widespread damage, displacement, and loss of life. Anticipatory analysis is essential to reduce the impact of these extreme weather events. By using forecast data and geospatial tools to predict the likely areas of impact, humanitarian actors and local authorities can take early action, such as pre-positioning supplies and issuing warnings, to protect lives and livelihoods before disaster strikes. This proactive approach strengthens preparedness and response capacities, ultimately saving time, resources, and lives.

Aina, the GIS expert at the Malagasy Red Cross (CRM), is preparing for the upcoming cyclone season. She wants to improve her team’s ability to act quickly once a storm is forecasted by automating key analyses in QGIS. These include estimating exposed populations, identifying impacted services like health and education, and assessing whether health posts can be reached from key warehouses within a critical 10-hour window.
The goal is to prepare an end-to-end analysis and visualization workflow that can support fast, data-driven anticipatory action before a cyclone makes landfall.

::::

:::{card}
:link:
__Exercice 1 : Estimation de la population exposée – L’approche manuelle d’Aina (Module 5)__
^^^

- importation des jeux de données dans QGIS

- reprojection des couches

- création de zones tampons autour des couches vectorielles

- découpage des couches raster

- calcul des statistiques zonales

- application d’une classification graduée aux résultats

:::

:::{card}
:link:
__Exercice 2 : Automatisation de l’estimation de la population exposée – Le modèle d’Aina (Module 7)__
^^^

- utilisation du générateur de modèles

- reprojection des couches

- création de zones tampons autour des couches vectorielles

- découpage des couches raster

- calcul des statistiques zonales

- application d’une classification graduée aux résultats

:::

:::{card}
:link:
__Exercice 3 : Identification des établissements de santé et écoles affectés – Aina ajoute des couches (Module 7)__
^^^

- extension du modèle

- comptage des points dans les polygones

- utilisation de la calculatrice de champs

:::

:::{card}
:link:
__Exercice 4 : Visualisation des résultats d’impact du cyclone – Aina applique des styles à ses couches (Module 4)__
^^^

- utilisation du panneau de style

- application de fichiers de style aux couches

- enregistrement de fichiers de style

:::

:::{card}
:link:
__Exercice 5 : Création rapide de cartes – Aina utilise des modèles de carte (Module 4)__
^^^

- utilisation du composeur de mise en page pour créer une carte

- utilisation de modèles de carte

- utilisation des tables attributaires dans le composeur de mise en page

:::

:::{card}
__Exercice 6 : Exportation des résultats du modèle pour l’équipe des opérations (Module 7)__
^^^

- extension du modèle
- jointure des résultats du modèle
- exportation des résultats du modèle au format tableur (.csv)

:::

:::{card}
__Exercice 7 : Accessibilité des postes de santé depuis les entrepôts de la CRM__
^^^

- Filtrage des jeux de données

:::