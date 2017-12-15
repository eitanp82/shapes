import math

from shapes import Circle


class TestCircle(object):
    radius = 10
    circle = Circle(radius)

    def test_area(self):
        expected = math.pi * self.__class__.radius ** 2
        assert self.circle.get_area() == expected

    def test_perimeter(self):
        expected = 2 * math.pi * self.__class__.radius
        assert self.circle.perimeter == expected


class TestUnitCircle(TestCircle):
    circle = Circle(1)

    def test_area(self):
        assert self.circle.get_area() == math.pi

    def test_perimeter(self):
        assert self.circle.perimeter == 2 * math.pi
