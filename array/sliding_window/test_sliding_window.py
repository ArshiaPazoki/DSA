import pytest
from sliding_window import sliding_window

def test_typical_case():
    assert sliding_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == (1, 4, 39)

def test_single_window():
    assert sliding_window([2, 3, 4], 3) == (0, 2, 9)

def test_k_equals_1():
    assert sliding_window([-1, -2, -3], 1) == (0, 0, -1)

def test_invalid_k():
    assert sliding_window([1, 2, 3], 0) is None
    assert sliding_window([1, 2, 3], 4) is None

def test_empty_array():
    assert sliding_window([], 2) is None
