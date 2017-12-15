import math
from .shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
