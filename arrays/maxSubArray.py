import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        sum_ = 0
        maxsum = -sys.maxsize - 1

        for i in range(len(nums)):
            sum_ += nums[i]

            if sum_ > maxsum:
                maxsum = sum_

            if sum_ < 0:
                sum_ = 0
        
        return maxsum    
