# LC.345
class Solution:
    def reverseVowels(self, s: str) -> str:
        str = list(s)
        vowels = set('aeiouAEIOU')
        i = 0
        j = len(str) - 1
        while i < j:
            if str[i] not in vowels:
                i += 1
                continue
            elif str[j] not in vowels:
                j -= 1
                continue
            else:
                str[i],str[j] = str[j],str[i]
                i += 1
                j -= 1
        return "".join(str)
                
        

if __name__ == "__main__":
    str = "IceCreAm"
    solution = Solution()
    result = solution.reverseVowels(str)
    print(result)