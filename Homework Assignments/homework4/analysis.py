"""
* Name:
* Date:
* CSE 160, Autumn 2024
* Homework 4
* Description:
* Collaboration:
"""

from utils import load_centroids, read_data
from kmeans import get_closest_centroid  # noqa: F401


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS
def assign_labels(list_of_points, labels, centroids_dict):
    """
    Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of strings representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = ['N', 'M', 'W']
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(assign_labels(list_of_points, labels, centroids_dict))
        Output:
            {'centroid1': ['M', 'N'], 'centroid2': ['W']}
    """

    labels_dictionary = {}
    for i in range(len(list_of_points)):
        point = list_of_points[i]
        label = labels[i]
        closest_cent = get_closest_centroid(point, centroids_dict)
        if closest_cent not in labels_dictionary:
            labels_dictionary[closest_cent] = []
        labels_dictionary[closest_cent].append(label)
    return labels_dictionary


def majority_count(labels):
    """
    Return the count of the majority label in the label list.

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list

    Example:
        Given labels = ['M', 'M', 'N']
        majority_count(labels) returns 2
    """

    d = {}
    for i in labels:
        if i not in d:
            d[i] = 0
        d[i] += 1
    max_label_occurence = 0
    for k, v in d.items():
        if v > max_label_occurence:
            max_label_occurence = v
    return max_label_occurence


def accuracy(list_of_points, labels, centroids_dict):
    """
    Calculate the accuracy of the algorithm. You should use assign_labels and
    majority_count (that you previously implemented)

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a float representing the accuracy of the algorithm
    """

    sum_count_majority_labels = 0
    data = assign_labels(list_of_points, labels, centroids_dict)
    for k, v in data.items():
        sum_count_majority_labels += majority_count(v)
    return sum_count_majority_labels / len(labels)


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv", with_key=True)
    # Consider exploring the centroids data here

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))
