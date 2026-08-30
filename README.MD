# GeoEconomic Analysis Project

## Tech Stack

- Python
- Pandas
- MySQL
- Power BI

## Project Overview

This project analyzes a collection of socioeconomic and economic indicators across different countries and years.

The goal of the project is to explore relationships and patterns between economic stress, GDP, inflation, unemployment, income groups, and agricultural indicators.

The project was developed using Python (Pandas), MySQL, and Power BI.

## 1. Data Preparation and Merging

The available datasets were combined to create a dataset suitable for business analysis.

The country-year economic indicators were merged with the economic stress dataset using `country_code` and `year` as the joining keys.

The resulting dataset was then used as the basis for the analysis.

## 2. Business Analysis – Python

Python and Pandas were used to perform an initial business analysis of the merged dataset.

The analysis focused on:

- Average economic stress by income group
- Average economic stress by region
- Economic stress trends over time
- Countries with the highest economic stress
- Average inflation by region and income group
- Average GDP per capita by region
- Top countries by GDP per capita
- Average GDP growth by region
- Average unemployment by region
- Unemployment trends over time
- Agricultural indicators by region
- Average population by region

This analysis was used to identify the main economic patterns and relevant indicators for the following stages of the project.

## 3. SQL Analysis

The business analysis was also performed using MySQL.

SQL queries were used to aggregate and compare economic indicators across countries, regions, income groups, and years.

The analysis mainly used:

- `AVG()`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`
- `JOIN`

The SQL analysis focused on economic stress, GDP, inflation, unemployment, and agricultural indicators.

## 4. Power BI Dashboard

The results of the analysis were visualized in Power BI through four pages:

### Executive Overview

Provides a high-level overview of the main economic indicators, including:

- Average GDP Growth
- Average GDP per Capita
- Average Inflation
- Average Economic Stress

It also includes trend visualizations for the main indicators.

### Regional Analysis

Focuses on comparing economic indicators across different regions, including economic stress, GDP, and other regional characteristics.

### Country Analysis

Provides a country-level comparison of the main economic indicators and highlights differences between countries.

### Agriculture

Focuses on agricultural indicators across regions, including:

- Food Production Index
- Agricultural Land
- Cereal Yield

## Conclusion

This project provided a concise analysis of global economic and socioeconomic indicators, combining Python-based analysis, SQL queries, and Power BI visualizations to identify differences and trends across countries, regions, income groups, and years.