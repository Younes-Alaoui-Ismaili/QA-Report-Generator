# QA Report Generator

## Description
Ce script Python génère automatiquement des rapports de tests à partir d’un fichier Excel. Il analyse les statuts des tests (Réussi/Échoué), met à jour les résultats dans le fichier et produit un rapport PDF récapitulatif.

## Fonctionnalités
- Lecture et analyse des cas de test à partir d’Excel.
- Calcul du nombre total de tests, réussites, et échecs.
- Génération d’un rapport PDF avec des statistiques claires.

## Technologies utilisées
- **Python** : pour le traitement des données.
- **pandas** : pour manipuler les fichiers Excel.
- **fpdf** : pour générer des rapports PDF.
- **openpyxl** : pour lire et écrire dans Excel.

## Prérequis
- Python 3.x installé.
- Bibliothèques requises :
  ```bash
  pip install pandas fpdf openpyxl
