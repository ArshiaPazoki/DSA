from dnf import dnf


def test_empty():
    """Empty array should remain empty."""
    arr = []
    dnf(arr)
    assert arr == []


def test_single_element():
    """Single elements should remain unchanged."""
    arr = [0]
    dnf(arr)
    assert arr == [0]

    arr = [1]
    dnf(arr)
    assert arr == [1]

    arr = [2]
    dnf(arr)
    assert arr == [2]


def test_two_distinct_values():
    """Test arrays with only two of the three values."""
    arr = [1, 0]
    dnf(arr)
    assert arr == [0, 1]

    arr = [2, 1]
    dnf(arr)
    assert arr == [1, 2]

    arr = [0, 2]
    dnf(arr)
    assert arr == [0, 2]

    arr = [2, 0, 2, 0]
    dnf(arr)
    assert arr == [0, 0, 2, 2]


def test_all_same_values():
    """Arrays with all identical values should remain sorted."""
    arr = [0, 0, 0]
    dnf(arr)
    assert arr == [0, 0, 0]

    arr = [1, 1, 1]
    dnf(arr)
    assert arr == [1, 1, 1]

    arr = [2, 2, 2]
    dnf(arr)
    assert arr == [2, 2, 2]


def test_mixed_order():
    """Classic mixed input: LeetCode "Sort Colors" test case."""
    arr = [2, 0, 2, 1, 1, 0]
    dnf(arr)
    assert arr == [0, 0, 1, 1, 2, 2]


def test_already_sorted():
    """Already sorted array should remain correct."""
    arr = [0, 1, 2]
    dnf(arr)
    assert arr == [0, 1, 2]


def test_reverse_sorted():
    """Reverse sorted: [2,1,0] → [0,1,2]"""
    arr = [2, 1, 0]
    dnf(arr)
    assert arr == [0, 1, 2]


def test_large_mixed_array():
    """Larger array with unbalanced counts."""
    arr = [1, 2, 0, 2, 0, 1, 0, 2, 1, 0]
    dnf(arr)
    assert arr == [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]


def test_adjacent_swaps():
    """Edge: swapping affects mid pointer correctly."""
    arr = [1, 2, 0]
    dnf(arr)
    assert arr == [0, 1, 2]


def test_no_ones():
    """Array without middle value (1)."""
    arr = [2, 0, 2, 0, 2]
    dnf(arr)
    assert arr == [0, 0, 2, 2, 2]


def test_no_zeros():
    """Array without 0s."""
    arr = [1, 2, 1, 2, 1]
    dnf(arr)
    assert arr == [1, 1, 1, 2, 2]


def test_no_twos():
    """Array without 2s."""
    arr = [1, 0, 1, 0, 1]
    dnf(arr)
    assert arr == [0, 0, 1, 1, 1]