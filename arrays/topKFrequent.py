class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_hash = dict.fromkeys(set(nums), 0)
        for num in nums:
            nums_hash[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in nums_hash.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
