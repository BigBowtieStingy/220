from graphics import Circle, Line, Polygon
"""
Name: Alex James
face.py
Problem: Create a Face class that can smile, be shocked, and wink.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        point_1 = self.mouth.getP1()
        point_2 = self.mouth.getP2()
        point_3 = self.mouth.getCenter()
        point_3.move(0, self.left_eye.getRadius() * 2)
        self.mouth.undraw()
        self.mouth = Polygon(point_1, point_2, point_3)
        self.mouth.draw(self.window)

    def shock(self):
        center_point = self.mouth.getCenter()
        self.mouth.undraw()
        radius = self.left_eye.getRadius()
        self.mouth = Circle(center_point, radius)
        self.mouth.draw(self.window)

    def wink(self):
        self.smile()
        self.left_eye.undraw()