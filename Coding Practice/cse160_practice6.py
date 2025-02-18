# Name: Miles Winarske
# CSE 160
# Autumn 2024
# Checkin 6

from operator import itemgetter


# Problem 1
def animal_shelter(animals):
    '''
    Given a list of tuples, where each tuple represents an animal in
    the format (name, age, species), sort the animals by reverse age.
    If there is a tie, sort the animals by name, if two animals have the same
    name and age, sort by species in alphabetical order.

    Arguments:
        animals: a list of tuples, where each tuple represents an animal in
    the format (name, age, species)

    Returns: a list of tuples in sorted order as defined above
    '''
    # your solution code should start here
    animals = sorted(animals, key=itemgetter(2, 0))
    animals = sorted(animals, key=itemgetter(1), reverse=True)
    return animals


assert animal_shelter([("A", 8, "Cat")]) == [("A", 8, "Cat")]
assert animal_shelter([("A", 8, "Cat"), ("B", 9, "Cat")]) == [("B", 9, "Cat"),
                                                              ("A", 8, "Cat")]
assert animal_shelter([("C", 8, "Cat"), ("D", 8, "Cat")]) == [("C", 8, "Cat"),
                                                              ("D", 8, "Cat")]
assert animal_shelter([("C", 8, "Cat"), ("C", 8, "Dog")]) == \
   [("C", 8, "Cat"), ("C", 8, "Dog")]
assert animal_shelter([("A", 8, "Cat"), ("B", 9, "Dog"), ("C", 7, "Rat")]) == \
    [('B', 9, 'Dog'), ('A', 8, 'Cat'), ('C', 7, 'Rat')]
assert animal_shelter([("A", 6, "Cat"), ("B", 9, "Dog"), ("C", 6, "Rat")]) == \
    [('B', 9, 'Dog'), ('A', 6, 'Cat'), ('C', 6, 'Rat')]
assert animal_shelter([("B", 8, "Cat"), ("B", 7, "Dog"), ("C", 8, "Rat")]) == \
   [('B', 8, 'Cat'), ('C', 8, 'Rat'), ('B', 7, 'Dog')]
assert animal_shelter([("C", 3, "Rat"), ("B", 8, "Cat"), ("B", 7, "Dog"),
                       ("C", 8, "Rat"), ("A", 3, "Rat")]) == \
    [('B', 8, 'Cat'), ('C', 8, 'Rat'), ('B', 7, 'Dog'), ('A', 3, 'Rat'),
     ('C', 3, 'Rat')]

print(animal_shelter([("C", 3, "Rat"), ("B", 8, "Cat"), ("B", 7, "Dog"),
                      ("C", 8, "Rat"), ("A", 3, "Rat")]))


# Problem 2
def subset_and_one(subset_one, subset_two):
    '''
    Return true if subset_one contains all elements of subset_two.
    Return false if subset_two contains an extra element besides
    the ones found in subset_one except if the extra element is 1.
    If the only additional element in subset_two is 1, return True.

    Arguments:
        subset_one: a set of integers
        subset_two: a set of integers

    Returns: False if subset_two contains additional elements besides
    the ones found in subset_one except if the extra element is 1
    '''
    # your solution code should start here
    extra_element = subset_two - subset_one
    return extra_element == set() or (len(extra_element)
                                      == 1 and 1 in extra_element)


print(subset_and_one({1}, {1}))


assert subset_and_one({1}, {1}) is True
assert subset_and_one({1}, {1, 2}) is False
assert subset_and_one({2}, {2, 1}) is True
assert subset_and_one({1, 2, 3}, {2, 3, 4}) is False
assert subset_and_one({5, 6, 7}, {6, 7}) is True
assert subset_and_one({100, 200, -5}, {-5}) is True
assert subset_and_one({1000, 3, 60}, {1, 3}) is True
assert subset_and_one({1, 2, 3}, {1, 2, 3, 4}) is False
