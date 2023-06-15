

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ')':'(', ']':'['}

        for char in s:
            if char in closeToOpen:
                print("if")
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                print("else")
                stack.append(char)
                
        return True if not stack else False



s = Solution()
print(s.isValid("[{}()]"))
                            
                