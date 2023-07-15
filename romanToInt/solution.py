class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = []
        num = 0
        for i in s:
            res.append(roman[i])
            
        for i in range(len(res) - 1):
            if res[i] < res[i + 1]:
                num -= res[i]
            else:
                num += res[i]
        num += res[-1]
        return num