# LC.125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

        
if __name__ == "__main__":
    str = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(str)
    print(result)