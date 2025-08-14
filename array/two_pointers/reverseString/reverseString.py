# LC.344
from typing import List

class Solution:
    def reverseString(self, str: List[str]) -> None:
        left = 0
        right = len(str) - 1
        while left < right:
            if str[left] != str[right]:
                str[left],str[right] = str[right],str[left]
            left += 1
            right -= 1
        

if __name__ == "__main__":
    str = ["h","e","l","l","o"]
    solution = Solution()
    solution.reverseString(str)
    print(str)