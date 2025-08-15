# LC.42
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3 :
            return 0
        l = 0
        r = n-1
        lmax = rmax = 0
        ans = 0
        while l < r and height[l] <= height[l+1]:
            l += 1
        while l < r and height[r] <= height[r-1]:
            r -= 1
        while l < r:
            if height[l] <= height[r]:
                if height[l] < lmax:
                    ans += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    ans += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return ans


        
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result = solution.trap(height=height)
    print(result)