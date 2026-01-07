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
2) Placer le fichier dans `C:\Users\<vous>\.kaggle\kaggle.json` (Windows). Alternativement, définir les variables d'environnement `KAGGLE_USERNAME` et `KAGGLE_KEY`.
3) Depuis la racine du projet :
	 - `python src/data/download_data.py`
	 - Options : `--dataset spscientist/students-performance-in-exams`, `--filename StudentsPerformance.csv`, `--raw-dir data/raw`.
4) Le script ne retélécharge pas si `data/raw/StudentsPerformance.csv` est déjà présent.

# Reproduire les résultats
A compléter.

# Résumé EDA

## Description
Le notebook `02_EDA_complet.ipynb` présente une analyse exploratoire complète et approfondie du dataset Students Performance in Exams. L'objectif principal est d'examiner en profondeur les distributions des variables, d'analyser les relations et corrélations entre elles, et d'identifier les facteurs clés influençant les performances académiques des étudiants. Cette analyse servira de base pour la phase de modélisation prédictive.

## Structure du notebook

### 1. Chargement et aperçu des données
Cette section initiale permet de préparer l'environnement de travail et de découvrir le dataset :
- Import des bibliothèques nécessaires (pandas, numpy, matplotlib, seaborn)
- Configuration du style de visualisation pour assurer la cohérence graphique
- Chargement du dataset depuis le repository GitHub
- Traduction des colonnes et valeurs en français pour faciliter l'interprétation
- Affichage des premières lignes du dataset
- Vérification complète de la qualité des données : recherche de valeurs manquantes, détection de doublons, analyse des types de données
- Statistiques descriptives de base pour chaque variable

### 2. Analyse univariée
Cette section examine chaque variable individuellement pour comprendre sa distribution et ses caractéristiques.

