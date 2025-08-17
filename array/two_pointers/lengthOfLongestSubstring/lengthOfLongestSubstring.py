class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxl = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxl = max(maxl, r-l+1)
        return maxl



if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)