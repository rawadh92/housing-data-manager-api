import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("model/model.joblib")
trained_columns = joblib.load("model/trained_columns.joblib")

@app.post("/predict")
def predict(data: dict):
    X_input = pd.DataFrame([data]).reindex(columns=trained_columns, fill_value=0)
    prediction = model.predict(X_input)[0]
    return {"prediction": float(prediction)}
