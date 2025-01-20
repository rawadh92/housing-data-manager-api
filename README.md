# housing-data-manager-api

## Description

Le projet **Housing-Data-Manager-api** est une API REST construite avec **FastAPI** permettant de gérer des données sur les logements. Il est conçu pour effectuer des opérations de base sur des ensembles de données immobilières, comme l'ajout et la récupération d'informations sur les maisons. Le projet utilise une base de données PostgreSQL avec SQLAlchemy pour gérer les modèles et Alembic pour les migrations.

---

## Fonctionnalités

1. **Récupérer toutes les maisons (GET `/houses`)**
   - Permet de récupérer une liste de toutes les maisons disponibles dans la base de données sous forme de JSON.

2. **Ajouter une nouvelle maison (POST `/houses`)**
   - Permet d'ajouter une nouvelle maison à la base de données en envoyant des informations comme les coordonnées géographiques, l'âge médian des logements, le nombre de pièces, la population, etc.

---

## Technologies utilisées

- **FastAPI** : Framework rapide pour la création d'API.
- **PostgreSQL** : Base de données relationnelle robuste et performante.
- **SQLAlchemy** : ORM (Object Relational Mapper) pour gérer les interactions avec la base de données.
- **Alembic** : Outil de gestion des migrations de base de données pour SQLAlchemy.
- **Uvicorn** : Serveur ASGI pour exécuter l'application FastAPI.
- **Pydantic** : Validation et sérialisation des données.

---

## Installation

### Pré-requis
- Python 3.9 ou supérieur
- PostgreSQL installé et configuré
- Un gestionnaire de dépendances comme **Poetry**

### Étapes

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/housing-data-manager-api.git
   cd housing-data-manager-api
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
├── alembic.ini        # Configuration d'Alembic
├── pyproject.toml     # Configuration de Poetry
├── README.md          # Documentation du projet
└── env/               # Environnement virtuel (non inclus dans Git)
```

---

## Fonctionnement du projet

1. **Initialisation** :
   - L'API démarre avec `uvicorn` et est exposée sur le port `8000`.
   - Swagger UI et ReDoc fournissent une documentation interactive pour tester les endpoints.

2. **Modèles et schémas** :
   - Les modèles définis dans `models.py` correspondent aux tables de la base de données.
   - Les schémas dans `schemas.py` valident les données entrantes et structurent les données sortantes.

3. **Logique CRUD** :
   - `crud.py` contient les fonctions pour interagir avec la base de données, comme récupérer toutes les maisons ou en ajouter une nouvelle.

4. **Base de données** :
   - La base est configurée via `database.py`, qui utilise SQLAlchemy pour la connexion.
   - Alembic est utilisé pour gérer les migrations (création/modification des tables).

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

---
