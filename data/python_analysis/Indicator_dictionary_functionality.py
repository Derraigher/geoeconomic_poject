from pathlib import Path
import pandas as pd

data_path = Path("../data2")
indicator_dictionary = pd.read_csv(data_path / "indicator_dictionary.csv")

#General information
print(indicator_dictionary.head())
print("Shape:", indicator_dictionary.shape)
print(indicator_dictionary.describe())

print(indicator_dictionary.isnull().sum())
print("Duplicates:", indicator_dictionary.duplicated().sum())