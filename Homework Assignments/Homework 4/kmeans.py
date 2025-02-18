"""
* Name: Miles Winarske
* Date: 10/23/2024
* CSE 160, Autumn 2024
* Homework 4
* Description:
'''
This program is a k-means clustering algorithm
that allows you to input datapoints to determine
where data points lie within various centroids.
'''
* Collaboration: I did this assignment on my own, with some help from reading
* the ED discussion boards, and attending office hours.
"""

from utils import (
    converged, plot_2d, plot_centroids, plot_fig, read_data,
    load_centroids, write_centroids_with_key
    )  # noqa: F401
import math  # noqa: F401
import os


def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two data points.

    Arguments:
        point1: a non-empty list of floats representing a data point
        point2: a non-empty list of floats representing a data point

    Returns: the Euclidean distance between two data points

    Example:
        Code:
            point1 = [1.1, 1, 1, 0.5]
            point2 = [4, 3.14, 2, 1]
            print(euclidean_distance(point1, point2))
        Output:
            3.7735394525564456
    """

    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i]) ** 2
        euclidean_distance = math.sqrt(sum)
    return euclidean_distance


def get_closest_centroid(point, centroids_dict):
    """
    Given a data point, finds the closest centroid. You should use
    the euclidean_distance function (that you previously implemented).

    Arguments:
        point: a list of floats representing a data point
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a string as the key name of the closest centroid to the data point

    Example:
        Code:
            point = [0, 0, 0, 0]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                            "centroid2": [2, 2, 2, 2]}
            print(get_closest_centroid(point, centroids_dict))
        Output:
            centroid1
    """

    closest_distance = {
        "centroid": None,
        "distance": float('inf')
    }
    for k, v in centroids_dict.items():
        distance = euclidean_distance(point, v)
        if distance < closest_distance["distance"]:
            closest_distance["centroid"] = k
            closest_distance["distance"] = distance
    return closest_distance["centroid"]


def assign_points_to_centroids(list_of_points, centroids_dict):
    """
    Assign all data points to the closest centroids. You should use
    the get_closest_centroid function (that you previously implemented).

    This function should return a new dictionary, not modify any
    passed in parameters.

    Arguments:
        list_of_points: a list of lists representing all data points
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                            "centroid2": [2, 2, 2, 2]}

            print(assign_points_to_centroids(list_of_points, centroids_dict))
        Output:
            {'centroid1': [[1.1, 1, 1, 0.5], [0, 0, 0, 0]],
             'centroid2': [[4, 3.14, 2, 1]]}
    """

    assign_dict = {}
    for datapoint in list_of_points:
        closest_cent = get_closest_centroid(datapoint, centroids_dict)
        if closest_cent not in assign_dict:
            assign_dict[closest_cent] = []
        assign_dict[closest_cent].append(datapoint)
    return assign_dict


def mean_of_points(list_of_points):
    """
    Calculate the mean of a given group of data points. You should NOT
    hard-code the dimensionality of the data points).

    Arguments:
        list_of_points: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            print(mean_of_points(list_of_points))
        Output:
            [1.7, 1.3800000000000001, 1.0, 0.5]
    """

    mean_data_points = []
    avg = 0
    for data_0 in range(0, len(list_of_points[0])):
        sum = 0
        for data_1 in range(0, len(list_of_points)):
            sum = sum + list_of_points[data_1][data_0]
        avg = sum / len(list_of_points)
        mean_data_points.append(float(avg))
    return mean_data_points


def update_centroids(assignment_dict):
    """
    Update centroid locations as the mean of all data points that belong
    to the cluster. You should use the mean_of_points function (that you
    previously implemented).

    This function should return a new dictionary, not modify any
    passed in parameters.

    Arguments:
        assignment_dict: a dictionary whose keys are the centroids' key
                         names and values are lists of points that belong
                         to the centroid. It is the dictionary
                         returned by assign_points_to_centroids function.

    Returns: A new dictionary representing the updated centroids. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary.

    Example:
        Code:
            assignment_dict = {'centroid1': [[1.1, 1, 1, 0.5], [0, 0, 0, 0]],
                               'centroid2': [[4, 3.14, 2, 1]]}
            print(update_centroids(assignment_dict))
        Output:
          {'centroid1': [0.55, 0.5, 0.5, 0.25],
           'centroid2': [4.0, 3.14, 2.0, 1.0]}
    """

    new_centroids = {}
    for k, v in assignment_dict.items():
        new_centroids[k] = mean_of_points(v)
    return new_centroids


def main(data, init_centroids, dataset):
    #########################################################################
    # You do not need to change anything in this function.
    # However it is HIGHLY RECOMMENDED to read through and understand what it
    # does. Particularly, the first few lines of the `while` loop show the
    # general flow of the k-means algorithm and how the data flows through
    # the functions you will implement for this assignment.
    #########################################################################
    if dataset == "2d":
        plot_steps, plot_init, plot_final = True, False, False
    elif dataset == "mnist":
        plot_steps, plot_init, plot_final = False, True, True

    centroids = init_centroids
    old_centroids = None
    step = 0

    if plot_init:
        # plot initial centroids
        plot_centroids(centroids, "init")

    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = assign_points_to_centroids(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1

        if plot_steps:
            # plot centroid
            fig = plot_2d(assignment_dict, centroids)
            results_dir = os.path.join("results", "2D")
            plot_fig(fig, results_dir, f"step{step}")

    print(f"K-means converged after {step} steps.")

    if plot_final:
        # plot final centroids
        plot_centroids(centroids, "final")

    return centroids


if __name__ == "__main__":
    dataset = "mnist"

    data, label = read_data("data/" + dataset + ".csv")
    init_c = load_centroids("data/" + dataset + "_init_centroids.csv")
    final_c = main(data, init_c, dataset)
    write_centroids_with_key(dataset + "_final_centroids.csv", final_c)
