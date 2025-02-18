# Name: Miles Winarske
# CSE 160
# Autumn 2024
# Checkin 5


# Problem 1
def first_name_letter(names):
    '''
    Given a list of student names, create a dictionary where the key
    is the first letter of students' names and the value is a list
    of all students who names start with that letter.
    If no student has a name that starts with a letter, that letter
    should not be a key in the dictionary

    Arguments:
        names: a list of strings containing student names.
        You may assume all names start with a capital letter

    Returns: a dictionary where the key is a single character
    and the value is a list of strings
    '''
    # your solution code should start here
    first_letter_dict = {}
    for name in names:
        first_letter = name[0]
        if first_letter in first_letter_dict:
            first_letter_dict[first_letter].append(name)
        else:
            first_letter_dict[first_letter] = [name]
    return first_letter_dict


print(first_name_letter(["Miles", "Ben", "Alexis"]))

assert first_name_letter(["Jen"]) == {"J": ["Jen"]}
assert first_name_letter(["A"]) == {"A": ["A"]}
assert first_name_letter(["A", "Aa"]) == {"A": ["A", "Aa"]}
assert first_name_letter(["Cse160", "Is", "Awesome"]) == \
    {"C": ["Cse160"], "I": ["Is"], "A": ["Awesome"]}
assert first_name_letter(["Alice", "Bob", "Che"]) == \
    {"A": ["Alice"], "B": ["Bob"], "C": ["Che"]}
assert first_name_letter(["Zack", "Yellen", "Xavier"]) == \
    {"Z": ["Zack"], "Y": ["Yellen"], "X": ["Xavier"]}
assert first_name_letter(["A", "A", "B", "D", "B", "C"]) == \
    {"A": ["A", "A"], "B": ["B", "B"], "D": ["D"], "C": ["C"]}
assert first_name_letter(["Amanda", "Zoe", "Sneh", "Sierrah", "Suhas",
                          "Lucas", "Matt"]) == \
    {"S": ["Sneh", "Sierrah", "Suhas"], "L": ["Lucas"], "Z": ["Zoe"],
     "M": ["Matt"], "A": ["Amanda"]}


# Problem 2
def dog_to_human_age(dog_ages):
    '''
    Given a list of dog ages, return a set containing
    the dogs' ages as a set of human ages.
    To convert a dog's age to human age, multiply it by 7

    Arguments:
        dog_ages: a list of integers greater than or equal to 7

    Returns: A set of integers representing the dog ages as human ages
    '''
    # your solution code should start here
    human_ages = set()
    for age in dog_ages:
        human_ages.add(age * 7)
    return human_ages


print(dog_to_human_age([20]))

assert dog_to_human_age([5]) == {35}
assert dog_to_human_age([7]) == {49}
assert dog_to_human_age([0]) == {0}
assert dog_to_human_age([1, 2, 3]) == {7, 14, 21}
assert dog_to_human_age([3, 4, 1, 6]) == {21, 28, 7, 42}
assert dog_to_human_age([5, 5, 5]) == {35}
assert dog_to_human_age([6, 1, 4, 1, 6]) == {42, 7, 28}
assert dog_to_human_age([80, 100, 2, 2, 2]) == {14, 560, 700}


# Problem 3
def remove_common(set_1, set_2):
    '''
    Return a list containing the elements from set_1
    with elements that are found in both set_1 and set_2 removed

    Arguments:
        set_1: a list of integers
        set_2: a list of integers

    Returns: A set containing elements from set_1 with
    elements found in both set_1 and set_2 removed

    '''
    # your solution code should start here
    return set_1 - set_2


print(remove_common({30}, {31}))

print(remove_common({17}, {17}))

assert remove_common({20}, {21}) == {20}
assert remove_common({1}, {1}) == set()
assert remove_common({1, 3, 4}, {3, 5, 6, 1}) == {4}
assert remove_common({2, 4, 6, 8}, {1, 3, 5, 7}) == {2, 4, 6, 8}
assert remove_common({1, 300, 2, 413}, {413, 300, 2, 1}) == set()
assert remove_common({-5}, {413, 300, 2, 1}) == {-5}
assert remove_common({15, 17, 20, 47, 49}, {5}) == {15, 17, 20, 47, 49}
assert remove_common({1, 2, 3, 4}, {-1, -2, -3, -4}) == {4, 2, 1, 3}
