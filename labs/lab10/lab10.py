from graphics import Point, Rectangle, Text, GraphWin, color_rgb
from Button import Button
from Door import Door
"""
Alex James
lab10.py
Problem: Create and use a custom door class and button class.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    win = GraphWin("Doors", 250, 250)
    rect = Rectangle(Point(75, 25), Point(175, 50))
    rect2 = Rectangle(Point(75, 75), Point(175, 250))
    button_color = color_rgb(15, 200, 50)
    door_color = color_rgb(215, 20, 20)
    door_color2 = color_rgb(250, 250, 250)
    # Generate starting button & door
    b = Button(rect, "Exit")
    b.color_button(button_color)
    b.draw(win)
    d = Door(rect2, "Closed!")
    d.color_door(door_color)
    d.draw(win)
    door_active = True
    door_open = False
    while door_active:
        p_click = win.getMouse()
        if d.is_clicked(p_click):
            if door_open:
                # Close Door
                d.close(door_color, "Closed!")
                door_open = False
            else:
                # Open Door
                d.open(door_color2, "Open!")
                door_open = True
        elif b.is_clicked(p_click):
            door_active = False
            win.close()