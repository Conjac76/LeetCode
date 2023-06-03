class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myMap = {}

        for i in s:
            myMap[i] = myMap.get(i, 0) + 1

        for j in t:
            if j not in myMap or myMap[j] == 0:
                return False
            else:
                myMap[j] -= 1
        return True

      