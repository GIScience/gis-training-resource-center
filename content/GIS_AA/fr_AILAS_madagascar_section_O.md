::::{admonition} French Translation 
:class: tip

La version originale anglaise de cet article se trouve [ici](/content/GIS_AA/en_AILAS_madagascar_section_O.md).

The english original version of this page can be found [here](/content/GIS_AA/en_AILAS_madagascar_section_O.md).

# Téléversement et gestion des images : Projet AILAS

Cette documentation fournit des instructions sur la manière de téléverser et de gérer les images au niveau de la rue qui sont capturées dans le cadre du projet AILAS.

## Contexte : Panoramax

Toutes les images capturées dans le cadre du projet AILAS doivent être téléversées vers une instance privée de la plateforme d’imagerie au niveau de la rue **Panoramax**. Cela garantit que les images soient facilement accessibles aux parties prenantes concernées pour une utilisation ultérieure dans le projet (annotation de données d’entraînement, modélisation), tout en étant protégées contre l’accès par des utilisateurs non autorisés.

### Qu’est-ce que Panoramax ?

[Panoramax](https://panoramax.fr) est une plateforme ouverte et fédérée pour le partage et la visualisation d’images au niveau de la rue. Comme [Google Street View](https://www.google.com/streetview/) et [Mapillary](https://www.mapillary.com), il permet aux utilisateurs d’explorer des lieux à travers des photos prises le long des rues et des chemins. Mais contrairement aux plateformes commerciales, Panoramax repose sur un **écosystème décentralisé et ouvert** : les images sont hébergées sur des serveurs indépendants (gérés par des institutions, des collectivités ou des communautés) plutôt que par une seule entreprise, et l’accès est régi par des standards ouverts. L’ensemble de la pile logicielle Panoramax est open source.

Cela signifie que la propriété des données reste entre les mains des contributeurs et des institutions hébergeantes, et que les images peuvent être plus facilement intégrées dans des projets locaux, des travaux de recherche ou des services publics. Panoramax met l’accent sur **l’ouverture, la transparence et la souveraineté** des données au niveau de la rue.

### Fonctionnalités

#### 🌍 Fonctionnalités principales

* **Visualiseur d’images au niveau de la rue** – explorer des images panoramiques ou directionnelles le long des routes, chemins et lieux.
* **Hébergement ouvert et fédéré** – les images sont stockées sur des serveurs indépendants opérés par différentes organisations (collectivités, centres de recherche, ONG, etc.).
* **Standards ouverts (STAC, OGC)** – assurent l’interopérabilité avec les plateformes de cartographie, outils SIG et portails de données.
* **Contributions de sources multiples** – les images peuvent provenir d’institutions, de projets communautaires ou d’individus.
* **Intégration dans les flux de cartographie** – les images peuvent être reliées à OpenStreetMap ou à d’autres jeux de données géospatiales.

#### 🔍 Vie privée & traitement

* **Floutage automatique des visages et plaques d’immatriculation** – anonymisation intégrée avant la publication des images.
* **Détection d’objets** – des modèles d’IA peuvent détecter des éléments pertinents (par ex. panneaux de signalisation) dans les images.
* **Modèles de détection personnalisés** – les opérateurs peuvent exécuter leurs propres pipelines de détection pour des cas d’usage spécifiques.
* **Enrichissement des métadonnées** – les objets détectés peuvent être stockés comme données liées aux images, ce qui rend les images consultables et analysables.

#### ⚙️ Plateforme & écosystème

* **Accès par API** – les développeurs peuvent interroger et utiliser les images de manière programmatique.
* **Visualiseur web** – un visualiseur léger et intégrable dans des portails publics ou des sites de projets.
* **Communautaire** – une pile logicielle open source, garantissant transparence et extensibilité.
* **Propriété des données à long terme** – les institutions gardent le contrôle sur l’endroit et la manière dont leurs images sont stockées et partagées.

### Confidentialité et sécurité des données

Panoramax empêche l’identification des personnes présentes dans les images en floutant automatiquement les visages et les plaques d’immatriculation. Ce processus intervient automatiquement au moment du téléversement, avant que les images ne soient publiées. Les utilisateurs peuvent signaler tout autre problème lié à une image via la plateforme. Dans ce cas, l’image est masquée du public jusqu’à intervention du propriétaire de l’image.

Alors qu’une des principales fonctionnalités de Panoramax est son **métacatalogue global public** qui permet de retrouver les images de toutes les instances fédérées, nous avons délibérément choisi de ne pas rejoindre la fédération avec l’instance Panoramax du projet AILAS. Cela signifie que les images téléversées sur notre instance ne peuvent pas être consultées via l’API globale.

L’API de l’instance Panoramax du projet AILAS fonctionne sur un serveur accessible uniquement depuis notre propre réseau. Les images et leurs dérivés sont stockés dans un bucket privé MinIO. L’accès au site web qui permet le téléversement et l’exploration visuelle des images collectées est protégé par mot de passe.

