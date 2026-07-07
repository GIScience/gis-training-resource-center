::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: /content/intro
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Pr?paration de l?environnement<a id="setting-up"></a>

Dans ce chapitre, nous allons pr?parer l?environnement n?cessaire ? la formation. Cela comprend l?installation de QGIS, la mise en place d?une arborescence de dossiers pour l?ensemble des donn?es utilis?es pendant la formation, ainsi que la gestion des ressources t?l?charg?es. La premi?re ?tape consiste ? installer QGIS. Ensuite, nous cr?erons une structure de dossiers pour la formation et passerons en revue quelques bonnes pratiques pour maintenir une gestion des donn?es claire et coh?rente.

## Guide rapide QGIS 3.34.12 - installation et configuration de base<a id="quick-guide-qgis-33412-installation-and-basic-setup"></a>

<iframe width="800" height="515" src="https://youtube.com/embed/ck4PjoOIwMQ?si=8HHR03VzpyuhXOmr" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## T?l?chargement et installation de QGIS<a id="qgis-download-and-installation"></a>

QGIS est un logiciel open source, et donc disponible gratuitement pour tous. Vous pouvez installer QGIS sur des ordinateurs Windows, macOS et Linux. L?installation de QGIS est tr?s simple. Selon votre syst?me (Windows, macOS ou Linux), certains points n?cessitent toutefois une attention particuli?re. Vous trouverez ci-dessous des recommandations pour installer QGIS sur les diff?rents syst?mes d?exploitation.

:::{Warning}

Plusieurs versions de QGIS sont disponibles au t?l?chargement. Il est recommand? d?utiliser les versions __Long Term Release (LTR)__ car elles sont les plus stables et comportent le moins de bugs.
La version__Long Term Release__ actuelle est __[QGIS 3.44 ](https://qgis.org/download/)__

:::

### T?l?chargement de QGIS<a id="qgis-download"></a>

1. Rendez-vous sur la [__page de t?l?chargement de QGIS__](https://www.qgis.org/en/site/forusers/download.html).
2. S?lectionnez `Download for Windows`, `Download for macOS` ou `Download for Linux`, selon votre syst?me d'exploitation.
3. Cliquez sur `Looking for the most stable version? Get QGIS 3.34 LTR`

```{figure} /fig/QGIS_download_LTR_version.png
---
width: 600 px
name: QGIS_download_LTR_version
align: center
---
The download page for QGIS 3.34.
```

4. Le t?l?chargement va commencer.
5. Rep?rez le fichier t?l?charg? (g?n?ralement dans votre dossier T?l?chargements) et ex?cutez-le pour lancer l?installateur.
6. Suivez les instructions d'installation pour installer QGIS !

## Points d?attention selon le syst?me d?exploitation<a id="operating-system-specific-considerations"></a>

:::::{tab-set}

::::{tab-item} Installation sous Windows

__32 bits ou 64 bits ?__
Pour les syst?mes __Windows__, il y a toujours une version 32 bits et une version 64 bits de chaque version QGIS disponible en t?l?chargement. La version ? installer d?pend de votre ordinateur et du syst?me d'exploitation. Si vous ne savez pas combien de bits votre syst?me d'exploitation poss?de, vous pouvez facilement le savoir : Faites un clic gauche sur l'ic?ne __Windows__ en bas ? gauche de l'?cran (alternativement, ouvrir la fonction de recherche Windows). Tapez __"Syst?me"__ sur le clavier, cliquez sur l'entr?e __"Syst?me"__ dans les r?sultats de recherche. Sous l'article __"Type de syst?me"__ vous pouvez lire le nombre de bits.

:::{Note}

Depuis QGIS 3.20, il n'y a que des ex?cutables Windows 64 bits disponibles.

:::

::::

::::{tab-item} Installation sous Linux

Pour l'installation sur des syst?mes Linux avec `apt` vous pouvez installer QGIS :

```
sudo apt install qgis qgis-plugin-grass
```


Dans les sources conventionnelles de paquets apt, une ancienne version de QGIS sera probablement install?e. Si vous utilisez la source du paquet [Ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa), observez l'installation suivante [notes](https://qgis.org/en/site/forusers/alldownloads.html#repositories).

Si vous installez une version 3.30 ou sup?rieure de QGIS, vous devez installer le plugin
_Processing Saga NextGen Provider_.

::::

:::::

## Mise en place d'une structure de dossier pour la formation <a id="setting-up-a-folder-structure-for-the-training"></a>

Garder vos donn?es et vos fichiers de projet bien organis?s est essentiel pour travailler efficacement avec un logiciel SIG. Les exercices de cette plateforme vous demandent de t?l?charger des donn?es g?ographiques et de les traiter par vous-m?me. Afin de tout garder organis?, nous vous conseillons de cr?er une arborescence de dossiers pour l?ensemble des donn?es et ressources t?l?charg?es au cours de cette formation.

- Cr?ez un dossier ? l'emplacement de votre choix avec le nom `GIS_Training`.
- Lors du t?l?chargement des donn?es pour les exercices, cr?ez des sous-dossiers pour chaque module et exercice de formation (par exemple `/GIS_Training/Module_1/Exercise_1`).
- Enregistrez tous les projets QGIS ainsi que les ressources t?l?charg?es pour les exercices dans ces dossiers.

[Module 2](/content/Module_2/en_qgis_geodata_concept.md) approfondira la gestion des donn?es g?ographiques et pr?sentera une arborescence standard pour les projets QGIS.

:::{note}

Assurez-vous de d?compresser les fichiers d'exercice avant de commencer les exercices.

:::

## Questions d'auto-?valuation <a id="self-assessment-questions"></a>

:::{admonition} V?rifiez vos acquis
:class: note
Prenez un moment pour r?capituler ce que vous avez appris dans ce module en v?rifiant que vous ma?trisez les comp?tences ci-dessous :

1. __Vous savez t?l?charger la version la plus r?cente de QGIS.__
2. __Vous savez mettre en place votre propre arborescence standard.__

:::
