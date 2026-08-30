from pathlib import Path
import pandas as pd

data_path = Path("../data2")
country_metadata = pd.read_csv(data_path / "country_metadata.csv")

#General information
print(country_metadata.head())
print("Shape:", country_metadata.shape)
print(country_metadata.describe())
print(country_metadata.info())

#Data quality
print(country_metadata.isnull().sum())
print("Duplicates:", country_metadata.duplicated().sum())
print("ISO3 Duplicates:", country_metadata["iso3"].duplicated().sum())
print("Country Duplicates:", country_metadata["country_name"].duplicated().sum())
print("Country code duplicates:", country_metadata["country_code"].duplicated().sum())
print("Countries without longitude", country_metadata["longitude"].isnull().sum())
print("Countries without latitude", country_metadata["latitude"].isnull().sum())

print(
    country_metadata[
        country_metadata["latitude"].isnull()
    ][["country_name", "region"]]
)
print(
    country_metadata[
    country_metadata["longitude"].isnull()
    ][["country_name", "region"]]
)

#Business metrics
print(
    country_metadata.groupby("region")
    .size()
    .sort_values(ascending=False)
)

print(
    country_metadata.groupby("income_group")
    .size()
    .sort_values(ascending=False)
)

#KPI
print("Total countries:", country_metadata["country_name"].nunique())
print("Total regions:", country_metadata["region"].nunique())
print("Income groups:", country_metadata["income_group"].nunique())
