# Name: Miles Winarske
# CSE 160
# Autumn 2024
# Practice 7


# Problem 1
def student_grades(student_gradebook, assignment_num):
    '''
    Given the following code, read the stacktrace and resolve
    the bugs to produce the expected behavior.

    Expected behavior: Given a dictionary where the keys
    are a two-element tuple containing a student's first
    and last name in the format (first_name, last_name) and the
    values are a list with the student's performance on the last
    three assignments in the format (grade1, grade2, grade3),
    return a set containing the first_name last_name tuples of each
    student who scored at least a 50 on the specified assignment.

    Hint: We expect there to be three bugs to fix.

    Arguments:
        student_gradebook: a dictionary where the keys
        are a two-element tuple containing a student's first
        and last name in the format (first_name, last_name) and the
        values are a list with the student's performance on the last
        three assignments in the format (grade1, grade2, grade3).

        assignment_num: an integer representing the assignment number
        to be checked. Will always be a number between 1-3, inclusive.
        For example, if assignment_num = 1, it is referring to the
        first element for each of the student_gradebook values.

    Returns: a set of tuples where each tuples has the format
    (first_name, last_name). If no students have the required grade
    for the assignment, return an empty set.
    '''

    student_names = set()
    for name, grades in student_gradebook.items():
        if grades[assignment_num - 1] >= 50:
            student_names.add(name)
    return student_names


assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                      {("Tweety", "Bird")}
assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 3) == set()
assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 2) == \
                      {("Tweety", "Bird")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 3) == \
                        {("Hector", "Bulldog")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 2) == \
                        {("Tweety", "Bird")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                        {("Tweety", "Bird"), ("Hector", "Bulldog")}
assert student_grades({("Sylvester", "Stallone"): [19, 76, 76],
                       ("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                        {("Tweety", "Bird"), ("Hector", "Bulldog")}
assert student_grades({("Sylvester", "Stallone"): [19, 76, 76],
                       ("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 3) == \
                        {("Sylvester", "Stallone"), ("Hector", "Bulldog")}


# Problem 2
def mutability_exercise(input_set, input_list, input_dict):
    '''
    Given a set, list, and dictionary, do the following operations
    in the given order:

    a) Modify input_set to contain all the original elements plus
    the keys from the dictionary.
    b) Replace all values in input_dict with the integer 160.
    c) Create and return a new list that contains all the original
    elements from input_list, but with all the elements also found in
    input_set removed. You can assume that input_list does not
    contain duplicate elements.

    Note: Because modification of the set occurs before adding new
    elements to the returned list, the returned list will also have
    any values that appear as keys in the dictionary removed.

    Arguments:
        input_set: a set of integers
        input_list: a list of integers
        input_dict: a dictionary where both the key and value are integers

    Returns: A list containing the elements of the input_list with all
    elements of input_set removed. The returned list must preserve the
    order of the original input_list.
    '''

    # your solution code should start here
    input_set.update(input_dict.keys())
    for key in input_dict:
        input_dict[key] = 160

        return_list = []
        for element in input_list:
            if element not in input_set:
                return_list.append(element)
    return return_list


input_set_one = {1, 2, 3, 4, 5}
input_list_one = [1, 6, 0, 15]
input_dict_one = {21: 5, 3: 6, 15: 2}
output_list_one = mutability_exercise(input_set_one, input_list_one,
                                      input_dict_one)

assert input_set_one == {1, 2, 3, 4, 5, 21, 15}
assert input_list_one == [1, 6, 0, 15]
assert input_dict_one == {21: 160, 3: 160, 15: 160}
assert output_list_one == [6, 0]

input_set_two = {2, 4, 8, 16, 4000}
input_list_two = [-2, 4, -8, 3]
input_dict_two = {160: 160, 2: 3, 4000: 120}
output_list_two = mutability_exercise(input_set_two, input_list_two,
                                      input_dict_two)

assert input_set_two == {2, 4, 8, 16, 4000, 160}
assert input_list_two == [-2, 4, -8, 3]
assert input_dict_two == {160: 160, 2: 160, 4000: 160}
assert output_list_two == [-2, -8, 3]
