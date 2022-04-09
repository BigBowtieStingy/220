import math
"""
Name: Alex James
sphere.py
Problem: Create a sphere class that can tell its surface area, volume, and radius.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * math.pow(self.radius, 2)

    def volume(self):
        return (4 / 3) * math.pi * math.pow(self.radius, 3)
