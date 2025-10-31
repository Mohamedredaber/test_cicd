# test_calcul.py
from calcul import addition, multiplication

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(0, 5) == 0
