import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = re.sub(r'W\+', '', s)
        alphaNum = alphaNum.lower()
        print(alphaNum)
            
        for i in range(len(alphaNum)):
            if(alphaNum[i] != alphaNum[len(alphaNum)-i]):
                return False 
            else:
                return True

solution = Solution()

print(solution.isPalindrome("racecar"))