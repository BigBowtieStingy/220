"""
Name: Alex James
hw2.py
Problem: This program solves various math problems using for loops and math functions.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    sum_threes = 0
    for i in range(0, upper_bound + 1, 3):
        sum_threes = sum_threes + i
    print("Sum of threes is", sum_threes)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    a_side = eval(input("Enter side length A:"))
    b_side = eval(input("Enter side length B:"))
    c_side = eval(input("Enter side length C:"))
    s_quotient = (a_side + b_side + c_side)/2
    area = math.sqrt(s_quotient * (s_quotient-a_side) * (s_quotient-b_side) * (s_quotient-c_side))
    print("The area of the triangle is", area)


def sum_squares():
    lower_range = eval(input("Enter the lower range:"))
    upper_range = eval(input("Enter the upper range:"))
    sum_square = 0
    for i in range(lower_range, upper_range + 1):
        sum_square = (i * i) + sum_square
    print("The sum of squares is", sum_square)


def power():
    request_number = eval(input("Enter the base number:"))
    requested_expo = eval(input("Enter the exponent:"))
    print(request_number, requested_expo)
    final_product = 1
    for _ in range(1, requested_expo + 1):
        final_product = (request_number * final_product)
        print(final_product)
    print(request_number, "^", requested_expo, "=", final_product)


if __name__ == '__main__':
    pass
