# Piste d'Exercice : Analyse d’Action Anticipative pour les Cyclones à Madagascar


Cette piste d’exercice se concentre sur l’évaluation préliminaire d’un événement cyclonique à Madagascar. L’objectif est de créer un flux de travail analytique sous forme de modèle QGIS permettant d’estimer la population exposée, les infrastructures exposées et les terres agricoles exposées. De plus, l’accessibilité des régions exposées peut être évaluée à l’aide d’isochrones pré-calculées.
Dans cette piste, vous construirez un flux de travail analytique sous forme de modèle QGIS et visualiserez les résultats à l’aide de modèles de cartes et de fichiers de style.


::::{admonition} French version - Version française
:class:

We offer an english version of this exercise track which can be found here: 

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Exercise_tracks/en_mdg_aa_cyclones.html
English version
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

Madagascar est fréquemment exposé à des cyclones tropicaux intenses, qui peuvent entraîner des dégâts 
considérables, des déplacements de population et des pertes humaines. Une analyse anticipative est essentielle pour 
réduire l’impact de ces événements météorologiques extrêmes. En utilisant des données de prévision et des outils 
géospatiaux pour anticiper les zones susceptibles d’être touchées, les acteurs humanitaires et les autorités 
locales peuvent prendre des mesures précoces, telles que le prépositionnement de stocks ou la diffusion d’alertes, 
afin de protéger les vies humaines et les moyens de subsistance avant que la catastrophe ne survienne. Cette 
approche proactive renforce les capacités de préparation et de réponse, tout en permettant de gagner du temps, de 
préserver des ressources et de sauver des vies.

Aina, experte SIG à la Croix-Rouge Malagasy (CRM), se prépare pour la prochaine saison cyclonique. Elle souhaite 
renforcer la capacité de son équipe à réagir rapidement dès qu’un cyclone est prévu, en automatisant des analyses 
clés dans QGIS. Celles-ci incluent l’estimation des populations exposées, l’identification des services impactés 
comme la santé et l’éducation, ainsi que l’évaluation de l’accessibilité des postes de santé depuis les entrepôts 
stratégiques, dans une fenêtre critique de 10 heures.

L’objectif est de mettre en place un flux de travail complet d’analyse et de visualisation qui soutienne une action 
anticipative rapide et fondée sur les données, avant que le cyclone n’atteigne les côtes.

::::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_5/fr_qgis_module_5_mdg_aa_ex_1.html 
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
:link: https://giscience.github.io/gis-training-resource-center/content/Module_7/en_module_7_mdg_aa_ex_2.html 
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
:link: https://giscience.github.io/gis-training-resource-center/content/Module_7/fr_module_7_mdg_aa_ex_3.html
__Exercice 3 : Identification des établissements de santé et écoles affectés – Aina ajoute des couches (Module 7)__
^^^

- extension du modèle

- comptage des points dans les polygones

- utilisation de la calculatrice de champs

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_4/fr_module_4_mdg_aa_ex_4.html
__Exercice 4 : Visualisation des résultats d’impact du cyclone – Aina applique des styles à ses couches (Module 4)__
^^^

- utilisation du panneau de style

- application de fichiers de style aux couches

- enregistrement de fichiers de style

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_4/fr_module_4_mdg_aa_ex_5.html
__Exercice 5 : Création rapide de cartes – Aina utilise des modèles de carte (Module 4)__
^^^

- utilisation du composeur de mise en page pour créer une carte

- utilisation de modèles de carte

- utilisation des tables attributaires dans le composeur de mise en page

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_7/fr_module_7_mdg_aa_ex_6.html
__Exercice 6 : Exportation des résultats du modèle pour l’équipe des opérations (Module 7)__
^^^

- extension du modèle
- jointure des résultats du modèle
- exportation des résultats du modèle au format tableur (.csv)

:::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_9/fr_qgis_module_9_mdg_aa_ex_7.html
__Exercice 7 : Accessibilité des postes de santé depuis les entrepôts de la CRM__
^^^

- Filtrage des jeux de données
- Réalisation d’une analyse d’accessibilité
- Mise à jour des ensembles de données avec de nouvelles informations
- Visualisation de l’accessibilité des établissements de santé

:::

