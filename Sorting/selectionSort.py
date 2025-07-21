class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(0, len(nums) - 1):
            min_ = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_]:
                    min_ = j
            nums[i], nums[min_] = nums[min_], nums[i]

        return nums
