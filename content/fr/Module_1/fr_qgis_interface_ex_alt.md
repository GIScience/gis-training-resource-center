# Exercice QGIS 2 : Comprendre l’interface utilisateur et le concept de couche

% CE FICHIER PEUT-IL ÊTRE SUPPRIMÉ ?

__🔙[Retour à la page d’accueil](/content/fr/intro.md)__

### Objectif de l’exercice :

Cet exercice approfondit le précédent. Cette fois-ci, nous allons également importer des données dans un projet QGIS. Nous apprendrons à afficher des données vectorielles dans QGIS, à consulter la table attributaire et à reprojeter des couches. Cet exercice aborde également des contenus du module 2 et vise à réactiver vos connaissances sur QGIS si vous avez déjà créé vos premiers projets.

### Wiki :

- [Interface](/content/fr/Wiki/fr_qgis_interface_wiki.md)

- [Projections](/content/fr/Wiki/fr_qgis_projections_wiki.md)

- [Concept de couche et importation de données](/content/fr/Wiki/fr_qgis_layer_concept_wiki.md)


### Données :

Téléchargez les données (fichier .zip : 83,23 KB) et enregistrez-les sur votre ordinateur. Créez un dossier local et enregistrez-y les données ci-dessus. (Les dossiers .zip doivent être décompressés au préalable.)

- Frontière de la Sierra Leone (polygones/lignes) – GeoPackage

- Frontières nationales de la Sierra Leone (polygones/lignes)

- Provinces de la Sierra Leone (lignes)

- Infrastructures de santé en Sierra Leone (points)

- Aéroports de Sierra Leone (CSV)

### Tâches :

1. Ouvrez QGIS et familiarisez-vous avec l’interface utilisateur.

2. Ouvrez les fichiers ci-dessus dans QGIS. Chargez les couches vectorielles dans votre projet. Importez le fichier CSV via `Ajouter un texte délimité`.

![QGIS_User_Interface](/fig/en_airports_text_layer.png)
Couche texte des aéroports

3. Interagissez avec la carte et explorez les jeux de données. Utilisez l’outil de zoom et déplacez la carte. Observez la barre d’état en bas de l’écran et notez comment elle évolue.

4. Familiarisez-vous avec le panneau des couches (Liste des couches). Affichez et masquez alternativement différentes couches et modifiez leur ordre dans la hiérarchie. Renommez les couches de manière explicite. Notez que cela n’a aucun effet sur les sources de données (noms des fichiers, emplacement de stockage).

5. Consultez les données attributaires des couches en ouvrant la table attributaire.

6. Modifiez le système de projection de l’affichage cartographique en WGS 84 / Pseudo-Mercator – EPSG:3857. Notez que cela ne modifie pas la projection (les coordonnées) des fichiers, mais uniquement celle de l’affichage de la carte. Vérifiez-le dans les propriétés de la couche de points. Quelle projection y est indiquée ? Astuce : utilisez la barre de recherche en haut.

7. Enregistrez maintenant la couche des infrastructures de santé dans la projection WGS 84 / Pseudo-Mercator – EPSG:3857. Cette opération modifie la projection du fichier. Vérifiez-le dans les propriétés de la nouvelle couche créée.

8. Enregistrez votre projet.

9. Optionnel : Vous pouvez ajouter le fond de carte OpenStreetMap via le panneau Explorateur ⇒ XYZ Tiles. Notez que les fonds de carte en ligne peuvent entraîner des problèmes de projection entre les différentes couches. Veillez à supprimer le fond de carte avant d’enregistrer le projet.

### Résultat : 

:::{dropdown} Voici (ou similaire) le résultat attendu :
![QGIS_User_Interface](/fig/en_eExercise_1_result.png)
:::