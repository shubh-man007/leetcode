class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums, low, mid, high):
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

        def checkPairs(nums, low, mid, high):
            r = mid + 1
            count = 0
            for i in range(low, mid + 1):
                while r <= high and nums[i] > nums[r] * 2:
                    r += 1
                count = count + (r -mid - 1)
            return count

        def mS(nums, low, high):
            if low == high:
                return 0
            mid = (low + high) // 2
            c = mS(nums, low, mid)
            c += mS(nums, mid + 1, high)
            c += checkPairs(nums, low, mid, high)
            merge(nums, low, mid, high)
            return c
        
        return mS(nums, 0, len(nums) - 1)
