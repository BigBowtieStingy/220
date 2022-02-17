from graphics import Point, GraphWin, Circle, Text, Polygon, Entry, color_rgb
import math

"""
Alex James
lab5.py
Problem: Solve problems using graphics, strings, and lists.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def triangle():
    win = GraphWin("Triangle", 500, 500)
    information_message = Text(Point(250, 450), "Click 3 times to create a triangle:")
    information_message.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    user_triangle = Polygon(point1, point2, point3)
    user_triangle.draw(win)
    side_length1 = math.sqrt(((point2.getX() - point1.getX()) ** 2) + ((point2.getY() - point1.getY()) ** 2))
    side_length2 = math.sqrt(((point3.getX() - point2.getX()) ** 2) + ((point3.getY() - point2.getY()) ** 2))
    side_length3 = math.sqrt(((point1.getX() - point3.getX()) ** 2) + ((point1.getY() - point3.getY()) ** 2))
    perimeter = round(side_length1 + side_length2 + side_length3, 2)
    s = perimeter / 2
    area = round(math.sqrt(s * (s - side_length1) * (s - side_length2) * (s - side_length3)), 2)
    message_text = ("The perimeter is " + str(perimeter) + ". The area is " + str(area))
    information_message.setText(message_text)
    win.getMouse()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry_point = red_text_pt.clone()
    red_entry_point.move(120, 0)
    green_entry_point = green_text_pt.clone()
    green_entry_point.move(120, 0)
    blue_entry_point = blue_text_pt.clone()
    blue_entry_point.move(120, 0)

    red_amount = Entry(red_entry_point, 20)
    green_amount = Entry(green_entry_point, 20)
    blue_amount = Entry(blue_entry_point, 20)

    red_amount.draw(win)
    green_amount.draw(win)
    blue_amount.draw(win)

    for i in range(5):
        win.getMouse()
        shape.setFill(color_rgb(eval(red_amount.getText()), eval(green_amount.getText()), eval(blue_amount.getText())))
        shape.undraw()
        shape.draw(win)

    # Wait for another click to exit
    inst.setText("Click again to close.")
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Enter a string:")
    print(user_string[0])
    print(user_string[-1])
    for i in range(1, 5):
        print(user_string[i])
    print(user_string[0] + user_string[-1])
    for i in range(10):
        for j in range(0, 3):
            print(user_string[j], end="")
    print("")
    for character in user_string:
        print(character)
    print(len(user_string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num_of_terms = eval(input("How many terms in the sequence?"))
    start_value = 0
    sum_value = 0
    for i in range(num_of_terms):
        start_value = start_value + 2
        print(start_value, end=" ")
        sum_value = start_value + sum_value
        start_value = start_value % 6
    print("The sum is:", sum_value)


def target():
    radius = 500
    target_window = GraphWin("Target", radius, radius)
    colors = ["white", "black", "blue", "red", "yellow"]
    radius = radius / 2
    for i in range(5):
        targetcircle = Circle(Point(250, 250), radius)
        targetcircle.setFill(colors[i])
        targetcircle.draw(target_window)
        radius = radius - 50
    exit_message = Text(Point(250, 250), "Click to Close")
    exit_message.draw(target_window)
    target_window.getMouse()
    target_window.close()

