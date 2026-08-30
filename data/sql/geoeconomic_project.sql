-- =====================================
-- CUSTOMER ANALYSIS GEOECONOMIC PROJECT
-- =====================================

USE geoeconomic_project;

-- Average Economic Stress by Income Group
SELECT cy.income_group,
AVG(final_economic_stress_score) AS avg_economic_stress
FROM country_year_indicators cy
JOIN economic_stress_score es
	ON cy.country_code = es.country_code
    AND cy.year = es.year
GROUP BY income_group
ORDER BY avg_economic_stress DESC;

-- Average Inflation by Region
SELECT region,
AVG(inflation) AS avg_inflation
FROM country_year_indicators
GROUP BY region
ORDER BY avg_inflation DESC;

-- Top 10 Countries by GDP per Capita
SELECT country_name,
AVG(gdp_per_capita) AS avg_gdp_per_capita
FROM country_year_indicators
GROUP BY country_name
ORDER BY avg_gdp_per_capita DESC
LIMIT 10;

-- Average Economic Stress by Year
SELECT year,
AVG(final_economic_stress_score) AS avg_stress_score
FROM economic_stress_score
GROUP BY year
ORDER BY year DESC;

-- Average GDP per capita by region
SELECT region,
AVG(gdp_per_capita) AS avg_gdp_per_capita
FROM country_year_indicators
GROUP BY region
ORDER BY avg_gdp_per_capita DESC;

-- Average GDP Growth by Region
SELECT region,
AVG(gdp_growth) AS avg_gdp_growth
FROM country_year_indicators
GROUP BY region
ORDER BY avg_gdp_growth DESC;

-- Average Inflation by Income Group
SELECT income_group,
AVG(inflation) AS avg_inflation
FROM country_year_indicators
GROUP BY income_group
ORDER BY avg_inflation DESC;

-- Average Unemployment by Region
SELECT region,
AVG(unemployment) AS avg_unemployment
FROM country_year_indicators
GROUP BY region
ORDER BY avg_unemployment DESC;

-- Unemployement trend
SELECT year,
AVG(unemployment) AS avg_unemployment
FROM country_year_indicators
GROUP BY year
ORDER BY year DESC;

-- Average Economic Stress by Region
SELECT region,
AVG(economic_stress_score) AS avg_economic_stress_score
FROM country_year_indicators
GROUP BY region
ORDER BY avg_economic_stress_score DESC;

-- Average Economic Stress by Income Group
SELECT income_group,
AVG(economic_stress_score) AS avg_economic_stress
FROM country_year_indicators
GROUP BY income_group
ORDER BY avg_economic_stress DESC;

-- Top 10 Countries with Highest Economic Stress
SELECT country_name,
AVG(economic_stress_score) AS avg_economic_stress
FROM country_year_indicators
GROUP BY country_name
ORDER BY avg_economic_stress DESC
LIMIT 10;

-- Economic Stress Trend
SELECT year,
AVG(economic_stress_score) AS economic_stress
FROM country_year_indicators
GROUP BY year
ORDER BY year;

-- Average Food Production Index by Region
SELECT region,
AVG(food_production_index) AS avg_food_production
FROM country_year_indicators
GROUP BY region
ORDER BY avg_food_production DESC;

-- Average Agricultural Land by Region
SELECT region,
AVG(agricultural_land_pct) AS avg_agricultural_land
FROM country_year_indicators
GROUP BY region
ORDER BY avg_agricultural_land DESC;

-- Average Cereal Yield by Region
SELECT region,
AVG(cereal_yield) AS avg_cereal_yield
FROM country_year_indicators
GROUP BY region
ORDER BY avg_cereal_yield DESC;

-- Average Population by Region
SELECT region,
AVG(population) AS avg_population
FROM country_year_indicators
GROUP BY region
ORDER BY avg_population DESC;