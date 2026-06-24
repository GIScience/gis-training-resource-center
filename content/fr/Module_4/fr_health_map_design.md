::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/fr/intro.html 
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Visualiser la capacité des établissements de santé à l’aide de symboles ponctuels multivariés <a id="visualising-health-facility-capacity-with-multi-variable-point-symbols"></a>

Une carte de capacité des établissements de santé est un outil pratique et précieux pour la préparation et la réponse sanitaires. Ces cartes aident les intervenants à identifier rapidement les emplacements des services de santé, à évaluer leur capacité et à déterminer s’ils sont opérationnels. Dans de nombreuses situations, cette information est cruciale pour prendre des décisions concernant l’allocation des ressources, les filières d’orientation, le renfort d’urgence et l’identification des lacunes de service. Les cartes sont généralement basées sur des jeux de données fournis par les gouvernements ou des organisations partenaires. Si des jeux de données officiels ne sont pas disponibles, OpenStreetMap peut constituer un bon point de départ.

Les cartes de capacité sanitaire combinent généralement plusieurs attributs dans un seul symbole en utilisant la taille, la couleur et différentes formes. 


```{figure} /fig/HS_capacity_map_examples.drawio.svg
---
name: Building a Multi-Variable Hospital Capacity Map Step by Step
width: 800
---
Construire pas à pas une carte multivariée de la capacité hospitalière.
```

Dans ce tutoriel, vous apprendrez à créer dans QGIS une carte ponctuelle multivariée des hôpitaux au Malawi. Vous travaillerez avec une version modifiée du Malawi Master Health Facility Registry (avec des chiffres fictifs et des nombres de lits hospitaliers ajoutés à des fins de formation) et appliquerez une combinaison de taille de symbole proportionnelle, de classification manuelle et de surcharges de couleur définies par les données afin de communiquer efficacement, en un coup d’œil, à la fois la capacité et le statut opérationnel.

## À propos du jeu de données <a id="about-the-dataset"></a>

