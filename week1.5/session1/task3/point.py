# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Constructor class
        """
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here
    def distance(self):
        """
        Calculates the distance from the given object from the origin
        """
        return math.hypot(self.x, self.y)
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, p, q):
        """
        Calculates the distance from the given object to a set point
        """
        first_point = (self.x, self.y)
        other_point = (p, q)
        self
        return math.dist(first_point, other_point)
# Finally, add code here to demonstrate use of Point
a = float(input("Enter the x coordinate for your point: "))
b = float(input("Now, enter the y coordinate for your point: "))
p1 = Point(a, b)
print("The distance from your point to the origin is", p1.distance())
c = float(input("Enter the x coordinate of your second point: "))
d = float(input("Now, enter the y coordinate of your second point: "))
print(f"The distance from your first point to your second point is {p1.distance_to(c, d):.2f}")
