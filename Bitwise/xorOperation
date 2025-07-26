class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        nums = [start]
        res = start
        for i in range(1,n):
            nums.append(nums[0] + 2*i)
            res = res ^ nums[i]
        
        return res
