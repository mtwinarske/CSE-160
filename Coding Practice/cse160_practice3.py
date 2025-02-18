# Name: Miles Winarske
# CSE 160
# Autumn 2024
# Checkin 3


# Problem 1
def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or
    last element in the array. The array will be length 1 or more.

    Arguments:
        nums: a list of integers

    Returns: a boolean representing whether or not 6 is the first or
    last element in a list
    '''
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

# testing my code
print(first_last6([6, 5, 2]))
print(first_last6([3, 5, 5]))


assert first_last6([1, 2, 6]) is True
assert first_last6([6, 1, 2, 3]) is True
assert first_last6([13, 6, 1, 2, 3]) is False
assert first_last6([13, 6, 1, 2, 6]) is True
assert first_last6([3, 2, 1]) is False
assert first_last6([3, 6, 1]) is False
assert first_last6([3, 6]) is True
assert first_last6([6]) is True
assert first_last6([3]) is False


# Problem 2
def get_last_pixel(pixel_grid):
    '''
    Return the value of the pixel (integer) on the last row in the
    last column of the given pixel_grid.
    The pixel_grid will always contain at least one value.

    Arguments:
        pixel_grid: a nested list of lists

    Returns: An integer representing the last int in the pixel_grid
    '''
    return pixel_grid[-1][-1]

# testing my code
print(get_last_pixel([[5, 2, 3], [1, 5, 2]]))


assert get_last_pixel([[5, 2, 3], [1, 5, 4]]) == 4
assert get_last_pixel([[1, 3], [3, 4], [15, 16], [9, 2]]) == 2
assert get_last_pixel([[100, 50]]) == 50
assert get_last_pixel([[35]]) == 35
assert get_last_pixel([[10, 3], [20, 7], [30, 1], [40, -4]]) == -4
assert get_last_pixel([[10], [20], [30], [40]]) == 40
assert get_last_pixel([[1, 2, 3, 4], [8, 8, 6, 9]]) == 9


# Problem 3
def sum_grid(pixel_grid):
    '''
    Return the sum of all the values in the given pixel_grid.
    The pixel_grid will always contain at least one value.

    Arguments:
        pixel_grid: a nested list of lists

    Returns: An integer representing the sum of values in pixel_grid
    '''
    sum = 0
    for row in pixel_grid:
        for col in row:
            sum += col
    return sum

# testing my code
print(sum_grid([[5, 2, 3], [1, 5, 2]]))


assert sum_grid([[5, 2, 3], [1, 5, 4]]) == 20
assert sum_grid([[1, 3], [3, 4], [15, 16], [9, 2]]) == 53
assert sum_grid([[100, 50]]) == 150
assert sum_grid([[35]]) == 35
assert sum_grid([[10, 3], [20, 7], [30, 1], [40, -4]]) == 107
assert sum_grid([[10], [20], [30], [40]]) == 100
assert sum_grid([[1, 2, 3, 4], [8, 8, 6, 9]]) == 41
