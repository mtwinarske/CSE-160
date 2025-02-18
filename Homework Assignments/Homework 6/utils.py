import matplotlib.pyplot as plt
import os
import math

from sys import platform
if platform == 'darwin':
    import matplotlib  # noqa: E402
    matplotlib.use("macosx")

###############################################################################
# You do not need to change anything in this file! However,                   #
# `plot_linear_prediction` relies on the functions you will implement in this #
# assignment and will not work until you have implemented them.               #
###############################################################################


def plot_linear_prediction(data, country_code):
    '''
    A function that takes the output of `parse_data("small.csv")` as its first
    parameter and a country code (e.g., "USA") as its second parameter. It
    then calls the `calculate_prediction` function with the production need
    data (from get_production_need) for the given country code, and then
    plots the best-fit line and prediction.

    NOTE: This is a complete function, you do not need to modify it. However,
    it relies on parse_data, get_production_need, and calculate_prediction to
    be implemented according to the assignment spec.

    You will be asked to run this function in Problem 4b.
    '''
    from fishing import get_production_need, predict_need
    real_min_year = data['min_year']
    real_max_year = data['max_year']
    observed_need_years = list(range(real_min_year, real_max_year + 1))
    observed_need_values = [get_production_need(data, country_code, year)
                            for year in observed_need_years]
    plt.plot(observed_need_years, observed_need_values, label='data', linestyle='', marker='s')

    prediction = predict_need(data, country_code, 50)
    plt.plot(prediction['years'], prediction['values'],
             linestyle='--', label='best-fit prediction')

    plt.title('Predicted Production Need For ' + country_code)
    plt.xlabel('Year')
    plt.ylabel('Metric Tonnes')
    plt.legend()
    plt.savefig(os.path.dirname(__file__) + "/" + country_code + "_need_prediction.png")


def min_year(fields):
    '''
    A helper function that, given a list of values, returns
    the minimum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return min([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


def max_year(fields):
    '''
    A helper function that, given a list of values, returns
    the maximum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return max([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the argument is a data structure will do an approximate check
    on all of its contents.

    Arguments:
        expected: the expected value
        received: the received value

    Returns: True if the received match the expected, False otherwise
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    if isinstance(expected, dict):
        return expected.keys() == received.keys() and \
            all(check_approx_equals(expected[k], received[k])
                for k in expected)
    elif isinstance(expected, (list, set)):
        return len(expected) == len(received) and \
            all(check_approx_equals(v1, v2)
                for v1, v2 in zip(expected, received))
    elif isinstance(expected, float):
        return math.isclose(expected, received, abs_tol=0.0001)
    else:
        return expected == received


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the argument is a data structure will do an approximate check
    on all of its contents.

    Arguments:
        expected: the expected value
        received: the received value
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    assert check_approx_equals(expected, received), \
        f'Expected {pformat(expected)},\n\tbut received {pformat(received)}'
