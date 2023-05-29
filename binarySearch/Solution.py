class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1


solution = Solution()

# Test case 1
nums = [-1, 2, 4, 6, 10]
target = 3
result = solution.search(nums, target)
print(result)