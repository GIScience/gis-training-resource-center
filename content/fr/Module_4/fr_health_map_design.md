::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html
{octicon}`home-fill;1.5em;sd-text-danger`
:::
::::


# Visualisation de la capacit? des ?tablissements de sant? avec des symboles multi-points <a id="visualising-health-facility-capacity-with-multi-variable-point-symbols"></a>

Une carte des capacit?s des ?tablissements de sant? est un outil pratique et pr?cieux pour pr?parer la sant? et y r?pondre. Ces cartes aident les intervenants ? identifier rapidement les emplacements des services de sant?, ? ?valuer leur capacit? et ? d?terminer s?ils sont op?rationnels. Dans de nombreuses situations, ces informations sont cruciales pour prendre des d?cisions sur l?allocation des ressources, les chemins de renvoi, le soutien et l?identification des lacunes des services. Les cartes sont g?n?ralement bas?es sur des jeux de donn?es fournis par des gouvernements ou des organisations partenaires. Si les jeux de donn?es officiels ne sont pas disponibles, OpenStreetMap peut servir de bon point de d?part.

Les cartes de capacit? de sant? combinent g?n?ralement plusieurs attributs en un seul symbole en utilisant la taille, la couleur et diff?rentes formes.


:::{figure} /fig/HS_capacity_map_examples.drawio.png
---
name: HS_capacity_map_examples.drawio.png
width: 800 px
---
Construire une carte de la capacit? de l'h?pital ? plusieurs variables ?tape par ?tape.
:::

