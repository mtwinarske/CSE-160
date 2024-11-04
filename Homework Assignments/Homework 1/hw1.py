"""
* Name: Miles Winarske
* Date: 10/4/24
* CSE 160, Autumn 2024
* Homework 1
* Description: working on simple math problems with loops and the math package
"""

import math

# Problem 1: roots
# Note: Computes and prints both roots in accending order

print("Problem 1 solution follows:")

# setting my coefficients into a variable
a = 3
b = -5.86
c = 2.5408

# finding the discriminant
discriminant = b**2 - 4*a*c

# using math.sqrt and the discriminant to find the roots
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)

# printing solutions for this problem, adding space for formatting
print("Root 1:", root1)
print("Root 2:", root2)
print("")

# Problem 2: Reciprocals
# Note: Uses a for loop to print the decimal representations
# of the given fractions

print("Problem 2 solution follows:")

# making a loop that extends from 2 to 10
for i in range(2, 11):
    # determining the version of a fraction as a decimal number
    decimal_version = 1 / i

    # printing the answer for this problem
    print(f"1/{i}: {decimal_version}")
# formatting for autograder
print("")

# Problem 3: Triangular Numbers
# Note: Uses a for loop to compute the 10th triangular number.
print("Problem 3 solution follows:")

# setting up my variables for the future
n = 10
triangular = 0

# making a for loop to add each number to the triangular variable
for i in range(1, 11):
    triangular += i
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)
print("")

# Problem 4: Factorial
# Note: Uses a for loop to compute 10!, the factorial of 10.

# setting up my variables
n = 10
factorial = 1
# making a for loop to multiply the numbers in the range
for i in range(1, n + 1):
    factorial *= i

# printing the answer to this problem
print("Problem 4 solution follows:")
print(f"{n}!: {factorial}")
print("")

# Problem 5: Multiple Factorials
# Prints the first 10 factorials in descending order.

print("Problem 5 solution follows:")
# setting my variable as 10 because it is standard
num_lines = 10

# creating an outer loop that uses num_lines in the range
for n in range(num_lines, 0, -1):
    factorial = 1

    # inner loop to figure out the factorial of n
    for i in range(1, n + 1):
        factorial *= i

    # printing the answer for this problem
    print(f"{n}!: {factorial}")
print("")

# Problem 6: Sums of the Reciprocals of Factorials
# Uses a for loop to compute the sums of reciprocals of factorials.
print("Problem 6 solution follows:")

# setting up the variables
# sum set to 1 because of the whole number in the problem
n = 10
sum = 1

# outer loop to use n in the range
for num in range(1, n + 1):
    factorial = 1

# inner loop used to figure out the factorial of the variable num
    for i in range(1, num + 1):
        factorial *= i

    # adding the reciprocal of factorial to the sum
    sum += 1 / factorial

# printing the answer to this problem
print("e:", sum)
