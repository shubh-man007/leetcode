class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if temp < 0:
            return False

        rev = 0
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        
        if rev == x:
            return True
        return False
