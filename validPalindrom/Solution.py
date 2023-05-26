import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = re.sub(r'\W+', '', s)
        alphaNum = alphaNum.lower()
        print(alphaNum)
        
        if len(alphaNum) == 0:
            return True

        index = int(len(alphaNum) / 2)

        for i in range(len(index)):
            if alphaNum[i] == '_' or alphaNum[len(alphaNum) -1 -i] == '_':
                continue;

            if(alphaNum[i] != alphaNum[len(alphaNum) -1 -i]):
                return False 

        return True

        