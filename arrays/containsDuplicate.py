class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = dict.fromkeys(nums, 0)
        for i in nums:
            nums_dict[i] += 1

        for val in nums_dict.values():
            if val > 1:
                return True
        
        else:
            return False
