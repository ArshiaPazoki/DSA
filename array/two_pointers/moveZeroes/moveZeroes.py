# LC.283
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

# Former Solution
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         i = 0
#         j = len(nums) -1
#         while i < j:
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#                 j -= 1
#             else:
#                 i += 1

if __name__ == "__main__":
    nums = [0,0,1]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)