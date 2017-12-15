import math

from .shape import Shape


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
