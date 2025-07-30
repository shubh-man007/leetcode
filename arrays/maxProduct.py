import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre = 1
        suff = 1
        max_prod = -sys.maxint - 1
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            
            pre *= nums[i]
            suff *= nums[len(nums) - i - 1]
            max_prod = max(max_prod, max(pre, suff))
        
        return max_prod
