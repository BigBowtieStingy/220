"""
Name: Alex James
hw4.py
Problem: Create programs that use the graphics package and accumulator patterns.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create squares")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(0, 0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to create multiple squares
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square
        # move amount is distance from center of square to the
        # point where the user clicked
        new_x = click.getX() - center.getX()
        new_y = click.getY() - center.getY()
        new_shape = shape.clone()
        new_shape.move(new_x, new_y)
        new_shape.draw(win)
    close_text_pt = Point(width / 2, height - 250)
    close_text = Text(close_text_pt, "Click again to close.")
    close_text.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    # Create window
    window_width = 400
    window_height = 400
    win = GraphWin("Rectangle", window_width, window_height)
    # Get points and create shape
    point1 = win.getMouse()
    point2 = win.getMouse()
    shape = Rectangle(point1, point2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    # Get the length and width of the rectangle
    length = abs(point1.getX() - point2.getX())
    width = abs(point1.getY() - point2.getY())
    # Convert area and perimeter to strings to be set as text later
    area = str("The Area is: ") + str(length * width)
    perimeter = str("The Perimeter is: ") + str((length * 2) + (width * 2))
    # Create area and perimeter text at bottom of window
    perimeter_text_pt = Point(window_width / 2, window_height - 35)
    perimeter_display_text = Text(perimeter_text_pt, perimeter)
    perimeter_display_text.draw(win)
    area_text_pt = Point(window_width / 2, window_height - 15)
    area_display_text = Text(area_text_pt, area)
    area_display_text.draw(win)
    # Display message to have user close window by clicking
    close_text_pt = Point(window_width / 2, window_height - 250)
    close_display_text = Text(close_text_pt, "Click again to close.")
    close_display_text.draw(win)
    win.getMouse()
    win.close()


def circle():
    window_width = 400
    window_height = 400
    win = GraphWin("Rectangle", window_width, window_height)
    # Get points
    center = win.getMouse()
    outer = win.getMouse()
    # Get radius and draw circle
    radius = math.sqrt(math.pow(outer.getX() - center.getX(), 2) + math.pow(outer.getY() - center.getY(), 2))
    shape = Circle(center, radius)
    shape.draw(win)
    # Display radius onto window
    radius_text = str("The Radius is: ") + str(radius)
    radius_text_pt = Point(window_width / 2, window_height - 15)
    radius_display_text = Text(radius_text_pt, radius_text)
    radius_display_text.draw(win)
    # Display text that asks the user to close
    close_text_pt = Point(window_width / 2, window_height - 250)
    close_display_text = Text(close_text_pt, "Click again to close.")
    close_display_text.draw(win)
    win.getMouse()
    win.close()


def pi2():
    # Ask for sequence length and set values
    sequence_length = eval(input("How many terms to sum?"))
    sign_constant = 1
    adder_value = 1
    pi_sum = 0
    # Loop for the number of times requested, add sums together each loop
    for i in range(sequence_length):
        pi_sum = ((4 / adder_value) * sign_constant) + pi_sum
        # Change the sign of what's being added every even iteration to simulate the "-" sign
        sign_constant = sign_constant * -1
        # Update denominator value every interation
        adder_value = adder_value + 2
    # Print the approximation and the accuracy
    print("Pi Approximation:", pi_sum)
    print("Accuracy:", abs(math.pi - pi_sum))


if __name__ == '__main__':
    pass
