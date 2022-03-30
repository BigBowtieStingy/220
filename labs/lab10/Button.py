from graphics import Point, Rectangle, Text, GraphWin
"""
Alex James
Button.py
Problem: For lab 10, create a button class with set instance variables and methods.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class Button:
    # Button is a rectangle shape, label is a string.
    def __init__(self, shape, label):
        self.shape = shape
        center_point = self.shape.getCenter()
        self.text = Text(center_point, "default")
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def color_button(self, color):
        self.shape.setFill(color)

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        # Check if X of point falls in shape:
        if p2.getX() >= point.getX() >= p1.getX():
            # Check if Y of point falls in shape:
            if p2.getY() >= point.getY() >= p1.getY():
                return True
        return False
