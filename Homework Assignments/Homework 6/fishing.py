# Miles Winarske
# Fall 2024
# CSE 160
# Homework 6

import csv  # noqa: F401
import os  # noqa: F401
import math  # noqa: F401
import matplotlib.pyplot as plt  # noqa: F401
from numpy.polynomial import polynomial as poly  # noqa: F401
from utils import (  # noqa: F401
    min_year, max_year, plot_linear_prediction
)

# -------------- Define your functions here --------------


def parse_data(filename):
    """
    Parses the data from a chosen CSV file
    and returns it as a nested dictionary.
    """
    data = {
        "min_year": None,
        "max_year": None,
        "farmed": {},
        "wild caught": {},
        "consumption": {},
        "population": {}
    }

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data["min_year"] = min_year(reader.fieldnames)
        data["max_year"] = max_year(reader.fieldnames)

        for row in reader:
            country_code = row["country code"]
            measure = row["measure"]

            if measure in data:
                if country_code not in data[measure]:
                    data[measure][country_code] = {}

                for year in range(data["min_year"], data["max_year"] + 1):
                    year_str = str(year)
                    value = row[year_str] if year_str in row else ""

                    if value == "":
                        parsed_value = None
                    elif measure == "population":
                        parsed_value = int(value)
                    else:
                        parsed_value = float(value)

                    data[measure][country_code][year] = parsed_value

    return data


def get_actual_production(data, country_code, year):
    """
    Calculates the actual production for a given country and year,
    and then returns the sum of farmed and wild-caught production.
    Returns None if both of the measures are missing.
    """
    farmed = data["farmed"].get(country_code, {}).get(year, None)
    wild_caught = data["wild caught"].get(country_code, {}).get(year, None)

    if farmed is None and wild_caught is None:
        return None
    elif farmed is None:
        return wild_caught
    elif wild_caught is None:
        return farmed
    else:
        return farmed + wild_caught


def get_production_need(data, country_code, year):
    """
    Calculates the production need for a given country and year.
    Population is multiplied by consumption (in kg per capita per year)
    and converted to metric tonnes by dividing by 1000.
    """
    population = data["population"].get(country_code, {}).get(year, None)
    consumption = data["consumption"].get(country_code, {}).get(year, None)

    if population is None or consumption is None:
        return None

    production_need = (population * consumption) / 1000
    return production_need


def plot_production_vs_consumption(data, country_code):
    """
    Plots actual fishing production versus the
    necessary production for a given country,
    and then saves it as a .png.
    """
    min_year = data["min_year"]
    max_year = data["max_year"]

    years = list(range(min_year, max_year + 1))
    actual_production = []
    production_need = []

    for year in years:
        actual = get_actual_production(data, country_code, year)
        need = get_production_need(data, country_code, year)
        actual_production.append(actual if actual is not None
                                 else float('nan'))
        production_need.append(need if need is not None else float('nan'))

    plt.plot(years, actual_production, label="Actual Production", marker='o')
    plt.plot(years, production_need, label="Production Need", marker='s')

    plt.xlabel("Year")
    plt.ylabel("Metric Tonnes")
    plt.title("Production vs. Need for {country_code}")
    plt.legend()

    plt.savefig("us-prod-vs-need.png")
    plt.show()


def predict_need(data, country_code, predict_years):
    """
    Predicts the future production need for a country using a best-fit line,
    and then returns a dictionary with predicted years and values.
    """
    min_year = data["min_year"]
    max_year = data["max_year"]

    years = []
    values = []

    for year in range(min_year, max_year + 1):
        need = get_production_need(data, country_code, year)
        if need is not None:
            years.append(year)
            values.append(need)

    if not years or not values:
        return {"years": [], "values": []}

    b, m = poly.polyfit(years, values, 1)

    all_years = list(range(min_year, max_year + predict_years + 1))
    all_values = [(m * year + b) for year in all_years]

    return {"years": all_years, "values": all_values}


def total_production_need(data, years_to_predict):
    """
    Calculates the total production need for the world
    based on a given number of years into the future.
    """
    total_need = 0
    for country in data["consumption"]:
        prediction = predict_need(data, country, years_to_predict)
        if prediction["values"]:
            total_need += prediction["values"][-1]

    return total_need


if __name__ == "__main__":
    data = parse_data("large.csv")
    total_need_50_years = total_production_need(data, 50)
    print(
        f"Metric tonnes of seafood needed to be produced in 50 years: "
        f"{total_need_50_years:,.3f}"
    )
    plot_linear_prediction(data, "USA")

# Colaboration: I completed this assignment alone, with
# help by referring to the ED discussion and
# the homework instructions.
