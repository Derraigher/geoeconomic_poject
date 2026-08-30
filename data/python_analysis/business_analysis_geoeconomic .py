from pathlib import Path
import pandas as pd

data_path = Path("../data2")

country_metadata = pd.read_csv(data_path / "country_metadata.csv")
country_year = pd.read_csv(data_path / "country_year_indicators.csv")
economic_stress = pd.read_csv(data_path / "economic_stress_score.csv")


# Merge economic stress information
merged = country_year.merge(
    economic_stress[
        [
            "country_code",
            "year",
            "final_economic_stress_score",
            "stress_category"
        ]
    ],
    on=["country_code", "year"],
    how="left"
)

# =====================================
# BUSINESS ANALYSIS
# =====================================

# Average Economic Stress by Income Group
print(
    merged.groupby("income_group")["final_economic_stress_score"]
    .mean()
    .sort_values(ascending=False)
)

# Average Inflation by Region
print(
    merged.groupby("region")["inflation"]
    .mean()
    .sort_values(ascending=False)
)

# Top 10 Countries by GDP per Capita
print(
    merged.groupby("country_name")["gdp_per_capita"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Average Economic Stress by Year
print(
    merged.groupby("year")["final_economic_stress_score"]
    .mean()
)

#Average GDP per capita by region
print(
    merged.groupby("region")["gdp_per_capita"]
    .mean()
    .sort_values(ascending=False)
)

#Average GDP Growth by Region
print(
    merged.groupby("region")["gdp_growth"]
    .mean()
    .sort_values(ascending=False)
)


#Average Inflation by Income Group
print(
    merged.groupby("income_group")["inflation"]
    .mean()
    .sort_values(ascending=False)
)

#Average Unemployment by Region
print(
    merged.groupby("region")["unemployment"]
    .mean()
    .sort_values(ascending=False)
)
#Unemployement trend
print(
    merged.groupby("year")["unemployment"]
    .mean()
)

#Average Economic Stress by Region
print(
    merged.groupby("region")["final_economic_stress_score"]
    .mean()
    .sort_values(ascending=False)
)

#Average Economic Stress by Income Group
print(
    merged.groupby("income_group")["final_economic_stress_score"]
    .mean()
    .sort_values(ascending=False)
)

#Top 10 Countries with Highest Economic Stress
print(
    merged.groupby("country_name")["final_economic_stress_score"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

#Economic Stress Trend
print(
    merged.groupby("year")["final_economic_stress_score"]
    .mean()
)

#Average Food Production Index by Region
print(
    merged.groupby("region")["food_production_index"]
    .mean()
    .sort_values(ascending=False)
)

#Average Agricultural Land by Region
print(
merged.groupby("region")["agricultural_land_pct"] \
    .mean() \
    .sort_values(ascending=False)
)

#Average Cereal Yield by Region
print(
merged.groupby("region")["cereal_yield"] \
    .mean() \
    .sort_values(ascending=False)
)

#Average Population by Region
print(
merged.groupby("region")["population"] \
    .mean() \
    .sort_values(ascending=False)
)