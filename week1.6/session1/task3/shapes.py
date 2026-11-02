# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour
# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle (Shape):
    """
    Class representing a circle, inheriting from shape
    """
    def __init__(self, radius, position, colour="red"):
        """
        Creates a circle with the specified radius, position and colour
        """
        self.set_radius(radius)
        self.set_position(position)
        self.set_colour(colour)

    def set_radius(self, radius):
        """
        Sets the circles radius
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Invalid data type, radius must be an integer or a real number")
        if radius <= 0:
            raise ValueError("Invalid value, radius must be greater than 0")
        self.radius = radius
    def area(self):
        """
        Returns the area of the circle, using a value of pi to 10 s.f.
        """
        area = (self.radius * self.radius) * 3.141592654
        return area
    def perimeter(self):
        """
        Returns the perimeter of the circle, using a value of pi to 10 s.f.
        """
        perimeter = (self.radius * 2) * 3.141592654
        return perimeter
    def __str__(self):
        return (self.colour,"circle", "radius", self.radius, "at", self.position)
q = Circle(1.5, Point(1, 2), "green")
q.area()
    






