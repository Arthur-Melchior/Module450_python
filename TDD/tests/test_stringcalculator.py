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


@pytest.mark.parametrize("my_param_mult, my_result_mult", [
    ("3;5", 15),  # test case
    ("3;6", 18),  # test case 2
    ("3;7", 21),  # test case 3
    ("3;8", 24),  # test case 4
    ("3;9", 27),  # test case 5
    ("3;10", 30),  # test case 6
])
def test_multiply_multiple_number(my_param_mult, my_result_mult):
    # act
    result = StringCalculator.multiply(my_param_mult)
    # assert
    assert result == my_result_mult


@pytest.mark.parametrize("my_param_divide, my_result_divide", [
    ("15;3", 5),  # test case
    ("18;3", 6),  # test case 2
    ("21;3", 7),  # test case 3
    ("24;3", 8),  # test case 4
    ("27;3", 9),  # test case 5
    ("30;3", 10),  # test case 6
])
def test_divide_multiple_numbers(my_param_divide, my_result_divide):
    # act
    resultat = StringCalculator.divide(my_param_divide)
    # assert
    assert resultat == my_result_divide


@pytest.mark.parametrize("my_param_subtract, my_result_subtract", [
    ("15;5", 10),  # test case
    ("18;5", 13),  # test case 2
    ("21;5", 16),  # test case 3
    ("24;5", 19),  # test case 4
    ("27;5", 22),  # test case 5
    ("30;5", 25),  # test case 6
])
def test_subtract_multiple_numbers(my_param_subtract, my_result_subtract):
    # act
    resultat = StringCalculator.subtract(my_param_subtract)
    # assert
    assert resultat == my_result_subtract


@pytest.mark.parametrize("my_param_subtract2, my_result_subtract2", [
    ("a;5", 10),  # test case
    ("18;bonjour", 13),  # test case 2
])
def test_subtract_a_letter_from_a_number(my_param_subtract2, my_result_subtract2):
    #act
    result = StringCalculator.subtract(my_param_subtract2)
    #assert
    assert result == my_result_subtract2
