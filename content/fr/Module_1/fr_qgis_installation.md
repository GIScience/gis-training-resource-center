::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: /content/intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Préparation de l’environnement<a id="setting-up"></a>

Dans ce chapitre, nous allons préparer l’environnement nécessaire à la formation. Cela comprend l’installation de QGIS, la mise en place d’une arborescence de dossiers pour l’ensemble des données utilisées pendant la formation, ainsi que la gestion des ressources téléchargées. La première étape consiste à installer QGIS. Ensuite, nous créerons une structure de dossiers pour la formation et passerons en revue quelques bonnes pratiques pour maintenir une gestion des données claire et cohérente.

## Guide rapide QGIS 3.34.12 - installation et configuration de base<a id="quick-guide-qgis-33412-installation-and-basic-setup"></a>

<iframe width="800" height="515" src="https://youtube.com/embed/ck4PjoOIwMQ?si=8HHR03VzpyuhXOmr" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Téléchargement et installation de QGIS<a id="qgis-download-and-installation"></a>

QGIS est un logiciel open source, et donc disponible gratuitement pour tous. Vous pouvez installer QGIS sur des ordinateurs Windows, macOS et Linux. L’installation de QGIS est très simple. Selon votre système (Windows, macOS ou Linux), certains points nécessitent toutefois une attention particulière. Vous trouverez ci-dessous des recommandations pour installer QGIS sur les différents systèmes d’exploitation.

:::{Warning}

Plusieurs versions de QGIS sont disponibles au téléchargement. Il est recommandé d’utiliser les versions __Long Term Release (LTR)__ car elles sont les plus stables et comportent le moins de bugs.
La version__Long Term Release__ actuelle est __[QGIS 3.44 ](https://qgis.org/download/)__

:::

### Téléchargement de QGIS<a id="qgis-download"></a>

1. Rendez-vous sur la [__page de téléchargement de QGIS__](https://www.qgis.org/en/site/forusers/download.html).
2. Sélectionnez `Download for Windows`, `Download for macOS` ou `Download for Linux`, selon votre système d'exploitation.
3. Cliquez sur `Looking for the most stable version? Get QGIS 3.34 LTR`

```{figure} /fig/QGIS_download_LTR_version.png
---
width: 600 px
name: QGIS_download_LTR_version
align: center
---
The download page for QGIS 3.34.
```

4. Le téléchargement va commencer.
5. Repérez le fichier téléchargé (généralement dans votre dossier Téléchargements) et exécutez-le pour lancer l’installateur.
6. Suivez les instructions d'installation pour installer QGIS !

## Points d’attention selon le système d’exploitation<a id="operating-system-specific-considerations"></a>

:::::{tab-set}

::::{tab-item} Installation sous Windows

__32 bits ou 64 bits ?__
Pour les systèmes __Windows__, il y a toujours une version 32 bits et une version 64 bits de chaque version QGIS disponible en téléchargement. La version à installer dépend de votre ordinateur et du système d'exploitation. Si vous ne savez pas combien de bits votre système d'exploitation possède, vous pouvez facilement le savoir : Faites un clic gauche sur l'icône __Windows__ en bas à gauche de l'écran (alternativement, ouvrir la fonction de recherche Windows). Tapez __"Système"__ sur le clavier, cliquez sur l'entrée __"Système"__ dans les résultats de recherche. Sous l'article __"Type de système"__ vous pouvez lire le nombre de bits.

:::{Note}

Depuis QGIS 3.20, il n'y a que des exécutables Windows 64 bits disponibles.

:::

::::

::::{tab-item} Installation sous Linux

Pour l'installation sur des systèmes Linux avec `apt` vous pouvez installer QGIS :

```
sudo apt install qgis qgis-plugin-grass
```


Dans les sources conventionnelles de paquets apt, une ancienne version de QGIS sera probablement installée. Si vous utilisez la source du paquet [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), observez l'installation suivante [notes](https://qgis.org/en/site/forusers/alldownloads.html#repositories).

Si vous installez une version 3.30 ou supérieure de QGIS, vous devez installer le plugin
_Processing Saga NextGen Provider_.

::::

:::::

## Mise en place d'une structure de dossier pour la formation <a id="setting-up-a-folder-structure-for-the-training"></a>

Garder vos données et vos fichiers de projet bien organisés est essentiel pour travailler efficacement avec un logiciel SIG. Les exercices de cette plateforme vous demandent de télécharger des données géographiques et de les traiter par vous-même. Afin de tout garder organisé, nous vous conseillons de créer une arborescence de dossiers pour l’ensemble des données et ressources téléchargées au cours de cette formation.

- Créez un dossier à l'emplacement de votre choix avec le nom `GIS_Training`.
- Lors du téléchargement des données pour les exercices, créez des sous-dossiers pour chaque module et exercice de formation (par exemple `/GIS_Training/Module_1/Exercise_1`).
- Enregistrez tous les projets QGIS ainsi que les ressources téléchargées pour les exercices dans ces dossiers.

[Module 2](/content/Module_2/en_qgis_geodata_concept.md) approfondira la gestion des données géographiques et présentera une arborescence standard pour les projets QGIS.

:::{note}

Assurez-vous de décompresser les fichiers d'exercice avant de commencer les exercices.

:::

## Questions d'auto-évaluation <a id="self-assessment-questions"></a>

:::{admonition} Vérifiez vos acquis
:class: note
Prenez un moment pour récapituler ce que vous avez appris dans ce module en vérifiant que vous maîtrisez les compétences ci-dessous :

1. __Vous savez télécharger la version la plus récente de QGIS.__
2. __Vous savez mettre en place votre propre arborescence standard.__

:::
