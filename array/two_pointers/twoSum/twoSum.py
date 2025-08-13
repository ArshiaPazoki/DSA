# Two Pointers Technique / Algorithm
# This strategy involves the use of two pointers/indices/references,
# that traverse a data structure, such as an array, list, or string, simultaneously.
# By manipulating the positions of these two pointers ,
# the technique aims to efficiently address a wide range of problems,
# making it a valuable tool in a programmer’s toolkit.

# LC.1
# O(n log n), O(n) space


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        
        indexed_numbers = [(numbers[i], i) for i in range(len(numbers))]
        indexed_numbers.sort()

        left = 0
        right = len(indexed_numbers) - 1

        while left < right:
            left_value, left_index = indexed_numbers[left]
            right_value, right_index = indexed_numbers[right]
            current_sum = left_value + right_value

            if current_sum == target:
                return sorted([left_index,right_index])
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
        


