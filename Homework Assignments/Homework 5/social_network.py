# Name: Miles Winarske
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """

    practice_graph = nx.Graph()
    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    practice_graph.add_edge("C", "D")
    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("F", "C")
    practice_graph.add_edge("F", "D")
    practice_graph.add_edge("E", "D")

    assert len(practice_graph.nodes()) == 6
    assert len(practice_graph.edges()) == 8

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    rj.add_edge("Nurse", "Juliet")
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edge("Juliet", "Capulet")
    rj.add_edge("Capulet", "Tybalt")
    rj.add_edge("Capulet", "Escalus")
    rj.add_edge("Capulet", "Paris")
    rj.add_edge("Paris", "Escalus")
    rj.add_edge("Friar Laurence", "Romeo")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Montague")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Benvolio", "Montague")
    rj.add_edge("Montague", "Escalus")
    rj.add_edge("Escalus", "Paris")
    rj.add_edge("Mercutio", "Escalus")
    rj.add_edge("Paris", "Mercutio")
    rj.add_edge("Juliet", "Romeo")
    rj.add_edge("Juliet", "Friar Laurence")

    assert len(rj.nodes()) == 11
    assert len(rj.edges()) == 17

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    user_and_friends = friends(graph, user)
    user_and_friends.add(user)
    friends_of_friends = set()
    for i in user_and_friends:
        friends_of_friends |= friends(graph, i)
    friends_of_friends_set = friends_of_friends - user_and_friends
    return friends_of_friends_set


def common_friends(graph, user1, user2):
    """
    Finds and returns the set of friends that user1
    and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a unique identifier representing one user
        user2: a unique identifier representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    user1_friends = friends(graph, user1)
    user2_friends = friends(graph, user2)
    common_friends_set = user1_friends & user2_friends
    return common_friends_set


def num_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      num_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    common_friends_map = {}
    friends_of_friends_set = friends_of_friends(graph, user)
    for i in friends_of_friends_set:
        common_friends_map[i] = len(common_friends(graph, user, i))
    return common_friends_map


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    sorted_keys_list = []
    dict_map = map_with_number_vals.items()
    map_sort_by_key = sorted(dict_map)
    map_sort_by_value = sorted(map_sort_by_key,
                               key=itemgetter(1),
                               reverse=True)
    for i in map_sort_by_value:
        sorted_keys_list.append(i[0])
    return sorted_keys_list


def recs_by_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a unique identifier

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    return num_map_to_sorted_list(
        num_common_friends_map(graph, user))


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    influence_map = {}
    u_not_user_or_friends = friends_of_friends(graph, user)
    for i in u_not_user_or_friends:
        cfs_u = common_friends(graph, i, user)
        for j in cfs_u:
            if i not in influence_map:
                influence_map[i] = 0.0
            influence_map[i] += 1/len(friends(graph, j))
    return influence_map


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    rec_list = influence_map(graph, user)
    sorted_recs = num_map_to_sorted_list(rec_list)
    return sorted_recs


###
#  Problem 5
###

def get_facebook_graph(filename):
    """Builds and returns the facebook graph
    Arguments:
        filename: the name of the datafile
    """
    facebook = nx.Graph()
    with open(filename, 'r') as fb_filename:
        for i in fb_filename:
            list = i.split('\t')
            facebook.add_edge(int(list[0].strip()), int(list[1].strip()))
    fb_filename.close()
    return facebook


def test_get_facebook_graph(facebook, filename):
    if (filename == "facebook-links-small.txt"):
        pass
    else:
        assert len(facebook.nodes()) == 63731
        assert len(facebook.edges()) == 817090
        print("Facebook test passed")


def main():
    # practice_graph = get_practice_graph()
    # Make sure to comment out this line after you have visually verified
    # your practice graph. Otherwise, the picture will pop up every time
    # that you run your program.
    # draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Make sure to comment out this line after you have visually verified
    # your rj graph and created your PDF file. Otherwise, the picture will
    # pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()
    names = list(rj.nodes)
    not_equal = []
    equal = []
    for i in names:
        rec_common_friends = recs_by_common_friends(rj, i)
        rec_influence = recommend_by_influence(rj, i)
        if rec_common_friends != rec_influence:
            not_equal.append(i)
        else:
            equal.append(i)
    sorted_not_equal = sorted(not_equal)
    sorted_equal = sorted(equal)
    print("Unchanged Recommendations: " + str(sorted_equal))
    print("Changed Recommendations: " + str(sorted_not_equal))

    ###
    #  Problem 5
    ###
    # (replace this filename with "facebook-links-small.txt" for testing)
    fb_filename = "facebook-links-small.txt"

    # (Make sure to call get_facebook_graph)
    facebook = get_facebook_graph(fb_filename)

    test_get_facebook_graph(facebook, fb_filename)

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    for user in sorted(facebook.nodes):
        if user % 1000 == 0:
            common_friends = recs_by_common_friends(facebook, user)
            if len(common_friends) < 10:
                common_friends_to_show = (common_friends)
            else:
                common_friends_to_show = (common_friends)[0:10]
            print(user, "(by num_common_friends):", common_friends_to_show)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    for user in sorted(list(facebook.nodes)):
        if user % 1000 == 0:
            common_friends = recommend_by_influence(facebook, user)
            common_friends_to_show = (common_friends)[0:10]
            print(user, "(by influence):", common_friends_to_show)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    same = 0
    different = 0
    for user_id in list(facebook.nodes()):
        if user_id % 1000 == 0:
            common_friends_by_number_of_common_friends = \
                recs_by_common_friends(facebook, user_id)
            common_friends_by_influence = \
                recommend_by_influence(facebook, user_id)
            if len(common_friends_by_number_of_common_friends) < 10 or \
                    len(common_friends_by_influence) < 10:
                pass
            else:
                same_count = 0
                for i in range(0, 10):
                    if common_friends_by_number_of_common_friends[i] == \
                            common_friends_by_influence[i]:
                        same_count += 1
                if same_count == 10:
                    same += 1
                else:
                    different += 1

    print("Same: " + str(same))
    print("Different: " + str(different))


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# I completed this assignment alone
