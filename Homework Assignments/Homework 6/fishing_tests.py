# Miles Winarske
# Fall 2024
# CSE 160
# Homework 6
# Fishing.py function tests


import math  # noqa: F401
import os  # noqa: F401
import matplotlib.pyplot as plt  # noqa: F401
from numpy.polynomial import polynomial as poly  # noqa: F401
from fishing import parse_data, get_actual_production, get_production_need
from fishing import predict_need, total_production_need
from fishing import plot_production_vs_consumption


def test_parse_data():
    """
    Tests the parse_data function on
    the small.csv file
    """
    data = parse_data("small.csv")
    assert data["min_year"] == 1995
    assert data["max_year"] == 2000
    assert data["farmed"]["CAN"][1995] == 65207.0
    assert data["wild caught"]["CAN"][1995] == 948410.0
    assert data["consumption"]["CAN"][1995] == 22.62
    assert data["population"]["CAN"][1995] == 29137000
    print("All parse_data tests passed!")


def test_get_actual_production():
    """
    Tests the get_actual_production function
    """
    data = parse_data("small.csv")
    assert math.isclose(get_actual_production(data, "CAN", 1995),
                        1013617.0)
    print("All get_actual_production tests passed!")


def test_get_production_need():
    """
    Tests the get_production_need function by multiplying the
    population and consumption, and then
    converting the result to metric tonnes
    """
    data = parse_data("small.csv")
    assert math.isclose(get_production_need(data, "CAN", 1995),
                        659078.94,
                        rel_tol=1e-5)
    assert math.isclose(get_production_need(data, "MEX", 1998),
                        867407.71,
                        rel_tol=1e-5)
    print("All get_production_need tests passed!")


def test_plot_production_vs_consumption():
    """
    Tests the plot_production_vs_consumption function to make
    sure it creates a plot showing the actual production,
    and production need over time for a given country.
    The plot is saved as a PNG file.
    """
    data = parse_data("small.csv")
    plot_production_vs_consumption(data, "USA")
    print("Plot production vs. consumption test passed!")


def test_predict_need():
    """
    Tests the predict_need function in an effort to
     check if it creates a best-fit line, based on
    production need over time, and also predicts the values for
    the future years. The function's return includes years and corresponding
    predicted values.
    """
    data = parse_data("small.csv")
    predictions = predict_need(data, "USA", 5)
    assert "years" in predictions
    assert "values" in predictions
    expected_years = (data["max_year"] - data["min_year"] + 1) + 5
    assert len(predictions["years"]) == expected_years
    assert len(predictions["values"]) == expected_years
    print("predict_need tests passed")


def test_total_production_need():
    """
    Tests the total_production_need function to make sure it correctly
    calculates the total global production needed for a specified number
    of years into the future by summing the predicted
    production needs for all of the countries.
    """
    data = parse_data("small.csv")
    total_need = total_production_need(data, 50)
    expected_total_need = 13243690.762868665
    assert math.isclose(total_need, expected_total_need, rel_tol=1e-5)
    print("total_production_need tests passed")


if __name__ == "__main__":
    """
    Runs all of the tests at once.
    """
    test_parse_data()
    test_get_actual_production()
    test_get_production_need()
    test_plot_production_vs_consumption()
    test_predict_need()
    test_total_production_need()
