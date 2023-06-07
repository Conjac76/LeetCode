class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        totalLegnth = width * height
        left = 0
        right = totalLegnth - 1

        while left <= right:
            
            mid = ((left + right)) // 2

            rowMid = mid // width
            colMid = mid % width

            if matrix[rowMid][colMid] > target:
                right -= 1
            elif matrix[rowMid][colMid] < target:
                left += 1
            else:
                return True 

        return False
