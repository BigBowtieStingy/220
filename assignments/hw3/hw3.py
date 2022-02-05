"""
Name: Alex James
hw3.py
Problem: Create programs that require the use of "For" loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    grades_to_average = eval(input("How many grades do you want to average?"))
    grade_total = 0
    for i in range(grades_to_average):
        grade_total = eval(input("Enter grade")) + grade_total
    print("The average is", (grade_total/grades_to_average))


def tip_jar():
    donation_total = 0
    for i in range(5):
        donation_total = eval(input("How much would you like to tip?")) + donation_total
    print("Total tips:", donation_total)


def newton():
    num_to_square_root = eval(input("What number do you want to square root?"))
    approximation_times = eval(input("How many times should we improve the approximation?"))
    approximated_num = num_to_square_root
    for i in range(approximation_times):
        approximated_num = ((num_to_square_root / approximated_num) + approximated_num)/2
    print("The square root is approximately", approximated_num)


def sequence():
    sequence_length = eval(input("How many numbers do you want in the sequence?"))
    sequence_number = 1
    sequence_adder = 0
    for i in range(1, (sequence_length + 1)):
        sequence_number = (sequence_adder * 2)
        sequence_adder = int(i / 2)
        print(sequence_number + 1, end=" ")


def pi():
    terms_in_series = eval(input("How many terms in series?"))
    denom = 1
    denom_adder = 0
    numerator = 1
    numer_adder = 0
    product = 1
    for i in range(1, terms_in_series + 1):
        denom = (denom_adder * 2)
        denom_adder = int((i + 1) / 2)
        numerator = (numer_adder * 2)
        numer_adder = int(i / 2)
        product = ((numerator + 2)/(denom + 1)) * product
    print(product * 2)


if __name__ == '__main__':
    pass
