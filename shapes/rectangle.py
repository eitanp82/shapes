from .shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width* self.height

    @property
    def perimeter(self):
        return 2 * (self.width+self.height)
