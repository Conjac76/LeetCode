class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False

        for i, j in zip(s, t):
            if i != j:
                return False

        return True