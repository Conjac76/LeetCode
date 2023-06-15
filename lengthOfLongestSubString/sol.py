class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        count = 0
        start = 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                count = max(count, i - start + 1)
            map[s[i]] = i

        return count
