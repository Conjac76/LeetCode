class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = [0] * len(nums)

        for i in nums:
            count[i] += 1

        for i in range(len(count)):
            if count[i] > 1:
                return i

    