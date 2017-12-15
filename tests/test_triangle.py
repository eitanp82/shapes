import pytest

from shapes.triangle import Triangle


@pytest.fixture(scope='module')
def triangle():
    return Triangle(4, 13, 15)  # provide the fixture value


def test_rectangle_area(triangle):
    area = triangle.get_area()
    assert area == 24


def test_rectangle_perimeter(triangle):
    assert triangle.perimeter == 32
