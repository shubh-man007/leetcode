class Solution(object):
    def merge(self, nums, low, mid, high):
        l = low
        r = mid + 1
        arr = []
        
        while l <= mid and r <= high:
            if nums[l] <= nums[r]:
                arr.append(nums[l])
                l += 1
            else:
                arr.append(nums[r])
                r += 1
        while l <=mid:
            arr.append(nums[l])
            l += 1
        while r <= high:
            arr.append(nums[r])
            r += 1
            
        for i in range(low, high + 1):
            nums[i] = arr[i - low]     

    def mS(self, nums, low, high):
        if low == high:
            return
        mid = (low + high) // 2
        self.mS(nums, low, mid)
        self.mS(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mS(nums, 0, len(nums) - 1)
        return nums
