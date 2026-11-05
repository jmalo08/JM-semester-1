# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance((width, height), int):
            raise TypeError ("Must be integer values")
        if width or height <= 0:
            raise ValueError("Either width of height must be greater than 0")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Validates if the rectangle is a square
        """
        if self.width != self.height:
            return False
        else:
            return True
    def area(self):
        """
        Returns area of the rectangle
        """
        area = self.width * self.height
        return area
    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        perimeter = (self.width * 2) + (self.height)
        return perimeter
    
    # (See README.md for details of what they should do)
