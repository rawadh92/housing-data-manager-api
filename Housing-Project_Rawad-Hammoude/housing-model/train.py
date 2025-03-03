import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Charger les données
housing_data = pd.read_csv("housing.csv")

# Préparation des données
features = [
    "longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms",
    "population", "households", "median_income"
]
target = "median_house_value"

X = housing_data[features]
y = housing_data[target]

# Diviser en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Sauvegarde du modèle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modèle entraîné et sauvegardé sous 'model.pkl'")