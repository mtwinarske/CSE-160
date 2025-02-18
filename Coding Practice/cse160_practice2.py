# Name: Miles Winarske
# CSE 160
# Autumn 2024
# Practice #2


# Problem 1
'''
Write a function letter_count(str, letter) that returns the number
of times letter appears in str. letter is case-sensitive.
'''


def letter_count(str, letter):
    count = 0
    for char in str:
        if char == letter:
            count += 1
    return count


'''
Arguments:
    str: an String
    letter: a char

Returns: An integer representing the count of letter in str.

Examples:'''
print(letter_count("hi", 'h'))
# returns 1
print(letter_count("festival", 'q'))
# returns 0
print(letter_count("astronomy", 'o'))
# returns 2


# Problem 2
'''
Write a function letter_multiply(num, letter) that returns a String containing
letter num many times. If num is a negative integer, return the String
"invalid value for num"
'''


def letter_multiply(num, letter):
    if num < 0:
        return "invalid value for num"
    else:
        return letter * num


'''
Arguments:
    num: an integer
    letter: a char

Returns: A String made of num many repeats of letter.

Examples:'''
print(letter_multiply(7, 'b'))
# returns "bbbbbbb"
print(letter_multiply(2, '&'))
# returns "&&"
print(letter_multiply(0, 'a'))
# returns ""


# Problem 3
'''
Write a function glitchy_message(msg) that repeats each char in msg the number
of times it appears in msg originally. Make function calls to letter_count
and letter_multiply above instead of coding their funcationality from scratch.
'''


def glitchy_message(msg):
    bad_message = ""
    for char in msg:
        count = letter_count(msg, char)
        bad_message += letter_multiply(count, char)
    return bad_message


'''
Arguments:
    msg: an String

Returns: A String made of each char in msg repeating the number of times it
appears in msg.

Examples:'''
print(glitchy_message("letter"))
# returns "leetttteer"
print(glitchy_message("banana"))
# returns "baaannaaannaaa"
print(glitchy_message("paint"))
# returns "paint"
