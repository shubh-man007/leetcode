class Solution(object):
    def get_next_row(self, current_row):
        next_row = []
        current_row.insert(0, 0)
        current_row.append(0)
        for i in range(len(current_row) - 1):
            next_row.append(current_row[i] + current_row[i + 1])
        return next_row

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_list = []

        if numRows == 1:
            return [[1]] 

        pascal_list.append([1])
        current_list = [1]

        for i in range(numRows - 1): 
            next_list = self.get_next_row(current_list[:])  
            pascal_list.append(next_list)
            current_list = next_list

        return pascal_list
