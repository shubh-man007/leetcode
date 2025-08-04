class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        
        def binSearch(low, high):
            if low > high:
                return False

            mid = (low + high) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return binSearch(low, mid - 1)
            else:
                return binSearch(mid + 1, high)

        return binSearch(0, m * n - 1)
