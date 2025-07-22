class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pos = []
        neg = []
        new_nums = []

        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
                
        for p, n in zip(pos, neg):
            new_nums.append(p)
            new_nums.append(n)

        return new_nums
