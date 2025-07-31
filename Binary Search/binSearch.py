class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binSearch(nums, low, high, target):
            if low > high:
                return -1
            
            mid = low + ((high - low) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                return binSearch(nums, low, high, target)
            else:
                low = mid + 1
                return binSearch(nums, low, high, target)
        
        return binSearch(nums, 0, len(nums) - 1, target)
      
