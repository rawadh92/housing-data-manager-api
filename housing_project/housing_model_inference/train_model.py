import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def main():
    df = pd.read_csv("data/housing_clean.csv")
    X = pd.get_dummies(df.drop("median_house_value", axis=1), columns=["ocean_proximity"], drop_first=True)
    y = df["median_house_value"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"MAE = {mean_absolute_error(y_test, y_pred)}")
    print(f"R^2 = {r2_score(y_test, y_pred)}")

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.joblib")
    joblib.dump(X_train.columns.tolist(), "model/trained_columns.joblib")

if __name__ == "__main__":
    main()
