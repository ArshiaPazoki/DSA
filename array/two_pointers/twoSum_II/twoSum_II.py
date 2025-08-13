# LC.167

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
    
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    solution = Solution()
    result = solution.twoSum(numbers=numbers, target=target)
    print(result)