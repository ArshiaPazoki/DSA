from max_subarray__kadane import max_subarray

def test_empty_array():
    assert max_subarray([]) is None


def test_single_positive():
    assert max_subarray([5]) == (0, 0, 5)


def test_single_negative():
    assert max_subarray([-3]) == (0, 0, -3)


def test_all_positive():
    s, e, total = max_subarray([1, 2, 3])
    assert (s, e) == (0, 2)
    assert total == 6


def test_all_negative():
    s, e, total = max_subarray([-5, -2, -8, -1])
    assert total == -1
    assert s == e == 3  # index of -1


def test_mixed_classic():
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4] → [4, -1, 2, 1] = 6
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s, e, total = max_subarray(arr)
    assert total == 6
    assert s == 3
    assert e == 6
    assert arr[s:e+1] == [4, -1, 2, 1]


def test_two_elements_positive_first():
    # [2, -1] → best is [2], sum = 2
    assert max_subarray([2, -1]) == (0, 0, 2)


def test_two_elements_negative_first():
    # [-1, 2] → best is [2]
    assert max_subarray([-1, 2]) == (1, 1, 2)


def test_with_zero():
    # [0, -1, 0] → best is 0 (either first or last)
    s, e, total = max_subarray([0, -1, 0])
    assert total == 0


def test_all_zeros():
    s, e, total = max_subarray([0, 0, 0])
    assert total == 0
    assert s == 0
    assert e == 0


def test_alternating():
    s, e, total = max_subarray([1, -1, 1, -1, 1])
    assert total == 1

def test_large_array_performance(benchmark):
    """Test performance on large input (optional: requires pytest-benchmark)."""
    arr = [1, -1] * 5000
    result = benchmark(max_subarray, arr)
    assert result[2] == 1  # sum should be 1