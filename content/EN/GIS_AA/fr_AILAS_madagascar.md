🚧 Cette partie de la plateforme de formation est en ⚠️construction⚠️ et ne doit pas être partagée ni publiée ! 🚧

::::{admonition} English Version 
:class: tip

La version originale anglaise de cet article se trouve [ici](/content/GIS_AA/en_AILAS_madagascar.md).

The english original version of this page can be found [here](/content/GIS_AA/en_AILAS_madagascar.md).
::::

# Système de conscience siuationelle logistique par IA (AILAS): Expérimentations de terrain pour la collecte d’images au niveau de la rue

Cette documentation vise à centraliser toutes les informations concernant les expériences de terrain de collecte d’images à l’échelle de la rue pour AILAS  
et à fournir un aperçu concis du projet AILAS. Elle se concentre sur le processus de collecte d’images de rue et est destinée à être utilisée par les participants aux expériences comme guide pratique.  

Les sous-sections __[Guide d’utilisation de la caméra : projet AILAS](/content/GIS_AA/fr_AILAS_madagascar_camera_usage_guide.md)__  
et __[Guide de téléchargement et de gestion des photos](/content/GIS_AA/fr_AILAS_madagascar_picture_upload_and_management.md)__  
fournissent des instructions détaillées au sujet de l'installation et la configuration de la caméra ainsi que sur le téléversement des données générées.

## Le projet AILAS
AILAS est un service de planification d’itinéraires prévu et adaptatif aux conditions météorologiques, qui aide les utilisateurs à planifier des déplacements sur des routes non revêtues en indiquant quels segments de route sont actuellement praticables. Il combine des images récentes à l’échelle de la rue avec des données ouvertes telles que les précipitations, l’humidité du sol, le terrain et d’autres géodonnées disponibles publiquement, puis fournit des suggestions d’itinéraires pratiques via la plateforme openrouteservice (ORS). L’objectif est de réduire les retards et les risques dans les opérations humanitaires et autres activités logistiques, en particulier dans des régions comme Madagascar où de nombreuses routes ne sont pas revêtues.

:::{admonition} Détails techniques
:class: note
Pour développer le système, des dashcams sur les véhicules CRM capturent des images géolocalisées à l’échelle de la rue le long des itinéraires planifiés. Toutes les images sont téléchargées sur un stockage cloud (Panoramax), où les visages et les plaques d’immatriculation sont floutés, et un prétraitement standard prépare les données pour l’analyse.  

Chaque image est horodatée et liée à son segment de route OpenStreetMap, puis classée dans différentes catégories de praticabilité (par ex. faible praticabilité / praticabilité moyenne). Ces images classifiées seront utilisées comme données d’entraînement pour le développement d’un modèle d’apprentissage profond, dont la tâche sera de classifier automatiquement la praticabilité des images de rue après l’entraînement.  

Ces classifications sont combinées avec des données météorologiques dynamiques et d’autres données secondaires (par ex. classes de terrain ou de sol) pour développer un modèle capable d’estimer la praticabilité en fonction des conditions météorologiques actuelles ou des prévisions.  

Enfin, les résultats sont intégrés dans openrouteservice afin de prendre en compte la praticabilité des routes non revêtues lors de la génération des itinéraires.

```{figure} /fig/AILAS_workflow.png
---
name: Workflow AILAS
width: 600px
---
Flux technique du projet AILAS
```
:::

## Acquisition sur le terrain d’images à l’échelle de la rue
La collecte d’images de rue de bonne qualité est essentielle pour AILAS, car le modèle d’apprentissage profond destiné à la classification de la praticabilité des routes a besoin de photos claires et géoréférencées des conditions routières sous différentes conditions météorologiques pour apprendre et améliorer sa capacité à reconnaître les propriétés de la chaussée et à attribuer une praticabilité plausible (voir figure XX).  

Pour cela, des dashcams montées sur les véhicules CRM enregistrent le long des itinéraires planifiés ; lorsque c’est utile, des images sous licence libre provenant de Mapillary peuvent étendre la couverture. Toutes les images sont téléchargées sur un serveur Panoramax, où un floutage respectueux de la vie privée et un prétraitement standard les préparent pour l’analyse. La capture fiable, la qualité suffisante des images et un téléchargement robuste malgré des connexions instables sont les principaux défis pratiques que nous testerons sur le terrain.  

```{figure} /fig/AILAS_model_demo.png
---
name: QR Code
width: 450px
---
Représentation conceptuelle des propriétés de la chaussée que le modèle d’apprentissage profond pourrait détecter pour classifier avec précision la praticabilité des routes
```

## Objectif de l’expérience
Cette première expérimentation à Madagascar a pour but d’acquérir une expérience pratique dans la manipulation des caméras, la qualité des images, la précision GPS et la stabilité de la chaîne de téléchargement, puis de recueillir des retours structurés des équipes CRM sur ce qui fonctionne et ce qui doit être amélioré.  

Nous commencerons également à constituer une base locale d’images (passages répétés sur les mêmes parcours dans différentes conditions météorologiques) qui pourra être utilisée ultérieurement pour entraîner et valider le modèle AILAS.  

Un objectif secondaire est de documenter un flux de travail simple de bout en bout — depuis le montage de la caméra, la conduite et l’enregistrement, jusqu’au téléchargement sur Panoramax et la vérification de l’apparition correcte des images — afin que les futures équipes puissent suivre les mêmes étapes.  

Les enseignements de ce test orienteront les choix d’équipement, les attentes en termes de volume de données et les procédures opérationnelles standard pour des déploiements plus larges, tout en fournissant un premier jeu de données pour développer le modèle d’apprentissage profond prévu.
