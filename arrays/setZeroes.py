class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_idx = []
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    zero_idx.append((i, j))

        for i, j in zero_idx:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
            for row in range(len(matrix)):
                matrix[row][j] = 0
