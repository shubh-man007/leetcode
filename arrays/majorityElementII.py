class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1, count2 = 0, 0
        ele1, ele2 = 0, 1 

        for num in nums:
            if num == ele1:
                count1 += 1
            elif num == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = num
                count1 = 1
            elif count2 == 0:
                ele2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(ele1) > len(nums) // 3:
            result.append(ele1)
        if ele2 != ele1 and nums.count(ele2) > len(nums) // 3:
            result.append(ele2)

        return result
