import pytest

from class_exercises.tdd.quadratic import quadratic


def test_quadratic():
    assert 2**0.5 == pytest.approx(1.414213562)
    with pytest.raises(ValueError):
        assert quadratic(2,3)


test_data_lower = [
                (5, 0, 0),
                (1, 6, 8),
                (1, 6, 5),
                (1, 6, 4),
                (1, 6, 3),
                (1, 6, 2),
]

@pytest.mark.parametrize("a, b, c", test_data_lower)
def test_min_boundary(a,b, c):
    assert quadratic(a, b, c) ==