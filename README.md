# Programmation avancée Projet d'examen - Students-Performance-in-Exams

# Dataset
- Source Kaggle : [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Téléchargement automatisé : [src/data/download_data.py](src/data/download_data.py)

# Type de problème
Ce projet implémente un pipeline de Machine Learning complet (End-to-End) pour analyser et prédire la performance des étudiants. L'objectif est double :

Classification : Prédire si un étudiant va échouer ou réussir (Target: exam passed), avec une priorité sur la détection des élèves en difficulté (Recall).

Régression : Estimer le score précis (Target: math score,  moyenne reading score et writing score, moyenne générale).

Nous nous concentrons principalement sur la tâche de classification binaire (exam passed).

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

Pour répondre à la problématique de prédiction de l'échec scolaire (Classification Binaire), nous avons implémenté et comparé plusieurs architectures de modèles. Le choix s'est porté sur une approche progressive, allant du modèle linéaire simple aux méthodes d'ensemble (Ensemble Learning) plus complexes.

Stratégie de Gestion du Déséquilibre :  
Les données étant déséquilibrées (moins d'échecs que de réussites), nous avons systématiquement appliqué des pondérations de classes (class\_weight='balanced' ou scale\_pos\_weight) pour forcer les modèles à pénaliser davantage les erreurs sur la classe minoritaire "Fail".

### **A. Les Modèles Sélectionnés**

| Modèle | Type | Pourquoi ce choix ? (Justification Architecturale) | Hypothèses & Fonctionnement |
| :---- | :---- | :---- | :---- |
| **Régression Logistique** | Linéaire | **Baseline (Référence).** Sert de point de comparaison. Si un modèle complexe ne bat pas la LogReg, il est inutile. | Suppose une séparation linéaire entre les classes (frontière droite). Interprétable via ses coefficients ($y \= \\sigma(WX \+ b)$). |
| **Random Forest** | Bagging (Ensemble) | Robustesse et réduction de la variance. Gère bien les relations non-linéaires et les interactions entre features sans configuration lourde. | Construit une "forêt" d'arbres de décision indépendants entraînés sur des sous-parties des données. La décision finale est un vote majoritaire. |
| **XGBoost / LightGBM** | Boosting (Ensemble) | **Performance SOTA (State Of The Art).** Ce sont les standards de l'industrie pour les données tabulaires. Ils corrigent itérativement les erreurs des arbres précédents. | Suppose que combiner plusieurs modèles "faibles" (arbres peu profonds) crée un modèle fort. Très sensible aux hyperparamètres mais très puissant. |
| **Linear SVM** | Marge Maximale | Alternative linéaire robuste aux outliers. | Cherche l'hyperplan qui maximise la distance (marge) entre les points des deux classes. |

### **B. Importance des Features (Feature Importance)**

L'analyse des modèles basés sur les arbres (Random Forest / XGBoost) a révélé que les facteurs socio-économiques prédominent sur la prédiction :

1. **Lunch (Standard/Free)** : Indicateur socio-économique fort.  
2. **Parental Level of Education** : Corrélation historique forte avec la réussite de l'enfant.  
3. **Test Preparation Course** : Impact direct sur la performance immédiate.

### **C. Analyse des Erreurs**

Le modèle peine principalement sur les cas "frontières" (borderline), c'est-à-dire les élèves ayant des indicateurs socio-économiques favorables mais qui échouent tout de même (faux positifs), ou inversement. La métrique prioritaire étant le **Recall (Rappel) sur la classe Fail**, nous acceptons d'avoir plus de fausses alertes (prédire un échec qui n'arrive pas) pour ne manquer aucun élève en difficulté réelle.

## **7\. Optimisation des Hyperparamètres**

Nous avons appliqué une approche rigoureuse pour optimiser le modèle **XGBoost**, identifié comme le plus prometteur lors de la phase de modélisation.

* **Méthode :** GridSearchCV (Recherche exhaustive sur grille).  
* **Validation :** StratifiedKFold (5 splits). *Crucial pour maintenir la proportion d'échecs dans chaque pli de validation.*  
* **Métrique d'optimisation (Refit) :** Recall sur la classe 0 (Fail).

### **Espace de Recherche (Search Space) Justifié**

| Hyperparamètre | Rôle | Valeurs testées & Justification |
| :---- | :---- | :---- |
| max\_depth | **Complexité.** Contrôle la profondeur de l'arbre. Trop profond \= Overfitting. | \[3, 4, 5\] : On reste sur des arbres peu profonds pour éviter le sur-apprentissage sur un petit dataset. |
| learning\_rate | **Convergence.** La taille du pas de correction à chaque itération. | \[0.02, 0.05, 0.1\] : Valeurs faibles pour une convergence douce et précise. |
| n\_estimators | **Capacité.** Nombre d'arbres (itérations). | \[200, 400, 600\] : Assez d'arbres pour stabiliser l'apprentissage. |
| scale\_pos\_weight | **Équilibrage.** Poids donné à la classe minoritaire. | Calculé dynamiquement selon le ratio n\_pass / n\_fail pour compenser le déséquilibre. |

## **8\. Évaluation & Sélection Finale**

### **A. Tableau Comparatif (Tâche : Exam Passing)**

Voici les résultats consolidés sur le jeu de validation croisée. L'objectif est de maximiser le **Recall (Fail)** tout en gardant une **F1-Score** acceptable.

| Modèle | Type | Recall (Fail) | F1-Score | Accuracy | ROC AUC |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **XGBoost (Tuned)** | **Optimisé** | **0.808** | **0.617** | **0.571** | **0.711** |
| Logistic Regression | Baseline | 0.655 | 0.672 | 0.595 | 0.683 |
| XGBoost (Base) | Baseline | 0.618 | 0.698 | 0.615 | 0.647 |
| LightGBM (Base) | Baseline | 0.600 | 0.675 | 0.590 | 0.630 |
| LightGBM (Random) | Optimisé | 0.598 | 0.729 | 0.646 | 0.689 |

### **B. Choix Final : XGBoost Tuned (GridSearch)**

Nous avons sélectionné le modèle **XGBoost optimisé via GridSearchCV**.

**Justification :**

1. **Sécurité (Recall) :** Il offre le meilleur score de Rappel (0.808). Dans notre contexte métier (détection du décrochage scolaire), **manquer un élève en difficulté est plus grave que de signaler à tort un élève qui va réussir**.  
2. **Stabilité :** Bien que son Accuracy (0.57) soit inférieure à la baseline, cela résulte d'un choix délibéré de déplacer le seuil de décision pour favoriser la classe minoritaire. Le ROC AUC (0.71) confirme que le modèle classe globalement bien les probabilités.  
3. **Robustesse :** XGBoost gère mieux la variance que les modèles linéaires sur ce type de données catégorielles complexes.

Le modèle final a été sauvegardé sous models/exam\_tuned.joblib pour le déploiement.

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
