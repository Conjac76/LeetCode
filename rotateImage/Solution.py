class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        [0, 0] == 1 -> [0, 2] == 1
        [1, 0] == 4 -> [0, 1] == 4
        [2, 0] == 7 -> [0, 0] == 7


        [0, 1] == 2 -> [1, 2] == 2
        [1, 1] == 5 -> [1, 1] == 5
        [2, 1] == 8 -> [1, 0] == 8


        [0, 2] == 3 -> [2, 2] == 3 
        [1, 2] == 6 -> [2, 1] == 6
        [2, 2] == 9 -> [2, 0] == 9
        '''

        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top = l
                bottom = r

                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft

            r -= 1
            l += 1
    