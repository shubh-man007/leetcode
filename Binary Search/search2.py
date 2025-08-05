class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binSearch(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    return True

                if nums[low] == nums[mid] == nums[high]:
                    low += 1
                    high -= 1
                    continue
                
                if nums[low] <= nums[mid]:
                    if nums[low] <= target < nums[mid]:
                        if nums[mid - 1] == nums[mid]:
                            high = mid - 2
                        else:
                            high = mid - 1
                    else:
                        low = mid + 1
                
                else:
                    if nums[mid] < target <= nums[high]:
                        if nums[mid + 1] == nums[mid]:
                            low = mid + 2
                        else:
                            low = mid + 1
                    else:
                        high = mid - 1
            
            return False

        return binSearch(nums, 0, len(nums)-1, target)
