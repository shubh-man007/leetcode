class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        idx = -1
        for i in range(len(nums) - 2, -1, -1):  
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:  
            nums.reverse()
            return

        for i in range(len(nums) - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        nums[idx + 1:] = reversed(nums[idx + 1:]) 
