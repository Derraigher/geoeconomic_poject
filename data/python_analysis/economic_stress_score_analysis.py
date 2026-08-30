from pathlib import Path
import pandas as pd

data_path = Path("../data2")
economic_stress_score = pd.read_csv(data_path / "economic_stress_score.csv")

#General information
print(economic_stress_score.head())
print("Shape:", economic_stress_score.shape)
print(economic_stress_score.describe())
print(economic_stress_score.info())

#Data quality
print(economic_stress_score.isnull().sum())
print("Duplicates:", economic_stress_score.duplicated().sum())
print("First year:", economic_stress_score.year.min())
print("Last year:", economic_stress_score.year.max())
print(
    "Country-Year duplicates:",
    economic_stress_score[
        ["country_code", "year"]
    ].duplicated().sum()
)
print(
    economic_stress_score[
        economic_stress_score["final_economic_stress_score"].isnull()
    ]["country_name"].unique()
)

#Business metrics
print(
    economic_stress_score["stress_category"]
    .value_counts()
)

print(
    economic_stress_score["final_economic_stress_score"]
    .describe()
)

#KPI
print(
    "Average Stress:",
    economic_stress_score["final_economic_stress_score"].mean()
)

print(
    "Max Stress:",
    economic_stress_score["final_economic_stress_score"].max()
)

print(
    "Min Stress:",
    economic_stress_score["final_economic_stress_score"].min()
)