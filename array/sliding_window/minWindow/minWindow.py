class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        if len(t) > len(s):
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        missing = len(t)
        l = 0
        min_window = ''
        min_len = float('inf')
        for r,ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1 
            
            while missing == 0:
                window_size = r - l + 1
                if window_size < min_len:
                    min_len = window_size
                    min_window = s[l:r+1]
                
                l_char = s[l]
                if l_char in need:
                    need[l_char] += 1
                    if need[l_char] > 0:
                        missing += 1
                l += 1
        return min_window

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    result = solution.minWindow(s,t)
    print(result)