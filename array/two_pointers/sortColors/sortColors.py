# LC.75
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for i in range(n):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        for i in range(left, n):
            if nums[i] == 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1