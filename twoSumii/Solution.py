class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            num = numbers[left] + numbers[right]

            if num < target:
                left = left + 1
            
            elif num > target:
                right = right - 1
            elif num == target:
                return left + 1, right + 1

//Awesome!
//