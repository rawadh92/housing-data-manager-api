# housing-data-manager-api

## Description

Le projet **Housing-Data-Manager-api** est une API REST construite avec **FastAPI** permettant de gérer des données sur les logements. Il est conçu pour effectuer des opérations de base sur des ensembles de données immobilières, comme l'ajout et la récupération d'informations sur les maisons. Le projet utilise une base de données PostgreSQL avec SQLAlchemy pour gérer les modèles et Alembic pour les migrations.

---

## Installation

### Pré-requis
- Python 3.9 ou supérieur
- PostgreSQL installé et configuré
- Un gestionnaire de dépendances comme **Poetry**

### Étapes

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/housing-api.git
   cd housing-api
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate   # Sous Windows : .\env\Scripts\activate
   ```

3. Installez les dépendances avec Poetry :
   ```bash
   poetry install
   ```

4. Configurez la base de données PostgreSQL :
   - Créez une base de données : `housing`
   - Modifiez la variable `DATABASE_URL` dans le fichier `database.py` ou utilisez une variable d'environnement.

5. Appliquez les migrations :
   ```bash
   alembic upgrade head
   ```

6. Lancez le serveur FastAPI :
   ```bash
   uvicorn app.main:app --reload
   ```

7. Accédez à la documentation interactive de l'API :
   - Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Dockerisation de l'API

Ce projet utilise **Docker** pour conteneuriser l'application et **Docker Compose** pour gérer les services. Voici les étapes pour exécuter l'API avec Docker.

### Étape 1 : Dockerfile
Le fichier `Dockerfile` configure l'environnement pour l'API. Il contient :
- L'image Python 3.9.
- L'installation des dépendances via **Poetry**.
- Une commande pour appliquer les migrations automatiquement avant de démarrer le serveur.

### Étape 2 : docker-compose.yml
Le fichier `docker-compose.yml` configure deux services :
- **`api`** : Le service qui exécute l'API FastAPI.
- **`db`** : Un service PostgreSQL pour la base de données.

### Étape 3 : Lancer les services avec Docker Compose
1. Assurez-vous que Docker et Docker Compose sont installés.
2. Exécutez la commande suivante pour construire les conteneurs et lancer les services :
   ```bash
   docker-compose up --build
   ```
3. Une fois les services lancés :
   - L'API est accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000).
   - Les données PostgreSQL sont stockées de manière persistante dans un volume Docker.

### Points clés
- Les migrations sont appliquées automatiquement lors du démarrage grâce à la commande `alembic upgrade head` dans le `Dockerfile`.
- Les variables d'environnement (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `DATABASE_URL`) sont configurées dans le fichier `docker-compose.yml`.
- Les données de PostgreSQL sont persistantes grâce au volume `db_data`.

---
## Structure du projet

```
housing-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # Point d'entrée de l'API
│   ├── models.py      # Définition des modèles SQLAlchemy
│   ├── schemas.py     # Définition des schémas Pydantic
│   ├── database.py    # Configuration de la base de données
│   ├── crud.py        # Logique CRUD pour interagir avec la base
│   └── migrations/    # Fichiers de migration Alembic
│
├── Dockerfile         # Configuration du conteneur pour l'API
├── docker-compose.yml # Orchestration des services Docker
├── alembic.ini        # Configuration d'Alembic
├── pyproject.toml     # Configuration de Poetry
├── README.md          # Documentation du projet
└── env/               # Environnement virtuel (non inclus dans Git)
```

---

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer :
1. Forkez le projet
2. Créez une branche pour votre fonctionnalité :
   ```bash
   git checkout -b nouvelle-fonctionnalite
   ```
3. Faites vos modifications et validez-les :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. Poussez votre branche :
   ```bash
   git push origin nouvelle-fonctionnalite
   ```
5. Créez une Pull Request sur GitHub