Les données utilisées dans cet exercice proviennent du Malawi Master Health Facility Registry (MHFR), la base de données nationale officielle de tous les établissements de santé du Malawi : **[Malawi - Health Facility Registry](https://data.humdata.org/dataset/malawi-health-facility-registry)**.
Elle existe afin de fournir une source unique et actualisée d’informations pour la planification et le suivi des services de santé.

> ⚠️ **Note :** Dans le cadre de ce tutoriel, le jeu de données a été **manipulé**.
---
Téléchargez le dossier de données [**ici**](https://nexus.heigit.org/repository/gis-training-resource-center/module_4/exercise_6/Module_4_Exercise_Malawi_Health_Facilities_Registry.zip) et enregistrez-le sur votre PC. Décompressez le fichier .zip.

### Champs utilisés dans ce tutoriel <a id="fields-used-in-this-tutorial"></a>

| **Champ**                | **Utilisation dans le tutoriel**                            |
|--------------------------|-------------------------------------------------------------|
| **TYPE**                 | Pour extraire les hôpitaux du jeu de données complet des établissements |
| **STATUS**               | Pour cartographier les établissements fonctionnels vs non fonctionnels à l’aide de la couleur |
| **Number_Beds**          | Pour représenter la capacité hospitalière à l’aide de tailles de symboles graduées |
| **LATITUDE & LONGITUDE** | Pour créer des géométries ponctuelles dans QGIS             |

Ces champs suffisent à construire une carte ponctuelle multivariée claire.

## Tutoriel sur la carte de capacité des établissements de santé <a id="health-facilit-capacity-map-tutorial"></a>

### Préparation des données <a id="data-preparation"></a>

Tout d’abord, nous devons charger dans QGIS le jeu de données Malawi - Health Facility Registry.

::::{dropdown} Importer le CSV des établissements de santé du Malawi dans QGIS.

#### Importer le CSV des établissements de santé du Malawi dans QGIS <a id="import-the-malawi-health-facilities-csv-into-qgis"></a>

1. Dans le menu supérieur, allez à  
   **Layer → Add Layer → Add Delimited Text Layer…**.

2. À côté du champ **File name**, cliquez sur les trois points ![](/fig/Three_points.png)   
    puis parcourez jusqu’à votre fichier **CSV des établissements de santé du Malawi** et cliquez sur `Open`.


3. Après avoir sélectionné le fichier, QGIS affichera un aperçu de la table.  
   Prenez un moment pour examiner les colonnes :
   - `OWNERSHIP`  
   - `TYPE`  
   - `STATUS`  
   - `ZONE`, `DISTRICT`  
   - `DATE OPENED`  
   - `LATITUDE`, `LONGITUDE`  
   - `Number_Beds`  
   Ces champs contiennent toutes les informations nécessaires pour l’exercice de cartographie.

4. Sous **Geometry Definition** :
   - Sélectionnez **Point coordinates**.  
   - Définissez **X field** = `LONGITUDE`.  
   - Définissez **Y field** = `LATITUDE`.  
   - Assurez-vous que le **Geometry CRS** est défini sur **EPSG:4326 – WGS 84**.

5. Cliquez sur **Add**.  
   La couche apparaîtra maintenant dans votre panneau **Layers** et les points s’afficheront sur le canevas cartographique.

```{figure} /fig/en_point_visualisation_malawi_HS_csv_import.png
---
name: import_health_facilities_csv
width: 700px
---
```
::::


Ensuite, nous devons réduire les points visualisés sur la carte aux établissements qui disposent réellement de lits hospitaliers. Dans ce tutoriel, il s’agit de `Central Hospital`, `District Hospital` et `Hospital`.

::::{dropdown} Filtrer le jeu de données pour ne voir que les hôpitaux (Vidéo)

#### Filtrer le jeu de données pour ne voir que les hôpitaux <a id="filter-the-dataset-to-see-only-hospitals"></a>

1. **Ouvrir la table attributaire**  
   - Faites un clic droit sur `Malawi_health_facilities_raw` → **Open Attribute Table**.  
   - Examinez brièvement les champs clés :
     - **TYPE** – identifie le type d’établissement. Les hôpitaux apparaissent généralement comme `Central Hospital`, `District Hospital` ou `Hospital`.  
     - **STATUS** – doit contenir `Functional` ou `Non-functional`.  
     - **Number_Beds** – mostly fill

2. Filtrer le jeu de données pour inclure uniquement les hôpitaux
    - Faites un clic droit sur Malawi_health_facilities_raw → Filter…
    - Saisissez l’expression :
   ```
   "TYPE" IN ('Central Hospital', 'District Hospital', 'Hospital')
   ```
    - Cliquez sur Test pour vérifier combien de lignes correspondent, puis sur OK.
    - QGIS masquera maintenant tous les établissements non hospitaliers.
    - Votre couche filtrée montre désormais uniquement les établissements hospitaliers.

    <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_malwai_exampel_hospital_filter.mp4"></video>

::::
### Visualiser le nombre de lits avec la méthode des cercles proportionnels <a id="visualising-the-number-of-beds-with-proportional-circle-methods"></a>

Maintenant que votre couche est filtrée pour n’afficher que les hôpitaux, vous pouvez créer une carte qui montre la capacité hospitalière à l’aide de cercles proportionnels.  
Le nombre de lits (`Number_Beds`) contrôlera la **taille** de chaque symbole.


::::{dropdown} Visualiser la capacité hospitalière à l’aide de cercles proportionnels (taille graduée) (vidéo)

### Visualiser la capacité hospitalière à l’aide de cercles proportionnels (taille graduée) <a id="visualise-hospital-capacity-using-proportional-circles-graduated-size"></a>


1. **Ouvrir le panneau de stylisation de la couche**  
   - Sélectionnez votre couche d’hôpitaux (la couche filtrée `Malawi_health_facilities_raw`).  
   - Faites un clic droit sur la couche → **Properties…** → **Symbology**.

2. **Changer le moteur de rendu en Graduated**
   - En haut de la fenêtre Symbology, changez le style de **Single Symbol** à **Graduated**.

3. **Sélectionner l’attribut pour la taille des symboles**
   - Sous **Value**, choisissez **`Number_Beds`**.  
     Il s’agit du champ qui contrôlera la taille de chaque cercle.

4. **Changer la Method en “Size”**
   - À côté de **Method**, changez la valeur par défaut (généralement “Color”) en **Size**.  
     Cela transforme la classification graduée en une **carte de cercles proportionnels**.

5. **Générer les classes**
   - Cliquez sur **Classify**.  
     QGIS créera des classes de taille basées sur l’intervalle des nombres de lits dans votre jeu de données.

#### Ajuster les classes manuellement (recommandé) <a id="adjust-the-classes-manually-recommended"></a>

L’intervalle des données est de **1 à 200 lits**, mais seuls quelques hôpitaux ont plus de **80 lits**.  
La plupart des hôpitaux sont petits ou moyens.

Une classification automatique regrouperait la plupart des établissements dans une ou deux classes.  
Pour éviter cela, nous créons des **classes équilibrées et fondées sur le domaine** :

| Classe | Intervalle de lits | Signification |
|-------|-----------|---------|
| 1 | **1–20** | Très petits hôpitaux |
| 2 | **21–40** | Petits hôpitaux |
| 3 | **41–60** | Hôpitaux moyens |
| 4 | **61–80** | Grands hôpitaux |
| 5 | **81–200** | Très grands hôpitaux / hôpitaux de référence |

Ajustez les valeurs Lower/Upper pour chaque classe en conséquence.


```{note}
Pourquoi ces intervalles ?  
- La plupart des hôpitaux se situent dans l’intervalle **1–60** lits → nous le divisons en trois groupes significatifs.  
- Peu d’hôpitaux dépassent **80 lits**, donc la classe supérieure isole les rares établissements de référence à forte capacité.  
- Cela garantit que la **variation de la taille des symboles** reste visible et n’est pas compressée dans une seule petite classe. 
(Voir [Graduated Classification](https://giscience.github.io/gis-training-resource-center/content/Module_3/fr_qgis_data_classification.html#graduated-classification))
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_proportionla_circel_map_malawi_exampel.mp4"></video>

::::

La carte obtenue affiche les hôpitaux sous forme de cercles de tailles différentes, chaque taille représentant l’une des classes de capacité en lits que vous avez définies précédemment. Cela donne une impression visuelle rapide de l’emplacement des petits et grands hôpitaux. Cependant, à ce stade, la carte ne montre que la capacité : elle n’indique pas encore si un hôpital est fonctionnel ou non fonctionnel.


::::{grid} 2

:::{grid-item} **Carte de cercles proportionnels montrant le nombre de lits**
```{figure} /fig/en_Malwai_Exampel_proportional_circel_result.png
---
name: Proportional circles: beds 
width: 400
---
Cercles proportionnels : lits 
```
:::

:::{grid-item} **Classes de la carte de cercles proportionnels**

Les petits cercles correspondent aux hôpitaux ayant peu de lits, tandis que les grands cercles indiquent des établissements ayant une capacité plus élevée.
```{figure} /fig/en_Malwai_Exampel_proportional_circel_result_legend.png
---
name: Proportional circles: beds classes
width: 100
---
Cercles proportionnels : classes de lits
```
:::
::::
### Ajouter la visualisation du statut opérationnel avec la couleur <a id="adding-visualisation-of-operational-status-with-colour"></a>

Pour visualiser le statut opérationnel de chaque hôpital (opérationnel ou non opérationnel) en même temps que sa capacité en lits, nous pouvons utiliser la fonctionnalité de surcharge définie par les données de QGIS. Une **surcharge définie par les données** vous permet de contrôler une propriété du symbole — comme la couleur, la taille, la rotation ou l’opacité — à l’aide d’une expression ou d’une valeur attributaire de la couche. Cela signifie que QGIS ajuste automatiquement le symbole pour chaque entité, en fonction des données plutôt que d’une stylisation manuelle. En utilisant cette technique, nous pouvons attribuer une couleur à chaque hôpital selon son statut tout en conservant les tailles de cercles proportionnelles pour la capacité en lits.

Tout d’abord, nous devons ouvrir le **data-defined override Expression Builder**.

::::{dropdown} Ouvrir la surcharge définie par les données pour ajuster la couleur selon le statut opérationnel (Vidéo)

### Ouvrir la surcharge définie par les données pour ajuster la couleur selon le statut opérationnel <a id="open-data-defined-override-to-adjust-colour-based-on-operational-status"></a>

1.  Sélectionnez votre couche d’hôpitaux (la couche filtrée `Malawi_health_facilities_raw`).  
2. Faites un clic droit sur la couche → **Properties…** → **Symbology**.
3. À côté de l’onglet `Symbol`, cliquez sur le menu déroulant, puis en haut cliquez sur `Configure Symbol`.
4. Dans la nouvelle fenêtre, cliquez sur `Simpel Marker`, puis à côté de `fill colour`, cliquez sur le symbole `data-defined override` ![](en_data_defined_overried_icon.png)
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_edit.mp4"></video>
::::

Pour que cela fonctionne, nous devons maintenant indiquer à QGIS quelle couleur utiliser pour chaque hôpital. Les surcharges définies par les données utilisent le langage d’expression QGIS, qui vous permet d’écrire de courtes règles appliquées automatiquement à chaque entité de la couche. Dans cette étape, nous allons écrire une petite expression qui vérifie la valeur du champ STATUS et attribue la bonne couleur selon que l’hôpital est fonctionnel ou non.

::::{dropdown} Utiliser une expression pour colorer les hôpitaux selon leur statut (Vidéo)
### Utiliser une expression pour colorer les hôpitaux selon leur statut <a id="use-an-expression-to-colour-hospitals-by-status"></a>

1. Cette expression indique à QGIS de choisir automatiquement une couleur pour chaque hôpital en fonction de son attribut `STATUS`.  
Les hôpitaux fonctionnels deviennent verts, les non fonctionnels deviennent rouges, et toute valeur manquante reçoit un gris neutre.
L’instruction `CASE` fonctionne comme une règle “if–else” : QGIS vérifie la valeur du champ `STATUS` et attribue la couleur RVB correspondante ([RGB Color Picker](https://share.google/mYczZipa9EqVWFvyD)), garantissant que chaque point est stylisé de manière cohérente sans modification manuelle.
Vous pouvez copier l’intégralité du code ici :
```
CASE
  WHEN "STATUS" = 'Functional' THEN color_rgb(0, 130, 0)     -- green
  WHEN "STATUS" = 'Non-functional' THEN color_rgb(190, 0, 0) -- red
  ELSE color_rgb(150, 150, 150)                               -- fallback for missing/unknown
END
```
Ou écrire le code vous-même à l’aide des fonctionnalités du générateur d’expressions :
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_code - Made with Clipchamp.mp4"></video>

```{figure} /fig/en_data_defined_overried_calculator_Malwai_Exampel.png
---
name: Expression in data-defined override Expression Builder
width: 700px
---
Expression dans le générateur d’expressions de surcharge définie par les données
```
::::


::::{grid} 2

:::{grid-item} **Carte de cercles proportionnels montrant le nombre de lits ET le statut opérationnel**
```{figure} /fig/en_Malwai_Exampel_proportional_data_difined_override_circel_result.png
---
name: Proportional circles: beds + operational status
width: 400
---
Cercles proportionnels : lits + statut opérationnel
```
:::

:::{grid-item} **Classes de la carte de cercles proportionnels**
Cette nouvelle visualisation montre la taille du cercle, le nombre de lits, la couleur (Vert : opérationnel ; Rouge : non opérationnel) et le statut opérationnel des hôpitaux.

```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_legend.png
---
name: Legend proportional circles: beds + operational status
width: 400
---
Légende des cercles proportionnels : lits + statut opérationnel
```
:::
::::

### Faire correspondre la légende à votre carte <a id="making-the-legend-match-your-map"></a>

> ⚠️ **Note :** Lorsque vous utilisez une surcharge définie par les données pour colorer vos symboles, QGIS ne met pas automatiquement à jour la légende. 
---

Pour vous assurer que les lecteurs de votre carte comprennent la signification des couleurs, vous devez personnaliser la légende manuellement. Voici deux façons pratiques de le faire.

::::{dropdown} Option 1 : Légende avec couche auxiliaire

Une solution simple consiste à dupliquer votre couche d’hôpitaux et à utiliser ces copies uniquement comme couches auxiliaires de légende. Renommez le doublon pour l’identifier facilement et changez sa couleur dans la visualisation. Assurez-vous de masquer cette couche dans la vue cartographique. 

Dans le `Print layout`, vous pouvez ajouter cette couche à la légende. Ainsi, la légende affichera les bonnes couleurs, tandis que votre couche d’origine, qui contient les surcharges définies par les données, restera responsable du style réel de la carte.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_helper_layer.mp4"></video>
::::

::::{dropdown} Option 2 : Modifier directement les couleurs de la légende dans le Print Layout

Une autre option ne fonctionne que dans le `Print Layout`. Dans la légende, ajoutez simplement votre couche d’hôpitaux deux fois. Sur la seconde, vous pouvez ajuster directement la couleur de chaque symbole dans la légende. Définissez chaque élément en vert. En utilisant l’option `Start a new column before this term`, vous pouvez placer les deux couches côte à côte.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_print_layout_costum_symbol.mp4"></video>
::::



```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_map.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status 
width: 800
---
Exemple de carte de cercles proportionnels : lits hospitaliers + statut opérationnel 
```

### Ajouter une troisième variable à l’aide du style de contour (type d’établissement) <a id="adding-a-third-variable-using-stroke-style-facility-type"></a>

Votre carte de capacité hospitalière contient maintenant une quantité riche d’informations et elle est déjà utile dans sa forme actuelle. Cependant, QGIS nous permet d’ajouter une couche de signification supplémentaire sans créer de nouvelles couches ni modifier la logique existante de taille et de couleur. Une manière d’y parvenir consiste à utiliser le contour — la bordure de chaque symbole — qui peut être stylisé ou tramé dynamiquement. Dans la section suivante, vous apprendrez à utiliser le style de contour pour représenter un troisième attribut, rendant ainsi votre visualisation encore plus informative tout en restant facile à lire.

::::{dropdown} Ajouter une troisième variable à l’aide du style de contour (Vidéo)

1.  Sélectionnez votre couche d’hôpitaux (la couche filtrée `Malawi_health_facilities_raw`).  
2. Faites un clic droit sur la couche → **Properties…** → **Symbology**.
3. À côté de l’onglet `Symbol`, cliquez sur le menu déroulant, puis en haut cliquez sur `Configure Symbol`.
4. Dans la nouvelle fenêtre, cliquez sur `Simpel Marker`, puis sur le 
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_edit.mp4"></video>

4. Vous verrez :
- Fill colour
- `Outline/stroke colour`
- `Outline width`
- `Stroke style` ← nous allons utiliser ceci
5. Ajouter une surcharge définie par les données pour Stroke Style
- À côté de `Stroke style`, cliquez sur le petit symbole `data-defined override` ![](en_data_defined_overried_icon.png)
- Choisissez `Edit` → Cela ouvre l’éditeur d’expressions QGIS.
6. Écrire une expression pour attribuer des styles de contour à `TYPE`

Voici un exemple qui distingue trois catégories d’hôpitaux à l’aide de motifs de contour clairs et lisibles :

```
CASE
  WHEN "TYPE" = 'Central Hospital' THEN 'solid'
  WHEN "TYPE" = 'District Hospital' THEN 'dash'
  WHEN "TYPE" = 'Hospital' THEN 'dot'
  ELSE 'solid'
END
```
QGIS applique automatiquement la règle à chaque entité.

**Comment cela fonctionne :**

- `Central Hospital` → contour plein
- `District Hospital` → contour en tirets
- `Hospital` → contour en pointillés
- `All others` → plein (valeur de repli)

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>

::::

En ajoutant des styles de contour à vos symboles, la carte porte désormais un troisième niveau d’information tout en conservant un design global compact et lisible. Cela fonctionne mieux lorsque vous limitez les styles de contour à seulement quelques catégories significatives ; l’utilisation d’un trop grand nombre de motifs rendra rapidement la carte visuellement chargée. Assurez-vous que votre légende explique clairement ce que représente chaque motif, et évitez de combiner le style de contour avec des couleurs de contour supplémentaires sauf si cela est absolument nécessaire — trop de variations peuvent submerger le lecteur. En gardant ces principes à l’esprit, votre carte mise à jour devrait maintenant communiquer trois attributs à la fois, de manière claire et équilibrée.

::::{grid} 2

:::{grid-item} 
```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map.png
---
name: Proportional circles: beds + operational status + Owner status
width: 400
---
Cercles proportionnels : lits + statut opérationnel + statut du propriétaire
```
:::

:::{grid-item} 


```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_strock_style_legend.png
---
name: Legend 
Proportional circles: beds + operational status + Owner status
width: 200
---
Légende 
Cercles proportionnels : lits + statut opérationnel + statut du propriétaire
```
:::
::::
Avec trois variables visuelles désormais affichées dans un seul symbole, il est important que la légende les reflète toutes clairement. QGIS ne met pas automatiquement à jour les entrées de légende lorsque des surcharges définies par les données ou des styles de contour sont utilisés, donc quelques étapes supplémentaires sont nécessaires pour que la légende corresponde à ce qui apparaît sur votre carte. Dans la section suivante, vous apprendrez des moyens simples d’ajuster la légende afin que toutes les classes de taille, couleurs et styles de contour soient représentés avec précision.



::::{dropdown} Légende avec couche auxiliaire
Une solution simple consiste à dupliquer votre couche d’hôpitaux et à utiliser la copie uniquement comme couche auxiliaire de légende. Renommez la couche dupliquée afin qu’elle soit facile à reconnaître dans la légende. Utilisez une classification 'categorised'. Ajustez le style de contour (plein, en tirets, en pointillés) pour correspondre aux catégories que vous avez utilisées dans votre carte. Assurez-vous de masquer la couche auxiliaire dans la vue cartographique afin qu’elle n’apparaisse pas sur la carte réelle.

Dans le Print layout, ajoutez la couche auxiliaire à la légende. Cela garantit que la légende montre les bons motifs de contour, tandis que votre couche d’origine — avec ses surcharges définies par les données — continue de contrôler la symbologie réelle de la carte.
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_Malwai_Exampel_Legend_workaround_helper_layer_strok_style.mp4"></video>
::::

```{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map_complet.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status 
width: 800
---
Exemple de carte de cercles proportionnels : lits hospitaliers + statut opérationnel 
```
