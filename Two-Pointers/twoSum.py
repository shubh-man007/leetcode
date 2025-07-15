class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = -1

        while True:
            diff = target - numbers[i]
            if diff > numbers[j]:
                i += 1
            if diff < numbers[j]:
                j -= 1
            if diff == numbers[j]:
                return [i + 1, len(numbers) + j + 1]
