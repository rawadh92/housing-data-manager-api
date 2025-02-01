import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("data/housing.csv")

    print(df.head())
    print(df.info())
    missing_values = df.isna().sum()
    print("Valeurs manquantes :", missing_values)

    df.dropna(subset=["total_bedrooms"], inplace=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="viridis")
    plt.title("Matrice de corrélation")
    plt.show()

    df.to_csv("data/housing_clean.csv", index=False)
    print("Dataset nettoyé et sauvegardé.")

if __name__ == "__main__":
    main()
