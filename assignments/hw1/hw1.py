"""
Name: Alex James
hw1.py
Problem: This program solves some conversion, cost calculation, and area/volume problems.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total number of shots: "))
    shots_made = eval(input("Enter the player's number of successful shots: "))
    shots_percent = (shots_made / total_shots) * 100
    print("Shooting Percentage =", shots_percent, "%")


def coffee():
    pounds_requested = eval(input("How many pounds of coffee would you like?"))
    cost = (pounds_requested * 10.50) + (pounds_requested * .86) + 1.50
    print("Your total cost is", cost)


def kilometers_to_miles():
    # 1 mile = 1.61 kilometers.
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
