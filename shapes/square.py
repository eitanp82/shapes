import math
import numbers

from .shape import Shape


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return math.pow(self.side, 2)

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        if not isinstance(side, numbers.Real):
            raise TypeError('side argument must be a number, not '
                            '{type}'.format(type=type(side).__name__))
        elif side < 0:
            raise ValueError('negative side is not legal for squares, '
                             '{value} given'.format( value=side))
        self._side = side
