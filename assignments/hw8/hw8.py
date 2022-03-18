import math
from graphics import Point, GraphWin, Circle, Text

"""
Name: Alex James
hw8.py
Problem: Create programs that use decision structures.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def add_ten(nums):
    index = 0
    for num in nums:
        num += 10
        nums[index] = num
        index += 1


def square_each(nums):
    index = 0
    for num in nums:
        # math.pow returns a float, so it used for floats
        # Lint check told me to use "isinstance()" instead of "type()"
        if isinstance(num, float):
            num = math.pow(num, 2)
        # The ** operator returns an int, so it is used for ints
        else:
            num = num ** 2
        nums[index] = num
        index += 1


def sum_list(nums):
    total_sum = 0
    for num in nums:
        total_sum = num + total_sum
    return total_sum


def to_numbers(nums):
    index = 0
    for num in nums:
        nums[index] = eval(num)
        index += 1


def sum_of_squares(nums):
    # Initialize the final list
    final_list = []
    # Split the nums list into strings of numbers
    for num in nums:
        # Split the num string contents into individual numbers in a list
        split_nums = num.split(",")
        new_list = []
        # Group the split numbers into a new list
        for split_num in split_nums:
            new_list.append(split_num)
        # Run the 3 functions on new_list to convert it to numbers, square each, and them sum them together
        to_numbers(new_list)
        square_each(new_list)
        final_list.append(sum_list(new_list))
    return final_list


def starter(weight, wins):
    if 160 > weight >= 150 and wins >= 5 or (weight > 199 or wins > 20):
        return True
    return False


def leap_year(year):
    # Create 3 booleans describing if the year can be cleanly divided into an integer
    four_year = (year / 4 == float(year // 4))
    hundred_year = (year / 100 == float(year // 100))
    four_hundred_year = (year / 400 == float(year // 400))
    # Check 3 booleans to decide to return false or true
    if four_year:
        if hundred_year:
            if four_hundred_year:
                return True
        else:
            return True
    return False


def circle_overlap():
    # Create window and change boundaries
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    # Create both circles with the user's mouse
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_two = Circle(center, radius)
    circle_two.setFill("green")
    circle_two.draw(win)
    # Check to see if circles overlap, and change message if so
    overlap_message = Text(Point(5, 5), "The circles do not overlap.")
    if did_overlap(circle_one, circle_two):
        overlap_message.setText("The circles overlap.")
    overlap_message.draw(win)
    # Wait for user to close the window
    close_message = Text(Point(5, 2), "Click again to Close.")
    close_message.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    p_1 = circle_one.getCenter()
    p_2 = circle_two.getCenter()
    distance = math.sqrt((p_1.getX() - p_2.getX()) ** 2 + (p_1.getY() - p_2.getY()) ** 2)
    r_1 = circle_one.getRadius()
    r_2 = circle_two.getRadius()
    # If the distance of the centers is smaller/equal than both circles' radi then they must intersect
    intersect = distance <= (r_1 + r_2)
    print(distance, (r_1 + r_2), intersect)
    return intersect


if __name__ == '__main__':
    pass
