housing-data-manager-api
Description
Le projet Housing-Data-Manager-API est une API REST construite avec FastAPI permettant de gérer des données sur les logements. Il inclut :

L'ajout et la récupération d'informations sur les maisons.
L'analyse et la visualisation des données de logements avec Pandas, Matplotlib et Seaborn.
Un modèle de prédiction basé sur Scikit-learn (RandomForestRegressor) pour estimer la valeur des maisons.
Le projet utilise PostgreSQL avec SQLAlchemy pour la gestion des modèles et Alembic pour les migrations.

Installation
Pré-requis
Python 3.9 ou supérieur
PostgreSQL installé et configuré
Docker et Docker Compose (facultatif)
Un gestionnaire de dépendances comme Poetry
Étapes
Clonez le dépôt GitHub :

bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/housing-api.git
cd housing-api
Créez et activez un environnement virtuel :

bash
Copier
Modifier
python -m venv env
source env/bin/activate   # Sous Windows : .\env\Scripts\activate
Installez les dépendances avec Poetry :

bash
Copier
Modifier
poetry install
Configurez la base de données PostgreSQL :

Créez une base de données : housing.
Modifiez la variable DATABASE_URL dans le fichier .env ou dans la configuration du docker-compose.yml.
Appliquez les migrations :

bash
Copier
Modifier
alembic upgrade head
Lancez le serveur FastAPI :

bash
Copier
Modifier
uvicorn app.main:app --reload
Accédez à la documentation interactive de l'API :

Swagger UI : http://127.0.0.1:8000/docs
ReDoc : http://127.0.0.1:8000/redoc
Dockerisation de l'API
Étape 1 : Dockerfile
Le fichier Dockerfile configure l'environnement pour l'API. Il contient :

L'image Python 3.9.
L'installation des dépendances via Poetry.
Une commande pour appliquer les migrations automatiquement avant de démarrer le serveur.
Étape 2 : docker-compose.yml
Le fichier docker-compose.yml configure deux services :

api : Le service qui exécute l'API FastAPI.
db : Le service PostgreSQL pour la base de données.
Étape 3 : Lancer les services avec Docker Compose
Assurez-vous que Docker et Docker Compose sont installés.

Exécutez la commande suivante pour construire les conteneurs et lancer les services :

bash
Copier
Modifier
docker-compose up --build
Une fois les services lancés :

L'API est accessible sur http://127.0.0.1:8000.
Les données PostgreSQL sont stockées de manière persistante dans un volume Docker.
Fonctionnalités
1. Gestion des données de maisons
Ajouter et récupérer des informations sur les maisons via l'API.
Structure des données :
longitude, latitude
housing_median_age, total_rooms, total_bedrooms, population, households
median_income, median_house_value, ocean_proximity
2. Analyse des données
Chargement et exploration des données depuis un fichier CSV.
Nettoyage des données et génération de visualisations (matrice de corrélation).
3. Modèle d'inférence
Entraînement d'un modèle de régression (RandomForestRegressor).
Déploiement d'une API de prédiction.
Sauvegarde et chargement du modèle avec Joblib.
Structure du projet
bash
Copier
Modifier
housing-api/
│
├── app/
│   ├── __init__.py       # Initialisation de l'application
│   ├── main.py           # Point d'entrée de l'API
│   ├── models.py         # Définition des modèles SQLAlchemy
│   ├── schemas.py        # Définition des schémas Pydantic
│   ├── database.py       # Configuration de la base de données
│   ├── crud.py           # Opérations CRUD sur les données
│   └── migrations/       # Fichiers de migration Alembic
│
├── Dockerfile            # Configuration du conteneur pour l'API principale
├── docker-compose.yml    # Orchestration des services Docker
├── pyproject.toml        # Configuration de Poetry
├── README.md             # Documentation du projet
└── .env                  # Variables d'environnement
Services supplémentaires
Analyse des données (analysis.py)
Nettoie les données d'un fichier CSV (data/housing.csv).
Génère une matrice de corrélation et enregistre les données nettoyées dans data/housing_clean.csv.
Modèle d'inférence (train_model.py et predict_api.py)
train_model.py
Entraîne un modèle de régression pour prédire la valeur des maisons.
Sauvegarde le modèle et les colonnes d’entraînement dans le dossier model/.
predict_api.py
Charge le modèle entraîné.
Fournit une route /predict permettant de faire des prédictions via une requête POST.
Contribution
Les contributions sont les bienvenues ! Si vous souhaitez contribuer, suivez ces étapes :

Forkez le projet :

bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/housing-api.git
Créez une branche pour votre fonctionnalité :

bash
Copier
Modifier
git checkout -b nouvelle-fonctionnalite
Faites vos modifications et validez-les :

bash
Copier
Modifier
git commit -m "Ajout d'une nouvelle fonctionnalité"
Poussez votre branche :

bash
Copier
Modifier
git push origin nouvelle-fonctionnalite
Créez une Pull Request sur GitHub.
