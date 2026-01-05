# Programmation avancée Projet d'examen - Students-Performance-in-Exams

# Dataset
- Source Kaggle : [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Téléchargement automatisé : [src/data/download_data.py](src/data/download_data.py)

# Type de problème
À compléter.

# Installation et environnement
- Python 3.10+.
- Installer les dépendances :
	- `pip install -r requirements.txt`

# Télécharger les données
1) Créer un token Kaggle : Profile → Settings → "Create Legacy API Key" → récupère `kaggle.json`.
2) Placer le fichier dans `C:\Users\<vous>\.kaggle\kaggle.json` (Windows). Alternativement, définir les variables d’environnement `KAGGLE_USERNAME` et `KAGGLE_KEY`.
3) Depuis la racine du projet :
	 - `python src/data/download_data.py`
	 - Options : `--dataset spscientist/students-performance-in-exams`, `--filename StudentsPerformance.csv`, `--raw-dir data/raw`.
4) Le script ne retélécharge pas si `data/raw/StudentsPerformance.csv` est déjà présent.

# Reproduire les résultats
A compléter.

# Résumé EDA
À compléter.

# Résumé de modélisation
À compléter.

# Résumé du tuning d’hyperparamètres
À compléter.

# Section analyse d’erreurs
À compléter.

# Explication de la structure du projet
- `src/` : code Python du pipeline (ingestion, features, modèles).
- `data/raw/` : données brutes (ignorées par git).
- `data/processed/` : sorties intermédiaires.
- `notebooks/` : explorations et prototypes.
- `models/` : artefacts de modèles si exportés.
- `reports/` : figures, rapports générés.

# Limites / pistes d’amélioration
À compléter.

# Références
Voir la page Kaggle et la bibliographie utilisée (à compléter).

# Authors
- Joseph MINCHIN
- Nicolas Mouton--Besson
- Gaspard Sadourny
- Louis Vanacker 
