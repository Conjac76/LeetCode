class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = []
        s = " "
        for i in digits:
            s += str(i)
            
        
        num = int(s)
        num += 1
        s = str(num)
        for i in s:
            nums.append(int(i))

        return nums
