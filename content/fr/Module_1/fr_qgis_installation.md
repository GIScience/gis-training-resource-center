::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::

# Préparation de l’environnement

Dans ce chapitre, nous allons préparer l’environnement nécessaire à la formation. Cela comprend l’installation de QGIS, la mise en place d’une arborescence de dossiers pour l’ensemble des données utilisées pendant la formation, ainsi que la gestion des ressources téléchargées. La première étape consiste à installer QGIS. Ensuite, nous créerons une structure de dossiers pour la formation et passerons en revue quelques bonnes pratiques pour maintenir une gestion des données claire et cohérente.

## Guide rapide QGIS 3.34.12 - installation et configuration de base

<iframe width="800" height="515" src="https://youtube.com/embed/ck4PjoOIwMQ?si=8HHR03VzpyuhXOmr" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Téléchargement et installation de QGIS

QGIS est un logiciel open source, et donc disponible gratuitement pour tous. Vous pouvez installer QGIS sur des ordinateurs Windows, macOS et Linux. L’installation de QGIS est très simple. Selon votre système (Windows, macOS ou Linux), certains points nécessitent toutefois une attention particulière. Vous trouverez ci-dessous des recommandations pour installer QGIS sur les différents systèmes d’exploitation.

:::{Warning} 

Plusieurs versions de QGIS sont disponibles au téléchargement. Il est recommandé d’utiliser les versions __Long Term Release (LTR)__ car elles sont les plus stables et comportent le moins de bugs.
La version __Long Term Release__ actuelle est __[QGIS 3.40.4. 'Bratislava'](https://qgis.org/download/)__

:::

### Téléchargement de QGIS

1. Rendez-vous sur la [__page de téléchargement de QGIS__](https://www.qgis.org/en/site/forusers/download.html).
2. Sélectionnez `Download for Windows`, `Download for macOS` ou `Download for Linux`, selon votre système d’exploitation.
3. Cliquez sur `Looking for the most stable version? Get QGIS 3.34 LTR`

:::{figure} /fig/QGIS_download_LTR_version.png
---
width: 600 px
name: QGIS_download_LTR_version
align: center
---
La page de téléchargement de QGIS 3.34.
:::

4. Le téléchargement démarre.
5. Repérez le fichier téléchargé (généralement dans votre dossier Téléchargements) et exécutez-le pour lancer l’installateur.
6. Suivez les instructions de l’assistant d’installation pour installer QGIS.

## Points d’attention selon le système d’exploitation

:::::{tab-set}

::::{tab-item} Installation sous Windows

__32 bits ou 64 bits ?__  
Pour les __systèmes Windows__, il existe généralement une version 32 bits et une version 64 bits pour chaque version de QGIS. Le choix de la version dépend de votre ordinateur et de votre système d’exploitation. Si vous ne savez pas si votre système est en 32 ou 64 bits, vous pouvez le vérifier facilement : cliquez sur l’__icône Windows__ en bas à gauche de l’écran (ou ouvrez la recherche Windows). Tapez __"System"__ au clavier, puis cliquez sur l’entrée __"System"__ dans les résultats. À la ligne __"System type"__, vous pouvez lire l’architecture (32 ou 64 bits).

:::{Note}

Depuis QGIS 3.20, seuls des exécutables Windows 64 bits sont disponibles.

:::

::::

::::{tab-item} Installation sous Linux

Pour une installation sur un système Linux avec `apt`, vous pouvez installer QGIS :

```
sudo apt install qgis qgis-plugin-grass
```


Dans les sources de paquets apt standard, une version plus ancienne de QGIS sera probablement installée. Si vous utilisez le dépôt [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), veuillez consulter les [notes d’installation](https://qgis.org/en/site/forusers/alldownloads.html#repositories).

Si vous installez une version de QGIS 3.30 ou supérieure, vous devez installer l’extension 
_Processing Saga NextGen Provider_.

::::

:::::

## Mettre en place une arborescence de dossiers pour la formation

Garder vos données et vos fichiers de projet bien organisés est essentiel pour travailler efficacement avec un logiciel SIG. Les exercices de cette plateforme vous demandent de télécharger des données géographiques et de les traiter par vous-même. Afin de tout garder organisé, nous vous conseillons de créer une arborescence de dossiers pour l’ensemble des données et ressources téléchargées au cours de cette formation.

- Créez un dossier à l’emplacement de votre choix, nommé `GIS_Training`. 
- Lors du téléchargement des données pour les exercices, créez des sous-dossiers pour chaque module et chaque exercice (par exemple `/GIS_Training/Module_1/Exercise_1`).
- Enregistrez tous les projets QGIS ainsi que les ressources téléchargées pour les exercices dans ces dossiers. 

[Module 2](/content/fr/Modul_2/fr_qgis_geodata_concept.md) approfondira la gestion des données géographiques et présentera une arborescence standard pour les projets QGIS. 

:::{note}

Assurez-vous de décompresser les fichiers des exercices avant de commencer. 

:::

## Questions d’auto-évaluation

:::{admonition} Vérifiez vos acquis
:class: note
Prenez un moment pour récapituler ce que vous avez appris dans ce module en vérifiant que vous maîtrisez les compétences ci-dessous :

1. __Vous savez télécharger la version la plus récente de QGIS.__
2. __Vous savez mettre en place votre propre arborescence standard.__

:::
