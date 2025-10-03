import pytest
from class_exercises.tdd.grade_boundaries import calc_grade

test_data_lower = [(0,"U"),
             (72,"E"),
             (111,"D"),
             (150, "C"),
             (189, "B"),
             (229, "A"),
             (264, "A*"),
            ]

test_data_upper = [(71,"U"),
             (110,"E"),
             (149,"D"),
             (188, "C"),
             (228, "B"),
             (263, "A"),
             (350, "A*"),
            ]

@pytest.mark.parametrize("grade,expected", test_data_lower)
def test_grade_min_boundary(grade, expected):
    assert calc_grade(grade) == expected


@pytest.mark.parametrize("grade,expected", test_data_upper)
def test_grade_max_boundary(grade, expected):
    assert calc_grade(grade) == expected


def test_calc_grade_normal():
    assert calc_grade(259) == "A"

def test_calc_grade_erroneous():
    with pytest.raises(ValueError):
        calc_grade(351)
    with pytest.raises(ValueError):
        calc_grade(-1)
    with pytest.raises(TypeError):
        calc_grade("B")
