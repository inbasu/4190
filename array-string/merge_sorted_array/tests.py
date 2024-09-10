from random import randint

from .solution import merge


def test_empty_arrays():
    num1 = []
    num2 = []
    merge(num1, num2)
    assert num1 == []


def test_one_empty_array():
    num1 = []
    num2 = [1, 2, 3]
    merge(num1, num2)
    assert num1 == [1, 2, 3]


def test_same_length():
    num1 = [1, 2, 4]
    num2 = [3, 5, 6]
    merge(num1, num2)
    assert num1 == [1, 2, 3, 4, 5, 6]


def test_equal_arrays():
    num1 = [1, 2, 3]
    num2 = [1, 2, 3]
    merge(num1, num2)
    assert num1 == [1, 1, 2, 2, 3, 3]


def test_not_equal_length():
    num1 = [3, 6, 9]
    num2 = [1, 2, 4, 99]
    merge(num1, num2)
    assert num1 == [1, 2, 3, 4, 6, 9, 99]


def test_random_arrays():
    num1 = sorted([randint(1, 999) for _ in range(randint(1, 999))])
    num2 = sorted([randint(1, 999) for _ in range(randint(1, 999))])
    result = sorted([*num1, *num2])
    merge(num1, num2)
    assert num1 == result
