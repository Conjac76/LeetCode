class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final = len(nums)*[1]
        prefix = len(nums)*[1]
        suffix = len(nums)*[1]
        pref, post = 1, 1

        for i in range(len(nums)):
            prefix[i] = pref;
            pref *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = post
            post *= nums[i]

        final[0] = suffix[0]
        final[len(nums)-1] = prefix[len(nums)-1]

        for i in range(1, len(nums)-1):
            final[i] = prefix[i] * suffix[i]

        return final
            
            