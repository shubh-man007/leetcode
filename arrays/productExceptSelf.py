class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        op = [1] * len(nums)

        pre = 1
        suff = 1

        for i in range(0, len(nums)):
            op[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            op[i] *= suff
            suff *= nums[i]

        return op        
