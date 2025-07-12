class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        num_to_index = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in num_to_index:
                return [num_to_index[diff], idx]
            num_to_index[val] = idx


