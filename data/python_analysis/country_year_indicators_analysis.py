from pathlib import Path
import pandas as pd

data_path = Path("../data2")
country_year_indicators = pd.read_csv(data_path / "country_year_indicators.csv")


#General information
print(country_year_indicators.head())
print("Shape:", country_year_indicators.shape)
print(country_year_indicators.describe())
print(country_year_indicators.info())

#Data quality
print(country_year_indicators.isnull().sum())
print("Duplicates:", country_year_indicators.duplicated().sum())
print("Country-Year duplicates:", country_year_indicators[["country_code", "year"]].duplicated().sum())
print("First year:", country_year_indicators["year"].min())
print("Last year:", country_year_indicators["year"].max())
print("Countries:", country_year_indicators["country_code"].nunique())
print(country_year_indicators["country_code"]
      .value_counts()
      .describe()
      )

print(
    country_year_indicators[
        ["gdp_growth",
         "inflation",
         "unemployment",
         "gdp_per_capita",
         "population",
         "economic_stress_score"]
    ].isnull().sum()
)


#Business metrics
print(country_year_indicators["year"].value_counts().sort_index())
print(country_year_indicators["gdp_growth"].describe())
print(country_year_indicators["inflation"].describe())
print(country_year_indicators["unemployment"].describe())
print(country_year_indicators["gdp_per_capita"].describe())
print(country_year_indicators["economic_stress_score"].describe())

print(
    country_year_indicators.groupby("year")["gdp_growth"]
)

print(
    country_year_indicators.groupby("year")["inflation"]

)

#KPI
print(
    "Average GDP Growth:",
    country_year_indicators["gdp_growth"].mean()
)

print(
    "Average Inflation:",
    country_year_indicators["inflation"].mean()
)

print(
    "Average Unemployment:",
    country_year_indicators["unemployment"].mean()
)

print(
    "Average GDP per capital:",
    country_year_indicators["gdp_per_capita"].mean()
)

print(
    "Average Economic Stress Score:",
    country_year_indicators["economic_stress_score"].mean()
)