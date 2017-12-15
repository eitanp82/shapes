import pytest

from shapes.square import Square


@pytest.fixture(scope='module')
def square():
    return Square(0)  # provide the fixture value


def test_square_side(square):
    square.side = 10
    assert square.side == 10


def test_square_negative_side(square):
    with pytest.raises(ValueError, message='Expecting ValueError'):
        square.side = -10


@pytest.mark.xfail(raises=TypeError)
def test_square_invalid_side(square):
    square.side = '10'


@pytest.mark.parametrize('side,expected', [(5, 25), (10, 100)])
def test_area(square, side, expected):
    square.side = side
    assert square.get_area() == expected


@pytest.mark.parametrize('side,expected', [(5, 20), (10, 40)])
def test_perimeter(square, side, expected):
    square.side = side
    assert square.perimeter == expected
