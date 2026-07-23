::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Visualisation de la capacité des établissements de santé avec des symboles multi-points <a id="visualising-health-facility-capacity-with-multi-variable-point-symbols"></a>

Une carte des capacités des établissements de santé est un outil pratique et précieux pour préparer la santé et y répondre. Ces cartes aident les intervenants à identifier rapidement les emplacements des services de santé, à évaluer leur capacité et à déterminer s’ils sont opérationnels. Dans de nombreuses situations, ces informations sont cruciales pour prendre des décisions sur l’allocation des ressources, les chemins de renvoi, le soutien et l’identification des lacunes des services. Les cartes sont généralement basées sur des jeux de données fournis par des gouvernements ou des organisations partenaires. Si les jeux de données officiels ne sont pas disponibles, OpenStreetMap peut servir de bon point de départ.

Les cartes de capacité de santé combinent généralement plusieurs attributs en un seul symbole en utilisant la taille, la couleur et différentes formes.


:::{figure} /fig/HS_capacity_map_examples.drawio.png
---
name: HS_capacity_map_examples.drawio.png
width: 800 px
---
Construire une carte de la capacité de l'hôpital à plusieurs variables étape par étape.
:::

Dans ce tutoriel, vous apprendrez comment créer une carte multi-variable des hôpitaux du Malawi en utilisant QGIS. Vous travaillerez avec une version modifiée du Registre des établissements de santé principal du Malawi (avec des figures fictives et des compteurs de lits d'hôpital ajoutés à des fins de formation) et appliquerez une combinaison de la taille proportionnelle du symbole, la classification manuelle et les substitutions de couleurs définies par les données pour communiquer efficacement à la fois la capacité et l'état opérationnel en un coup d'œil.

## À propos du jeu de données <a id="about-the-dataset"></a>

Les données utilisées dans cet exercice proviennent du Registre principal des établissements de santé du Malawi (MHFR), la base de données nationale officielle de tous les établissements de santé au Malawi : **[Malawi - Health Facility Registry](https://data.humdata.org/dataset/malawi-health-facility-registry)**.
Il existe pour fournir une source d’information unique et à jour pour la planification et le suivi des services de santé.

> ⚠️ **Note:** Pour le but de ce tutoriel, le jeu de données a été **manipulé**.
---
Téléchargez le dossier de données [**ici**](https://nexus.heigit.org/repository/gis-training-resource-center/module_4/exercise_6/Module_4_Exercise_Malawi_Health_Facilities_Registry.zip) et enregistrez-le sur votre PC. Décompressez le fichier .zip.

### Champs utilisés dans ce tutoriel <a id="fields-used-in-this-tutorial"></a>

| **Champ** | **Objectif dans le tutoriel** |
|--------------------------|-------------------------------------------------------------|
| **TYPE** | Pour extraire les hôpitaux du jeu de données complet des installations |
| **STATUS** | Pour cartographier les hôpitaux fonctionnels et non fonctionnels |
| **Number_Beds** | Représenter la capacité de l'hôpital à l'aide de symboles gradués |
| **LATITUDE & LONGITUDE** | Créer des géométries de points en QGIS |

Ces champs sont suffisants pour construire une carte claire et multivariable.

## Tutoriel sur la carte des capacités des établissements de santé
<a id="health-facilit-capacity-map-tutorial"></a>

### Préparation des données <a id="data-preparation"></a>

Tout d’abord, nous devons charger le jeu de données Malawi - Health Facility Registry dans QGIS.

::::{dropdown} Importez le fichier CSV des établissements de santé du Malawi dans QGIS.

#### Importez le CSV des établissements de santé du Malawi dans QGIS <a id="import-the-malawi-health-facilities-csv-into-qgis"></a>

1. Dans le menu du haut, allez à  
**Calque → Ajouter une couche → Ajouter une couche de texte délimité…**.

2. À côté du champ **Nom du fichier** cliquez sur les trois points ![](/fig/Three_points.png)   
    et accédez à votre fichier CSV **des établissements de santé Malawi au format** et cliquez sur `Open`.


3. Après avoir sélectionné le fichier, QGIS affichera un aperçu de la table.  
   Prenez un moment pour examiner les colonnes :
   - `OWNERSHIP`
   - `TYPE`
   - `STATUS`
   - `ZONE`, `DISTRICT`
   - `DATE OPENED`
   - `LATITUDE`, `LONGITUDE`
   - `Number_Beds`  
      Ces champs contiennent toutes les informations nécessaires à l'exercice de mappage.

4. Sous **Définition géométrique**:
   - Sélectionnez les coordonnées **Point**.
   - Définissez le champ **X** = `LONGITUDE`.
   - Définissez le champ **Y** = `LATITUDE`.
   - Assurez-vous que le **CRS** est réglé sur **EPSG:4326 – WGS 84**.

5. Cliquez sur **Ajouter**.  
   Le calque apparaîtra maintenant dans votre panneau **Calques** et les points s'afficheront sur la toile de la carte.

:::{figure} /fig/en_point_visualisation_malawi_HS_csv_import.png
---
name: import_health_facilities_csv
width: 700px
---
:::
::::


Ensuite, nous devons réduire les points visualisés sur la carte aux installations qui disposent en fait de lits d'hôpital. Dans ce tutoriel, ce sont `Central Hospital`, `District Hospital`, et `Hospital`.

::::{dropdown} Filtrez le jeu de données pour ne voir que les hôpitaux (Vidéo)

#### Filtrez le jeu de données pour ne voir que les hôpitaux <a id="filter-the-dataset-to-see-only-hospitals"></a>

1. **Ouvrez la table d'attributs**
   - Faites clic droit `Malawi_health_facilities_raw` → **Ouvrir la table d'attributs**.
   - Examinez brièvement les champs clés :
     - **TYPE** – identifiez le type d'établissement. Les hôpitaux apparaissent généralement comme `Central Hospital`, `District Hospital`, ou `Hospital`.
     - **STATUS** – doit contenir `Functional` ou `Non-functional`.
     - **Number_Beds** – presque rempli

2. Filtrez le jeu de données pour inclure uniquement les hôpitaux
    - Faites clic droit sur Malawi_health_facilities_raw → Filtre...
    - Entrez l'expression :
   ```
   "TYPE" IN ('Central Hospital', 'District Hospital', 'Hospital')
   ```
    - Cliquez sur Test pour vérifier combien de lignes correspondent, puis OK.
    - QGIS va masquer toutes les installations non hospitalières.
    - Votre calque filtré montre seulement les établissements hospitaliers.

   <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_malwai_exampel_hospital_filter.mp4"></video>

::::
### Visualisation du nombre de lits avec les méthodes du cercle proportionnel <a id="visualising-the-number-of-beds-with-proportional-circle-methods"></a>

Maintenant que votre couche est filtrée pour afficher uniquement les hôpitaux, vous pouvez créer une carte qui montre la capacité des hôpitaux à l’aide de cercles proportionnels.  
Le nombre de lits (`Number_Beds`) contrôlera la **taille** de chaque symbole.


::::{dropdown} Visualisez la capacité de l'hôpital à l'aide de cercles proportionnels (taille graduée) (vidéo)

### Visualiser la capacité de l'hôpital en utilisant des cercles proportionnels (taille graduée) <a id="visualise-hospital-capacity-using-proportional-circles-graduated-size"></a>


1. **Ouvrez le panneau de style de calque**
   - Sélectionnez votre calque hospitalière (la A filtrée `Malawi_health_facilities_raw`).
   - Faites un clic droit sur le calque → **Propriétés…** → **Symbologie**.

2. **Changez le mode de rendu en Gradué**
   - En haut de la fenêtre Symbologie, changez le style de **Symbole unique** en ****.

3. **Sélectionnez l'attribut pour la taille du symbole**
   - Sous **Valeur**, choisissez **`Number_Beds`**.  
        C'est le champ qui va contrôler la taille de chaque cercle.

4. **Changez la méthode à « Taille»**
   - À côté de **Méthode**, remplacez la valeur par défaut, généralement « Couleur », par **Taille**.  
        Cela transforme la classification graduée en une **carte à cercles proportionnels**.

5. **Générerez les classes**
   - Cliquez sur **Classer**.  
        QGIS créera des classes de taille en fonction de la plage de numéros de lit dans votre jeu de données.

#### Ajustez les classes manuellement (recommandé) <a id="adjust-the-classes-manually-recommended"></a>

La plage de données est de **1–200 lits**, mais seuls quelques hôpitaux ont plus de **80 lits**.  
La plupart des hôpitaux sont de petite ou moyenne taille.

La classification automatique regrouperait la plupart des installations dans une ou deux classes.  
Pour éviter cela, nous créons **des classes équilibrées, basées sur le domaine**:

| Classe | Nombre de lits disponibles | Signification |
|-------|-----------|---------|
| 1 | **1–20** | Très petits hôpitaux |
| 2 | **21-40** | Petits hôpitaux |
| 3 | **41–60** | Hôpitaux moyens |
| 4 | **61–80** | Grands hôpitaux |
| 5 | **81–200** | Très grands hôpitaux |

Ajuster les valeurs inférieures/supérieures pour chaque classe en conséquence.


```{note}
Why these ranges?  
- Most hospitals fall in the **1–60** bed range → we break this into three meaningful groups.  
- Few hospitals exceed **80 beds**, so the top class isolates the rare high-capacity referral facilities.  
- This ensures **variation in symbol size** is visible and not compressed into one tiny class.
(See [Graduated Classification](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_data_classification.html#graduated-classification))
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_proportionla_circel_map_malawi_exampel.mp4"></video>

::::

La carte qui en résulte affiche les hôpitaux sous forme de cercles de tailles différentes, chaque taille représentant une des classes de capacité de lit que vous avez définies précédemment. Cela donne une impression visuelle rapide de l'endroit où se trouvent les hôpitaux plus petits et plus grands. Cependant, à ce stade, la carte ne montre que la capacité: elle ne communique pas encore si un hôpital est fonctionnel ou non fonctionnel.


::::{grid} 2

:::{grid-item} **Carte circulaire proportionnelle montrant le nombre de lits**
:::{figure} /fig/en_Malwai_Exampel_proportional_circel_result.png
---
name: Proportional circles: beds
width: 400
---
Cercles proportionnels : lits
```
:::
:::{grid-item} **Classes of proportional circle map**
Smaller circles correspond to hospitals with few beds, while larger circles indicate facilities with higher capacity.
:::{figure} /fig/en_Malwai_Exampel_proportional_circel_result_legend.png
---
name: Proportional circles: beds classes
width: 100
---
Proportional circles: beds classes
```
:::
::::
### Ajout de la visualisation de l'état opérationnel avec la couleur <a id="adding-visualisation-of-operational-status-with-colour"></a>

Pour visualiser l’état de fonctionnement de chaque hôpital (opérationnel ou non opérationnel) à côté de sa capacité de lit, nous pouvons utiliser la fonctionnalité de surcharge de données définie par QGIS. Une substitution **définie par les données** vous permet de contrôler une propriété de symbole — telle que la couleur, taille, rotation, ou opacité, en utilisant une expression ou une valeur d'attribut du calque. Cela signifie que QGIS ajuste automatiquement le symbole pour chaque fonctionnalité, en fonction des données plutôt que du style manuel. Grâce à cette technique, nous pouvons attribuer une couleur à chaque hôpital en fonction de son statut tout en conservant la taille proportionnelle du cercle pour la capacité du lit.

Tout d'abord, nous devons ouvrir le module de substitution **défini par les données du constructeur d'expressions**.

::::{dropdown} Ouvre une substitution de données pour ajuster la couleur en fonction du statut opérationnel (Vidéo)

### Ouvre une substitution de données pour ajuster la couleur en fonction du statut opérationnel <a id="open-data-defined-override-to-adjust-colour-based-on-operational-status"></a>

1.  Sélectionnez votre calque hospitalière (la A filtrée `Malawi_health_facilities_raw`).
2. Faites un clic droit sur le calque → **Propriétés…** → **Symbologie**.
3. Nex to `Symbol` Tab cliquez sur le menu déroulant, puis cliquez en haut sur `Configure Symbol`.
4. <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_edit.mp4"></video>Dans la nouvelle fenêtre, cliquez sur `Simpel Marker` puis sur `fill colour`sur le symbole `data-defined override`![](en_data_defined_overried_icon.png)

::::

Pour faire ce travail, nous devons maintenant indiquer à QGIS quelle couleur utiliser pour chaque hôpital. Les substitutions définies par les données utilisent le langage d'expression QGIS, qui vous permet d'écrire des règles courtes qui sont appliquées automatiquement à chaque fonctionnalité du calque. Dans cette étape, nous allons écrire une petite expression qui vérifie la valeur dans le champ STATUS et assigne la bonne couleur selon que l'hôpital est fonctionnel ou non.

::::{dropdown} Utiliser une expression pour colorer les hôpitaux par status (Video)
### Utilisez une expression pour colorier les hôpitaux par le statut <a id="use-an-expression-to-colour-hospitals-by-status"></a>

1. Cette expression indique à QGIS de choisir automatiquement une couleur pour chaque hôpital en fonction de son attribut `STATUS`.  
Les hôpitaux fonctionnels deviennent verts, les hôpitaux non fonctionnels deviennent rouges, et toute valeur manquante reçoit un gris neutre.
L’instruction `CASE` fonctionne comme une règle « if–else » : QGIS vérifie la valeur dans le champ `STATUS` et attribue la couleur RGB correspondante ([Sélecteur de couleur RGB](https://share.google/mYczZipa9EqVWFvyD)), ce qui garantit que chaque point est stylisé de manière cohérente sans modification manuelle.
Vous pouvez copier le code complet ici :
```
CASE
  WHEN "STATUS" = 'Functional' THEN color_rgb(0, 130, 0)     -- green
  WHEN "STATUS" = 'Non-functional' THEN color_rgb(190, 0, 0) -- red
  ELSE color_rgb(150, 150, 150)                               -- fallback for missing/unknown
END
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_code - Made with Clipchamp.mp4"></video>Ou écrivez vous-même le code en utilisant l'aide de la fonctionnalité du constructeur d'expression :


:::{figure} /fig/en_data_defined_overried_calculator_Malwai_Exampel.png
---
name: Expression in data-defined override Expression Builder
width: 700px
---
Expression dans le Expression Builder
:::
::::


:::::{grid} 2

::::{grid-item} **Carte circulaire proportionnelle montrant le nombre de lits ET le statut opérationnel**
:::{figure} /fig/en_Malwai_Exampel_proportional_data_difined_override_circel_result.png
---
name: Proportional circles: beds + operational status
width: 400
---
Cercles proportionnels : lits + état opérationnel
:::
::::

::::{grid-item} **Classes de la carte proportionnelle du cercle**
Cette nouvelle visualisation montre la taille du cercle, le nombre de lits, la couleur (Vert : Opérationnel; Rouge: Non-opération), et le statut opérationnel des hôpitaux.

:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_legend.png
---
name: Legend proportional circles: beds + operational status
width: 400
---
Cercles proportionnels légendaires : lits + état opérationnel
:::
::::
:::::

### Faire correspondre la légende à votre carte <a id="making-the-legend-match-your-map"></a>

> ⚠️ **Note:** Lorsque vous utilisez une substitution définie pour colorier vos symboles, QGIS ne met pas automatiquement à jour la légende.
---

Pour vous assurer que vos lecteurs de cartes comprennent la signification des couleurs, vous devez personnaliser la légende manuellement. Voici deux façons pratiques d'y parvenir.

::::{dropdown} Option 1 : Légende avec calque d'aide

Une solution simple consiste à dupliquer votre couche hospitalière et à utiliser ces copies uniquement comme aides de légende. Renommez le doublon pour une identification facile et changer sa couleur dans la visualisation. Assurez-vous de cacher ce calque dans la vue de la carte.

Dans le `Print layout`, vous pouvez ajouter ce calque à la légende. De cette façon, la légende affichera les couleurs correctes, tandis que votre calque d'origine, qui contient les substitutions définies par les données, sera toujours responsable du style actuel de la carte.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_helper_layer.mp4"></video>
::::

::::{dropdown} Option 2 : Modifier les couleurs de légende directement dans la mise en page d'impression

Une autre option ne fonctionne que dans le `Print Layout`. Dans la Légende, il vous suffit d'ajouter la couche de l'hôpital deux fois. La secound, vous pouvez ajuster la couleur de chaque symbole directement dans la Legend. Définissez chaque élément en vert. En utilisant l'option `Start a new column before this term`, vous pouvez placer les deux calques les uns à côté des autres.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_print_layout_costum_symbol.mp4"></video>
::::



:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_map.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status
width: 800
---
Exampel Map Proportional circles: Hospital Leds + Operational Status
:::

### Ajout d'une troisième variable en utilisant le style de trait (Facility Type) <a id="adding-a-third-variable-using-stroke-style-facility-type"></a>

Votre carte des capacités de votre hôpital contient maintenant une riche quantité d'informations, et elle est déjà utile dans sa forme actuelle. Toutefois, QGIS nous permet d'ajouter une couche de sens supplémentaire sans créer de nouveaux calques ni modifier la taille et la logique de couleurs existantes. Une façon de le faire est d'utiliser le trait - le contour de chaque symbole - qui peut être stylisé ou modélisé dynamiquement. Dans la section suivante, vous apprendrez comment utiliser le style de trait pour représenter un troisième attribut, rendre votre visualisation encore plus instructive tout en la rendant facile à lire.

::::{dropdown} Ajout d'une troisième variable en utilisant le style de trait (vidéo)

1.  Sélectionnez votre calque hospitalière (la A filtrée `Malawi_health_facilities_raw`).
2. Faites un clic droit sur le calque → **Propriétés…** → **Symbologie**.
3. Nex to `Symbol` Tab cliquez sur le menu déroulant, puis cliquez en haut sur `Configure Symbol`.
4. <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_edit.mp4"></video>Dans la nouvelle fenêtre, cliquez sur `Simpel Marker` puis sur


4. Vous verrez :
- Couleur de remplissage
- `Outline/stroke colour`
- `Outline width`
- `Stroke style` ← Nous allons utiliser ceci
5. Ajoutez une substitution définie de données pour le style de trait
- À côté de `Stroke style`, cliquez sur le petit symbole `data-defined override`![](en_data_defined_overried_icon.png)
- Choisissez `Edit` → Ceci ouvre l'éditeur d'expressions QGIS.
6. Écrivez une expression pour assigner des styles de traits à `TYPE`

Voici un exemple qui distingue trois catégories d'hôpitaux en utilisant des traits clairs et lisibles :

```
CASE
  WHEN "TYPE" = 'Central Hospital' THEN 'solid'
  WHEN "TYPE" = 'District Hospital' THEN 'dash'
  WHEN "TYPE" = 'Hospital' THEN 'dot'
  ELSE 'solid'
END
```
QGIS applique automatiquement la règle à chaque fonction.

**Comment ça marche :**

- `Central Hospital` → contour solide
- `District Hospital` → contour pointillé
- `Hospital` → contour pointillé
- `All others` → solide (par défaut)

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>

::::

En ajoutant des styles de traits à vos symboles, la carte contient maintenant une troisième couche d'information tout en gardant la conception globale compacte et lisible. Cela fonctionne mieux lorsque vous limitez les styles de traits à quelques catégories significatives ; utiliser trop de motifs rendra rapidement la carte visuellement bruyante. Assurez-vous que votre légende explique clairement ce que chaque motif représente, et évitez de combiner le style de trait avec des couleurs de contour supplémentaires à moins que ce ne soit absolument nécessaire – trop de variations peuvent submerger le lecteur. En gardant ces principes à l'esprit, votre carte actualisée devrait maintenant communiquer trois attributs à la fois de manière claire et équilibrée.

:::::{grid} 2

::::{grid-item}
:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map.png
---
name: Proportional circles: beds + operational status + Owner status
width: 400
---
Cercles proportionnels : lits + statut opérationnel + statut du propriétaire
:::
::::

::::{grid-item}


:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_strock_style_legend.png
---
name: Legend
Cercles proportionnels : lits + statut opérationnel + statut du propriétaire
width: 200
---
Légende
Cercles proportionnels : lits + statut opérationnel + statut du propriétaire
:::
::::
:::::

Avec trois variables visuelles maintenant affichées en un seul symbole, il est important que la légende les reflète toutes clairement. QGIS ne met pas automatiquement à jour les entrées de légende lorsque des substitutions définies à des données ou des styles de traits sont utilisés, donc quelques étapes supplémentaires sont nécessaires pour s'assurer que la légende corresponde à ce qui apparaît sur votre carte. Dans la section suivante, vous apprendrez des façons simples d'ajuster la légende de façon à ce que toutes les classes de taille, les couleurs et les styles de traits soient représentées avec précision.



::::{dropdown} La légende avec la couche d'aide
Une solution simple est de dupliquer votre calque hospitalière et d'utiliser la copie uniquement comme aides de légende. Renommez le calque dupliqué pour qu’il soit facile à reconnaître dans la légende. Utilisez la classification 'catégorisée'. Ajustez le style de trait (solide, tirée, pointée) pour correspondre aux catégories que vous avez utilisées sur votre carte. Assurez-vous de cacher le calque d'aide dans la vue de la carte afin qu'il n'apparaisse pas sur la carte actuelle.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_Malwai_Exampel_Legend_workaround_helper_layer_strok_style.mp4"></video>Dans la mise en page Imprimer, ajoutez le calque d'aide à la légende. Cela permet de s'assurer que la légende montre les bons traits, tandis que votre calque d'origine, avec ses substitutions définies par des données, continue de contrôler la symbologie réelle de la carte.

::::

:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map_complet.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status
width: 800
---
Cercles proportionnels de carte d'exemple : Lits d'hôpital + Statut opérationnel
:::
