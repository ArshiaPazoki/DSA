class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i,j = len(s)-1,len(t)-1

        def cursor(string, p):
            skip = 0
            while p >= 0:
                if string[p] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return p
                p -= 1
            return -1
        
        while i>=0 or j>=0:
            i = cursor(s,i)
            j = cursor(t,j)

            if i == -1 and j == -1:
                return True
            if i == -1 or j == -1:
                return False
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True

if __name__ == '__main__':
    s = "ab##"
    t = "c#d#"
    solution = Solution()
    result = solution.backspaceCompare(s,t)
    print(result)