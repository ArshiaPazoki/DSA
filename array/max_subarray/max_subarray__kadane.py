# maximum sum subarray / maximum segment sum problem:
# find the contiguous subarray with the largest sum
# Kadane's Algorithm: 
# Traverse array, maintaining current sum (reset if negative) & updating max sum seen so far.
# O(n) time / O(1) space
# usages:
# - financial analysis (best stock trading period)
# - signal processing (finding peak activity intervals)
# - computational biology (identifying significant gene sequences)
# - image processing (segment detection)
# - algorithmic competitions and dynamic programming foundations
# - data analytics (identifying periods of peak performance)
# max_subarray.py

def max_subarray(a):
    if not a:
        return None
    best = current = a[0]
    start = end = here = 0

    for i in range(1, len(a)):
        x = a[i]
        if current < 0:
            current = x
            here = i
        else:
            current += x
        if current > best:
            best = current
            start = here
            end = i

    return start, end, best