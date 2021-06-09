-- Covid Data Exploration

-- Check Data

SELECT location, date, total_cases, new_cases, total_deaths, population
FROM CovidDeaths
ORDER BY 1,2

-- Looking at Total Cases vs Total Deaths
-- Shows the chance of dying if covid is contracted

SELECT location, date, total_cases, total_deaths, (total_deaths / total_cases) * 100 AS DeathPercentage
FROM CovidDeaths
WHERE location like 'Canada'
ORDER BY 1,2


-- Looking at Total Cases vs Population
-- Shows what percentage of the population has contracted covid

SELECT location, date, population, total_cases, (total_cases / population) * 100 AS ContractedPercentage
FROM CovidDeaths
WHERE location like 'Canada'
ORDER BY 1,2


-- Looking at Countries with Highest infection rate compared to Population

SELECT location, population, MAX(total_cases) AS HighestInfectionCount, MAX((total_cases / population)) * 100 AS ContractedPercentage
FROM CovidDeaths
GROUP BY location, population
ORDER BY ContractedPercentage DESC

-- Showing Location with Highest Death Count per Population

SELECT location, MAX(CAST(total_deaths as int)) AS TotalDeathCount
FROM CovidDeaths
WHERE continent IS NULL
GROUP BY location
ORDER BY TotalDeathCount DESC

-- Showing continents with the highest death count per population

SELECT continent, MAX(CAST(total_deaths as int)) AS TotalDeathCount
FROM CovidDeaths
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY TotalDeathCount DESC


-- Showing Countries with Highest Death Count per Population

SELECT location, population, MAX(CAST(total_deaths as int)) AS TotalDeathCount
FROM CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY TotalDeathCount DESC


-- Global Numbers

SELECT SUM(new_cases) AS total_cases, SUM(CAST(new_deaths as int)) as total_deaths, 
		SUM(CAST(new_deaths as int)) / SUM(new_cases) * 100 AS DeathPercentage
FROM CovidDeaths
WHERE continent IS NOT NULL
ORDER BY 1,2


SELECT date, SUM(new_cases) AS total_cases, SUM(CAST(new_deaths as int)) as total_deaths, 
		SUM(CAST(new_deaths as int)) / SUM(new_cases) * 100 AS DeathPercentage
FROM CovidDeaths
WHERE continent IS NOT NULL
GROUP BY date
ORDER BY 1,2


-- Join with vaccinations, use window function to see running sum of people vaccinated by country

SELECT deaths.continent, deaths.location, deaths.date, deaths.population, vacc.new_vaccinations,
SUM(CONVERT(int,vacc.new_vaccinations)) OVER (PARTITION BY deaths.location ORDER BY deaths.location, deaths.date) AS RollingPeopleVaccinated
FROM CovidDeaths as deaths
JOIN CovidVaccines as vacc
ON deaths.location = vacc.location AND deaths.date = vacc.date
WHERE deaths.continent IS NOT NULL
ORDER by 2,3


-- USE CTE to find rulling vaccination percentage

WITH PopvsVac (continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
AS
(
SELECT deaths.continent, deaths.location, deaths.date, deaths.population, vacc.new_vaccinations,
SUM(CONVERT(int,vacc.new_vaccinations)) OVER (PARTITION BY deaths.location ORDER BY deaths.location, deaths.date) AS RollingPeopleVaccinated
FROM CovidDeaths as deaths
JOIN CovidVaccines as vacc
ON deaths.location = vacc.location AND deaths.date = vacc.date
WHERE deaths.continent IS NOT NULL
)

SELECT *, (RollingPeopleVaccinated / population) * 100
FROM PopvsVac


-- USE Temp Table to find rulling vaccination percentage

-- DROP TABLE IF EXISTS #PercentPopulationVaccinated
SELECT deaths.continent, deaths.location, deaths.date, deaths.population, vacc.new_vaccinations,
SUM(CONVERT(int,vacc.new_vaccinations)) OVER (PARTITION BY deaths.location ORDER BY deaths.location, deaths.date) AS RollingPeopleVaccinated
INTO #PercentPopulationVaccinated
FROM CovidDeaths as deaths
JOIN CovidVaccines as vacc
ON deaths.location = vacc.location AND deaths.date = vacc.date
WHERE deaths.continent IS NOT NULL

SELECT * FROM #PercentPopulationVaccinated


-- Create View to store data for later visualization
CREATE VIEW PercentPopulationVaccinated AS
SELECT deaths.continent, deaths.location, deaths.date, deaths.population, vacc.new_vaccinations,
SUM(CONVERT(int,vacc.new_vaccinations)) OVER (PARTITION BY deaths.location ORDER BY deaths.location, deaths.date) AS RollingPeopleVaccinated
FROM CovidDeaths as deaths
JOIN CovidVaccines as vacc
ON deaths.location = vacc.location AND deaths.date = vacc.date
WHERE deaths.continent IS NOT NULL

SELECT * FROM PercentPopulationVaccinated