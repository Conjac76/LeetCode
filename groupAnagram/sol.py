class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            s = tuple(sorted(i))
            if s in map:
                map[s].append(i)
            else: 
                map[s] = [i]

        return list(map.values())