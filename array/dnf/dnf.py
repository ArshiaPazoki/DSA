# Dutch National Flag (DNF) by Edsger Dijkstra
# sort an array with 3 distinct values (commonly 0, 1, 2) in linear time
# Dutch National Flag (DNF) Algorithm:
# Use three pointers: low, mid, high to partition array into three sections:
# [0, low) → 0s / [low, mid) → 1s / [mid, high] → unknown / (high, end] → 2s
# Traverse with mid: swap elements to correct zones, shrink unknown region
# O(n) time / O(1) space
# usages:
# - Image processing: Group pixels by color intensity (dark, medium, bright) for fast segmentation
# - Medical data classification: Separate patient results into low/medium/high risk categories in real time
# - E-commerce: In-place reordering of items tagged as "low", "medium", "high" priority for display
# - Embedded systems: Sort sensor data (temperature: cold/warm/hot) on devices with limited memory
# - Database engines: Optimize queries with ternary filters (status: pending / approved / rejected)
# - Networking: Packet classification by priority (0=low, 1=normal, 2=high) in routers with minimal latency
# - Genomics: Partition DNA sequences by mutation severity (none / mild / severe) during analysis
# - Retail inventory: Reorganize stock labels (red/yellow/green) on handheld devices without extra storage

def dnf(arr):
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high - 1
    return arr

