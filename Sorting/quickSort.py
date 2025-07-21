class Solution(object):
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def qS(self, arr, low, high):
        if low >= high:
            return
        p = self.partition(arr, low, high)
        self.qS(arr, low, p - 1)
        self.qS(arr, p + 1, high)


    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.qS(nums, 0, len(nums) - 1)
        return nums
