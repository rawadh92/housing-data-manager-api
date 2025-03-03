from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle entraîné
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array([
        data["longitude"], data["latitude"], data["housing_median_age"],
        data["total_rooms"], data["total_bedrooms"], data["population"],
        data["households"], data["median_income"]
    ]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"predicted_median_house_value": prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)