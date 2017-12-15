import pytest

from shapes import Rectangle


@pytest.fixture(scope='module', params=[(2, 4), (10, 5)])
def rectangle(request):
    width, height = request.param
    return Rectangle(width, height)  # provide the fixture value


def test_rectangle_area(rectangle):
    area = rectangle.get_area()
    rectangle.width += 1
    assert area != rectangle.get_area()


def test_rectangle_perimeter(rectangle):
    perimeter = rectangle.perimeter
    rectangle.height += 1
    assert rectangle.perimeter != perimeter
