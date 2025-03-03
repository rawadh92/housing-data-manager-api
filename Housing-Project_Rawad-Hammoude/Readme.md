# Housing Project

Ce projet implémente une API Flask connectée à PostgreSQL pour stocker des informations sur les logements, un modèle de machine learning pour prédire la valeur médiane d’un logement, et un système de messaging basé sur Kafka permettant de traiter des données en temps réel.

---

## Prérequis

Avant de démarrer, assurez-vous d’avoir installé :

- Docker et Docker Compose
- Python 3.12 (si vous voulez exécuter certains scripts manuellement)
- Un compte Kaggle (si vous souhaitez télécharger les données du modèle)

---

## Démarrage rapide

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/housing-projet.git
   cd housing-projet
   ```

2. Lancez les services avec Docker Compose :

   ```bash
   docker-compose up --build
   ```

   Cela démarre :

   - PostgreSQL (db)
   - L’API Flask (api)
   - Le modèle ML de prédiction (model)
   - Le broker Kafka (broker)
   - Le consumer Kafka (consumer)

---

## Vérifier le bon fonctionnement

### Tester l'API principale

#### Vérifier que l'API est accessible :

```bash
curl http://localhost:8000/houses
```

Si aucun logement n’a encore été ajouté, la réponse sera `[]`.

#### Ajouter une maison (POST /houses)

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}' http://localhost:8000/houses
```

#### Vérifier que la maison a été bien ajoutée :

```bash
curl http://localhost:8000/houses
```

---
