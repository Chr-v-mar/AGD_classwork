import pytest
from class_exercises.tdd.cipherceaser import cipher




test_data_lower = [
                ("a", 1,"b"),
                ("a", 2, "c"),
                ("a", 3, "d"),
                ("a", 4, "e"),
                ("a", 5, "f"),
                ("a", 6, "g"),


]

test_data_upper = [
                ("z", 1, "a"),
                ("z", 2, "b"),
                ("z", 3, "c"),
                ("z", 4, "d"),
                ("z", 5, "e"),
                ("z", 6, "f"),
]



@pytest.mark.parametrize("message, shift, expected", test_data_lower)
def test_min_boundary(message,shift, expected):
    assert cipher(message, shift) == expected

@pytest.mark.parametrize("message, shift, expected", test_data_upper)
def test_max_boundary(message,shift, expected):
    assert cipher(message, shift) == expected

def test_erroneous():
    with pytest.raises(TypeError):
        cipher("hello","dfsg")
    with pytest.raises(ValueError):
        cipher("a",5000)