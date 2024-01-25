import pytest

from TDD.src.stringcalculator import StringCalculator


def test_add_param_vide_return_zero():
    # arrange
    mon_param = "5"
    mon_resultat = 5

    # act
    somme = StringCalculator.add(mon_param)

    # assert
    assert somme == mon_resultat


@pytest.mark.parametrize("mon_param, mon_resultat", [
    # arrange
    ("7;8", 15),  # test case
    ("1;2;3", 6),  # test case 4
    ("1;2;3;4", 10),  # test case 5
    ("1;2;5", 8),  # test case 6
    ("1;2;0", 3),  # test case 7
    ("1;2;1000", 1003),  # test case 8
    ("1;2;1001", 3),  # test case 9
])
def test_add_plusieurs_nombres(mon_param, mon_resultat):
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat


@pytest.mark.parametrize("mon_param_mult, mon_resultat_mult", [
    ("3;5", 15),
    ("3;6", 18),
    ("3;7", 21),
    ("3;8", 24),
    ("3;9", 27),
    ("3;10", 30),
])
def test_multiplier_plusieurs_nombres(mon_param_mult, mon_resultat_mult):
    # act
    resultat = StringCalculator.multiply(mon_param_mult)
    # assert
    assert resultat == mon_resultat_mult
