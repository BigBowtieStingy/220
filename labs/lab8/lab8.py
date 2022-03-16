from graphics import Point, GraphWin, Circle, Text, Polygon, Entry, color_rgb
from random import randint
import time

"""
Alex James
lab8.py
Problem: Create a bumper car simulation using functions and booleans.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def get_random_color():
    # Generate 3 random numbers 0-255
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball1, ball2):
    # Get the points of both balls (the corners)
    ball1_p1 = ball1.getP1()
    ball1_p2 = ball1.getP2()
    ball2_p1 = ball2.getP1()
    ball2_p2 = ball2.getP2()
    # Check if ball2's points fall in ball 1's x range at either point
    point1_xrange = ball1_p2.getX() >= ball2_p1.getX() >= ball1_p1.getX()
    point2_xrange = ball1_p2.getX() >= ball2_p2.getX() >= ball1_p1.getX()
    if point1_xrange or point2_xrange:
        # Check if ball2's points fall in ball 1's y range at either point
        point1_yrange = ball1_p2.getY() >= ball2_p1.getY() >= ball1_p1.getY()
        point2_yrange = ball1_p2.getY() >= ball2_p2.getY() >= ball1_p1.getY()
        if point1_yrange or point2_yrange:
            return True
    return False


def hit_vertical(ball, win):
    position1 = ball.getP1()
    position2 = ball.getP2()
    y_ceiling = win.winfo_height()
    y_floor = 0
    if position1.getY() >= y_ceiling or position2.getY() >= y_ceiling:
        return True
    elif position1.getY() <= y_floor or position2.getY() <= y_floor:
        return True
    return False


def hit_horizontal(ball, win):
    position1 = ball.getP1()
    position2 = ball.getP2()
    x_right = win.winfo_height()
    x_left = 0
    if position1.getX() >= x_right or position2.getX() >= x_right:
        return True
    elif position1.getX() <= x_left or position2.getX() <= x_left:
        return True
    return False


def bumper():
    window_size = 300
    window = GraphWin("Bumper Window", window_size, window_size)
    ball1 = Circle(Point(75, 75), 15)
    ball1.setFill(get_random_color())
    ball1.draw(window)
    ball2 = Circle(Point(225, 225), 15)
    ball2.setFill(get_random_color())
    ball2.draw(window)
    base_move_amount = 250
    ball1_move_amount_x = get_random(base_move_amount)
    ball2_move_amount_x = get_random(base_move_amount)
    ball1_move_amount_y = get_random(base_move_amount)
    ball2_move_amount_y = get_random(base_move_amount)
    begin_message = Text(Point(150, 150), "Click to Begin")
    begin_message.draw(window)
    window.getMouse()
    begin_message.undraw()
    for i in range(0, base_move_amount, 1):
        ball1.move(.05 * ball1_move_amount_x, .05 * ball1_move_amount_y)
        ball2.move(.05 * ball2_move_amount_x, .05 * ball2_move_amount_y)
        time.sleep(.05)
        # Change direction upon impact with a wall, horizontal changes x direction, vertical changes y direction
        if hit_horizontal(ball1, window):
            ball1_move_amount_x *= -1
        if hit_horizontal(ball2, window):
            ball2_move_amount_x *= -1
        if hit_vertical(ball1, window):
            ball1_move_amount_y *= -1
        if hit_vertical(ball2, window):
            ball2_move_amount_y *= -1
        # In the event both balls collide, change both x and y directions for both balls
        if did_collide(ball1, ball2):
            ball1_move_amount_x *= -1
            ball1_move_amount_y *= -1
            ball2_move_amount_x *= -1
            ball2_move_amount_y *= -1
    close_message = Text(Point(150, 150), "Click to Close")
    close_message.draw(window)
    window.getMouse()
    window.close()
