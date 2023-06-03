class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i, n in enumerate(nums):
            if n not in map:
                map.update({n : i})

            elif n in map:
                return True
        return False