# LC.16
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[0:3])
        n = len(nums)
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            min_sum = nums[i] + nums[left] + nums[left + 1]
            if min_sum > target:
                if abs(min_sum - target) < abs(result - target):
                    result = min_sum
                break

            max_sum = nums[i] + nums[right - 1] + nums[right]
            if max_sum < target:
                if abs(max_sum - target) < abs(result - target):
                    result = max_sum
                continue

            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(target - current) <= abs(target - result):
                    result = current
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current

        return result

if __name__ == "__main__":
    numbers = [-1,2,1,-4]
    target = 1
    solution = Solution()
    result = solution.threeSumClosest(nums=numbers, target=target)
    print(result)