# Problem: Maximum / Minimum Sum of K size subarray
# Sliding Window Algorithm:
# Maintain a window of size k, slide one element at a time, update the window sum
# O(n) time / O(1) space
# usages:
# - time-series data smoothing or aggregation
# - traffic/usage analysis over fixed intervals
# - rolling average in signal processing
# - detecting anomalies or spikes in data
# - memory-efficient streaming algorithms

def sliding_window(arr,k):
    if not arr or k <= 0 or k > len(arr):
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    index = 0
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        if window_sum > max_sum:
            max_sum = window_sum
            index = i - k + 1
    return index, index + k - 1, max_sum