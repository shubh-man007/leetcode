class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binSearch(nums, low, high):
            if len(nums) == 1:
                return 0
            if nums[0] > nums[1]:
                return 0
            if nums[-1] > nums[-2]:
                return len(nums) - 1
            while low <= high :
                mid = (low + high) // 2
                if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] > nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
            
        return binSearch(nums, 1, len(nums) - 2)
