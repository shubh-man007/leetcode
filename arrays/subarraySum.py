from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        prefix_sum = 0
        count = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1  

        for num in nums:
            prefix_sum += num
            count += sum_map.get(prefix_sum - k, 0)
            sum_map[prefix_sum] += 1
        
        return count
