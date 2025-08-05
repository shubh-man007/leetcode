class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(nums, low, high, target, findFirst):
            if low > high:
                return -1
            mid = int(low + (high - low)/2)
            if nums[mid] == target:
                if findFirst:
                    temp = binSearch(nums, low, mid - 1, target, findFirst)
                    return mid if temp == -1 else temp
                else:
                    temp = binSearch(nums, mid + 1, high, target, findFirst)
                    return mid if temp == -1 else temp
            elif nums[mid] > target:
                return binSearch(nums, low, mid - 1, target, findFirst)
            else:
                return binSearch(nums, mid + 1, high, target, findFirst)

        left = binSearch(nums, 0, len(nums) - 1, target, True)
        right = binSearch(nums, 0, len(nums) - 1, target, False)
        return [left, right]
