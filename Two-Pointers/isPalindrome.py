import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == " ":
            return True
        pattern = r"[^a-zA-Z0-9]"
        s_ = re.sub(pattern, '', s).lower() 

        for i in range(int(len(s_)/2)):
            if s_[i] == s_[-i-1]:
                continue
            return False

        return True
