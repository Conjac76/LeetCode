class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]
        encounters = []
        num = 0

        count = 0
        while num != 1:
            tempNum = 0
            for i in digits:
                tempNum += i * i
            if tempNum in encounters:
                return False
            else:
                encounters.append(tempNum)
            if tempNum == 1:
                return True;
            
            digits = [int(digit) for digit in str(tempNum)]

