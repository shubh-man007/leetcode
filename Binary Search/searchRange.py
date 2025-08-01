class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find = []
        def binSearch(nums, low, high, target):
            mid = int(low + (high - low)/2)
            if low > high:
                return -1, [-1, -1]
            if nums[mid] == target:
                find.append(mid)
                binSearch(nums, low, mid-1, target)
                binSearch(nums, mid+1, high, target)
                return mid, find
            elif nums[mid] > target:
                high = mid - 1
                return binSearch(nums, low, high, target)
            else:
                low = mid + 1
                return binSearch(nums, low, high, target)
            
        _, res = binSearch(nums, 0, len(nums) - 1, target)
        return [min(res), max(res)]