**Variables catégorielles :**
- Analyse détaillée des 5 variables catégorielles (genre, origine ethnique, niveau d'éducation des parents, type de déjeuner, cours de préparation)
- Calcul des effectifs et pourcentages pour chaque modalité
- Visualisation avec des graphiques en barres annotés montrant les distributions
- Identification des déséquilibres ou particularités dans les données

**Variables numériques (Scores) :**
- Calcul de statistiques descriptives complètes pour les trois scores (mathématiques, lecture, écriture) : moyenne, médiane, mode, écart-type, variance, asymétrie, aplatissement
- Visualisation avec histogrammes incluant les lignes de moyenne et médiane
- Création de boîtes à moustaches pour détecter visuellement les valeurs aberrantes
- Application de la méthode IQR (Interquartile Range) pour quantifier précisément les outliers
- Analyse de la forme des distributions (normalité, asymétrie)

### 3. Analyse bivariée
Cette section explore les relations entre deux variables à la fois pour identifier les dépendances et influences.

**Corrélations entre scores :**
- Calcul de la matrice de corrélation de Pearson entre les trois scores
- Visualisation avec une heatmap colorée montrant l'intensité des corrélations
- Création d'un pairplot pour visualiser graphiquement toutes les relations deux à deux
- Identification des scores fortement corrélés

**Impact des variables catégorielles sur les scores :**
- **Genre** : Boxplots comparant les distributions des scores entre hommes et femmes, analyse des différences moyennes
- **Niveau d'éducation des parents** : Visualisation de l'influence du capital culturel sur la réussite, identification d'une tendance progressive
- **Type de déjeuner** : Violin plots révélant l'impact socio-économique, comparaison entre déjeuner standard et gratuit/réduit
- **Cours de préparation** : Analyse de l'efficacité de cette intervention pédagogique, calcul du gain moyen
- **Origine ethnique** : Comparaison des performances moyennes entre les différents groupes ethniques

Chaque analyse est accompagnée d'observations détaillées expliquant les patterns observés, les écarts quantitatifs et leurs implications.

### 4. Analyse multivariée
Cette section étudie les interactions entre plusieurs variables simultanément pour comprendre les effets combinés.

**Interactions analysées :**
- **Genre × Cours de préparation** : Évaluation de l'effet combiné du genre et du cours de préparation sur les scores, vérification si le bénéfice du cours diffère selon le genre
- **Type de déjeuner × Cours de préparation** : Analyse de la compensation potentielle des inégalités socio-économiques par le cours de préparation
- Visualisation avec des barplots groupés permettant de comparer facilement les moyennes de chaque sous-groupe
- Observations sur la nature des effets : additifs (effets indépendants qui s'additionnent) ou multiplicatifs (effets qui se renforcent mutuellement)

### 5. Feature Engineering
Cette section crée de nouvelles variables dérivées pour enrichir l'analyse et faciliter la modélisation future.

**Nouvelles variables créées :**
- `score_total` : Somme des trois scores (mathématiques + lecture + écriture), donnant une vue globale de la performance
- `score_moyen` : Moyenne des trois scores, indicateur synthétique de performance
- `categorie_performance` : Classification des étudiants en 5 niveaux (Excellent ≥80, Bien ≥70, Moyen ≥60, Passable ≥50, Faible <50)
- `meilleure_matiere` : Identification de la matière où l'étudiant excelle (score maximal)
- `matiere_faible` : Identification de la matière la plus difficile pour l'étudiant (score minimal)

**Visualisations :**
- Histogramme du score total montrant la distribution globale
- Graphique en barres des catégories de performance
- Distribution de la meilleure matière par étudiant
- Distribution de la matière la plus faible
- Observations sur les profils d'étudiants identifiés

### 6. Conclusions et recommandations
Cette section finale synthétise les découvertes et oriente vers la modélisation prédictive.

**Contenu :**
- Résumé exécutif avec tous les chiffres clés et insights principaux
- Liste des variables les plus importantes identifiées pour la modélisation (cours de préparation, type de déjeuner, niveau d'éducation des parents, genre)
- Impact quantifié de chaque variable (gains moyens, écarts observés)
- Recommandations d'encodage des variables catégorielles (One-Hot Encoding)
- Algorithmes de machine learning suggérés : Random Forest (pour capturer les interactions), XGBoost (pour la performance optimale), Régression linéaire (comme baseline)
- Discussion des prochaines étapes : preprocessing, split train/test, entraînement, évaluation

## Méthodologie

### Approche de visualisation
- Utilisation systématique de seaborn et matplotlib pour créer des visualisations professionnelles et informatives
- Application d'une palette de couleurs cohérente tout au long du notebook pour faciliter la lecture
- Ajout d'annotations statistiques sur les graphiques (moyennes, médianes, effectifs, pourcentages)
- Choix de types de graphiques adaptés à chaque type d'analyse (barres, histogrammes, boxplots, violin plots, heatmaps, pairplots)

### Structure des observations
Chaque graphique est systématiquement suivi d'une cellule markdown contenant des observations structurées :
- **Description générale** : Ce qu'on observe visuellement dans le graphique
- **Analyse quantitative** : Chiffres précis, écarts, moyennes, différences entre groupes
- **Interprétation des patterns** : Explication des tendances, relations de cause à effet potentielles
- **Implications** : Conséquences pour l'analyse, importance pour la modélisation, recommandations
- Format en 5 lignes permettant une lecture rapide tout en fournissant suffisamment de détails

### Reproductibilité
- Chargement des données directement depuis GitHub pour assurer la reproductibilité
- Code organisé en cellules logiques et documentées
- Commentaires en français pour faciliter la compréhension
- Exécutable dans Google Colab ou Jupyter Notebook sans configuration particulière

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

# Limites / pistes d'amélioration
À compléter.

# Références
Voir la page Kaggle et la bibliographie utilisée (à compléter).

# Authors
- Joseph MINCHIN
- Nicolas Mouton--Besson
- Gaspard Sadourny
- Louis Vanacker
