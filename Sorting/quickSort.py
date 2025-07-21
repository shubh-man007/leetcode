class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums)-1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