Dans ce tutoriel, vous apprendrez comment cr?er une carte multi-variable des h?pitaux du Malawi en utilisant QGIS. Vous travaillerez avec une version modifi?e du Registre des ?tablissements de sant? principal du Malawi (avec des figures fictives et des compteurs de lits d'h?pital ajout?s ? des fins de formation) et appliquerez une combinaison de la taille proportionnelle du symbole, la classification manuelle et les substitutions de couleurs d?finies par les donn?es pour communiquer efficacement ? la fois la capacit? et l'?tat op?rationnel en un coup d'?il.

## ? propos du jeu de donn?es <a id="about-the-dataset"></a>

Les donn?es utilis?es dans cet exercice proviennent du Registre principal des ?tablissements de sant? du Malawi (MHFR), la base de donn?es nationale officielle de tous les ?tablissements de sant? au Malawi : **[Malawi - Health Facility Registry](https://data.humdata.org/dataset/malawi-health-facility-registry)**.
Il existe pour fournir une source d?information unique et ? jour pour la planification et le suivi des services de sant?.

> ?? **Note:** Pour le but de ce tutoriel, le jeu de donn?es a ?t? **manipul?**.
---
T?l?chargez le dossier de donn?es [**ici**](https://nexus.heigit.org/repository/gis-training-resource-center/module_4/exercise_6/Module_4_Exercise_Malawi_Health_Facilities_Registry.zip) et enregistrez-le sur votre PC. D?compressez le fichier .zip.

### Champs utilis?s dans ce tutoriel <a id="fields-used-in-this-tutorial"></a>

| **Champ** | **Objectif dans le tutoriel** |
|--------------------------|-------------------------------------------------------------|
| **TYPE** | Pour extraire les h?pitaux du jeu de donn?es complet des installations |
| **STATUS** | Pour cartographier les h?pitaux fonctionnels et non fonctionnels |
| **Number_Beds** | Repr?senter la capacit? de l'h?pital ? l'aide de symboles gradu?s |
| **LATITUDE & LONGITUDE** | Cr?er des g?om?tries de points en QGIS |

Ces champs sont suffisants pour construire une carte claire et multivariable.

## Tutoriel sur la carte des capacit?s des ?tablissements de sant?
<a id="health-facilit-capacity-map-tutorial"></a>

### Pr?paration des donn?es <a id="data-preparation"></a>

Tout d?abord, nous devons charger le jeu de donn?es Malawi - Health Facility Registry dans QGIS.

::::{dropdown} Importez le fichier CSV des ?tablissements de sant? du Malawi dans QGIS.

#### Importez le CSV des ?tablissements de sant? du Malawi dans QGIS <a id="import-the-malawi-health-facilities-csv-into-qgis"></a>

1. Dans le menu du haut, allez ?  
**Calque ? Ajouter une couche ? Ajouter une couche de texte d?limit??**.

2. ? c?t? du champ **Nom du fichier** cliquez sur les trois points ![](/fig/Three_points.png)   
    et acc?dez ? votre fichier CSV **des ?tablissements de sant? Malawi au format** et cliquez sur `Open`.


3. Apr?s avoir s?lectionn? le fichier, QGIS affichera un aper?u de la table.  
   Prenez un moment pour examiner les colonnes :
   - `OWNERSHIP`
   - `TYPE`
   - `STATUS`
   - `ZONE`, `DISTRICT`
   - `DATE OPENED`
   - `LATITUDE`, `LONGITUDE`
   - `Number_Beds`  
      Ces champs contiennent toutes les informations n?cessaires ? l'exercice de mappage.

4. Sous **D?finition g?om?trique**:
   - S?lectionnez les coordonn?es **Point**.
   - D?finissez le champ **X** = `LONGITUDE`.
   - D?finissez le champ **Y** = `LATITUDE`.
   - Assurez-vous que le **CRS** est r?gl? sur **EPSG:4326 ? WGS 84**.

5. Cliquez sur **Ajouter**.  
   Le calque appara?tra maintenant dans votre panneau **Calques** et les points s'afficheront sur la toile de la carte.

:::{figure} /fig/en_point_visualisation_malawi_HS_csv_import.png
---
name: import_health_facilities_csv
width: 700px
---
:::
::::


Ensuite, nous devons r?duire les points visualis?s sur la carte aux installations qui disposent en fait de lits d'h?pital. Dans ce tutoriel, ce sont `Central Hospital`, `District Hospital`, et `Hospital`.

::::{dropdown} Filtrez le jeu de donn?es pour ne voir que les h?pitaux (Vid?o)

#### Filtrez le jeu de donn?es pour ne voir que les h?pitaux <a id="filter-the-dataset-to-see-only-hospitals"></a>

1. **Ouvrez la table d'attributs**
   - Faites clic droit `Malawi_health_facilities_raw` ? **Ouvrir la table d'attributs**.
   - Examinez bri?vement les champs cl?s?:
     - **TYPE** ? identifiez le type d'?tablissement. Les h?pitaux apparaissent g?n?ralement comme `Central Hospital`, `District Hospital`, ou `Hospital`.
     - **STATUS** ? doit contenir `Functional` ou `Non-functional`.
     - **Number_Beds** ? presque rempli

2. Filtrez le jeu de donn?es pour inclure uniquement les h?pitaux
    - Faites clic droit sur Malawi_health_facilities_raw ? Filtre...
    - Entrez l'expression :
   ```
   "TYPE" IN ('Central Hospital', 'District Hospital', 'Hospital')
   ```
    - Cliquez sur Test pour v?rifier combien de lignes correspondent, puis OK.
    - QGIS va masquer toutes les installations non hospitali?res.
    - Votre calque filtr? montre seulement les ?tablissements hospitaliers.

   <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_malwai_exampel_hospital_filter.mp4"></video>

::::
### Visualisation du nombre de lits avec les m?thodes du cercle proportionnel <a id="visualising-the-number-of-beds-with-proportional-circle-methods"></a>

Maintenant que votre couche est filtr?e pour afficher uniquement les h?pitaux, vous pouvez cr?er une carte qui montre la capacit? des h?pitaux ? l?aide de cercles proportionnels.  
Le nombre de lits (`Number_Beds`) contr?lera la **taille** de chaque symbole.


::::{dropdown} Visualisez la capacit? de l'h?pital ? l'aide de cercles proportionnels (taille gradu?e) (vid?o)

### Visualiser la capacit? de l'h?pital en utilisant des cercles proportionnels (taille gradu?e) <a id="visualise-hospital-capacity-using-proportional-circles-graduated-size"></a>


1. **Ouvrez le panneau de style de calque**
   - S?lectionnez votre calque hospitali?re (la A filtr?e `Malawi_health_facilities_raw`).
   - Faites un clic droit sur le calque ? **Propri?t?s?** ? **Symbologie**.

2. **Changez le mode de rendu en Gradu?**
   - En haut de la fen?tre Symbologie, changez le style de **Symbole unique** en ****.

3. **S?lectionnez l'attribut pour la taille du symbole**
   - Sous **Valeur**, choisissez **`Number_Beds`**.  
        C'est le champ qui va contr?ler la taille de chaque cercle.

4. **Changez la m?thode ? ? Taille?**
   - ? c?t? de **M?thode**, remplacez la valeur par d?faut, g?n?ralement ? Couleur ?, par **Taille**.  
        Cela transforme la classification gradu?e en une **carte ? cercles proportionnels**.

5. **G?n?rerez les classes**
   - Cliquez sur **Classer**.  
        QGIS cr?era des classes de taille en fonction de la plage de num?ros de lit dans votre jeu de donn?es.

#### Ajustez les classes manuellement (recommand?) <a id="adjust-the-classes-manually-recommended"></a>

La plage de donn?es est de **1?200 lits**, mais seuls quelques h?pitaux ont plus de **80 lits**.  
La plupart des h?pitaux sont de petite ou moyenne taille.

La classification automatique regrouperait la plupart des installations dans une ou deux classes.  
Pour ?viter cela, nous cr?ons **des classes ?quilibr?es, bas?es sur le domaine**:

| Classe | Nombre de lits disponibles | Signification |
|-------|-----------|---------|
| 1 | **1?20** | Tr?s petits h?pitaux |
| 2 | **21-40** | Petits h?pitaux |
| 3 | **41?60** | H?pitaux moyens |
| 4 | **61?80** | Grands h?pitaux |
| 5 | **81?200** | Tr?s grands h?pitaux |

Ajuster les valeurs inf?rieures/sup?rieures pour chaque classe en cons?quence.


```{note}
Why these ranges?  
- Most hospitals fall in the **1?60** bed range ? we break this into three meaningful groups.  
- Few hospitals exceed **80 beds**, so the top class isolates the rare high-capacity referral facilities.  
- This ensures **variation in symbol size** is visible and not compressed into one tiny class.
(See [Graduated Classification](https://giscience.github.io/gis-training-resource-center/content/Module_3/en_qgis_data_classification.html#graduated-classification))
```

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_proportionla_circel_map_malawi_exampel.mp4"></video>

::::

La carte qui en r?sulte affiche les h?pitaux sous forme de cercles de tailles diff?rentes, chaque taille repr?sentant une des classes de capacit? de lit que vous avez d?finies pr?c?demment. Cela donne une impression visuelle rapide de l'endroit o? se trouvent les h?pitaux plus petits et plus grands. Cependant, ? ce stade, la carte ne montre que la capacit?: elle ne communique pas encore si un h?pital est fonctionnel ou non fonctionnel.


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
### Ajout de la visualisation de l'?tat op?rationnel avec la couleur <a id="adding-visualisation-of-operational-status-with-colour"></a>

Pour visualiser l??tat de fonctionnement de chaque h?pital (op?rationnel ou non op?rationnel) ? c?t? de sa capacit? de lit, nous pouvons utiliser la fonctionnalit? de surcharge de donn?es d?finie par QGIS. Une substitution **d?finie par les donn?es** vous permet de contr?ler une propri?t? de symbole ? telle que la couleur, taille, rotation, ou opacit?, en utilisant une expression ou une valeur d'attribut du calque. Cela signifie que QGIS ajuste automatiquement le symbole pour chaque fonctionnalit?, en fonction des donn?es plut?t que du style manuel. Gr?ce ? cette technique, nous pouvons attribuer une couleur ? chaque h?pital en fonction de son statut tout en conservant la taille proportionnelle du cercle pour la capacit? du lit.

Tout d'abord, nous devons ouvrir le module de substitution **d?fini par les donn?es du constructeur d'expressions**.

::::{dropdown} Ouvre une substitution de donn?es pour ajuster la couleur en fonction du statut op?rationnel (Vid?o)

### Ouvre une substitution de donn?es pour ajuster la couleur en fonction du statut op?rationnel <a id="open-data-defined-override-to-adjust-colour-based-on-operational-status"></a>

1.  S?lectionnez votre calque hospitali?re (la A filtr?e `Malawi_health_facilities_raw`).
2. Faites un clic droit sur le calque ? **Propri?t?s?** ? **Symbologie**.
3. Nex to `Symbol` Tab cliquez sur le menu d?roulant, puis cliquez en haut sur `Configure Symbol`.
4. <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_edit.mp4"></video>Dans la nouvelle fen?tre, cliquez sur `Simpel Marker` puis sur `fill colour`sur le symbole `data-defined override`![](en_data_defined_overried_icon.png)

::::

Pour faire ce travail, nous devons maintenant indiquer ? QGIS quelle couleur utiliser pour chaque h?pital. Les substitutions d?finies par les donn?es utilisent le langage d'expression QGIS, qui vous permet d'?crire des r?gles courtes qui sont appliqu?es automatiquement ? chaque fonctionnalit? du calque. Dans cette ?tape, nous allons ?crire une petite expression qui v?rifie la valeur dans le champ STATUS et assigne la bonne couleur selon que l'h?pital est fonctionnel ou non.

::::{dropdown} Utiliser une expression pour colorer les h?pitaux par status (Video)
### Utilisez une expression pour colorier les h?pitaux par le statut <a id="use-an-expression-to-colour-hospitals-by-status"></a>

1. Cette expression indique ? QGIS de choisir automatiquement une couleur pour chaque h?pital en fonction de son attribut `STATUS`.  
Les h?pitaux fonctionnels deviennent verts, les h?pitaux non fonctionnels deviennent rouges, et toute valeur manquante re?oit un gris neutre.
L?instruction `CASE` fonctionne comme une r?gle ? if?else ? : QGIS v?rifie la valeur dans le champ `STATUS` et attribue la couleur RGB correspondante ([S?lecteur de couleur RGB](https://share.google/mYczZipa9EqVWFvyD)), ce qui garantit que chaque point est stylis? de mani?re coh?rente sans modification manuelle.
Vous pouvez copier le code complet ici :
```
CASE
  WHEN "STATUS" = 'Functional' THEN color_rgb(0, 130, 0)     -- green
  WHEN "STATUS" = 'Non-functional' THEN color_rgb(190, 0, 0) -- red
  ELSE color_rgb(150, 150, 150)                               -- fallback for missing/unknown
END
```
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_code - Made with Clipchamp.mp4"></video>Ou ?crivez vous-m?me le code en utilisant l'aide de la fonctionnalit? du constructeur d'expression :


:::{figure} /fig/en_data_defined_overried_calculator_Malwai_Exampel.png
---
name: Expression in data-defined override Expression Builder
width: 700px
---
Expression dans le Expression Builder
:::
::::


:::::{grid} 2

::::{grid-item} **Carte circulaire proportionnelle montrant le nombre de lits ET le statut op?rationnel**
:::{figure} /fig/en_Malwai_Exampel_proportional_data_difined_override_circel_result.png
---
name: Proportional circles: beds + operational status
width: 400
---
Cercles proportionnels : lits + ?tat op?rationnel
:::
::::

::::{grid-item} **Classes de la carte proportionnelle du cercle**
Cette nouvelle visualisation montre la taille du cercle, le nombre de lits, la couleur (Vert : Op?rationnel; Rouge: Non-op?ration), et le statut op?rationnel des h?pitaux.

:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_legend.png
---
name: Legend proportional circles: beds + operational status
width: 400
---
Cercles proportionnels l?gendaires : lits + ?tat op?rationnel
:::
::::
:::::

### Faire correspondre la l?gende ? votre carte <a id="making-the-legend-match-your-map"></a>

> ?? **Note:** Lorsque vous utilisez une substitution d?finie pour colorier vos symboles, QGIS ne met pas automatiquement ? jour la l?gende.
---

Pour vous assurer que vos lecteurs de cartes comprennent la signification des couleurs, vous devez personnaliser la l?gende manuellement. Voici deux fa?ons pratiques d'y parvenir.

::::{dropdown} Option 1 : L?gende avec calque d'aide

Une solution simple consiste ? dupliquer votre couche hospitali?re et ? utiliser ces copies uniquement comme aides de l?gende. Renommez le doublon pour une identification facile et changer sa couleur dans la visualisation. Assurez-vous de cacher ce calque dans la vue de la carte.

Dans le `Print layout`, vous pouvez ajouter ce calque ? la l?gende. De cette fa?on, la l?gende affichera les couleurs correctes, tandis que votre calque d'origine, qui contient les substitutions d?finies par les donn?es, sera toujours responsable du style actuel de la carte.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_helper_layer.mp4"></video>
::::

::::{dropdown} Option 2 : Modifier les couleurs de l?gende directement dans la mise en page d'impression

Une autre option ne fonctionne que dans le `Print Layout`. Dans la L?gende, il vous suffit d'ajouter la couche de l'h?pital deux fois. La secound, vous pouvez ajuster la couleur de chaque symbole directement dans la Legend. D?finissez chaque ?l?ment en vert. En utilisant l'option `Start a new column before this term`, vous pouvez placer les deux calques les uns ? c?t? des autres.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_defined_overried_calculator_Malwai_Exampel_Legend_workaround_print_layout_costum_symbol.mp4"></video>
::::



:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_map.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status
width: 800
---
Exampel Map Proportional circles: Hospital Leds + Operational Status
:::

### Ajout d'une troisi?me variable en utilisant le style de trait (Facility Type) <a id="adding-a-third-variable-using-stroke-style-facility-type"></a>

Votre carte des capacit?s de votre h?pital contient maintenant une riche quantit? d'informations, et elle est d?j? utile dans sa forme actuelle. Toutefois, QGIS nous permet d'ajouter une couche de sens suppl?mentaire sans cr?er de nouveaux calques ni modifier la taille et la logique de couleurs existantes. Une fa?on de le faire est d'utiliser le trait - le contour de chaque symbole - qui peut ?tre stylis? ou mod?lis? dynamiquement. Dans la section suivante, vous apprendrez comment utiliser le style de trait pour repr?senter un troisi?me attribut, rendre votre visualisation encore plus instructive tout en la rendant facile ? lire.

::::{dropdown} Ajout d'une troisi?me variable en utilisant le style de trait (vid?o)

1.  S?lectionnez votre calque hospitali?re (la A filtr?e `Malawi_health_facilities_raw`).
2. Faites un clic droit sur le calque ? **Propri?t?s?** ? **Symbologie**.
3. Nex to `Symbol` Tab cliquez sur le menu d?roulant, puis cliquez en haut sur `Configure Symbol`.
4. <video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_edit.mp4"></video>Dans la nouvelle fen?tre, cliquez sur `Simpel Marker` puis sur


4. Vous verrez?:
- Couleur de remplissage
- `Outline/stroke colour`
- `Outline width`
- `Stroke style` ? Nous allons utiliser ceci
5. Ajoutez une substitution d?finie de donn?es pour le style de trait
- ? c?t? de `Stroke style`, cliquez sur le petit symbole `data-defined override`![](en_data_defined_overried_icon.png)
- Choisissez `Edit` ? Ceci ouvre l'?diteur d'expressions QGIS.
6. ?crivez une expression pour assigner des styles de traits ? `TYPE`

Voici un exemple qui distingue trois cat?gories d'h?pitaux en utilisant des traits clairs et lisibles :

```
CASE
  WHEN "TYPE" = 'Central Hospital' THEN 'solid'
  WHEN "TYPE" = 'District Hospital' THEN 'dash'
  WHEN "TYPE" = 'Hospital' THEN 'dot'
  ELSE 'solid'
END
```
QGIS applique automatiquement la r?gle ? chaque fonction.

**Comment ?a marche :**

- `Central Hospital` ? contour solide
- `District Hospital` ? contour pointill?
- `Hospital` ? contour pointill?
- `All others` ? solide (par d?faut)

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_open_data_defined_override_strock_style_expression_builder.mp4"></video>

::::

En ajoutant des styles de traits ? vos symboles, la carte contient maintenant une troisi?me couche d'information tout en gardant la conception globale compacte et lisible. Cela fonctionne mieux lorsque vous limitez les styles de traits ? quelques cat?gories significatives ; utiliser trop de motifs rendra rapidement la carte visuellement bruyante. Assurez-vous que votre l?gende explique clairement ce que chaque motif repr?sente, et ?vitez de combiner le style de trait avec des couleurs de contour suppl?mentaires ? moins que ce ne soit absolument n?cessaire ? trop de variations peuvent submerger le lecteur. En gardant ces principes ? l'esprit, votre carte actualis?e devrait maintenant communiquer trois attributs ? la fois de mani?re claire et ?quilibr?e.

:::::{grid} 2

::::{grid-item}
:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map.png
---
name: Proportional circles: beds + operational status + Owner status
width: 400
---
Cercles proportionnels : lits + statut op?rationnel + statut du propri?taire
:::
::::

::::{grid-item}


:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_result_strock_style_legend.png
---
name: Legend
Cercles proportionnels : lits + statut op?rationnel + statut du propri?taire
width: 200
---
L?gende
Cercles proportionnels : lits + statut op?rationnel + statut du propri?taire
:::
::::
:::::

Avec trois variables visuelles maintenant affich?es en un seul symbole, il est important que la l?gende les refl?te toutes clairement. QGIS ne met pas automatiquement ? jour les entr?es de l?gende lorsque des substitutions d?finies ? des donn?es ou des styles de traits sont utilis?s, donc quelques ?tapes suppl?mentaires sont n?cessaires pour s'assurer que la l?gende corresponde ? ce qui appara?t sur votre carte. Dans la section suivante, vous apprendrez des fa?ons simples d'ajuster la l?gende de fa?on ? ce que toutes les classes de taille, les couleurs et les styles de traits soient repr?sent?es avec pr?cision.



::::{dropdown} La l?gende avec la couche d'aide
Une solution simple est de dupliquer votre calque hospitali?re et d'utiliser la copie uniquement comme aides de l?gende. Renommez le calque dupliqu? pour qu?il soit facile ? reconna?tre dans la l?gende. Utilisez la classification 'cat?goris?e'. Ajustez le style de trait (solide, tir?e, point?e) pour correspondre aux cat?gories que vous avez utilis?es sur votre carte. Assurez-vous de cacher le calque d'aide dans la vue de la carte afin qu'il n'apparaisse pas sur la carte actuelle.

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_data_Malwai_Exampel_Legend_workaround_helper_layer_strok_style.mp4"></video>Dans la mise en page Imprimer, ajoutez le calque d'aide ? la l?gende. Cela permet de s'assurer que la l?gende montre les bons traits, tandis que votre calque d'origine, avec ses substitutions d?finies par des donn?es, continue de contr?ler la symbologie r?elle de la carte.

::::

:::{figure} /fig/en_Malwai_Exampel_proportional_circel_data_defined_override_strock_style_result_map_complet.png
---
name: Exampel Map Proportional circles: Hospital Beds + Operational Status
width: 800
---
Cercles proportionnels de carte d'exemple : Lits d'h?pital + Statut op?rationnel
:::
