from abc import ABCMeta, abstractmethod, abstractproperty
from six import with_metaclass


class Shape(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def get_area(self):
        return 0

    @abstractproperty
    def perimeter(self):
        return 0
