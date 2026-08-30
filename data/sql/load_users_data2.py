from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

data_path = Path("../data2")

engine = create_engine(
    "mysql+pymysql://root:0000@localhost/geoeconomic_project"
)

tables = [
    "country_metadata",
    "country_year_indicators",
    "economic_stress_score",
    "indicator_dictionary"

]

print(tables)


for table in tables:
    df = pd.read_csv(data_path / f"{table}.csv")
    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )
    print(f"{table} loaded")