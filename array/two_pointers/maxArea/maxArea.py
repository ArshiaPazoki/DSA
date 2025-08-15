# LC.11
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        
        while l < r:
            left_height = height[l]
            right_height = height[r]
            area = min(left_height, right_height) * (r - l)
            if area > ans:
                ans = area
            
            if left_height < right_height:
                while l < r and height[l] <= left_height:
                    l += 1
            else:
                while l < r and height[r] <= right_height:
                    r -= 1
        
        return ans


        
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    result = solution.maxArea(height=height)
    print(result)