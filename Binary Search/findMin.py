import sys
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binSearch(nums, low, high, target):
            while low <= high:
                mid = (high + low) // 2
                if nums[low] <= nums[mid]:
                    target = min(target, nums[low])
                    low = mid + 1
                else:
                    target = min(target, nums[mid])
                    high = mid - 1
            return target

        target = sys.maxint
        return binSearch(nums, 0, len(nums) - 1, target)
